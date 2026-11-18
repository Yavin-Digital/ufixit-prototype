---
project: "U-FIX-IT Appliance Parts — Ecommerce Rebuild"
slug: "ufixit"
client: "U-FIX-IT Appliance Parts (contact: Lisa Harlan)"

agency: "Yavin"
agency_github_org: "Yavin-Digital"
agency_local_folder: ""        # not needed for the automated loop

# Mike decided 2026-11-18 3:53 PM CT: the rebuild moves to Node (live site is WordPress + WooCommerce).
# "ecomm" = Node ecommerce per SCOPE.md.template. Rath to confirm ecomm vs headless-ecomm (which keeps WooCommerce as the backend).
project_type: "ecomm"
scaffold_repo: "app-shell-scaffold"   # PIPELINE.md / template default for new Node first-builds
scaffold_version: ""                  # Project Setup writes the tag/SHA at clone time

# WordPress fields — only used if the rebuild lands on WordPress. Unset until the stack is chosen.
wp_parent_theme: ""
wp_child_theme_slug: ""
wp_plugins: []
shop_mode: ""
external_shop_url: ""
payment_gateway: ""
wpengine_install_name: ""      # not used on the Node path
webinar_archive_slug: ""
wp_cli_pages: []
wp_cli_menus: []

integrations:
  database: true               # parts catalog, orders, per-store stock, admin reporting
  auth: true                   # customer account + admin sign-in shown in prototype
  storage: false               # no uploads in the prototype
  email_sendgrid: false        # order confirmation email undecided (Rath to research, see Open Questions)
  payment_gateway: ""          # undecided (see Open Questions)
  woocommerce_api: false
  age_gate: false
  spot_prices_ticker: false
  webinar_categories: false
  google_analytics: false      # GA4 ID not provided (Rath to research, see Open Questions)
  ga4_ids: []
  chat_widget: false
  sms_ottertext: false

features:
  blog_mode: "cms"             # prototype has a DIY Tips hub, 20+ tip articles and News articles
  forms: "contact"             # contact, shipping inquiry, share-feedback pages
  auth: "credentials"          # account.html (customers); admin demo sign-in is a stub
  ecommerce: "checkout"        # cart, mock checkout, order confirmation, order lookup
  payments: ""                 # open: gateway not chosen (Rath, see Open Questions)
  affiliates: "none"
  qbo: "none"
  woo_sync: ""                 # open: Rath to decide (see Open Questions)
  campaign: "none"
  media: "none"

content_types:
  - id: "parts"
    label: "Parts catalog"
    mode: "cms"
    admin: true
    public_routes:
      - "/shop.html"
      - "/product-*.html"
    notes: "438 parts. Admin parts page covers part #, compatibility/replaces, cost/price, on hand, reorder level, supplier."
  - id: "stores"
    label: "Store locations"
    mode: "cms"
    admin: true
    public_routes:
      - "/contact-us.html"
    notes: "Four stores: Arlington, East Dallas, South Dallas (Duncanville), Tyler. Per-store stock and pickup. Admin settings shows locations."
  - id: "brands"
    label: "Brands"
    mode: "static"
    admin: false
    public_routes:
      - "/find-your-brand.html"
    notes: "35 find-your-brand pages in the prototype."

site:
  name: "U-FIX-IT Appliance Parts"
  tagline: "We have it, or we'll get it!"
  tagline_em: ""
  sub_tagline: ""
  phone: "Arlington 817.472.7740; East Dallas 214.321.7054; South Dallas 972.780.9096; Tyler 903.592.5836"
  email: ""                    # Rath to research (see Open Questions)
  address: "Arlington: 4621 S Cooper St Suite 127, Arlington, TX 76017; East Dallas: 9919 Garland Rd, Dallas, TX 75218 (locked by Mike); South Dallas: 442 East Wheatland Road, Duncanville, TX 75116; Tyler: 2606 E 5th St, Tyler, TX 75701"
  hours: "Arlington 9am-6pm Mon-Sat, closed Sunday (confirmed by Mike, Nov 2026). East Dallas 9am-6pm Mon-Fri, closed Sat and Sun. South Dallas and Tyler 9am-6pm Mon-Fri, 9am-4pm Sat, closed Sun. Holiday exceptions on /about-us-store-hours.html."
  website: "https://ufixit.com/"

