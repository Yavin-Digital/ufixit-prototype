# U-FIX-IT Appliance Parts — Research Dossier

**Status:** READY for Growth handoff — sourced facts only; unknowns marked.  
**Nancy archive:** **APPROVED WITH CONDITIONS** — `/workspace/ufixit-prototype/references/signoff.md` (2026-09-16 ~8:20pm CT).  
**Content inventory:** **LOCKED** — `/workspace/ufixit/references/content-inventory.md` (Mac `UFixIt/references/content-inventory.md`).  
**Url-index:** SIGNED — KEEP 168 / DROP 72 — `/workspace/ufixit/references/url-index.md`.  
**Live:** https://ufixit.com/  
**Slug:** `ufixit`  
**Agency:** Yavin Digital / The Tribe Maker — Mac `/Users/mikemontes/My Projects/TheTribeMaker/UFixIt/`  
**Compiled / updated:** 2026-09-16 CT  
**Primary sources:** Nancy CONTENT.md (113 marketing/IA pages) + img/ (55) + live scrapes + signed url-index.  
**NAP policy:** East Dallas **9919** vs map **9917**; South Dallas ZIP **75116** vs **75237** — **Unverified / client confirmation needed**. Proto may scaffold primary visible NAP; do not invent resolution. Locations copy lock blocked until Mike/client confirms.

---

## 1. Company overview

**What they are (from live):** Texas specialty retailer of **appliance replacement parts** with in-store and phone **free diagnosis assistance / tech tips**, plus online shop (WooCommerce). Positioning is DIY-friendly expert help, not a full field-service repair company.

**Promise (verbatim, home / mission):** “We have it, or we’ll get it!” / “We Have It, or We’ll Get It!”

**Guiding principle (About / Mission):** “Love your neighbor as you love yourself.”

**Mission (verbatim, Mission page):** “When your appliance breaks we listen to your symptoms, we confirm and then we respond. We give away what we know and go the extra mile to make sure the appliance part you take home is the part you need.”

**Experience claim (About / home):** “more than 100 years of combined experience” (team aggregate — not a founding-year claim).

**Stack (url-index):** WordPress (WP Engine) + WooCommerce + Yoast; REST `/wp-json/`; ~438 Woo products (Store API).

**Brand spelling on site:** varies — U-Fix-It, U-FIX-IT, UFixIt. Prefer on-page form per URL when rewriting.

---

## 2. Locations (verified from live footer / store pages 2026-09-16)

Four brick-and-mortar stores listed consistently in global footer/nav:

| Store label | Phone | Address (footer / primary NAP) | Notes |
|-------------|-------|--------------------------------|-------|
| **Arlington** | 817.472.7740 | 4621 S Cooper St Suite 127, Arlington, TX 76017 | Location page: off I-20, ~6 mi west of HWY 360 |
| **East Dallas** | 214.321.7054 | 9919 Garland Rd, Dallas, TX 75218 | Location page also shows **9917** Garland Rd in one map/schema string — **NAP conflict** |
| **South Dallas** | 972.780.9096 | 442 East Wheatland Rd, Duncanville, TX 75237 | Location page hero: ZIP **75116**; alternate string **438** East Wheatland — **NAP/ZIP conflicts**. Banner: Sat hours |
| **Tyler, TX** | 903.592.5836 | 2606 E 5th St, Tyler, TX 75701 | Near hwys 323 & 64; banner: Sat hours |

**Hours (sitewide footer / banner, live):**
- Default: **9am–6pm Monday–Friday**
- **Closed Saturdays & Sundays** (base rule)
- Exception: **Tyler & South Dallas open 9am–4pm Saturday** (homepage banner + footer asterisk)
- About page body once said only “*South Dallas location open 9am-4pm Saturdays” (omitting Tyler) — **hours copy inconsistency**

**Holidays (Store Hours page; slight New Year’s Eve variance vs About):**
- New Year’s Eve: **9 to 3** (Store Hours page) — About page body once said **9 to 6** → **conflict**
- New Year’s Day: closed Jan 1
- Memorial Day, Independence Day (Jul 4), Labor Day, Thanksgiving: closed
- Christmas Eve: 9 to 3
- Christmas: closed Dec 25–26

**Contact hub quirk:** Contact Us cards list all four stores as Mon–Fri only / closed Sat–Sun — **does not surface Saturday hours** for Tyler & South Dallas (banner/footer do).

