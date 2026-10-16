"""QB-R: actual AST/integer metadata only; arithmetic uses explicit artificial data."""
import hashlib
import inspect
import itertools
import json
import math
from pathlib import Path
import subprocess
import unittest
from fractions import Fraction as F
import q_binding as B

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
REPO = HERE.parents[2]
ZERO = (0, 0, 0, 0)
PINNED = {
    'inner-quotient/quotient.py': '08a0e51912e5afab249fa6accc759a03023ee5def7e400e3654ce84dbd4f2b91',
    'inner-quotient/source-pins.json': 'bda2226ce1c4154b3c304da3ce13a98e35985bd9d66f343c45c85973ac6aecce',
    'inserted-coefficients/interfaces.py': '9ba74c9e328c38083c4f8d49a04818d8a67216aa0a0b477563523ed4728f72fa',
    'inserted-coefficients/polynomial_coefficients.py': 'c826bc5379910222bb962288581a9e5fec64d3b956c03cefdfc4566567cf19ee',
}
SOURCES = (
    ('research/hm/null-operator-compiler/outer_partition_source_binding.py',
     'f5a33e325e1eee6b801c94613093d1cd4686ca54',
     '3308e733e4fc12ee297964d9c3bd4c7166bac6b061853690ef309ea786c5bd2a'),
    ('research/hm/null-source-integration/combined-pole/PROOF.md',
     '9d7a5a400b48d9b8b46008fbd9fb3d79be601920',
     '03673d6f120cb0b89d6d3887b7ab0bfee6aa33acf2abcc0ddbb116071b159c25'),
)

def owner(c=5, m=0, t=8, seed=12, occurrence=('QB-R', 1)):
    return B.I.FullOwner(seed, occurrence, c, m, t)


def monomials(R, root):
    """Read unit-monomial AST exponents, without coefficient evaluation."""
    op, *args = R.nodes[root]
    if op == 'constant':
        if args == [1, 1]: return [ZERO]
        raise ValueError('only unit leaves in catalog monomials')
    if op == 'coordinate': return [tuple(int(i == args[0]) for i in range(4))]
    if op == 'sum': return [e for child in args[0] for e in monomials(R, child)]
    if op == 'product':
        return [tuple(a+b for a,b in zip(x,y))
                for x in monomials(R,args[0]) for y in monomials(R,args[1])]
    if op == 'power':
        base = monomials(R,args[0])
        if len(base) != 1: raise ValueError('monomial power required')
        return [tuple(n*args[1] for n in base[0])]
    raise ValueError(op)


def artificial():
    # Independent constants satisfying c0*v0+c1*v1=1 and h+v2*a=v^5.
    v, a, v2 = F(3,2), F(3,5), F(2,3)
    h = v**5-v2*a
    C = lambda x: {ZERO:x}
    return B.QH.ArtificialCatalog([C(v),C(v),C(v2),C(1),C(1)],
        [C(h)]*5,C(a),[C(1),C(F(1,3)),C(0),C(0),C(0)])


