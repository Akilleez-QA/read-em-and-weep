#!/usr/bin/env python3
"""Finite combinatorial specification only; never imports/evaluates physical sources."""
import argparse
import hashlib
import itertools
import json
import sys
from dataclasses import dataclass, replace

SCHEMA = 'hm-refined-detector-metadata-v1'
MAX_OUTPUT_BYTES = 24576
MAX_SEEDS = 78
OUTER = ('outer', 54, 29)
INNER = ('inner', 14, 1)
ROWS = (
    (2, 'CCBB', (-1,-2,-2,-2), 'M11', 9,3,1),
    (2, 'CCBB', (-1,-2,-2,-2), 'M11',10,4,1),
    (2, 'CCBB', (-1,-2,-2,-2), 'M11',12,6,-2),
    (3, 'CCCB', (-1,-2,-3,-3), 'M10',0,3,1),
    (3, 'CCCB', (-1,-2,-3,-3), 'M10',2,6,2),
    (3, 'CCCB', (-1,-2,-3,-3), 'M21',10,1,1),
    (3, 'CCCB', (-1,-2,-3,-3), 'M21',12,5,2),
    (4, 'CCCC', (-1,-2,-3,-4), 'M20',0,0,-1),
    (4, 'CCCC', (-1,-2,-3,-4), 'M31',10,0,1),
)

class ContractError(ValueError):
    pass


def require(ok, message):
    if not ok:
        raise ContractError(message)


def parity(p):
    return -1 if sum(p[i] > p[j] for i in range(len(p))
                     for j in range(i+1,len(p))) % 2 else 1


def staircase(cell, permutation):
    active = tuple(i for i,s in enumerate(cell) if s == 'C')
    require(tuple(sorted(permutation)) == active, 'bad staircase permutation')
    bits = [int(s == 'B') for s in cell]
    vertices = [sum(b << (3-i) for i,b in enumerate(bits))]
    for i in permutation:
        bits[i] = 1
        vertices.append(sum(b << (3-j) for j,b in enumerate(bits)))
    require(all(a < b for a,b in zip(vertices,vertices[1:])),
            'staircase must be increasing in standard order')
    return tuple(vertices)


def seed_records():
    seeds=[]
    for row_id,row in enumerate(ROWS):
        q,cell,_,_,_,_,coefficient=row
        for perm in itertools.permutations(range(q)):
            require(len(seeds) < MAX_SEEDS, 'seed metadata cap')
            seeds.append({'row':row_id,'standard':staircase(cell,perm),
                          'orientation':parity(perm),
                          'coefficient':coefficient*parity(perm),
                          'lift_depth':q-2})
    require(len(seeds)==78, 'terminal seed count mismatch')
    return seeds


@dataclass(frozen=True)
class OwnerState:
    """Kernel owners persist when a face no longer evaluates at that vertex."""
    active: tuple
    kernel_owners: frozenset
    weighted_owners: frozenset
    required_prefix: frozenset = frozenset()

    def validate(self):
        require(set(self.active) <= self.weighted_owners, 'unweighted active owner')
        require(self.kernel_owners <= self.weighted_owners, 'unweighted kernel owner')
        require(self.required_prefix <= self.kernel_owners, 'dropped prefix owner')
        require(len(set(self.active)) == len(self.active), 'duplicate common vertex')
        return self


def initial_owners(n):
    require(3 <= n <= 5, 'outer tuple degree unsupported')
    labels=tuple('o'+str(i) for i in range(n))
    return OwnerState(labels,frozenset(),frozenset(labels)).validate()


def homotopy_adjoint(state, internal_degree):
    state.validate()
    require(internal_degree in (0,-1), 'unexpected homotopy input degree')
    require(state.active, 'empty homotopy tuple')
    owner=state.active[0]
    out=replace(state,kernel_owners=state.kernel_owners|{owner},
                required_prefix=state.required_prefix|{owner})
    return out.validate(), (1, 1 if internal_degree==0 else -1)


