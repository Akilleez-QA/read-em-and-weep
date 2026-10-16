"""Independent metadata binder: no source-polynomial arithmetic."""
import hashlib,itertools,json,subprocess
from pathlib import Path
PIN='5df68750f766b18a746e50bff662b09829225ab1'
PATH='research/hm/null-support-certificates/seed-fingerprint.json'
raw=subprocess.check_output(['git','-C',str(Path(__file__).resolve().parents[2]),'show',PIN+':'+PATH])
x=json.loads(raw)
def check(c,m):
 if not c:raise ValueError(m)
check(x['schema']=='null-selector-seed-fingerprint-v1','schema')
check(x['source_commit']=='08b73637d4136f91606aad332c46cafd064417f8','source')
check(x['standard_bits']=='coordinate i uses bit 3-i','standard bits')
check(x['legal_mask_bits']=='coordinate i uses bit i','mask bits')
check(x['star_carrier']=='canonical carrier 5, sorting key -1 only','star')
check(x['seed_count']==len(x['seeds'])==78,'count')
# q4 row/lift minus signs cancel: effective selector coefficients +1,+1.
rows={2:[([9,3],1),([10,4],1),([12,6],-2)],3:[([0,3],1),([2,6],2),([10,1],1),([12,5],2)],4:[([0,0],1),([10,0],1)]}
kappas={2:[-1,-2,-2,-2],3:[-1,-2,-3,-3],4:[-1,-2,-3,-4]}
words=[([['I',0]],[['P',0]]),([['I',0]],[['P',0]]),([['I',0]],[['P',0]]),([['H',0],['I',1]],[['P',1]]),([['H',0],['I',1]],[['P',1]]),([['E',0],['I',1]],[['P',1],['H',0]]),([['E',0],['I',1]],[['P',1],['H',0]]),([['H',0],['E',1],['I',2]],[['P',2],['H',1]]),([['E',0],['E',1],['I',2]],[['P',2],['H',1],['H',0]])]
seed=0;row=0;mapping=[]
for q,rr in rows.items():
 for entry,c in rr:
  for localperm,p in enumerate(itertools.permutations(range(q))):
   sign=(-1)**sum(p[i]>p[j] for i in range(q) for j in range(i+1,q))
   cur=sum(1<<(3-i) for i in range(q,4));std=[cur]
   for i in p:cur|=1<<(3-i);std.append(cur)
   expected={'seed':seed,'row':row,'entry':entry,'coefficient':c*sign,'kappa':kappas[q],'standard':std,'tail':list(range(q-2,q+1)),'deleted_prefix_owners':list(range(q-2)),'weighted_owners':list(range(q+1)),'kernel_owners':list(range(q-1)),'left':words[row][0],'right':words[row][1]}
   actual=x['seeds'][seed]
   check(actual==expected,'metadata mismatch seed '+str(seed))
   mapping.append((seed,q,(row-(0 if q==2 else 3 if q==3 else 7))*len(list(itertools.permutations(range(q))))+localperm))
   seed+=1
  row+=1
check(seed==78,'enumeration')
print(json.dumps({'status':'pass','fingerprint_sha256':hashlib.sha256(raw).hexdigest(),'checked_seeds':seed,'reserved':{'seed':4,'q':2,'local_rank':4,'worker':'Codex-C02','channel':'E12','standard':[3,11,15],'coefficient':-2},'mapping':'q2 seed=r; q3 seed=6+r; q4 seed=30+r','source_label_coverage':'unproved','physical_source_evaluated':False},sort_keys=True))
