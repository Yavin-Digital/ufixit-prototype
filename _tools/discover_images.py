"""
discover_images.py — Stage 1 of the image extraction workflow.

Usage:
    python3 _tools/discover_images.py https://www.clientsite.com _Sales_Opp/ClientName/img

What it does:
    - Crawls every page on the client's site (follows internal links + sitemap.xml)
    - Extracts ALL image URLs regardless of host: <img src>, srcset, CSS background-image,
      <source>, og:image, Wix warmupData hashes, Cloudinary, Imgix, Shopify CDN, etc.
    - Writes a deduplicated list to img/_image_urls.txt
    - Max 50 pages crawled to prevent runaway loops on large sites

After running:
    1. Open img/_image_urls.txt
    2. Remove tracker pixels, social platform icons, and Google Maps tiles
    3. Save the cleaned list as img/_image_urls_clean.txt
    4. Run download_images.py to pull everything locally
"""
import sys, os, re, urllib.request, urllib.parse

if len(sys.argv) < 3:
    print("Usage: python3 discover_images.py <START_URL> <IMG_DIR>")
    sys.exit(1)

START_URL = sys.argv[1].rstrip('/')
IMG_DIR   = sys.argv[2]
os.makedirs(IMG_DIR, exist_ok=True)

HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'}
IMG_EXT = re.compile(r'\.(jpg|jpeg|png|webp|avif|gif|svg)(\?[^"\'>\s]*)?$', re.IGNORECASE)

PATTERNS = [
    re.compile(r'(?:src|href|content)=["\']([^"\']+\.(jpg|jpeg|png|webp|avif|gif|svg)[^"\']*)["\']', re.IGNORECASE),
    re.compile(r'url\(["\']?([^"\')\s]+\.(jpg|jpeg|png|webp|avif|gif|svg)[^"\')\s]*)["\']?\)', re.IGNORECASE),
    re.compile(r'srcset=["\']([^"\']+)["\']', re.IGNORECASE),
    re.compile(r'([a-f0-9]{32}~mv2\.[a-z]{3,4})', re.IGNORECASE),  # Wix
    re.compile(r'(https://[a-z0-9._-]+(?:cloudinary|imgix|fastly|cdn|media|assets|images|static)[a-z0-9._/-]*/[^\s"\'<>]+\.(jpg|jpeg|png|webp|avif|gif|svg)[^\s"\'<>]*)', re.IGNORECASE),
]

def fetch(url):
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.read().decode('utf-8', errors='ignore')
    except Exception as e:
        print(f'  WARN  {url} — {e}')
        return ''

def resolve(href, base):
    href = href.strip()
    if href.startswith('//'): return 'https:' + href
    if href.startswith('http'): return href
    return urllib.parse.urljoin(base, href)

def extract_img_urls(html, page_url):
    urls = set()
    for pat in PATTERNS:
        for m in pat.finditer(html):
            raw = m.group(1)
            if ',' in raw and ' ' in raw:
                for part in raw.split(','):
                    candidate = part.strip().split()[0]
                    if IMG_EXT.search(candidate):
                        urls.add(resolve(candidate, page_url))
            elif re.match(r'[a-f0-9]{32}~mv2\.[a-z]{3,4}$', raw, re.IGNORECASE):
                urls.add('https://static.wixstatic.com/media/' + raw)
            else:
                if IMG_EXT.search(raw):
                    urls.add(resolve(raw, page_url))
    return urls

def discover_pages(html, base_url):
    domain = urllib.parse.urlparse(base_url).netloc
    found = set()
    for m in re.finditer(r'href=["\']([^"\'#?]+)["\']', html):
        href = m.group(1).strip()
        abs_url = resolve(href, base_url)
        parsed = urllib.parse.urlparse(abs_url)
        if parsed.netloc == domain and not IMG_EXT.search(parsed.path):
            found.add(abs_url.split('?')[0].split('#')[0])
    return found

visited, all_urls, queue = set(), set(), [START_URL]

# Seed from sitemap
sitemap = fetch(START_URL + '/sitemap.xml')
for m in re.finditer(r'<loc>([^<]+)</loc>', sitemap):
    loc = m.group(1).strip()
    if not IMG_EXT.search(loc):
        queue.append(loc)

while queue:
    url = queue.pop(0)
    if url in visited: continue
    visited.add(url)
    print(f'  Crawling [{len(visited):02d}]: {url}')
    html = fetch(url)
    if not html: continue
    all_urls.update(extract_img_urls(html, url))
    if len(visited) < 50:
        for link in discover_pages(html, url):
            if link not in visited:
                queue.append(link)

out = os.path.join(IMG_DIR, '_image_urls.txt')
with open(out, 'w') as f:
    for u in sorted(all_urls):
        f.write(u + '\n')

print(f'\n✓ Found {len(all_urls)} unique image URLs across {len(visited)} pages.')
print(f'  URL list → {out}')
print('\nNext: review _image_urls.txt, remove trackers/icons, save as _image_urls_clean.txt, then run download_images.py')