def cech_face(state, delete):
    state.validate()
    require(0 <= delete < len(state.active), 'bad face index')
    out=replace(state,active=state.active[:delete]+state.active[delete+1:])
    return out.validate(), (-1 if delete%2 else 1)


def include_adjoint(state):
    state.validate()
    require(len(state.active)==3,'inclusion expects residual triple')
    return replace(state,kernel_owners=state.kernel_owners|{state.active[0]}).validate()


def check_partition(tag, role):
    require(role in ('outer','inner'), 'unknown partition role')
    require(tuple(tag)==(OUTER if role=='outer' else INNER), 'partition tag mismatch')


def check_standard_projection(target_standard, sampled_standard):
    require(tuple(target_standard)==tuple(sampled_standard), 'standard tag mismatch')


def check_source_assumptions(assumptions):
    require(set(assumptions) <= {'universal_dual_rows','source_first_order',
                                'owned_denominators','fresh_domain_54_29'},
            'unsupported old source sparsity assumption')


@dataclass(frozen=True)
class RationalState:
    partition: tuple
    phase: str
    inserted_carrier: int
    suffix_carrier: int
    suffix_legal: int
    standard_boundary: int
    cancellation_witness: str = ''
    derivative_count: int = 0


def raw_inner():
    return RationalState(INNER,'rational_pending',14,14,1,5250)


def cancel_inserted(state, witness):
    check_partition(state.partition,'inner')
    require(state.phase=='rational_pending','cancellation phase mismatch')
    require(witness=='N14-owned-polynomial-quotients', 'missing exact quotient witness')
    return replace(state,phase='inserted_canceled',inserted_carrier=0,
                   cancellation_witness=witness)


def differentiate_regularized(state):
    check_partition(state.partition,'inner')
    require(state.phase=='inserted_canceled' and state.inserted_carrier==0,
            'derivative before inserted cancellation')
    require(state.cancellation_witness=='N14-owned-polynomial-quotients',
            'derivative without quotient witness')
    require(state.derivative_count==0,'only one complementary derivative allowed')
    return replace(state,phase='differentiated_regularized',
                   suffix_carrier=state.suffix_carrier+1,
                   suffix_legal=state.suffix_legal+1,
                   standard_boundary=state.standard_boundary+1,derivative_count=1)


def outer_domain_check(state, tag, target_standard, sampled_standard):
    check_partition(tag,'outer')
    check_partition(state.partition,'inner')
    require(state.cancellation_witness=='N14-owned-polynomial-quotients',
            'outer domain missing quotient witness')
    require(state.derivative_count==1,'outer domain requires exactly one derivative')
    check_standard_projection(target_standard,sampled_standard)
    require(state.phase=='differentiated_regularized','unprepared derivative domain')
    require(state.inserted_carrier==0,'inserted pole survived cancellation')
    require(state.suffix_carrier<=15 and state.suffix_legal<=2,
            'scalar derivative exceeds proved domain')
    require(state.standard_boundary<=5251,'standard boundary bound exceeded')
    return {'domain':'symbolically_certified','carrier_cap':54,'legal_cap':29,
            'standard_factors':'actual_target_units',
            'computational_cancellation':'uninstantiated_leaf_circuits'}


def tensor_h_adjoint(n, states, exponents):
    """Returns at most four atoms; no source coefficients exist here."""
    require(len(n)==len(states)==len(exponents)==4,'tensor arity')
    require(all(x in (0,-2) for x in n),'unsupported twist')
    require(all(s in 'ABC' for s in states),'bad chart state')
    out=[]
    for j in range(4):
        ss=list(states)
        valid=True
        for i in range(j):
            if n[i]==0:
                valid &= states[i] in 'AB' and exponents[i]==0
                ss[i]='B'
            else:
                valid &= states[i]=='C' and exponents[i]==-1
        if not valid:
            continue
        if states[j]=='A' and exponents[j]>=0:
            local=-1
        elif states[j]=='B' and exponents[j]<0 and exponents[j]<=n[j]:
            local=1
        else:
            continue
        ss[j]='C'
        sign=local*(-1 if sum(s=='C' for s in states[:j])%2 else 1)
        out.append({'pivot':j,'states':''.join(ss),'exponents':tuple(exponents),
                    'coefficient':sign})
    return out


