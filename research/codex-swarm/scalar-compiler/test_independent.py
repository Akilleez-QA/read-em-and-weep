"""SC-R independent tiny formal controls. No physical model imports or scans."""
import hashlib
import copy
import importlib.util
import itertools
import json
from pathlib import Path
import subprocess
import unittest
from fractions import Fraction as Q

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PIN = '10810ee877fdaf291399198ad60d7dd0c316a42d'
OLD = '08b73637d4136f91606aad332c46cafd064417f8'
Z = (0, 0, 0, 0)
SOURCE_PINS = {
    (PIN,'research/hm/null-proof-foundations/direct-scalar-free-pairing-reduction.md'):'246b7265f4f8936bf5cc2bfd9f0f7505f119d4b3515acdd82822f7d45c0c4d00',
    (PIN,'research/hm/null-proof-foundations/hm-regular-cover-transport.md'):'98a10d3da934ef5b6dfe1e2cf6af4ac46fcf6347e0e6081a8c0cbd58b2f7f02d',
    (PIN,'research/hm/null-proof-foundations/transposed-scalar-demand-grammar.md'):'bcc18aff1cd807fae12093d9d2cc6271fb505b9151e28ab524a903114010d87b',
    (PIN,'research/hm/null-source-integration/combined-pole/PROOF.md'):'03673d6f120cb0b89d6d3887b7ab0bfee6aa33acf2abcc0ddbb116071b159c25',
    (PIN,'research/hm/null-source-integration/order-comparison/source-order-curvature-comparison.md'):'c8dc3acbda9bcfc80317116ff2ff400e275ecf82a18f5321479c936d3c109451',
    (OLD,'research/hm/current-scalar-geometric-dependencies/data/source-formulas.js'):'c4f65ff831092d0e56b3e33a0357f44182169fda45943ea780c8c551b4023f94',
    (OLD,'research/hm/current-scalar-geometric-dependencies/frames-and-poles.md'):'876cad001a8f96bb207ca246873e3efe67afd9a394cc4d2a0796992596b84916',
    (OLD,'research/hm/current-scalar-residual-attribution/closure-and-characters.md'):'434aa106d0780f6eeef956335cc207a8b436d35db52f515f52bb5d49204292a2',
    (OLD,'research/hm/current-scalar-proof/map-and-comparison.md'):'777a11e0e82ca5de557d1b756e9ce7535836a0ff4cc34ee6e50712e23f788e72',
}


class P(dict):
    """Sparse polynomial, deliberately independent of producer arithmetic."""
    def __init__(self, value=0):
        super().__init__({m: Q(c) for m, c in value.items() if c} if isinstance(value, dict)
                         else ({Z: Q(value)} if value else {}))
    def __add__(self, other):
        out = dict(self)
        for m, c in P(other).items(): out[m] = out.get(m, 0) + c
        return P(out)
    __radd__ = __add__
    def __neg__(self): return P({m: -c for m, c in self.items()})
    def __sub__(self, other): return self + -P(other)
    def __rsub__(self, other): return P(other) + -self
    def __mul__(self, other):
        out = {}
        for m, c in self.items():
            for n, d in P(other).items():
                k = tuple(a+b for a,b in zip(m,n)); out[k] = out.get(k,0)+c*d
        return P(out)
    __rmul__ = __mul__
    def d(self, i):
        return P({tuple(v-(j==i) for j,v in enumerate(m)): c*m[i]
                  for m,c in self.items() if m[i]})


def mat(a): return tuple(tuple(P(x) for x in row) for row in a)
I = mat(((1,0),(0,1)))
O = mat(((0,0),(0,0)))
def add(*args): return tuple(tuple(sum((a[i][j] for a in args),P()) for j in range(2)) for i in range(2))
def scale(a,c): return tuple(tuple(x*c for x in row) for row in a)
def mul(a,b): return tuple(tuple(sum((a[i][k]*b[k][j] for k in range(2)),P()) for j in range(2)) for i in range(2))
def inv(a): return ((a[1][1],-a[0][1]),(-a[1][0],a[0][0]))
def tr(a): return a[0][0]+a[1][1]
def tf(a): return add(a,scale(I,-Q(1,2)*tr(a)))
def der(a,i): return tuple(tuple(x.d(i) for x in row) for row in a)
def trans(a): return tuple(zip(*a))
def mu(a,b,p):
    i,j=p
    return scale(add(mul(der(a,i),der(b,j)),scale(mul(der(a,j),der(b,i)),-1)),Q(1,2))
