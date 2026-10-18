"""Independent literal metadata and formal cohomology-support audit only."""
import hashlib,json,math
from pathlib import Path
root=Path(__file__).resolve().parent; raw=(root/'model.json').read_bytes()
def need(c,s):
 if not c: raise ValueError(s)
need(hashlib.sha256(raw).hexdigest()=='635bb12d9986e0dcada161d4173c773c4f134b9225354a3bc74267840ca19926','pin')
m=json.loads(raw)
def terms(a):return {tuple(map(int,k.split(','))):v for k,v in a}
for name,(nr,nc) in {'gamma':(15,5),'delta':(10,15),'ev':(2,10)}.items():
 need(len(m[name])==nr and all(len(row)==nc for row in m[name]),'differential shape')
 for row in m[name]:
  for cell in row:
   for ex in terms(cell):need(len(ex)==4 and min(ex)>=0 and sum(ex)<=1,'linear differential')
for ch in m['charts']:
 for name,(nr,nc) in {'I':(15,2),'P':(2,15),'H0':(5,15),'H1':(15,10)}.items():
  need(len(ch[name])==nr and all(len(row)==nc for row in ch[name]),'primitive shape')
charts=[]
for a,ch in enumerate(m['charts']):
 p=ch['pivot'];need(p==(a if a<5 else 0),'pivot')
 expected=({(1,1,1,1):1,(0,0,0,0):-1} if a==0 else {(2,0,1,1):-1} if a==5 else {(1,1,1,1):1,tuple(5 if r==a-1 else 0 for r in range(4)):-1})
 out={}
 for name,key in [('I','di'),('P','dp'),('H0','dh'),('H1','dh')]:
  den=terms(ch[key]);need(den==expected,'denominator')
  D=max(sum(e) for e in den);maximum=0;count=0
  for r,row in enumerate(ch[name]):
   for c,cell in enumerate(row):
    w=(c if name=='I' else -r if name=='P' else -1)
    for ex,coeff in terms(cell).items():
     count+=1;maximum=max(maximum,sum(ex)-D-w)
  need(maximum <= (1 if a==0 else 2 if a==5 else 0),'extra v0 pole')
  out[name]={'extra_v0_pole_bound':maximum,'literal_terms_inspected':count,'denominator_degree':D}
 for row in ch['H1']:
  need(not row[p] and not row[5+p],'B selected columns')
 charts.append({'chart':a,'pivot':p,'bounds':out,'B_literal_zero':True})
# C: each delta block-column is a literal skew pair annihilated by its evaluation row.
tokens=[(0,0,0,0)]+[tuple(int(i==j) for i in range(4)) for j in range(4)]
for h in range(2):
 for r in range(10):need(terms(m['ev'][h][r])==({tokens[r%5]:1} if r//5==h else {}),'ev')
 for c in range(15):
  nz=[(r,terms(m['delta'][h*5+r][c])) for r in range(5) if m['delta'][h*5+r][c]]
  if not nz:continue
  need(len(nz)==2,'skew support');(r,u),(s,v)=nz
  need(set(u)=={tokens[s]} and set(v)=={tokens[r]} and u[tokens[s]]==-v[tokens[r]],'skew tokens')
# Formal support only, with multiplicities from ranks, not physical differential arithmetic.
ranks={-1:5,0:15,1:10,2:2}
mult={p:sum(ranks[i]*ranks[i+p] for i in ranks if i+p in ranks) for p in range(-3,4)}
support={(p,q) for p in range(-3,4) for q in range(5) if (p<0 and q==4) or (p==0) or (p>0 and q==0)}
need([z for z in sorted(support) if sum(z)==0]==[(0,0)],'total zero')
need(not [z for z in support if sum(z)==-1],'total minus one')
incoming=[(r,(-r,r-1)) for r in range(2,9) if (-r,r-1) in support]
need(not incoming,'incoming higher differential')
report={'status':'PASS','scope':'literal metadata, degree labels, skew support, formal cohomology support only; A not recomputed','charts':charts,'internal_Hom_multiplicities':mult,'X_E1_support':sorted(support),'higher_incoming_to_origin':incoming}
print(json.dumps(report,indent=2))
