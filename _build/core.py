# -*- coding: utf-8 -*-
"""Общее ядро: сброс стилей, движок анимаций, лайтбокс, форма, счётчики."""

CORE_CSS = r"""
*,*::before,*::after{box-sizing:border-box}
html{-webkit-text-size-adjust:100%;scroll-behavior:smooth}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
body{margin:0;background:var(--bg);color:var(--fg);font-family:var(--font-body);
  font-size:16px;line-height:1.6;-webkit-font-smoothing:antialiased;overflow-x:hidden}
img{max-width:100%;display:block}
a{color:inherit;text-decoration:none}
button{font:inherit;color:inherit;cursor:pointer;border:0;background:none}
h1,h2,h3,h4{margin:0;font-family:var(--font-head);line-height:1.05;font-weight:var(--head-weight,700)}
p{margin:0}
ul{margin:0;padding:0;list-style:none}
:focus-visible{outline:2px solid var(--accent);outline-offset:3px;border-radius:2px}
.wrap{width:min(1280px,100% - 2 * var(--gutter));margin-inline:auto}
:root{--gutter:20px}
@media(min-width:768px){:root{--gutter:40px}}
@media(min-width:1280px){:root{--gutter:56px}}
body.nav-open{overflow:hidden}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}

/* ---------- Движок появления ---------- */
[data-rv]{opacity:0;will-change:transform,opacity;
  transition:opacity .9s cubic-bezier(.16,1,.3,1),transform 1s cubic-bezier(.16,1,.3,1),clip-path 1.1s cubic-bezier(.16,1,.3,1);
  transition-delay:var(--d,0ms)}
[data-rv="up"]{transform:translate3d(0,42px,0)}
[data-rv="left"]{transform:translate3d(-48px,0,0)}
[data-rv="right"]{transform:translate3d(48px,0,0)}
[data-rv="zoom"]{transform:scale(.92)}
[data-rv="blur"]{filter:blur(14px);transform:translate3d(0,20px,0)}
[data-rv="mask"]{clip-path:inset(0 0 100% 0);opacity:1}
[data-rv="maskx"]{clip-path:inset(0 100% 0 0);opacity:1}
[data-rv].in{opacity:1;transform:none;filter:none;clip-path:inset(0 0 0 0)}
/* Построчный вылет заголовка */
.line{display:block;overflow:hidden;padding-bottom:.08em;margin-bottom:-.08em}
.line>span{display:block;transform:translate3d(0,105%,0) rotate(2deg);
  transition:transform 1.05s cubic-bezier(.16,1,.3,1);transition-delay:var(--d,0ms)}
.in .line>span,.line.in>span{transform:none}
/* Пословный вылет */
.w{display:inline-block;overflow:hidden;vertical-align:bottom;padding-bottom:.08em;margin-bottom:-.08em}
.w>i{display:inline-block;font-style:inherit;transform:translate3d(0,110%,0);
  transition:transform .95s cubic-bezier(.16,1,.3,1);transition-delay:var(--d,0ms)}
.in .w>i{transform:none}
@media (prefers-reduced-motion:reduce){
  [data-rv],[data-rv].in{opacity:1!important;transform:none!important;filter:none!important;clip-path:none!important;transition:none!important}
  .line>span,.w>i{transform:none!important;transition:none!important}
  .marquee__track{animation:none!important}
}

/* ---------- Плавающий индикатор прокрутки ---------- */
.progress{position:fixed;inset:0 0 auto 0;height:2px;z-index:120;background:transparent;pointer-events:none}
.progress__bar{height:100%;width:100%;transform-origin:0 50%;transform:scaleX(0);background:var(--accent)}

/* ---------- Курсор ---------- */
.cursor{position:fixed;top:0;left:0;z-index:200;pointer-events:none;mix-blend-mode:difference;
  width:16px;height:16px;border-radius:50%;background:#fff;translate:-50% -50%;
  transition:width .3s cubic-bezier(.16,1,.3,1),height .3s cubic-bezier(.16,1,.3,1),opacity .3s;opacity:0}
.cursor.on{opacity:1}
.cursor.big{width:76px;height:76px}
@media(hover:none),(pointer:coarse){.cursor{display:none}}

/* ---------- Бегущая строка ---------- */
.marquee{overflow:hidden;display:flex;user-select:none}
.marquee__track{display:flex;flex:0 0 auto;gap:var(--mq-gap,2rem);padding-right:var(--mq-gap,2rem);
  animation:mq var(--mq-dur,28s) linear infinite}
.marquee:hover .marquee__track{animation-play-state:paused}
@keyframes mq{to{transform:translate3d(-100%,0,0)}}

/* ---------- Лайтбокс ---------- */
.lb{position:fixed;inset:0;z-index:300;display:grid;place-items:center;padding:24px;
  background:rgba(8,8,9,.94);opacity:0;visibility:hidden;transition:opacity .4s,visibility .4s;backdrop-filter:blur(8px)}
.lb.open{opacity:1;visibility:visible}
.lb img{max-width:min(1200px,92vw);max-height:86vh;width:auto;border-radius:var(--radius,4px);
  transform:scale(.94);transition:transform .5s cubic-bezier(.16,1,.3,1);box-shadow:0 40px 120px rgba(0,0,0,.6)}
.lb.open img{transform:scale(1)}
.lb__x,.lb__nav{position:absolute;display:grid;place-items:center;width:52px;height:52px;border-radius:50%;
  background:rgba(255,255,255,.1);color:#fff;transition:background .25s,transform .25s}
.lb__x:hover,.lb__nav:hover{background:rgba(255,255,255,.22);transform:scale(1.08)}
.lb__x{top:20px;right:20px;font-size:26px;line-height:1}
.lb__nav{top:50%;translate:0 -50%;font-size:22px}
.lb__nav.prev{left:16px}.lb__nav.next{right:16px}
.lb__cap{position:absolute;bottom:22px;left:50%;translate:-50% 0;color:rgba(255,255,255,.75);
  font-size:13px;letter-spacing:.06em;text-align:center;max-width:80vw}

/* ---------- Форма ---------- */
.f-row{display:grid;gap:14px}
@media(min-width:640px){.f-row.two{grid-template-columns:1fr 1fr}}
.field{position:relative}
.field label{display:block;font-size:12px;letter-spacing:.12em;text-transform:uppercase;
  margin-bottom:8px;color:var(--muted)}
.field input,.field textarea{width:100%;padding:15px 16px;background:var(--input-bg);
  color:var(--fg);border:1px solid var(--line);border-radius:var(--radius-sm,4px);font:inherit;font-size:16px;
  transition:border-color .25s,background .25s,box-shadow .25s}
.field input:focus,.field textarea:focus{outline:none;border-color:var(--accent);
  box-shadow:0 0 0 4px color-mix(in srgb,var(--accent) 18%,transparent)}
.field .err{display:block;min-height:16px;margin-top:6px;font-size:12px;color:#ff6b6b;opacity:0;transition:opacity .2s}
.field.bad input{border-color:#ff6b6b}
.field.bad .err{opacity:1}
.form-note{font-size:12px;color:var(--muted);line-height:1.5}
.form-ok{display:none;padding:18px;border:1px solid var(--accent);border-radius:var(--radius-sm,4px);
  color:var(--accent);font-size:15px}
.form-ok.show{display:block;animation:pop .5s cubic-bezier(.16,1,.3,1)}
@keyframes pop{from{opacity:0;transform:translateY(10px) scale(.98)}to{opacity:1;transform:none}}

/* ---------- До / После ---------- */
.ba{position:relative;overflow:hidden;border-radius:var(--radius,4px);aspect-ratio:16/10;cursor:ew-resize;
  touch-action:none;user-select:none}
.ba img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.ba__after{clip-path:inset(0 0 0 var(--x,50%))}
.ba__line{position:absolute;top:0;bottom:0;left:var(--x,50%);width:2px;background:#fff;
  box-shadow:0 0 0 1px rgba(0,0,0,.25)}
.ba__grip{position:absolute;top:50%;left:var(--x,50%);translate:-50% -50%;width:54px;height:54px;
  border-radius:50%;background:#fff;color:#111;display:grid;place-items:center;font-size:16px;
  box-shadow:0 10px 34px rgba(0,0,0,.35)}
.ba__tag{position:absolute;bottom:14px;padding:7px 14px;border-radius:100px;font-size:11px;
  letter-spacing:.16em;text-transform:uppercase;background:rgba(0,0,0,.55);color:#fff;backdrop-filter:blur(6px)}
.ba__tag.l{left:14px}.ba__tag.r{right:14px}

/* ---------- Плавающие кнопки связи ---------- */
.dock{position:fixed;right:18px;bottom:18px;z-index:110;display:flex;flex-direction:column;gap:12px}
.dock a{display:grid;place-items:center;width:54px;height:54px;border-radius:50%;
  background:var(--accent);color:var(--on-accent);box-shadow:0 12px 34px rgba(0,0,0,.28);
  transition:transform .3s cubic-bezier(.16,1,.3,1),box-shadow .3s}
.dock a:hover{transform:translateY(-4px) scale(1.06);box-shadow:0 18px 44px rgba(0,0,0,.36)}
.dock a.wa{background:#25D366;color:#fff}
@media(min-width:1024px){.dock{right:28px;bottom:28px}}
"""

