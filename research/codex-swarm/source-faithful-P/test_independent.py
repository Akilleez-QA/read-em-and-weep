"""PB-R: authenticated metadata and artificial algebra only; run by filename."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
from unittest.mock import patch
import copy
import hashlib
import importlib
import inspect
import json
import subprocess
import unittest

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
MARKER_SHA = '8150a3a02b529be8398ba857b7e9f3fcd993900be2f14cc6f3a5fe2722169c62'
PINS_SHA = '0ac211d49398b2d64b1dac25f19e304d473890aa8d74188eca76a7de5f371fab'
CLR_REV = '82a8785d0a23e8d4e44e9ca4f52c8bb24fdadbdc'
CLR_REVIEWS = {
    'review-independent.md':'e1fc22e0352c91212df870a8591299986efa6f372909177e9174ac8cc1982226',
    'review-degree.md':'24de3cf66a2815f7cc81dfed8538648eb80c84f5b1bbf0596893ff1c04d30662',
}

def digest(b): return hashlib.sha256(b).hexdigest()
def authenticated():
    marker = (HERE/'producer-ready.json').read_bytes()
    if digest(marker) != MARKER_SHA: raise RuntimeError('producer marker drift')
    m = json.loads(marker)
    if len(m['files']) != 6: raise RuntimeError('producer file set')
    for name, expected in m['files'].items():
        if digest((HERE/name).read_bytes()) != expected: raise RuntimeError('producer drift: '+name)
    rawpins = (HERE/'source-pins.json').read_bytes()
    if digest(rawpins) != PINS_SHA: raise RuntimeError('pin manifest drift')
    raw = {}
    for row in json.loads(rawpins)['sources']:
        b = subprocess.check_output(['git','show',row['commit']+':'+row['path']], cwd=REPO, timeout=15)
        blob = hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
        if digest(b) != row['sha256'] or blob != row['git_blob']: raise RuntimeError('source pin drift')
        raw[row['path']] = b
    for name in ('interfaces.py','source_program.py','polynomial_coefficients.py'):
        path = 'research/codex-swarm/inserted-coefficients/'+name
        if (REPO/path).read_bytes() != raw[path]: raise RuntimeError('runtime dependency drift')
    # Additional accepted reviews are pinned by the authenticated PH frames.py.
    for name, expected in CLR_REVIEWS.items():
        b=subprocess.check_output(['git','show',CLR_REV+':research/codex-swarm/whole-source-clearing/'+name],cwd=REPO,timeout=15)
        if digest(b)!=expected:raise RuntimeError('CLR review drift')
    return raw

# Authenticate before importing any producer code; authenticate again at teardown.
RAW = authenticated()
import p_binding as pb
pc = importlib.import_module('polynomial_coefficients')
sp = importlib.import_module('source_program')

class Jet:
    """Exact artificial rational first jets, independent of INS Ring."""
    def __init__(self, v, d=(0,0,0,0)): self.v=F(v); self.d=tuple(map(F,d))
    def __add__(a,b):
        b = b if isinstance(b,Jet) else Jet(b)
        return Jet(a.v+b.v, [x+y for x,y in zip(a.d,b.d)])
    __radd__=__add__
    def __neg__(a): return Jet(-a.v,[-x for x in a.d])
    def __sub__(a,b): return a+-asjet(b)
    def __mul__(a,b):
        b=asjet(b)
        return Jet(a.v*b.v,[x*b.v+a.v*y for x,y in zip(a.d,b.d)])
    __rmul__=__mul__
    def __truediv__(a,b):
        b=asjet(b)
        return Jet(a.v/b.v,[(x*b.v-a.v*y)/b.v**2 for x,y in zip(a.d,b.d)])
    def __pow__(a,n):
        if n==0:return Jet(1)
        return Jet(a.v**n,[n*a.v**(n-1)*x for x in a.d])
def asjet(x):return x if isinstance(x,Jet) else Jet(x)
X=[Jet(v,[int(i==j) for j in range(4)]) for i,v in enumerate((2,3,4,5))]
def prod(xs):
    out=Jet(1)
    for x in xs:out=out*x
    return out

class ArtificialJetRing:
    """Replacement only during artificial lowering; no physical arrays enter."""
    def __init__(self,*args):self.nodes=[];self.tainted=[]
    def put(self,j,t=False):self.nodes.append(j);self.tainted.append(t);return len(self.nodes)-1
    def const(self,c):return self.put(Jet(c))
    def x(self,i):return self.put(X[i])
    def elementary(self,k):return self.put(sum((prod(X[i] for i in s) for s in combinations(range(4),k)),Jet(0)))
    def plus(self,*ids):return self.put(sum((self.nodes[i] for i in ids),Jet(0)),any(self.tainted[i] for i in ids))
    def times(self,*ids):return self.put(prod(self.nodes[i] for i in ids),any(self.tainted[i] for i in ids))
    def power(self,i,n):return self.put(self.nodes[i]**n,self.tainted[i])
    def partial(self,i,axis):
        if self.tainted[i]:raise RuntimeError('first jet used for nested derivative')
        return self.put(Jet(self.nodes[i].d[axis]),True)
    def polynomial(self,terms):return self.put(sum((prod(X[i]**e for i,e in enumerate(es))*c for es,c in terms.items()),Jet(0)))

def mm(a,b):return [[sum((a[i][k]*b[k][j] for k in range(len(b))),Jet(0)) for j in range(len(b[0]))] for i in range(len(a))]
def tr(a):return sum((a[i][i] for i in range(len(a))),Jet(0))
def transpose(a):return list(map(list,zip(*a)))
def add(a,b):return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def neg(a):return [[-x for x in r] for r in a]
def partial(a,i):return [[Jet(x.d[i]) for x in r] for r in a]
def scalar(a,c):return [[x*c for x in r] for r in a]
def owner_triple(masks=(1,2,3)):
    return tuple(pb.FullOwner(71,('review',i),i,m,15-i) for i,m in enumerate(masks))
def toys():
    # Stored entries in e1,e2, with independent carrier matrices; 13 zero pads.
    one=[['0,0,0,0',1]]; e1=[['1,0,0,0',1]]; e2=[['0,1,0,0',1]]
    blocks=[([one,e1,[],one],[e2,one,one,[]]),
            ([e2,one,one,one],[one,[],e1,one]),
            ([one,[],e1,e2],[one,e2,[],one])]
    charts=[]
    for a,b in blocks:
        charts.append({'I':[[copy.deepcopy(a[2*r+s]) if r<2 else [] for s in range(2)] for r in range(15)],
                       'P':[[copy.deepcopy(b[2*r+s]) if s<2 else [] for s in range(15)] for r in range(2)]})
    return charts

def direct(pair,oo,variant=None):
    e1=sum(X,Jet(0)); e2=sum((X[i]*X[j] for i,j in combinations(range(4),2)),Jet(0));z=Jet(0);u=Jet(1)
    Is=[[[u,e1],[z,u]],[[e2,u],[u,u]],[[u,z],[e1,e2]]]
    Ps=[[[e2,u],[u,z]],[[u,z],[e1,u]],[[u,e2],[z,u]]]
    H=[1+X[i] for i in range(3)]
    def K(a,b):return scalar(transpose(mm(Ps[a],Is[b])),Jet(1)/(H[a]*H[b]))
    def Q(a,i):
        m=(oo[a].legal_mask>>i)&1
        q=Jet(m)*(X[i]**2+1)/(X[i]*(X[i]**2-1)*2)
        if variant=='gerbe_as_Q':q=Jet(m)/X[i]
        return [[q,z],[z,-q]]
    def T(a,b,i):
        k=K(a,b);left=mm(Q(b,i),k);right=mm(k,Q(a,i))
        if variant=='omit_left':left=[[z,z],[z,z]]
        if variant=='omit_right':right=[[z,z],[z,z]]
        return add(add(partial(k,i),left),neg(right))
    p,q=pair;A=T(0,1,p);B=T(1,2,q);C=T(1,2,p);D=T(0,1,q)
    mixed=add(mm(C,D),neg(mm(B,A)))
    if variant=='reverse':mixed=add(mm(D,C),neg(mm(A,B)))
    gerbe=F(15,4)*Jet(((oo[1].legal_mask>>p)&1)-((oo[0].legal_mask>>p)&1))/X[p]
    gerbe=gerbe*Jet(((oo[2].legal_mask>>q)&1)-((oo[1].legal_mask>>q)&1))/X[q]
    f=gerbe-tr(mm(K(2,0),mixed))*F(-1 if variant=='wrong_trace_sign' else 1,4)
    clearing=prod(H[a]**14*prod(X[i]*(X[i]**2-1) if (o.legal_mask>>i)&1 else Jet(1) for i in pair) for a,o in enumerate(oo))
    return (clearing*f).v

class IndependentControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.binding=pb.ActualPBinding(REPO)
    @classmethod
    def tearDownClass(cls):authenticated()

    def test_153_lowering_artificial_rational_jets(self):
        for pair,masks in [((0,1),(1,2,3)),((2,3),(4,8,12))]:
            oo=owner_triple(masks)
            cat=pc.Catalog('synthetic',toys(),synthetic_H=[{(0,0,0,0):1,tuple(int(i==c) for i in range(4)):1} for c in range(3)])
            dag=self.binding.symbolic_program_definition(pair)['dag']
            with patch.object(pc,'Ring',ArtificialJetRing):
                program=pc.ClearedSourceProgram(dag,152,cat,oo)
            got=program.ring.nodes[program.root.node].v
            self.assertNotEqual(got,0)
            self.assertEqual(got,direct(pair,oo))
            for wrong in ('omit_left','omit_right','gerbe_as_Q','reverse','wrong_trace_sign'):
                self.assertNotEqual(got,direct(pair,oo,wrong),wrong)

    def test_free_word_matrix_contraction_order(self):
        class Words:
            def __init__(self):self.nodes=[]
            def put(self,w):self.nodes.append(w);return len(self.nodes)-1
            def const(self,c):return self.put({():F(c)})
            def times(self,*ids):
                out={():F(1)}
                for i in ids:
                    nxt={}
                    for a,c in out.items():
                        for b,d in self.nodes[i].items():nxt[a+b]=nxt.get(a+b,0)+c*d
                    out=nxt
                return self.put(out)
            def plus(self,*ids):
                out={}
                for i in ids:
                    for w,c in self.nodes[i].items():out[w]=out.get(w,0)+c
                return self.put(out)
        r=Words()
        a=[[pc.Scalar(r.put({('a'+str(i)+str(j),):F(1)})) for j in range(2)] for i in range(2)]
        b=[[pc.Scalar(r.put({('b'+str(i)+str(j),):F(1)})) for j in range(2)] for i in range(2)]
        ab=pc.times(a,b,r);ba=pc.times(b,a,r)
        self.assertEqual(r.nodes[ab[0][1].node],{('a00','b01'):1,('a01','b11'):1})
        self.assertNotEqual(r.nodes[ab[0][1].node],r.nodes[ba[0][1].node])

    def test_substitution_chain_derivative_coefficients(self):
        r=pc.Ring('synthetic',pc.Budget())
        # e1^2*e2 at x2=x3=0 is (x+y)^2*x*y.
        n=r.times(r.power(r.elementary(1),2),r.elementary(2))
        dx=r.partial(n,0)
        for e,want in [((2,1,0,0),3),((1,2,0,0),4),((0,3,0,0),1),((0,0,0,0),0)]:
            self.assertEqual(r.coefficient(dx,e),want)

    def test_catalog_opcode_recording_on_fabricated_entries(self):
        # Record method calls only: no actual model entry or polynomial ring.
        class Recorder:
            def const(self,c):return ('constant',F(c))
            def elementary(self,k):return ('elementary',k)
            def times(self,*a):return ('times',*a)
            def plus(self,*a):return ('plus',*a)
            def power(self,a,n):return ('power',a,n)
        r=Recorder();v=[r.elementary(k) for k in range(5)]
        charts=[{'I':[[[['2,1,0,0',3]]]],'P':[[[]]]} for _ in range(6)]
        cat=pc.Catalog('physical',charts)  # fabricated entries, inert recorder
        for c in range(6):
            owner=pb.FullOwner(1,str(c),c,0,0)
            h=r.times(v[1],v[3],v[4]) if c==5 else r.plus(r.power(v[c],5),r.times(r.const(-1),*v))
            self.assertEqual(cat.H(owner,r),h)
            multiplier=r.times(r.const(-1),v[3],v[4]) if c==5 else r.times(r.const(-1),h)
            numerator=r.plus(r.times(r.const(3),r.power(v[1],2),r.power(v[2],1)))
            self.assertEqual(cat.cleared(owner,'I',r)[0][0].node,r.times(multiplier,numerator))

    def test_binding_never_constructs_catalog_or_ring(self):
        with patch.object(pc,'Catalog',side_effect=RuntimeError('Catalog forbidden')), patch.object(pc,'Ring',side_effect=RuntimeError('Ring forbidden')):
            b=pb.ActualPBinding(REPO)
            self.assertEqual(len(b.describe(owner_triple())['program']['dag']),153)

    def test_exact_primitive_metadata_and_hidden_v0(self):
        model=json.loads(RAW[pb.MODEL]);bridges=self.binding.describe(owner_triple())['primitive_bridges']
        for c,chart in enumerate(model['charts']):
            expected={'2,0,1,1':-1} if c==5 else {'1,1,1,1':1,','.join(str(5 if i==c-1 else 0) for i in range(4)):-1}
            for den in ('di','dp'):self.assertEqual(dict(chart[den]),expected)
            for entry in bridges[c]['entry_degrees']:
                w=entry['column'] if entry['block']=='I' else -entry['row']
                self.assertEqual(entry['weight'],w)
                self.assertEqual(entry['stored_numerator_homogenization_degree'],(6 if c==5 else 5)+w)
                for key,_ in chart[entry['block']][entry['row']][entry['column']]:
                    degree=sum(map(int,key.split(',')))
                    self.assertLessEqual(degree,(6 if c==5 else 5)+w)
                    affine_den_degree=4 if c in (0,5) else 5
                    padding=max(0,degree-affine_den_degree-w)
                    self.assertLessEqual(padding,2 if c==5 else 1 if c==0 else 0)
        self.assertEqual(bridges[5]['homogeneous_H'],'v0*v1*v3*v4')
        bad=copy.deepcopy(model);bad['charts'][5]['di']=[['2,0,1,1',1]]
        with self.assertRaises(ValueError):pb._primitive_bridges(bad)

    def test_degrees_order_axes_and_fixed_tags(self):
        oo=(pb.FullOwner(9,'u',5,15,3),pb.FullOwner(9,'a',1,1,12),pb.FullOwner(9,'b',1,4,7))
        for pair in ((0,1),(2,3)):
            d=self.binding.describe(oo,pair)
            expected=tuple(sum(14*(4 if o.carrier==5 else 5)+(1+2*((o.legal_mask>>i)&1) if i in pair else 0) for o in oo)-(2 if i in pair else 0) for i in range(4))
            self.assertEqual(tuple(d['P_homogeneous_multidegree']),expected)
            self.assertEqual(d['ordered_owners'],[list(o.data()) for o in oo])
            self.assertFalse(d['physical_Q_is_gerbe_q'])
            self.assertFalse(d['representation_chart_transition']['owner_tags_reassigned'])
        a=self.binding.symbolic_program_definition()['dag'];b=self.binding.symbolic_program_definition((2,3))['dag']
        self.assertEqual(b,sp.pair_nodes(a,(2,3)))
        sigma=(2,3,0,1)
        for old,new in zip(a,b):
            expected=copy.deepcopy(old)
            if old[0]=='owned_polynomial_factor' and old[1][1]=='ell':expected[1][2]=sigma[old[1][2]]
            elif old[0]=='mask_times_x_squared_plus_one_over_two':expected[2]=sigma[old[2]]
            elif old[0]=='binary_mask_q_numerator':expected[3]=sigma[old[3]]
            elif old[0]=='polynomial_partial_after_elementary_substitution':expected[2]=sigma[old[2]]
            self.assertEqual(new,expected)
        masks=(1,2,4);rot=lambda m:((m&3)<<2)|(m>>2)
        self.assertNotEqual(tuple(rot(m) for m in masks),tuple(sorted(rot(m) for m in masks)))

    def test_guards_copies_and_unconditional_refusal(self):
        b=self.binding;oo=owner_triple()
        self.assertEqual(list(inspect.signature(pb.ActualPBinding).parameters),['repo'])
        for kw in ('catalog','callback','mode','status','source_graph'):
            with self.assertRaises(TypeError):pb.ActualPBinding(**{kw:True})
        bads=[oo[::-1],oo[:2],tuple(o.data() for o in oo),
              (oo[0],pb.FullOwner(72,'x',1,2,14),oo[2]),
              (oo[0],pb.FullOwner(71,oo[0].occurrence,1,2,14),oo[2]),
              (oo[0],pb.FullOwner(71,'x',0,1,15),oo[2])]
        for owners in bads:
            for method in (b.describe,b.degree_upper):
                with self.assertRaises(ValueError):method(owners)
        for pair in ((1,0),(3,2),(False,1),(0,True),(0,2),'01'):
            with self.assertRaises(ValueError):b.symbolic_program_definition(pair)
        same=(pb.FullOwner(1,'a',0,0,0),pb.FullOwner(1,'b',0,0,1),pb.FullOwner(1,'c',1,0,0))
        self.assertTrue(b.describe(same)['source_order']['repeated_physical_source_labels_zero'])
        original=b.describe(oo)
        altered=b.describe(oo);altered['program']['dag'].clear();altered['primitive_bridges'].clear();altered['proof_dependencies'].clear()
        altered['ordered_owners'][0][2]=5
        b.source_pins()['sources'].clear();b.symbolic_program_definition()['dag'].clear()
        self.assertEqual(b.describe(oo),original)
        with self.assertRaises(AttributeError):b.mode='synthetic'
        b.__dict__['mode']='synthetic';b.__dict__['physical_execution_admitted']=True
        for method in (b.coefficient,b.alternating_coefficient):
            for args,kw in [((),{}),((oo,(-10**100,0,0,0)),{}),((None,),{'pair':'bad','mode':'synthetic'}),((object(),),{'status':True})]:
                with self.assertRaises(pb.PhysicalAdmissionMissing):method(*args,**kw)

    def test_byte_mutations_fail_closed(self):
        pins=json.loads((HERE/'source-pins.json').read_bytes())
        bykey={(r['commit'],r['path']):RAW[r['path']] for r in pins['sources']}
        for row in pins['sources']:
            key=(row['commit'],row['path'])
            def reader(rev,path):return bykey[(rev,path)]+(b' ' if (rev,path)==key else b'')
            with self.assertRaisesRegex(ValueError,'source bytes drift'):pb._authenticate(REPO,reader)

if __name__=='__main__':unittest.main()
