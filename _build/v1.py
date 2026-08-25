# -*- coding: utf-8 -*-
"""Вариант 1 — NORDIC NOIR. Тёмный кинематографичный премиум, латунный акцент."""
import core
from data import *

FONTS = '<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@200;300;400;500;600;700;800&family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300&display=swap" rel="stylesheet">'

CSS = r"""
:root{
  --bg:#0B0B0C; --bg-2:#111113; --bg-3:#17171A;
  --fg:#EDEBE7; --muted:#8E8A83; --line:rgba(237,235,231,.12);
  --accent:#C8A56B; --on-accent:#0B0B0C; --input-bg:rgba(255,255,255,.03);
  --font-head:'Manrope',system-ui,sans-serif; --font-body:'Manrope',system-ui,sans-serif;
  --font-alt:'Cormorant Garamond',Georgia,serif;
  --radius:6px; --radius-sm:4px; --head-weight:300;
}
body{background:var(--bg)}
::selection{background:var(--accent);color:var(--on-accent)}
.h1{font-size:clamp(2.6rem,7.4vw,6.6rem);font-weight:200;letter-spacing:-.03em;line-height:.95}
.h2{font-size:clamp(1.9rem,4.4vw,3.8rem);font-weight:200;letter-spacing:-.025em}
.h3{font-size:clamp(1.15rem,2vw,1.6rem);font-weight:500;letter-spacing:-.01em}
.it{font-family:var(--font-alt);font-style:italic;font-weight:300}
.kicker{display:inline-flex;align-items:center;gap:12px;font-size:11px;letter-spacing:.28em;
  text-transform:uppercase;color:var(--accent);max-width:100%;flex-wrap:wrap}
.kicker::before{content:"";width:34px;height:1px;background:var(--accent);opacity:.7}
.lead{color:var(--muted);font-size:clamp(1rem,1.3vw,1.14rem);font-weight:300;max-width:62ch}
section{position:relative}
.sec{padding:clamp(80px,11vw,170px) 0}
.sec-head{display:grid;gap:24px;margin-bottom:clamp(40px,5vw,72px)}
@media(min-width:900px){.sec-head.split{grid-template-columns:1.15fr .85fr;align-items:end;gap:60px}}

/* --- Шапка --- */
.hdr{position:fixed;inset:0 0 auto 0;z-index:100;padding:20px 0;
  transition:background .5s cubic-bezier(.16,1,.3,1),padding .5s,transform .5s,backdrop-filter .5s}
.hdr.stuck{background:rgba(11,11,12,.72);backdrop-filter:blur(18px) saturate(140%);
  padding:12px 0;border-bottom:1px solid var(--line)}
.hdr.hide{transform:translateY(-102%)}
.hdr__in{display:flex;align-items:center;justify-content:space-between;gap:24px}
.logo{display:flex;align-items:baseline;gap:11px;font-weight:700;letter-spacing:.28em;font-size:15px}
.logo span{font-size:10px;letter-spacing:.2em;color:var(--muted);font-weight:400}
.nav{display:none;gap:34px}
@media(min-width:1024px){.nav{display:flex}}
.nav a{position:relative;font-size:12px;letter-spacing:.16em;text-transform:uppercase;
  color:var(--muted);transition:color .3s;padding:4px 0}
.nav a::after{content:"";position:absolute;left:0;bottom:0;height:1px;width:100%;background:var(--accent);
  transform:scaleX(0);transform-origin:100% 50%;transition:transform .45s cubic-bezier(.16,1,.3,1)}
.nav a:hover{color:var(--fg)}
.nav a:hover::after{transform:scaleX(1);transform-origin:0 50%}
.hdr .hdr__cta{display:none}
@media(min-width:640px){.hdr .hdr__cta{display:inline-flex}}
.btn{position:relative;display:inline-flex;align-items:center;justify-content:center;gap:10px;
  padding:15px 30px;border-radius:100px;font-size:12px;letter-spacing:.16em;text-transform:uppercase;
  font-weight:600;overflow:hidden;isolation:isolate;
  transform:translate3d(var(--tx,0),var(--ty,0),0);
  transition:transform .4s cubic-bezier(.16,1,.3,1),color .35s,border-color .35s}
.btn--fill{background:var(--accent);color:var(--on-accent)}
.btn--fill::before{content:"";position:absolute;inset:0;z-index:-1;background:var(--fg);
  transform:translateY(101%);transition:transform .5s cubic-bezier(.16,1,.3,1)}
.btn--fill:hover::before{transform:translateY(0)}
.btn--fill:hover{color:var(--bg)}
.btn--ghost{border:1px solid var(--line);color:var(--fg)}
.btn--ghost::before{content:"";position:absolute;inset:0;z-index:-1;background:var(--accent);
  transform:translateY(101%);transition:transform .5s cubic-bezier(.16,1,.3,1)}
.btn--ghost:hover{color:var(--on-accent);border-color:var(--accent)}
.btn--ghost:hover::before{transform:translateY(0)}
.burger{display:grid;gap:5px;padding:10px;margin:-10px}
@media(min-width:1024px){.burger{display:none}}
.burger i{display:block;width:24px;height:1.5px;background:var(--fg);transition:transform .4s,opacity .3s}
body.nav-open .burger i:nth-child(1){transform:translateY(6.5px) rotate(45deg)}
body.nav-open .burger i:nth-child(2){opacity:0}
body.nav-open .burger i:nth-child(3){transform:translateY(-6.5px) rotate(-45deg)}
.mnav{position:fixed;inset:0;z-index:99;background:var(--bg-2);display:grid;align-content:center;
  gap:8px;padding:0 var(--gutter);opacity:0;visibility:hidden;transition:opacity .5s,visibility .5s}
body.nav-open .mnav{opacity:1;visibility:visible}
.mnav a{font-family:var(--font-head);font-size:clamp(2rem,9vw,3.2rem);font-weight:200;letter-spacing:-.02em;
  opacity:0;transform:translateY(24px);transition:opacity .6s cubic-bezier(.16,1,.3,1),transform .6s cubic-bezier(.16,1,.3,1),color .3s}
body.nav-open .mnav a{opacity:1;transform:none}
.mnav a:hover{color:var(--accent)}
.mnav a:nth-child(1){transition-delay:.08s}.mnav a:nth-child(2){transition-delay:.14s}
.mnav a:nth-child(3){transition-delay:.2s}.mnav a:nth-child(4){transition-delay:.26s}
.mnav a:nth-child(5){transition-delay:.32s}
.mnav__foot{margin-top:36px;display:grid;gap:6px;color:var(--muted);font-size:14px}

/* --- Герой --- */
.hero{position:relative;min-height:100svh;display:flex;align-items:flex-end;
  padding:140px 0 56px;overflow:hidden}
.hero__bg{position:absolute;inset:-6%;background-size:cover;background-position:center;
  animation:ken 26s ease-in-out infinite alternate;transform-origin:60% 40%}
@keyframes ken{from{transform:scale(1.06)}to{transform:scale(1.2) translate3d(-1.5%,-1%,0)}}
.hero::after{content:"";position:absolute;inset:0;pointer-events:none;
  background:linear-gradient(180deg,rgba(11,11,12,.86) 0%,rgba(11,11,12,.32) 28%,rgba(11,11,12,.74) 60%,rgba(11,11,12,.98) 100%)}
.hero__in{position:relative;z-index:2}
.hero__grid{display:grid;gap:38px}
@media(min-width:1024px){.hero__grid{grid-template-columns:1.4fr .6fr;align-items:end;gap:56px}}
.hero .h1{margin:24px 0 26px}
.hero__side{display:grid;gap:26px;padding-bottom:8px}
.hero__price{font-size:clamp(2.1rem,3.6vw,3rem);font-weight:200;letter-spacing:-.03em;color:var(--accent)}
.hero__price small{display:block;font-size:11px;letter-spacing:.24em;text-transform:uppercase;
  color:var(--muted);margin-bottom:8px;font-weight:400}
.hero__acts{display:flex;flex-wrap:wrap;gap:14px;margin-top:34px}
.scrollcue{position:absolute;left:50%;bottom:26px;z-index:3;translate:-50% 0;display:grid;justify-items:center;gap:10px;
  font-size:10px;letter-spacing:.24em;text-transform:uppercase;color:var(--muted)}
.scrollcue i{display:block;width:1px;height:56px;background:linear-gradient(var(--accent),transparent);
  animation:cue 2.4s ease-in-out infinite}
@keyframes cue{0%,100%{transform:scaleY(.3);transform-origin:0 0;opacity:.4}50%{transform:scaleY(1);opacity:1}}
@media(max-width:640px){.scrollcue{display:none}}

/* --- Тикер --- */
.ticker{border-block:1px solid var(--line);padding:22px 0;background:var(--bg-2);--mq-gap:0px}
.ticker .marquee__track{--mq-dur:36s}
.tick{display:flex;align-items:center;gap:22px;padding-right:22px;white-space:nowrap}
.tick b{font-size:clamp(1.5rem,2.4vw,2.1rem);font-weight:200;color:var(--accent);letter-spacing:-.02em}
.tick span{font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:var(--muted)}
.tick em{font-style:normal;color:var(--line)}

/* --- О компании --- */
.about{display:grid;gap:44px}
@media(min-width:1000px){.about{grid-template-columns:1fr 1fr;gap:80px;align-items:center}}
.about__media{position:relative;overflow:hidden;border-radius:var(--radius);aspect-ratio:4/5}
.about__media img{width:100%;height:100%;object-fit:cover;transform:translate3d(0,var(--par,0),0) scale(1.14)}
.about__facts{display:grid;grid-template-columns:1fr 1fr;gap:1px;background:var(--line);
  border:1px solid var(--line);margin-top:34px}
.about__facts div{background:var(--bg);padding:24px 20px}
.about__facts b{display:block;font-size:2rem;font-weight:200;color:var(--accent);letter-spacing:-.02em}
.about__facts span{font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--muted)}

/* --- Галерея --- */
.strip{display:flex;gap:16px;overflow-x:auto;scroll-snap-type:x mandatory;padding-bottom:20px;
  cursor:grab;scrollbar-width:thin;scrollbar-color:var(--line) transparent}
.strip.dragging{cursor:grabbing;scroll-snap-type:none}
.strip::-webkit-scrollbar{height:3px}
.strip::-webkit-scrollbar-thumb{background:var(--line)}
.strip figure{flex:0 0 clamp(260px,42vw,460px);margin:0;scroll-snap-align:start;
  aspect-ratio:4/3;overflow:hidden;border-radius:var(--radius);position:relative}
.strip img{width:100%;height:100%;object-fit:cover;transition:transform 1.1s cubic-bezier(.16,1,.3,1),filter .6s;
  filter:saturate(.85) contrast(1.04)}
.strip figure:hover img{transform:scale(1.07);filter:saturate(1) contrast(1.04)}

/* --- Проекты --- */
.cards{display:grid;gap:20px}
@media(min-width:700px){.cards{grid-template-columns:repeat(2,1fr)}}
@media(min-width:1100px){.cards{grid-template-columns:repeat(3,1fr)}}
.card{position:relative;overflow:hidden;border-radius:var(--radius);background:var(--bg-2);
  border:1px solid var(--line);transition:border-color .5s,transform .6s cubic-bezier(.16,1,.3,1)}
.card:hover{border-color:color-mix(in srgb,var(--accent) 55%,transparent);transform:translateY(-6px)}
.card__img{position:relative;aspect-ratio:4/3;overflow:hidden}
.card__img img{width:100%;height:100%;object-fit:cover;transition:transform 1.2s cubic-bezier(.16,1,.3,1),filter .6s;
  filter:brightness(.88)}
.card:hover .card__img img{transform:scale(1.08);filter:brightness(1)}
.card__area{position:absolute;top:14px;left:14px;padding:7px 13px;border-radius:100px;font-size:11px;
  letter-spacing:.14em;background:rgba(11,11,12,.62);backdrop-filter:blur(8px);border:1px solid var(--line)}
.card__body{padding:24px 22px 26px;display:grid;gap:10px}
.card__body p{color:var(--muted);font-size:14px;font-weight:300;min-height:44px}
.card__price{display:flex;align-items:baseline;justify-content:space-between;gap:12px;
  margin-top:8px;padding-top:16px;border-top:1px solid var(--line)}
.card__price b{font-size:1.35rem;font-weight:300;color:var(--accent);letter-spacing:-.02em}
.card__price span{font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--muted)}
.card__go{display:inline-flex;align-items:center;gap:9px;font-size:11px;letter-spacing:.16em;
  text-transform:uppercase;color:var(--fg);margin-top:6px}
.card__go svg{transition:transform .4s cubic-bezier(.16,1,.3,1)}
.card:hover .card__go svg{transform:translateX(6px)}

/* --- Вкладки планировок --- */
.tabs{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:36px}
.tabs button{padding:13px 24px;border:1px solid var(--line);border-radius:100px;font-size:11px;
  letter-spacing:.16em;text-transform:uppercase;color:var(--muted);transition:.35s}
.tabs button.active{background:var(--accent);color:var(--on-accent);border-color:var(--accent)}
.tabs button:hover{color:var(--fg)}
.tabs button.active:hover{color:var(--on-accent)}
.plans{display:grid;gap:16px}
@media(min-width:620px){.plans{grid-template-columns:repeat(2,1fr)}}
@media(min-width:1000px){.plans{grid-template-columns:repeat(3,1fr)}}
@media(min-width:1300px){.plans{grid-template-columns:repeat(4,1fr)}}
.plan{border:1px solid var(--line);border-radius:var(--radius);overflow:hidden;background:var(--bg-2);
  transition:.5s cubic-bezier(.16,1,.3,1);cursor:zoom-in}
.plan:hover{background:var(--bg-3);border-color:color-mix(in srgb,var(--accent) 45%,transparent);transform:translateY(-4px)}
.plan__img{aspect-ratio:1/1;background:#fff;padding:12px;overflow:hidden}
.plan__img img{width:100%;height:100%;object-fit:contain;transition:transform .8s cubic-bezier(.16,1,.3,1)}
.plan:hover .plan__img img{transform:scale(1.06)}
.plan__b{padding:18px;display:grid;gap:6px}
.plan__b h4{font-size:14px;font-weight:600;letter-spacing:.02em}
.plan__b .m{font-size:12px;color:var(--muted);letter-spacing:.1em;text-transform:uppercase}
.plan__b .p{font-size:1.05rem;color:var(--accent);font-weight:300}

/* --- Комплектация --- */
.spec{display:grid;gap:20px}
@media(min-width:1000px){.spec{grid-template-columns:1.35fr .82fr .82fr;gap:20px}}
.spec__col{border:1px solid var(--line);border-radius:var(--radius);padding:32px 26px;background:var(--bg-2);
  transition:border-color .5s,background .5s}
.spec__col:hover{border-color:color-mix(in srgb,var(--accent) 40%,transparent)}
.spec__col h3{margin-bottom:22px;font-size:1.05rem;font-weight:600;letter-spacing:.01em}
.spec__col li{display:flex;gap:12px;padding:9px 0;font-size:14px;font-weight:300;color:var(--muted);
  border-bottom:1px solid rgba(237,235,231,.05);line-height:1.5}
.spec__col li:last-child{border:0}
.spec__col svg{flex:0 0 15px;margin-top:4px}
.spec--in svg{color:var(--accent)}
.spec--out svg{color:#6E6A64}
.spec--in li{color:var(--fg)}

/* --- Процесс: липкая прокрутка --- */
.proc{display:grid;gap:40px}
@media(min-width:1000px){.proc{grid-template-columns:.9fr 1.1fr;gap:70px;align-items:start}}
.proc__sticky{position:sticky;top:120px}
.proc__media{aspect-ratio:4/3;border-radius:var(--radius);overflow:hidden;position:relative;background:var(--bg-2)}
.proc__media img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:0;
  transform:scale(1.08);transition:opacity .9s cubic-bezier(.16,1,.3,1),transform 1.4s cubic-bezier(.16,1,.3,1)}
.proc__media img.on{opacity:1;transform:scale(1)}
.proc__steps{display:grid;gap:0}
.step{padding:38px 0;border-bottom:1px solid var(--line);opacity:.4;transition:opacity .6s}
.step.on{opacity:1}
.step__n{font-size:11px;letter-spacing:.24em;color:var(--accent);margin-bottom:14px;display:block}
.step h3{margin-bottom:14px}
.step p{color:var(--muted);font-size:15px;font-weight:300}
.step__bar{height:1px;background:var(--line);margin-top:22px;overflow:hidden}
.step__bar i{display:block;height:100%;background:var(--accent);transform:scaleX(0);transform-origin:0 50%;
  transition:transform .8s cubic-bezier(.16,1,.3,1)}
.step.on .step__bar i{transform:scaleX(1)}

/* --- Детали / интерьер --- */
.mosaic{display:grid;gap:16px;grid-template-columns:repeat(2,1fr)}
@media(min-width:900px){.mosaic{grid-template-columns:repeat(3,1fr)}}
.tile{position:relative;overflow:hidden;border-radius:var(--radius);aspect-ratio:3/4;cursor:zoom-in}
.tile:nth-child(3n+1){aspect-ratio:3/4}
@media(min-width:900px){.tile:nth-child(4){grid-column:span 2;aspect-ratio:16/9}}
.tile img{width:100%;height:100%;object-fit:cover;transition:transform 1.2s cubic-bezier(.16,1,.3,1),filter .6s;
  filter:brightness(.82)}
.tile:hover img{transform:scale(1.06);filter:brightness(1)}
.tile figcaption{position:absolute;inset:auto 0 0 0;padding:70px 20px 20px;font-size:13px;font-weight:300;
  background:linear-gradient(transparent,rgba(11,11,12,.92));
  transform:translateY(8px);opacity:.9;transition:transform .5s cubic-bezier(.16,1,.3,1),opacity .5s}
.tile:hover figcaption{transform:none;opacity:1}

/* --- Объекты --- */
.objs{display:grid;gap:1px;background:var(--line);border-block:1px solid var(--line)}
.obj{position:relative;background:var(--bg);display:grid;grid-template-columns:auto 1fr auto;gap:20px;
  align-items:center;padding:30px 8px;transition:background .5s,padding-left .5s cubic-bezier(.16,1,.3,1)}
.obj:hover{background:var(--bg-2);padding-left:24px}
.obj__n{font-size:11px;color:var(--accent);letter-spacing:.2em}
.obj__t{display:block}
.obj__t h3{font-size:clamp(1.2rem,2.6vw,2rem);font-weight:200;letter-spacing:-.02em}
.obj__t p{color:var(--muted);font-size:14px;font-weight:300;margin-top:6px}
.obj__go{width:44px;height:44px;border-radius:50%;border:1px solid var(--line);display:grid;place-items:center;
  transition:.4s}
.obj:hover .obj__go{background:var(--accent);color:var(--on-accent);border-color:var(--accent);transform:rotate(-45deg)}
.obj__peek{position:fixed;z-index:60;width:300px;aspect-ratio:4/3;border-radius:var(--radius);overflow:hidden;
  pointer-events:none;opacity:0;transform:translate(-50%,-50%) scale(.9);transition:opacity .35s,transform .5s cubic-bezier(.16,1,.3,1);
  box-shadow:0 30px 80px rgba(0,0,0,.6)}
.obj__peek.on{opacity:1;transform:translate(-50%,-50%) scale(1)}
.obj__peek img{width:100%;height:100%;object-fit:cover}
@media(max-width:900px){.obj__peek{display:none}
  .obj{grid-template-columns:auto 1fr;padding:22px 8px}.obj__go{display:none}}

/* --- До/После --- */
.ba-wrap{display:grid;gap:40px;align-items:center}
@media(min-width:1000px){.ba-wrap{grid-template-columns:.8fr 1.2fr;gap:70px}}

/* --- Заявка --- */
.cta{position:relative;overflow:hidden;background:var(--bg-2);border-block:1px solid var(--line)}
.cta__glow{position:absolute;width:60vw;aspect-ratio:1;border-radius:50%;left:-10vw;top:-30vw;
  background:radial-gradient(circle,color-mix(in srgb,var(--accent) 20%,transparent),transparent 62%);
  filter:blur(40px);animation:float 18s ease-in-out infinite alternate}
@keyframes float{to{transform:translate3d(18vw,12vw,0) scale(1.18)}}
.cta__in{position:relative;display:grid;gap:44px}
@media(min-width:1000px){.cta__in{grid-template-columns:1fr 1fr;gap:80px;align-items:center}}
.cta form{display:grid;gap:16px}

/* --- Подвал --- */
.foot{padding:80px 0 40px;background:var(--bg)}
.foot__grid{display:grid;gap:40px}
@media(min-width:800px){.foot__grid{grid-template-columns:1.4fr 1fr 1fr 1fr}}
.foot h4{font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:var(--muted);margin-bottom:18px;font-weight:500}
.foot li,.foot p{font-size:15px;font-weight:300;margin-bottom:10px}
.foot a{transition:color .3s}.foot a:hover{color:var(--accent)}
.foot__bot{margin-top:60px;padding-top:26px;border-top:1px solid var(--line);display:flex;
  flex-wrap:wrap;gap:14px;justify-content:space-between;font-size:12px;color:var(--muted)}
.foot__big{font-size:clamp(3rem,17vw,15rem);font-weight:200;letter-spacing:-.05em;line-height:.8;
  color:transparent;-webkit-text-stroke:1px rgba(237,235,231,.14);margin-top:70px;text-align:center;user-select:none}
"""

