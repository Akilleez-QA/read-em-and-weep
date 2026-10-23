"""Independent coefficient-index checks. Usage: python check.py ../radical-square-geometry"""
from pathlib import Path
import sys,json,itertools,hashlib
import sympy as s
root=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parent.parent/'radical-square-geometry'
p,q=s.symbols('p q'); z=s.sqrt(5)
Pi=s.Matrix([[z,0,1,0,-z/3,0,5],[0,z/3,0,-1,0,-z,0],[0,-z,0,-1,0,z/3,0],[5,0,-z/3,0,1,0,z]])
V=s.Matrix([[-s.Rational(1,15),0,-2*z/5],[0,1,0],[2*z/5,0,-3],[0,-2*z/3,0],[1,0,0],[0,1,0],[0,0,1]])
checks=0
def check(b):
 global checks
 if not b: raise ValueError('Independent check failed at '+str(checks+1))
 checks+=1
# Coefficient-index differential operator, independently of author polynomial differentiation.
def deriv(n):
 A=s.zeros(n,n+1)
 for i in range(n+1):
  if i<n:A[i,i]=(n-i)*p
  if i>0:A[i-1,i]=i*q
 return A
wedge=s.zeros(7,6)
for i in range(6):wedge[i,i]=q;wedge[i+1,i]=-p
matrices={'I':deriv(5)*deriv(6)*V,'II':Pi*wedge*deriv(6)*V}
result=json.loads((root/'RESULT.json').read_text());out={}
for name,M in matrices.items():
 M=M.applyfunc(s.expand)
 recorded=s.Matrix([[s.sympify(e,locals={'p':p,'q':q}) for e in r] for r in result['types'][name]['matrix']])
 check((M-recorded).applyfunc(s.simplify)==s.zeros(*M.shape))
 minors=[s.expand(M[list(rows),:].det()) for rows in itertools.combinations(range(M.rows),3)]
 for a,b in zip(minors,result['types'][name]['all_maximal_minors']):check(s.expand(a-s.sympify(b))==0)
 # Euclidean Bezout identity for all maximal minors on both complete symbolic charts.
 for a,b in [(p,q),(q,p)]:
  fs=[s.Poly(f.subs(a,1),b,extension=z) for f in minors]
  g=fs[0];coeffs=[s.Poly(1,b,extension=z)]
  for f in fs[1:]:
   u,v,h=s.gcdex(g,f);coeffs=[u*c for c in coeffs]+[v];g=h
  check(g.degree()==0)
  check(sum((c*f for c,f in zip(coeffs,fs)),s.Poly(0,b,extension=z))==g)
 # Explicit convolution blocks for degree-two transpose syzygies, independent of general-vector expansion.
 n=2;B=s.zeros(3*(n+3),M.rows*(n+1))
 for r in range(M.rows):
  for c in range(3):
   f=s.Poly(M[r,c],p,q)
   for j in range(n+1):
    for k in range(3):B[c*(n+3)+j+k,r*(n+1)+j]=f.coeff_monomial(p**(2-k)*q**k)
 check(B.rank()==M.rows*3)
 out[name]={'matrix_shape':list(M.shape),'degree_two_syzygy_matrix_shape':list(B.shape),'degree_two_syzygy_rank':B.rank(),'both_symbolic_chart_bezout_identities':True}
for key,target in [('E/S I',(14,-42)),('E/S II',(14,-42)),('K/S I',(12,-36)),('K/S II',(12,-36))]:
 blocks=result['quotient_invariants'][key]['rank_twist_blocks'];check((sum(r for r,d in blocks),sum(r*d for r,d in blocks))==target)
print(json.dumps({'checks':checks,'independent_results':out,'bound_sha256':{n:hashlib.sha256((root/n).read_bytes()).hexdigest() for n in ['PROOF.md','verify.py','RESULT.json','INPUTS.json']}},indent=2))
