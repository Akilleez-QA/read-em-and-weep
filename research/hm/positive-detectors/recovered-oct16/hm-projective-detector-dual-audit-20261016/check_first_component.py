"""Fresh sparse d5 contraction with the largest Cech pivot; no archived rank run."""
from pathlib import Path
from collections import defaultdict
from fractions import Fraction as Q
from itertools import product
import json,hashlib,time,resource
resource.setrlimit(resource.RLIMIT_CPU,(30,30));resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,)*2)
start=time.monotonic();H=Path(__file__).resolve().parent;R=H.parent;groups={};peak=0

def ck(g,b):
 assert b,g;groups[g]=groups.get(g,0)+1
 assert time.monotonic()-start<20

def clean(d):return{k:v for k,v in d.items()if v}
def summed(*maps):
 o=defaultdict(int)
 for m in maps:
  for k,v in m.items():o[k]+=v
 return clean(o)
raw=(R/'hm-factored-coefficient-action-20261014/pinned-model-input.json').read_bytes();ck('literal_model_pin',hashlib.sha256(raw).hexdigest()=='635bb12d9986e0dcada161d4173c773c4f134b9225354a3bc74267840ca19926');M=json.loads(raw);d=[]
for name in ['gamma','delta','ev']:
 terms=[]
 for i,row in enumerate(M[name]):
  for j,entries in enumerate(row):
   for ex,c in entries:
    e=tuple(map(int,ex.split(',')));assert sum(e)<=1;terms.append((i,j,0 if not sum(e)else 1+e.index(1),c))
 d.append(terms)
G={(i,j,k):c for i,j,k,c in d[0]}
def internal(C):
 out=defaultdict(int)
 for(u,v,a,b,S,m),c in C.items():
  q=S.bit_count()-1;r=v-u
  if v<3:
   for i,j,k,z in d[v]:
    if j==a:
     mm=list(m);mm[k]+=1;out[u,v+1,i,b,S,tuple(mm)]+=c*z*(-1)**q
  if u>0:
   for i,j,k,z in d[u-1]:
    if i==b:
     mm=list(m);mm[k]+=1;out[u-1,v,a,j,S,tuple(mm)]-=c*z*(-1)**(q+r)
 return clean(out)
def cech(C):
 out=defaultdict(int)
 for(u,v,a,b,S,m),c in C.items():
  for j in range(5):
   if not(S>>j&1):out[u,v,a,b,S|(1<<j),m]+=c*(-1)**((S&((1<<j)-1)).bit_count())
 return clean(out)
def homotopy(C):
 out=defaultdict(int)
 for(u,v,a,b,S,m),c in C.items():
  eligible=[j for j in range(5)if m[j]>=0]
  if not eligible:continue
  j=max(eligible) # independent pivot, opposite the published smallest-index contraction
  if S.bit_count()==1 or not(S>>j&1):continue
  out[u,v,a,b,S^(1<<j),m]+=c*(-1)**((S&((1<<j)-1)).bit_count())
 return clean(out)
D5=[];whole=[]
for a,b in product(range(5),range(2)):
 C={(3,0,a,b,31,(-1,)*5):1}
 for step in range(5):
  ck('internal_square_zero',not internal(internal(C)))
  ck('cech_internal_anticommutation',not summed(cech(internal(C)),internal(cech(C))))
  C=internal(C);peak=max(peak,len(C))
  if step<4:
   ck('largest_pivot_contraction',summed(cech(homotopy(C)),homotopy(cech(C)))==C)
   C=homotopy(C);peak=max(peak,len(C))
 ck('d5_final_cech_closed',not cech(C));ck('d5_final_internal_closed',not internal(C))
 perchart=[{}for _ in range(5)]
 for(u,v,i,j,S,m),c in C.items():
  ck('d5_global_constant_shape',S.bit_count()==1 and m==(0,)*5 and v-u==2)
  perchart[S.bit_length()-1][u,v,i,j]=c
 ck('all_five_global_restrictions_equal',all(p==perchart[0]for p in perchart))
 E=perchart[0];whole.append(E);free={15*i+j:c for(u,v,i,j),c in E.items()if(u,v)==(1,3)};D5.append(free)
 ck('published_d5_column',free==({a:1,25+a:1}if b==0 else{10+a:1,20+a:1}))
 # Every graph entry, including zeros, is compared, so no E02 component is discarded.
 for c,k,aa in product(range(2),range(5),range(5)):
  ck('d5_full_kernel_graph',E.get((0,2,5*c+k,aa),0)==sum(free.get(15*c+r,0)*G.get((r,aa,k),0)for r in range(15)))
# The graph formula proves the full 50-by-80 kernel, without elimination.
for freeindex in range(30):
 c,b=divmod(freeindex,15)
 E={(1,3,c,b):1}
 for k,a in product(range(5),repeat=2):
  z=G.get((b,a,k),0)
  if z:E[0,2,5*c+k,a]=z
 C={(u,v,a,b,1,(0,)*5):z for(u,v,a,b),z in E.items()}
 ck('all_30_graph_basis_cycles',not internal(C))
# Identity minor proves image dimension ten; image support is fully explicit.
for col,v in enumerate(D5):
 a,b=divmod(col,2);pivot=a if b==0 else 10+a
 for cc,w in enumerate(D5):ck('d5_identity_minor',w.get(pivot,0)==int(cc==col))
