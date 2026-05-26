# Image QA Report

## Audit Scope

- Site audited: Netlify deployment before custom-domain binding
- Audit date: 2026-05-25
- Coverage: 35 URLs in the live `sitemap.xml`, 115 live `<img>` references,
  repository image references, and visual review of the relevant existing
  `/assets/` files.
- Result of availability check: all 115 live image references returned
  successfully. No missing image file or wrong image path was found.
- This is a report only. It does not modify HTML, CSS, or image files.

Contact information remains unchanged:

- `xuke@link-jl.com`
- `+86 13201571341`

## Summary

| Category | Finding | Priority |
| --- | --- | --- |
| Missing image | None found in the live sitemap pages or repository references. | None |
| Wrong image path | None found; all audited live image requests resolved. | None |
| Placeholder-looking image | Three prominent solution/industry hero assets are labelled placeholder illustrations rather than product or application photography. | High |
| Weak image match | The Resources hero shows controller hardware instead of documents; several product/project pages reuse a broadly related image for a distinct subject. | High / Medium |
| Repeated image | Projects and Quality galleries show identical images more than once on the same page; some product families are visually indistinguishable. | Medium / Low |
| Layout or image sizing problem | No standalone broken sizing issue confirmed. The large empty feel on affected heroes is caused by placeholder artwork being enlarged, not a missing asset. | Covered by placeholder findings |

## High Priority Findings

### 1. Placeholder Industry Hero Image

`assets/hero-industry.jpg` is a generic illustration containing the visible
label `hero-industry` and `Application Solution`. Used in large hero or card
areas, it looks unfinished rather than representative of Apex equipment.

| Page file path | Image area | Exact `src` value | Issue type | Recommended existing replacement |
| --- | --- | --- | --- | --- |
| `index.html` | Homepage hero main image | `assets/hero-industry.jpg` | placeholder-looking image | `assets/flexible-480kw.jpg` for a real grid-to-plug charging scene, or `assets/integrated/production-03.jpg` for a real industrial capability scene |
| `products/index.html` | Products listing hero | `../assets/hero-industry.jpg` | placeholder-looking image | `../assets/flexible-480kw.jpg` as an available flagship equipment/application visual |
| `solutions/index.html` | Solutions listing hero | `../assets/hero-industry.jpg` | placeholder-looking image | `../assets/flexible-480kw.jpg` for EV infrastructure focus; an approved multi-application hero would ultimately be stronger |
| `solutions/index.html` | Industrial Plant Power System card | `../assets/hero-industry.jpg` | placeholder-looking image | `../assets/integrated/production-03.jpg` as an available real industrial image |
| `solutions/industrial-plant-power-system/index.html` | Solution hero | `../../assets/hero-industry.jpg` | placeholder-looking image | `../../assets/integrated/production-03.jpg` or `../../assets/integrated/production-05.jpg` as interim real-factory visuals |

Priority: **High**.

### 2. Placeholder EV Solution Image

`assets/ev-solution.jpg` is a labelled illustration (`ev-solution`,
`Application Solution`) with large blank visual space. It is especially weak
where used as the main image for a revenue-focused EV solution or contact page.

| Page file path | Image area | Exact `src` value | Issue type | Recommended existing replacement |
| --- | --- | --- | --- | --- |
| `index.html` | Featured EV solution image | `assets/ev-solution.jpg` | placeholder-looking image | `assets/flexible-480kw.jpg` |
| `contact/index.html` | Contact / RFQ hero | `../assets/ev-solution.jpg` | placeholder-looking image | `../assets/flexible-480kw.jpg` |
| `solutions/index.html` | EV Charging Station Power Solution card | `../assets/ev-solution.jpg` | placeholder-looking image | `../assets/flexible-480kw.jpg` |
| `solutions/index.html` | Commercial Building + EV Charging Solution card | `../assets/ev-solution.jpg` | placeholder-looking image | `../assets/ac-charger.jpg` for equipment focus, or `../assets/flexible-480kw.jpg` for application focus |
| `solutions/ev-charging-station-power-solution/index.html` | Solution hero | `../../assets/ev-solution.jpg` | placeholder-looking image | `../../assets/flexible-480kw.jpg` |
| `solutions/commercial-building-ev-charging-solution/index.html` | Solution hero | `../../assets/ev-solution.jpg` | placeholder-looking image | `../../assets/ac-charger.jpg` is available, although an approved commercial-parking installation photo would be preferable |

