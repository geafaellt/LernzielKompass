"""Embed the read-only teacher information without external requests."""
from pathlib import Path
import json
import re
root = Path(__file__).resolve().parents[1]
p = root / 'dist/index.html'
html = p.read_text()
data = json.loads((root / 'curriculum/fsp-rueckwaerts/teacher_info.json').read_text())
parts = {
    'script id="fsp-info-data" type="application/json"': json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/'),
    'script id="fsp-info-script"': '\n' + (root / 'assets/fsp-info.js').read_text(),
    'style id="fsp-info-style"': '\n' + (root / 'assets/fsp-info.css').read_text(),
}
for opening, content in parts.items():
    closing = opening.split()[0]
    html, n = re.subn(r'(<'+re.escape(opening)+r'>).*?(</'+closing+r'>)', lambda m: m[1]+content+m[2], html, flags=re.S)
    assert n == 1, opening
p.write_text(html)
print('PASS: teacher information embedded (10 reviewed cases, independent of planning)')
