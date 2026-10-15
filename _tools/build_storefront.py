import json,re,html,os,glob
from PIL import Image
S='/workspace/ufixit-ecom/site'; D='/workspace/ufixit-ecom/data'
E=html.escape
import shutil
shutil.copy('/workspace/ufixit-ecom/src/store.css',S+'/css/store.css'); shutil.copy('/workspace/ufixit-ecom/src/store.js',S+'/js/store.js')
ps=json.load(open(D+'/products.json')); cats=json.load(open(D+'/cats.json'))
pop=[2607,3143,3199,3141,2577,2535,2844,2562,3152,3123,2838,3195]
CM={c['id']:c for c in cats}
def un(s): return html.unescape(s)
TOP={'refrigerator-parts':('Refrigerator Parts','cat-refrigerator'),'washer-parts':('Washer Parts','cat-washer'),'dryer-parts':('Dryer Parts','cat-dryer'),'range-oven-parts':('Range & Oven Parts','cat-range'),'dishwasher-parts':('Dishwasher Parts','cat-dishwasher'),'air-conditioner-parts':('Air Conditioner Parts','cat-ac'),'furnace-parts':('Furnace Parts','cat-furnace'),'accessories':('Accessories','cat-accessories'),'microwave-parts':('Microwave Parts','cat-accessories'),'dishwasher-accessories':('Dishwasher Accessories','cat-dishwasher')}
def brand_of(name):
    b=re.sub(r'\s*(range\s*&\s*oven|refrigerator|washer|dryer|dishwasher)?\s*parts$','',un(name),flags=re.I).strip()
    b={'General Electric (GE)':'GE','General Electric':'GE','Maytag':'Maytag'}.get(b,b)
    return b
rank={pid:i for i,pid in enumerate(pop)}
P=[]
for idx,p in enumerate(ps):
    tops=[c['slug'] for c in p['categories'] if CM.get(c['id'],{}).get('parent')==0]
    subs=[c for c in p['categories'] if CM.get(c['id'],{}).get('parent',0)!=0]
    top=tops[0] if tops else (CM[subs[0]['id']] and [k for k in CM if False] or 'accessories')
    if not tops and subs: top=CM[CM[subs[0]['id']]['parent']]['slug']
    brands=sorted({brand_of(c['name']) for c in subs if CM[c['id']]['parent'] in [CM2['id'] for CM2 in cats if CM2['parent']==0 and CM2['slug']!='accessories']})
    if not brands:
        m=re.search(r'\bfor (?:the )?([A-Z][A-Za-z&]+)',un(p['name'])); brands=[m.group(1)] if m and m.group(1) not in ('Dryer','Washer','Refrigerator','Dishwasher','Range') else []
    imgs=[]
    for n in range(min(4,len(p['images']))):
        f=f"img/p/{p['id']}-{n}.webp"
        if os.path.exists(S+'/'+f): imgs.append((f,Image.open(S+'/'+f).size))
    st=p.get('stock_availability') or {}
    m=re.match(r'(\d+) in stock',st.get('text',''))
    P.append(dict(id=p['id'],n=un(p['name']),slug=p['slug'],sku=p['sku'],c=int(p['prices']['price']),top=top,subtops=[c['slug'] for c in subs],brand=next((b for b in brands if b.lower() in un(p['name']).lower()),brands[0] if brands else 'Other'),imgs=imgs,
      stock=p['is_in_stock'],qty=int(m.group(1)) if m else None,stxt=st.get('text',''),desc=p['description'],r=rank.get(p['id'],1000+idx),url=f"product-{p['slug']}.html"))
import hashlib
SN=['Arlington','East Dallas','South Dallas','Tyler']
for p in P:
    p['stores']=[s for s in SN if p['stock'] and int(hashlib.md5(f"{p['id']}{s}".encode()).hexdigest(),16)%10<7]