Priority: **High**.

### 3. Placeholder Solar Solution Image

`assets/solar-solution.jpg` is also a labelled illustration rather than an
actual solar-farm or distribution installation image.

| Page file path | Image area | Exact `src` value | Issue type | Recommended existing replacement |
| --- | --- | --- | --- | --- |
| `solutions/index.html` | Solar Farm Power Distribution Solution card | `../assets/solar-solution.jpg` | placeholder-looking image | `../assets/box-substation.jpg` is a usable equipment-focused interim image; no existing asset depicts a solar farm |
| `solutions/solar-farm-power-distribution-solution/index.html` | Solution hero | `../../assets/solar-solution.jpg` | placeholder-looking image | `../../assets/box-substation.jpg` as interim only; no strongly matched solar-site replacement exists in `/assets/` |

Priority: **High**.

### 4. Resources Hero Does Not Match the Page Topic

The Resources page promises catalogs, reports, certificates, and technical
documents, but its only hero image is a close-up collage of controller
hardware. The filename itself indicates it was used as a fallback.

| Page file path | Image area | Exact `src` value | Issue type | Recommended existing replacement |
| --- | --- | --- | --- | --- |
| `resources/index.html` | Resources hero | `../assets/integrated/reports-fallback-1.jpg` | weak image match / placeholder-looking image | No strong all-resources hero exists. `../assets/integrated/certificate-01.jpg` matches only the certificate portion of the page and is an interim option at best. |

Priority: **High**.

## Medium Priority Findings

### 5. Product Images Do Not Distinguish Different Products

These product pages load correctly, but reuse an image representing a related
product category. This can weaken buyer confidence because distinct models or
technologies appear visually identical.

| Page file path | Subject represented | Exact `src` value | Issue type | Recommended existing replacement |
| --- | --- | --- | --- | --- |
| `products/index.html` | Silicon Steel Core Transformer card | `../assets/oil-transformer.jpg` | repeated image / weak image match | No verified silicon-steel-specific asset available; retain only as interim until an approved product image exists. |
| `products/silicon-steel-core-transformer/index.html` | Product hero | `../../assets/oil-transformer.jpg` | repeated image / weak image match | No verified existing replacement. |
| `products/index.html` | Amorphous Alloy Transformer card | `../assets/dry-transformer.jpg` | repeated image / weak image match | No verified amorphous-alloy-specific asset available. |
| `products/amorphous-alloy-transformer/index.html` | Product hero | `../../assets/dry-transformer.jpg` | repeated image / weak image match | No verified existing replacement. |
| `products/index.html` | Solar Compact Substation card | `../assets/box-substation.jpg` | repeated image / weak image match | No dedicated solar compact substation asset; current image is an interim category match. |
| `products/solar-compact-substation/index.html` | Product hero | `../../assets/box-substation.jpg` | repeated image / weak image match | No dedicated existing replacement. |
| `products/index.html` | 160kW / 400kW Integrated DC Dual-Gun Charging Pile card | `../assets/heavy-duty-charger.jpg` | repeated image / weak image match | `../assets/flexible-480kw.jpg` is a possible application image but is not an exact model match; verified product photography is preferable. |
| `products/160kw-400kw-integrated-dc-dual-gun-charging-pile/index.html` | Product hero | `../../assets/heavy-duty-charger.jpg` | repeated image / weak image match | No exact verified existing replacement. |

Priority: **Medium**.

The same `box-substation.jpg` use on
`products/10kv-box-type-substation/index.html` and
`products/ev-charging-substation-solution/index.html` is not treated as a
definite mismatch: the photographed equipment is relevant to those subjects.

