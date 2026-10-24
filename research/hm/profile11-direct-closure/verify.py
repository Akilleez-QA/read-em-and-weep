#!/usr/bin/env python3
"""Fixed original159 records only. No historical enumeration or actual instance."""
from pathlib import Path
from collections import Counter
import hashlib, json
import characters as c
ROOT=Path(__file__).resolve().parent
checks=0
def check(ok, why):
    global checks
    checks+=1
    if not ok: raise RuntimeError(why)
def digest(b):
    return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
pins=json.loads((ROOT/'INPUTS.json').read_text())
for x in pins:
    b=(ROOT/x['file']).read_bytes()
    check(len(b)==x['bytes'],x['file']+' bytes')
    check(hashlib.sha256(b).hexdigest()==x['sha256'],x['file']+' sha256')
    check(digest(b)==x['git_blob_sha1'],x['file']+' git blob')
check(len(pins)==14,'14 immutable inputs')
def ordinary(X):return sorted([e for e,R in X for _ in range(c.DIM[R])],reverse=True)
def degree(X):return sum(e*c.DIM[R] for e,R in X)
def capacity(X,n):
    ds=ordinary(X)
    check(len(ds)==3,'rank3 capacity input')
    values=[dict(h1=h,h2=n-h,value=h*ds[0]-h*(h+1)+(n-h)*ds[1]-(n-h)*(n-h+1)) for h in range((n+1)//2,n+1)]
    best=max(x['value'] for x in values)
    return dict(n=n,ordinary_degrees=ds,height_values=values,capacity=best,optimizers=[[x['h1'],x['h2']] for x in values if x['value']==best])
def h0(X,t):return c.h0(X,t)
def display(x):return {r:x.get(r,0) for r in c.NAMES}
rows=json.loads((ROOT/'inputs/profile11-pairs.json').read_text())
check(len(rows)==159,'exact fixed input row count')
check(len({(tuple(map(tuple,x['A'])),tuple(map(tuple,x['B']))) for x in rows})==159,'ordered pairs unique')
records=[]; partitions={k:[] for k in ['source_degree_or_rank','cubic_visibility','dual_capacity','primal_capacity','six_shapes']}
for i,x in enumerate(rows):
    A,B=x['A'],x['B']; ad=ordinary(A); bd=ordinary(B)
    check(len(ad)==len(bd)==3,f'{i} ranks')
    check(degree(A)==x['a'] and degree(B)==x['b'],f'{i} degrees')
    check(x['defect']==-6-x['a']-x['b'],f'{i} original transpose defect')
    check(x['defect'] in [0,12,20,24],f'{i} original defect range')
    check(-4<=x['a']<=24 and -30<=x['b']<=-2,f'{i} original windows')
    for e,R in A+B:
        check(R in ['one','W','Wp','A','V'],f'{i} allowed rank3 irrep')
        check(e%2==(1 if R in ['W','Wp'] else 0),f'{i} center parity')
    cubic=h0(A,3); pa=capacity(A,14); du=capacity(B,10)
    if min(ad)<-8 or ad.count(-8)>1:reason='source_degree_or_rank'
    elif cubic['Wp']<1 or cubic['T']<2:reason='cubic_visibility'
    elif -54-x['b']>du['capacity']:reason='dual_capacity'
    elif -54-x['a']>pa['capacity']:reason='primal_capacity'
    else:reason='six_shapes'
    partitions[reason].append(i)
    records.append(dict(original_index=i,A=A,B=B,a=x['a'],b=x['b'],original_defect=x['defect'],cubic_character=display(cubic),primal_endpoint_degree=-54-x['a'],dual_endpoint_degree=-54-x['b'],primal=pa,dual=du,first_reason=reason))
check([len(v) for v in partitions.values()]==[56,32,62,3,6],'disjoint coverage sizes')
check(partitions['primal_capacity']==[32,50,52],'exact primal-only rows')
check(partitions['six_shapes']==[94,95,100,106,109,127],'exact six originals')
expected={
94:([[-8,'one'],[4,'one'],[6,'one']],[[-8,'one'],[-6,'one'],[6,'one']],2,-8,'PR1135'),
95:([[5,'W'],[-8,'one']],[[-7,'W'],[6,'one']],2,-8,'PR1135'),
100:([[-8,'one'],[4,'one'],[8,'one']],[[-10,'one'],[-6,'one'],[6,'one']],4,-10,'PR1142'),
106:([[-8,'one'],[4,'one'],[10,'one']],[[-12,'one'],[-6,'one'],[6,'one']],6,-12,'PR1142'),
109:([[-5,'Wp'],[16,'one']],[[3,'Wp'],[-18,'one']],6,-12,'Section5'),
127:([[-8,'one'],[2,'one'],[16,'one']],[[-18,'one'],[-4,'one'],[6,'one']],10,-16,'PR1145')}
for i,(A,B,a,b,theorem) in expected.items():
    x=rows[i]
    check((x['A'],x['B'],x['a'],x['b'],x['defect'])==(A,B,a,b,0),f'{i} exact residual')
    records[i]['closing_theorem']=theorem
check([records[i]['primal']['capacity'] for i in expected]==[-42,-42,-26,-10,20,38],'six primal capacities')
check([records[i]['dual']['capacity'] for i in expected]==[-42,-44,-42,-42,-30,-38],'six dual capacities')
Es=[ [[-2,'D'],[-3,'Wp'],[-3,'T'],[-4,'V'],[-8,'one']], [[-2,'P'],[-3,'Wp'],[-3,'T'],[-4,'V'],[-5,'Wp']], [[-2,'V'],[-3,'Wp'],[-3,'T'],[-4,'V'],[-4,'V']], [[-3,'Wp'],[-3,'T'],[-3,'T'],[-4,'V']] ]
for k,E in enumerate(Es):
    check(sum(c.DIM[R] for e,R in E)==17 and degree(E)==-54,f'E{k} rank degree')
    check(min(e for e,R in E)>=-8,f'E{k} minimum')
    check(sum(c.DIM[R] for e,R in E if e<=-8)==(1 if k==0 else 0),f'E{k} minus8 capacity')
check(c.product('Wp',3)['one']==0,'D lower row to Wp(-5) absent')
E=Es[1]; A=rows[109]['A']
source=h0(E,10)
target=Counter()
for i in range(9):target.update(h0(A,10-2*i))
check(source['one']==4 and target['one']==3,'invariant deficit4>3')
check([c.product('one',n)['Wp'] for n in [5,3,1]]==[0,0,0],'Wp scalar target invariants')
degrees=[26,24,22,20,18,16,14,12,10]
check([c.product('one',n)['one'] for n in degrees]==[0,1,0,1,0,0,0,1,0],'nine scalar invariant multiplicities')
check(c.product('one',6)==Counter(V=1,P=1),'Sym6 identity')
check(c.product('one',7)==Counter(Wp=1,T=1),'Sym7 identity')
check(c.product('one',8)==Counter(P=1,D=1),'Sym8 identity')
for n in range(32):
    check(sum(c.DIM[R]*v for R,v in c.product('one',n).items())==n+1,'symmetric dimension '+str(n))
result=dict(scope='Direct closure of original maximal profile (1,1), conditional on pinned actual inputs and original profile necessity; no global profile exhaustion.',checks=checks+c.checks,input_count=len(pins),original_record_count=len(rows),partition_indices=partitions,section5=dict(source=display(source),target=display(target),invariant_multiplicities=[4,3],scalar_degrees=degrees),records=records)
print(json.dumps(result,indent=2))
