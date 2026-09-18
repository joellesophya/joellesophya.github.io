#!/usr/bin/env python3
"""Generate the static multi-page site into docs/."""
from pathlib import Path
import html

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

SOCIAL_SVG = {
    "github": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2C6.48 2 2 6.58 2 12.26c0 4.52 2.87 8.35 6.84 9.7.5.1.68-.22.68-.48 0-.24-.01-.87-.01-1.7-2.78.62-3.37-1.37-3.37-1.37-.45-1.18-1.11-1.5-1.11-1.5-.91-.64.07-.63.07-.63 1 .07 1.53 1.06 1.53 1.06.89 1.56 2.34 1.11 2.91.85.09-.66.35-1.11.63-1.37-2.22-.26-4.55-1.14-4.55-5.07 0-1.12.39-2.03 1.03-2.75-.1-.26-.45-1.3.1-2.7 0 0 .84-.27 2.75 1.05A9.3 9.3 0 0 1 12 6.84c.85 0 1.7.12 2.5.34 1.9-1.32 2.74-1.05 2.74-1.05.55 1.4.2 2.44.1 2.7.64.72 1.03 1.63 1.03 2.75 0 3.94-2.34 4.8-4.57 5.06.36.32.68.94.68 1.9 0 1.37-.01 2.47-.01 2.81 0 .26.18.58.69.48A10.05 10.05 0 0 0 22 12.26C22 6.58 17.52 2 12 2z"/></svg>',
    "twitter": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-4.714-6.231-5.401 6.231H2.744l7.727-8.835L1.5 2.25H8.08l4.253 5.622L18.244 2.25zm-1.161 17.52h1.833L7.084 4.126H5.117L17.083 19.77z"/></svg>',
    "linkedin": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4.98 3.5C4.98 4.88 3.86 6 2.5 6S0 4.88 0 3.5 1.12 1 2.5 1s2.48 1.12 2.48 2.5zM.5 8.5h4V23h-4V8.5zM8.5 8.5h3.8v2h.05c.53-1 1.83-2.05 3.77-2.05 4.03 0 4.78 2.65 4.78 6.1V23h-4v-6.6c0-1.57-.03-3.6-2.2-3.6-2.2 0-2.54 1.72-2.54 3.5V23h-4V8.5z"/></svg>',
    "scholar": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2L1 9l4 2.5V17l7 4 7-4v-5.5L23 9 12 2zm0 2.3L19.2 9 12 13.7 4.8 9 12 4.3zM7 12.1l5 3.2 5-3.2V16l-5 2.9L7 16v-3.9z"/></svg>',
    "email": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4-8 5L4 8V6l8 5 8-5v2z"/></svg>',
}

SOCIALS = [
    ("GitHub", "https://github.com/joellesophya", "github"),
    ("Twitter / X", "https://twitter.com/joellembatchou", "twitter"),
    ("LinkedIn", "https://www.linkedin.com/in/jmbatchou/", "linkedin"),
    ("Google Scholar", "https://scholar.google.com/citations?hl=en&user=njW-kAMAAAAJ", "scholar"),
]

NAV = [
    ("Home", "index.html", "home"),
    ("Research", "research.html", "research"),
    ("Publications", "pubs.html", "pubs"),
    ("CV", "cv/cv.html", "cv"),
    ("Contact", "contact.html", "contact"),
]


def asset_prefix(page_id: str) -> str:
    return "../" if page_id == "cv" else ""


def nav_href(href: str, page_id: str) -> str:
    p = asset_prefix(page_id)
    if page_id == "cv":
        if href.startswith("cv/"):
            return href.replace("cv/", "", 1)
        return "../" + href
    return href