def derivative_demand(exponents, i):
    require(len(exponents)==4 and 0<=i<4,'derivative arity')
    coefficient=exponents[i]+1
    if coefficient==0:
        return None
    shifted=list(exponents);shifted[i]+=1
    return {'exponents':tuple(shifted),'coefficient':coefficient}


def build_certificate():
    check_source_assumptions({'universal_dual_rows','source_first_order',
                             'owned_denominators','fresh_domain_54_29'})
    state=initial_owners(5)
    state,_=homotopy_adjoint(state,-1)
    state,_=cech_face(state,0)  # removed prefix must remain owned and weighted
    state,_=homotopy_adjoint(state,0)
    state,_=cech_face(state,0)
    state=include_adjoint(state)
    derivative=differentiate_regularized(cancel_inserted(raw_inner(),
                                'N14-owned-polynomial-quotients'))
    domain=outer_domain_check(derivative,OUTER,(0,3,15),(0,3,15))
    return {
      'schema':SCHEMA,
      'status':'finite_metadata_specification_only',
      'execution_release':False,'physical_source_evaluated':False,
      'complete_arithmetic_contract':False,
      'metadata_policy':{'max_output_bytes':MAX_OUTPUT_BYTES,'max_seeds':MAX_SEEDS,
                         'huge_support_enumeration':False},
      'source_order':'original_source_vertex_then_standard_vertex',
      'partitions':{'outer':OUTER,'inner':INNER,'projection':'same_r_standard_tag'},
      'terminal_rows':[{'q':r[0],'cell':r[1],'exponent':r[2],
                        'entry':[r[3],r[4],r[5]],'coefficient':r[6]} for r in ROWS],
      'seed_count':78,'seeds':seed_records(),
      'raw_kernel_path_bound_before_outer_labels':4038,
      'raw_kernel_path_bound_formula':'6+24*2*4+48*2*5*2*4',
      'raw_kernel_paths_enumerated':False,
      'lift_templates':[
        {'q':2,'sign':1,'adjoint_nodes':['include']},
        {'q':3,'sign':1,'adjoint_nodes':['H(input_degree=0)','face(0..3)','include']},
        {'q':4,'sign':-1,'adjoint_nodes':['H(input_degree=-1)','face(0..4)',
                         'H(input_degree=0)','face(0..3)','include']}],
      'node_equations':{
        'H_adjoint':'W H + (-1)^r H W(IP); owner=current_tuple_first',
        'include_adjoint':'(P W I)^t; owner=residual_triple_first',
        'face':'(-1)^index; retain all prior kernel and weight owners',
        'E_adjoint':[['jk','a','L_b',1,2],['jk','b','L_a',-1,2],
                     ['ij','b','U_a',1,2],['ij','a','U_b',-1,2]],
        'U':'L_ik-L_ij',
        'derivative':'kappa->kappa+unit_i, multiplier=kappa_i+1',
        'weighted_derivative':'kappa-nu+unit_i, multiplier=kappa_i-nu_i+1',
        'h_adjoint':'exact executable chart/exponent filters in tensor_h_adjoint',
        'Pi':'symbolic bounded label sum; sort source-first with sign',
        'Hrho':[['b0,a0,a1','rho0',1],['b0,b1,a1','rho0*rho1',-1]],
        'K_edge':'[b,e0,e1]-sum reverse_coordinate_path [b,vprev,vnext]',
        'A_edge':'one pivot in coordinates1..4; edge orientation sign',
        'S_degree2':'path(d,e)-path(e,d)'},
      'residual_branches':[
        {'name':'baseline','target':'M0_tracefree','scalar_primitive':False},
        {'name':'F12_direct','target':'F12','kernel':'B34*Phi'},
        {'name':'F34_direct','target':'F34','kernel':'B12*Phi'},
        {'name':'F12_derivative','target':'F12','kernel':'T12*E34*Phi'},
        {'name':'F34_derivative','target':'F34','kernel':'T34*E12*Phi'}],
      'inner_branches':[
        {'name':'prism','nodes':['cancel_inserted','differentiate_regularized',
                                 'Hrho_symbolic_labels']},
        {'name':'K','adjoint_nodes':['R','K','Pi_inner'],
         'regularization_order':'cancel inserted before differentiated coefficient'},
        {'name':'AHS','adjoint_nodes':['R','A','h','S','Pi_inner'],
         'regularization_order':'cancel inserted before differentiated coefficient'}],
      'owner_control':{'active':state.active,'kernel':sorted(state.kernel_owners),
                       'weighted':sorted(state.weighted_owners),
                       'required_prefix':sorted(state.required_prefix)},
      'derivative_domain_control':domain,
      'support_envelopes':{'inner_Pi':[-1668,5248],
                           'outer_Pi_all_J':[-45684,73705]},
      'unresolved_leaves':[
        {'id':'M0','reason':'exact baseline numerator DAG and reuse not instantiated'},
        {'id':'F12_F34','reason':'physical scalar numerator DAGs and reuse not instantiated'},
        {'id':'currents_k_IPH','reason':'factored source kernels not compiled to arithmetic DAG'},
        {'id':'weight_coefficients','reason':'finite quotient formulas not priced/extracted'},
        {'id':'coefficient_demands','reason':'symbolic exponent predicates not reduced to priced DAG'},
        {'id':'exact_cancellation','reason':'proof-backed rewrites need concrete numerator ledger'},
        {'id':'product_ledger','reason':'complete count unknown; no complete arithmetic-cost pass'},
        {'id':'live_byte_schedule','reason':'coefficient widths/runtime/scratch not certified'}],
      'forbidden_shortcuts':['old_four_tail','old_781_features','derivative_before_cancellation',
                             'drop_deleted_prefix_owner','replace_standard_projection',
                             'physical_source_evaluation','dense_support_enumeration']}


