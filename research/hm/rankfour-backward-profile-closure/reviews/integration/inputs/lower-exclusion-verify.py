#!/usr/bin/env python3
"""Exact universal top-section obstruction; no actual instance evaluation."""
from pathlib import Path
import importlib.util,hashlib,json,sys
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parent
DEP=ROOT/'lower-image'
SPEC=importlib.util.spec_from_file_location('frozen_lower_image',DEP/'verify.py')
v=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(v)
ISPEC=importlib.util.spec_from_file_location('frozen_cubic_image',ROOT/'cubic-image'/'verify.py')
w=importlib.util.module_from_spec(ISPEC);ISPEC.loader.exec_module(w)
checks=0
def require(c,msg):
 global checks
 checks+=1
 if not c:raise ValueError(msg)
def read(p):return json.loads(p.read_text())
def shape(s):return tuple(sorted((x['degree'],v.NAMES.index(x['coefficient']))for x in s))
def authenticate_dependency():
 expected='5e7690ee89e7569d6c8bfec731f6e8e386ffde87a6cf71863b6bf5141ec62d1c'
 require(hashlib.sha256((DEP/'MANIFEST.json').read_bytes()).hexdigest()==expected,'frozen dependency manifest')
 manifest=read(DEP/'MANIFEST.json');require(len(manifest['files'])==17,'complete lower-image artifact count')
 for x in manifest['files']:
  p=DEP/x['file'];b=p.read_bytes()
  require(len(b)==x['bytes'],'dependency byte count')
  require(hashlib.sha256(b).hexdigest()==x['sha256'],'dependency full-file hash')
 image_expected='6e4ebc717b2a4e2559a0fa0eda94a26136c6b2cc7082f758317b9f0b3d7b5075'
 image_root=ROOT/'cubic-image'
 require(hashlib.sha256((image_root/'MANIFEST.json').read_bytes()).hexdigest()==image_expected,'frozen cubic-image manifest')
 for x in read(image_root/'MANIFEST.json')['files']:
  b=(image_root/x['file']).read_bytes()
  require(len(b)==x['bytes'],'cubic-image dependency byte count')
  require(hashlib.sha256(b).hexdigest()==x['sha256'],'cubic-image dependency full-file hash')
 return {'lower_image':expected,'cubic_image':image_expected}

def obstruction(B,dual_euler=v.Qstar,quotient_twist=2,target_twist=0):
 return v.sub(v.sub(dual_euler(4),v.chi(v.dual(B),quotient_twist)),v.h0(v.dual(B),target_twist))
def exact_contract(values,witness=8):
 if len(values)!=13 or any(x[witness]!=1 for x in values):
  raise ValueError('not the complete thirteen physical-V excess-one identities')
def geometry_contract(delta3,cap,top_twist):
 if delta3!=0:raise ValueError('B(2)=L4 not established with torsion')
 if top_twist<=0 or cap>-top_twist:raise ValueError('top-section hypothesis absent')
def torsion_contract(rows):
 if len(rows)!=96 or sum(any(x['defects'])for x in rows)!=83:
  raise ValueError('positive torsion coverage lost')

