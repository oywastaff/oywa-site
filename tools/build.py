#!/usr/bin/env python3
"""Genera le pagine HTML del sito OYWA nelle quattro lingue.

Uso, dalla cartella del sito:
    python3 tools/build.py          # rigenera le pagine e la sitemap
    python3 tools/build.py --og     # rigenera anche le immagini di anteprima (serve macOS)

I testi sono in tools/content.py (interfaccia) e tools/legal.py (pagine legali).
Lo stile è in style.css, gli script in main.js: non vengono generati.
"""

import html
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from content import COMMON, FEATURES, GALLERY, HOME, LANGS, SLUGS  # noqa: E402
from legal import COOKIE, PRIVACY, TERMS, TOC, TRANSLATION_NOTE, UPDATED  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://www.oywa.it"
EMAIL = "staff@oywa.it"
ASSET_VERSION = "4"
LASTMOD = "2026-10-11"

ICONS = {
    "check": '<path d="M5 12l5 5L20 7"/>',
    "send": '<path d="M22 2 11 13"/><path d="M22 2 15 22l-4-9-9-4 20-7z"/>',
    "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/>',
    "globe": '<circle cx="12" cy="12" r="10"/><path d="M2 12h20"/><path d="M12 2a15 15 0 0 1 0 20 15 15 0 0 1 0-20z"/>',
    "star": '<path d="m12 2 3 6.5 7 .8-5.2 4.8 1.5 7L12 17.6 5.7 21l1.5-7L2 9.3l7-.8z"/>',
    "phone": '<rect x="5" y="2" width="14" height="20" rx="2"/><path d="M12 18h.01"/>',
    "ban": '<circle cx="12" cy="12" r="10"/><path d="m4.9 4.9 14.2 14.2"/>',
    "download": '<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><path d="m7 10 5 5 5-5"/><path d="M12 15V3"/>',
    "upload": '<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><path d="m17 8-5-5-5 5"/><path d="M12 3v12"/>',
    "file": '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6"/><path d="M8 13h8M8 17h5"/>',
    "people": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/>',
    "trash": '<path d="M3 6h18"/><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6"/><path d="M8 6V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/><path d="M10 11v6M14 11v6"/>',
    "lang": '<path d="m5 8 6 6"/><path d="m4 14 6-6 2-3"/><path d="M2 5h12"/><path d="M7 2h1"/><path d="m22 22-5-10-5 10"/><path d="M14 18h6"/>',
    "prev": '<path d="m15 18-6-6 6-6"/>',
    "next": '<path d="m9 18 6-6-6-6"/>',
}

CURRENT = ' aria-current="true"'

CAT_COLORS = ["citta", "hotel", "ristorante", "bar", "colazione", "gelato", "poi", "attrazione", "aereo"]


