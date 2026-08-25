# -*- coding: utf-8 -*-
"""Вариант 3 — BENTO TECH. Бенто-сетка, тёмный графит, лаймовый акцент, калькулятор."""
import core
from data import *

FONTS = '<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">'

CSS = r"""
:root{
  --bg:#0E0F10; --bg-2:#16181A; --bg-3:#1D2023; --fg:#F2F4F3; --muted:#8B9199;
  --line:rgba(242,244,243,.1); --accent:#C6F24E; --accent-2:#FF7A3D; --on-accent:#0E0F10;
  --input-bg:rgba(255,255,255,.04);
  --font-head:'Space Grotesk',system-ui,sans-serif; --font-body:'Inter',system-ui,sans-serif;
  --radius:20px; --radius-sm:12px; --head-weight:600;
}
::selection{background:var(--accent);color:var(--on-accent)}
.h1{font-family:var(--font-head);font-size:clamp(2.5rem,6.6vw,5.6rem);line-height:.96;letter-spacing:-.035em;font-weight:600}
.h2{font-family:var(--font-head);font-size:clamp(1.9rem,4.2vw,3.4rem);line-height:1.02;letter-spacing:-.03em;font-weight:600}
.h3{font-family:var(--font-head);font-size:clamp(1.1rem,1.9vw,1.45rem);font-weight:600;letter-spacing:-.02em}
.mono{font-family:var(--font-head);font-size:11px;letter-spacing:.2em;text-transform:uppercase}
.kicker{display:inline-flex;align-items:center;gap:9px;font-family:var(--font-head);font-size:11px;
  letter-spacing:.2em;text-transform:uppercase;color:var(--accent);max-width:100%;flex-wrap:wrap}
.kicker i{width:7px;height:7px;border-radius:50%;background:var(--accent);animation:pulse 2.2s ease-in-out infinite}
@keyframes pulse{0%,100%{box-shadow:0 0 0 0 rgba(198,242,78,.5)}50%{box-shadow:0 0 0 8px rgba(198,242,78,0)}}
.lead{color:var(--muted);font-size:clamp(1rem,1.25vw,1.1rem);max-width:60ch;line-height:1.65}
.sec{padding:clamp(66px,8vw,120px) 0}
.sec-head{display:grid;gap:20px;margin-bottom:clamp(32px,4vw,56px)}
@media(min-width:900px){.sec-head.split{grid-template-columns:1.1fr .9fr;align-items:end;gap:48px}}

/* Сетка бенто */
.bento{display:grid;gap:14px;grid-template-columns:repeat(2,1fr)}
@media(min-width:900px){.bento{grid-template-columns:repeat(4,1fr);gap:16px}}
.box{background:var(--bg-2);border:1px solid var(--line);border-radius:var(--radius);padding:26px;
  position:relative;overflow:hidden;transition:border-color .45s,transform .55s cubic-bezier(.16,1,.3,1),background .45s}
.box::before{content:"";position:absolute;inset:0;opacity:0;transition:opacity .45s;pointer-events:none;
  background:radial-gradient(420px circle at var(--mx,50%) var(--my,50%),rgba(198,242,78,.12),transparent 62%)}
.box:hover{border-color:rgba(198,242,78,.4);transform:translateY(-4px)}
.box:hover::before{opacity:1}
.box--img{padding:0}
.box--img img{width:100%;height:100%;object-fit:cover;transition:transform 1.2s cubic-bezier(.16,1,.3,1)}
.box--img:hover img{transform:scale(1.06)}
.box--accent{background:var(--accent);color:var(--on-accent);border-color:var(--accent)}
.box--accent .lead{color:rgba(14,15,16,.72)}
.sp2{grid-column:span 2}
@media(min-width:900px){.sp3{grid-column:span 3}.sp4{grid-column:span 4}.r2{grid-row:span 2}}

/* Шапка */
.hdr{position:fixed;inset:12px 12px auto 12px;z-index:100;transition:.5s cubic-bezier(.16,1,.3,1)}
.hdr__in{display:flex;align-items:center;justify-content:space-between;gap:18px;padding:12px 14px 12px 22px;
  border-radius:100px;border:1px solid transparent;transition:.5s cubic-bezier(.16,1,.3,1)}
.hdr.stuck .hdr__in{background:rgba(22,24,26,.78);backdrop-filter:blur(20px) saturate(150%);border-color:var(--line)}
.hdr.hide{transform:translateY(-140%)}
.logo{font-family:var(--font-head);font-weight:700;font-size:19px;letter-spacing:-.02em;display:flex;align-items:center;gap:9px}
.logo i{width:9px;height:9px;background:var(--accent);border-radius:2px;display:block;
  animation:spin 6s linear infinite}
@keyframes spin{to{transform:rotate(180deg)}}
.nav{display:none;gap:6px}
@media(min-width:1024px){.nav{display:flex}}
.nav a{font-size:13px;color:var(--muted);padding:9px 15px;border-radius:100px;transition:.3s}
.nav a:hover{color:var(--fg);background:rgba(255,255,255,.06)}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:9px;padding:14px 24px;border-radius:100px;
  font-family:var(--font-head);font-size:13px;font-weight:600;letter-spacing:-.01em;position:relative;overflow:hidden;
  isolation:isolate;transform:translate3d(var(--tx,0),var(--ty,0),0);
  transition:transform .4s cubic-bezier(.16,1,.3,1),box-shadow .35s,color .3s}
.btn--fill{background:var(--accent);color:var(--on-accent);box-shadow:0 0 0 rgba(198,242,78,0)}
.btn--fill:hover{box-shadow:0 10px 40px rgba(198,242,78,.32)}
.btn--fill::before{content:"";position:absolute;inset:0;z-index:-1;background:#fff;border-radius:inherit;
  transform:scale(0);transition:transform .5s cubic-bezier(.16,1,.3,1)}
.btn--fill:hover::before{transform:scale(1.05)}
.btn--ghost{border:1px solid var(--line);color:var(--fg)}
.btn--ghost:hover{border-color:var(--accent);color:var(--accent)}
.hdr__cta{display:none;padding:12px 20px}@media(min-width:640px){.hdr__cta{display:inline-flex}}
.burger{display:grid;gap:5px;padding:10px;margin:-4px}
@media(min-width:1024px){.burger{display:none}}
.burger i{width:20px;height:2px;background:var(--fg);border-radius:2px;transition:.4s}
body.nav-open .burger i:nth-child(1){transform:translateY(7px) rotate(45deg)}
body.nav-open .burger i:nth-child(2){opacity:0}
body.nav-open .burger i:nth-child(3){transform:translateY(-7px) rotate(-45deg)}
.mnav{position:fixed;inset:0;z-index:99;background:var(--bg);display:grid;align-content:center;gap:4px;
  padding:0 var(--gutter);opacity:0;visibility:hidden;transition:.45s}
body.nav-open .mnav{opacity:1;visibility:visible}
.mnav a{font-family:var(--font-head);font-size:clamp(2rem,9vw,3.2rem);font-weight:600;letter-spacing:-.03em;
  opacity:0;transform:translateY(18px);transition:.55s cubic-bezier(.16,1,.3,1)}
body.nav-open .mnav a{opacity:1;transform:none}
.mnav a:nth-child(1){transition-delay:.05s}.mnav a:nth-child(2){transition-delay:.1s}
.mnav a:nth-child(3){transition-delay:.15s}.mnav a:nth-child(4){transition-delay:.2s}
.mnav a:nth-child(5){transition-delay:.25s}
.mnav__foot{margin-top:26px;display:grid;gap:6px;color:var(--muted)}

/* Герой-бенто */
.hero{padding:104px 0 0}
.hero__main{position:relative;min-height:min(76svh,640px);display:flex;align-items:flex-end;
  border-radius:var(--radius);overflow:hidden;padding:clamp(22px,3vw,42px)}
.hero__main .h1{font-size:clamp(2.1rem,5.2vw,4.6rem)}
.hero__main img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;
  animation:ken 24s ease-in-out infinite alternate}
@keyframes ken{from{transform:scale(1.05)}to{transform:scale(1.18)}}
.hero__main::after{content:"";position:absolute;inset:0;
  background:linear-gradient(180deg,rgba(14,15,16,.62),rgba(14,15,16,.15) 40%,rgba(14,15,16,.9))}
.hero__c{position:relative;z-index:2;max-width:min(56ch,100%)}
.hero__c .lead{margin-top:16px}
.hero__acts{display:flex;gap:12px;flex-wrap:wrap;margin-top:24px}
.stat b{display:block;font-family:var(--font-head);font-size:clamp(2rem,3.4vw,2.9rem);
  letter-spacing:-.04em;font-weight:600}
.stat span{color:var(--muted);font-size:13px}
.box--accent .stat span{color:rgba(14,15,16,.7)}

/* Модульная диаграмма */
.mods{display:flex;gap:6px;align-items:flex-end;height:96px;margin-top:18px}
.mods i{display:block;flex:1;background:var(--bg-3);border:1px solid var(--line);border-radius:8px;
  transform-origin:50% 100%;transform:scaleY(.15);opacity:.35;
  transition:transform .8s cubic-bezier(.16,1,.3,1),opacity .8s,background .5s}
.mods i:nth-child(1){height:52%}.mods i:nth-child(2){height:74%}.mods i:nth-child(3){height:100%}
.mods i:nth-child(4){height:80%}.mods i:nth-child(5){height:58%}
.in .mods i{transform:scaleY(1);opacity:1;background:linear-gradient(180deg,var(--bg-3),var(--bg-2))}
.in .mods i:nth-child(1){transition-delay:.05s}.in .mods i:nth-child(2){transition-delay:.15s}
.in .mods i:nth-child(3){transition-delay:.25s}.in .mods i:nth-child(4){transition-delay:.35s}
.in .mods i:nth-child(5){transition-delay:.45s}
.in .mods i:nth-child(3){background:var(--accent);border-color:var(--accent)}

/* Калькулятор */
.calc{display:grid;gap:26px}
@media(min-width:960px){.calc{grid-template-columns:1.1fr .9fr;gap:36px}}
.calc__panel{background:var(--bg-2);border:1px solid var(--line);border-radius:var(--radius);padding:clamp(24px,3vw,36px)}
.calc__group{margin-bottom:26px}
.calc__group>.mono{color:var(--muted);display:block;margin-bottom:12px}
.chips{display:flex;flex-wrap:wrap;gap:8px}
.chip{padding:11px 16px;border:1px solid var(--line);border-radius:100px;font-size:13px;color:var(--muted);
  transition:.3s;background:transparent}
.chip:hover{color:var(--fg);border-color:var(--muted)}
.chip.on{background:var(--accent);color:var(--on-accent);border-color:var(--accent)}
.opt{display:flex;align-items:center;gap:12px;padding:13px 0;border-bottom:1px solid var(--line);cursor:pointer}
.opt:last-child{border:0}
.opt input{position:absolute;opacity:0;pointer-events:none}
.opt .bx{width:22px;height:22px;border-radius:7px;border:1px solid var(--line);flex:0 0 22px;
  display:grid;place-items:center;transition:.3s}
.opt .bx svg{opacity:0;transform:scale(.6);transition:.3s}
.opt input:checked + .bx{background:var(--accent);border-color:var(--accent)}
.opt input:checked + .bx svg{opacity:1;transform:none;color:var(--on-accent)}
.opt input:focus-visible + .bx{outline:2px solid var(--accent);outline-offset:3px}
.opt span{font-size:14.5px;flex:1}
.opt b{font-size:14px;color:var(--muted);font-weight:500;white-space:nowrap}
.calc__sum{background:linear-gradient(160deg,var(--bg-3),var(--bg-2));border:1px solid var(--line);
  border-radius:var(--radius);padding:clamp(24px,3vw,34px);position:sticky;top:96px}
.calc__total{font-family:var(--font-head);font-size:clamp(2.2rem,5vw,3.4rem);font-weight:600;
  letter-spacing:-.04em;color:var(--accent);margin:6px 0 4px}
.calc__rows{margin:22px 0;display:grid;gap:9px}
.calc__rows div{display:flex;justify-content:space-between;gap:12px;font-size:14px;color:var(--muted)}
.calc__rows b{color:var(--fg);font-weight:500;text-align:right}
.calc__note{font-size:12px;color:var(--muted);line-height:1.55;margin-top:14px}

/* Карточки */
.cards{display:grid;gap:16px}
@media(min-width:700px){.cards{grid-template-columns:repeat(2,1fr)}}
@media(min-width:1100px){.cards{grid-template-columns:repeat(3,1fr)}}
.card{background:var(--bg-2);border:1px solid var(--line);border-radius:var(--radius);overflow:hidden;
  position:relative;transform-style:preserve-3d;
  transform:perspective(900px) rotateX(var(--rx,0)) rotateY(var(--ry,0));
  transition:transform .5s cubic-bezier(.16,1,.3,1),border-color .45s}
.card:hover{border-color:rgba(198,242,78,.42)}
.card__img{aspect-ratio:4/3;overflow:hidden;position:relative}
.card__img img{width:100%;height:100%;object-fit:cover;transition:transform 1.2s cubic-bezier(.16,1,.3,1)}
.card:hover .card__img img{transform:scale(1.07)}
.tag{position:absolute;top:14px;left:14px;padding:7px 13px;border-radius:100px;font-family:var(--font-head);
  font-size:11px;letter-spacing:.12em;background:rgba(14,15,16,.68);backdrop-filter:blur(8px);border:1px solid var(--line)}
.card__b{padding:22px;display:grid;gap:9px}
.card__b p{color:var(--muted);font-size:14px;min-height:42px}
.card__p{display:flex;justify-content:space-between;align-items:baseline;padding-top:15px;
  border-top:1px solid var(--line);margin-top:6px}
.card__p b{font-family:var(--font-head);font-size:1.35rem;color:var(--accent);font-weight:600;letter-spacing:-.02em}
.card__p span{font-size:12px;color:var(--muted)}

/* Планировки */
.tabs{display:inline-flex;gap:6px;padding:6px;background:var(--bg-2);border:1px solid var(--line);
  border-radius:100px;margin-bottom:28px;flex-wrap:wrap}
.tabs button{padding:11px 20px;border-radius:100px;font-family:var(--font-head);font-size:13px;font-weight:500;
  color:var(--muted);transition:.35s}
.tabs button.active{background:var(--accent);color:var(--on-accent)}
.plans{display:grid;gap:14px;grid-template-columns:repeat(2,1fr)}
@media(min-width:900px){.plans{grid-template-columns:repeat(4,1fr)}}
.plan{border:1px solid var(--line);border-radius:var(--radius-sm);overflow:hidden;background:var(--bg-2);
  cursor:zoom-in;transition:.45s cubic-bezier(.16,1,.3,1)}
.plan:hover{transform:translateY(-5px);border-color:rgba(198,242,78,.4);background:var(--bg-3)}
.plan__i{aspect-ratio:1/1;background:#fff;padding:10px}
.plan__i img{width:100%;height:100%;object-fit:contain}
.plan__b{padding:15px;display:grid;gap:5px}
.plan__b h4{font-family:var(--font-head);font-size:13.5px;font-weight:600}
.plan__b .m{font-size:12px;color:var(--muted)}
.plan__b .p{font-family:var(--font-head);font-size:15px;color:var(--accent);font-weight:600}

/* Комплектация — аккордеон */
.acc{display:grid;gap:12px}
.acc__item{border:1px solid var(--line);border-radius:var(--radius);background:var(--bg-2);overflow:hidden;
  transition:border-color .4s}
.acc__item.open{border-color:rgba(198,242,78,.4)}
.acc__head{width:100%;display:flex;align-items:center;justify-content:space-between;gap:16px;
  padding:24px 26px;text-align:left}
.acc__head h3{font-family:var(--font-head);font-size:clamp(1.05rem,1.8vw,1.3rem);font-weight:600}
.acc__head em{font-style:normal;font-size:12px;color:var(--muted);margin-left:12px}
.acc__ic{width:34px;height:34px;flex:0 0 34px;border-radius:50%;border:1px solid var(--line);
  display:grid;place-items:center;transition:.45s cubic-bezier(.16,1,.3,1)}
.acc__item.open .acc__ic{background:var(--accent);color:var(--on-accent);border-color:var(--accent);transform:rotate(135deg)}
.acc__body{max-height:0;overflow:hidden;transition:max-height .6s cubic-bezier(.16,1,.3,1)}
.acc__body ul{padding:0 26px 26px;display:grid;gap:2px}
@media(min-width:800px){.acc__body ul{grid-template-columns:1fr 1fr;column-gap:32px}}
.acc__body li{display:flex;gap:11px;padding:9px 0;font-size:14.5px;color:var(--muted);
  border-bottom:1px solid rgba(242,244,243,.05);line-height:1.5}
.acc__body svg{flex:0 0 15px;margin-top:4px;color:var(--accent)}

/* Процесс */
.steps{display:grid;gap:14px}
@media(min-width:900px){.steps{grid-template-columns:repeat(4,1fr)}}
.pstep{background:var(--bg-2);border:1px solid var(--line);border-radius:var(--radius);overflow:hidden;
  display:flex;flex-direction:column;transition:.5s cubic-bezier(.16,1,.3,1)}
.pstep:hover{transform:translateY(-6px);border-color:rgba(198,242,78,.4)}
.pstep__i{aspect-ratio:16/10;overflow:hidden}
.pstep__i img{width:100%;height:100%;object-fit:cover;transition:transform 1.2s cubic-bezier(.16,1,.3,1)}
.pstep:hover .pstep__i img{transform:scale(1.07)}
.pstep__b{padding:22px;display:grid;gap:10px;flex:1}
.pstep__n{font-family:var(--font-head);font-size:12px;letter-spacing:.16em;color:var(--accent)}
.pstep__b p{color:var(--muted);font-size:14px;line-height:1.6}

/* Мозаика */
.mos{display:grid;gap:14px;grid-template-columns:repeat(2,1fr)}
@media(min-width:900px){.mos{grid-template-columns:repeat(4,1fr)}
  .mos figure:nth-child(1){grid-column:span 2;grid-row:span 2}}
.mos figure{margin:0;border-radius:var(--radius);overflow:hidden;position:relative;aspect-ratio:1/1;cursor:zoom-in}
@media(min-width:900px){.mos figure:nth-child(1){aspect-ratio:auto}}
.mos img{width:100%;height:100%;object-fit:cover;transition:transform 1.2s cubic-bezier(.16,1,.3,1);filter:brightness(.86)}
.mos figure:hover img{transform:scale(1.06);filter:brightness(1)}
.mos figcaption{position:absolute;inset:auto 0 0 0;padding:50px 16px 16px;font-size:12.5px;
  background:linear-gradient(transparent,rgba(14,15,16,.9));opacity:0;transform:translateY(8px);transition:.45s}
.mos figure:hover figcaption{opacity:1;transform:none}

/* Объекты */
.objs{display:grid;gap:14px}
@media(min-width:800px){.objs{grid-template-columns:repeat(3,1fr)}
  .objs>*:nth-child(1),.objs>*:nth-child(2){grid-column:span 3}}
@media(min-width:1100px){.objs>*:nth-child(1){grid-column:span 2}.objs>*:nth-child(2){grid-column:span 1}}
.obj{position:relative;border-radius:var(--radius);overflow:hidden;display:block;aspect-ratio:16/10}
.obj img{width:100%;height:100%;object-fit:cover;transition:transform 1.3s cubic-bezier(.16,1,.3,1);filter:brightness(.82)}
.obj:hover img{transform:scale(1.05);filter:brightness(.95)}
.obj__c{display:block;position:absolute;inset:auto 0 0 0;padding:64px 22px 22px;
  background:linear-gradient(transparent,rgba(14,15,16,.92))}
.obj__c h3{font-family:var(--font-head);font-size:clamp(1.15rem,2vw,1.6rem);font-weight:600;letter-spacing:-.02em}
.obj__c p{font-size:13.5px;color:var(--muted);margin-top:5px}

/* До/после */
.ba-wrap{display:grid;gap:32px;align-items:center}
@media(min-width:1000px){.ba-wrap{grid-template-columns:.8fr 1.2fr;gap:56px}}

/* Заявка */
.cta{background:var(--bg-2);border:1px solid var(--line);border-radius:clamp(20px,3vw,32px);
  padding:clamp(30px,5vw,64px);position:relative;overflow:hidden}
.cta::after{content:"";position:absolute;width:48vw;aspect-ratio:1;border-radius:50%;right:-16vw;bottom:-26vw;
  background:radial-gradient(circle,rgba(198,242,78,.16),transparent 66%);animation:fl 18s ease-in-out infinite alternate}
@keyframes fl{to{transform:translate3d(-12vw,-14vw,0) scale(1.2)}}
.cta__in{position:relative;display:grid;gap:36px}
@media(min-width:960px){.cta__in{grid-template-columns:1fr 1fr;gap:64px;align-items:center}}
.cta form{display:grid;gap:14px}

/* Подвал */
.foot{padding:64px 0 32px}
.foot__grid{display:grid;gap:32px}
@media(min-width:800px){.foot__grid{grid-template-columns:1.5fr 1fr 1fr 1fr}}
.foot h4{font-family:var(--font-head);font-size:11px;letter-spacing:.18em;text-transform:uppercase;
  color:var(--muted);margin-bottom:15px}
.foot p{font-size:15px;margin-bottom:9px}
.foot a:hover{color:var(--accent)}
.foot__bot{margin-top:44px;padding-top:20px;border-top:1px solid var(--line);display:flex;flex-wrap:wrap;
  gap:12px;justify-content:space-between;font-size:12px;color:var(--muted)}
"""