BYID={p['id']:p for p in P}
def money(c): return f"${c/100:,.2f}"
STORES=[('Arlington','817.472.7740','8174727740','4621 S Cooper St Suite 127, Arlington, TX 76017','9am–6pm Mon–Fri','contact-us-arlington-appliance-parts-store.html'),
('East Dallas','214.321.7054','2143217054','9919 Garland Rd, Dallas, TX 75218 <span class="ph">street # to confirm (9919 vs 9917)</span>','9am–6pm Mon–Fri','contact-us-east-dallas.html'),
('South Dallas','972.780.9096','9727809096','442 East Wheatland Rd, Duncanville, TX <span class="ph">ZIP to confirm</span>','9am–6pm Mon–Fri · 9am–4pm Sat','contact-us-south-dallas.html'),
('Tyler','903.592.5836','9035925836','2606 E 5th St, Tyler, TX 75701','9am–6pm Mon–Fri · 9am–4pm Sat','contact-us-tyler-tx.html')]
idx=open('/workspace/ufixit-ecom/site.orig/index.html').read()
BANNER=idx[idx.index('<!--\n  ╔'):idx.index('<header class="site-header">')].replace('only here to show what is possible.','only here to show what is possible. Checkout is a mock: payment provider, tax and shipping rates are TBD.').replace('font-size: .78rem; line-height: 1.4;','font-size: .9rem; line-height: 1.4;').replace('font-size: .78rem; font-weight: 800;','font-size: .9rem; font-weight: 800; min-height:48px; display:inline-flex; align-items:center;').replace('font-size:.72rem;','font-size:.875rem;')
FONTS='<link rel="preconnect" href="https://fonts.googleapis.com" /><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin /><link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Oswald:wght@400;500;600;700&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&display=swap" onload="this.onload=null;this.rel=\'stylesheet\'" /><noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Oswald:wght@400;500;600;700&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&display=swap" /></noscript>'
NAVTOPS=['refrigerator-parts','washer-parts','dryer-parts','range-oven-parts','dishwasher-parts','air-conditioner-parts','furnace-parts']
HEADER='''<header class="sh">
<div class="sh__top">Same-day shipping on in-stock parts ordered by 3 pm CST Mon–Fri · Free diagnosis help: <a href="tel:8174727740">817.472.7740</a></div>
<div class="sh__in">
<a class="sh__logo" href="index.html" aria-label="U-FIX-IT Appliance Parts home"><img src="img/logo.png" alt="U-FIX-IT Appliance Parts" width="112" height="56" /></a>
<form class="sh__search" action="shop.html" role="search"><label class="skip" for="hq">Search parts</label><input id="hq" name="q" type="search" placeholder="Search by part number, model or part name" autocomplete="off" /><button>Search</button></form>
<div class="sh__icons"><button type="button" class="search-btn" aria-label="Search" aria-expanded="false"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-4-4"/></svg></button><a href="order-lookup.html"><span class="lbl">Track order</span></a><a href="account.html"><span class="lbl">Account</span></a><a class="cartlink" href="cart.html">Cart <span class="cartcount">0</span></a></div>
</div>
<nav class="sh__nav" aria-label="Shop"><div class="in"><button type="button" class="mystore" data-pick-store><span class="lbl-my">My store: </span><strong data-mystore>Pick a store</strong> <u>(change)</u></button><a class="hot" href="shop.html">Shop all parts</a>'''+''.join(f'<a href="product-category-{t}.html">{E(TOP[t][0].replace(" Parts",""))}</a>' for t in NAVTOPS)+'''<a href="find-your-brand.html">Brands</a><a href="how-to-choose.html">How to choose</a><a href="appliance-repair-tips.html">DIY tips</a><a href="contact-us.html">Stores</a></div></nav>
</header>'''
FOOTER='''<section class="capture"><div class="w in"><div><p class="eyebrow" style="color:#FAB143">DIY repair tips by email</p><h2>Fix it yourself, with the right part the first time</h2><p style="margin:0;font:1rem/1.5 system-ui;opacity:.9">Get U-FIX-IT repair tips and new-part alerts. <span class="ph">Signup offer: placeholder, U-FIX-IT to confirm (none on live site)</span></p></div>
<form class="js-capture"><label class="skip" for="em">Email</label><input id="em" type="email" required placeholder="Your email address" /><button class="btn-buy" style="padding:15px 22px">Sign up</button></form></div></section>
<footer class="sf"><div class="w"><div class="cols">
<div><img src="img/logo.png" alt="U-FIX-IT Appliance Parts" width="112" height="56" style="background:#fff;padding:6px;margin-bottom:12px;width:124px;height:auto;box-sizing:border-box" /><p>We have it, or we’ll get it! Free diagnosis assistance and tech tips in person or over the phone.</p></div>
<div><h2 class="fh">Shop</h2>'''+''.join(f'<a href="product-category-{t}.html">{E(TOP[t][0])}</a><br />' for t in NAVTOPS[:6])+'''</div>
<div><h2 class="fh">Help</h2><a href="how-to-choose.html">How to choose a part</a><br /><a href="order-lookup.html">Track an order</a><br /><a href="shipping-appliance-parts.html">Shipping</a><br /><a href="about-us-warranty-returns.html">Warranty &amp; returns</a><br /><a href="account.html">My account</a></div>
<div><h2 class="fh">Stores</h2>'''+''.join(f'{s[0]} <a href="tel:{s[2]}">{s[1]}</a><br />' for s in STORES)+'''</div>
<div><h2 class="fh">Company</h2><a href="about-us.html">About</a><br /><a href="appliance-repair-tips.html">DIY tips</a><br /><a href="share-feedback.html">Feedback</a><br /><a href="privacy-policy.html">Privacy</a><br /><a href="brand.html">Brand guide</a><br /><a href="sitemap.html">Sitemap</a></div>
</div><div class="legal">© U-FIX-IT Appliance Parts · Texas · HTML prototype by The Tribe Maker / Yavin Digital · Mock checkout: no real payments are taken.</div></div></footer>'''
def page(fn,title,desc,body,extra_head='',bodycls=''):
    out=f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
<title>{E(title)}</title><meta name="description" content="{E(desc)}" /><meta property="og:title" content="{E(title)}" /><meta property="og:description" content="{E(desc)}" /><meta property="og:image" content="img/photo/hero-parts.webp" />
<link rel="icon" href="img/favicon-192.png" sizes="192x192" />{FONTS}<link rel="stylesheet" href="css/site.css" /><link rel="stylesheet" href="css/store.css" />{extra_head}</head>
<body class="{bodycls}"><a class="skip" href="#main">Skip to content</a>{BANNER}{HEADER}<main id="main">{body}</main>{FOOTER}<script>(function(){{var b=document.getElementById('proto-banner');if(b&&matchMedia('(max-width:820px), (max-height:500px) and (orientation:landscape)').matches)document.body.appendChild(b)}})()</script><script src="js/store.js" defer></script></body></html>'''
    open(S+'/'+fn,'w').write(out)
def thumb(p):
    return p['imgs'][0][0] if p['imgs'] else 'img/logo.png'
def stock_html(p,cls='stk'):
    if not p['stock']: return f'<span class="{cls}" style="color:#b91c1c">Out of stock: we can order it</span>'
    if p['qty'] is not None and p['qty']<=3: return f'<span class="{cls} low">Only {p["qty"]} left in stock</span>'
    return f'<span class="{cls}">In stock</span>'
def adddata(p): return f'data-add data-id="{p["id"]}" data-n="{E(p["n"])}" data-p="{p["c"]}" data-i="{thumb(p)}" data-u="{p["url"]}" data-s="{E(p["sku"])}"'
def card(p,eager=False):
    t=(p['n']+' '+p['sku']+' '+p['brand']+' '+' '.join(re.findall(r'Replaces[^<]*',p['desc']))[:400]).lower()
    t=E(re.sub(r'\s+',' ',t))
    return f'''<article class="card" data-stores="{','.join(p['stores'])}" data-cat="{p['top']}" data-brand="{E(p['brand'])}" data-p="{p['c']}" data-n="{E(p['n'])}" data-r="{p['r']}" data-t="{t}">
<a class="im" href="{p['url']}"><img src="{thumb(p)}" alt="{E(p['n'])}" width="200" height="200" style="max-width:min(100%,{int((p['imgs'][0][1][0] if p['imgs'] else 228)/1.5)}px)" loading="{'eager' if eager else 'lazy'}" decoding="async" /></a>
<div class="bd"><a class="nm" href="{p['url']}">{E(p['n'])}</a><span class="sku">Part # {E(p['sku'])}</span>{stock_html(p)}<span class="pr">{money(p['c'])}</span><button class="add" {adddata(p)}>Add to cart</button></div></article>'''
TRUST=['Free diagnosis assistance','Same-day shipping by 3 pm CST (in stock)','1-year replacement warranty','Pick up at 4 Texas stores']
def trustrow(): return '<ul class="trustrow">'+''.join(f'<li>{x}</li>' for x in TRUST)+'</ul>'
T=json.load(open('/workspace/ufixit-prototype/raw/wp-json/testimonials-full.json'))
QUOTES=[(un(x['title']['rendered']),html.unescape(re.sub('<[^>]+>','',x['content']['rendered'])).strip()) for x in T]
def quotes(n=4,short=260):
    return '<div class="quotes">'+''.join(f'<blockquote class="quote">“{E(q[:short].rsplit(" ",1)[0]+"…" if len(q)>short else q)}”<cite>{E(a)} · customer review on ufixit.com</cite></blockquote>' for a,q in QUOTES[:n])+'</div>'
