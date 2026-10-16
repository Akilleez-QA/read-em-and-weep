"""Higher-selector AND/OR support, no source arithmetic; excludes q2/seed4 work."""
import subprocess,json,hashlib,itertools,collections
from pathlib import Path
PIN='08b73637d4136f91606aad332c46cafd064417f8'
raw=subprocess.check_output(['git','-C',str(Path(__file__).resolve().parents[2]),'show',PIN+':research/hm/current-scalar-geometric-dependencies/data/model.json'])
def check(c,m):
 if not c:raise ValueError(m)
check(hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()=='fcd48a9a22d40d55ce7a08b8aefcb4eaa2fdf761','blob')
m=json.loads(raw)
B={n:[[[bool(p) for p in row] for row in c[n]] for c in m['charts']] for n in ['I','P','H0','H1']}
def mul(a,b):
 check(len(a[0])==len(b),'shape')
 return [[any(x and b[k][j] for k,x in enumerate(row)) for j in range(len(b[0]))] for row in a]
def chain(*aa):
 r=aa[0]
 for a in aa[1:]:r=mul(r,a)
 return r
E=[mul(B['I'][a],B['P'][a]) for a in range(6)]
eta=[]
for c in m['charts']:
 eta.append([[i==h*5+c['pivot'] for h in range(2)] for i in range(10)])
def selectors(q,anchors,row):
 a,b,*rest=anchors
 if q==3:
  if row in (3,4):
   r,c=(0,3) if row==3 else (2,6)
   left=chain(B['H0'][a],B['I'][b])[r];right=[rr[c] for rr in B['P'][b]]
  else:
   r,c=(10,1) if row==5 else (12,5)
   left=chain(E[a],B['I'][b])[r];right=[rr[c] for rr in chain(B['P'][b],B['H1'][a])]
 else:
  c=rest[0]
  if row==7:
   left=chain(B['H0'][a],E[b],B['I'][c])[0];right=[rr[0] for rr in chain(B['P'][c],B['H1'][b])]
  else:
   left=chain(E[a],E[b],B['I'][c])[10];right=[rr[0] for rr in chain(B['P'][c],B['H1'][b],eta[a])]
 return [(i,j) for i in range(2) for j in range(2) if right[i] and left[j]]
key=lambda b:-1 if b==5 else b
alphabet=[5,0,1,2,3,4]
result=[]
for q in [3,4]:
 domain=[alphabet[:s+2] for s in range(4-q,5)]
 rawtuples=list(itertools.product(*domain))
 admissible=[]
 for sampled in rawtuples:
  ordered=tuple(sorted(sampled,key=key));anchor=ordered[:q-1]
  if all(key(anchor[j])<key(anchor[j+1]) for j in range(q-2)):
   admissible.append((sampled,ordered,anchor))
 for row in ([3,4,5,6] if q==3 else [7,8]):
  states={a:selectors(q,a,row) for a in itertools.combinations(alphabet,q-1)}
  count=collections.Counter(a for _,_,a in admissible)
  possible={a:paths for a,paths in states.items() if paths and count[a]}
  excluded=sum(count[a] for a,p in states.items() if not p)
  record={'q':q,'row':row,'sampled_domain_size':len(rawtuples),'strict_prefix_sampled_tuples':len(admissible),'strict_prefix_anchor_count':len(count),'boolean_zero_sampled_tuples':excluded,'unknown_sampled_tuples':len(admissible)-excluded,'unknown_anchors':[{'anchor':a,'residual_paths':p,'sampled_tuple_count':count[a]} for a,p in possible.items()],'zero_anchors':[a for a,p in states.items() if not p and count[a]],'anchor_domain':[{'anchor':a,'sampled_tuple_count':v} for a,v in count.items()]}
  result.append(record)
print(json.dumps({'status':'pass','domain':'sampled carrier tuples only; slot j allows star,0..4-q+j; no masks; no q2 work; flag-only superdomain not occupied weights','zero_means':'absence of Boolean path for arbitrary residual; true means UNKNOWN','same_for_all_staircase_permutations':True,'physical_source_evaluated':False,'results':result},sort_keys=True,indent=2))
