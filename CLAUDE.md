# Sardor Ismatov portfolio: notes for Claude

The owner adds projects and updates content by asking Claude. Read this first; it saves exploring the repo.

## How the site works
- Static site (plain HTML/CSS/JS). Cloudflare Workers Builds deploys every push to `main`
  (`wrangler.jsonc`, assets directory = repo root). Live: https://portfolio.sardorjonumidvich.workers.dev
- `.assetsignore` keeps non-site files (this file, `tools/`, README, `.docx`, config) off the public site.
  Anything new that is not part of the site must be added there.
- `_redirects` keeps old public URLs (old PDF names) working. Do not remove its rules.
- `vercel.json` makes the old Vercel site (sardorismatov.vercel.app) redirect every path here, so old links keep working.
- The pages (`index.html`, `All_Projects.html`, `Bank_PnL_performance.html`, `Uzbekistan_population.html`,
  `Retail_sales_page.html`, `404.html`) are **generated** by `tools/build.py`.
  Edit the generator, then run `python3 tools/build.py`. Never hand-edit the HTML: it is overwritten.
- Styles: `assets/css/site.css` (design tokens at the top; light theme is the default, dark only via the toggle).
  Behaviour: `assets/js/site.js`. Both hand-written, no build step.

## Content rules
- Only publish facts the owner gave (CV, messages). Never invent metrics, employers, dates or results.
- The Uzbekistan population numbers come from the owner's dashboard; do not change them unless asked.
- Projects show no creation date (owner's request). Data periods in titles or KPI notes are fine.
- Current role: BI Engineer at National Bank of Uzbekistan (NBU), Jul 2025 to present.
- The site must match the CV in `files/Sardor_Ismatov_Resume.pdf` (titles, dates, numbers).
  When the owner sends a new CV, replace that file and re-check the experience section against it.
  Exception: the 2023 bank internships are deliberately left off the site (owner's request), even if the CV lists them.

## Add a project
1. Screenshot (if any): save as `assets/img/<slug>.png` and also make a WebP:
   `python3 -c "from PIL import Image; Image.open('assets/img/<slug>.png').save('assets/img/<slug>.webp', quality=82)"`
2. Card only (external dashboard or GitHub link): append a dict to `PROJECTS` in `tools/build.py` with
   `key, type ('powerbi'|'sql'), label, title, desc, tags, ext=(url, "Open dashboard" or "View on GitHub")`
   and add an SVG cover under the same key in `COVERS` (copy an existing one).
3. Full case study page: append to `PROJECTS` with `page="<File>.html"`, `img=(slug, width, height, alt)`
   and `dash=<Power BI URL>`; add a matching entry to `CASES` (copy an existing one: KPIs, body HTML,
   prev/next links). New page filenames must keep working links from the other pages' prev/next.
4. Update counts that mention projects (projects page intro in `build_all`, the "Case studies" lead in `build_index`).
   The homepage features every project with a `page`; the first one in `PROJECTS` gets the wide card, so put the newest first
   and fix the prev/next links of the neighbouring case pages.
   Screenshots: Power BI is unreachable from the sandbox, so ask the owner for one. Crop to 1600x940 (the card ratio),
   save WebP, and keep the PNG fallback under ~400 KB (a 256-colour palette works well for dashboards).
5. Regenerate and check before pushing:
   - `python3 tools/build.py`
   - every local href/src resolves, one h1 per page
   - screenshots with Playwright (`NODE_PATH=/opt/node22/lib/node_modules`, serve with `npx http-server`) at 375px and 1440px
   - `npx -y wrangler@4.147.0 deploy --dry-run`, then delete `.wrangler/`
6. Commit, then push to `main` to deploy.
