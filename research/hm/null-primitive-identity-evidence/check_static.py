"""Only byte hashes, selected JSON shape checks and literal skew-pattern comparisons. No model evaluation."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
S=ROOT/'sources'
def need(c,m):
 if not c: raise ValueError(m)
def sha(b):return hashlib.sha256(b).hexdigest()
def blob(b):return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
EXPECTED={'certificates-homogeneous-identities.json': '55e78bbc838a971b64531379788192acf8877c04f2d797fb13b4f4a68e47b018', 'data-model.json': '635bb12d9986e0dcada161d4173c773c4f134b9225354a3bc74267840ca19926', 'manifest.json': '68f8f4ac9ab653dc07134f0c0a40c868a0c1944da2e22415f997e1316dc0698d', 'pinned-model.json': '635bb12d9986e0dcada161d4173c773c4f134b9225354a3bc74267840ca19926', 'verify.py.txt': 'b037eb1fe5d8d3434d793e133eb49e7cbc9e477f71dbadffce4a730559d47984', 'verify_homogeneous_identities.py.txt': 'ad6fdb925262b9661bd51c0f65fe1a48d8f4ab1927bbf14b23786a4f0e1503bf'}
for name,expected in EXPECTED.items():
 need(sha((S/name).read_bytes())==expected,name+' fixed hash mismatch')
manifest=json.loads((S/'manifest.json').read_text())['sha256']
files={'data/model.json':'data-model.json','certificates/homogeneous-identities.json':'certificates-homogeneous-identities.json','checks/verify_homogeneous_identities.py':'verify_homogeneous_identities.py.txt','verify.py':'verify.py.txt'}
hashes={}
for original,local in files.items():
 b=(S/local).read_bytes();need(sha(b)==manifest[original],original+' manifest mismatch')
 hashes[original]={'sha256':sha(b),'git_blob':blob(b),'bytes':len(b)}
m=json.loads((S/'data-model.json').read_text());cert=json.loads((S/'certificates-homogeneous-identities.json').read_text())
pinned=S/'pinned-model.json'
need(pinned.read_bytes()==(S/'data-model.json').read_bytes(),'pinned bytes differ')
need(sha(json.dumps(m,separators=(',',':')).encode())==cert['modelSha256'],'canonical hash mismatch')
need(len(m['charts'])==6,'six carriers')
need([c['pivot'] for c in m['charts']]==[0,1,2,3,4,0],'chart pivots')
for c in m['charts']:
 for k,(rows,cols) in {'I':(15,2),'P':(2,15),'H0':(5,15),'H1':(15,10)}.items():
  need(len(c[k])==rows and all(len(row)==cols for row in c[k]),k+' dimensions')
need(cert['schema']=='hm-negative-coset-identities-v1','receipt schema label')
need(cert['byIdentity']['E_identity']==1350,'A historical count')
need(cert['exactScalarChecks']==3090,'historical total count')
# Each symbol is a literal four-exponent token; v0 denotes the constant token.
tokens=['0,0,0,0','1,0,0,0','0,1,0,0','0,0,1,0','0,0,0,1']
need(len(m['ev'])==2 and all(len(row)==10 for row in m['ev']),'ev shape')
for h,row in enumerate(m['ev']):
 for r,p in enumerate(row):need(p==([[tokens[r%5],1]] if r//5==h else []),'ev literal')
need(len(m['delta'])==10 and all(len(r)==15 for r in m['delta']),'delta shape')
need(all(type(p) is list for row in m['delta'] for p in row),'delta entries are lists')
pairs=[]
for h in range(2):
 for j in range(15):
  nz=[(r,m['delta'][5*h+r][j]) for r in range(5) if m['delta'][5*h+r][j]]
  if not nz:pairs.append({'block':h,'column':j,'zero':True});continue
  need(len(nz)==2,'not pair');(r,p),(s,q)=nz
  need(len(p)==len(q)==1,'not singletons')
  need(p[0][0]==tokens[s] and q[0][0]==tokens[r],'not swapped tokens')
  need(p[0][1] in [-1,1] and q[0][1]==-p[0][1],'not opposite unit coefficients')
  pairs.append({'block':h,'column':j,'r':r,'s':s,'epsilon':p[0][1]})
need(sum(not p.get('zero',False) for p in pairs)==20,'twenty pairs')
need(sum(p.get('zero',False) for p in pairs)==10,'ten zero block columns')
report={'status':'PASS static bindings and literal C pattern only','hashes':hashes,'compactModelSha256':cert['modelSha256'],'historical_A_entry_checks':1350,'A_replayed':False,'C_pattern_pairs':sum(not p.get('zero',False) for p in pairs),'C_zero_blocks':sum(p.get('zero',False) for p in pairs),'pairs':pairs}
print(json.dumps(report,indent=2))