HELP='''<div class="helpbox"><strong>Not sure it’s the right part?</strong> Match the part number on your old part, or <a href="diy-tips-how-to-find-your-appliance-model-number-and-order-the-right-part.html">find your model number</a> first. Still stuck? Call any store for free diagnosis help: <a href="tel:8174727740">817.472.7740</a> · <a href="how-to-choose.html">How to choose</a></div>'''
# ---------- shop & categories
def facet(name,items,checked=()):
    return ''.join(f'<label><input type="checkbox" name="{name}" value="{E(v)}"{" checked" if v in checked else ""} /> {E(l)} <em>{n}</em></label>' for v,l,n in items)
def shop_page(fn,title,h1,intro,plist,preset_cat=None,preset_brand=None,crumb=None):
    from collections import Counter
    cc=Counter(p['top'] for p in plist); bc=Counter(p['brand'] for p in plist)
    catf=facet('cat',[(k,TOP[k][0],cc[k]) for k in TOP if cc[k]],[preset_cat] if preset_cat else [])
    brf=facet('brand',[(b,b,n) for b,n in sorted(bc.items())],[preset_brand] if preset_brand else [])
    lst=sorted(plist,key=lambda p:p['r'])
    body=f'''<div class="w"><p class="crumbs"><a href="index.html">Home</a> / <a href="shop.html">Shop</a>{" / "+E(crumb) if crumb else ""}</p>
<h1 style="margin:10px 0 6px">{E(h1)}</h1><p style="font:1rem/1.5 system-ui;max-width:48rem;margin:0 0 16px">{intro}</p>{trustrow()}
<div class="shop" data-shop><aside class="filters" id="filters" aria-label="Filters"><button type="button" class="btn-ghost clear-f" data-clear>Clear all filters</button><h3>Location</h3><div data-loc-filter></div><label class="toggle"><input type="checkbox" name="mystock" /> In stock at my store</label><p class="locnote"><span class="ph">Store stock is placeholder data (not in the live feed yet)</span></p><h3>Appliance</h3>{catf}<h3>Brand</h3>{brf}<h3>Price</h3><label>Min $ <input type="number" name="min" min="0" /></label><label>Max $ <input type="number" name="max" min="0" /></label>
<h3>Need help?</h3><p style="margin:0">Free diagnosis help by phone at any store. <a href="how-to-choose.html">How to choose</a></p></aside>
<div><div class="shopbar"><button class="btn-ghost filter-toggle" type="button" aria-expanded="false" aria-controls="filters">Filters</button><span><strong data-count>{len(plist)}</strong> parts</span><input data-q type="search" placeholder="Filter by part # or name" aria-label="Filter results" />
<label>Sort <select data-sort><option value="pop">Popular</option><option value="lo">Price: low to high</option><option value="hi">Price: high to low</option><option value="az">Name A–Z</option></select></label></div>
{HELP}<div class="grid">{"".join(card(p,i<8) for i,p in enumerate(lst))}</div><p data-empty hidden style="font:1rem system-ui">No parts match. <a href="shipping-inquiry.html">Send us the part or model number</a> and we’ll get it.</p></div></div></div>'''
    page(fn,title,re.sub('<[^>]+>','',intro)[:155],body)
shop_page('shop.html','Shop Appliance Parts — U-FIX-IT Appliance Parts','Shop all appliance parts',f'{len(P)} parts from the U-FIX-IT online catalog, with prices from ufixit.com. We have it, or we’ll get it!',P)
from collections import Counter
for c in cats:
    sl=c['slug']; par=CM[c['parent']]['slug'] if c['parent'] else None
    fn=f"product-category-{par+'-' if par else ''}{sl}.html"
    if par:
        pl=[p for p in P if sl in p['subtops']]; br=brand_of(c['name']) if par!='accessories' else None
        name=un(c['name'])
        if par=='accessories': shop_page(fn,f'{name} — U-FIX-IT',name,f'{len(pl)} parts. Prices from ufixit.com.',pl,crumb=name); continue
        top=par; 
        # brand page: preset both
        shop_page(fn,f'{name} — U-FIX-IT Appliance Parts',name,f'{len(pl)} {E(name.lower())} in the U-FIX-IT catalog. Free diagnosis help if you’re not sure which part failed.',[p for p in P if p['top']==top],preset_cat=top,preset_brand=br,crumb=name)
    else:
        pl=[p for p in P if p['top']==sl]
        if not pl: pl=[p for p in P if sl in p['subtops']]
        name=TOP.get(sl,(un(c['name']),))[0]
        shop_page(fn,f'{name} — U-FIX-IT Appliance Parts',name,f'{len(pl)} {E(name.lower())} in stock online, from the brands Texas homeowners own. Prices from ufixit.com.',pl,preset_cat=sl if sl in TOP else None,crumb=name)
# ---------- product pages
def related(p,n=8):
    same=[q for q in P if q['id']!=p['id'] and q['top']==p['top']]
    same.sort(key=lambda q:(q['brand']!=p['brand'],q['r']))
    return same[:n]
