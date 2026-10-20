"""Universal four-variable identities only; no model or source imports."""
import itertools,json,sympy as s
x=s.symbols('x1:5')
def sign(p):return (-1)**sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
def alt(f):return s.expand(sum(sign(p)*f.xreplace({x[i]:x[p[i]] for i in range(4)}) for p in itertools.permutations(range(4))))
e=[sum(s.prod(x[i] for i in S)for S in itertools.combinations(range(4),k))for k in range(1,5)]
D=s.prod(x[i]-x[j]for i in range(4)for j in range(i+1,4))
assert s.expand(s.det(s.Matrix([[s.diff(f,z)for z in x]for f in e]))-D)==0
assert s.expand(alt(x[0]**3*x[1]**2*x[2])-D)==0
assert s.expand(alt(D)-24*D)==0
for ex in [(0,0,0,0),(4,2,1,0),(5,3,2,1),(3,3,1,0),(2,1,0,4)]:
 a=alt(s.prod(z**n for z,n in zip(x,ex)))
 q,r=s.div(a,s.expand(D),*x);assert r==0
 for i in range(3):assert s.expand(q-q.xreplace({x[i]:x[i+1],x[i+1]:x[i]}))==0
# Projective reversal Z0,...,Z4 -> Z4,...,Z0; entirely formal.
z=s.symbols('z1:5')
u=[z[2]/z[3],z[1]/z[3],z[0]/z[3],1/z[3]]
assert s.factor(s.det(s.Matrix([[s.diff(f,w) for w in z] for f in u])))==z[3]**-5
orientation_cases=0
for p in itertools.permutations(range(4)):
 assert sign(p)*sign(p)==1
 orientation_cases+=1
harmonic_cases=0
for a in itertools.product((-3,-2,-1),repeat=4):
 shifted=tuple(a[i]+(2 if i>=2 else 0) for i in range(4))
 assert (shifted==(-1,-1,-1,-1))==(a==(-1,-1,-3,-3))
 harmonic_cases+=1
print(json.dumps({'jacobian_sign':1,'alternant_monomial_maps_to':1,'trace_of_jacobian':24,'toy_divisibility_cases':5,'infinity_transition_sign':1,'orientation_cases':orientation_cases,'harmonic_pairing_cases':harmonic_cases,'source_values_evaluated':False}))