colors:
  primary_accent: "#F50A0A"
  primary_accent_dark: "#D90000"   # on-screen buy button red (AA contrast), per brand.html
  background: "#FFFFFF"
  background_mid: "#F6F5F2"
  background_header: "#1C1D76"
  text_primary: "#000000"
  text_secondary: "#5E5E5E"
  # also: navy #1C1D76 (chrome, headings, prices), amber #FAB143, line #E6E6E6

fonts:
  display: "Oswald"
  body: "Source Serif 4"
  google_fonts_url: ""           # self-hosted in /fonts (css/fonts.css); store UI uses system sans

pages:
  - path: "/UFixIt-Presentation.html"
    name: "U-FIX-IT Appliance Parts — Website Redesign Preview"
  - path: "/UFixIt-SEO-AEO-Compare.html"
    name: "U-FIX-IT Appliance Parts — SEO / AEO Comparison · Sep 2026"
  - path: "/about-us-mission.html"
    name: "U-FIX-IT Mission"
  - path: "/about-us-really-matters.html"
    name: "U-FIX-IT Gives Back"
  - path: "/about-us-store-hours.html"
    name: "Store Hours & Holidays"
  - path: "/about-us-team-members.html"
    name: "Our Appliance Repair Experts"
  - path: "/about-us-warranty-returns.html"
    name: "Appliance Parts Warranty & Returns"
  - path: "/about-us.html"
    name: "About Us"
  - path: "/account.html"
    name: "My Account"
  - path: "/appliance-repair-tips.html"
    name: "Appliance Repair Tips"
  - path: "/appliances-30-expert-bosch-appliance-repair-fast-reliable-fixes-near-you.html"
    name: "Expert Bosch Appliance Repair"
  - path: "/appliances-air-conditioner-parts.html"
    name: "Air Conditioner Repair Parts"
  - path: "/appliances-dishwasher-parts.html"
    name: "Dishwasher Repair Parts"
  - path: "/appliances-dryer-parts.html"
    name: "Dryer Repair Parts"
  - path: "/appliances-furnace-parts.html"
    name: "Furnace Repair Parts"
  - path: "/appliances-how-to-choose-the-right-hotpoint-appliance-for-your-home.html"
    name: "How to Choose the Right Hotpoint Appliance for Your Home"
  - path: "/appliances-ranges-oven-parts.html"
    name: "Ranges & Oven Repair Parts"
  - path: "/appliances-refrigerator-parts.html"
    name: "Refrigerator Repair Parts"
  - path: "/appliances-washer-parts.html"
    name: "Washer Repair Parts"
  - path: "/appliances-why-monogram-appliances-are-the-ultimate-choice-for-luxury-kitchens.html"
    name: "Why Monogram Appliances Are the Ultimate Choice for Luxury Kitchens"
  - path: "/appliances.html"
    name: "Appliances"
  - path: "/brand.html"
    name: "U-FIX-IT Appliance Parts — Brand Guide"
  - path: "/cart.html"
    name: "Your Cart"
  - path: "/category-appliances.html"
    name: "Appliances (blog category)"
  - path: "/category-diy-tips.html"
    name: "Diy Tips (blog category)"
  - path: "/category-dryer.html"
    name: "Dryer (blog category)"
  - path: "/category-news.html"
    name: "News (blog category)"
  - path: "/category-refrigerator.html"
    name: "Refrigerator (blog category)"
  - path: "/checkout.html"
    name: "Checkout"
  - path: "/contact-us-arlington-appliance-parts-store.html"
    name: "Arlington Appliance Parts Store"
  - path: "/contact-us-east-dallas.html"
    name: "East Dallas Appliance Parts Store"
  - path: "/contact-us-south-dallas.html"
    name: "South Dallas Appliance Parts Store"
  - path: "/contact-us-tyler-tx.html"
    name: "Tyler TX Appliance Parts Store"
  - path: "/contact-us.html"
    name: "Contact Us"
  - path: "/diy-tips-4-household-appliance-myths.html"
    name: "4 Household Appliance Myths"
  - path: "/diy-tips-benefits-of-fixing-appliances-yourself-instead-of-replacing-them.html"
    name: "Benefits of Fixing Appliances Yourself Instead of Replacing Them"
  - path: "/diy-tips-best-replacement-parts-for-top-appliance-brands.html"
    name: "Best Replacement Parts for Top Appliance Brands"
  - path: "/diy-tips-complete-guide-to-dishwasher-parts.html"
    name: "Complete Guide to Dishwasher Parts"
  - path: "/diy-tips-discover-expert-device-appliance-repair-services-fast-reliable-solutions.html"
    name: "Discover Expert Device & Appliance Repair Services \\"
  - path: "/diy-tips-electrolux-appliance-repair-guide-troubleshooting-common-issues-error-codes-genuine-parts.html"
    name: "Electrolux Appliance Repair Guide"
  - path: "/diy-tips-essential-ac-parts-guide.html"
    name: "Essential AC Parts Guide:"
  - path: "/diy-tips-expert-customer-diy-support-for-your-appliance-repair-parts-needs.html"
    name: "Expert Customer DIY Support for Your Appliance Repair & Parts Needs"
  - path: "/diy-tips-find-quality-range-oven-parts-expert-guide-to-replacement-parts.html"
    name: "Find Quality Range & Oven Parts \\"
  - path: "/diy-tips-find-reliable-major-appliance-repair.html"
    name: "Find Reliable Major Appliance Repair"
  - path: "/diy-tips-gas-furnace-burner-goes-out.html"
    name: "Gas Furnace – Burner Goes Out"
  - path: "/diy-tips-home-air-conditioner-not-cooling.html"
    name: "Air conditioner not cooling – outdoor unit not running"
  - path: "/diy-tips-how-to-find-the-right-replacement-parts-for-your-appliances.html"
    name: "How to Find the Right Replacement Parts for Your Appliances"
  - path: "/diy-tips-how-to-find-your-appliance-model-number-and-order-the-right-part.html"
    name: "How to Find Your Appliance Model Number and Order the Right Part"
  - path: "/diy-tips-ice-maker-not-working-try-this.html"
    name: "Ice Maker Not Working? Try these easy steps."
  - path: "/diy-tips-lg-appliance-parts-guide.html"
    name: "LG Appliance Parts Guide"
  - path: "/diy-tips-on-doc-12-should-you-repair-or-replace-your-appliance-a-cost-benefit-guide-for-diy-homeowners.html"
    name: "Should You Repair or Replace Your Appliance?"
  - path: "/diy-tips-refrigerator-defrost-problems.html"
    name: "Refrigerator Defrost problems – Diagnosing the most common malfunction"
  - path: "/diy-tips-thermador-appliance-repair-guide-luxury-kitchen-troubleshooting-error-codes-genuine-parts.html"
    name: "Thermador Appliance Repair Guide"
  - path: "/diy-tips-viking-appliance-repair-guide-luxury-kitchen-troubleshooting-error-codes-genuine-parts.html"
    name: "Viking Appliance Repair Guide"
  - path: "/diy-tips-whirlpool-dryer-not-heating.html"
    name: "Whirlpool Dryer Not Heating: Causes and Troubleshooting Tips"
  - path: "/diy-tips-whirlpool-washer-not-fill.html"
    name: "What can be wrong when a Whirlpool washer will not fill with water?"
  - path: "/diy-tips.html"
    name: "DIY Tips | www.ufixit.com"
  - path: "/dryer-complete-dryer-parts-diagram-your-guide-to-diy-dryer-repair.html"
    name: "Complete Dryer Parts Diagram: Your Guide to DIY Dryer Repair"
  - path: "/find-your-brand-admiral.html"
    name: "Admiral"
  - path: "/find-your-brand-amana.html"
    name: "Amana"
  - path: "/find-your-brand-appliance-parts-lg.html"
    name: "LG"
  - path: "/find-your-brand-appliance-parts-whirpool.html"
    name: "Whirlpool"
  - path: "/find-your-brand-bosch.html"
    name: "Bosch"
  - path: "/find-your-brand-brown.html"
    name: "Brown"
  - path: "/find-your-brand-caloric.html"
    name: "Caloric"
  - path: "/find-your-brand-crosley.html"
    name: "Crosley"
  - path: "/find-your-brand-dacor.html"
    name: "Dacor"
  - path: "/find-your-brand-electrolux.html"
    name: "Electrolux"
  - path: "/find-your-brand-frigidaire-appliance-parts.html"
    name: "Frigidaire"
  - path: "/find-your-brand-gaggenau.html"
    name: "Gaggenau"
  - path: "/find-your-brand-ge-general-electric.html"
    name: "GE"
  - path: "/find-your-brand-gibson.html"
    name: "Gibson"
  - path: "/find-your-brand-glenwood.html"
    name: "Glenwood"
  - path: "/find-your-brand-haier.html"
    name: "Haier"
  - path: "/find-your-brand-hardwick.html"
    name: "Hardwick"
  - path: "/find-your-brand-hotpoint.html"
    name: "Hotpoint"
  - path: "/find-your-brand-jenn-air.html"
    name: "Jenn Air"
  - path: "/find-your-brand-kelvinator.html"
    name: "Kelvinator"
  - path: "/find-your-brand-kenmore-appliances.html"
    name: "Kenmore"
  - path: "/find-your-brand-maytag-appliance-parts.html"
    name: "Maytag"
  - path: "/find-your-brand-roper.html"
    name: "Roper"
  - path: "/find-your-brand-samsung.html"
    name: "Samsung"
  - path: "/find-your-brand-scotsman.html"
    name: "Scotsman"
  - path: "/find-your-brand-sears.html"
    name: "Sears"
  - path: "/find-your-brand-speed-queen.html"
    name: "Speed Queen"
  - path: "/find-your-brand-sub-zero.html"
    name: "Sub Zero"
  - path: "/find-your-brand-sunray.html"
    name: "Sunray"
  - path: "/find-your-brand-tappan.html"
    name: "Tappan"
  - path: "/find-your-brand-thermador.html"
    name: "Thermador"
  - path: "/find-your-brand-u-line.html"
    name: "U-LINE"
  - path: "/find-your-brand-wolf.html"
    name: "Wolf"
  - path: "/find-your-brand.html"
    name: "Find Your Brand"
  - path: "/how-to-choose.html"
    name: "How to Choose the Right Appliance Part"
  - path: "/"
    name: "Appliance Parts Store Texas — Shop Online"
  - path: "/news-home-air-conditioner-will-not-cool-outdoor-unit-condenser-not-running.html"
    name: "Home air conditioner will not cool – outdoor unit (condenser) not runn"
  - path: "/news-refrigerator-will-not-dispense-water-produce-ice-possible-quick-fix.html"
    name: "Two “not so obvious” things to check that can stop all waterflow in yo"
  - path: "/news-save-time-save-money-u-fix.html"
    name: "Save time, save money"
  - path: "/order-confirmation.html"
    name: "Order received"
  - path: "/order-lookup.html"
    name: "Track Your Order"
  - path: "/privacy-policy.html"
    name: "Privacy Policy"
  - path: "/refrigerator-frigidaire-parts-diy-guide.html"
    name: "Frigidaire Parts – DIY Guide"
  - path: "/refrigerator-frigidaire-refrigerator-not-cooling-fix-it-yourself-with-the-right-parts.html"
    name: "Frigidaire Refrigerator Not Cooling? Fix It Yourself with the Right Pa"
  - path: "/share-feedback-add-review.html"
    name: "Add a Review"
  - path: "/share-feedback-tell-us-bad-experience.html"
    name: "We are sorry to hear it…"
  - path: "/share-feedback.html"
    name: "Tell us About Your U-Fix-It Experience"
  - path: "/shipping-appliance-parts.html"
    name: "Shipping Appliance Parts"
  - path: "/shipping-inquiry.html"
    name: "Shipping Inquiry"
  - path: "/shop.html"
    name: "Shop Appliance Parts"
  - path: "/sitemap.html"
    name: "SiteMap"
  - path: "/product-category-*.html"
    name: "Product category pages (66, flat HTML; filters)"
  - path: "/product-*.html"
    name: "Product detail pages (438 parts: real names, part numbers, prices, stock from ufixit.com WooCommerce Store API, Oct 15 2026)"
  - path: "/admin/"
    name: "Admin sign-in (demo stub)"
  - path: "/admin/dashboard.html"
    name: "Admin dashboard"
  - path: "/admin/reports.html"
    name: "Admin sales reports"
  - path: "/admin/orders.html"
    name: "Admin orders"
  - path: "/admin/parts.html"
    name: "Admin parts and inventory"
  - path: "/admin/pos.html"
    name: "Admin POS integration (demo)"
  - path: "/admin/customers.html"
    name: "Admin customers"
  - path: "/admin/settings.html"
    name: "Admin settings"
  - path: "/admin/products.html"
    name: "Admin products (redirects to parts)"

