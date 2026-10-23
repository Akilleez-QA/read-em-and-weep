#!/usr/bin/env python3
"""Universal type III matrices; integer Laurent polynomials, no sampled points."""
import hashlib,json,itertools
from pathlib import Path
ROOT=Path(__file__).resolve().parent
checks=[]
def check(label,condition):
    if not condition: raise RuntimeError(label)
    checks.append(label)
def p(c=1,i=0,j=0): return {(i,j):c} if c else {}
def add(a,b):
    d=dict(a)
    for e,c in b.items(): d[e]=d.get(e,0)+c
    return {e:c for e,c in d.items() if c}
def mul(a,b):
    d={}
    for (i,j),c in a.items():
        for (k,l),v in b.items(): d[(i+k,j+l)]=d.get((i+k,j+l),0)+c*v
    return {e:c for e,c in d.items() if c}
def neg(a): return {e:-c for e,c in a.items()}
def zero(n,m): return [[{} for _ in range(m)] for _ in range(n)]
def eye(n):
    r=zero(n,n)
    for i in range(n):r[i][i]=p()
    return r
def mm(a,b):
    r=zero(len(a),len(b[0]))
    for i in range(len(a)):
        for k in range(len(b)):
            for j in range(len(b[0])):r[i][j]=add(r[i][j],mul(a[i][k],b[k][j]))
    return r
def ma(a,b): return [[add(x,y) for x,y in zip(r,s)] for r,s in zip(a,b)]
def block(a,b,i,j):
    for k,row in enumerate(b):
        for l,v in enumerate(row):a[i+k][j+l]=v
    return a
def scale(a,s): return [[mul(x,s) for x in row] for row in a]
def det3(a):
    out={}
    for z in itertools.permutations(range(3)):
        inv=sum(z[i]>z[j] for i in range(3) for j in range(i+1,3))
        t=p((-1)**inv)
        for i in range(3):t=mul(t,a[i][z[i]])
        out=add(out,t)
    return out
I=eye(3);x=p(1,1,0);y=p(1,0,1)
a=block(block(zero(6,3),scale(I,x),0,0),scale(I,y),3,0)
b=block(block(zero(3,6),scale(I,neg(y)),0,0),scale(I,x),0,3)
check('Euler b*a coefficientwise',mm(b,a)==zero(3,3))
for rows,mon in [([0,1,2],p(1,3,0)),([3,4,5],p(1,0,3))]:
    check('a minor '+str(rows),det3([a[i] for i in rows])==mon)
for cols,mon in [([0,1,2],p(-1,0,3)),([3,4,5],p(1,3,0))]:
    check('b minor '+str(cols),det3([[row[i] for i in cols] for row in b])==mon)
# K order: B3,C6,D1_3,D2_3. E adds L2 before K.
U=block(zero(15,15),b,0,3)
V1=block(zero(15,15),a,3,9)
V2=block(zero(15,15),a,3,12)
rad=[U,V1,V2]
z=block(block(zero(15,6),I,0,0),a,3,3)
q=block(block(block(zero(9,15),b,0,3),I,3,9),I,6,12)
check('quotient kills S',mm(q,z)==zero(9,6))
for n,rs in [(15,rad),(17,[block(zero(17,17),r,2,2) for r in rad])]:
    for i,r in enumerate(rs):
        for j,s in enumerate(rs):check(f'{n} radical product {i},{j}',mm(r,s)==zero(n,n))
# radical matrices are nonzero linearly independent: distinct support blocks.
for i,r in enumerate(rad):check(f'radical generator {i} nonzero',any(any(row) for row in r))
for i in range(3):
    for j in range(i):check(f'disjoint supports {i},{j}',all(not(rad[i][k][l] and rad[j][k][l]) for k in range(15) for l in range(15)))
