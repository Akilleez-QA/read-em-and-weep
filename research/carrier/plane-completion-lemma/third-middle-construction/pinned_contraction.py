#!/usr/bin/env python3
"""Rebuild all 15 order-two coefficients from full original-cover first cochains.

No producer/audit module is imported. Polynomial Hamiltonians in four frame
variables give the bracket by formal differentiation. All coefficients are Q.
Input boundary: fixed plane definitions below, declared first cochains, and
complete source/target basis labels. Even the selected D2 entries are rebuilt.
"""
import argparse
import hashlib
import json
from fractions import Fraction as Q
from itertools import combinations, combinations_with_replacement
from pathlib import Path
import sympy as sp

ZERO=(0,)*8
TOP=(0,1,2)
PAIRS=list(combinations(range(3),2))
NAMES=['1','a','b','c','d']
ROOT=Path(__file__).resolve().parent

def require(ok,message):
    if not ok:
        raise ValueError(message)

def plus(*polys):
    ans={}
    for p in polys:
        for e,a in p.items():
            ans[e]=ans.get(e,Q(0))+a
            if not ans[e]:del ans[e]
    return ans

def times(p,q):
    ans={}
    for e,a in p.items():
        for f,b in q.items():
            g=tuple(x+y for x,y in zip(e,f))
            ans[g]=ans.get(g,Q(0))+a*b
            if not ans[g]:del ans[g]
    return ans

def scalar(p,a):
    return {e:v*a for e,v in p.items() if v*a}

def mono(exponents=ZERO,a=1):
    return {tuple(exponents):Q(a)} if a else {}

def shift(p,z=0,X=0,Y=0,W=0):
    return times(p,mono((z,X,Y,W,0,0,0,0)))

def power(p,n):
    ans=mono()
    for _ in range(n):ans=times(ans,p)
    return ans

def var(i):
    e=list(ZERO);e[i]=1
    return mono(e)

z,X,Y,W=map(var,range(4))
f=tuple(map(var,range(4,8)))
S=plus(power(X,2),power(Y,2))
xy=times(X,Y)
A=plus(power(X,3),power(Y,3))
g=plus(S,scalar(times(z,power(W,2)),-1))
C=plus(power(S,2),times(times(z,S),power(W,2)),times(power(z,2),power(W,4)))
alpha=[plus(scalar(times(A,f[0]),-1),times(power(W,6),f[1]),scalar(times(g,f[2]),-1),times(xy,f[3])),
       plus(scalar(times(A,f[0]),-1),times(power(S,3),f[1]),scalar(times(shift(g,z=-1),f[2]),-1),times(xy,f[3]))]
B=[times(power(z,3),f[0]),f[1],plus(times(times(z,C),f[1]),times(power(z,4),f[2])),times(power(z,3),f[3])]
O=[{(1,2):xy,(1,3):g,(2,3):power(W,6)},
   {(1,2):xy,(1,3):shift(g,z=-1),(2,3):power(S,3)}]

def derivative(p,i):
    ans={}
    for e,a in p.items():
        if e[i+4]:
            ee=list(e);ee[i+4]-=1
            ans[tuple(ee)]=a*e[i+4]
    return ans

def poisson(p,q,chart):
    """grad(p)^T Omega grad(q), with multiplication of frame monomials."""
    ans={}
    dp=[derivative(p,i) for i in range(4)]
    dq=[derivative(q,i) for i in range(4)]
    for (i,j),omega in O[chart].items():
        ans=plus(ans,times(omega,plus(times(dp[i],dq[j]),scalar(times(dp[j],dq[i]),-1))))
    return ans

def transport(p,kind):
    ans={}
    for e,a in p.items():
        term=mono((*e[:4],0,0,0,0),a)
        for i,n in enumerate(e[4:]):term=times(term,power(B[i],n))
        ans=plus(ans,shift(term,z=-4 if kind=='W' else -1))
    return ans

def project(p):
    return {e:a for e,a in p.items() if all(v<0 for v in e[1:4])}

