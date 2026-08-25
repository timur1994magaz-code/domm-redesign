# -*- coding: utf-8 -*-
"""Вариант 8 — ПАСТЕЛЬ. Мягкий светлый минимализм, шалфейный акцент,
калькулятор с реальным графиком платежей по договору (30 / 40 / 15 / 15)."""
import core
from data import *

FONTS = ('<link href="https://fonts.googleapis.com/css2?'
         'family=Fraunces:opsz,wght@9..144,300;9..144,400;9..144,500;9..144,600&'
         'family=DM+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">')

CSS = r"""
:root{
  --bg:#FBFAF7; --bg-2:#FFFFFF; --bg-3:#EFF3EE; --fg:#1A211C; --muted:#6B756D;
  --line:rgba(26,33,28,.11); --hair:rgba(26,33,28,.06);
  --accent:#4F7059; --accent-soft:#E4EDE5; --on-accent:#FFFFFF; --input-bg:#FFFFFF;
  --font-head:'Fraunces',Georgia,serif; --font-body:'DM Sans',system-ui,sans-serif;
  --radius:26px; --radius-sm:16px; --head-weight:400;
  --shadow:0 2px 4px rgba(26,33,28,.03),0 12px 32px rgba(26,33,28,.06);
  --shadow-lg:0 4px 8px rgba(26,33,28,.04),0 30px 70px rgba(26,33,28,.11);
}
::selection{background:var(--accent);color:#fff}
/* мягкие пятна на фоне */
.mesh{position:fixed;inset:0;z-index:-1;pointer-events:none;overflow:hidden}
.mesh i{position:absolute;display:block;border-radius:50%;filter:blur(80px);opacity:.55}
.mesh i:nth-child(1){width:44vw;aspect-ratio:1;left:-10vw;top:-6vw;
  background:radial-gradient(circle,#CFE0D2,transparent 68%);animation:m1 28s ease-in-out infinite alternate}
.mesh i:nth-child(2){width:38vw;aspect-ratio:1;right:-8vw;top:38vh;
  background:radial-gradient(circle,#F0E4D6,transparent 68%);animation:m2 34s ease-in-out infinite alternate}
.mesh i:nth-child(3){width:34vw;aspect-ratio:1;left:26vw;bottom:-12vw;
  background:radial-gradient(circle,#DDE7EC,transparent 68%);animation:m3 30s ease-in-out infinite alternate}
@keyframes m1{to{transform:translate3d(12vw,10vh,0) scale(1.2)}}
@keyframes m2{to{transform:translate3d(-10vw,-8vh,0) scale(1.15)}}
@keyframes m3{to{transform:translate3d(8vw,-12vh,0) scale(1.25)}}
@media (prefers-reduced-motion:reduce){.mesh i{animation:none}}

.h1{font-family:var(--font-head);font-size:clamp(2.6rem,6.6vw,5.4rem);font-weight:400;
  line-height:1.02;letter-spacing:-.03em;font-variation-settings:'opsz' 120}
.h2{font-family:var(--font-head);font-size:clamp(2rem,4.2vw,3.4rem);font-weight:400;
  line-height:1.06;letter-spacing:-.025em;font-variation-settings:'opsz' 96}
.h3{font-size:clamp(1.05rem,1.7vw,1.3rem);font-weight:500;letter-spacing:-.015em}
.soft{color:var(--accent)}
.pill{display:inline-flex;align-items:center;gap:9px;padding:9px 17px;border-radius:100px;
  background:var(--accent-soft);color:var(--accent);font-size:12.5px;font-weight:500}
.pill i{width:6px;height:6px;border-radius:50%;background:var(--accent);display:block}
.lead{color:var(--muted);font-size:clamp(1rem,1.2vw,1.1rem);max-width:58ch;line-height:1.72;font-weight:300}
.sec{padding:clamp(64px,8vw,124px) 0;position:relative}
.sec-head{display:grid;gap:20px;margin-bottom:clamp(34px,4.5vw,58px)}
@media(min-width:900px){.sec-head.split{grid-template-columns:1.1fr .9fr;align-items:end;gap:50px}}

/* шапка */
.hdr{position:fixed;inset:12px 12px auto 12px;z-index:100;transition:.5s cubic-bezier(.16,1,.3,1)}
.hdr__in{display:flex;align-items:center;justify-content:space-between;gap:18px;
  padding:11px 12px 11px 22px;border-radius:100px;border:1px solid transparent;transition:.5s cubic-bezier(.16,1,.3,1)}
.hdr.stuck .hdr__in{background:rgba(255,255,255,.82);backdrop-filter:blur(18px);
  border-color:var(--line);box-shadow:var(--shadow)}
.hdr.hide{transform:translateY(-140%)}
.logo{font-family:var(--font-head);font-size:23px;font-weight:500;letter-spacing:-.02em;
  display:flex;align-items:center;gap:10px}
.logo i{width:11px;height:11px;border-radius:50%;background:var(--accent);display:block}
.nav{display:none;gap:4px}
@media(min-width:1024px){.nav{display:flex}}
.nav a{font-size:13.5px;color:var(--muted);padding:9px 15px;border-radius:100px;transition:.3s}
.nav a:hover{color:var(--fg);background:var(--accent-soft)}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:9px;padding:14px 26px;
  border-radius:100px;font-size:14px;font-weight:500;position:relative;overflow:hidden;isolation:isolate;
  transform:translate3d(var(--tx,0),var(--ty,0),0);
  transition:transform .4s cubic-bezier(.16,1,.3,1),box-shadow .4s,color .3s,background .3s}
.btn--fill{background:var(--accent);color:#fff;box-shadow:0 6px 20px rgba(79,112,89,.24)}
.btn--fill:hover{box-shadow:0 12px 34px rgba(79,112,89,.34)}
.btn--fill::before{content:"";position:absolute;inset:0;z-index:-1;background:var(--fg);
  transform:translateY(101%);transition:transform .5s cubic-bezier(.16,1,.3,1)}
.btn--fill:hover::before{transform:none}
.btn--soft{background:var(--bg-2);color:var(--fg);border:1px solid var(--line)}
.btn--soft:hover{border-color:var(--accent);color:var(--accent)}
.hdr__cta{display:none}@media(min-width:640px){.hdr__cta{display:inline-flex}}
.burger{display:grid;gap:5px;padding:10px;margin:-4px}
@media(min-width:1024px){.burger{display:none}}
.burger i{width:21px;height:2px;border-radius:2px;background:var(--fg);transition:.4s}
body.nav-open .burger i:nth-child(1){transform:translateY(7px) rotate(45deg)}
body.nav-open .burger i:nth-child(2){opacity:0}
body.nav-open .burger i:nth-child(3){transform:translateY(-7px) rotate(-45deg)}
.mnav{position:fixed;inset:0;z-index:99;background:var(--bg);display:grid;align-content:center;gap:6px;
  padding:0 var(--gutter);opacity:0;visibility:hidden;transition:.45s}
body.nav-open .mnav{opacity:1;visibility:visible}
.mnav a{font-family:var(--font-head);font-size:clamp(2.2rem,9vw,3.4rem);font-weight:400;
  opacity:0;transform:translateY(18px);transition:.55s cubic-bezier(.16,1,.3,1)}
body.nav-open .mnav a{opacity:1;transform:none}
.mnav a:nth-child(1){transition-delay:.05s}.mnav a:nth-child(2){transition-delay:.1s}
.mnav a:nth-child(3){transition-delay:.15s}.mnav a:nth-child(4){transition-delay:.2s}
.mnav a:nth-child(5){transition-delay:.25s}
.mnav__foot{margin-top:28px;display:grid;gap:6px;color:var(--muted);font-size:15px}

/* герой */
.hero{padding:124px 0 0}
.hero__in{display:grid;gap:38px;align-items:center}
@media(min-width:1000px){.hero__in{grid-template-columns:.95fr 1.05fr;gap:52px}}
.hero__acts{display:flex;gap:12px;flex-wrap:wrap;margin-top:28px}
.hero__vis{position:relative}
.hero__vis figure{margin:0;border-radius:var(--radius);overflow:hidden;aspect-ratio:4/3;box-shadow:var(--shadow-lg)}
.hero__vis img{width:100%;height:100%;object-fit:cover;transform:scale(1.06);
  animation:drift 26s ease-in-out infinite alternate}
@keyframes drift{to{transform:scale(1.16) translate3d(-1.5%,-1%,0)}}
@media (prefers-reduced-motion:reduce){.hero__vis img{animation:none}}
.sticker{position:absolute;left:-10px;bottom:-18px;background:var(--bg-2);border-radius:22px;
  padding:18px 22px;box-shadow:var(--shadow-lg);transform:rotate(-4deg);
  transition:transform .5s cubic-bezier(.16,1,.3,1)}
.sticker:hover{transform:rotate(0deg) scale(1.03)}
.sticker b{font-family:var(--font-head);display:block;font-size:1.7rem;font-weight:500;
  letter-spacing:-.03em;color:var(--accent)}
.sticker span{font-size:12.5px;color:var(--muted)}
@media(min-width:640px){.sticker{left:-26px;bottom:-26px}}

/* цифры */
.nums{display:grid;grid-template-columns:repeat(2,1fr);gap:14px;margin-top:clamp(44px,5vw,72px)}
@media(min-width:900px){.nums{grid-template-columns:repeat(4,1fr);gap:18px}}
.num{background:var(--bg-2);border-radius:var(--radius-sm);padding:26px 22px;box-shadow:var(--shadow);
  transition:transform .5s cubic-bezier(.16,1,.3,1),box-shadow .5s}
.num:hover{transform:translateY(-5px);box-shadow:var(--shadow-lg)}
.num b{font-family:var(--font-head);display:block;font-size:clamp(2rem,3.4vw,2.8rem);font-weight:500;
  letter-spacing:-.03em;font-variant-numeric:tabular-nums}
.num span{color:var(--muted);font-size:13.5px}

/* калькулятор платежей */
.calc{display:grid;gap:22px}
@media(min-width:1040px){.calc{grid-template-columns:1fr 1fr;gap:30px;align-items:start}}
.panel{background:var(--bg-2);border-radius:var(--radius);padding:clamp(24px,3vw,36px);box-shadow:var(--shadow)}
.grp{margin-bottom:24px}
.grp:last-child{margin-bottom:0}
.grp>span{display:block;font-size:12.5px;font-weight:500;color:var(--muted);margin-bottom:12px}
.chips{display:flex;flex-wrap:wrap;gap:8px}
.chip{padding:11px 16px;border-radius:100px;font-size:13.5px;color:var(--muted);
  background:var(--bg);border:1px solid var(--line);transition:.3s;text-align:left}
.chip:hover{border-color:var(--accent);color:var(--fg)}
.chip.on{background:var(--accent);color:#fff;border-color:var(--accent)}
.chip small{display:block;font-size:11.5px;opacity:.72;margin-top:2px}
.opt{display:flex;align-items:center;gap:12px;padding:12px 0;border-bottom:1px solid var(--hair);cursor:pointer}
.opt:last-child{border:0}
.opt input{position:absolute;opacity:0;pointer-events:none}
.opt .bx{flex:0 0 22px;width:22px;height:22px;border-radius:7px;border:1px solid var(--line);
  display:grid;place-items:center;transition:.3s;background:var(--bg)}
.opt .bx svg{opacity:0;transform:scale(.5);transition:.3s;color:#fff}
.opt input:checked + .bx{background:var(--accent);border-color:var(--accent)}
.opt input:checked + .bx svg{opacity:1;transform:none}
.opt input:focus-visible + .bx{outline:2px solid var(--accent);outline-offset:3px}
.opt span.t{flex:1;font-size:14.5px}
.opt b{font-size:13.5px;color:var(--muted);font-weight:500;white-space:nowrap;font-variant-numeric:tabular-nums}
/* итог и график платежей */
.sum{background:var(--accent);color:#fff;border-radius:var(--radius);padding:clamp(24px,3vw,36px);
  box-shadow:0 20px 50px rgba(79,112,89,.24);position:sticky;top:92px}
@media(max-width:1039px){.sum{position:static}}
.sum>span{font-size:12.5px;opacity:.78}
.sum__total{font-family:var(--font-head);font-size:clamp(2.4rem,5vw,3.4rem);font-weight:500;
  letter-spacing:-.03em;margin:6px 0 2px;font-variant-numeric:tabular-nums}
.sum__sub{font-size:13.5px;opacity:.78}
.pay{margin-top:26px;display:grid;gap:0}
.pay__row{display:grid;grid-template-columns:auto 1fr auto;gap:14px;align-items:center;
  padding:14px 0;border-top:1px solid rgba(255,255,255,.2)}
.pay__pc{font-family:var(--font-head);font-size:1.15rem;font-weight:500;width:44px;
  font-variant-numeric:tabular-nums}
.pay__t{min-width:0}
.pay__t b{display:block;font-size:14px;font-weight:500}
.pay__t span{display:block;font-size:12px;opacity:.75;margin-top:2px}
.pay__v{font-size:15px;font-weight:500;white-space:nowrap;font-variant-numeric:tabular-nums}
.pay__bar{grid-column:1/-1;height:3px;border-radius:3px;background:rgba(255,255,255,.22);overflow:hidden;margin-top:10px}
.pay__bar i{display:block;height:100%;background:#fff;transform-origin:0 50%;transform:scaleX(0);
  transition:transform .8s cubic-bezier(.16,1,.3,1)}
.in .pay__bar i{transform:scaleX(1)}
.sum__note{font-size:12px;opacity:.8;line-height:1.6;margin-top:18px}
.sum .btn{margin-top:20px;width:100%;background:#fff;color:var(--accent);box-shadow:none}
.sum .btn::before{background:var(--fg)}
.sum .btn:hover{color:#fff}

/* карточки */
.cards{display:grid;gap:20px}
@media(min-width:700px){.cards{grid-template-columns:repeat(2,1fr)}}
@media(min-width:1100px){.cards{grid-template-columns:repeat(3,1fr)}}
.card{background:var(--bg-2);border-radius:var(--radius);overflow:hidden;box-shadow:var(--shadow);
  transition:transform .55s cubic-bezier(.16,1,.3,1),box-shadow .55s}
.card:hover{transform:translateY(-7px);box-shadow:var(--shadow-lg)}
.card__i{aspect-ratio:4/3;overflow:hidden;position:relative}
.card__i img{width:100%;height:100%;object-fit:cover;transition:transform 1.2s cubic-bezier(.16,1,.3,1)}
.card:hover .card__i img{transform:scale(1.06)}
.card__tag{position:absolute;top:14px;right:14px;background:rgba(255,255,255,.93);backdrop-filter:blur(8px);
  border-radius:100px;padding:7px 14px;font-size:12.5px;font-weight:500}
.card__b{padding:24px;display:grid;gap:9px}
.card__b p{color:var(--muted);font-size:14px;font-weight:300;min-height:42px}
.card__p{display:flex;justify-content:space-between;align-items:baseline;padding-top:15px;
  border-top:1px solid var(--hair);margin-top:5px}
.card__p b{font-family:var(--font-head);font-size:1.4rem;font-weight:500;letter-spacing:-.02em}
.card__p span{font-size:12.5px;color:var(--muted)}

/* галерея */
.gal{display:flex;gap:16px;overflow-x:auto;scroll-snap-type:x mandatory;padding:6px var(--gutter) 20px;
  cursor:grab;scrollbar-width:none}
.gal::-webkit-scrollbar{display:none}
.gal.dragging{cursor:grabbing;scroll-snap-type:none}
.gal figure{margin:0;flex:0 0 clamp(240px,32vw,380px);scroll-snap-align:center;aspect-ratio:3/4;
  overflow:hidden;border-radius:var(--radius);box-shadow:var(--shadow)}
.gal img{width:100%;height:100%;object-fit:cover;transition:transform 1.1s cubic-bezier(.16,1,.3,1)}
.gal figure:hover img{transform:scale(1.05)}

/* планировки */
.tabs{display:inline-flex;gap:6px;padding:6px;background:var(--bg-2);border-radius:100px;
  margin-bottom:30px;box-shadow:var(--shadow);flex-wrap:wrap}
.tabs button{padding:11px 21px;border-radius:100px;font-size:13.5px;font-weight:500;color:var(--muted);transition:.35s}
.tabs button.active{background:var(--accent);color:#fff}
.plans{display:grid;gap:16px;grid-template-columns:repeat(2,1fr)}
@media(min-width:900px){.plans{grid-template-columns:repeat(4,1fr)}}
.plan{background:var(--bg-2);border-radius:var(--radius-sm);overflow:hidden;cursor:zoom-in;
  box-shadow:var(--shadow);transition:transform .5s cubic-bezier(.16,1,.3,1),box-shadow .5s}
.plan:hover{transform:translateY(-6px);box-shadow:var(--shadow-lg)}
.plan__i{aspect-ratio:1/1;background:#fff;padding:12px}
.plan__i img{width:100%;height:100%;object-fit:contain}
.plan__b{padding:16px;display:grid;gap:5px;border-top:1px solid var(--hair)}
.plan__b h4{font-size:13.5px;font-weight:500}
.plan__b .m{font-size:12px;color:var(--muted)}
.plan__b .p{font-family:var(--font-head);font-size:15px;font-weight:500;color:var(--accent)}

/* комплектация */
.spec{display:grid;gap:18px}
@media(min-width:1000px){.spec{grid-template-columns:1.4fr .8fr .8fr}}
.spec__c{background:var(--bg-2);border-radius:var(--radius);padding:30px 26px;box-shadow:var(--shadow);
  transition:transform .5s cubic-bezier(.16,1,.3,1),box-shadow .5s}
.spec__c:hover{transform:translateY(-5px);box-shadow:var(--shadow-lg)}
.spec__c h3{font-family:var(--font-head);font-size:1.45rem;font-weight:500;margin-bottom:18px}
.spec__c li{display:flex;gap:11px;padding:9px 0;font-size:14.5px;font-weight:300;line-height:1.55;
  border-bottom:1px solid var(--hair);color:var(--muted)}
.spec__c li:last-child{border:0}
.spec__c i{flex:0 0 18px;width:18px;height:18px;border-radius:50%;background:var(--accent-soft);
  display:grid;place-items:center;margin-top:3px}
.spec__c i svg{width:10px;height:10px;color:var(--accent)}
.spec--in li{color:var(--fg)}
.spec--out i{background:var(--bg-3)}
.spec--out i svg{color:var(--muted)}

/* процесс */
.pr{display:grid;gap:18px}
@media(min-width:900px){.pr{grid-template-columns:repeat(2,1fr)}}
.pstep{background:var(--bg-2);border-radius:var(--radius);overflow:hidden;box-shadow:var(--shadow);
  display:flex;flex-direction:column;transition:transform .55s cubic-bezier(.16,1,.3,1),box-shadow .55s}
.pstep:hover{transform:translateY(-6px);box-shadow:var(--shadow-lg)}
.pstep__i{aspect-ratio:16/10;overflow:hidden}
.pstep__i img{width:100%;height:100%;object-fit:cover;transition:transform 1.2s cubic-bezier(.16,1,.3,1)}
.pstep:hover .pstep__i img{transform:scale(1.05)}
.pstep__b{padding:26px;display:grid;gap:11px;flex:1}
.pstep__n{display:inline-flex;align-items:center;justify-content:center;width:34px;height:34px;
  border-radius:50%;background:var(--accent-soft);color:var(--accent);font-size:13px;font-weight:600}
.pstep h3{font-family:var(--font-head);font-size:1.3rem;font-weight:500}
.pstep p{color:var(--muted);font-size:14.5px;font-weight:300;line-height:1.7}

/* мозаика */
.mos{display:grid;gap:16px;grid-template-columns:repeat(2,1fr)}
@media(min-width:900px){.mos{grid-template-columns:repeat(4,1fr)}
  .mos figure:nth-child(1){grid-column:span 2;grid-row:span 2}
  .mos figure:nth-child(7){grid-column:span 2}}
.mos figure{margin:0;position:relative;aspect-ratio:1/1;overflow:hidden;border-radius:var(--radius);
  box-shadow:var(--shadow);cursor:zoom-in}
@media(min-width:900px){.mos figure:nth-child(1){aspect-ratio:auto}.mos figure:nth-child(7){aspect-ratio:2/1}}
.mos img{width:100%;height:100%;object-fit:cover;transition:transform 1.2s cubic-bezier(.16,1,.3,1)}
.mos figure:hover img{transform:scale(1.06)}
.mos figcaption{position:absolute;inset:auto 0 0 0;padding:60px 18px 18px;color:#fff;font-size:13px;
  background:linear-gradient(transparent,rgba(20,26,21,.86));opacity:0;transform:translateY(10px);
  transition:.5s cubic-bezier(.16,1,.3,1)}
.mos figure:hover figcaption{opacity:1;transform:none}

/* объекты */
.objs{display:grid;gap:20px}
@media(min-width:800px){.objs{grid-template-columns:repeat(2,1fr)}
  .objs>*:first-child{grid-column:span 2}}
.obj{display:block;border-radius:var(--radius);overflow:hidden;position:relative;
  box-shadow:var(--shadow);transition:transform .55s cubic-bezier(.16,1,.3,1),box-shadow .55s}
.obj:hover{transform:translateY(-6px);box-shadow:var(--shadow-lg)}
.obj img{width:100%;aspect-ratio:16/10;object-fit:cover;transition:transform 1.3s cubic-bezier(.16,1,.3,1)}
.objs>*:first-child .obj img{aspect-ratio:21/9}
.obj:hover img{transform:scale(1.04)}
.obj__c{position:absolute;inset:auto 0 0 0;padding:74px 24px 24px;color:#fff;
  background:linear-gradient(transparent,rgba(20,26,21,.88))}
.obj__c h3{font-family:var(--font-head);font-size:clamp(1.2rem,2.2vw,1.8rem);font-weight:500}
.obj__c p{font-size:13.5px;opacity:.85;margin-top:5px;font-weight:300}

/* до/после */
.ba{box-shadow:var(--shadow-lg)}
.ba-wrap{display:grid;gap:34px;align-items:center}
@media(min-width:1000px){.ba-wrap{grid-template-columns:.8fr 1.2fr;gap:56px}}

/* заявка */
.cta{background:var(--bg-2);border-radius:clamp(24px,3vw,36px);padding:clamp(28px,5vw,62px);
  box-shadow:var(--shadow-lg)}
.cta__in{display:grid;gap:38px}
@media(min-width:960px){.cta__in{grid-template-columns:1fr 1fr;gap:60px;align-items:center}}
.cta form{display:grid;gap:15px}
.field input,.field textarea{border-radius:14px}

/* подвал */
.foot{padding:64px 0 32px}
.foot__grid{display:grid;gap:32px}
@media(min-width:800px){.foot__grid{grid-template-columns:1.5fr 1fr 1fr 1fr}}
.foot h4{font-size:12.5px;font-weight:500;color:var(--muted);margin-bottom:15px}
.foot p{font-size:15px;margin-bottom:9px;font-weight:300}
.foot a:hover{color:var(--accent)}
.foot__bot{margin-top:46px;padding-top:20px;border-top:1px solid var(--line);display:flex;flex-wrap:wrap;
  gap:12px;justify-content:space-between;font-size:12.5px;color:var(--muted)}
"""

