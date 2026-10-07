#!/usr/bin/env python3
"""Generates the static HTML pages of the portfolio (output is plain HTML)."""
import os, textwrap

OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # repo root

EMAIL = "sardorjonumidvich@gmail.com"
PHONE_TEL = "+998931006500"
PHONE = "+998 93 100 65 00"
CV = "files/Sardor_Ismatov_Resume.pdf"
POP_PDF = "files/Uzbekistan_Population_Growth_Report.pdf"
FORM = "https://formspree.io/f/meoavvar"
SITE = "https://portfolio.sardorjonumidvich.workers.dev"  # used for absolute og:image URLs

POP_EMBED = "https://app.powerbi.com/view?r=eyJrIjoiNWJhZWM4MTMtYzA1Zi00YmM3LTg2YmItYjM2ZmEwZDI5Zjk1IiwidCI6ImY3YjQ5MjU0LTMxZmYtNDVkZS04NGJkLTEyMDczYzcyZDMzMSIsImMiOjEwfQ%3D%3D"
RETAIL_EMBED = "https://app.powerbi.com/view?r=eyJrIjoiZTNhMTE0NjctYjQyZS00NDI1LThkNzgtZmE3OGNmNzNlZjAzIiwidCI6ImY3YjQ5MjU0LTMxZmYtNDVkZS04NGJkLTEyMDczYzcyZDMzMSIsImMiOjEwfQ%3D%3D"
BLINKIT = "https://app.powerbi.com/view?r=eyJrIjoiNjljYWExZjgtNThlNS00Y2FlLWJiYmEtZTY1YTNmMjhhNzM1IiwidCI6ImY3YjQ5MjU0LTMxZmYtNDVkZS04NGJkLTEyMDczYzcyZDMzMSIsImMiOjEwfQ%3D%3D"
BANKING = "https://github.com/SardorIsmatov/PortfolioGithub/tree/main/Banking_project"
KPIS = "https://github.com/SardorIsmatov/PortfolioGithub/tree/main/Retail_sales_KPIs_with_SQL"

SOCIALS = [
    ("Telegram", "https://t.me/Sardor_Umidvich", "telegram"),
    ("LinkedIn", "https://www.linkedin.com/in/sardor-ismatov/", "linkedin"),
    ("GitHub", "https://github.com/SardorIsmatov", "github"),
    ("Instagram", "https://www.instagram.com/sardo.me", "instagram"),
]

# ---------------------------------------------------------------- icons
P = {
    "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2.5v2M12 19.5v2M4.6 4.6l1.4 1.4M18 18l1.4 1.4M2.5 12h2M19.5 12h2M4.6 19.4 6 18M18 6l1.4-1.4"/>',
    "moon": '<path d="M20 14.5A8 8 0 0 1 9.5 4 8 8 0 1 0 20 14.5Z"/>',
    "flow": '<rect x="3" y="4" width="6" height="5" rx="1.5"/><rect x="15" y="4" width="6" height="5" rx="1.5"/><rect x="9" y="15" width="6" height="5" rx="1.5"/><path d="M6 9v1.5a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2V9M12 12.5V15"/>',
    "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
    "close": '<path d="M6 6l12 12M18 6 6 18"/>',
    "arrow-right": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "arrow-left": '<path d="M19 12H5M11 6l-6 6 6 6"/>',
    "external": '<path d="M14 4h6v6M20 4l-9 9M18 14v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h5"/>',
    "download": '<path d="M12 4v11M7 10l5 5 5-5M5 20h14"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m4 7 8 6 8-6"/>',
    "phone": '<rect x="7" y="2.5" width="10" height="19" rx="2.5"/><path d="M11 18h2"/>',
    "pin": '<path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21Z"/><circle cx="12" cy="9.5" r="2.5"/>',
    "telegram": '<path d="M21 4 3 11.2l6.3 2.3L12 20l3.4-4.2 4.1 3.2L21 4Z"/><path d="m9.3 13.5 7.2-5.2"/>',
    "linkedin": '<rect x="3" y="3" width="18" height="18" rx="3"/><path d="M8 10.5V16M8 7.5v.01M12 16v-5.5M12 13a2.5 2.5 0 0 1 5 0v3"/>',
    "instagram": '<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><path d="M17.5 6.5h.01"/>',
    "github": '<path d="M9 19c-4.3 1.4-4.3-2.5-6-3m12 5v-3.5c0-1 .1-1.4-.5-2 2.8-.3 5.5-1.4 5.5-6a4.6 4.6 0 0 0-1.3-3.2 4.2 4.2 0 0 0-.1-3.2s-1.1-.3-3.5 1.3a12.3 12.3 0 0 0-6.2 0C6.5 2.8 5.4 3.1 5.4 3.1a4.2 4.2 0 0 0-.1 3.2A4.6 4.6 0 0 0 4 9.5c0 4.6 2.7 5.7 5.5 6-.6.6-.6 1.2-.5 2V21"/>',
    "chart": '<path d="M4 20h16M7 16v-5M12 16V7M17 16v-8"/>',
    "database": '<ellipse cx="12" cy="6" rx="7" ry="3"/><path d="M5 6v12c0 1.7 3.1 3 7 3s7-1.3 7-3V6M5 12c0 1.7 3.1 3 7 3s7-1.3 7-3"/>',
    "code": '<path d="m8 8-4 4 4 4M16 8l4 4-4 4M13.5 6l-3 12"/>',
    "table": '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 9.5h18M3 14.5h18M9 4v16"/>',
    "users": '<circle cx="9" cy="8" r="3.5"/><path d="M3 20a6 6 0 0 1 12 0M16 4.5a3.5 3.5 0 0 1 0 7M21 20a6 6 0 0 0-3.5-5.5"/>',
    "briefcase": '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2M3 12.5h18"/>',
    "cap": '<path d="m2 9 10-5 10 5-10 5-10-5Z"/><path d="M6 11v5c0 1.5 2.7 3 6 3s6-1.5 6-3v-5M22 9v5"/>',
    "award": '<circle cx="12" cy="9" r="6"/><path d="M8.5 14 7 21l5-3 5 3-1.5-7"/>',
    "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>',
    "bulb": '<path d="M9 18h6M10 21h4M12 3a6 6 0 0 0-3.5 10.9c.6.5 1 1.2 1 2V16h5v-.1c0-.8.4-1.5 1-2A6 6 0 0 0 12 3Z"/>',
    "file": '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8l-5-5Z"/><path d="M14 3v5h5M9 13h6M9 17h4"/>',
    "layout": '<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 9v12"/>',
    "send": '<path d="M21 3 10 14M21 3l-7 18-4-7-7-4 18-7Z"/>',
    "home": '<path d="m3 11 9-7 9 7"/><path d="M5 10v10h14V10"/>',
}


