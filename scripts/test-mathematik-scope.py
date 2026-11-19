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

# A limit explicitly stated in a subordinate target must not be relabelled
# as a stage-goal inference or moved to an unproven parent/sibling target.
validate_range = checks['check_number_range_alignment']
range_cases = []
c = copy.deepcopy(cards['MA-030']); c['number_range_alignment']['fsp_source_id'] = 'page139_37851'; range_cases.append(c)
c = copy.deepcopy(cards['MA-030']); c['number_range_alignment']['fsp_source_id'] = 'page139_37908'; range_cases.append(c)
c = copy.deepcopy(cards['MA-030']); c['number_range_alignment']['fsp_basis'] = 'stage_goal_context'; range_cases.append(c)
c = copy.deepcopy(cards['MA-030']); c['number_range_alignment']['fsp_max'] = 100; range_cases.append(c)
c = copy.deepcopy(cards['MA-031']); c['fsp_scope']['source_ids'] = ['Q-MA-page139_37863']; range_cases.append(c)
c = copy.deepcopy(cards['MA-031']); del c['number_range_alignment']['fsp_basis']; range_cases.append(c)
c = copy.deepcopy(cards['MA-030']); c['number_range_alignment'].update(fsp_basis='stage_goal_context', fsp_source_id='page139_37739'); c['context_source_ids'] = ['Q-MA-page139_37739']; range_cases.append(c)
for c in range_cases:
    try:
        validate_range(c)
    except (AssertionError, KeyError):
        pass
    else:
        raise AssertionError('Invalid target-row range provenance accepted: ' + c['id'])
for c in cards.values():
    validate_range(c)
print('PASS: explicit target-row bounds reject wrong parents, foreign anchors, stage-goal relabelling and inconsistent limits.')

# Elective evidence must not silently become an unconditional planning target.
validate_elective = checks['check_fsp_elective_requirement']
elective_cases = []
c = copy.deepcopy(cards['MA-040']); del c['fsp_elective_requirement']; elective_cases.append(c)
c = copy.deepcopy(cards['MA-040']); c['fsp_elective_requirement']['required'] = False; elective_cases.append(c)
c = copy.deepcopy(cards['MA-040']); c['fsp_scope']['planning_rule'] = 'Nur bis 20.'; elective_cases.append(c)
c = copy.deepcopy(cards['MA-040']); c['fsp_elective_requirement']['area_id'] = 'MA-page139_37744'; elective_cases.append(c)
for c in elective_cases:
    try:
        validate_elective(c)
    except (AssertionError, KeyError):
        pass
    else:
        raise AssertionError('Invalid elective prerequisite accepted: ' + c['id'])
for c in cards.values():
    validate_elective(c)
print('PASS: missing, disabled, hidden or wrongly sourced elective prerequisites rejected.')


# Missing operator evidence must not produce a guessed level or erase a real one.
validate_operator = checks['check_operator_evidence']
parent = checks['anchors']['page139_35456']
cases = []
c = copy.deepcopy(cards['MA-084']); c['fsp_operator'] = 'Anwenden'; cases.append(c)
c = copy.deepcopy(cards['MA-084']); del c['fsp_operator_evidence']; cases.append(c)
c = copy.deepcopy(cards['MA-084']); c['fsp_operator_evidence']['source_ids'] = ['Q-MA-page139_35554']; cases.append(c)
c = copy.deepcopy(cards['MA-084']); c['fsp_operator_evidence']['parent_target_id'] = 'page139_35451'; cases.append(c)
c = copy.deepcopy(cards['MA-084']); c['fsp_operator_evidence']['status'] = 'explicit'; cases.append(c)
for c in cases:
    try:
        validate_operator(c, 'fsp', parent)
    except (AssertionError, KeyError):
        pass
    else:
        raise AssertionError('Invalid operatorless source evidence accepted')
for c in cards.values():
    for side in ['gs', 'fsp']:
        validate_operator(c, side, checks['anchors'][c[side + '_target_ids'][0]])
c = copy.deepcopy(cards['MA-001']); c['fsp_operator'] = None
try:
    validate_operator(c, 'fsp', checks['anchors'][c['fsp_target_ids'][0]])
except AssertionError:
    pass
else:
    raise AssertionError('Explicit source operator may not be erased')
print('PASS: operatorless content requires reviewed evidence; invented, foreign and erased operators rejected.')

# A main target with a remark needs no invented subordinate row.
validate_primary = checks['check_primary_target_group']
single_cases = []
c = copy.deepcopy(cards['MA-091']); del c['fsp_single_row_evidence']; single_cases.append(c)
c = copy.deepcopy(cards['MA-091']); c['fsp_single_row_evidence']['target_id'] = 'page139_35554'; single_cases.append(c)
c = copy.deepcopy(cards['MA-091']); c['fsp_single_row_evidence']['remark_excerpt'] = 'Allgemeines Kartenlesen'; single_cases.append(c)
c = copy.deepcopy(cards['MA-091']); c['fsp_single_row_evidence']['source_id'] = 'Q-MA-page139_35563'; single_cases.append(c)
c = copy.deepcopy(cards['MA-091']); c['fsp_target_ids'] = ['page139_35563']; single_cases.append(c)
c = copy.deepcopy(cards['MA-091']); c['fsp_target_ids'] = []; single_cases.append(c)
c = copy.deepcopy(cards['MA-091']); c['fsp_target_ids'] *= 2; single_cases.append(c)
for c in single_cases:
    try:
        validate_primary(c, 'fsp')
    except (AssertionError, KeyError):
        pass
    else:
        raise AssertionError('Invalid single-row evidence accepted: ' + c['id'])
for c in cards.values():
    for side in ['gs', 'fsp']:
        validate_primary(c, side)
print('PASS: single main targets require matching remark evidence; missing, foreign, invented, child-only, empty and duplicate evidence rejected.')

# Gestalten is an official level, but must belong to the actual main row.
check_level = checks['check_operator_evidence']
for cid in ['MA-093', 'MA-094']:
    c = cards[cid]
    parent = checks['anchors'][c['fsp_target_ids'][0]]
    check_level(c, 'fsp', parent)
    for wrong in ['Kennen', 'Übertragen', 'Erkennen', 'Darstellen']:
        broken = copy.deepcopy(c); broken['fsp_operator'] = wrong
        try: check_level(broken, 'fsp', parent)
        except AssertionError: pass
        else: raise AssertionError('Wrong level or child action accepted: ' + wrong)
    broken_parent = copy.deepcopy(parent); broken_parent['target'] = 'Merkmale von Rechtecken'
    try: check_level(c, 'fsp', broken_parent)
    except AssertionError: pass
    else: raise AssertionError('Gestalten accepted without main-row evidence')
print('PASS: evidenced Gestalten accepted; borrowed levels and child actions rejected.')