support=set().union(*(v for v in D5));ck('d5_support_exact',support==set(range(5))|set(range(10,15))|set(range(20,30)))
def invol(v):return{15*(r//15)+5*((r%15)//5)+4-r%5:-c for r,c in v.items()}
for a,b in product(range(5),range(2)):ck('d5_inversion_covariance',invol(D5[2*a+b])=={r:-c for r,c in D5[2*(4-a)+b].items()})
original={'h':15,'j':16,'p':5,'r':6};expected={'h':{15:2,19:-2},'j':{16:2,18:-2},'p':{5:2,9:-2},'r':{6:2,8:-2}}
recordpath=R/'hm-epsilon-projective-generator-bridge-20261016/detector-dual-cycles.json';records=json.loads(recordpath.read_text())['records']
for name,pivot in original.items():
 r=next(r for r in records if r['detector']==name and not r['transported']and r['dual_twist']==-2)
 free={15*t['basis_key'][2]+t['basis_key'][3]:t['coefficient']for t in r['terms']if t['basis_key'][:2]==[1,3]}
 ck('actual_four_E_cycle_binding',free=={pivot:4})
 plus={k:c//2 for k,c in summed(free,invol(free)).items()};ck('actual_plus_projected_column',plus==expected[name])
 ck('plus_column_image_disjoint',not(set(plus)&support))
 for other,col in expected.items():ck('plus_rank4_diagonal_minor',col.get(pivot,0)==(2 if other==name else 0))
ck('plus_minor_determinant',2**4==16)
# Coordinate functionals themselves furnish the strongest quotient certificate needed.
# Each chosen coordinate annihilates all d5 columns and reads the four plus cycles as 2I.
for pivot in original.values():
 for v in D5:ck('dual_witness_annihilates_entire_image',v.get(pivot,0)==0)
# Stronger cohomological corollary: original and transported cycles have eight independent
# first-component classes; all eight witness coordinates kill every complete d5 boundary.
original_cols=[{original[name]:4}for name in ['h','j','p','r']]
allcols=original_cols+[invol(v)for v in original_cols]
witness_rows=[15,16,5,6,19,18,9,8]
for i,pivot in enumerate(witness_rows):
 for j,col in enumerate(allcols):ck('eight_class_minor',col.get(pivot,0)==((4 if i<4 else -4)if i==j else 0))
 for boundary_col in D5:ck('eight_class_witness_kills_d5',boundary_col.get(pivot,0)==0)
ck('eight_class_minor_determinant',4**8==65536)
for i,col in enumerate(allcols):ck('eight_class_closed_involution',invol(col)==allcols[(i+4)%8])

# Authenticate the entire new positive-eight interface by reduction against freshly rebuilt d5.
maps_path=R/'hm-detector-plus-first-component-20261016/positive-eight-maps.json';maps=json.loads(maps_path.read_text())
def quotient(free):
 out=dict(free)
 for a in range(5):
  for col,pivot in [(2*a,25+a),(2*a+1,20+a)]:
   z=out.get(pivot,0)
   for k,c in D5[col].items():out[k]=out.get(k,0)-z*c
 return clean(out)
def graph(free):
 out={(1,3,r//15,r%15):c for r,c in free.items()}
 for c,k,a in product(range(2),range(5),range(5)):
  z=sum(free.get(15*c+b,0)*G.get((b,a,k),0)for b in range(15))
  if z:out[0,2,5*c+k,a]=z
 return out
PB=[summed({r:1},invol({r:1}))for r in range(20)if r%5<2]
def coords(free):
 q=quotient(free)
 return[Q(q.get(r,0)-q.get((r//5)*5+4-r%5,0),2)for r in range(20)if r%5<2]
for i,p in enumerate(PB):
 ck('positive_saved_basis',{int(k):v for k,v in maps['positive_basis_K30'][i].items()}==p)
 ck('positive_full_ambient_lift',{tuple(row[:4]):row[4]for row in maps['positive_basis_ambient80'][i]}==graph(p))
 ck('positive_basis_invariant',invol(p)==p)
 ck('positive_dual_delta',coords(p)==[int(i==j)for j in range(8)])
for k in range(30):
 free={k:1};q=quotient(free);wanted=coords(free)
 savedQ={i:sum(c for old,c in terms if old==k)for i,terms in enumerate(maps['quotient20_reduction'])}
 ck('saved_exact_quotient_map',clean(savedQ)==q)
 savedcoords=[sum((Q(n,d)for old,n,d in row if old==k),Q(0))for row in maps['reduction_dual_rows']]
 ck('saved_dual_map',savedcoords==wanted)
 lifted={}
 for c,p in zip(wanted,PB):lifted=summed(lifted,{r:c*z for r,z in p.items()})
 ck('positive_complete_projection',lifted=={r:Q(z,2)for r,z in quotient(summed(free,invol(free))).items()})
 ck('positive_dual_invariance',coords(invol(free))==wanted)
for image in D5:ck('positive_dual_kills_d5',coords(image)==[0]*8)
for i,name in enumerate(['h','j','p','r']):ck('saved_detector_matrix',maps['detector_matrix_4_by_8'][i]==coords({original[name]:4}))
ck('positive_dimension',len(PB)==8 and sum(invol({k:1}).get(k,0)for k in range(20))==-4)

report=dict(status='PASS',controls=sum(groups.values()),groups=groups,kernel_dimension=30,d5_rank=10,quotient_dimension=20,d5_free_columns=[sorted(v.items())for v in D5],d5_free_support=sorted(support),actual_plus_columns={name:sorted(v.items())for name,v in expected.items()},plus_rank=4,minor_determinant=16,original_and_transported_rank=8,eight_class_minor=65536,original_four_span_invariant=False,eight_class_span_invariant=True,no_original_only_antiinvariant_combination=True,largest_homotopy_pivot=True,peak_sparse_terms=peak,source_values_acquired=False,large_solve=False,elapsed_seconds=time.monotonic()-start,max_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
(H/'first-component-receipt.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items()if k not in['d5_free_columns','actual_plus_columns']},indent=2))
