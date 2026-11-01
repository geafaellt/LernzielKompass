from pathlib import Path
import json,re,subprocess,tempfile
root=Path(__file__).resolve().parents[1];d=root/'curriculum/deutsch'
m=json.loads((d/'deutsch_module.json').read_text());html=(root/'dist/index.html').read_text()
rows={k:{r['id']:r for r in json.loads((d/(k+'_inventory.json')).read_text())['rows']} for k in ['gs','fsp']}
assert len(m['target_audit'])==117
assert len({c['id'] for c in m['connections']})==len(m['connections'])
sources={s['id']:s for s in m['sources']}
for c in m['connections']:
 assert 'task_suggestions' not in c and 'aid_suggestions' not in c, 'Teacher-owned fields must not contain suggestions'
 assert c['gs_target_ids'] and c['fsp_target_ids']
 for k in ['gs','fsp']:
  rs=[rows[k][rid] for rid in c[k+'_target_ids']]
  assert rs[0]['level']==1,(c['id'],k,'not root')
  assert all(r['grade']==rs[0]['grade'] for r in rs)
  assert rs[0]['target'].startswith(c[k+'_operator']),(c['id'],k)
  assert all('Q-DE-'+r['id'] in c['source_ids'] for r in rs)
 assert all(sid in sources for sid in c['source_ids'])
 assert len(c['fine_goals'])==2
 assert all(x['goal'] and x['criterion'] for x in c['fine_goals'])
embedded=json.loads(re.search(r'<script id="deutsch-data" type="application/json">(.*?)</script>',html,re.S)[1]);assert embedded==m
base=(root/'curriculum/sachunterricht/baseline.json').read_text()
pat=r'<script id="curriculum-data" type="application/json">(.*?)</script>'
assert re.search(pat,html,re.S)[1]==base,'Sachunterricht changed'
for attr,js in re.findall(r'<script([^>]*)>(.*?)</script>',html,re.S):
 if 'application/json' in attr or not js.strip():continue
 with tempfile.NamedTemporaryFile(suffix='.js',mode='w') as f:
  f.write(js);f.flush();subprocess.run(['node','--check',f.name],check=True,capture_output=True)
print(f"PASS: {len(m['connections'])} German cards, 117 block decisions, valid source anchors and scripts; Sachunterricht unchanged.")
