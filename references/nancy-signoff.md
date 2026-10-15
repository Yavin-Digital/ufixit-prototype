# Nancy Sign-Off — U-FIX-IT live-site content pull

**Client:** U-FIX-IT / U-Fix-It Appliance Parts (The Tribe Maker)  
**Canonical:** https://ufixit.com/  
**Packet:** `/workspace/ufixit-prototype/`  
**Mac project:** `/Users/mikemontes/My Projects/TheTribeMaker/UFixIt`  
**Reviewed:** 2026-09-16 ~8:20pm CT

---

## NANCY SIGN-OFF: APPROVED WITH CONDITIONS

**Phase:** Gate 1 archive / live content pull (SoT for Randy url-index inventory + Bob proto)

### What was reviewed
- `CONTENT.md` — 113 marketing/IA/store/tip pages, verbatim (nav/footer once)
- `URL-INDEX.md` — non-product + CRITICAL
- `URL-INDEX-products.md` — 438 `/product/` + 54 `/appliances/{sku}/` list-only
- `references/content-inventory.md`, `hidden-and-off-nav.md`, `source-assets.md`
- `img/` — 55 official brand/marketing/store assets
- `raw/` — Yoast sitemaps, WP REST, HTML fetches
- Aligns with Randy url-index plan: KEEP hubs; DROP individual SKUs (sample PDP only)

### Strengths
- Full Yoast tree covered (666 unique locs); catalog separated from body archive (correct for Woo).
- Four store landings body-archived (Arlington, East Dallas, South Dallas, Tyler).
- Brand + appliance hubs + repair tips archived without inventing catalog depth.
- Dummy `/sample-page/` caught and marked DROP.
- No casino/pharma spam; GF `(999) 999-9999` correctly identified as mask only.

### CRITICAL flags (live site — fold into dossier; do not ship as-is)
1. **DROP** `/sample-page/` — WP default “bike messenger / Doohickey Co” dummy.
2. **NAP East Dallas:** visible/schema **9919** Garland Rd vs map widget **9917** Garland Rd (same ZIP 75218). Lock one address with client before proto Locations.
3. **NAP South Dallas ZIP:** store page / some schema use Duncanville **75116**; footer/shared blocks also show **75237** for same Wheatland Rd line. Lock ZIP with client.
4. Thin Woo shells: `/shipping-inquiry/`, `/cart/`, `/checkout/`, `/my-account/` — system pages, not marketing copy.
5. Catalog volume: **438** products + **54** appliance SKU-like WP pages — proto does **not** rebuild every SKU; hubs + search/request-part pattern only unless Mike expands scope.

### Conditions
| # | Condition | Owner | Severity | Resolve by | Blocks launch? |
|---|-----------|-------|----------|------------|----------------|
| 1 | Confirm East Dallas street number (9919 vs 9917) with client | Randy / Mike | High | Before Locations copy lock | Yes if wrong NAP ships |
| 2 | Confirm South Dallas / Duncanville ZIP (75116 vs 75237) | Randy / Mike | High | Before Locations copy lock | Yes if wrong NAP ships |
| 3 | Delete or noindex `/sample-page/` on live; never USE in proto | Bob / live ops | Med | Proto + live cleanup | No for proto if DROPped |
| 4 | Mirror packet to Mac `UFixIt/references/` after this sign-off | Nancy / Bob | Low | After sign-off | No |
| 5 | Product annex is list-only — if proto needs PDP samples, use the 2 Randy samples only | Bob | Low | Build | No |

### Permission
Randy may treat `/workspace/ufixit-prototype/` as **source of truth** for CONTENT / images / inventory and lock USE/DROP/REWRITE (draft → final) against this packet + his KEEP/DROP url-index.

Bob may scaffold under `My Projects/TheTribeMaker/UFixIt` from Randy’s brief — **do not invent NAP, hours, or SKU inventory.** Hold Build Done until url-index + this archive are both signed (now true for archive).

### Stack
WordPress (WP Engine) + WooCommerce + Yoast (+ Otto SEO JSON-LD, Gravity Forms). Curl OK.

---

**NANCY STATUS:** APPROVED WITH CONDITIONS  
**Next phase allowed:** Randy USE/DROP/REWRITE inventory + Prototype brief. HTML proto may proceed from signed brief; Locations NAP blocked on client confirm for flags 2–3.
