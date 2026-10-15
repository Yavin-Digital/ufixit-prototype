# U-FIX-IT — Content inventory (LOCKED)

**Status:** LOCKED for Prototype density  
**Date:** 2026-09-16 ~8:20pm CT  
**Owners:** Randy (Research) from Nancy archive + signed url-index  
**Live:** https://ufixit.com/  
**Archive SoT:** `/workspace/ufixit-prototype/` — Nancy **APPROVED WITH CONDITIONS** (`references/signoff.md`)  
**Url-index:** `/workspace/ufixit/references/url-index.md` — KEEP 168 / DROP 72  

### Global locks
- **DROP** `/sample-page/` (WP dummy).
- **Catalog:** 438 products + ~54 `/appliances/{sku}/` = **DROP** individual SKUs; **USE** hubs + **2 sample PDPs** only (url-index).
- **Thin Woo shells:** cart / checkout / my-account / shipping-inquiry = system/REWRITE shells, not marketing density.
- **NAP Unverified (client confirm before Locations copy lock):** East Dallas **9919** vs map **9917** Garland Rd; South Dallas ZIP **75116** vs footer/shared **75237**. Proto may scaffold with primary visible NAP + Unverified tag — do not invent resolution.
- **Hours conflicts** (Sat exceptions; NYE 9–3 vs 9–6; Contact cards omit Sat) = REWRITE / client confirm.
- Official images: see `/workspace/ufixit-prototype/references/source-assets.md` + `img/` (55 assets).

### Block inventory (from Nancy archive)

