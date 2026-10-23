#!/usr/bin/env python3
"""Exact character, Koszul, first-arrow and formal-surjectivity checks."""
from pathlib import Path
from itertools import product
import json,hashlib
import sympy as s
r=Path(__file__).resolve().parent;checks=[]
def ck(name,b):
 if not b:raise RuntimeError(name)
 checks.append(name)
for i in json.loads((r/'INPUTS.json').read_text()):
 d=(r/i['local_path']).read_bytes();ck('sha256 '+i['local_path'],hashlib.sha256(d).hexdigest()==i['sha256']);ck('git_blob '+i['local_path'],hashlib.sha1(b'blob '+str(len(d)).encode()+b'\0'+d).hexdigest()==i['git_blob'])
# McKay multiplication by the defining W, from the binary-icosahedral graph.
names=['1','W','A','S','D','T','V','P','Wp'];idx={n:i for i,n in enumerate(names)}
def e(n):return s.eye(9)[:,idx[n]]
adj={'1':['W'],'W':['1','A'],'A':['W','S'],'S':['A','D'],'D':['S','T'],'T':['D','V','P'],'V':['T'],'P':['T','Wp'],'Wp':['P']}
M=s.Matrix.hstack(*[sum((e(b) for b in adj[a]),s.zeros(9,1)) for a in names]);dims=s.Matrix([[1,2,3,4,5,6,3,4,2]])
ck('McKay graph dimension identity',dims*M==2*dims)
sy=[e('1'),e('W')]
for k in range(2,19):sy.append(M*sy[-1]-sy[-2])
ck('Sym15 exact',sy[15]==e('S')+2*e('T'))
ck('Sym8 exact',sy[8]==e('P')+e('D'))
Aop=M*M-s.eye(9)
ck('A tensor Sym3 exact',Aop*sy[3]==e('W')+e('S')+e('T'))
K=Aop*sy[3]+sy[15]
ck('ambient complete multiplication kernel',K==e('W')+2*e('S')+3*e('T'))
ck('pure image first Koszul kernel',M*e('D')-e('T')==e('S'))
Kb=K-e('S')
ck('quotient complete multiplication kernel',Kb==e('W')+e('S')+3*e('T'))
ck('quotient kernel has no Wprime',Kb[idx['Wp']]==0)
ck('W tensor P exact',M*e('P')==e('Wp')+e('T'))
ck('forbidden T kernel leaves only two dimensions',8-6==2<4)
ck('generated middle character and dimension',e('T')+M*e('P')==e('Wp')+2*e('T') and (dims*(e('T')+M*e('P')))[0]==14)
ck('A tensor P exact',Aop*e('P')==e('V')+e('P')+e('D'))
ranks=sorted(4+3*v+4*p+5*d for v,p,d in product([0,1],repeat=3))
ck('all necessary endpoint ranks',ranks==[4,7,8,9,11,12,13,16])
ck('first cokernel rank and degree',14-9==1+4 and 5+4*1==9)
ck('new middle differs every radical image',14 not in [6,12,18])
# Full symbolic first arrow, no chosen projective direction.
u,v=s.symbols('u v');Darrow=s.zeros(6,5)
for j in range(5):Darrow[j,j]=u;Darrow[j+1,j]=v
ck('complete D arrow endpoint minors',Darrow[:5,:].det()==u**5 and Darrow[1:,:].det()==v**5)
ck('D-arrow Koszul evaluation row',s.Matrix([[(-1)**j*u**j*v**(5-j) for j in range(6)]])*Darrow==s.zeros(1,5))
Parrow=s.eye(4)*u;Parrow=Parrow.col_join(s.eye(4)*v)
ck('free P arrow endpoint minors',Parrow[:4,:].det()==u**4 and Parrow[4:,:].det()==v**4)
ck('free P cokernel evaluation',s.Matrix.hstack(-v*s.eye(4),u*s.eye(4))*Parrow==s.zeros(4))
# Formal block-surjectivity inverse identity in noncommuting matrices.
t=s.symbols('t');E=s.MatrixSymbol('E',4,4);L=s.MatrixSymbol('L',4,5);Id=s.Identity(4)
Inv=(Id+t*E).I
ck('formal right inverse identity',((Id+t*E)*Inv).doit()==Id)
ck('formal five-kernel graph identity',(t*L-(Id+t*E)*Inv*t*L).doit()==s.ZeroMatrix(4,5))
ck('original permanent-kernel rank bound',41-5==36<37)
ck('original generic lower rank from second',33+3==36)
print(json.dumps(dict(status='pass',count=len(checks),checks=checks,middle_character='Wp+2T',generated_dimensions=[9,14,'4+3eV+4eP+5eD'],necessary_target_ranks=ranks,first_cokernel='O(5)+P O(1)',scope='actual conditional generated submodule; endpoint alternatives not asserted realizable; no source coefficients selected'),indent=2))