def render_shell(title: str, page_id: str, body: str, description: str) -> str:
    p = asset_prefix(page_id)
    nav_items = []
    for label, href, pid in NAV:
        current = ' aria-current="page"' if pid == page_id else ""
        nav_items.append(f'<li><a href="{nav_href(href, page_id)}"{current}>{label}</a></li>')
    social_items = []
    for label, url, key in SOCIALS:
        social_items.append(
            f'<a href="{url}" target="_blank" rel="noopener noreferrer" aria-label="{label}">{SOCIAL_SVG[key]}</a>'
        )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title}</title>
  <meta name="description" content="{description}" />
  <meta name="author" content="Joelle Mbatchou" />
  <link rel="icon" href="{p}assets/JTM_Logo.png" type="image/png" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=IBM+Plex+Mono:wght@400;500&family=Source+Sans+3:wght@400;550;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="{p}assets/styles.css" />
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>
  <header class="site-header">
    <div class="nav-wrap">
      <a class="brand" href="{nav_href('index.html', page_id)}">
        <img src="{p}assets/JTM_Logo.png" alt="" width="36" height="36" />
        <div>
          <span>Joelle Mbatchou</span>
          <small>Statistical Geneticist</small>
        </div>
      </a>
      <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav">Menu</button>
      <div class="nav-panel" id="site-nav">
        <ul class="nav-links">
          {''.join(nav_items)}
        </ul>
        <div class="social">
          {''.join(social_items)}
        </div>
      </div>
    </div>
  </header>
  <main id="main">
{body}
  </main>
  <footer class="site-footer">
    <div class="footer-inner">
      <p>© Joelle Mbatchou. Content migrated from the prior Distill site.</p>
      <p><a href="https://creativecommons.org/licenses/by/4.0/" rel="license">CC BY 4.0</a> · <a href="mailto:joelle.mbatchou@gmail.com">Email</a></p>
    </div>
  </footer>
  <script src="{p}assets/site.js" defer></script>
</body>
</html>
"""


def page_home() -> str:
    body = """
    <section class="hero" aria-labelledby="hero-title">
      <div>
        <p class="eyebrow">Welcome</p>
        <h1 id="hero-title">Joelle Mbatchou, PhD</h1>
        <p class="lede">I am a statistical geneticist who is passionate about leveraging large scale genetic datasets to help improve our understanding of the relationship between genetics and human disease.</p>
        <div class="actions">
          <a class="btn btn-primary" href="research.html">Explore research</a>
          <a class="btn btn-ghost" href="pubs.html">View publications</a>
          <a class="btn btn-ghost" href="cv/cv.html">Curriculum vitae</a>
        </div>
      </div>
      <div class="hero-card">
        <picture>
          <source srcset="assets/jtm_2022.webp" type="image/webp" />
          <img class="hero-photo" src="assets/jtm_2022.jpg" alt="Portrait of Joelle Mbatchou" width="720" height="900" />
        </picture>
      </div>
    </section>

    <section class="section" aria-labelledby="focus-title">
      <div class="section-head">
        <h2 id="focus-title">Focus areas</h2>
        <p>Methods and tools for large-scale genetic association</p>
      </div>
      <div class="card-grid">
        <article class="card">
          <span class="tag">Methods</span>
          <h3>Whole-genome regression</h3>
          <p>Efficient association analyses for biobank-scale cohorts and many phenotypes.</p>
        </article>
        <article class="card">
          <span class="tag">Structure</span>
          <h3>Structured samples</h3>
          <p>Models and tests that account for population structure and relatedness.</p>
        </article>
        <article class="card">
          <span class="tag">Software</span>
          <h3>Scalable tooling</h3>
          <p>Computational methods and pipelines used in large human genetics studies.</p>
        </article>
      </div>
    </section>

    <section class="section">
      <div class="note">
        <p>Currently a statistical geneticist at the Regeneron Genetics Center. PhD in Statistics from the University of Chicago (advisor: Prof. Mary Sara McPeek).</p>
      </div>
    </section>
