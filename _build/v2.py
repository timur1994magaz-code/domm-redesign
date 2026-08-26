# -*- coding: utf-8 -*-
"""Вариант 2 — SCANDI LIGHT. Светлый тёплый минимализм, журнальная типографика."""
import core
from data import *

FONTS = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;1,400&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">'

CSS = r"""
:root{
  --bg:#F7F4EF; --bg-2:#FFFFFF; --bg-3:#EFE9E0; --ink:#1C1A17;
  --fg:#1C1A17; --muted:#7A736A; --line:rgba(28,26,23,.13);
  --accent:#8C6A46; --accent-2:#C9A227; --on-accent:#FFFFFF; --input-bg:#fff;
  --font-head:'Playfair Display',Georgia,serif; --font-body:'Inter',system-ui,sans-serif;
  --radius:14px; --radius-sm:10px; --head-weight:400;
}
::selection{background:var(--accent);color:#fff}
.h1{font-size:clamp(2.7rem,7.2vw,6.2rem);line-height:.98;letter-spacing:-.02em;font-weight:400}
.h2{font-size:clamp(2rem,4.6vw,3.7rem);line-height:1.04;letter-spacing:-.018em;font-weight:400}
.h3{font-size:clamp(1.15rem,1.9vw,1.5rem);font-weight:500;letter-spacing:-.01em}
.it{font-style:italic;color:var(--accent)}
.kicker{display:inline-block;font-family:var(--font-body);font-size:11px;letter-spacing:.24em;
  text-transform:uppercase;color:var(--accent);padding:7px 14px;border:1px solid var(--line);border-radius:100px}
.lead{color:var(--muted);font-size:clamp(1rem,1.25vw,1.12rem);max-width:60ch;font-weight:300;line-height:1.7}
.sec{padding:clamp(76px,10vw,150px) 0}
.sec-head{display:grid;gap:22px;margin-bottom:clamp(38px,5vw,66px)}
@media(min-width:900px){.sec-head.split{grid-template-columns:1.1fr .9fr;align-items:end;gap:56px}}
.paper{position:fixed;inset:0;z-index:-1;pointer-events:none;opacity:.5;
  background-image:radial-gradient(rgba(28,26,23,.055) 1px,transparent 1px);background-size:3px 3px}

/* Шапка */
.hdr{position:fixed;inset:0 0 auto 0;z-index:100;padding:18px 0;transition:.5s cubic-bezier(.16,1,.3,1)}
.hdr.stuck{background:rgba(247,244,239,.86);backdrop-filter:blur(16px);
  box-shadow:0 1px 0 var(--line);padding:11px 0}
.hdr.hide{transform:translateY(-105%)}
.hdr__in{display:flex;align-items:center;justify-content:space-between;gap:20px}
.logo{font-family:var(--font-head);font-size:22px;letter-spacing:.06em;font-weight:500}
.logo em{font-style:normal;color:var(--accent)}
.nav{display:none;gap:30px}
@media(min-width:1024px){.nav{display:flex}}
.nav a{font-size:13px;color:var(--muted);position:relative;padding:5px 0;transition:color .3s}
.nav a::after{content:"";position:absolute;left:0;right:0;bottom:0;height:1px;background:var(--accent);
  transform:scaleX(0);transform-origin:0 50%;transition:transform .45s cubic-bezier(.16,1,.3,1)}
.nav a:hover{color:var(--ink)}.nav a:hover::after{transform:scaleX(1)}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;padding:14px 26px;
  border-radius:100px;font-size:13px;font-weight:500;position:relative;overflow:hidden;isolation:isolate;
  transform:translate3d(var(--tx,0),var(--ty,0),0);transition:transform .4s cubic-bezier(.16,1,.3,1),color .3s,box-shadow .35s}
.btn--fill{background:var(--ink);color:#fff;box-shadow:0 6px 22px rgba(28,26,23,.16)}
.btn--fill::before{content:"";position:absolute;inset:0;z-index:-1;background:var(--accent);
  transform:translateY(100%);transition:transform .5s cubic-bezier(.16,1,.3,1)}
.btn--fill:hover::before{transform:none}
.btn--fill:hover{box-shadow:0 12px 32px rgba(140,106,70,.32)}
.btn--ghost{border:1px solid var(--line);color:var(--ink)}
.btn--ghost:hover{border-color:var(--accent);color:var(--accent)}
.hdr__cta{display:none}@media(min-width:640px){.hdr__cta{display:inline-flex}}
.burger{display:grid;gap:5px;padding:10px;margin:-10px}
@media(min-width:1024px){.burger{display:none}}
.burger i{width:22px;height:1.5px;background:var(--ink);transition:.4s}
body.nav-open .burger i:nth-child(1){transform:translateY(6.5px) rotate(45deg)}
body.nav-open .burger i:nth-child(2){opacity:0}
body.nav-open .burger i:nth-child(3){transform:translateY(-6.5px) rotate(-45deg)}
.mnav{position:fixed;inset:0;z-index:99;background:var(--bg);display:grid;align-content:center;gap:6px;
  padding:0 var(--gutter);opacity:0;visibility:hidden;transition:.5s}
body.nav-open .mnav{opacity:1;visibility:visible}
.mnav a{font-family:var(--font-head);font-size:clamp(2rem,9vw,3.4rem);opacity:0;transform:translateY(20px);
  transition:.6s cubic-bezier(.16,1,.3,1)}
body.nav-open .mnav a{opacity:1;transform:none}
.mnav a:nth-child(1){transition-delay:.06s}.mnav a:nth-child(2){transition-delay:.12s}
.mnav a:nth-child(3){transition-delay:.18s}.mnav a:nth-child(4){transition-delay:.24s}
.mnav a:nth-child(5){transition-delay:.3s}
.mnav__foot{margin-top:30px;color:var(--muted);font-size:15px;display:grid;gap:6px}

/* Герой */
.hero{padding:132px 0 0;overflow:hidden}
.hero__t{text-align:center;display:grid;gap:20px;justify-items:center}
.hero__sub{max-width:52ch;text-align:center}
.hero__acts{display:flex;gap:14px;flex-wrap:wrap;justify-content:center;margin-top:8px}
.hero__frame{margin-top:clamp(38px,5vw,64px);border-radius:var(--radius);overflow:hidden;
  aspect-ratio:16/9;position:relative;clip-path:inset(0 0 100% 0)}
.hero__frame.in{clip-path:inset(0 0 0 0);transition:clip-path 1.4s cubic-bezier(.16,1,.3,1)}
.hero__frame img{width:100%;height:100%;object-fit:cover;
  transform:scale(1.14) translate3d(0,var(--par,0),0);transition:transform 1.6s cubic-bezier(.16,1,.3,1)}
.hero__frame.in img{transform:scale(1.02) translate3d(0,var(--par,0),0)}
.hero__badge{position:absolute;left:20px;bottom:20px;background:rgba(255,255,255,.92);
  backdrop-filter:blur(10px);border-radius:100px;padding:12px 20px;font-size:13px;font-weight:500;
  display:flex;gap:10px;align-items:center}
.hero__badge b{color:var(--accent)}
@media(max-width:640px){.hero__frame{aspect-ratio:4/5}}

/* Цифры */
.nums{display:grid;grid-template-columns:repeat(2,1fr);gap:1px;background:var(--line);
  border:1px solid var(--line);border-radius:var(--radius);overflow:hidden}
@media(min-width:800px){.nums{grid-template-columns:repeat(4,1fr)}}
.nums div{background:var(--bg);padding:30px 24px;transition:background .4s}
.nums div:hover{background:var(--bg-2)}
.nums b{display:block;font-family:var(--font-head);font-size:clamp(2rem,3.4vw,2.9rem);color:var(--ink);
  letter-spacing:-.02em}
.nums span{font-size:12px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}

/* Галерея — горизонтальная лента */
.gal{display:flex;gap:14px;overflow-x:auto;scroll-snap-type:x mandatory;padding:0 var(--gutter) 18px;
  cursor:grab;scrollbar-width:none}
.gal::-webkit-scrollbar{display:none}
.gal.dragging{cursor:grabbing;scroll-snap-type:none}
.gal figure{margin:0;flex:0 0 clamp(230px,34vw,400px);scroll-snap-align:center;border-radius:var(--radius);
  overflow:hidden;aspect-ratio:3/4;position:relative}
.gal figure:nth-child(even){margin-top:34px}
.gal img{width:100%;height:100%;object-fit:cover;transition:transform 1.1s cubic-bezier(.16,1,.3,1)}
.gal figure:hover img{transform:scale(1.06)}

/* Карточки проектов */
.cards{display:grid;gap:22px}
@media(min-width:700px){.cards{grid-template-columns:repeat(2,1fr)}}
@media(min-width:1100px){.cards{grid-template-columns:repeat(3,1fr)}}
.card{background:var(--bg-2);border-radius:var(--radius);overflow:hidden;
  box-shadow:0 1px 2px rgba(28,26,23,.05);transition:transform .6s cubic-bezier(.16,1,.3,1),box-shadow .6s}
.card:hover{transform:translateY(-8px);box-shadow:0 26px 60px rgba(28,26,23,.14)}
.card__img{aspect-ratio:4/3;overflow:hidden;position:relative}
.card__img img{width:100%;height:100%;object-fit:cover;transition:transform 1.2s cubic-bezier(.16,1,.3,1)}
.card:hover .card__img img{transform:scale(1.07)}
.card__area{position:absolute;top:14px;right:14px;background:rgba(255,255,255,.94);border-radius:100px;
  padding:7px 14px;font-size:12px;font-weight:500}
.card__b{padding:24px 22px 26px;display:grid;gap:9px}
.card__b p{color:var(--muted);font-size:14px;font-weight:300;min-height:42px}
.card__p{display:flex;justify-content:space-between;align-items:baseline;padding-top:15px;
  margin-top:6px;border-top:1px solid var(--line)}
.card__p b{font-family:var(--font-head);font-size:1.4rem;font-weight:500}
.card__p span{font-size:12px;color:var(--muted)}

/* Калькулятор */
.calc{display:grid;gap:22px}
@media(min-width:1040px){.calc{grid-template-columns:1fr .82fr;gap:30px;align-items:start}}
.calc__panel{background:var(--bg-2);border-radius:var(--radius);padding:clamp(24px,3vw,36px);
  box-shadow:0 1px 2px rgba(28,26,23,.05)}
.grp{padding-bottom:24px;margin-bottom:24px;border-bottom:1px solid var(--line)}
.grp:last-child{padding-bottom:0;margin-bottom:0;border-bottom:0}
.grp>.gt{display:flex;align-items:baseline;gap:10px;margin-bottom:14px}
.grp>.gt b{font-family:var(--font-head);font-size:1.15rem;font-weight:500}
.grp>.gt span{font-size:12.5px;color:var(--muted)}
.chips{display:flex;flex-wrap:wrap;gap:8px}
.chip{padding:12px 16px;border-radius:100px;font-size:13.5px;color:var(--muted);text-align:left;
  background:var(--bg);border:1px solid var(--line);transition:.3s}
.chip:hover{border-color:var(--accent);color:var(--ink)}
.chip.on{background:var(--accent);color:#fff;border-color:var(--accent)}
.chip small{display:block;font-size:11.5px;opacity:.75;margin-top:2px}
.copt{display:flex;align-items:center;gap:12px;padding:11px 0;border-bottom:1px solid rgba(28,26,23,.07);cursor:pointer}
.copt:last-child{border-bottom:0}
.copt input{position:absolute;opacity:0;pointer-events:none}
.copt .bx{flex:0 0 22px;width:22px;height:22px;border-radius:7px;border:1px solid var(--line);
  background:var(--bg);display:grid;place-items:center;transition:.3s}
.copt .bx svg{width:11px;height:11px;color:#fff;opacity:0;transform:scale(.5);transition:.3s}
.copt input:checked + .bx{background:var(--accent);border-color:var(--accent)}
.copt input:checked + .bx svg{opacity:1;transform:none}
.copt input:focus-visible + .bx{outline:2px solid var(--accent);outline-offset:3px}
.copt .t{flex:1;font-size:14.5px}
.copt b{font-size:13.5px;color:var(--muted);font-weight:500;white-space:nowrap;font-variant-numeric:tabular-nums}
.rng{margin-top:4px}
.rng__top{display:flex;justify-content:space-between;align-items:baseline;gap:12px;margin-bottom:12px}
.rng__top span{font-size:12.5px;color:var(--muted)}
.rng__top b{font-size:15px;font-weight:600;font-variant-numeric:tabular-nums}
input[type=range]{-webkit-appearance:none;appearance:none;width:100%;height:26px;background:transparent;
  cursor:pointer;margin:0}
input[type=range]::-webkit-slider-runnable-track{height:2px;background:var(--line);border-radius:2px}
input[type=range]::-moz-range-track{height:2px;background:var(--line);border-radius:2px}
input[type=range]::-webkit-slider-thumb{-webkit-appearance:none;width:22px;height:22px;border-radius:50%;
  background:var(--accent);border:4px solid var(--bg-2);margin-top:-10px;
  box-shadow:0 2px 8px rgba(28,26,23,.24);transition:transform .2s}
input[type=range]::-moz-range-thumb{width:22px;height:22px;border-radius:50%;background:var(--accent);
  border:4px solid var(--bg-2);box-shadow:0 2px 8px rgba(28,26,23,.24)}
input[type=range]:active::-webkit-slider-thumb{transform:scale(1.15)}
input[type=range]:focus-visible::-webkit-slider-thumb{outline:2px solid var(--accent);outline-offset:3px}
/* итог */
.calc__sum{background:var(--ink);color:#F7F4EF;border-radius:var(--radius);
  padding:clamp(24px,3vw,34px);position:sticky;top:88px;overflow:hidden}
@media(max-width:1039px){.calc__sum{position:static}}
.calc__sum>.cap{font-size:12.5px;color:rgba(247,244,239,.66)}
.calc__total{font-family:var(--font-head);font-size:clamp(2.3rem,4.6vw,3.1rem);font-weight:500;
  letter-spacing:-.02em;color:#D9B87C;margin:6px 0 2px;font-variant-numeric:tabular-nums}
.calc__sub{font-size:13px;color:rgba(247,244,239,.66);line-height:1.5}
.calc__rows{margin:22px 0 0;border-top:1px solid rgba(247,244,239,.18)}
.calc__rows div{display:flex;justify-content:space-between;gap:12px;padding:10px 0;
  border-bottom:1px solid rgba(247,244,239,.1);font-size:13.5px;color:rgba(247,244,239,.68)}
.calc__rows b{color:#F7F4EF;font-weight:500;text-align:right;font-variant-numeric:tabular-nums}
.pay{margin-top:18px}
.pay>.cap{font-size:12.5px;color:rgba(247,244,239,.66);margin-bottom:4px;display:block}
.pay>.cap em{display:block;font-style:normal;font-size:11px;color:rgba(247,244,239,.45);margin-top:3px;line-height:1.45}
.pay>.cap em b{color:rgba(247,244,239,.7);font-weight:500}
.pay__row{position:relative;display:grid;grid-template-columns:40px 1fr auto;gap:12px;
  align-items:center;padding:10px 0 13px}
/* дорожка шкалы — она же разделитель строк */
.pay__row::before{content:"";position:absolute;left:0;right:0;bottom:0;height:2px;
  background:rgba(247,244,239,.14)}
/* --k задаёт скрипт: доля платежа во всей смете */
.pay__bar{position:absolute;left:0;right:0;bottom:0;height:2px;background:#D9B87C;
  transform-origin:0 50%;transform:scaleX(0);transition:transform .7s cubic-bezier(.16,1,.3,1)}
.in .pay__bar{transform:scaleX(var(--k,0))}
.pay__row--extra{color:rgba(247,244,239,.72)}
.pay__row--extra .pay__pc{font-family:var(--font-body);font-size:10.5px;letter-spacing:.1em;
  text-transform:uppercase;color:rgba(247,244,239,.4)}
.pay__row--extra .pay__bar{background:rgba(247,244,239,.42)}
.pay__pc{font-family:var(--font-head);font-size:1rem;font-weight:500;color:#D9B87C;
  font-variant-numeric:tabular-nums}
.pay__t b{display:block;font-size:13px;font-weight:500;line-height:1.3}
.pay__t span{display:block;font-size:11px;color:rgba(247,244,239,.58);margin-top:2px;line-height:1.35}
.pay__v{font-size:13.5px;font-weight:500;white-space:nowrap;font-variant-numeric:tabular-nums}
.calc__note{font-size:11.5px;color:rgba(247,244,239,.55);line-height:1.6;margin-top:16px}
.calc__sum .btn{margin-top:18px;width:100%;background:#D9B87C;color:var(--ink);box-shadow:none}
.calc__sum .btn::before{background:#F7F4EF}
.calc__sum .btn:hover{color:var(--ink)}

/* На широком экране блок должен помещаться в один экран целиком */
@media(min-width:1040px){
  .calc{gap:24px}
  .calc__panel,.calc__sum{padding:26px}
  .grp{padding-bottom:17px;margin-bottom:17px}
  .grp>.gt{margin-bottom:11px}
  .grp>.gt b{font-size:1.05rem}
  .chip{padding:10px 14px;font-size:13px}
  .chip small{font-size:11px;margin-top:1px}
  .copts{display:grid;grid-template-columns:1fr 1fr;column-gap:26px}
  .copt{padding:9px 0}
  .copts .copt:nth-last-child(-n+2){border-bottom:0}
  .copt .t{font-size:13.5px}
  .rng__top{margin-bottom:8px}
  input[type=range]{height:22px}
  .calc__total{font-size:clamp(2rem,3.4vw,2.6rem);margin:4px 0 2px}
  .calc__rows{margin:16px 0 0}
  .calc__rows div{padding:8px 0;font-size:13px}
  .calc__note{font-size:11px;margin-top:12px}
  .calc__sum .btn{margin-top:14px;padding:13px 24px}
}

/* Планировки — список-аккордеон */
.tabs{display:inline-flex;gap:6px;padding:6px;background:var(--bg-3);border-radius:100px;margin-bottom:32px}
.tabs button{padding:11px 22px;border-radius:100px;font-size:13px;font-weight:500;color:var(--muted);transition:.35s}
.tabs button.active{background:var(--bg-2);color:var(--ink);box-shadow:0 2px 10px rgba(28,26,23,.09)}
.plist{border-top:1px solid var(--line)}
.prow{display:grid;grid-template-columns:1fr auto;gap:16px;align-items:center;padding:22px 4px;
  border-bottom:1px solid var(--line);cursor:zoom-in;transition:padding-left .5s cubic-bezier(.16,1,.3,1),background .4s}
.prow:hover{padding-left:18px;background:var(--bg-2)}
.prow__l{display:flex;align-items:baseline;gap:16px;flex-wrap:wrap}
.prow__n{font-family:var(--font-head);font-size:clamp(1.1rem,2vw,1.5rem)}
.prow__m{font-size:13px;color:var(--muted)}
.prow__p{font-family:var(--font-head);font-size:clamp(1.05rem,1.8vw,1.4rem);white-space:nowrap}
.prow__th{width:0;height:64px;border-radius:8px;overflow:hidden;transition:width .55s cubic-bezier(.16,1,.3,1);
  background:#fff;flex:0 0 auto}
.prow:hover .prow__th{width:88px}
.prow__th img{width:88px;height:64px;object-fit:contain}
@media(max-width:700px){.prow__th{display:none}}

/* Комплектация */
.spec{display:grid;gap:18px}
@media(min-width:1000px){.spec{grid-template-columns:1.4fr .8fr .8fr}}
.spec__col{background:var(--bg-2);border-radius:var(--radius);padding:32px 26px;
  transition:box-shadow .5s,transform .5s cubic-bezier(.16,1,.3,1)}
.spec__col:hover{box-shadow:0 20px 50px rgba(28,26,23,.1);transform:translateY(-4px)}
.spec__col h3{font-family:var(--font-head);font-size:1.4rem;margin-bottom:20px}
.spec__col li{display:flex;gap:11px;padding:8px 0;font-size:14.5px;font-weight:300;line-height:1.55;
  border-bottom:1px solid rgba(28,26,23,.06)}
.spec__col li:last-child{border:0}
.spec__col svg{flex:0 0 16px;margin-top:4px;color:var(--accent)}
.spec--out svg{color:var(--muted)}
.spec--out li{color:var(--muted)}

/* Процесс — зигзаг */
.step{display:grid;gap:26px;align-items:center;padding:clamp(34px,5vw,64px) 0;border-top:1px solid var(--line)}
@media(min-width:900px){.step{grid-template-columns:1fr 1fr;gap:64px}
  .step:nth-child(even) .step__m{order:-1}}
.step__m{border-radius:var(--radius);overflow:hidden;aspect-ratio:4/3}
.step__m img{width:100%;height:100%;object-fit:cover;transform:scale(1.1) translate3d(0,var(--par,0),0)}
.step__n{font-family:var(--font-head);font-size:clamp(3rem,7vw,5.6rem);line-height:.8;color:var(--accent);
  opacity:.28;display:block;margin-bottom:16px}
.step h3{margin-bottom:14px}
.step p{color:var(--muted);font-size:15px;font-weight:300;line-height:1.72}

/* Мозаика деталей */
.mos{display:grid;gap:16px;grid-template-columns:repeat(2,1fr)}
@media(min-width:900px){.mos{grid-template-columns:repeat(4,1fr)}
  .mos figure:nth-child(1){grid-column:span 2;grid-row:span 2}
  .mos figure:nth-child(6){grid-column:span 2}}
.mos figure{margin:0;position:relative;border-radius:var(--radius);overflow:hidden;aspect-ratio:1/1;cursor:zoom-in}
@media(min-width:900px){.mos figure:nth-child(1){aspect-ratio:auto}.mos figure:nth-child(6){aspect-ratio:2/1}}
.mos img{width:100%;height:100%;object-fit:cover;transition:transform 1.2s cubic-bezier(.16,1,.3,1)}
.mos figure:hover img{transform:scale(1.07)}
.mos figcaption{position:absolute;inset:auto 0 0 0;padding:56px 18px 18px;color:#fff;font-size:13px;
  background:linear-gradient(transparent,rgba(20,18,16,.85));opacity:0;transform:translateY(10px);
  transition:.5s cubic-bezier(.16,1,.3,1)}
.mos figure:hover figcaption{opacity:1;transform:none}

/* Объекты */
.objs{display:grid;gap:20px}
@media(min-width:800px){.objs{grid-template-columns:repeat(2,1fr)}
  .objs>*:first-child{grid-column:span 2}}
.obj{position:relative;border-radius:var(--radius);overflow:hidden;aspect-ratio:16/10;display:block}
.objs>*:first-child .obj{aspect-ratio:21/9}
.obj img{width:100%;height:100%;object-fit:cover;transition:transform 1.3s cubic-bezier(.16,1,.3,1)}
.obj:hover img{transform:scale(1.05)}
.obj__c{display:block;position:absolute;inset:auto 0 0 0;padding:76px 26px 26px;color:#fff;
  background:linear-gradient(transparent,rgba(20,18,16,.86))}
.obj__c h3{font-family:var(--font-head);font-size:clamp(1.3rem,2.4vw,2rem);font-weight:500}
.obj__c p{font-size:14px;opacity:.82;margin-top:6px;font-weight:300}

/* До / после */
.ba-wrap{display:grid;gap:36px;align-items:center}
@media(min-width:1000px){.ba-wrap{grid-template-columns:.85fr 1.15fr;gap:64px}}

/* Заявка */
.cta{background:var(--ink);color:#F7F4EF;border-radius:clamp(16px,3vw,32px);
  padding:clamp(38px,6vw,80px);position:relative;overflow:hidden;
  --muted:rgba(247,244,239,.62);--line:rgba(247,244,239,.2);--fg:#F7F4EF;--input-bg:rgba(255,255,255,.05);--accent:#D9B87C}
.cta::after{content:"";position:absolute;width:52vw;aspect-ratio:1;border-radius:50%;right:-14vw;top:-24vw;
  background:radial-gradient(circle,rgba(217,184,124,.24),transparent 66%);animation:fl 20s ease-in-out infinite alternate}
@keyframes fl{to{transform:translate3d(-14vw,16vw,0) scale(1.2)}}
.cta__in{position:relative;display:grid;gap:40px}
@media(min-width:960px){.cta__in{grid-template-columns:1fr 1fr;gap:70px;align-items:center}}
.cta .h2{color:#F7F4EF}
.cta form{display:grid;gap:15px}
.cta .btn--fill{background:var(--accent);color:var(--ink)}
.cta .btn--fill::before{background:#F7F4EF}
.cta .kicker{color:var(--accent);border-color:var(--line)}

/* Подвал */
.foot{padding:70px 0 36px}
.foot__grid{display:grid;gap:36px}
@media(min-width:800px){.foot__grid{grid-template-columns:1.5fr 1fr 1fr 1fr}}
.foot h4{font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:var(--muted);margin-bottom:16px}
.foot p{font-size:15px;margin-bottom:9px;font-weight:300}
.foot a:hover{color:var(--accent)}
.foot__bot{margin-top:48px;padding-top:22px;border-top:1px solid var(--line);display:flex;
  flex-wrap:wrap;gap:12px;justify-content:space-between;font-size:12px;color:var(--muted)}
"""

