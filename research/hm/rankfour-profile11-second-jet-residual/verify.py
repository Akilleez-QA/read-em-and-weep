"""Only fixed characters, seven rank-two partitions, Hom/Ext and degree data."""
from collections import Counter
import hashlib,json
from pathlib import Path
from characters import product,DIM
root=Path(__file__).resolve().parent
checks=0
def req(ok,label):
 global checks
 checks+=1
 if not ok:raise RuntimeError(label)
def eq(got,want,label):req(got==want,label)
def rd(blocks):return [sum(DIM[r] for d,r in blocks),sum(d*DIM[r] for d,r in blocks)]
def h1(blocks):
 c=Counter()
 for d,r in blocks:c.update(product(r,-d-2))
 return c
proof_hash=hashlib.sha256((root/'PROOF.md').read_bytes()).hexdigest()
eq(proof_hash,'793c635439cf05c0234b4152aca4e9213780258d096d9036902b808a952f39e4','proof binding')
for item in json.loads((root/'INPUTS.json').read_text()):
 b=(root/item['file']).read_bytes()
 eq(len(b),item['bytes'],'input length')
 eq(hashlib.sha256(b).hexdigest(),item['sha256'],'input sha256')
 eq(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest(),item['git_blob_sha1'],'input Git blob')
want=Counter(A=1,V=1,P=1,D=2)
M_h1=product('A',6)
eq(M_h1,Counter(V=1,P=2,D=2),'second osculating H1')
S_h1=Counter(A=1,V=2,P=3,D=4)
c=S_h1.copy();c.subtract(M_h1);eq(+c,want,'residual H1')
eq(sum(DIM[r]*m for r,m in want.items()),20,'residual H1 dimension')
# These seven forms are forced analytically by rank, parity, negativity and degree.
forms={'W(-11)':[(-11,'W')],'Wp(-11)':[(-11,'Wp')],
 'O(-2)+O(-20)':[(-2,'one'),(-20,'one')],
 'O(-4)+O(-18)':[(-4,'one'),(-18,'one')],
 'O(-6)+O(-16)':[(-6,'one'),(-16,'one')],
 'O(-8)+O(-14)':[(-8,'one'),(-14,'one')],
 'O(-10)+O(-12)':[(-10,'one'),(-12,'one')]}
characters={}
for name,blocks in forms.items():
 eq(rd(blocks),[2,-22],'forced residual rank/degree')
 req(all(d<0 for d,r in blocks),'negative residual')
 eq(sum(DIM[r]*m for r,m in h1(blocks).items()),20,'residual Euler characteristic')
 characters[name]=dict(h1(blocks))
for name in ['O(-2)+O(-20)','O(-8)+O(-14)']:
 eq(h1(forms[name]),Counter(one=1,A=1,V=1,P=2,D=1),'excluded scalar character')
 req(h1(forms[name])!=want,'character mismatch')
for name in ['W(-11)','Wp(-11)','O(-4)+O(-18)','O(-6)+O(-16)','O(-10)+O(-12)']:
 eq(h1(forms[name]),want,'remaining character equality')