"""
    return render_shell(
        "Joelle Mbatchou, PhD",
        "home",
        body,
        "Personal academic website of Joelle Mbatchou, statistical geneticist.",
    )


def page_research() -> str:
    body = """
    <p class="eyebrow">Research</p>
    <h1>My research interests</h1>
    <p class="lede">I currently work as a statistical geneticist at the Regeneron Genetics Center where my research focuses on developing statistical methods and computational tools for large-scale genetic association analyses to better understand the impact of genetic variation on human disease.</p>
    <p>Prior to joining Regeneron, I obtained my PhD in Statistics from the University of Chicago under the supervision of Prof. Mary Sara McPeek where I built statistical models for genetic association analysis in structured samples.</p>
    <p>A key goal in my work is to identify associations between genetic markers (e.g. SNPs) and a phenotype of interest (e.g. complex human trait or gene expression levels). More recently, I have also been interested in building efficient models and tools for applications to large-scale biobanks (e.g. 100,000s of individuals and 1,000s of phenotypes).</p>

    <section class="section" aria-labelledby="projects-title">
      <div class="section-head">
        <h2 id="projects-title">Selected projects</h2>
      </div>
      <div class="research-list">
        <article class="research-item">
          <div class="mark" aria-hidden="true">1</div>
          <div>
            <h3>Computationally efficient whole genome regression for large-scale biobanks</h3>
            <p>Advances in sequencing technologies have enabled for biobanks to gather genetic information on hundred of thousands of individuals. Along with the use of electronic health records, this provides an invaluable resource to better understand how genetic variation influence human disease. Many association mapping tools have been released to analyze data at this scale yet they still remain highly computationally burdensome. We developed a novel tool for efficient genetic association analyses which reduces the computational requirements of current state-of-the-art tools by using a whole genome regression framework within a machine learning model.</p>
            <a class="more" href="https://doi.org/10.1038/s41588-021-00870-7" target="_blank" rel="noopener noreferrer">Read the paper (Nature Genetics)</a>
          </div>
        </article>
        <article class="research-item">
          <div class="mark" aria-hidden="true">2</div>
          <div>
            <h3>Permutation methods in binary trait association mapping</h3>
            <p>Identifying genetic associations involves assessing the statistical significance of a given test statistic by deriving its null distribution or an asymptotic approximation to it. However, this is not always feasible as the distribution may be intractable. This can be encountered in genome scans to establish a genome-wide significance threshold for the maximum of many correlated tests. We develop a novel method to overcome these limitations when testing association between a binary trait and an arbitrary predictor in samples with population structure.</p>
            <a class="more" href="https://doi.org/10.1371/journal.pgen.1011020" target="_blank" rel="noopener noreferrer">Read the paper (PLoS Genetics)</a>
          </div>
        </article>
        <article class="research-item">
          <div class="mark" aria-hidden="true">3</div>
          <div>
            <h3>Fast method for assessing significance for a wide class of association tests</h3>
            <p>We focus on the assessment of significance in genetic association analysis of single or multi-dimensional phenotypes, including high-dimensional phenotypes, where association is being tested with either a single genetic marker or with multiple genetic markers simultaneously such as in gene/region-based tests. Existing approaches are either computationally burdensome (permutation-based approaches), or do not perform well in settings such as small samples, high-dimensional traits, or misspecified phenotype model, or do not account for existing sample structure when it is present. We develop a novel method to assess significance for a broad class of test statistics currently used in genetic association analyses that is based on moment-matching and allows for very general population structure and relatedness in the data.</p>
            <a class="more" href="https://doi.org/10.1016/j.ajhg.2024.06.010" target="_blank" rel="noopener noreferrer">Read the paper (AJHG)</a>
          </div>
        </article>
      </div>
    </section>