| Source URL | Block | Kind | Decision | Why | Destination |
|---|---|---|---|---|---|
|https://ufixit.com/|Hero + value props + appliance tiles + brand logos + testimonials CTA|marketing|USE|Core home IA and offers|Home|
|https://ufixit.com/|Store phone strip (4 locations)|NAP|USE|Verbatim multi-location phones|Contact / footer|
|https://ufixit.com/about-us/|About body (100+ years experience, diagnosis specialty)|marketing|USE|Brand story|About|
|https://ufixit.com/about-us/mission/|Mission copy|marketing|USE|Short mission|About/Mission|
|https://ufixit.com/about-us/really-matters/|Gives Back / community|marketing|USE|CSR page|About/Gives Back|
|https://ufixit.com/about-us/store-hours/|Hours + holiday schedule|NAP|USE|Verbatim hours; confirm holidays annually|Hours|
|https://ufixit.com/about-us/team-members/|Team experts|marketing|USE|Team profiles/photos|About/Team|
|https://ufixit.com/about-us/warranty-returns/|Warranty & returns policy|legal|USE|Policy copy|Legal/Warranty|
|https://ufixit.com/contact-us/|Four-location hub with addresses/phones/hours|NAP|USE|Primary NAP hub|Contact|
|https://ufixit.com/contact-us/arlington-appliance-parts-store/|Arlington store page|store|USE|Location landing|Locations/Arlington|
|https://ufixit.com/contact-us/east-dallas/|East Dallas store page|store|REWRITE|NAP conflict 9919 vs map 9917 — fix address before ship|Locations/East Dallas|
|https://ufixit.com/contact-us/south-dallas/|South Dallas store page|store|USE|Location landing; verify ZIP 75116 vs schema 75237|Locations/South Dallas|
|https://ufixit.com/contact-us/tyler-tx/|Tyler store page|store|USE|Location landing|Locations/Tyler|
|https://ufixit.com/appliances/|Appliances hub|IA|USE|Category gateway|Appliances|
|https://ufixit.com/appliances/*-parts/|7 appliance category landings|IA|USE|Washer/Dryer/Fridge/AC/Furnace/Range/Dishwasher hubs|Appliances/{type}|
|https://ufixit.com/appliances/{sku}/|~54 part detail WP pages|catalog|DROP|SKU-like; empty WP content; do not prototype every SKU|Catalog (out of scope for CONTENT body)|
|https://ufixit.com/product/*|438 WooCommerce products|catalog|DROP|List in URL-INDEX only; catalog rebuild separate|Catalog|
|https://ufixit.com/find-your-brand/|Brand hub|IA|USE|Brand finder|Brands|
|https://ufixit.com/find-your-brand/{brand}/|33 brand CPT landings|IA|USE|Brand history/parts CTAs|Brands/{brand}|
|https://ufixit.com/appliance-repair-tips/|Tips index|blog|USE|DIY tips gateway|Tips|
|https://ufixit.com/diy-tips/* + /news/* + appliance SEO posts|~31 tip/news posts|blog|USE/REWRITE|Verbatim archive; some titles read SEO-thin — editorial review|Tips / News|
|https://ufixit.com/share-feedback/|Feedback funnel|form|USE|Review routing|Feedback|
|https://ufixit.com/share-feedback/add-review/|Add review|form|USE|Review form|Feedback|
|https://ufixit.com/share-feedback/tell-us-bad-experience/|Bad experience form|form|USE|Service recovery|Feedback|
|https://ufixit.com/shipping-appliance-parts/|Shipping info|legal|USE|Shipping policy/info|Shipping|
|https://ufixit.com/shipping-inquiry/|Shipping quote request|form|REWRITE|Thin/empty shell — rebuild form intentionally|Shipping inquiry|
|https://ufixit.com/privacy-policy/|Privacy policy|legal|USE|Legal|Privacy|
|https://ufixit.com/sitemap/|HTML sitemap|IA|USE|Discovery aid|Sitemap|
|https://ufixit.com/sample-page/|WP default dummy|dummy|DROP|Theme placeholder (bike messenger / Doohickey Co)|— delete|
|https://ufixit.com/shop/|Shop archive|catalog|USE|Shop entry (not every SKU)|Shop|
|https://ufixit.com/cart/|/checkout/|/my-account/|Woo system|system|REWRITE|Keep as functional routes; no marketing copy to port|Commerce system|
|https://ufixit.com/product-category/*|67 product cats (top + brand subcats)|catalog IA|USE|Top-level hubs in CONTENT; subcats indexed|Category IA|
|External Facebook location pages|Social|external|USE (link-only)|Do not scrape; list as external|Footer social|
### Expansion notes (Randy)
| Source | Decision | Why |
|--------|----------|-----|
| All url-index KEEP marketing/store/blog/brand/cat hubs not listed row-by-row above | **USE** | Full KEEP set from url-index; density from CONTENT.md verbatim — do not invent |
| Blog/DIY posts (~31) | **USE / REWRITE** | Verbatim archive; SEO-thin titles get editorial REWRITE not invented facts |
| Brand CPT landings (33–34) | **USE** | Hub pattern; one brand template OK |
| product_cat hubs (66) | **USE** | Category IA; not every SKU |
| Videos CPT / team query URLs / authors | **DROP** | Per url-index |
| Founding year (third-party 1975 vs BBB 1998) | **DROP / Unknown** | Live silent — do not claim |
| North Houston mention on East Dallas | **REWRITE / Unknown** | Possible stale — do not expand to 5th store |
| Gives Back named partners | **Unknown** | Use only what CONTENT.md states |

**Sign-off:** Randy locks this inventory for Bob Build Done gate (content). Growth dossier handoff separate. SEO/AEO Compare after proto pages.


## Proto file placement (Bob build 2026-09-16 CT)

