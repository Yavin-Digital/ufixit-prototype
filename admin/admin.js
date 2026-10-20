/* U-FIX-IT demo admin UI. Demo data only (data.js). No backend, nothing is saved. */
(function(){
var D=window.UFX_DEMO, page=document.body.getAttribute('data-page'), KEY='ufx_admin_demo';
if(page!=='signin'&&!sessionStorage.getItem(KEY)){location.replace('index.html');return}
function $(s,r){return (r||document).querySelector(s)}
function esc(s){return String(s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
function money(c,dec){var v=c/100;return '$'+(dec===0?Math.round(v).toLocaleString('en-US'):v.toLocaleString('en-US',{minimumFractionDigits:2,maximumFractionDigits:2}))}
function short$(c){var v=c/100;return v>=1e6?'$'+(v/1e6).toFixed(1)+'M':v>=1e3?'$'+(v/1e3).toFixed(v>=1e4?0:1)+'k':'$'+Math.round(v)}
function num(n){return n.toLocaleString('en-US')}
var fmtD=new Intl.DateTimeFormat('en-US',{timeZone:'UTC',month:'short',day:'numeric',year:'numeric'});
var fmtDT=new Intl.DateTimeFormat('en-US',{timeZone:'UTC',month:'short',day:'numeric',year:'numeric',hour:'numeric',minute:'2-digit'});
function d(t){return fmtD.format(new Date(t))}
function iso(t){return new Date(t).toISOString().slice(0,10)}
function parseISO(s){var m=/^(\d{4})-(\d{2})-(\d{2})$/.exec(s);return m?Date.UTC(+m[1],m[2]-1,+m[3]):null}
function stCls(s){return s=='Refunded'||s=='Cancelled'?'st-bad':s=='Processing'||s=='Ready for pickup'?'st-warn':s=='Shipped'?'st-info':'st-ok'}
function stockLbl(p){return p.stock==0?'<span class="st st-bad">Out of stock</span>':p.stock<=p.reorder?'<span class="st st-warn">Low: '+p.stock+'</span>':'<span class="st st-ok">'+p.stock+' on hand</span>'}
function toast(m){var t=$('.toast');if(!t){t=document.createElement('div');t.className='toast';t.setAttribute('role','status');document.body.appendChild(t)}t.textContent=m;t.hidden=false;clearTimeout(t._h);t._h=setTimeout(function(){t.hidden=true},4000)}
var so=$('#signout');if(so)so.addEventListener('click',function(){sessionStorage.removeItem(KEY);location.href='index.html'});

/* aggregation */
function inRange(a,b,ch){return D.orders.filter(function(o){return o.t>=a&&o.t<b+D.DAY&&(!ch||o.ch==ch)})}
function sum(os){var r={sales:0,orders:0,units:0,refunds:0};os.forEach(function(o){if(D.counted(o)){r.sales+=o.sub;r.orders++;o.lines.forEach(function(l){r.units+=l.qty})}else if(o.status=='Refunded')r.refunds+=o.sub});r.aov=r.orders?Math.round(r.sales/r.orders):0;return r}
function prodStats(os){var m={};os.forEach(function(o){if(!D.counted(o))return;o.lines.forEach(function(l){var x=m[l.id]||(m[l.id]={id:l.id,units:0,rev:0,orders:0});x.units+=l.qty;x.rev+=l.qty*l.price;x.orders++})});return Object.keys(m).map(function(k){return m[k]})}
function catStats(os){var m={};prodStats(os).forEach(function(s){var c=D.productById[s.id].cat,x=m[c]||(m[c]={cat:c,units:0,rev:0});x.units+=s.units;x.rev+=s.rev});return Object.keys(m).map(function(k){return m[k]}).sort(function(a,b){return b.rev-a.rev})}
function bucket(os,a,b){var span=(b-a)/D.DAY+1,g=span<=45?'day':span<=200?'week':'month',m={},keys=[];
  function key(t){var x=new Date(t),day=Date.UTC(x.getUTCFullYear(),x.getUTCMonth(),x.getUTCDate());if(g=='day')return day;if(g=='week')return b-6*D.DAY-7*D.DAY*Math.floor((b-day)/(7*D.DAY));return Date.UTC(x.getUTCFullYear(),x.getUTCMonth(),1)}
  function next(t){var x=new Date(t);return g=='day'?t+D.DAY:g=='week'?t+7*D.DAY:Date.UTC(x.getUTCFullYear(),x.getUTCMonth()+1,1)}
  for(var t=key(a);t<=b;t=next(t)){keys.push(t);m[t]={t:t,sales:0,orders:0,partial:g!='day'&&(t<a||next(t)-D.DAY>b)}}
  os.forEach(function(o){if(!D.counted(o))return;var k=key(o.t);if(m[k]){m[k].sales+=o.sub;m[k].orders++}});
  return {g:g,rows:keys.map(function(k){return m[k]})}}
var fmtM=new Intl.DateTimeFormat('en-US',{timeZone:'UTC',month:'short',year:'2-digit'}),fmtMD=new Intl.DateTimeFormat('en-US',{timeZone:'UTC',month:'short',day:'numeric'});
function bLabel(t,g){return g=='month'?fmtM.format(new Date(t)):fmtMD.format(new Date(t))}
function nice(max,n){var raw=max/n,p=Math.pow(10,Math.floor(Math.log10(raw||1))),st=[1,2,2.5,5,10].map(function(x){return x*p}).find(function(x){return x>=raw});return st*n}

/* SVG revenue chart: bars = net sales, line = orders */
function chart(el,bk,h){h=h||260;var rows=bk.rows,W=Math.max(300,Math.min(1100,el.clientWidth||760)),H=W<600?Math.round(h*.95):h,pl=58,pr=44,pt=14,pb=34,iw=W-pl-pr,ih=H-pt-pb;
  var top=nice(Math.max.apply(null,rows.map(function(r){return r.sales/100}).concat([1])),4)*100,otop=nice(Math.max.apply(null,rows.map(function(r){return r.orders}).concat([4])),4);
  var bw=iw/rows.length,s='<svg viewBox="0 0 '+W+' '+H+'" role="img" aria-label="Net sales and order count by '+bk.g+'. Data table below."><g>',anyP=false;
  for(var i=0;i<=4;i++){var y=pt+ih-ih*i/4;s+='<line x1="'+pl+'" x2="'+(W-pr)+'" y1="'+y+'" y2="'+y+'" stroke="#e6e6e6"/><text x="'+(pl-6)+'" y="'+(y+5)+'" text-anchor="end">'+short$(top*i/4)+'</text><text x="'+(W-pr+6)+'" y="'+(y+5)+'" fill="#b00000" style="fill:#b00000">'+num(Math.round(otop*i/4))+'</text>'}
  var lbEvery=Math.ceil(rows.length/(W<600?4:8)),pts=[];
  rows.forEach(function(r,i){var bh=ih*r.sales/top,x=pl+i*bw;if(r.partial)anyP=true;s+='<rect x="'+(x+bw*.12).toFixed(1)+'" y="'+(pt+ih-bh).toFixed(1)+'" width="'+Math.max(1,bw*.76).toFixed(1)+'" height="'+bh.toFixed(1)+'" fill="'+(r.partial?'url(#hatch)':'#1C1D76')+'"'+(r.partial?' stroke="#1C1D76" stroke-width="1.5"':'')+'><title>'+bLabel(r.t,bk.g)+(r.partial?' (partial)':'')+': '+money(r.sales)+', '+r.orders+' orders</title></rect>';
    pts.push((x+bw/2).toFixed(1)+','+(pt+ih-ih*r.orders/otop).toFixed(1));
    if(i%lbEvery==0)s+='<text x="'+(x+bw/2)+'" y="'+(H-10)+'" text-anchor="middle">'+bLabel(r.t,bk.g)+'</text>'});
  s='<svg'+s.slice(4).replace('<g>','<defs><pattern id="hatch" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="6" height="6" fill="#c9c9e3"/><line x1="0" y1="0" x2="0" y2="6" stroke="#1C1D76" stroke-width="2"/></pattern></defs><g>');
  s+='<polyline points="'+pts.join(' ')+'" fill="none" stroke="#F50A0A" stroke-width="2.5"/></g></svg>';
  el.innerHTML='<div class="chart">'+s+'</div><p class="legend"><span aria-hidden="true" class="sw"></span> Net sales (left axis) &nbsp; <span aria-hidden="true" class="sw ln"></span> Orders (right axis, count)'+(anyP?' &nbsp; <span aria-hidden="true" class="sw hat"></span> Partial '+bk.g+' (range starts or ends mid-'+bk.g+')':'')+' &nbsp;·&nbsp; by '+bk.g+' · demo data</p>'}

function pager(el,items,size,row,head,cls){cls=cls||'cards';var pg=0;function draw(){var n=Math.max(1,Math.ceil(items.length/size));pg=Math.min(pg,n-1);var sl=items.slice(pg*size,pg*size+size);
  el.innerHTML=items.length?'<div class="tw"><table class="t '+cls+'"><thead><tr>'+head+'</tr></thead><tbody>'+sl.map(row).join('')+'</tbody></table></div><div class="pager"><button class="btn-ghost" data-p="-1"'+(pg?'':' disabled')+'>Previous</button><span>Page '+(pg+1)+' of '+n+' · '+num(items.length)+' rows</span><button class="btn-ghost" data-p="1"'+(pg<n-1?'':' disabled')+'>Next</button></div>':'<p class="empty">No matching rows.</p>';
  el.querySelectorAll('[data-p]').forEach(function(b){b.onclick=function(){pg+=+b.getAttribute('data-p');draw();el.scrollIntoView({block:'start'})}})}
  draw();return {set:function(x){items=x;pg=0;draw()}}}
function custName(id){var c=D.customerById[id];return c?c.name:'Guest'}
function orderRow(o){var u=o.lines.reduce(function(a,l){return a+l.qty},0);return '<tr><td data-l="Order" class="c-no"><button class="lnk" data-o="'+o.no+'">'+o.no+'</button></td><td data-l="Date" class="c-dt">'+d(o.t)+'</td><td data-l="Customer" class="c-cu">'+esc(custName(o.cust))+'</td><td data-l="Channel" class="c-ch">'+o.ch+'</td><td data-l="Items" class="num c-it">'+u+'</td><td data-l="Total" class="num c-tot">'+money(o.total)+'</td><td data-l="Status" class="c-st"><span class="st '+stCls(o.status)+'">'+o.status+'</span></td></tr>'}
var orderHead='<th class="c-no">Order</th><th class="c-dt">Date</th><th class="c-cu">Customer</th><th class="c-ch">Channel</th><th class="num c-it">Items</th><th class="num c-tot">Total</th><th class="c-st">Status</th>';
var oIdx={};D.orders.forEach(function(o){oIdx[o.no]=o});
document.addEventListener('click',function(e){var b=e.target.closest('[data-o]');if(!b)return;var o=oIdx[b.getAttribute('data-o')],c=D.customerById[o.cust];
  var dl=$('#odlg');if(!dl){dl=document.createElement('dialog');dl.id='odlg';dl.setAttribute('aria-labelledby','odlg-h');document.body.appendChild(dl)}
  dl.innerHTML='<div class="panel"><h2 id="odlg-h">Order '+o.no+' <span class="tag-demo">Demo</span></h2><dl class="dl"><dt>Placed</dt><dd>'+fmtDT.format(new Date(o.t))+'</dd><dt>Customer</dt><dd>'+esc(c.name)+'<br>'+esc(c.email)+'</dd><dt>Channel</dt><dd>'+o.ch+(o.ch=='Online'?' (ships)':' (store pickup / counter)')+'</dd><dt>Payment</dt><dd>'+o.pay+'</dd><dt>Status</dt><dd><span class="st '+stCls(o.status)+'">'+o.status+'</span></dd></dl>'+
  '<table class="t cards"><thead><tr><th>Part</th><th class="num">Qty</th><th class="num">Price</th></tr></thead><tbody>'+o.lines.map(function(l){var p=D.productById[l.id];return '<tr><td data-l="Part" class="full">'+esc(p.name)+'<br><small>Part # '+esc(p.sku)+'</small></td><td data-l="Qty" class="num">'+l.qty+'</td><td data-l="Price" class="num">'+money(l.price)+'</td></tr>'}).join('')+'</tbody></table>'+
  '<dl class="dl" style="margin-top:12px"><dt>Subtotal</dt><dd>'+money(o.sub)+'</dd><dt>Shipping</dt><dd>'+money(o.ship)+'</dd><dt>Tax (8.25%)</dt><dd>'+money(o.tax)+'</dd><dt><b>Total</b></dt><dd><b>'+money(o.total)+'</b></dd></dl><button class="btn" id="odlg-x">Close</button></div>';
  dl.showModal();$('#odlg-x').focus();$('#odlg-x').onclick=function(){dl.close()};
  dl.onclose=function(){b.focus()}});

function rankList(stats,by,n){var top=stats.slice().sort(function(a,b){return b[by]-a[by]}).slice(0,n),mx=top.length?top[0][by]:1;
  return top.length?'<ol class="rank">'+top.map(function(s){var p=D.productById[s.id];return '<li><span class="nm"><a href="'+p.url+'">'+esc(p.name)+'</a><small>'+esc(p.cat)+' · Part # '+esc(p.sku)+'</small></span><span class="v">'+(by=='units'?num(s.units)+' units':money(s.rev,0))+'<small>'+(by=='units'?money(s.rev,0):num(s.units)+' units')+'</small></span><span class="bar" aria-hidden="true"><i style="width:'+(100*s[by]/mx).toFixed(1)+'%"></i></span></li>'}).join('')+'</ol>':'<p class="empty">No sales in this range.</p>'}
function catBars(cs){var tot=cs.reduce(function(a,c){return a+c.rev},0)||1;return '<ul class="hbars">'+cs.map(function(c){return '<li><div class="r"><b>'+esc(c.cat)+'</b><span>'+money(c.rev,0)+' · '+(100*c.rev/tot).toFixed(1)+'% · '+num(c.units)+' units</span></div><div class="bar" aria-hidden="true"><i style="width:'+(100*c.rev/cs[0].rev).toFixed(1)+'%"></i></div></li>'}).join('')+'</ul>'}
function kpis(el,cur,prev){function ch(a,b){if(!b)return '';var p=(a-b)/b*100;return ' <span class="'+(p>=0?'up':'dn')+'">'+(p>=0?'▲ ':'▼ ')+Math.abs(p).toFixed(1)+'%</span>'}
  el.innerHTML=[['Net sales',money(cur.sales,0),ch(cur.sales,prev&&prev.sales)],['Orders',num(cur.orders),ch(cur.orders,prev&&prev.orders)],['Avg order',money(cur.aov),ch(cur.aov,prev&&prev.aov)],['Units sold',num(cur.units),ch(cur.units,prev&&prev.units)]].map(function(k){return '<div class="kpi"><span>'+k[0]+'</span><b>'+k[1]+'</b><span>'+(prev?'vs prior period'+k[2]:'demo data')+'</span></div>'}).join('')}

var R={};
R.signin=function(){$('#sf').addEventListener('submit',function(e){e.preventDefault();sessionStorage.setItem(KEY,'1');location.href='dashboard.html'})};
R.dashboard=function(){var a=D.END-29*D.DAY,cur=inRange(a,D.END),prev=inRange(a-30*D.DAY,a-D.DAY);
  kpis($('#kpis'),sum(cur),sum(prev));chart($('#ch'),bucket(cur,a,D.END),240);
  $('#recent').innerHTML='<div class="tw"><table class="t cards orders"><thead><tr>'+orderHead+'</tr></thead><tbody>'+D.orders.slice(0,8).map(orderRow).join('')+'</tbody></table></div>';
  $('#top5').innerHTML=rankList(prodStats(cur),'rev',5);
  var low=D.products.filter(function(p){return p.stock<=p.reorder}).sort(function(a,b){return a.stock-b.stock}).slice(0,6);
  $('#low').innerHTML='<ul class="hbars">'+low.map(function(p){return '<li><div class="r"><span>'+esc(p.name)+'</span>'+stockLbl(p)+'</div></li>'}).join('')+'</ul>';
  var open=D.orders.filter(function(o){return o.status=='Processing'||o.status=='Ready for pickup'}).length;$('#open').textContent=open};
R.orders=function(){var q=$('#q'),s=$('#fs'),c=$('#fc'),p=pager($('#list'),D.orders,25,orderRow,orderHead,'cards orders');
  function f(){var t=q.value.trim().toLowerCase();p.set(D.orders.filter(function(o){return(!s.value||o.status==s.value)&&(!c.value||o.ch==c.value)&&(!t||o.no.toLowerCase().indexOf(t)>-1||custName(o.cust).toLowerCase().indexOf(t)>-1)}))}
  [q,s,c].forEach(function(x){x.addEventListener('input',f)})};
R.products=function(){var since=D.END-89*D.DAY,ps={};prodStats(inRange(since,D.END)).forEach(function(x){ps[x.id]=x});
  var cats=[];D.products.forEach(function(p){if(cats.indexOf(p.cat)<0)cats.push(p.cat)});$('#fcat').innerHTML+=cats.sort().map(function(c){return '<option>'+esc(c)+'</option>'}).join('');
  function row(p){var s=ps[p.id];return '<tr><td data-l="Image"><img src="'+p.img+'" alt="" loading="lazy" width="48" height="48"></td><td data-l="Part" class="full"><a href="'+p.url+'">'+esc(p.name)+'</a><br><small>Part # '+esc(p.sku)+' · '+esc(p.brand)+'</small></td><td data-l="Category">'+esc(p.cat)+'</td><td data-l="Price" class="num">'+money(p.price)+'</td><td data-l="Stock">'+stockLbl(p)+'</td><td data-l="Sold (90 days)" class="num">'+(s?s.units:0)+'</td></tr>'}
  var pg=pager($('#list'),D.products,25,row,'<th><span class="sr">Image</span></th><th>Part</th><th>Category</th><th class="num">Price</th><th>Stock</th><th class="num">Sold 90d</th>');
  var q=$('#q'),fc=$('#fcat'),fs=$('#fst');function f(){var t=q.value.trim().toLowerCase();pg.set(D.products.filter(function(p){return(!fc.value||p.cat==fc.value)&&(!fs.value||(fs.value=='low'?p.stock>0&&p.stock<=p.reorder:p.stock==0))&&(!t||(p.name+' '+p.sku+' '+p.brand).toLowerCase().indexOf(t)>-1)}))}
  [q,fc,fs].forEach(function(x){x.addEventListener('input',f)});
  $('#inv').textContent=num(D.products.length)+' parts · '+D.products.filter(function(p){return p.stock>0&&p.stock<=p.reorder}).length+' low · '+D.products.filter(function(p){return p.stock==0}).length+' out of stock'};
R.customers=function(){var cs=D.customers.filter(function(c){return c.orders}).sort(function(a,b){return b.spend-a.spend});
  function row(c){return '<tr><td data-l="Customer" class="full"><b>'+esc(c.name)+'</b><br><small>'+esc(c.email)+'</small></td><td data-l="Type">'+c.type+'</td><td data-l="City">'+esc(c.city)+'</td><td data-l="Orders" class="num">'+c.orders+'</td><td data-l="Lifetime spend" class="num">'+money(c.spend)+'</td><td data-l="Last order">'+d(c.last)+'</td></tr>'}
  var pg=pager($('#list'),cs,25,row,'<th>Customer</th><th>Type</th><th>City</th><th class="num">Orders</th><th class="num">Spend</th><th>Last order</th>');
  var q=$('#q'),ft=$('#ft');function f(){var t=q.value.trim().toLowerCase();pg.set(cs.filter(function(c){return(!ft.value||c.type==ft.value)&&(!t||(c.name+' '+c.email+' '+c.city).toLowerCase().indexOf(t)>-1)}))}[q,ft].forEach(function(x){x.addEventListener('input',f)})};
R.reports=function(){var from=$('#from'),to=$('#to'),chs=$('#rch');from.min=to.min=iso(D.START);from.max=to.max=iso(D.END);
  var by='units',last=null;
  function set(a,b){from.value=iso(a);to.value=iso(b);run()}
  document.querySelectorAll('[data-r]').forEach(function(b){b.onclick=function(){var r=b.getAttribute('data-r'),e=D.END,a;
    if(r=='ytd')a=Date.UTC(2026,0,1);else if(r=='all')a=D.START;else if(r=='ly')a=Date.UTC(2025,0,1),e=Date.UTC(2025,11,31);else a=e-(+r-1)*D.DAY;
    document.querySelectorAll('[data-r]').forEach(function(x){x.setAttribute('aria-pressed',x===b)});set(a,e)}});
  [from,to,chs].forEach(function(x){x.addEventListener('change',function(){if(x!==chs)document.querySelectorAll('[data-r]').forEach(function(y){y.setAttribute('aria-pressed','false')});run()})});
  document.querySelectorAll('[data-by]').forEach(function(b){b.onclick=function(){by=b.getAttribute('data-by');document.querySelectorAll('[data-by]').forEach(function(x){x.setAttribute('aria-pressed',x===b)});$('#rank').innerHTML=rankList(last.ps,by,10)}});
  var ol=pager($('#hist'),[],20,orderRow,orderHead,'cards orders');
  function run(){var a=parseISO(from.value),b=parseISO(to.value);if(a==null||b==null)return;if(a>b){var t=a;a=b;b=t}
    var os=inRange(a,b,chs.value),len=(b-a)/D.DAY+1,prev=a-len*D.DAY>=D.START?inRange(a-len*D.DAY,a-D.DAY,chs.value):null;
    var cur=sum(os);kpis($('#kpis'),cur,prev&&sum(prev));$('#rlbl').textContent=d(a)+' – '+d(b)+(chs.value?' · '+chs.value:' · All channels');
    var bk=bucket(os,a,b);chart($('#ch'),bk,280);
    $('#chtbl').innerHTML='<table class="t"><thead><tr><th>'+bk.g+'</th><th class="num">Net sales</th><th class="num">Orders</th></tr></thead><tbody>'+bk.rows.map(function(r){return '<tr><td>'+bLabel(r.t,bk.g)+(r.partial?' (partial)':'')+'</td><td class="num">'+money(r.sales)+'</td><td class="num">'+r.orders+'</td></tr>'}).join('')+'</tbody></table>';
    var ps=prodStats(os);last={ps:ps,os:os};$('#rank').innerHTML=rankList(ps,by,10);$('#cats').innerHTML=catBars(catStats(os));
    var cm={};os.forEach(function(o){if(!D.counted(o))return;var x=cm[o.ch]||(cm[o.ch]={cat:o.ch,rev:0,units:0});x.rev+=o.sub;o.lines.forEach(function(l){x.units+=l.qty})});
    $('#chan').innerHTML=catBars(Object.keys(cm).map(function(k){return cm[k]}).sort(function(x,y){return y.rev-x.rev}));
    $('#refunds').textContent=money(cur.refunds);ol.set(os)}
  $('#csv').onclick=function(){if(!last)return;var rows=[['order','date','customer','channel','status','items','subtotal','shipping','tax','total']].concat(last.os.map(function(o){return [o.no,iso(o.t),custName(o.cust),o.ch,o.status,o.lines.reduce(function(a,l){return a+l.qty},0),(o.sub/100).toFixed(2),(o.ship/100).toFixed(2),(o.tax/100).toFixed(2),(o.total/100).toFixed(2)]}));
    var blob=new Blob(['DEMO DATA - not real orders\n'+rows.map(function(r){return r.map(function(v){return '"'+String(v).replace(/"/g,'""')+'"'}).join(',')}).join('\n')],{type:'text/csv'}),u=URL.createObjectURL(blob),a=document.createElement('a');a.href=u;a.download='ufixit-demo-orders-'+from.value+'-to-'+to.value+'.csv';document.body.appendChild(a);a.click();a.remove();setTimeout(function(){URL.revokeObjectURL(u)},1000)};
  var rs=$('#rsel');rs.addEventListener('change',function(){if(rs.value)$('[data-r="'+rs.value+'"]').click()});
  document.querySelectorAll('[data-r]').forEach(function(b){b.addEventListener('click',function(){rs.value=b.getAttribute('data-r')})});
  [from,to].forEach(function(x){x.addEventListener('change',function(){rs.value=''})});
  $('[data-r="90"]').click()};
R.settings=function(){$('#setf').addEventListener('submit',function(e){e.preventDefault();toast('Demo only: settings are not saved.')})};
if(R[page])R[page]();
})();
