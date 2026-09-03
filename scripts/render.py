#!/usr/bin/env python3
"""Render the research memos (Markdown) into research/<slug>/index.html inside the site shell,
copying each memo's sources/ folder alongside so relative links keep working. Minimal Markdown:
#/##/### headings, paragraphs, bullet and numbered lists, pipe tables, **bold**, *em*, `code`,
[text](url); file:///home/... links are rewritten to relative. Idempotent."""
import html, os, re, shutil, glob
root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
MEMOS = [  # (slug, source markdown, title override)
    ("crowdfunding", "drafts/reviews/crowdfunding-findings.md", "Crowdfunding as a demand instrument (codex run)"),
    ("crowdfunding-gemini", "drafts/reviews/crowdfunding-findings-agy.md", "Crowdfunding as a demand instrument (Gemini run)"),
    ("crowdfunding-comparison", "drafts/notes/2026-09-03-comparison.md", "Crowdfunding: the two runs compared"),
    ("diaspora-demand", "drafts/research/diaspora-demand/findings.md", "Diaspora demand in the Netherlands"),
    ("succession", "drafts/research/succession/findings.md", "Business succession: what is for sale"),
    ("skills-licences", "drafts/research/skills-licences/findings.md", "Licences obtainable within twelve months"),
    ("trade-flows", "drafts/research/trade-flows/findings.md", "Trade-flow gaps: Poland and non-EU imports"),
    ("regulation-physical", "drafts/research/regulation-physical/findings.md", "Regulation that creates physical work, 2026–2028"),
    ("ai-physical-footprint", "drafts/research/ai-physical-footprint/findings.md", "The physical footprint of AI in the Netherlands"),
    ("boring-business", "drafts/research/boring-business/findings.md", "The boring-business lens: which small physical firms last"),
    ("triage", "drafts/notes/2026-09-03-fable-triage.md", "Triage: seven kept, thirteen cut"),
    ("triage-2", "drafts/notes/2026-09-04-fable-triage-2.md", "Triage, second pass: two Fable runs"),
    ("ideation-method", "scripts/prompts/idea-metaprompt.md", "The ideation metaprompt"),
    ("ideation-assembled-machines", "drafts/ideation/assembled-machines/ideas.md", "Ideation: assembled machines"),
    ("ideation-assembled-machines-reviewed", "drafts/ideation/assembled-machines/ideas-reviewed.md", "Ideation: assembled machines, precedent review"),
    ("ideation-crossing-flows", "drafts/ideation/crossing-flows/ideas.md", "Ideation: crossing flows"),
    ("ideation-crossing-flows-reviewed", "drafts/ideation/crossing-flows/ideas-reviewed.md", "Ideation: crossing flows, precedent review"),
    ("triage-3", "drafts/notes/2026-09-04-fable-triage-3.md", "Triage, third pass: the ideation results"),
    ("edge-inventory", "drafts/edge-inventory.md", "Edge inventory (draft, for correction)"),
]
def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r'`([^`]+)`', r'<code>\1</code>', t)
    t = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<![\w*])\*([^*\n]+)\*(?![\w*])', r'<em>\1</em>', t)
    t = re.sub(r'(?:file://)?/home/diablo/book19/drafts/research/[^/]+/', '', t)
    t = re.sub(r'(?:file://)?/home/diablo/book19/', '../../', t)
    t = re.sub(r'\[([^\]]+)\]\(([^)\s]+)\)', r'<a href="\2">\1</a>', t)
    return t