deployment:
  platform: "digital-ocean-app-platform"
  region: "sfo3"                 # Team Yavin DB cluster datacenter per template (App Platform slug "sfo"); Rath/DevOps to confirm against the business-apps cluster
  plan: "basic"
  spaces_bucket: "yavin-media"
  spaces_folder: "ufixit"
  domain: "ufixit.com"           # live domain; cutover is a later phase
  do_team: "Team Yavin"          # agency Yavin -> Team Yavin; ecomm uses the business-apps Postgres cluster (PIPELINE.md §6)

repo:
  github_org: "Yavin-Digital"
  prototype_repo: "ufixit-prototype"
  app_repo: "ufixit-app"
  default_branch: "main"

prototype:
  review_url: "https://ufixit.clientreview.co"
  github_repo: "Yavin-Digital/ufixit-prototype"
  location: ""
  guide: "PROJECT_GUIDE.md"
---

# U-FIX-IT Appliance Parts — Ecommerce Rebuild — Project Scope

## Overview

U-FIX-IT is a Texas appliance parts retailer with four stores (Arlington, East Dallas, South Dallas/Duncanville, Tyler), free diagnosis help in person or by phone, and an online parts shop. The live site is WordPress + WooCommerce at https://ufixit.com/. This scope covers an HTML prototype of a rebuilt, store-first ecommerce site, reviewed at https://ufixit.clientreview.co. The rebuild will be a Node ecommerce app (`project_type: ecomm`). Client approval: Lisa Harlan approved the prototype and the demo admin (confirmed by Mike, 2026-11-18). The written approval itself is not in the repo. The prototype also includes a demo admin area with sales reporting.

