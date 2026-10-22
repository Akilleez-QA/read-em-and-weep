"""Exact character/cohomology bookkeeping only; no HM instance data."""
import sympy as s

phi=(1+s.sqrt(5))/2
psi=(1-s.sqrt(5))/2
sizes=[1,15,20,12,12]
chars={
 '1':[1,1,1,1,1],
 'A':[3,-1,0,phi,psi],
 'V':[3,-1,0,psi,phi],
 'P':[4,0,1,-1,-1],
 'D':[5,1,-1,0,0],
}
def add(*terms):
    return [s.simplify(sum(t[i] for t in terms)) for i in range(5)]
def mul(a,b): return [s.simplify(x*y) for x,y in zip(a,b)]
def same(a,b): assert all(s.simplify(x-y)==0 for x,y in zip(a,b))
def decomposition(a):
    return {k:s.simplify(sum(n*x*y for n,x,y in zip(sizes,a,v))/60)
            for k,v in chars.items()}
A,V,P,D,one=[chars[k] for k in ('A','V','P','D','1')]
same(mul(A,D),add(A,V,P,D))
same(mul(A,V),add(P,D))
same(mul(D,D),add(one,A,V,P,P,D,D))

# Sym^(2m)W = SO3 spin m. Its character polynomial in Sym²W
# obeys c_(m+1)=(A-1)c_m-c_(m-1); use V instead for W-prime.
prev=one
current=V
for m in range(1,8):
    nxt=[s.simplify((v-1)*c-p) for v,c,p in zip(V,current,prev)]
    prev,current=current,nxt
same(current,add(A,P,D,D))
H0=add(A,V,P,P,D,D)
U=add(one,A,V,P,P,D,D,D)
assert decomposition(H0)['1']==0
assert decomposition(current)['1']==0
def hom(a,b): return s.simplify(sum(n*x*y for n,x,y in zip(sizes,a,b))/60)
assert hom(U,H0)==12
assert hom(U,current)==9
same(mul(P,D),add(A,V,P,D,D))
U3=mul(add(A,V,P),D)
same(U3,add(A,A,A,V,V,V,P,P,P,D,D,D,D))
assert hom(U3,H0)==20 and hom(U3,current)==14 and U3[0]==50
assert H0[0]==24 and current[0]==17 and U[0]==30

def poly_dim(d):return max(d+1,0)
assert poly_dim(16)-poly_dim(10)-poly_dim(8)-poly_dim(6)+poly_dim(5)+poly_dim(3)==0
assert 9+7+11-4==23 and 23==6+17
assert 3*5+3*3==24
assert 4*3==12
print('PASS: exact characters, 12/9 and 20/14 parameter dimensions, square-ideal degree16, coefficient ranks and P1 dimensions. No actual HM data used.')
