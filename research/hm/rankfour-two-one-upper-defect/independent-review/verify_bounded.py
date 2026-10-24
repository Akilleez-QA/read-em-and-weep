#!/usr/bin/env python3
"""Independent proof arithmetic for upper defect <=12 in the (2,1) profile.
Only the independent class-character and ordinary-partition helpers are used.
"""
from pathlib import Path
import independent as c
import json,hashlib
from itertools import product
ROOT=Path(__file__).resolve().parent
SRC=ROOT/'accepted-author-packet'
def freeze_row(row):
 a,b,d1,d2,d,F,D,B,T1,T2=row
 return (a,b,d1,d2,d,tuple(map(tuple,F)),tuple(map(tuple,D)),tuple(map(tuple,B)),tuple(map(tuple,T1)),tuple(map(tuple,T2)))
def author_row(row):
 bs=lambda name:tuple(sorted((x['degree'],c.NAMES.index(x['coefficient']))for x in row[name]))
 return tuple(row['case'])+(bs('F0'),bs('D0'),bs('B'),tuple(map(tuple,row['T1'])),tuple(map(tuple,row['T2'])))
def run():
 manifest_raw=(SRC/'MANIFEST.json').read_bytes()
 manifest_hash=hashlib.sha256(manifest_raw).hexdigest()
 c.check(manifest_hash=='70d00102e6e5ea920fc77ebd328b84cf7b8162cde7dc26b241577ca15864042d','accepted author manifest')
 manifest=json.loads(manifest_raw)
 c.check(len(manifest['files'])==14,'accepted author mathematical inventory')
 for entry in manifest['files']:
  raw=(SRC/entry['path']).read_bytes()
  c.check(len(raw)==entry['bytes'] and hashlib.sha256(raw).hexdigest()==entry['sha256'],'accepted author file '+entry['path'])
 for i,row in enumerate(c.CH):c.check(c.decompose(row)==c.unit(i),'character orthogonality')
 budget=c.vec(**{"W'":1,'T6':3})
 c.check(sum(d*x for d,x in zip(c.DIMS,budget))==20,'central cubic budget dimension')
 for e in range(-22,-10):
  for i in range(9):
   if c.DIMS[i]<=4 and c.PAR[i]==e%2:
    c.check(not c.pos(c.sub(budget,c.h1(((e,i),),1))),'complete B lower cutoff')
 originals=[]
 for item in json.loads((SRC/'INPUTS.json').read_text()):
  raw=(SRC/item['file']).read_bytes();local=ROOT/'remote-inputs'/Path(item['file']).name
  c.check(raw==local.read_bytes(),'independently fetched original bytes')
  c.check(hashlib.sha256(raw).hexdigest()==item['sha256'],'source SHA256')
  c.check(hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==item['git_blob_sha1'],'source blob')
  originals.append({'file':item['file'],'sha256':item['sha256']})
 cases,_=c.make_cases();cases=[x for x in cases if x[3]>=20]
 c.check(len(cases)==7,'complete high-defect cases')
 td=c.torsion_domains()
 c.check(all(n in td for n in(0,12,20,24)),'all required torsion lengths retained')
 c.check([len(td[n])for n in(0,12,20,24)]==[1,5,3,15],'all reduced and nonreduced torsion signatures retained')
 eds={};bds={};summary=[];cohom=[];horizontal=[];survivors=[]
 for a,b,d1,d2,d in cases:
  for degree in(a,b):
   if degree not in eds:
    eds[degree]={}
    for ep in c.splitting(9,degree,-3):eds[degree].setdefault(c.sig(ep),[]).append(ep)
  if d not in bds:bds[d]=[B for B in c.splitting(4,d,-10,True)if c.base_B_test(B)and c.new_B_test(B)is None]
  counts=[0,0]
  for B in bds[d]:
   ff=[];dd=[]
   for T1 in td[d1].values():
    sig=tuple(x for t in(0,1)for x in c.add(c.sub(c.E(t),c.add(c.chi(B,t),c.chi(B,t-2))),c.torsion(T1,t)))
    ff.extend((F,T1)for F in eds[a].get(sig,()))
   for T2 in td[d2].values():
    if not c.pos(c.sub(c.sub(c.neg(c.chi(B,-2)),c.torsion(T2,-2)),c.Qs(2))):continue
    sig=tuple(x for t in(0,1)for x in c.add(c.Qs(t),c.chi(B,-t),c.torsion(T2,-t)))
    dd.extend((D,T2)for D in eds[b].get(sig,()))
   for (F,T1),(D,T2)in product(ff,dd):
    row=(a,b,d1,d2,d,F,D,B,T1,T2);cohom.append(row);counts[0]+=1
    wf=c.horizontal_witness(F,c.shift(B,-4));wd=c.horizontal_witness(D,c.shift(c.dual(B),-4))
    if wf or wd:horizontal.append({'row':row,'F0_witness':wf,'D0_witness':wd})
    else:survivors.append(row);counts[1]+=1
  summary.append({'case':(a,b,d1,d2,d),'cohom_count':counts[0],'horizontal_survivors':counts[1]})
 c.check(len(cohom)==31 and len(horizontal)==26 and len(survivors)==5,'exact bounded frontier')
 author=json.loads((SRC/'RESULT.json').read_text())
 author_all=author['horizontal_rejections']+author['five_residual_tuples']
 c.check({freeze_row(r)for r in cohom}=={author_row(r)for r in author_all},'all 31 exact tuple sets agree')
 c.check({freeze_row(r)for r in survivors}=={author_row(r)for r in author['five_residual_tuples']},'all five residual tuples agree')
 # The independently authenticated primary-terminal slope theorem, not an
 # invented actual source, supplies precisely these four necessary E types.
 sources=( ((-2,4),(-3,7),(-3,5),(-4,8),(-8,0)),
           ((-2,6),(-3,7),(-3,5),(-4,8),(-5,7)),
           ((-2,8),(-3,7),(-3,5),(-4,8),(-4,8)),
           ((-3,7),(-3,5),(-3,5),(-4,8)) )
 sourceh1=[c.h1(E,3)for E in sources]
 c.check(sourceh1==[c.unit(3),c.unit(7),c.Z,c.Z],'source cubic cohomology')
 rejected=[];last=[]
 for row in survivors:
  h1=c.h1(row[7],3)
  if any(c.pos(c.sub(v,h1))for v in sourceh1):last.append(row)
  else:rejected.append({'row':row,'H1_B3':h1})
 c.check(len(rejected)==4 and len(last)==1,'source cubic quotient cuts')
 row=last[0];a,b,d1,d2,d,F,D,B,T1,T2=row
 c.check(F==((-4,8),(-3,5))and D==F and B==((-8,0),(-3,7),(6,0)),'unique literal final tuple')
 target=c.shift(B,-4);other=tuple(x for x in target if x!=(2,0))
 c.check(all(c.hom(x,y)==0 for x in F for y in other),'only scalar derivative target')
 # Geometric complete flag and persistence are proved in BOUNDED-REVIEW.md.
 c.check([n for n in range(12,31)if 30>=9*(n-9)]==[12],'unique constant span')
 n=12;r=9;weights=[(n-r)*j if j<r else r*(n-j)for j in range(1,n)]
 target=n*(30-r*(n-r))
 c.check(target==36 and weights[0]*12==36,'weighted flag budget')
 c.check(all(w*12>target for w in weights[1:]),'only first position can have a defect')
 c.check(weights[0]*20>target,'no larger orbit defect possible')
 deltas=[12]+[0]*10
 c1=(-(n-1)*n-sum((n-j)*dd for j,dd in enumerate(deltas,1)))//n
 lines=[c1]
 for dd in deltas:lines.append(lines[-1]+2+dd)
 c.check(lines==[-22,-8,-6,-4,-2,0,2,4,6,8,10,12],'all complete-flag line degrees')
 c.check(sum(lines)==0 and sum(lines[:9])==-30,'flag total and central degrees')
 c.check(sum(lines[:11])==-12>-22==-2*11,'second transform violates E twist-one cap')
 return {'status':'PASS','accepted_author_manifest_sha256':manifest_hash,'accepted_author_files':len(manifest['files']),'all_31_exact_tuples_match':True,'all_five_residual_tuples_match':True,'scope':'Upper defect delta2 belongs to {0,12}; the ordered (2,1) profile remains open.','originals':originals,'cases':summary,'cohom_count':len(cohom),'horizontal_rejections':horizontal,'five_residual_rows':survivors,'source_cubic_rejections':rejected,'last_row':row,'rankone':{'span':12,'rank':9,'degree':-30,'weights':weights,'required_weight':36,'defects':deltas,'line_degrees':lines,'second_forward_rank':11,'second_forward_degree':-12,'required_degree_cap':-22},'checks':c.checks}
if __name__=='__main__':
 result=run();(ROOT/'BOUNDED-RESULT.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');print(json.dumps({k:result[k]for k in('status','scope','cohom_count','checks')},sort_keys=True))
