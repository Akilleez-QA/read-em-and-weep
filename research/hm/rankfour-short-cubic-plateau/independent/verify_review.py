#!/usr/bin/env python3
"""Reproduce the independent review and exercise real fail-closed controls."""
from pathlib import Path
import hashlib,json,subprocess,sys,tempfile,shutil
ROOT=Path(__file__).resolve().parent

def need(c,m):
 if not c:raise RuntimeError(m)
def run(p,opt=False,cwd=None):
 return subprocess.run([sys.executable]+(['-O'] if opt else [])+[str(p)],cwd=cwd or ROOT,text=True,capture_output=True)
def verify_manifest():
 for p,want in json.loads((ROOT/'MANIFEST.json').read_text())['sha256'].items():
  need(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==want,'manifest mismatch: '+p)
def normal(d):
 return {({'P':'P4','D':'D5'}.get(k,k)):v for k,v in d.items()}
def candidates_comparison(ours,author):
 def key(a,b,B):return (a,b,tuple((r['degree'],{'P':'P4','D':'D5'}.get(r['coefficient'],r['coefficient'])) for r in B))
 left={key(*r['endpoint_degrees'],r['B']):(r['F0_twist4_Euler'],r['quartic_pass'],r.get('full_Euler_residuals',{}).get('0')) for r in ours['cubic_candidates']}
 right={key(r['a'],r['b'],r['B']):(normal(r['F0_quartic_Euler']),r['passes_quartic'],normal(r['upper_Euler_residual']) if 'upper_Euler_residual' in r else None) for r in author['candidates']}
 need(left==right and len(left)==13,'all thirteen candidates and exact residuals agree')

def main():
 verify_manifest()
 runs=[]
 for rel,result in [('independent_check.py','RESULT.json'),('reviewed_author/verify.py','reviewed_author/RESULT.json')]:
  for opt,cwd in [(False,ROOT),(True,ROOT),(False,Path('/tmp'))]:
   r=run(ROOT/rel,opt,cwd)
   need(r.returncode==0,r.stderr)
   need(r.stdout==(ROOT/result).read_text(),'nonreproducible output '+rel)
   runs.append({'program':rel,'optimized':opt,'other_working_directory':cwd!=ROOT,'status':'PASS'})
 ours=json.loads((ROOT/'RESULT.json').read_text());author=json.loads((ROOT/'reviewed_author/RESULT.json').read_text())
 candidates_comparison(ours,author)
 controls=[]
 with tempfile.TemporaryDirectory(prefix='rankfour-universal-audit-') as temp:
  base=Path(temp)/'packet';shutil.copytree(ROOT,base,ignore=shutil.ignore_patterns('__pycache__','CONTROLS.json'))
  def mutate(rel,new,programs,expected,label):
   path=base/rel;original=path.read_text();path.write_text(new)
   try:
    for prog in programs:
     r=run(base/prog,cwd=Path('/tmp'))
     need(r.returncode!=0 and expected in r.stderr,'mutation was not rejected correctly: '+label+' '+r.stderr)
     controls.append({'mutation':label,'program':prog,'rejected':True})
   finally:path.write_text(original)
  for registry,prefix,prog in [(ours,'','independent_check.py'),(author,'reviewed_author/','reviewed_author/verify.py')]:
   for source in json.loads((base/prefix/'INPUTS.json').read_text()):
    rel=prefix+source['file'];raw=(base/rel).read_text()
    mutate(rel,raw+'\n',[prog],'source SHA256','one-byte source corruption: '+Path(rel).name)
   rel=prefix+'INPUTS.json';data=json.loads((base/rel).read_text());data[0]['ref']='0'*40
   mutate(rel,json.dumps(data),[prog],'source ref' if not prefix else 'pinned original ref','changed immutable source ref')
  for prog in ['independent_check.py','reviewed_author/verify.py']:
   source=(base/prog).read_text()
   mutate(prog,source.replace('PARITY=(0,1,0,1,0,1,0,1,0)','PARITY=(0,1,1,1,0,1,0,1,0)',1),[prog],
          'parity' if prog=='independent_check.py' else 'parity','wrong A central parity')
   if prog=='independent_check.py':
    mutated=source.replace('ZERO=(0,)*9','CHARS[2],CHARS[8]=CHARS[8],CHARS[2]\nZERO=(0,)*9',1)
    expected='fixed W gives A, not V'
   else:
    mutated=source.replace('def char_eval(v,k):','CHARS[2],CHARS[8]=CHARS[8],CHARS[2]\ndef char_eval(v,k):',1)
    expected='McKay vs exact class product'
   mutate(prog,mutated,[prog],expected,'swap A and V while keeping physical W fixed')
  prog='independent_check.py';source=(base/prog).read_text()
  mutate(prog,source.replace('def chi(B,t):return sub(h0(B,t),h1(B,t))','def chi(B,t):return h0(B,t)'),[prog],
         'source split vs actual presentation Euler','discard all H1 tails')
  mutated=json.loads(json.dumps(author));mutated['candidates']=mutated['candidates'][:-1]
  try:candidates_comparison(ours,mutated)
  except RuntimeError:controls.append({'mutation':'omit one cubic candidate','program':'cross-comparison','rejected':True})
  else:raise RuntimeError('missing candidate was not detected')
  mutated=json.loads(json.dumps(author));row=next(x for x in mutated['candidates'] if 'upper_Euler_residual' in x);row['upper_Euler_residual']={}
  try:candidates_comparison(ours,mutated)
  except RuntimeError:controls.append({'mutation':'replace nonzero Euler obstruction by zero','program':'cross-comparison','rejected':True})
  else:raise RuntimeError('zero residual mutation was not detected')
 return {'status':'PASS','normal_optimized_and_portability_runs':runs,'thirteen_candidate_comparison':'PASS',
         'mutation_rejections':len(controls),'controls':controls,'independent_checks':ours['checks'],
         'author_checks':author['checks'],'author_internal_mutation_rejections':author['mutation_rejections']}

if __name__=='__main__':print(json.dumps(main(),indent=2,sort_keys=True))
