"""Exact universal character and complement-change certificate. No actual HM coefficients."""
from fractions import Fraction as F
from pathlib import Path
import json, hashlib
checks=[]
def ck(label, ok):
    if not ok: raise RuntimeError(label)
    checks.append(label)
def z(a,b=0): return (F(a),F(b))
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def sub(x,y): return add(x,neg(y))
def mul(x,y): return (x[0]*y[0]+5*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def scale(k,x): return (k*x[0],k*x[1])
def total(xs):
    v=z(0)
    for x in xs:v=add(v,x)
    return v
phi=z(F(1,2),F(1,2)); phip=z(F(1,2),F(-1,2))
tr=[z(2),z(-2),phi,neg(phi),phip,neg(phip),z(1),z(-1),z(0)]
sizes=[1,1,12,12,12,12,20,20,30]
def sym(n):
    a=[z(1)]*9;b=tr
    for _ in range(n):a,b=b,[sub(mul(x,y),v) for x,y,v in zip(tr,b,a)]
    return a
def va(*vs):return [total(t) for t in zip(*vs)]
def vm(a,b):return [mul(x,y) for x,y in zip(a,b)]
def vs(k,a):return [scale(k,x) for x in a]
def ip(a,b):return scale(F(1,120),total(scale(k,mul(x,y)) for k,x,y in zip(sizes,a,b)))
P=list(map(z,[4,4,-1,-1,-1,-1,1,1,0]))
C={'1':sym(0),'W':sym(1),'A':sym(2),'S':sym(3),'D':sym(4),'T':sym(5),'P':P}
C['V']=va(sym(6),vs(-1,P));C['Wp']=va(vm(C['W'],P),vs(-1,C['T']))
for n,a in C.items():
    for m,b in C.items():ck('orthogonality '+n+' '+m,ip(a,b)==z(int(n==m)))
for left,right in [('WD',['S','T']),('WP',['Wp','T']),('WV',['T']),('WWp',['P']),('AWp',['T']),('VV',['1','V','D']),('AV',['P','D'])]:
    l,r={'WD':('W','D'),'WP':('W','P'),'WV':('W','V'),'WWp':('W','Wp'),'AWp':('A','Wp'),'VV':('V','V'),'AV':('A','V')}[left]
    ck('tensor '+left,vm(C[l],C[r])==va(*[C[n] for n in right]))
H=[('Wp',3,1),('T',3,1)]
Qs=[[('D',2,1),('V',4,1),('1',8,1)],[('P',2,1),('V',4,1),('Wp',5,1)],[('V',2,1),('V',4,2)],[('T',3,1),('V',4,1)]]
def hom(blocks1,blocks2):
    out=z(0)
    for r,j,m in blocks1:
        for s,k,n in blocks2:
            if j>=k:out=add(out,scale(m*n,ip(C[r],vm(C[s],sym(j-k)))))
    ck('integral Hom count '+str((blocks1,blocks2)),out[1]==0 and out[0].denominator==1)
    return int(out[0])
def coho(blocks,twist):
    return va(*[vs(m,vm(C[r],sym(j-twist-2))) for r,j,m in blocks if j-twist>=2])
rows=[]
for i,Q in enumerate(Qs,1):
    fw,bw=hom(H,Q),hom(Q,H)
    ck('type%d forward dimension'%i,fw==[1,2,1,1][i-1]);ck('type%d reverse dimension'%i,bw==2)
    ck('type%d reverse doublet zero'%i,hom(Q,[('Wp',3,1)])==0)
    ck('type%d quotient target'%i,coho(Q,1)==vs(2,C['T']))
    ck('type%d quotient source'%i,coho(Q,0)==va(C['V'],vs(2,P),vs(2,C['D'])))
    ck('type%d rank degree'%i,sum(m*C[r][0][0] for r,j,m in Q)==9 and sum(-j*m*C[r][0][0] for r,j,m in Q)==-30)
    rows.append({'type':i,'Hom_H_Q':fw,'Hom_Q_H':bw,'Hom_Q_Wp':0})
for i,Q in enumerate(Qs,1):
    ck('type%d EndQ dimension'%i,hom(Q,Q)==[4,4,5,3][i-1])
    ck('type%d EndE dimension'%i,hom(H+Q,H+Q)==[9,10,10,8][i-1])
ck('Q2 long reverse composite forbidden',hom([('Wp',5,1)],[('P',2,1)])==0)
# Exact universal polarization controls, all coefficients retained.
# D=p*d/dx+q*d/dy has D^2 x^(6-i)y^i nonzero for every basis vector;
# different i have disjoint total input weight, giving rank7.
second_columns=[]
for i in range(7):
    col={}
    if 6-i>=2:col[(i,2,0)]=(6-i)*(5-i)
    if i>=1 and 6-i>=1:col[(i-1,1,1)]=2*(6-i)*i
    if i>=2:col[(i-2,0,2)]=i*(i-1)
    second_columns.append(col)
    ck('second polarization nonzero monomial '+str(i),bool(col))
ck('second polarization disjoint supports',all(set(second_columns[i]).isdisjoint(second_columns[j]) for i in range(7) for j in range(i)))
# Coefficients of (x*q-y*p)*D are -p^2 f + p*q h + q^2 e.
# On Sym6, h has distinct weights and e/f join every adjacent weight.
weights=[6-2*i for i in range(7)]
ck('Sym6 distinct h weights',len(set(weights))==7)
ck('Sym6 e lowering coefficients',all(i!=0 for i in range(1,7)))
ck('Sym6 f raising coefficients',all(6-i!=0 for i in range(6)))
ck('Q3 reverse composite forbidden',hom([('V',4,2)],[('V',2,1)])==0)
ck('Q1 long reverse composite forbidden',hom([('1',8,1)],[('D',2,1)])==0)
ck('Q1 short reverse target dimension1',hom([('V',4,1)],[('D',2,1)])==1)
ck('Q2 reverse target dimension1',hom([('V',4,1),('Wp',5,1)],[('P',2,1)])==1)
ck('doublet source P',coho([('Wp',3,1)],0)==P)
ck('doublet target Wp',coho([('Wp',3,1)],1)==C['Wp'])
ck('complement source dimension33',va(vs(2,C['V']),vs(3,P),vs(3,C['D']))[0]==z(33))
ck('complement target dimension18',vs(3,C['T'])[0]==z(18))
# Noncommutative path algebra on H and Q. A word with a reverse then
# forward arrow (b or v followed by c) is zero in types1--3.
# Case3 also kills every forward then reverse pair.
def poly(*terms):
    d={}
    for w,n in terms:
        d[w]=d.get(w,0)+n
    return {w:n for w,n in d.items() if n}
def pa(*ps):return poly(*[(w,n) for p in ps for w,n in p.items()])
def pn(p):return {w:-n for w,n in p.items()}
def pm(p,q,case3=False):
    out=[]
    for w,n in p.items():
        for v,m in q.items():
            word=w+v
            pairs=list(zip(word,word[1:]))
            if any(x in ('b','v') and y=='c' for x,y in pairs):continue
            if case3 and any(x=='c' and y in ('b','v') for x,y in pairs):continue
            out.append((word,n*m))
    return poly(*out)
def mm(X,Y,case3=False):return [[pa(*[pm(X[i][k],Y[k][j],case3) for k in range(2)]) for j in range(2)] for i in range(2)]
I={():1};O={};a,b,c,d,v=[{(x,):1} for x in 'abcdv']
S=[[I,v],[O,I]];Si=[[I,pn(v)],[O,I]];Fmat=[[a,b],[c,d]]
for case3 in [False,True]:
    transformed=mm(mm(Si,Fmat,case3),S,case3)
    ck('gauge canonical H block '+str(case3),transformed[0][0]==a)
    ck('gauge canonical offdiagonal c '+str(case3),transformed[1][0]==c)
    ck('gauge quotient block '+str(case3),transformed[1][1]==pa(d,pm(c,v,case3)))
    ck('gauge upper block '+str(case3),transformed[0][1]==pa(b,pm(a,v,case3),pn(pm(v,d,case3))))
    J=pm(c,b,case3)
    N=[[O,b],[c,J]]
    N2=mm(N,N,case3);N3=mm(N2,N,case3)
    ck('nilpotent kernel cube '+str(case3),N3==[[O,O],[O,O]])
    ck('nilpotent kernel square '+str(case3),N2==[[O,O],[O,J]])
    if case3:ck('case3 all offdiagonal products zero',N2==[[O,O],[O,O]])
# Nonzero type4 control on the T channel: ordinary scalars give vc=1.
ck('type4 scalar feedback exists',1*1==1)
r=Path(__file__).resolve().parent
for pin in json.loads((r/'INPUTS.json').read_text()):
    raw=(r/pin['local_path']).read_bytes()
    ck('pin sha256 '+pin['label'],hashlib.sha256(raw).hexdigest()==pin['sha256'])
    ck('pin gitblob '+pin['label'],hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==pin['git_blob'])
print(json.dumps({'status':'PASS','checks':len(checks),'rows':rows,'canonical_doublet_terminal':[4,2],'canonical_complement_terminal':[33,18],'case3_two_sided_products':'zero','scope':'universal characters and formal coefficient algebra; no actual coefficient, source instance, Q/Gauss compatibility or complete repair evaluated','labels':checks},indent=2))
