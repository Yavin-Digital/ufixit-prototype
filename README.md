# Sales Opportunities — The Tribe Maker

## Required Kickoff Inputs

When the following 2 inputs are received, the agent executes the full workflow end to end without further questions.

### The 2 Inputs

1. **Existing site URL** — used for logo, brand, fonts, images, page set
2. **Company / Client name** — used for the project folder name

### Auto-Pilot Contract

> **Once these 2 inputs are received, do not ask further questions — execute the full workflow end to end. Make assumptions where reasonable and document them in the deliverables.**

### Kickoff Prompt Template

```
Build a prototype.
URL: <existing site url>
Company: <client name>
```

---

This workspace is the **prototype process template**. New client prototypes are created under:

```
/Users/mikemontes/My Projects/<Agency>/<ClientName>/
```

Agency folders (examples): `TheTribeMaker`, `DPA`, `GDS`, `Ascend`, `Catalyst`, `YOLO Nerd`.

Pick the agency that owns the client, then create the project folder there. Do **not** create new prototypes under `Sales/` or the retired `_Sales_Opp/` path.

Each project folder ships with a prototype website, a brand guide, SEO/AEO reports, a presentation, and an admin panel.

---

## Completeness gates (locked 2026-09-10) — every proto

House standard. Not optional. Details: agent skill `prototype-completeness-gates`.

1. **Page discovery (Randy)** — before claiming a complete page set, write `references/url-index.md` from robots/sitemaps + **required** Google `site:domain` + WP REST when WordPress + nav/footer crawl. **Full live sitemap** on the proto; DROP only with an explicit reason.
2. **Brand gate (Proton Bob)** — `brand.html` first; CSS tokens from live extraction only; shared header/footer. No invented palette/fonts per page.
3. **Content inventory** — `references/content-inventory.md` (USE/DROP/REWRITE) + `references/source-assets.md` + official images in `img/`.
4. **Done block** — do not mark Build Prototype Done without url-index mirrored, brand.html + tokens, and content-inventory. If missing: Slack-ping Marcie once; create a Yavin OS task on that client/project assigned to Marcie, due in **3 business days**.
5. **PM approval Doc (before Phase 3)** — Marcie/PM owns a GatherContent-style Google Doc from the inventory for client sign-off. No Phase 3 without it.

---

## Full Workflow — Numbered Checklist

Once the 2 Kickoff Inputs are received, run this numbered checklist top to bottom. Each step links to the README section that defines the rules. Do not skip steps.

