# -*- coding: utf-8 -*-
"""Сборка всех вариантов: python3 _build/build.py"""
import os, sys, importlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

VARIANTS = [
    ("v2", "variant-2-scandi-light.html", "Scandi Light",
     "Светлый журнальный минимализм", "Тёплая бумага, Playfair Display, шторные раскрытия и зигзаг",
     "#F7F4EF", "#8C6A46", "#1C1A17"),
    ("v4", "variant-4-brutal-editorial.html", "Brutal Editorial",
     "Крупная типографика и рамки", "Фирменный жёлтый, бегущие строки, ч/б фото с возвратом цвета",
     "#F2F0EB", "#FFDD2D", "#0D0D0D"),
]

def main():
    # в папке не должно оставаться страниц вариантов, которых больше нет в списке
    keep = {fname for _, fname, *_ in VARIANTS}
    for f in sorted(os.listdir(ROOT)):
        if f.startswith("variant-") and f.endswith(".html") and f not in keep:
            os.remove(os.path.join(ROOT, f))
            print(f"– убран {f}")

    for mod, fname, *_ in VARIANTS:
        m = importlib.import_module(mod)
        importlib.reload(m)
        html = m.build()
        with open(os.path.join(ROOT, fname), "w", encoding="utf-8") as f:
            f.write(html)
        print(f"✓ {fname}  ({len(html)//1024} КБ)")

    import localize
    importlib.reload(localize)
    localize.main()

    import index
    importlib.reload(index)
    with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
        f.write(index.build(VARIANTS))
    print("✓ index.html")

if __name__ == "__main__":
    main()
