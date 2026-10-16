"""Invented contractible-pair controls, deliberately with [D,B_i] != 0."""
from fractions import Fraction as F
from random import Random
import json
import check_exterior as E

N=4
Z=(F(0),)*(N*N)

def ma(*xs): return tuple(sum(x[i] for x in xs) for i in range(N*N))
def ms(c,x): return tuple(c*y for y in x)
def mm(a,b): return tuple(sum(a[N*i+k]*b[N*k+j] for k in range(N)) for i in range(N) for j in range(N))
def st(a): return a[0]+a[5]+a[10]-a[15]
def br(a,b): return ma(mm(a,b),ms(-1,mm(b,a)))
def sp(a,b): return ma(a,ms(-1,b))
def ident(): return tuple(F(i==j) for i in range(N) for j in range(N))
def fa(*xs):
    out={}
    for x in xs:
        for k,v in x.items(): out[k]=ma(out.get(k,Z),v)
    return {k:v for k,v in out.items() if v!=Z}
def fs(c,x): return {k:ms(c,v) for k,v in x.items() if ms(c,v)!=Z}
def fw(x,y):
    out={}
    for a,xa in x.items():
        for b,yb in y.items():
            if not a&b: out[a|b]=ma(out.get(a|b,Z),ms(E.wedge_sign(a,b),mm(xa,yb)))
    return {k:v for k,v in out.items() if v!=Z}
def cube(B):
    x={1<<a:B[a] for a in range(4)}
    return fw(fw(x,x),x)
def sz(B): return {mask:E.times(st(v),E.ID) for mask,v in cube(B).items() if st(v)}
def derivatives(B,a,c): return ms(F(-1,2),br(B[a],B[c]))
def ds(A,B):
    return {(a,c,d):st(ma(mm(derivatives(A,a,c),B[d]),mm(A[c],derivatives(B,a,d)),ms(-1,mm(derivatives(A,a,d),B[c])),ms(-1,mm(A[d],derivatives(B,a,c)))))/4 for a in range(4) for c in range(4) for d in range(4)}
def coh(x): return (x[0],x[1],x[4],x[5])
def current(A,B): return [E.times(-1,E.trans(coh(sp(b,a)))) for a,b in zip(A,B)]
def sample(seed):
    r=Random(seed)
    def v(): return F(r.randrange(-5,6))
    common=[]
    for a in range(4):
        # Common basis motion need not be a chain map. It varies D itself.
        common.append((v(),v(),v(),0,v(),v(),v(),0,v(),v(),v(),0,0,0,0,v()))
    vertices=[]
    for vertex in range(3):
        Bs=[]
        for a in range(4):
            x,y,z,c,u,w=(v() for _ in range(6))
            # Degree zero has H^0 of rank two and a rank-one paired summand.
            # D maps coordinate 2 to coordinate 3. C commutes with D.
            C=(x,y,u,0,z,-x,w,0,0,0,c,0,0,0,0,c)
            Bs.append(ma(common[a],C))
        vertices.append(Bs)
    return vertices

if __name__=='__main__':
    D=tuple(F(i==3 and j==2) for i in range(N) for j in range(N))
    count=0
    for seed in range(1,17):
        bi,bj,bk=sample(seed)
        E.need(any(br(D,x)!=Z for x in bi),'B must not itself be a chain map')
        E.need(all(br(D,sp(x,y))==Z for x,y in zip(bj,bi)),'connection differences must be chain maps')
        l,u=current(bi,bj),current(bj,bk)
        for A,B,x in ((bi,bj,l),(bj,bk,u)):
            difference=[sp(b,a) for a,b in zip(A,B)]
            lhs={mask:E.times(st(v),E.ID) for mask,v in cube(difference).items() if st(v)}
            rhs=E.traceform(E.power(E.form(x),3))
            E.need(lhs==rhs,'chainmap supertrace cubic equals row cohomology cubic')
        zi,zj,zk=sz(bi),sz(bj),sz(bk)
        actual=E.plus(E.altq(l,u),E.alte(l,u,ds(bi,bj),ds(bj,bk)))
        pij=E.fs(F(-1,72),E.wedge(E.fadd(zi,zj),E.form(l)))
        pjk=E.fs(F(-1,72),E.wedge(E.fadd(zj,zk),E.form(u)))
        pik=E.fs(F(-1,72),E.wedge(E.fadd(zi,zk),E.fadd(E.form(l),E.form(u))))
        boundary=E.four(E.fadd(pjk,E.fs(-1,pik),pij))
        E.need(actual==boundary,'full non-chainmap B control equals boundary')
        if actual!=E.ZERO: count+=1
    E.need(count>0,'nonzero controls required')
    print(json.dumps({'status':'PASS','contractible_pair_cases':16,'nonzero_boundaries':count,'individual_B_chainmap':False,'source_evaluation':False},sort_keys=True))
