#!/usr/bin/env python3
"""Fixed provenance/representation checks; not an actual-map evaluation."""
from pathlib import Path
from collections import Counter
import hashlib
import json

ROOT = Path(__file__).resolve().parent

def require(condition, message):
    if not condition:
        raise RuntimeError(message)

inputs = json.loads((ROOT / 'INPUTS.json').read_text())
for rec in inputs:
    data = (ROOT / rec['file']).read_bytes()
    require(len(data) == rec['bytes'], 'byte length: ' + rec['file'])
    require(hashlib.sha256(data).hexdigest() == rec['sha256'], 'SHA256: ' + rec['file'])
    blob = b'blob ' + str(len(data)).encode() + b'\0' + data
    require(hashlib.sha1(blob).hexdigest() == rec['git_blob_sha1'], 'Git blob: ' + rec['file'])

# Universal SL2 characters as polynomials in the trace x of W.
# This checks W Sym3 W = Sym2 W + Sym4 W without evaluating a group element.
sym2 = [-1, 0, 1]
sym3 = [0, -2, 0, 1]
sym4 = [1, 0, -3, 0, 1]
lhs = [0] + sym3
rhs = [(sym2[i] if i < len(sym2) else 0) + sym4[i] for i in range(5)]
require(lhs == rhs, 'fixed Clebsch-Gordan polynomial identity')

source = Counter({'A_std': 1, 'V': 2, 'P': 3, 'D': 4})
target_direct = Counter({'A_std': 1}) + Counter({'A_std': 1, 'D': 1})
target_dual = Counter({'A_std': 1, 'D': 1}) + Counter({'A_std': 1})
dim = {'A_std': 3, 'V': 3, 'P': 4, 'D': 5}
require(target_direct == target_dual == Counter({'A_std': 2, 'D': 1}), 'two cohomology computations agree')
require(sum(dim[r] * n for r, n in source.items()) == 41, 'source dimension')
require(sum(dim[r] * n for r, n in target_direct.items()) == 11, 'target dimension')
require(target_direct['A_std'] > source['A_std'], 'strict multiplicity obstruction')

# Fixed dimensions, twists and Euler-characteristic sanity checks.
quotient_blocks = [(2, 3), (1, 2), (1, -8)]
dual_twist_blocks = [(rank, -degree - 2) for rank, degree in quotient_blocks]
require(dual_twist_blocks == [(2, -5), (1, -4), (1, 6)], 'dual cotangent twist')
require(sum(r for r, e in quotient_blocks) == 4, 'rank A_q')
require(sum(r * e for r, e in quotient_blocks) == 0, 'degree A_q')
require(sum(r * e for r, e in dual_twist_blocks) == -8, 'degree A_q dual minus two')
require(sum(r * max(e + 1, 0) for r, e in quotient_blocks) == 11, 'H0 A_q dimension')
require(sum(r * max(-e - 1, 0) for r, e in dual_twist_blocks) == 11, 'H1 dual target dimension')
require(13 - 54 == -41, 'actual S Euler characteristic')

# Executed fixed mutations: each must remove this particular multiplicity
# obstruction, without making any geometric occurrence claim.
def violates(required, available):
    return any(n > available[r] for r, n in required.items())
require(violates(target_direct, source), 'original case must obstruct')
source_two_A = source.copy()
source_two_A['A_std'] = 2
require(not violates(target_direct, source_two_A), 'mutation adding second A must remove obstruction')
drop_O2 = Counter({'A_std': 1, 'D': 1})
require(not violates(drop_O2, source), 'mutation deleting O(2) must remove obstruction')

# For the physical other doublet, use only the three fixed McKay identities:
# W Wp=P, W P=T+Wp, W T=D+V+P. They give Wp Sym2=T and
# Wp Sym3=(D+V+P)-P=D+V. No source instance is evaluated.
W_times_P = Counter({'T': 1, 'Wp': 1})
Wp_sym2 = W_times_P.copy()
Wp_sym2.subtract(Counter({'Wp': 1}))
require(+Wp_sym2 == Counter({'T': 1}), 'fixed Wp Sym2 identity')
Wp_sym3 = Counter({'D': 1, 'V': 1, 'P': 1})
Wp_sym3.subtract(Counter({'P': 1}))
require(+Wp_sym3 == Counter({'D': 1, 'V': 1}), 'fixed Wp Sym3 identity')
replace_W_by_Wp = (+Wp_sym3) + Counter({'A_std': 1})
require(not violates(replace_W_by_Wp, source), 'mutation W to Wp must not falsely exclude')
mutations = {
    'add_second_A_std_to_M2': 'This multiplicity obstruction disappears.',
    'drop_O2_from_A_q': 'This multiplicity obstruction disappears.',
    'replace_W_by_Wp': 'This multiplicity obstruction disappears: required character is A_std+D+V.'
}

result = {
    'authenticated_inputs': len(inputs),
    'fixed_character_identity': 'W tensor Sym3 W = Sym2 W + Sym4 W',
    'H1_S': dict(source),
    'H0_A_q_and_H1_A_q_dual_minus2': dict(target_direct),
    'A_std_source_multiplicity': source['A_std'],
    'A_std_required_multiplicity': target_direct['A_std'],
    'contradiction': True,
    'fixed_rank_degree_twist_checks': True,
    'executed_mutations': mutations,
    'defect_assumption': 'None: coherent sheaf injection and torsion-safe dual argument.',
    'scope': 'Excludes maxdeg(A_q)=3 in the imported actual rank-four maximal ordered profile (1,1), not higher-top branches or a global rank theorem.',
    'verification_boundary': 'This checks immutable input bytes and fixed representation arithmetic. It does not certify the imported geometric premises or the written coherent-image proof.'
}
print(json.dumps(result, indent=2))