def component(p,indices):
    target=tuple(indices.count(i) for i in range(4))
    return {e:a for e,a in p.items() if e[4:]==target}

def replace_frame(p,indices):
    tail=tuple(indices.count(i) for i in range(4))
    return {(*e[:4],*tail):a for e,a in p.items()}

def restrict_z(p,predicate):
    return {e:a for e,a in p.items() if predicate(e[0])}

def normalize_c(c):
    return {ij:p for ij,p in c.items() if p}

def cplus(*cs):
    return normalize_c({ij:plus(*(c.get(ij,{}) for c in cs)) for ij in set().union(*(set(c) for c in cs))})

def cmap(c,func):return normalize_c({ij:func(p) for ij,p in c.items()})

def delta(c,degree):
    return normalize_c({ij:plus(*(scalar(c.get(ij[:i]+ij[i+1:],{}),(-1)**i) for i in range(len(ij)))) for ij in combinations(range(3),degree+2)})

def homotopy(c):
    ans={}
    for ij,p in c.items():
        for e,a in p.items():
            choices=[i for i in range(3) if e[i+1]>=0]
            if choices and choices[0] in ij:
                i=choices[0];out=tuple(j for j in ij if j!=i)
                ans[out]=plus(ans.get(out,{}),mono(e,a*(-1)**ij.index(i)))
    return normalize_c(ans)

def relation_divide(p,chart=0):
    """Exact polynomial division by alpha using its E0 coefficient.

    Finite-chart alpha_E0=W^6 is a geometric unit on the triple overlap.
    The output is accepted only after reconstructing every input coefficient.
    """
    require(chart==0,'Only finite relation division is used.')
    h=shift(replace_frame(component(p,[1,1]),[1]),W=-6)
    for j in [0,2,3]:
        rem=plus(p,scalar(times(alpha[0],h),-1))
        h=plus(h,shift(replace_frame(component(rem,[1,j]),[j]),W=-6))
    require(times(alpha[0],h)==p,'Relation division has nonzero remainder.')
    return h

def split_base(u):
    """T_U v_infinity-v_finite=u in plane H2; triangular base splitting."""
    finite={};infty={}
    for j,d in [(0,2),(2,3),(3,2)]:
        part=component(u,[j])
        finite=plus(finite,scalar(restrict_z(part,lambda n:n>=0),-1))
        infty=plus(infty,shift(restrict_z(part,lambda n:n<0),z=-d))
    rest=plus(u,scalar(project(transport(infty,'U')),-1))
    part=component(rest,[1])
    finite=plus(finite,scalar(restrict_z(part,lambda n:n>=0),-1))
    infty=plus(infty,shift(restrict_z(part,lambda n:n<0),z=1))
    require(project(plus(transport(infty,'U'),scalar(finite,-1)))==u,'Base primitive failed.')
    return finite,infty

def unpack(records):
    result={}
    for record in records:
        p={}
        for indices,geom,value in record['terms']:
            indices=[indices] if isinstance(indices,int) else indices
            e=tuple(geom)+tuple(indices.count(i) for i in range(4))
            p=plus(p,mono(e,Q(value)))
        if p:result[tuple(record['open'])]=p
    return result

def packed(p):
    return [[list(e),str(a)] for e,a in sorted(p.items())]

def packed_c(c):
    return [{'open':list(ij),'terms':packed(p)} for ij,p in sorted(c.items())]

def encode(stages):
    return {k:packed_c(v) if k in ['mixed_BCH','relation_mixed_primitive','closed_mixed'] else packed(v) for k,v in stages.items()}