class Independent(unittest.TestCase):
    def test_exact_inputs_and_immutable_git_texts(self):
        marker = json.loads((HERE/'producer-ready.json').read_text())
        self.assertTrue(marker['ready_for_independent_review'])
        for name, digest in marker['files'].items():
            self.assertEqual(hashlib.sha256((HERE/name).read_bytes()).hexdigest(),digest)
        for name, digest in PINNED.items():
            self.assertEqual(hashlib.sha256((BASE/name).read_bytes()).hexdigest(),digest)
        pins=json.loads((BASE/'inner-quotient/source-pins.json').read_text())['sources']
        for row,(path,blob,digest) in zip(pins,SOURCES):
            self.assertEqual(row,dict(commit='10810ee877fdaf291399198ad60d7dd0c316a42d',
                path=path,git_blob=blob,sha256=digest))
            raw=subprocess.check_output(['git','show',row['commit']+':'+path],cwd=REPO)
            self.assertEqual(hashlib.sha256(raw).hexdigest(),digest)
            self.assertEqual(hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest(),blob)
        self.assertEqual(len(pins),2)

    def test_local_catalog_ast_all_charts_and_hidden_v0(self):
        for bits in itertools.product((0,1),repeat=4):
            R=B.QH.FiniteRing('physical',B.QH.Budget())
            v,h,a,H=B.QH.ActualCatalog().bind(R,bits)
            for j in range(5):
                expected=[tuple(int(selected[i] != bits[i]) for i in range(4))
                    for selected in itertools.product((0,1),repeat=4) if sum(selected)==j]
                self.assertEqual(sorted(monomials(R,v[j])),sorted(expected))
                self.assertEqual(h[j],R.plus(R.power(v[j],5),R.times(R.const(-1),*v)))
            self.assertEqual(a,R.times(v[0],v[1],v[3],v[4]))
            for k in range(5):
                expected=[e for e in itertools.product(range(k+1),repeat=4)
                    if sum(e)==k and all(not bits[i] or e[i]==0 for i in range(4))]
                self.assertEqual(sorted(monomials(R,H[k])),sorted(expected))
            self.assertEqual(R.budget.queries,0)

    def test_actual_fixed_parameters_owner_frame_and_ledger(self):
        for t in range(16):
            for c,p,m in ((5,(0,1),5),(2,(2,3),10)):
                o=owner(c,m,t);b=B.ActualQuotientBinding(o,p)
                bits=tuple((t>>(3-i))&1 for i in range(4));s=sum(bits)
                degrees=tuple(14*(4 if c==5 else 5)+(1+2*((m>>i)&1) if i in p else 0) for i in range(4))
                self.assertEqual(b.program.parameters,dict(N=14,M=27,T=135,L=134*(s+1)+1,s=s,legal_power=1))
                self.assertEqual(b.program.bits,bits)
                self.assertEqual(b.program.shift,tuple(-degrees[i] if bits[i] else 0 for i in range(4)))
                for C in (b.finite_C,b.local_C):
                    self.assertEqual(C.homogeneous_degree,degrees)
                    self.assertEqual(C.ledger,({'owner':o.data(),'kind':'H','axis':None,'power':14},)+
                        tuple({'owner':o.data(),'kind':'ell','axis':i,'power':1} for i in p))
                    R=C.R
                    cbits=bits if C.local else (0,0,0,0)
                    v,h,a,H=B.QH.ActualCatalog().bind(R,cbits)
                    factors=[R.power(a if c==5 else h[c],14)]
                    for i in p:
                        x=R.x(i);mask=(m>>i)&1
                        if cbits[i]:
                            ell=R.plus(R.const(1),R.times(R.const(-1),R.power(x,2))) if mask else x
                        else:
                            ell=R.plus(R.power(x,3),R.times(R.const(-1),x)) if mask else R.const(1)
                        factors.append(ell)
                    self.assertEqual(C.root,R.times(*factors))
                    self.assertEqual(C.R.budget.queries,0)
                box=b.support_box();bound=b.program.R.bound(b.program.root)
                if box is not None:
                    lo,hi=box
                    self.assertEqual(lo,tuple(-degrees[i]-bound[i] if bits[i] else 0 for i in range(4)))
                    self.assertEqual(hi,tuple(-degrees[i] if bits[i] else bound[i] for i in range(4)))
                self.assertEqual(b.program.R.budget.queries,0)
        api=B.ActualQBinding()
        for o in (owner(),owner(seed=30),owner(occurrence=('QB-R',2))):
            self.assertEqual(api.describe(o)['owner'],o.data())

    def test_actual_entrypoints_refuse_before_any_request_inspection(self):
        class Poison:
            def __iter__(self): raise AssertionError('inspected request')
            def __eq__(self,other): raise AssertionError('compared request')
        api=B.ActualQBinding()
        for o in (owner(),owner(4,1,0)):
            bound=B.ActualQuotientBinding(o)
            C=B.ClearingDefinition(o,(0,1))
            for obj in (api,bound,C):
                obj.mode='synthetic';obj.physical_admission=True;obj.status=lambda *a:True
            calls=(lambda e:api.coefficient(Poison(),e,Poison()),
                   lambda e:api.factor_terms(Poison(),Poison()),
                   lambda e:bound.coefficient(e),lambda e:bound.factor_terms(Poison(),Poison()),C.coefficient)
            for e in (Poison(),None,(),(-1,0,0,0),(True,0,0,0)):
                for call in calls:
                    with self.assertRaises(B.I.PhysicalAdmissionMissing): call(e)
            self.assertEqual(bound.program.R.budget.queries,0)

    def test_no_catalog_or_status_callback_constructor_path(self):
        self.assertEqual(tuple(inspect.signature(B.ActualQBinding).parameters),('repo',))
        self.assertEqual(tuple(inspect.signature(B.ActualQuotientBinding).parameters),('owner','p'))
        for key in ('catalog','status','admission','budget'):
            with self.assertRaises(TypeError): B.ActualQBinding(**{key:lambda *a:True})
            with self.assertRaises(TypeError): B.ActualQuotientBinding(owner(),**{key:lambda *a:True})
        with self.assertRaises((TypeError,ValueError)): B.ActualQBinding(repo=lambda *a:True)
        with self.assertRaises(ValueError): B.ArtificialBinding(owner(),B.QH.ActualCatalog())
        class Pretender(B.QH.ArtificialCatalog): pass
        fake=object.__new__(Pretender)
        with self.assertRaises(ValueError): B.ArtificialBinding(owner(),fake)
        for p in ((1,0),(3,2),(False,True),(0,1,2),None):
            with self.assertRaises(ValueError): B.pair(p)

    def test_tiny_rational_partition_and_binomial_quotients(self):
        cat=artificial();N=2;M=3;T=15;L=29;v=F(3,2);a=F(3,5);z=F(2,5);h=v**5-z
        Bs=[]
        for j in (0,1):
            Bs.append(sum((F(math.comb(L,n))*F(-1,3)**n*v**(L-T)
                for n in range(L+1) if (n>=T if j==0 else n<T and L-n>=T)),F(0)))
        self.assertEqual(sum(b*v**T for b in Bs),1)
        cb=sum(F(math.comb(M,k))*h**(k-N)*z**(M-k) for k in range(N,M+1))
        db=sum(F(math.comb(M,k))*h**k*F(2,3)**(M-k)*a**(M-k-N) for k in range(N))
        self.assertEqual(h**N*cb+a**N*db,v**T)
        for c,expected in ((0,Bs[0]*cb),(1,Bs[1]*cb),(5,sum(Bs)*db)):
            b=B.ArtificialBinding(owner(c),cat,N=N)
            # Infinity axis0 is in pair: local t, degree shift -(N*d+1).
            e=(-(N*(4 if c==5 else 5)+2),0,0,0)
            self.assertEqual(b.coefficient(e),expected)
        # Nonpair raw weight vs pair quotient, both legal bits; complete tiny streams.
        tiny_B0=sum(F(math.comb(9,n))*F(-1,3)**n*F(3,2)**4 for n in range(5,10))
        for p in ((0,1),(2,3)):
            for mask in (0,1):
                b=B.ArtificialBinding(owner(0,mask),cat,N=1,p=p)
                terms=dict(b.factor_terms(b.owner,p));box=b.support_box()
                self.assertTrue(all(all(lo<=e[i]<=hi for i,(lo,hi) in enumerate(zip(*box))) for e in terms))
                if p==(0,1):
                    shift=-5-(3 if mask else 1)
                    expected={(shift-(0 if mask else 1),0,0,0):tiny_B0}
                else:
                    expected={(-5,0,0,0):tiny_B0,(-7,0,0,0):-tiny_B0} if mask else {(-7,0,0,0):tiny_B0}
                self.assertEqual(terms,expected)
                with self.assertRaises(ValueError): b.factor_terms(owner(0,mask,occurrence=('QB-R',2)),p)
                with self.assertRaises(ValueError): b.factor_terms(b.owner,(2,3) if p==(0,1) else (0,1))

    def test_formal_rational_legal_division_and_frame_countercontrols(self):
        # Formal tiny homogeneous equations only; no actual catalog evaluation.
        for x in (F(2),F(-3,2)):
            t=1/x
            for mask in (0,1):
                d=1 if mask==0 else 3
                finite=F(1) if mask==0 else x*(x*x-1)
                local=t if mask==0 else 1-t*t
                self.assertEqual(local,t**d*finite)
                q=t if mask==0 else F(1)
                weight=t*t if mask==0 else 1-t*t
                self.assertEqual(local*q,weight)
                self.assertNotEqual(local*q*t**2,weight) # appended pair twist is wrong
            for d in (4,5):
                c=14*d+3;alpha=2;beta=3
                Cfinite=x**beta;Clocal=t**c*Cfinite
                qlocal=t**alpha;Qhat=x**(-c-alpha)
                self.assertEqual(Cfinite*Qhat,Clocal*qlocal)
                self.assertNotEqual(Cfinite*Qhat*x**2,Clocal*qlocal)

if __name__=='__main__': unittest.main()
