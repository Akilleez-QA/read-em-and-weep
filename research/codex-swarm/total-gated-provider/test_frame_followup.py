"""Independent TP frame correction + explicit historical-suite replay.

The original review/test files remain unchanged. ONLY their in-memory
MARKER_SHA assignment is replaced for replay after this file authenticates the
new marker and producer bytes. No other historical test/pin is modified.
"""
import ast
from fractions import Fraction as Q
import hashlib
import itertools
import json
from pathlib import Path
import resource
import sys
import types
import unittest
from unittest.mock import patch

if __name__=='__main__':
    resource.setrlimit(resource.RLIMIT_AS,(512*1024*1024,512*1024*1024))
    resource.setrlimit(resource.RLIMIT_CPU,(59,59))

HERE=Path(__file__).resolve().parent
NEW_MARKER='2b359484048dc31e8e4258f7ea864ec15f9a57c36729f71439f9954e230e750d'
OLD_MARKER='03dbc4a68984e973528c9584bbf042f44e53c5f74579e7a0737884b3d1f591b1'
OLD_TEST='5797d6a113fc63676e3373873ffb3dd15a177b4480a6db6b17b8e74bf95ec835'
OLD_REVIEW='23879d3ca96aeb342a59a42550a83c4ad4e569bb316eb3a4b951f9d4be49b1d2'
def sha(raw):return hashlib.sha256(raw).hexdigest()

def authenticate():
    raw=(HERE/'producer-ready.json').read_bytes()
    if sha(raw)!=NEW_MARKER:raise RuntimeError('new TP handoff drift')
    marker=json.loads(raw);seen={}
    for name,h in marker['files'].items():
        value=sha((HERE/name).read_bytes())
        if value!=h:raise RuntimeError('producer drift: '+name)
        seen[name]=value
    for name,h in(('test_independent.py',OLD_TEST),('review-independent.md',OLD_REVIEW)):
        if sha((HERE/name).read_bytes())!=h:raise RuntimeError('historical reviewer file changed: '+name)
    return seen

BEFORE=authenticate()
import provider as P
Z=(0,0,0,0)
def owner(c,m,t,j):return P.I.FullOwner(37,('frame-artificial',j),c,m,t)
def mat(rows):return tuple(tuple(Q(x)for x in row)for row in rows)
def mul(a,b):return tuple(tuple(sum((a[i][k]*b[k][j]for k in range(2)),Q(0))for j in range(2))for i in range(2))
def inv(a):
    d=a[0][0]*a[1][1]-a[0][1]*a[1][0]
    return mat([[a[1][1]/d,-a[0][1]/d],[-a[1][0]/d,a[0][0]/d]])
def scaled(c,a):return tuple(tuple(c*x for x in row)for row in a)
def apply_artificial_route(route,X,transitions):
    if route.get('zero_plan_requires_no_transport_evaluation',False):return mat([[0,0],[0,0]])
    if route['transport']=='identity':return scaled(route['parity'],X)
    edge=route['transition']['ordered_edge_request']
    G=transitions[edge]
    if route['ordered_actions']!=['inverse(g(original_first,canonical_first))','X_canonical','g(original_first,canonical_first)']:
        raise AssertionError('wrong ordered conjugation actions')
    return scaled(route['parity'],mul(mul(inv(G),X),G))