def coeff_bch(tensors,i,j):
    """Direct coefficient extraction, not numerical sampling/polarization."""
    ordered=[(i,j)] if i==j else [(i,j),(j,i)]
    finite={};infty={};mixed={}
    for a,b in ordered:
        F0,I0,H0=tensors[a];F1,I1,H1=tensors[b]
        finite=plus(finite,scalar(poisson(F0.get((0,1),{}),F1.get((1,2),{}),0),Q(1,2)))
        infty=plus(infty,scalar(poisson(I0.get((0,1),{}),I1.get((1,2),{}),1),Q(1,2)))
        for p,q in PAIRS:
            term=plus(poisson(H0.get((p,),{}),transport(I1.get((p,q),{}),'W'),0),
                      scalar(poisson(F0.get((p,q),{}),H1.get((q,),{}),0),-1))
            mixed[(p,q)]=plus(mixed.get((p,q),{}),scalar(term,Q(1,2)))
    mixed=normalize_c(mixed)
    raw=plus(transport(infty,'W'),scalar(finite,-1),scalar(delta(mixed,1).get(TOP,{}),-1))
    relation=relation_divide(raw)
    v0,vi=split_base(project(relation))
    residual=plus(transport(vi,'U'),scalar(v0,-1),scalar(relation,-1))
    vh=homotopy({TOP:residual})
    require(delta(vh,1).get(TOP,{})==residual,'Plane relation primitive failed.')
    closed0=plus(finite,scalar(times(alpha[0],v0),-1))
    closedi=plus(infty,scalar(times(alpha[1],vi),-1))
    closedh=cplus(mixed,cmap(vh,lambda p:scalar(times(alpha[0],p),-1)))
    require(plus(transport(closedi,'W'),scalar(closed0,-1),scalar(delta(closedh,1).get(TOP,{}),-1))=={},'Corrected W2 cocycle is not closed.')
    obs=project(closed0)
    require(project(transport(project(closedi),'W'))==obs,'Projected finite/infinity obstructions disagree.')
    return obs,dict(finite_BCH=finite,infinity_BCH=infty,mixed_BCH=mixed,relation_defect=raw,relation_quotient=relation,
                   relation_finite_primitive=v0,relation_infinity_primitive=vi,relation_mixed_primitive=vh,
                   closed_finite=closed0,closed_infinity=closedi,closed_mixed=closedh)

def make_source(basis):
    j,base,plane=basis
    e=(base,*[-n-1 for n in plane],*tuple(int(i==j) for i in range(4)))
    value=mono(e)
    if j==2:
        correction=project(times(shift(C,z=-3),replace_frame(value,[1])))
        value=plus(value,restrict_z(correction,lambda n:n>=0))
    return value

def reduce_target(value,target_lookup):
    red=value.copy()
    for source,dest,multiplicity,threshold in [([0,2],[0,1],1,0),([2,2],[1,2],2,1),([2,3],[1,3],1,0)]:
        forced=project(times(shift(C,z=-3),replace_frame(component(value,source),dest)))
        red=plus(red,scalar(restrict_z(forced,lambda n:n>=threshold),-multiplicity))
    require(all(e in target_lookup for e in red),'Unknown reduced target coordinate.')
    return {target_lookup[e]:a for e,a in red.items()}