**Stale / unverified geography:** East Dallas page body mentions serving **“North Houston”** alongside the four TX stores. No North Houston location URL in url-index KEEP set. Treat as **possible stale copy** until client confirms.

**Secondary (not live primary):** BBB profiles list alternate/legal names (e.g. UFI Parts, Inc.) and a Dallas Westmoreland address on one BBB listing — **not** used as current NAP here; confirm with client.

---

## 3. Audience

**Inferred from live offers/copy (not a client persona brief):**
- DIY homeowners who want to repair vs replace washers, dryers, refrigerators, ranges/ovens, dishwashers, AC, furnaces
- Callers/walk-ins needing diagnosis help before buying a part
- Spanish-speaking customers (team bio: Tony M. bilingual — South Dallas)
- Online buyers needing continental-US shipping of parts
- **UNKNOWN:** share of trade/tech vs consumer; B2B volume; commercial parts mix (warranty shortens for commercial use — see Offers)

---

## 4. Offers

### Parts retail
- Categories on home nav: Washer, Dryer, Refrigerator, Air Conditioner, Furnace, Ranges & Oven, Dishwasher
- Shop also lists Microwave Parts, Accessories, Dishwasher Accessories (Woo categories)
- Brand hub `/find-your-brand/` with many brand pages (Admiral, Amana, Bosch, GE, Kenmore, LG, Maytag, Samsung, Whirlpool, luxury brands like Sub-Zero / Thermador / Wolf, etc.)
- HVAC brand names listed on brand hub (Carrier, Trane, Lennox, etc.) for AC/heating parts — **inventory depth UNKNOWN**
- Woo catalog ~**438** products online (url-index / Store API) — marketing site is much larger than proto KEEP set
- In-store: “stocks the parts needed to repair the most common symptoms”; less common “available the next day”; rare “take a little longer” (About)
- Tyler page: special-order parts “usually available the next day freight free” (**confirm** — store-specific claim)

### DIY / education
- Free diagnosis assistance & tech tips **in person or over the phone** (home)
- Free **part testing** in-store (home pillars + location pages)
- Repair Tips hub, DIY Tips posts, brand/DIY guides, Videos CPT (**60** entries — query-string URLs; url-index DROP for proto)
- Feedback hub (`/share-feedback/`)

### Services vs repair
- **Not** positioned as on-site appliance repair service company; focus is parts + diagnosis help so customer (or their tech) can fix
- Some blog titles reference “repair services” generically — treat carefully; primary CTA is parts + ask-an-expert

### Shipping
- “In stock” items **ship same day if ordered by 3 pm CST Monday–Friday** (Shipping page)
- Ships across **continental United States**; optional priority shipping
- Shipping help phone cited on Shipping page: **972.780.9096** (South Dallas number)
- Quote form: part/model + zip → price & shipping

### Warranty / returns (Warranty page)
- Limited warranty to **original purchaser**, non-transferable
- **1-year** replacement warranty unless receipt states otherwise
- Defective: return with original receipt to any store for replace/repair
- Electrical-connection replacements: one replacement during warranty period then warranty ends
- Commercial/business use: warranty expires **30 days** after purchase
- Exclusions: improper install, abuse, homemade/modified appliances; belts, couplings, fuses, lamps, chemicals, oils; shipping costs not covered
- Returns: **no returns on special orders**; regular stock uninstalled/salable within **14 days** with invoice; scuff marks / mounted / connections made → ineligible

### Community
- `/about-us/really-matters/` — “Gives Back / Non-Profit Partners” exists
- **UNKNOWN:** which nonprofits are actually named/linked on the live page (scrape primary block did not list partner names clearly; SEO filler text is generic)

---

## 5. Proof / trust signals (sourced)

**Testimonials on home / brand hub (names from live + Testimonials CPT):**
- Erick Scott
- Kirby J
- Lisa Panelli-Valentin
- Rosamari Williamson  
(Full verbatim quotes available on homepage scrape — inventory before reuse.)

**Team (Team Members page / REST CPT, 5):**
- Jaime C. – Sales, Arlington
- Khristopher S. – Store Manager, East Dallas
- Eric W. – Senior Technical Advisor, South Dallas (since 2002; bio also says store manager since Apr 2006 — **title inconsistency** on page)
- Dustin R. – Manager, Tyler (joined Sep 2025)
- Tony M. – Sales, South Dallas (ex tech; bilingual)

