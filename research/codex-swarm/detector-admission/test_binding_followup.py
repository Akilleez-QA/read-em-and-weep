"""Independent byte-only transitive-binding mutations; no physical imports/runs."""
import ast,copy,hashlib,importlib.util,json,shutil,sys,tempfile,unittest
from pathlib import Path
from unittest.mock import patch
HERE=Path(__file__).resolve().parent
BASE=HERE.parent
sys.dont_write_bytecode=True
MARKER='b4ab5a47e4b3a64d11e674ce7a163ff959b16f0c3ad22216541e43a23a8e9b6b'

def sha(raw):return hashlib.sha256(raw).hexdigest()
def load(name,path):
 spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);sys.modules[name]=m;spec.loader.exec_module(m);return m

def frozen():
 raw=(HERE/'producer-ready.json').read_bytes()
 if sha(raw)!=MARKER:raise ValueError('independent AC marker mismatch')
 marker=json.loads(raw)
 for n,h in marker['files'].items():
  if Path(n).name!=n or sha((HERE/n).read_bytes())!=h:raise ValueError('AC producer drift')
 return sha(raw)

class BindingFollowup(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.before=frozen();cls.WE=load('ac_binding_WE',HERE/'whole_envelope.py')
  cls.runner=load('ac_binding_runner',BASE/'wave7/run_controls.py')
 @classmethod
 def tearDownClass(cls):
  if frozen()!=cls.before:raise ValueError('producer changed during independent review')
 def stage(self,root):
  B=Path(root)/'codex-swarm';src=BASE/'detector-realization';dst=B/'detector-realization';dst.mkdir(parents=True)
  marker=json.loads((src/'producer-ready.json').read_bytes())
  for n in [*marker['files'],'producer-ready.json']:shutil.copyfile(src/n,dst/n)
  pins=json.loads((src/'source-pins.json').read_bytes())
  for row in pins['local_dependencies']:
   p=B/row['path'];p.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(BASE/row['path'],p)
  return B,pins
 def envelope(self,B):
  with patch.object(self.WE,'BASE',B):return self.WE.build()
 def test_01_clean_byte_only_rebuild(self):
  with tempfile.TemporaryDirectory()as t:
   B,pins=self.stage(t);got=self.envelope(B)
   self.assertEqual(got,json.loads((HERE/'whole-route-envelope.json').read_bytes()))
   self.assertEqual(len(pins['local_dependencies']),10);self.assertFalse(got['physical_admission'])
 def test_02_same_AST_parity_change_rejected(self):
  with tempfile.TemporaryDirectory()as t:
   B,_=self.stage(t);p=B/'inserted-coefficients/interfaces.py';text=p.read_text();old='sign=(-1)**sum(';new='sign=(+1)**sum('
   self.assertIn(old,text);changed=text.replace(old,new,1)
   self.assertEqual(sum(1 for _ in ast.walk(ast.parse(text))),sum(1 for _ in ast.walk(ast.parse(changed))))
   p.write_text(changed)
   with patch.object(self.WE.ast,'parse',side_effect=AssertionError('AST reached before dependency refusal')):
    with self.assertRaises((ValueError,FileNotFoundError)):self.envelope(B)
 def test_03_each_declared_dependency_corruption_before_AST(self):
  pins=json.loads((BASE/'detector-realization/source-pins.json').read_bytes())
  for row in pins['local_dependencies']:
   with self.subTest(path=row['path']),tempfile.TemporaryDirectory()as t:
    B,_=self.stage(t);p=B/row['path'];p.write_bytes(p.read_bytes()+b'\n# corruption\n')
    with patch.object(self.WE.ast,'parse',side_effect=AssertionError('AST reached before dependency refusal')):
     with self.assertRaises((ValueError,FileNotFoundError)):self.envelope(B)
 def test_04_each_declared_dependency_missing_before_AST(self):
  pins=json.loads((BASE/'detector-realization/source-pins.json').read_bytes())
  for row in pins['local_dependencies']:
   with self.subTest(path=row['path']),tempfile.TemporaryDirectory()as t:
    B,_=self.stage(t);(B/row['path']).unlink()
    with patch.object(self.WE.ast,'parse',side_effect=AssertionError('AST reached before dependency refusal')):
     with self.assertRaises((ValueError,FileNotFoundError)):self.envelope(B)
 def test_05_SR_marker_and_own_byte_drift_rejected(self):
  for name in('producer-ready.json','program.py','source-pins.json'):
   with self.subTest(name=name),tempfile.TemporaryDirectory()as t:
    B,_=self.stage(t);p=B/'detector-realization'/name;p.write_bytes(p.read_bytes()+b' ')
    with self.assertRaises(ValueError):self.envelope(B)
 def synthetic_runner(self,t):
  root=Path(t);declared={'dep/alpha.py':sha(b'alpha'),'dep/beta.md':sha(b'beta')}
  for n,raw in [('dep/alpha.py',b'alpha'),('dep/beta.md',b'beta')]:
   p=root/n;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(raw)
  return root,declared
 def test_06_runner_exact_snapshot_and_drift(self):
  with tempfile.TemporaryDirectory()as t:
   root,d=self.synthetic_runner(t)
   with patch.object(self.runner,'ROOT',root):
    self.assertEqual(self.runner.verify_dependency_snapshot(d,d),d)
    (root/'dep/alpha.py').write_bytes(b'changed')
    with self.assertRaises(ValueError):self.runner.verify_dependency_snapshot(d,d)
 def test_07_runner_omission_extra_path_digest_rejection(self):
  with tempfile.TemporaryDirectory()as t:
   root,d=self.synthetic_runner(t)
   with patch.object(self.runner,'ROOT',root):
    for snapshot in ({},dict(d,extra='0'*64)):
     with self.subTest(snapshot=snapshot),self.assertRaises(ValueError):self.runner.verify_dependency_snapshot(snapshot,d)
    for n in('../outside','/absolute','dep//alpha.py','dep/./alpha.py'):
     with self.subTest(path=n),self.assertRaises(ValueError):self.runner.verify_dependency_snapshot({n:'0'*64},{n:'0'*64})
    with self.assertRaises(ValueError):self.runner.verify_dependency_snapshot({'dep/alpha.py':'bad'},{'dep/alpha.py':'bad'})
    (root/'dep/alpha.py').unlink()
    with self.assertRaises(FileNotFoundError):self.runner.verify_dependency_snapshot(d,d)
 def test_08_runner_symlink_escape_rejected(self):
  with tempfile.TemporaryDirectory()as t,tempfile.TemporaryDirectory()as outside:
   root,d=self.synthetic_runner(t);p=Path(outside)/'payload';p.write_bytes(b'alpha')
   (root/'dep/alpha.py').unlink();(root/'dep/alpha.py').symlink_to(p)
   with patch.object(self.runner,'ROOT',root),self.assertRaises(ValueError):self.runner.verify_dependency_snapshot(d,d)

 def test_09_authenticated_manifest_malformed_records_refused(self):
  original=json.loads((BASE/'detector-realization/source-pins.json').read_bytes())
  for kind in ('schema','missing-list','unsafe-path','bad-digest','duplicate-count'):
   with self.subTest(kind=kind),tempfile.TemporaryDirectory()as t:
    B,_=self.stage(t);p=B/'detector-realization/source-pins.json';pins=copy.deepcopy(original)
    if kind=='schema':pins={'schema':'wrong'}
    elif kind=='missing-list':pins.pop('local_dependencies')
    elif kind=='unsafe-path':pins['local_dependencies'][0]['path']='../../outside'
    elif kind=='bad-digest':pins['local_dependencies'][0]['sha256']='not-a-digest'
    else:pins['local_dependencies'].append(pins['local_dependencies'][0])
    p.write_text(json.dumps(pins))
    # The immutable marker authenticates this manifest itself. Do not forge a
    # new producer anchor to ask a frozen release to trust altered declarations.
    with patch.object(self.WE.ast,'parse',side_effect=AssertionError('AST reached')):
     with self.assertRaises(ValueError):self.envelope(B)
 def test_10_actual_route_certificate_reaches_same_transitive_guard(self):
  AC=load('ac_binding_certifier',HERE/'certifier.py')
  with tempfile.TemporaryDirectory()as t:
   B,_=self.stage(t)
   for row in json.loads((HERE/'source-pins.json').read_bytes())['workspace_inputs']:
    p=B/row['path'];p.parent.mkdir(parents=True,exist_ok=True)
    if not p.exists():shutil.copyfile(BASE/row['path'],p)
   with patch.object(AC,'BASE',B),patch.object(AC.A06,'__file__',str(B/'arithmetic/ledger/schedule_validator.py')),patch.object(self.WE,'BASE',B),patch.dict(sys.modules,{'whole_envelope':self.WE}):
    got=AC.actual_route_certificate();self.assertEqual(got,json.loads((HERE/'blocked-route.json').read_bytes()));self.assertFalse(got['physical_release'])
    p=B/'inserted-coefficients/interfaces.py';p.write_text(p.read_text().replace('sign=(-1)**sum(','sign=(+1)**sum(',1))
    with self.assertRaises(ValueError):AC.actual_route_certificate()
    with self.assertRaises(RuntimeError):AC.actual_admission()
 def test_11_runner_declared_union_and_immutable_records(self):
  with tempfile.TemporaryDirectory()as t:
   root,d=self.synthetic_runner(t);prefix=root/'research/codex-swarm'
   for lane in ('detector-realization','detector-admission'):(prefix/lane).mkdir(parents=True)
   sr={'local_dependencies':[{'path':'a.py','sha256':sha(b'a')}], 'git_objects':[
    {'commit':str(i)*40,'path':'immutable/'+str(i),'sha256':sha(str(i).encode())}for i in (1,2,3)]}
   ac={'workspace_inputs':[{'path':'b.md','sha256':sha(b'b')}]}
   (prefix/'a.py').write_bytes(b'a');(prefix/'b.md').write_bytes(b'b')
   (prefix/'detector-realization/source-pins.json').write_text(json.dumps(sr));ap=prefix/'detector-admission/source-pins.json';ap.write_text(json.dumps(ac))
   union={'research/codex-swarm/'+r['path']:r['sha256']for r in sr['local_dependencies']+ac['workspace_inputs']}
   bindings={'dependency_snapshot':union,'immutable_input_pins':sr['git_objects']}
   def byte_only(argv,**kw):
    self.assertEqual(argv[:2],['git','show']);return argv[2][0].encode()
   with patch.object(self.runner,'ROOT',root),patch.object(self.runner.subprocess,'check_output',side_effect=byte_only):
    got,objects=self.runner.dependency_inputs(bindings);self.assertEqual(got,union);self.assertEqual(len(objects),3)
    for key in ('dependency_snapshot','immutable_input_pins'):
     bad=copy.deepcopy(bindings)
     if key=='dependency_snapshot':bad[key].pop(next(iter(union)))
     else:bad[key].pop()
     with self.subTest(key=key),self.assertRaises(ValueError):self.runner.dependency_inputs(bad)
    ac['workspace_inputs'].append({'path':'a.py','sha256':sha(b'conflicting')});ap.write_text(json.dumps(ac))
    with self.assertRaises(ValueError):self.runner.dependency_inputs(bindings)

 def test_12_runner_actual_local_union_bytes_only(self):
  union={};sr_paths=set()
  for lane,key in(('detector-realization','local_dependencies'),('detector-admission','workspace_inputs')):
   for row in json.loads((BASE/lane/'source-pins.json').read_bytes())[key]:
    n='research/codex-swarm/'+row['path']
    if n in union:self.assertEqual(union[n],row['sha256'])
    union[n]=row['sha256']
    if lane=='detector-realization':sr_paths.add(n)
  self.assertEqual(len(sr_paths),10)
  self.assertTrue({'research/codex-swarm/'+n for n in ('inserted-coefficients/interfaces.py','full-source-application/PROOF.md','physical-homogenization/PROOF.md')}<=sr_paths)
  self.assertEqual(self.runner.verify_dependency_snapshot(union,union),union)

if __name__=='__main__':unittest.main()