TYPES=[('icemaker',r'ice ?maker'),('valve',r'valve'),('element',r'element'),('igniter',r'igniter'),('pump',r'pump'),('belt',r'belt'),('roller',r'roller|idler|pulley'),('thermal',r'thermostat|fuse|cut ?off|thermistor|hi[- ]limit'),('motor',r'motor'),('relay',r'relay|overload|start device'),('seal',r'seal|boot|gasket|bellows|hose'),('switch',r'switch|lock|latch'),('optic',r'optic|ice level'),('board',r'board|control'),('knob',r'knob'),('timer',r'timer'),('bearing',r'bearing'),('coupling',r'coupling|agitator|dogs'),('filter',r'filter|lint')]
COMP={'icemaker':['valve','optic'],'optic':['icemaker','valve'],'valve':['icemaker','filter'],'element':['thermal','switch'],'igniter':['valve','switch'],'pump':['seal','switch'],'belt':['roller','bearing','thermal'],'roller':['belt','bearing'],'bearing':['belt','roller'],'thermal':['element','belt'],'motor':['relay','thermal'],'relay':['motor','thermal'],'seal':['pump','switch'],'switch':['timer','seal'],'board':['thermal','motor'],'knob':['switch','igniter'],'timer':['switch','knob'],'coupling':['switch','pump'],'filter':['valve','icemaker']}
def ptype(n):
    for k,rx in TYPES:
        if re.search(rx,n,re.I): return k
    return None
for p in P: p['type']=ptype(p['n'])
def fbt(p):
    t=p['type']
    if not t: return []
    out=[]
    for ct in COMP.get(t,[]):
        c=[q for q in P if q['id']!=p['id'] and q['top']==p['top'] and q['type']==ct and q['stock'] and q not in out]
        c.sort(key=lambda q:(q['brand']!=p['brand'],q['r']))
        if c: out.append(c[0])
        if len(out)==2: break
    return out
def specs(p):
    t=html.unescape(re.sub('<[^>]+>',' ',p['desc'])); t=re.sub(r'\s+',' ',t)
    d={}
    m=re.search(r'(\d{3}(?:/\d{3})?) ?volts',t,re.I) or re.search(r'Volts:? ?(\d{3})',t,re.I)
    if m: d['Voltage']=m.group(1)+' V'
    m=re.search(r'(\d{3,4}(?:/\d{3,4})?) ?watts',t,re.I) or re.search(r'Watts:? ?(\d{3,4})',t,re.I)
    if m: d['Wattage']=m.group(1)+' W'
    m=re.search(r'Fits ([^.]{3,120}?)(?= Description| Cross|\.|$)',t)
    if m: d['Fits']=m.group(1).strip()
    m=re.search(r'Replaces:? ?([^.]{3,400}?)(?= Also fits|$|\. )',t)
    if m: d['Replaces']=m.group(1).strip(' .')
    return d
for p in P:
    big=p['imgs'][0] if p['imgs'] else ('img/logo.png',(228,114))
    dispmax=int(big[1][0]/1.5)
    thumbs=''.join(f'<button type="button" data-src="{f}" aria-current="{str(i==0).lower()}" aria-label="Image {i+1}"><img src="{f}" alt="" width="60" height="60" loading="lazy" /></button>' for i,(f,s) in enumerate(p['imgs'])) if len(p['imgs'])>1 else ''
    fb=fbt(p); rel=related(p)
    fbhtml=''
    if fb:
        tot=p['c']+sum(q['c'] for q in fb)
        fbhtml=f'''<div class="fbt"><h2 class="tabs-h" style="margin-top:0">Complete the repair</h2><p style="margin:-6px 0 12px;font-size:1rem;color:#5e5e5e">Related parts from the same appliance. Ask us if you’re not sure you need them.</p><div class="fbt-items">'''+'<span class="plus">+</span>'.join(f'<a class="fbt-item" href="{q["url"]}"><img src="{thumb(q)}" alt="" width="64" height="64" loading="lazy" /><span>{E(q["n"])}<br /><strong>{money(q["c"])}</strong></span></a>' for q in [p]+fb)+f'''</div><p style="margin:14px 0 0"><strong>Total {money(tot)}</strong> &nbsp; <button class="btn-buy" style="padding:11px 18px;font-size:.9rem" {adddata(p)} data-also="{','.join(str(q['id']) for q in fb)}">Add all {len(fb)+1} to cart</button></p></div>'''
    sp=specs(p); spec_rows=''.join(f'<tr><th>{k}</th><td>{E(v)}</td></tr>' for k,v in [('Part #',p['sku']),('Brand',p['brand']),('Appliance',TOP.get(p['top'],(p['top'],))[0])]+list(sp.items())+[('Price',money(p['c'])),('Availability',p['stxt'] or ('In stock' if p['stock'] else 'Out of stock'))])
    lead=f"The {E(p['n'])} (part # {E(p['sku'])}) is a {E(TOP.get(p['top'],(p['top'],))[0].lower().replace(' parts',''))} replacement part"+(f" rated {sp['Voltage']}"+(f", {sp['Wattage']}" if 'Wattage' in sp else '') if 'Voltage' in sp else '')+(f". It fits {E(sp['Fits'])}" if 'Fits' in sp else '')+(f" and replaces {E(sp['Replaces'][:160])}" if 'Replaces' in sp else '')+f". {money(p['c'])} at U-FIX-IT."
    ship='Ships same day if ordered by 3 pm CST Mon–Fri' if p['stock'] else 'We’ll order it for you. Call for an ETA'
    ld={"@context":"https://schema.org","@type":"Product","name":p['n'],"sku":p['sku'],"image":[f for f,s in p['imgs']],"brand":{"@type":"Brand","name":p['brand']},"offers":{"@type":"Offer","priceCurrency":"USD","price":f"{p['c']/100:.2f}","availability":"https://schema.org/"+("InStock" if p['stock'] else "OutOfStock")}}
    body=f'''<div class="w"><p class="crumbs"><a href="index.html">Home</a> / <a href="shop.html">Shop</a> / <a href="product-category-{p['top']}.html">{E(TOP.get(p['top'],(p['top'],))[0])}</a> / {E(p['n'])}</p>
<div class="pdp"><div><div class="gal-main"><img src="{big[0]}" alt="{E(p['n'])}" width="{big[1][0]}" height="{big[1][1]}" style="max-width:min(100%,{dispmax}px)" fetchpriority="high" /></div><div class="thumbs">{thumbs}</div></div>
<div><p class="eyebrow">{E(p['brand'])} · {E(TOP.get(p['top'],(p['top'],))[0])}</p><h1>{E(p['n'])}</h1><div class="meta"><span>Part # {E(p['sku'])}</span><span>Sold by U-FIX-IT Appliance Parts</span></div>
<p class="price-big">{money(p['c'])}</p>{stock_html(p,'instock')}
<div class="buybox"><div class="avail" data-avail data-online="{1 if p['stock'] else 0}" data-stores="{','.join(p['stores'])}"></div><div class="qtyrow"><div class="qty"><button type="button" data-d="-1" aria-label="Less">−</button><input id="q" value="1" inputmode="numeric" aria-label="Quantity" /><button type="button" data-d="1" aria-label="More">+</button></div><button class="btn-buy" id="buy" {adddata(p)} data-qty="#q">Add to cart</button></div>
<ul class="assure"><li>{ship}</li><li>1-year replacement warranty unless stated on your receipt. <a href="about-us-warranty-returns.html">Warranty &amp; returns</a></li><li>Free pickup at Arlington, East Dallas, South Dallas or Tyler</li><li>Not sure it’s the right part? Free diagnosis help: <a class="tap" href="tel:8174727740">817.472.7740</a></li><li>Secure checkout</li></ul></div>
{fbhtml}</div></div>
<h2 class="tabs-h">Part details</h2><p class="desc lead-p">{lead}</p><table class="compare spec">{spec_rows}</table><div class="desc">{p['desc']}</div>
<h2 class="tabs-h">What customers say about U-FIX-IT</h2><p style="font:.875rem system-ui;color:var(--muted)">Store reviews from ufixit.com. This part has no product reviews on the live site yet <span class="ph">product reviews: none on live site</span></p>{quotes(2,220)}
<div class="sec" style="padding:48px 0"><div class="row-head"><h2>You may also need</h2><a href="product-category-{p['top']}.html">See all {E(TOP.get(p['top'],(p['top'],))[0].lower())}</a></div><div class="grid">{"".join(card(q) for q in rel)}</div></div></div>
<div class="sticky-buy"><span class="p">{money(p['c'])}</span><button class="btn-buy" {adddata(p)} data-qty="#q">Add to cart</button></div>'''
    page(p['url'],f"{p['n']} — U-FIX-IT Appliance Parts",re.sub("<[^>]+>","",html.unescape(lead))[:155],body,f'<script type="application/ld+json">{json.dumps(ld)}</script>','has-sticky')
