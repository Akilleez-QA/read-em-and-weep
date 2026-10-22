#!/usr/bin/env python3
"""Exact binary-icosahedral character enumeration; no geometric coefficients or ranks.

Input: globally generated center-even rank-5 degree-26 G-bundle on P(W),
H0 character 1+3A+V+2P+2D. Character convention follows the project's
verify_negative_vertex_scalar.py. Arithmetic is exact in Q(sqrt(5)).
"""
from fractions import Fraction as F
from functools import lru_cache
import json
from pathlib import Path

def z(a,b=0): return (F(a),F(b))
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def sub(x,y): return add(x,neg(y))
def mul(x,y): return (x[0]*y[0]+5*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def scale(k,x): return (k*x[0],k*x[1])
def seq_sum(xs):
    out=z(0)
    for x in xs: out=add(out,x)
    return out
phi=z(F(1,2),F(1,2)); phip=z(F(1,2),F(-1,2))
tr=[z(2),z(-2),phi,neg(phi),phip,neg(phip),z(1),z(-1),z(0)]
sizes=[1,1,12,12,12,12,20,20,30]
def sym(n,x):
    if n==0:return z(1)
    a,b=z(1),x
    for _ in range(2,n+1): a,b=b,sub(mul(x,b),a)
    return b

def inner(a,b):return scale(F(1,120),seq_sum(scale(k,mul(x,y)) for k,x,y in zip(sizes,a,b)))
def vmul(a,b):return [mul(x,y) for x,y in zip(a,b)]
one=[z(1)]*9; W=tr; A=[sym(2,x) for x in tr]
S=[sym(3,x) for x in tr]; D=[sym(4,x) for x in tr]; T=[sym(5,x) for x in tr]
P=list(map(z,[4,4,-1,-1,-1,-1,1,1,0]))
V=[sub(sym(6,x),p) for x,p in zip(tr,P)]
Wp=[sub(mul(w,p),t) for w,p,t in zip(W,P,T)]
irreps={'1':one,'W':W,'Wp':Wp,'A':A,'V':V,'P':P,'S':S,'D':D,'T':T}
names=tuple(irreps)
dims={name:int(chi[0][0]) for name,chi in irreps.items()}
assert sum(sizes)==120
assert sum(d*d for d in dims.values())==120
for name,a in irreps.items():
    for other,b in irreps.items(): assert inner(a,b)==z(int(name==other))

def decompose(chi):
    result=[]
    for a in irreps.values():
        q=inner(chi,a)
        assert q[1]==0 and q[0].denominator==1 and q[0]>=0
        result.append(int(q[0]))
    assert sum(m*dims[n] for m,n in zip(result,names))==chi[0][0]
    return tuple(result)

target_dict={'1':1,'A':3,'V':1,'P':2,'D':2}
target=tuple(target_dict.get(n,0) for n in names)
assert sum(m*dims[n] for m,n in zip(target,names))==31
candidates=[]
for name,chi in irreps.items():
    rank=dims[name]
    if rank>5: continue
    for d in range(26//rank+1):
        # The bundle has center +1; O(d) has center (-1)^d.
        if chi[1] != z(((-1)**d)*rank): continue
        h0=decompose(vmul(chi,[sym(d,x) for x in W]))
        if all(a<=b for a,b in zip(h0,target)):
            candidates.append((name,d,rank,d*rank,h0))
candidates.sort(key=lambda x:(x[1],x[0]))

@lru_cache(None)
def solve(i,rank,degree,character):
    if rank==0:
        return ((),) if degree==0 and not any(character) else ()
    if i==len(candidates) or degree<0: return ()
    name,d,r,deg,h0=candidates[i]
    cap=rank//r
    if deg: cap=min(cap,degree//deg)
    cap=min([cap]+[a//b for a,b in zip(character,h0) if b])
    solutions=[]
    for mult in range(cap+1):
        rest=tuple(a-mult*b for a,b in zip(character,h0))
        for tail in solve(i+1,rank-mult*r,degree-mult*deg,rest):
            solutions.append((((i,mult),) if mult else ())+tail)
    return tuple(solutions)

raw=solve(0,5,26,target)
solutions=[]
for entries in raw:
    terms=[]; rank=degree=0; char=[0]*len(names)
    for i,m in entries:
        name,d,r,deg,h0=candidates[i]
        terms.append({'representation':name,'multiplicity':m,'degree':d,'representation_dimension':r})
        rank+=m*r;degree+=m*deg
        char=[a+m*b for a,b in zip(char,h0)]
    assert rank==5 and degree==26 and tuple(char)==target
    splitting=[]
    for term in terms: splitting.extend([term['degree']]*(term['multiplicity']*term['representation_dimension']))
    solutions.append({'terms':terms,'ordinary_splitting':sorted(splitting),
                      'h0_C_minus_6':sum(max(d-5,0) for d in splitting),
                      'h1_C_minus_6':sum(max(5-d,0) for d in splitting)})
# Independent cross-check: enumerate ordinary degree partitions first, then
# representations in each equal-degree block, comparing class-function values
# directly rather than using irreducible multiplicity vectors.
def degree_partitions(total,length,minimum=0):
    if length==0:
        if total==0: yield ()
        return
    for first in range(minimum,total//length+1):
        for tail in degree_partitions(total-first,length-1,first):
            yield (first,)+tail

@lru_cache(None)
def block_representations(dimension,parity,start=0):
    if dimension==0: return ((),)
    result=[]
    for j in range(start,len(names)):
        n=names[j]; r=dims[n]
        if r>dimension or irreps[n][1]!=z(parity*r): continue
        for tail in block_representations(dimension-r,parity,j):
            result.append((n,)+tail)
    return tuple(result)

def trace_sum_for(terms):
    out=[z(0)]*9
    for n,d in terms:
        v=vmul(irreps[n],[sym(d,x) for x in W])
        out=[add(a,b) for a,b in zip(out,v)]
    return out

def canonical(terms): return tuple(sorted(terms,key=lambda x:(x[1],x[0])))

target_trace=[seq_sum(scale(target_dict.get(n,0),irreps[n][j]) for n in names) for j in range(9)]
independent=set()
from collections import Counter
from itertools import product
for splitting in degree_partitions(26,5):
    blocks=sorted(Counter(splitting).items())
    choices=[block_representations(m,(-1)**d) for d,m in blocks]
    for selection in product(*choices):
        terms=[(n,d) for (d,_), reps in zip(blocks,selection) for n in reps]
        if trace_sum_for(terms)==target_trace: independent.add(canonical(terms))
first_pass=set()
for solution in solutions:
    terms=[(t['representation'],t['degree']) for t in solution['terms'] for _ in range(t['multiplicity'])]
    first_pass.add(canonical(terms))
assert independent==first_pass
assert len(first_pass)==29
assert all(min(s['ordinary_splitting'])<=2 for s in solutions)
assert not any(s['ordinary_splitting']==[5,5,5,5,6] for s in solutions)
assert min(s['h1_C_minus_6'] for s in solutions)==3

# Additional actual-sequence character, not a rank assumption:
# H0(C(-1)) = (2W+2Wp+3S+4T) - A tensor Sym^5(W).
source_minus_one={'W':2,'Wp':2,'S':3,'T':4}
source_trace=[seq_sum(scale(source_minus_one.get(n,0),irreps[n][j]) for n in names) for j in range(9)]
minus_one_trace=[sub(a,b) for a,b in zip(source_trace,vmul(A,T))]
minus_one_mult=decompose(minus_one_trace)
minus_one_dict={n:m for n,m in zip(names,minus_one_mult) if m}
assert sum(dims[n]*m for n,m in minus_one_dict.items())==26
refined=[]
for solution in solutions:
    terms=[(t['representation'],t['degree']-1) for t in solution['terms'] if t['degree']>=1 for _ in range(t['multiplicity'])]
    actual=trace_sum_for(terms)
    solution['h0_C_minus_1_character']={n:m for n,m in zip(names,decompose(actual)) if m}
    solution['satisfies_minus_one_constraint']=(actual==minus_one_trace)
    if actual==minus_one_trace: refined.append(solution)

assert len(refined)==21
# The direct-sum linear-block construction recovers these fixed characters.
right_source=decompose(vmul(A,T))
right_target=decompose(vmul(A,D))
assert {n:m for n,m in zip(names,right_source) if m}=={'Wp':1,'S':1,'T':2}
assert {n:m for n,m in zip(names,right_target) if m}=={'A':1,'V':1,'P':1,'D':1}
for solution in refined:
    dual_twist_2_terms=[(t['representation'],2-t['degree']) for t in solution['terms'] if t['degree']<=2 for _ in range(t['multiplicity'])]
    hom_mult=decompose(trace_sum_for(dual_twist_2_terms))
    solution['equivariant_maps_to_O2']=hom_mult[names.index('1')]
    assert solution['equivariant_maps_to_O2'] in (1,2)

# Geometric pruning supplied by the project: joint coefficient span is all
# of M3_+, hence H0(C*)=0 and no ordinary degree-zero summand occurs.
positive=[s for s in refined if min(s['ordinary_splitting'])>=1]
assert len(positive)==12
assert len({tuple(s['ordinary_splitting']) for s in positive})==11
at_least_two=[s for s in positive if min(s['ordinary_splitting'])>=2]
assert len(at_least_two)==4
assert sum(s['equivariant_maps_to_O2']==1 for s in positive)==10
assert sum(s['equivariant_maps_to_O2']==2 for s in positive)==2
# Actual exceptional-boundary theorem: H1(C(-3)) is a quotient of H2(B)=W.
# Since all degrees are positive, H1(C(-3)) is exactly the degree-one
# multiplicity representation, using H1(O(-2))=1 for SL(2,5).
boundary_compatible=[]
for solution in positive:
    degree_one={}
    for term in solution['terms']:
        if term['degree']==1:
            name=term['representation']
            degree_one[name]=degree_one.get(name,0)+term['multiplicity']
    solution['h1_C_minus_3_character']=degree_one
    allowed=degree_one in ({},{'W':1})
    solution['satisfies_exceptional_boundary_constraint']=allowed
    if allowed: boundary_compatible.append(solution)
assert len(boundary_compatible)==9
assert sum(not s['h1_C_minus_3_character'] for s in boundary_compatible)==4
assert sum(s['h1_C_minus_3_character']=={'W':1} for s in boundary_compatible)==5
assert sum(s['equivariant_maps_to_O2']==1 for s in boundary_compatible)==7
assert sum(s['equivariant_maps_to_O2']==2 for s in boundary_compatible)==2

report={'group':'SL(2,5), binary icosahedral', 'rank':5,'degree':26,'center_action':1,
        'h0_character':target_dict,'h0_C_minus_1_character':minus_one_dict,'irreducible_dimensions':dims,
        'candidate_count':len(candidates),'solution_count':len(solutions),'independent_partition_cross_check':True,'solutions':solutions,
        'method':'Exact Q(sqrt(5)) character inner products and exhaustive nonnegative integer enumeration.',
        'geometric_coefficients_or_ranks_evaluated':False,
        'refined_solution_count':len(refined),'refined_solutions':refined,
        'positive_solution_count':len(positive),'positive_solutions':positive,
        'exceptional_boundary_solution_count':len(boundary_compatible),'exceptional_boundary_solutions':boundary_compatible,
        'conditional_minimum_two_count':len(at_least_two),'conditional_minimum_two_solutions':at_least_two}
out=Path(__file__).with_name('c_lin_splittings.json')
out.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
