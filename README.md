# Apex Power Systems Static Website

This is a static B2B industrial website for **Apex Power Systems Co., Ltd.**

## Design System (2026 Redesign)

The site uses a **monochrome + electric blue** high-end industrial design:

- **Surfaces**: white `#fff`, off-black `#0b0d10`, light gray `#f5f6f7`
- **Accent**: electric blue `#1e5eff` — the only chromatic voice, used for CTAs, links, and key highlights
- **Type**: Space Grotesk (display) + Inter (body), loaded via Google Fonts
- **Architecture**: all styling lives in one shared file — `assets/site.css` — referenced by every page. Inline per-page CSS was removed in the redesign, so the whole site (42 pages) updates from a single file.
- **Layout**: sticky glassmorphism nav, dark hero sections with radial accent glow, card-based product grids, Netlify RFQ forms

To restyle the entire site, edit `assets/site.css` only.

## Positioning

**Grid-to-Plug Power Distribution & EV Charging Solutions**

Apex Power Systems provides integrated power distribution and EV charging infrastructure equipment, including transformers, prefabricated substations, MV/LV switchgear, EV charging piles, and intelligent charging controllers.

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
projects/
about/
quality/
certificates/
resources/
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
- Voltage / capacity / power
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