| Live URL | Local file | Decision at build |
|---|---|---|
| https://ufixit.com/ | `index.html` | USE |
| https://ufixit.com/about-us/ | `about-us.html` | USE |
| https://ufixit.com/about-us/mission/ | `about-us-mission.html` | USE |
| https://ufixit.com/about-us/really-matters/ | `about-us-really-matters.html` | USE |
| https://ufixit.com/about-us/store-hours/ | `about-us-store-hours.html` | USE |
| https://ufixit.com/about-us/team-members/ | `about-us-team-members.html` | USE |
| https://ufixit.com/about-us/warranty-returns/ | `about-us-warranty-returns.html` | USE |
| https://ufixit.com/appliance-repair-tips/ | `appliance-repair-tips.html` | USE |
| https://ufixit.com/appliances/ | `appliances.html` | USE |
| https://ufixit.com/appliances/30-expert-bosch-appliance-repair-fast-reliable-fixes-near-you/ | `appliances-30-expert-bosch-appliance-repair-fast-reliable-fixes-near-you.html` | USE |
| https://ufixit.com/appliances/air-conditioner-parts/ | `appliances-air-conditioner-parts.html` | USE |
| https://ufixit.com/appliances/dishwasher-parts/ | `appliances-dishwasher-parts.html` | USE |
| https://ufixit.com/appliances/dryer-parts/ | `appliances-dryer-parts.html` | USE |
| https://ufixit.com/appliances/furnace-parts/ | `appliances-furnace-parts.html` | USE |
| https://ufixit.com/appliances/how-to-choose-the-right-hotpoint-appliance-for-your-home/ | `appliances-how-to-choose-the-right-hotpoint-appliance-for-your-home.html` | USE |
| https://ufixit.com/appliances/ranges-oven-parts/ | `appliances-ranges-oven-parts.html` | USE |
| https://ufixit.com/appliances/refrigerator-parts/ | `appliances-refrigerator-parts.html` | USE |
| https://ufixit.com/appliances/washer-parts/ | `appliances-washer-parts.html` | USE |
| https://ufixit.com/appliances/why-monogram-appliances-are-the-ultimate-choice-for-luxury-kitchens/ | `appliances-why-monogram-appliances-are-the-ultimate-choice-for-luxury-kitchens.html` | USE |
| https://ufixit.com/category/appliances/ | `category-appliances.html` | USE |
| https://ufixit.com/category/diy-tips/ | `category-diy-tips.html` | USE |
| https://ufixit.com/category/dryer/ | `category-dryer.html` | USE |
| https://ufixit.com/category/news/ | `category-news.html` | USE |
| https://ufixit.com/category/refrigerator/ | `category-refrigerator.html` | USE |
| https://ufixit.com/contact-us/ | `contact-us.html` | USE |
| https://ufixit.com/contact-us/arlington-appliance-parts-store/ | `contact-us-arlington-appliance-parts-store.html` | USE |
| https://ufixit.com/contact-us/east-dallas/ | `contact-us-east-dallas.html` | REWRITE (NAP street # TBD) |
| https://ufixit.com/contact-us/south-dallas/ | `contact-us-south-dallas.html` | USE (ZIP TBD) |
| https://ufixit.com/contact-us/tyler-tx/ | `contact-us-tyler-tx.html` | USE |
| https://ufixit.com/diy-tips/ | `diy-tips.html` | USE (archive HTML) |
| https://ufixit.com/diy-tips/4-household-appliance-myths/ | `diy-tips-4-household-appliance-myths.html` | USE |
| https://ufixit.com/diy-tips/benefits-of-fixing-appliances-yourself-instead-of-replacing-them/ | `diy-tips-benefits-of-fixing-appliances-yourself-instead-of-replacing-them.html` | USE |
| https://ufixit.com/diy-tips/best-replacement-parts-for-top-appliance-brands/ | `diy-tips-best-replacement-parts-for-top-appliance-brands.html` | USE |
| https://ufixit.com/diy-tips/complete-guide-to-dishwasher-parts/ | `diy-tips-complete-guide-to-dishwasher-parts.html` | USE |
| https://ufixit.com/diy-tips/discover-expert-device-appliance-repair-services-fast-reliable-solutions/ | `diy-tips-discover-expert-device-appliance-repair-services-fast-reliable-solutions.html` | USE |
| https://ufixit.com/diy-tips/electrolux-appliance-repair-guide-troubleshooting-common-issues-error-codes-genuine-parts/ | `diy-tips-electrolux-appliance-repair-guide-troubleshooting-common-issues-error-codes-genuine-parts.html` | USE |
| https://ufixit.com/diy-tips/essential-ac-parts-guide/ | `diy-tips-essential-ac-parts-guide.html` | USE |
| https://ufixit.com/diy-tips/expert-customer-diy-support-for-your-appliance-repair-parts-needs/ | `diy-tips-expert-customer-diy-support-for-your-appliance-repair-parts-needs.html` | USE |
| https://ufixit.com/diy-tips/find-quality-range-oven-parts-expert-guide-to-replacement-parts/ | `diy-tips-find-quality-range-oven-parts-expert-guide-to-replacement-parts.html` | USE |
| https://ufixit.com/diy-tips/find-reliable-major-appliance-repair/ | `diy-tips-find-reliable-major-appliance-repair.html` | USE |
| https://ufixit.com/diy-tips/gas-furnace-burner-goes-out/ | `diy-tips-gas-furnace-burner-goes-out.html` | USE |
| https://ufixit.com/diy-tips/home-air-conditioner-not-cooling/ | `diy-tips-home-air-conditioner-not-cooling.html` | USE |
| https://ufixit.com/diy-tips/how-to-find-the-right-replacement-parts-for-your-appliances/ | `diy-tips-how-to-find-the-right-replacement-parts-for-your-appliances.html` | USE |
| https://ufixit.com/diy-tips/how-to-find-your-appliance-model-number-and-order-the-right-part/ | `diy-tips-how-to-find-your-appliance-model-number-and-order-the-right-part.html` | USE |
| https://ufixit.com/diy-tips/ice-maker-not-working-try-this/ | `diy-tips-ice-maker-not-working-try-this.html` | USE |
| https://ufixit.com/diy-tips/lg-appliance-parts-guide/ | `diy-tips-lg-appliance-parts-guide.html` | USE |
| https://ufixit.com/diy-tips/on-doc-12-should-you-repair-or-replace-your-appliance-a-cost-benefit-guide-for-diy-homeowners/ | `diy-tips-on-doc-12-should-you-repair-or-replace-your-appliance-a-cost-benefit-guide-for-diy-homeowners.html` | USE |
| https://ufixit.com/diy-tips/refrigerator-defrost-problems/ | `diy-tips-refrigerator-defrost-problems.html` | USE |
| https://ufixit.com/diy-tips/thermador-appliance-repair-guide-luxury-kitchen-troubleshooting-error-codes-genuine-parts/ | `diy-tips-thermador-appliance-repair-guide-luxury-kitchen-troubleshooting-error-codes-genuine-parts.html` | USE |
| https://ufixit.com/diy-tips/viking-appliance-repair-guide-luxury-kitchen-troubleshooting-error-codes-genuine-parts/ | `diy-tips-viking-appliance-repair-guide-luxury-kitchen-troubleshooting-error-codes-genuine-parts.html` | USE |
| https://ufixit.com/diy-tips/whirlpool-dryer-not-heating/ | `diy-tips-whirlpool-dryer-not-heating.html` | USE |
| https://ufixit.com/diy-tips/whirlpool-washer-not-fill/ | `diy-tips-whirlpool-washer-not-fill.html` | USE |
| https://ufixit.com/dryer/complete-dryer-parts-diagram-your-guide-to-diy-dryer-repair/ | `dryer-complete-dryer-parts-diagram-your-guide-to-diy-dryer-repair.html` | USE |
| https://ufixit.com/find-your-brand/ | `find-your-brand.html` | USE |
| https://ufixit.com/find-your-brand/admiral/ | `find-your-brand-admiral.html` | USE |
| https://ufixit.com/find-your-brand/amana/ | `find-your-brand-amana.html` | USE |
| https://ufixit.com/find-your-brand/appliance-parts-lg/ | `find-your-brand-appliance-parts-lg.html` | USE |
| https://ufixit.com/find-your-brand/appliance-parts-whirpool/ | `find-your-brand-appliance-parts-whirpool.html` | USE |
| https://ufixit.com/find-your-brand/bosch/ | `find-your-brand-bosch.html` | USE |
| https://ufixit.com/find-your-brand/brown/ | `find-your-brand-brown.html` | USE |
| https://ufixit.com/find-your-brand/caloric/ | `find-your-brand-caloric.html` | USE |
| https://ufixit.com/find-your-brand/crosley/ | `find-your-brand-crosley.html` | USE |
| https://ufixit.com/find-your-brand/dacor/ | `find-your-brand-dacor.html` | USE |
| https://ufixit.com/find-your-brand/electrolux/ | `find-your-brand-electrolux.html` | USE |
| https://ufixit.com/find-your-brand/frigidaire-appliance-parts/ | `find-your-brand-frigidaire-appliance-parts.html` | USE |
| https://ufixit.com/find-your-brand/gaggenau/ | `find-your-brand-gaggenau.html` | USE |
| https://ufixit.com/find-your-brand/ge-general-electric/ | `find-your-brand-ge-general-electric.html` | USE |
| https://ufixit.com/find-your-brand/gibson/ | `find-your-brand-gibson.html` | USE |
| https://ufixit.com/find-your-brand/glenwood/ | `find-your-brand-glenwood.html` | USE |
| https://ufixit.com/find-your-brand/haier/ | `find-your-brand-haier.html` | USE |
| https://ufixit.com/find-your-brand/hardwick/ | `find-your-brand-hardwick.html` | USE |
| https://ufixit.com/find-your-brand/hotpoint/ | `find-your-brand-hotpoint.html` | USE |
| https://ufixit.com/find-your-brand/jenn-air/ | `find-your-brand-jenn-air.html` | USE |
| https://ufixit.com/find-your-brand/kelvinator/ | `find-your-brand-kelvinator.html` | USE |
| https://ufixit.com/find-your-brand/kenmore-appliances/ | `find-your-brand-kenmore-appliances.html` | USE |
| https://ufixit.com/find-your-brand/maytag-appliance-parts/ | `find-your-brand-maytag-appliance-parts.html` | USE |
| https://ufixit.com/find-your-brand/roper/ | `find-your-brand-roper.html` | USE |
| https://ufixit.com/find-your-brand/samsung/ | `find-your-brand-samsung.html` | USE |
| https://ufixit.com/find-your-brand/scotsman/ | `find-your-brand-scotsman.html` | USE |
| https://ufixit.com/find-your-brand/sears/ | `find-your-brand-sears.html` | USE |
| https://ufixit.com/find-your-brand/speed-queen/ | `find-your-brand-speed-queen.html` | USE |
| https://ufixit.com/find-your-brand/sub-zero/ | `find-your-brand-sub-zero.html` | USE |
| https://ufixit.com/find-your-brand/sunray/ | `find-your-brand-sunray.html` | USE |
| https://ufixit.com/find-your-brand/tappan/ | `find-your-brand-tappan.html` | USE |
| https://ufixit.com/find-your-brand/thermador/ | `find-your-brand-thermador.html` | USE |
| https://ufixit.com/find-your-brand/u-line/ | `find-your-brand-u-line.html` | USE |
| https://ufixit.com/find-your-brand/wolf/ | `find-your-brand-wolf.html` | USE |
| https://ufixit.com/news/home-air-conditioner-will-not-cool-outdoor-unit-condenser-not-running/ | `news-home-air-conditioner-will-not-cool-outdoor-unit-condenser-not-running.html` | USE |
| https://ufixit.com/news/refrigerator-will-not-dispense-water-produce-ice-possible-quick-fix/ | `news-refrigerator-will-not-dispense-water-produce-ice-possible-quick-fix.html` | USE |
| https://ufixit.com/news/save-time-save-money-u-fix/ | `news-save-time-save-money-u-fix.html` | USE |
| https://ufixit.com/privacy-policy/ | `privacy-policy.html` | USE |
| https://ufixit.com/product-category/accessories/ | `product-category-accessories.html` | USE |
| https://ufixit.com/product-category/accessories/dryer-accessories/ | `product-category-accessories-dryer-accessories.html` | USE (hub template) |
| https://ufixit.com/product-category/air-conditioner-parts/ | `product-category-air-conditioner-parts.html` | USE |
| https://ufixit.com/product-category/dishwasher-accessories/ | `product-category-dishwasher-accessories.html` | USE |
| https://ufixit.com/product-category/dishwasher-parts/ | `product-category-dishwasher-parts.html` | USE |
| https://ufixit.com/product-category/dishwasher-parts/bosch-dishwasher-parts/ | `product-category-dishwasher-parts-bosch-dishwasher-parts.html` | USE (hub template) |
| https://ufixit.com/product-category/dishwasher-parts/electrolux-dishwasher-parts/ | `product-category-dishwasher-parts-electrolux-dishwasher-parts.html` | USE (hub template) |
| https://ufixit.com/product-category/dishwasher-parts/frigidaire-dishwasher-parts/ | `product-category-dishwasher-parts-frigidaire-dishwasher-parts.html` | USE (hub template) |
| https://ufixit.com/product-category/dishwasher-parts/kenmore-dishwasher-parts/ | `product-category-dishwasher-parts-kenmore-dishwasher-parts.html` | USE (hub template) |
| https://ufixit.com/product-category/dishwasher-parts/kitchenaid-dishwasher-parts/ | `product-category-dishwasher-parts-kitchenaid-dishwasher-parts.html` | USE (hub template) |
| https://ufixit.com/product-category/dishwasher-parts/lg-dishwasher-parts/ | `product-category-dishwasher-parts-lg-dishwasher-parts.html` | USE (hub template) |
| https://ufixit.com/product-category/dishwasher-parts/maytag-parts/ | `product-category-dishwasher-parts-maytag-parts.html` | USE (hub template) |
| https://ufixit.com/product-category/dishwasher-parts/whirlpool-dishwasher-parts/ | `product-category-dishwasher-parts-whirlpool-dishwasher-parts.html` | USE (hub template) |
| https://ufixit.com/product-category/dryer-parts/ | `product-category-dryer-parts.html` | USE |
| https://ufixit.com/product-category/dryer-parts/crosley-dryer-parts/ | `product-category-dryer-parts-crosley-dryer-parts.html` | USE (hub template) |
| https://ufixit.com/product-category/dryer-parts/electrolux-dryer-parts/ | `product-category-dryer-parts-electrolux-dryer-parts.html` | USE (hub template) |
| https://ufixit.com/product-category/dryer-parts/frigidaire-dryer-parts/ | `product-category-dryer-parts-frigidaire-dryer-parts.html` | USE (hub template) |
| https://ufixit.com/product-category/dryer-parts/general-electric-ge-dryer-parts/ | `product-category-dryer-parts-general-electric-ge-dryer-parts.html` | USE (hub template) |
| https://ufixit.com/product-category/dryer-parts/kenmore-dryer-parts/ | `product-category-dryer-parts-kenmore-dryer-parts.html` | USE (hub template) |
| https://ufixit.com/product-category/dryer-parts/lg-dryer-parts/ | `product-category-dryer-parts-lg-dryer-parts.html` | USE (hub template) |
| https://ufixit.com/product-category/dryer-parts/maytag-dryer-parts/ | `product-category-dryer-parts-maytag-dryer-parts.html` | USE (hub template) |
| https://ufixit.com/product-category/dryer-parts/montgomery-wards-dryer-parts/ | `product-category-dryer-parts-montgomery-wards-dryer-parts.html` | USE (hub template) |
| https://ufixit.com/product-category/dryer-parts/roper-dryer-parts/ | `product-category-dryer-parts-roper-dryer-parts.html` | USE (hub template) |
| https://ufixit.com/product-category/dryer-parts/samsung-dryer-parts/ | `product-category-dryer-parts-samsung-dryer-parts.html` | USE (hub template) |
| https://ufixit.com/product-category/dryer-parts/sears-dryer-parts/ | `product-category-dryer-parts-sears-dryer-parts.html` | USE (hub template) |
| https://ufixit.com/product-category/dryer-parts/whirlpool-dryer-parts/ | `product-category-dryer-parts-whirlpool-dryer-parts.html` | USE (hub template) |
| https://ufixit.com/product-category/furnace-parts/ | `product-category-furnace-parts.html` | USE |
| https://ufixit.com/product-category/microwave-parts/ | `product-category-microwave-parts.html` | USE |
| https://ufixit.com/product-category/range-oven-parts/ | `product-category-range-oven-parts.html` | USE |
| https://ufixit.com/product-category/range-oven-parts/amana-range-oven-parts/ | `product-category-range-oven-parts-amana-range-oven-parts.html` | USE (hub template) |
| https://ufixit.com/product-category/range-oven-parts/electrolux-range-oven-parts/ | `product-category-range-oven-parts-electrolux-range-oven-parts.html` | USE (hub template) |
| https://ufixit.com/product-category/range-oven-parts/frigidaire-range-oven-parts/ | `product-category-range-oven-parts-frigidaire-range-oven-parts.html` | USE (hub template) |
| https://ufixit.com/product-category/range-oven-parts/ge-range-oven-parts/ | `product-category-range-oven-parts-ge-range-oven-parts.html` | USE (hub template) |
| https://ufixit.com/product-category/range-oven-parts/general-electric-range-oven-parts/ | `product-category-range-oven-parts-general-electric-range-oven-parts.html` | USE (hub template) |
| https://ufixit.com/product-category/range-oven-parts/kenmore-range-oven-parts/ | `product-category-range-oven-parts-kenmore-range-oven-parts.html` | USE (hub template) |
| https://ufixit.com/product-category/range-oven-parts/maytag-range-oven-parts/ | `product-category-range-oven-parts-maytag-range-oven-parts.html` | USE (hub template) |
| https://ufixit.com/product-category/range-oven-parts/sears-range-oven-parts/ | `product-category-range-oven-parts-sears-range-oven-parts.html` | USE (hub template) |
| https://ufixit.com/product-category/range-oven-parts/whirlpool-range-oven-parts/ | `product-category-range-oven-parts-whirlpool-range-oven-parts.html` | USE (hub template) |
| https://ufixit.com/product-category/refrigerator-parts/ | `product-category-refrigerator-parts.html` | USE |
| https://ufixit.com/product-category/refrigerator-parts/bosch-refrigerator-parts/ | `product-category-refrigerator-parts-bosch-refrigerator-parts.html` | USE (hub template) |
| https://ufixit.com/product-category/refrigerator-parts/electrolux-refrigerator-parts/ | `product-category-refrigerator-parts-electrolux-refrigerator-parts.html` | USE (hub template) |
| https://ufixit.com/product-category/refrigerator-parts/frigidaire-refrigerator-parts/ | `product-category-refrigerator-parts-frigidaire-refrigerator-parts.html` | USE (hub template) |
| https://ufixit.com/product-category/refrigerator-parts/ge-refrigerator-parts/ | `product-category-refrigerator-parts-ge-refrigerator-parts.html` | USE (hub template) |
| https://ufixit.com/product-category/refrigerator-parts/kenmore-refrigerator-parts/ | `product-category-refrigerator-parts-kenmore-refrigerator-parts.html` | USE (hub template) |
| https://ufixit.com/product-category/refrigerator-parts/kitchenaid-refrigerator-parts/ | `product-category-refrigerator-parts-kitchenaid-refrigerator-parts.html` | USE (hub template) |
| https://ufixit.com/product-category/refrigerator-parts/lg-refrigerator-parts/ | `product-category-refrigerator-parts-lg-refrigerator-parts.html` | USE (hub template) |
| https://ufixit.com/product-category/refrigerator-parts/samsung-refrigerator-parts/ | `product-category-refrigerator-parts-samsung-refrigerator-parts.html` | USE (hub template) |
| https://ufixit.com/product-category/refrigerator-parts/sears-refrigerator-parts/ | `product-category-refrigerator-parts-sears-refrigerator-parts.html` | USE (hub template) |
| https://ufixit.com/product-category/refrigerator-parts/whirlpool-refrigerator-parts/ | `product-category-refrigerator-parts-whirlpool-refrigerator-parts.html` | USE (hub template) |
| https://ufixit.com/product-category/washer-parts/ | `product-category-washer-parts.html` | USE |
| https://ufixit.com/product-category/washer-parts/bosch-washer-parts/ | `product-category-washer-parts-bosch-washer-parts.html` | USE (hub template) |
| https://ufixit.com/product-category/washer-parts/electrolux-washer-parts/ | `product-category-washer-parts-electrolux-washer-parts.html` | USE (hub template) |
| https://ufixit.com/product-category/washer-parts/estate-washer-parts/ | `product-category-washer-parts-estate-washer-parts.html` | USE (hub template) |
| https://ufixit.com/product-category/washer-parts/fisher-and-paykel-washer-parts/ | `product-category-washer-parts-fisher-and-paykel-washer-parts.html` | USE (hub template) |
| https://ufixit.com/product-category/washer-parts/frigidaire-washer-parts/ | `product-category-washer-parts-frigidaire-washer-parts.html` | USE (hub template) |
| https://ufixit.com/product-category/washer-parts/ge-washer-parts/ | `product-category-washer-parts-ge-washer-parts.html` | USE (hub template) |
| https://ufixit.com/product-category/washer-parts/kenmore-washer-parts/ | `product-category-washer-parts-kenmore-washer-parts.html` | USE (hub template) |
| https://ufixit.com/product-category/washer-parts/lg-washer-parts/ | `product-category-washer-parts-lg-washer-parts.html` | USE (hub template) |
| https://ufixit.com/product-category/washer-parts/roper-washer-parts/ | `product-category-washer-parts-roper-washer-parts.html` | USE (hub template) |
| https://ufixit.com/product-category/washer-parts/samsung-washer-parts/ | `product-category-washer-parts-samsung-washer-parts.html` | USE (hub template) |
| https://ufixit.com/product-category/washer-parts/sears-washer-parts/ | `product-category-washer-parts-sears-washer-parts.html` | USE (hub template) |
| https://ufixit.com/product-category/washer-parts/speed-queen-washer-parts/ | `product-category-washer-parts-speed-queen-washer-parts.html` | USE (hub template) |
| https://ufixit.com/product-category/washer-parts/tappan-washer-parts/ | `product-category-washer-parts-tappan-washer-parts.html` | USE (hub template) |
| https://ufixit.com/product-category/washer-parts/wci-washer-parts/ | `product-category-washer-parts-wci-washer-parts.html` | USE (hub template) |
| https://ufixit.com/product-category/washer-parts/westinghouse-washer-parts/ | `product-category-washer-parts-westinghouse-washer-parts.html` | USE (hub template) |
| https://ufixit.com/product-category/washer-parts/whirlpool-washer-parts/ | `product-category-washer-parts-whirlpool-washer-parts.html` | USE (hub template) |
| https://ufixit.com/product/er-w10190961-icemaker-for-whirlpool/ | `product-er-w10190961-icemaker-for-whirlpool.html` | USE (sample PDP) |
| https://ufixit.com/product/part-no-er-b3200-bake-element-for-electrolux/ | `product-part-no-er-b3200-bake-element-for-electrolux.html` | USE (sample PDP) |
| https://ufixit.com/refrigerator/frigidaire-parts-diy-guide/ | `refrigerator-frigidaire-parts-diy-guide.html` | USE |
| https://ufixit.com/refrigerator/frigidaire-refrigerator-not-cooling-fix-it-yourself-with-the-right-parts/ | `refrigerator-frigidaire-refrigerator-not-cooling-fix-it-yourself-with-the-right-parts.html` | USE |
| https://ufixit.com/share-feedback/ | `share-feedback.html` | USE |
| https://ufixit.com/share-feedback/add-review/ | `share-feedback-add-review.html` | USE |
| https://ufixit.com/share-feedback/tell-us-bad-experience/ | `share-feedback-tell-us-bad-experience.html` | USE |
| https://ufixit.com/shipping-appliance-parts/ | `shipping-appliance-parts.html` | USE |
| https://ufixit.com/shipping-inquiry/ | `shipping-inquiry.html` | USE |
| https://ufixit.com/shop/ | `shop.html` | USE |
| https://ufixit.com/sitemap/ | `sitemap.html` | USE |

**Note:** East Dallas street # and South Dallas ZIP remain Unverified — omitted/TBD in HTML. sample-page DROP (not built).