def mu2(a,b):
    out=O
    for i,j,s in ((0,1,1),(1,0,-1)):
        for k,l,t in ((2,3,1),(3,2,-1)):
            out=add(out,scale(mul(der(der(a,i),k),der(der(b,j),l)),Q(s*t,4)))
    return out
def upper(x): return mat(((1,x),(0,1)))
def lower(x): return mat(((1,0),(x,1)))


class IndependentMath(unittest.TestCase):
    def test_exact_source_pins(self):
        for (pin,path),sha in SOURCE_PINS.items():
            with self.subTest(path=path):
                raw=subprocess.check_output(['git','show',pin+':'+path],cwd=ROOT)
                self.assertEqual(hashlib.sha256(raw).hexdigest(),sha)

    def test_end_homotopy_all_homogeneous_matrix_units(self):
        # Five-dimensional artificial split complex, one cohomology generator.
        degrees=(0,1,1,1,2); n=len(degrees)
        def zero(): return [[Q(0) for _ in range(n)] for _ in range(n)]
        def plus(a,b): return [[a[i][j]+b[i][j] for j in range(n)] for i in range(n)]
        def times(a,b): return [[sum(a[i][k]*b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
        def sc(a,c): return [[v*c for v in row] for row in a]
        d=zero(); d[1][0]=d[4][3]=1
        h=zero(); h[0][1]=h[3][4]=1
        e=zero(); e[2][2]=1
        def differential(f,r): return plus(times(d,f),sc(times(f,d),-(-1)**r))
        def H(f,r): return plus(times(h,f),sc(times(times(e,f),h),(-1)**r))
        negatives=0
        for i,j in itertools.product(range(n),repeat=2):
            f=zero(); f[i][j]=1; r=degrees[i]-degrees[j]
            lhs=plus(differential(H(f,r),r-1),H(differential(f,r),r+1))
            rhs=plus(f,sc(times(times(e,f),e),-1))
            self.assertEqual(lhs,rhs)
            wrong=plus(differential(H(f,0),r-1),H(differential(f,r),0))
            negatives+=wrong!=rhs
        self.assertGreater(negatives,0)

    def test_frozen_endpoint_value_does_not_freeze_frame_jets(self):
        # D(0)=I but D'(0)=S. d(D A D^-1)|0=[S,A].
        a=upper(P(1)); s=mat(((1,0),(0,-1)))
        frame_derivative=add(mul(s,a),scale(mul(a,s),-1))
        self.assertNotEqual(frame_derivative,O)
        self.assertEqual(frame_derivative,mat(((0,2),(0,0))))

    def test_lift_signs_on_varying_local_contractions(self):
        # Cech cochains on six vertices, with distinct local SDRs of one complex.
        n=5
        def zero(): return [[Q(0) for _ in range(n)] for _ in range(n)]
        def plus(a,b): return [[a[i][j]+b[i][j] for j in range(n)] for i in range(n)]
        def sc(a,c): return [[x*c for x in row] for row in a]
        def times(a,b): return [[sum(a[i][k]*b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
        d=zero(); d[1][0]=d[4][3]=1
        def end(f,r): return plus(times(d,f),sc(times(f,d),-(-1)**r))
        es=[]; hs=[]
        for a in range(6):
            t=Q(a+1); u=Q(a*a+1)
            iv=[0,t,1,0,0]; pv=[0,0,1,u,0]
            e=[[iv[i]*pv[j] for j in range(n)] for i in range(n)]
            h=zero(); h[0][1]=1; h[0][2]=-t
            h[3][4]=1; h[1][4]=-u*t; h[2][4]=-u
            es.append(e); hs.append(h)
        def H(f,r,a): return plus(times(hs[a],f),sc(times(times(es[a],f),hs[a]),(-1)**r))
        def delta(c,tu):
            out=zero()
            for i in range(len(tu)): out=plus(out,sc(c[tu[:i]+tu[i+1:]],(-1)**i))
            return out
        # Scalar R is a closed, nonzero 2-coboundary; only its formal values enter.
        edge=lambda a,b: Q((a+1)*(b+2)**2)
        j0={tu:sc(es[tu[0]],edge(tu[1],tu[2])-edge(tu[0],tu[2])+edge(tu[0],tu[1]))
            for tu in itertools.combinations(range(6),3)}
        js=[j0]
        for level,sign in ((1,1),(2,-1),(3,1)):
            js.append({tu:sc(H(delta(js[-1],tu),1-level,tu[0]),sign)
                       for tu in itertools.combinations(range(6),level+3)})
        self.assertTrue(any(v!=zero() for v in js[1].values()))
        self.assertTrue(any(v!=zero() for v in js[2].values()))
        for level in range(1,4):
            for tu,value in js[level].items():
                self.assertEqual(delta(js[level-1],tu),sc(end(value,-level),(-1)**(level+1)))
        self.assertTrue(all(end(f,0)==zero() for f in js[0].values()))

    def test_complete_source_identity_on_artificial_sl2_polynomials(self):
        x=[P({tuple(int(i==j) for j in range(4)):1}) for i in range(4)]
        A=mul(upper(x[0]+x[2]),lower(x[1]))
        B=mul(upper(x[3]),lower(x[0]*x[2]+x[1]))
        G=mul(B,A); gs=(A,B,G); pairs=((0,1),(2,3))
        self.assertEqual(mul(inv(G),G),I)
        ks=[[scale(mu(inv(g),g,p),-Q(1,2)) for g in gs] for p in pairs]
        cs=[mul(inv(G),mu(B,A,p)) for p in pairs]
        for k,c in zip(ks,cs):
            delta=add(mul(mul(inv(A),k[1]),A),scale(k[2],-1),k[0])
            self.assertEqual(delta,scale(tf(c),-1))
        sp=(x[0]*x[3]+1,x[1]+x[2],x[0]-x[2]*x[3])
        sq=(x[1]*x[2],x[3]+2,x[0]*x[1]+x[2])
        ss=(sp,sq); fs=[s[1]-s[2]+s[0] for s in ss]
        bs=[f+Q(1,2)*tr(c) for f,c in zip(fs,cs)]
        def residual(use_scalars, gerbe=True):
            us=[[mul(g,add(k,scale(I,s if use_scalars else 0)))
                 for g,k,s in zip(gs,kk,sc)] for kk,sc in zip(ks,ss)]
            up,uq=us
            out=add(mul(up[1],uq[0]),mul(uq[1],up[0]),mu2(B,A))
            for u,p in ((uq,pairs[0]),(up,pairs[1])):
                out=add(out,mu(u[1],A,p),mu(B,u[0],p))
            if gerbe: out=add(out,scale(uq[2],-bs[0]),scale(up[2],-bs[1]),scale(G,-bs[0]*bs[1]))
            return mul(inv(G),out)
        def directional(p,s):
            a,b=p; L=[mul(inv(A),der(A,d)) for d in p]
            U=[mul(mul(mul(inv(A),inv(B)),der(B,d)),A) for d in p]
            return scale(add(scale(L[1],s[1].d(a)),scale(L[0],-s[1].d(b)),
                             scale(U[0],s[0].d(b)),scale(U[1],-s[0].d(a))),Q(1,2))
        W=[add(scale(ks[0][i],sq[i]),scale(ks[1][i],sp[i])) for i in range(3)]
        dw=add(mul(mul(inv(A),W[1]),A),scale(W[2],-1),W[0])
        rsharp=add(tf(residual(False)),scale(ks[0][2],fs[1]),scale(ks[1][2],fs[0]),
                   directional(pairs[0],sq),directional(pairs[1],sp))
        self.assertEqual(tf(residual(True)),add(rsharp,scale(dw,-1)))
        self.assertNotEqual(tf(residual(False)),tf(residual(False,False)))
        self.assertNotEqual(mul(A,B),mul(B,A))
        self.assertEqual(trans(mul(A,B)),mul(trans(B),trans(A)))

    def test_moyal_square_has_two_cross_orders(self):
        # Expansion of (P12+P34)^2/8: each mixed orientation occurs twice.
        cross={}
        terms=((0,1,1),(1,0,-1),(2,3,1),(3,2,-1))
        for a,b,s in terms:
            for c,d,t in terms:
                if (a<2)!=(c<2):
                    key=(tuple(sorted((a,c))),tuple(sorted((b,d))))
                    cross[key]=cross.get(key,0)+Q(s*t,8)
        self.assertEqual(cross,{((0,2),(1,3)):Q(1,4),((0,3),(1,2)):-Q(1,4),
                                ((1,2),(0,3)):-Q(1,4),((1,3),(0,2)):Q(1,4)})

    def test_derivative_adjoint_convolution_including_zero(self):
        # Independent forward Laurent products versus reverse demand.
        f={-4:2,-1:3,0:7,2:-5}; w={-2:4,0:-2,3:6}
        for k in range(-8,8):
            forward=sum(a*b*j for i,a in w.items() for j,b in f.items() if i+j-1==k)
            reverse=sum(a*(k-i+1)*f.get(k-i+1,0) for i,a in w.items())
            self.assertEqual(forward,reverse)
        self.assertEqual(sum(b*j for j,b in f.items() if j-1==-1),0)

    def test_weighted_requests_by_counting_labelled_factors(self):
        raw=json.loads((HERE.parent/'detector-selection/weighted-requests.json').read_text())
        self.assertEqual(len(raw['requests']),32)
        base=[r for r in raw['requests'] if r['block']=='Q^2']
        expected_rows={(i,0) for i in range(5,11)}|{(i,1) for i in range(15) if i!=5}
        self.assertEqual({(r['scalar_map']['i'],r['scalar_map']['b']) for r in base},expected_rows)
        self.assertEqual([sum(r['block']==b for r in raw['requests'])
                          for b in ('Q^2','v_k Q','v_k v_l')],[20,10,2])
        for req in raw['requests']:
            block=req['block']; base=req['base_monomial']
            # Labelled subsets counted directly; no producer polynomial multiply.
            factors=([[(0,1),(2,3)]]*2 if block=='Q^2' else
                     [[s for s in itertools.combinations(range(4),base[0])],[(0,1),(2,3)]]
                     if block=='v_k Q' else
                     [[s for s in itertools.combinations(range(4),k)] for k in base])
            expected={}
            for choices in itertools.product(*factors):
                m=tuple(sum(i in s for s in choices) for i in range(4))
                expected[m]=expected.get(m,0)+1
            actual={tuple(t['dual_monomial']):t['coefficient'] for t in req['terms']}
            self.assertEqual(actual,expected)
            for t in req['terms']:
                m=t['dual_monomial']
                self.assertEqual(t['laurent_exponents'],[-v-1 for v in m])
                self.assertEqual(t['output_index'],int(''.join(str(2-v) for v in m),3))


# Producer-facing checks below retain the eight source-independent controls above.
# All evaluations here are artificial polynomial assignments, never source leaves.
spec = importlib.util.spec_from_file_location('reviewed_compiler', HERE/'compiler.py')
C = importlib.util.module_from_spec(spec)
spec.loader.exec_module(C)


def peval(nodes, root, leaves, solvers, cache=None):
    cache = {} if cache is None else cache
    if root in cache: return cache[root]
    n = nodes[root]; op = n['op']
    if op == 'leaf': out = leaves(n)
    elif op == 'physical_jet':
        out = leaves(nodes[n['children'][0]])
        for d in n['directions']: out = tuple(tuple(x.d(d) for x in row) for row in out)
    elif op == 'complete_inner_solver': out = ((solvers(n),),)
    elif op == 'differentiate_combined_solver': out = ((solvers(nodes[n['children'][0]]).d(n['direction']),),)
    elif op == 'identity': out = I
    else:
        a = [peval(nodes,k,leaves,solvers,cache) for k in n['children']]
        if op == 'add': out = tuple(tuple(sum((v[i][j] for v in a),P()) for j in range(n['shape'][1])) for i in range(n['shape'][0]))
        elif op == 'rational_scale': out = tuple(tuple(x*Q(*n['coefficient']) for x in row) for row in a[0])
        elif op == 'matrix_product':
            out = a[0]
            for b in a[1:]:
                out = tuple(tuple(sum((out[i][k]*b[k][j] for k in range(len(b))),P()) for j in range(len(b[0]))) for i in range(len(out)))
        elif op == 'matrix_inverse': out = inv(a[0])
        elif op == 'scalar_times_matrix': out = tuple(tuple(x*a[0][0][0] for x in row) for row in a[1])
        elif op == 'trace': out = ((tr(a[0]),),)
        elif op == 'transpose': out = trans(a[0])
        else: raise ValueError(op)
    cache[root] = out
    return out


class IndependentAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.t = json.loads((HERE/'compiled-template.json').read_text())
        _, cls.model, cls.shared, cls.weights = C.authenticate()

    def reject(self, mutate):
        bad = copy.deepcopy(self.t); mutate(bad)
        with self.assertRaises(ValueError): C.validate_template(bad)

    def test_handoff_and_additional_transport_pin(self):
        marker = json.loads((HERE/'producer-ready.json').read_text())
        for name, rec in marker['files'].items():
            # Reserved reviewer outputs necessarily change during this review.
            if name in ('test_independent.py','review-independent.md'): continue
            raw = (HERE/name).read_bytes()
            self.assertEqual((len(raw),hashlib.sha256(raw).hexdigest()),(rec['bytes'],rec['sha256']))
        raw = subprocess.check_output(['git','show','43193bc8badf3f29a1363132135d956cc12d46ad:research/hm/null-source-integration/scalar-family-transport/PROOF.md'],cwd=ROOT)
        self.assertEqual(hashlib.sha256(raw).hexdigest(),'e0fac7c2a2564dd1521a6055238e175fcf83e11e1b4bf9302eacad13ed040db3')

    def test_every_actual_node_and_physical_leaf_binding(self):
        nodes = self.t['nodes']; self.assertEqual(len(nodes),4270)
        for j,n in enumerate(nodes):
            self.assertTrue(all(type(k) is int and 0<=k<j for k in n['children']))
            self.assertTrue(all(type(x) is int and x>0 for x in n['shape']))
            if n['op']=='matrix_product':
                shapes=[nodes[k]['shape'] for k in n['children']]
                self.assertTrue(all(a[1]==b[0] for a,b in zip(shapes,shapes[1:])))
                self.assertEqual(n['shape'],[shapes[0][0],shapes[-1][1]])
            if n['op']=='physical_jet':
                base=nodes[n['children'][0]]
                self.assertEqual(base['op'],'leaf'); self.assertTrue(n['frames_differentiated'])
                self.assertEqual(n['directions'],sorted(n['directions']))
                self.assertTrue(all(type(d) is int and 0<=d<4 for d in n['directions']))
            if n['op']=='differentiate_combined_solver':
                solver=nodes[n['children'][0]]
                self.assertEqual(solver['op'],'complete_inner_solver')
                self.assertNotIn(n['direction'],solver['pair'])
                self.assertFalse(n['actual_source_clearing_witness'])
            if n['op']=='complete_inner_solver':
                self.assertEqual(n['partition'],{'carrier':14,'legal':1,'pair_specific':True})
                branches=[nodes[k] for k in n['children']]
                self.assertEqual([b['op'] for b in branches],['N14_Hrho','N14_R_Kcov_Pi','N14_R_A_h_S_Pi'])
                self.assertEqual([nodes[k]['sign'] for k in branches[0]['children']],[1,-1])
            if n['op']=='finite_outer_cover_transport':
                self.assertEqual(n['partition'],{'carrier':54,'legal':29})
                self.assertEqual(n['standard_unit_order'],5251)
                self.assertEqual(len(n['common_fibers']),5)
                self.assertEqual(len(n['staircases']),24)
                for staircase in n['staircases']:
                    perm=staircase['coordinate_order']; tags=[0]
                    for d in perm: tags.append(tags[-1]+2**(3-d))
                    sign=(-1)**sum(a>b for i,a in enumerate(perm) for b in perm[i+1:])
                    self.assertEqual(staircase['standard_tags'],tags)
                    self.assertEqual(staircase['orientation'],sign)
            if n['op']=='leaf':
                if n['name']=='g_phys':
                    self.assertEqual(n['shape'],[2,2]); self.assertEqual(len(n['owners']),2)
                    self.assertIn('complete moving frame',n['frame'])
                elif n['name']=='physical_q':
                    self.assertEqual(n['shape'],[1,1]); self.assertEqual(len(n['owners']),2)
                    self.assertIn(n['coordinate'],range(4))
                else:
                    self.assertIn(n['name'],('I_phys','P_phys','H0','H1','eta'))
                    self.assertEqual(n['frame'],'original fixed resolution')
        for r in self.t['source_residual_components']:
            self.assertEqual(set(r['components']),{'baseline','Fk12','Fk34','E12','E34'})
            self.assertEqual(len(r['baseline']['kinetic_terms']),7)
            self.assertEqual(len(r['baseline']['gerbe_terms']),3)

    def test_source_API_against_independent_polynomial_formula(self):
        x=[P({tuple(int(i==j) for j in range(4)):1}) for i in range(4)]
        A=mul(upper(x[0]+x[2]),lower(x[1])); B=mul(upper(x[3]),lower(x[0]*x[2]+x[1])); G=mul(B,A)
        edges=((0,1),(1,2),(0,2)); gs=dict(zip(edges,(A,B,G))); pairs=((0,1),(2,3))
        ss={(0,1):(x[0]*x[3]+1,x[1]+x[2],x[0]-x[2]*x[3]),(2,3):(x[1]*x[2],x[3]+2,x[0]*x[1]+x[2])}
        qs={(e,d):x[d]+(i+1)*(d+2) for i,e in enumerate(edges) for d in range(4)}
        def leaf(n):
            e=tuple(n['owners'])
            return gs[e] if n['name']=='g_phys' else ((qs[e,n['coordinate']],),)
        def solver(n): return ss[tuple(n['pair'])][edges.index(tuple(n['owners']))]
        c=C.Circuit(); src=C.Source(c); root=src.residual((0,1,2))
        ks=[[scale(mu(inv(g),g,p),-Q(1,2)) for g in (A,B,G)] for p in pairs]
        bs=[qs[(0,1),p[0]]*qs[(1,2),p[1]]*Q(15,4) for p in pairs]
        fs=[b-Q(1,2)*tr(mul(inv(G),mu(B,A,p))) for b,p in zip(bs,pairs)]
        up,uq=[[mul(g,k) for g,k in zip((A,B,G),kk)] for kk in ks]
        raw=add(mul(up[1],uq[0]),mul(uq[1],up[0]),mu2(B,A),mu(uq[1],A,pairs[0]),mu(up[1],A,pairs[1]),mu(B,uq[0],pairs[0]),mu(B,up[0],pairs[1]),scale(uq[2],-bs[0]),scale(up[2],-bs[1]),scale(G,-bs[0]*bs[1]))
        def correction(p,s):
            a,b=p
            L=lambda d:mul(inv(A),der(A,d))
            U=lambda d:mul(mul(mul(inv(A),inv(B)),der(B,d)),A)
            return scale(add(scale(L(b),s[1].d(a)),scale(L(a),-s[1].d(b)),scale(U(a),s[0].d(b)),scale(U(b),-s[0].d(a))),Q(1,2))
        expected={'baseline':tf(mul(inv(G),raw)),'Fk12':scale(ks[0][2],fs[1]),'Fk34':scale(ks[1][2],fs[0]),'E12':correction(pairs[0],ss[pairs[1]]),'E34':correction(pairs[1],ss[pairs[0]])}
        for name,n in src.components[(0,1,2)].items(): self.assertEqual(peval(c.nodes,n,leaf,solver),expected[name],name)
        self.assertEqual(peval(c.nodes,root,leaf,solver),add(*expected.values()))
        changed=copy.deepcopy(c.nodes)
        for n in changed:
            if n['op']=='matrix_product': n['children'].reverse()
        self.assertNotEqual(peval(changed,root,leaf,solver),add(*expected.values()))
        self.assertNotEqual(expected['baseline'],tf(mul(inv(G),add(raw,scale(uq[2],bs[0]),scale(up[2],bs[1]),scale(G,bs[0]*bs[1])))))

    def test_actual_J0_through_J3_by_independent_free_algebra(self):
        # Free words retain prefix owners even after Cech face deletion.
        nodes=self.t['nodes']; cache={}
        residuals={tuple(r['owners']):r['components'] for r in self.t['source_residual_components']}
        def plus(*ps):
            out={}
            for p in ps:
                for w,z in p.items(): out[w]=out.get(w,0)+z
            return {w:z for w,z in out.items() if z}
        def sc(p,z): return {w:v*z for w,v in p.items() if v*z}
        def times(*ps):
            out={():Q(1)}
            for p in ps:
                out=plus(*({a+b:x*y} for a,x in out.items() for b,y in p.items()))
            return out
        atom=lambda name,owner:{((name,owner),):Q(1)}
        roots={}
        # JSON key sorting changes dict order; use sets for source branch matching.
        for j,n in enumerate(nodes):
            if n['op']=='add':
                for owners,parts in residuals.items():
                    if len(n['children'])==5 and set(n['children'])==set(parts.values()): roots[j]=owners
        def actual(j):
            if j in cache:return cache[j]
            n=nodes[j]; op=n['op']
            if op=='leaf': out=atom(n['name'],n['owner'])
            elif op=='transpose' and n['children'][0] in roots:out=atom('Rt',roots[n['children'][0]])
            elif op=='matrix_product':out=times(*(actual(k) for k in n['children']))
            elif op=='add':out=plus(*(actual(k) for k in n['children']))
            elif op=='rational_scale':out=sc(actual(n['children'][0]),Q(*n['coefficient']))
            else:raise ValueError(op)
            cache[j]=out;return out
        def expected(stage,t):
            if stage==0:return {(1,1):times(atom('I_phys',t[0]),atom('Rt',t),atom('P_phys',t[0]))}
            faces={}
            for j in range(len(t)):
                for key,p in expected(stage-1,t[:j]+t[j+1:]).items():faces[key]=plus(faces.get(key,{}),sc(p,(-1)**j))
            out={}; r=1-stage; owner=t[0]
            def put(key,p):out[key]=plus(out.get(key,{}),sc(p,(-1 if stage==2 else 1)))
            for (u,v),p in faces.items():
                if v>0:put((u,v-1),times(atom(('H0','H1','eta')[v-1],owner),p))
                if v==1 and u<3:put((u+1,v),sc(times(atom('I_phys',owner),atom('P_phys',owner),p,atom(('H0','H1','eta')[u],owner)),(-1)**r))
            return out
        for stage in range(4):
            self.assertEqual({tuple(b['block']):actual(b['matrix']) for b in self.t['lift_components']['J'+str(stage)]},expected(stage,tuple(range(stage+3))))

    def test_constant_rows_directly_from_pinned_gamma_and_actual_demands(self):
        # Decode the pinned polynomial independently; never call gamma_coefficients.
        gamma={}
        for i,row in enumerate(self.model['gamma']):
            for a,poly in enumerate(row):
                for key,z in poly:
                    e=tuple(map(int,key.split(','))); k=0 if not any(e) else 1+e.index(1)
                    gamma[i,a,k]=gamma.get((i,a,k),0)+z
        nodes=self.t['nodes']; j2={tuple(b['block']):b['matrix'] for b in self.t['lift_components']['J2']}
        for row in self.t['scalar_templates']:
            i,b=row['i'],row['b']; expected=[{'block':[3,1],'entry':[i,b],'coefficient':1}]
            expected += [{'block':[2,0],'entry':[a,5*b+k],'coefficient':-gamma[i,a,k]} for a in range(5) for k in range(5) if gamma.get((i,a,k),0)]
            self.assertEqual(row['constant_terms'],expected)
            root=nodes[row['J2_scalar_circuit']]; kids=root['children'] if root['op']=='add' else [row['J2_scalar_circuit']]
            actual=[]
            for k in kids:
                n=nodes[k]; z=Q(1)
                if n['op']=='rational_scale':z=Q(*n['coefficient']); n=nodes[n['children'][0]]
                self.assertEqual(n['op'],'entry'); block=next(key for key,v in j2.items() if v==n['children'][0])
                actual.append({'block':list(block),'entry':n['entry'],'coefficient':z})
            self.assertEqual(actual,expected)
        actual=[]
        def expand(j,z=Q(1)):
            n=nodes[j]
            if n['op']=='add':return sum((expand(k,z) for k in n['children']),[])
            if n['op']=='rational_scale':return expand(n['children'][0],z*Q(*n['coefficient']))
            self.assertEqual(n['op'],'Laurent_coefficient')
            transport=nodes[n['children'][0]]; self.assertEqual(transport['op'],'finite_outer_cover_transport')
            return [(transport['children'][0],tuple(n['exponent']),n['output_index'],z)]
        rows={(r['i'],r['b']):r['J2_scalar_circuit'] for r in self.t['scalar_templates']}
        for r,w in zip(self.t['requests'],self.weights['requests']):
            self.assertEqual(r['weighted_request'],w)
            key=(w['scalar_map']['i'],w['scalar_map']['b']); terms=expand(r['compiled_output'])
            self.assertEqual(terms,[(rows[key],tuple(t['laurent_exponents']),t['output_index'],t['coefficient']) for t in w['terms']])
            actual.extend((key,e) for _,e,_,_ in terms)
        self.assertEqual(len(actual),127); self.assertEqual(len(set(actual)),121)

    def test_reject_missing_branches_top_wrong_signs_products_and_owners(self):
        mutations=[lambda t:t['lift_components'].pop('J3'),lambda t:t['source_residual_components'][0]['components'].pop('E34'),lambda t:t['closure'].__setitem__('source_geometry_instantiated',True)]
        for op,field in [('matrix_product','children'),('rational_scale','coefficient'),('leaf','owners'),('physical_jet','frames_differentiated'),('finite_outer_cover_transport','partition')]:
            def mutate(t,op=op,field=field):
                n=next(n for n in t['nodes'] if n['op']==op and field in n and (field!='children' or n[field]!=list(reversed(n[field]))))
                if field=='children':n[field]=list(reversed(n[field]))
                elif field=='coefficient':n[field][0]*=-1
                elif field=='owners':n[field][0]='lost-owner'
                elif field=='partition':n[field]['carrier']=14
                else:n[field]=False
            mutations.append(mutate)
        def missing_actual_branch(t):
            parts=t['source_residual_components'][0]['components']
            n=next(n for n in t['nodes'] if n['op']=='add' and len(n['children'])==5 and set(n['children'])==set(parts.values()))
            n['children'].remove(parts['E34'])
        mutations.append(missing_actual_branch)
        def missing_actual_gerbe(t):
            gerbe=t['source_residual_components'][0]['baseline']['gerbe_terms']
            n=next(n for n in t['nodes'] if n['op']=='add' and all(g in n['children'] for g in gerbe))
            n['children'].remove(gerbe[2])
        mutations.append(missing_actual_gerbe)
        for name in ('physical_q','g_phys'):
            mutations.append(lambda t,name=name:next(n for n in t['nodes'] if n.get('name')==name).__setitem__('owners',['forged','owners']))
        for mutation in mutations:
            with self.subTest(mutation=repr(mutation)):self.reject(mutation)

    def test_all_physical_gates_and_false_admission_rejected(self):
        for key,value in self.t['gates'].items():
            if value is False:
                with self.subTest(gate=key):self.reject(lambda t,key=key:t['gates'].__setitem__(key,True))
        for op,flag in [('complete_inner_solver','actual_source_clearing_witness'),('differentiate_combined_solver','actual_source_clearing_witness'),('finite_outer_cover_transport','actual_domain_witness')]:
            ns=[n for n in self.t['nodes'] if n['op']==op]; self.assertTrue(ns)
            self.assertTrue(all(n[flag] is False for n in ns))
            self.reject(lambda t,op=op,flag=flag:next(n for n in t['nodes'] if n['op']==op).__setitem__(flag,True))

    def test_owner_API_preserves_occurrences_and_rejects_bad_integer_fields(self):
        tags=[0,8,12,14,15]; owners=[[0,j,1,0,t] for j,t in enumerate(tags)]
        out=C.bind_outer_assignment(tags,owners)
        self.assertFalse(out['zero']); self.assertEqual(out['partition_owners'],owners)
        for field in range(5):
            bad=copy.deepcopy(owners);bad[0][field]=False
            with self.subTest(field=field),self.assertRaises(ValueError):C.bind_outer_assignment(tags,bad)
        bad=copy.deepcopy(owners);bad[1][1]=0
        with self.assertRaises(ValueError):C.bind_outer_assignment(tags,bad)
        c=C.Circuit(); a=c.leaf('A',(2,2))
        for action in (lambda:C.scalar_terms([[[0]*5 for _ in range(5)] for _ in range(15)],True,0),lambda:c.D(a,False),lambda:c.entry(a,False,0),lambda:c.leaf('bad',(True,2))):
            with self.assertRaises(ValueError):action()

    def test_boolean_standard_tag_must_be_rejected(self):
        tags=[False,8,12,14,15];owners=[[0,j,1,0,int(t)] for j,t in enumerate(tags)]
        with self.assertRaises(ValueError):C.bind_outer_assignment(tags,owners)

    def test_boolean_bottom_selector_must_be_rejected(self):
        g=[[[0]*5 for _ in range(5)] for _ in range(15)]
        with self.assertRaises(ValueError):C.row_bottom_coefficients(g,[{'block':[2,0],'entry':[False,0],'coefficient':1}])


if __name__=='__main__': unittest.main(verbosity=2)

