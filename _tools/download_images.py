"""
download_images.py — Stage 3 of the image extraction workflow.

Usage:
    python3 _tools/download_images.py _Sales_Opp/ClientName/img

What it does:
    - Reads img/_image_urls_clean.txt (produced after Stage 2 review)
    - Downloads every image into the img/ folder with a clean local filename
    - Skips files already downloaded (safe to re-run)
    - Skips responses under 200 bytes (tracking pixels / empty responses)
    - Prints a summary: downloaded / skipped / failed

After running:
    - Run: python3 _tools/download_images.py <img_dir>  (verify output)
    - Or use the sips shell loop in README Stage 4 to check dimensions
    - Update all <img src> and CSS background-image paths in prototype HTML
      to use relative img/ paths — NEVER reference external CDN URLs
"""
import sys, os, urllib.request, urllib.parse, mimetypes

if len(sys.argv) < 2:
    print("Usage: python3 download_images.py <IMG_DIR>")
    sys.exit(1)

IMG_DIR  = sys.argv[1]
URL_FILE = os.path.join(IMG_DIR, '_image_urls_clean.txt')
HEADERS  = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'}

if not os.path.exists(URL_FILE):
    print(f'ERROR: {URL_FILE} not found.')
    print('Run discover_images.py first, then review and save as _image_urls_clean.txt')
    sys.exit(1)

with open(URL_FILE) as f:
    urls = [l.strip() for l in f if l.strip() and not l.startswith('#')]

def safe_filename(url, index):
    parsed = urllib.parse.urlparse(url)
    basename = os.path.basename(parsed.path.rstrip('/'))
    basename = basename.split('?')[0]
    # Strip Shopify size suffixes like _800x.jpg → .jpg
    basename = re.sub(r'_\d+x(\.\w+)$', r'\1', basename) if __import__('re').search(r'_\d+x\.\w+$', basename) else basename
    if not basename or len(basename) < 4:
        ext = (mimetypes.guess_extension(mimetypes.guess_type(url)[0] or 'image/jpeg') or '.jpg')
        basename = f'img_{index:03d}{ext}'
    return basename

import re
ok = skip = fail = 0

for i, url in enumerate(urls, 1):
    fname = safe_filename(url, i)
    fpath = os.path.join(IMG_DIR, fname)

    if os.path.exists(fpath) and os.path.getsize(fpath) > 500:
        print(f'  SKIP  [{i:03d}] {fname}')
        skip += 1
        continue

    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read()
        if len(data) < 200:
            print(f'  TINY  [{i:03d}] {fname} ({len(data)}B) — skipped')
            fail += 1
            continue
        with open(fpath, 'wb') as f:
            f.write(data)
        print(f'  OK    [{i:03d}] {fname}: {len(data):,} bytes')
        ok += 1
    except Exception as e:
        print(f'  FAIL  [{i:03d}] {fname}: {e}')
        fail += 1

print(f'\n✓ Done. Downloaded: {ok}  Skipped (already exist): {skip}  Failed: {fail}')
print(f'  All images in: {IMG_DIR}')
print('\nNext: run the Stage 4 sips loop (see README) to check dimensions, then assign images to prototype sections.')
print('REMINDER: All <img src> and CSS background-image in the prototype MUST use relative img/ paths.')
