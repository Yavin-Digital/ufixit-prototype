# U-FIX-IT — SEO / AEO Compare Facts Ledger

**Compare UI:** `/workspace/ufixit/UFixIt-SEO-AEO-Compare.html` · Mac `UFixIt/UFixIt-SEO-AEO-Compare.html`  
**Live:** https://ufixit.com/  
**Proto:** local Mac KEEP-168 HTML under `/Users/mikemontes/My Projects/TheTribeMaker/UFixIt/`  
**Audit date:** 2026-09-16 CT  
**Score rule:** Pass=2 · Warn/Opportunity=1 · Gap=0 · Unknown excluded. Readiness only — **no invented ranks/traffic/stars.**

**Primary sources:** Nancy CRITICAL `signoff.md`; dossier; content-inventory; url-index KEEP 168 / DROP 72; live scrapes (`homepage.html`, hubs, `sitemap_index.xml`); robots.txt via curl; Mac proto samples (title/meta/H1/JSON-LD presence).

---

## Row ledger (22)

### Crawl & index (SEO)

| ID | Topic | Live | Proto | Fact basis |
|----|-------|------|-------|------------|
| `robots` | robots.txt | **Pass** — present; Yoast sitemap pointer | **Opportunity** — Designed for go-live · add at launch | Curl 2026-09-16: Woo disallows + Yoast block with `Sitemap: https://ufixit.com/sitemap_index.xml`. Proto has no robots.txt. |
| `sitemap` | Yoast XML sitemaps | **Pass** — sitemap_index + post/page/product/brands/cats | **Opportunity** — Designed for go-live · add at launch | `references/sitemap_index.xml` lists post, page, product, testimonials, brands, category, product_cat, author. Proto static ~169 HTML, no XML sitemap file. |
| `https-host` | HTTPS / WP Engine stack | **Pass** — HTTPS · WP + Woo + Yoast (WP Engine) | **Opportunity** — static local HTML; host at launch | Nancy sign-off Stack + dossier: WordPress (WP Engine) + WooCommerce + Yoast. Live canonical `https://ufixit.com/`. |

### On-page (SEO)

| ID | Topic | Live | Proto | Fact basis |
|----|-------|------|-------|------------|
| `titles` | Unique title tags | **Warn** — home OK; dishwasher product-cats titled “Washer Parts” | **Pass** — unique titles on sampled KEEP pages | Live home: `Appliance Parts Store in Texas \| U-Fix-It`. Url-index: multiple `/product-category/dishwasher-parts/*` titled **Washer Parts**. Proto samples: unique `— U-FIX-IT Appliance Parts` titles. |
| `meta` | Meta descriptions | **Pass** — home meta present (Otto/Yoast) | **Opportunity** — titles strong; meta often missing | Live home meta: parts + free diagnosis, Dallas/Arlington/Tyler. Sampled proto pages: no `meta name=description`. |
| `h1` | H1 / page clarity | **Pass** — clear H1s on hubs / stores | **Pass** — matching H1s on KEEP pages | Proto: East Dallas / Contact / Appliances / About H1s present and aligned. |
| `canonical` | Canonical URL | **Pass** — absolute `https://ufixit.com/` | **Opportunity** — Designed for go-live · add at launch | Live homepage `rel=canonical`. Proto: no absolute production canonicals on samples. |
| `og-twitter` | Open Graph / Twitter tags | **Pass** — og/twitter present on home | **Opportunity** — Designed for go-live · add at launch | Live home: `og:title`, `og:url`, `twitter:title`, `twitter:description`. Proto samples: no OG/Twitter. |
| `dishwasher-title` | Dishwasher category titled “Washer Parts” | **Gap** — multiple dishwasher product-cats | **Pass** — dishwasher appliance hub title correct | Url-index rows for `/product-category/dishwasher-parts/` (+ brand subcats) document title **Washer Parts**. Proto `appliances-dishwasher-parts.html` uses Dishwasher-oriented title. |

### Content & IA (SEO)

