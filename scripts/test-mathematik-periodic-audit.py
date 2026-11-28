"""MA-151 internal boundary audit; no learner-task generation or app changes."""
import json
from itertools import product


def values(start, plus, minus, length):
    result = [start]
    for i in range(length):
        result.append(result[-1] + plus if i % 2 == 0 else result[-1] - minus)
    return result


count = valid = missed_by_endpoint_check = 0
for start, plus, minus in product(range(21), repeat=3):
    row = values(start, plus, minus, 8)
    for i, actual in enumerate(row):
        k, phase = divmod(i, 2)
        assert actual == start + k * (plus - minus) + phase * plus
    for length in range(2, 9):
        chosen = row[:length + 1]
        fits = all(0 <= value <= 20 for value in chosen)
        endpoint_fits = 0 <= chosen[-1] <= 20
        count += 1
        valid += fits
        missed_by_endpoint_check += endpoint_fits and not fits
        # Start-only perturbation is constant only with every sign, operand and phase fixed.
        for delta in (-1, 1):
            changed = values(start + delta, plus, minus, length)
            assert all(v - u == delta for u, v in zip(chosen, changed))
            permitted = all(0 <= v <= 20 for v in changed)
            assert permitted == all(-delta <= v <= 20 - delta for v in chosen)

assert missed_by_endpoint_check > 0
for maximum in (20, 100, 1000):
    # Endpoint returns into range although the first intermediate value is outside it.
    row = values(maximum, 1, 1, 2)
    assert row[-1] == maximum and row[1] > maximum
    assert values(0, 0, 0, 30) == [0] * 31
    assert values(0, 2, 1, 3) != values(0, 1, 2, 3)

print(json.dumps({'status':'passed','exhaustive_frame':20,
    'ordered_start_and_operand_triples':21**3,
    'finite_prefix_cases':count,'valid_prefix_cases':valid,
    'endpoint_only_false_acceptances':missed_by_endpoint_check,
    'additional_boundary_frames':[20,100,1000],
    'limits':'Lengths2..8 and zero-test30 are audit samples, not curricular limits. Fixed known phase and operands only; not a proof of a curricular connection.'},ensure_ascii=False))