def icon(name, width="2"):
    return (f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{width}" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>')


def esc(text):
    return html.escape(text, quote=True)


def url(lang, page):
    return LANGS[lang]["prefix"] + SLUGS[page][lang]


def out_path(lang, page):
    rel = url(lang, page).lstrip("/")
    if rel == "" or rel.endswith("/"):
        rel += "index.html"
    return ROOT / rel


def mailto(lang):
    subject = COMMON[lang]["mail_subject"].replace(" ", "%20")
    return f"mailto:{EMAIL}?subject={subject}"


# ---------------------------------------------------------------------------
# Parti comuni
# ---------------------------------------------------------------------------

def redirect_script(page):
    """Solo sulle pagine italiane (lingua predefinita): porta alla lingua del
    browser, o a quella scelta in passato dal menu. I crawler non vengono
    reindirizzati, così Google indicizza ogni lingua al suo indirizzo."""
    targets = {lang: url(lang, page) for lang in LANGS if lang != "it"}
    return (
        "<script>(function(){var m=" + json.dumps(targets) + ";"
        "if(/bot|crawl|spider|slurp|lighthouse|preview/i.test(navigator.userAgent))return;"
        "var s=null;try{s=localStorage.getItem('oywa-lang')}catch(e){}"
        "var l=s||((navigator.languages&&navigator.languages[0])||navigator.language||'it').slice(0,2).toLowerCase();"
        "if(!s&&l!=='it'&&!m[l])l='en';"
        "if(l!=='it'&&m[l])location.replace(m[l]+location.hash);})();</script>\n"
    )


def head(lang, page, title, desc, og_title, extra=""):
    canonical = SITE + url(lang, page)
    alternates = "".join(
        f'<link rel="alternate" hreflang="{LANGS[l]["html"]}" href="{SITE + url(l, page)}">\n' for l in LANGS
    ) + f'<link rel="alternate" hreflang="x-default" href="{SITE + url("it", page)}">\n'
    image = f"{SITE}/assets/og-image-{lang}.jpg"
    v = ASSET_VERSION
    return f"""<!doctype html>
<html lang="{LANGS[lang]["html"]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
{redirect_script(page) if lang == "it" else ""}<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="canonical" href="{canonical}">
{alternates}<meta property="og:type" content="website">
<meta property="og:site_name" content="OYWA">
<meta property="og:locale" content="{LANGS[lang]["og"]}">
<meta property="og:url" content="{canonical}">
<meta property="og:title" content="{esc(og_title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:image" content="{image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(og_title)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="{image}">
<meta name="theme-color" content="#FAF3E6">
<link rel="icon" href="/assets/app_icon.png">
<link rel="apple-touch-icon" href="/assets/app_icon.png">
<link rel="preload" href="/assets/fonts/archivo-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/inter-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/fonts/fonts.css?v={v}">
<link rel="stylesheet" href="/style.css?v={v}">
{extra}</head>
<body>
<a class="skip" href="#main">{esc(COMMON[lang]["skip"])}</a>
"""


def lang_switcher(lang, page):
    c = COMMON[lang]
    items = "".join(
        f'<li><a href="{url(l, page)}" hreflang="{LANGS[l]["html"]}" lang="{LANGS[l]["html"]}" data-lang="{l}"'
        f'{CURRENT if l == lang else ""}>{LANGS[l]["name"]} <span>{l.upper()}</span></a></li>'
        for l in LANGS
    )
    return (f'<details class="lang"><summary aria-label="{esc(c["lang_label"])}">{icon("globe")}{lang.upper()}</summary>'
            f'<ul>{items}</ul></details>')


def header(lang, page):
    c = COMMON[lang]

    def link(target, label, cls=""):
        current = ' aria-current="page"' if target == page else ""
        klass = f' class="{cls}"' if cls else ""
        return f'<a{klass} href="{url(lang, target)}"{current}>{esc(label)}</a>'

    return f"""<header class="site-header"><div class="wrap">
  <a class="brand" href="{url(lang, "home")}" aria-label="{esc(c["brand_label"])}"><img src="/assets/app_icon.png" alt="">OYWA</a>
  <nav class="nav" aria-label="Menu">
    {link("home", c["nav_home"], "nav-home")}
    {link("features", c["nav_features"])}
    {link("privacy", c["nav_privacy"], "nav-privacy")}
    {lang_switcher(lang, page)}
    <a class="btn" href="{mailto(lang)}">{esc(c["cta_beta"])}</a>
  </nav>
</div></header>
"""


def footer(lang):
    c = COMMON[lang]
    return f"""<footer class="site-footer"><div class="wrap">
  <div>
    <a class="brand" href="{url(lang, "home")}"><img src="/assets/app_icon.png" alt="">OYWA</a>
    <p>{esc(c["footer_tag"])}</p>
  </div>
  <nav aria-label="Footer">
    <a href="{url(lang, "features")}">{esc(c["nav_features"])}</a>
    <a href="{url(lang, "privacy")}">{esc(c["privacy"])}</a>
    <a href="mailto:{EMAIL}">{esc(c["contacts"])}</a>
  </nav>
  <div class="legal">
    <span>© 2026 OYWA</span>
    <span>{esc(c["owner"])}</span>
    <a href="{url(lang, "privacy")}">{esc(c["privacy"])}</a>
    <a href="{url(lang, "cookie")}">{esc(c["cookie"])}</a>
    <a href="{url(lang, "terms")}">{esc(c["terms"])}</a>
    <a href="mailto:{EMAIL}">{EMAIL}</a>
  </div>
</div></footer>

<script src="/main.js?v={ASSET_VERSION}"></script>
</body>
</html>
"""


def screen(lang, img):
    """Schermata nella lingua della pagina, se esiste; altrimenti quella italiana."""
    if lang != "it" and (ROOT / "assets" / "screens" / lang / f"{img}.jpg").exists():
        return f"/assets/screens/{lang}/{img}.jpg"
    return f"/assets/screens/{img}.jpg"


def phone(lang, img, alt="", lazy=True):
    loading = ' loading="lazy"' if lazy else ""
    return f'<div class="phone"><img src="{screen(lang, img)}" alt="{esc(alt)}"{loading}></div>'


def feature_row(row, flip, lang):
    paragraphs = "".join(f"<p>{p}</p>" for p in row["p"])
    items = "".join(f"<li>{i}</li>" for i in row.get("list", []))
    lst = f"<ul>{items}</ul>" if items else ""
    more = f'<p><a href="{url(lang, "features")}">{esc(row["more"])}</a></p>' if row.get("more") else ""
    return f"""    <div class="feature{" flip" if flip else ""} reveal">
      <div class="feature-media">
        <div class="blob" style="background:var(--c-{row["color"]})"></div>
        {phone(lang, row["img"], row["alt"])}
      </div>
      <div class="feature-text">
        <span class="eyebrow">{esc(row["eyebrow"])}</span>
        <h3>{esc(row["h3"])}</h3>
        {paragraphs}{lst}{more}
      </div>
    </div>
"""


def cta(title, text, href, label, icon_name="mail"):
    return f"""<section>
  <div class="wrap">
    <div class="cta reveal">
      <div>
        <h2>{esc(title)}</h2>
        <p>{esc(text)}</p>
      </div>
      <a class="btn" href="{href}">{icon(icon_name)}{esc(label)}</a>
    </div>
  </div>
</section>
"""


# ---------------------------------------------------------------------------
# Pagine
# ---------------------------------------------------------------------------

def json_ld(lang):
    data = {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "Organization", "@id": SITE + "/#organization", "name": "OYWA", "url": SITE + "/",
             "logo": SITE + "/assets/app_icon.png", "email": EMAIL},
            {"@type": "WebSite", "@id": SITE + "/#website", "name": "OYWA", "url": SITE + "/",
             "inLanguage": [LANGS[l]["html"] for l in LANGS], "publisher": {"@id": SITE + "/#organization"}},
            {"@type": "MobileApplication", "name": "OYWA", "operatingSystem": "iOS, Android",
             "applicationCategory": "TravelApplication", "description": HOME[lang]["desc"],
             "inLanguage": [LANGS[l]["html"] for l in LANGS], "image": f"{SITE}/assets/og-image-{lang}.jpg",
             "screenshot": [SITE + screen(lang, s) for s in ("mappa", "rapido-nome", "voto", "paesi")],
             "publisher": {"@id": SITE + "/#organization"}},
        ],
    }
    return '<script type="application/ld+json">\n' + json.dumps(data, ensure_ascii=False, indent=2) + "\n</script>\n"