def ic(p, c="currentColor"):
    return f'<svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="{c}" stroke-width="1.6" stroke-linecap="round" aria-hidden="true">{p}</svg>'
CHECK = ic('<path d="M2.5 8.5l3.5 3.5 7.5-8"/>')
MINUS = ic('<path d="M3 8h10"/>')
PLUS = ic('<path d="M8 3v10M3 8h10"/>')
ARR = '<svg width="16" height="10" viewBox="0 0 18 10" fill="none" stroke="currentColor" stroke-width="1.4" aria-hidden="true"><path d="M0 5h16M12 1l4 4-4 4"/></svg>'

TICK = ('<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2.6" '
        'stroke-linecap="round" aria-hidden="true"><path d="M2.5 8.5l3.5 3.5 7.5-8"/></svg>')

# Наценки и ставки — заглушки, замените на свои перед публикацией
PACKS = [("Базовая", "по списку комплектации", 1.0),
         ("Расширенная", "фанера на стенах, кашировка рам", 1.12),
         ("Премиум", "полная отделка и сантехника", 1.25)]
COPTS = [("Система кондиционирования", 90000), ("Система тёплого пола", 110000),
         ("Сантехнические приборы", 75000), ("Светодиодные подсветки", 45000),
         ("Мебель и предметы интерьера", 250000), ("Внутренняя отделка стен фанерой", 85000)]