"""
    return render_shell(
        "Research — Joelle Mbatchou",
        "research",
        body,
        "Research interests of Joelle Mbatchou in statistical genetics.",
    )


BIB_PATH = DOCS / "assets" / "myrefs.bib"

# Fallback DOI links when a bib entry lacks a doi field (legacy special-cases).
DOI_BY_TITLE_HINT = {
    "whole-genome regression for quantitative": "10.1038/s41588-021-00870-7",
}


def _strip_braces(value: str) -> str:
    value = value.strip()
    while value.startswith("{") and value.endswith("}"):
        value = value[1:-1].strip()
    return value


def _latex_to_text(value: str) -> str:
    """Minimal LaTeX cleanup for display (accents, dashes, math-ish bits)."""
    import re
    value = _strip_braces(value)
    replacements = {
        r"{\\'i}": "í",
        r"{\\`a}": "à",
        r'{\\"u}': "ü",
        r"{\\ss}": "ß",
        r"{\\~n}": "ñ",
        r"\\&": "&",
        r"---": "—",
        r"--": "–",
        r"~": " ",
    }
    for a, b in replacements.items():
        value = value.replace(a, b)
    # Generic {\'x} / {\"x}
    value = re.sub(r"\{\\'([A-Za-z])\}", r"\1", value)
    value = re.sub(r"\{\\\"([A-Za-z])\}", r"\1", value)
    value = re.sub(r"\{([^}]*)\}", r"\1", value)
    value = value.replace("\\", "")
    return " ".join(value.split())


def parse_bibtex(path: Path) -> list[dict]:
    """Simple BibTeX parser for @article entries used on this site."""
    import re
    raw = path.read_text(encoding="utf-8-sig")
    entries = []
    for m in re.finditer(r"@(\w+)\s*\{\s*([^,]+)\s*,", raw):
        etype, key = m.group(1).lower(), m.group(2).strip()
        if etype != "article":
            continue
        # Find matching closing brace for this entry
        i = m.end()
        depth = 1
        while i < len(raw) and depth:
            if raw[i] == "{":
                depth += 1
            elif raw[i] == "}":
                depth -= 1
            i += 1
        body = raw[m.end() : i - 1]
        fields = {}
        for fm in re.finditer(
            r"(\w+)\s*=\s*(\{(?:[^{}]|\{[^{}]*\})*\}|\"[^\"]*\"|[^\s,]+)\s*,?",
            body,
            flags=re.S,
        ):
            name = fm.group(1).lower()
            val = fm.group(2).strip()
            if val.startswith("{") or val.startswith('"'):
                val = val[1:-1]
            fields[name] = _latex_to_text(val)
        if not fields.get("title") or not fields.get("year"):
            continue
        entries.append({"key": key, "type": etype, **fields})
    return entries


def _split_authors(author_field: str) -> list[str]:
    parts = [p.strip() for p in author_field.split(" and ") if p.strip()]
    return parts


def _initials(given: str) -> str:
    bits = []
    for token in given.replace("-", "-").split():
        if not token:
            continue
        if "-" in token:
            bits.append("-".join(p[0].upper() + "." for p in token.split("-") if p))
        else:
            bits.append(token[0].upper() + ".")
    return " ".join(bits)


def format_author_name(raw: str) -> str:
    raw = raw.strip()
    if raw.lower() in {"others", "et al", "et al."}:
        return "et al."
    if "Regeneron" in raw or "Collaboration" in raw or "Consortium" in raw:
        return raw
    if "," in raw:
        last, given = [x.strip() for x in raw.split(",", 1)]
        if given:
            return f"{last}, {_initials(given)}"
        return last
    # "First Last" form
    toks = raw.split()
    if len(toks) >= 2:
        return f"{toks[-1]}, {_initials(' '.join(toks[:-1]))}"
    return raw


def format_authors_nature(author_field: str, max_names: int = 10) -> str:
    names = _split_authors(author_field)
    formatted = []
    saw_etal = False
    for n in names:
        f = format_author_name(n)
        if f == "et al.":
            saw_etal = True
            break
        formatted.append(f)
    if len(formatted) > max_names:
        formatted = formatted[:max_names]
        saw_etal = True
    if not formatted:
        return "et al."
    if len(formatted) == 1:
        out = formatted[0]
    elif len(formatted) == 2 and not saw_etal:
        out = f"{formatted[0]} & {formatted[1]}"
    else:
        if saw_etal:
            out = ", ".join(formatted) + ", et al."
        elif len(formatted) <= 3:
            out = ", ".join(formatted[:-1]) + f" & {formatted[-1]}"
        else:
            out = ", ".join(formatted[:-1]) + f" & {formatted[-1]}"
    return out


def is_joelle_first_author(author_field: str) -> bool:
    names = _split_authors(author_field)
    if not names:
        return False
    first = names[0].lower()
    return "mbatchou" in first


def format_venue(entry: dict) -> str:
    journal = entry.get("journal") or entry.get("booktitle") or ""
    parts = [journal] if journal else []
    vol = entry.get("volume")
    pages = entry.get("pages")
    if vol and pages:
        parts.append(f"{vol}, {pages.replace('--', '–')}")
    elif vol:
        num = entry.get("number")
        parts.append(f"{vol} ({num})" if num else vol)
    elif pages:
        parts.append(pages.replace("--", "–"))
    return " ".join(parts).strip()


def resolve_doi(entry: dict) -> str | None:
    doi = (entry.get("doi") or "").strip()
    if doi:
        return doi.removeprefix("https://doi.org/")
    title_l = (entry.get("title") or "").lower()
    for hint, d in DOI_BY_TITLE_HINT.items():
        if hint in title_l:
            return d
    return None


def load_publications(bib_path: Path = BIB_PATH) -> list[dict]:
    entries = parse_bibtex(bib_path)
    pubs = []
    for e in entries:
        year = str(e.get("year", "")).strip()
        try:
            year_i = int(year[:4])
        except ValueError:
            year_i = 0
        pubs.append(
            {
                "year": year,
                "year_i": year_i,
                "authors": format_authors_nature(e.get("author", "")),
                "title": e.get("title", ""),
                "venue": format_venue(e),
                "first_author": is_joelle_first_author(e.get("author", "")),
                "doi": resolve_doi(e),
                "key": e.get("key", ""),
            }
        )
    # Newest first; within a year, first-author papers first, then title
    pubs.sort(key=lambda p: (-p["year_i"], 0 if p["first_author"] else 1, p["title"].lower()))
    return pubs


def page_pubs() -> str:
    publications = load_publications()
    items = []
    for i, pub in enumerate(publications, 1):
        cls = ' class="pub first-author"' if pub["first_author"] else ' class="pub"'
        doi_extra = ""
        if pub.get("doi"):
            doi_extra = (
                f' · <a href="https://doi.org/{pub["doi"]}" target="_blank" '
                f'rel="noopener noreferrer">DOI</a>'
            )
        venue = pub["venue"]
        year = pub["year"]
        title = html.escape(pub["title"])
        authors = html.escape(pub["authors"])
        venue_e = html.escape(venue)
        items.append(f"""
        <li{cls}>
          <div class="num">{i:02d}</div>
          <div>
            <p class="title">{title}</p>
            <p class="meta">{authors}{"." if not authors.endswith(".") else ""} <span class="venue">{venue_e}</span> ({html.escape(year)}).{doi_extra}</p>
          </div>
        </li>""")
    body = f"""
    <p class="eyebrow">Scholarship</p>
    <h1>My publications</h1>
    <p class="lede">First-author papers are marked.</p>
    <p style="margin-top:-0.5rem"><a href="https://scholar.google.com/citations?hl=en&amp;user=njW-kAMAAAAJ" target="_blank" rel="noopener noreferrer">Google Scholar profile</a></p>
    <ol class="pub-list">
      {''.join(items)}
    </ol>