for chart in ['x','y']:
    ell=zero(3,6);rho=zero(6,3)
    if chart=='x':block(ell,scale(I,p(1,-1,0)),0,0);block(rho,scale(I,p(1,-1,0)),3,0)
    else:block(ell,scale(I,p(1,0,-1)),0,3);block(rho,scale(I,p(-1,0,-1)),0,0)
    check(chart+' Euler left inverse',mm(ell,a)==I)
    check(chart+' Euler right inverse',mm(b,rho)==I)
    check(chart+' Euler exact homotopy',ma(mm(a,ell),mm(rho,b))==eye(6))
    retract=block(block(zero(6,15),I,0,0),ell,3,3)
    section=block(block(block(zero(15,9),rho,3,0),I,9,3),I,12,6)
    check(chart+' S retraction',mm(retract,z)==eye(6))
    check(chart+' quotient section',mm(q,section)==eye(9))
    check(chart+' full exact homotopy',ma(mm(z,retract),mm(section,q))==eye(15))
    # Stacked common-kernel operator F. Construct q = H F; F = G q.
    F=zero(45,15)
    for i,r in enumerate(rad):block(F,r,15*i,0)
    H=zero(9,45);block(H,I,0,0);block(H,ell,3,18);block(H,ell,6,33)
    G=zero(45,9);block(G,I,0,0);block(G,a,18,3);block(G,a,33,6)
    check(chart+' common kernel q=HF',mm(H,F)==q)
    check(chart+' common kernel F=Gq',mm(G,q)==F)
    # Images: R=[U V1 V2] factors through z, and z through R on each chart.
    R=zero(15,45)
    for i,r in enumerate(rad):block(R,r,0,15*i)
    C=zero(6,45);block(C,b,0,3);block(C,I,3,24);block(C,I,3,42)
    D=zero(45,6);block(D,rho,3,0);block(D,I,24,3)
    check(chart+' image R=zC',mm(z,C)==R)
    check(chart+' image z=RD',mm(R,D)==z)
    # E's annihilator is L plus S, image still S, quotient E/Ann has rank9.
    ZE=block(zero(17,6),z,2,0)
    AE=block(block(zero(17,8),eye(2),0,0),z,2,2)
    QE=block(zero(9,17),q,0,2)
    RE=block(block(zero(8,17),eye(2),0,0),retract,2,2)
    SE=block(zero(17,9),section,2,0)
    check(chart+' E annihilator exactness',ma(mm(AE,RE),mm(SE,QE))==eye(17))
    check(chart+' E annihilator injection',mm(RE,AE)==eye(8))
    FE=zero(51,17);GE=zero(51,9);HE=zero(9,51)
    for i,r in enumerate(rad):block(FE,block(zero(17,17),r,2,2),17*i,0)
    block(GE,I,2,0);block(GE,a,22,3);block(GE,a,39,6)
    block(HE,I,0,2);block(HE,ell,3,22);block(HE,ell,6,39)
    check(chart+' E common kernel QE=HEFE',mm(HE,FE)==QE)
    check(chart+' E common kernel FE=GEQE',mm(GE,QE)==FE)
    Rbig=zero(17,51);Cbig=zero(6,51);Dbig=zero(51,6)
    for i,r in enumerate(rad):block(Rbig,block(zero(17,17),r,2,2),0,17*i)
    block(Cbig,b,0,5);block(Cbig,I,3,28);block(Cbig,I,3,48)
    block(Dbig,rho,5,0);block(Dbig,I,28,3)
    check(chart+' E image R=ZC',mm(ZE,Cbig)==Rbig)
    check(chart+' E image Z=RD',mm(Rbig,Dbig)==ZE)
types={'K':{-2:3,-3:6,-4:6},'S':{-2:3,-4:3},'quotient':{-2:3,-4:6}}
metrics={k:{'rank':sum(t.values()),'degree':sum(d*n for d,n in t.items()),'h0_twist2':sum(n*max(d+3,0) for d,n in t.items())} for k,t in types.items()}
check('rank degree K',metrics['K']=={'rank':15,'degree':-48,'h0_twist2':3})
check('rank degree S',metrics['S']=={'rank':6,'degree':-18,'h0_twist2':3})
check('rank degree quotient',metrics['quotient']=={'rank':9,'degree':-30,'h0_twist2':3})
check('nonsplit h0 certificate',metrics['K']['h0_twist2']!=metrics['S']['h0_twist2']+metrics['quotient']['h0_twist2'])
data=(ROOT/'inputs/PR1127-PROOF.md').read_bytes()
sha=hashlib.sha256(data).hexdigest();blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
check('input sha256',sha=='3101157347802226a3b2638e76375854944d7a41d503b75b1591bc3eb66b1577')
check('input git blob',blob=='80faeb68639dc5f644397a54d5ca7a12009f616f')
# Type IV: K=C1_6 + C2_6 + D_3; E=L2+K.
IV=[block(zero(15,15),a,0,12),block(zero(15,15),a,6,12)]
Z=block(block(zero(15,6),a,0,0),a,6,3)
AN=block(zero(15,12),eye(12),0,0)
QD=block(zero(3,15),I,0,12)
QA=block(block(zero(6,12),b,0,0),b,3,6)
for n,rs in [(15,IV),(17,[block(zero(17,17),r,2,2) for r in IV])]:
    for i,r in enumerate(rs):
        for j,t in enumerate(rs):check(f'IV {n} product {i},{j}',mm(r,t)==zero(n,n))
