"""Refresh only the separately versioned German payload."""
from pathlib import Path
import json,re
root=Path(__file__).resolve().parents[1]
p=root/'dist/index.html'
s=p.read_text()
m=json.loads((root/'curriculum/deutsch/deutsch_module.json').read_text())
payload=json.dumps(m,ensure_ascii=False,separators=(',',':')).replace('</','<\\/')
s,n=re.subn(r'(<script id="deutsch-data" type="application/json">).*?(</script>)',lambda x:x[1]+payload+x[2],s,flags=re.S)
assert n==1
s=s.replace('Die fachliche Gegenprüfung und Freigabe stehen noch aus.','Die Vorschläge sind fachlich nachgeschärft; eine vollständige Prüfung aller Unterziele ist noch offen.')
p.write_text(s)
