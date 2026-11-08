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
context_sources = progress.get('context_sources', {})
cards = module['connections']
assert len(areas) == len(module['areas']) + len(progress['fsp_areas'])
assert len(sources) == len(module['sources'])
assert len({c['id'] for c in cards}) == len(cards) == progress['counts']['cards']
assert len({c['theme'] for c in cards}) == len(cards)
assert sum(c['stage_alignment']['relation'] == 'cross-band' for c in cards) == progress['counts']['cross_band']
def check_fsp_scope(card):
    cid = card['id']
    scope = card['fsp_scope']
    assert scope['status'] in {'explicit', 'derived', 'unspecified', 'domain_specific', 'not_applicable'}, cid
    assert all(scope[k] for k in ['summary', 'detail', 'planning_rule', 'source_ids']), cid
    assert set(scope['source_ids']).issubset(card['source_ids']), cid
    fsp_goal = card['fine_goals'][1]
    assert fsp_goal['scope_status'] == scope['status'], cid
    maximum = scope['max_value']
    if scope['status'] in {'explicit', 'derived'}:
        assert isinstance(maximum, int) and maximum > 0, cid
        assert fsp_goal['range_max'] == maximum, cid
        if scope['status'] == 'derived':
            context_ids = set(card.get('context_source_ids', []))
            assert set(scope['source_ids']) & context_ids, (cid, 'derived scope needs stage-goal evidence')
            assert all(sid in context_ids or sid.removeprefix('Q-MA-') in card['fsp_target_ids'] for sid in scope['source_ids']), cid
        else:
            assert all(sid.removeprefix('Q-MA-') in card['fsp_target_ids'] for sid in scope['source_ids']), cid
        for field in ['goal', 'criterion']:
            limits = [int(v.replace(' ', '').replace('.', '')) for v in re.findall(r'\bbis\s+(\d+(?:[ .]\d{3})*)\b', fsp_goal[field])]
            assert maximum in limits and all(v <= maximum for v in limits), (cid, field, 'range limit mismatch')
        if card.get('number_range_alignment'):
            assert card['number_range_alignment']['fsp_max'] == maximum, cid
    else:
        assert maximum is None and 'range_max' not in fsp_goal, cid
        if scope['status'] == 'unspecified':
            assert 'festgelegten Zahlenraum' in fsp_goal['goal'] and 'festgelegten Zahlenraum' in fsp_goal['criterion'], cid

def check_additional_gs_groups(card):
    """Reuse one card for another GS row without merging distinct target hierarchies."""
    cid = card['id']
    seen = set(card['gs_target_ids'])
    additional = set()
    for group in card.get('additional_gs_target_groups', []):
        ids = group['target_ids']
        assert len(ids) >= 2 and len(ids) == len(set(ids)), cid
        assert not seen.intersection(ids), (cid, 'duplicate GS evidence group')
        parent, *children = [anchors[rid] for rid in ids]
        assert parent['level'] == 1 and all(r['level'] > 1 for r in children), cid
        assert group['operator'] == parent['operator'] == card['gs_operator'], cid
        assert group['scope'] and group['covered_ids'], cid
        assert set(group['covered_ids']).isdisjoint(group['context_only_ids']), cid
        assert set(group['covered_ids']) | set(group['context_only_ids']) == set(ids), cid
        assert parent['id'] in group['context_only_ids'], cid
        for rid in ids:
            row = anchors[rid]
            sid = 'Q-MA-' + rid
            assert row['parent_target_id'] == parent['id'], (cid, rid)
            assert row['grade'] == card['stage_alignment']['gs_anchor_grade'], (cid, rid)
            assert row['area_id'] == card['app_area'], (cid, rid)
            assert sid in card['source_ids'], (cid, rid)
            assert sources[sid]['url'] == row['url'] == progress['source_plans']['gs'] + '#' + rid, cid
            assert sources[sid]['version'] == row['version'] == '2026', cid
        seen.update(ids)
        additional.update(ids)
    return additional


