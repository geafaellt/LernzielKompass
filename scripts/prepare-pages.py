"""Stamp the publication date in Berlin time and synchronize GitHub Pages."""
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import re
import json
import shutil
import runpy

root = Path(__file__).resolve().parents[1]
runpy.run_path(str(root / 'scripts/update-fsp-info.py'))
source = root / 'dist/index.html'
html = source.read_text()
titles = json.loads((root / 'curriculum/card_titles.json').read_text())
payload = json.dumps(titles, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
html, count = re.subn(r'(<script id="card-title-data" type="application/json">).*?(</script>)', lambda match: match[1] + payload + match[2], html, flags=re.S)
assert count == 1, 'Expected one card title payload'
today = datetime.now(ZoneInfo('Europe/Berlin')).date()
stamp = f'<p class="small" id="last-updated">Zuletzt aktualisiert: <time datetime="{today.isoformat()}">{today.strftime("%d.%m.%Y")}</time></p>'
html, count = re.subn(r'<p class="small" id="last-updated">.*?</p>', stamp, html)
assert count == 1, 'Expected one publication date'
source.write_text(html)
shutil.copyfile(source, root / 'index.html')
print(f'PASS: Pages entry synchronized; updated {today.isoformat()}')
