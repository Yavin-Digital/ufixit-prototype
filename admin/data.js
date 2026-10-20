/* U-FIX-IT DEMO ADMIN — DEMO DATA ONLY.
   Every order, customer and stock count below is generated in the browser from a fixed seed.
   Product names, part numbers and prices come from the prototype catalog (catalog.js).
   Nothing here is connected to a real store system. */
(function(){
var seed=20261013; // fixed demo seed
function rnd(){seed|=0;seed=seed+0x6D2B79F5|0;var t=Math.imul(seed^seed>>>15,1|seed);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296}
function pick(a){return a[Math.floor(rnd()*a.length)]}
var DAY=864e5;
var END=Date.UTC(2026,9,20), START=END-729*DAY; // 2 years of demo history, fixed dates
var CATS={'refrigerator-parts':'Refrigerator','washer-parts':'Washer','dryer-parts':'Dryer','range-oven-parts':'Range & Oven','dishwasher-parts':'Dishwasher','dishwasher-accessories':'Dishwasher','air-conditioner-parts':'Air Conditioner','furnace-parts':'Furnace','microwave-parts':'Microwave','accessories':'Accessories'};
var STORES=[{n:'Arlington',ph:'817.472.7740'},{n:'East Dallas',ph:'214.321.7054'},{n:'South Dallas',ph:'972.780.9096'},{n:'Tyler',ph:'903.592.5836'}];
var CHANNELS=['Online','Arlington','East Dallas','South Dallas','Tyler'], CHW=[.36,.2,.18,.14,.12];
var cat=(window.UFX_CATALOG||[]).filter(function(p){return p.p>0});
var products=cat.map(function(p){
  var r=rnd(), stock=p.st&&/Only (\d)/.test(p.st)?+RegExp.$1:(p.st?4+Math.floor(rnd()*22):0);
  if(rnd()<.04)stock=0;
  return {id:p.id,name:p.n,sku:p.sku,cat:CATS[p.c]||'Other',brand:p.b||'Universal',price:p.p,img:'../'+p.i,url:'../'+p.u,stock:stock,reorder:3,
    w:Math.pow(r,4)*(p.p<2500?3:p.p<8000?1.6:.8)+.02};
});
var tw=0,cum=[];products.forEach(function(p){tw+=p.w;cum.push(tw)});
function pickProduct(){var x=rnd()*tw,lo=0,hi=cum.length-1;while(lo<hi){var m=lo+hi>>1;if(cum[m]<x)lo=m+1;else hi=m}return products[lo]}
var FN=['James','Maria','Robert','Linda','Michael','Patricia','David','Jennifer','Carlos','Elizabeth','William','Ana','Richard','Susan','Jose','Karen','Thomas','Nancy','Daniel','Lisa','Anthony','Betty','Mark','Sandra','Luis','Ashley','Kevin','Donna','Brian','Emily','Juan','Michelle','Gary','Carol','Eric','Amanda','Tyrone','Melissa','Raymond','Deborah','Hector','Stephanie','Larry','Rebecca','Dennis','Laura','Jerry','Sharon','Tony','Cynthia'];
var LN=['Johnson','Garcia','Smith','Martinez','Brown','Hernandez','Davis','Lopez','Wilson','Gonzalez','Anderson','Perez','Thomas','Sanchez','Taylor','Ramirez','Moore','Torres','Jackson','Flores','White','Rivera','Harris','Nguyen','Clark','Lewis','Robinson','Walker','Young','Allen','King','Wright','Scott','Hill','Green','Adams','Baker','Nelson','Carter','Mitchell'];
var CITY={'Arlington':['Arlington','Grand Prairie','Mansfield','Fort Worth'],'East Dallas':['Dallas','Garland','Mesquite','Richardson'],'South Dallas':['Dallas','Duncanville','DeSoto','Lancaster'],'Tyler':['Tyler','Longview','Whitehouse','Lindale'],'Online':['Houston','San Antonio','Austin','Waco','Lubbock','Shreveport, LA','Oklahoma City, OK','El Paso','Denton','Plano']};
var customers=[],used={};
for(var i=0;i<420;i++){var f=pick(FN),l=pick(LN),k=f+l;used[k]=(used[k]||0)+1;var home=CHANNELS[Math.floor(rnd()*5)];
  var pro=rnd()<.12;
  customers.push({id:5000+i,name:f+' '+l,email:(f+'.'+l+(used[k]>1?used[k]:'')).toLowerCase()+'@example.com',phone:'(555) '+(100+Math.floor(rnd()*899))+'-'+(1000+Math.floor(rnd()*8999)),
    city:pick(CITY[home]),home:home,type:pro?'Repair tech':'DIY homeowner',since:0,orders:0,spend:0,last:0,w:pro?6:1})}
var cw=0,ccum=customers.map(function(c){return cw+=c.w});
function pickCustomer(){var x=rnd()*cw;for(var i=0;i<ccum.length;i++)if(ccum[i]>=x)return customers[i];return customers[0]}
function pickChannel(){var x=rnd(),a=0;for(var i=0;i<5;i++){a+=CHW[i];if(x<a)return CHANNELS[i]}return 'Online'}
var orders=[],n=104200;
for(var d=START;d<=END;d+=DAY){
  var dt=new Date(d),dow=dt.getUTCDay(),mo=dt.getUTCMonth(),age=(d-START)/(END-START);
  var summer=(mo>=4&&mo<=7)?1.2:(mo==11||mo==0)?1.1:1;
  var base=11*(1+.22*age)*summer*(dow==0?.35:dow==6?.8:1);
  var ramp=1+.22*Math.max(0,((d-START)/DAY-660)/69); // recent demo momentum
  var cnt=Math.max(0,Math.round(base*ramp*(.65+rnd()*.7)));
  for(var j=0;j<cnt;j++){
    var ch=dow==0?'Online':pickChannel(), cu=pickCustomer(), lines=[], nl=rnd()<.72?1:rnd()<.75?2:3, seen={};
    for(var q=0;q<nl;q++){var p=pickProduct();
      if((p.cat=='Refrigerator'||p.cat=='Air Conditioner')&&summer<1.2&&rnd()<.25)p=pickProduct();
      if(seen[p.id])continue;seen[p.id]=1;
      lines.push({id:p.id,qty:rnd()<.85?1:rnd()<.7?2:3,price:p.price})}
    var sub=lines.reduce(function(a,l){return a+l.qty*l.price},0);
    var ship=ch=='Online'?(sub>=7500?0:995):0, tax=Math.round(sub*.0825);
    var t=d+(8+Math.floor(rnd()*10))*36e5+Math.floor(rnd()*60)*6e4;
    var daysAgo=(END-d)/DAY, st;
    if(daysAgo<1)st=ch=='Online'?'Processing':pick(['Processing','Ready for pickup']);
    else if(daysAgo<4&&ch=='Online')st=pick(['Shipped','Shipped','Processing']);
    else {var r=rnd();st=r<.028?'Refunded':r<.038?'Cancelled':(ch=='Online'?'Delivered':'Picked up')}
    var o={no:'UFX-'+(++n),t:t,cust:cu.id,ch:ch,lines:lines,sub:sub,ship:ship,tax:tax,total:sub+ship+tax,status:st,pay:ch=='Online'?pick(['Card','Card','Card','PayPal']):pick(['Card','Card','Cash'])};
    orders.push(o);
    if(st!='Cancelled'&&st!='Refunded'){cu.orders++;cu.spend+=sub;if(!cu.since)cu.since=t;cu.last=t}
  }
}
orders.reverse(); // newest first
/* Parts extras (cost, supplier, reorder level, compatibility). Separate seed so order history stays identical. */
var s2=7741;function r2(){s2|=0;s2=s2+0x6D2B79F5|0;var t=Math.imul(s2^s2>>>15,1|s2);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296}
var SUP=['Lone Star Parts Supply (demo)','Gulf Coast Appliance Distributors (demo)','Red River OEM Parts (demo)','Trinity Wholesale Parts (demo)'];
var DEV={'Refrigerator':'refrigerators','Washer':'washers','Dryer':'dryers','Range & Oven':'ranges & ovens','Dishwasher':'dishwashers','Air Conditioner':'air conditioners','Furnace':'furnaces','Microwave':'microwaves','Accessories':'appliances'};
var srcById={};cat.forEach(function(c){srcById[c.id]=c});
products.forEach(function(p){var c=srcById[p.id];p.cost=Math.round(p.price*(.46+r2()*.16));p.supplier=SUP[Math.floor(r2()*SUP.length)];p.reorder=2+Math.floor(r2()*4);
  p.fits=(p.brand&&!/^(Universal|Other)$/i.test(p.brand)?p.brand+' ':'Universal fit ')+(DEV[p.cat]||'appliances');p.replaces=(c&&c.x)||[];p.leadDays=2+Math.floor(r2()*6);var q=r2();p.stock=q<.025?0:q<.1?1+Math.floor(r2()*p.reorder):p.reorder+1+Math.floor(r2()*20)});
/* POS sync log: in-store sales arrive from the POS provider; inventory counts sync back. */
var posLog=[];orders.forEach(function(o){if(o.ch!='Online'&&o.t>END-3*DAY)posLog.push({t:o.t+60000*(2+Math.floor(r2()*4)),kind:'Sale',ref:o.no,store:o.ch,amt:o.total,ok:true})});
for(var k=0;k<3;k++)for(var h=9;h<=18;h+=3){var tt=END-k*DAY+h*36e5;if(tt>END+18.6*36e5)continue;posLog.push({t:tt,kind:'Inventory',ref:(20+Math.floor(r2()*60))+' part counts',store:STORES[Math.floor(r2()*4)].n,ok:r2()>.06})}
posLog.sort(function(a,b){return b.t-a.t});
var byId={};products.forEach(function(p){byId[p.id]=p});
var custById={};customers.forEach(function(c){custById[c.id]=c});
window.UFX_DEMO={DEMO:true,START:START,END:END,DAY:DAY,products:products,productById:byId,customers:customers,customerById:custById,orders:orders,posLog:posLog,suppliers:SUP,stores:STORES,channels:CHANNELS,
  counted:function(o){return o.status!='Cancelled'&&o.status!='Refunded'}};
})();