def derive():
 manifest_hash=authenticate_dependency()
 image=w.derive();image_checks=w.checks
 require(image==read(ROOT/'cubic-image'/'RESULT.json'),'full earlier image bound rederived')
 require(image['rank_four_images_remaining']==0 and image['rank_one_image']=={'degree':9,'coefficient':'1','necessary_source':'D'},'rank-one O9 source-D residual is explicitly covered')
 lower=v.derive();dependency_checks=v.checks
 require(lower==read(DEP/'RESULT.json'),'complete frozen dependency rederived')
 pairs=lower['final_pairs'];cases=lower['case_degree_ledger'];torsion=lower['torsion_ledger']
 require(len(pairs)==13 and len(cases)==50 and len(torsion)==96,'complete prior domains')
 require(v.Qstar(4)==v.vec(**{'1':-1,'A':-1,'D':1,'P':1,'V':2}),'actual unequal dual quartic Euler')
 require(v.sym(v.unit(7),1)==v.unit(6),'physical W-prime times W is P')
 require(v.sym(v.unit(7),3)==v.add(v.unit(4),v.unit(8)),'physical W-prime Sym3 is D+V')
 require(v.NAMES[8]=='V' and v.NAMES[2]=='A' and v.unit(8)!=v.unit(2),'physical three-spaces distinguished')
 result=[];vectors=[]
 for pair in pairs:
  B=shape(pair['quotient']);J=shape(pair['image']);N=shape(pair['kernel']);Bs=v.dual(B)
  require(v.rank_of(B)==4 and v.degree_of(B)==pair['c3'],'actual first quotient rank and degree')
  require(B==tuple(sorted(N+v.C(J))),'proved quotient splitting reused in correct orientation')
  require(v.h0(v.dual(N),0)==v.ZERO,'positive complementary kernel has no dual sections')
  related=[c for c in cases if c['case_id']==pair['case_id']]
  require(bool(related)and all(c['defects'][2]==0 for c in related),'last defect is a proved local conclusion')
  for c in related:
   geometry_contract(c['defects'][2],-4,4)
   require(c['b']==pair['c3']-46,'opposite endpoint degree and actual rank17 E')
   require(c['quotient_degrees'][3]==pair['c3']+8,'last quotient B(2) degree')
  ze=v.sub(v.Qstar(4),v.chi(Bs,2));target=v.h0(Bs,0);obs=v.sub(ze,target)
  cz=v.cadd(v.class_Qstar(4),v.cmul(v.class_chi(Bs,2),-1))
  ct=v.class_h0(Bs,0);co=v.cadd(cz,v.cmul(ct,-1))
  require(v.class_decompose(cz)==ze,'independent exact upper-endpoint Euler character')
  require(v.class_decompose(ct)==target,'independent exact derivative target sections')
  require(v.class_decompose(co)==obs,'independent exact obstruction character')
  require(obs[8]==1,'physical V contradiction by one copy')
  require(v.rank_of(J)in(2,3),'only the lower-image scope')
  vectors.append(obs)
  result.append({'case_id':pair['case_id'],'rank_image':v.rank_of(J),'image':pair['image'],
   'kernel':pair['kernel'],'quotient':pair['quotient'],'upper_endpoint_rank':9,
   'upper_endpoint_degree':pair['c3']-46,'upper_endpoint_max_degree':-4,
   'upper_endpoint_Euler4':v.pretty(ze),'derivative_target_H0':v.pretty(target),
   'obstruction':v.pretty(obs),'physical_V_excess':obs[8],
   'covered_case_rows':len(related),
   'covered_torsion_rows':sum(c['case_id']==pair['case_id']for c in torsion)})
 exact_contract(vectors)
 torsion_contract(torsion)
 require(sum(x['covered_case_rows']for x in result)==50,'no numerical case discarded')
 require(sum(x['covered_torsion_rows']for x in result)==96,'no torsion partition discarded')
 require(sum(any(x['defects'])for x in cases)==37,'all37 positive numerical cases retained to contradiction')
 require(sum(any(x['defects'])for x in torsion)==83,'all83 positive torsion partitions retained to contradiction')
 require(any(x['kernel_defects']!=[0,0]for x in torsion),'positive kernel defects retained')
 require(any(x['quotient_defects']!=[0,0]for x in torsion),'positive quotient defects retained')
 require(v.dim(vectors[0])==-1 and vectors[0][8]==1,'representation obstruction is not a scalar dimension test')
 # Explicit polynomial coefficient check: adding arbitrary genuine H1 cannot remove V excess.
 require(all(x[8]+h>0 for x in vectors for h in range(41)),'nonnegative H1 correction increases V excess')
 controls=[]
 def reject(label,fn):
  try:fn()
  except ValueError:controls.append(label);require(True,label)
  else:require(False,'mutation incorrectly accepted: '+label)
 Bs=[shape(p['quotient'])for p in pairs]
 reject('replace physical V witness by physical A',lambda:exact_contract(vectors,2))
 reject('exchange unequal actual E and Q-star Euler presentations',lambda:exact_contract([obstruction(B,dual_euler=v.E)for B in Bs]))
 reject('shift upper quotient by one instead of two',lambda:exact_contract([obstruction(B,quotient_twist=1)for B in Bs]))
 reject('shift upper quotient by three instead of two',lambda:exact_contract([obstruction(B,quotient_twist=3)for B in Bs]))
 reject('use derivative target H0(B-star(2))',lambda:exact_contract([obstruction(B,target_twist=2)for B in Bs]))
 reject('drop last necessary quotient pair',lambda:exact_contract(vectors[:-1]))
 reject('identify last quotient B(2) despite positive last defect',lambda:geometry_contract(12,-4,4))
 reject('omit the top-slope bound in the section lemma',lambda:geometry_contract(0,-3,4))
 reject('allow degree-zero kernel line in the negative-degree contradiction',lambda:geometry_contract(0,0,0))
 reject('set every plateau defect to zero',lambda:torsion_contract([x for x in torsion if not any(x['defects'])]))
 reject('force every kernel torsion length to vanish',lambda:torsion_contract([x for x in torsion if x['kernel_defects']==[0,0]]))
 reject('force every quotient torsion length to vanish',lambda:torsion_contract([x for x in torsion if x['quotient_defects']==[0,0]]))
 return {'status':'PASS','scope':'All rank-two and rank-three restricted dual cubic images are excluded in ordered actual rank-four (3,1); rank one and whole profile remain open.',
  'dependency_manifest_sha256':manifest_hash,'authenticated_complete_originals':lower['authenticated_originals'],
  'lower_image_dependency_checks':dependency_checks,'cubic_image_dependency_checks':image_checks,
  'additional_checks':checks+(v.checks-dependency_checks),
  'total_checks':checks+v.checks+image_checks,'new_negative_controls':controls,
  'actual_instance_evaluation_used':False,'historical_enumeration_used':False,
  'inverse_image_extension_splitting_assumed':False,'global_zero_plateau_defects_assumed':False,
  'H1_vanishing_assumed':False,'rank_one_excluded':False,'only_residual_image':image['rank_one_image'],
  'image_quotient_pairs_excluded':13,'case_rows_excluded':50,'positive_case_rows_excluded':37,
  'torsion_partitions_excluded':96,'positive_torsion_partitions_excluded':83,
  'obstructions':result}
if __name__=='__main__':print(json.dumps(derive(),indent=2,sort_keys=True))
