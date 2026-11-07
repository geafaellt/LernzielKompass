"""Validate the teacher information against its reviewed evidence and embedded data."""
from pathlib import Path
import json
import re
from collections import Counter
root = Path(__file__).resolve().parents[1]
folder = root / 'curriculum/fsp-rueckwaerts'
data = json.loads((folder/'teacher_info.json').read_text())
review = json.loads((folder/'review_001.json').read_text())
items = data['items']
assert not data['complete'] and not review['complete_individual_reverse_mapping']
assert len(items) == len({i['id'] for i in items}) == 10
assert Counter(i['status'] for i in items) == Counter(specific_not_explicit=2, partial=5, choice_dependent=1, remark_only=1, cross_subject_counterpart=1)
reviewed = {i['id']: i for i in review['findings']}
for item in items:
    for key in ('subject','status','fsp_evidence','gs_comparators'):
        assert item[key] == reviewed[item['id']][key], (item['id'],key)
    assert item['title'] and item['interpretation']
    for key in ('fsp_evidence','gs_comparators'):
        assert item[key]
        for row in item[key]:
            assert re.fullmatch(r'https://www\.schulportal\.sachsen\.de/lplandb/lehrplan/(139|146|80|908|912)#'+row['id'],row['url'])
            assert row['grade'] in (('1/2','3/4') if key=='fsp_evidence' else ('1/2','3','4'))
            assert row['target'].strip()
html = (root/'dist/index.html').read_text()
payload = re.search(r'<script id="fsp-info-data" type="application/json">(.*?)</script>',html,re.S)
assert json.loads(payload[1]) == data
for kind, name in [('script','js'),('style','css')]:
    tag_id = 'fsp-info-script' if kind=='script' else 'fsp-info-style'
    content = re.search(r'<'+kind+' id="'+tag_id+r'">(.*?)</'+kind+'>',html,re.S)[1]
    assert content.strip() == (root/f'assets/fsp-info.{name}').read_text().strip()
assert (root/'index.html').read_bytes()==(root/'dist/index.html').read_bytes()
print('PASS: 10 cases, evidence unchanged, classifications, source URLs and embedded assets verified.')
