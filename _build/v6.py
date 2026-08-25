# -*- coding: utf-8 -*-
"""Вариант 6 — ЧЕРТЁЖ. Архитектурная подача: сетка листа, самоотрисовка линий,
подбор дома двумя ползунками с живой фильтрацией планировок."""
import math

import core
from data import *

FONTS = ('<link href="https://fonts.googleapis.com/css2?'
         'family=Manrope:wght@200;300;400;500;600;700;800&'
         'family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">')

CSS = r"""
:root{
  --bg:#F4F5F2; --bg-2:#FFFFFF; --bg-3:#E9EBE6; --fg:#101418; --muted:#59636E;
  --line:rgba(16,20,24,.13); --hair:rgba(16,20,24,.07);
  --accent:#1B4FD8; --dim:#C4362F; --on-accent:#FFFFFF; --input-bg:#FFFFFF;
  --font-head:'Manrope',system-ui,sans-serif; --font-body:'Manrope',system-ui,sans-serif;
  --font-mono:'IBM Plex Mono',ui-monospace,monospace;
  --radius:4px; --radius-sm:3px; --head-weight:300;
}
::selection{background:var(--accent);color:#fff}
/* сетка листа */
.sheet{position:fixed;inset:0;z-index:-1;pointer-events:none;
  background-image:linear-gradient(var(--hair) 1px,transparent 1px),
                   linear-gradient(90deg,var(--hair) 1px,transparent 1px);
  background-size:44px 44px;mask-image:linear-gradient(180deg,#000 0 62%,transparent)}
.h1{font-size:clamp(2.6rem,7vw,6rem);font-weight:200;line-height:.94;letter-spacing:-.045em}
.h2{font-size:clamp(1.9rem,4.2vw,3.4rem);font-weight:200;line-height:1;letter-spacing:-.035em}
.h3{font-size:clamp(1.05rem,1.8vw,1.3rem);font-weight:600;letter-spacing:-.015em}
.mono{font-family:var(--font-mono);font-size:11px;letter-spacing:.1em;text-transform:uppercase}
.lead{color:var(--muted);font-size:clamp(1rem,1.2vw,1.08rem);max-width:58ch;line-height:1.7;font-weight:300}
.sec{padding:clamp(60px,7.5vw,120px) 0;position:relative}
.sec+.sec{border-top:1px solid var(--line)}
/* колонтитул листа */
.sheet-no{display:flex;align-items:center;gap:14px;margin-bottom:26px;color:var(--muted)}
.sheet-no b{font-family:var(--font-mono);font-size:11px;letter-spacing:.14em;color:var(--accent);font-weight:600}
.sheet-no i{flex:1;height:1px;background:var(--line);display:block}
.sec-head{display:grid;gap:20px;margin-bottom:clamp(32px,4vw,56px)}
@media(min-width:900px){.sec-head.split{grid-template-columns:1.15fr .85fr;align-items:end;gap:48px}}

/* шапка */
.hdr{position:fixed;inset:0 0 auto 0;z-index:100;background:rgba(244,245,242,.86);
  backdrop-filter:blur(14px);border-bottom:1px solid transparent;transition:.45s cubic-bezier(.16,1,.3,1)}
.hdr.stuck{border-bottom-color:var(--line)}
.hdr.hide{transform:translateY(-102%)}
.hdr__in{display:flex;align-items:center;justify-content:space-between;gap:20px;padding:14px 0}
.logo{display:flex;align-items:center;gap:11px;font-weight:700;font-size:19px;letter-spacing:-.03em}
.logo i{width:16px;height:16px;border:1.5px solid var(--accent);display:block;position:relative}
.logo i::after{content:"";position:absolute;inset:3px;background:var(--accent)}
.nav{display:none;gap:28px}
@media(min-width:1024px){.nav{display:flex}}
.nav a{font-family:var(--font-mono);font-size:11px;letter-spacing:.1em;text-transform:uppercase;
  color:var(--muted);position:relative;padding:4px 0;transition:color .3s}
.nav a::after{content:"";position:absolute;left:0;right:0;bottom:0;height:1px;background:var(--accent);
  transform:scaleX(0);transform-origin:0 50%;transition:transform .45s cubic-bezier(.16,1,.3,1)}
.nav a:hover{color:var(--fg)}.nav a:hover::after{transform:scaleX(1)}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:9px;padding:14px 24px;
  font-family:var(--font-mono);font-size:11px;letter-spacing:.1em;text-transform:uppercase;font-weight:500;
  border-radius:var(--radius);position:relative;overflow:hidden;isolation:isolate;
  transform:translate3d(var(--tx,0),var(--ty,0),0);
  transition:transform .4s cubic-bezier(.16,1,.3,1),color .3s,border-color .3s}
.btn--fill{background:var(--accent);color:#fff}
.btn--fill::before{content:"";position:absolute;inset:0;z-index:-1;background:var(--fg);
  transform:translateY(101%);transition:transform .45s cubic-bezier(.16,1,.3,1)}
.btn--fill:hover::before{transform:none}
.btn--ghost{border:1px solid var(--line);color:var(--fg)}
.btn--ghost:hover{border-color:var(--accent);color:var(--accent)}
.hdr__cta{display:none}@media(min-width:640px){.hdr__cta{display:inline-flex}}
.burger{display:grid;gap:5px;padding:10px;margin:-10px}
@media(min-width:1024px){.burger{display:none}}
.burger i{width:22px;height:1.5px;background:var(--fg);transition:.4s}
body.nav-open .burger i:nth-child(1){transform:translateY(6.5px) rotate(45deg)}
body.nav-open .burger i:nth-child(2){opacity:0}
body.nav-open .burger i:nth-child(3){transform:translateY(-6.5px) rotate(-45deg)}
.mnav{position:fixed;inset:0;z-index:99;background:var(--bg);display:grid;align-content:center;gap:2px;
  padding:0 var(--gutter);opacity:0;visibility:hidden;transition:.4s}
body.nav-open .mnav{opacity:1;visibility:visible}
.mnav a{font-size:clamp(2rem,9vw,3.2rem);font-weight:200;letter-spacing:-.04em;padding:8px 0;
  border-bottom:1px solid var(--line);opacity:0;transform:translateX(-20px);
  transition:.55s cubic-bezier(.16,1,.3,1)}
body.nav-open .mnav a{opacity:1;transform:none}
.mnav a:nth-child(1){transition-delay:.05s}.mnav a:nth-child(2){transition-delay:.1s}
.mnav a:nth-child(3){transition-delay:.15s}.mnav a:nth-child(4){transition-delay:.2s}
.mnav a:nth-child(5){transition-delay:.25s}
.mnav__foot{margin-top:26px;font-family:var(--font-mono);font-size:13px;display:grid;gap:6px;color:var(--muted)}

/* герой */
.hero{padding:110px 0 0}
.hero__top{display:grid;gap:26px}
@media(min-width:1000px){.hero__top{grid-template-columns:1.25fr .75fr;align-items:end;gap:48px}}
.hero__acts{display:flex;gap:12px;flex-wrap:wrap;margin-top:26px}
.hero__spec{display:grid;gap:0;border-top:1px solid var(--line)}
.hero__spec div{display:flex;justify-content:space-between;gap:16px;padding:11px 0;
  border-bottom:1px solid var(--hair);font-family:var(--font-mono);font-size:12px}
.hero__spec span{color:var(--muted);letter-spacing:.06em;text-transform:uppercase;font-size:10.5px}
.hero__spec b{font-weight:500;letter-spacing:-.01em}
/* чертёж */
.draw{margin-top:clamp(30px,4vw,52px);display:grid;gap:26px}
@media(min-width:1000px){.draw{grid-template-columns:1fr 268px;gap:40px;align-items:center}}
.draw svg{width:100%;height:auto;display:block;overflow:visible}
.draw path,.draw circle{fill:none;stroke:var(--fg);stroke-width:1.4;
  stroke-linecap:square;stroke-linejoin:miter;vector-effect:non-scaling-stroke}
.draw .thin{stroke-width:.8;stroke:var(--muted)}
.draw .glass{stroke:var(--accent);stroke-width:1.4}
.draw .glass.thin{stroke-width:.8}
.draw .dimen{stroke:var(--dim);stroke-width:.9}
.draw .dimen.fill{fill:var(--dim);stroke:none}
.draw .dimen.thin{stroke:var(--dim);opacity:.55}
.draw .calls circle{fill:var(--bg);stroke:var(--accent);stroke-width:1.3}
.draw .calls .lead{stroke:var(--accent);stroke-width:.8}
.draw .calls text{font-family:var(--font-mono);font-size:15px;font-weight:600;fill:var(--accent)}
.draw .dims text{font-family:var(--font-mono);font-size:14px;fill:var(--dim);letter-spacing:.04em}
/* линии вычерчиваются по очереди */
.draw .ink path{stroke-dasharray:1;stroke-dashoffset:1;
  transition:stroke-dashoffset 1.1s cubic-bezier(.55,0,.25,1);
  transition-delay:calc(var(--i,0) * 70ms)}
.draw.in .ink path{stroke-dashoffset:0}
.draw .dim-g{opacity:0;transition:opacity .7s ease}
.draw.in .dims{opacity:1;transition-delay:1.05s}
.draw.in .calls{opacity:1;transition-delay:1.3s}
@media(max-width:639px){.draw .dims{display:none}}
@media (prefers-reduced-motion:reduce){
  .draw .ink path{stroke-dashoffset:0;transition:none}
  .draw .dim-g{opacity:1;transition:none}}
.draw__legend{display:grid;gap:0;border-top:1px solid var(--line)}
.draw__legend li{display:flex;gap:12px;padding:12px 0;border-bottom:1px solid var(--hair);
  font-size:13px;line-height:1.5;color:var(--muted);font-weight:300}
.draw__legend b{flex:0 0 24px;height:24px;border-radius:50%;border:1px solid var(--accent);
  color:var(--accent);font-family:var(--font-mono);font-size:11px;font-weight:600;
  display:grid;place-items:center}

/* подбор */
.pick{display:grid;gap:26px}
@media(min-width:1000px){.pick{grid-template-columns:340px 1fr;gap:40px;align-items:start}}
.pick__panel{border:1px solid var(--line);background:var(--bg-2);padding:26px;border-radius:var(--radius);
  position:sticky;top:88px}
@media(max-width:999px){.pick__panel{position:static}}
.rng{margin-bottom:26px}
.rng__top{display:flex;justify-content:space-between;align-items:baseline;gap:12px;margin-bottom:14px}
.rng__top span{font-family:var(--font-mono);font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}
.rng__top b{font-family:var(--font-mono);font-size:15px;font-weight:600;letter-spacing:-.02em}
input[type=range]{-webkit-appearance:none;appearance:none;width:100%;height:26px;background:transparent;cursor:pointer;margin:0}
input[type=range]::-webkit-slider-runnable-track{height:2px;background:var(--line)}
input[type=range]::-moz-range-track{height:2px;background:var(--line)}
input[type=range]::-webkit-slider-thumb{-webkit-appearance:none;width:22px;height:22px;border-radius:50%;
  background:var(--accent);border:4px solid var(--bg-2);margin-top:-10px;
  box-shadow:0 1px 6px rgba(16,20,24,.28);transition:transform .2s}
input[type=range]::-moz-range-thumb{width:22px;height:22px;border-radius:50%;background:var(--accent);
  border:4px solid var(--bg-2);box-shadow:0 1px 6px rgba(16,20,24,.28)}
input[type=range]:active::-webkit-slider-thumb{transform:scale(1.16)}
input[type=range]:focus-visible::-webkit-slider-thumb{outline:2px solid var(--accent);outline-offset:3px}
.chips{display:flex;flex-wrap:wrap;gap:7px;margin-top:12px}
.chip{padding:9px 14px;border:1px solid var(--line);border-radius:100px;font-size:12.5px;color:var(--muted);
  background:transparent;transition:.3s}
.chip:hover{color:var(--fg);border-color:var(--muted)}
.chip.on{background:var(--fg);color:var(--bg);border-color:var(--fg)}
.pick__found{margin:22px 0 18px;padding-top:18px;border-top:1px solid var(--line);
  display:flex;align-items:baseline;gap:10px}
.pick__found b{font-size:2.2rem;font-weight:200;letter-spacing:-.04em;font-variant-numeric:tabular-nums}
.pick__found span{font-family:var(--font-mono);font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
.pick__hint{font-family:var(--font-mono);font-size:11px;color:var(--muted);line-height:1.6;margin-top:14px}
.pick__grid{display:grid;gap:14px;grid-template-columns:repeat(2,1fr)}
@media(min-width:760px){.pick__grid{grid-template-columns:repeat(3,1fr)}}
@media(min-width:1280px){.pick__grid{grid-template-columns:repeat(4,1fr)}}
.pl{border:1px solid var(--line);background:var(--bg-2);border-radius:var(--radius);overflow:hidden;
  cursor:zoom-in;transition:border-color .35s,transform .45s cubic-bezier(.16,1,.3,1),box-shadow .45s;
  opacity:0;transform:translateY(14px) scale(.97)}
.pl.show{opacity:1;transform:none}
.pl.hide{display:none}
.pl:hover{border-color:var(--accent);transform:translateY(-4px);box-shadow:0 14px 34px rgba(16,20,24,.11)}
.pl__i{aspect-ratio:1/1;background:#fff;padding:11px;border-bottom:1px solid var(--hair)}
.pl__i img{width:100%;height:100%;object-fit:contain}
.pl__b{padding:14px;display:grid;gap:5px}
.pl__b h4{font-size:13px;font-weight:600;letter-spacing:-.01em}
.pl__b .m{font-family:var(--font-mono);font-size:11px;color:var(--muted)}
.pl__b .p{font-family:var(--font-mono);font-size:14px;font-weight:600;color:var(--accent);letter-spacing:-.02em}
.pick__empty{padding:40px;text-align:center;border:1px dashed var(--line);border-radius:var(--radius);color:var(--muted)}

/* карточки моделей */
.cards{display:grid;gap:18px}
@media(min-width:700px){.cards{grid-template-columns:repeat(2,1fr)}}
@media(min-width:1100px){.cards{grid-template-columns:repeat(3,1fr)}}
.card{border:1px solid var(--line);background:var(--bg-2);border-radius:var(--radius);overflow:hidden;
  transition:border-color .4s,transform .5s cubic-bezier(.16,1,.3,1),box-shadow .5s}
.card:hover{border-color:var(--accent);transform:translateY(-5px);box-shadow:0 18px 44px rgba(16,20,24,.12)}
.card__i{aspect-ratio:4/3;overflow:hidden;position:relative}
.card__i img{width:100%;height:100%;object-fit:cover;transition:transform 1.2s cubic-bezier(.16,1,.3,1)}
.card:hover .card__i img{transform:scale(1.06)}
.card__tag{position:absolute;top:12px;left:12px;background:var(--bg-2);border:1px solid var(--line);
  padding:6px 11px;font-family:var(--font-mono);font-size:10.5px;letter-spacing:.08em}
.card__b{padding:20px;display:grid;gap:8px}
.card__b p{color:var(--muted);font-size:14px;font-weight:300;min-height:42px}
.card__p{display:flex;justify-content:space-between;align-items:baseline;padding-top:14px;
  border-top:1px solid var(--hair);margin-top:4px}
.card__p b{font-family:var(--font-mono);font-size:1.15rem;font-weight:600;letter-spacing:-.03em}
.card__p span{font-family:var(--font-mono);font-size:10.5px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}

/* галерея */
.strip{display:flex;gap:14px;overflow-x:auto;scroll-snap-type:x mandatory;padding-bottom:16px;
  cursor:grab;scrollbar-width:none}
.strip::-webkit-scrollbar{display:none}
.strip.dragging{cursor:grabbing;scroll-snap-type:none}
.strip figure{margin:0;flex:0 0 clamp(250px,36vw,420px);scroll-snap-align:start;aspect-ratio:4/3;
  overflow:hidden;border-radius:var(--radius);border:1px solid var(--line)}
.strip img{width:100%;height:100%;object-fit:cover;transition:transform 1.1s cubic-bezier(.16,1,.3,1)}
.strip figure:hover img{transform:scale(1.05)}

/* комплектация */
.spec{display:grid;gap:0;border-top:1px solid var(--line);border-left:1px solid var(--line)}
@media(min-width:1000px){.spec{grid-template-columns:1.4fr .8fr .8fr}}
.spec__c{border-right:1px solid var(--line);border-bottom:1px solid var(--line);padding:26px 22px;background:var(--bg-2)}
.spec__c h3{margin-bottom:16px}
.spec__c li{display:flex;gap:10px;padding:8px 0;font-size:14px;font-weight:300;line-height:1.5;
  border-bottom:1px solid var(--hair);color:var(--muted)}
.spec__c li:last-child{border:0}
.spec__c .n{font-family:var(--font-mono);font-size:10px;color:var(--accent);flex:0 0 22px;padding-top:3px}
.spec--in li{color:var(--fg)}
.spec--out .n{color:var(--muted)}

/* процесс */
.pr{display:grid;gap:0;border-top:1px solid var(--line)}
.pstep{display:grid;gap:20px;padding:clamp(26px,3.5vw,44px) 0;border-bottom:1px solid var(--line)}
@media(min-width:900px){.pstep{grid-template-columns:88px 1fr 1fr;gap:36px;align-items:start}}
.pstep__n{font-family:var(--font-mono);font-size:11px;letter-spacing:.12em;color:var(--accent);padding-top:6px}
.pstep h3{margin-bottom:12px}
.pstep p{color:var(--muted);font-size:14.5px;font-weight:300;line-height:1.7}
.pstep__i{overflow:hidden;aspect-ratio:16/10;border:1px solid var(--line);border-radius:var(--radius)}
.pstep__i img{width:100%;height:100%;object-fit:cover;transform:scale(1.08) translate3d(0,var(--par,0),0)}

/* мозаика */
.mos{display:grid;gap:14px;grid-template-columns:repeat(2,1fr)}
@media(min-width:900px){.mos{grid-template-columns:repeat(3,1fr)}}
.mos figure{margin:0;position:relative;aspect-ratio:1/1;overflow:hidden;border-radius:var(--radius);
  border:1px solid var(--line);cursor:zoom-in}
.mos img{width:100%;height:100%;object-fit:cover;transition:transform 1.2s cubic-bezier(.16,1,.3,1)}
.mos figure:hover img{transform:scale(1.05)}
.mos figcaption{position:absolute;inset:auto 0 0 0;background:rgba(244,245,242,.94);backdrop-filter:blur(8px);
  border-top:1px solid var(--line);padding:11px 13px;font-family:var(--font-mono);font-size:10.5px;
  line-height:1.45;transform:translateY(101%);transition:transform .45s cubic-bezier(.16,1,.3,1)}
.mos figure:hover figcaption{transform:none}

/* объекты */
.objs{display:grid;gap:16px}
@media(min-width:800px){.objs{grid-template-columns:repeat(2,1fr)}
  .objs>*:first-child{grid-column:span 2}}
.obj{display:block;border:1px solid var(--line);border-radius:var(--radius);overflow:hidden;
  position:relative;transition:border-color .4s}
.obj:hover{border-color:var(--accent)}
.obj__i{aspect-ratio:16/10;overflow:hidden;display:block}
.objs>*:first-child .obj__i{aspect-ratio:21/9}
.obj img{width:100%;height:100%;object-fit:cover;transition:transform 1.3s cubic-bezier(.16,1,.3,1)}
.obj:hover img{transform:scale(1.04)}
.obj__c{display:block;padding:18px 20px;background:var(--bg-2);border-top:1px solid var(--line)}
.obj__c h3{font-size:clamp(1.1rem,2vw,1.5rem);font-weight:300;letter-spacing:-.025em}
.obj__c p{font-size:13.5px;color:var(--muted);margin-top:5px;font-weight:300}

/* до/после */
.ba{border:1px solid var(--line)}
.ba-wrap{display:grid;gap:32px;align-items:center}
@media(min-width:1000px){.ba-wrap{grid-template-columns:.8fr 1.2fr;gap:52px}}

/* заявка */
.cta{background:var(--fg);color:var(--bg);border-radius:var(--radius);padding:clamp(28px,5vw,60px);
  --muted:rgba(244,245,242,.62);--line:rgba(244,245,242,.22);--hair:rgba(244,245,242,.12);
  --fg:#F4F5F2;--input-bg:rgba(255,255,255,.06);--accent:#7FA0FF}
.cta__in{display:grid;gap:34px}
@media(min-width:960px){.cta__in{grid-template-columns:1fr 1fr;gap:56px;align-items:center}}
.cta .h2{color:var(--bg)}
.cta form{display:grid;gap:14px}
.cta .btn--fill{background:var(--accent);color:#0B1020}
.cta .btn--fill::before{background:#F4F5F2}
.cta .sheet-no b{color:var(--accent)}

/* подвал */
.foot{padding:56px 0 30px;border-top:1px solid var(--line)}
.foot__grid{display:grid;gap:30px}
@media(min-width:800px){.foot__grid{grid-template-columns:1.5fr 1fr 1fr 1fr}}
.foot h4{font-family:var(--font-mono);font-size:10.5px;letter-spacing:.12em;text-transform:uppercase;
  color:var(--muted);margin-bottom:14px}
.foot p{font-size:14.5px;margin-bottom:8px;font-weight:300}
.foot a:hover{color:var(--accent)}
.foot__bot{margin-top:40px;padding-top:18px;border-top:1px solid var(--line);display:flex;flex-wrap:wrap;
  gap:12px;justify-content:space-between;font-family:var(--font-mono);font-size:10.5px;color:var(--muted)}
"""