1. **Confirm the 2 Kickoff Inputs** — URL and Company name. If either is missing, ask once and stop. *(see [Required Kickoff Inputs](#required-kickoff-inputs))*
2. **Create the project folder** at `My Projects/<Agency>/<ClientName>/` with `img/`, `references/`, and `js/` subfolders — then immediately create `references/chat.md` using the Chat Log Standard template. *(see [Workspace Structure](#workspace-structure) and [Chat Log Standard](#chat-log-standard))*
3. **Pull brand assets from the live site** — logo (SVG preferred, then PNG; **never recreate it**), brand colors, fonts, favicon, social share image, at least 3 hero/section images. Save to `img/`. *(see [Brand Enforcement Rules](#brand-enforcement-rules--non-negotiable-on-every-project))*
4. **Build `brand.html` first** — document the existing logo exactly as found, colors, fonts, and tone of voice. Never design a new logo or invent new brand elements. *(see [Brand Guide Standard](#brand-guide-standard))*
5. **Crawl the live site and mirror the page list** — use Randy’s `references/url-index.md` (robots/sitemaps + Google `site:domain` + WP REST). Produce one prototype HTML file per KEEP URL, with an HTML comment at the top documenting source URL and UX improvements. *(see Completeness gates + [Prototype Build Standards](#prototype-build-standards))*
6. **Build the prototype pages** — 60vh hero, 1400px container, mobile-first responsive, content always stacks on mobile, every CTA simulated end to end. *(see [Layout & Hero Standards](#layout--hero-standards--non-negotiable) and [Prototype Build Standards](#prototype-build-standards))*
7. **Build the complete login/auth views** — `login.html`, `forgot-password.html`, `reset-password.html`, and any other auth screen the prototype needs. All views must be fully fleshed out with no dead ends. *(see [Login & Auth Structure Standard](#login--auth-structure-standard))*
8. **Build `admin.html`** — admin panel with configuration fields for Google Analytics, Google Search Console, Google Tag Manager, and SendGrid API key. *(see [Admin Panel Standard](#admin-panel-standard))*
9. **Run the Gap Analysis** — after the prototype is complete, review it for missing pages, incomplete flows, or industry-standard features that are absent. Document all findings and present them as actionable suggestions to the user. *(see [Gap Analysis Standard](#gap-analysis-standard))*
10. **Build `seo.html`** — research competitor and keyword gaps, then merge with any user-provided goals. *(see [SEO Audit Standard](#seo-audit-standard))*
11. **Build `aeo.html`** — run the AI ranking test, populate the Q&A bank, and embed all required JSON-LD schema blocks. *(see [AEO Standard](#aeo-standard))*
12. **Build `<ClientName>-Social.html`** — research every social platform, document follower counts, posting cadence, brand consistency, and gaps. *(see [Social Media Review Standard](#social-media-review-standard))*
13. **Build `<ClientName>-Presence.html`** — synthesize findings from steps 10–12 into the channel-by-channel green/yellow/red overview. This is the first document shown in the sales meeting. *(see [Digital Presence Report Standard](#digital-presence-report-standard))*
14. **Build `<ClientName>-SEOPlan.html`** — derive a client-specific, actionable SEO roadmap directly from `seo.html` findings. *(see [SEO Marketing Plan Standard](#seo-marketing-plan-standard))*
15. **Build `<ClientName>-Marketing.html`** — build the full digital marketing plan; include the Funnel System section when client acquisition is a stated or implied goal. *(see [Digital Marketing Plan Standard](#digital-marketing-plan-standard) and [Funnel System Standard](#funnel-system-standard))*
16. **Build `<ClientName>-Functionality.html`** — write the React handoff spec: page map, component inventory, interactive features, auth flow, admin integrations, and deployment notes. *(see [React Functionality Specification Standard](#react-functionality-specification-standard))*
17. **Build `<ClientName>-Presentation.html`** — a clean, simple slide-style presentation with labeled image placeholders for the current live site and the new prototype pages. *(see [Presentation Standard](#presentation-standard))*
18. **Run the QA checklist** — mobile usability, contrast, no horizontal scroll, 44×44px tap targets, working hamburger, alt text on every content image, no `{{TOKEN}}` placeholders remaining in any file.
19. **Final review** — open every HTML file, click every CTA, complete every flow, verify no dead links and no placeholder text remains. Then notify the user the project is ready to present.

---

## Workspace Structure

```
My Projects/<Agency>/
├── README.md                        ← you are here (agent instructions live here)
├── index.html                       ← Sales Tracker Dashboard (Kanban pipeline)
├── references/                      ← research, screenshots, or reference files
├── _tools/                          ← reusable Python scripts (shared across all projects)
│   ├── discover_images.py           ← Stage 1: crawl site + collect all image URLs
│   └── download_images.py           ← Stage 3: download all images to img/ folder
│
└── <ClientName>/                    ← every new project lives here
    │
    ├── img/                             ← REQUIRED — create before any HTML
    │   ├── logo.png                     ← REQUIRED — client logo pulled from live site (never recreated)
    │   ├── logo-white.png               ← white variant if available on dark backgrounds
    │   ├── og-share.jpg                 ← REQUIRED — 1200×630 social share image
    │   └── favicon.ico                  ← REQUIRED — pulled from live site or provided by client
    │
    ├── references/                      ← screenshots, competitor research, brand notes for this project
    │   └── chat.md                      ← ★ REQUIRED — created at chat start; logs all changes + site architecture
    │
    ├── js/                              ← site data + layout engine + animations
    │   ├── site.js                      ← window.SITE = { … } — single source of truth for all content
    │   ├── layout.js                    ← mounts header + footer dynamically on every page
    │   ├── anim.js                      ← anime.js reveal helpers
    │   ├── modal.js                     ← prototype modal (showPrototypeModal)
    │   └── pages/
    │       ├── home.js
    │       ├── about.js
    │       ├── services.js
    │       ├── products.js              ← (if applicable)
    │       ├── product.js               ← (if applicable)
    │       └── contact.js
    │
    ├── index.html                       ← prototype home page
    ├── about.html
    ├── services.html
    ├── products.html                    ← (if applicable)
    ├── product.html                     ← (if applicable)
    ├── contact.html
    │   (+ any other pages mirrored from the live site)
    │
    ├── login.html                       ← ★ AUTH — Login view
    ├── forgot-password.html             ← ★ AUTH — Forgot password view
    ├── reset-password.html              ← ★ AUTH — Reset password view (token-based)
    ├── admin.html                       ← ★ ADMIN — GA / GSC / GTM / SendGrid configuration
    │
    ├── brand.html                            ← ★ DELIVERABLE 1  — Brand Guide (existing logo + colors + fonts + tone)
    ├── <ClientName>-Presence.html           ← ★ DELIVERABLE 2  — Digital Presence Report (shown first in sales meeting)
    ├── seo.html                              ← ★ DELIVERABLE 3  — SEO Audit
    ├── aeo.html                              ← ★ DELIVERABLE 4  — Answer Engine Optimization
    ├── <ClientName>-Social.html             ← ★ DELIVERABLE 5  — Social Media Platform Audit
    ├── <ClientName>-SEOPlan.html            ← ★ DELIVERABLE 6  — SEO Marketing Plan (built from seo.html findings)
    ├── <ClientName>-Marketing.html          ← ★ DELIVERABLE 7  — Digital Marketing Plan (includes Funnel System if applicable)
    ├── <ClientName>-Functionality.html      ← ★ DELIVERABLE 8  — React Handoff Spec
    └── <ClientName>-Presentation.html       ← ★ DELIVERABLE 9  — Before/After slide presentation
```

### The Required Deliverables

Every client project must include **all of the following** before it is considered ready to present.

| # | File | Purpose |
|---|---|---|
| 1 | `brand.html` | Brand Guide — existing logo documented as-is, colors, fonts, tone of voice |
| 2 | Prototype pages (`index.html`, etc.) | Full mirrored prototype with UX/conversion improvements |
| 3 | `login.html` · `forgot-password.html` · `reset-password.html` | Complete auth views — no dead ends |
| 4 | `admin.html` | Admin panel with GA, GSC, GTM, and SendGrid API key configuration |
| 5 | `<ClientName>-Presence.html` | Digital Presence Report — first shown in the sales meeting; all channels green/yellow/red |
| 6 | `seo.html` | SEO audit — user input + researched keyword and gap analysis |
| 7 | `aeo.html` | AEO report — user Q&A + discovered gaps + JSON-LD schema |
| 8 | `<ClientName>-Social.html` | Social media platform audit — follower counts, posting cadence, brand consistency |
| 9 | `<ClientName>-SEOPlan.html` | Actionable SEO marketing plan derived directly from `seo.html` findings |
| 10 | `<ClientName>-Marketing.html` | Full digital marketing plan — includes Funnel System when client acquisition is a goal |
| 11 | `<ClientName>-Functionality.html` | React handoff spec — page map, component inventory, auth flow, API integrations |
| 12 | `<ClientName>-Presentation.html` | Simple slide-style presentation with before/after image placeholders |

---

## Brand Enforcement Rules — Non-Negotiable on Every Project

> These rules apply **before the first line of HTML is written** and govern every design decision for the entire project.

### Rule 1 — Always pull the logo from the live site. Never recreate or replace it.

The client's existing logo is used exactly as-is. Do not redesign it, redraw it, or substitute a different mark under any circumstances.

1. Fetch the client's live website and extract the logo URL from the HTML source.
2. Download it and save it to `<ClientName>/img/` using this priority order:
   - `logo.svg` — if SVG is available (preferred — scales perfectly)
   - `logo.png` — PNG with transparency (second choice)
   - `logo-white.png` — white/light variant for dark backgrounds (save alongside the main logo if available)
   - `logo.jpg` — only if no transparent format exists
3. The logo **must appear** in `brand.html` and every prototype page nav and footer. A broken image or missing logo is a blocking error.
4. In `brand.html`, document what logo was found: file format, source URL, dimensions, and any usage notes (e.g. "dark version only — use on light backgrounds").
5. If the client's site is down or has no logo, ask the user for a logo file before proceeding. **Never generate or design a replacement.**

### Rule 2 — Always pull brand colors from the live site's CSS. Never invent colors.

1. Fetch the client's live site and extract hex/RGB values from CSS custom properties, inline styles, or computed styles.
2. Use one of the three extraction methods documented in Step 2b (Python Pillow, Digital Color Meter, CSS fetch).
3. Map the extracted values to roles: `--brand-color`, `--accent`, `--dark`, `--muted`, `--bg`.
4. Document every color as a swatch in `brand.html` **before using it anywhere else**.
5. **If you cannot extract a color from the live site, ask the user — do not make one up.**

### Rule 3 — Always pull fonts from the live site. Never substitute.

1. Check the site's `<link>` tags and `@font-face` rules for the font family names.
2. Use the exact same font families in `brand.html` and every prototype page.
3. Load them from the same CDN source (Google Fonts, Adobe Fonts, etc.) as the live site uses.
4. **If a font cannot be identified, use the closest system fallback and document the uncertainty in `brand.html`.**

### Rule 4 — brand.html is the single source of truth. Build it first.

All colors, fonts, and button styles used in any other file must match `brand.html` exactly. If a value in a prototype page does not appear in `brand.html`, it must be added to `brand.html` before the page ships. No prototype or deliverable may introduce a new color or font that is not documented in the brand guide.

### Rule 5 — Save all research and references in the references folder.

Any file that is not a deliverable but is useful for the project — competitor screenshots, brand inspiration, research notes, spec PDFs — must be saved to `<ClientName>/references/`. Use descriptive filenames (e.g., `competitor-abc-screenshot.png`, `brand-color-notes.md`). Never leave reference material loose in the root of the project folder.

`chat.md` lives here and is the single most important file in `references/` — see [Chat Log Standard](#chat-log-standard).

### Rule 6 — The logo must always be large and clearly visible on a contrasting background.

The logo is the most important brand element on every page. It must never be small, faint, or lost against a background that is too similar in color.

1. **Size:** The logo must be large enough to read comfortably — minimum `160px` wide in navbars, and significantly larger (at least `240px` wide or equivalent) in hero sections, brand guides, and report headers.
2. **Background contrast:** The logo must always be placed on a background whose lightness is the **opposite** of the logo itself:
   - A **dark logo** (black, navy, dark gray) must sit on a **light or white background**
   - A **light or white logo** must sit on a **dark or brand-colored background**
   - Never place a dark logo on a dark background, or a white logo on a white/light background
3. **If two logo variants are available** (e.g. dark version + white version), use the dark version on light backgrounds and the white version on dark backgrounds. Save both as `logo.png` and `logo-white.png`.
4. **If only one logo version exists**, and it does not contrast with the intended background, add a solid contrasting background pill, card, or panel behind the logo — do not let it disappear into the page.
5. A logo that cannot be read at a glance is a blocking defect. Fix it before presenting any deliverable.

### Rule 7 — Never use emojis unless the user explicitly requests them.

All deliverables — HTML pages, brand guides, reports, proposals, agreements, and any copy written for the client — must be **emoji-free by default**. This applies to:

- Page headings, body copy, and labels
- Navigation links and button text
- Report section headers, table cells, and callout boxes
- Footer text, legal copy, and contact information
- Any text written inside `<script>` tags (JSON-LD schema, alt text, etc.)

Emojis are informal and inconsistent across platforms. Professional agency deliverables use typography, spacing, icons (SVG), and color to create visual hierarchy — not emoji characters.

**The only exception:** If the user explicitly says *"use emojis"* or pastes in copy that contains emojis and asks you to match it, then match it. Otherwise, treat any emoji in a deliverable as a defect to be removed.

---

## Layout & Hero Standards — Non-Negotiable

> These three rules are the most-missed standards in past builds. They govern every page layout in every prototype.

### 1. Hero Height — 60vh

- Every hero/page-top section is **`60vh`** tall with **`min-height: 480px`** as a mobile fallback.
- Never use `100vh` (mobile browser chrome makes it render wrong).
- Vertical-center content in the hero using flexbox.

### 2. Content Max-Width — 1400px

- All readable content lives in a `.container` that is **`max-width: 1400px`**, `margin-inline: auto`, and `padding-inline: 20px` on mobile (`40px` on desktop).
- **1400px is the hard ceiling. Nothing — no section, no grid, no image — may exceed this width on desktop.**
- This is the single source of truth for content width — every other "max-width" in this README must match.

### 3. Full-Width Backgrounds, Constrained Content

- The outer `<section>` (or `<header>`) is **100% width** and holds the background color, gradient, or image.
- The inner `<div class="container">` constrains the content to 1400px.
- Never put the background on the container.

### 4. Mobile Content Always Stacks — Non-Negotiable

- **Every multi-column layout must collapse to a single column on screens narrower than 768px.** No exceptions.
- This means: grids, flex rows, card rows, nav links, hero side-by-side layouts, form + image splits, icon rows — all of them stack vertically on mobile.
- The correct pattern is always: **base styles = single column, media queries add columns**. Never write multi-column as the base and try to undo it.
- A layout that does not stack on mobile is a blocking defect — do not deliver it.

### 4. Copy-Paste Reference Pattern

```html
<section class="hero">
  <div class="container">
    <h1>Headline</h1>
    <p>Subhead</p>
    <a class="btn-primary" href="#cta">Primary CTA</a>
  </div>
</section>
```

```css
/* Hero — 60vh, full-bleed background, centered content */
.hero {
  width: 100%;
  min-height: 480px;
  height: 60vh;
  display: flex;
  align-items: center;
  background:
    linear-gradient(120deg, rgba(7,26,62,0.85) 0%, rgba(13,43,94,0.75) 100%),
    url('./img/hero.jpg') center/cover no-repeat;
  color: #fff;
}

/* Container — 1400px max-width, mobile gutters */
.container {
  width: 100%;
  max-width: 1400px;
  margin-inline: auto;
  padding-inline: 20px;
}

@media (min-width: 1024px) {
  .container { padding-inline: 40px; }
}
```

### 5. Cross-Reference Note

> *These three rules are the most-missed standards in past builds. Confirm each one is satisfied in every prototype HTML file before marking work complete. See also the "UI Design Standards — Responsive & Mobile" section below for the wider mobile rule set.*

---

## Prototype Build Standards

> **Standing rules for every prototype build.** These come up on every project; codified here so they don't get missed.

### 1. Mirror the Live Site's Page Set

- Before building, crawl the live site and list every top-level page in its primary nav and footer.
- Create one prototype HTML file per discovered page (e.g., live site has Home, About, Services, Locations, Pricing, FAQ, Contact → produce `index.html`, `about.html`, `services.html`, `locations.html`, `pricing.html`, `faq.html`, `contact.html`).
- Improve UX/UI and conversion on every page. At the top of each HTML file, add an HTML comment block:

  ```html
  <!--
    Page: <page name>
    Source: <live site URL of the corresponding page>
    Improvements vs live site:
    - <improvement 1>
    - <improvement 2>
    - <improvement 3>
  -->
  ```

- If the live site has fewer than 4 top-level pages, propose 1–2 additional conversion-focused pages (e.g., a "Why Us" or "Process" page) and document them as additions in the same comment block.

### 2. Mobile-First + Interactive Simulation

- Build mobile-first per the existing **UI Design Standards — Responsive & Mobile** section.
- **Every** CTA, form, modal, multi-step flow, gated action, calculator, booking step, and quote builder must be simulated end to end. No dead buttons.
- Server-bound actions (form submit, checkout, account creation, contact form) use `showPrototypeModal()` from `js/modal.js` with a realistic next-step preview.
- Multi-step flows must allow forward and back navigation through every step.
- Hover, focus, active, disabled, and loading states must all be visible somewhere in the prototype.

### 3. Animation & 3D

- Use `anime.js` for reveal-on-scroll, count-ups, and micro-interactions (already in the stack via `js/anim.js`).
- Use `three.js` (via CDN) **only when the industry/site benefits**: hero scenes for product showcases, immersive backgrounds, 3D logo reveals, interactive product configurators, architectural/real-estate walkthroughs.
- Performance guardrail: maintain **60 fps** on a mid-tier laptop. `three.js` scenes must respect `prefers-reduced-motion: reduce` and fall back to a static hero image.
- Never use animation that delays the first paint of headline + primary CTA.

### 4. ADA Compliance Simulator

Required for any client in a regulated industry. Trigger list:

| Industry | Examples |
|----------|----------|
| Legal | Law firms, attorneys, courts |
| Medical | Hospitals, clinics, dentists, med spas, pharmacies |
| Government | City/county, agencies, elected officials |
| Financial | Banks, credit unions, lenders, advisors, insurance |
| Education | Schools, universities, training providers |
| Public accommodation | Restaurants, hotels, retail, entertainment venues |

Process:

1. Add **axe-core** via CDN to every prototype page.
2. Run an axe-core scan against the live site **and** the prototype.
3. Capture both result sets in `references/ada-report.md` with the date, page URL, violation count by severity (critical/serious/moderate/minor), and a prioritized fix list.
4. Add an "Accessibility" badge to `report.html` showing the prototype's WCAG conformance level.

axe-core CDN snippet for easy paste-in:

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/axe-core/4.10.0/axe.min.js"></script>
<script>
  window.addEventListener('load', () => {
    axe.run().then(results => {
      console.log('axe-core violations:', results.violations);
    });
  });
</script>
```

### 5. Brand + Logo Always From the Live Site

- Cross-reference the existing [Brand Enforcement Rules](#brand-enforcement-rules--non-negotiable-on-every-project) section so this rule isn't lost.
- One-line summary: *"Every prototype copies the live site's logo (preferred SVG), brand colors, fonts, and at least 3 high-quality images from the live site into `img/`. Never substitute, never invent."*

### 6. 404 Page — Required on Every Project

> Every prototype must include a `404.html` file. It must be clever and specific to the client's industry and company — never generic. A generic 404 is a missed moment; a clever one shows the client what good design thinking looks like.

**Built from:** `_templates/404-template.html` — copy the template, replace all `{{TOKEN}}` values, never leave a placeholder in the delivered file.

#### How to Write the Clever Copy

The three copy lines (`{{HEADLINE}}`, `{{TAGLINE}}`, `{{CLEVER_LINE}}`) must be written based on the client's actual business. Before writing, answer:
1. What does this company do or sell?
2. What would go "missing" in their world? (a job, a patient, a product, a shot, a case, a booking)
3. What is the driest, most brand-appropriate way to acknowledge that in one line?

**The three copy fields:**

| Token | Purpose | Rules |
|---|---|---|
| `{{HEADLINE}}` | The punchline — clever, industry-specific, references what the business does | Max 10 words. No emojis in the headline itself. |
| `{{TAGLINE}}` | One plain sentence explaining what actually happened | Clear, not cute. "The page you're looking for doesn't exist or has moved." |
| `{{CLEVER_LINE}}` | A dry, brand-appropriate follow-up — the moment that makes the client laugh | Max 12 words. Italic. One sentence. Should feel like the brand's voice. |

**Industry copy examples — use as inspiration, never copy verbatim:**

| Industry | Icon | Headline | Clever Line |
|---|---|---|---|
| Home Inspection | 🔍 | "We inspect everything — except this page." | *"Looks like this one slipped past the checklist."* |
| Med Spa / Aesthetics | 💉 | "This page didn't make it to the treatment plan." | *"Even the best glow-up can't fix a broken link."* |
| Firearms / Gun Range | 🎯 | "Shot in the dark — this page doesn't exist." | *"Even our aim isn't perfect. This one missed."* |
| Plumbing | 🔧 | "Something's leaking — and it's this URL." | *"We've fixed worse. But this page is gone."* |
| HVAC | ❄️ | "This page has left the building. Like warm air in July." | *"We can fix your system. This URL is on you."* |
| Law Firm | ⚖️ | "We rest our case — this page doesn't exist." | *"The evidence suggests you took a wrong turn."* |
| Restaurant | 🍽️ | "This page isn't on the menu." | *"But everything else we make is worth the trip."* |
| Real Estate | 🏠 | "This property is off the market." | *"The good news — everything else is still available."* |
| Moving Company | 📦 | "Looks like this page got lost in the move." | *"It happens to the best of us. We'll help you find your way."* |
| Roofing | 🏚️ | "This page has a leak. We're working on it." | *"In the meantime, let us fix what we're actually good at."* |
| Security / Armory | 🔒 | "Access denied. This page is off the grid." | *"Some things are meant to stay hidden. This URL is one of them."* |
| Fire Protection | 🔥 | "This page went up in smoke." | *"We contain fires — not missing pages."* |
| Auto / Dealership | 🚗 | "This page took a wrong turn." | *"No GPS can fix this one. Head back to the homepage."* |
| Pet Services | 🐾 | "This page ran off. We're looking for it." | *"Check the yard. If not there, try the homepage."* |
| Financial / Payments | 💳 | "This page didn't process. Try again." | *"Transaction failed. Fortunately, everything else here works."* |

#### Icon Selection

`{{ICON_EMOJI}}` — pick one emoji that represents the industry without being childish. It sits above the headline. Examples: 🔍 🔧 ❄️ ⚖️ 🏠 🎯 💉 🔒 🔥 — match the tone of the brand. If the brand is premium/formal, use a subtle icon or none at all (remove the `<span class="icon">` line entirely).

#### Quick Links

`{{QUICK_LINK_1_LABEL}}` through `{{QUICK_LINK_3_LABEL}}` — use the 3 most important pages for this client. Typical choices:

| Business Type | Link 1 | Link 2 | Link 3 |
|---|---|---|---|
| Service business | Our Services | About Us | Get a Quote |
| Retail / product | Shop | About | Contact |
| Medical / wellness | Services | Book Now | Contact |
| Restaurant | Menu | Reservations | Contact |
| Professional services | Practice Areas | Our Team | Contact |

#### Pre-Launch Check for 404

- [ ] `404.html` exists in the project folder
- [ ] All three copy lines (`{{HEADLINE}}`, `{{TAGLINE}}`, `{{CLEVER_LINE}}`) are replaced with client-specific text — no token placeholders remain
- [ ] Logo loads correctly from `img/logo.png`
- [ ] Brand colors match `brand.html`
- [ ] All three quick links point to real pages in the prototype
- [ ] Page is fully responsive at 375px — card fits without horizontal scroll
- [ ] "Take Me Home" button links to `index.html`

### 7. Prototype Banner — Required on Every Prototype Page

> Every prototype HTML file must include a fixed banner at the top that clearly marks it as a prototype and opens a performance modal. **The developer must remove or ignore this banner entirely in the React production build.**

**Built from:** `_templates/prototype-banner-snippet.html` — copy the entire block and paste it immediately after `<body>` on every prototype page (index.html, about.html, services.html, contact.html, 404.html, login.html, forgot-password.html, reset-password.html, admin.html, and any additional pages).

#### What the Banner Includes

| Element | Description |
|---|---|
| Fixed dark header | Amber bottom border, "Prototype Only" badge, disclaimer text |
| Disclaimer text | "For prototype purposes only. All content and images are not final and are only here to show what is possible." |
| "View Performance Report" button | Opens the performance modal. Amber, on-brand. Developer note printed inside. |
| Performance modal | Shows actual page load time (from `performance.getEntriesByType()`), estimated React load (42% faster), and improvement percentage |
| Schema detection | Counts all `<script type="application/ld+json">` blocks on the page and reports types found |
| Body padding | Automatically pushes page content below the fixed banner via `body { padding-top: 42px }` |

#### How to Inject It

```html
<body>

<!-- paste prototype-banner-snippet.html block here -->

<!-- rest of prototype content -->
```

#### Developer Note (printed in the modal footer)

> "Developer note: Remove this banner and modal entirely from the React production build."

This line must remain in every copy so the developer knows at a glance that the banner is prototype-only.

#### Pre-Launch Check for Prototype Banner

- [ ] Banner is present on every prototype HTML file
- [ ] "View Performance Report" button opens the modal
- [ ] Load time populates correctly (not "—")
- [ ] Schema detection reports the correct count (or notes no schema)
- [ ] Banner does not appear on any report/audit HTML files — only on prototype pages

---

## Agent Instructions — Read This Before Starting Any New Project

> **When the user provides the site URL and company name, execute the full workflow immediately. Do not ask for additional information before creating the project folder and pulling site assets.**

### Step 1 — Gather Client Info

The only two required inputs are the URL and the company name. Everything else is derived from the live site or documented as unknown.

| Field | How to Get It |
|---|---|
| `CLIENT_COMPANY` | Provided by user |
| `CLIENT_WEBSITE` | Provided by user |
| `CLIENT_OWNER` | Pull from live site's About or Contact page (if available) |
| `CLIENT_PHONE` | Pull from live site |
| `CLIENT_EMAIL` | Pull from live site |
| `OG_IMAGE` | Check live site for a 1200×630 image; if none, generate from logo using `make_og_share.py` |
| `FAVICON` | Pull from live site; if none, use logo mark cropped to 64×64 |

### Step 2 — Create the Project Folder & img Directory

Create the folder and subfolders at the workspace root:

```bash
mkdir -p "/Users/mikemontes/My Projects/<Agency>/<ClientName>/img" \
         "/Users/mikemontes/My Projects/<Agency>/<ClientName>/references" \
         "/Users/mikemontes/My Projects/<Agency>/<ClientName>/js"/js/pages
```

### Step 2b — Extract Site Assets (Images, Logo, Social Links + Brand Colors)

Before building the brand guide, pull **all usable assets** from the client's live site: photography, logo, social media links, and the color palette. Complete this step immediately after creating the project folder.

> **Non-negotiable rules that apply to every project:**
> - **Always grab the logo** from the client's website and save it as `img/logo.png` (or `.svg` / `.avif` if available). The prototype and brand guide must use the real logo — never a placeholder.
> - **Always match the client's brand colors** from their existing site unless the user explicitly requests a different palette. Derive colors from the logo and/or CSS as described in Part B below.
> - **Always pull all social media links** from the client's site and use standard Font Awesome platform icons. Never leave social links as `#` in the final prototype.

---

#### Part A — Pull ALL Images from the Client's Website

> **The goal is completeness.** Every image displayed on the client's site — regardless of where it is hosted (their own server, a CDN, Wix, WordPress, Cloudinary, Squarespace, Shopify, or any third-party host) — must be downloaded into the project's `img/` folder before building the prototype. The prototype must never hot-link to external CDN URLs. Those URLs break, get renamed, or go behind auth walls. Local copies are the only reliable approach.

**The standard workflow is four stages: Discover → Collect → Download → Verify.**

---

##### Stage 1 — Discover: Crawl Every Page and Collect All Image URLs

Do not crawl only the home page. Run the full-site discovery script below against every page in the site's nav and sitemap. It visits each URL, extracts all image references (including those inside `<img>`, `srcset`, CSS `background-image`, `<picture>`, `<source>`, inline styles, and `<meta og:image>`), and writes a deduplicated URL list to a text file.

```python
# save as: _tools/discover_images.py
# usage:   python3 _tools/discover_images.py https://www.clientsite.com My Projects/<Agency>/ClientName/img
import sys, os, re, urllib.request, urllib.parse

START_URL = sys.argv[1].rstrip('/')
IMG_DIR   = sys.argv[2]
os.makedirs(IMG_DIR, exist_ok=True)

HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'}
IMG_EXT  = re.compile(r'\.(jpg|jpeg|png|webp|avif|gif|svg)(\?[^"\'>\s]*)?$', re.IGNORECASE)

# Patterns that find image URLs in HTML source (covers <img src>, srcset, og:image, CSS url(), etc.)
PATTERNS = [
    re.compile(r'(?:src|href|content)=["\']([^"\']+\.(jpg|jpeg|png|webp|avif|gif|svg)[^"\']*)["\']', re.IGNORECASE),
    re.compile(r'url\(["\']?([^"\')\s]+\.(jpg|jpeg|png|webp|avif|gif|svg)[^"\')\s]*)["\']?\)', re.IGNORECASE),
    re.compile(r'srcset=["\']([^"\']+)["\']', re.IGNORECASE),
    # Wix warmupData hashes
    re.compile(r'([a-f0-9]{32}~mv2\.[a-z]{3,4})', re.IGNORECASE),
    # Cloudinary, Imgix, Fastly, generic CDN paths
    re.compile(r'(https://[a-z0-9._-]+(?:cloudinary|imgix|fastly|cdn|media|assets|images|static)[a-z0-9._/-]*/[^\s"\'<>]+\.(jpg|jpeg|png|webp|avif|gif|svg)[^\s"\'<>]*)', re.IGNORECASE),
]

def fetch(url):
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.read().decode('utf-8', errors='ignore')
    except Exception as e:
        print(f'  WARN fetch failed: {url} — {e}')
        return ''

def resolve(href, base):
    """Turn relative or protocol-relative URLs into absolute URLs."""
    href = href.strip()
    if href.startswith('//'):
        return 'https:' + href
    if href.startswith('http'):
        return href
    return urllib.parse.urljoin(base, href)

def extract_img_urls(html, page_url):
    urls = set()
    base = urllib.parse.urlparse(page_url)
    for pat in PATTERNS:
        for m in pat.finditer(html):
            raw = m.group(1)
            # Handle srcset (space-separated list of "url width" pairs)
            if ',' in raw and ' ' in raw:
                for part in raw.split(','):
                    candidate = part.strip().split()[0]
                    if IMG_EXT.search(candidate):
                        urls.add(resolve(candidate, page_url))
            # Handle Wix hashes — prepend CDN base
            elif re.match(r'[a-f0-9]{32}~mv2\.[a-z]{3,4}$', raw, re.IGNORECASE):
                urls.add('https://static.wixstatic.com/media/' + raw)
            else:
                if IMG_EXT.search(raw):
                    urls.add(resolve(raw, page_url))
    return urls

def discover_internal_pages(html, base_url):
    """Find all internal page links to crawl."""
    domain = urllib.parse.urlparse(base_url).netloc
    found = set()
    for m in re.finditer(r'href=["\']([^"\'#?]+)["\']', html):
        href = m.group(1).strip()
        abs_url = resolve(href, base_url)
        parsed = urllib.parse.urlparse(abs_url)
        # Only follow same-domain HTML pages
        if parsed.netloc == domain and not IMG_EXT.search(parsed.path):
            found.add(abs_url.split('?')[0].split('#')[0])
    return found

# --- Main crawl ---
visited_pages = set()
all_img_urls  = set()
queue = [START_URL]

# Also check sitemap.xml for additional pages
sitemap_html = fetch(START_URL + '/sitemap.xml')
for m in re.finditer(r'<loc>([^<]+)</loc>', sitemap_html):
    loc = m.group(1).strip()
    if not IMG_EXT.search(loc):
        queue.append(loc)

while queue:
    page_url = queue.pop(0)
    if page_url in visited_pages:
        continue
    visited_pages.add(page_url)
    print(f'  Crawling: {page_url}')
    html = fetch(page_url)
    if not html:
        continue
    found = extract_img_urls(html, page_url)
    all_img_urls.update(found)
    # Add unvisited internal pages to the queue (max 50 pages)
    if len(visited_pages) < 50:
        for link in discover_internal_pages(html, page_url):
            if link not in visited_pages:
                queue.append(link)

# Write the URL list
out_file = os.path.join(IMG_DIR, '_image_urls.txt')
with open(out_file, 'w') as f:
    for url in sorted(all_img_urls):
        f.write(url + '\n')

print(f'\nFound {len(all_img_urls)} unique image URLs across {len(visited_pages)} pages.')
print(f'URL list written to: {out_file}')
print('Run Stage 2 (download) next.')
```

---

##### Stage 2 — Collect: Review and Clean the URL List

Open `img/_image_urls.txt` and remove any URLs that are clearly not useful for the prototype:

| Remove these | Keep these |
|---|---|
| Tiny tracking pixels (1×1 or under 500 bytes) | Hero photos, section backgrounds |
| Social media platform icons (facebook.com, twitter.com assets) | Team photos, product shots |
| Google Maps embed tiles | Logos, brand graphics |
| Font files accidentally caught by the pattern | Icons used on the site |
| Duplicate images with only `?w=` or `?quality=` query param differences — keep the largest | Any image displayed visibly on any page |

Rename the cleaned file to `_image_urls_clean.txt` before running Stage 3.

---

##### Stage 3 — Download: Pull Every Image Locally

```python
# save as: _tools/download_images.py
# usage:   python3 _tools/download_images.py My Projects/<Agency>/ClientName/img
import sys, os, re, urllib.request, urllib.parse, hashlib, mimetypes

IMG_DIR  = sys.argv[1]
URL_FILE = os.path.join(IMG_DIR, '_image_urls_clean.txt')
HEADERS  = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'}

with open(URL_FILE) as f:
    urls = [line.strip() for line in f if line.strip() and not line.startswith('#')]

def safe_filename(url, index):
    """Derive a clean local filename from the URL."""
    parsed = urllib.parse.urlparse(url)
    basename = os.path.basename(parsed.path.rstrip('/'))
    # Strip query strings from the name
    basename = basename.split('?')[0]
    # Fall back to a hash-based name if basename is empty or too generic
    if not basename or len(basename) < 5 or basename in ('image', 'photo', 'img'):
        ext = mimetypes.guess_extension(mimetypes.guess_type(url)[0] or 'image/jpeg') or '.jpg'
        basename = f'img_{index:03d}{ext}'
    return basename

ok = skip = fail = 0
for i, url in enumerate(urls, 1):
    fname  = safe_filename(url, i)
    fpath  = os.path.join(IMG_DIR, fname)
    # Skip if already downloaded and non-empty
    if os.path.exists(fpath) and os.path.getsize(fpath) > 500:
        print(f'  SKIP  [{i:03d}] {fname}')
        skip += 1
        continue
    try:
        req  = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read()
        if len(data) < 200:          # likely a tracker or empty response
            print(f'  TINY  [{i:03d}] {fname} ({len(data)} bytes) — skipped')
            fail += 1
            continue
        with open(fpath, 'wb') as f:
            f.write(data)
        print(f'  OK    [{i:03d}] {fname}: {len(data):,} bytes')
        ok += 1
    except Exception as e:
        print(f'  FAIL  [{i:03d}] {fname}: {e}')
        fail += 1

print(f'\nDone. Downloaded: {ok}  Skipped: {skip}  Failed: {fail}')
print(f'All images saved to: {IMG_DIR}')
```

---

##### Stage 4 — Verify: Confirm What You Have

After downloading, run this check to see dimensions and file sizes in one view. Use this to decide which images to use for heroes, sections, and cards.

```bash
# macOS — run from the project folder
for f in img/*.jpg img/*.jpeg img/*.png img/*.webp img/*.avif; do
  [ -f "$f" ] || continue
  dims=$(sips -g pixelWidth -g pixelHeight "$f" 2>/dev/null | awk '/pixel/{printf $2"x"}' | sed 's/x$//')
  sz=$(ls -lh "$f" | awk '{print $5}')
  echo "$(basename $f): ${dims} (${sz})"
done | sort
```

**Image assignment guide — use this after verification:**

| Dimension / Orientation | Best Use in Prototype |
|---|---|
| 1920 × 1080 px or larger, landscape | Hero section background, full-bleed photo bands |
| 1200 × 800 px — 1800 × 1200 px, landscape | About page, services section backgrounds |
| 600 × 400 px — 1200 × 800 px, landscape | Card images, testimonial backgrounds, gallery |
| Any portrait (height > width) | Team photos, feature columns, sidebars |
| Under 400 × 400 px | Thumbnails, icon accents — never stretch as a hero |
| PNG with transparency | Logo, graphic overlays — never use as a CSS background |
| SVG | Logo (preferred), icons — scale perfectly at any size |

---

##### Platform-Specific Notes

**Wix (`static.wixstatic.com`):**
The discover script captures Wix hashes directly. All Wix media URLs are publicly accessible with no auth. Full-quality images use the base URL without any `~mv2_d_...~mv2` resizing suffix — the script handles this automatically.

**WordPress (`/wp-content/uploads/`):**
WordPress images are always on the same domain under `/wp-content/uploads/YYYY/MM/`. The crawler catches these automatically. If the site uses a CDN offload plugin (Jetpack CDN, WP Offload Media), the images will be on an external domain — the `PATTERNS` list in the discover script catches these too.

**Squarespace (`sqspcdn.com` or `images.squarespace-cdn.com`):**
Images are served from `images.squarespace-cdn.com`. They appear in `<img>` tags with `data-src` or `src` attributes. The discover script catches both. Append `?format=original` to the URL when downloading to get the full-resolution version instead of a resized variant.

**Shopify (`cdn.shopify.com`):**
Shopify serves all product and theme images from `cdn.shopify.com/s/files/`. These are always publicly accessible. The discover script catches them via the CDN pattern. For product images, strip the `_[size]x` size suffix from the filename (e.g., `product_image_800x.jpg` → `product_image.jpg`) to get the original full-resolution file.

**Cloudinary / Imgix / Fastly / other CDNs:**
These are transformation CDNs — they add size/quality params to URLs. Download the URL exactly as found on the site (it may already be cropped/resized). If you need a larger version, try removing query params or replacing `w_800` with `w_2000` in the URL.

**Images loaded by JavaScript (lazy-load, infinite scroll, carousels):**
Some images only appear after JS execution — the curl-based crawler cannot see them. If the discover script misses images you can see in the browser, open the page in Chrome DevTools → Network tab → filter by "Img" → reload the page — copy any missing URLs manually into `_image_urls_clean.txt` before running Stage 3.

---

##### Using Downloaded Images in the Prototype

Once all images are in `img/`, reference them with relative paths. **Never use the original CDN URLs in the prototype HTML.** The prototype must be fully self-contained and work on `file://`.

```html
<!-- ✅ Correct — relative path to local img/ folder -->
<img src="img/hero.jpg" alt="[Client Name] storefront" />

<!-- ❌ Wrong — external CDN URL; breaks offline, may expire -->
<img src="https://static.wixstatic.com/media/abc123~mv2.jpg" alt="..." />
```

**Always layer a gradient over background photos so text stays readable:**

```css
.hero {
  background:
    linear-gradient(120deg, rgba(7,26,62,0.92) 0%, rgba(13,43,94,0.82) 100%),
    url('img/hero.jpg') center/cover no-repeat;
}
```

---

##### Pre-Launch Checklist for Images

- [ ] `_tools/discover_images.py` was run against the live site covering all pages and the sitemap
- [ ] `img/_image_urls_clean.txt` was reviewed — tracker pixels and platform icons removed
- [ ] `_tools/download_images.py` downloaded all images to `img/` — zero external CDN URLs remain in any HTML file
- [ ] Stage 4 verification run — image dimensions noted and best candidates assigned to hero/section/card roles
- [ ] Logo saved as `img/logo.png` (or `.svg`) — sourced from live site, not recreated
- [ ] All `<img>` tags in the prototype use relative `img/` paths
- [ ] No `<img src="https://...">` pointing to an external domain in any HTML file
- [ ] All images have descriptive `alt` text — no empty `alt=""` on content images
- [ ] All images are responsive: `max-width: 100%; height: auto`

---

#### Part B — Extract the Brand Color Scheme from the Logo

**Method 1 — Python dominant color extraction (recommended):**

```bash
# Install Pillow if needed (one-time)
pip3 install Pillow

python3 -c "
from PIL import Image
import urllib.request, os, collections

# Option A: analyze a local logo file
logo_path = '<ClientName>/img/logo.png'

# Option B: download and analyze the logo directly from the site
# logo_url = 'https://www.clientsite.com/logo.png'
# urllib.request.urlretrieve(logo_url, logo_path)

img = Image.open(logo_path).convert('RGB')
img = img.resize((150, 150))  # shrink for speed

# Count pixels, skip near-white and near-black (background colors)
pixels = list(img.getdata())
filtered = [p for p in pixels if not (p[0]>230 and p[1]>230 and p[2]>230)
                               and not (p[0]<25  and p[1]<25  and p[2]<25)]

counts = collections.Counter(
    ('#%02x%02x%02x' % (r//32*32, g//32*32, b//32*32))
    for r,g,b in filtered
)

print('Top dominant colors (quantized):')
for hex_color, count in counts.most_common(8):
    pct = count / len(filtered) * 100
    print(f'  {hex_color}  ({pct:.1f}%)')
"
```

**Method 2 — macOS built-in Digital Color Meter:**
1. Open the client's website in Safari or Chrome
2. Open **Digital Color Meter** (`/Applications/Utilities/Digital Color Meter.app`)
3. Set display to **Display in sRGB**
4. Hover over each brand color in the logo or navigation and read the R/G/B values
5. Convert to hex: `python3 -c "print('#%02x%02x%02x' % (R, G, B))"`

**Method 3 — Extract colors from the site's CSS directly:**
```bash
# Fetch the main stylesheet and look for CSS custom properties / variables
curl -s "https://www.clientsite.com/" -A "Mozilla/5.0" 2>/dev/null \
  | grep -oE 'href="[^"]+\.css[^"]*"' \
  | head -5

# Then fetch that stylesheet and look for color variables
curl -s "<STYLESHEET_URL>" 2>/dev/null \
  | grep -E '#[0-9a-fA-F]{3,6}|rgb\(' \
  | grep -v '/\*' | head -30
```

**How to use the extracted colors:**

Once you have the dominant hex values, assign them using this guide:

| Role | How to Identify It | CSS Variable |
|---|---|---|
| **Primary / Brand** | The most prominent non-neutral color in the logo | `--brand-color` / `--navy` |
| **Accent / CTA** | A high-contrast secondary color (often orange, red, or gold) | `--accent` / `--orange` |
| **Dark text** | Near-black used for body copy | `--dark` |
| **Muted text** | Mid-gray for secondary copy | `--muted` |
| **Background** | Off-white or light surface color | `--light` |

Document all colors in `brand.html` with swatches before using them anywhere else.

---

#### Part C — Extract the Logo

The logo must be pulled from the client's live website and saved locally before building any HTML page. Never use a placeholder — the real logo must appear in the nav, footer, og:image, and brand guide.

```bash
# Step 1 — Find the logo URL in the page source
# Look for common logo patterns in the HTML: <img> with "logo" in src, site-icon, or favicon link tags
curl -s "https://www.clientsite.com/" -A "Mozilla/5.0" 2>/dev/null \
  | grep -iE '(logo|brand|header).*(src|href)="[^"]+\.(png|svg|avif|jpg|webp)"' \
  | grep -oE '"https://[^"]+"' | head -10

# Step 2 — Also check for WordPress site icon / custom logo
curl -s "https://www.clientsite.com/wp-json/wp/v2/media?search=logo&per_page=5" 2>/dev/null \
  | python3 -c "import sys,json; d=json.load(sys.stdin); [print(x['source_url']) for x in d]"

# Step 3 — Download the logo
curl -L "https://www.clientsite.com/path/to/logo.png" -A "Mozilla/5.0" -o "<AgencyName>/<ClientName>/img/logo.png"
```

**Logo naming rule:** Always save as one of the following (in priority order):
1. `img/logo.svg` — if SVG is available (scales perfectly at any size)
2. `img/logo.png` — PNG with transparency preferred
3. `img/logo-white.png` — white version for use on dark/colored backgrounds (if the site provides one)
4. `img/logo.jpg` — only if no transparent format exists

**Usage rule:** Every HTML page must reference `img/logo.png` (or `.svg`) in the nav and footer — not a text wordmark, not a placeholder div. If the client's site has a white/light variant for dark headers, save it as `img/logo-white.png` and use it on dark backgrounds.

---

#### Part D — Extract Social Media Links

Pull all social media profile links from the client's live website. These must appear in the footer of every page, using the correct Font Awesome icon for each platform.

```bash
# Find all social media profile links in the page source
curl -s "https://www.clientsite.com/" -A "Mozilla/5.0" 2>/dev/null \
  | grep -oE 'https?://(www\.)?(facebook|instagram|twitter|x|linkedin|youtube|tiktok|pinterest|yelp)\.com/[^"&\s]+' \
  | sort -u
```

**Standard social icon mapping (Font Awesome 6):**

| Platform | FA Icon Class | Example URL Pattern |
|---|---|---|
| Facebook | `fa-brands fa-facebook-f` | `facebook.com/pagename` |
| Instagram | `fa-brands fa-instagram` | `instagram.com/handle` |
| Twitter / X | `fa-brands fa-x-twitter` | `x.com/handle` or `twitter.com/handle` |
| LinkedIn | `fa-brands fa-linkedin-in` | `linkedin.com/company/name` |
| YouTube | `fa-brands fa-youtube` | `youtube.com/@channel` |
| TikTok | `fa-brands fa-tiktok` | `tiktok.com/@handle` |
| Pinterest | `fa-brands fa-pinterest-p` | `pinterest.com/handle` |
| Yelp | `fa-brands fa-yelp` | `yelp.com/biz/name` |

**Required HTML pattern for social icons (use in every footer):**

```html
<!-- Social links — always use real URLs from the client's site, never # -->
<div class="social-links">
  <a href="https://www.facebook.com/clientpage" target="_blank" rel="noopener" aria-label="Facebook">
    <i class="fa-brands fa-facebook-f"></i>
  </a>
  <a href="https://www.instagram.com/clienthandle" target="_blank" rel="noopener" aria-label="Instagram">
    <i class="fa-brands fa-instagram"></i>
  </a>
  <!-- Add only the platforms the client actually uses -->
</div>
```

**Rules:**
- Only include platforms the client actually has a presence on — do not add empty or fake links
- Always use `target="_blank" rel="noopener"` on social links
- Always include an `aria-label` matching the platform name for accessibility
- If a social link cannot be found on the live site, search the client's Google Business Profile or ask the user before leaving it blank

---

### Step 2c — Create the Social Share Image (og:image)

Every project must have a **1200 × 630 px** branded image that appears when any page link is shared on social media, in iMessage, Slack, WhatsApp, or any link-preview platform. This is called the **Open Graph image** (`og:image`).

---

#### What the og:image must contain

| Element | Notes |
|---|---|
| **Client logo** | Top-left or centered — always on a branded background |
| **Brand background** | Solid primary color or a subtle photo with dark overlay |
| **One clear headline** | Client name or a short tagline (e.g. "Family-Owned Since 1954") |
| **Supporting detail** | Phone number or service area — something scannable at thumbnail size |
| **No clutter** | Image will display at ~500 px wide in most previews — keep it simple |

#### Required dimensions

| Property | Value |
|---|---|
| Width | **1200 px** |
| Height | **630 px** |
| Aspect ratio | 1.91:1 |
| Format | `.jpg` (smaller file) or `.png` (if logo needs transparency) |
| File size | Under 300 KB — compress before saving |
| File name | `img/og-share.jpg` (use this path on every project for consistency) |

> **Why 1200 × 630?** Facebook, LinkedIn, Twitter/X, iMessage, and Slack all render link previews at this ratio. Images that are too small (under 600 × 315) get shown as tiny thumbnails. Images over 8 MB are rejected entirely.

---

#### How to create the og:image — run the script (standard method)

A reusable script lives at the workspace root: **`make_og_share.py`**

It automatically finds the logo in the project's `img/` folder, scales it to fit a 1200 × 630 branded canvas, adds accent bars, and saves `img/og-share.jpg` — no design tools required.

```bash
# From the workspace root (My Projects/<Agency>/)
python3 make_og_share.py <ClientFolder> "<bg_color>" "<accent_color>"

# Examples:
python3 make_og_share.py JackRobinsonMoving "#0D2B5E" "#E85C1A"
python3 make_og_share.py ArgyleMedSpa      "#2C1A4A" "#C9A96E"
python3 make_og_share.py FirePlus          "#B22222" "#1A1A1A"
```

**What the script does:**
1. Searches `<ClientFolder>/img/` for the logo — checks `logo.avif`, `logo.png`, `logo.jpg`, then any file with "logo" in the name
2. Creates a 1200 × 630 canvas filled with `bg_color`
3. Scales the logo to fit (max 700 × 460 px) and centers it
4. Draws a 12 px left-edge accent bar and a 14 px bottom stripe in `accent_color`
5. Saves as `<ClientFolder>/img/og-share.jpg` at JPEG quality 88

**Logo file naming convention (so the script finds it automatically):**

| Priority | File name | Notes |
|---|---|---|
| 1st | `logo.avif` | Best quality, smallest file — preferred format |
| 2nd | `logo.png` | Use if AVIF not available; supports transparency |
| 3rd | `logo.jpg` | Acceptable; no transparency |
| Fallback | Any file with "logo" in the name | e.g. `JRM Logo 2025_edited.avif` |

> **Best practice:** When extracting the logo from the client's site (Step 2b), save it as `logo.png` or `logo.avif` in the `img/` folder. The script will find it on the first try every time.

---

#### Meta tags to add to every HTML page `<head>`

Add all of the following immediately after `<title>` and `<meta name="description">` on **every page** in the project:

```html
<!-- Open Graph / Social Share -->
<meta property="og:type"        content="website"/>
<meta property="og:url"         content="https://www.clientsite.com/page.html"/>
<meta property="og:title"       content="Page Title — Client Name"/>
<meta property="og:description" content="Page-specific 1–2 sentence description."/>
<meta property="og:image"       content="https://www.clientsite.com/img/og-share.jpg"/>
<meta property="og:image:width"  content="1200"/>
<meta property="og:image:height" content="630"/>
<meta property="og:site_name"   content="Client Company Name"/>
<!-- Twitter / X / iMessage -->
<meta name="twitter:card"        content="summary_large_image"/>
<meta name="twitter:title"       content="Page Title — Client Name"/>
<meta name="twitter:description" content="Page-specific 1–2 sentence description."/>
<meta name="twitter:image"       content="https://www.clientsite.com/img/og-share.jpg"/>
```

**Rules:**
- `og:url` and `og:image` must be **absolute URLs** — social crawlers cannot resolve relative paths
- `og:title` and `og:description` should be **page-specific**, not the same on every page
- The `og:image` URL always points to the same `og-share.jpg` file across all pages (one image for the whole site)
- `twitter:card` must be `summary_large_image` — this is what causes the full-width preview image to appear instead of a tiny thumbnail

#### Testing the share image

Once the site is live on a real domain, validate with these free tools:

| Tool | URL | Tests |
|---|---|---|
| **Facebook Debugger** | https://developers.facebook.com/tools/debug/ | Facebook + iMessage (Apple uses OG tags) |
| **LinkedIn Post Inspector** | https://www.linkedin.com/post-inspector/ | LinkedIn previews |
| **Twitter Card Validator** | https://cards-dev.twitter.com/validator | Twitter / X previews |
| **OpenGraph.xyz** | https://www.opengraph.xyz/ | General preview across all platforms |

> **Prototype note:** The `og:image` URL won't resolve on `localhost` or `file://`. That is expected. Add the correct live domain URL when the site launches so it works immediately on go-live.

---

### Step 2d — Get or Create the Favicon

Every project must have a favicon. **Always ask the user first** before generating or downloading one.

#### Ask the user this question before proceeding:

> *"Do you have a favicon file for [Client Name]? If so, please drop it in the `img/` folder. Accepted formats: `.ico`, `.png` (32×32 or 64×64), or `.svg`. If you don't have one, I'll pull the existing favicon from their live site."*

---

#### Option A — Client provides a favicon (preferred)

If the user supplies a file:
1. Save it as `img/favicon.ico` (or `img/favicon.png` if PNG)
2. Use it in every HTML page's `<head>` (see tag block below)
3. Document it in `brand.html` under the logo section

---

#### Option B — Pull from the live site

If the client does not provide one, check the live site:

```bash
# Check for a declared favicon in the page <head>
curl -s "https://www.clientsite.com/" -A "Mozilla/5.0" \
  | grep -iE '<link[^>]+(icon|shortcut)[^>]+href="([^"]+)"'

# Common fallback locations if no <link> tag is found
# https://www.clientsite.com/favicon.ico
# https://www.clientsite.com/favicon.png
```

Download whichever file resolves and save it to `img/favicon.ico`.

---

#### Option C — No favicon exists on the live site

If the live site has no favicon and the client has not provided one:
1. Use the client's logo mark (square crop, no padding) resized to 64×64 px
2. Save as `img/favicon.png`
3. Note in `brand.html` that the favicon was derived from the logo — the client should commission a proper icon before launch

---

#### Required `<head>` tags for favicon (add to every HTML file)

```html
<link rel="icon" type="image/x-icon" href="img/favicon.ico">
<!-- If using PNG instead of .ico -->
<link rel="icon" type="image/png" sizes="32x32" href="img/favicon.png">
<link rel="apple-touch-icon" sizes="180x180" href="img/favicon.png">
```

---

#### Pre-launch checklist items for favicon

- [ ] `img/favicon.ico` (or `favicon.png`) exists in the project `img/` folder
- [ ] Every HTML page has a `<link rel="icon">` tag in the `<head>`
- [ ] Favicon renders correctly in the browser tab when the file is opened locally
- [ ] If the favicon was sourced from the live site, it matches the client's current branding

---

### Step 3 — Build the Brand Guide First

Before writing a single line of prototype HTML, create `<AgencyName>/<ClientName>/brand.html`. This is **Required Deliverable #1** on every project — not optional.

The brand guide is a single self-contained HTML page (no external dependencies beyond Google Fonts + Tailwind CDN) that documents the complete visual and verbal identity for the client. See **Section: Brand Guide Standard** below for the exact format and required sections.

**How to populate it:**
- Scrape the client's existing website for colors (read CSS variables or computed styles), fonts (Google Fonts or @font-face names), and logo assets.
- If no website exists, use the client's industry, name, and any materials provided to propose a palette and font pairing.
- Confirm the tone-of-voice keywords with the user before finalizing.

The brand guide becomes the **single source of truth** for every color, font, and button used in the prototype and the agreement. Do not use a color or font in any other file that is not first documented in `brand.html`.

### Step 4 — Build the Prototype Website *(Required Deliverable #2 — the site itself)*

Scaffold a prototype using the **FirePlus project as the reference implementation**. Unless the user explicitly says otherwise, the prototype should be planned as a future **React implementation** even if the sales preview is delivered as static HTML for speed.

- Tech: Tailwind Play CDN + DaisyUI CDN + AnimeJS CDN (zero build step, runs on `file://`)
- Data: all site content in `js/site.js` as `window.SITE = { … }`
- Scripts loaded in every HTML page in this order:
  1. `js/site.js`
  2. `js/anim.js`
  3. `js/modal.js`
  4. `js/layout.js`
  5. `js/pages/<page>.js`
- Pages to build: **Home, About, Services, Products, Product Detail, Contact** (adjust per scope)
- Images: **all images must be downloaded locally to `img/`** using the Stage 1–4 process in Step 2b Part A — no hot-linking to Unsplash, Wix CDN, or any external host; every `<img>` and CSS `background-image` must reference a relative `img/` path
- "Add to Quote" / form submissions: prototype modal only (`showPrototypeModal`)
- All asset paths must be **relative** (`./js/`, `./img/`) so the site works on `file://`

### Step 5 — Build the SEO Audit *(Required Deliverable)*

Create `<ClientName>/seo.html`. See **Section: SEO Audit Standard** for the exact required format.

**Process — always do both:**
1. **Ask the user** these targeted questions before building:
   - *"What keywords do you most want to rank for?"*
   - *"Which competitors concern you most?"*
   - *"Are there any SEO gaps or problems you already know about?"*
2. **Research independently** — search the client's name, primary keyword + city, and competitor names to find real review counts, ranking data, and keyword gaps the user may not be aware of.
3. Merge both sources into one cohesive document. Clearly note which findings came from the user vs. independent research.

**Key rules:**
- Include real competitor review counts and ratings sourced from live searches
- The audit must have a score (e.g. X/100), a competitor table, a keyword ranking table, a review breakdown, and a prioritized action plan
- Branding matches the client's palette from `brand.html`

### Step 6 — Build the AEO Page *(Required Deliverable)*

Create `<ClientName>/aeo.html`. See **Section: AEO Standard** for the exact required format.

**Process — always do both:**
1. **Ask the user** these targeted questions before building:
   - *"What are the top 3–5 questions your clients ask most often?"*
   - *"Are there any common misconceptions about your services?"*
   - *"What makes you different from competitors in one sentence?"*
2. **Research independently** — search the client's industry + location to discover additional questions, competitor schema, and gaps the user hasn't mentioned.
3. Merge both into the Q&A bank and schema blocks.

**Key rules:**
- Every business entity fact must be written explicitly and unambiguously
- Include embedded JSON-LD schema for: `Organization`, `LocalBusiness`, `FAQPage`, `HowTo` (where applicable), `Service`
- Write 8–12 Q&A pairs as direct declarative answers — not marketing copy
- Validate all schema with Google's Rich Results Test before marking complete

### Step 7 — Build the Presentation *(Required Deliverable)*

Create `<ClientName>/<ClientName>-Presentation.html`. See **Section: Presentation Standard** for the exact required format. This is a simple, clean slide-style document with labeled image placeholders for the current site and the new prototype pages.

### Step 9 — Prototype → Live Launch Checklist

Run every item below before marking a project ready to present or hand off. This checklist is project-agnostic — it applies to every build regardless of industry or scope.

---

#### ✦ Brand & Visual Integrity

- [ ] `img/logo.png` (or `.svg`) was downloaded from the client's **live website** — not recreated or approximated
- [ ] Logo renders correctly in nav, footer, and brand guide (no broken image, no wrong size)
- [ ] `brand.html` is complete: logo documented with source URL and format, color swatches with hex codes, typography specimens, button demos, tone of voice, logo usage rules
- [ ] Every color used across all HTML files is documented in `brand.html` and was sourced from the live site CSS — no invented colors
- [ ] Every font used across all HTML files matches `brand.html` and the live site's font stack — no substitutions
- [ ] Button padding, border-radius, and hover states match the project's button standard from `brand.html`

---

#### ✦ Required Deliverables

- [ ] `brand.html` — complete, existing logo documented as-is, all brand tokens present, tone of voice written
- [ ] Prototype pages — all live-site pages mirrored, each with HTML comment documenting source URL and UX improvements
- [ ] `login.html` — fully designed with form, validation states, link to forgot-password and register
- [ ] `forgot-password.html` — email input, submit confirmation state, back-to-login link
- [ ] `reset-password.html` — new password + confirm fields, success state, back-to-login link
- [ ] `admin.html` — configuration panel with GA Measurement ID, GSC verification tag, GTM container ID, and SendGrid API key fields
- [ ] `seo.html` — real competitor data, keyword table with search volumes, score X/100, user input incorporated, independent gap research documented
- [ ] `aeo.html` — entity facts documented, 8–12 Q&A pairs as direct answers, JSON-LD schema embedded and validated, user Q&A input incorporated
- [ ] `<ClientName>-Presentation.html` — slide-style, before/after image placeholders labeled, simple clean design
- [ ] Gap analysis reported to user — list of missing pages, flows, or industry-standard features with recommendations

---

#### ✦ Meta Tags & Social Sharing

- [ ] Every page has a unique `<title>` tag (not the same on every page)
- [ ] Every page has a unique `<meta name="description">` (150–160 characters, page-specific)
- [ ] `og:title` is set and page-specific
- [ ] `og:description` is set and page-specific
- [ ] `og:url` is an **absolute URL** and is page-specific (not the same on every page)
- [ ] `og:image` points to the absolute URL of `img/og-share.jpg`
- [ ] `og:image:width` is `1200` and `og:image:height` is `630`
- [ ] `og:type` is `website`
- [ ] `og:site_name` matches the client's brand name
- [ ] `twitter:card` is `summary_large_image`
- [ ] `twitter:title`, `twitter:description`, and `twitter:image` are all set
- [ ] `img/og-share.jpg` exists at exactly **1200 × 630 px**, under 300 KB, with real logo + brand background color
- [ ] `img/favicon.ico` or `img/favicon.png` exists in the project folder (sourced from live site or provided by client — never skipped)
- [ ] Every HTML page has a `<link rel="icon">` tag pointing to the favicon
- [ ] Favicon renders correctly in the browser tab when opened locally

---

#### ✦ Schema / Structured Data (SEO + AEO)

- [ ] `Organization` or `LocalBusiness` JSON-LD is present on every page (name, url, telephone, address, sameAs social links)
- [ ] `FAQPage` schema is present on any page with FAQ content (matches the Q&A pairs in `aeo.html`)
- [ ] `HowTo` schema is present where applicable (e.g. multi-step service or process pages)
- [ ] `Service` schema is present on each services page with `name`, `description`, and `provider`
- [ ] `BreadcrumbList` schema is present on inner pages (About, Services, Contact)
- [ ] All schema validated with **Google Rich Results Test** (`search.google.com/test/rich-results`) — zero errors, zero warnings
- [ ] Entity facts in schema match `aeo.html` exactly (name, phone, address, hours, service area)

---

#### ✦ Mobile & Responsive

- [ ] Hamburger / mobile menu opens and closes correctly on phones and tablets
- [ ] All nav links in the mobile menu work and close the menu after tapping
- [ ] Hero text is readable on mobile (no overflow, no clipping)
- [ ] All images are responsive (`max-width: 100%`, no horizontal scroll)
- [ ] Forms are usable on a 375 px wide screen (inputs don't overflow, labels are visible)
- [ ] Tap targets (buttons, links) are at least 44 × 44 px on mobile
- [ ] Footer links and social icons are tappable without zooming
- [ ] No horizontal scroll on any page at 375 px, 768 px, or 1280 px viewport widths

---

#### ✦ Navigation & Links

- [ ] Every nav link on every page works correctly with relative paths (`./about.html`, not `/about.html`)
- [ ] Footer links all work
- [ ] Social media links open in `target="_blank"` with `rel="noopener"` and go to the real client profiles — never `#`
- [ ] CTA buttons on every page link to the correct destination (contact form, phone, or specific page)
- [ ] All internal anchor links (`#section`) scroll to the correct element
- [ ] `404.html` exists and contains client-specific clever copy — no `{{TOKEN}}` placeholders remain
- [ ] Every other linked file exists in the project folder (no broken internal links)
- [ ] Phone number links use `href="tel:..."` format
- [ ] Email links use `href="mailto:..."` format

---

#### ✦ Forms & Contact

- [ ] Contact form submits without errors (or shows the prototype modal correctly)
- [ ] All form fields have visible `<label>` elements associated via `for`/`id`
- [ ] Required fields are marked and validated before submit
- [ ] Success and error states are visible (confirmation message or prototype modal)
- [ ] No form action points to a dead endpoint in the prototype

---

#### ✦ Images & Performance

- [ ] All images have descriptive `alt` text (no empty `alt=""` on content images)
- [ ] Hero images have a dark overlay/gradient so text is readable at all screen sizes
- [ ] Logo is not used as a background image — it is always an `<img>` tag
- [ ] Images do not cause layout shift on load (width and height attributes set, or CSS aspect-ratio applied)
- [ ] Page loads in under 3 seconds on a simulated mobile connection (check with browser DevTools throttling)

---

#### ✦ Accessibility

- [ ] All images have `alt` attributes
- [ ] Color contrast meets WCAG AA (4.5:1 for body text, 3:1 for large text) — verify with browser DevTools or Colour Contrast Analyser
- [ ] All interactive elements (buttons, links, inputs) are reachable by keyboard Tab key
- [ ] Focus state is visible on all interactive elements (never `outline: none` without a replacement style)
- [ ] Heading hierarchy is logical: one `<h1>` per page, `<h2>` for sections, `<h3>` for subsections — no skipped levels

---

#### ✦ Auth Views

- [ ] `login.html` — email + password fields, submit button, "Forgot password?" link, "Create account" link, error state visible
- [ ] `forgot-password.html` — email input, submit confirmation state, back-to-login link, no dead ends
- [ ] `reset-password.html` — new password + confirm password fields, show/hide toggle, success state, back-to-login link
- [ ] All auth views use the client's brand colors and logo from `brand.html`
- [ ] All auth forms validate required fields client-side before showing a prototype modal response

---

#### ✦ Admin Panel

- [ ] `admin.html` — all four integration fields present and labeled: Google Analytics Measurement ID, Google Search Console verification tag, Google Tag Manager container ID, SendGrid API key
- [ ] Each field has a save/update button and a visual confirmation state
- [ ] Admin panel is password-protected in the prototype (even a simple hardcoded PIN is acceptable)
- [ ] Admin panel is mobile-responsive

---

#### ✦ Final Housekeeping

- [ ] Sales Tracker `index.html` has a card for this client with correct status
- [ ] All required deliverables are linked from the client card in the Sales Tracker
- [ ] `<ClientName>/references/` folder contains any competitor research, brand notes, or screenshots from the project
- [ ] No placeholder content remains: no "Lorem ipsum", no `href="#"` on real links, no "TBD" in visible copy
- [ ] Gap analysis has been presented to the user

---

---

## UI Design Standards — Buttons

> These rules apply to **every button in every project**, regardless of brand. The only thing that changes is the brand color and the hover animation style — which is always chosen to match the company's industry and tone.

---

### Rule 1 — Contrast Is Non-Negotiable

Every button must have readable text at all times — default state AND hover state.

| Background | Required text color |
|---|---|
| Dark (brand primary, navy, black, deep green, etc.) | `#ffffff` white |
| Light (white, off-white, light gray) | Brand primary color (dark) |
| Accent/mid-tone | Whichever of white or brand-dark achieves higher contrast — test it |

**Never** use a brand color as both background and text. **Never** use a gray text on a light button. **Never** trust "it looks fine" — if a human would squint to read it, it fails.

---

### Rule 2 — Always Set the Border

Set `border: 2px solid` on every button, in every state. If the border is absent on the default state and appears on hover, the button will jump in size and break layout.

```
Default state:  border: 2px solid var(--brand-primary);
Hover state:    border: 2px solid var(--brand-primary);  ← same, never change this
```

---

### Rule 3 — Hover Animation Must Match the Brand Tone

Every button gets a hover animation. The animation is not decoration — it signals the brand's personality. Choose from the table below based on the industry.

| Industry / Tone | Animation to use | What it feels like |
|---|---|---|
| **Tech / SaaS / Software** | Glowing box-shadow pulse + slight scale-up | Energetic, digital, alive |
| **Professional Services / Law / Finance / Consulting** | Subtle underline-slide or left-border-reveal + no transform | Controlled, authoritative, elegant |
| **Home Services / Trades (HVAC, Plumbing, Roofing)** | Solid fill invert (brand ↔ white swap) + mild lift | Dependable, no-nonsense |
| **Med Spa / Aesthetics / Luxury** | Soft shimmer sweep (shine passes left-to-right) + no transform | Premium, refined, sensory |
| **Restaurant / Food / Hospitality** | Warm background shift + scale-up | Welcoming, approachable |
| **Real Estate** | Border thickens + background lightens | Stable, trustworthy, upscale |
| **Retail / E-commerce** | Bounce (`translateY(-3px)`) + shadow deepens | Playful, tactile, shoppable |
| **Fitness / Sports / Outdoors** | Fast invert + scale-up | Bold, confident, high-energy |
| **Security / Fire / Safety** | Solid fill invert (no transform, fast transition) | Serious, reliable, instant |
| **Pet Services / Kids / Family** | Bounce + slight border-radius increase | Friendly, joyful, approachable |

> When in doubt: if the client wears a suit, use a classy animation. If the client wears a uniform or logo tee, use a confident invert. If the client wears a lab coat, use restraint.

---

### The Three Button Variants

Every project ships with all three. Never invent a fourth.

#### Primary (dark background → light text)

Used for the main CTA — "Get a Quote", "Schedule Now", "Book Today".

```css
.btn-primary {
  display: inline-block;
  padding: 12px 28px;
  border-radius: 6px;
  border: 2px solid var(--brand-primary);
  background: var(--brand-primary);
  color: #ffffff;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  text-decoration: none;
  cursor: pointer;
  transition: background 0.22s ease, color 0.22s ease, transform 0.18s ease, box-shadow 0.22s ease;
}
/* Hover — replace with industry-appropriate animation from the table above */
.btn-primary:hover {
  background: #ffffff;
  color: var(--brand-primary);
  transform: translateY(-2px);
  box-shadow: 0 6px 18px rgba(0,0,0,.12);
}
```

#### Outline / Secondary (transparent background → brand text)

Used for secondary actions — "Learn More", "See Our Work", "Download Report".

```css
.btn-outline {
  display: inline-block;
  padding: 12px 28px;
  border-radius: 6px;
  border: 2px solid var(--brand-primary);
  background: transparent;
  color: var(--brand-primary);
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  text-decoration: none;
  cursor: pointer;
  transition: background 0.22s ease, color 0.22s ease, transform 0.18s ease, box-shadow 0.22s ease;
}
.btn-outline:hover {
  background: var(--brand-primary);
  color: #ffffff;
  transform: translateY(-2px);
  box-shadow: 0 6px 18px rgba(0,0,0,.12);
}
```

#### On-Dark (used inside dark hero sections or dark callout cards)

When the surrounding section has a dark background, the button must start white so the text (brand color) remains readable. On hover it inverts to transparent with white text.

```css
.btn-on-dark {
  display: inline-block;
  padding: 12px 28px;
  border-radius: 6px;
  border: 2px solid #ffffff;
  background: #ffffff;
  color: var(--brand-primary);
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  text-decoration: none;
  cursor: pointer;
  transition: background 0.22s ease, color 0.22s ease, transform 0.18s ease;
}
.btn-on-dark:hover {
  background: transparent;
  color: #ffffff;
  transform: translateY(-2px);
}
```

---

### Industry Hover Animation Snippets

Copy the appropriate block into the project's CSS, replacing the generic hover above.

**Tech / SaaS — glowing pulse:**
```css
.btn-primary:hover {
  background: #ffffff;
  color: var(--brand-primary);
  box-shadow: 0 0 0 4px rgba(var(--brand-primary-rgb), 0.25), 0 8px 24px rgba(0,0,0,.14);
  transform: scale(1.03);
}
```

**Law / Finance / Consulting — border-slide, no lift:**
```css
.btn-primary {
  position: relative;
  overflow: hidden;
}
.btn-primary::after {
  content: '';
  position: absolute;
  bottom: 0; left: 0;
  width: 0; height: 2px;
  background: var(--brand-accent);
  transition: width 0.3s ease;
}
.btn-primary:hover::after { width: 100%; }
.btn-primary:hover {
  background: #ffffff;
  color: var(--brand-primary);
  transform: none;
  box-shadow: none;
}
```

**Med Spa / Luxury — shimmer sweep:**
```css
.btn-primary {
  position: relative;
  overflow: hidden;
}
.btn-primary::after {
  content: '';
  position: absolute;
  top: 0; left: -75%;
  width: 50%; height: 100%;
  background: linear-gradient(120deg, transparent 0%, rgba(255,255,255,.35) 50%, transparent 100%);
  transform: skewX(-20deg);
  transition: left 0.5s ease;
}
.btn-primary:hover::after { left: 130%; }
.btn-primary:hover {
  background: var(--brand-primary);
  color: #ffffff;
  transform: none;
  box-shadow: 0 4px 20px rgba(0,0,0,.15);
}
```

**Home Services / Trades — solid invert + lift:**
```css
.btn-primary:hover {
  background: #ffffff;
  color: var(--brand-primary);
  transform: translateY(-3px);
  box-shadow: 0 8px 20px rgba(0,0,0,.16);
}
```

**Retail / E-commerce — bounce:**
```css
.btn-primary:hover {
  background: #ffffff;
  color: var(--brand-primary);
  transform: translateY(-4px);
  box-shadow: 0 10px 24px rgba(0,0,0,.18);
}
```

---

### Never Do This

- ❌ No `border: none` on any button — ever. Always set `border: 2px solid` explicitly.
- ❌ No hard-coded hex colors in button rules — always use `var(--brand-primary)` or `var(--brand-accent)`.
- ❌ No same color for both background and text — light text on light background is invisible.
- ❌ No `border-radius > 8px` — pill buttons are not part of this system.
- ❌ No emoji or icon-only buttons without visible text labels.
- ❌ No generic `opacity: .88` hover — that is a fallback, not an animation.
- ❌ No missing hover animation — every button must have one, and it must fit the brand tone.
- ❌ **Never mix DaisyUI size modifiers (`btn-xs`, `btn-sm`) with custom color classes.** Always use `btn-lg` when DaisyUI is present. `btn-sm` collapses height to 2rem and breaks padding.

```html
<!-- ✅ Correct (DaisyUI project) -->
<a href="contact.html" class="btn btn-red btn-lg">Request Consultation</a>

<!-- ❌ Wrong — btn-sm collapses height, shape breaks -->
<a href="contact.html" class="btn btn-red btn-sm">Request Consultation</a>
```

---

## UI Design Standards — Input Fields

> These rules apply to **every `<input>`, `<select>`, and `<textarea>` in every project**, regardless of brand. They exist to prevent text from touching the edge of a field and to ensure consistent cross-browser rendering.

### The Rule

| Property | Value |
|---|---|
| `padding` | `0 0 0 20px` — left padding only; vertical centering is handled by `min-height` + `line-height` |
| `min-height` | `52px` — prevents collapsed inputs on Safari and mobile |
| `line-height` | `1.5` — prevents text from being vertically clipped |
| `border` | `1.5px solid [light-gray]` — visible but not heavy (e.g. `#e5e7eb`) |
| `border-radius` | `8px` |
| `font-family` | **must match the project's body font** — browsers do not inherit font into inputs automatically |
| `font-size` | `15px` |
| `color` | Project's dark text color (e.g. `#1e2025` or `#2d3436`) |
| `background` | `#ffffff` |
| `box-sizing` | `border-box` — required so `width:100%` + padding don't overflow the container |
| `-webkit-appearance` | `none` — removes Safari/Chrome native input chrome that can collapse padding |
| Focus `border-color` | Project's brand color |
| Focus `outline` | `none` |

### Why `padding: 0 0 0 20px`

Using only left padding keeps the field height controlled entirely by `min-height` and `line-height`, avoiding conflicts with vertical padding on different browsers. The `20px` left value ensures text is never flush with the left border.

### Why `-webkit-appearance: none` Is Required

Safari and Chrome apply native OS-level styling to inputs (`-webkit-appearance: auto`). This can add internal padding, background gradients, or border treatments that collapse or ignore the CSS padding you set. Setting `-webkit-appearance: none` disables native chrome entirely and hands full control back to your CSS.

### CSS Pattern (copy and adapt per project)

```css
input, select, textarea {
  width: 100%;
  padding: 0 0 0 20px;          /* left padding only — do not add top/bottom here */
  min-height: 52px;             /* controls field height; line-height centers the text vertically */
  line-height: 1.5;
  border: 1.5px solid #e5e7eb;
  border-radius: 8px;
  font-family: inherit;         /* or match project body font explicitly */
  font-size: 15px;
  color: var(--text-dark);
  background: #ffffff;
  box-sizing: border-box;
  -webkit-appearance: none;     /* prevents Safari from collapsing padding */
  transition: border-color 0.2s ease;
}

input:focus, select:focus, textarea:focus {
  outline: none;
  border-color: var(--brand-color);
}

textarea {
  resize: vertical;
  min-height: 140px;
}
```

### Label Rules

| Property | Value |
|---|---|
| `display` | `block` |
| `font-size` | `12px`–`13px` |
| `font-weight` | `700` |
| `text-transform` | `uppercase` |
| `letter-spacing` | `0.06em` |
| `margin-bottom` | `10px` — **minimum**; never less than `8px` or the label and field touch |
| `color` | Muted dark (e.g. `#4b5563`) — not full black, not brand color |

### Form Group Spacing

```css
.form-group {
  margin-bottom: 24px;   /* vertical rhythm between fields */
}
```

For side-by-side field rows (e.g. First Name / Last Name):

```css
.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
}
```

### Never Do This

- ❌ No `padding: 0` — always include the `20px` left value
- ❌ No `min-height` omitted — inputs will collapse on Safari
- ❌ No `font-family: sans-serif` on inputs — always match the project font explicitly
- ❌ No `box-sizing: content-box` — `width: 100%` will overflow when padding is added
- ❌ No `-webkit-appearance` omitted on projects targeting Safari or mobile
- ❌ No `label margin-bottom` less than `8px` — text and field will appear merged
- ❌ No `outline: auto` on focus — always set `outline: none` and style `border-color` instead

---

## UI Design Standards — Responsive & Mobile

> These rules apply to **every HTML file in every project** — prototype pages, brand guide, seo.html, aeo.html, marketing plan, social media plan, proposal, and agreement. Every deliverable must be fully usable on a phone without horizontal scrolling, pinching, or zooming.

### The Mobile-First Rule

Build styles for the smallest screen first, then add breakpoints for larger screens. Never design desktop-first and try to squeeze it onto mobile afterward.

### Required Breakpoints

| Breakpoint | Width | Use |
|---|---|---|
| **Mobile** | `< 768px` | Base styles — single-column layout, stacked nav |
| **Tablet** | `768px – 1024px` | 2-column grids, side-by-side cards |
| **Desktop** | `> 1024px` | Full layout, multi-column grids, max-width container |

### Standard CSS Pattern

```css
/* Mobile first — no media query needed for base styles */
.container {
  width: 100%;
  padding-inline: 20px;   /* 20px side gutters on mobile */
}

/* Tablet */
@media (min-width: 768px) {
  .container { padding-inline: 32px; }
  .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; }
}

/* Desktop */
@media (min-width: 1024px) {
  .container { max-width: 1400px; margin-inline: auto; padding-inline: 40px; }
  .grid-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 28px; }
}
```

### Navigation — Hamburger Menu Required

Every prototype must have a working hamburger menu on mobile. No exceptions — a desktop nav that is hidden on small screens without a mobile replacement is a blocking defect.

**Required behavior:**
- Desktop nav (`≥ 768px`): horizontal link row, visible
- Mobile nav (`< 768px`): hamburger icon (≥ 44 × 44 px tap target), toggles a full-width dropdown or slide-in panel
- Tapping a mobile nav link closes the menu
- The active page link is visually highlighted in both nav states

**Minimal hamburger pattern (pure CSS + one line of JS):**

```html
<!-- In <head> -->
<style>
  .nav-links { display: flex; gap: 24px; }
  .hamburger { display: none; cursor: pointer; background: none; border: none; padding: 10px; }
  @media (max-width: 767px) {
    .nav-links { display: none; flex-direction: column; position: absolute;
                 top: 100%; left: 0; right: 0; background: var(--dark);
                 padding: 16px 20px; gap: 0; z-index: 100; }
    .nav-links.open { display: flex; }
    .nav-links a { padding: 12px 0; border-bottom: 1px solid rgba(255,255,255,0.1); }
    .hamburger { display: block; }
  }
</style>

<!-- In <body> -->
<button class="hamburger" aria-label="Open menu" onclick="this.closest('header').querySelector('.nav-links').classList.toggle('open')">
  ☰
</button>
<nav class="nav-links">
  <a href="index.html">Home</a>
  <a href="about.html">About</a>
  <a href="services.html">Services</a>
  <a href="contact.html">Contact</a>
</nav>
```

### Touch Target Rule

Every tappable element (button, link, nav item, icon) must be **at least 44 × 44 px** on mobile. Use padding to hit the size without changing the visual appearance:

```css
nav a {
  display: inline-block;
  padding: 10px 8px;   /* enlarges tap area without changing visual width */
  min-height: 44px;
  line-height: 24px;
}
```

### Max Content Width

**All content is hard-capped at `max-width: 1400px` on desktop.** No page, section, grid, or element may render wider than 1400px. Full-bleed backgrounds (hero sections, colored bands) span 100% width, but the content inside them is always wrapped in a `.container` div with `max-width: 1400px` applied. This rule applies to every prototype page, every report template, every auth view, and the admin panel — no exceptions.

### Images on Mobile

```css
img {
  max-width: 100%;
  height: auto;
  display: block;
}
```

Never set a fixed pixel `width` on an image without also setting `max-width: 100%`. Fixed-width images are the most common cause of horizontal scroll on mobile.

### Grid → Stack Pattern

**Every multi-column layout must collapse to a single column on mobile. This is non-negotiable.** Write base styles as single-column first, then add columns at wider breakpoints. Never write multi-column as the default and try to override it for mobile.

This rule applies to: CSS grids, flexbox rows, card rows, two-up image + text splits, icon grids, stat rows, comparison tables, footer columns — everything.

```css
/* ❌ Wrong — multi-column as base, will overflow on mobile */
.cards { display: grid; grid-template-columns: repeat(3, 1fr); }

/* ✅ Correct — single column base, columns added at wider breakpoints */
.cards { display: grid; grid-template-columns: 1fr; gap: 16px; }
@media (min-width: 768px)  { .cards { grid-template-columns: 1fr 1fr; } }
@media (min-width: 1024px) { .cards { grid-template-columns: repeat(3, 1fr); } }
```

```css
/* ❌ Wrong — flex row with no wrap, overflows on mobile */
.row { display: flex; gap: 24px; }

/* ✅ Correct — stacks on mobile, goes side-by-side on tablet+ */
.row { display: flex; flex-direction: column; gap: 16px; }
@media (min-width: 768px) { .row { flex-direction: row; gap: 24px; } }
```

### Required Viewport Testing Before Handoff

Test every page at all three of the following widths — in the browser DevTools device emulator or on a real device:

| Width | Represents | What to verify |
|---|---|---|
| **375 px** | iPhone SE / most small Android phones | All content stacks, no horizontal scroll, hamburger works |
| **768 px** | iPad portrait / large phone landscape | 2-column layouts appear, nav transitions correctly |
| **1400 px** | Wide desktop — the hard content ceiling | Container hits max-width, nothing bleeds wider than 1400px |
| **1920 px** | Large monitor | Background fills edge-to-edge, content stays within 1400px container |

**Pass criteria at 375 px:**
- [ ] No horizontal scrollbar
- [ ] Hamburger menu opens and closes
- [ ] All text is readable without zooming
- [ ] All buttons are tappable (≥ 44 × 44 px)
- [ ] Forms are usable (labels visible, inputs don't overflow)
- [ ] Images fit within the viewport

### Never Do This

- ❌ **No container wider than 1400px** — this is the hard desktop ceiling for all content
- ❌ **No multi-column layout as the base style** — always start single-column, add columns at `768px`+
- ❌ No fixed-width elements without `max-width: 100%` — they will overflow on mobile
- ❌ No `overflow: hidden` on `<body>` that blocks scrolling permanently on mobile
- ❌ No `font-size` below `14px` on body text on mobile — fails WCAG contrast thresholds
- ❌ No desktop nav hidden on mobile without a working hamburger replacement
- ❌ No `vh` heights on hero sections without a `min-height` fallback (`100vh` renders wrong on mobile browsers with dynamic toolbars)
- ❌ No side-by-side columns in tables or flex rows on mobile without a scroll wrapper or stack fallback
- ❌ No hardcoded pixel widths on images — always `max-width: 100%; height: auto`
- ❌ No absolute-positioned elements that bleed outside the 1400px container on wide screens

---

## Brand Guide Standard

> Every new project **must include** a `brand.html` file. This is the single source of truth for all visual and verbal decisions across the prototype. It documents the client's **existing** brand — never invents new brand elements.

### Required Sections in Every `brand.html`

| Section | What to include |
|---|---|
| **Logo** | The actual logo pulled from the live site — displayed prominently. Document: file format (SVG/PNG/JPG), source URL it was pulled from, dimensions, and which backgrounds it works on. Note if only one variant exists. **Never redesign or recreate it.** |
| **Color Palette** | Colors extracted from the live site CSS and/or logo — shown as swatches with hex code and usage note (e.g. "use for CTAs and active nav links"). Label the source of each color (CSS variable, inline style, logo extraction). |
| **Typography** | Fonts pulled from the live site's `<link>` tags or `@font-face` rules — heading font (name, weights, CDN link) and body font. Include live rendered specimens H1–H4 + body paragraph. |
| **Tone of Voice** | 3–5 keywords that describe how the client already communicates on their site (e.g. "Direct, Local, Trustworthy"). What their current copy says well. What to avoid in the prototype. Include one "Write like this" and one "Not like this" example derived from their actual site copy. |
| **Buttons** | Visual demo of primary, outline, and on-dark button variants using the extracted brand colors |
| **Iconography** | Icon library used in the prototype (e.g. Font Awesome, Lucide) — match what the live site uses if possible |
| **Spacing & Layout** | Max content width, section vertical padding, card border-radius and shadow — all matched to the live site's visual rhythm |

### How to Build `brand.html`

1. **Build it first, before any prototype page.** Every color, font, and button in every other file must come from here.
2. **Pull everything from the live site** — colors from CSS, fonts from `<link>` tags, logo from the DOM. Document the source of each item.
3. Each section is a visually distinct card or row — the guide must be usable, not a text list.
4. Buttons must be live HTML elements (demonstrating hover animation).
5. **Confirm tone-of-voice keywords with the user before finalizing** — ask once, then document the confirmed keywords.

### Example Color Swatch Format

```html
<div style="background:#c42436; width:80px; height:80px; border-radius:6px;"></div>
<p><strong>#c42436</strong> — Brand Red</p>
<p style="font-size:12px; color:#666;">CTAs, active states, accent borders</p>
```

---

## SEO Audit Standard

> Every project **must include** a `seo.html` file (previously called `audit.html`). This is the competitive intelligence report that justifies the investment — it shows the client exactly where they stand on Google relative to competitors and gives a clear, prioritized path forward.

### ⚠ Mandatory Template

**Every `seo.html` must be built from `_templates/seo-template.html`.** Do not invent a new layout. Do not improvise structure. Copy the template, replace every `{{TOKEN}}` with real client data, apply the client's brand colors from `brand.html`, and swap in the client's logo.

**Token replacement rules:**
- `{{CLIENT_NAME}}` — the client's business name exactly as it appears on their live site
- `{{LOGO_PATH}}` — relative path to the client's logo file (e.g., `img/logo.png`)
- `{{BRAND_PRIMARY}}`, `{{BRAND_ACCENT}}`, `{{BRAND_DARK}}`, `{{BRAND_LIGHT}}`, `{{BRAND_TEXT}}` — pulled from `brand.html`
- `{{REPORT_DATE}}` — current month and year (e.g., "August 2026")
- All score tokens (`{{TOTAL_SCORE}}`, `{{ORGANIC_SCORE}}`, etc.) — calculated per the Score Calculation Guide below
- All `{{COLOR}}` tokens — set to `green`, `yellow`, or `red` based on score thresholds
- All `{{PCT}}` tokens — percentage of max points earned (e.g., if organic score is 18/25, set `{{ORGANIC_PCT}}` to `72`)
- All keyword, competitor, GBP, and action plan tokens — populated from live research

**Do not leave any `{{TOKEN}}` in the final delivered file.** Every placeholder must be replaced before delivery.

### Required Sections in Every `seo.html`

| Section | Content |
|---|---|
| **Hero / Score Card** | Overall presence score (X/100) · Score category label (e.g. "Opportunity Stage") · 3–4 hero stats (organic rank, Google reviews, monthly searches, website grade) |
| **Score Breakdown** | 4 scored categories as progress bars: Organic Visibility / Google Reviews / Website Quality / Local Citations — each out of a defined max and color-coded green/yellow/red |
| **Keyword Rankings** | Table of 6–10 target keywords with: estimated rank, monthly search volume, trend, and status badge (Ranking / Competitive / Gap Opportunity) |
| **Competitor Table** | 5–7 real competitors found in live Google searches — with review count, star rating, threat level (High/Medium/Low), and a one-sentence note explaining the threat |
| **Review Breakdown** | Where the client's reviews currently live (Google, Yelp, Facebook, industry platforms) and the total count per platform — with a callout if Google reviews are the weak point |
| **Action Plan** | Top 3 prioritized recommendations, numbered 1–3 in order of ROI, each with a title, explanation, and effort/impact label |
| **Unfair Advantages** | A dark callout card listing 3–5 things the client already has that competitors don't (e.g. local since X year, specific license, address advantage) |
| **Footer** | Created by Mike Montes · Prepared for [Client] · Month Year |

### SEO Audit Research Rules

- **Always search before writing.** Use web search to find the client's actual Google reviews count and top competitors before filling in the audit.
- Competitor review counts and ratings must be based on real data — do not invent numbers.
- Keyword search volumes should reflect realistic local market estimates for the client's city and industry.
- The score (X/100) should be calculated honestly — a client with no Google reviews and a poor website should score low (50–65), not high.
- The action plan must be ordered by **ROI / ease of impact** — not alphabetically or randomly.
- Branding: use the client's palette from `brand.html` for the score color, section labels, and callout cards — only colors documented in `brand.html` may be used.
- File name: `<AgencyName>/<ClientName>/seo.html`

### Score Calculation Guide

| Category | Max Points | How to Score |
|---|---|---|
| Organic Visibility | 25 | Top 3 organic rank = 22–25 · Page 1 = 15–21 · Page 2+ = 0–10 |
| Google Reviews | 25 | 100+ reviews = 22–25 · 25–99 = 15–21 · Under 25 = 0–10 · 0 = 0 |
| Website Quality | 30 | Modern + mobile + fast = 25–30 · Outdated Wix/Squarespace = 12–18 · No site = 0 |
| Local Citations | 20 | Listed on 5+ directories with consistent NAP = 18–20 · Partial = 10–16 · Missing = 0–8 |

### Google Business Profile (GBP) Audit (required in every `seo.html`)

> Every `seo.html` must include a dedicated GBP section. The GBP is often the highest-ROI improvement available to a local business — always check it and always report on it honestly.

**Research the client's GBP by searching Google for: `[Business Name] [City]` and checking the Knowledge Panel.**

| GBP Field | What to Check | Score Impact |
|---|---|---|
| **Listing claimed?** | Is the business verified? Unclaimed = critical failure | −10 if unclaimed |
| **Business name** | Exact match to real business name (no keyword stuffing) | Flag if stuffed |
| **Primary category** | Is it the most specific, accurate category available? | Note if improvable |
| **Secondary categories** | Are all relevant secondary categories added? | Note gaps |
| **Address / Service area** | Correct and complete? Service-area businesses should hide address | Note issues |
| **Phone number** | Matches website and other listings (NAP consistency)? | Flag mismatches |
| **Website link** | Points to correct page (homepage or location page)? | Flag if missing/wrong |
| **Hours** | Accurate and complete including holiday hours? | Flag if missing |
| **Photos** | Owner-uploaded photo count — logo, cover, team, work samples | Score: 10+ = good, <5 = weak |
| **Review count & rating** | Total reviews and average star rating | Scored in main SEO score |
| **Review responses** | Does the owner respond to reviews? | Flag if none |
| **Posts activity** | Has the business posted to GBP in the last 30 days? | Flag if inactive |
| **Q&A section** | Are there unanswered questions? Any spam? | Flag issues |
| **Products/Services listed** | Are services or products added to the profile? | Note if empty |
| **Attributes** | Relevant attributes added (e.g., "Women-owned," "Veteran-owned," accessibility)? | Note gaps |

**GBP Scoring (add to existing score card as a 5th category):**

| Category | Max Points | How to Score |
|---|---|---|
| GBP Completeness | 20 | Claimed + all fields complete + 10+ photos + active posts = 18–20 · Claimed but incomplete = 10–16 · Unclaimed = 0 |

**GBP Section Output Format:**

```
GOOGLE BUSINESS PROFILE AUDIT — [ClientName]

Status: [Claimed ✅ / Unclaimed ❌ / Suspended ⚠️]
Overall GBP Score: [X/20]

Field Audit:
✅ / ❌  Business Name: [value] — [note]
✅ / ❌  Primary Category: [value] — [note if improvable]
✅ / ❌  Phone: [value] — NAP match: [Yes/No]
✅ / ❌  Website: [URL] — [correct/incorrect/missing]
✅ / ❌  Hours: [complete/incomplete/missing]
✅ / ❌  Photos: [count] owner-uploaded — [assessment]
✅ / ❌  Review responses: [Yes — owner responds / No — no responses found]
✅ / ❌  Recent posts: [Last post: X days ago / No posts found]
✅ / ❌  Q&A: [X questions — Y unanswered]
✅ / ❌  Services listed: [Yes / No]

Top 3 GBP Improvements (ordered by ROI):
1. [Action] — [Why it matters]
2. [Action] — [Why it matters]
3. [Action] — [Why it matters]
```

---

## AEO Standard

> Every project **must include** an `aeo.html` file. This is the Answer Engine Optimization deliverable — it documents and embeds the structured content, entity data, and schema that causes Google AI Overviews, ChatGPT, Perplexity, Gemini, and other AI engines to quote the client's site by name.

### ⚠ Mandatory Template

**Every `aeo.html` must be built from `_templates/aeo-template.html`.** Do not invent a new layout. Copy the template, replace every `{{TOKEN}}` with real client data, apply the client's brand colors from `brand.html`, and embed the correct JSON-LD schema blocks in the `<head>`.

**Token replacement rules:**
- `{{CLIENT_NAME}}` — business name exactly as it appears on the live site
- `{{CLIENT_SERVICE}}` — primary service category (e.g., "home inspection", "med spa")
- `{{CLIENT_CITY}}` — primary city served
- `{{LOGO_PATH}}` — relative path to the logo file (e.g., `img/logo.png`)
- `{{CLIENT_LOGO_URL}}` — absolute URL of the logo on the live site (for schema)
- `{{CLIENT_URL}}` — the client's live website URL (for schema)
- `{{CLIENT_PHONE}}`, `{{CLIENT_STREET}}`, `{{CLIENT_STATE}}`, `{{CLIENT_ZIP}}` — from live site / GBP
- `{{CLIENT_HOURS}}` — business hours in schema format (e.g., `Mo-Fr 08:00-17:00`)
- `{{CLIENT_SERVICE_AREA}}` — city and surrounding areas served
- `{{CLIENT_PRICE_RANGE}}` — e.g., `$$`, `$$$`, or a stated range
- `{{CLIENT_FOUNDED}}` — year founded if available; otherwise `"Established [decade]"`
- `{{CLIENT_CREDENTIALS}}` — licenses, certifications, or relevant credentials
- `{{BRAND_PRIMARY}}`, `{{BRAND_ACCENT}}`, `{{BRAND_DARK}}`, `{{BRAND_LIGHT}}`, `{{BRAND_TEXT}}` — from `brand.html`
- `{{REPORT_DATE}}` — current month and year
- `{{SNAPSHOT_DATE}}` — the date the AI ranking tests were actually run
- `{{AI_VISIBILITY_SCORE}}` — count of tests (out of 6) where the client was cited or ranked
- `{{AI_VISIBILITY_LABEL}}` — e.g., "Not Visible", "Partially Visible", "Visible"
- `{{AI_VISIBILITY_SUMMARY}}` — one sentence describing what the score means
- `{{AI_TEST_QUERY_1}}` — the exact service + city query used (e.g., "home inspector Denton TX")
- `{{AI_TEST_1_PILL}}` through `{{AI_TEST_6_PILL}}` — set to `cited`, `missing`, or `partial`
- `{{AI_TEST_1_RESULT}}` through `{{AI_TEST_6_RESULT}}` — short label (e.g., "Not cited", "Page 2")
- `{{FAQ_Q1}}` / `{{FAQ_A1}}` through `{{FAQ_Q12}}` / `{{FAQ_A12}}` — 8–12 real customer Q&A pairs
- `{{FAQ_COUNT}}` — total number of FAQ pairs included
- `{{SERVICE_1_NAME}}` / `{{SERVICE_1_DESCRIPTION}}` through N — one entry per core service
- `{{TRUST_YEARS}}`, `{{TRUST_CLIENTS}}`, `{{TRUST_CERT_COUNT}}`, `{{TRUST_REVIEWS}}` — real numbers
- `{{TRUST_CLIENTS_LABEL}}` — label for the clients stat (e.g., "Clients Served", "Inspections Completed")
- `{{TRUST_CERTS_LIST}}`, `{{TRUST_AWARDS}}`, `{{TRUST_PRESS}}` — plain text lists
- `{{SOCIAL_URLS_COMMA_SEPARATED}}` — JSON array of social profile URLs for schema `sameAs`
- `{{SOCIAL_URLS_DISPLAY}}` — human-readable version for the schema inspector section
- `{{ADDITIONAL_SCHEMA_SUMMARY}}` — comment block listing HowTo / Service / BreadcrumbList blocks included
- `{{SCHEMA_BLOCK_COUNT}}` — total number of schema blocks embedded
- `{{VALIDATED_TYPES_LIST}}` — comma-separated list of validated schema types
- `{{VALIDATION_DATE}}` — date validation was run (or "Pending — deploy to public URL first")
- `{{PRIMARY_CITATION_TOPIC}}` — the top keyword/topic this client should be cited for
- `{{AI_SNAPSHOT_KEY_FINDING}}` — 1–2 sentence summary of what the AI ranking test revealed
- `{{AI_SNAPSHOT_AEO_GOAL}}` — what the schema and Q&A work is designed to change

**Do not leave any `{{TOKEN}}` in the final delivered file.** Every placeholder must be replaced before delivery.

### What AEO Is and Why It Matters

Traditional SEO earns a blue-link ranking. AEO earns the **zero-click citation** — the sentence an AI answer engine quotes directly in its response, with the business name attached. As of 2026, Google AI Overviews appear on the majority of informational searches. ChatGPT and Perplexity are now primary research tools for millions of users. Sites that are not structured for answer engines are invisible to this growing traffic source.

AEO and SEO reinforce each other: the writing structure that makes a page easy for an AI to quote also makes it easy for a human to skim and for Google to understand. A correctly built `aeo.html` + JSON-LD schema set turns a single rebuild into a durable competitive advantage.

### Required Sections in Every `aeo.html`

| Section | Content |
|---|---|
| **Entity Overview** | Business name, category, address, phone, website, hours of operation, service area, founding year, credentials — every fact stated explicitly and unambiguously |
| **How We Answer Questions** | Plain-English explanation of what AEO is and how this site is structured to be cited by AI |
| **Q&A Bank** | 8–12 real questions a customer would ask, each followed by a direct, declarative 1–3 sentence answer. Written for extraction — not marketing copy |
| **Service Descriptions** | One-paragraph description of each core service — factual, specific, includes location if local |
| **Trust & Authority Signals** | Years in business, licenses, certifications, awards, memberships, number of clients served, press mentions |
| **Schema Inspector** | A visible, human-readable preview of the JSON-LD blocks embedded in the page — so the client can see what AI engines are reading |
| **Validation Status** | A callout confirming schema passed Google Rich Results Test with zero errors |
| **Footer** | Created by Mike Montes · Client name · Date |

### Required JSON-LD Schema Blocks

Every `aeo.html` must embed all applicable schema types as `<script type="application/ld+json">` blocks:

| Schema Type | When to Include | Key Fields |
|---|---|---|
| `Organization` | Always | `name`, `url`, `logo`, `contactPoint`, `sameAs` (social profiles) |
| `LocalBusiness` | Any business with a physical location or service area | `name`, `address`, `telephone`, `openingHours`, `geo`, `areaServed`, `priceRange` |
| `FAQPage` | Always — minimum 6 Q&A pairs | `mainEntity` array of `Question` + `acceptedAnswer` |
| `HowTo` | Any service with steps (e.g. "How does the process work?") | `name`, `step` array with `name` and `text` |
| `Service` | One block per major service offered | `name`, `description`, `provider`, `areaServed` |
| `BreadcrumbList` | All inner pages (About, Services, Contact) | `itemListElement` array |
| `WebSite` | Home page only | `name`, `url`, `potentialAction` (SearchAction if site has search) |

### AEO Writing Rules

- **Every answer must be a direct, declarative sentence.** Begin with the answer — do not bury it after context.
  - ✅ *"Smith Plumbing serves the Dallas-Fort Worth metro area, including Frisco, Allen, and McKinney."*
  - ❌ *"If you're wondering about our service area, we'd love to tell you more about where we operate across North Texas."*
- **State the business name in the first sentence of every major section.** AI engines use proximity to determine entity association.
- **Use exact match phrasing** for the questions customers type or speak into search: "How much does a home inspection cost in Denton TX?" not "Our pricing structure."
- **Include real numbers wherever possible**: years in business, number of clients, inspection scores, certifications held, square footage, price ranges.
- **Never use filler phrases** like "We are committed to excellence" or "We pride ourselves on quality." State the specific fact that proves the claim instead.

### AEO Ranking Test (required for every `aeo.html`)

> Before delivering the AEO report, run a live ranking test to document what the client's site currently ranks for — or doesn't — across AI answer engines. This test establishes the **before baseline** so the impact of the AEO work can be measured later.

**Run the following tests and document the results in a "Current AI Ranking Snapshot" section inside `aeo.html`:**

| Test | Query to Run | What to Record |
|---|---|---|
| **Google AI Overview** | `[primary service] [city]` (e.g., "home inspection Denton TX") | Is the client cited in the AI Overview? What site is cited instead? |
| **Google AI Overview — brand** | `[Business Name]` | Does Google's AI Overview surface the business? What does it say? |
| **ChatGPT** | "Who is the best [service] in [city]?" | Is the client mentioned? What competitors are named? |
| **Perplexity** | "Find a [service] near [city]" | Is the client cited? What sources does Perplexity pull from? |
| **Google Search — organic** | `[primary service] [city]` | What position does the client appear in the organic blue-link results? Page 1 / 2 / not found? |
| **Google Search — local pack** | Same query | Does the client appear in the Local 3-Pack? What position? |

**AEO Ranking Test Output Format (inside `aeo.html`):**

```
AI RANKING SNAPSHOT — [ClientName]
Test Date: [Date]

Google AI Overview ("[service] [city]"):
  Result: [Cited ✅ / Not cited ❌]
  What AI says: "[excerpt or 'not mentioned']"
  Who is cited instead: [competitor name or 'N/A']

Google AI Overview ("[Business Name]"):
  Result: [Cited ✅ / Not cited ❌]
  What AI says: "[excerpt or 'not mentioned']"

ChatGPT ("Who is the best [service] in [city]?"):
  Result: [Mentioned ✅ / Not mentioned ❌]
  Competitors named by ChatGPT: [list]

Perplexity ("Find a [service] near [city]"):
  Result: [Cited ✅ / Not cited ❌]
  Sources Perplexity used: [list]

Google Organic Rank: [Position / Page / Not found]
Google Local 3-Pack: [Position 1–3 / Not in pack]

Overall AI Visibility Score: [X/6 tests where client appeared]

Key Finding: [1–2 sentence summary — what this means for the client's current discoverability]
AEO Goal: [What the schema and Q&A work in this document is designed to change]
```

**Rules:**
- Run real searches — do not fabricate results.
- If a test cannot be run (e.g., no ChatGPT access), mark the row "Not tested — manual verification required."
- The AI Ranking Snapshot must appear near the top of `aeo.html` — before the Q&A bank — so it establishes the "why" for all the work that follows.

### AEO File Design Rules

1. The page must be a polished standalone HTML file matching the client's brand from `brand.html`.
2. JSON-LD blocks are embedded in the `<head>` — one `<script>` block per schema type.
3. A human-readable "Schema Preview" section displays the key facts from the schema in a formatted card — so the client understands what AI engines are reading.
4. The Q&A bank is rendered as a visible accordion or FAQ list on the page — not just hidden in schema.
5. File must validate with zero errors on [Google Rich Results Test](https://search.google.com/test/rich-results) before it is considered complete.
6. File name: `<AgencyName>/<ClientName>/aeo.html`

---

## Social Media Review Standard

> Every project must include a `<ClientName>-Social.html` file — a platform-by-platform review of the client's current social media presence. This is a **research-based audit**, not a content plan. It tells the client what the social media world currently sees when they look up the business, and identifies the gaps.

### How to Research

Before writing a single line, search for the client on every major platform. Check for handles, follower counts, recent post dates, engagement, and brand consistency. If a profile doesn't exist, that is data — mark it as a gap.

### Required Sections in `<ClientName>-Social.html`

| Section | Content |
|---|---|
| **Overall Social Presence Score** | A single X/100 score based on platform coverage, posting consistency, engagement, and brand alignment |
| **Platform Audit Table** | One row per platform checked (see format below) |
| **Brand Consistency Review** | Does the business use the same logo, handle, bio, and tone across all platforms? Note every inconsistency |
| **Content Pillar Analysis** | What 3–5 content themes does the client already post about? Are they aligned with what their audience wants? |
| **Engagement Snapshot** | Average likes/comments/shares on recent posts — identify which content type performs best |
| **Competitor Social Comparison** | Pick 2–3 competitors from the SEO audit and compare their social presence vs. the client |
| **Gap Summary** | Bulleted list of missing platforms, inactive accounts, unclaimed handles, and content gaps |
| **Footer** | Created by Mike Montes · [Client] · [Date] |

### Platform Audit Table Format

```
| Platform   | Handle       | Followers | Last Post    | Avg Engagement | Profile Complete? | Notes                        |
|------------|--------------|-----------|--------------|----------------|-------------------|------------------------------|
| Facebook   | @handle      | 1,240     | 3 days ago   | 12 likes/post  | ✅ Yes            | Cover photo outdated         |
| Instagram  | @handle      | 890       | 2 weeks ago  | 8 likes/post   | ⚠️ Partial        | No bio link, no highlights   |
| TikTok     | Not found    | —         | —            | —              | ❌ No profile     | Handle available — opportunity |
| LinkedIn   | [Company]    | 42        | 6 months ago | <5 interactions| ⚠️ Partial        | No banner image, sparse about |
| YouTube    | Not found    | —         | —            | —              | ❌ No channel     | Competitors active here      |
| X (Twitter)| @handle      | 310       | 8 months ago | <3 interactions| ⚠️ Stale          | Low value for this industry  |
| Google     | GBP Profile  | [reviews] | [last post]  | —              | See GBP section   | Cross-reference with SEO audit |
```

### Social Presence Scoring

| Category | Max Points | How to Score |
|---|---|---|
| Platform coverage (relevant platforms active) | 25 | 4+ relevant platforms active = 22–25 · 2–3 = 12–20 · 0–1 = 0–10 |
| Posting consistency | 25 | Posted in last 7 days on 2+ platforms = 22–25 · Last 30 days = 12–20 · Inactive = 0–10 |
| Brand alignment (logo, handle, bio consistent) | 25 | Fully consistent = 22–25 · Minor gaps = 12–20 · Inconsistent = 0–10 |
| Engagement quality | 25 | Above industry average = 22–25 · Average = 12–20 · Below / ghost account = 0–10 |

### Social Review Rules

- **Research every platform** — do not skip platforms you think are irrelevant. Note them and explain why they may or may not apply.
- **Never invent data.** If a platform has no profile, state "No profile found" — this is a finding, not a blank.
- **Identify the client's tone of voice** from their existing posts — is it professional, casual, promotional, educational? Flag when posts are off-brand.
- **Industry context matters** — a restaurant not on TikTok is a bigger gap than a B2B law firm not on TikTok. Calibrate findings to the client's industry.

---

## SEO Marketing Plan Standard

> Every project must include a `<ClientName>-SEOPlan.html` — a client-specific, actionable SEO marketing plan built directly from the findings in `seo.html`. This is **not a template**. Every section must reference the client's actual keywords, competitors, and gaps found during the audit. No generic advice.

### Required Sections in `<ClientName>-SEOPlan.html`

| Section | Content |
|---|---|
| **Executive Summary** | 3–4 sentences: where the client stands today, what the biggest opportunity is, and what the plan prioritizes |
| **Keyword Strategy** | Primary, secondary, and long-tail keywords — derived from the `seo.html` keyword table. Each keyword has: search intent label, monthly volume, current rank, and target rank |
| **On-Page SEO Checklist** | Page-by-page checklist of title tags, meta descriptions, H1s, image alt text, internal links, and schema needed for each prototype page |
| **Local SEO Actions** | GBP optimizations from the audit + local citation building targets (which directories to list on, in priority order) |
| **Content Gap Plan** | Pages or blog posts that should be created based on keyword gaps — each with a suggested title, target keyword, and content brief |
| **Backlink Opportunities** | 3–5 specific backlink opportunities identified for this client (local chamber, industry associations, press, partner sites) |
| **Review Generation Strategy** | Specific plan for increasing Google reviews — timing, ask method, response protocol |
| **Monthly Milestones** | A 3-month action timeline with specific deliverables per month, ordered by ROI |
| **KPIs to Track** | 4–6 measurable KPIs specific to this client: target rank position, review count goal, citation count, organic traffic benchmark |
| **Footer** | Created by Mike Montes · [Client] · [Date] |

### Keyword Strategy Format

```
PRIMARY KEYWORD: "[keyword]"
  Monthly searches: [volume]
  Current rank: [position or "Not ranking"]
  Target rank: [position]
  Search intent: [Informational / Navigational / Transactional / Local]
  Target page: [which prototype page this keyword should own]
  On-page action: [what needs to change on that page to rank]

SECONDARY KEYWORD: "[keyword]"
  [same format]

LONG-TAIL OPPORTUNITIES:
  "[keyword phrase]" — [volume] searches/mo — currently [rank/not ranking] — target page: [page]
  "[keyword phrase]" — [same]
```

### SEO Plan Rules

1. **Every recommendation must tie back to a specific finding** in `seo.html` — reference the section by name.
2. **The content gap plan must name specific page titles** — not "write a blog post" but "Write: '5 Things to Look for in a [City] Home Inspection' targeting '[keyword]'."
3. **Monthly milestones must be realistic** — Month 1 = quick wins (GBP, on-page basics); Month 2 = content + citations; Month 3 = backlinks + review push.
4. **KPIs must be measurable and time-bound** — "Reach position 5 for '[keyword]' by Month 3" not "improve rankings."
5. File uses client brand from `brand.html`. No generic stock advice.

---

## Digital Marketing Plan Standard

> Every project must include a `<ClientName>-Marketing.html` — a complete digital marketing plan that goes beyond SEO. It is built from the combined findings of `seo.html`, `<ClientName>-Social.html`, and the GBP audit. It is **100% client-specific** — different for every client based on what is missing, what is working, and what their industry demands.
>
> **When the client's goal is acquiring more customers**, the marketing plan must include a full Funnel System section built on the Value Ladder methodology. See [Funnel System Standard](#funnel-system-standard) below.

---

### How to Customize Per Client

Before writing the marketing plan, answer these questions from the research:

1. What channels are underperforming or missing entirely? (from Social Review)
2. What is the client's primary acquisition method today? (walk-in, referral, search, social, ads?)
3. Who is their ideal customer? (inferred from industry + live site copy)
4. What do their top competitors do well that this client doesn't? (from SEO competitor table)
5. What is the client's content style? (from Social Review — tone of voice)
6. **Is client acquisition a stated or implied goal?** If yes — add the Funnel System section.

The answers determine which sections get the most depth. A restaurant with zero TikTok but strong Instagram gets a different plan than a B2B contractor with a dead LinkedIn and no Google reviews.

---

### Required Sections in `<ClientName>-Marketing.html`

| Section | When to include | Content |
|---|---|---|
| **Marketing Snapshot** | Always | 3-sentence summary: what the research found, what the biggest opportunity is, and what this plan addresses |
| **Audience Profile** | Always | Inferred ideal customer: demographics, search behavior, social platform preference, purchase trigger |
| **Channel Priority Matrix** | Always | All digital channels ranked by ROI opportunity for this specific client |
| **Funnel System** | When client wants more customers | Full Value Ladder funnel mapped to this client's business — see Funnel System Standard |
| **Email Marketing** | If client has/needs a list | Recommended email sequence, frequency, SendGrid integration note |
| **Paid Ads Recommendation** | Always | Google Ads vs. Meta Ads vs. neither — specific recommendation with rationale |
| **Content Marketing** | Always | 3–5 specific content ideas tailored to the client's industry and audience |
| **Referral & Review Strategy** | Always | How to build word-of-mouth — specific to this client's customer journey |
| **90-Day Marketing Calendar** | Always | Week-by-week or month-by-month action plan — specific to this client |
| **Budget Guidance** | Always | Suggested monthly marketing spend ranges by channel |
| **Footer** | Always | Created by Mike Montes · [Client] · [Date] |

---

### Channel Priority Matrix Format

```
| Channel              | Current Status        | Opportunity Level | Recommended Action                  | Priority |
|----------------------|-----------------------|-------------------|--------------------------------------|----------|
| Google Search (SEO)  | Page 2, low reviews   | 🔴 High           | Execute SEO plan (see seo-plan.html) | 1        |
| Google Business      | Claimed, incomplete   | 🔴 High           | Complete profile, start posting      | 2        |
| Facebook             | Active, low reach     | 🟡 Medium         | Boost top posts, add CTA button      | 3        |
| Instagram            | Inactive              | 🟡 Medium         | Reactivate with weekly Reels         | 4        |
| Email                | No list               | 🟢 Low (now)      | Start list with lead magnet          | 5        |
| Google Ads           | Not running           | 🟡 Medium         | Test $300/mo campaign on top keyword | 6        |
| TikTok               | No account            | 🟢 Low            | Not recommended for this industry    | —        |
```

---

### Marketing Plan Rules

1. **No generic marketing advice.** Every section must reference the client's name, industry, city, or a specific finding from the audit.
2. **The 90-day calendar must be specific** — name the content pieces, post days, and actions. Not "post to social" but "Post before/after photo of [specific service] on Instagram, Tuesday 10am."
3. **Paid ads recommendation must include a specific keyword or audience** — not just "run Google Ads" but "Run Google Search Ads targeting '[keyword]' in [city], estimated CPC $[X], suggested budget $[Y]/mo."
4. **Email section is only included if the client has a form, booking system, or existing contact list** — do not recommend email marketing for a business with zero digital infrastructure.
5. **Channel Priority Matrix must match the Social Review findings** — if Instagram was marked inactive in `<ClientName>-Social.html`, it must appear in the matrix with that status.
6. **Funnel System section is mandatory when client acquisition is a goal** — if the client wants more customers, the funnel plan is not optional.

---

## Funnel System Standard

> When a client's goal includes acquiring more customers, the marketing plan must include a Funnel System section. The framework follows Russell Brunson's Value Ladder methodology — the strategy, not the ClickFunnels design aesthetic. Every funnel is built around this client's services, pricing, and customer journey. No generic funnels. No copy-paste offers.

---

### The Core Concept — Value Ladder

Every customer relationship moves through levels of value and trust. The mistake most local businesses make is trying to sell their biggest, most expensive service to a cold stranger. The funnel system fixes this by building a ladder of increasing value and investment — each step earns the right to offer the next.

```
COLD                                                              WARM
│                                                                    │
▼                                                                    ▼
[LEAD MAGNET] → [TRIPWIRE] → [CORE OFFER] → [UPSELL] → [HIGH-TICKET / CONTINUITY]
Free or $0      $7–$97        Main service    Add-on        Premium package / retainer
Gets the lead   First buyer   Core revenue    More value    Maximum relationship
```

A cold prospect never buys the premium package on first contact. The funnel earns trust at every rung before asking for the next level of commitment.

---

### The 5 Funnel Rungs — Applied to Local Business

#### Rung 1 — Lead Magnet (Free)

**Goal:** Get the name and email. Give genuine value with zero friction.

This is what most businesses skip. They wait for someone to be ready to buy. The lead magnet catches people who are interested but not ready — and keeps the business top of mind until they are.

**What it looks like for local businesses:**

| Industry | Lead Magnet Example |
|---|---|
| Home Inspection | "10 Things to Check Before Buying Any Home" (PDF download) |
| HVAC | "Free AC Tune-Up Checklist — Before Summer Hits" |
| Med Spa | "Your Skin Type Guide — Which Treatment Is Right for You" (quiz) |
| Law | "Free 15-Minute Legal Consultation — No Obligation" |
| Real Estate | "Neighborhood Price Report for [City] — Updated Monthly" |
| Roofing | "Free Storm Damage Inspection — Book Online in 60 Seconds" |
| Restaurant | "Loyalty Club — Get a Free Appetizer on Your Next Visit" |

**Rules:**
- Specific, useful, and immediately consumable — not a vague "newsletter signup"
- Delivered instantly (automated email or download link)
- Collects: first name + email at minimum. Phone optional but valuable.
- Headline must address a specific fear, question, or desire the ideal customer has right now

---

#### Rung 2 — Tripwire (First Paid Offer, Low Risk)

**Goal:** Turn a lead into a buyer. Even a $1 transaction changes the relationship permanently.

A buyer is worth 10x a non-buyer on the same list. The tripwire's job is not to make money — it is to create a customer. Price the tripwire so low that saying no feels unreasonable.

**What it looks like for local businesses:**

| Industry | Tripwire Example |
|---|---|
| Home Inspection | "$49 Pre-Listing Walkthrough" (normally $150) |
| HVAC | "$29 System Health Check" |
| Med Spa | "$49 Introductory Facial or Consultation" |
| Law | "$97 1-Hour Strategy Session" |
| Real Estate | "$97 Home Valuation Report with Comp Analysis" |
| Roofing | "$49 Full Roof Inspection + Written Report" |
| Restaurant | "$19 Date Night Tasting Plate for 2" |

**Rules:**
- Must have real, standalone value — not a watered-down version of the core service
- Price must create urgency or feel like an obvious deal
- Often paired with an **Order Bump** on the checkout page — a small, related add-on offered as a checkbox before payment (e.g., "Add a digital copy of your report — $9")
- Tripwire buyers are shown the Core Offer immediately after purchase (see Rung 3)

---

#### Rung 3 — Core Offer (Main Service)

**Goal:** Deliver the primary service. This is the center of the business.

The core offer is not the cheapest thing and not the most expensive. It is the thing the business is known for — the service that solves the customer's main problem completely.

**What it looks like:**

| Industry | Core Offer |
|---|---|
| Home Inspection | Standard home inspection ($350–$500) |
| HVAC | Full system tune-up or installation |
| Med Spa | Botox, filler, or signature treatment package |
| Law | Retainer or case representation |
| Real Estate | Full buyer or seller representation |
| Roofing | Full roof replacement or repair |
| Restaurant | Regular dining experience |

**Rules:**
- This is what all the earlier rungs are leading to
- The customer who entered at Rung 1 or 2 already trusts the business — the conversion rate here is significantly higher than cold traffic
- Core offer must be presented with a clear outcome statement: "What your life looks like after this service is complete"

---

#### Rung 4 — Upsell / Order Bump (More Value, Same Customer)

**Goal:** Increase the value of the existing transaction. The customer already said yes — offer them more.

The best time to sell to someone is right after they have already bought. Their wallet is out. Their trust is established. An upsell shown immediately after the core offer purchase converts at 20–30% with zero new ad spend.

**What it looks like:**

| Industry | Upsell / Order Bump |
|---|---|
| Home Inspection | "Add Sewer Scope + Radon Test — $75 more" |
| HVAC | "Add a UV Air Purifier Install — $199" |
| Med Spa | "Add a follow-up touch-up session — $99" |
| Law | "Add document drafting to your consultation — $150" |
| Real Estate | "Add a home staging consultation — $200" |
| Roofing | "Add gutter cleaning and inspection — $89" |
| Restaurant | "Add a dessert platter and bottle of wine — $39" |

**Rules:**
- Must be related to and enhance the core purchase — not a random upsell
- Present as a natural next step, not a separate sales pitch: "Most clients who get X also add Y because..."
- A **downsell** is offered if the upsell is declined — a smaller version or payment plan: "Or try just the [component] for $X"
- Never offer more than 2 upsells in sequence — more than that creates fatigue and kills trust

---

#### Rung 5 — High-Ticket / Continuity (Maximum Relationship)

**Goal:** Serve the client's biggest need, or retain them indefinitely.

This is the top of the ladder. Only a fraction of customers reach here, but they generate disproportionate revenue. For most local businesses, this is either a premium package or a recurring membership/retainer.

**What it looks like:**

| Industry | High-Ticket / Continuity |
|---|---|
| Home Inspection | Annual maintenance inspection plan ($199/yr subscription) |
| HVAC | Seasonal maintenance plan — 2 visits/yr ($299/yr) |
| Med Spa | Monthly membership — 1 treatment/month + priority booking |
| Law | Monthly retainer for ongoing legal counsel |
| Real Estate | Investor services — ongoing acquisition support (retainer) |
| Roofing | Roof maintenance plan — annual inspection + priority storm response |
| Restaurant | VIP membership — priority reservations + exclusive events |

**Rules:**
- Recurring revenue is always the goal at this rung — monthly or annual beats one-time
- High-ticket must include a clear premium experience, not just "more of the same"
- Continuity offers reduce the cost of acquisition over time — one customer pays indefinitely

---

### Funnel Types — Which to Build for Each Client

Not every client needs every type of funnel. Choose based on their business model and primary goal.

| Funnel Type | Best For | Structure |
|---|---|---|
| **Lead Generation Funnel** | Service businesses, B2B, contractors | Lead Magnet → Thank You Page → Core Offer sequence via email |
| **Appointment Funnel** | Any business that books consultations | Lead Magnet → Book a Call page → Confirmation → Reminder sequence |
| **Tripwire Funnel** | Businesses with a natural low-cost entry point | Tripwire offer → Order Bump → Core Offer upsell → Thank You |
| **Webinar / Workshop Funnel** | Coaches, consultants, premium services | Free webinar registration → Live/Recorded value delivery → Offer at the end |
| **Survey / Quiz Funnel** | Med spa, skincare, fitness, nutrition | Quiz ("What's your skin type?") → Results page → Personalized offer |
| **Referral Funnel** | High-trust local services (law, finance, medical) | Referral program page → Incentive offer → Tracking link per referrer |

---

### How to Write the Funnel Section in the Marketing Plan

When adding the Funnel System to `<ClientName>-Marketing.html`, include all of the following — fully populated with the client's actual services and pricing:

**1. Their Current Funnel (Before)**
Describe honestly where the client's funnel breaks down today. Most local businesses have:
- No lead magnet — cold traffic hits the homepage and bounces
- No follow-up — leads who don't call back are lost forever
- No ascension — existing customers are never offered the next thing

**2. The Recommended Value Ladder**
Map all 5 rungs to this client's actual services. Use the format:

```
Rung 1 — Lead Magnet: [specific offer + delivery method]
Rung 2 — Tripwire:    [specific offer + price + order bump]
Rung 3 — Core Offer:  [primary service + outcome statement]
Rung 4 — Upsell:      [add-on + price + downsell fallback]
Rung 5 — Continuity:  [membership / retainer name + price + renewal]
```

**3. The Recommended Funnel Type**
State which funnel type fits best (from the table above) and why.

**4. Traffic Source**
Where does the cold traffic come from? The funnel is useless without traffic. Tie this directly to the Channel Priority Matrix — which channel drives cold traffic into Rung 1.

**5. Email Follow-Up Sequence**
Every lead captured at Rung 1 enters an automated email sequence. Minimum 5 emails:

| Email | Timing | Purpose |
|---|---|---|
| Email 1 | Immediately | Deliver the lead magnet. No pitch. Pure value. |
| Email 2 | Day 2 | Share a relevant story or result. Build trust. |
| Email 3 | Day 4 | Address the #1 objection your ideal customer has. |
| Email 4 | Day 6 | Introduce the Tripwire offer with urgency. |
| Email 5 | Day 8 | Final reminder — "I don't want you to miss this." |

**6. Funnel Metrics to Track**
Every funnel is measured. Include these benchmarks in the plan:

| Metric | What it means | Benchmark to aim for |
|---|---|---|
| Opt-in rate | % of visitors who take the Lead Magnet | 25–50% (depends on traffic quality) |
| Tripwire conversion | % of leads who buy the Tripwire | 5–15% |
| Core Offer conversion | % of Tripwire buyers who buy Core | 20–40% |
| Upsell take rate | % of Core buyers who take the Upsell | 15–30% |
| Email open rate | % of list who open each email | 25–45% for warm local list |

---

### Funnel Rules

1. **Map to real services and real prices** — never use placeholder numbers. Research the client's actual pricing from the live site or make a reasonable inference based on industry.
2. **The Lead Magnet must be specific** — "Free Guide" is not a lead magnet. "The [City] Homeowner's Pre-Sale Inspection Checklist" is.
3. **The Tripwire must have standalone value** — it cannot feel like a stripped-down version of something better. It must be genuinely useful on its own.
4. **Never skip from Lead Magnet straight to High-Ticket** — this is the most common funnel mistake. Earn trust at every rung before climbing.
5. **Every rung must have a clear next step** — the customer must always know what happens after they say yes.
6. **The email sequence is not optional** — a funnel without follow-up email is a leaky bucket. If no email infrastructure exists, recommend SendGrid setup as the first technical action.
7. **Design is not ClickFunnels** — do not use white sales pages with yellow headlines, red countdown timers, or long-form scroll pages. The funnel strategy is Brunson. The design is always on-brand for this client: their colors, their fonts, their photography, their tone of voice.

---

## Digital Presence Report Standard

> Every project must include a `<ClientName>-Presence.html` — a client-facing, sales-conversation report on the client's current digital footprint. It covers every channel across a single, consistent green/yellow/red framework. This is the **first document shown during the sales meeting**, before the SEO report, AEO report, or any other deliverable.

### Purpose

This report does one thing: it shows the client, in plain language, where they stand right now — what's working, what's idle, and what's actively costing them customers. It is written for a business owner who is not technical. Every section has a built-in sales talking point so the sales rep knows exactly what to say.

### ⚠ Mandatory Template

**Every `<ClientName>-Presence.html` must be built from `_templates/presence-report-template.html`.** Copy the template, replace every `{{TOKEN}}`, apply the client's brand colors from `brand.html`, and populate every channel row from live research. Do not leave any `{{TOKEN}}` in the delivered file.

### Channels to Evaluate (always cover all of these)

| Channel | Icon | What to assess |
|---|---|---|
| Website / UX | 🌐 | Mobile-friendly? Fast? Clear CTAs? Modern design? Easy to navigate? |
| Google Search Ranking | 🔍 | What page do they appear on for their primary keyword + city? |
| Google Business Profile | 📍 | Claimed? Complete? Photos? Posts? Reviews responded to? |
| Google Reviews | ⭐ | Count, average rating, recency, owner responses |
| AI Visibility (AEO) | 🤖 | Do they appear in Google AI Overview, ChatGPT, or Perplexity results? |
| Facebook | 📘 | Active? Complete profile? Engagement? Recent posts? |
| Instagram | 📸 | Active? Bio link? Highlights? Engagement per post? |
| Other Social (TikTok / LinkedIn / YouTube / X) | 📱 | Presence or absence — note which apply to the industry |
| Local Citations / NAP Consistency | 🗺️ | Listed on Yelp, Angi, BBB, industry directories? NAP match across all? |
| Content / Blog | ✍️ | Any blog or content presence? Indexed pages? Topical authority signals? |

### Status Definitions

| Status | Color | Meaning |
|---|---|---|
| **Going Well** | 🟢 Green | Actively working in the client's favor — a real strength to preserve and amplify |
| **Flat** | 🟡 Yellow | Exists but isn't generating results — untapped potential with low lift to improve |
| **Needs Improvement** | 🔴 Red | Broken, missing, or actively hurting the business — costs customers every day |

### Channel Row Content Rules

**Going Well rows must include:**
- What we found (the specific positive data point)
- Why it matters (what this does for the business)

**Flat rows must include:**
- What we found (what exists)
- What's missing (the specific gap)
- Opportunity (what a small improvement would unlock)

**Needs Improvement rows must include:**
- What we found (the specific problem)
- The problem (why this is hurting them)
- Cost of inaction (what keeps happening every day this stays broken)

### Scorecard Counts

After assigning every channel a status, count them:
- `{{COUNT_GOING_WELL}}` — number of green channels
- `{{COUNT_FLAT}}` — number of yellow channels
- `{{COUNT_NEEDS_IMPROVEMENT}}` — number of red channels
- `{{CHANNELS_REVIEWED}}` — total channels evaluated (sum of all three)

### Priority Action List Rules

The bottom section lists 5 priorities ordered by impact — not effort. These are the highest-ROI moves available to this client right now:
- Priority 1 is always the single highest-impact action regardless of difficulty
- Effort tags: `quick` (days), `medium` (weeks), `project` (months)
- Each priority must be specific — not "improve your website" but "Complete your Google Business Profile — add 10 photos, respond to all reviews, and post weekly"

### Token Reference

| Token | Replace with |
|---|---|
| `{{CLIENT_NAME}}` | Business name |
| `{{CLIENT_SERVICE}}` | Primary service (e.g., "home inspection") |
| `{{CLIENT_CITY}}` | Primary city served |
| `{{LOGO_PATH}}` | Relative path to logo (e.g., `img/logo.png`) |
| `{{BRAND_PRIMARY/ACCENT/DARK/LIGHT/TEXT}}` | From `brand.html` |
| `{{REPORT_DATE}}` | Month and year report was prepared |
| `{{CHANNELS_REVIEWED}}` | Total number of channels evaluated |
| `{{COUNT_GOING_WELL/FLAT/NEEDS_IMPROVEMENT}}` | Counts per status |
| `{{GW_N_ICON}}` | Emoji icon for the channel |
| `{{GW_N_CHANNEL}}` | Channel name |
| `{{GW_N_FINDING}}` | Specific positive finding |
| `{{GW_N_WHY}}` | Why it matters to the business |
| `{{FL_N_ICON/CHANNEL/FINDING/GAP/OPPORTUNITY}}` | Flat channel fields |
| `{{NI_N_ICON/CHANNEL/FINDING/PROBLEM/COST}}` | Needs Improvement channel fields |
| `{{PRIORITY_N_TITLE/DESCRIPTION/EFFORT_CLASS/EFFORT_LABEL}}` | Priority action items (effort class: `quick`, `medium`, or `project`) |
| `{{CLOSING_SUMMARY}}` | 2–3 sentence plain-English summary of the overall picture |

### Workflow Position

This report is built **after** the SEO audit, GBP audit, AEO ranking test, and Social Review research is complete — because it draws from all of those. It is delivered **first** in the sales conversation. The SEO report, AEO report, and other detailed documents are shown as supporting evidence if the client wants to go deeper.

---

## Completed Projects

| Client | Folder | Prototype | Brand | Presence | SEO | AEO | Social | SEO Plan | Marketing | Functionality | Auth | Admin | Presentation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fire Plus Industries | `FirePlus/` | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| STARpay Solutions | `STARpay/` | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Argyle Med Spa | `ArgyleMedSpa/` | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Brownie's Home Inspections | `BrownieInspects/` | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| IGY6 Armory | `IGY6Armory/` | 🔄 In Progress | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |

*Add a row here each time a new project is created. Update checkmarks as deliverables are completed.*


---

## Login & Auth Structure Standard

> Every project must include a complete set of authentication views — `login.html`, `forgot-password.html`, and `reset-password.html`. These are prototype HTML files, not live auth systems. All form submissions use `showPrototypeModal()`. There must be no dead ends in any auth flow.

### Required Auth Files

| File | Purpose |
|---|---|
| `login.html` | Primary sign-in screen |
| `forgot-password.html` | User enters email to request a reset link |
| `reset-password.html` | User sets a new password (token-based flow, simulated) |

### `login.html` — Required Elements

| Element | Notes |
|---|---|
| Client logo | Centered at top, min 160px wide, on a contrasting background |
| Email input | Label "Email Address", type="email", required |
| Password input | Label "Password", type="password", show/hide toggle button, required |
| "Forgot password?" link | Links to `forgot-password.html` |
| Submit button | "Sign In" — uses `showPrototypeModal()` on success |
| "Create account" link | If registration is in scope, link to a register view or show prototype modal |
| Error state | Visible inline error for incorrect credentials (prototype: toggle a `.error` class) |
| Loading state | Button text changes to "Signing in..." while simulated request is in progress |

### `forgot-password.html` — Required Elements

| Element | Notes |
|---|---|
| Client logo | Same as login |
| Email input | Label "Email Address", type="email", required |
| Submit button | "Send Reset Link" — on submit, hide the form and show a success confirmation message |
| Success state | "Check your email — a reset link has been sent to [email]." No redirect; keep user on page. |
| Back link | "Back to Sign In" → `login.html` |

### `reset-password.html` — Required Elements

| Element | Notes |
|---|---|
| Client logo | Same as login |
| New password input | Label "New Password", type="password", show/hide toggle, required |
| Confirm password input | Label "Confirm Password", type="password", required |
| Client-side validation | Passwords must match before submit button activates |
| Submit button | "Set New Password" — on success, show confirmation message + link back to `login.html` |
| Success state | "Your password has been updated. Sign in to continue." + link to `login.html` |

### Auth Design Rules

1. All three views must use the client's brand colors and logo from `brand.html`.
2. All auth views must be **centered card layout** — white card on a light or brand-colored background, max-width 420px.
3. All form inputs follow the Input Field Standards (min-height 52px, 20px left padding, border-radius 8px).
4. All views are fully responsive — usable on a 375px phone without horizontal scroll.
5. Never link auth views to a real backend in the prototype — always simulate with `showPrototypeModal()` or an inline state change.
6. Include visible focus states on all interactive elements for accessibility.

---

## Admin Panel Standard

> Every project must include an `admin.html` page — a simple configuration panel where the site owner can add their Google Analytics, Google Search Console, Google Tag Manager, and SendGrid credentials. This is a prototype admin interface; actual integration happens in the production build.

### Required Configuration Sections in `admin.html`

| Section | Fields | Notes |
|---|---|---|
| **Google Analytics** | Measurement ID (`G-XXXXXXXXXX`) | Paste-in field, save button, confirmation state |
| **Google Search Console** | HTML meta verification tag | Textarea for the full `<meta>` tag, save button |
| **Google Tag Manager** | Container ID (`GTM-XXXXXXX`) | Paste-in field, save button, confirmation state |
| **SendGrid** | API Key (`SG.XXXXXXXXXX`) | Password-type field (masked), save button, test connection button |

### Admin Panel Design Rules

1. **Access protection:** Include a simple PIN or password prompt before the admin panel is shown. Even a hardcoded PIN (`1234`) is acceptable for the prototype — label it clearly as "prototype PIN."
2. **Layout:** Each integration is a separate card or section with a header icon, field(s), and a save button.
3. **Save confirmation:** After clicking Save, the button state changes to "Saved" with a green checkmark for 2 seconds, then returns to normal.
4. **Field masking:** API key fields (SendGrid) must be `type="password"` by default with a show/hide toggle.
5. **Copy instructions:** Below each field, include a brief plain-English instruction on where to find the value:
   - GA: *"Find this in Google Analytics → Admin → Property → Measurement ID"*
   - GSC: *"Copy the HTML tag from Google Search Console → Settings → Ownership verification"*
   - GTM: *"Find this in Google Tag Manager → Admin → Your container ID"*
   - SendGrid: *"Create an API key at sendgrid.com → Settings → API Keys → Create API Key"*
6. **SendGrid — Test Connection button:** Clicking it shows a prototype modal confirming the key format is valid (no real API call in prototype).
7. Must use the client's brand colors from `brand.html`.
8. Must be fully responsive.

### Admin Nav Link

Add a discreet "Admin" link in the footer of every prototype page (small font, muted color). This link goes to `admin.html`. Label it plainly — no jargon.

---

## React Functionality Specification Standard

> Every project must include `<ClientName>-Functionality.html`. This file explains how the prototype translates into a production React application. React is the default for all projects unless the user explicitly says otherwise.

### Purpose

This document bridges the gap between the HTML prototype and a real React build. It is written for a developer who will build the production site — not for the client. It must be specific enough that the developer can start building without asking questions.

### Required Sections

| Section | Content |
|---|---|
| **1. Project Overview** | Client name, industry, prototype URL, and a 2–3 sentence summary of the site's purpose |
| **2. Tech Stack** | Recommended stack: React (Vite), React Router, Tailwind CSS, and any third-party libraries needed (e.g., react-hook-form, framer-motion, react-query) |
| **3. Page Map** | Table of every prototype page → its React route → component file path |
| **4. Component Inventory** | List of all shared components (Navbar, Footer, HeroSection, CTAButton, etc.) with a brief description of each |
| **5. Interactive Features** | For every `showPrototypeModal()` or simulated interaction in the prototype, describe the real React implementation: state, props, API calls, and expected behavior |
| **6. Forms & Validation** | Every form in the prototype mapped to: field names, validation rules, submit handler, success/error states, and the API endpoint or service (e.g., SendGrid) it connects to |
| **7. Auth Flow** | Describes the real implementation for `login.html`, `forgot-password.html`, and `reset-password.html` — JWT or session-based, auth context/provider, protected route wrapper |
| **8. Admin Panel** | Describes how `admin.html` connects to a backend config store — which env vars map to which admin fields, how saves are persisted |
| **9. SEO & AEO Integration** | How schema markup from `aeo.html` is added to React pages (react-helmet-async or Next.js head), and how GA/GTM/GSC are integrated (react-ga4, GTM script in index.html) |
| **10. Responsive Breakpoints** | Documents the breakpoint system used in the prototype and confirms it maps to Tailwind's default breakpoints (or lists custom ones) |
| **11. Deployment Notes** | Recommended hosting (Vercel, Netlify, or custom VPS), environment variable list, and build command |

### Page Map Format

```
| Prototype File       | React Route        | Component File                  |
|----------------------|--------------------|----------------------------------|
| index.html           | /                  | src/pages/Home.jsx              |
| about.html           | /about             | src/pages/About.jsx             |
| services.html        | /services          | src/pages/Services.jsx          |
| contact.html         | /contact           | src/pages/Contact.jsx           |
| login.html           | /login             | src/pages/auth/Login.jsx        |
| forgot-password.html | /forgot-password   | src/pages/auth/ForgotPassword.jsx |
| reset-password.html  | /reset-password    | src/pages/auth/ResetPassword.jsx |
| admin.html           | /admin             | src/pages/admin/Dashboard.jsx   |
```

### Interactive Feature Format

For each simulated interaction, document it as:

```
Feature: Contact Form Submission
Prototype behavior: showPrototypeModal("Thanks! We'll be in touch shortly.")
React implementation:
  - Component: src/components/ContactForm.jsx
  - Library: react-hook-form
  - On submit: POST to /api/contact (SendGrid via backend API route)
  - Success state: replace form with <SuccessMessage /> component
  - Error state: show inline error banner, keep form fields populated
  - Required fields: name (string), email (email), phone (tel, optional), message (string, min 20 chars)
```

### Build Rules

1. Single self-contained HTML file — styled consistently with other deliverables.
2. Uses the client's brand colors from `brand.html` for headers and accents.
3. All code snippets are in `<pre><code>` blocks — syntax-highlighted with a CDN highlight.js if desired.
4. No placeholder content — every section is populated based on the actual prototype.
5. Footer: *"Created by Mike Montes"*

---

## Gap Analysis Standard

> After the prototype is fully built, run a gap analysis. This is not a document — it is a structured report delivered directly to the user as a message (or included as a collapsible section at the bottom of `admin.html`). It identifies pages, flows, or features that are missing or underdeveloped compared to industry standards for the client's type of business.

### Gap Analysis Process

1. **Compare the prototype page list against the client's industry standard** — what pages do competitors and industry leaders have that this prototype is missing?
2. **Review every CTA flow end-to-end** — are there forms that lead nowhere? CTAs that use `showPrototypeModal()` but were not fully described in the modal? Multi-step flows that skip steps?
3. **Check for industry-specific pages** — examples by industry:
   - Service businesses: Testimonials/Reviews page, Before & After gallery, Service area map, FAQ page
   - E-commerce: Cart, Checkout, Order confirmation, Account/order history
   - Professional services: Case studies, Team bios, Awards/certifications
   - Healthcare/legal: Disclaimer pages, HIPAA/privacy notices, Patient/client portal link
   - Restaurants: Menu page, Reservations, Online ordering integration
4. **Check for missing auth coverage** — are there pages in the prototype that reference a user account but don't link to `login.html` or `forgot-password.html`?
5. **Check the admin panel** — are there integrations mentioned in the prototype (contact forms, booking, etc.) that require a SendGrid API key or analytics that are not covered by the admin panel fields?

### Gap Analysis Output Format

Present findings as a numbered list grouped by priority:

```
GAP ANALYSIS — [ClientName]

HIGH PRIORITY (conversion impact):
1. Missing: Testimonials/Reviews page — competitors have 50+ visible reviews; this prototype has none.
2. Incomplete: Contact form on contact.html has no success state — users don't know it submitted.

MEDIUM PRIORITY (UX improvement):
3. Missing: FAQ page — client's industry commonly uses this to reduce pre-sale calls.
4. Missing: Service area map — 3 top competitors display this prominently.

LOW PRIORITY (nice to have):
5. Suggestion: Add a "Why Us" or "Process" page to differentiate from generic competitors.
6. Suggestion: The admin panel does not have a field for a Calendly or booking embed URL — consider adding one.

NEXT STEPS:
Present this list to the user and ask which items they want added to the current prototype build.
```

---

## Presentation Standard

> Every project must include `<ClientName>-Presentation.html` — an HTML deck that **behaves like PowerPoint**: one full-viewport slide at a time (no long-scroll as primary UX), keyboard/click/swipe navigation, slide counter/dots, and fullscreen. Used to walk the client through the new prototype side-by-side with their current site. Design is intentionally minimal so the content is the focus.

### Design Principles

- **Simple and clean** — white or very light background, generous whitespace, the client's brand accent as the only color.
- **No animations** — static layout, printable.
- **No heavy frameworks** — Tailwind CDN is acceptable; keep it fast and lightweight.
- **Image placeholders only** — every screenshot slot uses a labeled placeholder `<div>` (not a real screenshot). The placeholder shows: the image label, the source URL to screenshot, and the recommended dimensions.

### Required Slides (in this order)

| Slide | Content |
|---|---|
| **1. Cover** | Client logo (from `img/`) · Project title: "[ClientName] — Website Redesign Preview" · Created by Mike Montes · Date |
| **2. The Challenge** | 2–3 bullet points describing what the current site lacks (pulled from the UX improvement comments in the prototype HTML files) |
| **3. Current Site — Before** | One large image placeholder per key page (Home, About, Services, Contact). Label each: "SCREENSHOT PLACEHOLDER — [PageName] · Source: [live URL]" |
| **4. New Prototype — After** | One large image placeholder per corresponding prototype page. Label each: "SCREENSHOT PLACEHOLDER — [PageName] · Source: [filename].html" |
| **5. Brand** | Brief brand summary: logo (live), primary color swatch, heading font, body font, 3 tone-of-voice keywords — all pulled from `brand.html` |
| **6. SEO Snapshot** | 3 key findings from `seo.html` — overall score, top keyword opportunity, and biggest competitor gap |
| **7. AEO Snapshot** | 2–3 key facts from `aeo.html` — schema types added, FAQ count, one example Q&A pair |
| **8. What's Included** | Bulleted list of all prototype pages + auth views + admin panel + SEO + AEO deliverables |
| **9. Next Steps** | Clear call to action: next steps for the client to move forward |

### Image Placeholder Pattern

```html
<!-- Use this pattern for every before/after screenshot slot -->
<div class="screenshot-placeholder">
  <span class="label">SCREENSHOT PLACEHOLDER</span>
  <span class="page">Home Page — Current Site</span>
  <span class="source">Source: https://www.clientsite.com/</span>
  <span class="dims">Recommended: 1280 × 800 px</span>
</div>
```

```css
.screenshot-placeholder {
  width: 100%;
  aspect-ratio: 16/10;
  background: #f0f2f5;
  border: 2px dashed #c0c7d0;
  border-radius: 8px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 24px;
  text-align: center;
}
.screenshot-placeholder .label {
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: #94a3b8;
}
.screenshot-placeholder .page {
  font-size: 16px;
  font-weight: 600;
  color: #334155;
}
.screenshot-placeholder .source,
.screenshot-placeholder .dims {
  font-size: 12px;
  color: #64748b;
}
```

### Presentation Build Rules

1. File is a **single self-contained HTML file** — no external JS dependencies (inline CSS/JS OK).
2. Client logo appears on the cover and in the footer of every slide.
3. Each slide is a distinct `<section>` element; **primary UX is one slide filling the viewport** (100vh / 100dvh) with Prev/Next — not continuous scroll between slides.
4. Navigation: Arrow Left/Right, PageUp/PageDown, Space/Enter, optional Home/End and number keys; Prev/Next buttons + slide counter or dots; click right half optional; mobile swipe when easy; **F** or a button for `requestFullscreen` on the deck.
5. Hide browser scrollbar for the deck; prevent body scroll while presenting; subtle fade/slide transition.
6. Must be **printable to PDF** — use `@media print` with page-breaks; hide deck chrome.
7. No placeholder text — every text field is populated with real client-specific content.
8. Footer on every slide: *"Created by Mike Montes"*
9. A `.pptx` is **not** required; HTML PowerPoint-style behavior is the deliverable.

---

## Chat Log Standard

> `references/chat.md` is created at the start of every new chat for a project and updated throughout. It is the living record of what was built, what changed, and what the developer needs to build.

---

### Why This File Exists

This file serves two audiences simultaneously:

| Audience | What they use it for |
|---|---|
| **Mike (you)** | Know exactly what changed, when, and why — across multiple sessions |
| **Developer** | Understand the full site architecture before writing a single line of code |

Every decision made in the chat — page added, section changed, component invented — is logged here the moment it happens. The developer reads this file before touching anything else.

---

### When to Create It

**Immediately** — the moment a new chat begins for a project. Before pulling assets, before building any HTML, before asking any questions. The file must exist from the first action.

If a `chat.md` already exists for the project (from a prior session), **do not recreate it** — open it, add a new `## Session` entry at the bottom, and continue appending.

---

### File Location

```
My Projects/<Agency>/<ClientName>/references/chat.md
```

---

### Template — Copy Exactly on Creation

```markdown
# <ClientName> — Project Chat Log

> Single source of truth for all project changes and the developer handoff architecture.
> Updated throughout every chat session. Never deleted. Never overwritten.

---

## Project Info

| Field | Value |
|---|---|
| Client | <ClientName> |
| Industry | <e.g. Home Inspection / Med Spa / HVAC> |
| Live Site URL | <URL> |
| Prototype Started | <YYYY-MM-DD> |
| Primary Contact | <name if known> |

---

## Site Architecture

> This section is the developer's map. Every page, its purpose, its URL slug, and its key sections. Update this table any time a page is added, renamed, or removed.

| Page | File | Route (React) | Purpose | Key Sections |
|---|---|---|---|---|
| Home | index.html | / | Primary landing — hero, services overview, social proof, CTA | Hero, Services Grid, Why Us, Reviews, CTA Banner |
| About | about.html | /about | Brand story, team, values | Story, Team, Values, CTA |
| Services | services.html | /services | Full service list with descriptions | Service Cards, Process, FAQ, CTA |
| Contact | contact.html | /contact | Quote request / consultation booking | Contact Form, Map, Phone/Email |
| Login | login.html | /login | Auth — user login | Email + Password, Forgot Link, Error State |
| Forgot Password | forgot-password.html | /forgot-password | Auth — trigger reset email | Email Field, Confirmation State |
| Reset Password | reset-password.html | /reset-password | Auth — set new password via token | New Password, Confirm, Success State |
| Admin | admin.html | /admin | Internal config panel | GA ID, GSC, GTM, SendGrid Key |
| Brand Guide | brand.html | /brand | Internal — logo, colors, fonts, tone | Logo, Swatches, Type Specimens, Button Demos |
| Presence Report | <ClientName>-Presence.html | /presence | Sales meeting opener — all channels green/yellow/red | Scorecard, Channel Rows, Priority Actions |
| SEO Report | seo.html | /seo | SEO audit and action plan | Score Card, Keywords, Competitors, Action Plan |
| AEO Report | aeo.html | /aeo | AI visibility audit and schema | AI Snapshot, Entity Data, Q&A Bank, Schema |
| Social Review | <ClientName>-Social.html | /social | Social platform audit | Platform Table, Engagement, Brand Consistency, Gaps |
| SEO Plan | <ClientName>-SEOPlan.html | /seo-plan | Actionable SEO roadmap from audit findings | Keyword Strategy, On-Page Checklist, 3-Month Timeline |
| Marketing Plan | <ClientName>-Marketing.html | /marketing | Full digital marketing plan + Funnel System | Channel Priority, Funnel / Value Ladder, Email Sequence |
| Functionality Spec | <ClientName>-Functionality.html | /functionality | React handoff doc for the developer | Page Map, Components, Auth Flow, API Integrations |
| Presentation | <ClientName>-Presentation.html | /presentation | Before/after slide deck for client meeting | Cover, Challenge, Before, After, Brand, SEO/AEO, Next Steps |
| 404 | 404.html | * | Error page | Clever copy, quick links |

> Add rows for any additional pages discovered during the site crawl or added during the project.

---

## Component Inventory

> All shared UI components used across the prototype. The developer builds these as React components.

| Component | Used On | Description |
|---|---|---|
| `<Navbar>` | All pages | Logo + nav links + hamburger on mobile |
| `<Footer>` | All pages | Links, contact info, social icons, legal |
| `<HeroSection>` | Home, Services, Contact | 60vh min, brand background, headline + subhead + CTA |
| `<CTABanner>` | Home, About, Services | Dark brand-color strip with headline and primary button |
| `<ServiceCard>` | Services, Home | Icon + title + description card in a responsive grid |
| `<ReviewCard>` | Home | Star rating + quote + reviewer name |
| `<ContactForm>` | Contact | Name, email, phone, message, submit — validated |
| `<PrototypeModal>` | Any simulated action | Overlay modal confirming the action was received |

> Add rows for any additional components invented during the build.

---

## Session Log

> One entry per chat session. Append — never overwrite.

---

### Session 1 — <YYYY-MM-DD>

**What was done:**
- Created project folder and all subfolders
- Pulled logo, colors, and images from live site
- Built brand.html

**Decisions made:**
- Brand primary: `#______` — pulled from live site nav background
- Brand accent: `#______` — pulled from CTA buttons on live site
- Font: _______ — matched from Google Fonts embed on live site

**Pages created this session:**
- [ ] index.html
- [ ] about.html
- [ ] contact.html

**Changes from the original scope:**
- _(none yet)_

**Open items / next session:**
- Build services.html
- Pull remaining service page images
```

---

### Logging Rules

These rules apply every time `chat.md` is updated:

1. **Log every page addition** — when a new HTML file is created, add it to the Site Architecture table immediately.
2. **Log every section addition** — if a new section is added to an existing page (e.g., "added FAQ section to services.html"), record it in the session log under that page's row.
3. **Log every decision** — brand color chosen, font confirmed, layout changed, copy revised. Write the reason if it's not obvious.
4. **Log every scope change** — if the user asks to add or remove something, note what changed and why.
5. **Log every open item** — anything not finished in this session goes into "Open items / next session" so the next session starts with context.
6. **Never delete old session entries** — the log is append-only. Old sessions provide a complete history.
7. **Update the Site Architecture table in real time** — do not wait until the end of the session. Add rows as pages are created.

---

### Developer Handoff Note

The `chat.md` file is part of the developer handoff package alongside `<ClientName>-Functionality.html`. When a developer receives the project, they read `chat.md` first to understand:

- What pages exist and what each one does
- What components are shared across pages
- What decisions were made and why
- What is still outstanding

The developer should never have to ask "what does this page do?" — the answer is in `chat.md`.

> **Presentation rule (Mike clarified 2026-09-08):** Client presentations are **HTML with PowerPoint-style behavior** (`<ClientName>-Presentation.html`) — one full-viewport slide at a time with arrow/space navigation and fullscreen. A `.pptx` file is **not** required. Do not ship long-scroll HTML as the meeting deck.