| ID | Topic | Live | Proto | Fact basis |
|----|-------|------|-------|------------|
| `ia-keep` | KEEP 168 hubs vs 438 SKU bloat | **Warn** — 438 products + ~54 appliance SKU pages | **Pass** — hub strategy (~169 HTML); SKUs not rebuilt | Nancy CRITICAL #5; url-index KEEP 168 / DROP SKUs; content-inventory catalog DROP. Mac ~169 `*.html`. |
| `hub-depth` | Brand + appliance hub depth | **Pass** — find-your-brand + appliance landings | **Pass** — hubs in KEEP HTML | Live `/find-your-brand/` + appliance cats; proto appliances/brand/tips KEEP files. |
| `sample-page` | DROP `/sample-page/` dummy | **Gap** — still in page-sitemap | **Pass** — absent from proto | Nancy CRITICAL #1; url-index DROP; `page-sitemap.xml` includes `https://ufixit.com/sample-page/`. Proto: no `*sample*` HTML. |
| `woo-shells` | Thin Woo system shells | **Warn** — cart/checkout/my-account/shipping-inquiry | **Pass** — system/REWRITE, not marketing density | Nancy CRITICAL #4; content-inventory thin Woo shells. |
| `nap-east` | NAP East Dallas **9919** Garland Rd | **Warn** — visible/schema 9919 vs map 9917 | **Pass** — Mike locked **9919**; Unverified tag removed | Nancy CRITICAL #2 resolved by Mike lock (2026-09-16 CT). Proto ships 9919 everywhere East Dallas NAP appears. |
| `nap-south-zip` | South Dallas ZIP 75116 vs 75237 | **Warn** — store/schema vs footer/shared | **Opportunity** — Unverified; client lock | Nancy CRITICAL #3; dossier South Dallas / Duncanville ZIP conflict. |
| `hours` | Hours Sat + NYE consistency | **Warn** — Sat exceptions + NYE 9–3 vs 9–6 + Contact omits Sat | **Opportunity** — REWRITE / client confirm | Dossier hours section: Tyler & South Dallas Sat 9–4; Contact cards Mon–Fri only; NYE conflict Store Hours vs About. |

### Answer engines (AEO)

| ID | Topic | Live | Proto | Fact basis |
|----|-------|------|-------|------------|
| `lb-schema` | LocalBusiness / Organization JSON-LD ×4 stores | **Warn** — Otto Store/FAQ/WebPage; Yoast `@graph:false`; NAP conflicts | **Opportunity** — Designed for go-live · LocalBusiness ×4 | Homepage: Otto `Store` + FAQPage + WebPage; Yoast graph false; no clean LocalBusiness×4 with locked NAP. Proto: content ready; schema at launch after NAP lock. |
| `entity-clarity` | Parts + diagnosis (not field service) | **Warn** — offer clear; some blog titles muddy | **Pass** — parts + diagnosis retained | Dossier: not field-service; free diagnosis + parts. Some DIY titles say “repair services.” Proto positioning from signed copy. |
| `faq-howto` | FAQ / how-to answer surfaces | **Warn** — DIY tips real; home FAQPage placeholder junk | **Pass** — tips/mission hubs quotable | Live DIY tips USE; Otto FAQPage first Q: “None - No questions provided for evaluation?” Proto keeps tips + mission pages. |
| `mission-promise` | Mission / promise answer blocks | **Pass** — promise + mission page | **Pass** — About KEEP set | Dossier verbatim: “We have it, or we’ll get it!” + mission listen/confirm/respond. Proto About/Mission KEEP. |
| `review-schema` | Review schema honesty (no invented stars) | **Pass** — testimonials; no AggregateRating invent | **Pass** — no fabricated stars | Homepage scrape: testimonials named; no AggregateRating star counts asserted. Policy: never invent stars. |
| `faq-schema-quality` | FAQPage schema quality | **Gap** — placeholder/empty Q&A in schema | **Opportunity** — only real Q&A at go-live | Otto FAQPage includes junk first Question + generic answers. Proto must not claim FAQ schema until approved Q&A exists. |

---

## Scoring notes

- **SEO group:** rows `robots` … `hours` (16 rows).  
- **AEO group:** rows `lb-schema` … `faq-schema-quality` (6 rows).  
- Proto technical / Unverified NAP items score **Opportunity** (1), not Pass.  
- Scores are checklist readiness only — never Google rank, traffic, or competitor position claims.

## Verify

- HTML title: `U-FIX-IT Appliance Parts — SEO / AEO Comparison · Sep 2026`  
- Mentions U-FIX-IT / ufixit.com; does **not** mention theamericanquiz or USCIS.  
- Theme: navy `#1C1D76`, accent red `#F50A0A`.  
- Row count: **22**.
