"""CLR-R: metadata and artificial exact first-jet controls only.

Never evaluates a physical model polynomial. Run with PYTHONDONTWRITEBYTECODE=1.
"""
import importlib.util
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path
import subprocess
import unittest

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
PIN = '10810ee877fdaf291399198ad60d7dd0c316a42d'

def pinned(path):
    return subprocess.check_output(['git', 'show', PIN + ':' + path], cwd=REPO)

def producer():
    spec = importlib.util.spec_from_file_location('clr_producer', HERE / 'clearing.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

class J:
    """Two artificial first derivatives over exact rationals, not source jets."""
    def __init__(self, v, dx=0, dy=0): self.v, self.d = Q(v), (Q(dx), Q(dy))
    def __add__(self, b):
        b = lift(b); return J(self.v+b.v, *(a+c for a,c in zip(self.d,b.d)))
    __radd__ = __add__
    def __neg__(self): return J(-self.v, *(-a for a in self.d))
    def __sub__(self,b): return self+-lift(b)
    def __rsub__(self,b): return lift(b)+-self
    def __mul__(self,b):
        b=lift(b); return J(self.v*b.v, *(a*b.v+self.v*c for a,c in zip(self.d,b.d)))
    __rmul__=__mul__
    def __truediv__(self,b):
        b=lift(b); return J(self.v/b.v, *((a*b.v-self.v*c)/b.v**2 for a,c in zip(self.d,b.d)))
    def __pow__(self,n):
        if n == 0: return J(1)
        return J(self.v**n, *(n*self.v**(n-1)*a for a in self.d))

def lift(a): return a if isinstance(a,J) else J(a)
def mat(a): return isinstance(a,list)
def add(a,b):
    return [[add(x,y) for x,y in zip(r,s)] for r,s in zip(a,b)] if mat(a) else a+b
def mul(a,b):
    if mat(a) and mat(b):
        return [[sum((mul(a[i][k],b[k][j]) for k in range(2)),J(0)) for j in range(2)] for i in range(2)]
    if mat(a): return [[mul(x,b) for x in r] for r in a]
    if mat(b): return mul(b,a)
    return a*b
def trans(a): return [list(r) for r in zip(*a)]
def deriv(a,d): return [[deriv(x,d) for x in r] for r in a] if mat(a) else J(a.d[d])
def val(a): return [[val(x) for x in r] for r in a] if mat(a) else a.v
def inv(a): return [[a[1][1],-a[0][1]],[-a[1][0],a[0][0]]]

class Independent(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not (HERE/'producer-ready.json').exists():
            raise RuntimeError('Producer staging handoff required before final tests')
        cls.m=producer()
        cls.model=json.loads(pinned('research/hm/null-operator-compiler/hm-pinned-model.json'))

    def test_authentication_and_source_scope(self):
        model,pins=self.m.authenticate(REPO)
        self.assertEqual(model,self.model)
        # Independent expectations retained from staging's pinned-source notes.
        expected={
            'null-operator-compiler/hm-pinned-model.json':'635bb12d9986e0dcada161d4173c773c4f134b9225354a3bc74267840ca19926',
            'null-operator-compiler/hm-pinned-source-formulas.js':'c4f65ff831092d0e56b3e33a0357f44182169fda45943ea780c8c551b4023f94',
            'null-source-integration/combined-pole/PROOF.md':'03673d6f120cb0b89d6d3887b7ab0bfee6aa33acf2abcc0ddbb116071b159c25',
            'null-source-integration/combined-pole/certificate.py':'57fc3b13f0853a1364d2a5911884fe0d89bd3b287c9913bf2f377f24da0eff26',
            'null-support-certificates/pinned-homogeneous-identities.json':'55e78bbc838a971b64531379788192acf8877c04f2d797fb13b4f4a68e47b018',
            'null-source-integration/order-comparison/source-order-curvature-comparison.md':'c8dc3acbda9bcfc80317116ff2ff400e275ecf82a18f5321479c936d3c109451'}
        self.assertEqual(set(pins),{'research/hm/'+p for p in expected})
        for suffix,digest in expected.items():
            path='research/hm/'+suffix
            self.assertEqual(hashlib.sha256(pinned(path)).hexdigest(),digest,path)
            self.assertEqual(pins[path]['sha256'],digest,path)
        self.assertIn('research/hm/null-source-integration/order-comparison/source-order-curvature-comparison.md',pins)
        source=pinned('research/hm/null-operator-compiler/hm-pinned-source-formulas.js').decode()
        self.assertIn('bcoef=(i,j,k,a,b)=>mul(R(15n,4n),mul(q(i,j,a)[0],q(j,k,b)[0]))',source)
        self.assertIn('const core=mtimes(charts[i].P,charts[j].I)',source)
        self.assertIn('li=[ji(charts[i].nu),charts[i].nu],rj=[charts[j].nu,ji(charts[j].nu)]',source)

    def test_all_360_primitive_entries_are_polynomial_metadata(self):
        entries=0
        for carrier,chart in enumerate(self.model['charts']):
            for block,shape in [('I',(15,2)),('P',(2,15))]:
                self.assertEqual((len(chart[block]),len(chart[block][0])),shape)
                for r,row in enumerate(chart[block]):
                    for s,poly in enumerate(row):
                        entries+=1
                        for exponent,coefficient in poly:
                            es=list(map(int,exponent.split(',')))
                            self.assertEqual(len(es),4)
                            self.assertTrue(all(e>=0 for e in es))
                            self.assertIs(type(coefficient),int)
                            weight=s if block=='I' else -r
                            self.assertLessEqual(sum(es),(6 if carrier==5 else 5)+weight)
        self.assertEqual(entries,360)

    def test_six_literal_denominators_and_uniform_clearing(self):
        for c,chart in enumerate(self.model['charts']):
            expected={(1,1,1,1):1}
            if c==0: expected[(0,0,0,0)]=-1
            elif c<5: expected[tuple(5 if i==c-1 else 0 for i in range(4))]=-1
            else: expected={(2,0,1,1):-1}
            for name in ('di','dp'):
                self.assertEqual({tuple(map(int,e.split(','))):a for e,a in chart[name]},expected)
        catalog=self.m.primitive_catalog(self.model)
        self.assertEqual([c['cleared_primitive_multiplier'] for c in catalog],['-H']*5+['-v3*v4'])
        # Monomial auxiliary identity a²/(-v1*a)=-v3*v4, no evaluation.
        self.assertEqual(tuple(2*a-b for a,b in zip((1,0,1,1),(2,0,1,1))),(0,0,1,1))

    def test_mask_rewrite_all_four_cases(self):
        for x in (Q(2),Q(-3),Q(5,2)):
            for a in (0,1):
                for b in (0,1):
                    ell=lambda mask:x*(x*x-1) if mask else Q(1)
                    rewrite=b*(1-a)*(x*x-1)/ell(b)-a*(1-b)*(x*x-1)/ell(a)
                    self.assertEqual(rewrite,(b-a)/x)

    def test_independent_owned_order_ledger(self):
        # K_ca: (2,0,2); T_bc: (0,3,3); T_ab: (3,3,0).
        self.assertEqual(tuple(sum(z) for z in zip((2,0,2),(0,3,3),(3,3,0))),(5,6,5))
        f=self.m.whole_source(self.m.primitive_catalog(self.model))
        self.assertEqual(f['finite_carrier_orders'],[5,6,5])
        legal=[x for x in f['F_denominator'] if x['factor'][1]=='ell']
        self.assertEqual({tuple(x['factor']) for x in legal},{(s,'ell',d) for s in range(3) for d in (0,1)})
        self.assertTrue(all(x['exponent']==1 for x in legal))
        self.assertFalse(f['physical_homogeneous_frame_identification_verified'])

    def test_handoff_and_exact_regenerated_artifact(self):
        marker=json.loads((HERE/'producer-ready.json').read_text())
        self.assertEqual(len(marker['files_sha256']),5)
        for name,digest in marker['files_sha256'].items():
            self.assertEqual(hashlib.sha256((HERE/name).read_bytes()).hexdigest(),digest,name)
        artifact=json.loads((HERE/'source-integration.json').read_text())
        self.assertEqual(self.m.build(REPO),artifact)
        self.assertEqual(artifact['source_commit'],PIN)
        self.assertTrue(all(v is False for v in artifact['gates'].values()))

    def test_degree_slack_and_formal_leading_functional(self):
        # Count cases only, not source tuples or physical polynomial arithmetic.
        catalog=self.m.primitive_catalog(self.model)
        self.assertEqual([c['finite_carrier_degree'] for c in catalog],[4,5,5,5,5,3])
        self.assertEqual([c['assigned_carrier_degree'] for c in catalog],[5,5,5,5,5,4])
        self.assertEqual([c['finite_primitive_weight_excess'] for c in catalog],[1,0,0,0,0,2])
        for n0 in range(4):
            for n5 in range(4-n0):
                for z in range(4):
                    excess=2*n0+4*n5
                    slack=-14*(n0+n5)-z
                    gap=1+excess+slack
                    if n0+n5+z:self.assertLessEqual(gap,0)
                    else:self.assertEqual(gap,1)
        # sigma_r-sigma_s=-2(r-s). The coefficient at degree w-1
        # in dK + rf*(sigma_r-sigma_s)K is identically zero for any
        # leading coefficient, including negative w; lower Laurent terms
        # have degree <=w-2 and rf-1/(2x) has degree -3.
        sigma=(1,-1)
        for r in range(2):
            for s in range(2):
                w=r-s
                self.assertEqual(Q(w)+Q(sigma[r]-sigma[s],2),0)
                if w:
                    self.assertNotEqual(Q(w)+Q(sigma[r],2),0) # one endpoint
                    self.assertNotEqual(Q(w)-Q(sigma[s],2),0)
                    self.assertNotEqual(Q(w),0) # gerbe q=0 cannot replace Q
        self.assertEqual(14*15+3*3-2,217)
        self.assertEqual(14*15,210)

    def test_all_eight_branches_and_four_complete_owned_edges(self):
        artifact=json.loads((HERE/'source-integration.json').read_text())
        self.assertEqual([r['v5_binding']['request']['seed'] for r in artifact['requests']],[12,30])
        for request in artifact['requests']:
            binding=request['v5_binding']; owners=binding['request']['owners']
            self.assertEqual(binding['request']['channel'],'E34(T12F12)')
            edges={e['id']:e for e in request['combined_edges']}
            self.assertEqual(len(edges),2)
            self.assertEqual(len(binding['branches']),4)
            self.assertEqual([b['pending_null_lemma']['coordinate'] for b in binding['branches']],[2,3,3,2])
            for index,branch in enumerate(binding['branches']):
                edge=edges[branch['combined_numerator_reference']]
                expected=owners[-2:] if index<2 else owners[-3:-1]
                self.assertEqual(edge['output_edge'],expected)
                self.assertEqual(branch['pending_null_lemma']['scalar_edge_owners'],expected)
                self.assertIn('then one complementary derivative',branch['differentiation_order'])
                self.assertEqual(branch['demand_current']['operator'],'tracefree')
            for edge in edges.values():
                a,b=edge['output_edge']; full=edge['N_fullsum']
                self.assertEqual(full['standard'],'C_a*C_b*Z_ab*B_ab, B=complete R(Kcov Pi + A h S Pi)F12; never split into free leaves')
                self.assertEqual(full['prism1'],'Z_ab*sum_u Qhat_u*P_[u,a,b]')
                self.assertEqual(full['prism2'],'-C_a*Z_ab*sum_(u,v) Qhat_u*Qhat_v*P_[u,v,b]')
                self.assertEqual(full['padding'],{'standard':['C_a','C_b','Z_ab'],'prism1':['Z_ab'],'prism2':['C_a','Z_ab']})
                self.assertEqual(edge['derivative'],'(Delta*dN-N*sum_f a_f*(df)*product_(g!=f)g)/(D*Delta)')
                self.assertEqual(edge['standard_B_requirements']['support'],[-1668,5248])
                self.assertTrue(edge['standard_B_requirements']['complete_sum'])
                self.assertEqual([v['owner'] for v in edge['C_output']],[a,b])
                self.assertEqual([v['owner'] for v in edge['Z_output']],[a,b])
                for name,owner in [('u',a),('v',b)]:
                    inserted=edge['inserted_owner_maps'][name]
                    self.assertEqual(inserted['standard_tag'],owner[4])
                    self.assertEqual(inserted['carrier_domain_inclusive'],[0,5])
                    self.assertEqual(inserted['mask_domain_inclusive'],[0,15])
                self.assertNotEqual(edge['inserted_owner_maps']['u']['occurrence'],edge['inserted_owner_maps']['v']['occurrence'])
                self.assertFalse(edge['geometric_source_premise_discharged'])

    def test_whole_DAG_against_physical_frame_artificial_first_jets(self):
        self.artificial_jet_control()

    def test_artificial_control_detects_wrong_Q_trace_and_order(self):
        for fault in ('Q_as_mask_over_x','reverse_products','trace_half','drop_left_Q','drop_right_Q'):
            with self.subTest(fault=fault):
                actual,expected=self.artificial_jet_control(fault)
                self.assertNotEqual(actual,expected)

    def test_source_alternation_is_not_nonlinear_recomputation(self):
        original=self.artificial_jet_control()
        rebuilt=self.artificial_jet_control(permutation=(1,0,2))
        # A source-first alternating adapter must use -original here.
        # Rebuilding the raw nonlinear formula is a different operation.
        self.assertNotEqual(rebuilt,-original)
        definition=self.m.whole_source(self.m.primitive_catalog(self.model))['source_triple_order']
        self.assertIn('otherwise alternate',definition)
        self.assertIn('never rebuild nonlinear source',definition)

    def artificial_jet_control(self,fault=None,permutation=None):
        # Arbitrary SL2 polynomial frames, artificial x=2,y=3; no model coefficients.
        x,y=J(2,1,0),J(3,0,1)
        coords=(x,y); masks=((0,1),(1,0),(1,1))
        hs=[x+s+2 for s in range(3)]
        ss=[]; ds=[]
        for s in range(3):
            u=x+s;v=y-s
            ss.append([[1+u*v,u],[v,J(1)]])
            rf=[(z*z+1)/(2*z*(z*z-1)) for z in coords]
            nu=J(s+2,*((s+2)*masks[s][d]*rf[d].v for d in range(2)))
            ds.append([[nu,J(0)],[J(0),J(1)/nu]])
        if permutation:
            masks=tuple(masks[i] for i in permutation)
            hs=[hs[i] for i in permutation]
            ss=[ss[i] for i in permutation]
            ds=[ds[i] for i in permutation]
        core=lambda a,b:mul(ss[b],inv(ss[a]))
        physical=lambda a,b:mul(mul(ds[b],core(a,b)),inv(ds[a]))
        g01,g12,g20=physical(0,1),physical(1,2),physical(2,0)
        mixed=add(mul(deriv(g12,0),deriv(g01,1)),mul(-1,mul(deriv(g12,1),deriv(g01,0))))
        product=mul(g20,mixed)
        q=lambda a,b,d:Q(masks[b][d]-masks[a][d])/coords[d].v
        expected=Q(15,4)*q(0,1,0)*q(1,2,1)-(product[0][0].v+product[1][1].v)/4
        f=self.m.whole_source(self.m.primitive_catalog(self.model));nodes=[]
        for op,*args in f['dag']:
            if op=='owned_polynomial_factor':
                slot,kind,d=args[0]
                z=hs[slot] if kind=='H' else coords[d]*(coords[d]**2-1) if masks[slot][d] else J(1)
            elif op=='catalog_cleared_primitive':
                slot,block=args;z=mul(hs[slot]**2,trans(inv(ss[slot]) if block=='P' else ss[slot]))
            elif op=='ordered_product':
                z=J(1)
                for i in (reversed(args) if fault=='reverse_products' else args):z=mul(z,nodes[i])
            elif op=='sum':
                z=nodes[args[0]]
                for i in args[1:]:z=add(z,nodes[i])
            elif op=='power':z=nodes[args[0]]**args[1]
            elif op=='scale':z=mul(Q(args[0],2 if fault=='trace_half' and args[:2]==[-1,4] else args[1]),nodes[args[2]])
            elif op=='transpose':z=trans(nodes[args[0]])
            elif op=='trace':z=nodes[args[0]][0][0]+nodes[args[0]][1][1]
            elif op=='polynomial_partial_after_elementary_substitution':z=deriv(nodes[args[0]],args[1])
            elif op=='mask_times_x_squared_plus_one_over_two':
                slot,d=args;z=masks[slot][d]*(coords[d]**2+1)/2
                if fault=='Q_as_mask_over_x':z=masks[slot][d]*(coords[d]**2-1)
            elif op=='polynomial_diagonal':z=[[nodes[args[0]],J(0)],[J(0),-nodes[args[0]]]]
            elif op=='binary_mask_q_numerator':
                a,b,d,sign=args
                coefficient=masks[b][d]*(1-masks[a][d]) if sign==1 else -masks[a][d]*(1-masks[b][d])
                z=coefficient*(coords[d]**2-1)
            else:self.fail('unknown op '+op)
            nodes.append(z)
            # Identify the physical endpoint products by their AST shape;
            # keep zero matrix shape when deleting one endpoint contribution.
            if op=='ordered_product' and len(args)==2:
                left=f['dag'][args[0]][0];right=f['dag'][args[1]][0]
                if (fault=='drop_left_Q' and left=='polynomial_diagonal') or (fault=='drop_right_Q' and right=='polynomial_diagonal'):
                    nodes[-1]=mul(0,z)
        def denominator(items):
            out=Q(1)
            for item in items:
                slot,kind,d=item['factor']
                factor=hs[slot].v if kind=='H' else (coords[d]*(coords[d]**2-1)).v if masks[slot][d] else Q(1)
                out*=factor**item['exponent']
            return out
        actual=val(nodes[f['F_numerator']])/denominator(f['F_denominator'])
        if fault:return actual,expected
        self.assertEqual(actual,expected)
        self.assertEqual(val(nodes[f['cleared_P']]),expected*denominator(f['clearing']))
        self.assertNotEqual(expected,0)
        return expected

if __name__=='__main__': unittest.main(verbosity=2)
