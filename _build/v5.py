# -*- coding: utf-8 -*-
"""Вариант 5 — GLASS AURORA. Стекло, живые градиенты, 3D-наклон, свечение."""
import core
from data import *

FONTS = '<link href="https://fonts.googleapis.com/css2?family=Sora:wght@200;300;400;500;600;700&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">'

CSS = r"""
:root{
  --bg:#070A0E; --bg-2:#0C1117; --fg:#EAF0F5; --muted:#8896A5;
  --line:rgba(234,240,245,.12); --glass:rgba(255,255,255,.05);
  --accent:#5EE7C4; --accent-2:#7C8CFF; --accent-3:#FFB35C; --on-accent:#06110D;
  --input-bg:rgba(255,255,255,.04);
  --font-head:'Sora',system-ui,sans-serif; --font-body:'Inter',system-ui,sans-serif;
  --radius:22px; --radius-sm:14px; --head-weight:400;
}
::selection{background:var(--accent);color:var(--on-accent)}
body{position:relative}
.aurora{position:fixed;inset:0;z-index:-2;overflow:hidden;pointer-events:none}
.aurora i{position:absolute;display:block;border-radius:50%;filter:blur(90px);opacity:.5}
.aurora i:nth-child(1){width:52vw;aspect-ratio:1;background:radial-gradient(circle,#0E6B57,transparent 66%);
  left:-12vw;top:-8vw;animation:a1 26s ease-in-out infinite alternate}
.aurora i:nth-child(2){width:46vw;aspect-ratio:1;background:radial-gradient(circle,#2B3B96,transparent 66%);
  right:-10vw;top:24vh;animation:a2 32s ease-in-out infinite alternate}
.aurora i:nth-child(3){width:40vw;aspect-ratio:1;background:radial-gradient(circle,#7A4A17,transparent 66%);
  left:22vw;bottom:-14vw;animation:a3 28s ease-in-out infinite alternate}
@keyframes a1{to{transform:translate3d(16vw,12vh,0) scale(1.25)}}
@keyframes a2{to{transform:translate3d(-14vw,-10vh,0) scale(1.18)}}
@keyframes a3{to{transform:translate3d(10vw,-16vh,0) scale(1.3)}}
@media (prefers-reduced-motion:reduce){.aurora i{animation:none}}
.noise{position:fixed;inset:0;z-index:-1;pointer-events:none;opacity:.3;
  background-image:radial-gradient(rgba(255,255,255,.045) 1px,transparent 1px);background-size:3px 3px}

.h1{font-family:var(--font-head);font-size:clamp(2.5rem,6.8vw,5.8rem);font-weight:300;line-height:1;letter-spacing:-.035em}
.h2{font-family:var(--font-head);font-size:clamp(1.9rem,4.3vw,3.5rem);font-weight:300;line-height:1.05;letter-spacing:-.03em}
.h3{font-family:var(--font-head);font-size:clamp(1.1rem,1.9vw,1.4rem);font-weight:500;letter-spacing:-.02em}
.grad{background:linear-gradient(100deg,var(--accent),var(--accent-2) 55%,var(--accent-3));
  -webkit-background-clip:text;background-clip:text;color:transparent}
.kicker{display:inline-flex;align-items:center;gap:9px;padding:8px 15px;border-radius:100px;
  background:var(--glass);border:1px solid var(--line);backdrop-filter:blur(12px);
  font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:var(--accent);max-width:100%;flex-wrap:wrap}
.kicker i{width:6px;height:6px;border-radius:50%;background:var(--accent);
  box-shadow:0 0 12px var(--accent);animation:blink 2.4s ease-in-out infinite}
@keyframes blink{0%,100%{opacity:1}50%{opacity:.35}}
.lead{color:var(--muted);font-size:clamp(1rem,1.25vw,1.1rem);max-width:60ch;line-height:1.68;font-weight:300}
.sec{padding:clamp(66px,8.5vw,130px) 0}
.sec-head{display:grid;gap:20px;margin-bottom:clamp(34px,4.5vw,60px)}
@media(min-width:900px){.sec-head.split{grid-template-columns:1.1fr .9fr;align-items:end;gap:50px}}
.glass{background:var(--glass);border:1px solid var(--line);border-radius:var(--radius);
  backdrop-filter:blur(18px) saturate(140%);position:relative;overflow:hidden}
.glass::after{content:"";position:absolute;inset:0;pointer-events:none;border-radius:inherit;
  background:linear-gradient(140deg,rgba(255,255,255,.1),transparent 42%)}

/* Шапка */
.hdr{position:fixed;inset:14px 14px auto 14px;z-index:100;transition:.5s cubic-bezier(.16,1,.3,1)}
.hdr__in{display:flex;align-items:center;justify-content:space-between;gap:18px;padding:11px 12px 11px 22px;
  border-radius:100px;border:1px solid transparent;transition:.5s cubic-bezier(.16,1,.3,1)}
.hdr.stuck .hdr__in{background:rgba(12,17,23,.62);backdrop-filter:blur(22px) saturate(160%);
  border-color:var(--line);box-shadow:0 12px 44px rgba(0,0,0,.34)}
.hdr.hide{transform:translateY(-150%)}
.logo{font-family:var(--font-head);font-weight:600;font-size:19px;letter-spacing:.02em;display:flex;align-items:center;gap:10px}
.logo i{width:22px;height:22px;border-radius:7px;display:block;
  background:linear-gradient(140deg,var(--accent),var(--accent-2));box-shadow:0 0 18px rgba(94,231,196,.4)}
.nav{display:none;gap:4px}
@media(min-width:1024px){.nav{display:flex}}
.nav a{font-size:13px;color:var(--muted);padding:9px 14px;border-radius:100px;transition:.3s}
.nav a:hover{color:var(--fg);background:rgba(255,255,255,.07)}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:9px;padding:14px 24px;border-radius:100px;
  font-size:13px;font-weight:500;position:relative;overflow:hidden;isolation:isolate;
  transform:translate3d(var(--tx,0),var(--ty,0),0);
  transition:transform .4s cubic-bezier(.16,1,.3,1),box-shadow .4s,color .3s,border-color .3s}
.btn--fill{background:linear-gradient(100deg,var(--accent),var(--accent-2));color:var(--on-accent);font-weight:600;
  box-shadow:0 8px 30px rgba(94,231,196,.22)}
.btn--fill:hover{box-shadow:0 14px 46px rgba(94,231,196,.38)}
.btn--fill::before{content:"";position:absolute;inset:0;z-index:-1;
  background:linear-gradient(100deg,var(--accent-2),var(--accent-3));opacity:0;transition:opacity .45s}
.btn--fill:hover::before{opacity:1}
.btn--glass{background:var(--glass);border:1px solid var(--line);backdrop-filter:blur(12px);color:var(--fg)}
.btn--glass:hover{border-color:var(--accent);color:var(--accent)}
.hdr__cta{display:none;padding:12px 20px}@media(min-width:640px){.hdr__cta{display:inline-flex}}
.burger{display:grid;gap:5px;padding:10px;margin:-4px}
@media(min-width:1024px){.burger{display:none}}
.burger i{width:20px;height:2px;background:var(--fg);border-radius:2px;transition:.4s}
body.nav-open .burger i:nth-child(1){transform:translateY(7px) rotate(45deg)}
body.nav-open .burger i:nth-child(2){opacity:0}
body.nav-open .burger i:nth-child(3){transform:translateY(-7px) rotate(-45deg)}
.mnav{position:fixed;inset:0;z-index:99;background:rgba(7,10,14,.9);backdrop-filter:blur(26px);
  display:grid;align-content:center;gap:4px;padding:0 var(--gutter);opacity:0;visibility:hidden;transition:.45s}
body.nav-open .mnav{opacity:1;visibility:visible}
.mnav a{font-family:var(--font-head);font-size:clamp(2rem,9vw,3.2rem);font-weight:300;letter-spacing:-.03em;
  opacity:0;transform:translateY(18px);transition:.55s cubic-bezier(.16,1,.3,1)}
body.nav-open .mnav a{opacity:1;transform:none}
.mnav a:nth-child(1){transition-delay:.05s}.mnav a:nth-child(2){transition-delay:.1s}
.mnav a:nth-child(3){transition-delay:.15s}.mnav a:nth-child(4){transition-delay:.2s}
.mnav a:nth-child(5){transition-delay:.25s}
.mnav__foot{margin-top:26px;display:grid;gap:6px;color:var(--muted)}

/* Герой */
.hero{padding:132px 0 0;position:relative}
.hero__in{display:grid;gap:36px;align-items:center}
@media(min-width:1000px){.hero__in{grid-template-columns:1.05fr .95fr;gap:56px}}
.hero__acts{display:flex;gap:12px;flex-wrap:wrap;margin-top:28px}
.hero__vis{position:relative;border-radius:var(--radius);overflow:hidden;aspect-ratio:4/3;
  transform:perspective(1200px) rotateX(var(--rx,0)) rotateY(var(--ry,0));
  transition:transform .6s cubic-bezier(.16,1,.3,1);box-shadow:0 40px 100px rgba(0,0,0,.5)}
.hero__vis img{width:100%;height:100%;object-fit:cover;animation:ken 26s ease-in-out infinite alternate}
@keyframes ken{from{transform:scale(1.04)}to{transform:scale(1.16)}}
.hero__chip{position:absolute;padding:14px 18px;border-radius:16px;background:rgba(12,17,23,.62);
  border:1px solid var(--line);backdrop-filter:blur(16px);font-size:13px;
  animation:bob 6s ease-in-out infinite}
.hero__chip b{display:block;font-family:var(--font-head);font-size:1.35rem;font-weight:500;letter-spacing:-.03em}
.hero__chip.c1{left:16px;bottom:16px}
.hero__chip.c2{right:16px;top:16px;animation-delay:-3s}
@keyframes bob{0%,100%{transform:translateY(0)}50%{transform:translateY(-9px)}}
@media (prefers-reduced-motion:reduce){.hero__chip,.hero__vis img{animation:none}}

/* Цифры */
.nums{display:grid;grid-template-columns:repeat(2,1fr);gap:12px;margin-top:clamp(40px,5vw,70px)}
@media(min-width:900px){.nums{grid-template-columns:repeat(4,1fr);gap:16px}}
.num{padding:26px 22px;transition:transform .5s cubic-bezier(.16,1,.3,1),border-color .4s}
.num:hover{transform:translateY(-5px);border-color:rgba(94,231,196,.4)}
.num b{display:block;font-family:var(--font-head);font-size:clamp(2rem,3.4vw,2.9rem);font-weight:300;
  letter-spacing:-.04em;position:relative;z-index:1}
.num span{color:var(--muted);font-size:13px;position:relative;z-index:1}

/* Галерея */
.gal{display:flex;gap:14px;overflow-x:auto;scroll-snap-type:x mandatory;padding:0 var(--gutter) 16px;
  cursor:grab;scrollbar-width:none}
.gal::-webkit-scrollbar{display:none}
.gal.dragging{cursor:grabbing;scroll-snap-type:none}
.gal figure{margin:0;flex:0 0 clamp(240px,32vw,380px);scroll-snap-align:center;border-radius:var(--radius);
  overflow:hidden;aspect-ratio:3/4;position:relative;border:1px solid var(--line)}
.gal img{width:100%;height:100%;object-fit:cover;transition:transform 1.2s cubic-bezier(.16,1,.3,1);filter:brightness(.9)}
.gal figure:hover img{transform:scale(1.07);filter:brightness(1)}

/* Карточки */
.cards{display:grid;gap:18px}
@media(min-width:700px){.cards{grid-template-columns:repeat(2,1fr)}}
@media(min-width:1100px){.cards{grid-template-columns:repeat(3,1fr)}}
.card{border-radius:var(--radius);overflow:hidden;transform-style:preserve-3d;
  transform:perspective(1000px) rotateX(var(--rx,0)) rotateY(var(--ry,0));
  transition:transform .5s cubic-bezier(.16,1,.3,1),box-shadow .5s,border-color .45s}
.card:hover{box-shadow:0 30px 70px rgba(0,0,0,.44);border-color:rgba(94,231,196,.36)}
.card__img{aspect-ratio:4/3;overflow:hidden;position:relative}
.card__img img{width:100%;height:100%;object-fit:cover;transition:transform 1.2s cubic-bezier(.16,1,.3,1);filter:brightness(.9)}
.card:hover .card__img img{transform:scale(1.07);filter:brightness(1)}
.chip{position:absolute;top:14px;left:14px;padding:7px 13px;border-radius:100px;font-size:11.5px;
  background:rgba(7,10,14,.6);backdrop-filter:blur(10px);border:1px solid var(--line);z-index:2}
.card__b{padding:24px 22px;display:grid;gap:9px;position:relative;z-index:1}
.card__b p{color:var(--muted);font-size:14px;font-weight:300;min-height:42px}
.card__p{display:flex;justify-content:space-between;align-items:baseline;padding-top:15px;
  border-top:1px solid var(--line);margin-top:6px}
.card__p b{font-family:var(--font-head);font-size:1.35rem;font-weight:400;letter-spacing:-.03em}
.card__p span{font-size:12px;color:var(--muted)}

/* Планировки */
.tabs{display:inline-flex;gap:5px;padding:5px;border-radius:100px;margin-bottom:28px;flex-wrap:wrap}
.tabs button{padding:11px 20px;border-radius:100px;font-size:13px;font-weight:500;color:var(--muted);transition:.35s}
.tabs button.active{background:linear-gradient(100deg,var(--accent),var(--accent-2));color:var(--on-accent);font-weight:600}
.plans{display:grid;gap:14px;grid-template-columns:repeat(2,1fr)}
@media(min-width:900px){.plans{grid-template-columns:repeat(4,1fr)}}
.plan{border-radius:var(--radius-sm);overflow:hidden;cursor:zoom-in;
  transition:transform .5s cubic-bezier(.16,1,.3,1),border-color .4s}
.plan:hover{transform:translateY(-6px);border-color:rgba(94,231,196,.4)}
.plan__i{aspect-ratio:1/1;background:#fff;padding:10px;position:relative;z-index:1}
.plan__i img{width:100%;height:100%;object-fit:contain}
.plan__b{padding:15px;display:grid;gap:5px;position:relative;z-index:1}
.plan__b h4{font-family:var(--font-head);font-size:13.5px;font-weight:500}
.plan__b .m{font-size:12px;color:var(--muted)}
.plan__b .p{font-family:var(--font-head);font-size:15px;font-weight:500}

/* Комплектация */
.spec{display:grid;gap:16px}
@media(min-width:1000px){.spec{grid-template-columns:1.4fr .8fr .8fr}}
.spec__c{padding:30px 26px;transition:transform .5s cubic-bezier(.16,1,.3,1),border-color .4s}
.spec__c:hover{transform:translateY(-5px);border-color:rgba(94,231,196,.32)}
.spec__c h3{margin-bottom:20px;position:relative;z-index:1}
.spec__c ul{position:relative;z-index:1}
.spec__c li{display:flex;gap:11px;padding:9px 0;font-size:14.5px;font-weight:300;color:var(--muted);
  border-bottom:1px solid rgba(234,240,245,.06);line-height:1.55}
.spec__c li:last-child{border:0}
.spec__c svg{flex:0 0 15px;margin-top:4px;color:var(--accent)}
.spec--in li{color:var(--fg)}
.spec--out svg{color:var(--muted)}

/* Процесс — вертикальная линия */
.tl{position:relative;padding-left:0}
@media(min-width:900px){.tl{padding-left:52px}
  .tl::before{content:"";position:absolute;left:16px;top:8px;bottom:8px;width:2px;
    background:linear-gradient(var(--accent),var(--accent-2),var(--accent-3));opacity:.28}}
.tstep{display:grid;gap:22px;padding:clamp(24px,3.5vw,44px) 0;position:relative}
@media(min-width:900px){.tstep{grid-template-columns:1fr 1fr;gap:44px;align-items:center}
  .tstep::before{content:"";position:absolute;left:-44px;top:50%;width:14px;height:14px;border-radius:50%;
    background:var(--accent);box-shadow:0 0 0 5px rgba(94,231,196,.15);transform:translate(0,-50%) scale(0);
    transition:transform .6s cubic-bezier(.16,1,.3,1)}
  .tstep.in::before{transform:translate(0,-50%) scale(1)}
  .tstep:nth-child(even) .tstep__i{order:-1}}
.tstep__n{font-family:var(--font-head);font-size:12px;letter-spacing:.18em;color:var(--accent);
  text-transform:uppercase;display:block;margin-bottom:12px}
.tstep h3{margin-bottom:12px}
.tstep p{color:var(--muted);font-size:15px;font-weight:300;line-height:1.7}
.tstep__i{border-radius:var(--radius);overflow:hidden;aspect-ratio:4/3;border:1px solid var(--line)}
.tstep__i img{width:100%;height:100%;object-fit:cover;transform:scale(1.1) translate3d(0,var(--par,0),0)}

/* Мозаика */
.mos{display:grid;gap:14px;grid-template-columns:repeat(2,1fr)}
@media(min-width:900px){.mos{grid-template-columns:repeat(4,1fr)}
  .mos figure:nth-child(1){grid-column:span 2;grid-row:span 2}
  .mos figure:nth-child(7){grid-column:span 2}}
.mos figure{margin:0;border-radius:var(--radius);overflow:hidden;position:relative;aspect-ratio:1/1;
  cursor:zoom-in;border:1px solid var(--line)}
@media(min-width:900px){.mos figure:nth-child(1){aspect-ratio:auto}.mos figure:nth-child(7){aspect-ratio:2/1}}
.mos img{width:100%;height:100%;object-fit:cover;transition:transform 1.2s cubic-bezier(.16,1,.3,1);filter:brightness(.85)}
.mos figure:hover img{transform:scale(1.06);filter:brightness(1)}
.mos figcaption{position:absolute;inset:auto 0 0 0;padding:52px 16px 16px;font-size:12.5px;font-weight:300;
  background:linear-gradient(transparent,rgba(7,10,14,.92));opacity:0;transform:translateY(8px);transition:.45s}
.mos figure:hover figcaption{opacity:1;transform:none}

/* Объекты */
.objs{display:grid;gap:16px}
@media(min-width:800px){.objs{grid-template-columns:repeat(2,1fr)}
  .objs>*:first-child{grid-column:span 2}}
.obj{position:relative;border-radius:var(--radius);overflow:hidden;display:block;aspect-ratio:16/10;
  border:1px solid var(--line)}
.objs>*:first-child .obj{aspect-ratio:21/9}
.obj img{width:100%;height:100%;object-fit:cover;transition:transform 1.3s cubic-bezier(.16,1,.3,1);filter:brightness(.82)}
.obj:hover img{transform:scale(1.05);filter:brightness(.95)}
.obj__c{display:block;position:absolute;inset:auto 0 0 0;padding:70px 24px 24px;
  background:linear-gradient(transparent,rgba(7,10,14,.92))}
.obj__c h3{font-family:var(--font-head);font-size:clamp(1.2rem,2.2vw,1.8rem);font-weight:400;letter-spacing:-.03em}
.obj__c p{font-size:14px;color:var(--muted);margin-top:5px;font-weight:300}

/* До/после */
.ba-wrap{display:grid;gap:34px;align-items:center}
@media(min-width:1000px){.ba-wrap{grid-template-columns:.8fr 1.2fr;gap:56px}}

/* Заявка */
.cta{padding:clamp(30px,5vw,64px);border-radius:clamp(22px,3vw,34px)}
.cta__in{display:grid;gap:36px;position:relative;z-index:1}
@media(min-width:960px){.cta__in{grid-template-columns:1fr 1fr;gap:60px;align-items:center}}
.cta form{display:grid;gap:14px}

/* Подвал */
.foot{padding:66px 0 32px}
.foot__grid{display:grid;gap:32px}
@media(min-width:800px){.foot__grid{grid-template-columns:1.5fr 1fr 1fr 1fr}}
.foot h4{font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:var(--muted);margin-bottom:15px}
.foot p{font-size:15px;margin-bottom:9px;font-weight:300}
.foot a:hover{color:var(--accent)}
.foot__bot{margin-top:46px;padding-top:20px;border-top:1px solid var(--line);display:flex;flex-wrap:wrap;
  gap:12px;justify-content:space-between;font-size:12px;color:var(--muted)}
"""

