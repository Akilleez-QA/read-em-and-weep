#!/usr/bin/env python3
"""Executed mutation tests for the necessary one-tuple theorem's finite certificate."""
import importlib,json
import base,verify

def run(name,change):
 b=importlib.reload(base);m=importlib.reload(verify);change(m,b)
 try:m.main()
 except (ValueError,RuntimeError) as exc:return {'mutation':name,'rejected':True,'reason':str(exc)}
 raise RuntimeError('Mutation was not rejected: '+name)

def euler_shift(m,b):
 original=m.Qs;m.Qs=lambda t:original(t-1)
def torsion_erasure(m,b):m.tor=lambda r,t:b.zero
def endpoint_truncation(m,b):
 original=m.endpoints
 def changed(rank,d):
  domain=original(rank,d);return set(sorted(domain)[1:])
 m.endpoints=changed
def endpoint_parity(m,b):
 original=m.endpoints_independent;m.endpoints_independent=lambda rank,d:{K for K in original(rank,d)if all(e%2==0 for e,i in K)}
def cubic_single_channel(m,b):b.E3=b.add(b.basis(7),b.basis(5))
def capacity_wrong_rank(m,b):
 original=b.capacity;b.capacity=lambda B,n=13:original(B,n-1)
def hom_erasure(m,b):m.hom=lambda B,C:0
def flag_acceptance(m,b):
 original=m.weighted_gap
 def changed(N,r,D):
  target,got=original(N,r,D);return target,sorted(set(got+[target]))
 m.weighted_gap=changed
def omit_kernel_alternative(m,b):
 original=m.classify_lower_kernel;m.classify_lower_kernel=lambda B:original(B)[:1]
def wrong_kernel_types(m,b):
 original=m.classify_lower_kernel;m.classify_lower_kernel=lambda B:[tuple((e,2 if i==8 else i)for e,i in K)for K in original(B)]

def main():
 tests=[('actual Qstar Euler shifted',euler_shift),('length-twelve torsion erased',torsion_erasure),('complete endpoint domain truncated',endpoint_truncation),('odd coefficient parity removed',endpoint_parity),('second actual cubic T channel omitted',cubic_single_channel),('endpoint capacity rank lowered',capacity_wrong_rank),('all equivariant Hom spaces erased',hom_erasure),('forbidden rank-one target admitted',flag_acceptance),('second lower kernel alternative dropped',omit_kernel_alternative),('lower-kernel V marking exchanged',wrong_kernel_types)]
 out=[run(name,f)for name,f in tests]
 b=importlib.reload(base);m=importlib.reload(verify);result=m.main()
 if len(result['necessary_survivors'])!=1:raise RuntimeError('unmutated positive control')
 return {'executed_mutations':len(out),'all_rejected':True,'unmutated_result_retained':True,'tests':out}
if __name__=='__main__':print(json.dumps(main(),indent=2,sort_keys=True))
