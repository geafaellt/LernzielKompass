"""Check mathematics source anchors, stage bands and the published payload."""
import csv
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
folder = root / 'curriculum/mathematik'
module = json.loads((folder / 'mathematik_module.json').read_text())
progress = json.loads((folder / 'review_progress.json').read_text())
html = (root / 'dist/index.html').read_text()
payload = re.search(r'<script id="mathematik-data" type="application/json">(.*?)</script>', html, re.S)
assert payload and json.loads(payload[1]) == module
assert (root / 'dist/index.html').read_bytes() == (root / 'index.html').read_bytes()

areas = {a['id']: a for a in module['areas'] + progress['fsp_areas']}
sources = {s['id']: s for s in module['sources']}
anchors = progress['reviewed_anchors']
cards = module['connections']
assert len(areas) == len(module['areas']) + len(progress['fsp_areas'])
assert len(sources) == len(module['sources'])
assert len({c['id'] for c in cards}) == len(cards) == progress['counts']['cards']
assert len({c['theme'] for c in cards}) == len(cards)
assert sum(c['stage_alignment']['relation'] == 'cross-band' for c in cards) == progress['counts']['cross_band']
used_anchors = set()
used_sources = set()
for card in cards:
    card_id = card['id']
    assert re.fullmatch(r'MA-\d{3}', card_id) and card['subject'] == 'Mathematik'
    assert not {'task_suggestions', 'aid_suggestions'} & card.keys(), card_id
    assert [g['track'] for g in card['fine_goals']] == ['Grundschule', 'FSP Lernen'], card_id
    assert all(g['goal'] and g['criterion'] for g in card['fine_goals']), card_id
    assert card['app_review_message'] and card['operator_relation'], card_id
    number_range = card.get('number_range_alignment')
    if number_range:
        assert number_range['relation'] == 'reduced-fsp', card_id
        assert 0 < number_range['fsp_max'] < number_range['gs_max'], card_id
        assert number_range['full_gs_goal_covered'] is False, card_id
        assert number_range['gs_source_id'] == card['gs_target_ids'][0], card_id
        assert number_range['fsp_source_id'] == card['fsp_target_ids'][0], card_id
        assert card['content_review_required'] and number_range['notice'] in card['app_review_message'], card_id
        for side in ['gs', 'fsp']:
            displayed_max = f"{number_range[side + '_max']:,}".replace(',', ' ')
            assert displayed_max in number_range['notice'], card_id
    stage = card['stage_alignment']
    gs_grade = stage['gs_anchor_grade']
    fsp_band, = stage['fsp_curriculum_bands']
    assert gs_grade in {'1/2', '3', '4'} and fsp_band in {'1/2', '3/4'}, card_id
    assert stage['gs_curriculum_band'] == ('1/2' if gs_grade == '1/2' else '3/4'), card_id
    expected_relation = 'same-band' if stage['gs_curriculum_band'] == fsp_band else 'cross-band'
    assert stage['relation'] == expected_relation, card_id
    expected_sources = set()
    for side, grade, plan, version in [('gs', gs_grade, 912, '2026'), ('fsp', fsp_band, 139, '2019')]:
        ids = card[side + '_target_ids']
        assert len(ids) >= 2 and len(ids) == len(set(ids)), (card_id, side)
        parent, *children = [anchors[i] for i in ids]
        assert parent['level'] == 1 and all(r['level'] > 1 for r in children), (card_id, side)
        assert card[side + '_operator'] == parent['operator'] in {
            'Einblick gewinnen', 'Kennen', 'Übertragen', 'Beherrschen', 'Anwenden',
        }, (card_id, side)
        area = areas[parent['area_id']]
        assert area['side'] == side and area['grades'] == grade.split('/'), (card_id, side)
        if side == 'gs':
            assert card['app_area'] == area['id'], card_id
        for rid in ids:
            row = anchors[rid]
            sid = 'Q-MA-' + rid
            assert row['id'] == rid and row['parent_target_id'] == parent['id'], (card_id, rid)
            assert row['area_id'] == area['id'] and row['grade'] == grade, (card_id, rid)
            assert re.fullmatch(rf'page{plan}_\d+', rid), (card_id, rid)
            assert sources[sid]['url'] == row['url'] == progress['source_plans'][side] + '#' + rid, (card_id, rid)
            assert sources[sid]['version'] == row['version'] == version, (card_id, rid)
            expected_sources.add(sid)
            used_anchors.add(rid)
    assert set(card['source_ids']) == expected_sources, card_id
    used_sources.update(expected_sources)

assert used_anchors == set(anchors) and used_sources == set(sources)
with (folder / 'row_audit.csv').open(newline='') as audit_file:
    audit_rows = list(csv.DictReader(audit_file))
audit = {row['Ziel-ID']: row for row in audit_rows}
assert len(audit) == len(audit_rows), 'Duplicate audit row'
if not progress['complete']:
    assert progress['next_step']
    next_row = audit.get(progress['next_id'])
    assert next_row and 'offen' in next_row['Prüfstatus'], 'Next row must remain open'
for card in cards:
    context_ids = card.get('evidence_classification', {}).get('context_only_gs_ids', [])
    assert set(context_ids).issubset(card['gs_target_ids'])
    for rid in context_ids:
        assert card['id'] not in audit[rid]['Karten'].split(';'), 'Context is not coverage'

print(f"PASS: {len(cards)} mathematics cards, {len(sources)} source anchors, synchronized Pages entry.")
