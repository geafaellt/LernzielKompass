"""Embed the versioned mathematics module in the app source."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
app = root / 'dist/index.html'
module = json.loads((root / 'curriculum/mathematik/mathematik_module.json').read_text())
payload = json.dumps(module, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
html, count = re.subn(
    r'(<script id="mathematik-data" type="application/json">).*?(</script>)',
    lambda match: match[1] + payload + match[2],
    app.read_text(),
    flags=re.S,
)
assert count == 1, 'Expected one mathematics payload'
app.write_text(html)