### 6. Project Cases Use Manufacturing or Duplicate Images

The Projects page presents application cases, but the displayed images are
factory-production scenes rather than field project examples. It also repeats
the same photograph for two adjacent cases.

| Page file path | Image area | Exact `src` value | Issue type | Recommended existing replacement |
| --- | --- | --- | --- | --- |
| `projects/index.html` | Hero: Application Cases | `../assets/integrated/production-03.jpg` | weak image match | `../assets/flexible-480kw.jpg` better represents a deployed charging application; no existing multi-sector project hero is available. |
| `projects/index.html` | EV Charging Infrastructure Project card | `../assets/integrated/production-03.jpg` | weak image match / repeated image | `../assets/flexible-480kw.jpg` |
| `projects/index.html` | Solar Farm Power Distribution Project card | `../assets/integrated/production-04.jpg` | weak image match | `../assets/box-substation.jpg` is an interim equipment match; no solar-farm scene exists. |
| `projects/index.html` | Industrial Power Distribution Project card | `../assets/integrated/production-05.jpg` | weak image match | An installed industrial-distribution project image is not present; current factory view is only an interim match. |
| `projects/index.html` | Manufacturing & Delivery Case card | `../assets/integrated/production-05.jpg` | repeated image | `../assets/integrated/production-11.jpg` or `../assets/integrated/production-12.jpg` provides distinct existing factory imagery. |

Priority: **Medium**.

## Low Priority Findings

### 7. Same-Page Repetition in Supporting Galleries

These areas use real, relevant assets, but repeat an image within the same
page. The repetition is less urgent than hero placeholders because it does not
misrepresent the site category.

| Page file path | Repeated areas | Exact `src` value | Issue type | Recommended existing replacement |
| --- | --- | --- | --- | --- |
| `quality/index.html` | Hero and first Production Photos card | `../assets/integrated/production-01.jpg` | repeated image | Keep one placement and consider `../assets/integrated/production-10.jpg`, `production-11.jpg`, or `production-12.jpg` for additional variety. |
| `quality/index.html` | Component Processing and Final Assembly cards | `../assets/integrated/production-05.jpg` | repeated image | `../assets/integrated/production-11.jpg` or `../assets/integrated/production-12.jpg` |
| `certificates/index.html` | Hero and first Certificate Gallery card | `../assets/integrated/certificate-01.jpg` | repeated image | An alternative certificate image such as `../assets/integrated/certificate-02.jpg` could avoid immediate repetition, although the current asset is relevant. |
| `solutions/oem-odm-charging-equipment-solution/index.html` | Hero and JC-6513 recommended-product card | `../../assets/jc6513-controller.jpg` | repeated image | No clear solution-scene image exists; this is acceptable interim reuse or the hero could use another relevant controller asset if approved. |

Priority: **Low**.

## Existing Replacement Assets Worth Reusing

No replacement is applied by this report. The following existing images are
strong candidates for a future approved implementation:

| Existing asset | Suitable future use |
| --- | --- |
| `assets/flexible-480kw.jpg` | EV charging station / grid-to-plug hero imagery and EV project case |
| `assets/heavy-duty-charger.jpg` | Heavy-duty truck charging content where the subject matches |
| `assets/box-substation.jpg` | Substation-focused pages; interim equipment image for solar distribution content |
| `assets/integrated/production-03.jpg` | Factory capability or industrial manufacturing imagery |
| `assets/integrated/production-10.jpg` | Distinct manufacturing/process gallery visual |
| `assets/integrated/production-11.jpg` | Distinct factory automation/gallery visual |
| `assets/integrated/production-12.jpg` | Distinct factory automation/gallery visual |
| `assets/integrated/certificate-01.jpg` | Certification/document-specific content only |

## Constraints for Any Future Fix

- Do not change HTML as part of this audit report.
- Do not change CSS as part of this audit report.
- Do not add new images as part of this audit report.
- Do not delete files as part of this audit report.
- Preserve the current contact information:
  `xuke@link-jl.com` and `+86 13201571341`.