def check_number_range_alignment(card):
    """Keep the range comparison tied to the precise target or stage-goal source."""
    card_id = card['id']
    number_range = card.get('number_range_alignment')
    if number_range:
        assert number_range.get('fsp_basis') in {None, 'stage_goal_context', 'target_row'}, card_id
        assert number_range['fsp_max'] == card['fsp_scope']['max_value'], card_id
        assert number_range['relation'] == 'reduced-fsp', card_id
        assert 0 < number_range['fsp_max'] < number_range['gs_max'], card_id
        assert number_range['full_gs_goal_covered'] is False, card_id
        assert number_range['gs_source_id'] == card['gs_target_ids'][0], card_id
        if number_range.get('fsp_basis') == 'stage_goal_context':
            assert card['fsp_scope']['status'] == 'derived', card_id
            assert 'Q-MA-' + number_range['fsp_source_id'] in card['fsp_scope']['source_ids'], card_id
            assert 'Q-MA-' + number_range['fsp_source_id'] in card.get('context_source_ids', []), card_id
        elif number_range.get('fsp_basis') == 'target_row':
            assert number_range['fsp_source_id'] in card['fsp_target_ids'], card_id
            assert card['fsp_scope']['status'] == 'explicit', card_id
            assert 'Q-MA-' + number_range['fsp_source_id'] in card['fsp_scope']['source_ids'], card_id
        else:
            assert number_range['fsp_source_id'] == card['fsp_target_ids'][0], card_id
        assert card['content_review_required'] and number_range['notice'] in card['app_review_message'], card_id
        for side in ['gs', 'fsp']:
            displayed_max = f"{number_range[side + '_max']:,}".replace(',', ' ')
            assert displayed_max in number_range['notice'], card_id


used_anchors = set()
used_sources = set()
for card in cards:
    assert card.get("shared_object_suggestion", "").strip(), (card["id"], "missing shared mathematical object")
    assert card["shared_object_suggestion"].strip().casefold() != card["theme"].strip().casefold(), (card["id"], "shared object must not merely repeat the card title")
    card_id = card['id']
    check_fsp_scope(card)
    assert re.fullmatch(r'MA-\d{3}', card_id) and card['subject'] == 'Mathematik'
    assert not {'task_suggestions', 'aid_suggestions'} & card.keys(), card_id
    assert [g['track'] for g in card['fine_goals']] == ['Grundschule', 'FSP Lernen'], card_id
    assert all(g['goal'] and g['criterion'] for g in card['fine_goals']), card_id
    assert card['app_review_message'] and card['operator_relation'], card_id
    check_number_range_alignment(card)
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
    additional_gs_ids = check_additional_gs_groups(card)
    used_anchors.update(additional_gs_ids)
    expected_sources.update('Q-MA-' + rid for rid in additional_gs_ids)
    context_ids = card.get('context_source_ids', [])
    assert len(context_ids) == len(set(context_ids)), card_id
    for sid in context_ids:
        source = context_sources[sid]
        assert source == sources[sid], card_id
        assert source['kind'] == 'stage_goals' and source['grade'] == fsp_band, card_id
        assert source['url'] == progress['source_plans']['fsp'] + '#' + sid.removeprefix('Q-MA-'), card_id
        assert source['version'] == '2019', card_id
        assert sid.removeprefix('Q-MA-') not in anchors, 'Context source must stay separate from target rows'
        expected_sources.add(sid)
    assert set(card['source_ids']) == expected_sources, card_id
    used_sources.update(expected_sources)

assert used_anchors == set(anchors) and used_sources == set(sources)
assert set(context_sources) == {sid for c in cards for sid in c.get('context_source_ids', [])}
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
    for group in card.get('additional_gs_target_groups', []):
        for rid in group['context_only_ids']:
            assert card['id'] not in audit[rid]['Karten'].split(';'), 'Context is not coverage'
        for rid in group['covered_ids']:
            assert card['id'] in audit[rid]['Karten'].split(';'), 'Reused card needs row-level audit'

print(f"PASS: {len(cards)} mathematics cards, {len(sources)} source links ({len(anchors)} target anchors, {len(context_sources)} context sources), synchronized Pages entry.")
