"""Bind the actual153-node finite source DAG without running physical coefficients."""
import hashlib,json,subprocess
from pathlib import Path
from interfaces import FullOwner,need,require_synthetic,sorted_source,exponent
from polynomial_coefficients import Catalog,ClearedSourceProgram,Budget
SOURCE_COMMIT='82a8785d0a23e8d4e44e9ca4f52c8bb24fdadbdc'
SOURCE_PATH='research/codex-swarm/whole-source-clearing/source-integration.json'
SOURCE_SHA='a7070e531edd2d034c7ddac8899cf4fcc7e880d4bb3adf5d0d37c8abb7b86a4c'
MODEL_COMMIT='10810ee877fdaf291399198ad60d7dd0c316a42d'
MODEL_PATH='research/hm/null-operator-compiler/hm-pinned-model.json'
MODEL_SHA='635bb12d9986e0dcada161d4173c773c4f134b9225354a3bc74267840ca19926'

def read(repo,c,p,sha):
 raw=subprocess.check_output(['git','show',c+':'+p],cwd=repo,timeout=10)
 need(hashlib.sha256(raw).hexdigest()==sha,'source program pin drift')
 return json.loads(raw)

def actual_program_definition(repo):
 a=read(repo,SOURCE_COMMIT,SOURCE_PATH,SOURCE_SHA)['finite_actual_source_clearing']
 need(a['schema']=='whole-F-finite-factored-clearing-v1'and a['pair']==[0,1],'whole finiteF schema')
 need(len(a['dag'])==153 and a['cleared_P']==152,'actual finite source DAG identity')
 raw=subprocess.check_output(['git','show',TRANSFER_COMMIT+':'+TRANSFER_PATH],cwd=repo,timeout=10)
 need(hashlib.sha256(raw).hexdigest()==TRANSFER_SHA,'raw-pair transfer proof pin drift')
 model=read(repo,MODEL_COMMIT,MODEL_PATH,MODEL_SHA)
 return a,Catalog('physical',model['charts'])

TRANSFER_COMMIT='02d0e727ffb95dfd9281906cc284c56e8bffd018'
TRANSFER_PATH='research/hm/null-source-integration/complementary-pair/PROOF.md'
TRANSFER_SHA='edf2efafdb0f1891af0c9adf02a133e683633466686813e0f8aba48f85abe6bc'

def pair_nodes(nodes,pair):
 """Rename raw formula axes only. Input slots and target-source ordering stay fixed."""
 need(pair in((0,1),(2,3)), 'unsupported ordered source pair')
 if pair==(0,1):return nodes
 out=[];sigma=(2,3,0,1)
 for row in nodes:
  op,*args=row
  if op=='owned_polynomial_factor':
   slot,kind,axis=args[0];args=[[slot,kind,sigma[axis]if kind=='ell'else axis]]
  elif op in('mask_times_x_squared_plus_one_over_two','binary_mask_q_numerator'):
   axis_slot=1 if op=='mask_times_x_squared_plus_one_over_two'else 2
   args[axis_slot]=sigma[args[axis_slot]]
  elif op=='polynomial_partial_after_elementary_substitution':args[1]=sigma[args[1]]
  out.append([op,*args])
 return out

class ProgramOracle:
 def __init__(self,definition,catalog,budget=None):
  self.definition=definition;self.catalog=catalog;self.mode=catalog.mode;self.budget=budget or Budget();self.programs={}
 def validate(self,owners,pair):
  need(pair in((0,1),(2,3)), 'unsupported ordered source pair')
  need(len(owners)==3 and all(isinstance(o,FullOwner)for o in owners)and tuple(owners)==sorted_source(owners)[0],'sorted SOURCE triple required')
 def program(self,owners,pair=(0,1)):
  self.validate(owners,pair);key=(tuple(owners),pair)
  if key not in self.programs:
   need(len(self.programs)<128,'source-program metadata cache cap')
   self.programs[key]=ClearedSourceProgram(pair_nodes(self.definition['dag'],pair),self.definition['cleared_P'],self.catalog,owners,self.budget)
  return self.programs[key]
 def degree_upper(self,owners,pair=(0,1)):
  self.validate(owners,pair)
  if self.mode=='physical':
   d=sum(4 if v.carrier==5 else 5 for v in owners)
   return tuple(14*d+(sum(1+2*((v.legal_mask>>i)&1)for v in owners)-2 if i in pair else 0)for i in range(4))
  return self.program(owners,pair).degree_upper()
 def coefficient(self,owners,e,pair=(0,1)):
  require_synthetic(self.mode);exponent(e)
  return self.program(owners,pair).coefficient(e)
 def alternating_coefficient(self,owners,e,pair=(0,1)):
  require_synthetic(self.mode);ordered,sign=sorted_source(owners)
  return sign*self.coefficient(ordered,e,pair)
