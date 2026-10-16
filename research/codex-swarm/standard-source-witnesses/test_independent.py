"""SW-R independent coefficient-free/artificial adversarial controls."""
import unittest,itertools,json,hashlib,subprocess
from copy import deepcopy
from pathlib import Path
from fractions import Fraction
import witnesses as W

HERE=Path(__file__).resolve().parent

def owners(tags):
 return tuple(W.I.FullOwner(30,('independent',j),c,m,t)for j,(c,m,t)in enumerate(zip((5,0,3),(0,5,15),tags)))

def independent_c(o,p):
 return tuple(14*(4 if o.carrier==5 else 5)+(1+2*((o.legal_mask>>i)&1)if i in p else 0)for i in range(4))

class Independent(unittest.TestCase):
 def test_all_standard_triples_extension_arithmetic(self):
  # 16^3 tagged intersections, each pair. No source/fiber data.
  for tags in itertools.product(range(16),repeat=3):
   for p in((0,1),(2,3)):
    os=owners(tags);cs=[independent_c(o,p)for o in os]
    D=tuple(sum(c[i]for c in cs)-2*(i in p)for i in range(4))
    self.assertEqual(W.numerator_degree(os,p),D)
    qs=[{tuple(-c[i]if(t>>(3-i))&1 else 0 for i in range(4)):1}for c,t in zip(cs,tags)]
    pe=tuple(D[i]if all((t>>(3-i))&1 for t in tags)else 0 for i in range(4))
    out=W.synthetic_extension_control(os,p,{pe:Fraction(2,3)},qs)
    ee=next(iter(out));self.assertEqual(out[ee],Fraction(2,3))
    for i in range(4):
     states={(t>>(3-i))&1 for t in tags}
     if states=={0}:self.assertGreaterEqual(ee[i],0)
     if states=={1}:self.assertLessEqual(ee[i],-2*(i in p))
 def test_uniform_degree_and_common_local_substitutes_fail(self):
  os=owners((15,15,15));p=(0,1);cs=[independent_c(o,p)for o in os]
  qs=[{tuple(-z for z in c):1}for c in cs]
  D=W.numerator_degree(os,p);wrong=list(D);wrong[0]+=1
  self.assertLessEqual(wrong[0],217)
  with self.assertRaises(ValueError):W.synthetic_extension_control(os,p,{tuple(wrong):1},qs)
  bad=deepcopy(qs);bad[0]={(0,0,0,0):1}
  with self.assertRaises(ValueError):W.synthetic_extension_control(os,p,{(0,0,0,0):1},bad)
 def test_all_candidate_hashes_never_prove_truth(self):
  x=W.proposal(owners((12,0,8)),(0,1))
  for slot in x['obligations']:x['obligations'][slot]={'status':'candidate','candidate_proof_sha256':'f'*64}
  result=W.validate_proposal(x)
  self.assertFalse(result['actual_source_identity_accepted']);self.assertFalse(result['admitted'])
  for key in('admitted','physical_execution_authorized','actual_source_evaluated','source_faithful_oracle_identity_accepted'):
   for forged in(True,0,1,'false'):
    y=deepcopy(x);y[key]=forged
    with self.assertRaises(ValueError):W.validate_proposal(y)
  for slot in x['obligations']:
   y=deepcopy(x);y['obligations'][slot]['status']='verified'
   with self.assertRaises(ValueError):W.validate_proposal(y)
  with self.assertRaises(W.I.PhysicalAdmissionMissing):W.require_actual_admission(x)
 def test_source_scope_sign_and_full_owner_mutations(self):
  x=W.proposal(owners((12,0,8)),(2,3))
  mutations=[lambda y:y.update(numerator_scope='trace_only'),lambda y:y.update(extension_scope='common_local_only'),
   lambda y:y.update(source_sorting_sign=-y['source_sorting_sign']),lambda y:y['target_standard_tags'].__setitem__(0,0),
   lambda y:y['source_sorted_owners'][0].__setitem__(4,7),lambda y:y.update(pair=[3,2])]
  for mutate in mutations:
   y=deepcopy(x);mutate(y)
   with self.assertRaises(ValueError):W.validate_proposal(y)
 def test_immutable_proof_pin_authentication_only(self):
  pins=json.loads((HERE/'source-pins.json').read_text());repo=HERE.parents[2]
  for row in pins['immutable_proof_dependencies']:
   raw=subprocess.check_output(['git','show',row['commit']+':'+row['path']],cwd=repo,timeout=10)
   self.assertEqual(hashlib.sha256(raw).hexdigest(),row['sha256'])
   self.assertEqual(len(raw),row['bytes'])
   blob=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
   self.assertEqual(blob,row['git_blob'])

if __name__=='__main__':unittest.main()