def icon(name, cls="icon", label=None):
    aria = f'role="img" aria-label="{label}"' if label else 'aria-hidden="true" focusable="false"'
    return f'<svg class="{cls}" viewBox="0 0 24 24" {aria}>{P[name]}</svg>'


NEWTAB = '<span class="visually-hidden"> (opens in a new tab)</span>'


def ext_link(href, text, cls, ic="external"):
    return (f'<a class="{cls}" href="{href}" target="_blank" rel="noopener noreferrer">{text}'
            f'{NEWTAB}{icon(ic, "icon icon-sm")}</a>')

# ---------------------------------------------------------------- layout


GTAG = """  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-4Y6XTBYX7K"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-4Y6XTBYX7K');
  </script>"""


def head(title, desc, og_image, base=""):
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="author" content="Sardor Ismatov">
  <meta name="theme-color" content="#ffffff">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Sardor Ismatov">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:image" content="{SITE}/{og_image.lstrip('/')}">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="{base}assets/img/favicon.svg" type="image/svg+xml">
  <link rel="icon" href="{base}assets/img/favicon-48.png" sizes="48x48" type="image/png">
  <link rel="apple-touch-icon" href="{base}assets/img/apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&amp;family=JetBrains+Mono:wght@400;500;600&amp;display=swap">
  <link rel="stylesheet" href="{base}assets/css/site.css">
  <script>
    (function () {{
      var d = document.documentElement;
      try {{
        var t = localStorage.getItem("theme");
        if (t === "light" || t === "dark") d.setAttribute("data-theme", t);
      }} catch (e) {{}}
      d.className += " js";
    }})();
  </script>
{GTAG}
  <script src="{base}assets/js/site.js" defer></script>
</head>"""


def header(page, base=""):
    home = base + "index.html" if base == "" else "/"
    if page == "home":
        links = [("Home", "#top", "top"), ("Projects", "#projects", "projects"),
                 ("Experience", "#experience", "experience"), ("About", "#about", "about"),
                 ("Contact", "#contact", "contact")]
    else:
        h = "index.html" if base == "" else "/"
        links = [("Home", h, None), ("Projects", f"{base}All_Projects.html", None),
                 ("Experience", f"{h}#experience", None), ("About", f"{h}#about", None),
                 ("Contact", f"{h}#contact", None)]
    items = []
    for text, href, spy in links:
        attrs = ""
        if spy:
            attrs += f' data-spy="{spy}"'
        if page == "projects" and text == "Projects":
            attrs += ' aria-current="page"'
        items.append(f'          <li><a class="nav-link" href="{href}"{attrs}>{text}</a></li>')
    items = "\n".join(items)
    brand_href = "#top" if page == "home" else home
    return f"""<body>
  <a class="skip-link" href="#main">Skip to content</a>
  <header class="site-header">
    <div class="container header-inner">
      <a class="brand" href="{brand_href}" aria-label="Sardor Ismatov, home">
        <span class="brand-mark" aria-hidden="true">SI</span>
        <span class="brand-name">Sardor Ismatov</span>
        <span class="brand-role">BI Developer</span>
      </a>
      <nav class="site-nav" id="site-nav" aria-label="Main">
        <ul class="nav-list">
{items}
        </ul>
      </nav>
      <button class="icon-btn theme-toggle" type="button" data-theme-toggle aria-label="Toggle colour theme">
        {icon("sun", "icon icon-sun")}{icon("moon", "icon icon-moon")}
      </button>
      <button class="icon-btn menu-toggle" type="button" data-menu-toggle aria-controls="site-nav" aria-expanded="false" aria-label="Open menu">
        {icon("menu", "icon icon-open")}{icon("close", "icon icon-close")}
      </button>
    </div>
  </header>
"""


def socials_list(cls="socials"):
    out = [f'<ul class="{cls}">']
    for name, href, ic in SOCIALS:
        out.append(f'  <li><a class="social-link" href="{href}" target="_blank" rel="noopener noreferrer" aria-label="{name} (opens in a new tab)">{icon(ic)}</a></li>')
    out.append("</ul>")
    return "\n".join(out)


def footer(base=""):
    h = "index.html" if base == "" else "/"
    soc = textwrap.indent(socials_list(), " " * 6)
    return f"""  <footer class="site-footer">
    <div class="container footer-inner">
      <p>&copy; <span data-year>2026</span> Sardor Ismatov &middot; BI Developer, Tashkent</p>
      <ul class="footer-links">
        <li><a href="{base}All_Projects.html">Projects</a></li>
        <li><a href="{base}{CV}">CV (PDF)</a></li>
        <li><a href="mailto:{EMAIL}">Email</a></li>
      </ul>
{soc}
    </div>
  </footer>