Prototype links:
- Prototype: https://ufixit.clientreview.co/
- Brand page: https://ufixit.clientreview.co/brand.html
- SEO/AEO compare: https://ufixit.clientreview.co/UFixIt-SEO-AEO-Compare.html
- Presentation: https://ufixit.clientreview.co/UFixIt-Presentation.html
- Demo admin: https://ufixit.clientreview.co/admin/

## Key Features

- Store-first shopping: pick a store, per-store stock and pickup, or ship (placeholder per-store stock filtering in the prototype).
- Catalog: shop hub, 66 category pages with filters, 438 part detail pages, find-your-brand pages (35), how-to-choose guide.
- Cart, mock checkout, order confirmation, order lookup, customer account page.
- DIY Tips hub with articles, and News articles (blog, `blog_mode: cms`).
- About, Mission, Store Hours and Holidays, Warranty and Returns, Team, contact pages for each store, shipping, share-feedback pages.
- Demo admin (now in scope, see below): dashboard, reports, orders, parts/inventory, POS integration, customers, settings. Data is generated demo data (about 8.8k orders over 2 years, fixed seed); sign-in is a stub.
- Admin dashboard: 30-day KPIs vs prior 30 days, net sales chart, top sellers, recent and open orders, low stock.
- Admin reports: quick and custom ranges, channel filter, online + in-store (POS) split, top parts by units and revenue, sales by category and channel, paginated order history, CSV export.
- Admin parts: part number, compatibility/replaces, cost/price, on hand, reorder level, supplier, low-stock alerts, orders per part.
- Admin POS: generic "POS provider" demo connect toggle, sync status and log. The vendor is not chosen.