def encode_certificate(certificate, cap=MAX_OUTPUT_BYTES):
    require(type(cap) is int and 0 < cap <= MAX_OUTPUT_BYTES,'invalid metadata cap')
    require(certificate.get('execution_release') is False,'release flag forbidden')
    require(certificate.get('physical_source_evaluated') is False,'source evaluation forbidden')
    require(certificate.get('complete_arithmetic_contract') is False,'arithmetic readiness forbidden')
    require(certificate.get('schema')==SCHEMA,'schema mismatch')
    require(len(certificate.get('seeds',[]))==MAX_SEEDS,'seed shape mismatch')
    data=(json.dumps(certificate,sort_keys=True,separators=(',',':'))+'\n').encode()
    canonical=(json.dumps(build_certificate(),sort_keys=True,separators=(',',':'))+'\n').encode()
    require(data==canonical,'noncanonical metadata specification')
    require(len(data)<=cap,'serialized metadata cap exceeded')
    return data


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--max-output-bytes',type=int,default=MAX_OUTPUT_BYTES)
    args=parser.parse_args()
    try:
        require(__debug__,'optimized Python rejected')
        data=encode_certificate(build_certificate(),args.max_output_bytes)
    except ContractError as exc:
        print('BLOCKED: '+str(exc),file=sys.stderr)
        return 2
    sys.stdout.buffer.write(data)
    return 0

if __name__=='__main__':
    sys.exit(main())