**Local SEO / performance (agency presentation draft — Report Builder 72296, ~Aug 2026 window — draft only):**
- GSC: ~2,041 clicks (+19%); impressions ~36.7K; avg pos ~4.59
- GA4: ~16.8K sessions; revenue ~$1,282 (− vs prior window in deck)
- GBP impressions cited for Arlington & Dallas in deck  
→ Treat as **internal measured snapshot**, not client-approved public claims. Deck README: draft — do not email until Mike says send.

**BBB:** Public profiles exist for Dallas / Tyler area listings — useful for legal name research; **rating/complaint detail not pulled for this dossier**.

---

## 6. Current site gaps (observed, not invented)

1. **Huge catalog vs marketing IA** — 438 SKUs + many `/appliances/{part}` landings; proto KEEP drops most SKUs (url-index policy).
2. **NAP / hours inconsistencies** — ZIP/street variants; NYE hours; Saturday hours missing on Contact hub cards; About vs footer on Saturday stores.
3. **Thin / SEO-bloated copy** — Mission, Gives Back, hours, and some DIY posts include keyword-stuffed FAQ/boilerplate that reads AI-generated; brand voice uneven.
4. **Gives Back** page claims partners but partner names not clearly evidenced in scrape — risk of empty social-proof section.
5. **“North Houston”** mention without a matching store page.
6. **Team title drift** (Eric W. Senior Technical Advisor vs store-manager bio language).
7. **Jaime C. slug** in REST: `jaime-c-sales-south-dallas` while title says Arlington.
8. **Product-category title bugs** (url-index): several dishwasher category URLs titled “Washer Parts.”
9. **Whirlpool brand URL typo:** `/find-your-brand/appliance-parts-whirpool/`
10. **Videos** exist as CPT without pretty permalinks in sitemap — discoverability gap.
11. **Social:** Facebook per-store links present; no findable public Instagram/YouTube/X profile URLs on homepage (honeypot fields labeled Instagram/X/Twitter/LinkedIn only).
12. **Ecommerce UX** — cart/checkout/account are DROP for marketing proto; live conversion soft in Aug 2026 deck (revenue down while traffic up) — Growth should validate with current analytics.
13. **AEO / AI visibility:** not measured (presentation slide).
14. Archive / Nancy signoff **pending** — no locked official copy blocks yet.

---

## 7. Social (public, findable on live)

**Facebook (footer “follow us” — per store):**
- South Dallas: `https://www.facebook.com/profile.php?id=61574402897239`
- Tyler: `https://www.facebook.com/profile.php?id=61575521014984`
- East Dallas: `https://www.facebook.com/people/U-Fix-It-Appliance-Parts-East-Dallas/61575226514241/`
- Arlington: `https://www.facebook.com/profile.php?id=61575636570477`

**Instagram / YouTube / X / LinkedIn / TikTok:** **No public profile URLs found** on homepage or about scrapes (only anti-spam honeypot field labels). **UNKNOWN** if accounts exist off-site.

**Email newsletter:** signup in footer (sales, product info, team updates).

---

## 8. History

| Claim | Source class | Status |
|-------|--------------|--------|
| Combined team experience “100+ years” | Live About/home | Use as **team aggregate**, not founding date |
| Eric W. at U-FIX-IT since **2002** | Live team bio | Sourced |
| Dustin joined **Sep 2025** | Live team bio | Sourced |
| Business started **1975** / two generations | Third-party directory (e.g. UniLocal) | **Unverified on live About** — mark UNKNOWN until client/live confirms |
| BBB “Business Started” **1998-08-25**; incorporated **2001-11-26**; alt name UFI Parts, Inc.; co-owners Jim & Sharon Plummer listed on BBB schema | BBB public profiles | Secondary; **do not invent** into marketing without client OK |
| Copyright “2026 U-FIX-IT Appliance Parts” | Live footer | Present |

**Founding story on live About:** not a clear year/narrative in primary About body beyond mission/experience — **UNKNOWN** official founding year from live SoT.

---

## 9. Assets

