# Universal nine-class character identities only, no HM map entries.
import sympy as s
e=(s.sqrt(5)-1)/2; f=-(s.sqrt(5)+1)/2
rows={'1':[1]*9,'5':[5,5,1,-1,-1,0,0,0,0],'6':[6,-6,0,0,0,1,1,-1,-1],'4':[4,4,0,1,1,-1,-1,-1,-1],'Q':[4,-4,0,1,-1,-1,-1,1,1],'3':[3,3,-1,0,0,-e,-f,-e,-f],'3p':[3,3,-1,0,0,-f,-e,-f,-e],'W':[2,-2,0,-1,1,e,f,-e,-f],'Wp':[2,-2,0,-1,1,f,e,-f,-e]}
v={k:s.Matrix(x) for k,x in rows.items()}; M=s.Matrix.hstack(*v.values())
def mul(a,b):return a.multiply_elementwise(b)
def decomp(a):return {k:s.simplify(x) for k,x in zip(v,M.inv()*a) if s.simplify(x)!=0}
G=mul(v['3']+v['Wp'],v['Q'])-mul(v['Wp'],v['5']+v['Wp'])+v['1']
P=mul(v['3p']+v['W'],v['W']+v['5'])-mul(mul(v['3']+v['Wp'],v['Q']),v['3p'])+mul(v['Wp'],v['4']+v['Q']+v['3']+v['3p'])
source=mul(G,v['3']+v['Wp'])
print('G coeff',decomp(G)); print('P coeff',decomp(P)); print('source',decomp(source))
# P tensor H1F1 = V* V1 tensor Pcoeff Wp; V*V1=V(3p+W).
# C tensor H1F2=V tensor 4 Wp.
target=mul(mul(v['3p']+v['W'],P),v['Wp'])+mul(v['4'],v['Wp'])
print('target',decomp(target)); scalar=v['4']+v['Q']+v['3']+v['3p']
print('tracefree_source',decomp(source-scalar)); print('target minus tracefree source',decomp(target-source+scalar))
