#!/usr/bin/env python3
"""Independent universal rank-four corner control; no actual HM instances."""
from pathlib import Path
from hashlib import sha256
from itertools import combinations_with_replacement
import json

ROOT=Path(__file__).resolve().parent
NAMES=('1','W','A','S4','D','T6','P',"W'",'V')
DIMS=(1,2,3,4,5,6,4,2,3)
PARITY=(0,1,0,1,0,1,0,1,0)
EDGES=((0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(5,8))
ZERO=(0,)*9

def require(c,why):
    if not c:raise ValueError(why)
def vec(**kw):return tuple(kw.get(n,0) for n in NAMES)
def add(*xs):return tuple(sum(x[i] for x in xs) for i in range(9))
def scale(x,n):return tuple(n*c for c in x)
def sub(a,b):return add(a,scale(b,-1))
def dim(v):return sum(a*b for a,b in zip(v,DIMS))
def times_w(v):
    r=[0]*9
    for i,j in EDGES:r[i]+=v[j];r[j]+=v[i]
    return tuple(r)
def sym_times(v,n):
    require(n>=0,'negative symmetric index')
    p,c=ZERO,v
    for _ in range(n):p,c=c,sub(times_w(c),p)
    return c
def char(v):return {n:c for n,c in zip(NAMES,v) if c}
def qbadd(x,y):return (x[0]+y[0],x[1]+y[1])
def qbscale(x,n):return (n*x[0],n*x[1])
def qbmul(x,y):
    a,b=x;c,d=y
    return (a*c+b*d,a*d+b*c+b*d)
def poly_sym(x,n):
    p,c=(0,0),(1,0)
    for _ in range(n):p,c=c,qbadd(qbmul(x,c),qbscale(p,-1))
    return c

def build_table():
    # Binary icosahedral SU(2) trace classes: phi^2=phi+1.
    xs=((2,0),(-2,0),(0,0),(1,0),(-1,0),(0,1),(0,-1),(-1,1),(1,-1))
    sizes=(1,1,30,20,20,12,12,12,12)
    rows=[]
    for x in xs:
        ss=[poly_sym(x,n) for n in range(8)]
        wp=qbadd(ss[7],qbscale(ss[5],-1))
        p=qbmul(x,wp)
        v=qbadd(ss[6],qbscale(p,-1))
        rows.append(ss[:6]+[p,wp,v])
    require(sum(sizes)==120,'class order')
    require(tuple(y[0] for y in rows[0])==DIMS and all(y[1]==0 for y in rows[0]),'dimension row')
    for i in range(9):
        for j in range(9):
            total=(0,0)
            for w,row in zip(sizes,rows):total=qbadd(total,qbscale(qbmul(row[i],row[j]),w))
            require(total==(120*int(i==j),0),'exact character orthogonality')
        vi=tuple(int(j==i) for j in range(9))
        product=times_w(vi)
        for x,row in zip(xs,rows):
            got=(0,0)
            for c,y in zip(product,row):got=qbadd(got,qbscale(y,c))
            require(got==qbmul(x,row[i]),'independent McKay multiplication')
    for n in range(10):
        for i in range(9):
            prod=sym_times(tuple(int(j==i) for j in range(9)),n)
            require(min(prod)>=0,'non-genuine tensor character')
            for x,row in zip(xs,rows):
                got=(0,0)
                for c,y in zip(prod,row):got=qbadd(got,qbscale(y,c))
                require(got==qbmul(poly_sym(x,n),row[i]),'direct class-value cross-check')
    return {'class_sizes':sizes,'class_trace_phi_coordinates':xs,'orthogonal_irreducibles':9,'tensor_checks':90}

def bundle_h0(blocks,t):
    return add(*(sym_times(tuple(int(j==i) for j in range(9)),e+t) for e,i in blocks if e+t>=0))
def bundle_h1(blocks,t):
    return add(*(sym_times(tuple(int(j==i) for j in range(9)),-e-t-2) for e,i in blocks if e+t<=-2))
def bundle_euler(blocks,t):return sub(bundle_h0(blocks,t),bundle_h1(blocks,t))

def source_control():
    m3=vec(**{"W'":3,'S4':3,'T6':6});m4=vec(V=2,P=4,D=3)
    h1=sub(times_w(m4),m3)
    require(h1==vec(**{"W'":1,'T6':3}),'actual E(1) cohomology input arithmetic')
    # maxdeg E <= -3 and total deficit 3 permit only one dimension-three
    # even degree -4 block, or a single trivial degree -6 block.
    even_rank3=[vec(A=1),vec(V=1),vec(**{'1':3})]
    residuals=[sub(h1,times_w(r)) for r in even_rank3]
    require([i for i,v in enumerate(residuals) if min(v)>=0]==[1],'unique degree -4 coefficient')
    require(residuals[1]==vec(**{"W'":1,'T6':2}),'Z coefficient')
    require(min(sub(h1,sym_times(vec(**{'1':1}),3)))<0,'degree -6 tail forbidden')
    return {'deficit':3,'degree_minus4_coefficient':'V','degree_minus3_coefficient':char(residuals[1]),'historical_enumeration_used':False}

def integer_control():
    # Equality is a formal identity in a,c1,delta1,...,delta5.
    # Coefficient vectors avoid any finite sampling of this identity.
    a=(1,0,0,0,0,0,0,0)
    c=(0,1,0,0,0,0,0,0)
    def plus(*vs):return tuple(sum(v[i] for v in vs) for i in range(8))
    def mul(v,n):return tuple(n*x for x in v)
    cs=[]
    for i in range(6):
        row=list(c);row[7]=8*i
        for j in range(i):row[2+j]=1
        cs.append(tuple(row))
    E=plus(a,*cs[:3]);b=plus(a,*cs)
    lhs=plus(a,b,mul(E,-2))
    require(lhs==(0,0,1,2,3,2,1,72),'formal six-block determinant identity')
    require(2*(-54)+72==-36,'identity constant')
    bounds=(-30,-6);weights=(1,2,3,2,1)
    require(sum(bounds)==-36 and min(weights)>0,'equality trapping')
    aa,bb=-30,-6;cc=(-54-aa-24)//3
    degrees=tuple(cc+8*i for i in range(6))
    require(degrees==(-16,-8,0,8,16,24),'graded degrees')
    require(aa+sum(degrees)==bb,'endpoint degrees')
    return {'a':aa,'b':bb,'determinant_defects':[0]*5,'graded_degrees':degrees,
            'F0_rank_degree_top':[5,-30,-6],'F1_rank_degree_top':[9,-46,-5],'F2_rank_degree_top':[13,-54,-4],
            'F1_excess':46-5*9,'F2_excess':54-4*13}

def quotient_control():
    U=vec(**{"W'":1,'T6':2})
    targets=[add(U,vec(W=1)),add(U,vec(**{"W'":1}))]
    blocks=[(e,i) for e in range(-2,7) for i in range(9) if DIMS[i]<=4 and PARITY[i]==e%2]
    eligible=[]
    for e,i in blocks:
        h=bundle_h0([(e,i)],3)
        if any(all(x<=y for x,y in zip(h,t)) for t in targets):eligible.append((e,i))
    expected=[(-2,0),(-2,6),(-2,8),(-1,7),(2,0),(3,1),(4,0)]
    require(eligible==expected,'complete positive-character block filter')
    # Independent rank/degree multiset control; no historical source list.
    shapes=[];survivors=[]
    for count in range(1,5):
        for row in combinations_with_replacement(blocks,count):
            if sum(DIMS[i] for e,i in row)!=4 or sum(e*DIMS[i] for e,i in row)!=0:continue
            shapes.append(row)
            if bundle_h0(row,3) in targets:survivors.append(row)
    survivor=((-2,0),(-1,7),(4,0))
    require(len(shapes)==20,'new complete forced-window shape count')
    require(survivors==[survivor],'unique quotient shape')
    require(bundle_h1(survivor,1)==ZERO,'slope-window acyclicity')
    require(bundle_h0(survivor,1)==vec(**{"W'":1,'T6':1}),'quotient twist1')
    require(bundle_h0(survivor,3)==targets[0],'cubic exact sequence')
    E=[(-3,7),(-3,5),(-3,5),(-4,8)]
    chi_kernel=sub(bundle_euler(E,4),bundle_euler(survivor,4))
    require(chi_kernel==vec(A=-1,V=2,P=2),'kernel Euler identity')
    possible_h1=[ZERO,vec(**{'1':1})]
    impossible=[add(chi_kernel,v) for v in possible_h1]
    require(all(v[2]==-1 for v in impossible),'negative physical A obstruction')
    require(dim(chi_kernel)==11,'ordinary Euler dimension')
    return {'eligible_blocks':[{'degree':e,'coefficient':NAMES[i],'H0_twist3':char(bundle_h0([(e,i)],3))} for e,i in eligible],
            'universal_shapes':len(shapes),'unique_survivor':[[e,NAMES[i]] for e,i in survivor],
            'H0_B1':char(bundle_h0(survivor,1)), 'H0_B3':char(bundle_h0(survivor,3)),
            'chi_F2_4':char(chi_kernel),'possible_H0_F2_4':[char(v) for v in impossible]}

def authenticate():
    p=ROOT/'INPUTS.json'
    if not p.exists():raise ValueError('missing hash manifest')
    records=json.loads(p.read_text())
    for r in records:
        data=(ROOT/r['file']).read_bytes()
        require(sha256(data).hexdigest()==r['sha256'],'source changed: '+r['file'])
        require(len(data)==r['bytes'],'source length changed')
    return len(records)

def main():
    out={'verdict':'PASS, conditional on stated actual geometric premises','authenticated_inputs':authenticate(),
         'independent_character_control':build_table(),'source_Z_without_historical_enumeration':source_control(),
         'integer_control':integer_control(),'quotient_control':quotient_control(),
         'actual_HM_coefficients_parameters_jets_matrices_or_ranks_evaluated':False,
         'rank_three_exclusion_transplanted':False,
         'scope':'Only generic rank four with maximal ordered plateau (3,3) is excluded.'}
    print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__':main()