</body>
</html>
"""


def picture(name, w, h, alt, eager=False, cls=""):
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    c = f' class="{cls}"' if cls else ""
    return (f'<picture{c}><source srcset="assets/img/{name}.webp" type="image/webp">'
            f'<img src="assets/img/{name}.png" width="{w}" height="{h}" alt="{alt}" {load} decoding="async"></picture>')

# ---------------------------------------------------------------- projects

COVERS = {
    "blinkit": """<svg viewBox="0 0 240 150" aria-hidden="true" focusable="false">
            <rect class="c-fill" x="14" y="12" width="212" height="126" rx="10"/>
            <rect class="c-accent" x="26" y="24" width="56" height="6" rx="3"/>
            <rect class="c-fill" x="26" y="40" width="58" height="26" rx="5"/><rect class="c-accent-soft" x="34" y="49" width="30" height="7" rx="3"/>
            <rect class="c-fill" x="91" y="40" width="58" height="26" rx="5"/><rect class="c-accent-soft" x="99" y="49" width="30" height="7" rx="3"/>
            <rect class="c-fill" x="156" y="40" width="58" height="26" rx="5"/><rect class="c-accent-soft" x="164" y="49" width="30" height="7" rx="3"/>
            <rect class="c-fill" x="26" y="74" width="110" height="52" rx="5"/>
            <path class="c-line" d="M36 112c12-4 18-16 30-14s16 8 28-6 18-10 32-14"/>
            <rect class="c-fill" x="144" y="74" width="70" height="52" rx="5"/>
            <rect class="c-accent" x="154" y="98" width="9" height="20" rx="2"/><rect class="c-accent-soft" x="168" y="88" width="9" height="30" rx="2"/><rect class="c-accent" x="182" y="104" width="9" height="14" rx="2"/><rect class="c-hl" x="196" y="94" width="9" height="24" rx="2"/>
          </svg>""",
    "banking": """<svg viewBox="0 0 240 150" aria-hidden="true" focusable="false">
            <path class="c-link" d="M78 44h28v58h22M78 44h28V30h22M156 30h20v70h-20"/>
            <g><rect class="c-fill" x="22" y="26" width="56" height="62" rx="6"/><rect class="c-accent" x="22" y="26" width="56" height="12" rx="6"/><rect class="c-muted" x="30" y="46" width="34" height="4" rx="2"/><rect class="c-muted" x="30" y="56" width="26" height="4" rx="2"/><rect class="c-muted" x="30" y="66" width="38" height="4" rx="2"/><rect class="c-muted" x="30" y="76" width="22" height="4" rx="2"/></g>
            <g><rect class="c-fill" x="128" y="14" width="56" height="44" rx="6"/><rect class="c-accent" x="128" y="14" width="56" height="12" rx="6"/><rect class="c-muted" x="136" y="34" width="34" height="4" rx="2"/><rect class="c-muted" x="136" y="44" width="24" height="4" rx="2"/></g>
            <g><rect class="c-fill" x="128" y="80" width="56" height="52" rx="6"/><rect class="c-accent" x="128" y="80" width="56" height="12" rx="6"/><rect class="c-muted" x="136" y="100" width="30" height="4" rx="2"/><rect class="c-muted" x="136" y="110" width="38" height="4" rx="2"/><rect class="c-muted" x="136" y="120" width="22" height="4" rx="2"/></g>
            <text class="c-text" x="22" y="124" font-size="15">30 tables</text>
          </svg>""",
    "kpis": """<svg viewBox="0 0 240 150" aria-hidden="true" focusable="false">
            <rect class="c-fill" x="22" y="16" width="196" height="118" rx="10"/>
            <circle class="c-muted" cx="36" cy="29" r="3.5"/><circle class="c-muted" cx="48" cy="29" r="3.5"/><circle class="c-hl" cx="60" cy="29" r="3.5"/>
            <path class="c-link" d="M22 40h196"/>
            <text class="c-text" x="36" y="68" font-size="18">SQL</text>
            <rect class="c-accent-soft" x="80" y="56" width="78" height="7" rx="3.5"/>
            <rect class="c-muted" x="48" y="78" width="96" height="6" rx="3"/>
            <rect class="c-muted" x="48" y="92" width="120" height="6" rx="3"/>
            <rect class="c-accent-soft" x="48" y="106" width="64" height="6" rx="3"/>
            <rect class="c-muted" x="36" y="120" width="52" height="6" rx="3"/>
          </svg>""",
}

PROJECTS = [
    dict(key="population", type="powerbi", label="Power BI", title="Uzbekistan Population Growth Analysis (2010&ndash;2023)",
         desc="Power BI dashboard built on real demographic data, tracking population change across regions, districts and years.",
         tags=["Power BI", "SQL", "Pandas"], img=("uzbekistan-population-dashboard", 1409, 830,
         "Uzbekistan Population Growth dashboard in Power BI with KPI cards, population over time, year-over-year change and the most populated districts"),
         page="Uzbekistan_population.html", dash=POP_EMBED),
    dict(key="retail", type="powerbi", label="Power BI", title="Retail Sales Analysis",
         desc="Power BI sales dashboard on a demo dataset, with drill-through and drill-down into sales, products, stores and customers.",
         tags=["Power BI", "DAX", "SQL", "Python"], img=("retail-sales-dashboard", 1271, 702,
         "Retail Sales Overview dashboard in Power BI with KPI cards, monthly sales, product categories, revenue by state, customer segments and store types"),
         page="Retail_sales_page.html", dash=RETAIL_EMBED),
    dict(key="blinkit", type="powerbi", label="Power BI", title="Blinkit Dashboard",
         desc="An interactive Power BI dashboard for Blinkit, an Indian quick-commerce service.",
         tags=["Power BI"], ext=(BLINKIT, "Open dashboard")),
    dict(key="banking", type="sql", label="SQL", title="Banking Operations Relational Database",
         desc="A relational database of 30 tables modelling banking operations, written in SQL.",
         tags=["SQL", "Relational database"], ext=(BANKING, "View on GitHub")),
    dict(key="kpis", type="sql", label="SQL", title="Retail Sales KPIs for Growth",
         desc="A set of SQL queries that calculate retail sales KPIs for growth.",
         tags=["SQL", "KPIs"], ext=(KPIS, "View on GitHub")),
]


def project_card(p, indent=8, featured=False, hl="h3"):
    chips = "".join(f'<li class="chip">{t}</li>' for t in p["tags"])
    if "page" in p:
        name, w, h, alt = p["img"]
        media = (f'<a class="project-media" href="{p["page"]}" tabindex="-1" aria-hidden="true">'
                 f'{picture(name, w, h, alt)}</a>')
        title = f'<a href="{p["page"]}">{p["title"]}</a>'
        actions = (f'<a class="btn btn-primary btn-sm" href="{p["page"]}">Case study {icon("arrow-right", "icon icon-sm")}</a>'
                   + ext_link(p["dash"], "Open dashboard", "btn btn-ghost btn-sm"))
    else:
        href, text = p["ext"]
        media = (f'<div class="project-media"><div class="cover">{COVERS[p["key"]]}</div>'
                 f'<span class="project-type">{p["label"]}</span></div>')
        title = p["title"]
        actions = ext_link(href, text, "btn btn-secondary btn-sm", "github" if "GitHub" in text else "external")
        if "GitHub" in text:
            actions = (f'<a class="btn btn-secondary btn-sm" href="{href}" target="_blank" rel="noopener noreferrer">'
                       f'{icon("github", "icon icon-sm")}{text}{NEWTAB}{icon("external", "icon icon-sm")}</a>')
    pad = " " * indent
    return f"""{pad}<li class="reveal" data-type="{p['type']}">
{pad}  <article class="project-card">
{pad}    {media}
{pad}    <div class="project-body">
{pad}      <{hl} class="project-title">{title}</{hl}>
{pad}      <p class="project-desc">{p['desc']}</p>
{pad}      <ul class="chips" aria-label="Tools">{chips}</ul>
{pad}      <div class="project-actions">{actions}</div>
{pad}    </div>
{pad}  </article>
{pad}</li>"""

# ---------------------------------------------------------------- index


def build_index():
    featured = "\n".join(project_card(p) for p in PROJECTS[:2])
    contact_items = f"""          <li><a class="contact-item" href="mailto:{EMAIL}"><span class="contact-ico">{icon("mail")}</span><span><small>Email</small><span>{EMAIL}</span></span></a></li>
          <li><a class="contact-item" href="tel:{PHONE_TEL}"><span class="contact-ico">{icon("phone")}</span><span><small>Phone</small><span>{PHONE.replace(" ", "&nbsp;")}</span></span></a></li>
          <li><div class="contact-item"><span class="contact-ico">{icon("pin")}</span><span><small>Location</small><span>Tashkent, Uzbekistan</span></span></div></li>"""

    html = head("Sardor Ismatov | BI Developer &amp; Data Analyst",
                "Sardor Ismatov, BI developer and data analyst at National Bank of Uzbekistan in Tashkent. ETL with Apache Airflow, SQL on Oracle and SAP HANA, Power BI dashboards and projects.",
                "assets/img/sardor-ismatov-og.jpg")
    html += "\n" + header("home")
    html += f"""
  <main id="main">
    <section class="hero" id="top" aria-labelledby="hero-title">
      <div class="container hero-grid">
        <div>
          <p class="eyebrow">Portfolio</p>
          <h1 class="hero-title" id="hero-title">Sardor Ismatov <span class="role"><span class="nowrap">BI Developer</span> <span class="nowrap">&amp; Data Analyst</span></span></h1>
          <p class="hero-lead">I build and run the BI pipeline at National Bank of Uzbekistan: Airflow ETL into an Oracle data warehouse, SQL on Oracle and SAP HANA, and Power BI reports used by about 100 people, including senior management.</p>
          <ul class="chips" aria-label="Main tools">
            <li class="chip chip-accent">Python</li>
            <li class="chip chip-accent">Apache Airflow</li>
            <li class="chip chip-accent">SQL</li>
            <li class="chip chip-accent">Oracle</li>
            <li class="chip chip-accent">SAP HANA</li>
            <li class="chip chip-accent">Power BI</li>
          </ul>
          <div class="hero-actions">
            <a class="btn btn-primary" href="#projects">View projects {icon("arrow-right")}</a>
            <a class="btn btn-secondary" href="{CV}" download="Sardor_Ismatov_Resume.pdf">{icon("download")} Download CV</a>
          </div>
          <ul class="hero-meta">
            <li>{icon("pin", "icon icon-sm")} Tashkent, Uzbekistan</li>
            <li><a href="mailto:{EMAIL}">{icon("mail", "icon icon-sm")} {EMAIL}</a></li>
          </ul>
        </div>
        <div class="portrait">
          <div class="portrait-frame">
            <picture>
              <source srcset="assets/img/sardor-ismatov.webp" type="image/webp">
              <img src="assets/img/sardor-ismatov.jpg" width="960" height="1200" alt="Portrait of Sardor Ismatov" fetchpriority="high" decoding="async">
            </picture>
          </div>
          <div class="portrait-badge">
            <span class="badge-bars" aria-hidden="true"><i></i><i></i><i></i><i></i></span>
            <div><strong>BI Developer</strong><span>National Bank of Uzbekistan &middot; since Jul 2025</span></div>
          </div>
        </div>
      </div>
    </section>

    <div class="container">
      <ul class="facts" aria-label="Quick facts">
        <li class="fact"><span class="fact-value">~100</span><span class="fact-label">report users at NBU</span></li>
        <li class="fact"><span class="fact-value">5</span><span class="fact-label">source systems in the ETL</span></li>
        <li class="fact"><span class="fact-value">3</span><span class="fact-label">public Power BI dashboards</span></li>
        <li class="fact"><span class="fact-value">C1</span><span class="fact-label">IELTS English</span></li>
      </ul>
    </div>

    <section class="section" id="projects" aria-labelledby="projects-title">
      <div class="container">
        <div class="section-head">
          <div>
            <p class="eyebrow">Featured work</p>
            <h2 class="section-title" id="projects-title">Case studies</h2>
            <p class="section-lead">Two Power BI dashboards with a full write-up: the question, the findings and how the report is built.</p>
          </div>
          <a class="btn btn-secondary" href="All_Projects.html">All projects {icon("arrow-right")}</a>
        </div>
        <ul class="project-grid featured">
{featured}
        </ul>
      </div>
    </section>

    <section class="section section-alt" id="skills" aria-labelledby="skills-title">
      <div class="container">
        <div class="section-head">
          <div>
            <p class="eyebrow">Toolkit</p>
            <h2 class="section-title" id="skills-title">Skills</h2>
          </div>
        </div>
        <ul class="skills-grid">
          <li class="card skill-card reveal">
            <div class="skill-head"><span class="skill-icon">{icon("flow")}</span><h3>Data engineering &amp; ETL</h3></div>
            <p>Airflow DAGs in Python that move data from several source systems into an Oracle data warehouse.</p>
            <ul class="chips"><li class="chip">Python</li><li class="chip">Apache Airflow</li><li class="chip">oracledb</li><li class="chip">hdbcli</li><li class="chip">pyodbc</li><li class="chip">SAP Data Services</li></ul>
          </li>
          <li class="card skill-card reveal">
            <div class="skill-head"><span class="skill-icon">{icon("database")}</span><h3>Databases &amp; SQL</h3></div>
            <p>Complex, optimised SQL, data modelling and reporting marts.</p>
            <ul class="chips"><li class="chip">Oracle</li><li class="chip">SAP HANA</li><li class="chip">SQL Server</li><li class="chip">PostgreSQL</li><li class="chip">Data modelling</li></ul>
          </li>
          <li class="card skill-card reveal">
            <div class="skill-head"><span class="skill-icon">{icon("chart")}</span><h3>BI &amp; reporting</h3></div>
            <p>Power BI dashboards and DAX measures, published to the business on Power BI Report Server.</p>
            <ul class="chips"><li class="chip">Power BI</li><li class="chip">DAX</li><li class="chip">Power BI Report Server</li><li class="chip">Drill-through</li><li class="chip">Excel</li></ul>
          </li>
          <li class="card skill-card reveal">
            <div class="skill-head"><span class="skill-icon">{icon("code")}</span><h3>Analysis in Python</h3></div>
            <p>Exploratory analysis and charts, including data pulled from APIs.</p>
            <ul class="chips"><li class="chip">Pandas</li><li class="chip">NumPy</li><li class="chip">Matplotlib</li><li class="chip">Seaborn</li><li class="chip">API requests</li></ul>
          </li>
        </ul>
      </div>
    </section>

    <section class="section" id="experience" aria-labelledby="experience-title">
      <div class="container">
        <div class="section-head">
          <div>
            <p class="eyebrow">Background</p>
            <h2 class="section-title" id="experience-title">Experience &amp; education</h2>
          </div>
          <a class="btn btn-secondary" href="{CV}" download="Sardor_Ismatov_Resume.pdf">{icon("download")} Download CV</a>
        </div>
        <div class="timeline-grid">
          <div>
            <h3 class="timeline-heading">{icon("briefcase")} Experience</h3>
            <ol class="timeline">
              <li class="tl-item is-current reveal">
                <article class="card tl-card">
                  <div class="tl-top"><span class="tl-date">Jul 2025 &ndash; Present<span class="tl-now">Current</span></span><span class="tl-date">Tashkent</span></div>
                  <h4>BI Developer</h4>
                  <p class="tl-org"><a href="https://nbu.uz/" target="_blank" rel="noopener noreferrer">National Bank of Uzbekistan (NBU){NEWTAB}</a></p>
                  <p class="tl-text">I build and maintain the bank&rsquo;s BI pipeline end to end, working largely solo across every layer.</p>
                  <ul class="tl-list">
                    <li><strong>ETL &amp; orchestration:</strong> design and run Apache Airflow DAGs in Python (oracledb, hdbcli, pyodbc) that move data from core banking (Oracle), SAP HANA, SQL Server, PostgreSQL and SAP Data Services into an Oracle data warehouse.</li>
                    <li><strong>Data modelling &amp; SQL:</strong> write and optimise complex SQL on Oracle and SAP HANA, including migrating HANA calculation views to Oracle and building reporting marts for loans, interest income and liquidity.</li>
                    <li><strong>Reporting:</strong> Power BI dashboards and DAX measures for the credit portfolio, loan disbursement, regulatory liquidity (VLA/HLA), branch financial monitoring and market benchmarking.</li>
                    <li><strong>Platform administration:</strong> deployed and administer Power BI Report Server for ~100 users, including senior management, and built a custom web tool for managing report permissions.</li>
                  </ul>
                  <ul class="chips tl-stack" aria-label="Stack"><li class="chip">Python</li><li class="chip">Apache Airflow</li><li class="chip">Oracle</li><li class="chip">SAP HANA</li><li class="chip">SQL Server</li><li class="chip">Power BI / DAX</li><li class="chip">PBIRS</li></ul>
                </article>
              </li>
              <li class="tl-item reveal">
                <article class="card tl-card">
                  <div class="tl-top"><span class="tl-date">Mar 2025 &ndash; Jul 2025</span><span class="tl-date">Tashkent</span></div>
                  <h4>Data Analyst (Support Teacher)</h4>
                  <p class="tl-org"><a href="https://it-market.uz/company/5Cjm2RyaagiFPc8zuK7Lsg/" target="_blank" rel="noopener noreferrer">MAAB Innovation{NEWTAB}</a></p>
                  <ul class="tl-list">
                    <li>Supported students in data analytics projects with SQL, Excel, Python (Pandas, Seaborn) and Power BI.</li>
                    <li>Debugged code, reviewed submissions and gave feedback on data cleaning and visualization.</li>
                  </ul>
                </article>
              </li>
              <li class="tl-item reveal">
                <article class="card tl-card">
                  <div class="tl-top"><span class="tl-date">Aug 2023 &ndash; Nov 2023</span><span class="tl-date">Bukhara</span></div>
                  <h4>Intern</h4>
                  <p class="tl-org"><a href="https://brb.uz/" target="_blank" rel="noopener noreferrer">Biznesni Rivojlantirish Banki{NEWTAB}</a> &middot; Karakul region bank services office</p>
                  <ul class="tl-list">
                    <li>Tracked loan repayment progress in Excel and contacted 400+ loan defaulters by phone, contributing to a 60% faster repayment process.</li>
                    <li>Advised 200+ customers on deposits, interest rates and loans (customer satisfaction +80%).</li>
                    <li>Managed 80+ customer accounts in iABS.</li>
                    <li>Retrieved 120+ ATM cards (customer satisfaction +70%).</li>
                  </ul>
                </article>
              </li>
              <li class="tl-item reveal">
                <article class="card tl-card">
                  <div class="tl-top"><span class="tl-date">Jan 2023 &ndash; Mar 2023</span><span class="tl-date">Bukhara</span></div>
                  <h4>Intern</h4>
                  <p class="tl-org"><a href="https://brb.uz/" target="_blank" rel="noopener noreferrer">Biznesni Rivojlantirish Banki{NEWTAB}</a> &middot; Bukhara city branch</p>
                  <ul class="tl-list">
                    <li>Organised the document archive and kept Excel logs of customer interactions and loan statuses.</li>
                    <li>Assisted 400+ customers, resolving issues twice as fast.</li>
                    <li>Contacted 200+ loan defaulters, speeding up the repayment process by 40%.</li>
                    <li>Joined field visits on problem loans (+30% efficiency).</li>
                  </ul>
                </article>
              </li>
            </ol>
          </div>
          <div>
            <h3 class="timeline-heading">{icon("cap")} Education</h3>
            <ol class="timeline">
              <li class="tl-item reveal">
                <article class="card tl-card">
                  <div class="tl-top"><span class="tl-date">Nov 2024 &ndash; Feb 2025</span></div>
                  <h4>Data Analytics trainee</h4>
                  <p class="tl-org"><a href="https://academy.maab.uz/" target="_blank" rel="noopener noreferrer">MAAB Academy{NEWTAB}</a></p>
                  <p class="tl-text">Training in SQL, Python and Power BI.</p>
                </article>
              </li>
              <li class="tl-item reveal">
                <article class="card tl-card">
                  <div class="tl-top"><span class="tl-date">Sep 2019 &ndash; Jul 2023</span></div>
                  <h4>Economics / Banking</h4>
                  <p class="tl-org"><a href="https://www.sies.uz/" target="_blank" rel="noopener noreferrer">Samarkand Institute of Economics and Service{NEWTAB}</a></p>
                  <p class="tl-text">Focused on finance, banking operations and economics.</p>
                </article>
              </li>
            </ol>
          </div>
        </div>
      </div>
    </section>

    <section class="section section-alt" id="about" aria-labelledby="about-title">
      <div class="container">
        <div class="section-head">
          <div>
            <p class="eyebrow">About</p>
            <h2 class="section-title" id="about-title">About me</h2>
          </div>
        </div>
        <div class="about-grid">
          <div class="about-text">
            <p>I&rsquo;m a BI developer and data analyst with a background in banking and finance. Since July 2025 I&rsquo;ve been building the BI pipeline at National Bank of Uzbekistan: ETL in Apache Airflow, SQL on Oracle and SAP HANA, and Power BI reporting for around 100 users, including senior management.</p>
            <p>My journey started with a Bachelor&rsquo;s in Banking, followed by banking internships and a role as a support teacher in data analytics. I enjoy solving problems, building dashboards and helping others understand data better.</p>
            <div class="hero-actions">
              <a class="btn btn-primary" href="#contact">Get in touch {icon("arrow-right")}</a>
              <a class="btn btn-secondary" href="{CV}" download="Sardor_Ismatov_Resume.pdf">{icon("download")} Download CV</a>
            </div>
          </div>
          <div class="about-side">
            <div class="card info-card reveal">
              <h3>{icon("award")} Certificates</h3>
              <ul class="cert-list">
                <li><div><strong>IELTS C1</strong></div><span class="year">2023</span></li>
                <li><div><strong>Microsoft Excel &ndash; Excel from Beginner to Advanced</strong><span>Udemy</span></div><span class="year">2024</span></li>
                <li><div><strong>Google Data Analytics: Foundations</strong><span>Coursera</span></div><span class="year">2024</span></li>
              </ul>
            </div>
            <div class="card info-card reveal">
              <h3>{icon("globe")} Languages</h3>
              <ul class="lang-list">
                <li><span>Uzbek</span><span class="level">Native</span></li>
                <li><span>English</span><span class="level">Professional</span></li>
                <li><span>Russian</span><span class="level">Intermediate</span></li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="section" id="contact" aria-labelledby="contact-title">
      <div class="container">
        <div class="section-head">
          <div>
            <p class="eyebrow">Contact</p>
            <h2 class="section-title" id="contact-title">Get in touch</h2>
            <p class="section-lead">Have a question or an opportunity? Send a message or reach me directly.</p>
          </div>
        </div>
        <div class="contact-grid">
          <form class="card form-card" action="{FORM}" method="POST" data-contact-form data-email="{EMAIL}">
            <div class="form-grid">
              <div class="field">
                <label for="cf-name">Name</label>
                <input id="cf-name" name="name" type="text" autocomplete="name" required>
              </div>
              <div class="field">
                <label for="cf-email">Email</label>
                <input id="cf-email" name="email" type="email" autocomplete="email" required>
              </div>
              <div class="field full">
                <label for="cf-phone">Phone <span class="opt">(optional)</span></label>
                <input id="cf-phone" name="phone" type="tel" autocomplete="tel" inputmode="tel">
              </div>
              <div class="field full">
                <label for="cf-message">Message</label>
                <textarea id="cf-message" name="message" rows="6" required></textarea>
              </div>
            </div>
            <div class="hp" aria-hidden="true">
              <label for="cf-gotcha">Leave this field empty</label>
              <input id="cf-gotcha" type="text" name="_gotcha" tabindex="-1" autocomplete="off">
            </div>
            <div class="form-foot">
              <p class="form-note">All fields except phone are required.</p>
              <button class="btn btn-primary" type="submit">{icon("send")} Send message</button>
            </div>
            <div class="form-status" data-form-status role="status" aria-live="polite" hidden></div>
          </form>
          <div class="card details-card">
            <h3>Contact details</h3>
            <ul class="contact-list">
{contact_items}
            </ul>
{textwrap.indent(socials_list(), " " * 12)}
          </div>
        </div>
      </div>
    </section>
  </main>