def icon_check():
    return '<svg width="15" height="15" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M2.5 8.5l3.5 3.5 7.5-8"/></svg>'
def icon_minus():
    return '<svg width="15" height="15" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M3 8h10"/></svg>'
def icon_plus():
    return '<svg width="15" height="15" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M8 3v10M3 8h10"/></svg>'
def arrow():
    return '<svg width="16" height="10" viewBox="0 0 18 10" fill="none" stroke="currentColor" stroke-width="1.4" aria-hidden="true"><path d="M0 5h16M12 1l4 4-4 4"/></svg>'

def build():
    b = BRAND
    nav = "".join(f'<a href="{h}">{t}</a>' for h, t in NAV)
    out = [core.head("ДОММ — модульные дома для жизни и отдыха | Новосибирск",
                     "Модульные дома под ключ от 990 000 ₽ за 30 дней. Собственное производство в Новосибирске, более 80 реализованных проектов.",
                     FONTS, CSS, "#0B0B0C")]
    out.append('<div class="cursor"></div>')

    # Шапка
    out.append(f"""
<header class="hdr" data-header>
  <div class="wrap hdr__in">
    <a class="logo" href="#top">ДОММ<span>модульные дома</span></a>
    <nav class="nav">{nav}</nav>
    <a class="btn btn--ghost hdr__cta" href="tel:{b['phone2_href']}" data-magnet=".25">Заказать расчёт</a>
    <button class="burger" data-burger aria-label="Меню" aria-expanded="false"><i></i><i></i><i></i></button>
  </div>
</header>
<nav class="mnav" data-menu>
  {nav}
  <div class="mnav__foot">
    <a href="tel:{b['phone1_href']}">{b['phone1']}</a>
    <a href="tel:{b['phone2_href']}">{b['phone2']}</a>
    <a href="mailto:{b['email']}">{b['email']}</a>
  </div>
</nav>""")

    # Герой
    out.append(f"""
<section class="hero" id="top">
  <div class="hero__bg" style="background-image:url('{HERO['bg']}')"></div>
  <div class="wrap hero__in">
    <div class="hero__grid">
      <div data-rv="up">
        <span class="kicker">{HERO['kicker']}</span>
        <h1 class="h1" data-split="line">Модульные дома<br><span class="it">для жизни</span> и отдыха</h1>
        <p class="lead">{HERO['sub']} {HERO['sub2']}</p>
        <div class="hero__acts">
          <a class="btn btn--fill" href="#projects" data-magnet=".3">Смотреть проекты {arrow()}</a>
          <a class="btn btn--ghost" href="{b['wa']}" target="_blank" rel="noopener" data-magnet=".25">Написать в WhatsApp</a>
        </div>
      </div>
      <div class="hero__side" data-rv="up" style="--d:260ms">
        <div class="hero__price"><small>Под ключ от</small>990 000 ₽</div>
        <div class="hero__price"><small>Срок производства</small>30 дней</div>
      </div>
    </div>
  </div>
  <div class="scrollcue"><i></i>Листайте</div>
</section>""")

    # Тикер
    tick = "".join(f'<div class="tick"><b>{v}</b><span>{t}</span><em>/</em></div>' for v, t in STATS * 2)
    out.append(f"""
<section class="ticker"><div class="marquee">
  <div class="marquee__track">{tick}</div><div class="marquee__track" aria-hidden="true">{tick}</div>
</div></section>""")

    # О компании
    facts = "".join(f'<div><b>{v}</b><span>{t}</span></div>' for v, t in STATS)
    out.append(f"""
<section class="sec" id="about">
  <div class="wrap about">
    <div class="about__media" data-rv="mask">
      <img src="{GALLERY[0]}" alt="Модульный дом ДОММ с террасой" loading="lazy" data-par="70">
    </div>
    <div data-rv="up">
      <span class="kicker">О производстве</span>
      <h2 class="h2" style="margin:22px 0 24px" data-split="line">Дом, который<br>приезжает <span class="it">готовым</span></h2>
      <p class="lead">Мы производим модули в цехе в Новосибирске: с отделкой, окнами, электрикой,
      водопроводом и готовым санузлом. На участок дом приезжает на трале, а силовой монтаж
      краном занимает один день. Вам остаётся только внести мебель.</p>
      <div class="about__facts">{facts}</div>
    </div>
  </div>
</section>""")

    # Галерея
    figs = "".join(
        f'<figure data-lb="g" data-full="{u}" data-cap="Дом ДОММ — фото {i+1}"><img src="{u}" alt="Интерьер и экстерьер модульного дома ДОММ" loading="lazy"></figure>'
        for i, u in enumerate(GALLERY))
    out.append(f"""
<section class="sec" id="gallery" style="padding-top:0">
  <div class="wrap sec-head split">
    <div data-rv="up"><span class="kicker">Галерея</span>
      <h2 class="h2" style="margin-top:22px" data-split="line">Декорируем дома<br>в <span class="it">уютном</span> стиле</h2></div>
    <p class="lead" data-rv="up" style="--d:160ms">Тёплое дерево, чёрная фурнитура, панорамные окна и мягкий свет.
    Потяните ленту в сторону — или нажмите на фото, чтобы открыть его целиком.</p>
  </div>
  <div class="wrap"><div class="strip" data-drag>{figs}</div></div>
</section>""")

    # Проекты
    cards = "".join(f"""
    <article class="card" data-rv="up">
      <div class="card__img"><span class="card__area">{area}</span>
        <img src="{im}" alt="{name}" loading="lazy"></div>
      <div class="card__body">
        <h3 class="h3">{name}</h3><p>{desc}</p>
        <div class="card__price"><b>от {price} ₽</b><span>под ключ</span></div>
        <a class="card__go" href="#cta">Узнать подробнее {arrow()}</a>
      </div>
    </article>""" for name, desc, price, area, im in PROJECTS)
    out.append(f"""
<section class="sec" id="projects">
  <div class="wrap">
    <div class="sec-head split">
      <div data-rv="up"><span class="kicker">Каталог</span>
        <h2 class="h2" style="margin-top:22px" data-split="line">Проекты домов<br>и <span class="it">бань</span></h2></div>
      <p class="lead" data-rv="up" style="--d:160ms">Семь базовых моделей и две бани. Любую планировку
      адаптируем под ваш участок и сценарий жизни.</p>
    </div>
    <div class="cards" data-stagger="90">{cards}</div>
  </div>
</section>""")

    # Планировки
    def plan_grid(items, key):
        return "".join(f"""
      <article class="plan" data-lb="{key}" data-full="{im}" data-cap="{n} — {a}, от {p} тыс. ₽">
        <div class="plan__img"><img src="{im}" alt="Планировка {n}" loading="lazy"></div>
        <div class="plan__b"><h4>{n}</h4><span class="m">{a}{' · ' + note if note else ''}</span>
          <span class="p">от {p} тыс. ₽</span></div>
      </article>""" for n, a, p, im, note in items)
    out.append(f"""
<section class="sec" id="prices" style="background:var(--bg-2);border-block:1px solid var(--line)">
  <div class="wrap" data-tabs>
    <div class="sec-head split">
      <div data-rv="up"><span class="kicker">Планировки и цены</span>
        <h2 class="h2" style="margin-top:22px" data-split="line">Выберите свой<br><span class="it">метраж</span></h2></div>
      <p class="lead" data-rv="up" style="--d:160ms">Дома собираются из модулей 2,5×6 м и 3×6 м.
      Нажмите на планировку, чтобы рассмотреть её крупно.</p>
    </div>
    <div class="tabs" role="tablist">
      <button data-tab="a" class="active" role="tab" aria-selected="true">Модули 2,5 × 6</button>
      <button data-tab="b" role="tab" aria-selected="false">Модули 3 × 6</button>
      <button data-tab="c" role="tab" aria-selected="false">Визуализации</button>
    </div>
    <div class="plans" data-panel="a" data-stagger="60">{plan_grid(PLANS_25,'p25')}</div>
    <div class="plans" data-panel="b" hidden data-stagger="60">{plan_grid(PLANS_36,'p36')}</div>
    <div class="cards" data-panel="c" hidden data-stagger="80">{"".join(f'''
      <article class="card" data-lb="rn" data-full="{im}" data-cap="{n}">
        <div class="card__img"><img src="{im}" alt="{n}" loading="lazy"></div>
        <div class="card__body"><h3 class="h3">{n}</h3><p>{d}</p></div>
      </article>''' for n, d, im in RENDERS)}</div>
  </div>
</section>""")

    # Комплектация
    li_in = "".join(f'<li>{icon_check()}<span>{t}</span></li>' for t in INCLUDED)
    li_out = "".join(f'<li>{icon_minus()}<span>{t}</span></li>' for t in EXCLUDED)
    li_op = "".join(f'<li>{icon_plus()}<span>{t}</span></li>' for t in OPTIONS)
    out.append(f"""
<section class="sec" id="spec">
  <div class="wrap">
    <div class="sec-head split">
      <div data-rv="up"><span class="kicker">Комплектация</span>
        <h2 class="h2" style="margin-top:22px" data-split="line">Что входит<br>в <span class="it">базовую</span> стоимость</h2></div>
      <p class="lead" data-rv="up" style="--d:160ms">Честный список без звёздочек: что вы получаете сразу,
      что оплачивается отдельно и что можно добавить по желанию.</p>
    </div>
    <div class="spec" data-stagger="110">
      <div class="spec__col spec--in"><h3>Входит в стоимость</h3><ul>{li_in}</ul></div>
      <div class="spec__col spec--out"><h3>Не входит</h3><ul>{li_out}</ul></div>
      <div class="spec__col spec--in"><h3>Дополнительные опции</h3><ul>{li_op}</ul></div>
    </div>
  </div>
</section>""")

    # Процесс
    imgs = "".join(f'<img src="{im}" alt="{t}" class="{"on" if i==0 else ""}" loading="lazy" data-pi="{i}">'
                   for i, (n, t, d, im) in enumerate(PROCESS))
    steps = "".join(f"""
      <article class="step{' on' if i==0 else ''}" data-step="{i}">
        <span class="step__n">Этап {n}</span><h3 class="h3">{t}</h3><p>{d}</p>
        <div class="step__bar"><i></i></div>
      </article>""" for i, (n, t, d, im) in enumerate(PROCESS))
    out.append(f"""
<section class="sec" id="process" style="background:var(--bg-2);border-block:1px solid var(--line)">
  <div class="wrap">
    <div class="sec-head" data-rv="up"><span class="kicker">Как мы работаем</span>
      <h2 class="h2" style="margin-top:22px" data-split="line">Четыре шага<br>до <span class="it">новоселья</span></h2></div>
    <div class="proc">
      <div class="proc__sticky"><div class="proc__media">{imgs}</div></div>
      <div class="proc__steps">{steps}</div>
    </div>
  </div>
</section>""")

    # Детали + интерьер
    tiles = "".join(f"""
      <figure class="tile" data-lb="d" data-full="{im}" data-cap="{t}">
        <img src="{im}" alt="{t}" loading="lazy"><figcaption>{t}</figcaption></figure>""" for t, im in DETAILS + INTERIOR)
    out.append(f"""
<section class="sec" id="details">
  <div class="wrap">
    <div class="sec-head split">
      <div data-rv="up"><span class="kicker">Black Paket</span>
        <h2 class="h2" style="margin-top:22px" data-split="line">Детали в едином<br><span class="it">чёрном</span> стиле</h2></div>
      <p class="lead" data-rv="up" style="--d:160ms">Электрощит, розетки, выключатели, светильники, дверные ручки
      и фасадный свет — всё в одном оформлении, без визуального шума.</p>
    </div>
    <div class="mosaic" data-stagger="80">{tiles}</div>
  </div>
</section>""")

    # До/После
    out.append(f"""
<section class="sec" style="background:var(--bg-2);border-block:1px solid var(--line)">
  <div class="wrap ba-wrap">
    <div data-rv="up"><span class="kicker">Посмотрите разницу</span>
      <h2 class="h2" style="margin:22px 0 22px" data-split="line">Ваш дом у нас —<br>и <span class="it">ваш дом</span> у вас</h2>
      <p class="lead">Слева — модуль на производстве, справа — тот же дом на участке.
      Потяните ползунок, чтобы сравнить.</p></div>
    <div class="ba" data-rv="zoom" role="img" aria-label="Сравнение: дом на производстве и дом на участке">
      <img src="{BEFORE}" alt="Модуль на производстве" loading="lazy">
      <img class="ba__after" src="{AFTER}" alt="Готовый дом на участке" loading="lazy">
      <span class="ba__line"></span>
      <span class="ba__grip">&#8596;</span>
      <span class="ba__tag l">Ваш дом у нас</span><span class="ba__tag r">Ваш дом у вас</span>
    </div>
  </div>
</section>""")

    # Объекты
    objs = "".join(f"""
    <a class="obj" href="#cta" data-peek="{im}">
      <span class="obj__n">{i+1:02d}</span>
      <span class="obj__t"><h3>{t}</h3><p>{d}</p></span>
      <span class="obj__go">{arrow()}</span>
    </a>""" for i, (t, d, im) in enumerate(OBJECTS))
    out.append(f"""
<section class="sec" id="objects">
  <div class="wrap">
    <div class="sec-head" data-rv="up"><span class="kicker">Наши дома</span>
      <h2 class="h2" style="margin-top:22px" data-split="line">Реализованные <span class="it">объекты</span></h2></div>
    <div class="objs" data-stagger="70" data-rv-child="left">{objs}</div>
  </div>
  <div class="obj__peek"><img src="" alt=""></div>
</section>""")

    # Заявка
    out.append(f"""
<section class="sec cta" id="cta">
  <div class="cta__glow"></div>
  <div class="wrap cta__in">
    <div data-rv="up">
      <span class="kicker">Свяжитесь с нами</span>
      <h2 class="h2" style="margin:22px 0 22px" data-split="line">Оставьте заявку<br>и получите <span class="it">расчёт</span></h2>
      <p class="lead">Ответим в рабочее время, подберём планировку под участок и посчитаем стоимость
      с доставкой и монтажом.</p>
      <div style="margin-top:34px;display:grid;gap:8px">
        <a href="tel:{b['phone1_href']}" style="font-size:1.5rem;font-weight:200">{b['phone1']}</a>
        <a href="tel:{b['phone2_href']}" style="font-size:1.5rem;font-weight:200">{b['phone2']}</a>
      </div>
    </div>
    <form data-form data-rv="up" style="--d:180ms" novalidate>
      <div class="f-row two">
        <div class="field"><label for="n1">Ваше имя</label>
          <input id="n1" name="name" type="text" required autocomplete="name" placeholder="Иван">
          <span class="err">Укажите имя</span></div>
        <div class="field"><label for="t1">Телефон</label>
          <input id="t1" name="phone" type="tel" required autocomplete="tel" placeholder="+7 (___) ___-__-__" inputmode="tel">
          <span class="err">Введите номер полностью</span></div>
      </div>
      <div class="field"><label for="m1">Комментарий</label>
        <textarea id="m1" name="msg" rows="3" placeholder="Интересует MODUL HOUSE 3, участок в Бердске"></textarea></div>
      <button class="btn btn--fill" type="submit" data-magnet=".2" style="justify-self:start">Отправить заявку {arrow()}</button>
      <p class="form-note">Нажимая кнопку, вы соглашаетесь с обработкой персональных данных.</p>
      <div class="form-ok" role="status">Спасибо! Заявка принята — мы перезвоним в рабочее время.</div>
    </form>
  </div>
</section>""")

    # Подвал
    out.append(f"""
<footer class="foot" id="contacts">
  <div class="wrap">
    <div class="foot__grid">
      <div data-rv="up">
        <a class="logo" href="#top">ДОММ<span>модульные дома</span></a>
        <p class="lead" style="margin-top:18px;font-size:15px">Производство и продажа модульных домов
        под ключ в Новосибирске и по России.</p>
      </div>
      <div data-rv="up" style="--d:80ms"><h4>Телефоны</h4>
        <p><a href="tel:{b['phone1_href']}">{b['phone1']}</a></p>
        <p><a href="tel:{b['phone2_href']}">{b['phone2']}</a></p>
        <p><a href="mailto:{b['email']}">{b['email']}</a></p></div>
      <div data-rv="up" style="--d:160ms"><h4>Адреса</h4>
        <p>Офис — г. {b['city']}</p><p>Производство — г. {b['city']}</p>
        <p>{b['hours']}</p><p>{b['hours2']}</p></div>
      <div data-rv="up" style="--d:240ms"><h4>Соцсети</h4>
        <p><a href="{b['vk']}" target="_blank" rel="noopener">ВКонтакте</a></p>
        <p>Instagram: {b['inst']}</p>
        <p><a href="{b['wa']}" target="_blank" rel="noopener">WhatsApp</a></p></div>
    </div>
    <div class="foot__big" aria-hidden="true">ДОММ</div>
    <div class="foot__bot"><span>© <span data-year></span> ДОММ. Модульные дома.</span>
      <span>Новосибирск</span></div>
  </div>
</footer>""")

    out.append(core.dock(b))

    extra = r"""
/* Процесс: подсветка активного шага */
(function(){
  var steps = document.querySelectorAll('.step');
  var imgs = document.querySelectorAll('.proc__media img');
  if(!steps.length) return;
  var so = new IntersectionObserver(function(es){
    es.forEach(function(e){
      if(!e.isIntersecting) return;
      var i = +e.target.dataset.step;
      steps.forEach(function(s,k){ s.classList.toggle('on', k===i); });
      imgs.forEach(function(im,k){ im.classList.toggle('on', k===i); });
    });
  },{rootMargin:'-45% 0px -45% 0px'});
  steps.forEach(function(s){ so.observe(s); });
})();
/* Превью объекта у курсора */
(function(){
  var peek = document.querySelector('.obj__peek');
  if(!peek || !window.matchMedia('(hover:hover)').matches) return;
  var im = peek.querySelector('img');
  document.querySelectorAll('[data-peek]').forEach(function(row){
    row.addEventListener('pointerenter', function(){ im.src = row.dataset.peek; peek.classList.add('on'); });
    row.addEventListener('pointerleave', function(){ peek.classList.remove('on'); });
    row.addEventListener('pointermove', function(e){
      peek.style.left = e.clientX + 'px';
      peek.style.top = Math.max(120, Math.min(window.innerHeight-120, e.clientY)) + 'px';
    });
  });
})();
"""
    out.append(core.tail(extra))
    return "".join(out)