def check_first_cochains(tensors):
    # Validate the fixed plane gluing and the scalar compatibility used by brackets.
    require(transport(alpha[1],'U')==shift(alpha[0],z=2),'Alpha transport failed.')
    for i in range(4):
        require(poisson(alpha[0],f[i],0)=={},'Alpha is not radical in finite chart.')
        require(poisson(alpha[1],f[i],1)=={},'Alpha is not radical in infinity chart.')
        for j in range(4):
            # B transforms an L-valued form by z^4.
            require(poisson(B[i],B[j],0)==shift(poisson(f[i],f[j],1),z=4),'Form transport failed.')
    pd=[-3,0,-4,-4]
    for n,(finite,infty,mixed) in enumerate(tensors):
        for chart,cochain in enumerate([finite,infty,mixed]):
            weights=[3,6,0,2] if chart==1 else [3,0,2,2]
            offset=-7 if chart==1 else -3
            for ij,p in cochain.items():
                for e in p:
                    require(all(e[t+1]>=0 for t in range(3) if t not in ij),'First cochain not regular on declared plane intersection.')
                    require(chart==2 or (e[0]<=0 if chart==1 else e[0]>=0),'First cochain not regular on base chart.')
                    require(sum(e[4:])==2,'First cochain not a quadratic Hamiltonian.')
                    require(sum(e[1:4])==sum(x*y for x,y in zip(pd,e[4:]))+1,'First cochain plane degree mismatch.')
                    require(2*e[0]+e[1]+e[2]==offset+sum(x*y for x,y in zip(weights,e[4:])),'First cochain character mismatch.')
        # Plane cocycle equations hold modulo the line relation, and the mixed
        # equations are relation-valued. This checks the actual declared input.
        relation_divide(delta(finite,1).get(TOP,{}))
        inf_delta=delta(infty,1).get(TOP,{})
        relation_divide(transport(inf_delta,'W'))
        defect=cplus(cmap(infty,lambda p:transport(p,'W')),cmap(finite,lambda p:scalar(p,-1)),cmap(delta(mixed,0),lambda p:scalar(p,-1)))
        for p in defect.values():relation_divide(p)
    # The H1(W1) directions are literally the declared repeated mixed tensors.
    for n,geom in [(3,(-2,1,0,0)),(4,(-2,0,1,0))]:
        expected=mono((*geom,0,2,0,0))
        require(tensors[n]==({}, {},{(i,):expected for i in range(3)}),'H1(W1) coordinate convention changed.')

def inverse_source(u):
    ans={}
    for j,degree in [(0,2),(2,3),(3,2)]:
        ans=plus(ans,shift(component(u,[j]),z=-degree))
    ans=plus(ans,shift(component(u,[1]),z=1),scalar(times(shift(C,z=-2),replace_frame(component(u,[2]),[1])),-1))
    return project(ans)

def exact_primitive(stages,source,order):
    """Explicit original-cover primitive modulo alpha for a zero n obstruction."""
    source_i=inverse_source(source)
    require(project(transport(source_i,'U'))==source,'Preimage is not globally compatible in U.')
    src_h=homotopy({TOP:plus(transport(source_i,'U'),scalar(source,-1))})
    require(delta(src_h,1).get(TOP,{})==plus(transport(source_i,'U'),scalar(source,-1)),'Global source Cech lift failed.')
    r0=plus(stages['closed_finite'],scalar(times(alpha[0],source),-1))
    ri=plus(stages['closed_infinity'],scalar(times(alpha[1],source_i),-1))
    rh=cplus(stages['closed_mixed'],cmap(src_h,lambda p:scalar(times(alpha[0],p),-1)))
    require(project(r0)==project(ri)=={},'Preimage did not kill both plane projections.')
    p0=homotopy({TOP:r0});pi=homotopy({TOP:ri})
    require(delta(p0,1).get(TOP,{})==r0 and delta(pi,1).get(TOP,{})==ri,'Finite/infinity W primitive failed.')
    remainder=cplus(rh,cmap(pi,lambda p:scalar(transport(p,'W'),-1)),p0)
    require(delta(remainder,1)=={},'Mixed W primitive has a nonclosed residual.')
    ph=cmap(homotopy(remainder),lambda p:scalar(p,-1))
    require(delta(ph,0)==cmap(remainder,lambda p:scalar(p,-1)),'Mixed W primitive failed.')
    # Check against the RAW BCH tensors, not merely the corrected cocycle.
    u0=plus(stages['relation_finite_primitive'],source)
    ui=plus(stages['relation_infinity_primitive'],source_i)
    uh=cplus(stages['relation_mixed_primitive'],src_h)
    require(plus(delta(p0,1).get(TOP,{}),times(alpha[0],u0))==stages['finite_BCH'],'Raw finite exactness failed.')
    require(plus(delta(pi,1).get(TOP,{}),times(alpha[1],ui))==stages['infinity_BCH'],'Raw infinity exactness failed.')
    reconstructed=cplus(cmap(pi,lambda p:transport(p,'W')),cmap(p0,lambda p:scalar(p,-1)),cmap(delta(ph,0),lambda p:scalar(p,-1)),cmap(uh,lambda p:times(alpha[0],p)))
    require(reconstructed==stages['mixed_BCH'],'Raw mixed exactness failed.')
    for chain,kind,chart in [(p0,'W',0),(pi,'W',1),(ph,'W',2),({TOP:u0},'U',0),({TOP:ui},'U',1),(uh,'U',2)]:
        validate_cover(chain,order,kind,chart)
    return {'finite_W_primitive':packed_c(p0),'infinity_W_primitive':packed_c(pi),'mixed_W_primitive':packed_c(ph),
            'finite_relation_primitive':packed(u0),'infinity_relation_primitive':packed(ui),'mixed_relation_primitive':packed_c(uh)}

