# -*- coding: utf-8 -*-
"""Вариант 4 — BRUTAL EDITORIAL. Крупная типографика, сетка-рамка, фирменный жёлтый."""
import core
from data import *

FONTS = '<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">'

CSS = r"""
:root{
  --bg:#F2F0EB; --bg-2:#FFFFFF; --ink:#0D0D0D; --fg:#0D0D0D; --muted:#5C5C58;
  --line:#0D0D0D; --hair:rgba(13,13,13,.16); --accent:#FFDD2D; --on-accent:#0D0D0D;
  --input-bg:#fff;
  --font-head:'Archivo',system-ui,sans-serif; --font-body:'Archivo',system-ui,sans-serif;
  --font-mono:'JetBrains Mono',ui-monospace,monospace;
  --radius:0px; --radius-sm:0px; --head-weight:800;
}
::selection{background:var(--accent);color:var(--ink)}
body{font-weight:400}
.grain{position:fixed;inset:0;z-index:-1;pointer-events:none;opacity:.4;
  background-image:radial-gradient(rgba(13,13,13,.09) 1px,transparent 1px);background-size:3px 3px}
.h1{font-size:clamp(2.6rem,7.6vw,6.8rem);font-weight:900;line-height:.86;letter-spacing:-.045em;text-transform:uppercase}
.h2{font-size:clamp(2rem,6.4vw,5rem);font-weight:900;line-height:.9;letter-spacing:-.04em;text-transform:uppercase}
.h3{font-size:clamp(1.05rem,1.8vw,1.35rem);font-weight:700;letter-spacing:-.02em;text-transform:uppercase}
.mono{font-family:var(--font-mono);font-size:11px;letter-spacing:.14em;text-transform:uppercase}
.lead{font-size:clamp(1rem,1.3vw,1.15rem);max-width:58ch;line-height:1.6;color:var(--muted)}
.hl{background:var(--accent);padding:0 .12em;box-decoration-break:clone;-webkit-box-decoration-break:clone}
.sec{padding:clamp(56px,7vw,110px) 0;border-top:2px solid var(--line)}
.sec-head{display:grid;gap:18px;margin-bottom:clamp(30px,4vw,54px)}
@media(min-width:900px){.sec-head.split{grid-template-columns:1.25fr .75fr;align-items:end;gap:44px}}
.tag{display:inline-block;font-family:var(--font-mono);font-size:11px;letter-spacing:.14em;
  text-transform:uppercase;background:var(--ink);color:var(--bg);padding:6px 12px}

/* Шапка */
.hdr{position:fixed;inset:0 0 auto 0;z-index:100;background:var(--bg);border-bottom:2px solid var(--line);
  transition:transform .45s cubic-bezier(.16,1,.3,1)}
.hdr.hide{transform:translateY(-102%)}
.hdr__in{display:flex;align-items:stretch;justify-content:space-between;gap:0}
.logo{display:flex;align-items:center;gap:10px;font-weight:900;font-size:20px;letter-spacing:-.04em;
  text-transform:uppercase;padding:14px 0}
.logo i{width:12px;height:12px;background:var(--accent);border:2px solid var(--ink);display:block}
.nav{display:none}
@media(min-width:1024px){.nav{display:flex}}
.nav a{display:flex;align-items:center;padding:0 20px;font-family:var(--font-mono);font-size:11px;
  letter-spacing:.14em;text-transform:uppercase;border-left:2px solid var(--line);
  position:relative;overflow:hidden;transition:color .3s}
.nav a::before{content:"";position:absolute;inset:0;background:var(--accent);transform:translateY(101%);
  transition:transform .4s cubic-bezier(.16,1,.3,1);z-index:-1}
.nav a:hover::before{transform:none}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:9px;padding:15px 26px;
  font-family:var(--font-mono);font-size:11px;letter-spacing:.14em;text-transform:uppercase;font-weight:500;
  border:2px solid var(--line);position:relative;overflow:hidden;isolation:isolate;
  transform:translate3d(var(--tx,0),var(--ty,0),0);transition:transform .35s cubic-bezier(.16,1,.3,1),color .3s}
.btn::before{content:"";position:absolute;inset:0;z-index:-1;background:var(--ink);
  transform:translateY(101%);transition:transform .45s cubic-bezier(.16,1,.3,1)}
.btn:hover::before{transform:none}
.btn:hover{color:var(--bg)}
.btn--fill{background:var(--accent)}
.btn--fill::before{background:var(--ink)}
.hdr__cta{display:none;border:0;border-left:2px solid var(--line);padding:0 24px}
@media(min-width:640px){.hdr__cta{display:inline-flex}}
.burger{display:grid;gap:5px;padding:0 18px;border-left:2px solid var(--line)}
@media(min-width:1024px){.burger{display:none}}
.burger i{width:22px;height:2.5px;background:var(--ink);transition:.35s}
body.nav-open .burger i:nth-child(1){transform:translateY(7.5px) rotate(45deg)}
body.nav-open .burger i:nth-child(2){opacity:0}
body.nav-open .burger i:nth-child(3){transform:translateY(-7.5px) rotate(-45deg)}
.mnav{position:fixed;inset:0;z-index:99;background:var(--accent);display:grid;align-content:center;
  padding:0 var(--gutter);opacity:0;visibility:hidden;transition:.35s}
body.nav-open .mnav{opacity:1;visibility:visible}
.mnav a{font-size:clamp(2.2rem,10vw,4rem);font-weight:900;text-transform:uppercase;letter-spacing:-.04em;
  line-height:1.02;border-bottom:2px solid var(--ink);padding:10px 0;opacity:0;transform:translateX(-24px);
  transition:.5s cubic-bezier(.16,1,.3,1)}
body.nav-open .mnav a{opacity:1;transform:none}
.mnav a:nth-child(1){transition-delay:.04s}.mnav a:nth-child(2){transition-delay:.09s}
.mnav a:nth-child(3){transition-delay:.14s}.mnav a:nth-child(4){transition-delay:.19s}
.mnav a:nth-child(5){transition-delay:.24s}
.mnav__foot{margin-top:24px;font-family:var(--font-mono);font-size:13px;display:grid;gap:5px}

/* Герой */
.hero{padding-top:64px;border-top:2px solid var(--line)}
.hero__type{padding:clamp(28px,4vw,54px) 0 0}
.hero__meta{display:grid;gap:16px;padding:22px 0;border-top:2px solid var(--line);
  border-bottom:2px solid var(--line);margin-top:clamp(22px,3vw,34px)}
@media(min-width:800px){.hero__meta{grid-template-columns:repeat(4,1fr);gap:0}
  .hero__meta>div{padding-right:20px;border-right:1px solid var(--hair)}
  .hero__meta>div:last-child{border:0}}
.hero__meta b{display:block;font-size:clamp(1.5rem,2.6vw,2.2rem);font-weight:800;letter-spacing:-.04em}
.hero__meta span{font-family:var(--font-mono);font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
.hero__img{margin-top:0;border-bottom:2px solid var(--line);overflow:hidden;aspect-ratio:21/9;position:relative}
@media(max-width:700px){.hero__img{aspect-ratio:4/3}}
.hero__img img{width:100%;height:100%;object-fit:cover;filter:grayscale(1) contrast(1.12);
  transition:filter .9s,transform 1.4s cubic-bezier(.16,1,.3,1);transform:scale(1.08)}
.hero__img:hover img{filter:none;transform:scale(1.02)}
.hero__acts{display:flex;flex-wrap:wrap;gap:0;border-bottom:2px solid var(--line)}
.hero__acts .btn{flex:1;border:0;border-right:2px solid var(--line);padding:22px 20px;min-width:200px}
.hero__acts .btn:last-child{border-right:0}

/* Бегущая строка */
.band{background:var(--accent);border-block:2px solid var(--line);padding:14px 0;--mq-gap:0}
.band .marquee__track{--mq-dur:26s}
.band span{display:flex;align-items:center;gap:20px;padding-right:20px;white-space:nowrap;
  font-weight:900;font-size:clamp(1.1rem,2.2vw,1.8rem);text-transform:uppercase;letter-spacing:-.03em}
.band em{font-style:normal;font-size:.8em}
.band--dark{background:var(--ink);color:var(--bg)}

/* Проекты — строки-каталог */
.rows{border-top:2px solid var(--line)}
.row{display:grid;grid-template-columns:auto 1fr auto;gap:16px;align-items:center;
  padding:22px 6px;border-bottom:2px solid var(--line);position:relative;overflow:hidden;
  transition:padding-left .45s cubic-bezier(.16,1,.3,1),color .35s}
.row::before{content:"";position:absolute;inset:0;background:var(--accent);transform:translateY(101%);
  transition:transform .45s cubic-bezier(.16,1,.3,1);z-index:-1}
.row:hover::before{transform:none}
.row:hover{padding-left:22px}
.row__n{font-family:var(--font-mono);font-size:12px}
.row__t{display:block}
.row__t h3{font-size:clamp(1.3rem,3.4vw,2.6rem);font-weight:900;letter-spacing:-.04em;text-transform:uppercase;line-height:.95}
.row__t p{font-size:14px;color:var(--muted);margin-top:6px;max-width:48ch}
.row:hover .row__t p{color:var(--ink)}
.row__p{display:block;text-align:right}
.row__p b{display:block;font-size:clamp(1.05rem,2vw,1.5rem);font-weight:800;letter-spacing:-.03em;white-space:nowrap}
.row__p span{font-family:var(--font-mono);font-size:10px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
.row__th{position:fixed;z-index:60;width:280px;aspect-ratio:4/3;pointer-events:none;opacity:0;
  transform:translate(-50%,-50%) scale(.92) rotate(-3deg);border:2px solid var(--line);
  transition:opacity .3s,transform .5s cubic-bezier(.16,1,.3,1)}
.row__th.on{opacity:1;transform:translate(-50%,-50%) scale(1) rotate(-2deg)}
.row__th img{width:100%;height:100%;object-fit:cover}
@media(max-width:900px){.row__th{display:none}.row{grid-template-columns:1fr auto}.row__n{display:none}}

/* Плитки-планировки */
.grid4{display:grid;gap:0;border-left:2px solid var(--line);border-top:2px solid var(--line)}
@media(min-width:560px){.grid4{grid-template-columns:repeat(2,1fr)}}
@media(min-width:960px){.grid4{grid-template-columns:repeat(4,1fr)}}
.cell{border-right:2px solid var(--line);border-bottom:2px solid var(--line);background:var(--bg-2);
  cursor:zoom-in;transition:background .35s}
.cell:hover{background:var(--accent)}
.cell__i{aspect-ratio:1/1;padding:14px;background:#fff;overflow:hidden}
.cell__i img{width:100%;height:100%;object-fit:contain;transition:transform .7s cubic-bezier(.16,1,.3,1)}
.cell:hover .cell__i img{transform:scale(1.07)}
.cell__b{padding:16px;border-top:2px solid var(--line);display:grid;gap:5px}
.cell__b h4{font-size:14px;font-weight:800;text-transform:uppercase;letter-spacing:-.02em}
.cell__b .m{font-family:var(--font-mono);font-size:11px;color:var(--muted)}
.cell__b .p{font-size:15px;font-weight:800;letter-spacing:-.02em}
.tabs{display:flex;flex-wrap:wrap;gap:0;margin-bottom:0;border:2px solid var(--line);border-bottom:0}
.tabs button{flex:1;min-width:150px;padding:16px 18px;font-family:var(--font-mono);font-size:11px;
  letter-spacing:.14em;text-transform:uppercase;border-right:2px solid var(--line);transition:.3s}
.tabs button:last-child{border-right:0}
.tabs button.active{background:var(--ink);color:var(--bg)}
.tabs button:not(.active):hover{background:var(--accent)}

/* Комплектация */
.spec{display:grid;border-top:2px solid var(--line);border-left:2px solid var(--line)}
@media(min-width:1000px){.spec{grid-template-columns:1.45fr .8fr .8fr}}
.spec__c{border-right:2px solid var(--line);border-bottom:2px solid var(--line);padding:28px 22px;background:var(--bg-2)}
.spec__c h3{margin-bottom:18px}
.spec__c li{display:flex;gap:10px;padding:8px 0;font-size:14.5px;border-bottom:1px solid var(--hair);line-height:1.5}
.spec__c li:last-child{border:0}
.spec__c .mono{flex:0 0 auto;color:var(--muted)}
.spec--y{background:var(--accent)}

/* Процесс */
.pr{border-top:2px solid var(--line)}
.pstep{display:grid;gap:20px;padding:clamp(26px,4vw,46px) 0;border-bottom:2px solid var(--line);align-items:start}
@media(min-width:900px){.pstep{grid-template-columns:100px 1fr 1fr;gap:38px}}
.pstep__n{font-size:clamp(2.4rem,5vw,4.4rem);font-weight:900;letter-spacing:-.05em;line-height:.8;
  -webkit-text-stroke:2px var(--ink);color:transparent;transition:color .5s}
.pstep:hover .pstep__n{color:var(--accent)}
.pstep h3{margin-bottom:12px}
.pstep p{font-size:15px;color:var(--muted);line-height:1.65}
.pstep__i{overflow:hidden;aspect-ratio:16/10;border:2px solid var(--line)}
.pstep__i img{width:100%;height:100%;object-fit:cover;filter:grayscale(1) contrast(1.08);
  transition:filter .7s,transform 1.2s cubic-bezier(.16,1,.3,1)}
.pstep:hover .pstep__i img{filter:none;transform:scale(1.05)}

/* Мозаика */
.mos{display:grid;grid-template-columns:repeat(2,1fr);border-left:2px solid var(--line);border-top:2px solid var(--line)}
@media(min-width:900px){.mos{grid-template-columns:repeat(3,1fr)}
  .mos--d figure:nth-child(7){grid-column:span 2;aspect-ratio:2/1}}
.mos figure{margin:0;position:relative;border-right:2px solid var(--line);border-bottom:2px solid var(--line);
  aspect-ratio:1/1;overflow:hidden;cursor:zoom-in}
.mos img{width:100%;height:100%;object-fit:cover;filter:grayscale(1) contrast(1.06);
  transition:filter .7s,transform 1.2s cubic-bezier(.16,1,.3,1)}
.mos figure:hover img{filter:none;transform:scale(1.06)}
.mos figcaption{position:absolute;inset:auto 0 0 0;background:var(--accent);border-top:2px solid var(--line);
  padding:12px 14px;font-family:var(--font-mono);font-size:11px;line-height:1.4;
  transform:translateY(101%);transition:transform .4s cubic-bezier(.16,1,.3,1)}
.mos figure:hover figcaption{transform:none}

/* Объекты */
.objs{display:grid;border-top:2px solid var(--line);border-left:2px solid var(--line)}
@media(min-width:800px){.objs{grid-template-columns:repeat(2,1fr)}}
.obj{display:block;border-right:2px solid var(--line);border-bottom:2px solid var(--line);position:relative;overflow:hidden}
.obj__i{display:block;aspect-ratio:4/3;overflow:hidden}
.obj img{width:100%;height:100%;object-fit:cover;filter:grayscale(1) contrast(1.08);
  transition:filter .7s,transform 1.3s cubic-bezier(.16,1,.3,1)}
.obj:hover img{filter:none;transform:scale(1.05)}
.obj__c{display:block;padding:20px;border-top:2px solid var(--line);background:var(--bg-2);transition:background .35s}
.obj:hover .obj__c{background:var(--accent)}
.obj__c h3{font-size:clamp(1.2rem,2.4vw,1.8rem);font-weight:900;text-transform:uppercase;letter-spacing:-.03em}
.obj__c p{font-size:14px;color:var(--muted);margin-top:5px}
.obj:hover .obj__c p{color:var(--ink)}

/* До/после */
.ba{border:2px solid var(--line);border-radius:0}
.ba-wrap{display:grid;gap:30px;align-items:center}
@media(min-width:1000px){.ba-wrap{grid-template-columns:.8fr 1.2fr;gap:50px}}

/* Заявка */
.cta{background:var(--ink);color:var(--bg);--muted:rgba(242,240,235,.65);--fg:#F2F0EB;
  --line:#F2F0EB;--hair:rgba(242,240,235,.2);--input-bg:rgba(255,255,255,.06)}
.cta .btn{border-color:var(--accent);color:var(--accent)}
.cta .btn::before{background:var(--accent)}
.cta .btn:hover{color:var(--ink)}
.cta__in{display:grid;gap:34px}
@media(min-width:960px){.cta__in{grid-template-columns:1fr 1fr;gap:60px;align-items:center}}
.cta form{display:grid;gap:14px}
.cta .field input,.cta .field textarea{border:2px solid rgba(242,240,235,.3)}
.cta .tag{background:var(--accent);color:var(--ink)}

/* Подвал */
.foot{border-top:2px solid var(--line);padding:52px 0 28px}
.foot__grid{display:grid;gap:30px}
@media(min-width:800px){.foot__grid{grid-template-columns:1.5fr 1fr 1fr 1fr}}
.foot h4{font-family:var(--font-mono);font-size:11px;letter-spacing:.14em;text-transform:uppercase;margin-bottom:14px}
.foot p{font-size:15px;margin-bottom:8px}
.foot a{border-bottom:1px solid transparent;transition:border-color .3s}
.foot a:hover{border-color:var(--ink)}
.foot__big{font-size:clamp(3.5rem,20vw,17rem);font-weight:900;letter-spacing:-.06em;line-height:.75;
  margin-top:44px;text-align:center;user-select:none;overflow:hidden}
.foot__big span{display:block;transform:translateY(101%);transition:transform 1.1s cubic-bezier(.16,1,.3,1)}
.foot__big.in span{transform:none}
.foot__bot{margin-top:34px;padding-top:18px;border-top:2px solid var(--line);display:flex;flex-wrap:wrap;
  gap:12px;justify-content:space-between;font-family:var(--font-mono);font-size:11px;color:var(--muted)}
"""

