# Codex Deployment Task: Apex Power Systems Static Website

## Project Overview

This repository contains a static B2B industrial website for **Apex Power Systems Co., Ltd.**

Apex Power Systems provides **Grid-to-Plug power distribution and EV charging infrastructure solutions**, including:

- Power transformers
- Prefabricated substations
- MV/LV switchgear
- AC/DC EV charging piles
- Intelligent EV charging station controllers
- OCPP / protocol conversion boards

Contact information to preserve throughout the site:

- Email: `xuke@link-jl.com`
- Phone / WhatsApp: `+86 13201571341`

## Current Website Structure

The site is already arranged in an SEO-friendly static directory structure:

```text
/
  index.html
  404.html
  robots.txt
  sitemap.xml
  .htaccess
  /assets/
  /products/
  /solutions/
  /projects/
  /about/
  /quality/
  /certificates/
  /resources/
  /contact/
```

Product and solution pages are already nested as directory-based URLs, for example:

```text
/products/oil-immersed-transformer/
/products/10kv-box-type-substation/
/solutions/ev-charging-station-power-solution/
```

## Main Tasks

Please turn this static website into a clean, deployable GitHub repository.

### 1. Preserve the Current Visual Design

Do not redesign the site unless necessary to fix bugs.

Preserve:

- Dark navy / electric blue / green / orange industrial UI style
- Grid-to-Plug positioning
- Product and solution structure
- Apex Power Systems branding
- Current image assets
- Current SEO directory structure

### 2. Verify Internal Links

Check and fix all internal links.

Requirements:

- No links to `-single.html`
- No flat old links such as `product-xxx.html`
- Product URLs should use `/products/<slug>/`
- Solution URLs should use `/solutions/<slug>/`
- Main pages should use `/about/`, `/contact/`, `/quality/`, etc.
- No broken image references
- No broken CSS, favicon, or asset paths

### 3. Prepare Deployment Configurations

Add deployment support for at least these platforms:

#### Vercel

Add a `vercel.json` file if useful.

Recommended:

```json
{
  "cleanUrls": true,
  "trailingSlash": true,
  "headers": [
    {
      "source": "/assets/(.*)",
      "headers": [
        {
          "key": "Cache-Control",
          "value": "public, max-age=31536000, immutable"
        }
      ]
    }
  ]
}
```

#### Netlify

Add a `netlify.toml` file.

Recommended:

```toml
[build]
  publish = "."

[[headers]]
  for = "/assets/*"
  [headers.values]
    Cache-Control = "public, max-age=31536000, immutable"

[[redirects]]
  from = "/*"
  to = "/404.html"
  status = 404
```

#### Generic Static Hosting

Keep `.htaccess` for Apache hosting.

### 4. Confirm Deployment Domain

The current sitemap uses:

```text
https://apexps.netlify.app
```

The current live Netlify domain is used for sitemap and canonical URLs.

If a custom production domain is provided later, replace all sitemap, canonical, and Open Graph URLs with that domain.

### 5. Add README.md

Create a complete `README.md` with:

- Project overview
- File structure
- Local preview instructions
- Deployment instructions for Vercel
- Deployment instructions for Netlify
- Deployment instructions for generic cPanel / Apache hosting
- How to update sitemap domain
- How to update contact information
- How to add new product pages
- How to add new solution pages

### 6. RFQ Form Integration

The current RFQ forms are static and do not submit.

Please implement one of these options, preferably configurable:

#### Option A: Formspree / Getform / Basin

Set all RFQ forms to submit to a configurable endpoint.

Example:

```html
<form action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
```

Every form should include:

- name
- email
- company
- country
- product or solution interest
- voltage / capacity / power
- quantity or project scale
- message

#### Option B: Netlify Forms

If using Netlify, add:

```html
<form name="rfq" method="POST" data-netlify="true">
<input type="hidden" name="form-name" value="rfq">
```

#### Option C: Keep Static but Document

If no endpoint is available, keep the forms visually intact and add a clear note in README.md explaining how to connect the forms later.

Preferred target email:

```text
xuke@link-jl.com
```

### 7. SEO Checks

Please verify:

- Every page has a unique `<title>`
- Every page has a meta description
- Canonical URLs are present
- `sitemap.xml` includes all important pages
- `robots.txt` points to sitemap
- 404 page exists
- No hidden noindex meta tags
- Images have reasonable alt text

### 8. Performance Cleanup

Please optimize if possible without changing design:

- Remove unused duplicate files
- Compress or resize images if needed
- Keep assets folder organized
- Avoid huge base64 inline images
- Do not include old preview-only files

### 9. Deliverables

Please provide:

- A cleaned GitHub-ready repository
- `README.md`
- `DEPLOYMENT_TASK.md`
- `vercel.json`
- `netlify.toml`
- Updated `sitemap.xml`
- Working static site structure
- Confirmation that there are no broken internal links or missing assets

## Important Constraints

- Do not remove product pages.
- Do not remove solution pages.
- Do not change Apex contact information.
- Do not invent certifications, clients, project locations, or technical claims.
- If a document/certificate scope is unclear, use cautious wording such as:
  “Documents are available upon request.”
- Keep the website in English.
