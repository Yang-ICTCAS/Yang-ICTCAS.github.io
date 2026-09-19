"""Build a dependency-free academic site from editable bibliographic data."""
from pathlib import Path
import html
import json
import re

ROOT = Path(__file__).resolve().parent
def esc(value):
    return html.escape(str(value), quote=True)

def build():
    data = json.loads((ROOT / 'data/publications.json').read_text(encoding='utf-8'))
    papers = sorted(data['articles'], key=lambda p: (p.get('rank', 999), -int(p.get('year') or 0), p['title'].lower()))
    rows = []
    selected_rows = []
    for p in papers:
        featured = p.get('featured', False)
        authors = re.sub(r'\b(?:Xiaodong Yang|XD Yang|X Yang|X YANG)\b', lambda m: '<strong>' + m[0] + '</strong>', esc(p['authors']))
        links = [('Scholar', p['scholar'])]
        if p.get('paper'):
            links.insert(0, ('Paper', p['paper']))
        if p.get('pdf'):
            links.append(('PDF', p['pdf']))
        if p.get('code'):
            links.append(('Code', p['code']))
        link_html = ''.join(f'<a href="{esc(url)}" target="_blank" rel="noopener noreferrer">{label}<span aria-hidden="true"> ↗</span><span class="visually-hidden"> — {esc(p["title"])}</span></a>' for label, url in links)
        summary = ''
        if p.get('summary_en'):
            summary = f'<p class="pub-summary" data-en="{esc(p["summary_en"])}" data-zh="{esc(p["summary_zh"])}">{esc(p["summary_en"])}</p>'
        paper_type = f'<span class="paper-type">{esc(p["type"])}</span>' if p.get('type') else ''
        rows.append(f'''<article class="publication" data-featured="{str(featured).lower()}" data-topic="{esc(p['topic'])}" data-year="{esc(p['year'])}">
  <div class="pub-year">{esc(p['year'])}<span class="pub-venue-short">{esc(p.get('short',''))}</span></div>
  <div><a class="pub-title" href="{esc(p.get('paper',p['scholar']))}" target="_blank" rel="noopener noreferrer">{esc(p['title'])}</a>
  <p class="pub-authors">{authors}</p><p class="pub-venue">{esc(p['venue'])}{paper_type}</p>{summary}
  <div class="pub-links">{link_html}</div></div>
</article>''')
        if featured:
            selected_rows.append(rows[-1])
    all_rows = [row for _, row in sorted(zip(papers, rows), key=lambda item: (-int(item[0].get('year') or 0), item[0]['title'].lower()))]
    years = sorted({p['year'] for p in papers if p.get('year')}, reverse=True)
    options = ''.join(f'<option value="{esc(y)}">{esc(y)}</option>' for y in years)
    layout = (ROOT / 'templates/layout.html').read_text(encoding='utf-8')
    for filename, key, title_en, title_zh in [
        ('index.html', 'home', 'Home', '首页'),
        ('research.html', 'research', 'Research', '研究方向'),
        ('publications.html', 'publications', 'Publications', '学术成果'),
    ]:
        content = (ROOT / 'templates' / filename).read_text(encoding='utf-8')
        page = layout.replace('{{CONTENT}}', content)
        values = {'PUBLICATIONS': '\n'.join(all_rows), 'SELECTED_PUBLICATIONS': '\n'.join(selected_rows), 'YEAR_OPTIONS': options,
                  'TOTAL_COUNT': str(len(papers)), 'PAGE': key, 'URL': filename,
                  'TITLE_EN': title_en, 'TITLE_ZH': title_zh}
        for token, value in values.items():
            page = page.replace('{{' + token + '}}', value)
        page = page.replace(f'data-page="{key}" data-en=', f'data-page="{key}" class="active" aria-current="page" data-en=')
        (ROOT / 'site' / filename).write_text(page, encoding='utf-8')
    (ROOT / 'site/.nojekyll').touch()
    print(f'Built 3 pages: {len(papers)} records, {sum(p.get("featured",False) for p in papers)} selected.')

if __name__ == '__main__':
    build()
