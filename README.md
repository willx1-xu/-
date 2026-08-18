# Apex Power Systems Static Website

This is a static B2B website for **Apex Power Systems Co., Ltd.** — focused on EV charging infrastructure.

## Positioning

**EV Charging Piles & Intelligent Charging Controllers**

Apex Power Systems specializes in AC/DC EV charging piles (7kW to 480kW) and OCPP 1.6J/2.0-ready charging station controllers and protocol boards for commercial, public, fleet, and OEM/ODM projects.

## Product Scope

The site covers two focused product families (power transformers, substations, and switchgear were removed in the 2026 restructure):

- **AC/DC Charging Piles** — 7kW AC, 40kW DC, 160kW/400kW dual-gun DC, 400kW truck charger, 480kW group charging
- **Charging Station Controllers** — JC-6512 DC controller, JC-6513 hub controller, JC-6650 AC controller, JC-6620 OCPP board, JC-1301 CHAdeMO board
- **Solutions** — EV charging stations, commercial buildings, OEM/ODM programs

## Design System (v2 — Minimal High-End White)

- **Surfaces**: white-led with generous whitespace; off-black `#0a0d11` for hero/footer contrast; light gray `#f7f8f9` for soft sections
- **Accent**: electric blue `#1257e8` — restrained, used for CTAs, links, and key highlights
- **Type**: Space Grotesk (display) + Inter (body), loaded via Google Fonts
- **Architecture**: all styling lives in one shared file — `assets/site.css` — referenced by every page. Inline per-page CSS was removed, so the whole site updates from a single file.
- **Layout**: sticky glassmorphism nav, dark hero with radial accent glow, 3-column product grids, Netlify RFQ forms

To restyle the entire site, edit `assets/site.css` only.

## Contact

- Email: `xuke@link-jl.com`
- Phone / WhatsApp: `+86 13201571341`

## Local Preview

Open `dev-index.html` in a browser to navigate the site locally.

Or open:

```text
index.html
products/index.html
solutions/index.html
contact/index.html
```

## Deployment Options

### Vercel

1. Push this folder to GitHub.
2. Import the GitHub repository into Vercel.
3. Use default static site settings.
4. Set the project root to this repository root.
5. Deploy.

### Netlify

1. Push this folder to GitHub.
2. Import the GitHub repository into Netlify.
3. Set publish directory to `.`
4. Deploy.
5. In Netlify Forms, configure submission notifications for `rfq` to `xuke@link-jl.com`.

### Generic Hosting / cPanel / Apache

1. Upload all files and folders to the web root.
2. Keep `.htaccess`.
3. Enable SSL.
4. Update sitemap domain.
5. Submit sitemap to Google Search Console.

## Important Files

```text
index.html
404.html
robots.txt
sitemap.xml
.htaccess
assets/
products/
solutions/
about/
quality/
contact/
```

## Form Integration

All RFQ and contact forms are configured for Netlify Forms using the form name `rfq`. Submissions include:

- Name
- Email
- Phone / WhatsApp
- Company
- Country
- Product or solution interest
- Power rating / connector / protocol
- Quantity / project scale
- Message

After the first Netlify deployment, enable email notifications for `rfq` submissions to:

```text
xuke@link-jl.com
```

Vercel and generic static hosting remain compatible for displaying the website. Form processing on those hosts requires connecting the same named fields to a form endpoint or backend handler.

## SEO Notes

The canonical production domain is:

```text
https://www.link-jl.com
```

If a custom production domain is added later, replace this URL in:

```text
sitemap.xml
robots.txt
canonical tags
Open Graph URLs
```

## Maintenance

To add a new product page:

1. Copy an existing page under `/products/<product-slug>/index.html`
2. Update title, meta description, hero text, image, specs, applications, FAQ, and RFQ product option.
3. Add the page to `/products/index.html`
4. Add the URL to `sitemap.xml`

To add a new solution page:

1. Copy an existing page under `/solutions/<solution-slug>/index.html`
2. Update solution overview, system architecture, products, applications, FAQ, and RFQ.
3. Add the page to `/solutions/index.html`
4. Add the URL to `sitemap.xml`
