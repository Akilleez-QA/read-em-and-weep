"""Exact invented exterior-algebra checks; no physical source inputs/imports."""
from fractions import Fraction as F
from itertools import permutations
import json
from random import Random

ZERO=(F(0),)*4
ID=(F(1),F(0),F(0),F(1))
h=(F(1),F(0),F(0),F(-1))
e=(F(0),F(1),F(0),F(0))
f=(F(0),F(0),F(1),F(0))
PERMS=tuple(permutations(range(4)))

def plus(*xs): return tuple(sum(x[i] for x in xs) for i in range(4))
def times(c,x): return tuple(c*v for v in x)
def mm(x,y): return (x[0]*y[0]+x[1]*y[2],x[0]*y[1]+x[1]*y[3],x[2]*y[0]+x[3]*y[2],x[2]*y[1]+x[3]*y[3])
def tr(x): return x[0]+x[3]
def trans(x): return (x[0],x[2],x[1],x[3])
def comm(x,y): return plus(mm(x,y),times(-1,mm(y,x)))
def sign(p): return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
def need(x,msg):
    if not x: raise RuntimeError(msg)
def mval(a,b,c): return (F(a),F(b),F(c),F(-a))
def array(seed):
    rng=Random(str(seed))
    return [mval(*(rng.randrange(-7,8) for _ in range(3))) for a in range(4)]

def wedge_sign(a,b):
    return (-1)**sum((a>>i)&1 and (b>>j)&1 for i in range(4) for j in range(i))
def fadd(*fs):
    out={}
    for form in fs:
        for k,v in form.items(): out[k]=plus(out.get(k,ZERO),v)
    return {k:v for k,v in out.items() if v!=ZERO}
def fs(c,x): return {k:times(c,v) for k,v in x.items() if times(c,v)!=ZERO}
def wedge(x,y):
    out={}
    for a,xa in x.items():
        for b,yb in y.items():
            if not a&b:
                out[a|b]=plus(out.get(a|b,ZERO),times(wedge_sign(a,b),mm(xa,yb)))
    return {k:v for k,v in out.items() if v!=ZERO}
def power(x,n):
    out={0:ID}
    for _ in range(n): out=wedge(out,x)
    return out
def traceform(x): return {k:times(tr(v),ID) for k,v in x.items() if tr(v)}
def form(x): return {1<<a:x[a] for a in range(4)}
def four(x): return x.get(15,ZERO)
def comp(x,indices):
    if len(set(indices))<len(indices): return ZERO
    return times(sign(indices),x.get(sum(1<<a for a in indices),ZERO))

def K(x,a,b): return times(F(1,4),comm(x[a],x[b]))
def T4(l,u,a,b,c,d):
    return times(F(1,4),plus(times(tr(mm(u[a],K(u,c,d))),l[b]),times(-tr(mm(u[b],K(u,c,d))),l[a]),times(tr(mm(l[b],K(l,c,d))),u[a]),times(-tr(mm(l[a],K(l,c,d))),u[b])))
def ct(l,u,a,b): return (tr(mm(u[a],l[b]))-tr(mm(u[b],l[a])))/4
def quartic(l,u,a,b,c,d):
    v=[plus(x,y) for x,y in zip(l,u)]
    return plus(times(F(1,2),plus(comm(K(u,a,b),K(l,c,d)),comm(K(u,c,d),K(l,a,b)))),T4(l,u,a,b,c,d),T4(l,u,c,d,a,b),times(-ct(l,u,c,d),K(v,a,b)),times(-ct(l,u,a,b),K(v,c,d)))
def altq(l,u): return times(F(1,24),plus(*(times(sign(p),quartic(l,u,*p)) for p in PERMS)))
def qform(l,u):
    L,U=form(l),form(u)
    return fs(F(1,24),wedge(traceform(wedge(U,L)),fadd(power(L,2),power(U,2))))
def E(l,u,di,dj,a,b,c,d):
    return times(F(1,2),plus(times(dj[a,c,d],l[b]),times(-dj[b,c,d],l[a]),times(di[b,c,d],u[a]),times(-di[a,c,d],u[b])))
def alte(l,u,di,dj):
    return times(F(1,24),plus(*(times(sign(p),plus(E(l,u,di,dj,*p),E(l,u,di,dj,p[2],p[3],p[0],p[1]))) for p in PERMS)))
def exterior_derivative(ds):
    out={}
    for a in range(4):
        for c in range(4):
            for d in range(c+1,4):
                if a not in (c,d):
                    mask=(1<<a)|(1<<c)|(1<<d)
                    out[mask]=plus(out.get(mask,ZERO),times(sign((a,c,d))*ds[a,c,d],ID))
    return out

