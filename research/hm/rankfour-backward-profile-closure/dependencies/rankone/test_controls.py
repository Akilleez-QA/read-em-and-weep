from pathlib import Path
import tempfile,subprocess,sys,json
ROOT=Path(__file__).resolve().parent;src=(ROOT/'verify.py').read_text()
mutations=[('image_twist','J=((9,0),)','J=((7,0),)'),('domain_count','len(domain)==53','len(domain)==52'),('kernel_rank','c.rank_of(N)==3','c.rank_of(N)==2'),('extension_twist','c.ext_character(J,N)==c.ZERO','c.ext_character(((1,0),),N)==c.ZERO'),('endpoint_degree','a=-24 if d==-2 else -30','a=-22 if d==-2 else -30'),('upper_E_Q_swap','c.Qstar(4)','c.E(4)'),('upper_dual_twist','c.chi(dual,2)','c.chi(dual,1)'),('physical_V_A','eul[8]==1 and target[8]==0','eul[2]==1 and target[2]==0')]
results=[]
with tempfile.TemporaryDirectory() as td:
 d=Path(td);(d/'dependency').symlink_to(ROOT/'dependency',target_is_directory=True)
 for name,old,new in mutations:
  if old not in src:raise RuntimeError('Mutation target absent '+name)
  (d/'verify.py').write_text(src.replace(old,new,1))
  r=subprocess.run([sys.executable,str(d/'verify.py')],capture_output=True,text=True)
  if r.returncode==0:raise RuntimeError('Mutation survived '+name)
  results.append({'name':name,'rejected':True})
print(json.dumps(results,indent=2))