def check_grading(p,k,kind,chart,label):
    pd=[-3,0,-4,-4]
    weights=[3,6,0,2] if chart==1 else [3,0,2,2]
    offset=k-8 if chart==1 else k-4
    for e in p:
        require(sum(e[4:])==(2 if kind=='W' else 1),label+': frame degree')
        expected=sum(a*b for a,b in zip(pd,e[4:]))+(2-k if kind=='W' else -4-k)
        require(sum(e[1:4])==expected,label+': plane degree')
        require(2*e[0]+e[1]+e[2]==offset+sum(a*b for a,b in zip(weights,e[4:])),label+': secondary character')

def check_stage_gradings(stages,k):
    count=0
    for name,value in stages.items():
        chart=1 if name in ['infinity_BCH','closed_infinity','relation_infinity_primitive'] else 0
        kind='U' if name.startswith('relation_') and name!='relation_defect' else 'W'
        cochain=name in ['mixed_BCH','relation_mixed_primitive','closed_mixed']
        for p in value.values() if cochain else [value]:
            check_grading(p,k,kind,chart,name)
            count+=len(p)
    return count

def validate_cover(cochain,k,kind,chart):
    for opened,p in cochain.items():
        check_grading(p,k,kind,chart,'original-cover primitive')
        for e in p:
            require(all(e[i+1]>=0 for i in range(3) if i not in opened),'Primitive has a pole outside its original-cover intersection.')
            require(chart==2 or (e[0]<=0 if chart==1 else e[0]>=0),'Primitive has a pole outside its base chart.')