CHECK = '<svg width="15" height="15" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" aria-hidden="true"><path d="M2.5 8.5l3.5 3.5 7.5-8"/></svg>'
MINUS = '<svg width="15" height="15" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" aria-hidden="true"><path d="M3 8h10"/></svg>'
PLUSI = '<svg width="15" height="15" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" aria-hidden="true"><path d="M8 3v10M3 8h10"/></svg>'
ARR = '<svg width="16" height="10" viewBox="0 0 18 10" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" aria-hidden="true"><path d="M0 5h16M12 1l4 4-4 4"/></svg>'

def build():
    b = BRAND
    nav = "".join(f'<a href="{h}">{t}</a>' for h, t in NAV)
    o = [core.head("ДОММ — модульные дома для жизни и отдыха | Новосибирск",
                   "Модульные дома с террасой под ключ от 990 000 ₽ за 30 дней. Собственное производство в Новосибирске, 80+ проектов.",
                   FONTS, CSS, "#070A0E")]
    o.append('<div class="aurora"><i></i><i></i><i></i></div><div class="noise"></div><div class="cursor"></div>')
    o.append(f"""
<header class="hdr" data-header><div class="wrap"><div class="hdr__in">
  <a class="logo" href="#top"><i></i>ДОММ</a>
  <nav class="nav">{nav}</nav>
  <div style="display:flex;gap:10px;align-items:center">
    <a class="btn btn--fill hdr__cta" href="tel:{b['phone2_href']}" data-magnet=".25">Заказать расчёт</a>
    <button class="burger" data-burger aria-label="Меню" aria-expanded="false"><i></i><i></i><i></i></button>
  </div>
</div></div></header>
<nav class="mnav" data-menu>{nav}
  <div class="mnav__foot"><a href="tel:{b['phone1_href']}">{b['phone1']}</a>
  <a href="tel:{b['phone2_href']}">{b['phone2']}</a><a href="mailto:{b['email']}">{b['email']}</a></div>
</nav>""")

    nums = "".join(f'<div class="num glass" data-rv="up"><b>{v}</b><span>{t}</span></div>' for v, t in STATS)
    o.append(f"""
<section class="hero" id="top"><div class="wrap">
  <div class="hero__in">
    <div data-rv="up">
      <span class="kicker"><i></i>{HERO['kicker']}</span>
      <h1 class="h1" style="margin:20px 0 20px" data-split="line">Модульные дома<br><span class="grad">для жизни</span><br>и отдыха</h1>
      <p class="lead">{HERO['sub']} {HERO['sub2']}</p>
      <div class="hero__acts">
        <a class="btn btn--fill" href="#projects" data-magnet=".3">Смотреть проекты {ARR}</a>
        <a class="btn btn--glass" href="{b['wa']}" target="_blank" rel="noopener" data-magnet=".25">WhatsApp</a>
      </div>
    </div>
    <div class="hero__vis" data-tilt="7" data-rv="zoom">
      <img src="{HERO['bg']}" alt="Модульный дом ДОММ с террасой">
      <div class="hero__chip c1"><b>от 990 000 ₽</b><span style="color:var(--muted)">дом под ключ</span></div>
      <div class="hero__chip c2"><b>30 дней</b><span style="color:var(--muted)">производство</span></div>
    </div>
  </div>
  <div class="nums" data-stagger="80">{nums}</div>
</div></section>""")

    figs = "".join(f'<figure data-lb="g" data-full="{u}" data-cap="Дом ДОММ"><img src="{u}" alt="Модульный дом ДОММ" loading="lazy"></figure>'
                   for u in GALLERY)
    o.append(f"""
<section class="sec" id="gallery">
  <div class="wrap sec-head split">
    <div data-rv="up"><span class="kicker"><i></i>Галерея</span>
      <h2 class="h2" style="margin-top:18px" data-split="line">Декорируем дома<br>в <span class="grad">уютном</span> стиле</h2></div>
    <p class="lead" data-rv="up" style="--d:150ms">Тёплое дерево, мягкий свет, панорамные окна.
    Потяните ленту вбок или нажмите на снимок.</p>
  </div>
  <div class="gal" data-drag>{figs}</div>
</section>""")

    cards = "".join(f"""
    <article class="card glass" data-tilt="7" data-rv="up">
      <div class="card__img"><span class="chip">{area}</span><img src="{im}" alt="{n}" loading="lazy"></div>
      <div class="card__b"><h3 class="h3">{n}</h3><p>{d}</p>
        <div class="card__p"><b class="grad">от {p} ₽</b><span>под ключ</span></div>
        <a class="btn btn--glass" href="#cta" style="margin-top:12px;justify-self:start">Подробнее {ARR}</a></div>
    </article>""" for n, d, p, area, im in PROJECTS)
    o.append(f"""
<section class="sec" id="projects"><div class="wrap">
  <div class="sec-head split">
    <div data-rv="up"><span class="kicker"><i></i>Каталог</span>
      <h2 class="h2" style="margin-top:18px" data-split="line">Проекты домов<br>и <span class="grad">бань</span></h2></div>
    <p class="lead" data-rv="up" style="--d:150ms">Семь базовых моделей и две бани — любую адаптируем
    под участок и сценарий жизни.</p>
  </div>
  <div class="cards" data-stagger="90">{cards}</div>
</div></section>""")

    def pg(items, key):
        return "".join(f"""
      <article class="plan glass" data-lb="{key}" data-full="{im}" data-cap="{n} — {a}, от {p} тыс. ₽">
        <div class="plan__i"><img src="{im}" alt="Планировка {n}" loading="lazy"></div>
        <div class="plan__b"><h4>{n}</h4><span class="m">{a}{' · ' + note if note else ''}</span>
          <span class="p grad">от {p} тыс. ₽</span></div></article>""" for n, a, p, im, note in items)
    rend = "".join(f"""
      <article class="card glass" data-lb="rn" data-full="{im}" data-cap="{n}" style="cursor:zoom-in" data-tilt="7">
        <div class="card__img"><img src="{im}" alt="{n}" loading="lazy"></div>
        <div class="card__b"><h3 class="h3">{n}</h3><p>{d}</p></div></article>""" for n, d, im in RENDERS)
    o.append(f"""
<section class="sec" id="prices"><div class="wrap" data-tabs>
  <div class="sec-head split">
    <div data-rv="up"><span class="kicker"><i></i>Планировки и цены</span>
      <h2 class="h2" style="margin-top:18px" data-split="line">Выберите свой <span class="grad">метраж</span></h2></div>
    <p class="lead" data-rv="up" style="--d:150ms">Дома собираются из модулей 2,5×6 м и 3×6 м.
    Нажмите на планировку, чтобы открыть её крупно.</p>
  </div>
  <div class="tabs glass" role="tablist">
    <button data-tab="a" class="active" role="tab" aria-selected="true">Модули 2,5 × 6</button>
    <button data-tab="b" role="tab" aria-selected="false">Модули 3 × 6</button>
    <button data-tab="c" role="tab" aria-selected="false">Визуализации</button>
  </div>
  <div class="plans" data-panel="a" data-stagger="50">{pg(PLANS_25,'p25')}</div>
  <div class="plans" data-panel="b" hidden data-stagger="50">{pg(PLANS_36,'p36')}</div>
  <div class="cards" data-panel="c" hidden data-stagger="70">{rend}</div>
</div></section>""")

    def li(items, ic):
        return "".join(f'<li>{ic}<span>{t}</span></li>' for t in items)
    o.append(f"""
<section class="sec" id="spec"><div class="wrap">
  <div class="sec-head split">
    <div data-rv="up"><span class="kicker"><i></i>Комплектация</span>
      <h2 class="h2" style="margin-top:18px" data-split="line">Что входит<br>в <span class="grad">базовую</span> стоимость</h2></div>
    <p class="lead" data-rv="up" style="--d:150ms">Честный список без звёздочек: что вы получаете сразу,
    что оплачивается отдельно и что можно добавить.</p>
  </div>
  <div class="spec" data-stagger="110">
    <div class="spec__c glass spec--in"><h3 class="h3">Входит в стоимость</h3><ul>{li(INCLUDED, CHECK)}</ul></div>
    <div class="spec__c glass spec--out"><h3 class="h3">Не входит</h3><ul>{li(EXCLUDED, MINUS)}</ul></div>
    <div class="spec__c glass"><h3 class="h3">Дополнительные опции</h3><ul>{li(OPTIONS, PLUSI)}</ul></div>
  </div>
</div></section>""")

    steps = "".join(f"""
    <article class="tstep" data-rv="up">
      <div><span class="tstep__n">Этап {n}</span><h3 class="h2" style="font-size:clamp(1.4rem,2.6vw,2.1rem)">{t}</h3><p>{d}</p></div>
      <div class="tstep__i"><img src="{im}" alt="{t}" loading="lazy" data-par="30"></div>
    </article>""" for n, t, d, im in PROCESS)
    o.append(f"""
<section class="sec" id="process"><div class="wrap">
  <div class="sec-head" data-rv="up"><span class="kicker"><i></i>Как мы работаем</span>
    <h2 class="h2" style="margin-top:18px">Четыре шага до <span class="grad">новоселья</span></h2></div>
  <div class="tl">{steps}</div>
</div></section>""")

    mos = "".join(f'<figure data-lb="d" data-full="{im}" data-cap="{t}"><img src="{im}" alt="{t}" loading="lazy"><figcaption>{t}</figcaption></figure>'
                  for t, im in DETAILS + INTERIOR)
    o.append(f"""
<section class="sec" id="details"><div class="wrap">
  <div class="sec-head split">
    <div data-rv="up"><span class="kicker"><i></i>Black Paket</span>
      <h2 class="h2" style="margin-top:18px" data-split="line">Детали в едином<br><span class="grad">чёрном</span> стиле</h2></div>
    <p class="lead" data-rv="up" style="--d:150ms">Электрощит, розетки, выключатели, светильники и ручки —
    одно оформление без визуального шума.</p>
  </div>
  <div class="mos" data-stagger="70">{mos}</div>
</div></section>""")

    objs = "".join(f"""
    <div><a class="obj" href="#cta"><img src="{im}" alt="{t}" loading="lazy">
      <span class="obj__c"><h3>{t}</h3><p>{d}</p></span></a></div>""" for t, d, im in OBJECTS)
    o.append(f"""
<section class="sec" id="objects"><div class="wrap">
  <div class="sec-head" data-rv="up"><span class="kicker"><i></i>Наши дома</span>
    <h2 class="h2" style="margin-top:18px">Реализованные <span class="grad">объекты</span></h2></div>
  <div class="objs" data-stagger="90">{objs}</div>
</div></section>""")

    o.append(f"""
<section class="sec"><div class="wrap ba-wrap">
  <div data-rv="up"><span class="kicker"><i></i>Посмотрите разницу</span>
    <h2 class="h2" style="margin:18px 0 16px" data-split="line">Ваш дом у нас —<br>и ваш дом <span class="grad">у вас</span></h2>
    <p class="lead">Слева — модуль на производстве, справа — тот же дом на участке. Потяните ползунок.</p></div>
  <div class="ba" data-rv="zoom" role="img" aria-label="Сравнение: дом на производстве и на участке">
    <img src="{BEFORE}" alt="Модуль на производстве" loading="lazy">
    <img class="ba__after" src="{AFTER}" alt="Готовый дом на участке" loading="lazy">
    <span class="ba__line"></span><span class="ba__grip">&#8596;</span>
    <span class="ba__tag l">Ваш дом у нас</span><span class="ba__tag r">Ваш дом у вас</span>
  </div>
</div></section>""")

    o.append(f"""
<section class="sec" id="cta"><div class="wrap"><div class="cta glass" data-rv="up"><div class="cta__in">
  <div>
    <span class="kicker"><i></i>Свяжитесь с нами</span>
    <h2 class="h2" style="margin:18px 0 16px">Оставьте заявку и получите <span class="grad">расчёт</span></h2>
    <p class="lead">Подберём планировку под участок и посчитаем стоимость с доставкой и монтажом.</p>
    <div style="margin-top:26px;display:grid;gap:8px;font-family:var(--font-head);font-size:1.5rem;font-weight:300;letter-spacing:-.03em">
      <a href="tel:{b['phone1_href']}">{b['phone1']}</a><a href="tel:{b['phone2_href']}">{b['phone2']}</a>
    </div>
  </div>
  <form data-form novalidate>
    <div class="f-row two">
      <div class="field"><label for="n5">Ваше имя</label>
        <input id="n5" type="text" required autocomplete="name" placeholder="Иван"><span class="err">Укажите имя</span></div>
      <div class="field"><label for="t5">Телефон</label>
        <input id="t5" type="tel" required autocomplete="tel" inputmode="tel" placeholder="+7 (___) ___-__-__">
        <span class="err">Введите номер полностью</span></div>
    </div>
    <div class="field"><label for="m5">Комментарий</label>
      <textarea id="m5" rows="3" placeholder="Интересует MODUL HOUSE 3, участок в Бердске"></textarea></div>
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
    o.append(core.tail())
    return "".join(o)
