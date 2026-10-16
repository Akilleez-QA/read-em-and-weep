"""Literal model support certificate; no polynomial arithmetic or source scan."""
import hashlib,json,subprocess
from pathlib import Path
PIN='08b73637d4136f91606aad332c46cafd064417f8'
PATH='research/hm/current-scalar-geometric-dependencies/data/model.json'
raw=subprocess.check_output(['git','-C',str(Path(__file__).resolve().parents[2]),'show',PIN+':'+PATH])
def check(c,m):
 if not c:raise ValueError(m)
blob=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
check(blob=='fcd48a9a22d40d55ce7a08b8aefcb4eaa2fdf761','model blob')
x=json.loads(raw);check(len(x['charts'])==6,'carriers')
results=[]
for row,col in [(9,3),(10,4)]:
 isup=[];psup=[];both=[];cert=[]
 for b,c in enumerate(x['charts']):
  left=any(c['I'][row]);right=any(r[col] for r in c['P'])
  if left:isup.append(b)
  if right:psup.append(b)
  if left and right:both.append(b)
  else:cert.append({'carrier':b,'I_row_literal_zero':not left,'P_column_literal_zero':not right})
 check(both==[3,4],'expected selector support enclosure')
 # Initial CCBB vertex has exactly two infinity coordinates. Generic
 # partition formula sets primary R_j=0 for j>s and star sorts before0.
 admitted_first=[5,0,1,2]
 key=lambda b:-1 if b==5 else b
 check(all(key(a)<key(b) for a in admitted_first for b in both),'leading carrier separation')
 results.append({'entry':[row,col],'I_row_nonempty':isup,'P_column_nonempty':psup,'intersection_enclosure':both,'literal_zero_witnesses':cert})
print(json.dumps({'status':'pass','model_blob':blob,'selectors':results,'standard_initial':[0,0,1,1],'first_carrier_enclosure':[5,0,1,2],'excluded_seed_ids':[0,1,2,3],'channels':['E12','E34'],'excluded_cells':8,'partition_premise':'fixed parameterized carrier construction PR1 6141322825 section5 at N54; R_j=0 for j>s','source_label_enumerated':False,'physical_source_evaluated':False},sort_keys=True))