ARR = ('<svg width="16" height="10" viewBox="0 0 18 10" fill="none" stroke="currentColor" '
       'stroke-width="1.5" aria-hidden="true"><path d="M0 5h16M12 1l4 4-4 4"/></svg>')

# --- чертёж фасада: односкатная кровля, витраж, терраса, размеры и выноски ---
ELEVATION = """
<svg viewBox="0 0 960 440" role="img" aria-label="Чертёж фасада модульного дома: односкатная кровля, витражное остекление, терраса">
  <g class="ink">
    <path class="thin" style="--i:0" pathLength="1" d="M70 372 H910"/>
    <path style="--i:1" pathLength="1" d="M180 146 L680 198"/>
    <path style="--i:2" pathLength="1" d="M180 160 L680 212"/>
    <path style="--i:3" pathLength="1" d="M180 146 V160 M680 198 V212"/>
    <path style="--i:4" pathLength="1" d="M196 159 V372"/>
    <path style="--i:5" pathLength="1" d="M664 210 V372"/>
    <path style="--i:6" pathLength="1" d="M196 372 H664"/>
    <path class="glass" style="--i:7" pathLength="1" d="M424 236 H648 V358 H424 Z"/>
    <path class="glass thin" style="--i:8" pathLength="1" d="M498 236 V358 M573 236 V358"/>
    <path style="--i:9" pathLength="1" d="M250 258 H322 V372"/>
    <path style="--i:10" pathLength="1" d="M250 258 V372"/>
    <path class="thin" style="--i:11" pathLength="1" d="M222 165 V372 M340 177 V372 M366 180 V372 M392 183 V372"/>
    <path style="--i:12" pathLength="1" d="M664 346 H872 V356 H664"/>
    <path class="thin" style="--i:13" pathLength="1" d="M706 356 V372 M784 356 V372 M862 356 V372"/>
  </g>
  <g class="dim-g dims">
    <path class="dimen" d="M180 416 H872"/>
    <path class="dimen fill" d="M180 416 l10 -4.5 v9 z M872 416 l-10 -4.5 v9 z"/>
    <path class="dimen thin" d="M180 376 V424 M872 360 V424"/>
    <text x="526" y="408" text-anchor="middle">9 000</text>
    <path class="dimen" d="M132 146 V372"/>
    <path class="dimen fill" d="M132 146 l-4.5 10 h9 z M132 372 l-4.5 -10 h9 z"/>
    <path class="dimen thin" d="M140 146 H186 M140 372 H200"/>
    <text x="120" y="264" text-anchor="end">3 200</text>
  </g>
  <g class="dim-g calls">
    <path class="lead" d="M300 133 V171"/>
    <circle cx="300" cy="120" r="14"/><text x="300" y="125" text-anchor="middle">1</text>
    <circle cx="536" cy="297" r="14"/><text x="536" y="302" text-anchor="middle">2</text>
    <path class="lead" d="M768 332 V346"/>
    <circle cx="768" cy="318" r="14"/><text x="768" y="323" text-anchor="middle">3</text>
    <circle cx="282" cy="205" r="14"/><text x="282" y="210" text-anchor="middle">4</text>
  </g>
</svg>"""