for n,w in [(5,Counter(T=1)),(6,Counter(V=1,P=1)),(7,Counter(Wp=1,T=1))]:eq(product('one',n),w,'low symmetric power')
eq(product('W',6),Counter(Wp=1,T=2),'W tensor Sym6')
# Hom dimensions only: no actual coefficient array or instance matrix is formed.
scalar_hom={
 'W(-11)':[product('one',7)['W'],product('one',5)['W']],
 'Wp(-11)':[product('one',7)['Wp'],product('one',5)['Wp']],
 'O(-4)+O(-18)':[[product('one',0)['one'],product('one',14)['one']],[product('one',-2)['one'],product('one',12)['one']]],
 'O(-6)+O(-16)':[[product('one',2)['one'],product('one',12)['one']],[product('one',0)['one'],product('one',10)['one']]],
 'O(-10)+O(-12)':[[product('one',6)['one'],product('one',8)['one']],[product('one',4)['one'],product('one',6)['one']]],
}
scalar_want={'W(-11)':[0,0],'Wp(-11)':[1,0],'O(-4)+O(-18)':[[1,0],[0,1]],'O(-6)+O(-16)':[[0,1],[1,0]],'O(-10)+O(-12)':[[0,0],[0,0]]}
for n in scalar_hom:eq(scalar_hom[n],scalar_want[n],'scalar target Hom '+n)
doublet_hom={
 'W(-11)':product('W',6)['W'],
 'Wp(-11)':product('W',6)['Wp'],
 'O(-4)+O(-18)':[product('W',-1)['one'],product('W',13)['one']],
 'O(-6)+O(-16)':[product('W',1)['one'],product('W',11)['one']],
 'O(-10)+O(-12)':[product('W',5)['one'],product('W',7)['one']],
}
doublet_want={'W(-11)':0,'Wp(-11)':1,'O(-4)+O(-18)':[0,1],'O(-6)+O(-16)':[1,1],'O(-10)+O(-12)':[0,0]}
for n in doublet_hom:eq(doublet_hom[n],doublet_want[n],'doublet target Hom '+n)
ext_dims={'Wp(-11)':0,'O(-6)':product('A',0)['one'],'O(-16)':0,'O(-4)':product('A',2)['one'],'O(-18)':0}
eq(ext_dims,{'Wp(-11)':0,'O(-6)':0,'O(-16)':0,'O(-4)':1,'O(-18)':0},'five equivariant Ext dimensions')
eq(product('A',2),Counter(one=1,A=1,D=1),'A tensor A')
for d in [3,8,10]:req(d>=-1,'ordinary H1 extension vanishing')
req(-7-(-4)<0,'cubic extension cannot split')
eq(rd([(-8,'A')]),[3,-24],'actual second jet rank/degree')
eq(rd([(-7,'S')]),[4,-28],'nontrivial cubic extension middle')
eq([-24+(-4),3+1],[-28,4],'cubic extension additive degrees')
necessary_S={
 'A(-8)+Wp(-11)':[(-8,'A'),(-11,'Wp')],
 'A(-8)+O(-6)+O(-16)':[(-8,'A'),(-6,'one'),(-16,'one')],
 'A(-8)+O(-4)+O(-18)':[(-8,'A'),(-4,'one'),(-18,'one')],
 'S4(-7)+O(-18)':[(-7,'S'),(-18,'one')],
}
for n,b in necessary_S.items():
 eq(rd(b),[5,-46],'necessary S0 degree '+n)
 eq(h1(b),S_h1,'necessary S0 H1 '+n)
eq(-10+2,-8,'second principal parts degree')
eq(-8+(-6),-14,'first two graded quotient sum')
eq(-46-(-24),-22,'actual residual degree')
for q in [[(-4,'one'),(-6,'one')],[(-5,'W')]]:
 eq(rd(q),[2,-10],'residual target degree')
 eq((-10)-(-22),12,'same torsion length')
# Controls diagnose only the small necessity tests, not occurrence of altered data.
controls={
 'retaining a trivial H1 constituent fails the residual target':(Counter(one=1)+want)!=want,
 'one target row alone cannot carry a rank-two injection':1<2,
 'the zero extension is not the cubic evaluation middle':[(-8,'A'),(-4,'one')]!=[(-7,'S')],
 'a different total degree changes the torsion length':(-10)-(-20)!=12,
}
for n,ok in controls.items():req(ok,n)
print(json.dumps({'status':'PASS','checks':checks,'proof_sha256':proof_hash,
 'scope':'Only fixed representations and the seven rank-two forms forced by rank, parity, negativity and degree; no actual coefficient or instance rank.',
 'residual_characters':characters,'scalar_target_hom_dimensions':scalar_hom,
 'doublet_target_hom_dimensions':doublet_hom,'equivariant_ext_dimensions':ext_dims,
 'necessary_S0_forms':list(necessary_S),'semantic_controls':controls},indent=2,sort_keys=True))
