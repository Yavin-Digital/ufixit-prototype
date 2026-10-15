import json,os,subprocess,concurrent.futures as cf,hashlib
from PIL import Image
ps=json.load(open('products.json'))
jobs=[]
for p in ps:
    for n,i in enumerate(p['images'][:4]):
        jobs.append((p['id'],n,i['src']))
out={}
def run(j):
    pid,n,src=j
    dst=f"/workspace/ufixit-ecom/site/img/p/{pid}-{n}.webp"
    if os.path.exists(dst):
        im=Image.open(dst); return j,im.size
    tmp=f"/tmp/ufraw/{pid}-{n}"
    r=subprocess.run(['curl','-s','-f','-A','Mozilla/5.0 (Macintosh)','-o',tmp,src])
    if r.returncode: return j,None
    try:
        im=Image.open(tmp); im.load()
        if im.mode not in ('RGB','RGBA'): im=im.convert('RGBA')
        if max(im.size)>900: im.thumbnail((900,900))
        im.save(dst,'WEBP',quality=80,method=5)
        os.remove(tmp); return j,im.size
    except Exception as e:
        return j,None
with cf.ThreadPoolExecutor(8) as ex:
    for j,s in ex.map(run,jobs):
        out[f"{j[0]}-{j[1]}"]=s
json.dump(out,open('imgsizes.json','w'))
print(len(out),sum(1 for v in out.values() if v))
