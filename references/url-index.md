# U-FIX-IT Appliance Parts — URL Index

**Brand (site spelling):** U-Fix-It / U-FIX-IT Appliance Parts  
**Live:** https://ufixit.com/  
**Slug:** ufixit  
**Discovery date:** 2026-09-16 20:11 CT  
**Box SoT:** `/workspace/ufixit/references/url-index.md`  
**Archive SoT (content pull):** pending at `/workspace/ufixit-prototype/` (not blocking this index)

## Discovery method

| Source | Status | Notes |
|--------|--------|-------|
| Yoast sitemap index | COMPLETE | https://ufixit.com/sitemap_index.xml → post, page, product, testimonials, brands, category, product_cat, author |
| Child sitemaps | COMPLETE | pages=86, posts=32, products=436 (+ shop), brands=34, product_cat=66, blog cats=5, testimonials=4, authors=3 |
| Product sitemap pagination | N/A | Single `product-sitemap.xml` (not split) |
| WP REST `/wp/v2/pages` | COMPLETE | x-wp-total=87 (1 page @ per_page=100) |
| WP REST `/wp/v2/posts` | COMPLETE | x-wp-total=31 |
| WP REST CPTs | COMPLETE | brands=33, testimonials=4, videos=60, team=5; `products` route 404 (use Woo Store API) |
| Woo Store API products | COMPLETE | `GET /wp-json/wc/store/v1/products` → **x-wp-total=438** |
| Homepage + primary nav + footer | COMPLETE | Parsed `homepage.html`; nav=35 unique, footer=2 (sitemap, privacy); off-nav home links included in Sources |
| Google `site:ufixit.com` | **PARTIAL** | Captcha /sorry on curl (HTTP 429) and Playwright Chromium (2 attempts). Evidence: `references/google_site_p1.html`, `references/google_browser_p1.html`, `references/google_attempt2.html`, `references/google_site_results.json` (status=PARTIAL, last_page=1, count=0). Index not held for Google. |

## Counts summary

| Metric | Count |
|--------|------:|
| Rows in table (KEEP) | 168 |
| Rows in table (DROP) | 72 |
| WP pages (REST) | 87 |
| WP posts (REST) | 31 |
| Woo products (Store API) | **438** (HUGE catalog relative to marketing IA — SKUs DROP) |
| Sitemap PDPs `/product/` | 436 |
| Brand URLs (sitemap) | 34 |
| Product category hubs | 66 |
| Blog category hubs | 5 |
| Videos CPT | 60 |
| Google site: | PARTIAL |

### KEEP / DROP policy (ecommerce)

- **KEEP:** Home, About (+ mission, gives-back, hours, team, warranty), Contact + 4 store locations, Shipping, Privacy, Sitemap, feedback hub, Repair Tips / DIY hubs, all blog posts, brand hub + brand pages, appliance category hubs, all `product-category` hubs, Shop hub, **2 sample PDPs** for proto pattern.
- **DROP:** Cart / Checkout / My Account / Sample Page; **434 product SKUs** (pattern row); individual `/appliances/{part-slug}/` SKU-like WP pages; author archives; individual testimonial/team/video query-string CPT URLs.
- Individual part landings under `/appliances/` (non-hub) treated like SKUs for proto — hubs + sample PDPs only.

## Full URL table