"""
    return render_shell(
        "Publications — Joelle Mbatchou",
        "pubs",
        body,
        "Publications by Joelle Mbatchou.",
    )


def page_contact() -> str:
    body = f"""
    <p class="eyebrow">Get in touch</p>
    <h1>Contact me</h1>
    <p class="lede">I look forward to connect with you!</p>
    <div class="contact-grid">
      <ul class="contact-list">
        <li>
          <div class="icon" aria-hidden="true">{SOCIAL_SVG['email']}</div>
          <div>
            <span class="label">Email</span>
            <a href="mailto:joelle.mbatchou@gmail.com">joelle.mbatchou@gmail.com</a>
          </div>
        </li>
        <li>
          <div class="icon" aria-hidden="true">{SOCIAL_SVG['twitter']}</div>
          <div>
            <span class="label">Twitter / X</span>
            <a href="https://twitter.com/joellembatchou" target="_blank" rel="noopener noreferrer">@joellembatchou</a>
          </div>
        </li>
        <li>
          <div class="icon" aria-hidden="true">{SOCIAL_SVG['linkedin']}</div>
          <div>
            <span class="label">LinkedIn</span>
            <a href="https://www.linkedin.com/in/jmbatchou/" target="_blank" rel="noopener noreferrer">/in/jmbatchou</a>
          </div>
        </li>
        <li>
          <div class="icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor" aria-hidden="true"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5A2.5 2.5 0 1 1 12 6a2.5 2.5 0 0 1 0 5.5z"/></svg></div>
          <div>
            <span class="label">Location</span>
            <span>777 Old Saw Mill River Road · Tarrytown, NY 10591 · USA</span>
          </div>
        </li>
      </ul>
      <aside class="note">
        <p>Also on <a href="https://github.com/joellesophya" target="_blank" rel="noopener noreferrer">GitHub</a> and <a href="https://scholar.google.com/citations?hl=en&amp;user=njW-kAMAAAAJ" target="_blank" rel="noopener noreferrer">Google Scholar</a>.</p>
      </aside>
    </div>
