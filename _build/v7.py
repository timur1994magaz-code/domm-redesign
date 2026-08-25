# -*- coding: utf-8 -*-
"""Вариант 7 — ТАЙГА. Кинематографичный тёмный лес, горизонтальная прокрутка
и пошаговый конфигуратор дома с живой сметой."""
import core
from data import *

FONTS = ('<link href="https://fonts.googleapis.com/css2?'
         'family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,300&'
         'family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">')

CSS = r"""
:root{
  --bg:#0B120F; --bg-2:#111A16; --bg-3:#16211C; --fg:#E8E4D9; --muted:#7E8A82;
  --line:rgba(232,228,217,.13); --hair:rgba(232,228,217,.07);
  --accent:#E0873C; --moss:#5C7A62; --on-accent:#160C03; --input-bg:rgba(255,255,255,.04);
  --font-head:'Cormorant Garamond',Georgia,serif; --font-body:'Inter',system-ui,sans-serif;
  --radius:2px; --radius-sm:2px; --head-weight:300;
}
::selection{background:var(--accent);color:var(--on-accent)}
.h1{font-family:var(--font-head);font-size:clamp(3rem,9vw,8rem);font-weight:300;line-height:.92;letter-spacing:-.02em}
.h2{font-family:var(--font-head);font-size:clamp(2.2rem,5.4vw,4.6rem);font-weight:300;line-height:.98;letter-spacing:-.015em}
.h3{font-size:clamp(1rem,1.6vw,1.2rem);font-weight:500;letter-spacing:-.005em}
.it{font-style:italic;color:var(--accent)}
.label{display:inline-flex;align-items:center;gap:10px;font-size:10.5px;letter-spacing:.26em;
  text-transform:uppercase;color:var(--accent)}
.label::before{content:"";width:26px;height:1px;background:var(--accent)}
.lead{color:var(--muted);font-size:clamp(1rem,1.2vw,1.08rem);max-width:58ch;line-height:1.75;font-weight:300}
.sec{padding:clamp(70px,9vw,140px) 0;position:relative}
.sec-head{display:grid;gap:20px;margin-bottom:clamp(34px,4.5vw,60px)}
@media(min-width:900px){.sec-head.split{grid-template-columns:1.1fr .9fr;align-items:end;gap:52px}}
.chapter{position:absolute;left:0;top:clamp(70px,9vw,140px);writing-mode:vertical-rl;
  font-size:10px;letter-spacing:.3em;text-transform:uppercase;color:var(--muted);opacity:.6}
@media(max-width:1279px){.chapter{display:none}}

/* шапка */
.hdr{position:fixed;inset:0 0 auto 0;z-index:100;padding:18px 0;transition:.5s cubic-bezier(.16,1,.3,1)}
.hdr.stuck{background:rgba(11,18,15,.82);backdrop-filter:blur(16px);padding:11px 0;
  border-bottom:1px solid var(--line)}
.hdr.hide{transform:translateY(-102%)}
.hdr__in{display:flex;align-items:center;justify-content:space-between;gap:20px}
.logo{font-family:var(--font-head);font-size:26px;letter-spacing:.16em;font-weight:400}
.nav{display:none;gap:30px}
@media(min-width:1024px){.nav{display:flex}}
.nav a{font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--muted);
  position:relative;padding:4px 0;transition:color .3s}
.nav a::after{content:"";position:absolute;left:0;right:0;bottom:0;height:1px;background:var(--accent);
  transform:scaleX(0);transform-origin:100% 50%;transition:transform .45s cubic-bezier(.16,1,.3,1)}
.nav a:hover{color:var(--fg)}
.nav a:hover::after{transform:scaleX(1);transform-origin:0 50%}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;padding:15px 28px;
  font-size:11px;letter-spacing:.16em;text-transform:uppercase;font-weight:500;
  position:relative;overflow:hidden;isolation:isolate;border-radius:var(--radius);
  transform:translate3d(var(--tx,0),var(--ty,0),0);
  transition:transform .4s cubic-bezier(.16,1,.3,1),color .3s,border-color .3s}
.btn--fill{background:var(--accent);color:var(--on-accent)}
.btn--fill::before{content:"";position:absolute;inset:0;z-index:-1;background:var(--fg);
  transform:translateY(101%);transition:transform .5s cubic-bezier(.16,1,.3,1)}
.btn--fill:hover::before{transform:none}
.btn--fill:hover{color:var(--bg)}
.btn--ghost{border:1px solid var(--line);color:var(--fg)}
.btn--ghost::before{content:"";position:absolute;inset:0;z-index:-1;background:var(--accent);
  transform:translateY(101%);transition:transform .5s cubic-bezier(.16,1,.3,1)}
.btn--ghost:hover{color:var(--on-accent);border-color:var(--accent)}
.btn--ghost:hover::before{transform:none}
.btn:disabled{opacity:.35;pointer-events:none}
.hdr__cta{display:none}@media(min-width:640px){.hdr__cta{display:inline-flex}}
.burger{display:grid;gap:5px;padding:10px;margin:-10px}
@media(min-width:1024px){.burger{display:none}}
.burger i{width:23px;height:1.5px;background:var(--fg);transition:.4s}
body.nav-open .burger i:nth-child(1){transform:translateY(6.5px) rotate(45deg)}
body.nav-open .burger i:nth-child(2){opacity:0}
body.nav-open .burger i:nth-child(3){transform:translateY(-6.5px) rotate(-45deg)}
.mnav{position:fixed;inset:0;z-index:99;background:var(--bg-2);display:grid;align-content:center;gap:6px;
  padding:0 var(--gutter);opacity:0;visibility:hidden;transition:.45s}
body.nav-open .mnav{opacity:1;visibility:visible}
.mnav a{font-family:var(--font-head);font-size:clamp(2.4rem,10vw,3.8rem);font-weight:300;
  opacity:0;transform:translateY(20px);transition:.6s cubic-bezier(.16,1,.3,1)}
body.nav-open .mnav a{opacity:1;transform:none}
.mnav a:nth-child(1){transition-delay:.06s}.mnav a:nth-child(2){transition-delay:.12s}
.mnav a:nth-child(3){transition-delay:.18s}.mnav a:nth-child(4){transition-delay:.24s}
.mnav a:nth-child(5){transition-delay:.3s}
.mnav__foot{margin-top:30px;display:grid;gap:6px;color:var(--muted);font-size:14px}

/* герой */
.hero{position:relative;min-height:100svh;display:flex;align-items:flex-end;padding:140px 0 60px;overflow:hidden}
.hero__bg{position:absolute;inset:-5%;background-size:cover;background-position:center 60%;
  animation:ken 30s ease-in-out infinite alternate}
@keyframes ken{from{transform:scale(1.05)}to{transform:scale(1.2) translate3d(-2%,-1%,0)}}
.hero::after{content:"";position:absolute;inset:0;
  background:linear-gradient(90deg,rgba(11,18,15,.72) 0%,rgba(11,18,15,.12) 58%,transparent 100%),
             linear-gradient(180deg,rgba(11,18,15,.86) 0%,rgba(11,18,15,.42) 32%,rgba(11,18,15,.76) 66%,rgba(11,18,15,.98) 100%)}
.hero__in{position:relative;z-index:2}
.hero__grid{display:grid;gap:34px}
@media(min-width:1024px){.hero__grid{grid-template-columns:1.35fr .65fr;align-items:end;gap:52px}}
.hero .h1{margin:22px 0 24px}
.hero__acts{display:flex;flex-wrap:wrap;gap:14px;margin-top:30px}
.hero__side{display:grid;gap:22px}
.hero__side div{border-top:1px solid var(--line);padding-top:14px}
.hero__side b{font-family:var(--font-head);display:block;font-size:clamp(1.9rem,3vw,2.6rem);
  font-weight:300;letter-spacing:-.02em;color:var(--accent)}
.hero__side span{font-size:10.5px;letter-spacing:.2em;text-transform:uppercase;color:var(--muted)}

/* горизонтальная прокрутка */
.hs{position:relative}
.hs__pin{position:sticky;top:0;height:100svh;display:flex;align-items:center;overflow:hidden}
.hs__track{display:flex;gap:22px;padding-inline:var(--gutter);will-change:transform}
.hs__item{flex:0 0 clamp(260px,44vw,520px);position:relative}
.hs__item figure{margin:0;aspect-ratio:4/5;overflow:hidden;border:1px solid var(--line)}
.hs__item img{width:100%;height:100%;object-fit:cover;filter:brightness(.86);transition:filter .6s}
.hs__item:hover img{filter:brightness(1)}
.hs__item figcaption{margin-top:12px;font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--muted)}
.hs__intro{flex:0 0 clamp(280px,34vw,440px);align-self:center}
.hs__hint{position:absolute;left:50%;bottom:36px;translate:-50% 0;font-size:10px;letter-spacing:.24em;
  text-transform:uppercase;color:var(--muted);display:flex;align-items:center;gap:10px}
.hs__hint i{width:40px;height:1px;background:var(--muted);display:block;transform-origin:0 50%;
  animation:swipe 2.6s ease-in-out infinite}
@keyframes swipe{0%,100%{transform:scaleX(.35)}50%{transform:scaleX(1)}}
/* на узких экранах — обычная лента с перетаскиванием */
@media(max-width:899px){
  .hs{height:auto!important}
  .hs__pin{position:static;height:auto;display:block}
  .hs__track{overflow-x:auto;scroll-snap-type:x mandatory;padding-bottom:18px;
    cursor:grab;scrollbar-width:none;transform:none!important}
  .hs__track::-webkit-scrollbar{display:none}
  .hs__item{scroll-snap-align:center}
  .hs__intro{flex:0 0 82vw}
  .hs__hint{display:none}
}
@media (prefers-reduced-motion:reduce){.hs__hint i{animation:none}}

/* конфигуратор */
.wiz{display:grid;gap:0;border:1px solid var(--line);background:var(--bg-2)}
@media(min-width:1000px){.wiz{grid-template-columns:1fr 380px}}
.wiz__main{padding:clamp(24px,3.2vw,40px);display:flex;flex-direction:column}
.wiz__top{display:flex;align-items:center;gap:18px;padding-bottom:22px;border-bottom:1px solid var(--line);margin-bottom:26px}
.ring{position:relative;width:56px;height:56px;flex:0 0 56px}
.ring svg{width:100%;height:100%;transform:rotate(-90deg)}
.ring circle{fill:none;stroke-width:2}
.ring .bg{stroke:var(--line)}
.ring .fg{stroke:var(--accent);stroke-dasharray:1;stroke-dashoffset:calc(1 - var(--p,.25));
  transition:stroke-dashoffset .6s cubic-bezier(.16,1,.3,1)}
.ring b{position:absolute;inset:0;display:grid;place-items:center;font-size:12px;font-weight:600;
  font-variant-numeric:tabular-nums}
.wiz__ttl span{display:block;font-size:10.5px;letter-spacing:.2em;text-transform:uppercase;color:var(--muted);margin-bottom:6px}
.wiz__ttl h3{font-family:var(--font-head);font-size:clamp(1.4rem,2.4vw,2rem);font-weight:400;letter-spacing:-.01em}
.wiz__step{display:none;animation:stepIn .55s cubic-bezier(.16,1,.3,1)}
.wiz__step.on{display:block}
@keyframes stepIn{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:none}}
@media (prefers-reduced-motion:reduce){.wiz__step{animation:none}}
.opts{display:grid;gap:10px}
@media(min-width:620px){.opts{grid-template-columns:1fr 1fr}}
.opt{display:flex;align-items:center;gap:14px;padding:16px;border:1px solid var(--line);
  background:transparent;text-align:left;cursor:pointer;transition:border-color .3s,background .3s}
.opt:hover{border-color:var(--muted)}
.opt.on{border-color:var(--accent);background:rgba(224,135,60,.07)}
.opt input{position:absolute;opacity:0;pointer-events:none}
.opt .mark{flex:0 0 20px;width:20px;height:20px;border:1px solid var(--line);display:grid;place-items:center;
  transition:.3s;border-radius:50%}
.opt .mark svg{opacity:0;transform:scale(.5);transition:.3s}
.opt.on .mark{background:var(--accent);border-color:var(--accent)}
.opt.on .mark svg{opacity:1;transform:none;color:var(--on-accent)}
.opt.sq .mark{border-radius:3px}
.opt__t{flex:1;min-width:0}
.opt__t b{display:block;font-size:14.5px;font-weight:500;letter-spacing:-.01em}
.opt__t span{display:block;font-size:12.5px;color:var(--muted);margin-top:3px}
.opt__p{font-size:13px;color:var(--accent);white-space:nowrap;font-variant-numeric:tabular-nums}
.wiz__rng{margin-top:6px}
.wiz__rng .rt{display:flex;justify-content:space-between;align-items:baseline;gap:12px;margin-bottom:14px}
.wiz__rng .rt span{font-size:10.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--muted)}
.wiz__rng .rt b{font-size:15px;font-weight:500;font-variant-numeric:tabular-nums}
input[type=range]{-webkit-appearance:none;appearance:none;width:100%;height:26px;background:transparent;cursor:pointer;margin:0}
input[type=range]::-webkit-slider-runnable-track{height:1px;background:var(--line)}
input[type=range]::-moz-range-track{height:1px;background:var(--line)}
input[type=range]::-webkit-slider-thumb{-webkit-appearance:none;width:20px;height:20px;border-radius:50%;
  background:var(--accent);margin-top:-9.5px;transition:transform .2s}
input[type=range]::-moz-range-thumb{width:20px;height:20px;border:0;border-radius:50%;background:var(--accent)}
input[type=range]:active::-webkit-slider-thumb{transform:scale(1.2)}
input[type=range]:focus-visible::-webkit-slider-thumb{outline:2px solid var(--accent);outline-offset:3px}
.wiz__nav{display:flex;gap:12px;align-items:center;margin-top:auto;padding-top:26px}
.wiz__dots{display:flex;gap:7px;margin-left:auto}
.wiz__dots i{width:6px;height:6px;border-radius:50%;background:var(--line);display:block;transition:.35s}
.wiz__dots i.on{background:var(--accent);transform:scale(1.35)}
.wiz__sum{padding:clamp(24px,3.2vw,40px);background:var(--bg-3);border-top:1px solid var(--line);
  display:flex;flex-direction:column}
@media(min-width:1000px){.wiz__sum{border-top:0;border-left:1px solid var(--line)}}
.wiz__sum>span{font-size:10.5px;letter-spacing:.2em;text-transform:uppercase;color:var(--muted)}
.wiz__total{font-family:var(--font-head);font-size:clamp(2.4rem,5vw,3.4rem);font-weight:300;
  letter-spacing:-.02em;color:var(--accent);margin:8px 0 4px;font-variant-numeric:tabular-nums}
.wiz__rows{margin:22px 0;display:grid;gap:0;border-top:1px solid var(--line)}
.wiz__rows div{display:flex;justify-content:space-between;gap:12px;padding:10px 0;
  border-bottom:1px solid var(--hair);font-size:13px;color:var(--muted)}
.wiz__rows b{color:var(--fg);font-weight:500;text-align:right;font-variant-numeric:tabular-nums}
.wiz__note{font-size:11.5px;color:var(--muted);line-height:1.6;margin-top:14px}
.wiz__cta{margin-top:auto}

/* карточки */
.cards{display:grid;gap:20px}
@media(min-width:700px){.cards{grid-template-columns:repeat(2,1fr)}}
@media(min-width:1100px){.cards{grid-template-columns:repeat(3,1fr)}}
.card{border:1px solid var(--line);background:var(--bg-2);overflow:hidden;
  transition:border-color .45s,transform .55s cubic-bezier(.16,1,.3,1)}
.card:hover{border-color:var(--accent);transform:translateY(-5px)}
.card__i{aspect-ratio:4/3;overflow:hidden;position:relative}
.card__i img{width:100%;height:100%;object-fit:cover;filter:brightness(.88);
  transition:transform 1.2s cubic-bezier(.16,1,.3,1),filter .6s}
.card:hover .card__i img{transform:scale(1.06);filter:brightness(1)}
.card__tag{position:absolute;top:12px;left:12px;padding:6px 12px;font-size:10.5px;letter-spacing:.14em;
  background:rgba(11,18,15,.72);backdrop-filter:blur(6px);border:1px solid var(--line)}
.card__b{padding:22px;display:grid;gap:9px}
.card__b p{color:var(--muted);font-size:14px;font-weight:300;min-height:42px}
.card__p{display:flex;justify-content:space-between;align-items:baseline;padding-top:15px;
  border-top:1px solid var(--line);margin-top:5px}
.card__p b{font-family:var(--font-head);font-size:1.5rem;font-weight:400;color:var(--accent)}
.card__p span{font-size:10.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--muted)}

/* планировки */
.tabs{display:flex;gap:0;flex-wrap:wrap;margin-bottom:30px;border-bottom:1px solid var(--line)}
.tabs button{padding:14px 22px;font-size:11px;letter-spacing:.16em;text-transform:uppercase;
  color:var(--muted);position:relative;transition:color .3s}
.tabs button::after{content:"";position:absolute;left:0;right:0;bottom:-1px;height:1px;background:var(--accent);
  transform:scaleX(0);transition:transform .4s cubic-bezier(.16,1,.3,1)}
.tabs button.active{color:var(--fg)}
.tabs button.active::after{transform:scaleX(1)}
.plans{display:grid;gap:16px;grid-template-columns:repeat(2,1fr)}
@media(min-width:900px){.plans{grid-template-columns:repeat(4,1fr)}}
.plan{border:1px solid var(--line);background:var(--bg-2);cursor:zoom-in;
  transition:.45s cubic-bezier(.16,1,.3,1)}
.plan:hover{border-color:var(--accent);transform:translateY(-4px)}
.plan__i{aspect-ratio:1/1;background:#fff;padding:10px}
.plan__i img{width:100%;height:100%;object-fit:contain}
.plan__b{padding:15px;display:grid;gap:5px}
.plan__b h4{font-size:13px;font-weight:500}
.plan__b .m{font-size:11.5px;color:var(--muted)}
.plan__b .p{font-family:var(--font-head);font-size:16px;color:var(--accent)}

/* комплектация */
.spec{display:grid;gap:18px}
@media(min-width:1000px){.spec{grid-template-columns:1.4fr .8fr .8fr}}
.spec__c{border:1px solid var(--line);padding:30px 26px;background:var(--bg-2);transition:border-color .45s}
.spec__c:hover{border-color:var(--accent)}
.spec__c h3{font-family:var(--font-head);font-size:1.5rem;font-weight:400;margin-bottom:18px}
.spec__c li{display:flex;gap:11px;padding:9px 0;font-size:14px;font-weight:300;color:var(--muted);
  border-bottom:1px solid var(--hair);line-height:1.55}
.spec__c li:last-child{border:0}
.spec__c i{flex:0 0 5px;width:5px;height:5px;border-radius:50%;background:var(--accent);margin-top:9px;display:block}
.spec--in li{color:var(--fg)}
.spec--out i{background:var(--muted)}

/* процесс */
.pr{display:grid;gap:0}
.pstep{display:grid;gap:22px;padding:clamp(28px,4vw,52px) 0;border-top:1px solid var(--line);align-items:center}
@media(min-width:900px){.pstep{grid-template-columns:1fr 1fr;gap:56px}
  .pstep:nth-child(even) .pstep__i{order:-1}}
.pstep__n{font-family:var(--font-head);font-size:clamp(2.4rem,5vw,4rem);font-weight:300;
  color:var(--accent);opacity:.5;line-height:.8;display:block;margin-bottom:14px}
.pstep h3{font-family:var(--font-head);font-size:clamp(1.5rem,2.8vw,2.2rem);font-weight:400;margin-bottom:12px}
.pstep p{color:var(--muted);font-size:14.5px;font-weight:300;line-height:1.75}
.pstep__i{overflow:hidden;aspect-ratio:4/3;border:1px solid var(--line)}
.pstep__i img{width:100%;height:100%;object-fit:cover;transform:scale(1.1) translate3d(0,var(--par,0),0);
  filter:brightness(.9)}

/* мозаика */
.mos{display:grid;gap:16px;grid-template-columns:repeat(2,1fr)}
@media(min-width:900px){.mos{grid-template-columns:repeat(3,1fr)}
  .mos figure:nth-child(4){grid-column:span 2}}
.mos figure{margin:0;position:relative;aspect-ratio:3/4;overflow:hidden;border:1px solid var(--line);cursor:zoom-in}
@media(min-width:900px){.mos figure:nth-child(4){aspect-ratio:16/9}}
.mos img{width:100%;height:100%;object-fit:cover;filter:brightness(.8);
  transition:transform 1.2s cubic-bezier(.16,1,.3,1),filter .6s}
.mos figure:hover img{transform:scale(1.05);filter:brightness(1)}
.mos figcaption{position:absolute;inset:auto 0 0 0;padding:60px 18px 18px;font-size:12.5px;font-weight:300;
  background:linear-gradient(transparent,rgba(11,18,15,.94));transform:translateY(6px);opacity:.9;
  transition:.5s cubic-bezier(.16,1,.3,1)}
.mos figure:hover figcaption{transform:none;opacity:1}

/* объекты */
.objs{display:grid;gap:1px;background:var(--line);border-block:1px solid var(--line)}
.obj{background:var(--bg);display:grid;grid-template-columns:auto 1fr auto;gap:20px;align-items:center;
  padding:26px 8px;transition:background .5s,padding-left .5s cubic-bezier(.16,1,.3,1)}
.obj:hover{background:var(--bg-2);padding-left:22px}
.obj__n{font-size:10.5px;color:var(--accent);letter-spacing:.2em}
.obj__t{display:block}
.obj__t h3{font-family:var(--font-head);font-size:clamp(1.3rem,2.6vw,2.1rem);font-weight:400}
.obj__t p{color:var(--muted);font-size:13.5px;font-weight:300;margin-top:5px}
.obj__go{width:42px;height:42px;border-radius:50%;border:1px solid var(--line);display:grid;place-items:center;transition:.4s}
.obj:hover .obj__go{background:var(--accent);color:var(--on-accent);border-color:var(--accent);transform:rotate(-45deg)}
@media(max-width:899px){.obj{grid-template-columns:auto 1fr}.obj__go{display:none}}

/* до/после */
.ba{border:1px solid var(--line)}
.ba-wrap{display:grid;gap:34px;align-items:center}
@media(min-width:1000px){.ba-wrap{grid-template-columns:.8fr 1.2fr;gap:56px}}

/* заявка */
.cta{border:1px solid var(--line);background:var(--bg-2);padding:clamp(28px,5vw,62px);position:relative;overflow:hidden}
.cta::after{content:"";position:absolute;width:46vw;aspect-ratio:1;border-radius:50%;right:-14vw;top:-22vw;
  background:radial-gradient(circle,rgba(224,135,60,.15),transparent 66%);animation:fl 22s ease-in-out infinite alternate}
@keyframes fl{to{transform:translate3d(-12vw,14vw,0) scale(1.2)}}
.cta__in{position:relative;display:grid;gap:38px}
@media(min-width:960px){.cta__in{grid-template-columns:1fr 1fr;gap:60px;align-items:center}}
.cta form{display:grid;gap:15px}

/* подвал */
.foot{padding:64px 0 32px;border-top:1px solid var(--line)}
.foot__grid{display:grid;gap:32px}
@media(min-width:800px){.foot__grid{grid-template-columns:1.5fr 1fr 1fr 1fr}}
.foot h4{font-size:10.5px;letter-spacing:.2em;text-transform:uppercase;color:var(--muted);margin-bottom:15px}
.foot p{font-size:14.5px;margin-bottom:9px;font-weight:300}
.foot a:hover{color:var(--accent)}
.foot__bot{margin-top:46px;padding-top:20px;border-top:1px solid var(--line);display:flex;flex-wrap:wrap;
  gap:12px;justify-content:space-between;font-size:11px;color:var(--muted)}
"""

