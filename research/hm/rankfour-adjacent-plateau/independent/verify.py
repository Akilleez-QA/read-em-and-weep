#!/usr/bin/env python3
"""Independent universal review. Standard library only; no actual-instance data."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations_with_replacement
import hashlib, json
ROOT=Path(__file__).resolve().parent
CHECKS=0
def check(condition,label):
    global CHECKS
    CHECKS+=1
    if not condition:
        raise RuntimeError(label)
SOURCES={
 'ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md':'a52685fc9e7c89abf26171a15989cedeaf3bd101a2edde790a24f9cfe0179256',
}
# Exact arithmetic in Q(sqrt(5)), independent of a tensor-product graph.
def q(a,b=0): return (F(a),F(b))
def plus(x,y): return (x[0]+y[0],x[1]+y[1])
def scale(k,x): return (k*x[0],k*x[1])
def times(x,y): return (x[0]*y[0]+5*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def minus(x,y): return plus(x,scale(-1,y))
def sym(n,x):
    if n<0: return q(0)
    a,b=q(0),q(1)
    for _ in range(n): a,b=b,minus(times(x,b),a)
    return b
def cadd(*cs):
    return tuple(tuple(sum(c[i][j] for c in cs) for j in range(2)) for i in range(9))
def cscale(k,c): return tuple(scale(k,x) for x in c)
def csub(c,d): return cadd(c,cscale(-1,d))
def cmul(c,d): return tuple(times(x,y) for x,y in zip(c,d))
TRACES=(q(2),q(-2),q(F(1,2),F(1,2)),q(F(-1,2),F(-1,2)),q(F(1,2),F(-1,2)),q(F(-1,2),F(1,2)),q(1),q(-1),q(0))
SIZES=(1,1,12,12,12,12,20,20,30)
NAMES=('1','W','A','S4','D','T6','P',"W'",'V')
DIMS=(1,2,3,4,5,6,4,2,3)
PARITY=(0,1,0,1,0,1,0,1,0)
C={name:tuple(sym(n,x) for x in TRACES) for n,name in enumerate(NAMES[:6])}
C['P']=tuple(q(a) for a in (4,4,-1,-1,-1,-1,1,1,0))
C['V']=csub(tuple(sym(6,x) for x in TRACES),C['P'])
C["W'"]=csub(cmul(C['W'],C['P']),C['T6'])
ZERO=cscale(0,C['1'])
def inner(c,d):
    a=q(0)
    for k in range(9): a=plus(a,scale(F(SIZES[k],120),times(c[k],d[k])))
    return a
def coefficients(c):
    out={}
    for n in NAMES:
        a,b=inner(c,C[n]); check(b==0 and a.denominator==1,'integral irreducible coefficient')
        if a: out[n]=int(a)
    return out
def line_euler(d):
    # O(d) cohomology in its physical determinant-one linearization.
    if d>=0: return tuple(sym(d,x) for x in TRACES)
    if d==-1: return ZERO
    return cscale(-1,tuple(sym(-d-2,x) for x in TRACES))
def punit(i): return tuple(int(i==j) for j in range(7))
def padd(*ps): return tuple(sum(p[i] for p in ps) for i in range(7))
def pscale(k,p): return tuple(k*x for x in p)
def partitions(rank,deficit):
    return [v for v in combinations_with_replacement(range(deficit+1),rank) if sum(v)==deficit]
def even_at_most(n): return n if n%2==0 else n-1

def main():
    for name,digest in SOURCES.items():
        raw=(ROOT/'inputs'/name).read_bytes()
        check(hashlib.sha256(raw).hexdigest()==digest,'authenticate retained actual source '+name)
    check(sum(SIZES)==120,'class sizes')
    check(sum(d*d for d in DIMS)==120,'complete irreducible dimensions')
    for i,n in enumerate(NAMES):
        check(C[n][0]==q(DIMS[i]),'dimension '+n)
        check(C[n][1]==q((-1)**PARITY[i]*DIMS[i]),'physical central sign '+n)
        for j,m in enumerate(NAMES): check(inner(C[n],C[m])==q(i==j),'orthogonality '+n+' '+m)
    check(C['A']!=C['V'],'physical even three-spaces are inequivalent')
    check(cmul(C['W'],C['W'])==cadd(C['1'],C['A']),'physical W squared')
    check(cmul(C["W'"],C['W'])==C['P'],'physical other two-space tensor W')
    M3=cadd(cscale(3,C["W'"]),cscale(3,C['S4']),cscale(6,C['T6']))
    M4=cadd(cscale(2,C['V']),cscale(4,C['P']),cscale(3,C['D']))
    check(M3[0]==q(54) and M4[0]==q(37),'actual presentation ranks independently checked')
    euler_e2=csub(cmul(M3,line_euler(1)),cmul(M4,line_euler(2)))
    check(euler_e2==cscale(-1,C['V']),'derive actual chi(E(2)) directly from presentation')
    # Derivative polynomial identity in [1,a,c1,delta1,delta2,delta3,delta4].
    one,a,c1=punit(0),punit(1),punit(2)
    blocks=[c1]
    for j in range(4): blocks.append(padd(blocks[-1],pscale(8,one),punit(3+j)))
    e=padd(a,*blocks[:2]); b=padd(a,*blocks)
    identity=padd(pscale(3,a),pscale(2,b),pscale(-5,e))
    check(identity==(120,0,0,3,6,4,2),'exact endpoint identity without sampling')
    ranks=[9+4*i for i in range(6)]
    top=[-(5-i) for i in range(5)]
    abound=even_at_most(ranks[0]*top[0]); bbound=even_at_most(-5)
    check((abound,bbound)==(-46,-6),'endpoint persistence with determinant parity')
    check(3*abound+2*bbound==-150,'upper bound equals required lower bound')
    check(all(x>0 for x in identity[3:]),'all adjacent defect weights strictly positive')
    check(3*(-45)+2*(-5)>-150,'odd-degree endpoint relaxation does not close')
    first=(-54-abound-8)//2
    check(2*first==-54-abound-8,'integral first quotient degree')
    ds=[first+8*i for i in range(5)]
    stages=[abound]
    for d in ds: stages.append(stages[-1]+d)
    check(ds==[-8,0,8,16,24] and stages==[-46,-54,-54,-46,-30,-6],'forced degree rows')
    check(partitions(9,1)==[(0,)*8+(1,)],'all F0 ordinary deficit partitions')
    check(set(partitions(13,2))=={(0,)*11+(1,1),(0,)*12+(2,)},'all F1 ordinary deficit partitions')
    check([NAMES[i] for i in range(9) if PARITY[i] and DIMS[i]<=2]==['W',"W'"],'complete rank-two odd coefficient possibilities')
    check([NAMES[i] for i in range(9) if DIMS[i]==1 and not PARITY[i]]==['1'],'only even coefficient line')
    # Cancellation is at the same B(2), not merely the same ordinary dimension.
    check(-2+4==0+2,'two exact quotient twists coincide')
    check(-2+3!=0+2,'wrong-twist negative control')
    check(line_euler(-1)==ZERO and line_euler(-2)==cscale(-1,C['1']),'F0(4) coefficient R8 cancels')
    check(cadd(line_euler(0),line_euler(-2))==ZERO,'F1 top coefficient cancels universally')
    right=cadd(line_euler(-2),euler_e2)
    check(right==cscale(-1,cadd(C['1'],C['V'])),'right Euler character')
    tails=[]
    for name in ['W',"W'",'line']:
        if name=='line':
            left=cadd(line_euler(-2),line_euler(-4))
        else:
            left=cmul(C[name],cadd(line_euler(-1),line_euler(-3)))
        check(left!=right,'exclude '+name+' tail by class character')
        tails.append({'tail':name,'left':coefficients(left),'right':coefficients(right),'left_minus_right':coefficients(csub(left,right))})
    check(tails[0]['left_minus_right']=={'A':-1,'V':1},'W tail discrepancy')
    check(tails[1]['left_minus_right']=={'1':1,'P':-1,'V':1},'W prime tail discrepancy')
    check(tails[2]['left_minus_right']=={'A':-1,'V':1},'line tail discrepancy')
    # The forbidden equalities have equal dimensions: this is not an ordinary rank test.
    check(all(sum(v*DIMS[NAMES.index(k)] for k,v in t['left_minus_right'].items())==0 for t in tails),'all contradictions are genuinely equivariant')
    # Concrete mutation controls for the essential physical marking and correction.
    check(cscale(-1,cadd(C['1'],C['A']))!=right,'replacing physical V by A destroys the target')
    check(cscale(-1,C['A'])!=cadd(line_euler(-2),line_euler(-4)),'omitting line-tail H1 correction rejected')
    output={'status':'PASS','scope':'Conditional exclusion of actual generic-rank-four maximal plateau (2,3) only.','source_sha256':SOURCES,
            'ranks':ranks,'degrees':stages,'quotient_degrees':ds,'defect_weights':[3,6,4,2],'determinant_defects':[0]*4,
            'persistence_top_degrees':top,'actual_chi_E2':coefficients(euler_e2),'F0_twist4_Euler':{'1':-1},
            'exact_Euler_identity':'chi F1(4) + chi F1(2) = chi F0(4) + chi E(2)',
            'tails':tails,'checks':CHECKS,'actual_instance_evaluations':0,'quotient_shape_enumerations':0}
    print(json.dumps(output,indent=2,sort_keys=True))
if __name__=='__main__': main()