"""
    html += footer()
    return html

# ---------------------------------------------------------------- all projects


def build_all():
    cards = "\n".join(project_card(p, hl="h2") for p in PROJECTS)
    n_pbi = sum(1 for p in PROJECTS if p["type"] == "powerbi")
    n_sql = sum(1 for p in PROJECTS if p["type"] == "sql")
    html = head("Projects | Sardor Ismatov, BI Developer",
                "All data analytics projects by Sardor Ismatov: Power BI dashboards on population and retail sales data, and SQL projects.",
                "assets/img/uzbekistan-population-dashboard.png")
    html += "\n" + header("projects")
    html += f"""
  <main id="main">
    <div class="container page-head">
      <nav class="breadcrumb" aria-label="Breadcrumb">
        <ol>
          <li><a href="index.html">Home</a></li>
          <li><span aria-current="page">Projects</span></li>
        </ol>
      </nav>
      <h1 class="page-title">Projects</h1>
      <p class="page-lead">Power BI dashboards and SQL work. The first two have full case studies; the others open the dashboard or the code on GitHub.</p>
    </div>

    <section class="container" aria-label="Project list" style="padding-bottom: clamp(56px, 8vw, 96px);">
      <div class="filters" data-filters role="group" aria-label="Filter projects" hidden>
        <button class="filter-btn" type="button" data-filter="all" aria-pressed="true">All <span class="count">{len(PROJECTS)}</span></button>
        <button class="filter-btn" type="button" data-filter="powerbi" aria-pressed="false">{icon("chart", "icon icon-sm")} Power BI <span class="count">{n_pbi}</span></button>
        <button class="filter-btn" type="button" data-filter="sql" aria-pressed="false">{icon("database", "icon icon-sm")} SQL <span class="count">{n_sql}</span></button>
      </div>
      <p class="visually-hidden" data-filter-status aria-live="polite"></p>
      <ul class="project-grid">
{cards}
      </ul>
    </section>
  </main>