| URL | Title | In-nav? | Source | KEEP/DROP | Why |
|-----|-------|---------|--------|-----------|-----|
| https://ufixit.com/ | Home | Y | REST+sitemap+nav | **KEEP** | Marketing / IA / store / legal / hub page |
| https://ufixit.com/about-us/ | About Us | Y | REST+sitemap+nav | **KEEP** | Marketing / IA / store / legal / hub page |
| https://ufixit.com/about-us/mission/ | U-FIX-IT Mission | Y | REST+sitemap+nav | **KEEP** | Marketing / IA / store / legal / hub page |
| https://ufixit.com/about-us/really-matters/ | U-FIX-IT Gives Back | N | REST+sitemap | **KEEP** | Marketing / IA / store / legal / hub page |
| https://ufixit.com/about-us/store-hours/ | Store Hours & Holidays | Y | REST+sitemap+nav | **KEEP** | Marketing / IA / store / legal / hub page |
| https://ufixit.com/about-us/team-members/ | Our Appliance Repair Experts | Y | REST+sitemap+nav | **KEEP** | Marketing / IA / store / legal / hub page |
| https://ufixit.com/about-us/warranty-returns/ | Appliance Parts Warranty & Returns | Y | REST+sitemap+nav | **KEEP** | Marketing / IA / store / legal / hub page |
| https://ufixit.com/appliance-repair-tips/ | Appliance Repair Tips | Y | REST+sitemap+nav | **KEEP** | Marketing / IA / store / legal / hub page |
| https://ufixit.com/appliances/ | Appliances | Y | REST+sitemap+nav | **KEEP** | Marketing / IA / store / legal / hub page |
| https://ufixit.com/appliances/30-expert-bosch-appliance-repair-fast-reliable-fixes-near-you/ | Expert Bosch Appliance Repair | N | REST+sitemap | **KEEP** | Blog / DIY tips / news content |
| https://ufixit.com/appliances/air-conditioner-parts/ | Air Conditioner Repair Parts | Y | REST+sitemap+nav | **KEEP** | Marketing / IA / store / legal / hub page |
| https://ufixit.com/appliances/dishwasher-parts/ | Dishwasher Repair Parts | Y | REST+sitemap+nav | **KEEP** | Marketing / IA / store / legal / hub page |
| https://ufixit.com/appliances/dryer-parts/ | Dryer Repair Parts | Y | REST+sitemap+nav | **KEEP** | Marketing / IA / store / legal / hub page |
| https://ufixit.com/appliances/furnace-parts/ | Furnace Repair Parts | Y | REST+sitemap+nav | **KEEP** | Marketing / IA / store / legal / hub page |
| https://ufixit.com/appliances/how-to-choose-the-right-hotpoint-appliance-for-your-home/ | How to Choose the Right Hotpoint Appliance for Your Home | N | REST+sitemap | **KEEP** | Blog / DIY tips / news content |
| https://ufixit.com/appliances/ranges-oven-parts/ | Ranges & Oven Repair Parts | Y | REST+sitemap+nav | **KEEP** | Marketing / IA / store / legal / hub page |
| https://ufixit.com/appliances/refrigerator-parts/ | Refrigerator Repair Parts | Y | REST+sitemap+nav | **KEEP** | Marketing / IA / store / legal / hub page |
| https://ufixit.com/appliances/washer-parts/ | Washer Repair Parts | Y | REST+sitemap+nav | **KEEP** | Marketing / IA / store / legal / hub page |
| https://ufixit.com/appliances/why-monogram-appliances-are-the-ultimate-choice-for-luxury-kitchens/ | Why Monogram Appliances Are the Ultimate Choice for Luxury Kitchens | N | REST+sitemap | **KEEP** | Blog / DIY tips / news content |
| https://ufixit.com/category/appliances/ | Appliances (blog category) | N | sitemap | **KEEP** | Blog category hub |
| https://ufixit.com/category/diy-tips/ | Diy Tips (blog category) | N | sitemap | **KEEP** | Blog category hub |
| https://ufixit.com/category/dryer/ | Dryer (blog category) | N | sitemap | **KEEP** | Blog category hub |
| https://ufixit.com/category/news/ | News (blog category) | N | sitemap | **KEEP** | Blog category hub |
| https://ufixit.com/category/refrigerator/ | Refrigerator (blog category) | N | sitemap | **KEEP** | Blog category hub |
| https://ufixit.com/contact-us/ | Contact Us | Y | REST+sitemap+nav | **KEEP** | Marketing / IA / store / legal / hub page |
| https://ufixit.com/contact-us/arlington-appliance-parts-store/ | Arlington Appliance Parts Store | Y | REST+sitemap+nav | **KEEP** | Marketing / IA / store / legal / hub page |
| https://ufixit.com/contact-us/east-dallas/ | East Dallas Appliance Parts Store | Y | REST+sitemap+nav | **KEEP** | Marketing / IA / store / legal / hub page |
| https://ufixit.com/contact-us/south-dallas/ | South Dallas Appliance Parts Store | Y | REST+sitemap+nav | **KEEP** | Marketing / IA / store / legal / hub page |
| https://ufixit.com/contact-us/tyler-tx/ | Tyler TX Appliance Parts Store | Y | REST+sitemap+nav | **KEEP** | Marketing / IA / store / legal / hub page |
| https://ufixit.com/diy-tips/ | DIY Tips | N | home-crawl(HTTP200) | **KEEP** | Blog / DIY tips hub path |
| https://ufixit.com/diy-tips/4-household-appliance-myths/ | 4 Household Appliance Myths | N | REST+sitemap | **KEEP** | Blog / DIY tips / news content |
| https://ufixit.com/diy-tips/benefits-of-fixing-appliances-yourself-instead-of-replacing-them/ | Benefits of Fixing Appliances Yourself Instead of Replacing Them | N | REST+sitemap | **KEEP** | Blog / DIY tips / news content |
| https://ufixit.com/diy-tips/best-replacement-parts-for-top-appliance-brands/ | Best Replacement Parts for Top Appliance Brands | N | REST+sitemap | **KEEP** | Blog / DIY tips / news content |
| https://ufixit.com/diy-tips/complete-guide-to-dishwasher-parts/ | Complete Guide to Dishwasher Parts | N | REST+sitemap | **KEEP** | Blog / DIY tips / news content |
| https://ufixit.com/diy-tips/discover-expert-device-appliance-repair-services-fast-reliable-solutions/ | Discover Expert Device & Appliance Repair Services \| Fast & Reliable Solutions | N | REST+sitemap | **KEEP** | Blog / DIY tips / news content |
| https://ufixit.com/diy-tips/electrolux-appliance-repair-guide-troubleshooting-common-issues-error-codes-genuine-parts/ | Electrolux Appliance Repair Guide | N | REST+sitemap | **KEEP** | Blog / DIY tips / news content |
| https://ufixit.com/diy-tips/essential-ac-parts-guide/ | Essential AC Parts Guide: | N | REST+sitemap | **KEEP** | Blog / DIY tips / news content |
| https://ufixit.com/diy-tips/expert-customer-diy-support-for-your-appliance-repair-parts-needs/ | Expert Customer DIY Support for Your Appliance Repair & Parts Needs | N | REST+sitemap | **KEEP** | Blog / DIY tips / news content |
| https://ufixit.com/diy-tips/find-quality-range-oven-parts-expert-guide-to-replacement-parts/ | Find Quality Range & Oven Parts \| Expert Guide to Replacement Parts | N | REST+sitemap | **KEEP** | Blog / DIY tips / news content |
| https://ufixit.com/diy-tips/find-reliable-major-appliance-repair/ | Find Reliable Major Appliance Repair | N | REST+sitemap | **KEEP** | Blog / DIY tips / news content |
| https://ufixit.com/diy-tips/gas-furnace-burner-goes-out/ | Gas Furnace – Burner Goes Out | N | REST+sitemap | **KEEP** | Blog / DIY tips / news content |
| https://ufixit.com/diy-tips/home-air-conditioner-not-cooling/ | Air conditioner not cooling – outdoor unit not running | N | REST+sitemap | **KEEP** | Blog / DIY tips / news content |
| https://ufixit.com/diy-tips/how-to-find-the-right-replacement-parts-for-your-appliances/ | How to Find the Right Replacement Parts for Your Appliances | N | REST+sitemap | **KEEP** | Blog / DIY tips / news content |
| https://ufixit.com/diy-tips/how-to-find-your-appliance-model-number-and-order-the-right-part/ | How to Find Your Appliance Model Number and Order the Right Part | N | REST+sitemap | **KEEP** | Blog / DIY tips / news content |
| https://ufixit.com/diy-tips/ice-maker-not-working-try-this/ | Ice Maker Not Working? Try these easy steps. | N | REST+sitemap | **KEEP** | Blog / DIY tips / news content |
| https://ufixit.com/diy-tips/lg-appliance-parts-guide/ | LG Appliance Parts Guide | N | REST+sitemap | **KEEP** | Blog / DIY tips / news content |
| https://ufixit.com/diy-tips/on-doc-12-should-you-repair-or-replace-your-appliance-a-cost-benefit-guide-for-diy-homeowners/ | Should You Repair or Replace Your Appliance? | N | REST+sitemap | **KEEP** | Blog / DIY tips / news content |
| https://ufixit.com/diy-tips/refrigerator-defrost-problems/ | Refrigerator Defrost problems – Diagnosing the most common malfunction of refrigerators and freezers | N | REST+sitemap | **KEEP** | Blog / DIY tips / news content |
| https://ufixit.com/diy-tips/thermador-appliance-repair-guide-luxury-kitchen-troubleshooting-error-codes-genuine-parts/ | Thermador Appliance Repair Guide | N | REST+sitemap | **KEEP** | Blog / DIY tips / news content |
| https://ufixit.com/diy-tips/viking-appliance-repair-guide-luxury-kitchen-troubleshooting-error-codes-genuine-parts/ | Viking Appliance Repair Guide | N | REST+sitemap | **KEEP** | Blog / DIY tips / news content |
| https://ufixit.com/diy-tips/whirlpool-dryer-not-heating/ | Whirlpool Dryer Not Heating: Causes and Troubleshooting Tips | N | REST+sitemap | **KEEP** | Blog / DIY tips / news content |
| https://ufixit.com/diy-tips/whirlpool-washer-not-fill/ | What can be wrong when a Whirlpool washer will not fill with water? | N | REST+sitemap | **KEEP** | Blog / DIY tips / news content |
| https://ufixit.com/dryer/complete-dryer-parts-diagram-your-guide-to-diy-dryer-repair/ | Complete Dryer Parts Diagram: Your Guide to DIY Dryer Repair | N | REST+sitemap | **KEEP** | Blog / DIY tips / news content |
| https://ufixit.com/find-your-brand/ | Find Your Brand | Y | sitemap+nav | **KEEP** | Brand hub |
| https://ufixit.com/find-your-brand/admiral/ | Admiral | Y | sitemap+REST+nav | **KEEP** | Brand hub page |
| https://ufixit.com/find-your-brand/amana/ | Amana | N | sitemap+REST | **KEEP** | Brand hub page |
| https://ufixit.com/find-your-brand/appliance-parts-lg/ | LG | Y | sitemap+REST+nav | **KEEP** | Brand hub page |
| https://ufixit.com/find-your-brand/appliance-parts-whirpool/ | Whirlpool | Y | sitemap+REST+nav | **KEEP** | Brand hub page |
| https://ufixit.com/find-your-brand/bosch/ | Bosch | Y | sitemap+REST+nav | **KEEP** | Brand hub page |
| https://ufixit.com/find-your-brand/brown/ | Brown | Y | sitemap+REST+nav | **KEEP** | Brand hub page |
| https://ufixit.com/find-your-brand/caloric/ | Caloric | Y | sitemap+REST+nav | **KEEP** | Brand hub page |
| https://ufixit.com/find-your-brand/crosley/ | Crosley | N | sitemap+REST | **KEEP** | Brand hub page |
| https://ufixit.com/find-your-brand/dacor/ | Dacor | N | sitemap+REST | **KEEP** | Brand hub page |
| https://ufixit.com/find-your-brand/electrolux/ | Electrolux | N | sitemap+REST | **KEEP** | Brand hub page |
| https://ufixit.com/find-your-brand/frigidaire-appliance-parts/ | Frigidaire | Y | sitemap+REST+nav | **KEEP** | Brand hub page |
| https://ufixit.com/find-your-brand/gaggenau/ | Gaggenau | N | sitemap+REST | **KEEP** | Brand hub page |
| https://ufixit.com/find-your-brand/ge-general-electric/ | GE | Y | sitemap+REST+nav | **KEEP** | Brand hub page |
| https://ufixit.com/find-your-brand/gibson/ | Gibson | N | sitemap+REST | **KEEP** | Brand hub page |
| https://ufixit.com/find-your-brand/glenwood/ | Glenwood | N | sitemap+REST | **KEEP** | Brand hub page |
| https://ufixit.com/find-your-brand/haier/ | Haier | N | sitemap+REST | **KEEP** | Brand hub page |
| https://ufixit.com/find-your-brand/hardwick/ | Hardwick | N | sitemap+REST | **KEEP** | Brand hub page |
| https://ufixit.com/find-your-brand/hotpoint/ | Hotpoint | N | sitemap+REST | **KEEP** | Brand hub page |
| https://ufixit.com/find-your-brand/jenn-air/ | Jenn Air | N | sitemap+REST | **KEEP** | Brand hub page |
| https://ufixit.com/find-your-brand/kelvinator/ | Kelvinator | N | sitemap+REST | **KEEP** | Brand hub page |
| https://ufixit.com/find-your-brand/kenmore-appliances/ | Kenmore | Y | sitemap+REST+nav | **KEEP** | Brand hub page |
| https://ufixit.com/find-your-brand/maytag-appliance-parts/ | Maytag | Y | sitemap+REST+nav | **KEEP** | Brand hub page |
| https://ufixit.com/find-your-brand/roper/ | Roper | N | sitemap+REST | **KEEP** | Brand hub page |
| https://ufixit.com/find-your-brand/samsung/ | Samsung | Y | sitemap+REST+nav | **KEEP** | Brand hub page |
| https://ufixit.com/find-your-brand/scotsman/ | Scotsman | N | sitemap+REST | **KEEP** | Brand hub page |
| https://ufixit.com/find-your-brand/sears/ | Sears | Y | sitemap+REST+nav | **KEEP** | Brand hub page |
| https://ufixit.com/find-your-brand/speed-queen/ | Speed Queen | N | sitemap+REST | **KEEP** | Brand hub page |
| https://ufixit.com/find-your-brand/sub-zero/ | Sub Zero | N | sitemap+REST | **KEEP** | Brand hub page |
| https://ufixit.com/find-your-brand/sunray/ | Sunray | N | sitemap+REST | **KEEP** | Brand hub page |
| https://ufixit.com/find-your-brand/tappan/ | Tappan | N | sitemap+REST | **KEEP** | Brand hub page |
| https://ufixit.com/find-your-brand/thermador/ | Thermador | N | sitemap+REST | **KEEP** | Brand hub page |
| https://ufixit.com/find-your-brand/u-line/ | U-LINE | N | sitemap+REST | **KEEP** | Brand hub page |
| https://ufixit.com/find-your-brand/wolf/ | Wolf | N | sitemap+REST | **KEEP** | Brand hub page |
| https://ufixit.com/news/home-air-conditioner-will-not-cool-outdoor-unit-condenser-not-running/ | Home air conditioner will not cool – outdoor unit (condenser) not running | N | REST+sitemap | **KEEP** | Blog / DIY tips / news content |
| https://ufixit.com/news/refrigerator-will-not-dispense-water-produce-ice-possible-quick-fix/ | Two “not so obvious” things to check that can stop all waterflow in your refrigerator. | N | REST+sitemap | **KEEP** | Blog / DIY tips / news content |
| https://ufixit.com/news/save-time-save-money-u-fix/ | Save time, save money – U-FIX-IT | N | REST+sitemap | **KEEP** | Blog / DIY tips / news content |
| https://ufixit.com/privacy-policy/ | Privacy Policy | Y | REST+sitemap+nav | **KEEP** | Marketing / IA / store / legal / hub page |
| https://ufixit.com/product-category/accessories/ | Accessories | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/accessories/dryer-accessories/ | Dryer Accessories | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/air-conditioner-parts/ | Air Conditioner Parts | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/dishwasher-accessories/ | Dishwasher Accessories | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/dishwasher-parts/ | Washer Parts | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/dishwasher-parts/bosch-dishwasher-parts/ | Washer Parts | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/dishwasher-parts/electrolux-dishwasher-parts/ | Washer Parts | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/dishwasher-parts/frigidaire-dishwasher-parts/ | Washer Parts | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/dishwasher-parts/kenmore-dishwasher-parts/ | Washer Parts | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/dishwasher-parts/kitchenaid-dishwasher-parts/ | Washer Parts | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/dishwasher-parts/lg-dishwasher-parts/ | Washer Parts | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/dishwasher-parts/maytag-parts/ | Maytag Parts | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/dishwasher-parts/whirlpool-dishwasher-parts/ | Whirlpool Dishwasher Parts | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/dryer-parts/ | Dryer Parts | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/dryer-parts/crosley-dryer-parts/ | Dryer Parts | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/dryer-parts/electrolux-dryer-parts/ | Electrolux Dryer Parts | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/dryer-parts/frigidaire-dryer-parts/ | Frigidaire Dryer Parts | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/dryer-parts/general-electric-ge-dryer-parts/ | General Electric (GE) Dryer Parts | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/dryer-parts/kenmore-dryer-parts/ | Kenmore Dryer Parts | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/dryer-parts/lg-dryer-parts/ | LG Dryer Parts | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/dryer-parts/maytag-dryer-parts/ | Maytag Dryer Parts | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/dryer-parts/montgomery-wards-dryer-parts/ | Montgomery Wards Dryer Parts | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/dryer-parts/roper-dryer-parts/ | Roper Dryer Parts | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/dryer-parts/samsung-dryer-parts/ | Samsung Dryer Parts | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/dryer-parts/sears-dryer-parts/ | Sears Dryer Parts | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/dryer-parts/whirlpool-dryer-parts/ | Whirlpool Dryer Parts | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/furnace-parts/ | Furnace Parts | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/microwave-parts/ | Microwave Parts | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/range-oven-parts/ | Range & Oven Parts | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/range-oven-parts/amana-range-oven-parts/ | Range & Oven Parts | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/range-oven-parts/electrolux-range-oven-parts/ | Range & Oven Parts | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/range-oven-parts/frigidaire-range-oven-parts/ | Range & Oven Parts | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/range-oven-parts/ge-range-oven-parts/ | Range & Oven Parts | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/range-oven-parts/general-electric-range-oven-parts/ | Range & Oven Parts | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/range-oven-parts/kenmore-range-oven-parts/ | Range & Oven Parts | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/range-oven-parts/maytag-range-oven-parts/ | Range & Oven Parts | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/range-oven-parts/sears-range-oven-parts/ | Sears Range & Oven Parts | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/range-oven-parts/whirlpool-range-oven-parts/ | Whirlpool Range & Oven Parts | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/refrigerator-parts/ | Refrigerator Parts | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/refrigerator-parts/bosch-refrigerator-parts/ | Refrigerator Parts | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/refrigerator-parts/electrolux-refrigerator-parts/ | Refrigerator Parts | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/refrigerator-parts/frigidaire-refrigerator-parts/ | Refrigerator Parts | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/refrigerator-parts/ge-refrigerator-parts/ | Refrigerator Parts | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/refrigerator-parts/kenmore-refrigerator-parts/ | Refrigerator Parts | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/refrigerator-parts/kitchenaid-refrigerator-parts/ | Refrigerator Parts | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/refrigerator-parts/lg-refrigerator-parts/ | Refrigerator Parts | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/refrigerator-parts/samsung-refrigerator-parts/ | Samsung Refrigerator Parts | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/refrigerator-parts/sears-refrigerator-parts/ | Sears Refrigerator Parts | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/refrigerator-parts/whirlpool-refrigerator-parts/ | Whirlpool Refrigerator Parts | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/washer-parts/ | Washer Parts | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/washer-parts/bosch-washer-parts/ | Washer Parts | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/washer-parts/electrolux-washer-parts/ | Washer Parts | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/washer-parts/estate-washer-parts/ | Washer Parts | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/washer-parts/fisher-and-paykel-washer-parts/ | Washer Parts | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/washer-parts/frigidaire-washer-parts/ | Washer Parts | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/washer-parts/ge-washer-parts/ | Washer Parts | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/washer-parts/kenmore-washer-parts/ | Washer Parts | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/washer-parts/lg-washer-parts/ | Washer Parts | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/washer-parts/roper-washer-parts/ | Washer Parts | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/washer-parts/samsung-washer-parts/ | Washer Parts | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/washer-parts/sears-washer-parts/ | Washer Parts | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/washer-parts/speed-queen-washer-parts/ | Washer Parts | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/washer-parts/tappan-washer-parts/ | Washer Parts | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/washer-parts/wci-washer-parts/ | WCI Washer Parts | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/washer-parts/westinghouse-washer-parts/ | Westinghouse Washer Parts | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product-category/washer-parts/whirlpool-washer-parts/ | Whirlpool Washer Parts | N | sitemap+Woo | **KEEP** | WooCommerce product category hub |
| https://ufixit.com/product/er-w10190961-icemaker-for-whirlpool/ | Er W10190961 Icemaker For Whirlpool | N | sitemap | **KEEP** | Sample PDP pattern for proto (1 of 2) |
| https://ufixit.com/product/part-no-er-b3200-bake-element-for-electrolux/ | Part No Er B3200 Bake Element For Electrolux | N | sitemap | **KEEP** | Sample PDP pattern for proto (1 of 2) |
| https://ufixit.com/refrigerator/frigidaire-parts-diy-guide/ | Frigidaire Parts – DIY Guide | N | REST+sitemap | **KEEP** | Blog / DIY tips / news content |
| https://ufixit.com/refrigerator/frigidaire-refrigerator-not-cooling-fix-it-yourself-with-the-right-parts/ | Frigidaire Refrigerator Not Cooling? Fix It Yourself with the Right Parts | N | REST+sitemap | **KEEP** | Blog / DIY tips / news content |
| https://ufixit.com/share-feedback/ | Tell us About Your U-Fix-It Experience | N | REST+sitemap+REST+nav | **KEEP** | Marketing / IA / store / legal / hub page |
| https://ufixit.com/share-feedback/add-review/ | Add a Review | N | REST+sitemap | **KEEP** | Marketing / IA / store / legal / hub page |
| https://ufixit.com/share-feedback/tell-us-bad-experience/ | We are sorry to hear it… | N | REST+sitemap | **KEEP** | Marketing / IA / store / legal / hub page |
| https://ufixit.com/shipping-appliance-parts/ | Shipping Appliance Parts | Y | REST+sitemap+nav | **KEEP** | Marketing / IA / store / legal / hub page |
| https://ufixit.com/shipping-inquiry/ | U-FIX-IT | N | REST+sitemap | **KEEP** | Marketing / IA / store / legal / hub page |
| https://ufixit.com/shop/ | Shop | N | REST+sitemap+sitemap+nav | **KEEP** | Marketing / IA / store / legal / hub page |
| https://ufixit.com/sitemap/ | SiteMap | Y | REST+sitemap+nav | **KEEP** | Marketing / IA / store / legal / hub page |
| https://ufixit.com/?team=dustin-r-manager-tyler | Dustin R. – Manager, Tyler | N | REST | **DROP** | Individual team CPT query URL — rolls up to /about-us/team-members/ |
| https://ufixit.com/?team=eric-w-senior-technical-advisor-south-dallas-store | Eric W.- Senior Technical Advisor, South Dallas | N | REST | **DROP** | Individual team CPT query URL — rolls up to /about-us/team-members/ |
| https://ufixit.com/?team=jaime-c-sales-south-dallas | Jaime C. – Sales, Arlington | N | REST | **DROP** | Individual team CPT query URL — rolls up to /about-us/team-members/ |
| https://ufixit.com/?team=khristopher-s-store-manager-east-dallas | Khristopher S. – Store Manager, East Dallas | N | REST | **DROP** | Individual team CPT query URL — rolls up to /about-us/team-members/ |
| https://ufixit.com/?team=tony-m-sales-south-dallas | Tony M. – Sales, South Dallas | N | REST | **DROP** | Individual team CPT query URL — rolls up to /about-us/team-members/ |
| https://ufixit.com/?testimonials=erick-scott | Erick Scott | N | REST+sitemap | **DROP** | Individual testimonial CPT query URL — thin; content rolls up to feedback hub |
| https://ufixit.com/?testimonials=kirby-j | Kirby J | N | REST+sitemap | **DROP** | Individual testimonial CPT query URL — thin; content rolls up to feedback hub |
| https://ufixit.com/?testimonials=lisa-panelli-valentin | Lisa Panelli-Valentin | N | REST+sitemap | **DROP** | Individual testimonial CPT query URL — thin; content rolls up to feedback hub |
| https://ufixit.com/?testimonials=rosamari-williamson | Rosamari Williamson | N | REST+sitemap | **DROP** | Individual testimonial CPT query URL — thin; content rolls up to feedback hub |
| https://ufixit.com/?videos={slug} | [PATTERN] 60 video CPT entries | N | REST | **DROP** | DROP 60 video CPT query URLs (?videos=) — no public pretty permalinks in sitemap; how-to content overlaps Repair Tips / DIY. List retained in discovery JSON if needed for archive. |
| https://ufixit.com/appliances/3-wing-fan-blade/ | 3 Wing Fan Blade | N | REST+sitemap | **DROP** | Individual appliance part landing (SKU-like WP page) — proto uses appliance hubs + sample PDPs; catalog archive SoT pending |
| https://ufixit.com/appliances/agitator-dogs-su-lp338/ | Agitator Dogs Washer Part # JA 80040 | N | REST+sitemap | **DROP** | Individual appliance part landing (SKU-like WP page) — proto uses appliance hubs + sample PDPs; catalog archive SoT pending |
| https://ufixit.com/appliances/bake-element-erb44x200/ | Bake Element ERB44X200 | N | REST+sitemap | **DROP** | Individual appliance part landing (SKU-like WP page) — proto uses appliance hubs + sample PDPs; catalog archive SoT pending |
| https://ufixit.com/appliances/bake-element-erb44x5082/ | Bake Element ERB44X5082 | N | REST+sitemap | **DROP** | Individual appliance part landing (SKU-like WP page) — proto uses appliance hubs + sample PDPs; catalog archive SoT pending |
| https://ufixit.com/appliances/blower-assembly/ | Blower Assembly | N | REST+sitemap | **DROP** | Individual appliance part landing (SKU-like WP page) — proto uses appliance hubs + sample PDPs; catalog archive SoT pending |
| https://ufixit.com/appliances/blower-motor-mr-10464/ | Blower Motor MR 10464 | N | REST+sitemap | **DROP** | Individual appliance part landing (SKU-like WP page) — proto uses appliance hubs + sample PDPs; catalog archive SoT pending |
| https://ufixit.com/appliances/condenser-fan-motor-mr-10458/ | Air Conditioner Motor MR 10458 | N | REST+sitemap | **DROP** | Individual appliance part landing (SKU-like WP page) — proto uses appliance hubs + sample PDPs; catalog archive SoT pending |
| https://ufixit.com/appliances/coupler-ja-285753/ | Coupler JA 285753 | N | REST+sitemap | **DROP** | Individual appliance part landing (SKU-like WP page) — proto uses appliance hubs + sample PDPs; catalog archive SoT pending |
| https://ufixit.com/appliances/dampening-strap-ja-wh1x2727/ | Dampening Strap JA WH1X2727 | N | REST+sitemap | **DROP** | Individual appliance part landing (SKU-like WP page) — proto uses appliance hubs + sample PDPs; catalog archive SoT pending |
| https://ufixit.com/appliances/defrost-thermostat-erml45/ | Defrost Thermostat ERML45 | N | REST+sitemap | **DROP** | Individual appliance part landing (SKU-like WP page) — proto uses appliance hubs + sample PDPs; catalog archive SoT pending |
| https://ufixit.com/appliances/direct-drive-blower-wheels/ | Direct Drive Blower Wheels | N | REST+sitemap | **DROP** | Individual appliance part landing (SKU-like WP page) — proto uses appliance hubs + sample PDPs; catalog archive SoT pending |
| https://ufixit.com/appliances/dishwasher-pump-er-gedwm/ | Dishwasher Pump ER GEDWM | N | REST+sitemap | **DROP** | Individual appliance part landing (SKU-like WP page) — proto uses appliance hubs + sample PDPs; catalog archive SoT pending |
| https://ufixit.com/appliances/door-gasket-right-hand-erwd8x227/ | Door gasket (right hand) ERWD8X227 | N | REST+sitemap | **DROP** | Individual appliance part landing (SKU-like WP page) — proto uses appliance hubs + sample PDPs; catalog archive SoT pending |
| https://ufixit.com/appliances/drain-pump-er21001906/ | Drain pump ER21001906 | N | REST+sitemap | **DROP** | Individual appliance part landing (SKU-like WP page) — proto uses appliance hubs + sample PDPs; catalog archive SoT pending |
| https://ufixit.com/appliances/drain-pump-er3363394/ | Drain pump ER3363394 | N | REST+sitemap | **DROP** | Individual appliance part landing (SKU-like WP page) — proto uses appliance hubs + sample PDPs; catalog archive SoT pending |
| https://ufixit.com/appliances/drip-pan-6-inch-wb32x5075/ | Drip Pan 6 inch GE WB32X5075 | N | REST+sitemap | **DROP** | Individual appliance part landing (SKU-like WP page) — proto uses appliance hubs + sample PDPs; catalog archive SoT pending |
| https://ufixit.com/appliances/dryer-bearing-kit-ja-we25x205/ | Dryer Bearing Kit JA WE25X205 | N | REST+sitemap | **DROP** | Individual appliance part landing (SKU-like WP page) — proto uses appliance hubs + sample PDPs; catalog archive SoT pending |
| https://ufixit.com/appliances/dryer-drum-bearing-erwe3m26/ | Dryer Drum Bearing ERWE3M26 | N | REST+sitemap | **DROP** | Individual appliance part landing (SKU-like WP page) — proto uses appliance hubs + sample PDPs; catalog archive SoT pending |
| https://ufixit.com/appliances/dryer-flame-sensor-er338906/ | Dryer Flame Sensor ER338906 | N | REST+sitemap | **DROP** | Individual appliance part landing (SKU-like WP page) — proto uses appliance hubs + sample PDPs; catalog archive SoT pending |
| https://ufixit.com/appliances/dryer-heating-element-na-279838/ | Dryer Heating Element NA 279838 | N | REST+sitemap | **DROP** | Individual appliance part landing (SKU-like WP page) — proto uses appliance hubs + sample PDPs; catalog archive SoT pending |
| https://ufixit.com/appliances/dryer-heating-element-na-3387747/ | Dryer Heating Element NA 3387747 | N | REST+sitemap | **DROP** | Individual appliance part landing (SKU-like WP page) — proto uses appliance hubs + sample PDPs; catalog archive SoT pending |
| https://ufixit.com/appliances/dryer-motor-ja-279827/ | Dryer Motor SU SM279827 (279827) | N | REST+sitemap | **DROP** | Individual appliance part landing (SKU-like WP page) — proto uses appliance hubs + sample PDPs; catalog archive SoT pending |
| https://ufixit.com/appliances/dual-capacitor/ | Dual Air Conditioner Capacitor | N | REST+sitemap | **DROP** | Individual appliance part landing (SKU-like WP page) — proto uses appliance hubs + sample PDPs; catalog archive SoT pending |
| https://ufixit.com/appliances/furnace-control-board-icm280/ | Furnace Control Board ICM280 | N | REST+sitemap | **DROP** | Individual appliance part landing (SKU-like WP page) — proto uses appliance hubs + sample PDPs; catalog archive SoT pending |
| https://ufixit.com/appliances/furnace-control-module-js-l37-928/ | Furnace Control Module JS L37-928 | N | REST+sitemap | **DROP** | Individual appliance part landing (SKU-like WP page) — proto uses appliance hubs + sample PDPs; catalog archive SoT pending |
| https://ufixit.com/appliances/furnace-igniter-erb1401018s/ | Furnace Igniter ERB1401018S | N | REST+sitemap | **DROP** | Individual appliance part landing (SKU-like WP page) — proto uses appliance hubs + sample PDPs; catalog archive SoT pending |
| https://ufixit.com/appliances/gas-valve-js-l37-436/ | Gas Valve JS L37-436 | N | REST+sitemap | **DROP** | Individual appliance part landing (SKU-like WP page) — proto uses appliance hubs + sample PDPs; catalog archive SoT pending |
| https://ufixit.com/appliances/ge-drain-hose-ejssd6-ge/ | GE Drain Hose EJSSD6-GE | N | REST+sitemap | **DROP** | Individual appliance part landing (SKU-like WP page) — proto uses appliance hubs + sample PDPs; catalog archive SoT pending |
| https://ufixit.com/appliances/high-limit-kit-na-279769/ | High Limit Thermostat & Fuse Kit NA 279769 | N | REST+sitemap | **DROP** | Individual appliance part landing (SKU-like WP page) — proto uses appliance hubs + sample PDPs; catalog archive SoT pending |
| https://ufixit.com/appliances/high-limit-kit-na-3977767/ | High Limit Dryer Thermostat Kit NA 3977767 | N | REST+sitemap | **DROP** | Individual appliance part landing (SKU-like WP page) — proto uses appliance hubs + sample PDPs; catalog archive SoT pending |
| https://ufixit.com/appliances/ice-maker-ergeim/ | Ice Maker ERGEIM | N | REST+sitemap | **DROP** | Individual appliance part landing (SKU-like WP page) — proto uses appliance hubs + sample PDPs; catalog archive SoT pending |
| https://ufixit.com/appliances/ice-maker-erwim/ | Ice Maker ERWIM | N | REST+sitemap | **DROP** | Individual appliance part landing (SKU-like WP page) — proto uses appliance hubs + sample PDPs; catalog archive SoT pending |
| https://ufixit.com/appliances/inlet-adapter-er34fht/ | Inlet Adapter ER34FHT | N | REST+sitemap | **DROP** | Individual appliance part landing (SKU-like WP page) — proto uses appliance hubs + sample PDPs; catalog archive SoT pending |
| https://ufixit.com/appliances/lid-lock-assembly-er134101800/ | Lid Lock Assembly ER134101800 | N | REST+sitemap | **DROP** | Individual appliance part landing (SKU-like WP page) — proto uses appliance hubs + sample PDPs; catalog archive SoT pending |
| https://ufixit.com/appliances/lid-switch-er279347/ | Lid Switch ER279347 | N | REST+sitemap | **DROP** | Individual appliance part landing (SKU-like WP page) — proto uses appliance hubs + sample PDPs; catalog archive SoT pending |
| https://ufixit.com/appliances/lid-switch-ja-3949247/ | Lid Switch JA 3949247 | N | REST+sitemap | **DROP** | Individual appliance part landing (SKU-like WP page) — proto uses appliance hubs + sample PDPs; catalog archive SoT pending |
| https://ufixit.com/appliances/motor-air-conditioner-capacitor/ | Motor Air Conditioner Capacitor | N | REST+sitemap | **DROP** | Individual appliance part landing (SKU-like WP page) — proto uses appliance hubs + sample PDPs; catalog archive SoT pending |
| https://ufixit.com/appliances/motor-capacitor/ | Motor Air Conditioner Capacitor | N | REST+sitemap | **DROP** | Individual appliance part landing (SKU-like WP page) — proto uses appliance hubs + sample PDPs; catalog archive SoT pending |
| https://ufixit.com/appliances/oven-igniter-ergr403/ | Oven Igniter ERGR403 | N | REST+sitemap | **DROP** | Individual appliance part landing (SKU-like WP page) — proto uses appliance hubs + sample PDPs; catalog archive SoT pending |
| https://ufixit.com/appliances/oven-igniter-erig35/ | Oven Igniter ERIG35 | N | REST+sitemap | **DROP** | Individual appliance part landing (SKU-like WP page) — proto uses appliance hubs + sample PDPs; catalog archive SoT pending |
| https://ufixit.com/appliances/oven-igniter-erig9998/ | Oven Igniter ERIG9998 | N | REST+sitemap | **DROP** | Individual appliance part landing (SKU-like WP page) — proto uses appliance hubs + sample PDPs; catalog archive SoT pending |
| https://ufixit.com/appliances/refrigerator-filter-ermwf/ | Refrigerator Filter ERMWF | N | REST+sitemap | **DROP** | Individual appliance part landing (SKU-like WP page) — proto uses appliance hubs + sample PDPs; catalog archive SoT pending |
| https://ufixit.com/appliances/soap-dispenser-erudwd2/ | Soap Dispenser ERUDWD2 | N | REST+sitemap | **DROP** | Individual appliance part landing (SKU-like WP page) — proto uses appliance hubs + sample PDPs; catalog archive SoT pending |
| https://ufixit.com/appliances/transformer-mr-50203/ | Transformer MR 50203 | N | REST+sitemap | **DROP** | Individual appliance part landing (SKU-like WP page) — proto uses appliance hubs + sample PDPs; catalog archive SoT pending |
| https://ufixit.com/appliances/transformer/ | Transformer | N | REST+sitemap | **DROP** | Individual appliance part landing (SKU-like WP page) — proto uses appliance hubs + sample PDPs; catalog archive SoT pending |
| https://ufixit.com/appliances/universal-drain-hose-or-extension-ja-dwdh78/ | Universal Drain Hose or extension JA DWDH78 | N | REST+sitemap | **DROP** | Individual appliance part landing (SKU-like WP page) — proto uses appliance hubs + sample PDPs; catalog archive SoT pending |
| https://ufixit.com/appliances/universal-washer-drain-hose-ejssd6/ | Universal Washer Drain Hose EJSSD6 | N | REST+sitemap | **DROP** | Individual appliance part landing (SKU-like WP page) — proto uses appliance hubs + sample PDPs; catalog archive SoT pending |
| https://ufixit.com/appliances/wall-thermostat-icm-sc1001/ | Wall Thermostat ICM SC1001 | N | REST+sitemap | **DROP** | Individual appliance part landing (SKU-like WP page) — proto uses appliance hubs + sample PDPs; catalog archive SoT pending |
| https://ufixit.com/appliances/wall-thermostat/ | Wall Thermostat | N | REST+sitemap | **DROP** | Individual appliance part landing (SKU-like WP page) — proto uses appliance hubs + sample PDPs; catalog archive SoT pending |
| https://ufixit.com/appliances/washer-clutch-er285785/ | Washer Clutch ER285785 | N | REST+sitemap | **DROP** | Individual appliance part landing (SKU-like WP page) — proto uses appliance hubs + sample PDPs; catalog archive SoT pending |
| https://ufixit.com/appliances/washer-inlet-valve-ja-wv1/ | Washer Water Inlet Valve JA WV1 | N | REST+sitemap | **DROP** | Individual appliance part landing (SKU-like WP page) — proto uses appliance hubs + sample PDPs; catalog archive SoT pending |
| https://ufixit.com/appliances/washer-motor-glide-kit-er205000/ | Washer Motor Glide Kit ER205000 | N | REST+sitemap | **DROP** | Individual appliance part landing (SKU-like WP page) — proto uses appliance hubs + sample PDPs; catalog archive SoT pending |
| https://ufixit.com/appliances/water-filter-erwf270/ | Water Filter ERWF270 | N | REST+sitemap | **DROP** | Individual appliance part landing (SKU-like WP page) — proto uses appliance hubs + sample PDPs; catalog archive SoT pending |
| https://ufixit.com/appliances/water-filter-erwfcb/ | Water Filter ERWFCB | N | REST+sitemap | **DROP** | Individual appliance part landing (SKU-like WP page) — proto uses appliance hubs + sample PDPs; catalog archive SoT pending |
| https://ufixit.com/author/lisa/ | Author: lisa | N | sitemap | **DROP** | Author archive — no unique marketing content |
| https://ufixit.com/author/nicole/ | Author: nicole | N | sitemap | **DROP** | Author archive — no unique marketing content |
| https://ufixit.com/author/wla_admin/ | Author: wla_admin | N | sitemap | **DROP** | Author archive — no unique marketing content |
| https://ufixit.com/cart/ | Cart | Y | REST+sitemap | **DROP** | WooCommerce cart — ecommerce chrome, not marketing content |
| https://ufixit.com/checkout/ | Checkout | N | REST+sitemap | **DROP** | WooCommerce checkout — ecommerce chrome |
| https://ufixit.com/my-account/ | My account | N | REST+sitemap | **DROP** | Account portal — not marketing |
| https://ufixit.com/product/{sku}/ | [PATTERN] 434 individual product SKUs | N | sitemap+WooStore(x-wp-total:438) | **DROP** | DROP 434 product SKUs (+ shop listed separately). Woo store API total products=438; sitemap PDPs=436. Proto uses shop hub + product_cat hubs + 1–2 sample PDPs. Full catalog archive SoT pending at /workspace/ufixit-prototype/. |
| https://ufixit.com/sample-page/ | Sample Page | N | REST+sitemap | **DROP** | Default WP sample page — junk |