CORE_JS = r"""
(function(){
  'use strict';
  var RM = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* --- Появление при прокрутке ---
     Считаем позицию сами: clip-path у «шторных» блоков обнуляет
     площадь пересечения, и IntersectionObserver для них не срабатывает. --- */
  var queue = [];
  function checkReveal(){
    if(!queue.length) return;
    var h = window.innerHeight, rest = [];
    for(var i = 0; i < queue.length; i++){
      var el = queue[i], r = el.getBoundingClientRect();
      if(r.width === 0 && r.height === 0){ rest.push(el); continue; }  /* скрытая вкладка */
      if(r.top < h * 0.88) el.classList.add('in'); else rest.push(el);
    }
    queue = rest;
  }
  function scan(root){
    (root||document).querySelectorAll('[data-rv],[data-stagger],.split').forEach(function(el){
      if(el.dataset.rvBound) return; el.dataset.rvBound = '1'; queue.push(el);
    });
    checkReveal();
  }

  /* --- Разбивка заголовков на строки/слова --- */
  document.querySelectorAll('[data-split="word"]').forEach(function(el){
    var i = 0;
    el.innerHTML = el.textContent.trim().split(/\s+/).map(function(w){
      var d = (i++) * 55;
      return '<span class="w"><i style="--d:'+d+'ms">'+w+'</i></span>';
    }).join(' ');
    el.classList.add('split');
  });
  document.querySelectorAll('[data-split="line"]').forEach(function(el){
    var i = 0;
    el.innerHTML = el.innerHTML.split(/<br\s*\/?>/i).map(function(l){
      var d = (i++) * 130;
      return '<span class="line"><span style="--d:'+d+'ms">'+l.trim()+'</span></span>';
    }).join('');
    el.classList.add('split');
  });

  /* --- Каскад для групп --- */
  document.querySelectorAll('[data-stagger]').forEach(function(g){
    var step = parseInt(g.dataset.stagger,10) || 70;
    Array.prototype.forEach.call(g.children,function(c,i){
      if(!c.hasAttribute('data-rv')) c.setAttribute('data-rv', g.dataset.rvChild || 'up');
      c.style.setProperty('--d', (i*step)+'ms');
    });
  });

  /* --- Индикатор прокрутки --- */
  var bar = document.querySelector('.progress__bar');
  /* --- Шапка --- */
  var head = document.querySelector('[data-header]');
  var lastY = 0, ticking = false;
  function onScroll(){
    var y = window.scrollY;
    if(bar){
      var h = document.documentElement.scrollHeight - window.innerHeight;
      bar.style.transform = 'scaleX(' + (h>0 ? y/h : 0) + ')';
    }
    if(head){
      head.classList.toggle('stuck', y > 40);
      head.classList.toggle('hide', y > 560 && y > lastY);
    }
    /* параллакс */
    document.querySelectorAll('[data-par]').forEach(function(el){
      var r = el.getBoundingClientRect();
      if(r.bottom < -200 || r.top > window.innerHeight + 200) return;
      var p = (r.top + r.height/2 - window.innerHeight/2) / window.innerHeight;
      el.style.setProperty('--par', (p * (parseFloat(el.dataset.par)||30)).toFixed(2) + 'px');
    });
    checkReveal();
    lastY = y; ticking = false;
  }
  function req(){ if(!ticking){ ticking = true; requestAnimationFrame(onScroll); } }
  window.addEventListener('scroll', req, {passive:true});
  window.addEventListener('resize', req);

  /* --- Счётчики --- */
  var cio = new IntersectionObserver(function(es){
    es.forEach(function(e){
      if(!e.isIntersecting) return;
      cio.unobserve(e.target);
      var el = e.target, to = parseFloat(el.dataset.count), t0 = null, dur = 1500;
      if(RM){ el.textContent = el.dataset.raw || to; return; }
      requestAnimationFrame(function step(t){
        if(!t0) t0 = t;
        var k = Math.min((t-t0)/dur,1), e2 = 1 - Math.pow(1-k,3);
        el.textContent = Math.round(to*e2).toLocaleString('ru-RU') + (el.dataset.suffix||'');
        if(k<1) requestAnimationFrame(step);
      });
    });
  },{threshold:.4});
  document.querySelectorAll('[data-count]').forEach(function(el){ cio.observe(el); });

  /* --- Наклон карточек --- */
  if(!RM && window.matchMedia('(hover:hover)').matches){
    document.querySelectorAll('[data-tilt]').forEach(function(el){
      var max = parseFloat(el.dataset.tilt) || 8;
      el.addEventListener('pointermove', function(ev){
        var r = el.getBoundingClientRect();
        var x = (ev.clientX - r.left)/r.width - .5, y = (ev.clientY - r.top)/r.height - .5;
        el.style.setProperty('--rx', (-y*max).toFixed(2)+'deg');
        el.style.setProperty('--ry', (x*max).toFixed(2)+'deg');
        el.style.setProperty('--mx', (x*100+50).toFixed(1)+'%');
        el.style.setProperty('--my', (y*100+50).toFixed(1)+'%');
      });
      el.addEventListener('pointerleave', function(){
        el.style.setProperty('--rx','0deg'); el.style.setProperty('--ry','0deg');
      });
    });
  }

  /* --- Магнитные кнопки --- */
  if(!RM && window.matchMedia('(hover:hover)').matches){
    document.querySelectorAll('[data-magnet]').forEach(function(el){
      var s = parseFloat(el.dataset.magnet) || .3;
      el.addEventListener('pointermove', function(ev){
        var r = el.getBoundingClientRect();
        el.style.setProperty('--tx', ((ev.clientX - r.left - r.width/2)*s).toFixed(1)+'px');
        el.style.setProperty('--ty', ((ev.clientY - r.top - r.height/2)*s).toFixed(1)+'px');
      });
      el.addEventListener('pointerleave', function(){
        el.style.setProperty('--tx','0px'); el.style.setProperty('--ty','0px');
      });
    });
  }

  /* --- Курсор --- */
  var cur = document.querySelector('.cursor');
  if(cur && window.matchMedia('(hover:hover)').matches && !RM){
    var cx=0, cy=0, tx=0, ty=0;
    window.addEventListener('pointermove', function(e){ tx=e.clientX; ty=e.clientY; cur.classList.add('on'); });
    (function loop(){ cx += (tx-cx)*.18; cy += (ty-cy)*.18;
      cur.style.transform = 'translate3d('+cx+'px,'+cy+'px,0)'; requestAnimationFrame(loop); })();
    document.addEventListener('pointerover', function(e){
      var t = e.target.closest('a,button,[data-cursor]');
      cur.classList.toggle('big', !!t);
    });
  }

  /* --- Лайтбокс --- */
  var lb = document.querySelector('.lb');
  if(lb){
    var lbImg = lb.querySelector('img'), lbCap = lb.querySelector('.lb__cap');
    var pool = [], idx = 0;
    function show(i){
      idx = (i + pool.length) % pool.length;
      lbImg.src = pool[idx].src;
      lbCap.textContent = pool[idx].cap || '';
    }
    function open(list, i){ pool = list; show(i); lb.classList.add('open');
      document.body.style.overflow='hidden'; lb.focus(); }
    function close(){ lb.classList.remove('open'); document.body.style.overflow=''; }
    document.addEventListener('click', function(e){
      var t = e.target.closest('[data-lb]');
      if(!t) return;
      e.preventDefault();
      var group = t.dataset.lb;
      var items = Array.prototype.slice.call(document.querySelectorAll('[data-lb="'+group+'"]'));
      open(items.map(function(n){
        return {src: n.dataset.full || (n.querySelector('img')||n).src, cap: n.dataset.cap || ''};
      }), items.indexOf(t));
    });
    lb.addEventListener('click', function(e){
      if(e.target.closest('.next')) return show(idx+1);
      if(e.target.closest('.prev')) return show(idx-1);
      if(!e.target.closest('img')) close();
    });
    document.addEventListener('keydown', function(e){
      if(!lb.classList.contains('open')) return;
      if(e.key==='Escape') close();
      if(e.key==='ArrowRight') show(idx+1);
      if(e.key==='ArrowLeft') show(idx-1);
    });
  }

  /* --- До / после --- */
  document.querySelectorAll('.ba').forEach(function(el){
    function set(clientX){
      var r = el.getBoundingClientRect();
      var p = Math.max(0, Math.min(100, (clientX - r.left)/r.width*100));
      el.style.setProperty('--x', p.toFixed(1)+'%');
    }
    var down = false;
    el.addEventListener('pointerdown', function(e){ down=true; el.setPointerCapture(e.pointerId); set(e.clientX); });
    el.addEventListener('pointermove', function(e){ if(down) set(e.clientX); });
    el.addEventListener('pointerup', function(){ down=false; });
    el.addEventListener('pointercancel', function(){ down=false; });
  });

  /* --- Вкладки --- */
  document.querySelectorAll('[data-tabs]').forEach(function(root){
    var btns = root.querySelectorAll('[data-tab]');
    btns.forEach(function(b){
      b.addEventListener('click', function(){
        btns.forEach(function(x){ x.classList.remove('active'); x.setAttribute('aria-selected','false'); });
        b.classList.add('active'); b.setAttribute('aria-selected','true');
        root.querySelectorAll('[data-panel]').forEach(function(p){
          var on = p.dataset.panel === b.dataset.tab;
          p.hidden = !on;
          if(on){ p.classList.remove('in'); void p.offsetWidth; scan(p); p.classList.add('in'); }
        });
      });
    });
  });

  /* --- Аккордеон --- */
  document.querySelectorAll('[data-acc] > .acc__item').forEach(function(item){
    var head = item.querySelector('.acc__head');
    if(!head) return;
    head.addEventListener('click', function(){
      var open = item.classList.toggle('open');
      head.setAttribute('aria-expanded', open ? 'true':'false');
      var b = item.querySelector('.acc__body');
      if(b) b.style.maxHeight = open ? b.scrollHeight + 'px' : '0px';
    });
  });

  /* --- Горизонтальные ленты: перетаскивание --- */
  document.querySelectorAll('[data-drag]').forEach(function(el){
    var down=false, sx=0, sl=0;
    el.addEventListener('pointerdown', function(e){
      if(e.target.closest('a,button')) return;
      down=true; sx=e.clientX; sl=el.scrollLeft; el.classList.add('dragging');
    });
    window.addEventListener('pointerup', function(){ down=false; el.classList.remove('dragging'); });
    el.addEventListener('pointermove', function(e){ if(down) el.scrollLeft = sl - (e.clientX - sx); });
  });

  /* --- Форма --- */
  document.querySelectorAll('[data-form]').forEach(function(form){
    var phone = form.querySelector('input[type="tel"]');
    if(phone){
      phone.addEventListener('input', function(){
        var d = phone.value.replace(/\D/g,'').replace(/^8/,'7').replace(/^([^7])/,'7$1').slice(0,11);
        var out = '+7';
        if(d.length>1) out += ' (' + d.slice(1,4);
        if(d.length>=5) out += ') ' + d.slice(4,7);
        if(d.length>=8) out += '-' + d.slice(7,9);
        if(d.length>=10) out += '-' + d.slice(9,11);
        phone.value = out;
      });
    }
    form.addEventListener('submit', function(e){
      e.preventDefault();
      var ok = true;
      form.querySelectorAll('[required]').forEach(function(f){
        var bad = !f.value.trim() || (f.type==='tel' && f.value.replace(/\D/g,'').length < 11);
        f.closest('.field').classList.toggle('bad', bad);
        if(bad) ok = false;
      });
      if(!ok){ var b = form.querySelector('.field.bad input'); if(b) b.focus(); return; }
      var btn = form.querySelector('[type="submit"]');
      if(btn){ btn.disabled = true; btn.dataset.txt = btn.textContent; btn.textContent = 'Отправляем…'; }
      setTimeout(function(){
        form.querySelector('.form-ok').classList.add('show');
        form.querySelectorAll('input,textarea').forEach(function(f){ f.value=''; });
        if(btn){ btn.disabled=false; btn.textContent = btn.dataset.txt; }
      }, 700);
    });
  });

  /* --- Мобильное меню --- */
  var burger = document.querySelector('[data-burger]'), menu = document.querySelector('[data-menu]');
  if(burger && menu){
    burger.addEventListener('click', function(){
      var open = document.body.classList.toggle('nav-open');
      burger.setAttribute('aria-expanded', open?'true':'false');
    });
    menu.addEventListener('click', function(e){
      if(e.target.closest('a')) document.body.classList.remove('nav-open');
    });
  }

  /* --- Год --- */
  document.querySelectorAll('[data-year]').forEach(function(el){ el.textContent = new Date().getFullYear(); });

  scan();
  onScroll();
  window.addEventListener('load', function(){ document.body.classList.add('ready'); onScroll(); });
})();
"""