"""
    html += footer()
    return html

# ---------------------------------------------------------------- case studies


def build_case(c):
    kpis = "\n".join(
        f'          <li class="kpi"><span class="kpi-value">{v}</span><span class="kpi-label">{l}</span></li>'
        for v, l in c["kpis"])
    name, w, h, alt = c["img"]
    links = [f'<li><a href="{c["embed"]}" target="_blank" rel="noopener noreferrer">{icon("layout")} Interactive dashboard{NEWTAB}{icon("external", "icon icon-sm ext")}</a></li>']
    if c.get("pdf"):
        links.append(f'<li><a href="{c["pdf"]}">{icon("file")} PDF report</a></li>')
    links.append(f'<li><a href="All_Projects.html">{icon("layout")} All projects</a></li>')
    links = "\n".join("              " + l for l in links)
    tip = c.get("tip", "")
    pdf_btn = (f'<a class="btn btn-ghost btn-sm" href="{c["pdf"]}">{icon("file", "icon icon-sm")} PDF report</a>' if c.get("pdf") else "")
    prev_html = (f'<a class="prev" href="{c["prev"][0]}"><small>{icon("arrow-left", "icon icon-sm")} Previous</small><strong>{c["prev"][1]}</strong></a>'
                 if c.get("prev") else "")
    next_html = (f'<a class="next" href="{c["next"][0]}"><small>Next {icon("arrow-right", "icon icon-sm")}</small><strong>{c["next"][1]}</strong></a>'
                 if c.get("next") else "")

    html = head(c["doc_title"], c["meta_desc"], f"assets/img/{name}.png")
    html += "\n" + header("projects")
    html += f"""
  <main id="main">
    <div class="container page-head">
      <nav class="breadcrumb" aria-label="Breadcrumb">
        <ol>
          <li><a href="index.html">Home</a></li>
          <li><a href="All_Projects.html">Projects</a></li>
          <li><span aria-current="page">{c["crumb"]}</span></li>
        </ol>
      </nav>
      <p class="eyebrow" style="margin-top: 24px;">Case study &middot; Power BI</p>
      <h1 class="page-title">{c["title"]}</h1>
      <p class="page-lead">{c["lead"]}</p>
      <dl class="meta-row">
        <div><dt>Category</dt><dd>Data Analysis</dd></div>
        <div><dt>Type</dt><dd>Academic project</dd></div>
        <div><dt>Date</dt><dd>March 2025</dd></div>
        <div><dt>Tools</dt><dd>{c["tools"]}</dd></div>
      </dl>
    </div>

    <section class="container" aria-labelledby="kpi-title">
      <h2 class="visually-hidden" id="kpi-title">Key figures</h2>
      <ul class="kpis">
{kpis}
      </ul>
    </section>

    <section class="container dash" id="dashboard" aria-labelledby="dash-title">
      <div class="dash-bar">
        <h2 id="dash-title">{icon("layout")} Interactive dashboard</h2>
        <div class="dash-links">
          {pdf_btn}{ext_link(c["embed"], "Open in new tab", "btn btn-ghost btn-sm")}
        </div>
      </div>
      <div class="dash-frame">
        <div class="dash-embed" style="background-image: url('assets/img/{name}.webp');">
          <iframe title="{c["iframe_title"]}" data-src="{c["embed"]}" loading="lazy" allowfullscreen></iframe>
        </div>
        <div class="dash-poster">
          {picture(name, w, h, alt, eager=True)}
          <div class="dash-poster-cta">
            <p>Screenshot of the report. The live version is interactive.</p>
            {ext_link(c["embed"], "Open interactive dashboard", "btn btn-primary")}
          </div>
        </div>
      </div>
{tip}
    </section>

    <div class="container case-layout">
      <article class="prose">
{c["body"]}
      </article>
      <aside class="case-aside" aria-label="Project details">
        <div class="card aside-card aside-details">
          <h2>Project details</h2>
          <dl class="aside-dl">
            <div><dt>Category</dt><dd>Data Analysis</dd></div>
            <div><dt>Type</dt><dd>Academic project</dd></div>
            <div><dt>Date</dt><dd>March 2025</dd></div>
            <div><dt>Tools</dt><dd>{c["tools"]}</dd></div>
          </dl>
        </div>
        <div class="card aside-card">
          <h2>Links</h2>
          <ul class="aside-links">
{links}
          </ul>
        </div>
      </aside>
    </div>

    <nav class="container pager" aria-label="More projects">
      {prev_html}
      {next_html}
    </nav>
  </main>

