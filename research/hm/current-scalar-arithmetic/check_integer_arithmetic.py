#!/usr/bin/env python3
"""Independent exact integer arithmetic fixtures. Never opens the actual source DAG."""
import importlib.util,json,hashlib,random,time,sys
from pathlib import Path
from fractions import Fraction
from itertools import product
sys.path.insert(0,str(Path(__file__).resolve().parent))
import exact_oracle as oracle
if sys.flags.optimize:
 raise RuntimeError('Run assertion-enabled Python, without -O')
H=Path(__file__).resolve().parent;B=H
p=B/'integer_quotient_ring.py';before=hashlib.sha256(p.read_bytes()).hexdigest()
spec=importlib.util.spec_from_file_location('candidate_integer_ring',p);R=importlib.util.module_from_spec(spec);spec.loader.exec_module(R)
assert (R.V,R.W,R.Z)==oracle.SHAPE and (R.RV,R.RW,R.QZ)==(11,73,803)
keys=list(product(range(6),range(37),range(22)));rng=random.Random(102571);count={'product':0,'denseAnalytic':0,'power':0,'shift':0,'guard':0};start=time.monotonic()
def enc(t):return t[0]+11*t[1]+803*t[2]
def candidate(p):return R.make({enc(k):v for k,v in p.items() if v})
def decode(p):return {(q%11,(q//11)%73,q//803):v for q,v in p.p.items()}
def check(a,b):
 expected=oracle.mul(a,b)
 A,B=candidate(a),candidate(b)
 for func in (R.sparse_mul,R.packed_mul,R.mul):assert decode(func(A,B))==expected,func.__name__
 count['product']+=1
# Distinct exponent tuples, mixed signs, huge integer limbs, zero and identity.
for n in range(90):
 size=rng.choice([0,1,2,7,31,67,101]);bits=rng.choice([1,8,31,127,269,423,777])
 a={k:rng.choice([-1,1])*rng.randrange(1,1<<bits) for k in rng.sample(keys,size)}
 b={k:rng.choice([-1,1])*rng.randrange(1,1<<bits) for k in rng.sample(keys,rng.choice([0,1,3,19,71]))}
 check(a,b)
for bit in (7,8,15,16,31,32,269,423):
 check({(0,0,0):1<<bit},{(0,0,0):1<<(bit+1)})
for a,b in [((5,0,0),(1,0,0)),((0,36,0),(0,1,0)),((0,0,21),(0,0,1)),((5,36,21),(5,36,21)),((4,35,20),(1,1,1))]:check({a:-9},{b:17})
# Full4884-slot dense convolution. Each retained coefficient has exactly
# (r+1)(w+1)(z+1) products. Alternating signs force all four signed products.
for bit,alternating in [(1,False),(269,True),(423,False)]:
 M=(1<<bit)-1
 a={k:(-1)**sum(k)*M if alternating else M for k in keys}
 expected={k:(-1)**sum(k)*(k[0]+1)*(k[1]+1)*(k[2]+1)*M*M if alternating else (k[0]+1)*(k[1]+1)*(k[2]+1)*M*M for k in keys}
 assert decode(R.packed_mul(candidate(a),candidate(a)))==expected
 count['denseAnalytic']+=1
for exponent in [0,1,2,3,13,71,72,142]:
 a={(0,0,0):2,(1,0,0):-3,(0,1,0):1}
 assert decode(R.power(candidate(a),exponent))==oracle.power(a,exponent)
 count['power']+=1
# Nonconstant71st powers retain cross terms in characteristic zero.
a={(0,0,0):1,(1,0,0):1};assert decode(R.power(candidate(a),71))[(1,0,0)]==71
for _ in range(90):
 a={k:rng.choice([-1,1])*rng.randrange(1,1<<35) for k in rng.sample(keys,30)}
 c=rng.choice([-17,-1,0,1,23]);du=rng.randrange(9);dt=rng.randrange(40)
 base={k:rng.randrange(-100,100) for k in rng.sample(keys,10)};base={k:v for k,v in base.items() if v}
 expected=dict(base)
 for (r,w,z),v in a.items():
  if r+du<6 and w+dt<37:expected[r+du,w+dt,z]=expected.get((r+du,w+dt,z),0)+c*v
 expected={k:v for k,v in expected.items() if v}
 C={enc(k):v for k,v in base.items()};R.add_shift(C,candidate(a),c,du,dt)
 assert {(q%11,(q//11)%73,q//803):v for q,v in C.items()}==expected
 count['shift']+=1
for args in [({},R.ONE,1,-1,0),({},R.ONE,1,0,-1),({},R.ONE,Fraction(1,2),0,0)]:
 try:R.add_shift(*args)
 except AssertionError:count['guard']+=1
 else:raise AssertionError('invalid shift/scalar accepted')
try:R.packed_mul(candidate({(0,0,0):1<<4096}),R.ONE)
except AssertionError:count['guard']+=1
else:raise AssertionError('width guard absent')
assert hashlib.sha256(p.read_bytes()).hexdigest()==before
report={'status':'PASS','field':'Z','arithmeticSHA256':before,'independentOracleSHA256':hashlib.sha256((H/'exact_oracle.py').read_bytes()).hexdigest(),'counts':count,'operations':dict(R.OP),'fullDenseSlots':4884,'largestDenseInputBits':423,'largestSparseInputBits':777,'ordinaryPower71CrossTermChecked':True,'signedPackingProof':'At every encoded exponent, positive and negative pair subsets are disjoint; each total has at most min(nnzA,nnzB) summands. Both packed totals are bounded by min(nnzA,nnzB)*maxAbsA*maxAbsB, strictly below byte-rounded base. Strides11 and73 exceed product r and w degrees10 and72.','actualSourceNodesEvaluated':0,'elapsedSeconds':time.monotonic()-start}
print(json.dumps(report,indent=2))