for chart in ['x','y']:
    ell=zero(3,6);rho=zero(6,3)
    if chart=='x':block(ell,scale(I,p(1,-1,0)),0,0);block(rho,scale(I,p(1,-1,0)),3,0)
    else:block(ell,scale(I,p(1,0,-1)),0,3);block(rho,scale(I,p(-1,0,-1)),0,0)
    R=block(block(zero(15,30),IV[0],0,0),IV[1],0,15)
    C=block(block(zero(6,30),I,0,12),I,3,27)
    D=block(block(zero(30,6),I,12,0),I,27,3)
    check('IV '+chart+' image R=ZC',mm(Z,C)==R)
    check('IV '+chart+' image Z=RD',mm(R,D)==Z)
    F=block(block(zero(30,15),IV[0],0,0),IV[1],15,0)
    H=block(zero(3,30),ell,0,0)
    G=block(block(zero(30,3),a,0,0),a,21,0)
    check('IV '+chart+' kernel QD=HF',mm(H,F)==QD)
    check('IV '+chart+' kernel F=GQD',mm(G,QD)==F)
    ret=block(block(zero(6,12),ell,0,0),ell,3,6)
    sec=block(block(zero(12,6),rho,0,0),rho,6,3)
    Z12=Z[:12]
    check('IV '+chart+' doubled Euler exactness',ma(mm(Z12,ret),mm(sec,QA))==eye(12))
    check('IV '+chart+' doubled Euler left inverse',mm(ret,Z12)==eye(6))
    check('IV '+chart+' doubled Euler right inverse',mm(QA,sec)==eye(6))
    check('IV '+chart+' doubled Euler zero',mm(QA,Z12)==zero(6,6))
    Aret=block(zero(12,15),eye(12),0,0)
    Dsec=block(zero(15,3),I,12,0)
    check('IV '+chart+' annihilator saturated',ma(mm(AN,Aret),mm(Dsec,QD))==eye(15))
    # Saturation of S in all K: quotient consists of QA and the D identity.
    Qall=block(block(zero(9,15),QA,0,0),I,6,12)
    Sret=block(zero(6,15),ret,0,0)
    Qsec=block(block(zero(15,9),sec,0,0),I,12,6)
    check('IV '+chart+' image saturated',ma(mm(Z,Sret),mm(Qsec,Qall))==eye(15))
    # Full 17-dimensional kernel and image certificates.
    F17=block(block(zero(34,17),block(zero(17,17),IV[0],2,2),0,0),block(zero(17,17),IV[1],2,2),17,0)
    Q17=block(zero(3,17),I,0,14)
    H17=block(zero(3,34),ell,0,2)
    G17=block(block(zero(34,3),a,2,0),a,25,0)
    check('IV '+chart+' E kernel Q=HF',mm(H17,F17)==Q17)
    check('IV '+chart+' E kernel F=GQ',mm(G17,Q17)==F17)
    R17=block(block(zero(17,34),block(zero(17,17),IV[0],2,2),0,0),block(zero(17,17),IV[1],2,2),0,17)
    Z17=block(zero(17,6),Z,2,0)
    C17=block(block(zero(6,34),I,0,14),I,3,31)
    D17=block(block(zero(34,6),I,14,0),I,31,3)
    check('IV '+chart+' E image R=ZC',mm(Z17,C17)==R17)
    check('IV '+chart+' E image Z=RD',mm(R17,D17)==Z17)
iv_types={'S':{-4:6},'Ann':{-3:12},'Ann/S':{-2:6},'K/Ann':{-4:3}}
iv_metrics={k:{'rank':sum(t.values()),'degree':sum(d*n for d,n in t.items()),'h0_twist2':sum(n*max(d+3,0) for d,n in t.items())} for k,t in iv_types.items()}
check('IV nonsplit doubled Euler h0',iv_metrics['Ann']['h0_twist2']==0 and iv_metrics['S']['h0_twist2']+iv_metrics['Ann/S']['h0_twist2']==6)
check('IV rank degree S',iv_metrics['S']['rank']==6 and iv_metrics['S']['degree']==-24)
check('IV rank degree Ann',iv_metrics['Ann']['rank']==12 and iv_metrics['Ann']['degree']==-36)
check('IV rank degree Ann/S',iv_metrics['Ann/S']['rank']==6 and iv_metrics['Ann/S']['degree']==-12)
check('IV rank degree K/Ann',iv_metrics['K/Ann']['rank']==3 and iv_metrics['K/Ann']['degree']==-12)
print(json.dumps({'status':'PASS','checks':len(checks),'labels':checks,'type_IV_metrics':iv_metrics,'input_sha256':sha,'input_git_blob':blob,'scope':'Conditional types III and IV universal matrices, with IV image/annihilator filtration; no actual type selection.'},indent=2,sort_keys=True))