"""
    html += footer()
    return html


POP_BODY = """        <section>
          <h2>Project overview</h2>
          <p>Over the past 13 years, Uzbekistan has witnessed steady and notable population growth. Based on the provided demographic dashboard, the analysis covers the overall population increase from 2010 to 2023, year-over-year changes, and regional/district-level distribution. This analysis is crucial for understanding demographic trends and informing strategic decisions.</p>
        </section>

        <section>
          <h2>Key findings</h2>
          <p>From 2010 to 2023, Uzbekistan&rsquo;s population increased by <span class="num">10.68 million</span> people. This growth occurred across 12 regions, the Republic of Karakalpakstan, and the city of Tashkent &mdash; making up a total of <span class="num">14</span> administrative divisions. The growth was recorded across <span class="num">206</span> districts, with an overall increase of <span class="num">42.99%</span> during this period. The average annual growth (YoY) stood at <span class="num">3.31%</span>, reflecting a stable and healthy demographic expansion.</p>
        </section>

        <section>
          <h2>Year-on-year change dynamics</h2>
          <p>The annual growth rates varied over time. Particularly high growth was observed in 2013 (<span class="num">8.70%</span>) and 2019 (<span class="num">7.41%</span>). However, some years also showed a decline in growth, such as 2011 (<span class="num">-1.89%</span>), 2016 (<span class="num">-1.09%</span>), and 2017 (<span class="num">-1.47%</span>). These drops might be attributed to factors like external migration, economic fluctuations, or differences in statistical methodology. In 2023, the population grew by <span class="num">3.19%</span>, continuing the positive growth trend in recent years.</p>
        </section>

        <section>
          <h2>Regional breakdown and distribution</h2>
          <p>The dashboard highlights Samarkand region as an example, with a population of <span class="num">1.297 million</span>. Among its districts, Urgut (<span class="num">194K</span>), Samarkand city (<span class="num">140K</span>), and Pastdargom (<span class="num">119K</span>) are the most populated. Additionally, regions like Fergana (<span class="num">1.15M</span>) and Kashkadarya (<span class="num">1.13M</span>) also have substantial population numbers, indicating their demographic and economic significance.</p>
        </section>

        <section>
          <h2>Top 5 most populated districts</h2>
          <p>Across the entire country, the top 5 most populated districts are:</p>
          <ol>
            <li>Namangan city &ndash; <span class="num">212K</span></li>
            <li>Urgut district &ndash; <span class="num">194K</span></li>
            <li>Chiroqchi district &ndash; <span class="num">163K</span></li>
            <li>Andijan city &ndash; <span class="num">143K</span></li>
            <li>Denau district &ndash; <span class="num">141K</span></li>
          </ol>
        </section>

        <section>
          <h2>Conclusion</h2>
          <p>The analysis clearly shows that Uzbekistan has experienced significant population growth from 2010 to 2023. This demographic increase puts pressure on infrastructure, education, healthcare, and housing. Regions and densely populated districts in particular require focused social and economic policies. With the growth expected to continue, such demographic insights will play a vital role in planning, investment decisions, and the formulation of national development strategies.</p>
        </section>"""


def barlist(rows, maxv):
    out = ['          <ul class="barlist">']
    for name, v, label in rows:
        pct = round(v / maxv * 100, 1)
        out.append(f'            <li><span class="bl-name">{name}</span><span class="bl-track" aria-hidden="true"><span class="bl-fill" style="width: {pct}%"></span></span><span class="bl-val">{label}</span></li>')
    out.append("          </ul>")
    return "\n".join(out)


CATS = [("Electronics &amp; Gadgets", 0.79, "$0.79M"), ("Home &amp; Living", 0.58, "$0.58M"),
        ("Sports &amp; Outdoor", 0.47, "$0.47M"), ("Apparel &amp; Fashion", 0.40, "$0.40M"),
        ("Tools &amp; Hardware", 0.27, "$0.27M"), ("Toys &amp; Games", 0.17, "$0.17M"),
        ("Stationery &amp; Office", 0.14, "$0.14M")]

RETAIL_BODY = f"""        <section>
          <h2>Project overview</h2>
          <p>This Retail Sales Dashboard provides a comprehensive view of overall business performance in the retail sector. The analysis includes key performance metrics, monthly sales trends, product category breakdowns, store type comparisons, and customer segmentation. The dashboard is designed to help businesses understand their growth, optimize strategies, and make informed decisions based on historical and current sales data.</p>
        </section>

        <section>
          <h2>Key findings</h2>

          <h3>Total sales &amp; profitability</h3>
          <p>The business achieved <span class="num">$3.01 million</span> in total sales and <span class="num">$858.8K</span> in profit, resulting in a profit margin of <span class="num">28.51%</span> &mdash; indicating healthy profitability.</p>

          <h3>Customer &amp; order metrics</h3>
          <p>The dataset includes <span class="num">1,500</span> customers and approximately <span class="num">27,000</span> orders, reflecting a solid and active customer base.</p>

          <h3>Monthly sales trends (2023&ndash;2025)</h3>
          <p>The sales trend chart shows seasonal peaks in November, likely due to holiday shopping. There is a consistent year-over-year increase with some expected fluctuations, confirming long-term business growth.</p>

          <h3>Product category breakdown</h3>
          <p>Electronics &amp; Gadgets lead total sales, followed by Home &amp; Living, Sports &amp; Outdoor and Apparel &amp; Fashion. Sales by category, as shown on the dashboard:</p>
{barlist(CATS, 0.79)}

          <h3>Store type comparison</h3>
          <p>Sales distribution by channel shows:</p>
          <ul>
            <li>Outlet stores dominate with <span class="num">$2.0M</span> in revenue</li>
            <li>Online sales &ndash; <span class="num">$0.7M</span></li>
            <li>Flagship stores &ndash; a smaller share</li>
          </ul>

          <h3>Customer segmentation</h3>
          <p>Loyalty-based customer breakdown:</p>
          <ul>
            <li>New customers &ndash; <span class="num">52.2%</span></li>
            <li>Regular customers &ndash; <span class="num">37.53%</span></li>
            <li>VIP customers &ndash; <span class="num">10.27%</span></li>
          </ul>

          <h3>Geographic sales distribution</h3>
          <p>A choropleth map of the U.S. reveals stronger sales performance in the Midwest and East Coast, suggesting potential regions for expansion or focused marketing.</p>
        </section>

        <section>
          <h2>Conclusion</h2>
          <p>The analysis provides a 360-degree view of the business&rsquo;s retail performance. The consistent growth in sales, combined with customer segmentation and product breakdowns, empowers the company to make strategic decisions on inventory, marketing, and store operations. Seasonal insights and regional differences also provide a competitive edge in resource allocation and customer targeting.</p>
        </section>

        <section>
          <h2>Dashboard design &amp; interactivity</h2>
          <p>To ensure a user-friendly and insightful experience, I designed this dashboard with the following interactive features:</p>
          <ul>
            <li><strong>One main overview page:</strong> all key metrics and summaries are shown on the main page to provide a high-level snapshot of business performance.</li>
            <li><strong>Drill-through functionality:</strong> the main dashboard enables users to right-click and navigate to four detailed drill-through pages focused on Sales Performance, Product Insights, Store Performance and Customer Analysis.</li>
            <li><strong>Drill-down</strong> functionality (e.g., Year &rarr; Month) in trend visuals.</li>
            <li><strong>Custom DAX measures and calculated columns</strong> for calculating profit margin, YoY growth, and segmentation.</li>
            <li>Clean, responsive layout with tooltips for an enhanced user experience.</li>
          </ul>
        </section>"""

RETAIL_TIP = f"""      <div class="callout">
        {icon("bulb")}
        <div>
          <strong>Quick tip: the best way to explore is the drill-through feature</strong>
          <ol>
            <li>Right-click on anything that looks interesting.</li>
            <li>Choose &ldquo;Drill through&rdquo;.</li>
            <li>Pick where you want to go.</li>
          </ol>
        </div>
      </div>"""

CASES = {
    "Uzbekistan_population.html": dict(
        doc_title="Uzbekistan Population Growth Analysis (2010&ndash;2023) | Sardor Ismatov",
        meta_desc="Power BI case study by Sardor Ismatov: Uzbekistan's population growth from 2010 to 2023 across 14 administrative divisions and 206 districts.",
        crumb="Uzbekistan Population Growth",
        title="Uzbekistan Population Growth Analysis <span style=\"white-space: nowrap\">(2010&ndash;2023)</span>",
        lead="A data visualization dashboard in Power BI built on real demographic data: overall growth, year-over-year change and the regional and district-level distribution.",
        tools="SQL, Power BI, Pandas",
        kpis=[("+10.68M", "Population growth, <span style=\"white-space: nowrap\">2010&ndash;2023</span>"), ("+42.99%", "Overall increase"),
              ("3.31%", "Average annual growth (YoY)"), ("14", "Administrative divisions"), ("206", "Districts")],
        img=PROJECTS[0]["img"], embed=POP_EMBED,
        iframe_title="Uzbekistan Population Growth (2010-2023), interactive Power BI dashboard",
        pdf=POP_PDF, body=POP_BODY,
        next=("Retail_sales_page.html", "Retail Sales Analysis"),
        prev=("All_Projects.html", "All projects"),
    ),
    "Retail_sales_page.html": dict(
        doc_title="Retail Sales Analysis | Sardor Ismatov",
        meta_desc="Power BI case study by Sardor Ismatov: a retail sales dashboard with drill-through and drill-down covering sales, profit, categories, store types and customer segments.",
        crumb="Retail Sales Analysis",
        title="Retail Sales Analysis",
        lead="A data visualization dashboard in Power BI (demo dataset) giving an overview of company sales performance, with drill-through and drill-down for detail.",
        tools="SQL, Power BI, Python",
        kpis=[("$3.01M", "Total sales"), ("$858.8K", "Profit"), ("28.51%", "Profit margin"),
              ("1,500", "Customers"), ("~27K", "Orders")],
        img=PROJECTS[1]["img"], embed=RETAIL_EMBED,
        iframe_title="Retail Sales Overview, interactive Power BI dashboard",
        body=RETAIL_BODY, tip=RETAIL_TIP,
        prev=("Uzbekistan_population.html", "Uzbekistan Population Growth Analysis"),
        next=("All_Projects.html", "All projects"),
    ),
}

# ---------------------------------------------------------------- 404


def build_404():
    html = head("Page not found | Sardor Ismatov",
                "This page does not exist. Go back to the portfolio of Sardor Ismatov, BI developer and data analyst.",
                "assets/img/sardor-ismatov-og.jpg", base="/")
    html += "\n" + header("404", base="/")
    html += f"""
  <main id="main" class="container notfound">
    <div>
      <p class="notfound-code">404</p>
      <h1>This page could not be found</h1>
      <p>The link may be old or mistyped. Everything on the site is still reachable from the home page and the project list.</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="/">{icon("home")} Home</a>
        <a class="btn btn-secondary" href="/All_Projects.html">All projects {icon("arrow-right")}</a>
      </div>
    </div>
  </main>

"""
    html += footer(base="/")
    return html


def write(name, html):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(html)


write("index.html", build_index())
write("All_Projects.html", build_all())
for fname, c in CASES.items():
    write(fname, build_case(c))
write("404.html", build_404())
print("ok")
