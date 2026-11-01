"""Stamp the publication date in Berlin time and synchronize GitHub Pages."""
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import re
import shutil

root = Path(__file__).resolve().parents[1]
source = root / 'dist/index.html'
html = source.read_text()
today = datetime.now(ZoneInfo('Europe/Berlin')).date()
stamp = f'<p class="small" id="last-updated">Zuletzt aktualisiert: <time datetime="{today.isoformat()}">{today.strftime("%d.%m.%Y")}</time></p>'
html, count = re.subn(r'<p class="small" id="last-updated">.*?</p>', stamp, html)
assert count == 1, 'Expected one publication date'
source.write_text(html)
shutil.copyfile(source, root / 'index.html')
print(f'PASS: Pages entry synchronized; updated {today.isoformat()}')
