"""Seed30 E34 symbolic recurrence contract. No physical arithmetic entry point."""
import hashlib
import importlib
import json
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from package_snapshot import package_path
import sys

RELEASE = '6e28c6b59f8245779f6c03a20798e4de6842ae19'
SOURCE = '08b73637d4136f91606aad332c46cafd064417f8'
PUBLIC = package_path()
MANIFEST_SHA = 'ec0746ba0d537ec3edeb96f396a02e426225e904227e4c500dad0f5e0d3fbb64'


def public_modules():
    """Authenticate the explicit release before importing its two inert binders."""
    raw = (PUBLIC / 'release-manifest.json').read_bytes()
    if hashlib.sha256(raw).hexdigest() != MANIFEST_SHA:
        raise ValueError('release manifest changed')
    manifest = json.loads(raw)
    for name, digest in manifest['files_sha256'].items():
        path = (PUBLIC / name).resolve()
        if not path.is_relative_to(PUBLIC) or hashlib.sha256(path.read_bytes()).hexdigest() != digest:
            raise ValueError('unsupported or changed release file: ' + name)
    sys.dont_write_bytecode = True
    names = ('owned_scalar_denominator_binding', 'outer_partition_source_binding')
    for name in names:
        if name in sys.modules and Path(sys.modules[name].__file__).resolve() != PUBLIC / (name + '.py'):
            raise ValueError('foreign module already loaded: ' + name)
    sys.path.insert(0, str(PUBLIC))
    try:
        modules = tuple(importlib.import_module(name) for name in names)
    finally:
        sys.path.pop(0)
    for module, name in zip(modules, names):
        if Path(module.__file__).resolve() != PUBLIC / (name + '.py'):
            raise ValueError('module origin mismatch')
    modules[1].authenticate_public_sources()
    return modules


