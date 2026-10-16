"""Independent narrow JC domain-clarification followup; no actual source values."""
import ast,hashlib,json,subprocess,unittest
from pathlib import Path
from unittest.mock import patch
import lift as L
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2];PREFIX='research/codex-swarm/full-lift-domain/'
OLD='ce8b3eeae';NEW='92b2a88ed'
MARKER='88cd12c2a2a90e5300966adc6b01999d6f65559e2b7a8c8d5c36b0946f323ae9'
def git(rev,name):return subprocess.check_output(['git','show',rev+':'+PREFIX+name],cwd=ROOT,timeout=10)
def sha(b):return hashlib.sha256(b).hexdigest()
class StripDomainDescriptions(ast.NodeTransformer):
 def visit_Dict(self,node):
  self.generic_visit(node);ks=[];vs=[]
  for k,v in zip(node.keys,node.values):
   name=k.value if isinstance(k,ast.Constant)else None
   if name in('fully_weighted_Pi_out_value_extends_full_standard_target','prism_full_standard_extension_scope','uncleared_prism_full_standard_extension_claimed'):continue
   ks.append(k);vs.append(ast.Constant(value='domain-description')if name=='regularity_theorem'else v)
  node.keys=ks;node.values=vs;return node
class Followup(unittest.TestCase):
 def test_exact_six_file_diff_and_unchanged_algorithms(self):
  changed=subprocess.check_output(['git','diff','--name-only',OLD,NEW,'--',PREFIX],cwd=ROOT).decode().splitlines()
  self.assertEqual({s.removeprefix(PREFIX)for s in changed},{'PROOF.md','README.md','build_handoff.py','lift-contract.json','lift.py','producer-ready.json'})
  normalize=lambda raw:ast.dump(StripDomainDescriptions().visit(ast.parse(raw)),include_attributes=False)
  self.assertEqual(normalize(git(OLD,'lift.py')),normalize((HERE/'lift.py').read_bytes()))
  for name in('source-pins.json','face-program-example.json','test_lift.py','run_controls.py','controls-normal.log','controls-optimized.log','controls-receipt.json','review-independent.md'):
   self.assertEqual(git(OLD,name),(HERE/name).read_bytes(),name)
  old=git(OLD,'test_independent.py').decode().replace('f08c891d7639d6487efcb65cc9d582e31428bbe48fdd775266d9f4179cf9178e',MARKER)
  self.assertEqual(old,(HERE/'test_independent.py').read_text())
 def test_current_marker_contract_and_scope(self):
  raw=(HERE/'producer-ready.json').read_bytes();self.assertEqual(sha(raw),MARKER)
  marker=json.loads(raw)
  for name,h in marker['files'].items():
   self.assertEqual(sha((HERE/name).read_bytes()),h)
   self.assertEqual(git(NEW,name),(HERE/name).read_bytes())
  c=json.loads((HERE/'lift-contract.json').read_text())
  self.assertIn('H_rho weights inserted owners only',c['whole_standard_extension'])
  for key in('outer_J2_indices_example','outer_delta_J3_seven_owner_indices_example'):
   x=c[key];self.assertTrue(x['fully_weighted_Pi_out_value_extends_full_standard_target'])
   self.assertFalse(x['uncleared_prism_full_standard_extension_claimed'])
   self.assertIn('retained owned suffix divisors',x['prism_full_standard_extension_scope'])
   self.assertTrue(x['index_checks_are_not_source_clearing_proof']);self.assertFalse(x['physical_execution_authorized'])
 def test_formal_suffix_divisor_countercontrol(self):
  # Laurent exponents in independent artificial (inserted,suffix) divisors.
  coefficient=(-1,-1);inserted_weight=(1,0);all_weights=(1,1)
  add=lambda a,b:tuple(x+y for x,y in zip(a,b))
  prism=add(coefficient,inserted_weight);projection=add(coefficient,all_weights)
  self.assertEqual(prism,(0,-1));self.assertLess(prism[1],0)
  self.assertEqual(projection,(0,0));self.assertEqual(add(prism,(0,1)),(0,0))
  # Thus uncleared prism can retain a suffix pole while cleared prism extends.
 def test_imported_domain_section_and_unconditional_gate(self):
  path='research/hm/null-proof-foundations/hm-regular-cover-transport.md'
  raw=subprocess.check_output(['git','show','10810ee877fdaf291399198ad60d7dd0c316a42d:'+path],cwd=ROOT,timeout=10)
  self.assertEqual(hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest(),'1131532f944cf23319329d0904a8c8a4afc8b10e')
  section=raw.decode().split('## 6. The one common pole-domain requirement')[1].split('### 6.1')[0]
  self.assertIn('leaves the original vertex denominators in the allowed domain',section)
  self.assertIn('after multiplication, for each vertex occurrence',section)
  with self.assertRaises(L.I.PhysicalAdmissionMissing):L.actual_coefficient('structural-zero')
if __name__=='__main__':unittest.main()
