#!/usr/bin/env python3
"""Abstract split-complex matrix tests only; never evaluate pinned polynomials."""
import copy
from functools import lru_cache
from itertools import combinations
from pathlib import Path
import tempfile
import unittest
import numpy as np
import resolution_selector_source_binding as s
import owned_scalar_denominator_binding as o
import prune_refined_selector_paths as pruning
import compile_refined_detector_metadata as spec

N=32
OFF=(0,5,20,30,32)

def abstract_owners():
    rng=np.random.default_rng(733)
    H=np.zeros((N,N),dtype=object)
    H[0:5,5:10]=np.eye(5,dtype=object)
    H[10:18,20:28]=np.eye(8,dtype=object)
    H[28:30,30:32]=np.eye(2,dtype=object)
    I=np.zeros((N,2),dtype=object);I[18:20,:]=np.eye(2,dtype=object)
    P=I.T.copy()
    out=[]
    for owner in range(5):
        G=np.eye(N,dtype=object);Gi=G.copy()
        for a,b in zip(OFF,OFF[1:]):
            # Invertible degree-preserving shear products over exact integers.
            for _ in range(15):
                x,y=rng.choice(np.arange(a,b),2,replace=False)
                z=int(rng.choice([-1,1]))
                S=np.eye(N,dtype=object);S[x,y]=z
                Si=np.eye(N,dtype=object);Si[x,y]=-z
                G=G@S;Gi=Si@Gi
        out.append({'H':G@H@Gi,'I':G@I,'P':P@Gi})
    return out

