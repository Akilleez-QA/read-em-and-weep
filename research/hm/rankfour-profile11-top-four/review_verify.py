#!/usr/bin/env python3
"""Independent closed-class-character review; fixed symbolic facts only.
No McKay recurrence, bundle-domain generator, actual map, or height search.
All checks survive python -O: no assert statements are used.
"""
from fractions import Fraction as F
from math import comb, floor
from pathlib import Path
import hashlib, json
ROOT=Path(__file__).resolve().parent
checks=0

def require(test,label):
    global checks
    checks+=1
    if not test: raise RuntimeError(label)

def q(a,b=0): return F(a),F(b)
def add(x,y): return x[0]+y[0],x[1]+y[1]
def scale(a,x): return a*x[0],a*x[1]
def mul(x,y): return x[0]*y[0]+5*x[1]*y[1],x[0]*y[1]+x[1]*y[0]
def power(x,n):
    r=q(1)
    for _ in range(n): r=mul(r,x)
    return r
def total(xs):
    z=q(0)
    for x in xs: z=add(z,x)
    return z
# Chebyshev closed polynomial, not the author's graph/representation recurrence.
def sym_at(n,x):
    if n<0:return q(0)
    return total(scale((-1)**k*comb(n-k,k),power(x,n-2*k)) for k in range(n//2+1))
tr=[q(2),q(-2),q(F(1,2),F(1,2)),q(F(-1,2),F(-1,2)),q(F(1,2),F(-1,2)),q(F(-1,2),F(1,2)),q(1),q(-1),q(0)]
sizes=[1,1,12,12,12,12,20,20,30]
def sym(n):return tuple(sym_at(n,x) for x in tr)
def plus(*cs):return tuple(total(xs) for xs in zip(*cs))
def times(c,d):return tuple(mul(x,y) for x,y in zip(c,d))
def scaled(k,c):return tuple(scale(k,x) for x in c)
char={"1":sym(0),"W":sym(1),"A":sym(2),"S":sym(3),"D":sym(4),"T":sym(5),"P":tuple(q(x) for x in [4,4,-1,-1,-1,-1,1,1,0])}
char["V"]=plus(sym(6),scaled(-1,char["P"]))
char["Wp"]=plus(times(char["W"],char["P"]),scaled(-1,char["T"]))
names=["1","W","Wp","A","V","P","S","D","T"]
dim={r:int(char[r][0][0]) for r in names}
def inner(c,d): return scale(F(1,120),total(scale(s,mul(x,y)) for s,x,y in zip(sizes,c,d)))
def decomposition(c):
    out={}
    for r in names:
        v=inner(char[r],c)
        require(v[1]==0 and v[0].denominator==1,"integral multiplicity "+r)
        if v[0]:out[r]=int(v[0])
    return out
def rep(**d):return plus(*(scaled(m,char[r]) for r,m in d.items())) if d else sym(-1)
def product(r,n):return times(char[r],sym(n))
def mult(r,c):return decomposition(c).get(r,0)
def contained(c,d):return all(v>=0 for v in decomposition(plus(d,scaled(-1,c))).values())
def sections(blocks,t):return plus(*(product(r,e+t) for r,e in blocks))
def hom(r,d,u,e):return mult(r,product(u,e-d))
for r in names:
    for s in names:require(inner(char[r],char[s])==q(int(r==s)),"class orthogonality")
require(sum(dim[r]**2 for r in names)==120,"sum squared dimensions")
require(dim==dict(zip(names,[1,2,2,3,3,4,4,5,6])),"physical dimensions")
require(times(char["Wp"],char["Wp"])==rep(**{"1":1,"V":1}),"physical V=Sym2 Wp")
identities=[("A",4,{"A":1,"V":1,"P":1,"D":1}),("A",5,{"Wp":1,"S":1,"T":2}),("V",4,{"A":1,"V":1,"P":1,"D":1}),("V",5,{"W":1,"S":1,"T":2}),("W",1,{"1":1,"A":1}),("Wp",1,{"P":1}),("Wp",2,{"T":1}),("W",3,{"A":1,"D":1}),("Wp",3,{"V":1,"D":1}),("W",4,{"S":1,"T":1}),("Wp",4,{"S":1,"T":1}),("W",6,{"Wp":1,"T":2}),("Wp",6,{"W":1,"Wp":1,"S":1,"T":1}),("1",7,{"Wp":1,"T":1}),("1",8,{"P":1,"D":1}),("Wp",5,{"A":1,"P":1,"D":1}),("A",1,{"W":1,"S":1}),("V",1,{"T":1})]
for r,n,expect in identities:require(product(r,n)==rep(**expect),f"product {r} Sym{n}")
sources={"D":[("D",-2),("Wp",-3),("T",-3),("V",-4),("1",-8)],"P":[("P",-2),("Wp",-3),("T",-3),("V",-4),("Wp",-5)],"V":[("V",-2),("Wp",-3),("T",-3),("V",-4),("V",-4)],"Z":[("Wp",-3),("T",-3),("T",-3),("V",-4)]}
for s,rows in sources.items():
    require(sum(dim[r] for r,d in rows)==17,"source rank")
    require(sum(dim[r]*d for r,d in rows)==-54,"source degree")
negative_hom={}
for u,e in [("1",e) for e in [-8,-6,-4,-2]]+[(r,e) for r in ["W","Wp"] for e in [-7,-5,-3,-1]]:
    rows={s:[[r,d,hom(r,d,u,e)] for r,d in bs if hom(r,d,u,e)] for s,bs in sources.items()}
    negative_hom[f"{u}({e})"]=rows
    if (u,e) in [("1",-6),("1",-4),("1",-2),("W",-5),("W",-3),("Wp",-7)]:require(not any(rows.values()),"negative Hom vanishing")
    if (u,e)==("1",-8):require(rows=={"D":[["1",-8,1]],"P":[],"V":[],"Z":[]},"unique negative scalar")
    if (u,e)==("W",-7):require(rows=={"D":[["1",-8,1]],"P":[],"V":[],"Z":[]},"rank-one cannot surject doublet")
    if (u,e)==("Wp",-5):require(rows=={"D":[],"P":[["Wp",-5,1]],"V":[],"Z":[]},"source P tail")
    if (u,e)==("Wp",-3):require(all(v==[["Wp",-3,1]] for v in rows.values()),"unique source cubic doublet")
    if (u,e)==("Wp",-1):require(all(rows.values()),"minus-one doublet source Hom")
M2=rep(A=1,V=2,P=3,D=4);M3=rep(Wp=3,S=3,T=6);cubic=rep(Wp=1,T=2)
require(not contained(sections([("1",0)],0),M2),"exclude scalar zero")
require(mult("A",M2)==1 and sections([("1",2)],0)==char["A"],"at most one degree-two scalar")
require(not contained(sections([("W",1)],0),M2),"exclude W(1)")
require(not contained(sections([("W",-1)],1),M3),"exclude W(-1)")
require(not contained(sections([("V",4)],1),M3),"exclude V(4)")
# Literal symbolic output of the rank partition proof, NOT a bundle search.
shapes=[
("T",[("A",4),("1",-8)],(5,4,4),-18),
("C1",[("1",4),("V",-2)],(6,4,3),-64),
("C2",[("1",-8),("1",2),("1",4),("1",4)],(5,4,4),-26),
("C3",[("1",-8),("1",4),("1",4),("1",4)],(5,4,4),-18),
("C4",[("1",-8),("1",4),("Wp",-1)],(6,4,3),-57),
("C5",[("1",-8),("1",4),("Wp",1)],(5,4,4),-42),
("C6",[("1",-8),("1",4),("W",3)],(5,4,4),-26),
("C7",[("1",-8),("1",4),("Wp",3)],(5,4,4),-26),
("C8",[("1",4),("1",2),("Wp",-1)],(5,5,3),-45),
("C9",[("1",4),("1",4),("Wp",-1)],(5,5,3),-35),
("C10",[("1",4),("1",2),("Wp",-3)],(6,5,2),-50),
("C11",[("1",4),("1",4),("Wp",-3)],(6,5,2),-40),
("C12",[("1",4),("1",2),("Wp",-5)],(6,5,2),-54),
("C13",[("1",4),("1",4),("Wp",-5)],(6,6,1),-43)]
results=[]
for tag,bs,hs,cap in shapes:
    degrees=sorted([e for r,e in bs for _ in range(dim[r])],reverse=True)
    require(len(degrees)==4 and degrees[0]==4 and degrees[-1]<0,"shape rank and signs")
    require(contained(sections(bs,0),M2) and contained(sections(bs,1),M3) and contained(cubic,sections(bs,3)),"all initial coefficient gates")
    ls=degrees[:3];L=sum(ls)
    C=-F(208,3)+F(13*L,3)+F(3*sum(x*x for x in ls)-L*L,12)
    cs=[F(x,2)+F(26-L,6) for x in ls]
    value=sum(h*l-h*(h+1) for h,l in zip(hs,ls))
    require(sum(hs)==13 and hs[0]>=hs[1]>=hs[2]>=0,"legal capacity certificate")
    require(value==C-sum((h-c)**2 for h,c in zip(hs,cs)),"exact square-completion identity")
    require(value==cap==floor(C),"matching integer upper bound and witness")
    # Coefficients in the quadratic identity on the sum-height plane: center sum,
    # gradient modulo a common Lagrange multiplier, constant term.
    require(sum(cs)==13,"center on plane")
    require(len(set(2*c-l+1 for c,l in zip(cs,ls)))==1,"gradient on plane")
    require(C==sum(c*l-c*(c+1) for c,l in zip(cs,ls)),"continuous maximum constant")
    degK=-54-sum(degrees);quartic=decomposition(sections(bs,4))
    results.append({"tag":tag,"blocks":bs,"degree":sum(degrees),"degree_K":degK,"top_three":ls,"heights":hs,"continuous_bound":str(C),"capacity":cap,"capacity_pass":degK<=cap,"quartic":quartic,"V_quartic":quartic.get("V",0)})
require([r['tag'] for r in results if not r['capacity_pass']]==['C1','C4','C12'],"three capacity cuts")
require([r['tag'] for r in results if r['capacity_pass'] and not r['V_quartic']]==['C3','C5','C11','C13'],"four new quartic cuts")
require([r['tag'] for r in results if r['capacity_pass'] and r['V_quartic']]==['T','C2','C6','C7','C8','C9','C10'],"seven intermediate survivors")
# Fixed possible internal-derivative targets, after removing all quartic V rows.
internal={}
for s,bs in sources.items():
    complement=[(r,d) for r,d in bs if (r,d)!=("V",-4)]
    targets=[[r,d-2,hom("V",-4,r,d-2)] for r,d in complement if hom("V",-4,r,d-2)]
    internal[s]=targets
require(internal=={"D":[],"P":[],"V":[["V",-4,1]],"Z":[]},"only V-type internal target")
require(hom("V",-4,"V",-6)==0,"vanishing of remaining kernel derivative")
manifest=json.loads((ROOT/'INPUTS.json').read_text())
for m in manifest:
    b=(ROOT/m['file']).read_bytes()
    require(len(b)==m['bytes'] and hashlib.sha256(b).hexdigest()==m['sha256'],"source bytes")
    require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==m['git_blob_sha1'],"Git blob identity")
auth=json.loads((ROOT/'REVIEW-AUTHENTICITY.json').read_text())
require(len(auth)==4 and all(x['local_equals_fresh'] and x['all_manifest_fields_match'] for x in auth),"fresh source authentication")
# Subsequent dual-sign and actual-kernel exclusions, all universally symbolic.
by_tag={r['tag']:r for r in results}
by_blocks={tag:bs for tag,bs,_,_ in shapes}
sign_cuts=[]
for tag in ['T','C2','C6','C7','C8','C9','C10']:
    row=by_tag[tag]
    v=min(e for r,e in by_blocks[tag])
    left=row['degree']+9*v
    if left>-8:sign_cuts.append(tag)
require(sign_cuts==['C8','C9'],'two all-defect dual-sign cuts')
require(by_tag['C8']['degree']+9*(-1)==-5,'C8 strict sign failure')
require(by_tag['C9']['degree']+9*(-1)==-3,'C9 strict sign failure')

def line_euler(n):
    if n>=0:return sym(n)
    if n==-1:return sym(-1)
    return scaled(-1,sym(-n-2))
def euler(bs,t):return plus(*(times(char[r],line_euler(e+t)) for r,e in bs))
def kernel_euler(source,tag,t):return plus(euler(sources[source],t),scaled(-1,euler(by_blocks[tag],t)))
# A kernel split K=R3(-3)+R4(-4)+N has N of degrees at most -5.
# At twist three a fixed N atom R(-j) contributes R Sym^(j-5) W to H1.
# These literal candidate atoms are forced solely by central parity and the
# dimension bound (j-4)*dim R <= 6 (respectively <= 4), not a bundle search.
atoms6=[('W',5),('Wp',5),('S',5),('T',5),('1',6),('A',6),('V',6),('W',7),('Wp',7),('1',8),('1',10)]
atoms4=[('W',5),('Wp',5),('S',5),('1',6),('1',8)]
for r,j in atoms6:require((j-4)*dim[r]<=6,'fixed six-dimensional atom bound')
for r,j in atoms4:require((j-4)*dim[r]<=4,'fixed four-dimensional atom bound')
allow6=[(r,j) for r,j in atoms6 if contained(product(r,j-5),rep(S=1,Wp=1))]
allow4=[(r,j) for r,j in atoms4 if contained(product(r,j-5),rep(W=1,Wp=1))]
require(allow6==[('Wp',5),('S',5),('1',8)],'exact fixed atom types for S+Wp')
require(allow4==[('W',5),('Wp',5),('1',6)],'exact fixed atom types for W+Wp')

def tail_h1(bs,t):
    return plus(*(product(r,-e-t-2) if e+t<=-2 else sym(-1) for r,e in bs))
# C10: all four sources have the same Euler data, including their H1 terms.
for source in sources:
    require(kernel_euler(source,'C10',3)==rep(Wp=-1),'C10 chi K3 '+source)
    require(kernel_euler(source,'C10',4)==rep(V=2,D=1),'C10 chi K4 '+source)
require(sections(by_blocks['C10'],1)==rep(S=1,T=1),'C10 derivative cubic target')
require(sections(by_blocks['C10'],2)==rep(V=1,P=1,D=1),'C10 derivative quartic target')
require(mult('Wp',sections(by_blocks['C10'],1))==0,'C10 excludes cubic Wp kernel')
c10_cases=[
 ('R3=0',rep(),[('Wp',-5)],rep(V=2,D=1)),
 ('R3=S; N=S(-5)+Wp(-5)',char['S'],[('S',-5),('Wp',-5)],rep(V=2,A=-1)),
 ('R3=S; N=O(-8)+Wp(-5)',char['S'],[('1',-8),('Wp',-5)],rep(V=2))]
case_records=[]
for desc,r3,n,r4 in c10_cases:
    require(tail_h1(n,3)==plus(r3,char['Wp']),'C10 required N twist-three cohomology')
    derived=plus(rep(V=2,D=1),scaled(-1,times(r3,char['W'])),tail_h1(n,4))
    require(derived==r4,'C10 R4 Euler derivation')
    genuine=all(v>=0 for v in decomposition(r4).values())
    if genuine:require(not contained(r4,sections(by_blocks['C10'],2)),'C10 near-top injection obstruction')
    else:require(decomposition(r4).get('A')==-1,'C10 negative coefficient obstruction')
    case_records.append({'shape':'C10','case':desc,'R4':decomposition(r4),'genuine':genuine})
# C7: only source D; a cubic S kernel would be the unique evaluation-kernel row.
require([(r,d,hom('S',-3,r,d)) for r,d in sources['D'] if hom('S',-3,r,d)]==[('D',-2,1)],'C7 unique cubic S source row')
require(all(hom('1',2,r,e)==0 for r,e in by_blocks['C7']),'C7 no equivariant map O2 to quotient')
require(kernel_euler('D','C7',3)==rep(W=-1,Wp=-1),'C7 chi K3')
require(kernel_euler('D','C7',4)==rep(V=2,P=1,**{'1':-1}),'C7 chi K4')
require(sections(by_blocks['C7'],2)==rep(A=1,V=1,P=2,D=1),'C7 derivative quartic target')
c7_cases=[
 ('N=W(-5)+Wp(-5)',[('W',-5),('Wp',-5)],rep(V=2,P=1,**{'1':-1})),
 ('N=O(-6)+Wp(-5)',[('1',-6),('Wp',-5)],rep(V=2,P=1))]
for desc,n,r4 in c7_cases:
    require(tail_h1(n,3)==rep(W=1,Wp=1),'C7 required N twist-three cohomology')
    derived=plus(rep(V=2,P=1,**{'1':-1}),tail_h1(n,4))
    require(derived==r4,'C7 R4 Euler derivation')
    genuine=all(v>=0 for v in decomposition(r4).values())
    if genuine:require(not contained(r4,sections(by_blocks['C7'],2)),'C7 near-top injection obstruction')
    else:require(decomposition(r4).get('1')==-1,'C7 negative coefficient obstruction')
    case_records.append({'shape':'C7','case':desc,'R4':decomposition(r4),'genuine':genuine})
final_remaining=[tag for tag in ['T','C2','C6','C7','C8','C9','C10'] if tag not in sign_cuts+['C7','C10']]
require(final_remaining==['T','C2','C6'],'exact three final necessary shapes')

proof_hash=hashlib.sha256((ROOT/"PROOF.md").read_bytes()).hexdigest()
require(proof_hash=="56bb8a0aa5ada0f550e0967ef9e535838e9162c2ff2e5ced039a3f6ddb2aacf0","exact reviewed proof")
output={"final_remaining":final_remaining,"dual_sign_cuts":sign_cuts,"kernel_cuts":["C7","C10"],"kernel_cases":case_records,"proof_sha256":proof_hash,"status":"PASS","method":"closed Q(sqrt(5)) class characters, no McKay recurrence; fixed source facts and fixed symbolic shapes only","checks":checks,"negative_hom":negative_hom,"internal_derivative_targets":internal,"shapes":results,"source_authentication":"four complete originals freshly fetched and byte-identical","scope":"Arithmetic verification only; actual ambient/source premises remain imported. No actual coefficients, bundle-domain enumeration, or height scan."}
print(json.dumps(output,indent=2,sort_keys=True))
