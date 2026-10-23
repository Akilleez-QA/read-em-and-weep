#!/usr/bin/env python3
"""Independent synthetic scalar chain and adversarial-input review."""
import copy,json,math
from fractions import Fraction
import check_certificate as c

checks=[]
def ok(label,value):
 if not value:raise RuntimeError(label)
 checks.append(label)
def matrix(terms):return {'rows':1,'cols':1,'terms':terms}
def term(e,q):return [0,0,list(e),[q.numerator,q.denominator]]
def seal(data):
 return {'schema':c.SCHEMA,'binding':{'theorem_commit':c.COMMIT,'theorem_sha256':c.THEOREM_SHA256,'data_sha256':c.canonical_digest(data)},'data':data}
# Full multinomial formula, independent of production fixture generation.
# Q=3, T=2*a0-3*a1+5*a2, x_i=(-T/3)^i.
xs=[]
for i in range(24):
 terms=[]
 for j in range(i+1):
  for k in range(i-j+1):
   h=i-j-k
   q=Fraction(math.factorial(i),math.factorial(j)*math.factorial(k)*math.factorial(h))*Fraction(-2,3)**j*Fraction(1)**k*Fraction(-5,3)**h
   terms.append(term((j,k,h),q))
 xs.append(matrix(terms))
data={'variables':['a0','a1','a2'],'dimensions':{'N':1,'M':1,'P':1},'maps':{'Q':matrix([term((0,0,0),Fraction(3))]),'T':matrix([term((1,0,0),Fraction(2)),term((0,1,0),Fraction(-3)),term((0,0,1),Fraction(5))]),'s':xs[0],'i_P':matrix([term((0,0,0),Fraction(3))])},'corrections':xs,'generators':[]}
result=c.check(seal(data))
ok('independent full multinomial chain accepted',result['status']=='ALGEBRAIC_IDENTITIES_VERIFIED')
ok('actual rank remains unselected',result['actual_original_positive_rank']=='NOT_DETERMINED')
ok('generator claim absent',result['supplied_generator_equivariance']=='NOT_CHECKED')
for i in range(1,24):
 bad=copy.deepcopy(data);bad['corrections'][i]['terms'][0][3][0]*=-1
 try:c.check(seal(bad))
 except c.InvalidCertificate as exc:ok('detect changed full coefficient at x'+str(i),'identity fails at x'+str(i) in str(exc))
 else:raise RuntimeError('missed changed x'+str(i))
for label,value in [('bool exponent',[True,0,0]),('fractional exponent',[Fraction(1,2),0,0]),('huge exponent',[24,0,0])]:
 bad=copy.deepcopy(data);bad['maps']['T']['terms'][0][2]=value
 try:
  if label=='fractional exponent':c.matrix(bad['maps']['T'],1,1,1,c.Budget(),'T')
  else:c.check(seal(bad))
 except c.InvalidCertificate:checks.append(label+' rejected')
 else:raise RuntimeError(label)
for raw in [b'{"data":{},"data":{}}',b'{"n":1e2}',b'{"n":NaN}']:
 try:c.load_bytes(raw)
 except c.InvalidCertificate:checks.append('invalid serialization rejected '+raw.decode())
 else:raise RuntimeError('invalid serialization accepted')
ok('formal tail genuinely nonzero',Fraction(-5,3)**23*5!=0)
print(json.dumps({'status':'PASS','count':len(checks),'checks':checks,'scope':'Independent synthetic rational chain only; no actual coefficients or geometry authenticated.'},sort_keys=True,indent=2))
