# SCOPE — U-FIX-IT Appliance Parts (Phase 1 HTML Prototype)

**Proto path:** `/Users/mikemontes/My Projects/TheTribeMaker/UFixIt/`  
**Agency:** Yavin Digital / The Tribe Maker  
**Client:** U-FIX-IT Appliance Parts (Texas)  
**Live (copy / NAP / hours / brand only):** https://ufixit.com/  
**Slug:** `ufixit` → proposed review `https://ufixit.clientreview.co` (**do NOT stand Pages until Mike says Phase 2**)  
**Proposed repo (not created until Mike unlocks):** `Yavin-Digital/ufixit-prototype`  
**Assigned:** Jarvis (from Mike / Yavin OS)  
**KEEP set built:** 2026-09-16 CT (America/Chicago)  
**Build Done checklist:** `references/build-done-checklist.md` — **CLAIMABLE** (2026-09-16 ~9:00pm CT)

---

## Architecture locks

- Vanilla HTML / CSS / JS. No framework. No build step.
- **Flat root HTML only** (`about-us.html`, `about-us-mission.html` — never folders, never `--`).
- **Brand first:** `brand.html` + `css/site.css` tokens from live — never invent colors.
- Body type: `--text: 1.25rem` / `--text-lh: 1.6` (20px).
- Display: Oswald · Body: Source Serif 4 · Primary navy `#1C1D76` · Accent red `#F50A0A`.
- **No invent NAP/hours** — pull from live / Nancy CONTENT.md only; Unverified tags for conflicts.
- Catalog: **hubs + 2 sample PDPs only** (DROP 434 other SKUs / sample-page).
- GitHub Pages / clientreview.co = Phase 2 only (Mike call).

---

## Pages (Phase 1)

| Page set | Count | Status |
|----------|------:|--------|
| Brand gate | 1 | DONE (`brand.html`) |
| KEEP flat HTML (url-index) | **168** | DONE — see `references/url-to-file-map.md` |
| Presentation | 1 | DONE (`UFixIt-Presentation.html`) |
| SEO/AEO Compare | 1 | DONE (Randy — `UFixIt-SEO-AEO-Compare.html`) |
| DROP (not built) | 72 | sample-page, cart/checkout/account shells not marketing KEEP, 434 SKUs, authors, etc. |

**Home preview:** `index.html`  
**Map:** `references/url-to-file-map.md`  
**Compare:** `UFixIt-SEO-AEO-Compare.html` (banner + Presentation deep-link)  
**Checklist:** `references/build-done-checklist.md`

### NAP status (Locations copy lock)

| Item | Status |
|------|--------|
| East Dallas street # **9919** Garland Rd | **LOCKED** (Mike 2026-09-16 CT) — shipped on footer / locations / contact / about / home |
| South Dallas ZIP **75116 vs 75237** | **Unverified** — omitted on store pages; tagged |

Phones + Arlington/Tyler full addresses + East Dallas **9919** Garland Rd + city/ZIP + South Dallas street (no ZIP) used where unambiguous.

---

## Known business facts (live / brief)

- Four Texas stores: **Arlington**, **East Dallas**, **South Dallas / Duncanville**, **Tyler**
- Appliance parts + **free diagnosis** / tech tips (in person or phone)
- Promise: **“We have it, or we’ll get it!”**
- Same-day shipping language only as it appears on live / CONTENT.md

### Hours (footer SoT; holiday exceptions on Hours page — confirm annually)

9am–6pm Monday–Friday · Closed Saturdays & Sundays · *Tyler & South Dallas open 9am–4pm Saturday  
NYE / Christmas Eve: 9 to 3 (Store Hours page)

---

## Sources

- Randy `references/url-index.md` — KEEP 168 / DROP 72 (signed)
- Randy `references/content-inventory.md` — LOCKED for density
- Randy `UFixIt-SEO-AEO-Compare.html` + `references/seo-aeo-compare-facts.md`
- Nancy `/workspace/ufixit-prototype/CONTENT.md` — APPROVED WITH CONDITIONS

---

## Out of scope (this pass)

- GitHub Pages / CNAME / Phase 2 publish
- Full WooCommerce catalog / invent SKUs / invent NAP resolution
- Banned Unsplash stock
- Slack Marcie

## Ecommerce prototype extension (Oct 15, 2026)
Mike asked for an ecommerce prototype. Added on top of the 168-page KEEP set: storefront home, `shop.html`, 66 `product-category-*.html` pages with filters, 438 `product-*.html` detail pages (real names, part numbers, prices, stock, descriptions and images from the ufixit.com WooCommerce Store API, Oct 15, 2026), `cart.html`, `checkout.html` (mock), `order-confirmation.html`, `order-lookup.html`, `account.html`, `how-to-choose.html`. See `CONVERSION.md`. Platform for the build is undecided (live is WordPress + WooCommerce).

## Demo admin + reporting (Oct 20, 2026, PR #12)

Requested by Mike on Oct 20, 2026. This is a **demo-only** store admin under `/admin/`, reached from a discreet footer "Admin" link (`rel=nofollow`). There is no backend or real integration, and every number is labeled as demo data.

- **Pages:** `admin/index.html` (demo sign-in stub: any email or password works, sessionStorage only), `dashboard.html`, `reports.html`, `orders.html`, `parts.html` (`products.html` redirects to it), `customers.html`, `pos.html` and `settings.html`. All admin pages are `noindex, nofollow`.
- **Data:**
  - `admin/catalog.js` holds the real part names, part numbers, prices and "replaces" cross-references extracted from `shop.html`.
  - `admin/data.js` generates deterministic demo data from fixed seeds: about 8.5k orders from Oct 21, 2024 to Oct 20, 2026, plus customers, part cost, stock, reorder levels, suppliers (fictional, tagged "(demo)") and a POS sync log.
- **Reports:**
  - Date-range presets and custom dates, plus a channel filter.
  - KPIs vs the prior period.
  - A revenue-over-time SVG chart (net sales on the left axis, order count on the right, partial periods hatched) with a data table.
  - Top products by units and by revenue, sales by category and by channel.
  - Online + in-store (POS) combined, with a split.
  - Top parts used, a paginated order history and a CSV export.
- **Parts & inventory:** each part shows part #, name, compatibility ("Fits" plus the part numbers it replaces), cost and price, on hand, reorder level and supplier. Low-stock alerts appear on Parts and the Dashboard. Each part links to the orders that used it, and each order links to its parts.
- **POS provider:** a generic placeholder (**vendor TBD, Mike to confirm**). It has a demo connect/disconnect toggle (localStorage), sync status, last sync time, and a sync log of sales in and inventory counts.
- **Rules:**
  - Brand tokens from `css/site.css`.
  - Text at least 16px (chart axis ticks 13px), inputs 16px, 48px targets.
  - No page-level sideways scroll at 320, 390, 844x390 or 1440.
  - Tables become stacked cards below 760px, and the phone nav is a select below 600px.
  - Order #, date, total and status cells don't wrap.
  - Gains show a green ▲ and drops a red ▼.
  - Plain SVG charts, with no chart library.
- **Out of scope:** real authentication, persistence, payments, POS or supplier integrations, and any production admin. A real build would replace `data.js` with live sources.
