#!/usr/bin/env python3
"""Independent small-integer controls for a necessary Gauss-rank overlist.

Does not import the author's code, evaluate an actual bundle/map, or rerun
historical splitting/profile enumerations. Geometric premises remain premises.
"""
from pathlib import Path
from fractions import Fraction
from math import ceil, floor
import hashlib
import json

ROOT = Path(__file__).resolve().parent
FROZEN = ROOT.parent

def require(value, message):
    if not value:
        raise ValueError(message)

def even_ceiling(n):
    return 2 * ceil(Fraction(n, 2))

def admissible(r, k, l, source=None):
    return (4 <= r <= 13 and 1 <= k <= 3 and 1 <= l <= 3
            and r*k < 17 and r*l <= 13
            and (source not in ('D', 'P', 'V') or l <= 2))

def independent_degree_witness(r, k, l, source=None):
    """Solve a closed even-integer interval, choosing its UPPER endpoint.

    The author's routine chooses a lower endpoint; no witness is copied.
    """
    p, q = 17-r*k, 13-r*l
    t = 3 if source == 'Z' else 2
    lower = Fraction(even_ceiling(t*p)-54-r*k*(k-1), k)
    upper = Fraction(54-even_ceiling(q)-r*l*(2*k+l-1), l)
    c = 2*floor(upper/2)
    require(c >= lower, 'empty independent even degree interval')
    if q == 0:
        require(c == upper, 'full endpoint must have degree exactly zero')
    degrees = [c + 2*r*i for i in range(k+l)]
    a = -54-sum(degrees[:k])
    b = a+sum(degrees)
    require(a <= -even_ceiling(t*p), 'lower endpoint degree bound')
    require((b == 0) if q == 0 else (b <= -even_ceiling(q)), 'upper endpoint degree bound')
    require(all(x % 2 == 0 for x in [a,b]+degrees), 'center-even parity')
    require(all(y-x == 2*r for x,y in zip(degrees,degrees[1:])), 'determinant increments')
    require((k+l)*(-54) == l*a+k*b-r*k*l*(k+l), 'zero-defect identity')
    return {'a':a, 'c':degrees, 'b':b}

def universal_identity(k,l):
    """Check the coefficients of a,c,r,delta_1,...,delta_(m-1)."""
    m=k+l
    size=m+2
    def unit(index, factor=1):
        v=[0]*size; v[index]=factor; return v
    def add(*vs): return [sum(parts) for parts in zip(*vs)]
    def mul(n,v): return [n*x for x in v]
    a=unit(0); r=unit(2)
    cs=[add(unit(1),unit(2,2*i),*[unit(3+j) for j in range(i)]) for i in range(m)]
    d=add(a,*cs[:k]); b=add(a,*cs)
    correction=add(*([unit(3+j,-l*(j+1)) for j in range(k-1)]
                   +[unit(3+j,-k*(m-j-1)) for j in range(k-1,m-1)]))
    rhs=add(mul(l,a),mul(k,b),mul(-k*l*m,r),correction)
    require(mul(m,d)==rhs, 'general determinant identity coefficient mismatch')

def ordinary_source_checks():
    # These are ranks of the ordinary summands in the four imported types.
    split={'D':{2:5,3:8,4:3,8:1},
           'P':{2:4,3:8,4:3,5:2},
           'V':{2:3,3:8,4:6},
           'Z':{3:14,4:3}}
    report={}
    for name,blocks in split.items():
        h0=lambda twist:sum(n*max(twist-j+1,0) for j,n in blocks.items())
        h1=lambda twist:sum(n*max(j-twist-1,0) for j,n in blocks.items())
        require(sum(blocks.values())==17,'source rank mismatch')
        require(sum(-j*n for j,n in blocks.items())==-54,'source degree mismatch')
        require(h0(1)==0 and h1(1)==20,'twist-one source cohomology')
        require(h0(3)-h1(3)==14,'cubic Euler dimension')
        require(h0(2)-h1(2)==-3,'quadratic Euler dimension')
        expected={'D':5,'P':4,'V':3,'Z':0}[name]
        require(h0(2)==expected,'quadratic source visibility')
        report[name]={'rank':17,'degree':-54,'h0_twist2':h0(2),'h0_twist3':h0(3)}
    # b,c >=1; b+c+e+f=3 is equivalent to four nonnegative integers
    # summing to one. Its entire solution set consists of the four units.
    compositions=[]
    for i in range(4):
        unit=[int(i==j) for j in range(4)]
        compositions.append([1+unit[0],1+unit[1],unit[2],unit[3]])
    require(sorted(compositions)==[[1,1,0,1],[1,1,1,0],[1,2,0,0],[2,1,0,0]],'four source composition')
    return report