def home(lang):
    t, c = HOME[lang], COMMON[lang]
    chip_colors = ["attrazione", "aereo", "ristorante"]
    chips = "".join(
        f'<li><i style="background:var(--c-{col})">{icon("check", "3")}</i>{esc(txt)}</li>'
        for col, txt in zip(chip_colors, t["chips"])
    )
    strip = "".join(f"<li><b>{esc(n)}</b><span>{esc(s)}</span></li>" for n, s in t["strip"])
    rows = "".join(feature_row(r, i % 2 == 1, lang) for i, r in enumerate(t["rows"]))
    cats = "".join(f'<span style="--c:var(--c-{col})">{esc(name)}</span>' for col, name in zip(CAT_COLORS, t["cats"]))
    gallery = "".join(
        f'<figure>{phone(lang, img, alt)}<figcaption>{esc(cap)}<span>{esc(sub)}</span></figcaption></figure>'
        for img, cap, sub, alt in GALLERY[lang]
    )
    facts_icons = ["phone", "ban", "download"]
    facts = "".join(
        f"<li><i>{icon(ic)}</i><span><b>{esc(b)}</b> {esc(rest)}</span></li>"
        for ic, (b, rest) in zip(facts_icons, t["facts"])
    )
    note = esc(t["night_note"]).replace("{link}", f'<a href="{url(lang, "privacy")}">{esc(t["night_link"])}</a>')
    (f1b, f1s), (f2b, f2s) = t["float1"], t["float2"]

    body = f"""{header(lang, "home")}
<main id="main">

<section class="hero">
  <div class="wrap">
    <div class="reveal">
      <span class="eyebrow">{esc(t["eyebrow"])}</span>
      <h1>{esc(t["h1"])} <em>{esc(t["h1_em"])}<svg viewBox="0 0 300 20" preserveAspectRatio="none" aria-hidden="true"><path d="M3 14 C 60 4, 120 4, 170 10 S 260 16, 297 6" fill="none" stroke="#D2785A" stroke-width="5" stroke-linecap="round" opacity=".45"/></svg></em>.</h1>
      <p class="lead">{esc(t["lead"])}</p>
      <div class="actions">
        <a class="btn" href="{mailto(lang)}">{icon("send")}{esc(t["btn_try"])}</a>
        <a class="btn ghost" href="{url(lang, "features")}">{esc(t["btn_features"])}</a>
      </div>
      <ul class="chips">{chips}</ul>
    </div>

    <div class="hero-visual reveal" aria-hidden="true">
      <svg class="route" viewBox="0 0 600 680" fill="none">
        <path d="M40 600 C 120 420, 60 260, 220 200 S 520 160, 560 40" stroke="#D2785A" stroke-width="2.5" stroke-dasharray="2 12" stroke-linecap="round" opacity=".55"/>
        <circle cx="40" cy="600" r="7" fill="#D2785A" opacity=".55"/>
        <path d="M552 30 l18 6 -14 12z" fill="#D2785A" opacity=".55"/>
      </svg>
      <div class="phone p2"><img src="{screen(lang, "voto")}" alt=""></div>
      <div class="phone p1"><img src="{screen(lang, "mappa")}" alt=""></div>
      <div class="float-card f1">
        <span class="dot" style="background:var(--c-poi)">{icon("globe")}</span>
        <div><b>{esc(f1b)}</b><span>{esc(f1s)}</span></div>
      </div>
      <div class="float-card f2">
        <span class="dot" style="background:#6E8259">{icon("star", "2.4")}</span>
        <div><b>{esc(f2b)}</b><span>{esc(f2s)}</span></div>
      </div>
    </div>
  </div>
</section>

<div class="strip">
  <ul class="wrap">{strip}</ul>
</div>

<section>
  <div class="wrap">
    <div class="section-head center reveal">
      <span class="eyebrow">{esc(t["sec_eyebrow"])}</span>
      <h2>{esc(t["sec_h2"])}</h2>
      <p>{esc(t["sec_p"])}</p>
    </div>
{rows}
    <div class="cats reveal">{cats}</div>
  </div>
</section>

<section class="gallery-section">
  <div class="wrap">
    <div class="section-head center reveal">
      <span class="eyebrow">{esc(t["gal_eyebrow"])}</span>
      <h2>{esc(t["gal_h2"])}</h2>
      <p>{esc(t["gal_p"])}</p>
    </div>
  </div>
  <div class="gallery reveal" tabindex="0">{gallery}</div>
  <div class="gallery-nav">
    <button type="button" data-gallery="prev" aria-label="{esc(c["prev"])}">{icon("prev")}</button>
    <button type="button" data-gallery="next" aria-label="{esc(c["next"])}">{icon("next")}</button>
  </div>
</section>

<section class="night">
  <div class="wrap">
    <div class="reveal">
      <span class="eyebrow">{esc(t["night_eyebrow"])}</span>
      <h2>{esc(t["night_h2"])}</h2>
      <p>{esc(t["night_p"])}</p>
      <ul class="facts">{facts}</ul>
      <p>{note}</p>
    </div>
    <img class="poster reveal" src="/assets/illustrazione.png" alt="{esc(t["poster_alt"])}" loading="lazy">
  </div>
</section>

{cta(t["cta_h2"], t["cta_p"], mailto(lang), EMAIL)}
</main>

{footer(lang)}"""
    return head(lang, "home", t["title"], t["desc"], t["og_title"], json_ld(lang)) + body