def rebuilt_block(d,k):
    prefix='D'+str(k)
    source_basis=d[prefix+'_source_basis'];target_basis=d[prefix+'_target_basis']
    weights=[3,0,2,2]
    cols=[i for i,(ch,b,p) in enumerate(source_basis) if 2*b-p[0]-p[1]-2==k-4+weights[ch]]
    rows=[i for i,(ch,b,p) in enumerate(target_basis) if 2*b+p[0]+p[1]==k-4+weights[ch[0]]+weights[ch[1]]]
    lookup={(*[b,*p],*tuple(ch.count(i) for i in range(4))):n for n,(ch,b,p) in enumerate(target_basis)}
    def vector(p):
        red=reduce_target(p,lookup)
        require(set(red)<=set(rows),'Coefficient leaves the prescribed order-'+str(k)+' target.')
        return sp.Matrix([sp.Rational(red.get(i,0)) for i in rows])
    columns=[vector(project(times(alpha[0],make_source(source_basis[n])))) for n in cols]
    D=sp.Matrix.hstack(*columns)
    supplied=sp.zeros(*d[prefix+'_shape'])
    for row,col,value in d[prefix+'_sparse']:supplied[row,col]=sp.Rational(value)
    require(D==supplied[rows,cols],'Geometrically regenerated D'+str(k)+' block differs from supplied entries.')
    return D,cols,rows,vector


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--package',type=Path,default=ROOT.parent)
    parser.add_argument('--output',type=Path,default=ROOT/'audit-four-parameter-order-two-certificate.json')
    parser.add_argument('--verify-certificate',type=Path,help='Compare the regenerated certificate exactly; do not write an output.')
    args=parser.parse_args()
    first=args.package/'data/first_jet.json';second=args.package/'data/order_2.json'
    j=json.loads(first.read_text());d=json.loads(second.read_text())
    tensors=[tuple(unpack(t[k]) for k in ['finite','infinity','mixed']) for t in [j['origin'],*j['directions']]]
    check_first_cochains(tensors)
    D,source_cols,target_rows,vector=rebuilt_block(d,2)
    require(D.shape==(16,15) and D.rank()==15,'Unexpected order-two rank/dimension.')
    detector=D.T.nullspace()[0]
    _,pivots=D.T.rref();pivots=list(pivots)
    inverse=D[pivots,:].inv()
    report={
      'method':'Direct polynomial-Hamiltonian bracket coefficient extraction; no point evaluations and no producer imports.',
      'fixed_input_boundary':'Plane gluing/form/alpha definitions and declared first cochains; completeness of supplied source/target labels remains an input. The selected D2 entries are regenerated from alpha.',
      'input_hashes':{str(p.relative_to(args.package)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [first,second]},
      'coordinate_order':['a','b','c','d'],'source_columns':source_cols,'target_rows':target_rows,
      'D2_hom':[[str(v) for v in D.row(i)] for i in range(D.rows)],
      'detector':[str(v) for v in detector], 'minor_rows':pivots,'minor_determinant':str(D[pivots,:].det()),
      'coefficients':{},'c_d_raw_stages':{}}
    variables=sp.symbols('a b c d');obs_poly=sp.zeros(16,1);pre_poly=sp.zeros(15,1)
    for i,k in combinations_with_replacement(range(5),2):
        label='1' if i==k==0 else NAMES[k] if i==0 else NAMES[i]+'*'+NAMES[k]
        obs,stages=coeff_bch(tensors,i,k)
        graded_terms=check_stage_gradings(stages,2)
        value=vector(obs);pre=inverse*value[pivots,:]
        require(D*pre==value,'Actual coefficient has a nonzero obstruction class: '+label)
        require((detector.T*value)[0]==0,'Detector coefficient is nonzero: '+label)
        term=(1 if i==0 else variables[i-1])*(1 if k==0 else variables[k-1])
        obs_poly+=value*term;pre_poly+=pre*term
        counts={name:sum(map(len,p.values())) if name in ['mixed_BCH','relation_mixed_primitive','closed_mixed'] else len(p) for name,p in stages.items()}
        report['coefficients'][label]={'raw_stage_term_counts':counts,'projected_relation_quotient_terms':len(project(stages['relation_quotient'])),
                                     'obstruction_vector':[str(v) for v in value], 'preimage_vector':[str(v) for v in pre], 'scalar':'0'}
        source=plus(*(scalar(make_source(d['D2_source_basis'][n]),Q(v)) for n,v in zip(source_cols,pre)))
        primitive=exact_primitive(stages,source,2)
        report['coefficients'][label]['termwise_grading_checks']=graded_terms
        report['coefficients'][label]['original_cover_primitive']=primitive
        if i>=3 or k>=3:report['c_d_raw_stages'][label]=encode(stages)
        print(f'{label:4s} mixed BCH {counts["mixed_BCH"]:3d}; relation {counts["relation_quotient"]:3d}; projected relation {len(project(stages["relation_quotient"])):2d}; obstruction nonzeros {sum(v!=0 for v in value):2d}; scalar 0')
    obs_poly=obs_poly.applyfunc(sp.expand);pre_poly=pre_poly.applyfunc(sp.expand)
    report['obstruction_vector']=[str(v) for v in obs_poly]
    report['polynomial_preimage']=[str(v) for v in pre_poly]
    expected_path=args.package/'certificates/quadratic_certificate.json'
    expected=json.loads(expected_path.read_text())
    require(len(expected['obstruction_vector'])==16 and len(expected['polynomial_preimage'])==15,'Shipped witness dimensions changed.')
    require(all(sp.expand(sp.sympify(w,locals=dict(zip(['a','b','c','d'],variables)))-v)==0 for w,v in zip(expected['obstruction_vector'],obs_poly)),'Rebuilt quadratic representative disagrees with shipped witness.')
    require(all(sp.expand(sp.sympify(w,locals=dict(zip(['a','b','c','d'],variables)))-v)==0 for w,v in zip(expected['polynomial_preimage'],pre_poly)),'Rebuilt polynomial preimage disagrees with shipped witness.')
    report['comparison']={'shipped_witness_sha256':hashlib.sha256(expected_path.read_bytes()).hexdigest(),'full_vector_and_preimage_match':True,
                          'first_cochains_validated':True,'selected_D2_rebuilt_from_relation':True,
                          'all_15_direct_coefficients_checked':True,'parameter_divisions':False}
    # Only the lambda-dependent order-three difference is computed, not a full
    # third jet. It is the polarized quadratic BCH term of eta1 and kappa2.
    third_path=args.package/'data/order_3.json'
    third=json.loads(third_path.read_text())
    D3,cols3,rows3,vector3=rebuilt_block(third,3)
    require(D3.shape==(9,9) and D3.det()==1,'Unexpected D3 prescribed block.')
    inverse3=D3.inv()
    require(D3*inverse3==sp.eye(9),'D3 inverse failed.')
    kappa=mono((-1,0,0,0,0,2,0,0))
    require(delta({(i,):kappa for i in range(3)},0)=={},'Kappa2 is not closed.')
    require(poisson(kappa,f[1],0)=={},'Kappa2 does not annihilate the initial section.')
    check_grading(kappa,2,'W',0,'kappa2')
    lambda_tensors=tensors+[({}, {},{(i,):kappa for i in range(3)})]
    lreport={'normal_order':3,'normal_order_reason':'h*eta1 paired with h^2*lambda*kappa2 contributes first to h^3; quadratic kappa terms start at h^4.',
             'convention':'Coefficient of lambda in the quadratic BCH defect, i.e. its polarized eta1/kappa2 bracket with the displayed 1/2 normalization.',
             'source_columns':cols3,'target_rows':rows3,'D3_hom':[[str(v) for v in D3.row(i)] for i in range(9)],
             'D3_inverse':[[str(v) for v in inverse3.row(i)] for i in range(9)],'determinant':'1','coefficients':{}}
    for n in range(5):
        obs,stages=coeff_bch(lambda_tensors,n,5)
        checked=check_stage_gradings(stages,3)
        v=vector3(obs);p=inverse3*v
        require(D3*p==v,'Lambda order-three matrix witness failed.')
        src=plus(*(scalar(make_source(third['D3_source_basis'][j]),Q(c)) for j,c in zip(cols3,p)))
        primitive=exact_primitive(stages,src,3)
        lreport['coefficients'][NAMES[n]]={'raw_stages':encode(stages),'termwise_grading_checks':checked,
                                         'target_vector':[str(c) for c in v],'D3_inverse_preimage':[str(c) for c in p],
                                         'original_cover_primitive':primitive}
        print('lambda*'+NAMES[n]+': original-cover bracket checked; '+str(checked)+' termwise grades; D3 preimage '+str(list(p)))
    report['lambda_order_three']=lreport
    report['input_hashes'][str(third_path.relative_to(args.package))]=hashlib.sha256(third_path.read_bytes()).hexdigest()
    if args.verify_certificate:
        require(report==json.loads(args.verify_certificate.read_text()),'Regenerated audit certificate differs.')
        print('PASS: regenerated certificate equals frozen audit certificate.')
    else:
        args.output.write_text(json.dumps(report,indent=2)+'\n')
    print('PASS: full four-parameter original-cover brackets; 15 coefficients; regenerated D2; shipped vector and preimage agree.')
    if not args.verify_certificate:print(args.output)

if __name__=='__main__':main()