def build():
    owned, outer = public_modules()
    triples = ((0, 0, 0), (1, 1, 8), (2, 3, 12), (3, 7, 14), (4, 15, 15))
    vertices = tuple(owned.VertexLabel(30, i, *triple) for i, triple in enumerate(triples))
    partitions = []
    for v in vertices:
        chart = outer.PartitionChart(v.standard_tag)
        if v.carrier != chart.s:
            raise ValueError('this contract supports only its five fixed diagonal carriers')
        partitions.append({
            'owner': v.data(), 'N': 54, 'P': 29, 's': chart.s,
            'M': chart.M, 'T': chart.threshold, 'L': chart.L,
            'outer_reference': outer.bind_reference(v),
            'earlier_composition_ranges': [[0, chart.threshold - 1]] * chart.s,
            'final_n': 'L-r; r=sum(n_i for i<s)',
            'r_range': [0, chart.s * (chart.threshold - 1)],
            'B_s_special_case': '1' if chart.s in (0, 4) else 'symbolic divided-power diagonal',
        })
    return {
        'schema': 'A04-seed30-partition-demand-v1',
        'release_pin': RELEASE, 'immutable_source_pin': SOURCE,
        'reviewer': ['A03', 'V06'], 'artifact_review': 'pending',
        'domain': {'seed': 30, 'channel': 'E34(T12 F12)', 'row': 7,
                   'entry': [0, 0], 'terminal_block': 'M20',
                   'terminal_exponent': [-1, -2, -3, -4],
                   'effective_word_coefficient': 1, 'orientation': 1,
                   'owners': [v.data() for v in vertices],
                   'standard_bits': 'high bit 3-i', 'legal_bits': 'low bit i',
                   'anchors_0_1_2': 'Boolean UNKNOWN; not nonzero'},
        'partitions': partitions,
        'prefix_kernel': {
            'left': [['H0', 0], ['I', 1], ['P', 1], ['I', 2]],
            'right': [['P', 2], ['H1', 1]],
            'left_row': 0, 'right_column': 0,
            'pairing': 'sum_(u,v=0..1) left[0,u]*Rbar[v,u]*right[v,0]',
            'block_denominator_occurrences': [[0, 'dh', 1], [1, 'di', 1],
                [1, 'dp', 1], [1, 'dh', 1], [2, 'di', 1], [2, 'dp', 1]],
            'denominator_scope': 'prefix selector only; add branch current/scalar/derivative/weight ledgers before clearance',
            'carrier0_dh': 'unreduced pinned charts[0].dh reference; no -h0 substitution admitted',
            'weighted_owners': [0, 1, 2, 3, 4], 'tail_owners': [2, 3, 4],
            'frame': 'common original resolution frame; normalized Rbar after matching conjugation exactly once',
            'physical_logarithmic_Q_terms_required': True,
        },
        'recurrence': {
            'coefficient_ring': 'commutative characteristic zero; formula is integral via binomial recurrence',
            'variables': 'u=(owner local finite x, infinity t); z auxiliary divided-power variable',
            'factor': 'f_i,n=c_i^n*v_i^(n-T*[i=j]); c_i=(-1)^(s-i)*H_(s-i)(finite coordinates)',
            'allowed_n': 'i<j:0<=n<T; i=j:T<=n<=L; i>j:0<=n<=L',
            'GF': 'B_j=L! [z^L] product_i sum_(allowed n) f_i,n*z^n/n!',
            'state': 'C_i(ell,alpha)=ell! [z^ell u^alpha] product_(h<i) F_h',
            'base': 'C_0(0,0)=1; all other C_0=0',
            'step': 'C_(i+1)(ell,alpha)=sum_(allowed n<=ell) binom(ell,n) sum_beta coeff(f_i,n,beta)*C_i(ell-n,alpha-beta)',
            'result': 'coeff(B_j,alpha)=C_(s+1)(L,alpha)',
            'diagonal': 'For this request j=s: cache earlier C_s(r,gamma); n_s=L-r. Read C_(s+1)(L,alpha) by convolution with f_s,L-r, without generating compositions.',
            'cache_key': '(release,full owner,partition tag,N,P,j,i,ell,alpha,frame,derivative multiindex)',
            'polynomial_zero_boundary': 'ell<0 or ell>L or any alpha_i<0 is zero; missing support is unresolved',
            'all_infinity': 's=4: c0=c1=c2=c3=0,c4=1,v4=1; only n4=L survives. B4=1. Primary b<4 has weight zero; auxiliary5 is outside this request and is not declared zero.',
        },
        'demand_transport': {
            'product': 'Demand(FG,kappa) -> {(F,beta),(G,kappa-beta): beta in certified supp(F), kappa-beta in certified supp(G)}',
            'matrix': 'preserve ordered products and sum all contracted entry indices; cache equal typed coefficient requests',
            'prefix': 'push terminal kappa through left/right and all five outer weights; four E34 branches share prefix coefficient states',
            'E34_branches': [
                {'edge': [3,4], 'scalar_derivative': 2, 'current': ['L',3], 'sign': 1},
                {'edge': [3,4], 'scalar_derivative': 3, 'current': ['L',2], 'sign': -1},
                {'edge': [2,3], 'scalar_derivative': 3, 'current': ['U',2], 'sign': 1},
                {'edge': [2,3], 'scalar_derivative': 2, 'current': ['U',3], 'sign': -1}],
            'E34_common_factor': '1/2; coordinates zero-based; scalar is the combined canceled T12 F12 quotient',
            'derivative_finite': 'coeff(partial_i F,beta)=(beta_i+1)*coeff(F,beta+e_i)',
            'infinity_warning': 'use global finite derivative and character conversion; never replace it with local partial_t',
            'signed_pullback': 'kappa=a+sum_o epsilon_o*b_o-m; epsilon_oi=1-2*standard_bit_oi; m is authenticated owner homogeneous/frame shift, not guessed',
            'order': 'cancel combined inserted-owner quotients before differentiating; pull frames once; demand convolution last',
        },
        'unresolved': ['source-bound full A02 branch DAG and exact inner prism owner ledger',
            'carrier0 dh clearance proof; full branch denominator maxima and standard/frame shift',
            'certified support/predecessor closure for physical leaves and coefficient schedule'],
        'next_step': 'A03/V06 review recurrence; attach A02 exact branch/owner/frame ledger before instantiating physical predecessor sets',
        'gates': {key: False for key in ('source_admitted', 'pole_domain_proved',
            'physical_polynomial_expansion', 'physical_polynomial_evaluation',
            'arithmetic_cost_certificate', 'execution_release')},
    }


if __name__ == '__main__':
    print(json.dumps(build(), indent=2, sort_keys=True))