CHECK = '<svg width="15" height="15" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><path d="M2.5 8.5l3.5 3.5 7.5-8"/></svg>'
MINUS = '<svg width="15" height="15" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><path d="M3 8h10"/></svg>'
PLUSI = '<svg width="15" height="15" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><path d="M8 3v10M3 8h10"/></svg>'
ARR = '<svg width="16" height="10" viewBox="0 0 18 10" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" aria-hidden="true"><path d="M0 5h16M12 1l4 4-4 4"/></svg>'

CALC_MODELS = [
    ("MODUL HOUSE 1", "27 м²", 990000), ("MODUL HOUSE 2", "30 м²", 1450000),
    ("MODUL HOUSE 3", "40 м²", 1550000), ("MODUL HOUSE 4", "56,3 м²", 1650000),
    ("MODUL HOUSE 6", "60 м²", 2500000), ("MODUL HOUSE 7", "72 м²", 3300000),
    ("Модульная баня", "15 м²", 1050000),
]
CALC_OPTS = [
    ("Система кондиционирования", 90000), ("Светодиодные подсветки", 45000),
    ("Сантехнические приборы", 75000), ("Система тёплого пола", 110000),
    ("Мебель и предметы интерьера", 250000), ("Отделка стен фанерой", 85000),
    ("Кашировка оконных рам", 40000),
]