def render_md(md):
    out, i, lines = [], 0, md.splitlines()
    while i < len(lines):
        l = lines[i]
        if not l.strip(): i += 1; continue
        if l.startswith('#'):
            n = len(l) - len(l.lstrip('#')); txt = l.lstrip('#').strip()
            if n == 1: i += 1; continue  # title handled separately
            out.append('<h%d>%s</h%d>' % (min(n, 4), inline(txt), min(n, 4))); i += 1; continue
        if l.lstrip().startswith('|'):
            rows = []
            while i < len(lines) and lines[i].lstrip().startswith('|'):
                rows.append(lines[i].strip()); i += 1
            rows = [r for r in rows if not re.fullmatch(r'\|?[\s:|-]+\|?', r)]
            if rows:
                cells = lambda r: [c.strip() for c in r.strip('|').split('|')]
                out.append('<div class="table-wrap"><table><thead><tr>' + ''.join('<th>%s</th>' % inline(c) for c in cells(rows[0])) + '</tr></thead><tbody>')
                for r in rows[1:]: out.append('<tr>' + ''.join('<td>%s</td>' % inline(c) for c in cells(r)) + '</tr>')
                out.append('</tbody></table></div>')
            continue
        if re.match(r'\s*([-*]|\d+\.)\s', l):
            ordered = bool(re.match(r'\s*\d+\.', l)); items = []
            while i < len(lines) and re.match(r'\s*([-*]|\d+\.)\s', lines[i]):
                item = re.sub(r'^\s*([-*]|\d+\.)\s', '', lines[i]); i += 1
                while i < len(lines) and lines[i].startswith('  ') and lines[i].strip() and not re.match(r'\s*([-*]|\d+\.)\s', lines[i]):
                    item += ' ' + lines[i].strip(); i += 1
                items.append(item)
            tag = 'ol' if ordered else 'ul'
            out.append('<%s>%s</%s>' % (tag, ''.join('<li>%s</li>' % inline(x) for x in items), tag)); continue
        if l.startswith('```'):
            i += 1; buf = []
            while i < len(lines) and not lines[i].startswith('```'): buf.append(lines[i]); i += 1
            i += 1; out.append('<pre><code>%s</code></pre>' % html.escape('\n'.join(buf))); continue
        if l.startswith('    ') and not l.strip().startswith('|'):
            buf = []
            while i < len(lines) and (lines[i].startswith('    ') or not lines[i].strip()) and not (i+1 < len(lines) and not lines[i].strip() and not lines[i+1].startswith('    ')):
                buf.append(lines[i][4:] if lines[i].startswith('    ') else ''); i += 1
            out.append('<pre><code>%s</code></pre>' % html.escape('\n'.join(buf).strip('\n'))); continue
        para = [l.strip()]; i += 1
        while i < len(lines) and lines[i].strip() and not lines[i].lstrip().startswith(('|', '#', '```')) and not re.match(r'\s*([-*]|\d+\.)\s', lines[i]) and not lines[i].startswith('    '):
            para.append(lines[i].strip()); i += 1
        out.append('<p>%s</p>' % inline(' '.join(para)))
    return '\n'.join(out)
SHELL = open(os.path.join(root, 'scripts', 'memo-shell.html'), encoding='utf-8').read()
for slug, src, title in MEMOS:
    p = os.path.join(root, src)
    if not os.path.exists(p): print('  missing', src); continue
    md = open(p, encoding='utf-8').read()
    m = re.search(r'^#\s+(.*)$', md, re.M); heading = m.group(1).strip() if m else title
    dst = os.path.join(root, 'research', slug); os.makedirs(dst, exist_ok=True)
    srcdir = os.path.join(os.path.dirname(p), 'sources')
    if os.path.isdir(srcdir):
        if os.path.isdir(os.path.join(dst, 'sources')): shutil.rmtree(os.path.join(dst, 'sources'))
        shutil.copytree(srcdir, os.path.join(dst, 'sources'), ignore=lambda d, names: [n for n in names if n.endswith(('.zip', '.pyc', '.pdf')) or n == '__pycache__' or (os.path.isfile(os.path.join(d, n)) and os.path.getsize(os.path.join(d, n)) > 2_000_000)])
    for extra in glob.glob(os.path.join(os.path.dirname(p), '*.csv')) + glob.glob(os.path.join(os.path.dirname(p), '*.json')):
        shutil.copy(extra, dst)
    body = render_md(md)
    page = SHELL.replace('{{TITLE}}', html.escape(title)).replace('{{HEADING}}', inline(heading)).replace('{{BODY}}', body).replace('{{SRC}}', src)
    open(os.path.join(dst, 'index.html'), 'w', encoding='utf-8').write(page); print('  wrote research/%s/index.html' % slug)
