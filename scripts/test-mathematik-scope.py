"""Regression cases for the authored scope/goal data contract (not arbitrary task semantics)."""
import copy
import runpy
from pathlib import Path
checks = runpy.run_path(str(Path(__file__).with_name('check-mathematik.py')))
validate = checks['check_fsp_scope']
cards = {c['id']: c for c in checks['cards']}
cases = []
c = copy.deepcopy(cards['MA-008']); del c['fsp_scope']; cases.append(c)
c = copy.deepcopy(cards['MA-008']); c['fine_goals'][1]['criterion'] = 'Die Anzahl stimmt bis 100.'; cases.append(c)
c = copy.deepcopy(cards['MA-016']); c['fine_goals'][1]['goal'] += ' Auch bis 1 000.'; cases.append(c)
c = copy.deepcopy(cards['MA-020']); c['context_source_ids'] = []; cases.append(c)
c = copy.deepcopy(cards['MA-004']); c['fsp_scope']['max_value'] = 100; cases.append(c)
c = copy.deepcopy(cards['MA-003']); c['fsp_scope']['source_ids'] = ['Q-MA-page139_37926']; cases.append(c)
for c in cases:
    try:
        validate(c)
    except (AssertionError, KeyError):
        pass
    else:
        raise AssertionError('Invalid scope accepted: ' + c['id'])
for c in cards.values():
    validate(c)
print('PASS: missing scope, exceeded limits, missing context evidence and invented bound rejected; all valid scopes accepted.')

validate_reuse = checks['check_additional_gs_groups']
reuse_cases = []
c = copy.deepcopy(cards['MA-014']); c['additional_gs_target_groups'][0]['operator'] = 'Kennen'; reuse_cases.append(c)
c = copy.deepcopy(cards['MA-014']); c['additional_gs_target_groups'][0]['target_ids'][0] = 'page912_1833'; reuse_cases.append(c)
c = copy.deepcopy(cards['MA-014']); c['additional_gs_target_groups'][0]['covered_ids'].append('page912_1842'); reuse_cases.append(c)
c = copy.deepcopy(cards['MA-014']); c['source_ids'].remove('Q-MA-page912_1846'); reuse_cases.append(c)
for c in reuse_cases:
    try:
        validate_reuse(c)
    except (AssertionError, KeyError):
        pass
    else:
        raise AssertionError('Invalid reused GS evidence accepted: ' + c['id'])
for c in cards.values():
    validate_reuse(c)
print('PASS: reused GS evidence preserves parent/operator/source and separates coverage from context.')