ARR = ('<svg width="16" height="10" viewBox="0 0 18 10" fill="none" stroke="currentColor" '
       'stroke-width="1.6" stroke-linecap="round" aria-hidden="true"><path d="M0 5h16M12 1l4 4-4 4"/></svg>')
TICK = ('<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2.4" '
        'stroke-linecap="round" aria-hidden="true"><path d="M2.5 8.5l3.5 3.5 7.5-8"/></svg>')
DASH = ('<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2.4" '
        'stroke-linecap="round" aria-hidden="true"><path d="M3.5 8h9"/></svg>')

PACKS = [("Базовая", "по списку комплектации", 1.0),
         ("Расширенная", "фанера, кашировка рам", 1.12),
         ("Премиум", "полная отделка", 1.25)]
COPTS = [("Кондиционирование", 90000), ("Тёплый пол", 110000),
         ("Сантехнические приборы", 75000), ("Светодиодные подсветки", 45000),
         ("Мебель и интерьер", 250000)]
# реальный график из договора, указанный на сайте
SCHEDULE = [
    (30, "Аванс при заключении договора", "цена фиксируется и больше не меняется"),
    (40, "Через две недели", "дом уходит в производство"),
    (15, "После приёмки на производстве", "перед отгрузкой на трал"),
    (15, "После монтажа на участке", "когда получаете ключи"),
]

