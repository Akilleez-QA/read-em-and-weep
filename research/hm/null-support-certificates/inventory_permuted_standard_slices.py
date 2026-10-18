"""Finite labels only. No physical source evaluation."""
import itertools,json
from collections import Counter
from pathlib import Path
T=(3,11,15)
def rank(v):
 c,m,t=v
 return (-1 if c==5 else c,m,t)
def active(v):
 c,m,t=v
 return (c==5 or (c<=t.bit_count() and (t!=15 or c==4))) and all(not ((m>>i)&1) or ((t>>(3-i))&1) for i in range(4))
def inventory(carriers):
 counts={p:Counter() for p in itertools.permutations(T)};sectors={p:Counter() for p in counts}
 for pairs in itertools.product(tuple(itertools.product(carriers,range(16))),repeat=3):
  vs=sorted((*v,t) for v,t in zip(pairs,T)) if 5 not in carriers else sorted(((*v,t) for v,t in zip(pairs,T)),key=rank)
  tags=tuple(v[2] for v in vs);r=counts[tags];r['full']+=1
  if all(map(active,vs)):
   r['outer_active']+=1;sectors[tags][tuple(v[0] for v in vs)]+=1
   r['exceptional_first' if vs[0][0] in (0,5) else 'carrier2_first' if vs[0][0]==2 else 'other_first']+=1
  else:r['outer_inactive']+=1
 return [{'standard_tags':p,'sorting_sign':(-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3)),'counts':dict(counts[p]),'active_carrier_sectors':{str(k):v for k,v in sorted(sectors[p].items())}} for p in counts]
if __name__=='__main__':
 r={'full_carriers_0_through_5':inventory(tuple(range(6))),'primary_carriers_1_through_4':inventory(tuple(range(1,5))),'physical_products_spent':0}
 Path(__file__).with_name('permuted-standard-domain-inventory.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
