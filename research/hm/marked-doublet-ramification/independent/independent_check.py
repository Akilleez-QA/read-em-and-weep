"""Portable public-input and universal group/local-algebra controls; no HM instances."""
from pathlib import Path
from itertools import product
import hashlib,json,sys,subprocess
root=Path(__file__).resolve().parent
packet=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else root.parent
checks=[]
def ck(s,v):
 if not v:raise RuntimeError(s)
 checks.append(s)
pins={'PROOF.md':'e374e3cb656f64f408832557369e9d5b1cf2bc34efc612820641b99dd81cf4e7','verify.py':'94cf9a481c517e6dbc15b724048144312395aeabef6082bb3b13eb80c21883b3','INPUTS.json':'0f6bda3f423438e1c9b34a6a525b835c5e112209dbe740cbbc67bbdd5079d137','RESULT.json':'05e69682736f49f437a5e47929434c0652be361c83ab015ba4909e20c45e0b80'}
for n,h in pins.items():ck('bound '+n,hashlib.sha256((packet/n).read_bytes()).hexdigest()==h)
auth=json.loads((root/'AUTHENTICATED.json').read_text())
manifest=json.loads((packet/'INPUTS.json').read_text())
for rec in manifest:
 remote=next(a for a in auth if int(a['pr'])==rec['pr'])
 ck('public original matches PR'+str(rec['pr']),remote['content'].encode()==(packet/rec['file']).read_bytes() and remote['sha']==rec['git_blob'])
normal=subprocess.check_output([sys.executable,str(packet/'verify.py')])
optimized=subprocess.check_output([sys.executable,'-O',str(packet/'verify.py')])
ck('151 checks identical normal optimized recorded',normal==optimized==(packet/'RESULT.json').read_bytes() and json.loads(normal)['checks']==151)
# Independent construction of SL(2,F5), not its character table.
p=5
G=[x for x in product(range(p),repeat=4) if (x[0]*x[3]-x[1]*x[2])%p==1]
def mul(a,b):return ((a[0]*b[0]+a[1]*b[2])%p,(a[0]*b[1]+a[1]*b[3])%p,(a[2]*b[0]+a[3]*b[2])%p,(a[2]*b[1]+a[3]*b[3])%p)
def inv(a):return(a[3],-a[1]%p,-a[2]%p,a[0])
one=(1,0,0,1)
ck('SL2F5 order',len(G)==120)
comm={mul(mul(mul(a,b),inv(a)),inv(b)) for a in G for b in G}
closure={one};todo=[one]
while todo:
 a=todo.pop()
 for c in comm:
  v=mul(a,c)
  if v not in closure:closure.add(v);todo.append(v)
ck('SL2F5 perfect by commutator closure',len(closure)==120)
# Exhaust all two-by-two matrices over F3[t]/t^2. This supports only the
# universal local implication, not an actual bundle or source experiment.
simple=0
for v in product(range(3),repeat=8):
 a,b,c,d=v[:4];A,B,C,D=v[4:]
 det0=(a*d-b*c)%3;det1=(a*D+A*d-b*C-B*c)%3
 if det0==0 and det1!=0:
  simple+=1
  if not any((a,b,c,d)):raise RuntimeError('simple determinant but rank zero')
ck('dual-number simple determinant implies residue rank one',simple>0)
result={'status':'pass','checks':checks,'simple_determinant_controls':simple,'matrix_controls':3**8,'scope':'Independent abstract finite group and local algebra controls, plus public source authentication and packet reproduction; no actual HM/source instances','bound_packet_sha256':pins}
print(json.dumps(result,indent=2))
