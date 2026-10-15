# U-FIX-IT — Content Map DRAFT (pending Nancy signoff)

**Status:** DRAFT seed only — **not** final inventory.  
**Lock rule:** Do **not** finalize USE / DROP / REWRITE until `/workspace/ufixit-prototype/references/signoff.md` is Nancy-signed.  
**As of:** 2026-09-16 CT — `CONTENT.md` + draft inventory exist under `/workspace/ufixit-prototype/`; `references/signoff.md` = **PENDING NANCY** (not approved).  
**Seeded from:** signed url-index KEEP/DROP policy + prototype `references/content-inventory.md` (advisory) + obvious junk kills.  
**Related:** Mac `references/content-inventory.md` stub still WAITING official sync after Nancy.

Legend (provisional — **not** Nancy-final; do not ship as locked USE/DROP/REWRITE):
- **SEED-KEEP** — url-index KEEP and/or draft inventory USE; likely proto/marketing inclusion
- **SEED-DROP** — url-index DROP, draft DROP, or obvious junk
- **REVIEW** — draft REWRITE or SEO-bloat risk; Nancy decides USE vs REWRITE vs DROP
- **UNKNOWN** — needs live/client/store-manager check (esp. NAP)

---

## Proto / marketing hubs (SEED-KEEP)

| Area | URLs / pattern | Seed note |
|------|----------------|-----------|
| Home | `/` | Promise, pillars, NAP, testimonials |
| About cluster | `/about-us/`, mission, really-matters, store-hours, team-members, warranty-returns | Mission/Gives Back may need REWRITE (SEO fluff); warranty is operational SoT |
| Contact + 4 stores | `/contact-us/` + Arlington, East Dallas, South Dallas, Tyler | Fix NAP conflicts before publish |
| Shipping | `/shipping-appliance-parts/`, `/shipping-inquiry/` | Same-day-by-3pm CST claim |
| Appliances hubs | `/appliances/` + washer/dryer/fridge/AC/furnace/range/dishwasher | Category marketing hubs |
| Brands | `/find-your-brand/` + brand children | Keep hub; brand pages REVIEW for thin/duplicate |
| Shop | `/shop/` + `product-category/*` hubs | Category hubs KEEP; titles bugs (dishwasher→“Washer Parts”) REVIEW |
| Sample PDPs (2) | `/product/er-w10190961-icemaker-for-whirlpool/`, `/product/part-no-er-b3200-bake-element-for-electrolux/` | Pattern only |
| DIY / tips / news | `/appliance-repair-tips/`, `/diy-tips/` (+ posts), blog categories, select `/news/`, `/dryer/`, `/refrigerator/` posts | Many REVIEW for AI/SEO tone |
| Feedback | `/share-feedback/` (+ add-review, bad-experience) | KEEP hub |
| Legal | `/privacy-policy/`, `/sitemap/` | KEEP |

## Obvious junk / ecommerce chrome (SEED-DROP)

| Pattern | Why |
|---------|-----|
| `/cart/`, `/checkout/`, `/my-account/` | Woo chrome — not marketing content |
| `/sample-page/` | Default WP junk |
| `/product/{sku}/` × ~434 | Catalog SKUs — proto uses shop + cats + 2 samples |
| `/appliances/{part-slug}/` individual part landings | SKU-like WP pages — DROP for proto |
| `?team=`, `?testimonials=`, `?videos=` | CPT query URLs — roll up to hubs |
| `/author/*` | Author archives — no unique marketing value |

## REVIEW before Nancy (likely REWRITE or merge)

- Gives Back / really-matters — partners unclear in scrape
- Mission + hours pages — keyword FAQ appendages
- DIY posts with “repair services” framing that muddies parts-retail positioning
- Brand pages with thin/duplicate content
- Contact hub hours cards missing Saturday exceptions
- Product-category wrong titles; Whirlpool `whirpool` slug typo
- East Dallas “North Houston” copy

## Explicitly not locked

USE / DROP / REWRITE columns for a full page-by-page inventory will be filled **after** Nancy signoff. This file is a **seed map** for Growth/proto planning only.

## Align with prototype draft inventory (advisory)

From `/workspace/ufixit-prototype/references/content-inventory.md` (unsigned):
- East Dallas → draft **REWRITE** (9919 vs 9917)
- South Dallas → USE but verify ZIP 75116 vs schema/footer 75237
- Shipping inquiry → draft **REWRITE** (thin shell)
- DIY/news posts → USE/REWRITE mix (SEO-thin titles)
- sample-page → DROP
- Cart/checkout/account → functional routes, not marketing port

## Archive dependency

Verbatim bodies: `/workspace/ufixit-prototype/CONTENT.md`. Images: 55 in prototype `img/` (`source-assets.md`). **Do not treat as signed** until Nancy completes `signoff.md`. Until signed, proto may use live NAP/promise only per Mac SCOPE rules.
