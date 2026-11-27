"""Internal arithmetic audit for MA-150; no learner tasks or generated app data."""
from math import comb
import json


def fibonacci_coefficient(n):
    if n == 0:
        return 0
    return sum(comb(n - 1 - k, k) for k in range((n - 1) // 2 + 1))


def prefix(a, b, new_terms):
    values = [a, b]
    for _ in range(new_terms):
        values.append(values[-2] + values[-1])
    return values


results = []
for maximum in (20, 100):
    checked = valid = 0
    for a in range(maximum + 1):
        for b in range(maximum + 1):
            values = prefix(a, b, 8)
            for j in range(2, len(values)):
                # Independent binomial expression for the recurrence coefficients.
                assert values[j] == fibonacci_coefficient(j - 1) * a + fibonacci_coefficient(j) * b
            # For nonnegative starts all later terms are nondecreasing from index2.
            assert all(values[j] >= values[j - 1] for j in range(2, len(values)))
            for new_terms in range(2, 9):
                chosen = values[:new_terms + 2]
                fits = all(0 <= v <= maximum for v in chosen)
                assert fits == (chosen[-1] <= maximum)
                checked += 1
                valid += fits
            # Two new terms require a+2b<=M, not merely a,b<=M.
            assert (max(values[:4]) <= maximum) == (a + 2 * b <= maximum)
    results.append(dict(maximum=maximum,ordered_start_pairs=(maximum + 1)**2,
                        finite_prefix_cases=checked,valid_prefix_cases=valid))

for maximum in (20, 100, 1000):
    assert prefix(maximum, 0, 2) == [maximum, 0, maximum, maximum]
    assert prefix(0, maximum, 2)[-1] > maximum
    assert prefix(0, 0, 30) == [0] * 32
    # Start perturbations propagate recursively, not as a constant offset.
    differences = [v - u for u, v in zip(prefix(0, 0, 6), prefix(1, 0, 6))]
    assert differences == [1, 0, 1, 1, 2, 3, 5, 8]
    assert max(differences) <= maximum

print(json.dumps({'status':'passed','exhaustive_frames':results,
    'boundary_frames':[20,100,1000],
    'test_lengths_only':'2..8 new terms; this is a test sample, not a curricular length limit',
    'findings':'All generated terms match independent coefficients. Start bounds alone are insufficient. Zero starts impose no universal maximum length. Start changes do not create a constant offset.'},ensure_ascii=False))