LEGEND = [
    ("1", "Кровля односкатная, наплавляемое покрытие «Технониколь» в два слоя"),
    ("2", "Витражное остекление, двухкамерные стеклопакеты, профиль VEKA"),
    ("3", "Терраса из лиственницы с покрытием маслом"),
    ("4", "Внешняя отделка — планкен, вагонка или окрашенный металлопрофиль"),
]

def num_area(s):
    return float(s.replace(" м²", "").replace(",", ".").strip())

def num_price(s):
    return float(s.replace(" ", "").replace(" ", ""))

def build():
    b = BRAND
    legend = "".join(f'<li><b>{n}</b><span>{t}</span></li>' for n, t in LEGEND)
    nav = "".join(f'<a href="{h}">{t}</a>' for h, t in NAV)
    o = [core.head("ДОММ — модульные дома под ключ от 990 000 ₽ | Новосибирск",
                   "Подберите модульный дом по площади и бюджету: 18 планировок, цены под ключ, "
                   "собственное производство в Новосибирске.",
                   FONTS, CSS, "#F4F5F2")]
    o.append('<div class="sheet"></div><div class="cursor"></div>')

    o.append(f"""
<header class="hdr" data-header><div class="wrap hdr__in">
  <a class="logo" href="#top"><i></i>ДОММ</a>
  <nav class="nav">{nav}</nav>
  <a class="btn btn--fill hdr__cta" href="#pick" data-magnet=".25">Подобрать дом</a>
  <button class="burger" data-burger aria-label="Меню" aria-expanded="false"><i></i><i></i><i></i></button>
</div></header>
<nav class="mnav" data-menu>{nav}
  <div class="mnav__foot"><a href="tel:{b['phone1_href']}">{b['phone1']}</a>
  <a href="tel:{b['phone2_href']}">{b['phone2']}</a><a href="mailto:{b['email']}">{b['email']}</a></div>
</nav>""")

    spec_rows = "".join(f'<div><span>{t}</span><b>{v}</b></div>' for v, t in STATS)
    o.append(f"""
<section class="hero" id="top"><div class="wrap">
  <div class="sheet-no" data-rv="up"><b>ЛИСТ 01</b><i></i><span class="mono">Общие данные</span></div>
  <div class="hero__top">
    <div data-rv="up">
      <h1 class="h1" data-split="line">Модульные дома<br>для жизни и отдыха</h1>
      <p class="lead" style="margin-top:22px">{HERO['sub']} {HERO['sub2']}</p>
      <div class="hero__acts">
        <a class="btn btn--fill" href="#pick" data-magnet=".3">Подобрать по параметрам {ARR}</a>
        <a class="btn btn--ghost" href="{b['wa']}" target="_blank" rel="noopener">Написать в WhatsApp</a>
      </div>
    </div>
    <div class="hero__spec" data-rv="up" style="--d:180ms">{spec_rows}</div>
  </div>
  <div class="draw" data-rv="up" style="--d:120ms">
    {ELEVATION}
    <ol class="draw__legend">{legend}</ol>
  </div>
</div></section>""")

    # --- подбор ---
    all_plans = [(n, a, p, im, note, "2,5 × 6") for n, a, p, im, note in PLANS_25] + \
                [(n, a, p, im, note, "3 × 6") for n, a, p, im, note in PLANS_36]
    areas = [num_area(a) for _, a, _, _, _, _ in all_plans]
    prices = [num_price(p) for _, _, p, _, _, _ in all_plans]
    a_min, a_max = int(min(areas)), math.ceil(max(areas))
    p_min = int(min(prices))
    # верх ползунка должен быть кратен шагу, иначе самый дорогой дом недостижим
    P_STEP = 50
    p_max = p_min + math.ceil((max(prices) - p_min) / P_STEP) * P_STEP

    cards_pick = "".join(f"""
      <article class="pl show" data-lb="pk" data-full="{im}" data-cap="{n} — {a}, от {p} тыс. ₽"
               data-area="{num_area(a)}" data-price="{num_price(p)}" data-mod="{mod}">
        <div class="pl__i"><img src="{im}" alt="Планировка {n}" loading="lazy"></div>
        <div class="pl__b"><h4>{n}</h4><span class="m">{a} · модуль {mod}{' · ' + note if note else ''}</span>
          <span class="p">от {p} тыс. ₽</span></div>
      </article>""" for n, a, p, im, note, mod in all_plans)

    o.append(f"""
<section class="sec" id="pick"><div class="wrap">
  <div class="sheet-no" data-rv="up"><b>ЛИСТ 02</b><i></i><span class="mono">Подбор дома</span></div>
  <div class="sec-head split">
    <div data-rv="up"><h2 class="h2" data-split="line">Подберите дом<br>по площади и бюджету</h2></div>
    <p class="lead" data-rv="up" style="--d:150ms">Двигайте ползунки — подходящие планировки
    остаются на месте, остальные уходят. Нажмите на планировку, чтобы рассмотреть её крупно.</p>
  </div>
  <div class="pick">
    <div class="pick__panel" data-rv="up">
      <div class="rng">
        <div class="rng__top"><span>Площадь, м²</span><b data-out="area">любая</b></div>
        <input type="range" id="f-area" min="{a_min}" max="{a_max}" value="{a_max}" step="1"
               aria-label="Максимальная площадь, м²">
      </div>
      <div class="rng">
        <div class="rng__top"><span>Бюджет, тыс. ₽</span><b data-out="price">любой</b></div>
        <input type="range" id="f-price" min="{p_min}" max="{p_max}" value="{p_max}" step="{P_STEP}"
               aria-label="Максимальный бюджет, тысяч рублей">
      </div>
      <div>
        <div class="rng__top"><span>Ширина модуля</span></div>
        <div class="chips" role="group" aria-label="Ширина модуля">
          <button class="chip on" data-mod="all">Любая</button>
          <button class="chip" data-mod="2,5 × 6">2,5 × 6</button>
          <button class="chip" data-mod="3 × 6">3 × 6</button>
        </div>
      </div>
      <div class="pick__found"><b data-found>{len(all_plans)}</b>
        <span data-found-word>планировок подходит</span></div>
      <a class="btn btn--fill" href="#cta" data-send-pick style="width:100%">Получить подборку {ARR}</a>
      <p class="pick__hint">Пришлём PDF с подходящими планировками, ценами под ключ
      и расчётом доставки на ваш участок.</p>
    </div>
    <div>
      <div class="pick__grid" data-pick-grid>{cards_pick}</div>
      <div class="pick__empty" hidden data-pick-empty>
        Под эти параметры ничего не нашлось — попробуйте увеличить бюджет или площадь.
      </div>
    </div>
  </div>
</div></section>""")

    cards = "".join(f"""
    <article class="card" data-rv="up">
      <div class="card__i"><span class="card__tag">{area}</span><img src="{im}" alt="{n}" loading="lazy"></div>
      <div class="card__b"><h3 class="h3">{n}</h3><p>{d}</p>
        <div class="card__p"><b>от {p} ₽</b><span>под ключ</span></div>
        <a class="btn btn--ghost" href="#cta" style="margin-top:10px;justify-self:start">Подробнее {ARR}</a></div>
    </article>""" for n, d, p, area, im in PROJECTS)
    o.append(f"""
<section class="sec" id="projects"><div class="wrap">
  <div class="sheet-no" data-rv="up"><b>ЛИСТ 03</b><i></i><span class="mono">Каталог моделей</span></div>
  <div class="sec-head split">
    <div data-rv="up"><h2 class="h2">Проекты домов и бань</h2></div>
    <p class="lead" data-rv="up" style="--d:150ms">Семь базовых моделей и две бани — любую
    адаптируем под участок и сценарий жизни.</p>
  </div>
  <div class="cards" data-stagger="80">{cards}</div>
</div></section>""")

    figs = "".join(f'<figure data-lb="g" data-full="{u}" data-cap="Дом ДОММ"><img src="{u}" alt="Модульный дом ДОММ" loading="lazy"></figure>'
                   for u in GALLERY)
    o.append(f"""
<section class="sec" id="gallery"><div class="wrap">
  <div class="sheet-no" data-rv="up"><b>ЛИСТ 04</b><i></i><span class="mono">Галерея</span></div>
  <div class="sec-head split">
    <div data-rv="up"><h2 class="h2">Декорируем дома в уютном стиле</h2></div>
    <p class="lead" data-rv="up" style="--d:150ms">Тёплое дерево, чёрная фурнитура, панорамные окна.
    Потяните ленту вбок.</p>
  </div>
  <div class="strip" data-drag>{figs}</div>
</div></section>""")

    def li(items, pre):
        return "".join(f'<li><span class="n">{pre}{i+1:02d}</span><span>{t}</span></li>'
                       for i, t in enumerate(items))
    o.append(f"""
<section class="sec" id="spec"><div class="wrap">
  <div class="sheet-no" data-rv="up"><b>ЛИСТ 05</b><i></i><span class="mono">Спецификация</span></div>
  <div class="sec-head split">
    <div data-rv="up"><h2 class="h2" data-split="line">Что входит<br>в базовую стоимость</h2></div>
    <p class="lead" data-rv="up" style="--d:150ms">Честный список без звёздочек: что вы получаете сразу,
    что оплачивается отдельно и что можно добавить.</p>
  </div>
  <div class="spec" data-stagger="110">
    <div class="spec__c spec--in"><h3 class="h3">Входит в стоимость</h3><ul>{li(INCLUDED,'A.')}</ul></div>
    <div class="spec__c spec--out"><h3 class="h3">Не входит</h3><ul>{li(EXCLUDED,'B.')}</ul></div>
    <div class="spec__c"><h3 class="h3">Опции</h3><ul>{li(OPTIONS,'C.')}</ul></div>
  </div>
</div></section>""")

    steps = "".join(f"""
    <article class="pstep">
      <div class="pstep__n" data-rv="up">ЭТАП {n}</div>
      <div data-rv="up" style="--d:80ms"><h3 class="h3">{t}</h3><p>{d}</p></div>
      <div class="pstep__i" data-rv="mask" style="--d:140ms"><img src="{im}" alt="{t}" loading="lazy" data-par="26"></div>
    </article>""" for n, t, d, im in PROCESS)
    o.append(f"""
<section class="sec" id="process"><div class="wrap">
  <div class="sheet-no" data-rv="up"><b>ЛИСТ 06</b><i></i><span class="mono">Порядок работ</span></div>
  <div class="sec-head" data-rv="up"><h2 class="h2">Четыре шага до новоселья</h2></div>
  <div class="pr">{steps}</div>
</div></section>""")

    mos = "".join(f'<figure data-lb="d" data-full="{im}" data-cap="{t}"><img src="{im}" alt="{t}" loading="lazy"><figcaption>{t}</figcaption></figure>'
                  for t, im in DETAILS + INTERIOR)
    o.append(f"""
<section class="sec" id="details"><div class="wrap">
  <div class="sheet-no" data-rv="up"><b>ЛИСТ 07</b><i></i><span class="mono">Узлы и материалы</span></div>
  <div class="sec-head split">
    <div data-rv="up"><h2 class="h2" data-split="line">Детали в едином<br>чёрном стиле</h2></div>
    <p class="lead" data-rv="up" style="--d:150ms">Электрощит, розетки, выключатели, светильники
    и ручки — одно оформление без визуального шума.</p>
  </div>
  <div class="mos" data-stagger="70">{mos}</div>
</div></section>""")

    objs = "".join(f"""
    <div><a class="obj" href="#cta"><span class="obj__i"><img src="{im}" alt="{t}" loading="lazy"></span>
      <span class="obj__c"><h3>{t}</h3><p>{d}</p></span></a></div>""" for t, d, im in OBJECTS)
    o.append(f"""
<section class="sec" id="objects"><div class="wrap">
  <div class="sheet-no" data-rv="up"><b>ЛИСТ 08</b><i></i><span class="mono">Реализовано</span></div>
  <div class="sec-head" data-rv="up"><h2 class="h2">Наши дома на участках</h2></div>
  <div class="objs" data-stagger="90">{objs}</div>
</div></section>""")

    o.append(f"""
<section class="sec"><div class="wrap ba-wrap">
  <div data-rv="up">
    <div class="sheet-no"><b>ЛИСТ 09</b><i></i><span class="mono">Сравнение</span></div>
    <h2 class="h2" data-split="line">Ваш дом у нас —<br>и ваш дом у вас</h2>
    <p class="lead" style="margin-top:18px">Слева — модуль на производстве, справа — тот же дом
    на участке. Потяните ползунок.</p></div>
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
    <div class="sheet-no"><b>ЛИСТ 10</b><i></i><span class="mono">Заявка</span></div>
    <h2 class="h2">Оставьте заявку<br>и получите расчёт</h2>
    <p class="lead" style="margin-top:16px">Подберём планировку под участок и посчитаем стоимость
    с доставкой и монтажом.</p>
    <div style="margin-top:24px;display:grid;gap:6px;font-family:var(--font-mono);font-size:1.25rem;font-weight:500">
      <a href="tel:{b['phone1_href']}">{b['phone1']}</a><a href="tel:{b['phone2_href']}">{b['phone2']}</a>
    </div>
  </div>
  <form data-form novalidate>
    <div class="f-row two">
      <div class="field"><label for="n6">Ваше имя</label>
        <input id="n6" type="text" required autocomplete="name" placeholder="Иван"><span class="err">Укажите имя</span></div>
      <div class="field"><label for="t6">Телефон</label>
        <input id="t6" type="tel" required autocomplete="tel" inputmode="tel" placeholder="+7 (___) ___-__-__">
        <span class="err">Введите номер полностью</span></div>
    </div>
    <div class="field"><label for="m6">Комментарий</label>
      <textarea id="m6" rows="3" placeholder="Интересует MODUL HOUSE 3, участок в Бердске"></textarea></div>
    <button class="btn btn--fill" type="submit" data-magnet=".2" style="justify-self:start">Отправить заявку {ARR}</button>
    <p class="form-note">Нажимая кнопку, вы соглашаетесь с обработкой персональных данных.</p>
    <div class="form-ok" role="status">Спасибо! Заявка принята — мы перезвоним в рабочее время.</div>
  </form>
</div></div></div></section>""")

    o.append(f"""
<footer class="foot" id="contacts"><div class="wrap">
  <div class="foot__grid">
    <div data-rv="up"><a class="logo" href="#top"><i></i>ДОММ</a>
      <p class="lead" style="margin-top:14px;font-size:14.5px">Производство и продажа модульных домов
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
/* --- Подбор дома: два ползунка + ширина модуля --- */
(function(){
  var root = document.getElementById('pick'); if(!root) return;
  var area  = root.querySelector('#f-area'),
      price = root.querySelector('#f-price'),
      outA  = root.querySelector('[data-out="area"]'),
      outP  = root.querySelector('[data-out="price"]'),
      found = root.querySelector('[data-found]'),
      word  = root.querySelector('[data-found-word]'),
      empty = root.querySelector('[data-pick-empty]'),
      grid  = root.querySelector('[data-pick-grid]'),
      items = Array.prototype.slice.call(root.querySelectorAll('.pl')),
      chips = root.querySelectorAll('[data-mod]');
  var mod = 'all';

  function plural(n){
    if(n % 10 === 1 && n % 100 !== 11) return 'планировка подходит';
    if([2,3,4].indexOf(n % 10) >= 0 && [12,13,14].indexOf(n % 100) < 0) return 'планировки подходят';
    return 'планировок подходит';
  }
  function fmt(n){ return Math.round(n).toLocaleString('ru-RU'); }

  function apply(){
    var a = +area.value, p = +price.value, n = 0;
    outA.textContent = a >= +area.max ? 'любая' : 'до ' + a;
    outP.textContent = p >= +price.max ? 'любой' : 'до ' + fmt(p);
    items.forEach(function(el, i){
      var ok = (+el.dataset.area) <= a && (+el.dataset.price) <= p &&
               (mod === 'all' || el.dataset.mod === mod);
      if(ok){
        n++;
        if(el.classList.contains('hide')){
          el.classList.remove('hide');
          el.classList.remove('show');
          /* даём браузеру применить стартовое состояние, потом анимируем */
          requestAnimationFrame(function(){ el.classList.add('show'); });
        }
      } else {
        el.classList.remove('show');
        el.classList.add('hide');
      }
    });
    found.textContent = n;
    word.textContent = plural(n);
    empty.hidden = n > 0;
    grid.hidden = n === 0;
  }

  area.addEventListener('input', apply);
  price.addEventListener('input', apply);
  chips.forEach(function(c){
    c.addEventListener('click', function(){
      chips.forEach(function(x){ x.classList.remove('on'); });
      c.classList.add('on');
      mod = c.dataset.mod;
      apply();
    });
  });

  /* подборка переносится в заявку, чтобы человеку не пришлось её описывать */
  var send = root.querySelector('[data-send-pick]');
  if(send) send.addEventListener('click', function(){
    var box = document.querySelector('#cta textarea');
    if(!box) return;
    var m = mod === 'all' ? 'любая ширина модуля' : 'модуль ' + mod;
    var aTxt = (+area.value >= +area.max) ? 'площадь любая'
                                          : 'площадь до ' + area.value + ' м²';
    var pTxt = (+price.value >= +price.max) ? 'бюджет любой'
                                            : 'бюджет до ' + fmt(price.value) + ' тыс. ₽';
    box.value = 'Подберите дом: ' + aTxt + ', ' + pTxt + ', ' + m +
                '. Подходит вариантов: ' + found.textContent + '.';
    box.dispatchEvent(new Event('input'));
    setTimeout(function(){ var n = document.querySelector('#cta input[type="text"]'); if(n) n.focus(); }, 700);
  });

  apply();
})();
"""
    o.append(core.tail(extra))
    return "".join(o)