"""
    return render_shell(
        "Contact — Joelle Mbatchou",
        "contact",
        body,
        "Contact Joelle Mbatchou.",
    )


def page_cv() -> str:
    # CV content migrated from docs/cv/cv.html (structured summary) + PDF download
    body = """
    <p class="eyebrow">Curriculum vitae</p>
    <h1>Joelle Mbatchou, Ph.D.</h1>
    <p class="lede">Proficient and innovative researcher with 10+ years of research experience in developing cutting-edge methods to help improve understanding of genetic variation and its relationship to human health and disease.</p>
    <div class="actions" style="margin-bottom:1.75rem">
      <a class="btn btn-primary" href="cv2025.pdf">Download CV (PDF)</a>
      <a class="btn btn-ghost" href="../pubs.html">Publications list</a>
    </div>

    <div class="cv-layout">
      <div>
        <section class="section" aria-labelledby="exp-title">
          <div class="section-head"><h2 id="exp-title">Experience</h2></div>
          <div class="timeline">
            <article class="job">
              <div class="when">2024 – Current · Tarrytown, New York</div>
              <h3>Senior Manager, Statistical Genetics</h3>
              <p>Regeneron Genetics Center</p>
              <ul>
                <li>Leading and mentoring a team member in the development of an analytical pipeline for time-to-event data.</li>
                <li>Develop machine learning methods to integrate functional annotations into rare variant association analyses using exome sequencing data.</li>
              </ul>
            </article>
            <article class="job">
              <div class="when">2022 – 2023 · Tarrytown, New York</div>
              <h3>Manager, Statistical Genetics</h3>
              <p>Regeneron Genetics Center</p>
              <ul>
                <li>Routinely carry out statistical analyses using cloud-based computing platforms on large-scale and high-dimensional human genetics datasets containing millions of genetic variants and 100,000s of individuals.</li>
                <li>Develop statistical methods and computational tools geared for large-scale genetic and genomics studies.</li>
                <li>Build WDL pipelines for data sets with 100,000s of individuals from whole-exome and whole-genome sequencing data.</li>
              </ul>
            </article>
            <article class="job">
              <div class="when">2019 – 2021 · Tarrytown, New York</div>
              <h3>Senior Statistical Geneticist</h3>
              <p>Regeneron Genetics Center</p>
              <ul>
                <li>Developed a computationally efficient whole genome regression method REGENIE for large-scale genetic association analyses which can be more than 100x faster than current state-of-the-art methods and can handle population structure and imbalanced binary traits.</li>
                <li>Implemented REGENIE into a C++ software which was publicly released on GitHub.</li>
                <li>Published the REGENIE method as first author in Nature Genetics where it was applied to UK Biobank data (&gt;100 phenotypes, &gt;400K individuals and &gt;10M genetic variants).</li>
              </ul>
            </article>
            <article class="job">
              <div class="when">2013 – 2019 · Chicago, IL</div>
              <h3>Graduate Student Researcher</h3>
              <p>Department of Statistics, University of Chicago</p>
              <ul>
                <li>Developed a computationally fast method JASPER to assess significance for a general class of association tests, including tests for high dimensional phenotypes and gene-based tests, adjusting for population structure and family relatedness.</li>
                <li>Designed a permutation-based testing procedure BRASS for assessing significance with binary traits in structured samples for association tests with unknown exact/asymptotic distributions.</li>
                <li>Built C/C++ software to evaluate JASPER and BRASS through simulation studies &amp; real data applications.</li>
              </ul>
            </article>
          </div>
        </section>

        <section class="section" aria-labelledby="teach-title">
          <div class="section-head"><h2 id="teach-title">Teaching</h2></div>
          <div class="timeline">
            <article class="job">
              <div class="when">2022 – Current</div>
              <h3>Instructor</h3>
              <p>Summer Institute in Statistical Genetics · University of Washington / Georgia Institute of Technology</p>
              <ul>
                <li>Taught the association mapping module on genome-wide association studies and sequencing (120 students).</li>
                <li>Designed coursework as well as hands-on practical exercises using software such as PLINK, REGENIE and R packages GWASTools and bigsnpr.</li>
                <li>Built a website to host the course materials using workflowr R package.</li>
              </ul>
            </article>
            <article class="job">
              <div class="when">2012 – 2019 · University of Chicago</div>
              <h3>Teaching Assistant &amp; Course Instructor</h3>
              <ul>
                <li>Assisted in undergraduate courses: Statistical Methods and Applications, Statistical Models/Methods, Applied Regression Analysis and Analysis of Categorical Data.</li>
                <li>Created introductory material for R and STATA through weekly computer sessions; organized weekly office hours.</li>
                <li>Taught introductory statistical methods (STAT 234) in 2018 to a class of 36 students.</li>
                <li>Statistics Collaborative Learning Team Leader (2016–2017).</li>
              </ul>
            </article>
          </div>
        </section>

        <section class="section" aria-labelledby="edu-title">
          <div class="section-head"><h2 id="edu-title">Education</h2></div>
          <div class="timeline">
            <article class="edu">
              <div class="when">2019 · Chicago, IL</div>
              <h3>PhD, Statistics</h3>
              <p>University of Chicago</p>
            </article>
            <article class="edu">
              <div class="when">2011 · Chicago, IL</div>
              <h3>BSc Biology &amp; Mathematical Sciences</h3>
              <p>DePaul University</p>
            </article>
          </div>
        </section>

        <section class="section" aria-labelledby="awards-title">
          <div class="section-head"><h2 id="awards-title">Selected honors</h2></div>
          <div class="timeline">
            <article class="award"><div class="when">2022</div><h3>Selected as one of 35 innovators under 35</h3></article>
            <article class="award"><div class="when">2022</div><h3>Selected as one of 17 Rising Stars in Health Tech</h3></article>
            <article class="award"><div class="when">2021</div><h3>Selected for Reviewers’ Choice (top 10% scoring abstracts)</h3></article>
            <article class="award"><div class="when">2013</div><h3>Department of Education GAANN Fellowship Recipient</h3></article>
            <article class="award"><div class="when">—</div><h3>Departmental Award for Outstanding Performance in Organic Chemistry</h3></article>
          </div>
        </section>

        <section class="section">
          <div class="section-head"><h2>Service</h2></div>
          <article class="note"><p>Manuscript reviewer for Nature Genetics, Genetic Epidemiology, and Bioinformatics.</p></article>
        </section>
      </div>

      <aside class="cv-side">
        <h3>Contact</h3>
        <ul>
          <li>Chicago, IL</li>
          <li>US Citizen</li>
          <li>(773) 599-2825</li>
          <li><a href="mailto:joelle.mbatchou@gmail.com">joelle.mbatchou@gmail.com</a></li>
          <li><a href="https://twitter.com/joellembatchou">@joellembatchou</a></li>
          <li><a href="https://www.linkedin.com/in/jmbatchou/">linkedin.com/in/jmbatchou</a></li>
          <li><a href="https://github.com/joellesophya">github.com/joellesophya</a></li>
          <li><a href="https://joellesophya.github.io/">joellesophya.github.io</a></li>
        </ul>
        <h3>Technical skills</h3>
        <div class="skills">
          <span>R</span><span>C/C++</span><span>Bash</span><span>WDL</span><span>docker</span><span>Jupyter</span><span>Python</span>
        </div>
        <p style="margin:1rem 0 0;font-size:0.85rem;color:var(--muted)">CV last updated on 2025-06-05 (source PDF).</p>
      </aside>
    </div>
"""
    return render_shell(
        "CV — Joelle Mbatchou",
        "cv",
        body,
        "Curriculum vitae of Joelle Mbatchou.",
    )


def main():
    pages = {
        DOCS / "index.html": page_home(),
        DOCS / "research.html": page_research(),
        DOCS / "pubs.html": page_pubs(),
        DOCS / "contact.html": page_contact(),
        DOCS / "cv" / "cv.html": page_cv(),
    }
    for path, html in pages.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(html, encoding="utf-8")
        print("wrote", path, f"({len(html)} bytes)")


if __name__ == "__main__":
    main()
