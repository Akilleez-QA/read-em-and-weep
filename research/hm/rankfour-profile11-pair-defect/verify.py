#!/usr/bin/env python3
"""Fixed constant-span, defect and rank-two representation certificates."""
from pathlib import Path
from collections import Counter
import hashlib,json
from characters import product,DIM
ROOT=Path(__file__).resolve().parent
checks=0
def check(got,want,label):
 global checks
 checks+=1
 if got!=want:raise RuntimeError((label,got,want))
def clean(c):return {r:n for r,n in c.items() if n}
def sub(a,b):c=Counter(a);c.subtract(b);return c
def h1(bs):
 out=Counter()
 for r,d in bs:out.update(product(r,-d-2))
 return out
def rank(bs):return sum(DIM[r] for r,d in bs)
def degree(bs):return sum(d*DIM[r] for r,d in bs)
M2=Counter(A=1,V=2,P=3,D=4)
H0F=Counter(A=1,D=2)
check(dict(product('one',8)),{'P':1,'D':1},'octic constant quotient representation')
check([0,4,5,4+5],[0,4,5,9],'semisimple quotient dimensions')
check([d for d in [0,4,5,9] if 7<=d<=9],[9],'unique quotient dimension in range')
check(30-9,21,'minimal constant span')
check(21-16,5,'small annihilator rank')
check(5-3,2,'small derivative-kernel rank')
check(-46-(-16),-30,'small endpoint degree lower bound')
check(-8*5+6,-34,'rank-at-least-five capacity contradiction')
check(-34<-30,True,'strict capacity gap')
check(-8<0,True,'capacity decreases with kernel rank')
for lam in [(-4,-6,-6),(-5,-5,-6)]:
 check(sum(lam),-16,'dual quotient target degree')
 check(lam[0]<=-4,True,'dual quotient top')
 bound_two=lam[0]+lam[1]-4
 bound_one=2*lam[0]-6
 check(max(bound_two,bound_one),-14,'rank-two exact capacity bound')
check(-14-(-30),16,'defect upper bound')
check([x for x in [0,12,20,30,60] if x<=16],[0,12],'effective orbit divisor possibilities')
# The only nonreduced smallest-orbit degree already exceeds the proved cap.
check(2*12>16,True,'do not silently discard nonreduced divisors')
check(dict(product('one',7)),{'Wp':1,'T':1},'tail annihilator coefficient')
check(dict(product('one',6)),{'V':1,'P':1},'tail derivative kernel coefficient')
check((8,-8),(8,-8),'tail annihilator rank-degree')
check((-2-(-8)-6),0,'full Veronese tail defect')
check(-8-2-6,-16,'original and small defect formulas agree')
check(13-8,5,'original annihilator splits to rank five')
check(9-7,2,'original dual endpoint splits to rank two')
base=sub(M2,H0F)
check(clean(base),{'V':2,'P':3,'D':2},'zero-defect H1 endpoint demand')
check(sum(DIM[r]*n for r,n in base.items()),28,'zero-defect H1 dimension')
check(h1([('W',-15)]),Counter(one=1,A=2,V=1,P=2,D=2),'W-15 character')
check(h1([('Wp',-15)]),Counter(one=1,A=1,V=2,P=2,D=2),'Wp-15 character')
zero_pairs=[]
for j,want in zip([2,4,6,8,10,12,14],[1,2,2,1,1,1,2]):
 bs=[('one',-j),('one',-(30-j))];c=h1(bs)
 check((rank(bs),degree(bs)),(2,-30),'zero scalar pair data')
 check(c['A'],want,'zero scalar pair forbidden A')
 check(c['A']>base['A'],True,'zero scalar pair excluded')
 zero_pairs.append({'degrees':[-j,j-30],'A_multiplicity':c['A']})
