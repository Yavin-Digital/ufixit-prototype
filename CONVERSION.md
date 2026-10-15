# U-FIX-IT ecommerce prototype: conversion tactics

Mike's direction (Oct 15, 2026): conversion is the primary design goal. Nothing below invents a review, discount, rating or countdown. Every gap is shown on the page as a yellow dashed **placeholder** tag.

| # | Tactic | Where it lives | Data source |
|---|---|---|---|
| 1 | Hero leads straight to best sellers with a red **Shop now** CTA (+ "Help me find my part") | `index.html` hero → `#best-sellers` | Live tagline "We have it, or we'll get it!" |
| 2 | Best sellers grid | `index.html#best-sellers` | ufixit.com WooCommerce Store API `orderby=popularity` (live store's own ranking) |
| 3 | Add to cart on every product card (one tap, toast with "View cart & checkout") | all shop/category grids, `js/store.js` | — |
| 4 | Sticky Add to Cart bar on mobile product pages | `product-*.html` `.sticky-buy` (≤900px) | — |
| 5 | Trust signals beside every buy button: same-day shipping by 3 pm CST (in stock), 1-year replacement warranty, free store pickup, free diagnosis help, phone | PDP buy box `.assure`, header strip, hero, shop pages, cart, checkout | Live Shipping and Warranty & Returns pages |
| 6 | Real customer reviews | Home "Why Texans come back", every PDP | 4 testimonials from ufixit.com. No star ratings shown (none exist). Product reviews: **placeholder** (none on live site) |
| 7 | Real urgency only: "Only N left in stock" when the live stock count is 3 or less; same-day cutoff | cards + PDP | Live `stock_availability` at build time (Oct 15, 2026 snapshot) |
| 8 | Free-shipping progress bar | `cart.html` | **Placeholder threshold $75** (`js/store.js` `CFG.freeShip`); live site quotes shipping by request |
| 9 | Frequently bought together, "Add all to cart" | PDP `.fbt` | **Placeholder pairing** (same appliance + brand); needs real order data |
| 10 | Related products "You may also need" + "Popular add-ons" in cart | PDP, `cart.html` | Same appliance/brand; popularity |
| 11 | Short guest checkout: 3 steps on one page, no account required, free pickup option | `checkout.html` → `order-confirmation.html` | Mock: no payment taken. Payment provider, tax and ship rates are **placeholders** |
| 12 | Order lookup without an account; optional account with history | `order-lookup.html`, `account.html` | localStorage mock |
| 13 | Email capture | site-wide footer band | Offer/incentive is a **placeholder** (none on live site) |
| 14 | How to choose + comparison table (online vs pickup vs call for help) | `how-to-choose.html`, home 3-step band, "Not sure?" box on every shop page | Live DIY guide (model number) + live policies |
| 15 | Search by part #/model/name in header; instant filters (appliance, brand, price) + sort | header, `shop.html`, `product-category-*.html` | Search covers name, SKU, cross-reference numbers in descriptions |
| 16 | Fast pages | static HTML, images WebP ≤900px (product) lazy-loaded, 1 CSS + 1 small JS, no framework | — |

## Placeholders to confirm with U-FIX-IT
- Free-shipping threshold (placeholder $75) and shipping rates (live site quotes by request)
- Payment provider and Texas sales tax calculation
- Product reviews/ratings (none live) and email signup offer
- Frequently-bought-together pairings (need order history)
- East Dallas street number (9919 vs 9917), South Dallas ZIP
- Vector logo master (live logo is a 228px PNG)
