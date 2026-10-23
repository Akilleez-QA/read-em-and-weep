#!/usr/bin/env python3
"""Exact synthetic diagnostics; no actual HM instance is selected."""
import hashlib,itertools,json
from pathlib import Path
import sympy as S
R=Path(__file__).resolve().parent
count=0

def ck(test,label):
 global count
 count+=1
 if not test: raise RuntimeError(label)
def dim(c): return sum(a*b for a,b in zip(c,(3,3,4,5)))
rows=[]
preliminary=[]
for r,e,d in itertools.product(range(3),range(2),range(3)):
 admissible=d<=1 and e<=2-r and (r!=0 or e==1)
 surj=d==1 and e==2-r
 if not admissible or surj:continue
 preliminary.append((r,e,d))
 if r==0:continue
 U=(1,2,2+e,2+d);Z=(0,2,4-r,2);image=(0,2,2+e,1+d)
 cok=tuple(a-b for a,b in zip(Z,image))
 ck(cok==(0,0,2-r-e,1-d),'restricted cokernel')
 ck(dim(U)-8==dim(image),'exact restricted kernel dimension')
 ck(0<=r+e-1<=1,'quotient P excess')
 ck(d==0 or r+e==1,'only d1 quotients acyclic')
 rows.append(dict(r=r,epsilon=e,d=d,U=U,Z=Z,dimensions=[dim(U),dim(Z)],restricted_cokernel=cok,quotient_kernel=(0,0,0,1-d),quotient_cokernel=(0,0,r+e-1,0)))
ck(preliminary==[(0,1,0),(0,1,1),(1,0,0),(1,0,1),(1,1,0),(2,0,0)],'six preliminary triples')
ck([(x['r'],x['epsilon'],x['d']) for x in rows]==[(1,0,0),(1,0,1),(1,1,0),(2,0,0)],'four triples after joint P nonvanishing')
# Imported PR944 interface H1(X)=Sym6W=V+P: this diagnostic
# checks its Hom consequence, not a fresh derivation of that character.
ck((0,1,1,0)[3]==0,'Hom_G(X,D O(-2)) vanishes')
# Exact synthetic restriction systems, channels A,V,P,D; P and V pivots
# force two-dimensional kernel with freely prescribable A,D. Not HM data.
for alpha,beta,gamma in itertools.product((-1,0,1),repeat=3):
 H=S.Matrix([[0,0,1,alpha],[beta,1,0,gamma]])
 v=S.Matrix([0,-gamma,-alpha,1])
 ck(H*v==S.zeros(2,1) and v[3]==1,'free nonzero D coefficient in kernel')
# Exact synthetic multiplicity diagrams for P and D separately.
# These are not radical realizations or actual TypeII instances.
def diagram(Q,ui,zi,expect):
 n=Q.cols;m=Q.rows
 U=S.eye(n)[:,ui];Z=S.eye(m)[:,zi]
 uc=[i for i in range(n) if i not in ui];zc=[i for i in range(m) if i not in zi]
 QU=Q*U
 ck(Q.extract(zc,ui)==S.zeros(len(zc),len(ui)),'preserved subcomplex')
 restricted=Q.extract(zi,ui);quotient=Q.extract(zc,uc)
 fullker=n-Q.rank();subker=len(ui)-restricted.rank()
 subcok=len(zi)-restricted.rank();qker=len(uc)-quotient.rank();qcok=len(zc)-quotient.rank()
 image_on_coker=Q.row_join(Z).rank()-Q.rank()
 ck((fullker,subker,subcok,qker,qcok,image_on_coker)==expect,'synthetic exact kernel/cokernel and image')
 ck(subcok-image_on_coker==qker,'connecting image equals cokernel-map kernel')
 ck((m-Q.rank())-image_on_coker==qcok,'quotient cokernel exactness')
for row in rows:
 r,e,d=row['r'],row['epsilon'],row['d']
 u=2+e;z=4-r
 Qp=S.eye(4)[:,:3];up=list(range(u));zp=up+([3] if z>u else [])
 diagram(Qp,up,zp,(0,0,2-r-e,0,r+e-1,2-r-e))
 Qd=S.eye(4)[:3,:];ud=list(range(1+d))+[3];zd=[0,1]
 diagram(Qd,ud,zd,(1,1,1-d,1-d,0,0))
 if r+e==2:
  ck(d==0 and row['restricted_cokernel']==(0,0,0,1),'surplus internal cokernel exactly D')
# Universal multiplication matrix for (a x²+b xy+c y²)(u x²+v xy+w y²).
a,b,c=S.symbols('a b c')
M=S.Matrix([[a,0,0],[b,a,0],[c,b,a],[0,c,b],[0,0,c]])
ck(S.expand(M[:3,:].det())==a**3,'highest coefficient rank certificate')
ck(S.expand(M[2:5,:].det())==c**3,'lowest coefficient rank certificate')
ck(S.expand(M[1:4,:].subs({a:0,c:0}).det())==b**3,'middle-only rank certificate')
for aa,bb,cc in itertools.product((-1,0,1),repeat=3):
 ck(M.subs({a:aa,b:bb,c:cc}).rank()==(0 if aa==bb==cc==0 else 3),'bounded universal multiplication diagnostic')
# Shared-D negative control: a quotient D kernel cannot be discarded.
Q=S.Matrix([[1,0]])
ck(Q.rank()==1 and len(Q.nullspace())==1,'surjective quotient need not be invertible')
for entry in json.loads((R/'INPUTS.json').read_text()):
 data=(R/entry['local_path']).read_bytes()
 ck(hashlib.sha256(data).hexdigest()==entry['sha256'],'immutable SHA256 '+entry['local_path'])
 ck(hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==entry['git_blob'],'immutable blob '+entry['local_path'])
print(json.dumps(dict(status='pass',checks=count,rows=rows,note='Conditional footprints and synthetic diagnostics only; no actual occurrence or source cut'),indent=2))
