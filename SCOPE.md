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
