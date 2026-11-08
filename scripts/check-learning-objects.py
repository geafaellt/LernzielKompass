"""Validate editorial learning-object overrides without modifying curriculum evidence."""
import json,re
from pathlib import Path
root=Path(__file__).resolve().parents[1]
folder=root/'curriculum/learning_objects'
overrides=json.loads((folder/'overrides.json').read_text())
audit=json.loads((folder/'review_001.json').read_text())
models={'Deutsch':json.loads((root/'curriculum/deutsch/deutsch_module.json').read_text()),'Sachunterricht':json.loads((root/'curriculum/sachunterricht/baseline.json').read_text())}
cards={c['id']:c for m in models.values() for c in m['connections']}
rows={r['id']:r for r in audit['cards']}
assert len(rows)==len(audit['cards']) and set(rows)==set(cards)
assert set(overrides)<=set(cards)
for subject,m in models.items():
 expected={'reviewed':len(m['connections']),'reworded':sum(c['id'] in overrides for c in m['connections'])}
 expected['retained']=expected['reviewed']-expected['reworded']
 assert all(audit['counts'][subject][k]==v for k,v in expected.items())
 for c in m['connections']:
  r=rows[c['id']];assert r['subject']==subject and r['source_ids']==c['source_ids']
  assert r['before']==c['shared_object_suggestion']
  assert r['after']==overrides.get(c['id'],c['shared_object_suggestion'])
  assert r['decision']==('reworded' if c['id'] in overrides else 'retained')
  assert r['reason'] and r['after'].strip()
# These narrow conditions must survive future copy edits; no claim of semantic auto-validation.
for cid,terms in {'SU-028':['unterschiedliche Bezugsräume','Methodische Brücke'],'SU-061':['unterschiedlichen Bezugsräumen','kein identischer'],'SU-064':['GS-Wahlbereich 3'],'SU-128':['beiden Lehrplanausschnitten'],'SU-131':['kein vollständiger Körperbauvergleich'],'SU-146':['FSP-Bandziele'],'SU-147':['GS-Wahlbereich 1'],'SU-149':['FSP-Wahlbereich 3'],'SU-152':['FSP-Wahlbereich 4'],'DE-131':['FSP-Wahlbereich 1'],'DE-139':['FSP-Wahlbereich 1'],'DE-179':['bisherigen GS-Lernstand']}.items():
 assert all(t in overrides[cid] for t in terms),cid
html=(root/'dist/index.html').read_text()
embedded=json.loads(re.search(r'<script id="learning-object-data" type="application/json">(.*?)</script>',html,re.S)[1])
assert embedded==overrides
assert (root/'index.html').read_bytes()==(root/'dist/index.html').read_bytes()
print(f'PASS: all {len(cards)} reviewed learning objects, {len(overrides)} isolated copy overrides, source references, counts, selection conditions and synchronized payload.')
