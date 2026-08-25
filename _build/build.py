# -*- coding: utf-8 -*-
"""Сборка всех вариантов: python3 _build/build.py"""
import os, sys, importlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Какие варианты попадают на сайт. Чтобы вернуть остальные —
# допишите сюда их ключи ("v1", "v3", "v5") и пересоберите.
PUBLISHED = ("v2", "v4")

ALL_VARIANTS = [
    ("v1", "variant-1-nordic-noir.html", "Nordic Noir",
     "Тёмный кинематографичный премиум", "Латунь на графите, ken-burns герой, липкая прокрутка процесса",
     "#0B0B0C", "#C8A56B", "#EDEBE7"),
    ("v2", "variant-2-scandi-light.html", "Scandi Light",
     "Светлый журнальный минимализм", "Тёплая бумага, Playfair Display, шторные раскрытия и зигзаг",
     "#F7F4EF", "#8C6A46", "#1C1A17"),
    ("v3", "variant-3-bento-tech.html", "Bento Tech",
     "Бенто-сетка с калькулятором", "Графит и лайм, живой расчёт цены, 3D-наклон карточек",
     "#0E0F10", "#C6F24E", "#F2F4F3"),
    ("v4", "variant-4-brutal-editorial.html", "Brutal Editorial",
     "Крупная типографика и рамки", "Фирменный жёлтый, бегущие строки, ч/б фото с возвратом цвета",
     "#F2F0EB", "#FFDD2D", "#0D0D0D"),
    ("v5", "variant-5-glass-aurora.html", "Glass Aurora",
     "Стекло и живые градиенты", "Мятно-фиолетовое сияние, блюр-панели, парящие чипы",
     "#070A0E", "#5EE7C4", "#EAF0F5"),
]

VARIANTS = [v for v in ALL_VARIANTS if v[0] in PUBLISHED]

def main():
    # страницы вариантов, снятых с публикации, не должны оставаться в папке
    for mod, fname, *_ in ALL_VARIANTS:
        if mod not in PUBLISHED:
            stale = os.path.join(ROOT, fname)
            if os.path.exists(stale):
                os.remove(stale)
                print(f"– убран {fname}")

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
