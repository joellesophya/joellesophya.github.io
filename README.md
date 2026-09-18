# Joelle Mbatchou — personal academic website (static revamp)

Modern static rebuild of [joellesophya.github.io](https://joellesophya.github.io/), migrated from the previous Distill / R Markdown site.

## Stack

- **Clean multi-page HTML / CSS / JS** (no framework build step)
- Deployable output lives in **`docs/`** (same GitHub Pages layout as before)
- Shared stylesheet + small nav script; Google Fonts (Fraunces + Source Sans 3)
- Regenerator: `src/build_site.py` (builds pages; Publications are generated from the BibTeX file)

Astro was considered; plain static HTML was chosen so GitHub Pages works with zero toolchain and a familiar `docs/` folder.

## What’s included

| Path | Purpose |
|------|---------|
| `docs/` | Site to publish (Pages source) |
| `docs/index.html` | Home |
| `docs/research.html` | Research |
| `docs/pubs.html` | Publications |
| `docs/cv/cv.html` | CV (HTML summary) |
| `docs/cv/cv2025.pdf` | CV PDF (from previous site) |
| `docs/contact.html` | Contact |
| `docs/assets/` | Logo, photo (optimized), CSS, JS |
| `docs/.nojekyll` | Keeps Pages from running Jekyll |
| `src/build_site.py` | Rebuild HTML from the generator |
| `docs/assets/myrefs.bib` | Canonical publications bibliography (BibTeX) |
| `_source_fetch/` | Cached source excerpts used during migration (optional to keep) |

## Preview locally

From this directory:

```bash
python3 -m http.server 8080 --directory docs
```

Then open http://127.0.0.1:8080/

## Publish to GitHub Pages (user site `joellesophya.github.io`)

1. Back up the current repo (or work on a branch).
2. Replace the repo contents with this project (at minimum keep/replace the `docs/` folder and root `README.md`).
3. In the GitHub repo: **Settings → Pages → Build and deployment**
   - Source: **Deploy from a branch**
   - Branch: `master` (or `main`), folder: **`/docs`**
4. Commit and push. Site should appear at https://joellesophya.github.io/

### URL continuity

Filenames match the previous site (`research.html`, `pubs.html`, `cv/cv.html`, `contact.html`) so most bookmarks keep working.

### Optional: publish from repo root instead

Copy everything inside `docs/` to the repository root, set Pages to **`/` (root)**, and keep `.nojekyll`.

## Migrated content

- **Home** — welcome bio (fixed typo `relationshp` → `relationship`); portrait; social links
- **Research** — Regeneron / UChicago intro + three project cards (REGENIE DOI + BRASS bioRxiv link from source)
- **Publications** — generated from `docs/assets/myrefs.bib` (BibTeX); first-author flagged; DOI links when present
- **CV** — experience, teaching, education, honors, skills, service from prior `cv/cv.html`; PDF download
- **Contact** — email, Twitter, LinkedIn, Tarrytown address
- **Assets** — `JTM_Logo.png`; portrait optimized to WebP/JPEG (original PNG was ~5.5 MB)
- **Social** — GitHub, Twitter `@joellembatchou`, LinkedIn `/in/jmbatchou/`, Google Scholar `njW-kAMAAAAJ`, email

No publications, affiliations, or bio facts were invented.

## Design notes

- Soft cream background, deep ink text, teal accent, warm terracotta highlights
- Sticky responsive nav with Home / Research / Publications / CV / Contact + social icons
- Generous spacing, accessible focus states, skip link, mobile menu
- Distinctive display type (Fraunces) rather than a generic template look

## Follow-ups (optional)

- Wire DOI / PubMed links for every publication (source bib often lacked DOIs)
- Replace the large CV PDF with a lighter export if desired
- Add Open Graph image meta if you want richer social previews
- Conference talks listed on the old HTML CV were summarized lightly; full talk list can be restored from the PDF if you want them on-page

## Update publications

Edit the BibTeX file, then rebuild:

```bash
# 1. Edit bibliography
#    docs/assets/myrefs.bib

# 2. Regenerate HTML (including pubs.html)
python3 src/build_site.py
```

Publications are **not** hardcoded in Python — `src/build_site.py` parses `docs/assets/myrefs.bib`, sorts by year (newest first), marks first-author papers when Mbatchou is first, and emits DOI links when a `doi` field (or known fallback) is present.

## Rebuild pages after editing the generator

```bash
python3 src/build_site.py
```
