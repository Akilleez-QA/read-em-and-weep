"""Abstract controls only: no physical source, polynomial or compiler imports."""
import itertools
import json
from collections import Counter
from pathlib import Path
import unittest


def mm(a,b):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def plus(a,b,s=1):
    return [[x+s*y for x,y in zip(r,t)] for r,t in zip(a,b)]
def transpose(a): return list(map(list,zip(*a)))
def tr(a): return sum(a[i][i] for i in range(len(a)))
def mat(n,m,seed): return [[((i+1)*7+(j+1)*11+seed)%13-6 for j in range(m)] for i in range(n)]
def coeff_index(m): return sum((2-x)*3**(3-i) for i,x in enumerate(m))
def sign(p): return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))

class Contract(unittest.TestCase):
    def test_all_thirty_bottom_chain_identities_formal(self):
        # Independent formal atoms gamma(i,a,k) W(a,b) v(k), not polynomials.
        for i,b in itertools.product(range(15),range(2)):
            positive=Counter({(i,a,k,a,b,k):1 for a,k in itertools.product(range(5),repeat=2)})
            negative=Counter()
            for a in range(5):
                for column in range(10):
                    ev_b,k=divmod(column,5)
                    if ev_b==b: negative[(i,a,k,a,ev_b,k)]+=1
            self.assertEqual(positive,negative)
            self.assertNotEqual(positive,Counter())

    def test_homotopy_trace_adjoint_both_signs(self):
        W,F,H,E=[mat(3,3,n) for n in [0,2,5,8]]
        for s in [1,-1]:
            HF=plus(mm(H,F),mm(mm(E,F),H),s)
            adj=plus(mm(W,H),mm(mm(H,W),E),s)
            self.assertEqual(tr(mm(W,HF)),tr(mm(adj,F)))

    def test_inclusion_adjoint_transpose(self):
        I,P,W,R=mat(4,2,1),mat(2,4,3),mat(4,4,4),mat(2,2,7)
        lhs=tr(mm(W,mm(mm(I,transpose(R)),P)))
        adj=transpose(mm(mm(P,W),I))
        self.assertEqual(lhs,tr(mm(adj,R)))
        self.assertNotEqual(lhs,tr(mm(mm(mm(P,W),I),R)))

    def test_negative_projection_has_no_perturbation_paths(self):
        paths=[(q,k) for q in range(5) for k in range(8) if q-k==4]
        self.assertEqual(paths,[(4,0)])
        # Dropping q=5 is justified only AFTER transport to tensor cover.
        self.assertIn((5,1),[(q,k) for q in range(6) for k in range(8) if q-k==4])

    def test_scalar_harmonic_window_kills_regular_faces(self):
        harmonic=set(range(-3,0))
        for e in range(-20,21):
            if e>=0 or e<=-4: self.assertNotIn(e,harmonic)
        self.assertEqual(harmonic,{-3,-2,-1})

    def test_twenty_maps_thirtytwo_requests(self):
        data=json.loads((Path(__file__).parent/'weighted-requests.json').read_text())
        req=data['requests']
        pairs={(r['scalar_map']['i'],r['scalar_map']['b']) for r in req}
        want={(i,0) for i in range(5,11)}|{(i,1) for i in range(5)}|{(i,1) for i in range(6,15)}
        self.assertEqual(pairs,want); self.assertEqual(len(req),32)
        self.assertEqual(Counter(r['block'] for r in req),{'Q^2':20,'v_k Q':10,'v_k v_l':2})
        terms=[(r['scalar_map']['i'],r['scalar_map']['b'],tuple(t['laurent_exponents'])) for r in req for t in r['terms']]
        self.assertEqual(len(terms),127); self.assertEqual(len(set(terms)),121)
        for r in req:
            for t in r['terms']:
                m=t['dual_monomial']; e=t['laurent_exponents']
                self.assertEqual(e,[-v-1 for v in m]); self.assertEqual(t['output_index'],coeff_index(m))
                self.assertTrue(all(x+y==-1 for x,y in zip(e,m)))
        self.assertFalse(any(data['gates'].values()))

    def test_all_eightyone_indices(self):
        self.assertEqual({coeff_index(m) for m in itertools.product(range(3),repeat=4)},set(range(81)))

    def test_twentyfour_oriented_staircases(self):
        paths=[]
        for p in itertools.permutations(range(4)):
            vertex=0; path=[vertex]
            for i in p:
                vertex|=1<<(3-i); path.append(vertex)
            self.assertEqual(path[-1],15); self.assertEqual(len(set(path)),5)
            paths.append((tuple(path),sign(p)))
        self.assertEqual(len({p for p,s in paths}),24)
        self.assertEqual(Counter(s for p,s in paths),{-1:12,1:12})

    def test_owner_bound_ledger(self):
        for s in range(4):
            self.assertLessEqual(32+4+6*s,54)
            self.assertLessEqual(18+2+3*s,29)
        self.assertEqual(5608*5-4,28036)
        self.assertEqual((-5*2006-5*5608,28036+5*6677),(-38070,61421))
        self.assertEqual((-6*2006-6*5608,5608*6-5+6*6677),(-45684,73705))

    def test_owner_retention_after_face_deletion(self):
        tuple_owners=('a','b','c','d','e')
        kernel_owners={tuple_owners[0]}
        face=tuple_owners[1:]
        self.assertNotIn('a',face)
        self.assertIn('a',kernel_owners)
        # Equal divisor names never collapse owned factors.
        factors={('a','h0'):54,('b','h0'):54}
        self.assertEqual(len(factors),2)
        self.assertNotIn(('c','h0'),factors)

    def test_top_closure_is_required(self):
        # A formal L(delta J2) need not vanish until delta J2=dJ3
        # and Ld=0 are both supplied; this control forbids a truncation proof.
        obligations={'delta_J2_equals_d_J3':True,'L_d_equals_zero':True}
        closed=lambda o: all(o.values())
        self.assertTrue(closed(obligations))
        for k in obligations:
            changed=dict(obligations); changed[k]=False
            self.assertFalse(closed(changed))

if __name__=='__main__': unittest.main(verbosity=2)