## Summary for Proton Bob — flat HTML KEEP list

Suggested filenames under prototype root (flatten path with `--`). Catalog SKUs intentionally omitted except 2 samples.

| Suggested file | URL | Title |
|----------------|-----|-------|
| `index.html` | https://ufixit.com/ | Home |
| `about-us.html` | https://ufixit.com/about-us/ | About Us |
| `about-us--mission.html` | https://ufixit.com/about-us/mission/ | U-FIX-IT Mission |
| `about-us--really-matters.html` | https://ufixit.com/about-us/really-matters/ | U-FIX-IT Gives Back |
| `about-us--store-hours.html` | https://ufixit.com/about-us/store-hours/ | Store Hours & Holidays |
| `about-us--team-members.html` | https://ufixit.com/about-us/team-members/ | Our Appliance Repair Experts |
| `about-us--warranty-returns.html` | https://ufixit.com/about-us/warranty-returns/ | Appliance Parts Warranty & Returns |
| `appliance-repair-tips.html` | https://ufixit.com/appliance-repair-tips/ | Appliance Repair Tips |
| `appliances.html` | https://ufixit.com/appliances/ | Appliances |
| `appliances--30-expert-bosch-appliance-repair-fast-reliable-fixes-near-you.html` | https://ufixit.com/appliances/30-expert-bosch-appliance-repair-fast-reliable-fixes-near-you/ | Expert Bosch Appliance Repair |
| `appliances--air-conditioner-parts.html` | https://ufixit.com/appliances/air-conditioner-parts/ | Air Conditioner Repair Parts |
| `appliances--dishwasher-parts.html` | https://ufixit.com/appliances/dishwasher-parts/ | Dishwasher Repair Parts |
| `appliances--dryer-parts.html` | https://ufixit.com/appliances/dryer-parts/ | Dryer Repair Parts |
| `appliances--furnace-parts.html` | https://ufixit.com/appliances/furnace-parts/ | Furnace Repair Parts |
| `appliances--how-to-choose-the-right-hotpoint-appliance-for-your-home.html` | https://ufixit.com/appliances/how-to-choose-the-right-hotpoint-appliance-for-your-home/ | How to Choose the Right Hotpoint Appliance for Your Home |
| `appliances--ranges-oven-parts.html` | https://ufixit.com/appliances/ranges-oven-parts/ | Ranges & Oven Repair Parts |
| `appliances--refrigerator-parts.html` | https://ufixit.com/appliances/refrigerator-parts/ | Refrigerator Repair Parts |
| `appliances--washer-parts.html` | https://ufixit.com/appliances/washer-parts/ | Washer Repair Parts |
| `appliances--why-monogram-appliances-are-the-ultimate-choice-for-luxury-kitchens.html` | https://ufixit.com/appliances/why-monogram-appliances-are-the-ultimate-choice-for-luxury-kitchens/ | Why Monogram Appliances Are the Ultimate Choice for Luxury Kitchens |
| `category--appliances.html` | https://ufixit.com/category/appliances/ | Appliances (blog category) |
| `category--diy-tips.html` | https://ufixit.com/category/diy-tips/ | Diy Tips (blog category) |
| `category--dryer.html` | https://ufixit.com/category/dryer/ | Dryer (blog category) |
| `category--news.html` | https://ufixit.com/category/news/ | News (blog category) |
| `category--refrigerator.html` | https://ufixit.com/category/refrigerator/ | Refrigerator (blog category) |
| `contact-us.html` | https://ufixit.com/contact-us/ | Contact Us |
| `contact-us--arlington-appliance-parts-store.html` | https://ufixit.com/contact-us/arlington-appliance-parts-store/ | Arlington Appliance Parts Store |
| `contact-us--east-dallas.html` | https://ufixit.com/contact-us/east-dallas/ | East Dallas Appliance Parts Store |
| `contact-us--south-dallas.html` | https://ufixit.com/contact-us/south-dallas/ | South Dallas Appliance Parts Store |
| `contact-us--tyler-tx.html` | https://ufixit.com/contact-us/tyler-tx/ | Tyler TX Appliance Parts Store |
| `diy-tips.html` | https://ufixit.com/diy-tips/ | DIY Tips |
| `diy-tips--4-household-appliance-myths.html` | https://ufixit.com/diy-tips/4-household-appliance-myths/ | 4 Household Appliance Myths |
| `diy-tips--benefits-of-fixing-appliances-yourself-instead-of-replacing-them.html` | https://ufixit.com/diy-tips/benefits-of-fixing-appliances-yourself-instead-of-replacing-them/ | Benefits of Fixing Appliances Yourself Instead of Replacing Them |
| `diy-tips--best-replacement-parts-for-top-appliance-brands.html` | https://ufixit.com/diy-tips/best-replacement-parts-for-top-appliance-brands/ | Best Replacement Parts for Top Appliance Brands |
| `diy-tips--complete-guide-to-dishwasher-parts.html` | https://ufixit.com/diy-tips/complete-guide-to-dishwasher-parts/ | Complete Guide to Dishwasher Parts |
| `diy-tips--discover-expert-device-appliance-repair-services-fast-reliable-solutio.html` | https://ufixit.com/diy-tips/discover-expert-device-appliance-repair-services-fast-reliable-solutions/ | Discover Expert Device & Appliance Repair Services \| Fast & Reliable Solutions |
| `diy-tips--electrolux-appliance-repair-guide-troubleshooting-common-issues-error-.html` | https://ufixit.com/diy-tips/electrolux-appliance-repair-guide-troubleshooting-common-issues-error-codes-genuine-parts/ | Electrolux Appliance Repair Guide |
| `diy-tips--essential-ac-parts-guide.html` | https://ufixit.com/diy-tips/essential-ac-parts-guide/ | Essential AC Parts Guide: |
| `diy-tips--expert-customer-diy-support-for-your-appliance-repair-parts-needs.html` | https://ufixit.com/diy-tips/expert-customer-diy-support-for-your-appliance-repair-parts-needs/ | Expert Customer DIY Support for Your Appliance Repair & Parts Needs |
| `diy-tips--find-quality-range-oven-parts-expert-guide-to-replacement-parts.html` | https://ufixit.com/diy-tips/find-quality-range-oven-parts-expert-guide-to-replacement-parts/ | Find Quality Range & Oven Parts \| Expert Guide to Replacement Parts |
| `diy-tips--find-reliable-major-appliance-repair.html` | https://ufixit.com/diy-tips/find-reliable-major-appliance-repair/ | Find Reliable Major Appliance Repair |
| `diy-tips--gas-furnace-burner-goes-out.html` | https://ufixit.com/diy-tips/gas-furnace-burner-goes-out/ | Gas Furnace – Burner Goes Out |
| `diy-tips--home-air-conditioner-not-cooling.html` | https://ufixit.com/diy-tips/home-air-conditioner-not-cooling/ | Air conditioner not cooling – outdoor unit not running |
| `diy-tips--how-to-find-the-right-replacement-parts-for-your-appliances.html` | https://ufixit.com/diy-tips/how-to-find-the-right-replacement-parts-for-your-appliances/ | How to Find the Right Replacement Parts for Your Appliances |
| `diy-tips--how-to-find-your-appliance-model-number-and-order-the-right-part.html` | https://ufixit.com/diy-tips/how-to-find-your-appliance-model-number-and-order-the-right-part/ | How to Find Your Appliance Model Number and Order the Right Part |
| `diy-tips--ice-maker-not-working-try-this.html` | https://ufixit.com/diy-tips/ice-maker-not-working-try-this/ | Ice Maker Not Working? Try these easy steps. |
| `diy-tips--lg-appliance-parts-guide.html` | https://ufixit.com/diy-tips/lg-appliance-parts-guide/ | LG Appliance Parts Guide |
| `diy-tips--on-doc-12-should-you-repair-or-replace-your-appliance-a-cost-benefit-g.html` | https://ufixit.com/diy-tips/on-doc-12-should-you-repair-or-replace-your-appliance-a-cost-benefit-guide-for-diy-homeowners/ | Should You Repair or Replace Your Appliance? |
| `diy-tips--refrigerator-defrost-problems.html` | https://ufixit.com/diy-tips/refrigerator-defrost-problems/ | Refrigerator Defrost problems – Diagnosing the most common malfunction of refrigerators and freezers |
| `diy-tips--thermador-appliance-repair-guide-luxury-kitchen-troubleshooting-error-.html` | https://ufixit.com/diy-tips/thermador-appliance-repair-guide-luxury-kitchen-troubleshooting-error-codes-genuine-parts/ | Thermador Appliance Repair Guide |
| `diy-tips--viking-appliance-repair-guide-luxury-kitchen-troubleshooting-error-cod.html` | https://ufixit.com/diy-tips/viking-appliance-repair-guide-luxury-kitchen-troubleshooting-error-codes-genuine-parts/ | Viking Appliance Repair Guide |
| `diy-tips--whirlpool-dryer-not-heating.html` | https://ufixit.com/diy-tips/whirlpool-dryer-not-heating/ | Whirlpool Dryer Not Heating: Causes and Troubleshooting Tips |
| `diy-tips--whirlpool-washer-not-fill.html` | https://ufixit.com/diy-tips/whirlpool-washer-not-fill/ | What can be wrong when a Whirlpool washer will not fill with water? |
| `dryer--complete-dryer-parts-diagram-your-guide-to-diy-dryer-repair.html` | https://ufixit.com/dryer/complete-dryer-parts-diagram-your-guide-to-diy-dryer-repair/ | Complete Dryer Parts Diagram: Your Guide to DIY Dryer Repair |
| `find-your-brand.html` | https://ufixit.com/find-your-brand/ | Find Your Brand |
| `find-your-brand--admiral.html` | https://ufixit.com/find-your-brand/admiral/ | Admiral |
| `find-your-brand--amana.html` | https://ufixit.com/find-your-brand/amana/ | Amana |
| `find-your-brand--appliance-parts-lg.html` | https://ufixit.com/find-your-brand/appliance-parts-lg/ | LG |
| `find-your-brand--appliance-parts-whirpool.html` | https://ufixit.com/find-your-brand/appliance-parts-whirpool/ | Whirlpool |
| `find-your-brand--bosch.html` | https://ufixit.com/find-your-brand/bosch/ | Bosch |
| `find-your-brand--brown.html` | https://ufixit.com/find-your-brand/brown/ | Brown |
| `find-your-brand--caloric.html` | https://ufixit.com/find-your-brand/caloric/ | Caloric |
| `find-your-brand--crosley.html` | https://ufixit.com/find-your-brand/crosley/ | Crosley |
| `find-your-brand--dacor.html` | https://ufixit.com/find-your-brand/dacor/ | Dacor |
| `find-your-brand--electrolux.html` | https://ufixit.com/find-your-brand/electrolux/ | Electrolux |
| `find-your-brand--frigidaire-appliance-parts.html` | https://ufixit.com/find-your-brand/frigidaire-appliance-parts/ | Frigidaire |
| `find-your-brand--gaggenau.html` | https://ufixit.com/find-your-brand/gaggenau/ | Gaggenau |
| `find-your-brand--ge-general-electric.html` | https://ufixit.com/find-your-brand/ge-general-electric/ | GE |
| `find-your-brand--gibson.html` | https://ufixit.com/find-your-brand/gibson/ | Gibson |
| `find-your-brand--glenwood.html` | https://ufixit.com/find-your-brand/glenwood/ | Glenwood |
| `find-your-brand--haier.html` | https://ufixit.com/find-your-brand/haier/ | Haier |
| `find-your-brand--hardwick.html` | https://ufixit.com/find-your-brand/hardwick/ | Hardwick |
| `find-your-brand--hotpoint.html` | https://ufixit.com/find-your-brand/hotpoint/ | Hotpoint |
| `find-your-brand--jenn-air.html` | https://ufixit.com/find-your-brand/jenn-air/ | Jenn Air |
| `find-your-brand--kelvinator.html` | https://ufixit.com/find-your-brand/kelvinator/ | Kelvinator |
| `find-your-brand--kenmore-appliances.html` | https://ufixit.com/find-your-brand/kenmore-appliances/ | Kenmore |
| `find-your-brand--maytag-appliance-parts.html` | https://ufixit.com/find-your-brand/maytag-appliance-parts/ | Maytag |
| `find-your-brand--roper.html` | https://ufixit.com/find-your-brand/roper/ | Roper |
| `find-your-brand--samsung.html` | https://ufixit.com/find-your-brand/samsung/ | Samsung |
| `find-your-brand--scotsman.html` | https://ufixit.com/find-your-brand/scotsman/ | Scotsman |
| `find-your-brand--sears.html` | https://ufixit.com/find-your-brand/sears/ | Sears |
| `find-your-brand--speed-queen.html` | https://ufixit.com/find-your-brand/speed-queen/ | Speed Queen |
| `find-your-brand--sub-zero.html` | https://ufixit.com/find-your-brand/sub-zero/ | Sub Zero |
| `find-your-brand--sunray.html` | https://ufixit.com/find-your-brand/sunray/ | Sunray |
| `find-your-brand--tappan.html` | https://ufixit.com/find-your-brand/tappan/ | Tappan |
| `find-your-brand--thermador.html` | https://ufixit.com/find-your-brand/thermador/ | Thermador |
| `find-your-brand--u-line.html` | https://ufixit.com/find-your-brand/u-line/ | U-LINE |
| `find-your-brand--wolf.html` | https://ufixit.com/find-your-brand/wolf/ | Wolf |
| `news--home-air-conditioner-will-not-cool-outdoor-unit-condenser-not-running.html` | https://ufixit.com/news/home-air-conditioner-will-not-cool-outdoor-unit-condenser-not-running/ | Home air conditioner will not cool – outdoor unit (condenser) not running |
| `news--refrigerator-will-not-dispense-water-produce-ice-possible-quick-fix.html` | https://ufixit.com/news/refrigerator-will-not-dispense-water-produce-ice-possible-quick-fix/ | Two “not so obvious” things to check that can stop all waterflow in your refrigerator. |
| `news--save-time-save-money-u-fix.html` | https://ufixit.com/news/save-time-save-money-u-fix/ | Save time, save money – U-FIX-IT |
| `privacy-policy.html` | https://ufixit.com/privacy-policy/ | Privacy Policy |
| `product-category--accessories.html` | https://ufixit.com/product-category/accessories/ | Accessories |
| `product-category--accessories--dryer-accessories.html` | https://ufixit.com/product-category/accessories/dryer-accessories/ | Dryer Accessories |
| `product-category--air-conditioner-parts.html` | https://ufixit.com/product-category/air-conditioner-parts/ | Air Conditioner Parts |
| `product-category--dishwasher-accessories.html` | https://ufixit.com/product-category/dishwasher-accessories/ | Dishwasher Accessories |
| `product-category--dishwasher-parts.html` | https://ufixit.com/product-category/dishwasher-parts/ | Washer Parts |
| `product-category--dishwasher-parts--bosch-dishwasher-parts.html` | https://ufixit.com/product-category/dishwasher-parts/bosch-dishwasher-parts/ | Washer Parts |
| `product-category--dishwasher-parts--electrolux-dishwasher-parts.html` | https://ufixit.com/product-category/dishwasher-parts/electrolux-dishwasher-parts/ | Washer Parts |
| `product-category--dishwasher-parts--frigidaire-dishwasher-parts.html` | https://ufixit.com/product-category/dishwasher-parts/frigidaire-dishwasher-parts/ | Washer Parts |
| `product-category--dishwasher-parts--kenmore-dishwasher-parts.html` | https://ufixit.com/product-category/dishwasher-parts/kenmore-dishwasher-parts/ | Washer Parts |
| `product-category--dishwasher-parts--kitchenaid-dishwasher-parts.html` | https://ufixit.com/product-category/dishwasher-parts/kitchenaid-dishwasher-parts/ | Washer Parts |
| `product-category--dishwasher-parts--lg-dishwasher-parts.html` | https://ufixit.com/product-category/dishwasher-parts/lg-dishwasher-parts/ | Washer Parts |
| `product-category--dishwasher-parts--maytag-parts.html` | https://ufixit.com/product-category/dishwasher-parts/maytag-parts/ | Maytag Parts |
| `product-category--dishwasher-parts--whirlpool-dishwasher-parts.html` | https://ufixit.com/product-category/dishwasher-parts/whirlpool-dishwasher-parts/ | Whirlpool Dishwasher Parts |
| `product-category--dryer-parts.html` | https://ufixit.com/product-category/dryer-parts/ | Dryer Parts |
| `product-category--dryer-parts--crosley-dryer-parts.html` | https://ufixit.com/product-category/dryer-parts/crosley-dryer-parts/ | Dryer Parts |
| `product-category--dryer-parts--electrolux-dryer-parts.html` | https://ufixit.com/product-category/dryer-parts/electrolux-dryer-parts/ | Electrolux Dryer Parts |
| `product-category--dryer-parts--frigidaire-dryer-parts.html` | https://ufixit.com/product-category/dryer-parts/frigidaire-dryer-parts/ | Frigidaire Dryer Parts |
| `product-category--dryer-parts--general-electric-ge-dryer-parts.html` | https://ufixit.com/product-category/dryer-parts/general-electric-ge-dryer-parts/ | General Electric (GE) Dryer Parts |
| `product-category--dryer-parts--kenmore-dryer-parts.html` | https://ufixit.com/product-category/dryer-parts/kenmore-dryer-parts/ | Kenmore Dryer Parts |
| `product-category--dryer-parts--lg-dryer-parts.html` | https://ufixit.com/product-category/dryer-parts/lg-dryer-parts/ | LG Dryer Parts |
| `product-category--dryer-parts--maytag-dryer-parts.html` | https://ufixit.com/product-category/dryer-parts/maytag-dryer-parts/ | Maytag Dryer Parts |
| `product-category--dryer-parts--montgomery-wards-dryer-parts.html` | https://ufixit.com/product-category/dryer-parts/montgomery-wards-dryer-parts/ | Montgomery Wards Dryer Parts |
| `product-category--dryer-parts--roper-dryer-parts.html` | https://ufixit.com/product-category/dryer-parts/roper-dryer-parts/ | Roper Dryer Parts |
| `product-category--dryer-parts--samsung-dryer-parts.html` | https://ufixit.com/product-category/dryer-parts/samsung-dryer-parts/ | Samsung Dryer Parts |
| `product-category--dryer-parts--sears-dryer-parts.html` | https://ufixit.com/product-category/dryer-parts/sears-dryer-parts/ | Sears Dryer Parts |
| `product-category--dryer-parts--whirlpool-dryer-parts.html` | https://ufixit.com/product-category/dryer-parts/whirlpool-dryer-parts/ | Whirlpool Dryer Parts |
| `product-category--furnace-parts.html` | https://ufixit.com/product-category/furnace-parts/ | Furnace Parts |
| `product-category--microwave-parts.html` | https://ufixit.com/product-category/microwave-parts/ | Microwave Parts |
| `product-category--range-oven-parts.html` | https://ufixit.com/product-category/range-oven-parts/ | Range & Oven Parts |
| `product-category--range-oven-parts--amana-range-oven-parts.html` | https://ufixit.com/product-category/range-oven-parts/amana-range-oven-parts/ | Range & Oven Parts |
| `product-category--range-oven-parts--electrolux-range-oven-parts.html` | https://ufixit.com/product-category/range-oven-parts/electrolux-range-oven-parts/ | Range & Oven Parts |
| `product-category--range-oven-parts--frigidaire-range-oven-parts.html` | https://ufixit.com/product-category/range-oven-parts/frigidaire-range-oven-parts/ | Range & Oven Parts |
| `product-category--range-oven-parts--ge-range-oven-parts.html` | https://ufixit.com/product-category/range-oven-parts/ge-range-oven-parts/ | Range & Oven Parts |
| `product-category--range-oven-parts--general-electric-range-oven-parts.html` | https://ufixit.com/product-category/range-oven-parts/general-electric-range-oven-parts/ | Range & Oven Parts |
| `product-category--range-oven-parts--kenmore-range-oven-parts.html` | https://ufixit.com/product-category/range-oven-parts/kenmore-range-oven-parts/ | Range & Oven Parts |
| `product-category--range-oven-parts--maytag-range-oven-parts.html` | https://ufixit.com/product-category/range-oven-parts/maytag-range-oven-parts/ | Range & Oven Parts |
| `product-category--range-oven-parts--sears-range-oven-parts.html` | https://ufixit.com/product-category/range-oven-parts/sears-range-oven-parts/ | Sears Range & Oven Parts |
| `product-category--range-oven-parts--whirlpool-range-oven-parts.html` | https://ufixit.com/product-category/range-oven-parts/whirlpool-range-oven-parts/ | Whirlpool Range & Oven Parts |
| `product-category--refrigerator-parts.html` | https://ufixit.com/product-category/refrigerator-parts/ | Refrigerator Parts |
| `product-category--refrigerator-parts--bosch-refrigerator-parts.html` | https://ufixit.com/product-category/refrigerator-parts/bosch-refrigerator-parts/ | Refrigerator Parts |
| `product-category--refrigerator-parts--electrolux-refrigerator-parts.html` | https://ufixit.com/product-category/refrigerator-parts/electrolux-refrigerator-parts/ | Refrigerator Parts |
| `product-category--refrigerator-parts--frigidaire-refrigerator-parts.html` | https://ufixit.com/product-category/refrigerator-parts/frigidaire-refrigerator-parts/ | Refrigerator Parts |
| `product-category--refrigerator-parts--ge-refrigerator-parts.html` | https://ufixit.com/product-category/refrigerator-parts/ge-refrigerator-parts/ | Refrigerator Parts |
| `product-category--refrigerator-parts--kenmore-refrigerator-parts.html` | https://ufixit.com/product-category/refrigerator-parts/kenmore-refrigerator-parts/ | Refrigerator Parts |
| `product-category--refrigerator-parts--kitchenaid-refrigerator-parts.html` | https://ufixit.com/product-category/refrigerator-parts/kitchenaid-refrigerator-parts/ | Refrigerator Parts |
| `product-category--refrigerator-parts--lg-refrigerator-parts.html` | https://ufixit.com/product-category/refrigerator-parts/lg-refrigerator-parts/ | Refrigerator Parts |
| `product-category--refrigerator-parts--samsung-refrigerator-parts.html` | https://ufixit.com/product-category/refrigerator-parts/samsung-refrigerator-parts/ | Samsung Refrigerator Parts |
| `product-category--refrigerator-parts--sears-refrigerator-parts.html` | https://ufixit.com/product-category/refrigerator-parts/sears-refrigerator-parts/ | Sears Refrigerator Parts |
| `product-category--refrigerator-parts--whirlpool-refrigerator-parts.html` | https://ufixit.com/product-category/refrigerator-parts/whirlpool-refrigerator-parts/ | Whirlpool Refrigerator Parts |
| `product-category--washer-parts.html` | https://ufixit.com/product-category/washer-parts/ | Washer Parts |
| `product-category--washer-parts--bosch-washer-parts.html` | https://ufixit.com/product-category/washer-parts/bosch-washer-parts/ | Washer Parts |
| `product-category--washer-parts--electrolux-washer-parts.html` | https://ufixit.com/product-category/washer-parts/electrolux-washer-parts/ | Washer Parts |
| `product-category--washer-parts--estate-washer-parts.html` | https://ufixit.com/product-category/washer-parts/estate-washer-parts/ | Washer Parts |
| `product-category--washer-parts--fisher-and-paykel-washer-parts.html` | https://ufixit.com/product-category/washer-parts/fisher-and-paykel-washer-parts/ | Washer Parts |
| `product-category--washer-parts--frigidaire-washer-parts.html` | https://ufixit.com/product-category/washer-parts/frigidaire-washer-parts/ | Washer Parts |
| `product-category--washer-parts--ge-washer-parts.html` | https://ufixit.com/product-category/washer-parts/ge-washer-parts/ | Washer Parts |
| `product-category--washer-parts--kenmore-washer-parts.html` | https://ufixit.com/product-category/washer-parts/kenmore-washer-parts/ | Washer Parts |
| `product-category--washer-parts--lg-washer-parts.html` | https://ufixit.com/product-category/washer-parts/lg-washer-parts/ | Washer Parts |
| `product-category--washer-parts--roper-washer-parts.html` | https://ufixit.com/product-category/washer-parts/roper-washer-parts/ | Washer Parts |
| `product-category--washer-parts--samsung-washer-parts.html` | https://ufixit.com/product-category/washer-parts/samsung-washer-parts/ | Washer Parts |
| `product-category--washer-parts--sears-washer-parts.html` | https://ufixit.com/product-category/washer-parts/sears-washer-parts/ | Washer Parts |
| `product-category--washer-parts--speed-queen-washer-parts.html` | https://ufixit.com/product-category/washer-parts/speed-queen-washer-parts/ | Washer Parts |
| `product-category--washer-parts--tappan-washer-parts.html` | https://ufixit.com/product-category/washer-parts/tappan-washer-parts/ | Washer Parts |
| `product-category--washer-parts--wci-washer-parts.html` | https://ufixit.com/product-category/washer-parts/wci-washer-parts/ | WCI Washer Parts |
| `product-category--washer-parts--westinghouse-washer-parts.html` | https://ufixit.com/product-category/washer-parts/westinghouse-washer-parts/ | Westinghouse Washer Parts |
| `product-category--washer-parts--whirlpool-washer-parts.html` | https://ufixit.com/product-category/washer-parts/whirlpool-washer-parts/ | Whirlpool Washer Parts |
| `product--er-w10190961-icemaker-for-whirlpool.html` | https://ufixit.com/product/er-w10190961-icemaker-for-whirlpool/ | Er W10190961 Icemaker For Whirlpool |
| `product--part-no-er-b3200-bake-element-for-electrolux.html` | https://ufixit.com/product/part-no-er-b3200-bake-element-for-electrolux/ | Part No Er B3200 Bake Element For Electrolux |
| `refrigerator--frigidaire-parts-diy-guide.html` | https://ufixit.com/refrigerator/frigidaire-parts-diy-guide/ | Frigidaire Parts – DIY Guide |
| `refrigerator--frigidaire-refrigerator-not-cooling-fix-it-yourself-with-the-right.html` | https://ufixit.com/refrigerator/frigidaire-refrigerator-not-cooling-fix-it-yourself-with-the-right-parts/ | Frigidaire Refrigerator Not Cooling? Fix It Yourself with the Right Parts |
| `share-feedback.html` | https://ufixit.com/share-feedback/ | Tell us About Your U-Fix-It Experience |
| `share-feedback--add-review.html` | https://ufixit.com/share-feedback/add-review/ | Add a Review |
| `share-feedback--tell-us-bad-experience.html` | https://ufixit.com/share-feedback/tell-us-bad-experience/ | We are sorry to hear it… |
| `shipping-appliance-parts.html` | https://ufixit.com/shipping-appliance-parts/ | Shipping Appliance Parts |
| `shipping-inquiry.html` | https://ufixit.com/shipping-inquiry/ | U-FIX-IT |
| `shop.html` | https://ufixit.com/shop/ | Shop |
| `sitemap.html` | https://ufixit.com/sitemap/ | SiteMap |

## Product DROP pattern (for dossier / archive handoff)

- **DROP 434 product SKUs** — proto uses `/shop/` + `product-category` hubs + **2 sample PDPs**:
  - KEEP sample: https://ufixit.com/product/er-w10190961-icemaker-for-whirlpool/
  - KEEP sample: https://ufixit.com/product/part-no-er-b3200-bake-element-for-electrolux/
- Woo `x-wp-total=438` products; sitemap lists shop + 436 `/product/` URLs.
- Full catalog content pull: archive SoT pending `/workspace/ufixit-prototype/` (Nancy).

## Notes

- Stack: WordPress (WP Engine) + WooCommerce + Yoast; REST at `/wp-json/`.
- Site spelling varies: **U-Fix-It**, **U-FIX-IT**, **UFixIt** — prefer on-page form per URL when writing copy later.
- No ranks or business claims in this file — discovery only.
