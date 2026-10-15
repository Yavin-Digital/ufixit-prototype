/* U-FIX-IT prototype storefront. Mock only: no real payments, data in localStorage. */
(function(){
var CFG={freeShip:75,freeShipIsPlaceholder:true};
var K='ufx_cart',O='ufx_orders';
function get(k,d){try{return JSON.parse(localStorage.getItem(k))||d}catch(e){return d}}
function set(k,v){localStorage.setItem(k,JSON.stringify(v))}
function money(c){return '$'+(c/100).toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g,',')}
function cart(){return get(K,[])}
function count(){return cart().reduce(function(a,l){return a+l.q},0)}
function paint(){var n=count();document.querySelectorAll('.cartcount').forEach(function(e){e.textContent=n})}
function add(it,q){var c=cart(),f=c.find(function(l){return l.id==it.id});if(f)f.q+=q;else c.push({id:+it.id,q:q,n:it.n,p:+it.p,i:it.i,u:it.u,s:it.s});set(K,c);paint();toast(it.n,q)}
function toast(n,q){var t=document.querySelector('.toast');if(!t){t=document.createElement('div');t.className='toast';t.setAttribute('role','status');document.body.appendChild(t)}
t.innerHTML='<span>Added '+(q>1?q+' x ':'')+'to cart</span><a href="cart.html">View cart &amp; checkout</a>';t.classList.add('on');clearTimeout(t._h);t._h=setTimeout(function(){t.classList.remove('on')},4200)}
window.UFXrun=null;window.UFX={cart:cart,set:function(c){set(K,c);paint()},money:money,CFG:CFG,orders:function(){return get(O,[])},saveOrder:function(o){var a=get(O,[]);a.unshift(o);set(O,a)},clear:function(){set(K,[]);paint()},add:add};
document.addEventListener('click',function(e){var b=e.target.closest('[data-add]');if(!b)return;e.preventDefault();var q=1,qi=document.querySelector(b.getAttribute('data-qty')||'#none');if(qi)q=Math.max(1,parseInt(qi.value)||1);add(b.dataset,q);
if(b.dataset.also){b.dataset.also.split(',').forEach(function(id){var x=document.querySelector('[data-add][data-id="'+id+'"]');if(x)add(x.dataset,1)})}});
document.addEventListener('submit',function(e){var f=e.target;if(f.matches('.js-capture')){e.preventDefault();f.innerHTML='<p style="margin:0;font:600 1rem system-ui">Thanks. You are on the list (prototype: nothing was sent).</p>'}});
/* shop filters */
var shop=document.querySelector('[data-shop]');
if(shop){var cards=[].slice.call(shop.querySelectorAll('.card')),grid=shop.querySelector('.grid'),F=document.querySelector('.filters'),cnt=document.querySelector('[data-count]'),srt=document.querySelector('[data-sort]'),qs=new URLSearchParams(location.search),qin=document.querySelector('[data-q]');
if(qs.get('q')&&qin)qin.value=qs.get('q');
function run(){var q=(qin&&qin.value||'').toLowerCase().trim(),cs=[].map.call(F.querySelectorAll('[name=cat]:checked'),function(i){return i.value}),bs=[].map.call(F.querySelectorAll('[name=brand]:checked'),function(i){return i.value}),mn=parseFloat(F.querySelector('[name=min]').value)*100||0,mx=parseFloat(F.querySelector('[name=max]').value)*100||1e12,n=0,st=localStorage.getItem('ufx_store')||'',ms=F.querySelector('[name=mystock]'),only=ms&&ms.checked&&st&&st!='ship';
cards.forEach(function(c){var ok=(!q||c.dataset.t.indexOf(q)>-1)&&(!cs.length||cs.indexOf(c.dataset.cat)>-1)&&(!bs.length||bs.indexOf(c.dataset.brand)>-1)&&(+c.dataset.p>=mn&&+c.dataset.p<=mx)&&(!only||(','+c.dataset.stores+',').indexOf(','+st+',')>-1);c.hidden=!ok;if(ok)n++});
if(cnt)cnt.textContent=n;var s=srt.value,arr=cards.slice();if(s!='pop')arr.sort(function(a,b){return s=='lo'?a.dataset.p-b.dataset.p:s=='hi'?b.dataset.p-a.dataset.p:a.dataset.n.localeCompare(b.dataset.n)});else arr.sort(function(a,b){return a.dataset.r-b.dataset.r});arr.forEach(function(c){grid.appendChild(c)});
var em=document.querySelector('[data-empty]');if(em)em.hidden=n>0}
F.addEventListener('input',run);window.UFXrun=run;srt.addEventListener('change',run);if(qin)qin.addEventListener('input',run);
var tg=document.querySelector('.filter-toggle');if(qs.get('q'))run();
var cl=F.querySelector('[data-clear]');if(cl)cl.addEventListener('click',function(){F.querySelectorAll('input[type=checkbox]').forEach(function(i){i.checked=false});F.querySelectorAll('input[type=number]').forEach(function(i){i.value=''});if(qin)qin.value='';run()});if(tg)tg.addEventListener('click',function(){var o=F.classList.toggle('open');tg.setAttribute('aria-expanded',o)});run()}
/* gallery */
document.querySelectorAll('.thumbs button').forEach(function(b){b.addEventListener('click',function(){var m=document.querySelector('.gal-main img');m.src=b.dataset.src;b.parentNode.querySelectorAll('button').forEach(function(x){x.setAttribute('aria-current',x==b)})})});
document.querySelectorAll('.qty').forEach(function(q){var i=q.querySelector('input');q.querySelectorAll('button').forEach(function(b){b.addEventListener('click',function(){i.value=Math.max(1,(parseInt(i.value)||1)+(+b.dataset.d))})})});
var sb=document.querySelector('.search-btn');if(sb)sb.addEventListener('click',function(){var h=document.querySelector('.sh'),o=h.classList.toggle('search-open');sb.setAttribute('aria-expanded',o);if(o)h.querySelector('.sh__search input').focus()});
var hq=document.getElementById('hq'),q0=new URLSearchParams(location.search).get('q');if(hq&&q0)hq.value=q0;
function placeBanner(){var b=document.getElementById('proto-banner');if(!b)return;var m=matchMedia('(max-width:820px), (max-height:500px) and (orientation:landscape)').matches;if(m&&b.nextElementSibling){document.body.appendChild(b)}}
placeBanner();

/* store-first: real locations; coords approximate (geocoded from street address) */
var STORES=[{n:'Arlington',ph:'817.472.7740',a:'4621 S Cooper St Suite 127, Arlington, TX 76017',lat:32.6788,lng:-97.1128},{n:'East Dallas',ph:'214.321.7054',a:'9919 Garland Rd, Dallas, TX 75218',lat:32.8517,lng:-96.6958},{n:'South Dallas',ph:'972.780.9096',a:'442 East Wheatland Rd, Duncanville, TX',lat:32.6467,lng:-96.9010},{n:'Tyler',ph:'903.592.5836',a:'2606 E 5th St, Tyler, TX 75701',lat:32.3337,lng:-95.2707}];
function myStore(){return localStorage.getItem('ufx_store')||''}
function setStore(n){localStorage.setItem('ufx_store',n);paintStore()}
function paintStore(){var m=myStore(),lbl=m=='ship'?'Ship to me':(m||'Pick a store');document.querySelectorAll('[data-mystore]').forEach(function(e){e.textContent=lbl});document.querySelectorAll('.mystore').forEach(function(b){b.classList.toggle('set',!!m);b.setAttribute('aria-haspopup','dialog');b.setAttribute('aria-label',m?'My store: '+lbl+'. Change store':'Pick a store')});var ms=document.querySelector('[name=mystock]');if(ms){ms.disabled=!m||m=='ship';if(ms.disabled)ms.checked=false}
document.querySelectorAll('.pick').forEach(function(b){b.setAttribute('aria-pressed',b.dataset.store==m)});
document.querySelectorAll('[data-loc-filter] input').forEach(function(i){i.checked=i.value==(m||'')});
var av=document.querySelector('[data-avail]');if(av){var on=av.dataset.online=='1',ss=(av.dataset.stores||'').split(',');av.innerHTML='<p class="avail-h">Pick up or ship <span class="ph">store stock: placeholder</span></p><button type="button" class="row'+(m=='ship'?' me':'')+'" data-setstore="ship"><span>Ship to me</span><em>'+(on?'In stock online · ships same day by 3 pm CST':'Order online, we’ll get it')+'</em></button>'+STORES.map(function(s){var ok=ss.indexOf(s.n)>-1;return '<button type="button" class="row'+(s.n==m?' me':'')+'" data-setstore="'+s.n+'"><span>Pickup: '+s.n+(s.n==m?' (my store)':'')+'</span><em class="'+(ok?'ok':'')+'">'+(ok?'Available for pickup':'Order for pickup')+'</em></button>'}).join('')+'<p class="avail-note">Tap a store to make it yours. Questions? Call <a class="tap" href="tel:8174727740">817.472.7740</a></p>'}}
function km(a,b,c,d){var r=Math.PI/180,x=(d-b)*r*Math.cos((a+c)/2*r),y=(c-a)*r;return Math.sqrt(x*x+y*y)*6371}
document.addEventListener('click',function(e){var ss=e.target.closest('[data-setstore]');if(ss){setStore(ss.dataset.setstore);return}var b=e.target.closest('.pick');if(b){setStore(b.dataset.store);var g=document.querySelector('[data-geo-msg]');if(g)g.innerHTML='Shopping <strong>'+b.dataset.store+'</strong>. <a href="shop.html">Shop parts</a>';closeDlg();return}
if(e.target.closest('[data-pick-store]')){openDlg();return}
if(e.target.closest('[data-geo]')){var msg=document.querySelector('[data-geo-msg]');if(!navigator.geolocation){msg.textContent='Location not available. Pick a store above.';return}msg.textContent='Finding your nearest store…';
navigator.geolocation.getCurrentPosition(function(p){var best=STORES.map(function(s){return [km(p.coords.latitude,p.coords.longitude,s.lat,s.lng),s]}).sort(function(a,b){return a[0]-b[0]})[0];setStore(best[1].n);msg.innerHTML='Nearest store: <strong>'+best[1].n+'</strong> (about '+Math.round(best[0]*0.621)+' mi). <a href="shop.html">Shop parts</a>'},function(){msg.textContent='Couldn’t get your location. Pick a store above.'},{timeout:8000})}});
function openDlg(){var d=document.getElementById('storedlg');if(!d){d=document.createElement('dialog');d.id='storedlg';d.setAttribute('aria-labelledby','dlg-h');d.innerHTML='<div class="picker" style="margin:0"><button type="button" class="dlg-x" aria-label="Close store picker" onclick="this.closest(\'dialog\').close()">×</button><p class="pick-h" id="dlg-h">Pick your store</p><div class="pick-grid">'+STORES.map(function(s){return '<button type="button" class="pick" data-store="'+s.n+'"><strong>'+s.n+'</strong><span>'+s.a.split(',')[0]+' · '+s.ph+'</span></button>'}).join('')+'</div><p class="pick-alt"><button type="button" class="pick" data-store="ship" style="width:100%"><strong>Ship to me</strong><span>Shop the whole store, shipped</span></button></p><p style="text-align:right;margin:10px 0 0"><button type="button" class="btn-ghost" onclick="this.closest(\'dialog\').close()">Close</button></p></div>';d.style.cssText='border:0;padding:0;max-width:min(640px,calc(100vw - 24px));width:calc(100vw - 24px)';document.body.appendChild(d)}d.showModal();paintStore()}
function closeDlg(){var d=document.getElementById('storedlg');if(d&&d.open)d.close()}
var lf=document.querySelector('[data-loc-filter]');if(lf){lf.innerHTML=STORES.map(function(s){return '<label><input type="radio" name="loc" value="'+s.n+'"> '+s.n+'</label>'}).join('')+'<label><input type="radio" name="loc" value="ship"> Ship to me (whole store)</label>';lf.addEventListener('change',function(e){setStore(e.target.value);var ms=document.querySelector('[name=mystock]');if(ms&&e.target.value!='ship'){ms.checked=true}if(window.UFXrun)UFXrun()})}
var qst=new URLSearchParams(location.search).get('store');if(qst)setStore(qst);
paintStore();

document.addEventListener('keydown',function(e){if(e.key!=='Escape')return;var h=document.querySelector('.sh.search-open');if(h){h.classList.remove('search-open');var b=document.querySelector('.search-btn');b.setAttribute('aria-expanded','false');b.focus()}var F2=document.querySelector('.filters.open');if(F2){F2.classList.remove('open');var t=document.querySelector('.filter-toggle');t.setAttribute('aria-expanded','false');t.focus()}});
(function(){var g=document.querySelector('.gal-main'),th=[].slice.call(document.querySelectorAll('.thumbs button'));if(!g||th.length<2)return;var x0=null;
function go(dx){if(Math.abs(dx)<40)return;var i=th.findIndex(function(b){return b.getAttribute('aria-current')=='true'});if(i<0)i=0;i=(i+(dx<0?1:-1)+th.length)%th.length;th[i].click()}
g.addEventListener('touchstart',function(e){x0=e.touches[0].clientX},{passive:true});g.addEventListener('touchend',function(e){if(x0===null)return;var d=e.changedTouches[0].clientX-x0;x0=null;go(d)},{passive:true});
var p0=null;g.addEventListener('pointerdown',function(e){if(e.pointerType!='mouse')p0=e.clientX});g.addEventListener('pointerup',function(e){if(p0===null||x0!==null)return;var d=e.clientX-p0;p0=null;go(d)});g.addEventListener('pointercancel',function(){p0=null});
g.addEventListener('dragstart',function(e){e.preventDefault()});g.setAttribute('aria-roledescription','swipeable gallery')})();
paint();
})();
