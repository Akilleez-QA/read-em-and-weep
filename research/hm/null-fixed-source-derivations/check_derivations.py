"""Pure label/mask controls. No physical/source/jet arithmetic or imports."""
from collections import defaultdict

count = 0

def require(condition, message):
    global count
    if not condition:
        raise RuntimeError(message)
    count += 1

# On an invented function label z, expand [sum f_i D_i, D_j]z.
# Commuting D labels are sorted; first coefficient derivatives are labels.
for j in range(4):
    terms = defaultdict(int)
    for i in range(4):
        terms[(('f', i), ('D2z', tuple(sorted((i, j)))))] += 1
        terms[(('Df', j, i), ('Dz', i))] -= 1
        terms[(('f', i), ('D2z', tuple(sorted((i, j)))))] -= 1
    actual = {t: c for t, c in terms.items() if c}
    expected = {(('Df', j, i), ('Dz', i)): -1 for i in range(4)}
    require(actual == expected, 'Wrong vector-field commutator')
    require(actual != {t: -c for t, c in expected.items()}, 'Sign mutation undetected')

# An operator coefficient with character s followed by D_i shifts masks by s XOR e_i.
# [operator, full-sign projector] on mask m has this scalar multiplier.
def commutator_multiplier(m, shift):
    return int(m == 15) - int((m ^ shift) == 15)

for i in range(4):
    e = 1 << i
    for s in range(16):
        shift = s ^ e
        values = [commutator_multiplier(m, shift) for m in range(16)]
        require(all(v == 0 for v in values) == (s == e), 'Character criterion failed')
        for m in range(16):
            # Conjugation identity for every abstract deck element g.
            for g in range(16):
                sign_in = (-1) ** ((m & g).bit_count())
                sign_out = (-1) ** (((m ^ shift) & g).bit_count())
                sign_operator = (-1) ** ((shift & g).bit_count())
                require(sign_out == sign_in * sign_operator, 'Deck conjugation sign failed')
    require(any(commutator_multiplier(m, e) for m in range(16)), 'V_i false zero')
    require(all(commutator_multiplier(m, e ^ e) == 0 for m in range(16)),
            'Twisted constant counterexample failed')

# f^(i) has character full XOR e_i; D_j toggles precisely e_j.
for i in range(4):
    witness_mask = 15 ^ (1 << i)
    require(witness_mask != 15, 'Witness projected incorrectly')
    retained = [j for j in range(4) if (witness_mask ^ (1 << j)) == 15]
    require(retained == [i], 'Witness did not isolate its coefficient')

# An added invariant parameter derivative is a nonzero abstract operator with zero shift.
require(all(commutator_multiplier(m, 0) == 0 for m in range(16)),
        'Invariant parameter derivative falsely excluded')
print(f'PASS: {count} formal label/character checks; no production execution.')