FOUND = [("Винтовые сваи", "подходит большинству участков", 180000),
         ("Бетонные сваи", "для сложных грунтов", 260000),
         ("Фундамент уже есть", "не считаем", 0)]
MONTAGE = 120000      # монтаж краном на участке
PER_KM = 90           # доставка тралом, ₽ за км
# Реальный порядок оплаты по договору
SCHEDULE = [(30, "Аванс при заключении договора", "цена фиксируется и больше не меняется"),
            (40, "Через две недели", "дом уходит в производство"),
            (15, "После приёмки на производстве", "перед отгрузкой на трал"),
            (15, "После монтажа на участке", "когда получаете ключи")]

CALC_JS = r"""
/* --- Калькулятор стоимости и график платежей --- */
(function(){
  var root = document.getElementById('calc'); if(!root) return;
  var total = root.querySelector('[data-total]'),
      sub   = root.querySelector('[data-sub]'),
      km    = root.querySelector('[data-km]'),
      kmOut = root.querySelector('[data-km-out]'),
      pays  = root.querySelectorAll('[data-pay]'),
      houseOut = root.querySelector('[data-house-sum]');
  var MONTAGE = MONTAGE_PLACEHOLDER, PER_KM = PERKM_PLACEHOLDER;
  var RM = window.matchMedia('(prefers-reduced-motion: reduce)');
  var shown = {};   /* что сейчас на экране — от этих значений считаем следующий пересчёт */

  function money(n){ return Math.round(n).toLocaleString('ru-RU') + ' ₽'; }

  /* Одна анимация на все суммы сразу: итог и четыре платежа идут синхронно. */
  var tween = null;
  function animate(targets){
    if(tween) cancelAnimationFrame(tween);
    if(RM.matches){
      targets.forEach(function(t){ t.el.textContent = money(t.to); shown[t.key] = t.to; });
      return;
    }
    var t0 = null;
    /* первый кадр только через rAF: при прямом вызове t === undefined и получится NaN */
    tween = requestAnimationFrame(function step(t){
      if(t0 === null) t0 = t;
      var q = Math.min((t - t0) / 520, 1), e = 1 - Math.pow(1 - q, 3);
      targets.forEach(function(x){
        var v = x.from + (x.to - x.from) * e;
        x.el.textContent = money(v);
        shown[x.key] = v;
      });
      if(q < 1) tween = requestAnimationFrame(step); else tween = null;
    });
  }

  function pick(sel, el){
    root.querySelectorAll(sel).forEach(function(x){ x.classList.remove('on'); });
    el.classList.add('on');
    calc();
  }
  ['[data-model]', '[data-pack]', '[data-found]'].forEach(function(sel){
    root.querySelectorAll(sel).forEach(function(x){
      x.addEventListener('click', function(){ pick(sel, x); });
    });
  });
  root.querySelectorAll('.copt input').forEach(function(x){ x.addEventListener('change', calc); });
  if(km) km.addEventListener('input', calc);

  function calc(){
    var m = root.querySelector('[data-model].on'),
        pk = root.querySelector('[data-pack].on'),
        f  = root.querySelector('[data-found].on');

    var withPack = parseFloat(m.dataset.price) * parseFloat(pk.dataset.k);
    var add = 0, names = [];
    root.querySelectorAll('.copt input:checked').forEach(function(x){
      add += parseFloat(x.value); names.push(x.dataset.name);
    });
    /* договор на дом — по нему и считается график 30/40/15/15 */
    var house = withPack + add;
    var d = km ? +km.value : 0;
    var log = MONTAGE + d * PER_KM;
    var foundation = parseFloat(f.dataset.price);
    var sum = house + foundation + log;

    sub.textContent = m.dataset.name + ' · комплектация «' + pk.dataset.name + '»' +
                      (names.length ? ' · опций: ' + names.length : '');
    root.querySelector('[data-r-house]').textContent = money(withPack);
    root.querySelector('[data-r-opts]').textContent  = names.length ? names.length + ' шт · ' + money(add) : '—';
    root.querySelector('[data-r-found]').textContent = foundation ? money(foundation) : f.dataset.name;
    root.querySelector('[data-r-log]').textContent   = money(log) + ' · ' + d + ' км';
    if(kmOut) kmOut.textContent = d + ' км';
    if(houseOut) houseOut.textContent = money(house);

    var extraSum = foundation + log;
    var extraEl = root.querySelector('[data-extra]');

    var targets = [{key: 'total', el: total, from: shown.total || 0, to: sum}];
    var values = [];
    pays.forEach(function(el, i){
      var v = house * (+el.dataset.pay) / 100;
      values.push(v);
      targets.push({key: 'pay' + i, el: el, from: shown['pay' + i] || 0, to: v});
    });
    values.push(extraSum);
    if(extraEl) targets.push({key: 'extra', el: extraEl, from: shown.extra || 0, to: extraSum});
    animate(targets);

    /* Шкала = доля платежа во всей смете. Она меняется от любой настройки:
       график по договору считается от дома, а фундамент и доставка идут отдельно. */
    root.querySelectorAll('.pay__bar').forEach(function(bar, i){
      bar.style.setProperty('--k', sum ? (values[i] / sum).toFixed(4) : 0);
    });
  }

  /* расчёт уезжает в заявку — человеку не нужно ничего описывать словами */
  var send = root.querySelector('[data-send-calc]');
  if(send) send.addEventListener('click', function(){
    var box = document.querySelector('#cta textarea'); if(!box) return;
    var lines = ['Расчёт с сайта — ' + total.textContent, sub.textContent, ''];
    root.querySelectorAll('.calc__rows div').forEach(function(r){
      lines.push(r.querySelector('span').textContent + ': ' + r.querySelector('b').textContent);
    });
    lines.push('');
    root.querySelectorAll('.pay__row').forEach(function(r){
      var pc = r.querySelector('.pay__pc').textContent.trim();
      var name = r.querySelector('.pay__t b').textContent.trim();
      /* у строки «вне договора» вместо доли стоит пометка — её в текст не тащим */
      lines.push((/%$/.test(pc) ? pc + ' — ' : '') + name + ': ' +
                 r.querySelector('.pay__v').textContent);
    });
    box.value = lines.join('\n');
    setTimeout(function(){
      var n = document.querySelector('#cta input[type="text"]');
      if(n) n.focus();
    }, 700);
  });

  calc();
})();
"""

