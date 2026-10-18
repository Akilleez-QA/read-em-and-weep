"""Independent finite-label combinatorics and support replay; no polynomial evaluation."""
from pathlib import Path
import itertools,json,unittest,math,hashlib
import lower_permuted_standard_sector as lowering
import preflight_permuted_standard_sector as scan
import resolution_selector_source_binding as selector
import test_selected_support_separation_independent as independent
ROOT=Path(__file__).parent
class PermutationTests(unittest.TestCase):
 def test_count_formula_and_partition(self):
  saved=json.loads((ROOT/'permuted-standard-domain-inventory.json').read_text())
  for label,N in [('full_carriers_0_through_5',96),('primary_carriers_1_through_4',64)]:
   self.assertEqual(sum(r['counts']['full'] for r in saved[label]),N**3)
   for r in saved[label]:
    p=r['standard_tags'];d=sum(a>b for a,b in zip(p,p[1:]));self.assertEqual(r['counts']['full'],math.comb(N+2-d,3))
    self.assertEqual(r['sorting_sign'],(-1)**sum(a>b for i,a in enumerate(p) for b in p[i+1:]))
    self.assertEqual(r['counts']['full'],r['counts'].get('outer_active',0)+r['counts']['outer_inactive'])
  self.assertEqual(sum(r['counts'].get('outer_active',0) for r in saved['primary_carriers_1_through_4']),3072)
 def test_only_guard_changes_in_class(self):
  original=(ROOT/'lower_selected_kernel_denominators.py').read_text().split('\ndef build():')[0]
  expected=original.replace("if tuple(v.standard_tag for v in vertices)!=(3,11,15):raise ValueError('selected staircase only')", "if sorted(v.standard_tag for v in vertices)!=[3,11,15]:raise ValueError('selected staircase multiset only')")
  self.assertEqual((ROOT/'lower_permuted_standard_sector.py').read_text().split('\ndef build(')[0],expected)
 def test_build_changes_only(self):
  original=(ROOT/'lower_primary_carrier_sector.py').read_text();original=original[original.index('def build('):]
  expected=original.replace('def build(masks=(12,13,15), carriers=(1,2,4)):', 'def build(masks=(0,0,0), carriers=(1,2,4), standards=(11,3,15)):').replace('zip(carriers,masks,(3,11,15))','zip(carriers,masks,standards)').replace("'sorting_sign':1", "'sorting_sign':(-1)**sum(standards[i]>standards[j] for i in range(3) for j in range(i+1,3))").replace('standards(3,11,15)', 'standard permutation of(3,11,15)')
  actual=(ROOT/'lower_permuted_standard_sector.py').read_text();actual=actual[actual.index('def build('):];self.assertEqual(actual,expected)
 def test_outer_owner_activity_all_tags(self):
  vs=tuple(lowering.owned.VertexLabel(4,o,c,0,t) for o,(c,t) in enumerate(zip((1,2,4),(11,3,15))))
  lo=lowering.Lower(vs)
  for t,c,m in itertools.product((3,11,15),range(1,5),range(16)):
   v=lowering.owned.VertexLabel(4,0,c,m,t)
   eligible=c<=t.bit_count() and (t!=15 or c==4) and all(not ((m>>i)&1) or ((t>>(3-i))&1) for i in range(4))
   self.assertEqual(lo.quotient(v)==lo.g.c(0),not eligible)
 def test_selector_and_sign(self):
  for tags in itertools.permutations((3,11,15)):
   vs=tuple(lowering.owned.VertexLabel(4,o,c,0,t) for o,(c,t) in enumerate(zip((1,2,4),tags)))
   s=selector.bind_seed(4,vs)
   self.assertEqual(s['coefficient'],-2);self.assertEqual(s['entry'],[12,6]);self.assertEqual(s['tail_owners'],[v.data() for v in vs])
   self.assertEqual(s['left_ast']['op'],'pinned_resolution_rational_block');self.assertEqual(s['left_ast']['args'][1],list(vs[0].data()));self.assertEqual(s['left_ast']['args'][2],'I')
   self.assertEqual(s['right_ast']['args'][1],list(vs[0].data()));self.assertEqual(s['right_ast']['args'][2],'P')
 def test_every_separator_independently(self):
  saved=json.loads((ROOT/'permuted-standard-sector-support.json').read_text());self.assertEqual(saved['counts'],{'active_tuples':704,'certified_zero':704,'unresolved':0})
  seen=set()
  for r in saved['results']:
   cs=tuple(r['carriers']);ms=tuple(r['legal_masks']);self.assertNotIn((cs,ms),seen);seen.add((cs,ms))
   a=lowering.build(ms,cs);self.assertEqual(a['sorting_sign'],-1)
   self.assertEqual(hashlib.sha256(json.dumps(a,sort_keys=True,separators=(',',':')).encode()).hexdigest(),r['dag_sha256'])
   independent.nodes=a['dag'];independent.bound.cache_clear()
   for t in r['multipliers']:
    cert=t['certificate'];self.assertIsNotNone(cert);w=tuple(cert['normal']);b=independent.bound(t['root'],w);self.assertEqual(list(b),cert['multiplier_bounds'])
    shift=[int(t['kind']=='B' and i==t['derivative']) for i in range(4)]
    M=[(0,0,-2,-2)[i]+sum(5321+2*((ms[o]>>i)&1) for o in t['edge']) for i in range(4)];self.assertEqual(M,t['complete_numerator_degree'])
    target=sum(w[i]*((-1,-2,-2,-2)[i]+shift[i]) for i in range(4))
    lo=sum(w[i]*(shift[i] if w[i]>=0 else M[i]) for i in range(4));hi=sum(w[i]*(M[i] if w[i]>=0 else shift[i]) for i in range(4))
    self.assertEqual([lo,hi],cert['full_numerator_projection']);gap=max(target-b[1]-hi,lo-target+b[0]);self.assertGreater(gap,0);self.assertEqual(gap,cert['gap'])
  expected={(cs,ms) for cs in ((1,1,4),(1,2,4)) for ms in itertools.product(*(scan.active_masks(t) for t in (11,3,15))) if list(zip(cs,ms,(11,3,15)))==sorted(zip(cs,ms,(11,3,15)))}
  self.assertEqual(seen,expected)
if __name__=='__main__':unittest.main()
