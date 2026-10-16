"""Independent metadata audit of every label in the fixed carrier sector."""
import hashlib,itertools,json,unittest
from pathlib import Path
import lower_selected_kernel_denominators as original
import lower_legal_mask_sector as parameterized
import preflight_legal_mask_sector as sector
import test_selected_support_separation_independent as independent
ROOT=Path(__file__).parent

class LegalSectorTests(unittest.TestCase):
    def test_original_exact_byte_equivalence(self):
        raw=(json.dumps(parameterized.build(),sort_keys=True,separators=(',',':'))+'\n').encode()
        self.assertEqual(raw,(ROOT/'selected-full-owner-kernel-lowering.json').read_bytes())
        self.assertEqual(hashlib.sha256(raw).hexdigest(),sector.PIN)
        self.assertEqual(hashlib.sha256((ROOT/'lower_selected_kernel_denominators.py').read_bytes()).hexdigest(),sector.COMPILER)

    def test_parameterized_build_has_only_label_substitution(self):
        src=(ROOT/'lower_selected_kernel_denominators.py').read_text()
        expected=src[src.index('def build():'):src.index("if __name__=='__main__'")]
        expected=expected.replace('def build():','def build(masks=(12,13,15)):').replace('    outer.authenticate_public_sources()',"    if len(masks)!=3 or any(type(m) is not int or not 0<=m<16 for m in masks):raise ValueError('three legal masks required')\n    outer.authenticate_public_sources()",1).replace('((1,12,3),(2,13,11),(4,15,15))','((1,masks[0],3),(2,masks[1],11),(4,masks[2],15))')
        actual=(ROOT/'lower_legal_mask_sector.py').read_text()
        self.assertEqual(actual[actual.index('def build('):],expected)

    def test_independent_mask_bit_order_and_exhaustive_domain(self):
        # Strings avoid sharing either decoder's bit manipulation.
        ds=[]
        for tag in (3,11,15):
            std=tuple(int(x) for x in format(tag,'04b'))
            self.assertEqual(original.owned.decode_standard_tag(tag),std)
            allowed=[]
            for mask in range(16):
                legal=tuple(int(x) for x in format(mask,'04b')[::-1])
                self.assertEqual(original.owned.decode_legal_mask(mask),legal)
                if all(l<=s for l,s in zip(legal,std)):allowed.append(mask)
            ds.append(allowed)
        self.assertEqual(ds,[[0,4,8,12],[0,1,4,5,8,9,12,13],list(range(16))])
        active=set(itertools.product(*ds))
        inactive=set(itertools.product(range(16),repeat=3))-active
        self.assertEqual((len(active),len(inactive)),(512,3584))
        self.assertEqual(tuple(map(tuple,ds)),tuple(sector.active_masks(t) for t in (3,11,15)))

    def test_every_inactive_owner_has_exact_zero_outer_factor(self):
        # Check 3*16 owner possibilities, proving the union of 3584 tuple cases.
        for owner,tag in enumerate((3,11,15)):
            for mask in range(16):
                masks=[12,13,15];masks[owner]=mask
                vs=tuple(original.owned.VertexLabel(4,o,b,m,t) for o,(b,m,t) in enumerate(zip((1,2,4),masks,(3,11,15))))
                lo=original.Lower(vs);root=lo.quotient(vs[owner])
                if mask not in sector.active_masks(tag):self.assertEqual(root,lo.g.c(0))
                else:self.assertNotEqual(root,lo.g.c(0))

    def test_all_saved_separators_with_independent_vertex_optimizer(self):
        saved=json.loads((ROOT/'legal-mask-sector-support.json').read_text())
        self.assertEqual(saved['counts'],{'full_legal_tuples':4096,'structurally_zero_inactive':3584,'active_tuples':512,'support_certified_zero_active':512,'unresolved_active':0,'active_multipliers':4096,'certified_zero_multipliers':4096})
        self.assertEqual(saved['scope'],{'seed':4,'row':2,'standard':[3,11,15],'carrier':[1,2,4],'terminal_target':[-1,-2,-2,-2],'input_character':[0,0,-2,-2]})
        self.assertEqual(saved['held_limits'],{'private_resource_configuration_omitted':True})
        for flag in ('physical_polynomial_evaluation','physical_polynomial_expansion','execution_release','actual_factorization_accepted'):
            self.assertIs(saved[flag],False)
        self.assertEqual(saved['physical_products_spent'],0)
        self.assertEqual(len(saved['active_results']),512)
        seen=set();count=0;baseline_ledgers=None
        for row in saved['active_results']:
            masks=tuple(row['legal_masks']);self.assertNotIn(masks,seen);seen.add(masks)
            self.assertEqual(row['status'],'certified_zero')
            self.assertEqual(len(row['multipliers']),8)
            self.assertEqual(row['owners'],[[4,o,b,m,t] for o,(b,m,t) in enumerate(zip((1,2,4),masks,(3,11,15)))])
            self.assertEqual(row['vertex_degrees'],[[5321+2*int(format(m,'04b')[3-i]) for i in range(4)] for m in masks])
            a=parameterized.build(masks)
            digest=hashlib.sha256(json.dumps(a,sort_keys=True,separators=(',',':')).encode()).hexdigest()
            self.assertEqual(digest,row['dag_sha256'])
            self.assertEqual(json.loads(json.dumps(a['owners'])),row['owners'])
            independent.nodes=a['dag'];independent.bound.cache_clear()
            current_ledgers=[[(v['carrier'],v['standard']) for v in t[k]['derived_denominators']] for t in a['terms'] for k in ('A','B')]
            if baseline_ledgers is None:baseline_ledgers=current_ledgers
            self.assertEqual(current_ledgers,baseline_ledgers)
            term_index=-1
            for term,results in zip(a['terms'],(row['multipliers'][i:i+2] for i in range(0,8,2))):
                # Independent complete homogeneous degree formula: legal section
                # degree 1+2*m, carrier degree 14*5, standard degree 5250.
                M=[(0,0,-2,-2)[i]+sum(5321+2*int(format(masks[o],'04b')[3-i]) for o in term['edge']) for i in range(4)]
                for kind,result in zip(('A','B'),results):
                    term_index+=1
                    self.assertEqual(result['status'],'certified_zero')
                    self.assertEqual(result['edge'],list(term['edge']))
                    self.assertEqual(result['kind'],kind)
                    self.assertEqual(result['derivative'],term['coordinate'] if kind=='B' else None)
                    self.assertEqual(result['root'],term[kind]['root'])
                    self.assertEqual(result['complete_numerator_degree'],M)
                    self.assertEqual([list(x['owner']) for x in term[kind]['derived_denominators']],row['owners'])
                    for ledger in term[kind]['derived_denominators']:
                        self.assertGreaterEqual(ledger['carrier'],0)
                        self.assertLessEqual(ledger['carrier'],54)
                        for i,e in enumerate(ledger['standard']):
                            self.assertGreaterEqual(e,0)
                            self.assertLessEqual(e,5251)
                            if format(ledger['owner'][4],'04b')[i]=='0':self.assertEqual(e,0)
                        for i,e in enumerate(ledger['legal']):
                            self.assertGreaterEqual(e,0)
                            self.assertLessEqual(e,29)
                            if not (ledger['owner'][3]>>i)&1:self.assertEqual(e,0)
                    cert=result['certificate']
                    if cert is None:
                        self.assertEqual(result['status'],'unresolved');continue
                    self.assertNotIn('literal_zero',cert)
                    w=tuple(cert['normal']);b=independent.bound(term[kind]['root'],w)
                    self.assertEqual(list(b),cert['multiplier_bounds'])
                    root_node=a['dag'][term[kind]['root']];self.assertEqual(root_node[0],'multiply')
                    numerator_upper=independent.bound(root_node[1],w)[1]
                    adjustment=sum((ledger['legal'][i]-int(o in term['edge'])*int(bool(masks[o]&(1<<i))))*max(w[i],3*w[i]) for o,ledger in enumerate(term[kind]['derived_denominators']) for i in range(4))
                    self.assertEqual(numerator_upper-adjustment,[113,83,113,82,67,55,68,56][term_index])
                    m=[[int(bool(mask&(1<<i))) for i in range(4)] for mask in masks]
                    expected_gap=(487-58*(m[0][2]+m[0][3])-57*(m[1][0]+m[1][2]+m[1][3]+m[2][0]+m[2][2]+m[2][3])) if term_index<4 else ((273 if term_index<6 else 272)-57*(m[0][3]+m[1][3])-58*m[2][3])
                    self.assertEqual(cert['gap'],expected_gap)
                    self.assertGreaterEqual(expected_gap,29 if term_index<4 else 101 if term_index<6 else 100)
                    # Remove only the extra legal common-denominator lifts.
                    # The edge's actual legal denominator remains present.
                    root_node=a['dag'][term[kind]['root']]
                    self.assertEqual(root_node[0],'multiply')
                    numerator_high=independent.bound(root_node[1],w)[1]
                    compensation=sum((ledger['legal'][i]-int(o in term['edge'])*((masks[o]>>i)&1))*max(w[i],3*w[i]) for o,ledger in enumerate(term[kind]['derived_denominators']) for i in range(4))
                    order=2*a['terms'].index(term)+int(kind=='B')
                    self.assertEqual(numerator_high-compensation,[113,83,113,82,67,55,68,56][order])
                    shift=tuple(int(kind=='B' and i==term['coordinate']) for i in range(4))
                    target=sum(w[i]*((-1,-2,-2,-2)[i]+shift[i]) for i in range(4))
                    proj=[sum(w[i]*(shift[i] if w[i]>=0 else M[i]) for i in range(4)),sum(w[i]*(M[i] if w[i]>=0 else shift[i]) for i in range(4))]
                    self.assertEqual(proj,cert['full_numerator_projection'])
                    self.assertEqual(target,cert['target_projection'])
                    necessary=[target-b[1],target-b[0]]
                    self.assertEqual(necessary,cert['necessary_numerator_projection'])
                    self.assertEqual(cert['gap'],max(necessary[0]-proj[1],proj[0]-necessary[1]))
                    self.assertTrue(proj[1]<necessary[0] or proj[0]>necessary[1]);count+=1
            # End-owner composition collapses at n=(0,0,0,0,2671),
            # with literal zero bases at exponent zero retained as unit factors.
            terminal_nodes=[i for i,n in enumerate(a['dag']) if n[0]=='bounded_composition_sum' and n[1]['dimension']==5]
            self.assertEqual(len(terminal_nodes),1)
            self.assertEqual([x['node'] for x in row['terminal_composition_unit_identities']],terminal_nodes)
            for identity in row['terminal_composition_unit_identities']:
                node=a['dag'][identity['node']];self.assertEqual(identity['unique_index'],[0,0,0,0,2671])
                self.assertEqual(identity['value'],'1')
                d=node[1];self.assertEqual(d,{'dimension':5,'total':2671,'chosen':4,'threshold':535,'earlier_upper':534})
                # Derive the singleton independently from each literal-zero base.
                forced_zero=set()
                for power in node[2]['powers']:
                    if a['dag'][power['base']]==['rational',0,1]:
                        e=power['exponent'];self.assertEqual(e['constant'],0)
                        self.assertEqual(sorted(e['coefficients']),[0,0,0,0,1])
                        forced_zero.add(e['coefficients'].index(1))
                self.assertEqual(forced_zero,{0,1,2,3})
                coefficient=node[2]['coefficient'];self.assertEqual(coefficient['op'],'multiply_binomials')
                self.assertEqual(len(coefficient['factors']),5)
                for factor in coefficient['factors']:
                    values=[factor[key]['constant']+sum(x*y for x,y in zip(factor[key]['coefficients'],[0,0,0,0,2671])) for key in ('top','bottom')]
                    self.assertIn(values[1],(0,values[0]))
                    self.assertGreaterEqual(values[0],0)
                for power in node[2]['powers']:
                    e=power['exponent'];n=[0,0,0,0,2671]
                    exponent=e['constant']+sum(x*y for x,y in zip(n,e['coefficients']))
                    base=a['dag'][power['base']]
                    if exponent:self.assertEqual(base,['rational',1,1])
                    elif base==['rational',0,1]:self.assertEqual(exponent,0)
        self.assertEqual(count,saved['counts']['certified_zero_multipliers'])
        self.assertEqual(seen,set(itertools.product(*(sector.active_masks(t) for t in (3,11,15)))))

if __name__=='__main__':unittest.main()