# ---------- home
def sect(id_):
    m=re.search(r'<section class="band[^"]*" id="'+id_+r'">.*?</section>',idx,re.S); return m.group(0).replace('<small style="display:block;margin-top:0.5rem;','<small style="display:block;font-size:.875rem;margin-top:0.5rem;') if m else ''
best=[BYID[i] for i in pop if i in BYID]
cc=Counter(p['top'] for p in P)
tiles=''.join(f'<a class="cat" href="product-category-{k}.html"><img src="img/photo/{TOP[k][1]}.webp" alt="" width="450" height="300" loading="lazy" /><span>{E(TOP[k][0])}<small>{cc[k]} parts</small></span></a>' for k in NAVTOPS+['accessories'] if cc[k])
PICKS=''.join(f'<button type="button" class="pick" data-store="{x[0]}"><strong>{x[0]}</strong><span>{re.sub("<[^>]+>","",x[3]).split(",")[0]} · {x[1]}</span></button>' for x in STORES)
home=f'''<section class="hero"><div class="w"><p class="eyebrow">Appliance parts store · Texas · Ships nationwide</p><h1>We have it, or we’ll get it!</h1>
<p class="lead">Replacement parts for refrigerators, washers, dryers, ranges and more, with real people who help you pick the right one.</p>
<div class="picker" id="pick"><p class="pick-h">Step 1 · Pick your store</p><div class="pick-grid">{PICKS}</div>
<div class="pick-row"><button type="button" class="btn-ghost geo" data-geo>Use my location</button><a class="btn-buy" href="shop.html?store=ship">Shop all parts, shipped to you</a></div><p class="geo-msg" data-geo-msg aria-live="polite"></p></div>
{trustrow()}</div></section>
<section class="sec" id="best-sellers"><div class="w"><div class="row-head"><div><p class="eyebrow">Popular right now</p><h2>Best sellers</h2><p class="best-sub" style="font:1rem system-ui;color:var(--muted);margin:0">Ranked by the live store’s popularity sort on ufixit.com.</p></div><a class="btn-buy" style="padding:12px 20px" href="shop.html">Shop all {len(P)} parts</a></div><div class="grid">{"".join(card(p,i<4) for i,p in enumerate(best[:8]))}</div></div></section>
<section class="sec sec--tint"><div class="w"><div class="row-head"><h2>Shop by appliance</h2><a href="find-your-brand.html">Or shop by brand</a></div><div class="cats">{tiles}</div></div></section>
<section class="sec"><div class="w"><p class="eyebrow">Right part, first time</p><h2>How to choose the right part</h2><div class="steps3">
<div><h3>1. Find your model number</h3><p>It’s on a tag inside the door, on the back or under the lid. <a href="diy-tips-how-to-find-your-appliance-model-number-and-order-the-right-part.html">Where to look</a></p></div>
<div><h3>2. Match the part number</h3><p>Search the number printed on your old part. Product pages list cross-reference numbers it replaces.</p></div>
<div><h3>3. Not sure? Ask us free</h3><p>Call or visit any store for free diagnosis help. Bring the part in and we’ll test it.</p></div></div>
<p style="margin-top:22px"><a class="btn-ghost" href="how-to-choose.html">Compare your options</a></p></div></section>
<section class="sec sec--tint"><div class="w"><p class="eyebrow">Real reviews from ufixit.com</p><h2>Why Texans come back</h2>{quotes()}</div></section>
<section class="trustbar"><div class="w">{trustrow()}</div></section>
{sect('why')}{sect('stores')}{sect('diy')}'''
page('index.html','Appliance Parts Store Texas — Shop Online | U-FIX-IT Appliance Parts','Shop appliance parts online from U-FIX-IT: refrigerator, washer, dryer, range and dishwasher parts. Free diagnosis help, same-day shipping on in-stock parts, 4 Texas stores.',home,'<link rel="preload" as="image" href="img/photo/hero-parts-m.webp" media="(max-width:820px)" fetchpriority="high" /><link rel="preload" as="image" href="img/photo/hero-parts.webp" media="(min-width:821px)" fetchpriority="high" />')
# ---------- how to choose
htc=f'''<div class="w" style="padding:20px 0 60px"><p class="crumbs"><a href="index.html">Home</a> / How to choose</p><h1>How to choose the right appliance part</h1>
<p style="font:1.05rem/1.6 system-ui;max-width:46rem">The fastest way to the right part is the part number on your old part, or your appliance’s model number. Here’s how to get there, and the three ways to buy.</p>
<div class="steps3" style="margin:28px 0">
<div><h3>Find your model number</h3><p>Look inside the door frame, on the back panel, or under the lid. <a href="diy-tips-how-to-find-your-appliance-model-number-and-order-the-right-part.html">Full guide</a></p></div>
<div><h3>Read the part number</h3><p>Most parts have a number stamped or printed on them. Search it in the bar above. Our product pages list the numbers each part replaces.</p></div>
<div><h3>Confirm the symptom</h3><p>Each product page lists failure symptoms and how to test the part. Not sure? We offer free diagnosis assistance.</p></div></div>
<h2>Which way to buy is right for you?</h2><table class="compare"><thead><tr><th></th><th>Order online</th><th>Pick up in store</th><th>Call or visit for help</th></tr></thead><tbody>
<tr><td><strong>Best when</strong></td><td>You know the part number</td><td>You need it today in DFW or Tyler</td><td>You’re not sure what failed</td></tr>
<tr><td><strong>Speed</strong></td><td>Same-day shipping on in-stock parts ordered by 3 pm CST, Mon–Fri</td><td>During store hours</td><td>Same call</td></tr>
<tr><td><strong>Cost to ship</strong></td><td><span class="ph">shipping rates TBD (live site quotes by request)</span></td><td>Free</td><td>—</td></tr>
<tr><td><strong>Help</strong></td><td>Part details, symptoms and cross references on every page</td><td>Free diagnosis and part testing</td><td>Free diagnosis assistance and tech tips</td></tr>
<tr><td><strong>Warranty</strong></td><td colspan="3">1-year replacement warranty unless otherwise stated on your receipt. <a href="about-us-warranty-returns.html">Details</a></td></tr></tbody></table>
<h2 style="margin-top:44px">Shop by appliance</h2><div class="cats">{tiles}</div></div>'''
page('how-to-choose.html','How to Choose the Right Appliance Part — U-FIX-IT','Find your model number, match the part number, and compare ordering online, in-store pickup, or free diagnosis help.',htc)
# ---------- cart / checkout / confirm / account / lookup
storeopts=''.join(f'<option value="{s[0]}">{s[0]} · {s[1]}</option>' for s in STORES)
cart_js='''<script>document.addEventListener('DOMContentLoaded',function(){var U=UFX,el=document.getElementById('lines'),sum=document.getElementById('sum');
function r(){var c=U.cart(),st=0;if(!c.length){el.innerHTML='<p>Your cart is empty. <a href="shop.html">Shop parts</a> or see <a href="index.html#best-sellers">best sellers</a>.</p>';sum.hidden=true;return}sum.hidden=false;
el.innerHTML=c.map(function(l,i){st+=l.p*l.q;return '<div class="line"><a href="'+l.u+'"><img src="'+l.i+'" alt=""></a><div><a class="nm" href="'+l.u+'">'+l.n+'</a><div style="font-size:.875rem;color:#5e5e5e">Part # '+l.s+'</div><div style="margin-top:8px;display:flex;gap:10px;align-items:center"><div class="qty"><button data-i="'+i+'" data-d="-1" aria-label="Decrease quantity of '+l.n.replace(/"/g,'')+'">−</button><input value="'+l.q+'" readonly aria-label="Quantity"><button data-i="'+i+'" data-d="1" aria-label="Increase quantity of '+l.n.replace(/"/g,'')+'">+</button></div><a href="#" class="rm" data-rm="'+i+'">Remove</a></div></div><strong>'+U.money(l.p*l.q)+'</strong></div>'}).join('');
var f=U.CFG.freeShip*100,left=f-st;document.getElementById('meter').innerHTML=(left>0?'You’re <strong>'+U.money(left)+'</strong> away from free shipping':'<strong>You’ve unlocked free shipping</strong>')+' <span class="ph">threshold placeholder: $'+U.CFG.freeShip+', U-FIX-IT to set</span><div class="bar"><i style="width:'+Math.min(100,st/f*100)+'%"></i></div>';
document.getElementById('st').textContent=U.money(st);document.getElementById('tot').textContent=U.money(st)}
el.addEventListener('click',function(e){var c=U.cart(),b=e.target.closest('[data-d]'),x=e.target.closest('[data-rm]');if(b){var sel='[data-i="'+b.dataset.i+'"][data-d="'+b.dataset.d+'"]';c[b.dataset.i].q=Math.max(1,c[b.dataset.i].q+(+b.dataset.d));U.set(c);r();var nb=el.querySelector(sel);if(nb)nb.focus()}if(x){e.preventDefault();c.splice(x.dataset.rm,1);U.set(c);r();var h=document.querySelector('main h1');h.tabIndex=-1;h.focus()}});r()});</script>'''
upsell=''.join(card(p) for p in best[:4])
page('cart.html','Your Cart — U-FIX-IT Appliance Parts','Your cart',f'''<div class="w"><h1 style="margin:24px 0 0">Your cart</h1><div class="cartwrap"><div><div id="lines"></div><div class="helpbox" style="margin-top:22px"><strong>Double-check fit:</strong> compare the part # with the one on your old part. Questions? Free diagnosis help at <a href="tel:8174727740">817.472.7740</a>.</div></div>
<aside class="summary" id="sum"><div class="ship-meter" id="meter"></div><div class="r"><span>Subtotal</span><span id="st"></span></div><div class="r"><span>Shipping</span><span>Free pickup, or calculated at checkout</span></div><div class="r"><span>Tax</span><span>At checkout <span class="ph">TX tax calc TBD</span></span></div><div class="r tot"><span>Total</span><span id="tot"></span></div>
<a class="btn-buy" style="width:100%;margin-top:14px" href="checkout.html">Checkout</a><p style="font-size:.875rem;color:#5e5e5e;margin:10px 0 0">Guest checkout, no account needed.</p>{trustrow()}</aside></div>
<h2>Popular add-ons</h2><div class="grid" style="margin-bottom:60px">{upsell}</div></div>{cart_js}''')
co_js='''<script>document.addEventListener('DOMContentLoaded',function(){var U=UFX,c=U.cart(),st=c.reduce(function(a,l){return a+l.p*l.q},0);if(!c.length){location.href='cart.html';return}
document.getElementById('items').innerHTML=c.map(function(l){return '<div class="r"><span>'+l.q+' × '+l.n+'</span><span>'+U.money(l.p*l.q)+'</span></div>'}).join('');document.getElementById('st').textContent=U.money(st);
var f=document.getElementById('co'),shipF=['addr','city','state','zip'];
function sh(){var p=f.ful.value=='pickup';document.getElementById('shipf').hidden=p;document.getElementById('pickf').hidden=!p;shipF.forEach(function(n){f[n].required=!p});document.getElementById('shipcost').innerHTML=p?'Free':(st>=U.CFG.freeShip*100?'Free':'Calculated after order')}
f.addEventListener('change',sh);sh();
f.querySelector('[name=ccnum]').addEventListener('input',function(e){var v=e.target.value.replace(/\\D/g,'').slice(0,16);e.target.value=v.replace(/(.{4})/g,'$1 ').trim()});
f.querySelector('[name=ccexp]').addEventListener('input',function(e){var v=e.target.value.replace(/\\D/g,'').slice(0,4);e.target.value=v.length>2?v.slice(0,2)+' / '+v.slice(2):v});
var MSG={email:'Enter a valid email address',fname:'Enter your first name',lname:'Enter your last name',addr:'Enter your street address',city:'Enter your city',state:'Choose your state',zip:'Enter a 5-digit ZIP code',ccnum:'Enter a 15 or 16 digit card number',ccexp:'Enter expiry as MM / YY',cccsc:'Enter the 3 or 4 digit code'};
function err(i,show){var e=i.parentNode.querySelector('.err');if(!e){e=document.createElement('span');e.className='err';e.id=i.name+'-err';e.setAttribute('aria-live','polite');i.parentNode.appendChild(e);i.setAttribute('aria-describedby',e.id)}e.textContent=show?MSG[i.name]||'Required':'';i.setAttribute('aria-invalid',show)}
function check(i){var ok=i.checkValidity();err(i,!ok);return ok}
f.querySelectorAll('input[name],select[name]').forEach(function(i){if(MSG[i.name]){err(i,false);i.removeAttribute('aria-invalid')}});
f.querySelectorAll('input[name],select[name]').forEach(function(i){if(MSG[i.name])i.addEventListener('blur',function(){check(i)})});
f.addEventListener('submit',function(e){e.preventDefault();var bad=null;f.querySelectorAll('input[name],select[name]').forEach(function(i){if(!MSG[i.name]||i.closest('[hidden]'))return;if(!check(i)&&!bad)bad=i});var nb=f.querySelectorAll('[aria-invalid=true]').length;document.getElementById('co-sum').textContent=nb?('Please fix '+nb+' field'+(nb>1?'s':'')+' below.'):'';if(bad){bad.focus();return}
var o={no:'UFX-'+Math.floor(100000+Math.random()*900000),email:f.email.value.trim().toLowerCase(),name:f.fname.value+' '+f.lname.value,items:c,total:st,ful:f.ful.value,store:f.store.value,date:new Date().toISOString(),status:'Received (prototype)'};U.saveOrder(o);U.clear();location.href='order-confirmation.html?o='+o.no})});</script>'''
STATES=['AL','AK','AZ','AR','CA','CO','CT','DE','DC','FL','GA','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']
stateopts='<option value="">Choose</option>'+''.join(f'<option{" selected" if x=="TX" else ""}>{x}</option>' for x in STATES)
page('checkout.html','Checkout — U-FIX-IT Appliance Parts','Checkout',f'''<div class="w"><h1 style="margin:24px 0 0">Checkout</h1><p style="font-size:1.125rem;margin:4px 0 0;font-family:system-ui">Guest checkout, no account needed · <a class="tap" href="account.html">Sign in</a> (optional)</p>
<form id="co" class="cartwrap" novalidate><div class="form"><div class="step-h">1. Contact</div><label>Email<input name="email" type="email" required autocomplete="email" /></label><div class="two"><label>First name<input name="fname" required autocomplete="given-name" /></label><label>Last name<input name="lname" required autocomplete="family-name" /></label></div><label>Phone (optional)<input name="phone" type="tel" autocomplete="tel" inputmode="tel" /></label>
<div class="step-h">2. Delivery</div><label class="opt"><input type="radio" name="ful" value="ship" checked /> <span><strong>Ship to me</strong><br />Continental US. In-stock parts ship same day if ordered by 3 pm CST Mon–Fri.</span></label><label class="opt"><input type="radio" name="ful" value="pickup" /> <span><strong>Free store pickup</strong><br />Arlington, East Dallas, South Dallas or Tyler</span></label>
<div id="shipf" class="form"><label>Street address<input name="addr" autocomplete="address-line1" /></label><div class="two"><label>City<input name="city" autocomplete="address-level2" /></label><label>State<select name="state" autocomplete="address-level1">{stateopts}</select></label></div><label>ZIP<input name="zip" inputmode="numeric" pattern="\\d{{5}}" maxlength="5" autocomplete="postal-code" /></label></div>
<div id="pickf" hidden><label>Pickup store<select name="store">{storeopts}</select></label></div>
<div class="step-h">3. Payment</div><label>Card number<input name="ccnum" inputmode="numeric" autocomplete="cc-number" pattern="[\\d ]{{17,19}}" maxlength="19" placeholder="1234 5678 9012 3456" required /></label><div class="two"><label>Expiry<input name="ccexp" inputmode="numeric" autocomplete="cc-exp" pattern="(0[1-9]|1[0-2]) / \\d{{2}}" maxlength="7" placeholder="MM / YY" required /></label><label>Security code<input name="cccsc" inputmode="numeric" autocomplete="cc-csc" pattern="\\d{{3,4}}" maxlength="4" placeholder="CVC" required /></label></div>
<p id="co-sum" class="err-sum" role="alert" aria-live="assertive"></p><button class="btn-buy">Place order</button></div>
<aside class="summary"><div id="items"></div><div class="r"><span>Subtotal</span><span id="st"></span></div><div class="r"><span>Shipping</span><span id="shipcost"></span></div><div class="r"><span>Tax</span><span>Calculated after order</span></div>{trustrow()}<p style="font-size:1rem;margin:12px 0 0">1-year replacement warranty unless stated on your receipt.</p></aside></form></div>{co_js}''')
page('order-confirmation.html','Order received — U-FIX-IT','Order confirmation','''<div class="w" style="padding:40px 0 70px;font-family:system-ui"><p class="eyebrow">Thank you</p><h1>Order received</h1><div id="o"></div><p><a class="btn-buy" href="shop.html">Keep shopping</a> <a class="btn-ghost" href="order-lookup.html">Track this order</a></p></div>
<script>document.addEventListener('DOMContentLoaded',function(){var n=new URLSearchParams(location.search).get('o'),o=UFX.orders().find(function(x){return x.no==n});document.getElementById('o').innerHTML=o?'<p>Order <strong>'+o.no+'</strong> for '+o.email+'. Total '+UFX.money(o.total)+' plus shipping/tax (TBD). '+(o.ful=='pickup'?'Pickup at '+o.store+'.':'We will email tracking when it ships.')+'</p><p><span class="ph">Prototype: no email was sent and no payment was taken.</span></p>':'<p>Order not found on this device.</p>'})</script>''')
lk='''<script>document.addEventListener('DOMContentLoaded',function(){var f=document.getElementById('lk');f.addEventListener('submit',function(e){e.preventDefault();var o=UFX.orders().find(function(x){return x.no.toUpperCase()==f.no.value.trim().toUpperCase()&&x.email==f.em.value.trim().toLowerCase()});document.getElementById('res').innerHTML=o?'<div class="helpbox"><strong>'+o.no+'</strong> · '+o.status+' · '+new Date(o.date).toLocaleDateString()+'<br>'+o.items.map(function(l){return l.q+' × '+l.n}).join('<br>')+'<br>Total '+UFX.money(o.total)+'</div>':'<p>No order found. Check the number and email, or call any store.</p>'})})</script>'''
page('order-lookup.html','Track Your Order — U-FIX-IT','Look up an order by number and email',f'''<div class="w" style="padding:30px 0 70px;max-width:620px;font-family:system-ui"><h1>Track your order</h1><p>Enter your order number and the email used at checkout. No account needed.</p><form id="lk" class="form"><label>Order number<input name="no" required placeholder="UFX-123456" autocapitalize="characters" spellcheck="false" autocomplete="off" /></label><label>Email<input name="em" type="email" required autocomplete="email" /></label><button class="btn-buy">Find order</button></form><div id="res" style="margin-top:20px"></div><p style="font-size:.875rem;color:#5e5e5e">Prototype: looks up orders placed on this device. <span class="ph">Live order status source TBD</span></p></div>{lk}''')
ac='''<script>document.addEventListener('DOMContentLoaded',function(){var k='ufx_user',u=localStorage.getItem(k),box=document.getElementById('acct');function r(){u=localStorage.getItem(k);if(!u){box.innerHTML=document.getElementById('tpl').innerHTML;box.querySelectorAll('form').forEach(function(f){f.addEventListener('submit',function(e){e.preventDefault();localStorage.setItem(k,f.querySelector('[type=email]').value.toLowerCase());r()})});return}
var os=UFX.orders().filter(function(o){return o.email==u});box.innerHTML='<p>Signed in as <strong>'+u+'</strong> · <a href="#" id="so">Sign out</a></p><h2>Order history</h2>'+(os.length?os.map(function(o){return '<div class="line" style="grid-template-columns:1fr auto"><div><strong>'+o.no+'</strong> · '+new Date(o.date).toLocaleDateString()+' · '+o.status+'<br><span style="font-size:.875rem">'+o.items.map(function(l){return l.q+' × '+l.n}).join(', ')+'</span></div><strong>'+UFX.money(o.total)+'</strong></div>'}).join(''):'<p>No orders yet. <a href="shop.html">Shop parts</a></p>')+'<h2>Saved addresses</h2><p><span class="ph">Address book: placeholder</span></p>';document.getElementById('so').onclick=function(e){e.preventDefault();localStorage.removeItem(k);r()}}r()})</script>'''
page('account.html','My Account — U-FIX-IT','Sign in or create an account',f'''<div class="w" style="padding:30px 0 70px;font-family:system-ui"><h1>My account</h1><p><span class="ph">Mock accounts: stored on this device only</span></p><div id="acct"></div>
<template id="tpl"><div class="cartwrap" style="grid-template-columns:1fr 1fr;padding-top:10px"><form class="form"><div class="step-h">Sign in</div><label>Email<input type="email" required /></label><label>Password<input type="password" required /></label><button class="btn-buy">Sign in</button></form><form class="form"><div class="step-h">Create account</div><label>Email<input type="email" required /></label><label>Password<input type="password" required /></label><button class="btn-ghost">Create account</button><p style="font-size:.875rem">You can always check out as a guest.</p></form></div></template></div>{ac}''')
# ---------- retrofit existing pages
gen=set([p['url'] for p in P]+['shop.html','index.html','how-to-choose.html','cart.html','checkout.html','order-confirmation.html','order-lookup.html','account.html','brand.html']+[f for f in os.listdir(S) if f.startswith('product-category-')])
n=0
for f in glob.glob(S+'/*.html'):
    b=os.path.basename(f)
    if b in gen or b.startswith('UFixIt-'): continue
    h=open(f).read()
    if 'css/store.css' in h:
        h=h.replace('content="width=device-width, initial-scale=1" />','content="width=device-width, initial-scale=1, viewport-fit=cover" />',1)
        h=re.sub(r'<header class="sh">.*?</header>',lambda m:HEADER,h,count=1,flags=re.S)
        h=re.sub(r'<section class="capture">.*?</footer>',lambda m:FOOTER,h,count=1,flags=re.S)
        open(f,'w').write(h); n+=1; continue
    h=h.replace('<link rel="stylesheet" href="css/site.css" />','<link rel="stylesheet" href="css/site.css" /><link rel="stylesheet" href="css/store.css" />',1)
    h=re.sub(r'<header class="site-header">.*?</header>',lambda m:HEADER,h,count=1,flags=re.S)
    h=re.sub(r'<footer class="site-footer">.*?</footer>',lambda m:FOOTER,h,count=1,flags=re.S)
    h=h.replace('</body>','<script>(function(){var b=document.getElementById(\'proto-banner\');if(b&&matchMedia(\'(max-width:820px), (max-height:500px) and (orientation:landscape)\').matches)document.body.appendChild(b)})()</script><script src="js/store.js" defer></script></body>',1); open(f,'w').write(h); n+=1
print('products',len(P),'retrofit',n, Counter(p['brand'] for p in P).most_common(8))
json.dump([{k:p[k] for k in ('id','n','sku','c','top','brand','url')} for p in P],open(S+'/references/catalog-snapshot.json','w'))