def build():
    b = BRAND
    nav = "".join(f'<a href="{h}">{t}</a>' for h, t in NAV)
    o = [core.head("ДОММ — модульные дома под ключ за 30 дней | Новосибирск",
                   "Модульные дома с террасой от 990 000 ₽. Калькулятор стоимости, 20+ планировок, собственное производство в Новосибирске.",
                   FONTS, CSS, "#0E0F10")]
    o.append('<div class="cursor"></div>')
    o.append(f"""
<header class="hdr" data-header><div class="wrap"><div class="hdr__in">
  <a class="logo" href="#top"><i></i>ДОММ</a>
  <nav class="nav">{nav}</nav>
  <div style="display:flex;gap:10px;align-items:center">
    <a class="btn btn--fill hdr__cta" href="#calc" data-magnet=".25">Рассчитать дом</a>
    <button class="burger" data-burger aria-label="Меню" aria-expanded="false"><i></i><i></i><i></i></button>
  </div>
</div></div></header>
<nav class="mnav" data-menu>{nav}
  <div class="mnav__foot"><a href="tel:{b['phone1_href']}">{b['phone1']}</a>
  <a href="tel:{b['phone2_href']}">{b['phone2']}</a><a href="mailto:{b['email']}">{b['email']}</a></div>
</nav>""")

    o.append(f"""
<section class="hero" id="top"><div class="wrap">
  <div class="bento">
    <div class="hero__main sp2 sp4" data-rv="zoom">
      <img src="{HERO['bg']}" alt="Модульный дом ДОММ с террасой">
      <div class="hero__c">
        <span class="kicker"><i></i>{HERO['kicker']}</span>
        <h1 class="h1" style="margin:16px 0 0" data-split="line">Модульные дома<br>для жизни<br>и отдыха</h1>
        <p class="lead">{HERO['sub']}</p>
        <div class="hero__acts">
          <a class="btn btn--fill" href="#calc" data-magnet=".3">Рассчитать стоимость {ARR}</a>
          <a class="btn btn--ghost" href="{b['wa']}" target="_blank" rel="noopener">WhatsApp</a>
        </div>
      </div>
    </div>
    <div class="box box--accent" data-tilt="0" data-rv="up">
      <span class="mono" style="opacity:.65">Реализовано</span>
      <div class="stat"><b data-count="80" data-suffix="+">0</b><span>проектов по России</span></div>
    </div>
    <div class="box" data-tilt="0" data-rv="up" style="--d:80ms">
      <span class="mono" style="color:var(--muted)">Срок</span>
      <div class="stat"><b data-count="30">0</b><span>дней производство</span></div>
    </div>
    <div class="box" data-tilt="0" data-rv="up" style="--d:160ms">
      <span class="mono" style="color:var(--muted)">Монтаж краном</span>
      <div class="stat"><b>1 день</b><span>дом собирается на участке</span></div>
      <div class="mods"><i></i><i></i><i></i><i></i><i></i></div>
    </div>
    <div class="box box--img" data-rv="up" style="--d:240ms;min-height:200px">
      <img src="{GALLERY[3]}" alt="Интерьер модульного дома" loading="lazy">
    </div>
  </div>
</div></section>""")

    # Калькулятор
    chips = "".join(f'<button class="chip{" on" if i==0 else ""}" data-model data-price="{p}" data-name="{n}" data-area="{a}">{n} · {a}</button>'
                    for i, (n, a, p) in enumerate(CALC_MODELS))
    opts = "".join(f"""<label class="opt"><input type="checkbox" data-opt value="{p}">
      <span class="bx">{CHECK}</span><span>{n}</span><b>+{p:,} ₽</b></label>""".replace(",", " ")
                   for n, p in CALC_OPTS)
    o.append(f"""
<section class="sec" id="calc"><div class="wrap">
  <div class="sec-head split">
    <div data-rv="up"><span class="kicker"><i></i>Калькулятор</span>
      <h2 class="h2" style="margin-top:16px" data-split="line">Соберите свой дом<br>и узнайте цену</h2></div>
    <p class="lead" data-rv="up" style="--d:150ms">Выберите модель и дополнительные опции — стоимость
    пересчитается сразу. Итог ориентировочный: точную смету пришлём после разговора.</p>
  </div>
  <div class="calc">
    <div class="calc__panel" data-rv="up">
      <div class="calc__group"><span class="mono">1 — Модель дома</span><div class="chips">{chips}</div></div>
      <div class="calc__group"><span class="mono">2 — Комплектация под ключ</span>
        <div class="chips">
          <button class="chip on" data-pack data-k="1">Базовая</button>
          <button class="chip" data-pack data-k="1.12">Расширенная +12%</button>
          <button class="chip" data-pack data-k="1.25">Премиум +25%</button>
        </div></div>
      <div class="calc__group" style="margin-bottom:0"><span class="mono">3 — Дополнительные опции</span>{opts}</div>
    </div>
    <div class="calc__sum" data-rv="up" style="--d:120ms">
      <span class="mono" style="color:var(--muted)">Ориентировочная стоимость</span>
      <div class="calc__total" data-total>990 000 ₽</div>
      <div class="calc__rows">
        <div><span>Модель</span><b data-r-model>MODUL HOUSE 1 · 27 м²</b></div>
        <div><span>Комплектация</span><b data-r-pack>Базовая</b></div>
        <div><span>Опции</span><b data-r-opts>—</b></div>
        <div><span>Цена за м²</span><b data-r-sq>36 667 ₽</b></div>
      </div>
      <a class="btn btn--fill" href="#cta" data-magnet=".25" style="width:100%">Зафиксировать цену {ARR}</a>
      <p class="calc__note">Без доставки, фундамента и монтажа на участке — считаем индивидуально
      по адресу. Аванс 30% фиксирует стоимость на весь срок производства.</p>
    </div>
  </div>
</div></section>""")

    cards = "".join(f"""
    <article class="card" data-tilt="6" data-rv="up">
      <div class="card__img"><span class="tag">{area}</span><img src="{im}" alt="{n}" loading="lazy"></div>
      <div class="card__b"><h3 class="h3">{n}</h3><p>{d}</p>
        <div class="card__p"><b>от {p} ₽</b><span>под ключ</span></div>
        <a class="btn btn--ghost" href="#cta" style="margin-top:12px;justify-self:start">Подробнее {ARR}</a></div>
    </article>""" for n, d, p, area, im in PROJECTS)
    o.append(f"""
<section class="sec" id="projects"><div class="wrap">
  <div class="sec-head split">
    <div data-rv="up"><span class="kicker"><i></i>Каталог</span>
      <h2 class="h2" style="margin-top:16px">Проекты домов и бань</h2></div>
    <p class="lead" data-rv="up" style="--d:150ms">Семь базовых моделей и две бани — любую адаптируем
    под участок и сценарий жизни.</p>
  </div>
  <div class="cards" data-stagger="80">{cards}</div>
</div></section>""")

    def pg(items, key):
        return "".join(f"""
      <article class="plan" data-lb="{key}" data-full="{im}" data-cap="{n} — {a}, от {p} тыс. ₽">
        <div class="plan__i"><img src="{im}" alt="Планировка {n}" loading="lazy"></div>
        <div class="plan__b"><h4>{n}</h4><span class="m">{a}{' · ' + note if note else ''}</span>
          <span class="p">от {p} тыс. ₽</span></div></article>""" for n, a, p, im, note in items)
    rend = "".join(f"""
      <article class="card" data-lb="rn" data-full="{im}" data-cap="{n}" style="cursor:zoom-in" data-tilt="6">
        <div class="card__img"><img src="{im}" alt="{n}" loading="lazy"></div>
        <div class="card__b"><h3 class="h3">{n}</h3><p>{d}</p></div></article>""" for n, d, im in RENDERS)
    o.append(f"""
<section class="sec" id="prices" style="background:var(--bg-2)"><div class="wrap" data-tabs>
  <div class="sec-head split">
    <div data-rv="up"><span class="kicker"><i></i>Планировки</span>
      <h2 class="h2" style="margin-top:16px">Выберите свой метраж</h2></div>
    <p class="lead" data-rv="up" style="--d:150ms">Дома собираются из модулей 2,5×6 м и 3×6 м.
    Нажмите на планировку, чтобы рассмотреть крупно.</p>
  </div>
  <div class="tabs" role="tablist">
    <button data-tab="a" class="active" role="tab" aria-selected="true">Модули 2,5 × 6</button>
    <button data-tab="b" role="tab" aria-selected="false">Модули 3 × 6</button>
    <button data-tab="c" role="tab" aria-selected="false">Визуализации</button>
  </div>
  <div class="plans" data-panel="a" data-stagger="50">{pg(PLANS_25,'p25')}</div>
  <div class="plans" data-panel="b" hidden data-stagger="50">{pg(PLANS_36,'p36')}</div>
  <div class="cards" data-panel="c" hidden data-stagger="70">{rend}</div>
</div></section>""")

    def lis(items, ic):
        return "".join(f'<li>{ic}<span>{t}</span></li>' for t in items)
    o.append(f"""
<section class="sec" id="spec"><div class="wrap">
  <div class="sec-head" data-rv="up"><span class="kicker"><i></i>Комплектация</span>
    <h2 class="h2" style="margin-top:16px">Что входит в базовую стоимость</h2></div>
  <div class="acc" data-acc data-stagger="90">
    <div class="acc__item open">
      <button class="acc__head" aria-expanded="true"><h3>Входит в стоимость<em>{len(INCLUDED)} пунктов</em></h3>
        <span class="acc__ic">{PLUSI}</span></button>
      <div class="acc__body" style="max-height:2200px"><ul>{lis(INCLUDED, CHECK)}</ul></div>
    </div>
    <div class="acc__item">
      <button class="acc__head" aria-expanded="false"><h3>Не входит в стоимость<em>{len(EXCLUDED)} пунктов</em></h3>
        <span class="acc__ic">{PLUSI}</span></button>
      <div class="acc__body"><ul>{lis(EXCLUDED, MINUS)}</ul></div>
    </div>
    <div class="acc__item">
      <button class="acc__head" aria-expanded="false"><h3>Дополнительные опции<em>{len(OPTIONS)} пунктов</em></h3>
        <span class="acc__ic">{PLUSI}</span></button>
      <div class="acc__body"><ul>{lis(OPTIONS, PLUSI)}</ul></div>
    </div>
  </div>
</div></section>""")

    steps = "".join(f"""
    <article class="pstep" data-rv="up">
      <div class="pstep__i"><img src="{im}" alt="{t}" loading="lazy"></div>
      <div class="pstep__b"><span class="pstep__n">ЭТАП {n}</span><h3 class="h3">{t}</h3><p>{d}</p></div>
    </article>""" for n, t, d, im in PROCESS)
    o.append(f"""
<section class="sec" id="process" style="background:var(--bg-2)"><div class="wrap">
  <div class="sec-head" data-rv="up"><span class="kicker"><i></i>Как мы работаем</span>
    <h2 class="h2" style="margin-top:16px">Четыре шага до новоселья</h2></div>
  <div class="steps" data-stagger="100">{steps}</div>
</div></section>""")

    mos = "".join(f'<figure data-lb="d" data-full="{im}" data-cap="{t}"><img src="{im}" alt="{t}" loading="lazy"><figcaption>{t}</figcaption></figure>'
                  for t, im in DETAILS + INTERIOR)
    o.append(f"""
<section class="sec" id="details"><div class="wrap">
  <div class="sec-head split">
    <div data-rv="up"><span class="kicker"><i></i>Black Paket</span>
      <h2 class="h2" style="margin-top:16px">Детали в едином чёрном стиле</h2></div>
    <p class="lead" data-rv="up" style="--d:150ms">Электрощит, розетки, выключатели, светильники,
    дверные ручки и фасадный свет — одно оформление без визуального шума.</p>
  </div>
  <div class="mos" data-stagger="70">{mos}</div>
</div></section>""")

    objs = "".join(f"""
    <div><a class="obj" href="#cta"><img src="{im}" alt="{t}" loading="lazy">
      <span class="obj__c"><h3>{t}</h3><p>{d}</p></span></a></div>""" for t, d, im in OBJECTS)
    o.append(f"""
<section class="sec" id="objects" style="background:var(--bg-2)"><div class="wrap">
  <div class="sec-head" data-rv="up"><span class="kicker"><i></i>Наши дома</span>
    <h2 class="h2" style="margin-top:16px">Реализованные объекты</h2></div>
  <div class="objs" data-stagger="90">{objs}</div>
</div></section>""")

    o.append(f"""
<section class="sec"><div class="wrap ba-wrap">
  <div data-rv="up"><span class="kicker"><i></i>Посмотрите разницу</span>
    <h2 class="h2" style="margin:16px 0 16px">Ваш дом у нас — и ваш дом у вас</h2>
    <p class="lead">Слева — модуль на производстве, справа — тот же дом на участке. Потяните ползунок.</p></div>
  <div class="ba" data-rv="zoom" role="img" aria-label="Сравнение: дом на производстве и на участке">
    <img src="{BEFORE}" alt="Модуль на производстве" loading="lazy">
    <img class="ba__after" src="{AFTER}" alt="Готовый дом на участке" loading="lazy">
    <span class="ba__line"></span><span class="ba__grip">&#8596;</span>
    <span class="ba__tag l">Ваш дом у нас</span><span class="ba__tag r">Ваш дом у вас</span>
  </div>
</div></section>""")

    o.append(f"""
<section class="sec" id="cta"><div class="wrap"><div class="cta" data-rv="up"><div class="cta__in">
  <div>
    <span class="kicker"><i></i>Свяжитесь с нами</span>
    <h2 class="h2" style="margin:16px 0 16px">Оставьте заявку и получите расчёт</h2>
    <p class="lead">Подберём планировку под участок и посчитаем стоимость с доставкой и монтажом.</p>
    <div style="margin-top:26px;display:grid;gap:8px;font-family:var(--font-head);font-size:1.45rem;font-weight:600;letter-spacing:-.03em">
      <a href="tel:{b['phone1_href']}">{b['phone1']}</a><a href="tel:{b['phone2_href']}">{b['phone2']}</a>
    </div>
  </div>
  <form data-form novalidate>
    <div class="f-row two">
      <div class="field"><label for="n3">Ваше имя</label>
        <input id="n3" type="text" required autocomplete="name" placeholder="Иван"><span class="err">Укажите имя</span></div>
      <div class="field"><label for="t3">Телефон</label>
        <input id="t3" type="tel" required autocomplete="tel" inputmode="tel" placeholder="+7 (___) ___-__-__">
        <span class="err">Введите номер полностью</span></div>
    </div>
    <div class="field"><label for="m3">Комментарий</label>
      <textarea id="m3" rows="3" placeholder="Интересует MODUL HOUSE 3, участок в Бердске"></textarea></div>
    <button class="btn btn--fill" type="submit" data-magnet=".2" style="justify-self:start">Отправить заявку {ARR}</button>
    <p class="form-note">Нажимая кнопку, вы соглашаетесь с обработкой персональных данных.</p>
    <div class="form-ok" role="status">Спасибо! Заявка принята — мы перезвоним в рабочее время.</div>
  </form>
</div></div></div></section>""")

    o.append(f"""
<footer class="foot" id="contacts"><div class="wrap">
  <div class="foot__grid">
    <div data-rv="up"><a class="logo" href="#top"><i></i>ДОММ</a>
      <p class="lead" style="margin-top:14px;font-size:15px">Производство и продажа модульных домов
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
  <div class="foot__bot"><span>© <span data-year></span> ДОММ. Модульные дома.</span><span>Новосибирск</span></div>
</div></footer>""")

    o.append(core.dock(b))

    extra = r"""
/* Калькулятор */
(function(){
  var root = document.getElementById('calc'); if(!root) return;
  var models = root.querySelectorAll('[data-model]');
  var packs = root.querySelectorAll('[data-pack]');
  var opts = root.querySelectorAll('[data-opt]');
  var total = root.querySelector('[data-total]');
  var rM = root.querySelector('[data-r-model]'), rP = root.querySelector('[data-r-pack]'),
      rO = root.querySelector('[data-r-opts]'), rS = root.querySelector('[data-r-sq]');
  var cur = 0;
  function fmt(n){ return Math.round(n).toLocaleString('ru-RU') + ' ₽'; }
  function calc(){
    var m = root.querySelector('[data-model].on') || models[0];
    var p = root.querySelector('[data-pack].on') || packs[0];
    var k = parseFloat(p.dataset.k);
    var base = parseFloat(m.dataset.price) * k;
    var add = 0, cnt = 0;
    opts.forEach(function(o){ if(o.checked){ add += parseFloat(o.value); cnt++; } });
    var sum = base + add;
    var area = parseFloat(m.dataset.area.replace(',', '.'));
    rM.textContent = m.dataset.name + ' · ' + m.dataset.area;
    rP.textContent = p.textContent;
    rO.textContent = cnt ? cnt + ' шт · ' + fmt(add) : '—';
    rS.textContent = fmt(sum / area);
    /* плавный счёт */
    var from = cur, t0 = null;
    cur = sum;
    if(window.matchMedia('(prefers-reduced-motion: reduce)').matches){ total.textContent = fmt(sum); return; }
    requestAnimationFrame(function step(t){
      if(!t0) t0 = t;
      var q = Math.min((t - t0)/500, 1), e = 1 - Math.pow(1-q, 3);
      total.textContent = fmt(from + (sum - from) * e);
      if(q < 1) requestAnimationFrame(step);
    });
  }
  function pick(list, el){ list.forEach(function(x){ x.classList.toggle('on', x === el); }); calc(); }
  models.forEach(function(x){ x.addEventListener('click', function(){ pick(models, x); }); });
  packs.forEach(function(x){ x.addEventListener('click', function(){ pick(packs, x); }); });
  opts.forEach(function(x){ x.addEventListener('change', calc); });
  calc();
})();
"""
    o.append(core.tail(extra))
    return "".join(o)
