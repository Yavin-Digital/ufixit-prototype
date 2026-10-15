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
window.UFX={cart:cart,set:function(c){set(K,c);paint()},money:money,CFG:CFG,orders:function(){return get(O,[])},saveOrder:function(o){var a=get(O,[]);a.unshift(o);set(O,a)},clear:function(){set(K,[]);paint()},add:add};
document.addEventListener('click',function(e){var b=e.target.closest('[data-add]');if(!b)return;e.preventDefault();var q=1,qi=document.querySelector(b.getAttribute('data-qty')||'#none');if(qi)q=Math.max(1,parseInt(qi.value)||1);add(b.dataset,q);
if(b.dataset.also){b.dataset.also.split(',').forEach(function(id){var x=document.querySelector('[data-add][data-id="'+id+'"]');if(x)add(x.dataset,1)})}});
document.addEventListener('submit',function(e){var f=e.target;if(f.matches('.js-capture')){e.preventDefault();f.innerHTML='<p style="margin:0;font:600 1rem system-ui">Thanks. You are on the list (prototype: nothing was sent).</p>'}});
/* shop filters */
var shop=document.querySelector('[data-shop]');
if(shop){var cards=[].slice.call(shop.querySelectorAll('.card')),grid=shop.querySelector('.grid'),F=document.querySelector('.filters'),cnt=document.querySelector('[data-count]'),srt=document.querySelector('[data-sort]'),qs=new URLSearchParams(location.search),qin=document.querySelector('[data-q]');
if(qs.get('q')&&qin)qin.value=qs.get('q');
function run(){var q=(qin&&qin.value||'').toLowerCase().trim(),cs=[].map.call(F.querySelectorAll('[name=cat]:checked'),function(i){return i.value}),bs=[].map.call(F.querySelectorAll('[name=brand]:checked'),function(i){return i.value}),mn=parseFloat(F.querySelector('[name=min]').value)*100||0,mx=parseFloat(F.querySelector('[name=max]').value)*100||1e12,n=0;
cards.forEach(function(c){var ok=(!q||c.dataset.t.indexOf(q)>-1)&&(!cs.length||cs.indexOf(c.dataset.cat)>-1)&&(!bs.length||bs.indexOf(c.dataset.brand)>-1)&&(+c.dataset.p>=mn&&+c.dataset.p<=mx);c.hidden=!ok;if(ok)n++});
if(cnt)cnt.textContent=n;var s=srt.value,arr=cards.slice();if(s!='pop')arr.sort(function(a,b){return s=='lo'?a.dataset.p-b.dataset.p:s=='hi'?b.dataset.p-a.dataset.p:a.dataset.n.localeCompare(b.dataset.n)});else arr.sort(function(a,b){return a.dataset.r-b.dataset.r});arr.forEach(function(c){grid.appendChild(c)});
var em=document.querySelector('[data-empty]');if(em)em.hidden=n>0}
F.addEventListener('input',run);srt.addEventListener('change',run);if(qin)qin.addEventListener('input',run);
var tg=document.querySelector('.filter-toggle');if(tg)tg.addEventListener('click',function(){F.classList.toggle('open')});run()}
/* gallery */
document.querySelectorAll('.thumbs button').forEach(function(b){b.addEventListener('click',function(){var m=document.querySelector('.gal-main img');m.src=b.dataset.src;b.parentNode.querySelectorAll('button').forEach(function(x){x.setAttribute('aria-current',x==b)})})});
document.querySelectorAll('.qty').forEach(function(q){var i=q.querySelector('input');q.querySelectorAll('button').forEach(function(b){b.addEventListener('click',function(){i.value=Math.max(1,(parseInt(i.value)||1)+(+b.dataset.d))})})});
paint();
})();