ARR = '<svg width="18" height="10" viewBox="0 0 18 10" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M0 5h16M12 1l4 4-4 4"/></svg>'

def build():
    b = BRAND
    nav = "".join(f'<a href="{h}">{t}</a>' for h, t in NAV)
    o = [core.head("ДОММ — модульные дома под ключ | Новосибирск",
                   "Модульные дома с террасой от 990 000 ₽ за 30 дней. Собственное производство в Новосибирске, 80+ реализованных проектов.",
                   FONTS, CSS, "#F2F0EB")]
    o.append('<div class="grain"></div><div class="cursor"></div>')
    o.append(f"""
<header class="hdr" data-header><div class="wrap hdr__in">
  <a class="logo" href="#top"><i></i>ДОММ</a>
  <div style="display:flex;margin-right:calc(var(--gutter) * -1)">
    <nav class="nav">{nav}</nav>
    <a class="btn hdr__cta" href="tel:{b['phone2_href']}">Заказать расчёт</a>
    <button class="burger" data-burger aria-label="Меню" aria-expanded="false"><i></i><i></i><i></i></button>
  </div>
</div></header>
<nav class="mnav" data-menu>{nav}
  <div class="mnav__foot"><a href="tel:{b['phone1_href']}">{b['phone1']}</a>
  <a href="tel:{b['phone2_href']}">{b['phone2']}</a><a href="mailto:{b['email']}">{b['email']}</a></div>
</nav>""")

    meta = "".join(f'<div><b>{v}</b><span>{t}</span></div>' for v, t in STATS)
    o.append(f"""
<section class="hero" id="top">
  <div class="wrap hero__type">
    <span class="tag" data-rv="up">{HERO['kicker']}</span>
    <h1 class="h1" style="margin-top:18px" data-split="line">Модульные дома<br><span class="hl">для жизни</span><br>и отдыха</h1>
    <div class="hero__meta" data-stagger="80">{meta}</div>
  </div>
  <div class="hero__img" data-rv="mask"><img src="{HERO['bg']}" alt="Модульный дом ДОММ с террасой"></div>
  <div class="wrap"><div class="hero__acts">
    <a class="btn btn--fill" href="#projects" data-magnet=".25">Смотреть проекты {ARR}</a>
    <a class="btn" href="{b['wa']}" target="_blank" rel="noopener" data-magnet=".25">Написать в WhatsApp</a>
    <a class="btn" href="tel:{b['phone2_href']}" data-magnet=".25">{b['phone2']}</a>
  </div></div>
</section>""")

    band = "".join(f'<span>{HERO["sub"].upper()}<em>◆</em></span>' for _ in range(3))
    o.append(f'<section class="band"><div class="marquee"><div class="marquee__track">{band}</div>'
             f'<div class="marquee__track" aria-hidden="true">{band}</div></div></section>')

    figs = "".join(f'<figure data-lb="g" data-full="{u}" data-cap="Дом ДОММ"><img src="{u}" alt="Модульный дом ДОММ" loading="lazy"><figcaption>ФОТО {i+1:02d} / ОБЪЕКТ ДОММ</figcaption></figure>'
                   for i, u in enumerate(GALLERY[:9]))
    o.append(f"""
<section class="sec" id="gallery" style="border-top:0">
  <div class="wrap sec-head split">
    <div data-rv="up"><span class="tag">Галерея</span>
      <h2 class="h2" style="margin-top:16px" data-split="line">Декорируем дома<br>в уютном стиле</h2></div>
    <p class="lead" data-rv="up" style="--d:150ms">Тёплое дерево, чёрная фурнитура, панорамные окна.
    Наведите на снимок — цвет вернётся. Нажмите — откроется крупно.</p>
  </div>
  <div class="wrap"><div class="mos" data-stagger="60">{figs}</div></div>
</section>""")

    rows = "".join(f"""
    <a class="row" href="#cta" data-th="{im}">
      <span class="row__n">{i+1:02d}</span>
      <span class="row__t"><h3>{n}</h3><p>{d}</p></span>
      <span class="row__p"><b>от {p} ₽</b><span>{area} · под ключ</span></span>
    </a>""" for i, (n, d, p, area, im) in enumerate(PROJECTS))
    o.append(f"""
<section class="sec" id="projects"><div class="wrap">
  <div class="sec-head split">
    <div data-rv="up"><span class="tag">Каталог</span>
      <h2 class="h2" style="margin-top:16px" data-split="line">Проекты<br>домов и бань</h2></div>
    <p class="lead" data-rv="up" style="--d:150ms">Семь базовых моделей и две бани.
    Любую планировку адаптируем под ваш участок.</p>
  </div>
  <div class="rows" data-stagger="70" data-rv-child="left">{rows}</div>
</div>
<div class="row__th"><img src="" alt=""></div>
</section>""")

    def cells(items, key):
        return "".join(f"""
      <article class="cell" data-lb="{key}" data-full="{im}" data-cap="{n} — {a}, от {p} тыс. ₽">
        <div class="cell__i"><img src="{im}" alt="Планировка {n}" loading="lazy"></div>
        <div class="cell__b"><h4>{n}</h4><span class="m">{a}{' · ' + note if note else ''}</span>
          <span class="p">от {p} тыс. ₽</span></div></article>""" for n, a, p, im, note in items)
    rend = "".join(f"""
      <article class="cell" data-lb="rn" data-full="{im}" data-cap="{n}">
        <div class="cell__i" style="padding:0;aspect-ratio:4/3"><img src="{im}" alt="{n}" style="object-fit:cover" loading="lazy"></div>
        <div class="cell__b"><h4>{n}</h4><span class="m">{d}</span></div></article>""" for n, d, im in RENDERS)
    o.append(f"""
<section class="sec" id="prices"><div class="wrap" data-tabs>
  <div class="sec-head split">
    <div data-rv="up"><span class="tag">Планировки и цены</span>
      <h2 class="h2" style="margin-top:16px" data-split="line">Выберите<br>свой метраж</h2></div>
    <p class="lead" data-rv="up" style="--d:150ms">Дома собираются из модулей 2,5×6 м и 3×6 м.
    Нажмите на планировку, чтобы открыть её крупно.</p>
  </div>
  <div class="tabs" role="tablist">
    <button data-tab="a" class="active" role="tab" aria-selected="true">Модули 2,5 × 6</button>
    <button data-tab="b" role="tab" aria-selected="false">Модули 3 × 6</button>
    <button data-tab="c" role="tab" aria-selected="false">Визуализации</button>
  </div>
  <div class="grid4" data-panel="a" data-stagger="50">{cells(PLANS_25,'p25')}</div>
  <div class="grid4" data-panel="b" hidden data-stagger="50">{cells(PLANS_36,'p36')}</div>
  <div class="grid4" data-panel="c" hidden data-stagger="50">{rend}</div>
</div></section>""")

    def li(items, sign):
        return "".join(f'<li><span class="mono">{sign}</span><span>{t}</span></li>' for t in items)
    o.append(f"""
<section class="sec" id="spec"><div class="wrap">
  <div class="sec-head split">
    <div data-rv="up"><span class="tag">Комплектация</span>
      <h2 class="h2" style="margin-top:16px" data-split="line">Что входит<br>в стоимость</h2></div>
    <p class="lead" data-rv="up" style="--d:150ms">Честный список без звёздочек: что вы получаете сразу,
    что оплачивается отдельно и что можно добавить.</p>
  </div>
  <div class="spec" data-stagger="110">
    <div class="spec__c spec--y"><h3 class="h3">Входит</h3><ul>{li(INCLUDED,'+')}</ul></div>
    <div class="spec__c"><h3 class="h3">Не входит</h3><ul>{li(EXCLUDED,'—')}</ul></div>
    <div class="spec__c"><h3 class="h3">Опции</h3><ul>{li(OPTIONS,'★')}</ul></div>
  </div>
</div></section>""")

    band2 = "".join('<span>30 ДНЕЙ ПРОИЗВОДСТВО<em>◆</em>1 ДЕНЬ МОНТАЖ<em>◆</em>80+ ПРОЕКТОВ<em>◆</em></span>' for _ in range(2))
    o.append(f'<section class="band band--dark"><div class="marquee"><div class="marquee__track">{band2}</div>'
             f'<div class="marquee__track" aria-hidden="true">{band2}</div></div></section>')

    steps = "".join(f"""
    <article class="pstep">
      <div class="pstep__n" data-rv="up">{n}</div>
      <div data-rv="up" style="--d:80ms"><h3 class="h3">{t}</h3><p>{d}</p></div>
      <div class="pstep__i" data-rv="mask" style="--d:140ms"><img src="{im}" alt="{t}" loading="lazy"></div>
    </article>""" for n, t, d, im in PROCESS)
    o.append(f"""
<section class="sec" id="process" style="border-top:0"><div class="wrap">
  <div class="sec-head" data-rv="up"><span class="tag">Как мы работаем</span>
    <h2 class="h2" style="margin-top:16px">Четыре шага до новоселья</h2></div>
  <div class="pr">{steps}</div>
</div></section>""")

    mos = "".join(f'<figure data-lb="d" data-full="{im}" data-cap="{t}"><img src="{im}" alt="{t}" loading="lazy"><figcaption>{t}</figcaption></figure>'
                  for t, im in DETAILS + INTERIOR)
    o.append(f"""
<section class="sec" id="details"><div class="wrap">
  <div class="sec-head split">
    <div data-rv="up"><span class="tag">Black Paket</span>
      <h2 class="h2" style="margin-top:16px" data-split="line">Детали в едином<br>чёрном стиле</h2></div>
    <p class="lead" data-rv="up" style="--d:150ms">Электрощит, розетки, выключатели, светильники и ручки —
    одно оформление без визуального шума.</p>
  </div>
  <div class="mos mos--d" data-stagger="60">{mos}</div>
</div></section>""")

    objs = "".join(f"""
    <a class="obj" href="#cta"><span class="obj__i"><img src="{im}" alt="{t}" loading="lazy"></span>
      <span class="obj__c"><h3>{t}</h3><p>{d}</p></span></a>""" for t, d, im in OBJECTS)
    o.append(f"""
<section class="sec" id="objects"><div class="wrap">
  <div class="sec-head" data-rv="up"><span class="tag">Наши дома</span>
    <h2 class="h2" style="margin-top:16px">Реализованные объекты</h2></div>
  <div class="objs" data-stagger="80">{objs}</div>
</div></section>""")

    o.append(f"""
<section class="sec"><div class="wrap ba-wrap">
  <div data-rv="up"><span class="tag">Посмотрите разницу</span>
    <h2 class="h2" style="margin:16px 0 16px" data-split="line">Ваш дом у нас —<br>ваш дом у вас</h2>
    <p class="lead">Слева — модуль на производстве, справа — тот же дом на участке. Потяните ползунок.</p></div>
  <div class="ba" data-rv="zoom" role="img" aria-label="Сравнение: дом на производстве и на участке">
    <img src="{BEFORE}" alt="Модуль на производстве" loading="lazy">
    <img class="ba__after" src="{AFTER}" alt="Готовый дом на участке" loading="lazy">
    <span class="ba__line"></span><span class="ba__grip">&#8596;</span>
    <span class="ba__tag l">Ваш дом у нас</span><span class="ba__tag r">Ваш дом у вас</span>
  </div>
</div></section>""")

    o.append(f"""
<section class="sec cta" id="cta"><div class="wrap cta__in">
  <div data-rv="up">
    <span class="tag">Свяжитесь с нами</span>
    <h2 class="h2" style="margin:16px 0 16px">Оставьте заявку<br>и получите расчёт</h2>
    <p class="lead">Подберём планировку под участок и посчитаем стоимость с доставкой и монтажом.</p>
    <div style="margin-top:24px;display:grid;gap:6px;font-size:1.6rem;font-weight:800;letter-spacing:-.04em">
      <a href="tel:{b['phone1_href']}">{b['phone1']}</a><a href="tel:{b['phone2_href']}">{b['phone2']}</a>
    </div>
  </div>
  <form data-form data-rv="up" style="--d:150ms" novalidate>
    <div class="f-row two">
      <div class="field"><label for="n4">Ваше имя</label>
        <input id="n4" type="text" required autocomplete="name" placeholder="Иван"><span class="err">Укажите имя</span></div>
      <div class="field"><label for="t4">Телефон</label>
        <input id="t4" type="tel" required autocomplete="tel" inputmode="tel" placeholder="+7 (___) ___-__-__">
        <span class="err">Введите номер полностью</span></div>
    </div>
    <div class="field"><label for="m4">Комментарий</label>
      <textarea id="m4" rows="3" placeholder="Интересует MODUL HOUSE 3, участок в Бердске"></textarea></div>
    <button class="btn" type="submit" data-magnet=".2" style="justify-self:start">Отправить заявку {ARR}</button>
    <p class="form-note">Нажимая кнопку, вы соглашаетесь с обработкой персональных данных.</p>
    <div class="form-ok" role="status">Спасибо! Заявка принята — мы перезвоним в рабочее время.</div>
  </form>
</div></section>""")

    o.append(f"""
<footer class="foot" id="contacts"><div class="wrap">
  <div class="foot__grid">
    <div data-rv="up"><a class="logo" href="#top"><i></i>ДОММ</a>
      <p class="lead" style="margin-top:12px;font-size:15px">Производство и продажа модульных домов
      под ключ в Новосибирске и по России.</p></div>
    <div data-rv="up" style="--d:80ms"><h4>Телефоны</h4>
      <p><a href="tel:{b['phone1_href']}">{b['phone1']}</a></p>
      <p><a href="tel:{b['phone2_href']}">{b['phone2']}</a></p>
      <p><a href="mailto:{b['email']}">{b['email']}</a></p></div>
    <div data-rv="up" style="--d:160ms"><h4>Адреса</h4>
      <p>Офис — г. {b['city']}</p><p>Производство — г. {b['city']}</p>
      <p>{b['hours']}</p><p>{b['hours2']}</p></div>
    <div data-rv="up" style="--d:240ms"><h4>Соцсети</h4>
      <p><a href="{b['vk']}" target="_blank" rel="noopener">ВКонтакте</a></p>
      <p>Instagram: {b['inst']}</p><p><a href="{b['wa']}" target="_blank" rel="noopener">WhatsApp</a></p></div>
  </div>
  <div class="foot__big" data-rv="up" aria-hidden="true"><span>ДОММ</span></div>
  <div class="foot__bot"><span>© <span data-year></span> ДОММ. Модульные дома.</span><span>Новосибирск</span></div>
</div></footer>""")

    o.append(core.dock(b))

    extra = r"""
/* Превью проекта у курсора */
(function(){
  var th = document.querySelector('.row__th');
  if(!th || !window.matchMedia('(hover:hover)').matches) return;
  var im = th.querySelector('img');
  document.querySelectorAll('[data-th]').forEach(function(r){
    r.addEventListener('pointerenter', function(){ im.src = r.dataset.th; th.classList.add('on'); });
    r.addEventListener('pointerleave', function(){ th.classList.remove('on'); });
    r.addEventListener('pointermove', function(e){
      th.style.left = e.clientX + 'px';
      th.style.top = Math.max(130, Math.min(window.innerHeight-130, e.clientY)) + 'px';
    });
  });
})();
"""
    o.append(core.tail(extra))
    return "".join(o)