def quartic_checks():
    for n in range(1,25):
        l,u=array(n),array(-n-2)
        L,U=form(l),form(u)
        t=traceform(wedge(U,L))
        need(fadd(wedge(U,L),fs(-1,wedge(L,U)))==t,'graded anticommutator')
        for X in (L,U): need(power(X,3)==fs(F(1,2),traceform(power(X,3))),'scalar cubic')
        need(fadd(wedge(power(U,2),power(L,2)),fs(-1,wedge(power(L,2),power(U,2))))==fs(2,wedge(t,fadd(wedge(U,L),wedge(L,U)))),'square commutator')
        need(wedge(traceform(power(U,3)),L)==fs(3,wedge(t,power(U,2))),'cubic-U identity')
        need(wedge(traceform(power(L,3)),U)==fs(-3,wedge(t,power(L,2))),'cubic-L identity')
        need(altq(l,u)==four(qform(l,u)),'full quartic exterior expression')
    l,u=[h,e,f,ZERO],[ZERO,ZERO,ZERO,h]
    need(altq(l,u)==times(F(-1,12),h),'required -h/12 control')
    need(altq(l,u)==four(qform(l,u)),'negative control form coefficient')

def scalar_alternation_checks():
    for n in range(1,17):
        l,u=array(n),array(2*n+3)
        ds=[]
        anti=[]
        for endpoint in (1,2):
            d={}; a={}
            for v in range(4):
                for c in range(4):
                    for e_ in range(4):
                        a[v,c,e_]=F((c-e_)*(n+v+endpoint)*(c+e_+2))
                        # Arbitrary symmetric pair correction also differentiates.
                        d[v,c,e_]=a[v,c,e_]+F((c+e_+1)*(n-v+endpoint))
            ds.append(d); anti.append(a)
        expected=fs(F(1,6),fadd(wedge(exterior_derivative(anti[1]),form(l)),fs(-1,wedge(exterior_derivative(anti[0]),form(u)))))
        need(alte(l,u,*ds)==four(expected),'E exterior coefficient with symmetric raw correction retained')

# Flat invented block data: at a point these are the coefficients of
# -d exp(-sum_a x_a B_a) exp(sum_a x_a B_a), so dB=-B^2.
def derivative(B,a,c): return times(F(-1,2),comm(B[a],B[c]))
def ds_from_raw(Bi,Bj):
    ds={}
    for a in range(4):
        for c in range(4):
            for d in range(4):
                ds[a,c,d]=F(1,4)*tr(plus(mm(derivative(Bi,a,c),Bj[d]),mm(Bi[c],derivative(Bj,a,d)),times(-1,mm(derivative(Bi,a,d),Bj[c])),times(-1,mm(Bi[d],derivative(Bj,a,c)))))
    return ds

def Tform(Bi,Bj):
    I,J=form(Bi),form(Bj)
    return traceform(fadd(wedge(I,power(J,2)),fs(-1,wedge(power(I,2),J))))
def cubic_form(B): return traceform(power(form(B),3))
def edge_current(Bi,Bj): return [times(-1,trans(plus(y,times(-1,x)))) for x,y in zip(Bi,Bj)]

def transgression_checks():
    nonzero=0
    for n in range(1,21):
        bi,bj,bk=array(n),array(-n-3),array(2*n+5)
        l,u=edge_current(bi,bj),edge_current(bj,bk)
        L,U=form(l),form(u)
        Zij,Zjk=Tform(bi,bj),Tform(bj,bk)
        zi,zj,zk=map(cubic_form,(bi,bj,bk))
        for bx,by,current,T in ((bi,bj,l,Zij),(bj,bk,u,Zjk)):
            ds=ds_from_raw(bx,by)
            need(exterior_derivative(ds)==fs(F(1,4),T),'dS=T/4 from flat jets')
            need(fs(3,T)==fadd(cubic_form(by),fs(-1,cubic_form(bx)),fs(-1,traceform(power(form(current),3)))),'cubic edge transgression with row transpose')
            # Scalar shift in a cubic trace, with arbitrary scalar one-form.
            x=fadd(form(by),fs(-1,form(bx)))
            scalar={1<<a:times(F(n+a),ID) for a in range(4)}
            need(traceform(power(fadd(x,scalar),3))==traceform(power(x,3)),'scalar shift cubic invariance')
        actual=plus(altq(l,u),alte(l,u,ds_from_raw(bi,bj),ds_from_raw(bj,bk)))
        expected=four(fs(F(1,72),fadd(wedge(fadd(zk,fs(-1,zj)),L),fs(-1,wedge(fadd(zj,fs(-1,zi)),U)))))
        pij=fs(F(-1,72),wedge(fadd(zi,zj),L))
        pjk=fs(F(-1,72),wedge(fadd(zj,zk),U))
        pik=fs(F(-1,72),wedge(fadd(zi,zk),fadd(L,U)))
        boundary=four(fadd(pjk,fs(-1,pik),pij))
        need(actual==expected==boundary,'full raw Q4+E alternation equals explicit boundary')
        if actual!=ZERO:
            nonzero+=1
            need(actual!=times(-1,boundary),'wrong-sign primitive rejected')
    need(nonzero>0,'controls must detect a nonzero pointwise representative')
    return nonzero

if __name__=='__main__':
    quartic_checks()
    scalar_alternation_checks()
    count=transgression_checks()
    print(json.dumps({'status':'PASS','quartic_cases':24,'scalar_alternation_cases':16,'flat_transgression_cases':20,'nonzero_boundary_controls':count,'negative_control':'-h/12','source_evaluation':False},sort_keys=True))