def features(lang):
    t = FEATURES[lang]
    rows = "".join(feature_row(r, i % 2 == 1, lang) for i, r in enumerate(t["rows"]))
    cards = "".join(
        f'<div class="card reveal"><div class="ico" style="background:var(--c-{col})">{icon(ic)}</div>'
        f"<h3>{esc(h)}</h3><p>{p}</p></div>"
        for col, ic, h, p in t["cards"]
    )
    body = f"""{header(lang, "features")}
<main id="main">

<div class="page-hero">
  <div class="wrap reveal">
    <span class="eyebrow">{esc(t["eyebrow"])}</span>
    <h1>{esc(t["h1"])}</h1>
    <p>{esc(t["p"])}</p>
  </div>
</div>

<section style="padding-top:40px">
  <div class="wrap">
{rows}  </div>
</section>

<section class="gallery-section">
  <div class="wrap">
    <div class="section-head center reveal">
      <span class="eyebrow">{esc(t["more_eyebrow"])}</span>
      <h2>{esc(t["more_h2"])}</h2>
    </div>
    <div class="cards">{cards}</div>
  </div>
</section>

{cta(t["cta_h2"], t["cta_p"], mailto(lang), t["cta_btn"])}
</main>

{footer(lang)}"""
    return head(lang, "features", t["title"], t["desc"], t["og_title"]) + body