def build():
    b = BRAND
    nav = "".join(f'<a href="{h}">{t}</a>' for h, t in NAV)
    o = [core.head("ДОММ — модульные дома под ключ | Новосибирск",
                   "Соберите комплектацию, узнайте стоимость и график платежей по договору. "
                   "Модульные дома от 990 000 ₽ за 30 дней.",
                   FONTS, CSS, "#FBFAF7")]
    o.append('<div class="mesh"><i></i><i></i><i></i></div><div class="cursor"></div>')

    o.append(f"""
<header class="hdr" data-header><div class="wrap"><div class="hdr__in">
  <a class="logo" href="#top"><i></i>ДОММ</a>
  <nav class="nav">{nav}</nav>
  <div style="display:flex;gap:10px;align-items:center">
    <a class="btn btn--fill hdr__cta" href="#calc" data-magnet=".25">Рассчитать</a>
    <button class="burger" data-burger aria-label="Меню" aria-expanded="false"><i></i><i></i><i></i></button>
  </div>
</div></div></header>
<nav class="mnav" data-menu>{nav}
  <div class="mnav__foot"><a href="tel:{b['phone1_href']}">{b['phone1']}</a>
  <a href="tel:{b['phone2_href']}">{b['phone2']}</a><a href="mailto:{b['email']}">{b['email']}</a></div>
</nav>""")

    o.append(f"""
<section class="hero" id="top"><div class="wrap">
  <div class="hero__in">
    <div data-rv="up">
      <span class="pill"><i></i>{HERO['kicker']}</span>
      <h1 class="h1" style="margin:20px 0 20px" data-split="line">Модульные дома<br>для жизни<br>и <span class="soft">отдыха</span></h1>
      <p class="lead">{HERO['sub']} {HERO['sub2']}</p>
      <div class="hero__acts">
        <a class="btn btn--fill" href="#calc" data-magnet=".3">Рассчитать стоимость {ARR}</a>
        <a class="btn btn--soft" href="{b['wa']}" target="_blank" rel="noopener">Написать в WhatsApp</a>
      </div>
    </div>
    <div class="hero__vis" data-rv="zoom">
      <figure><img src="{HERO['bg']}" alt="Модульный дом ДОММ с террасой"></figure>
      <div class="sticker"><b>от 990 000 ₽</b><span>дом под ключ за 30 дней</span></div>
    </div>
  </div>
  <div class="nums" data-stagger="80">
    <div class="num" data-rv="up"><b data-count="80" data-suffix="+">0</b><span>реализованных проектов</span></div>
    <div class="num" data-rv="up"><b data-count="30">0</b><span>дней до готового дома</span></div>
    <div class="num" data-rv="up"><b>1 день</b><span>монтаж краном на участке</span></div>
    <div class="num" data-rv="up"><b data-count="18">0</b><span>готовых планировок</span></div>
  </div>
</div></section>""")

    models = "".join(f"""
      <button class="chip{' on' if i==0 else ''}" data-model data-price="{p.replace(' ','')}"
              data-name="{n}">{n}<small>{area} · от {p} ₽</small></button>""" 
              for i, (n, d, p, area, im) in enumerate(PROJECTS))
    packs = "".join(f"""
      <button class="chip{' on' if i==0 else ''}" data-pack data-k="{k}" data-name="{n}">{n}<small>{d}</small></button>"""
              for i, (n, d, k) in enumerate(PACKS))
    copts = "".join(f"""
      <label class="opt"><input type="checkbox" value="{p}" data-name="{n}"><span class="bx">{TICK}</span>
        <span class="t">{n}</span><b>+{p:,} ₽</b></label>""".replace(",", " ") for n, p in COPTS)
    pays = "".join(f"""
      <div class="pay__row">
        <span class="pay__pc">{pc}%</span>
        <span class="pay__t"><b>{t}</b><span>{d}</span></span>
        <span class="pay__v" data-pay="{pc}">—</span>
        <span class="pay__bar"><i style="width:{pc}%"></i></span>
      </div>""" for pc, t, d in SCHEDULE)

    o.append(f"""
<section class="sec" id="calc"><div class="wrap">
  <div class="sec-head split">
    <div data-rv="up"><span class="pill"><i></i>Калькулятор</span>
      <h2 class="h2" style="margin-top:18px" data-split="line">Соберите дом<br>и посмотрите <span class="soft">график платежей</span></h2></div>
    <p class="lead" data-rv="up" style="--d:150ms">Стоимость пересчитывается сразу, а рядом сразу видно,
    сколько и когда платить по договору. Никакой рассрочки и процентов — это наш обычный порядок оплаты.</p>
  </div>
  <div class="calc">
    <div class="panel" data-rv="up">
      <div class="grp"><span>Модель дома</span><div class="chips">{models}</div></div>
      <div class="grp"><span>Комплектация</span><div class="chips">{packs}</div></div>
      <div class="grp"><span>Дополнительные опции</span>{copts}</div>
    </div>
    <div class="sum" data-rv="up" style="--d:120ms">
      <span>Стоимость дома</span>
      <div class="sum__total" data-total>990 000 ₽</div>
      <div class="sum__sub" data-sub>MODUL HOUSE 1 · базовая комплектация</div>
      <div class="pay">{pays}</div>
      <p class="sum__note">Без доставки, фундамента и монтажа на участке — их считаем отдельно
      по адресу. Сроки готовности фиксируются в договоре и зависят от очереди на производстве.</p>
      <a class="btn" href="#cta" data-send-calc>Зафиксировать расчёт {ARR}</a>
    </div>
  </div>
</div></section>""")

    cards = "".join(f"""
    <article class="card" data-rv="up">
      <div class="card__i"><span class="card__tag">{area}</span><img src="{im}" alt="{n}" loading="lazy"></div>
      <div class="card__b"><h3 class="h3">{n}</h3><p>{d}</p>
        <div class="card__p"><b>от {p} ₽</b><span>под ключ</span></div>
        <a class="btn btn--soft" href="#cta" style="margin-top:12px;justify-self:start">Подробнее {ARR}</a></div>
    </article>""" for n, d, p, area, im in PROJECTS)
    o.append(f"""
<section class="sec" id="projects"><div class="wrap">
  <div class="sec-head split">
    <div data-rv="up"><span class="pill"><i></i>Каталог</span>
      <h2 class="h2" style="margin-top:18px">Проекты домов и <span class="soft">бань</span></h2></div>
    <p class="lead" data-rv="up" style="--d:150ms">Семь базовых моделей и две бани — любую адаптируем
    под участок и сценарий жизни.</p>
  </div>
  <div class="cards" data-stagger="90">{cards}</div>
</div></section>""")

    figs = "".join(f'<figure data-lb="g" data-full="{u}" data-cap="Дом ДОММ"><img src="{u}" alt="Модульный дом ДОММ" loading="lazy"></figure>'
                   for u in GALLERY)
    o.append(f"""
<section class="sec" id="gallery">
  <div class="wrap sec-head split">
    <div data-rv="up"><span class="pill"><i></i>Галерея</span>
      <h2 class="h2" style="margin-top:18px">Декорируем дома в <span class="soft">уютном</span> стиле</h2></div>
    <p class="lead" data-rv="up" style="--d:150ms">Тёплое дерево, мягкий свет и панорамные окна.
    Потяните ленту вбок.</p>
  </div>
  <div class="gal" data-drag>{figs}</div>
</section>""")

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
  <div class="sec-head split">
    <div data-rv="up"><span class="pill"><i></i>Планировки и цены</span>
      <h2 class="h2" style="margin-top:18px">Выберите свой <span class="soft">метраж</span></h2></div>
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

    def li(items_, ic):
        return "".join(f'<li><i>{ic}</i><span>{t}</span></li>' for t in items_)
    o.append(f"""
<section class="sec" id="spec"><div class="wrap">
  <div class="sec-head split">
    <div data-rv="up"><span class="pill"><i></i>Комплектация</span>
      <h2 class="h2" style="margin-top:18px" data-split="line">Что входит<br>в <span class="soft">базовую</span> стоимость</h2></div>
    <p class="lead" data-rv="up" style="--d:150ms">Честный список без звёздочек: что вы получаете сразу,
    что оплачивается отдельно и что можно добавить.</p>
  </div>
  <div class="spec" data-stagger="110">
    <div class="spec__c spec--in"><h3>Входит в стоимость</h3><ul>{li(INCLUDED, TICK)}</ul></div>
    <div class="spec__c spec--out"><h3>Не входит</h3><ul>{li(EXCLUDED, DASH)}</ul></div>
    <div class="spec__c"><h3>Опции</h3><ul>{li(OPTIONS, TICK)}</ul></div>
  </div>
</div></section>""")

    steps = "".join(f"""
    <article class="pstep" data-rv="up">
      <div class="pstep__i"><img src="{im}" alt="{t}" loading="lazy"></div>
      <div class="pstep__b"><span class="pstep__n">{n}</span><h3>{t}</h3><p>{d}</p></div>
    </article>""" for n, t, d, im in PROCESS)
    o.append(f"""
<section class="sec" id="process"><div class="wrap">
  <div class="sec-head" data-rv="up"><span class="pill"><i></i>Как мы работаем</span>
    <h2 class="h2" style="margin-top:18px">Четыре шага до <span class="soft">новоселья</span></h2></div>
  <div class="pr" data-stagger="100">{steps}</div>
</div></section>""")

    mos = "".join(f'<figure data-lb="d" data-full="{im}" data-cap="{t}"><img src="{im}" alt="{t}" loading="lazy"><figcaption>{t}</figcaption></figure>'
                  for t, im in DETAILS + INTERIOR)
    o.append(f"""
<section class="sec" id="details"><div class="wrap">
  <div class="sec-head split">
    <div data-rv="up"><span class="pill"><i></i>Black Paket</span>
      <h2 class="h2" style="margin-top:18px" data-split="line">Детали в едином<br><span class="soft">чёрном</span> стиле</h2></div>
    <p class="lead" data-rv="up" style="--d:150ms">Электрощит, розетки, выключатели, светильники
    и ручки — одно оформление без визуального шума.</p>
  </div>
  <div class="mos" data-stagger="70">{mos}</div>
</div></section>""")

    objs = "".join(f"""
    <div><a class="obj" href="#cta"><img src="{im}" alt="{t}" loading="lazy">
      <span class="obj__c"><h3>{t}</h3><p>{d}</p></span></a></div>""" for t, d, im in OBJECTS)
    o.append(f"""
<section class="sec" id="objects"><div class="wrap">
  <div class="sec-head" data-rv="up"><span class="pill"><i></i>Наши дома</span>
    <h2 class="h2" style="margin-top:18px">Реализованные <span class="soft">объекты</span></h2></div>
  <div class="objs" data-stagger="90">{objs}</div>
</div></section>""")

    o.append(f"""
<section class="sec"><div class="wrap ba-wrap">
  <div data-rv="up"><span class="pill"><i></i>Посмотрите разницу</span>
    <h2 class="h2" style="margin:18px 0 16px" data-split="line">Ваш дом у нас —<br>и ваш дом <span class="soft">у вас</span></h2>
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
    <span class="pill"><i></i>Свяжитесь с нами</span>
    <h2 class="h2" style="margin:18px 0 16px">Оставьте заявку и получите <span class="soft">расчёт</span></h2>
    <p class="lead">Подберём планировку под участок и посчитаем стоимость с доставкой и монтажом.</p>
    <div style="margin-top:26px;display:grid;gap:8px;font-family:var(--font-head);font-size:1.5rem;font-weight:500">
      <a href="tel:{b['phone1_href']}">{b['phone1']}</a><a href="tel:{b['phone2_href']}">{b['phone2']}</a>
    </div>
  </div>
  <form data-form novalidate>
    <div class="f-row two">
      <div class="field"><label for="n8">Ваше имя</label>
        <input id="n8" type="text" required autocomplete="name" placeholder="Иван"><span class="err">Укажите имя</span></div>
      <div class="field"><label for="t8">Телефон</label>
        <input id="t8" type="tel" required autocomplete="tel" inputmode="tel" placeholder="+7 (___) ___-__-__">
        <span class="err">Введите номер полностью</span></div>
    </div>
    <div class="field"><label for="m8">Комментарий</label>
      <textarea id="m8" rows="4" placeholder="Интересует MODUL HOUSE 3, участок в Бердске"></textarea></div>
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
/* --- Калькулятор и график платежей --- */
(function(){
  var root = document.getElementById('calc'); if(!root) return;
  var total = root.querySelector('[data-total]'),
      sub   = root.querySelector('[data-sub]'),
      pays  = root.querySelectorAll('[data-pay]');
  var cur = 0;
  function money(n){ return Math.round(n).toLocaleString('ru-RU') + ' ₽'; }

  function pick(sel, el){
    root.querySelectorAll(sel).forEach(function(x){ x.classList.remove('on'); });
    el.classList.add('on'); calc();
  }
  root.querySelectorAll('[data-model]').forEach(function(x){
    x.addEventListener('click', function(){ pick('[data-model]', x); }); });
  root.querySelectorAll('[data-pack]').forEach(function(x){
    x.addEventListener('click', function(){ pick('[data-pack]', x); }); });
  root.querySelectorAll('.opt input').forEach(function(x){ x.addEventListener('change', calc); });

  function calc(){
    var m = root.querySelector('[data-model].on'), p = root.querySelector('[data-pack].on');
    var add = 0, names = [];
    root.querySelectorAll('.opt input:checked').forEach(function(x){
      add += parseFloat(x.value); names.push(x.dataset.name);
    });
    var sum = parseFloat(m.dataset.price) * parseFloat(p.dataset.k) + add;

    sub.textContent = m.dataset.name + ' · комплектация «' + p.dataset.name + '»' +
                      (names.length ? ' · опций: ' + names.length : '');
    pays.forEach(function(el){ el.textContent = money(sum * (+el.dataset.pay) / 100); });

    var from = cur, t0 = null; cur = sum;
    if(window.matchMedia('(prefers-reduced-motion: reduce)').matches){ total.textContent = money(sum); return; }
    /* первый кадр только через rAF, иначе t === undefined и получится NaN */
    requestAnimationFrame(function anim(t){
      if(t0 === null) t0 = t;
      var q = Math.min((t - t0) / 480, 1), e = 1 - Math.pow(1 - q, 3);
      total.textContent = money(from + (sum - from) * e);
      if(q < 1) requestAnimationFrame(anim);
    });
  }

  var send = root.querySelector('[data-send-calc]');
  if(send) send.addEventListener('click', function(){
    var box = document.querySelector('#cta textarea'); if(!box) return;
    var lines = ['Расчёт с сайта — ' + total.textContent, sub.textContent];
    root.querySelectorAll('.pay__row').forEach(function(r){
      lines.push(r.querySelector('.pay__pc').textContent + ' — ' +
                 r.querySelector('.pay__t b').textContent + ': ' +
                 r.querySelector('.pay__v').textContent);
    });
    box.value = lines.join('\n');
    setTimeout(function(){ var n = document.querySelector('#cta input[type="text"]'); if(n) n.focus(); }, 700);
  });

  calc();
})();
"""
    o.append(core.tail(extra))
    return "".join(o)
