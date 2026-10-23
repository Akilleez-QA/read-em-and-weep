"""Universal block conjugation and canonical-kernel controls, not HM evaluations."""
import itertools,json

def mul(a,b):
 return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
checks=0
# In basis H' then E^0, Hom(E^0,H')=0 forces lower triangular blocks.
# Independently check closure and invariant kernel without assuming centrality.
for a,b,c,d,e,f in itertools.product(range(-1,2),repeat=6):
 A=[[a,0],[b,c]];B=[[d,0],[e,f]]
 C=mul(A,B)
 if C[0][1]!=0 or C[0][0]!=a*d:raise RuntimeError('canonical quotient')
 checks+=1
P=[[1,0],[0,0]];A=[[0,0],[1,0]]
if mul(P,A)==mul(A,P):raise RuntimeError('noncentrality control')
checks+=1
# Full change of complement, no relation assumption.
for a,b,c,d,v in itertools.product(range(-2,3),repeat=5):
 F=[[a,b],[c,d]];S=[[1,v],[0,1]];Si=[[1,-v],[0,1]]
 actual=mul(mul(Si,F),S)
 expected=[[a-v*c,a*v+b-v*c*v-v*d],[c,d+c*v]]
 if actual!=expected:raise RuntimeError('conjugation')
 checks+=1
print(json.dumps({'status':'PASS','checks':checks,'scope':'synthetic scalar block identities only; not proof of HM vanishing hypotheses'},indent=2))