def legal(lang, page, data):
    def fill(text):
        return (text.replace("{MAIL}", f'<a href="mailto:{EMAIL}">{EMAIL}</a>')
                .replace("{PRIVACY}", url(lang, "privacy"))
                .replace("{COOKIE}", url(lang, "cookie"))
                .replace("{TERMS}", url(lang, "terms")))

    summary = ""
    if data.get("summary"):
        cards = "".join(
            f'<div><i style="background:var(--c-{col})">{icon(ic)}</i><b>{esc(h)}</b><span>{esc(p)}</span></div>'
            for col, ic, h, p in data["summary"]
        )
        summary = f'<div class="summary reveal">{cards}</div>'
    toc = "".join(
        f'<li><a href="#{sid}">{n}. {esc(title)}</a></li>' for n, (sid, title, _) in enumerate(data["sections"], 1)
    )
    sections = "".join(
        f'<h2 id="{sid}"><span>{n}.</span>{esc(title)}</h2>{fill(text)}'
        for n, (sid, title, text) in enumerate(data["sections"], 1)
    )
    note = f'<p class="note">{esc(TRANSLATION_NOTE[lang])}</p>' if TRANSLATION_NOTE[lang] else ""

    body = f"""{header(lang, page)}
<main id="main">

<div class="page-hero">
  <div class="wrap reveal">
    <span class="eyebrow">OYWA</span>
    <h1>{esc(data["h1"])}</h1>
    <p>{esc(UPDATED[lang])}</p>
  </div>
</div>

<div class="wrap">
  {summary}
  <div class="doc-layout">
    <nav class="toc" aria-label="{esc(TOC[lang])}">
      <b>{esc(TOC[lang])}</b>
      <ol>{toc}</ol>
    </nav>
    <article class="doc">
      <p class="meta">{esc(data["intro"])}</p>
      {note}
      {sections}
    </article>
  </div>
</div>
</main>

{footer(lang)}"""
    return head(lang, page, data["title"], data["desc"], data["title"]) + body


