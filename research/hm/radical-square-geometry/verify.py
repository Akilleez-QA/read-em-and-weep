"""Exact universal binary-polynomial calculation; no source instances."""
import sympy as s
import hashlib,json,pathlib
from itertools import combinations
ROOT=pathlib.Path(__file__).resolve().parent
checks=0
def check(v,msg):
 global checks
 if not v: raise RuntimeError(msg)
 checks+=1
for item in json.loads((ROOT/'INPUTS.json').read_text()):
 b=(ROOT/item['local_path']).read_bytes()
 check(hashlib.sha256(b).hexdigest()==item['sha256'],'sha256 '+item['local_path'])
 check(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==item['git_blob'],'blob '+item['local_path'])
x,y,p,q=s.symbols('x y p q');z=s.sqrt(5)
Pi=s.Matrix([[z,0,1,0,-z/3,0,5],[0,z/3,0,-1,0,-z,0],[0,-z,0,-1,0,z/3,0],[5,0,-z/3,0,1,0,z]])
V=s.Matrix([[-s.Rational(1,15),0,-2*z/5],[0,1,0],[2*z/5,0,-3],[0,-2*z/3,0],[1,0,0],[0,1,0],[0,0,1]])
check(Pi*V==s.zeros(4,3),'kernel');check(V.rank()==3,'V dimension');check(Pi.rank()==4,'Pi dimension')
def cv(f,n):
 f=s.Poly(s.expand(f),x,y);return s.Matrix([f.coeff_monomial(x**(n-i)*y**i) for i in range(n+1)])
def dp(f):return p*s.diff(f,x)+q*s.diff(f,y)
vs=[sum(V[i,j]*x**(6-i)*y**i for i in range(7)) for j in range(3)]
M1=s.Matrix.hstack(*[cv(dp(dp(f)),4) for f in vs]).applyfunc(s.expand)
M2=s.Matrix.hstack(*[Pi*cv((x*q-y*p)*dp(f),6) for f in vs]).applyfunc(s.expand)
result={'scope':'universal full coefficient maps only','types':{}}
for name,M,expected in [('I',M1,7),('II',M2,4)]:
 minors=[s.expand(M[list(r),:].det()) for r in combinations(range(M.rows),3)]
 polys=[s.Poly(f,p,q,extension=z) for f in minors]
 for f in polys:check(f.total_degree()==6,'homogeneous maximal minor');check(all(sum(m)==6 for m,c in f.terms()),'homogeneous coefficients')
 C=s.Matrix([[f.coeff_monomial(p**(6-i)*q**i) for i in range(7)] for f in polys])
 check(C.rank()==expected,'full sextic span')
 g=polys[0]
 for f in polys[1:]:g=s.gcd(g,f)
 check(g.total_degree()==0,'no projective common root')
 # Two entire symbolic charts, not selected points.
 for var,other in [(p,q),(q,p)]:
  gb=s.groebner([f.as_expr().subs(var,1) for f in polys],other,extension=z)
  check(list(gb)==[1],'unit chart ideal')
 dims=[]
 for n in range(4):
  unknown=s.symbols('a:'+str(M.rows*(n+1)))
  vec=s.Matrix([sum(unknown[j*(n+1)+i]*p**(n-i)*q**i for i in range(n+1)) for j in range(M.rows)])
  eq=[s.Poly(s.expand(f),p,q).coeff_monomial(p**(n+2-i)*q**i) for f in M.T*vec for i in range(n+3)]
  A=s.linear_eq_to_matrix(eq,unknown)[0]
  dims.append(len(unknown)-A.rank())
 check(dims==([0,0,0,2] if name=='I' else [0,0,0,0]),'transpose syzygies')
 result['types'][name]={'matrix':[[str(e) for e in M.row(i)] for i in range(M.rows)],'all_maximal_minors':[str(f.as_expr()) for f in polys],'minor_coefficient_rank':expected,'homogeneous_gcd':'1 up to unit','symbolic_chart_ideals':['1','1'],'transpose_syzygy_dimensions_degree_0_through_3':dims,'all_projective_ranks':3}
quotients={
 'E/S I':[(2,1),(8,-3),(3,-4),(1,-8)],
 'E/S II':[(1,4),(8,-3),(3,-4),(2,-5)],
 'K/S I':[(2,1),(6,-3),(3,-4),(1,-8)],
 'K/S II':[(1,4),(6,-3),(3,-4),(2,-5)]}
result['quotient_invariants']={}
for name,blocks in quotients.items():
 rank=sum(r for r,d in blocks);degree=sum(r*d for r,d in blocks)
 expected=(14,-42) if name.startswith('E') else (12,-36)
 check((rank,degree)==expected,'retained-source quotient '+name)
 result['quotient_invariants'][name]={'rank':rank,'degree':degree,'rank_twist_blocks':blocks}
result['checks']=checks
print(json.dumps(result,indent=2))