ARR = ('<svg width="16" height="10" viewBox="0 0 18 10" fill="none" stroke="currentColor" '
       'stroke-width="1.4" aria-hidden="true"><path d="M0 5h16M12 1l4 4-4 4"/></svg>')
TICK = ('<svg width="11" height="11" viewBox="0 0 16 16" fill="none" stroke="currentColor" '
        'stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><path d="M2.5 8.5l3.5 3.5 7.5-8"/></svg>')

PACKS = [
    ("Базовая", "Как в описании комплектации", 1.0),
    ("Расширенная", "Фанера на стенах, кашировка рам", 1.12),
    ("Премиум", "Полная отделка и сантехника", 1.25),
]
WOPTS = [
    ("Кондиционирование", 90000), ("Светодиодные подсветки", 45000),
    ("Сантехнические приборы", 75000), ("Тёплый пол", 110000),
    ("Мебель и интерьер", 250000), ("Отделка стен фанерой", 85000),
]
FOUND = [
    ("Винтовые сваи", "Быстро, подходит большинству участков", 180000),
    ("Бетонные сваи", "Для сложных грунтов", 260000),
    ("Фундамент уже есть", "Ничего не считаем", 0),
]
MONTAGE = 120000
PER_KM = 90

def build():
    b = BRAND
    nav = "".join(f'<a href="{h}">{t}</a>' for h, t in NAV)
    o = [core.head("ДОММ — модульные дома под ключ | Новосибирск",
                   "Соберите свой модульный дом в конфигураторе и узнайте стоимость с доставкой и монтажом. "
                   "От 990 000 ₽ за 30 дней.",
                   FONTS, CSS, "#0B120F")]
    o.append('<div class="cursor"></div>')

    o.append(f"""
<header class="hdr" data-header><div class="wrap hdr__in">
  <a class="logo" href="#top">ДОММ</a>
  <nav class="nav">{nav}</nav>
  <a class="btn btn--ghost hdr__cta" href="#config" data-magnet=".25">Собрать дом</a>
  <button class="burger" data-burger aria-label="Меню" aria-expanded="false"><i></i><i></i><i></i></button>
</div></header>
<nav class="mnav" data-menu>{nav}
  <div class="mnav__foot"><a href="tel:{b['phone1_href']}">{b['phone1']}</a>
  <a href="tel:{b['phone2_href']}">{b['phone2']}</a><a href="mailto:{b['email']}">{b['email']}</a></div>
</nav>""")

    side = "".join(f'<div><b>{v}</b><span>{t}</span></div>' for v, t in STATS[:3])
    o.append(f"""
<section class="hero" id="top">
  <div class="hero__bg" style="background-image:url('{HERO['bg']}')"></div>
  <div class="wrap hero__in"><div class="hero__grid">
    <div data-rv="up">
      <span class="label">{HERO['kicker']}</span>
      <h1 class="h1" data-split="line">Модульные дома<br><span class="it">для жизни</span> и отдыха</h1>
      <p class="lead">{HERO['sub']} {HERO['sub2']}</p>
      <div class="hero__acts">
        <a class="btn btn--fill" href="#config" data-magnet=".3">Собрать свой дом {ARR}</a>
        <a class="btn btn--ghost" href="{b['wa']}" target="_blank" rel="noopener">Написать в WhatsApp</a>
      </div>
    </div>
    <div class="hero__side" data-rv="up" style="--d:220ms">{side}</div>
  </div></div>
</section>""")

    # горизонтальная лента
    items = "".join(f"""
    <div class="hs__item"><figure><img src="{u}" alt="Модульный дом ДОММ" loading="lazy"
      data-lb="g" data-full="{u}" data-cap="Дом ДОММ"></figure>
      <figcaption>{i+1:02d} / Дом ДОММ</figcaption></div>""" for i, u in enumerate(GALLERY))
    o.append(f"""
<section class="hs" id="gallery" data-hs>
  <div class="hs__pin">
    <div class="hs__track">
      <div class="hs__intro">
        <span class="label">Галерея</span>
        <h2 class="h2" style="margin:18px 0 18px">Декорируем дома<br>в <span class="it">уютном</span> стиле</h2>
        <p class="lead">Тёплое дерево, мягкий свет и панорамные окна. Прокрутите — лента поедет вбок.</p>
      </div>
      {items}
    </div>
    <div class="hs__hint"><i></i>Прокрутите</div>
  </div>
</section>""")

    # конфигуратор
    models = "".join(f"""
      <button class="opt{' on' if i==0 else ''}" data-model data-price="{p.replace(' ','')}"
              data-name="{n}" data-area="{area}">
        <span class="mark">{TICK}</span>
        <span class="opt__t"><b>{n}</b><span>{area}</span></span>
        <span class="opt__p">от {p} ₽</span>
      </button>""" for i, (n, d, p, area, im) in enumerate(PROJECTS))
    packs = "".join(f"""
      <button class="opt{' on' if i==0 else ''}" data-pack data-k="{k}" data-name="{n}">
        <span class="mark">{TICK}</span>
        <span class="opt__t"><b>{n}</b><span>{d}</span></span>
        <span class="opt__p">{'включено' if k==1.0 else '+' + str(int((k-1)*100)) + '%'}</span>
      </button>""" for i, (n, d, k) in enumerate(PACKS))
    wopts = "".join(f"""
      <label class="opt sq" data-wopt>
        <input type="checkbox" value="{p}" data-name="{n}">
        <span class="mark">{TICK}</span>
        <span class="opt__t"><b>{n}</b></span>
        <span class="opt__p">+{p:,} ₽</span>
      </label>""".replace(",", " ") for n, p in WOPTS)
    founds = "".join(f"""
      <button class="opt{' on' if i==0 else ''}" data-found data-price="{p}" data-name="{n}">
        <span class="mark">{TICK}</span>
        <span class="opt__t"><b>{n}</b><span>{d}</span></span>
        <span class="opt__p">{'включено' if p==0 else '+' + f'{p:,}'.replace(',', ' ') + ' ₽'}</span>
      </button>""" for i, (n, d, p) in enumerate(FOUND))

    o.append(f"""
<section class="sec" id="config"><div class="wrap">
  <span class="chapter">Конфигуратор</span>
  <div class="sec-head split">
    <div data-rv="up"><span class="label">Соберите свой дом</span>
      <h2 class="h2" style="margin-top:18px" data-split="line">Четыре шага —<br>и вы знаете <span class="it">цену</span></h2></div>
    <p class="lead" data-rv="up" style="--d:150ms">Выберите модель, комплектацию и опции, укажите расстояние
    до участка. Смета пересчитывается сразу и уедет вместе с заявкой — не придётся ничего описывать словами.</p>
  </div>
  <div class="wiz" data-rv="up">
    <div class="wiz__main">
      <div class="wiz__top">
        <div class="ring">
          <svg viewBox="0 0 40 40" aria-hidden="true">
            <circle class="bg" cx="20" cy="20" r="18" pathLength="1"></circle>
            <circle class="fg" cx="20" cy="20" r="18" pathLength="1"></circle>
          </svg>
          <b data-ring-txt>1/4</b>
        </div>
        <div class="wiz__ttl"><span data-step-no>Шаг 1 из 4</span><h3 data-step-ttl>Модель дома</h3></div>
      </div>

      <div class="wiz__step on" data-wstep="1"><div class="opts">{models}</div></div>
      <div class="wiz__step" data-wstep="2"><div class="opts">{packs}</div></div>
      <div class="wiz__step" data-wstep="3"><div class="opts">{wopts}</div></div>
      <div class="wiz__step" data-wstep="4">
        <div class="opts">{founds}</div>
        <div class="wiz__rng" style="margin-top:22px">
          <div class="rt"><span>Расстояние до участка</span><b data-km-out>50 км</b></div>
          <input type="range" data-km min="0" max="1500" value="50" step="10" aria-label="Расстояние до участка, км">
        </div>
      </div>

      <div class="wiz__nav">
        <button class="btn btn--ghost" data-prev disabled>Назад</button>
        <button class="btn btn--fill" data-next>Далее {ARR}</button>
        <span class="wiz__dots" aria-hidden="true"><i class="on"></i><i></i><i></i><i></i></span>
      </div>
    </div>

    <aside class="wiz__sum">
      <span>Стоимость под ключ</span>
      <div class="wiz__total" data-total>990 000 ₽</div>
      <div class="wiz__rows">
        <div><span>Дом</span><b data-r-model>MODUL HOUSE 1</b></div>
        <div><span>Комплектация</span><b data-r-pack>Базовая</b></div>
        <div><span>Опции</span><b data-r-opts>—</b></div>
        <div><span>Фундамент</span><b data-r-found>Винтовые сваи</b></div>
        <div><span>Доставка и монтаж</span><b data-r-log>—</b></div>
      </div>
      <p class="wiz__note">Расчёт ориентировочный. Точную смету пришлём после разговора —
      она зависит от подъезда к участку и техники на монтаже. Аванс 30% фиксирует цену на весь срок.</p>
      <a class="btn btn--fill wiz__cta" href="#cta" data-send-cfg style="margin-top:22px">
        Зафиксировать расчёт {ARR}</a>
    </aside>
  </div>
</div></section>""")

    cards = "".join(f"""
    <article class="card" data-rv="up">
      <div class="card__i"><span class="card__tag">{area}</span><img src="{im}" alt="{n}" loading="lazy"></div>
      <div class="card__b"><h3 class="h3">{n}</h3><p>{d}</p>
        <div class="card__p"><b>от {p} ₽</b><span>под ключ</span></div></div>
    </article>""" for n, d, p, area, im in PROJECTS)
    o.append(f"""
<section class="sec" id="projects"><div class="wrap">
  <span class="chapter">Каталог</span>
  <div class="sec-head split">
    <div data-rv="up"><span class="label">Каталог</span>
      <h2 class="h2" style="margin-top:18px">Проекты домов и <span class="it">бань</span></h2></div>
    <p class="lead" data-rv="up" style="--d:150ms">Семь базовых моделей и две бани — любую адаптируем
    под участок и сценарий жизни.</p>
  </div>
  <div class="cards" data-stagger="90">{cards}</div>
</div></section>""")

    def pg(items_, key):
        return "".join(f"""
      <article class="plan" data-lb="{key}" data-full="{im}" data-cap="{n} — {a}, от {p} тыс. ₽">
        <div class="plan__i"><img src="{im}" alt="Планировка {n}" loading="lazy"></div>
        <div class="plan__b"><h4>{n}</h4><span class="m">{a}{' · ' + note if note else ''}</span>
          <span class="p">от {p} тыс. ₽</span></div></article>""" for n, a, p, im, note in items_)
    rend = "".join(f"""
      <article class="card" data-lb="rn" data-full="{im}" data-cap="{n}" style="cursor:zoom-in">
        <div class="card__i"><img src="{im}" alt="{n}" loading="lazy"></div>
        <div class="card__b"><h3 class="h3">{n}</h3><p>{d}</p></div></article>""" for n, d, im in RENDERS)
    o.append(f"""
<section class="sec" id="prices"><div class="wrap" data-tabs>
  <span class="chapter">Планировки</span>
  <div class="sec-head split">
    <div data-rv="up"><span class="label">Планировки и цены</span>
      <h2 class="h2" style="margin-top:18px">Выберите свой <span class="it">метраж</span></h2></div>
    <p class="lead" data-rv="up" style="--d:150ms">Дома собираются из модулей 2,5×6 м и 3×6 м.
    Нажмите на планировку, чтобы открыть её крупно.</p>
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

    def li(items_):
        return "".join(f'<li><i></i><span>{t}</span></li>' for t in items_)
    o.append(f"""
<section class="sec" id="spec"><div class="wrap">
  <span class="chapter">Спецификация</span>
  <div class="sec-head split">
    <div data-rv="up"><span class="label">Комплектация</span>
      <h2 class="h2" style="margin-top:18px" data-split="line">Что входит<br>в <span class="it">базовую</span> стоимость</h2></div>
    <p class="lead" data-rv="up" style="--d:150ms">Честный список без звёздочек: что вы получаете сразу,
    что оплачивается отдельно и что можно добавить.</p>
  </div>
  <div class="spec" data-stagger="110">
    <div class="spec__c spec--in"><h3>Входит в стоимость</h3><ul>{li(INCLUDED)}</ul></div>
    <div class="spec__c spec--out"><h3>Не входит</h3><ul>{li(EXCLUDED)}</ul></div>
    <div class="spec__c"><h3>Опции</h3><ul>{li(OPTIONS)}</ul></div>
  </div>
</div></section>""")

    steps = "".join(f"""
    <article class="pstep" data-rv="up">
      <div><span class="pstep__n">{n}</span><h3>{t}</h3><p>{d}</p></div>
      <div class="pstep__i"><img src="{im}" alt="{t}" loading="lazy" data-par="30"></div>
    </article>""" for n, t, d, im in PROCESS)
    o.append(f"""
<section class="sec" id="process"><div class="wrap">
  <span class="chapter">Порядок работ</span>
  <div class="sec-head" data-rv="up"><span class="label">Как мы работаем</span>
    <h2 class="h2" style="margin-top:18px">Четыре шага до <span class="it">новоселья</span></h2></div>
  <div class="pr">{steps}</div>
</div></section>""")

    mos = "".join(f'<figure data-lb="d" data-full="{im}" data-cap="{t}"><img src="{im}" alt="{t}" loading="lazy"><figcaption>{t}</figcaption></figure>'
                  for t, im in DETAILS + INTERIOR)
    o.append(f"""
<section class="sec" id="details"><div class="wrap">
  <span class="chapter">Материалы</span>
  <div class="sec-head split">
    <div data-rv="up"><span class="label">Black Paket</span>
      <h2 class="h2" style="margin-top:18px" data-split="line">Детали в едином<br><span class="it">чёрном</span> стиле</h2></div>
    <p class="lead" data-rv="up" style="--d:150ms">Электрощит, розетки, выключатели, светильники
    и ручки — одно оформление без визуального шума.</p>
  </div>
  <div class="mos" data-stagger="70">{mos}</div>
</div></section>""")

    objs = "".join(f"""
    <a class="obj" href="#cta"><span class="obj__n">{i+1:02d}</span>
      <span class="obj__t"><h3>{t}</h3><p>{d}</p></span>
      <span class="obj__go">{ARR}</span></a>""" for i, (t, d, im) in enumerate(OBJECTS))
    o.append(f"""
<section class="sec" id="objects"><div class="wrap">
  <span class="chapter">Объекты</span>
  <div class="sec-head" data-rv="up"><span class="label">Наши дома</span>
    <h2 class="h2" style="margin-top:18px">Реализованные <span class="it">объекты</span></h2></div>
  <div class="objs" data-stagger="70" data-rv-child="left">{objs}</div>
</div></section>""")

    o.append(f"""
<section class="sec"><div class="wrap ba-wrap">
  <div data-rv="up"><span class="label">Посмотрите разницу</span>
    <h2 class="h2" style="margin:18px 0 16px" data-split="line">Ваш дом у нас —<br>и ваш дом <span class="it">у вас</span></h2>
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
    <span class="label">Свяжитесь с нами</span>
    <h2 class="h2" style="margin:18px 0 16px">Оставьте заявку<br>и получите <span class="it">расчёт</span></h2>
    <p class="lead">Подберём планировку под участок и посчитаем стоимость с доставкой и монтажом.</p>
    <div style="margin-top:26px;display:grid;gap:6px;font-family:var(--font-head);font-size:1.7rem;font-weight:300">
      <a href="tel:{b['phone1_href']}">{b['phone1']}</a><a href="tel:{b['phone2_href']}">{b['phone2']}</a>
    </div>
  </div>
  <form data-form novalidate>
    <div class="f-row two">
      <div class="field"><label for="n7">Ваше имя</label>
        <input id="n7" type="text" required autocomplete="name" placeholder="Иван"><span class="err">Укажите имя</span></div>
      <div class="field"><label for="t7">Телефон</label>
        <input id="t7" type="tel" required autocomplete="tel" inputmode="tel" placeholder="+7 (___) ___-__-__">
        <span class="err">Введите номер полностью</span></div>
    </div>
    <div class="field"><label for="m7">Комментарий</label>
      <textarea id="m7" rows="4" placeholder="Интересует MODUL HOUSE 3, участок в Бердске"></textarea></div>
    <button class="btn btn--fill" type="submit" data-magnet=".2" style="justify-self:start">Отправить заявку {ARR}</button>
    <p class="form-note">Нажимая кнопку, вы соглашаетесь с обработкой персональных данных.</p>
    <div class="form-ok" role="status">Спасибо! Заявка принята — мы перезвоним в рабочее время.</div>
  </form>
</div></div></div></section>""")

    o.append(f"""
<footer class="foot" id="contacts"><div class="wrap">
  <div class="foot__grid">
    <div data-rv="up"><a class="logo" href="#top">ДОММ</a>
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

    extra = """
/* --- Горизонтальная прокрутка галереи --- */
(function(){
  var sec = document.querySelector('[data-hs]'); if(!sec) return;
  var pin = sec.querySelector('.hs__pin'), track = sec.querySelector('.hs__track');
  var wide = window.matchMedia('(min-width: 900px)');
  var RM = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var dist = 0, run = 0;
  /* лента едет быстрее прокрутки: иначе 13 кадров растягиваются на восемь экранов */
  var PACE = 0.62;

  function measure(){
    if(!wide.matches || RM){ sec.style.height = ''; track.style.transform = ''; return; }
    dist = Math.max(0, track.scrollWidth - window.innerWidth);
    run = dist * PACE;
    /* высота секции задаёт, сколько вертикальной прокрутки уйдёт на горизонтальный ход */
    sec.style.height = (window.innerHeight + run) + 'px';
    move();
  }
  function move(){
    if(!wide.matches || RM || !run) return;
    var top = sec.offsetTop;
    var p = (window.scrollY - top) / run;
    p = Math.max(0, Math.min(1, p));
    track.style.transform = 'translate3d(' + (-p * dist) + 'px,0,0)';
  }
  var tick = false;
  window.addEventListener('scroll', function(){
    if(tick) return; tick = true;
    requestAnimationFrame(function(){ move(); tick = false; });
  }, {passive:true});
  window.addEventListener('resize', measure);
  window.addEventListener('load', measure);
  if(wide.addEventListener) wide.addEventListener('change', measure);
  measure();
})();

/* --- Конфигуратор --- */
(function(){
  var root = document.getElementById('config'); if(!root) return;
  var steps = root.querySelectorAll('[data-wstep]');
  var dots  = root.querySelectorAll('.wiz__dots i');
  var ring  = root.querySelector('.ring .fg');
  var ringT = root.querySelector('[data-ring-txt]');
  var stNo  = root.querySelector('[data-step-no]');
  var stTtl = root.querySelector('[data-step-ttl]');
  var prev  = root.querySelector('[data-prev]');
  var next  = root.querySelector('[data-next]');
  var km    = root.querySelector('[data-km]');
  var kmOut = root.querySelector('[data-km-out]');
  var total = root.querySelector('[data-total]');
  var TITLES = ['Модель дома', 'Комплектация', 'Дополнительные опции', 'Фундамент и доставка'];
  var MONTAGE = %d, PER_KM = %d;
  var step = 1, cur = 0;

  function money(n){ return Math.round(n).toLocaleString('ru-RU') + ' ₽'; }

  function pick(sel, el){
    root.querySelectorAll(sel).forEach(function(x){ x.classList.remove('on'); });
    el.classList.add('on');
    calc();
  }
  root.querySelectorAll('[data-model]').forEach(function(x){
    x.addEventListener('click', function(){ pick('[data-model]', x); }); });
  root.querySelectorAll('[data-pack]').forEach(function(x){
    x.addEventListener('click', function(){ pick('[data-pack]', x); }); });
  root.querySelectorAll('[data-found]').forEach(function(x){
    x.addEventListener('click', function(){ pick('[data-found]', x); }); });
  root.querySelectorAll('[data-wopt] input').forEach(function(x){
    x.addEventListener('change', function(){
      x.closest('[data-wopt]').classList.toggle('on', x.checked);
      calc();
    });
  });
  if(km) km.addEventListener('input', calc);

  function show(n){
    step = Math.max(1, Math.min(steps.length, n));
    steps.forEach(function(s){ s.classList.toggle('on', +s.dataset.wstep === step); });
    dots.forEach(function(d, i){ d.classList.toggle('on', i < step); });
    ring.style.setProperty('--p', step / steps.length);
    ringT.textContent = step + '/' + steps.length;
    stNo.textContent = 'Шаг ' + step + ' из ' + steps.length;
    stTtl.textContent = TITLES[step - 1];
    prev.disabled = step === 1;
    next.innerHTML = step === steps.length ? 'Перейти к заявке' : 'Далее';
  }
  prev.addEventListener('click', function(){ show(step - 1); });
  next.addEventListener('click', function(){
    if(step === steps.length){ toRequest(); return; }
    show(step + 1);
  });

  function calc(){
    var m = root.querySelector('[data-model].on'),
        p = root.querySelector('[data-pack].on'),
        f = root.querySelector('[data-found].on');
    var base = parseFloat(m.dataset.price) * parseFloat(p.dataset.k);
    var add = 0, names = [];
    root.querySelectorAll('[data-wopt] input:checked').forEach(function(x){
      add += parseFloat(x.value); names.push(x.dataset.name);
    });
    var d = km ? +km.value : 0;
    var log = MONTAGE + d * PER_KM;
    var sum = base + add + parseFloat(f.dataset.price) + log;

    root.querySelector('[data-r-model]').textContent = m.dataset.name;
    root.querySelector('[data-r-pack]').textContent  = p.dataset.name;
    root.querySelector('[data-r-opts]').textContent  = names.length ? names.length + ' шт · ' + money(add) : '—';
    root.querySelector('[data-r-found]').textContent = f.dataset.name;
    root.querySelector('[data-r-log]').textContent   = money(log) + ' · ' + d + ' км';
    if(kmOut) kmOut.textContent = d + ' км';

    var from = cur, t0 = null; cur = sum;
    if(window.matchMedia('(prefers-reduced-motion: reduce)').matches){ total.textContent = money(sum); return; }
    /* первый кадр только через rAF: при прямом вызове t === undefined и сумма даёт NaN */
    requestAnimationFrame(function anim(t){
      if(t0 === null) t0 = t;
      var q = Math.min((t - t0) / 480, 1), e = 1 - Math.pow(1 - q, 3);
      total.textContent = money(from + (sum - from) * e);
      if(q < 1) requestAnimationFrame(anim);
    });
  }

  /* смета уезжает в заявку — человеку не нужно ничего описывать */
  function toRequest(){
    var box = document.querySelector('#cta textarea');
    if(box){
      var rows = [];
      root.querySelectorAll('.wiz__rows div').forEach(function(r){
        rows.push(r.querySelector('span').textContent + ': ' + r.querySelector('b').textContent);
      });
      box.value = 'Расчёт из конфигуратора — ' + total.textContent + '\\n' + rows.join('\\n');
    }
    var cta = document.getElementById('cta');
    if(cta) cta.scrollIntoView({behavior:'smooth', block:'start'});
    setTimeout(function(){ var n = document.querySelector('#cta input[type="text"]'); if(n) n.focus(); }, 700);
  }
  var send = root.querySelector('[data-send-cfg]');
  if(send) send.addEventListener('click', function(e){ e.preventDefault(); toRequest(); });

  show(1); calc();
})();
""" % (MONTAGE, PER_KM)
    o.append(core.tail(extra))
    return "".join(o)
