# -*- coding: utf-8 -*-
"""Забирает все фото с CDN в папку img/ (WebP) и переписывает ссылки в собранных страницах."""
import os, re, sys, base64, urllib.request, concurrent.futures
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image
import data

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, 'img')
RAW = os.path.join(ROOT, '_build', '.raw')
PAGES = [f for f in os.listdir(ROOT) if f.startswith('variant-') and f.endswith('.html')]

PLANS = {u.split('/')[-1] for n, a, p, u, note in data.PLANS_25 + data.PLANS_36}

def collect():
    urls = set()
    for f in PAGES:
        src = open(os.path.join(ROOT, f), encoding='utf-8').read()
        urls |= set(re.findall(r'https://90f1661d[^"\' )]+\.(?:jpe?g|png)', src))
    return sorted(urls)

def fetch(u):
    """Качает файл с повторами: CDN иногда обрывает соединение."""
    name = u.split('/')[-1]
    dst = os.path.join(RAW, name)
    if os.path.exists(dst) and os.path.getsize(dst) > 1024:
        return name
    last = None
    for attempt in range(5):
        try:
            req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=90) as r:
                blob = r.read()
                want = r.headers.get('Content-Length')
            if want and len(blob) != int(want):
                raise IOError(f'получено {len(blob)} из {want} байт')
            with open(dst, 'wb') as f:
                f.write(blob)
            return name
        except Exception as e:
            last = e
    raise IOError(f'не удалось скачать {name}: {last}')

def convert(name):
    out = os.path.join(IMG, name.rsplit('.', 1)[0] + '.webp')
    if os.path.exists(out):
        return out
    im = Image.open(os.path.join(RAW, name))
    if im.mode in ('RGBA', 'P', 'LA'):
        bg = Image.new('RGB', im.size, (255, 255, 255))
        im = im.convert('RGBA'); bg.paste(im, mask=im.split()[-1]); im = bg
    else:
        im = im.convert('RGB')
    is_plan = name in PLANS
    cap, q = (1400, 82) if is_plan else (1800, 78)
    w, h = im.size
    if max(w, h) > cap:
        k = cap / max(w, h)
        im = im.resize((round(w * k), round(h * k)), Image.LANCZOS)
    im.save(out, 'WEBP', quality=q, method=6)
    return out

def main():
    os.makedirs(IMG, exist_ok=True); os.makedirs(RAW, exist_ok=True)
    urls = collect()
    print(f"уникальных изображений: {len(urls)}")
    with concurrent.futures.ThreadPoolExecutor(8) as ex:
        names = list(ex.map(fetch, urls))
    print("скачано")
    with concurrent.futures.ThreadPoolExecutor(os.cpu_count() or 4) as ex:
        list(ex.map(convert, names))
    total = sum(os.path.getsize(os.path.join(IMG, f)) for f in os.listdir(IMG))
    print(f"img/: {len(os.listdir(IMG))} файлов, {total/1024/1024:.1f} МБ")

    for f in PAGES:
        p = os.path.join(ROOT, f)
        src = open(p, encoding='utf-8').read()
        src = re.sub(r'https://90f1661d[^"\' )]+/([^/"\' )]+)\.(?:jpe?g|png)',
                     lambda m: 'img/' + m.group(1) + '.webp', src)
        left = len(re.findall(r'https://90f1661d', src))
        open(p, 'w', encoding='utf-8').write(src)
        print(f"  {f}: осталось внешних ссылок {left}")

if __name__ == '__main__':
    main()