class FrameFollowup(unittest.TestCase):
    @classmethod
    def tearDownClass(cls):
        if authenticate()!=BEFORE:raise RuntimeError('TP producer inputs changed')
    def test_current_hashes_and_historical_artifacts_unchanged(self):self.assertEqual(authenticate(),BEFORE)
    def test_noncommuting_countercontrol_and_ordered_reverse_edge(self):
        a,b,c=owner(0,0,0,0),owner(1,1,8,1),owner(4,15,15,2)
        route=P.frame_plan(P.request_plan('Rsharp',(b,a,c)))
        self.assertEqual(route['transition']['ordered_edge_request'],(b.data(),a.data()))
        G=mat([[1,2],[3,7]]);X=mat([[2,5],[7,11]])
        y=apply_artificial_route(route,X,{(b.data(),a.data()):G})
        self.assertEqual(y,mat([[-39,-91],[11,26]]))
        self.assertNotEqual(y,scaled(-1,X))
        self.assertNotEqual(y,scaled(-1,mul(mul(G,X),inv(G))))
        with self.assertRaises(KeyError):apply_artificial_route(route,X,{(a.data(),b.data()):inv(G)})
    def test_all_permutations_parity_and_first_common_key(self):
        ordered=(owner(5,0,0,0),owner(1,1,8,1),owner(4,15,15,2));X=mat([[1,2],[0,-1]])
        for perm in itertools.permutations(range(3)):
            raw=tuple(ordered[i]for i in perm);plan=P.request_plan('Rsharp',raw);r=P.frame_plan(plan)
            sign=-1 if sum(perm[i]>perm[j]for i in range(3)for j in range(i+1,3))%2 else 1
            self.assertEqual(r['parity'],sign);self.assertEqual(r['original_first_owner'],raw[0].data())
            self.assertEqual(r['canonical_first_owner'],ordered[0].data())
            self.assertEqual(r['transport'],'identity'if raw[0].common_key==ordered[0].common_key else'ordered_conjugation')
            self.assertEqual(plan.owners,raw);self.assertEqual(plan.sorted_owners,ordered)
            if r['transport']=='identity':self.assertEqual(apply_artificial_route(r,X,{}),scaled(sign,X))
            self.assertFalse(r['physical_transport_evaluated'])
    def test_scalar_F_T_scope_and_physical_repeat_Rsharp_survival(self):
        a,b,c=owner(1,2,0,0),owner(1,2,8,1),owner(4,15,15,2)
        for k in('F','T'):
            r=P.frame_plan(P.request_plan(k,(b,a,c)))
            self.assertEqual(r['value_frame'],'common_finite_fixed_frame')
            self.assertEqual(r['transport'],'identity');self.assertEqual(r['coefficient_type'],'scalar')
        self.assertEqual(P.request_plan('F',(b,a,c)).effective_sign,0)
        r=P.frame_plan(P.request_plan('Rsharp',(b,a,c)))
        self.assertNotEqual(r['parity'],0);self.assertEqual(r['transport'],'ordered_conjugation')
        self.assertEqual(r['transition']['ordered_edge_request'],(b.data(),a.data()))
    def test_zero_empty_alias_and_prefix_owners_have_no_transport_execution(self):
        a,b=owner(0,0,0,0),owner(1,1,8,1);X=mat([[2,3],[5,7]])
        class PoisonTransitions:
            def __getitem__(self,key):raise AssertionError('zero plan attempted transport')
        repeated=P.request_plan('Rsharp',(b,a,a));r=P.frame_plan(repeated)
        self.assertEqual(r['parity'],0);self.assertTrue(r['zero_plan_requires_no_transport_evaluation'])
        self.assertEqual(apply_artificial_route(r,X,PoisonTransitions()),mat([[0,0],[0,0]]))
        empty=P.frame_plan(P.request_plan('Rsharp',()))
        self.assertTrue(empty['empty_tuple_has_no_base_owner']);self.assertIsNone(empty['transition']['ordered_edge_request'])
        alias=owner(2,3,12,0);plan=P.request_plan('Rsharp',(b,a,alias))
        self.assertTrue(plan.occurrence_alias);self.assertEqual(plan.owners,(b,a,alias));self.assertNotEqual(plan.effective_sign,0)
        # Provenance aliases/prefix positions are retained, not repaired or
        # converted into common-cover repetitions by the frame correction.
        self.assertEqual(plan.describe()['owners'],[b.data(),a.data(),alias.data()])
    def test_actual_gates_refuse_before_frame_or_normalization(self):
        actual=object.__new__(P.ActualProvider)
        actual.mode='synthetic';actual.verified=True
        with patch.object(P,'request_plan',side_effect=AssertionError('normalization bypass')),patch.object(P,'frame_plan',side_effect=AssertionError('transport bypass')):
            for fn in(actual.coefficient,actual.alternating_coefficient,actual.factor_terms,actual.owners):
                with self.assertRaises(P.I.PhysicalAdmissionMissing):fn(object(),True,'invalid exponent')
    def test_toy_named_Rsharp_is_explicitly_scalar_only(self):
        self.assertEqual(P.ToyProvider.coefficient_scope,'scalar_fixture_only')
        a,b,c=owner(0,0,0,0),owner(1,1,8,1),owner(4,15,15,2)
        key=('Rsharp',tuple(o.common_key for o in(a,b,c)),Z,(0,1))
        toy=P.ToyProvider({key:Q(3,7)},{})
        self.assertEqual(toy.coefficient('Rsharp',(b,a,c),Z),Q(-3,7))
        with self.assertRaises(ValueError):P.ToyProvider({key:mat([[1,0],[0,1]])},{})

def historical_suite(loader):
    raw=(HERE/'test_independent.py').read_bytes()
    if sha(raw)!=OLD_TEST:raise RuntimeError('historical test byte drift')
    tree=ast.parse(raw,filename=str(HERE/'test_independent.py'));changed=0
    for node in tree.body:
        if isinstance(node,ast.Assign)and any(isinstance(t,ast.Name)and t.id=='MARKER_SHA'for t in node.targets):
            if not isinstance(node.value,ast.Constant)or node.value.value!=OLD_MARKER:raise RuntimeError('unexpected old marker anchor')
            node.value=ast.copy_location(ast.Constant(NEW_MARKER),node.value);changed+=1
    if changed!=1:raise RuntimeError('must override exactly one historical marker constant')
    module=types.ModuleType('tp_explicit_frame_followup_historical_replay');module.__file__=str(HERE/'test_independent.py')
    sys.modules[module.__name__]=module
    exec(compile(ast.fix_missing_locations(tree),module.__file__,'exec'),module.__dict__)
    return loader.loadTestsFromTestCase(module.Independent)

def load_tests(loader,tests,pattern):
    tests.addTests(historical_suite(loader));return tests

if __name__=='__main__':unittest.main()