class BindingTests(unittest.TestCase):
    def test_all_paths_against_direct_cech_J(self):
        owners=abstract_owners();rng=np.random.default_rng(91)
        residual={t:rng.integers(-2,3,size=(2,2)).astype(object) for t in combinations(range(5),3)}
        for d in owners:
            H,I,P=d['H'],d['I'],d['P'];d['E']=I@P
            self.assertFalse(np.any(H@H));self.assertFalse(np.any(H@I));self.assertFalse(np.any(P@H))
            self.assertTrue(np.array_equal(P@I,np.eye(2)))
        @lru_cache(None)
        def direct(t,depth):
            a=owners[t[0]]
            if depth==0:return a['I']@residual[t].T@a['P']
            F=sum(((-1)**i)*direct(t[:i]+t[i+1:],depth-1) for i in range(len(t)))
            r=-(depth-1)
            return (1 if depth==1 else -1)*(a['H']@F+(-1 if r%2 else 1)*(a['E']@F@a['H']))
        def evaluate(ast):
            op=ast['op'];args=ast['args']
            if op=='multiply':return evaluate(args[0])@evaluate(args[1])
            if op=='transpose':return evaluate(args[0]).T
            if op=='row':return evaluate(args[0])[args[1]:args[1]+1,:]
            if op=='column':return evaluate(args[0])[:,args[1]:args[1]+1]
            if op=='normalized_row_residual_slot':return residual[tuple(v[1] for v in args[0])]
            if op in ('pinned_resolution_rational_block','pinned_pivot_section'):
                d=owners[args[1][1]];name=args[2] if op!='pinned_pivot_section' else 'eta'
                return {'I':d['I'][5:20,:],'P':d['P'][:,5:20],
                        'H0':d['H'][0:5,5:20],'H1':d['H'][5:20,20:30],
                        'eta':d['H'][20:30,30:32]}[name]
            raise AssertionError(op)
        nonzero=0;transpose_detected=False;sign_detected=False;owner_detected=False
        for seed,record in enumerate(spec.seed_records()):
            binding=s.bind_seed(seed);row=spec.ROWS[record['row']];q,_,_,block,a,b,_=row
            # Mst convention is source s, target t.
            source,target=int(block[1]),int(block[2])
            expected=record['coefficient']*direct(tuple(range(q+1)),q-2)[OFF[target]+a,OFF[source]+b]
            actual=binding['coefficient']*evaluate(binding['source_ast'])[0,0]
            self.assertEqual(actual,expected,(seed,block))
            kernel=evaluate(binding['dual_kernel_ast']);tail=tuple(range(q-2,q+1))
            self.assertEqual(actual,binding['coefficient']*np.trace(kernel@residual[tail]))
            if actual:nonzero+=1;sign_detected|=(-actual!=expected)
            wrong_owner=copy.deepcopy(binding['source_ast'])
            def switch_owner(node):
                if node['op']=='pinned_resolution_rational_block':
                    fields=list(node['args'][1]);fields[1]=(fields[1]+1)%5;node['args'][1]=fields
                    return True
                return any(switch_owner(x) for x in node['args'] if isinstance(x,dict) and 'op' in x)
            switch_owner(wrong_owner)
            owner_detected|=(binding['coefficient']*evaluate(wrong_owner)[0,0]!=expected)
            wrong=copy.deepcopy(binding['source_ast'])
            wrong['args'][0]['args'][1]=wrong['args'][0]['args'][1]['args'][0]
            transpose_detected|=(binding['coefficient']*evaluate(wrong)[0,0]!=expected)
        self.assertGreater(nonzero,0);self.assertTrue(transpose_detected);self.assertTrue(sign_detected);self.assertTrue(owner_detected)

    def test_all_owner_ledgers_and_eta(self):
        paths=pruning.generate()['paths']
        for i,p in enumerate(paths):
            b=s.bind_seed(i)
            self.assertEqual(b['coefficient'],p['coefficient'])
            self.assertEqual(b['weighted_owners'],p['weighted_owners'])
            self.assertEqual(len(b['owners']),spec.ROWS[p['row']][0]+1)
            self.assertEqual(b['owners'][p['tail'][0]],b['tail_owners'][0])
            self.assertFalse(b['actual_factorization']);self.assertFalse(b['execution_release'])
            text=str(b['right_ast'])
            self.assertEqual('pinned_pivot_section' in text,b['terminal_block']=='M31')

    def test_canonical_carriers_and_bits(self):
        self.assertEqual(s.definition()['carrier_domain'],list(range(6)))
        for carrier in range(6):
            v=o.VertexLabel(0,0,carrier,1,8)
            self.assertEqual(s.block(v,'I').args[1],v.data())
            self.assertEqual(o.decode_legal_mask(v.legal_mask),(1,0,0,0))
            self.assertEqual(o.decode_standard_tag(v.standard_tag),(1,0,0,0))
        with self.assertRaises(ValueError):o.VertexLabel(0,0,-1,0,0)

    def test_binding_mutations(self):
        b=s.bind_seed(0);self.assertTrue(s.validate_binding(b))
        for field,value in [('coefficient',99),('entry',[0,0]),('actual_factorization',True)]:
            bad=copy.deepcopy(b);bad[field]=value
            with self.assertRaises(ValueError):s.validate_binding(bad)
        self.assertIn('h_j=v_j^5-product',s.definition()['eta_owned_cancellation'])
        for carrier in range(6):
            eta=s.block(o.VertexLabel(0,0,carrier,0,0),'eta')
            self.assertIn('denominator owned by this carrier',eta.args[-1])

    def test_negative_inputs(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'bad.json';p.write_text('{}')
            with self.assertRaises(ValueError):s.authenticate(p)
        for seed in (-1,78,True,'0'):
            with self.assertRaises(ValueError):s.bind_seed(seed)
        vertices=[o.label(0,i) for i in range(3)]
        vertices[0]=o.label(0,1)
        with self.assertRaises(ValueError):s.bind_seed(0,vertices)
        with self.assertRaises(ValueError):s.block(o.label(0,0),'H')

if __name__=='__main__':
    if not __debug__:raise SystemExit(2)
    unittest.main(verbosity=2)