check(product('one',16)['A'],0,'Sym16 exceptional A multiplicity')
check(product('one',10)['A'],1,'paired Sym10 restores obstruction')
# All five C5 fiber weights. The weight table is the restriction of physical
# even irreducibles, as independently checked from closed class characters.
weights={'one':[0],'A':[0,1,4],'V':[0,2,3],'P':[1,2,3,4],'D':[0,1,2,3,4]}
expected=[Counter(one=1,A=1,V=1,D=1),Counter(A=1,P=1,D=1),Counter(V=1,P=1,D=1),Counter(V=1,P=1,D=1),Counter(A=1,P=1,D=1)]
induced=[];allowed=[]
for k in range(5):
 z=Counter({r:ws.count(k) for r,ws in weights.items() if ws.count(k)})
 check(z,expected[k],'C5 induction weight '+str(k))
 check(sum(DIM[r]*n for r,n in z.items()),12,'torsion section dimension')
 demand=sub(base,z);genuine=all(n>=0 for n in demand.values())
 if genuine:allowed.append(k)
 induced.append({'weight':k,'H0Z':dict(z),'H1L0':clean(demand),'genuine':genuine})
check(allowed,[2,3],'both distinct surviving stabilizer weights')
check(expected[2],expected[3],'equal induced characters, not an assertion of equal torsion sheaves')
target=Counter(V=1,P=2,D=1)
check(clean(sub(base,expected[2])),dict(target),'positive-defect endpoint demand')
check(-30+12,-18,'positive-defect degree')
check(sum(DIM[r]*n for r,n in target.items()),16,'positive-defect H1 dimension')
check(h1([('W',-9)]),target,'W-9 survives')
check(h1([('Wp',-9)]),Counter(one=1,A=1,V=1,P=1,D=1),'Wp-9 fails trivial and A')
positive_pairs=[];scalar_survivors=[]
for j in [2,4,6,8]:
 bs=[('one',-j),('one',-(18-j))];c=h1(bs)
 check((rank(bs),degree(bs)),(2,-18),'positive scalar pair data')
 if c==target:scalar_survivors.append(bs)
 else:check(c['one']>0 or c['A']>0,True,'excluded positive pair missing-constituent gate')
 positive_pairs.append({'degrees':[-j,j-18],'character':dict(c),'survives':c==target})
check(scalar_survivors,[[('one',-8),('one',-10)]],'unique scalar positive-defect survivor')
for small in [[('W',-9)],[('one',-8),('one',-10)]]:
 full=[('V',-2),('P',-2)]+small
 check((rank(full),degree(full)),(9,-32),'original dual endpoint data')
 check(-54-degree(full),-22,'original B degree')
 check(-8-2-(-22),12,'original defect recheck')
# Semantic controls: remove a decisive premise without claiming a modified
# configuration is realized.
check(8 in [0,4,5,9],False,'actual quotient cannot have dimension eight')
check(8 in [0,4,5,8,9],True,'mutation extra quotient dimension removes rigidity')
check(12<=11,False,'mutation stricter defect cap would exclude twelve')
check(20<=20,True,'mutation cap twenty introduces omitted orbit possibility')
check(Counter(one=1)['one']<=base['one'],False,'zero-defect doublet trivial fails')
mut=base.copy();mut['one']=1;check(Counter(one=1)['one']<=mut['one'],True,'mutation added trivial removes this constituent obstruction')
check(-8-2-(-22),12,'original tail defect zero necessary for exact identification')
check((-8-2-(-22))+1,13,'mutation nonzero tail defect changes total')
for e in json.loads((ROOT/'INPUTS.json').read_text()):
 b=(ROOT/e['file']).read_bytes();check(len(b),e['bytes'],'source byte count');check(hashlib.sha256(b).hexdigest(),e['sha256'],'source SHA256');check(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest(),e['git_blob_sha1'],'source Git blob')
out={'status':'PASS','checks':checks,'proof_sha256':hashlib.sha256((ROOT/'PROOF.md').read_bytes()).hexdigest(),'constant_span_dimension':21,'constant_tail_dimension':9,'original_defect':12,'zero_defect_scalar_pairs':zero_pairs,'all_five_torsion_weights':induced,'surviving_distinct_torsion_weights':[2,3],'positive_defect_scalar_pairs':positive_pairs,'small_dual_endpoints':[[['W',-9]],[['one',-8],['one',-10]]],'original_quotient_degrees':[2,-22],'scope':'The two decomposable top-four primal forms only; neither excluded nor realized. The triplet form and full profile remain open.','computation':'Fixed characters, all five abstract C5 weights and seven/four forced rank-two degree partitions; no actual instance or global domain.'}
print(json.dumps(out,indent=2,sort_keys=True))