def build():
    b = BRAND
    # калькулятор есть только на этой странице, поэтому пункт добавляем локально
    menu = NAV[:1] + [("#calc", "Калькулятор")] + NAV[1:]
    nav = "".join(f'<a href="{h}">{t}</a>' for h, t in menu)
    o = [core.head("ДОММ — модульные дома под ключ | Новосибирск",
                   "Модульные дома с террасой под ключ от 990 000 ₽ за 30 дней. Собственное производство, 80+ проектов.",
                   FONTS, CSS, "#F7F4EF")]
    o.append('<div class="paper"></div><div class="cursor"></div>')
    o.append(f"""
<header class="hdr" data-header><div class="wrap hdr__in">
  <a class="logo" href="#top">DOM<em>M</em></a>
  <nav class="nav">{nav}</nav>
  <a class="btn btn--fill hdr__cta" href="tel:{b['phone2_href']}" data-magnet=".25">Заказать расчёт</a>
  <button class="burger" data-burger aria-label="Меню" aria-expanded="false"><i></i><i></i><i></i></button>
</div></header>
<nav class="mnav" data-menu>{nav}
  <div class="mnav__foot"><a href="tel:{b['phone1_href']}">{b['phone1']}</a>
  <a href="tel:{b['phone2_href']}">{b['phone2']}</a><a href="mailto:{b['email']}">{b['email']}</a></div>
</nav>""")

    o.append(f"""
<section class="hero" id="top"><div class="wrap">
  <div class="hero__t" data-rv="up">
    <span class="kicker">{HERO['kicker']}</span>
    <h1 class="h1" data-split="line">Модульные дома<br>для <span class="it">жизни</span> и отдыха</h1>
    <p class="lead hero__sub">{HERO['sub']} {HERO['sub2']}</p>
    <div class="hero__acts">
      <a class="btn btn--fill" href="#calc" data-magnet=".3">Рассчитать стоимость {ARR}</a>
      <a class="btn btn--ghost" href="#projects">Смотреть проекты</a>
    </div>
  </div>
  <div class="hero__frame" data-rv="mask">
    <img src="{HERO['bg']}" alt="Модульный дом ДОММ с террасой" data-par="40">
    <div class="hero__badge"><b>80+</b> реализованных проектов</div>
  </div>
</div></section>""")

    nums = "".join(f'<div><b>{v}</b><span>{t}</span></div>' for v, t in STATS)
    o.append(f'<section class="sec" style="padding-top:clamp(48px,6vw,80px)"><div class="wrap">'
             f'<div class="nums" data-rv="up">{nums}</div></div></section>')

    figs = "".join(f'<figure data-lb="g" data-full="{u}" data-cap="Дом ДОММ"><img src="{u}" alt="Модульный дом ДОММ" loading="lazy"></figure>'
                   for u in GALLERY)
    o.append(f"""
<section class="sec" id="gallery" style="padding-top:0">
  <div class="wrap sec-head split">
    <div data-rv="up"><span class="kicker">Галерея</span>
      <h2 class="h2" style="margin-top:20px" data-split="line">Декорируем дома<br>в <span class="it">уютном</span> стиле</h2></div>
    <p class="lead" data-rv="up" style="--d:150ms">Тёплое дерево, мягкий свет и панорамные окна.
    Потяните ленту вбок или нажмите на снимок.</p>
  </div>
  <div class="gal" data-drag>{figs}</div>
</section>""")

    cards = "".join(f"""
    <article class="card" data-rv="up">
      <div class="card__img"><span class="card__area">{area}</span><img src="{im}" alt="{n}" loading="lazy"></div>
      <div class="card__b"><h3 class="h3">{n}</h3><p>{d}</p>
        <div class="card__p"><b>от {p} ₽</b><span>под ключ</span></div>
        <a class="btn btn--ghost" href="#cta" style="margin-top:12px;justify-self:start">Узнать подробнее {ARR}</a>
      </div>
    </article>""" for n, d, p, area, im in PROJECTS)
    o.append(f"""
<section class="sec" id="projects" style="background:var(--bg-3)">
  <div class="wrap">
    <div class="sec-head split">
      <div data-rv="up"><span class="kicker">Каталог</span>
        <h2 class="h2" style="margin-top:20px" data-split="line">Проекты домов<br>и <span class="it">бань</span></h2></div>
      <p class="lead" data-rv="up" style="--d:150ms">Семь базовых моделей и две бани — любую адаптируем
      под ваш участок и сценарий жизни.</p>
    </div>
    <div class="cards" data-stagger="90">{cards}</div>
  </div>
</section>""")

    models = "".join(f"""
      <button class="chip{' on' if i == 0 else ''}" data-model data-price="{p.replace(' ', '')}"
              data-name="{n}" type="button">{n}<small>{area} · от {p} ₽</small></button>"""
        for i, (n, d, p, area, im) in enumerate(PROJECTS))
    packs = "".join(f"""
      <button class="chip{' on' if i == 0 else ''}" data-pack data-k="{k}" data-name="{n}"
              type="button">{n}<small>{d}</small></button>"""
        for i, (n, d, k) in enumerate(PACKS))
    copts = "".join(f"""
      <label class="copt"><input type="checkbox" value="{pr}" data-name="{n}"><span class="bx">{TICK}</span>
        <span class="t">{n}</span><b>+{pr:,} ₽</b></label>""".replace(",", " ")
        for n, pr in COPTS)
    founds = "".join(f"""
      <button class="chip{' on' if i == 0 else ''}" data-found data-price="{pr}" data-name="{n}"
              type="button">{n}<small>{d}</small></button>"""
        for i, (n, d, pr) in enumerate(FOUND))
    # шкалу задаёт скрипт: она показывает долю платежа во всей смете,
    # а эта доля меняется от модели, опций, фундамента и расстояния
    pays = "".join(f"""
      <div class="pay__row">
        <span class="pay__pc">{pc}%</span>
        <span class="pay__t"><b>{t}</b><span>{d}</span></span>
        <span class="pay__v" data-pay="{pc}">—</span>
        <i class="pay__bar" aria-hidden="true"></i>
      </div>""" for pc, t, d in SCHEDULE)
    pays += """
      <div class="pay__row pay__row--extra">
        <span class="pay__pc">вне</span>
        <span class="pay__t"><b>Фундамент, доставка и монтаж</b>
          <span>оплачиваются отдельно от договора на дом</span></span>
        <span class="pay__v" data-extra>—</span>
        <i class="pay__bar" aria-hidden="true"></i>
      </div>"""

    o.append(f"""
<section class="sec" id="calc">
  <div class="wrap">
    <div class="sec-head split">
      <div data-rv="up"><span class="kicker">Калькулятор</span>
        <h2 class="h2" style="margin-top:20px" data-split="line">Соберите свой дом<br>и узнайте <span class="it">цену</span></h2></div>
      <p class="lead" data-rv="up" style="--d:150ms">Выберите модель, комплектацию и опции, добавьте
      фундамент и расстояние до участка. Стоимость пересчитывается сразу, а рядом видно,
      сколько и когда платить по договору.</p>
    </div>
    <div class="calc">
      <div class="calc__panel" data-rv="up">
        <div class="grp"><span class="gt"><b>Модель дома</b><span>1 из 4</span></span>
          <div class="chips">{models}</div></div>
        <div class="grp"><span class="gt"><b>Комплектация</b><span>2 из 4</span></span>
          <div class="chips">{packs}</div></div>
        <div class="grp"><span class="gt"><b>Дополнительные опции</b><span>3 из 4</span></span>
          <div class="copts">{copts}</div></div>
        <div class="grp"><span class="gt"><b>Фундамент и доставка</b><span>4 из 4</span></span>
          <div class="chips">{founds}</div>
          <div class="rng">
            <div class="rng__top"><span>Расстояние до участка</span><b data-km-out>50 км</b></div>
            <input type="range" data-km min="0" max="1500" value="50" step="10"
                   aria-label="Расстояние до участка в километрах">
          </div>
        </div>
      </div>

      <aside class="calc__sum" data-rv="up" style="--d:120ms">
        <span class="cap">Под ключ с монтажом на участке</span>
        <div class="calc__total" data-total>1 294 500 ₽</div>
        <p class="calc__sub" data-sub>MODUL HOUSE 1 · комплектация «Базовая»</p>
        <div class="calc__rows">
          <div><span>Дом с комплектацией</span><b data-r-house>—</b></div>
          <div><span>Опции</span><b data-r-opts>—</b></div>
          <div><span>Фундамент</span><b data-r-found>—</b></div>
          <div><span>Доставка и монтаж</span><b data-r-log>—</b></div>
        </div>
        <div class="pay"><span class="cap">Как распределяется смета<em>четыре платежа по договору на дом · <b data-house-sum>—</b> · полоса — доля во всей смете</em></span>{pays}</div>
        <p class="calc__note">Расчёт ориентировочный — точную смету пришлём после разговора.</p>
        <a class="btn btn--fill" href="#cta" data-send-calc>Зафиксировать расчёт {ARR}</a>
      </aside>
    </div>
  </div>
</section>""")

    def rows(items, key):
        return "".join(f"""
      <div class="prow" data-lb="{key}" data-full="{im}" data-cap="{n} — {a}, от {p} тыс. ₽" data-rv="up">
        <span class="prow__l"><span class="prow__n">{n}</span>
          <span class="prow__m">{a}{' · ' + note if note else ''}</span></span>
        <span style="display:flex;align-items:center;gap:18px">
          <span class="prow__th"><img src="{im}" alt="Планировка {n}" loading="lazy"></span>
          <span class="prow__p">от {p} тыс. ₽</span></span>
      </div>""" for n, a, p, im, note in items)
    o.append(f"""
<section class="sec" id="prices">
  <div class="wrap" data-tabs>
    <div class="sec-head split">
      <div data-rv="up"><span class="kicker">Планировки и цены</span>
        <h2 class="h2" style="margin-top:20px" data-split="line">Выберите свой <span class="it">метраж</span></h2></div>
      <p class="lead" data-rv="up" style="--d:150ms">Дома собираются из модулей 2,5×6 м и 3×6 м.
      Наведите на строку, чтобы увидеть планировку, нажмите — чтобы открыть крупно.</p>
    </div>
    <div class="tabs" role="tablist">
      <button data-tab="a" class="active" role="tab" aria-selected="true">Модули 2,5 × 6</button>
      <button data-tab="b" role="tab" aria-selected="false">Модули 3 × 6</button>
    </div>
    <div class="plist" data-panel="a">{rows(PLANS_25,'p25')}</div>
    <div class="plist" data-panel="b" hidden>{rows(PLANS_36,'p36')}</div>
  </div>
</section>""")

    rend = "".join(f"""
    <article class="card" data-lb="rn" data-full="{im}" data-cap="{n}" style="cursor:zoom-in">
      <div class="card__img"><img src="{im}" alt="{n}" loading="lazy"></div>
      <div class="card__b"><h3 class="h3">{n}</h3><p>{d}</p></div>
    </article>""" for n, d, im in RENDERS)
    o.append(f"""
<section class="sec" style="padding-top:0"><div class="wrap">
  <div class="sec-head" data-rv="up"><span class="kicker">Визуализации</span>
    <h2 class="h2" style="margin-top:20px">Как это <span class="it">выглядит</span></h2></div>
  <div class="cards" data-stagger="80">{rend}</div>
</div></section>""")

    li_in = "".join(f'<li>{CHECK}<span>{t}</span></li>' for t in INCLUDED)
    li_out = "".join(f'<li>{MINUS}<span>{t}</span></li>' for t in EXCLUDED)
    li_op = "".join(f'<li>{PLUS}<span>{t}</span></li>' for t in OPTIONS)
    o.append(f"""
<section class="sec" id="spec" style="background:var(--bg-3)"><div class="wrap">
  <div class="sec-head split">
    <div data-rv="up"><span class="kicker">Комплектация</span>
      <h2 class="h2" style="margin-top:20px" data-split="line">Что входит<br>в <span class="it">базовую</span> стоимость</h2></div>
    <p class="lead" data-rv="up" style="--d:150ms">Честный список без звёздочек: что вы получаете сразу,
    что оплачивается отдельно и что можно добавить.</p>
  </div>
  <div class="spec" data-stagger="110">
    <div class="spec__col"><h3>Входит в стоимость</h3><ul>{li_in}</ul></div>
    <div class="spec__col spec--out"><h3>Не входит</h3><ul>{li_out}</ul></div>
    <div class="spec__col"><h3>Дополнительные опции</h3><ul>{li_op}</ul></div>
  </div>
</div></section>""")

    steps = "".join(f"""
    <article class="step" data-rv="up">
      <div><span class="step__n">{n}</span><h3 class="h2" style="font-size:clamp(1.4rem,2.6vw,2.1rem)">{t}</h3><p>{d}</p></div>
      <div class="step__m"><img src="{im}" alt="{t}" loading="lazy" data-par="34"></div>
    </article>""" for n, t, d, im in PROCESS)
    o.append(f"""
<section class="sec" id="process"><div class="wrap">
  <div class="sec-head" data-rv="up"><span class="kicker">Как мы работаем</span>
    <h2 class="h2" style="margin-top:20px">Четыре шага до <span class="it">новоселья</span></h2></div>
  {steps}
</div></section>""")

    mos = "".join(f'<figure data-lb="d" data-full="{im}" data-cap="{t}"><img src="{im}" alt="{t}" loading="lazy"><figcaption>{t}</figcaption></figure>'
                  for t, im in DETAILS + INTERIOR)
    o.append(f"""
<section class="sec" id="details" style="background:var(--bg-3)"><div class="wrap">
  <div class="sec-head split">
    <div data-rv="up"><span class="kicker">Black Paket</span>
      <h2 class="h2" style="margin-top:20px" data-split="line">Детали в едином<br><span class="it">чёрном</span> стиле</h2></div>
    <p class="lead" data-rv="up" style="--d:150ms">Электрощит, розетки, выключатели, светильники и дверные ручки —
    всё в одном оформлении.</p>
  </div>
  <div class="mos" data-stagger="80">{mos}</div>
</div></section>""")

    objs = "".join(f"""
    <div><a class="obj" href="#cta"><img src="{im}" alt="{t}" loading="lazy">
      <span class="obj__c"><h3>{t}</h3><p>{d}</p></span></a></div>""" for t, d, im in OBJECTS)
    o.append(f"""
<section class="sec" id="objects"><div class="wrap">
  <div class="sec-head" data-rv="up"><span class="kicker">Наши дома</span>
    <h2 class="h2" style="margin-top:20px">Реализованные <span class="it">объекты</span></h2></div>
  <div class="objs" data-stagger="90">{objs}</div>
</div></section>""")

    o.append(f"""
<section class="sec" style="background:var(--bg-3)"><div class="wrap ba-wrap">
  <div data-rv="up"><span class="kicker">Посмотрите разницу</span>
    <h2 class="h2" style="margin:20px 0 18px" data-split="line">Ваш дом у нас —<br>и ваш дом <span class="it">у вас</span></h2>
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
    <span class="kicker">Свяжитесь с нами</span>
    <h2 class="h2" style="margin:20px 0 18px">Оставьте заявку и получите <span class="it" style="color:var(--accent)">расчёт</span></h2>
    <p class="lead">Подберём планировку под участок и посчитаем стоимость с доставкой и монтажом.</p>
    <div style="margin-top:28px;display:grid;gap:8px;font-family:var(--font-head);font-size:1.5rem">
      <a href="tel:{b['phone1_href']}">{b['phone1']}</a>
      <a href="tel:{b['phone2_href']}">{b['phone2']}</a>
    </div>
  </div>
  <form data-form novalidate>
    <div class="f-row two">
      <div class="field"><label for="n2">Ваше имя</label>
        <input id="n2" type="text" required autocomplete="name" placeholder="Иван"><span class="err">Укажите имя</span></div>
      <div class="field"><label for="t2">Телефон</label>
        <input id="t2" type="tel" required autocomplete="tel" inputmode="tel" placeholder="+7 (___) ___-__-__">
        <span class="err">Введите номер полностью</span></div>
    </div>
    <div class="field"><label for="m2">Комментарий</label>
      <textarea id="m2" rows="3" placeholder="Интересует MODUL HOUSE 3, участок в Бердске"></textarea></div>
    <button class="btn btn--fill" type="submit" data-magnet=".2" style="justify-self:start">Отправить заявку {ARR}</button>
    <p class="form-note">Нажимая кнопку, вы соглашаетесь с обработкой персональных данных.</p>
    <div class="form-ok" role="status">Спасибо! Заявка принята — мы перезвоним в рабочее время.</div>
  </form>
</div></div></div></section>""")

    o.append(f"""
<footer class="foot" id="contacts"><div class="wrap">
  <div class="foot__grid">
    <div data-rv="up"><a class="logo" href="#top">DOM<em>M</em></a>
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
    o.append(core.tail(CALC_JS.replace('MONTAGE_PLACEHOLDER', str(MONTAGE))
                               .replace('PERKM_PLACEHOLDER', str(PER_KM))))
    return "".join(o)