def head(title, desc, fonts, css, theme):
    return f"""<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="{theme}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
{fonts}
<style>
{CORE_CSS}
{css}
</style>
</head>
<body>
<div class="progress"><div class="progress__bar"></div></div>
"""

def tail(extra_js=""):
    return f"""
<div class="lb" tabindex="-1" role="dialog" aria-label="Просмотр фотографии">
  <button class="lb__x" aria-label="Закрыть">&times;</button>
  <button class="lb__nav prev" aria-label="Предыдущее фото">&#10094;</button>
  <img src="" alt="">
  <button class="lb__nav next" aria-label="Следующее фото">&#10095;</button>
  <div class="lb__cap"></div>
</div>
<script>
{CORE_JS}
{extra_js}
</script>
</body>
</html>
"""

def dock(b):
    return f"""
<div class="dock">
  <a class="wa" href="{b['wa']}" target="_blank" rel="noopener" aria-label="Написать в WhatsApp">
    <svg width="26" height="26" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.5 14.4c-.3-.2-1.7-.9-2-1-.3-.1-.5-.2-.7.2s-.8 1-.9 1.1c-.2.2-.3.2-.6.1-.3-.2-1.2-.5-2.3-1.4-.9-.8-1.4-1.7-1.6-2-.2-.3 0-.5.1-.6l.5-.6c.1-.2.2-.3.3-.5s0-.4 0-.5-.7-1.6-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.2.2 2.1 3.2 5.1 4.5.7.3 1.3.5 1.7.6.7.2 1.4.2 1.9.1.6-.1 1.7-.7 2-1.4.2-.7.2-1.3.2-1.4-.1-.2-.3-.3-.6-.4z"/><path d="M12 2C6.5 2 2 6.5 2 12c0 1.8.5 3.4 1.3 4.9L2 22l5.3-1.4c1.4.8 3 1.2 4.7 1.2 5.5 0 10-4.5 10-10S17.5 2 12 2zm0 18.2c-1.5 0-3-.4-4.3-1.2l-.3-.2-3.1.8.8-3-.2-.3C4.1 15 3.7 13.5 3.7 12 3.7 7.4 7.4 3.7 12 3.7S20.3 7.4 20.3 12 16.6 20.2 12 20.2z"/></svg>
  </a>
  <a href="tel:{b['phone2_href']}" aria-label="Позвонить">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.4 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.5c.9.4 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></svg>
  </a>
</div>
"""