def not_found():
    lines = {
        "it": ("Questo luogo non è sulla mappa.", "La pagina che cerchi non esiste o è stata spostata.", "Torna alla home"),
        "en": ("This place isn't on the map.", "The page you're looking for doesn't exist or has moved.", "Back to home"),
    }
    it, en = lines["it"], lines["en"]
    v = ASSET_VERSION
    return f"""<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>404 – OYWA</title>
<meta name="robots" content="noindex">
<meta name="theme-color" content="#FAF3E6">
<link rel="icon" href="/assets/app_icon.png">
<link rel="stylesheet" href="/assets/fonts/fonts.css?v={v}">
<link rel="stylesheet" href="/style.css?v={v}">
</head>
<body>
<header class="site-header"><div class="wrap">
  <a class="brand" href="/"><img src="/assets/app_icon.png" alt="">OYWA</a>
</div></header>
<main class="page-hero">
  <div class="wrap">
    <span class="eyebrow">404</span>
    <h1>{it[0]}</h1>
    <p>{it[1]}<br><span lang="en">{en[1]}</span></p>
    <p style="margin-top:28px"><a class="btn" href="/">{it[2]}</a> <a class="btn ghost" href="/en/" lang="en">{en[2]}</a></p>
  </div>
</main>
</body>
</html>
"""


def sitemap():
    entries = []
    for page in SLUGS:
        for lang in LANGS:
            alts = "".join(
                f'\n    <xhtml:link rel="alternate" hreflang="{LANGS[l]["html"]}" href="{SITE + url(l, page)}"/>'
                for l in LANGS
            )
            entries.append(f"  <url>\n    <loc>{SITE + url(lang, page)}</loc>\n    <lastmod>{LASTMOD}</lastmod>{alts}\n  </url>")
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
            + "\n".join(entries) + "\n</urlset>\n")


def og_images():
    script = Path(__file__).parent / "og-image.swift"
    for lang in LANGS:
        t = HOME[lang]
        out = ROOT / "assets" / f"og-image-{lang}.png"
        shots = ROOT / "assets" / "screens" / (lang if lang != "it" else "")
        subprocess.run(["swift", str(script), str(ROOT), str(out), *t["og_lines"], *t["og_sub"], str(shots)], check=True)
        jpg = out.with_suffix(".jpg")
        subprocess.run(["sips", "-s", "format", "jpeg", "-s", "formatOptions", "85", str(out), "--out", str(jpg)],
                       check=True, stdout=subprocess.DEVNULL)
        out.unlink()
        print("og:", jpg.relative_to(ROOT))


def check_keys():
    for name, table in [("COMMON", COMMON), ("HOME", HOME), ("FEATURES", FEATURES), ("GALLERY", GALLERY),
                        ("PRIVACY", PRIVACY), ("COOKIE", COOKIE), ("TERMS", TERMS)]:
        ref = table["it"]
        for lang in LANGS:
            other = table[lang]
            if isinstance(ref, dict):
                missing = set(ref) - set(other)
                assert not missing, f"{name}[{lang}] senza {missing}"
                for key in ("rows", "sections", "cards"):
                    if key in ref:
                        assert len(ref[key]) == len(other[key]), f"{name}[{lang}].{key}: numero diverso"
            else:
                assert len(ref) == len(other), f"{name}[{lang}]: numero diverso"


def main():
    check_keys()
    pages = {
        "home": home,
        "features": features,
        "privacy": lambda l: legal(l, "privacy", PRIVACY[l]),
        "cookie": lambda l: legal(l, "cookie", COOKIE[l]),
        "terms": lambda l: legal(l, "terms", TERMS[l]),
    }
    for page, render in pages.items():
        for lang in LANGS:
            path = out_path(lang, page)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(render(lang), encoding="utf-8")
            print("page:", path.relative_to(ROOT))
    (ROOT / "404.html").write_text(not_found(), encoding="utf-8")
    (ROOT / "sitemap.xml").write_text(sitemap(), encoding="utf-8")
    if "--og" in sys.argv:
        og_images()


if __name__ == "__main__":
    main()
