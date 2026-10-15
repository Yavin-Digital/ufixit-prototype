# Development Reference — Launch Guide

This document contains the technical data needed to take a prototype from this repo into a live production deployment. Update each value as credentials and hosting decisions are confirmed.

---

## Google Analytics

| Field | Value |
|---|---|
| **Measurement ID** | `G-XXXXXXXXXX` ← replace with actual ID |
| **Property type** | GA4 |
| **Integration method** | `react-ga4` via `VITE_GA_MEASUREMENT_ID` env var |
| **Where to find it** | Google Analytics → Admin → Property → Data Streams → Measurement ID |

Initialize in `src/main.jsx`:
```js
import ReactGA from 'react-ga4';
ReactGA.initialize(import.meta.env.VITE_GA_MEASUREMENT_ID);
router.subscribe(() => ReactGA.send('pageview'));
```

---

## Google Tag Manager

| Field | Value |
|---|---|
| **Container ID** | `GTM-XXXXXXX` ← replace with actual ID |
| **Integration method** | Script tag in `index.html` + noscript fallback in `<body>` |
| **Where to find it** | Google Tag Manager → Admin → Container ID |

---

## Google Search Console

| Field | Value |
|---|---|
| **Verification tag** | `<meta name="google-site-verification" content="XXXX" />` ← replace |
| **Integration method** | `VITE_GSC_META_TAG` env var rendered via `react-helmet-async` |
| **Where to find it** | GSC → Settings → Ownership Verification → HTML tag |

---

## SendGrid

| Field | Value |
|---|---|
| **API Key** | `SG.XXXXXXXXXX` ← stored as server-side env var only (never expose client-side) |
| **Where to find it** | sendgrid.com → Settings → API Keys → Create API Key |

---

## Required Environment Variables

| Variable | Source | Used In |
|---|---|---|
| `VITE_GA_MEASUREMENT_ID` | GA4 property | `src/main.jsx` |
| `VITE_GTM_ID` | GTM container | `index.html` script tag |
| `VITE_GSC_META_TAG` | Search Console | `react-helmet-async` head |
| `SENDGRID_API_KEY` | SendGrid (server only) | Contact form API route |

> **Never commit real values to the repo.** Use `.env.local` locally and the host's secrets panel in production.

---

## Build & Deployment

| Step | Command / Detail |
|---|---|
| **Install deps** | `npm install` |
| **Local dev** | `npm run dev` |
| **Production build** | `npm run build` → output in `dist/` |
| **Recommended host** | Vercel / Netlify / custom VPS |
| **Node version** | 18+ (LTS) |

---

## Pre-Launch Checklist

- [ ] GA Measurement ID confirmed and set in host environment
- [ ] GTM Container ID confirmed and set in host environment
- [ ] GSC verification tag confirmed and added to head
- [ ] SendGrid API key set as server-only secret
- [ ] All `{{TOKEN}}` placeholders replaced in every delivered HTML file
- [ ] `img/og-share.jpg` exists at 1200 × 630 px, under 300 KB
- [ ] `favicon.ico` in place
- [ ] `robots.txt` and sitemap.xml generated and submitted to GSC
- [ ] DNS records pointed to production host
- [ ] SSL certificate active (HTTPS enforced)
- [ ] Contact form tested end-to-end (SendGrid delivery confirmed)
- [ ] 404 page live and on-brand
- [ ] axe-core accessibility scan passed (zero critical violations)

---

*Last updated: September 2026*