def main():
    authored=json.loads((FROZEN/'RESULT.json').read_text())
    coarse={(r,k,l) for r in range(4,14) for k in range(1,5)
            for l in range(1,5) if admissible(r,k,l)}
    refined={(s,r,k,l) for s in ('D','P','V','Z') for r,k,l in coarse if admissible(r,k,l,s)}
    actual_coarse=[(p['r'],p['k'],p['l']) for p in authored['profiles']]
    actual_refined=[(p['source'],p['r'],p['k'],p['l']) for p in authored['source_refined_profiles']]
    require(len(actual_coarse)==len(set(actual_coarse)) and set(actual_coarse)==coarse,'coarse exact-set equality')
    require(len(actual_refined)==len(set(actual_refined)) and set(actual_refined)==refined,'refined exact-set equality')
    counts=[sum(row[0]==r for row in coarse) for r in range(4,14)]
    require(counts==[9,6,4,2,2,1,1,1,1,1],'coarse row counts')
    require(len(coarse)==28 and sum(r<13 for r,k,l in coarse)==27,'coarse totals')
    require(len(refined)==103 and sum(r<13 for s,r,k,l in refined)==99,'refined totals')
    require({(r,k,l) for r,k,l in coarse if 13-r*l==0}=={(13,1,1)},'full endpoint exception')
    require({(s,r) for s,r,k,l in refined if l==3}=={('Z',4)},'cubic-only source exception')
    for p in authored['profiles']:
        r,k,l=p['r'],p['k'],p['l']; bottom=17-r*k; top=13-r*l
        require(bottom>0 and top>=0,'endpoint dimensions')
        require(p['lower_endpoint_rank']==bottom and p['upper_endpoint_codimension']==top,'reported endpoint dimensions')
        require(p['lower_endpoint_SF_rank_range']==[1,min(r-1,bottom)],'lower endpoint derivative range')
        require(p['upper_endpoint_SF_rank_range']==([0,0] if top==0 else [1,min(r-1,top)]),'upper endpoint derivative range')
    for row in authored['rows']:
        r=row['r']
        require(41-(17-r)==37-(13-r)==24+r,'square dimensions from both kernel and cokernel')
        require(row['positive_square_rank']==24+r and row['positive_square_kernel_dimension']==17-r
                and row['positive_square_cokernel_dimension']==13-r,'reported square dimensions')
        require(row['status']==('auxiliary-surjectivity-success-if-attained' if r==13 else 'unresolved-bad-rank'),'rank success classification')
    witnesses=[{'r':r,'k':k,'l':l,'degrees':independent_degree_witness(r,k,l)} for r,k,l in sorted(coarse)]
    refined_witnesses=[{'source':s,'r':r,'k':k,'l':l,'degrees':independent_degree_witness(r,k,l,s)} for s,r,k,l in sorted(refined)]
    for k in range(1,6):
        for l in range(1,6): universal_identity(k,l)
    # Negative controls test exactly the mistakes at issue, not actual instances.
    controls={
        'rank4_fourth_backward_block_rejected':not admissible(4,4,1),
        'rank4_D_third_forward_block_rejected':not admissible(4,1,3,'D'),
        'rank4_Z_third_forward_block_retained':admissible(4,1,3,'Z'),
        'rank5_ordered32_retained':admissible(5,3,2),
        'rank5_swapped23_rejected':not admissible(5,2,3),
        'rank13_full_endpoint_retained':admissible(13,1,1),
        'rank13_second_forward_block_rejected':not admissible(13,1,2),
        'rank14_rejected':not admissible(14,1,1),
        'rank3_outside_conditional_scope':not admissible(3,1,1),
        'missing_success_bin_detected':coarse-{(13,1,1)}!=set(actual_coarse),
        'duplicate_bin_detected':len(actual_coarse+[actual_coarse[0]])!=len(set(actual_coarse+[actual_coarse[0]])),
    }
    require(all(controls.values()),'negative control failure')
    report={'verdict':'PASS for the stated conditional necessary partition',
        'premise_r_at_least_4':'imported separately, not proved here',
        'row_counts':counts,'coarse_total':28,'coarse_bad':27,
        'refined_total':103,'refined_bad':99,'source_counts':{s:sum(t[0]==s for t in refined) for s in ('D','P','V','Z')},
        'ordinary_source_checks':ordinary_source_checks(),
        'symbolic_coefficient_identities':25,'negative_controls':controls,
        'independent_degree_witnesses':witnesses,'independent_source_degree_witnesses':refined_witnesses,
        'actual_instances_evaluated':False,'historical_enumeration_run':False,
        'realizability_asserted':False,'full_adjoint_or_original_repair_asserted':False}
    print(json.dumps(report,indent=2,sort_keys=True))

if __name__=='__main__': main()