## Feature modes

`features.blog_mode` is `cms`: the prototype includes DIY Tips and News articles. Do not ship a hard-coded post array. Implementation installs `@yavin/feature-blog` at the newest exact tag (`v0.1.0` as of 2026-11-18, from `gh api repos/Yavin-Digital/feature-blog/tags`); Project Setup rewrites the tag here at Phase 3.

`features.forms` is `contact`. `features.auth` is `credentials` (customer accounts; the admin sign-in in the prototype is a stub and must become real). `features.ecommerce` is `checkout`. `features.payments` and `features.woo_sync` are blank until Rath answers the questions below. `project_type` is `ecomm` on `app-shell-scaffold` (Mike's decision, 2026-11-18).

Blog is not a content type and is not duplicated under `content_types`.

## Content types

- `parts` (cms, admin): the 438-part catalog with stock, price, cost, supplier, compatibility.
- `stores` (cms, admin): four locations with hours, phones, per-store stock and pickup.
- `brands` (static): find-your-brand pages.

## Preserve / Don't invent

- Use real data from the live site (ufixit.com WooCommerce Store API snapshot, Oct 15 2026): names, part numbers, prices, stock, images. Do not invent SKUs.
- Do not invent NAP or hours. Arlington hours are Mon-Sat 9am-6pm, closed Sunday. Keep other locations as listed in `site.hours`.
- Promise line: "We have it, or we'll get it!"
- Brand tokens are in `brand.html` and `css/site.css`. Keep the self-hosted Oswald and Source Serif 4. Do not use banned Unsplash stock.
- Flat root HTML naming is a prototype convention only.
- Admin pages are noindex and the Admin footer link is `rel=nofollow`. Keep the admin out of search.

## Open Questions

All items below are for Rath. Blocking means it would change a mode, integration or content type before Phase 3 can finish; non-blocking means it can be answered during the build.

- **Blocking:** Payment gateway (`features.payments`, `integrations.payment_gateway`): authnet, stripe or both? Not chosen. Rath to decide.
- **Blocking:** Does WooCommerce stay the system of record (`features.woo_sync`), or is the catalog migrated once? Rath to decide.
- **Blocking:** POS vendor for in-store sales (the admin POS page is a generic demo). Rath to decide.
- **Non-blocking:** Confirm `project_type: ecomm` vs `headless-ecomm`, and `deployment.region: sfo3` (Rath/DevOps).
- **Non-blocking:** Contact email for the site and stores. Rath to research.
- **Non-blocking:** GA4 measurement ID(s) (`integrations.ga4_ids`). Rath to research.
- **Non-blocking:** Whether an order confirmation email is needed (`integrations.email_sendgrid`). Rath to research.
- **Non-blocking:** South Dallas street number: the live store page heading, schema and Google/Waze listing say 442 East Wheatland Rd; the live page body also shows 438. The prototype uses 442.
- **Non-blocking:** Holiday matrix (New Year's Eve 9-3, etc.): confirm annually, and check whether Arlington's Saturday change affects holiday copy.

Resolved on 2026-11-18: Node stack (Mike); South Dallas ZIP 75116 (live store page, schema, Google/Waze listing; the live footer's 75237 is wrong); East Dallas is 9919 Garland Rd (Mike); Lisa's approval of the prototype and demo admin (Mike).

## Out of Scope

- Going live, DNS cutover, and migrating WooCommerce data (later phases).
- Real payment processing and real POS sync in the prototype (checkout and POS are mock/demo).
- Real orders in the admin (demo data only).
- The 72 DROP URLs from the signed url-index (sample-page, authors, etc.).

## Notes for the coding agent

- Prototype lives in `Yavin-Digital/ufixit-prototype` and at https://ufixit.clientreview.co. Do not copy it into the app repo. Do not use the `ufixit-preview` repo; it was a deploy mirror of the demo-admin branch and is superseded by main.
- `PROJECT_GUIDE.md`, `CONVERSION.md`, `DEVELOPMENT.md` and `references/` hold the content inventory, url map and sign-offs.
- Hours history: the live site's Arlington Saturday hours were added on Nov 6, 2026 (client email), and the prototype was updated to match.