| Asset | Location / note |
|-------|-----------------|
| Live site | https://ufixit.com/ |
| Url-index (SIGNED discovery) | `/workspace/ufixit/references/url-index.md` (+ Mac `references/url-index.md`) |
| Homepage + hub HTML scrapes | `/workspace/ufixit/references/homepage.html`, `hub_*.html` |
| Prototype raw KEEP-ish HTML + images | `/workspace/ufixit-prototype/raw/pages/`, `img/` |
| Mac Phase 1 scaffold | brand tokens (`#1C1D76` navy, `#F50A0A` red; Oswald + Source Serif 4), `img/logo.png`, Home shell |
| SEO/AEO presentation draft | `/workspace/ufixit/presentation/ufixit-seo-aeo-2026-08.html` (+ PDF) — **draft, not client-sent** |
| WP REST dumps | `/workspace/ufixit/references/wp-rest/` |
| Content archive | `/workspace/ufixit-prototype/CONTENT.md` (verbatim pull; pending Nancy) |
| Prototype content inventory (draft) | `/workspace/ufixit-prototype/references/content-inventory.md` — proposed USE/REWRITE/DROP **not signed** |
| Source assets | `/workspace/ufixit-prototype/references/source-assets.md` — **55** images in `img/`; **0** PDFs |
| Signoff | `/workspace/ufixit-prototype/references/signoff.md` — **APPROVED WITH CONDITIONS (see header)** |
| Mac content inventory stub | `TheTribeMaker/UFixIt/references/content-inventory.md` — still WAITING / may sync after signoff |

---

## 10. Unknowns (explicit)

1. Official **founding year** / ownership narrative approved for marketing (1975 vs 1998 tension).
2. Whether **North Houston** (or any fifth store) is real/current.
3. Canonical NAP for East Dallas (9919 vs 9917) and South Dallas (442/438; ZIP 75237 vs 75116).
4. Canonical **holiday / Saturday** hours matrix (resolve About vs Store Hours vs Contact cards).
5. Named **nonprofit partners** for Gives Back.
6. Public **Instagram/YouTube** (and other) handles if any.
7. True **SKU/catalog** depth beyond Woo 438; in-store vs online overlap.
8. Share of revenue: counter vs ecommerce vs phone order.
9. Whether they perform **on-site repair** (site suggests no; some content muddies this).
10. Nancy **signoff** — **APPROVED WITH CONDITIONS**; inventory **LOCKED**.
11. Eric W. / Jaime C. title/location accuracy.
12. Legal entity display name for footer vs BBB (U-FIX-IT Appliance Parts, Inc. / UFI Parts, Inc.).

---

## 11. Competitive comps (3–6) — why relevant

Chosen for **appliance parts / specialty retail / DIY repair** adjacency (not generic “pretty” marketing sites):

1. **RepairClinic** (repairclinic.com) — National DIY appliance-parts leader: symptom search, model lookup, guides, strong ecommerce UX. Comp for how U-FIX-IT’s local expertise + free testing could differentiate against scale catalog UX.
2. **PartSelect** (partselect.com) — Model-driven parts finder + installation content. Comp for information architecture of “find the right part” journeys.
3. **AppliancePartsPros** (appliancepartspros.com) — Parts ecommerce + repair help content. Comp for DIY content + PDP patterns.
4. **Encompass** (encompass.com) — OEM/parts distribution brand presence; more trade/OEM. Comp for authenticity of “genuine/OEM-adjacent” sourcing language (without claiming U-FIX-IT’s supplier status — **UNKNOWN**).
5. **Reliable Parts** (reliableparts.com) — Multi-location parts retailer/distributor serving pros + consumers. Comp for multi-store specialty retail + shipping.
6. **Marcone** (marcone.com) — Trade-oriented appliance parts network. Comp for pro/tech audience overlap if U-FIX-IT serves technicians (volume **UNKNOWN**).

**Local specialty angle:** Multi-location Texas counter culture + phone diagnosis is the differentiator vs pure national ecom — Growth should stress NAP accuracy, store pages, and expert proof over catalog mimicry alone.

---

## 12. Handoff notes for Growth

- Proto KEEP/DROP policy is in **url-index** (168 KEEP / 72 DROP rows; SKUs mostly DROP).
- **Do not lock USE/DROP/REWRITE** until Nancy marks `signoff.md` approved (currently APPROVED WITH CONDITIONS (see header)). Draft inventory at prototype `references/content-inventory.md` is advisory only.
- Do **not** invent NAP, hours, awards, stock claims, or founding year.
- Parent will hand to Max — this agent does not Slack Max.

---

## Source checklist

- [x] Live home, about, mission, team, warranty, shipping, four location pages (prototype raw 200s + homepage references scrape)
- [x] Url-index SIGNED
- [x] Nav/footer JSON
- [x] Team/testimonials REST
- [x] Facebook footer links
- [x] CONTENT.md present — [x] Nancy-signed APPROVED WITH CONDITIONS — [x] content-inventory LOCKED
- [ ] Google site: crawl — PARTIAL (captcha) per url-index
