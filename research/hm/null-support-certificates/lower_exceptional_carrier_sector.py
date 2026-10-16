"""Authenticated exceptional-carrier rational AST and source-column zero proof.

No physical polynomial arithmetic. No extension of the old clearance/cancel
routine is permitted. Star uses its actual -v1*a denominator, not -a.
"""
from itertools import combinations, combinations_with_replacement
from math import comb
import json, hashlib
from pathlib import Path
import lower_selected_kernel_denominators as base

STANDARDS=(3,11,15)
CARRIERS=(5,0,1,2,3,4)
def source_key(v):
    return (-1 if v.carrier==5 else v.carrier,v.legal_mask,v.standard_tag)

def authentication():
    m=base.source.authenticate()
    for b,c in enumerate(m['charts']):
        expected={(1,1,1,1):1,tuple(5 if i==b-1 else 0 for i in range(4)):-1} if b<5 else {(2,0,1,1):-1}
        for name in ('di','dp','dh'):
            got={tuple(map(int,e.split(','))):n for e,n in c[name]}
            if got!=expected:raise ValueError('actual carrier denominator changed')
    if m['charts'][0]['pivot']!=0 or m['charts'][5]['pivot']!=0:raise ValueError('exceptional pivot changed')
    for b in (0,5):
        if any(row[6] for row in m['charts'][b]['P']):raise ValueError('selected column not literal zero')
    return {'model_sha256':base.source.MODEL_SHA256,'outer_sources':base.outer.authenticate_public_sources(),
      'contraction_certificate':base.contraction_certificate(),
      'denominators':{'0':'-h0= v1*v2*v3*v4 - 1','5':'-v1*a=-v1^2*v3*v4'},
      'unit_proof':'On D(a), v1 is a unit: inverse(v1)=v0*v3*v4/a; on the global finite chart v0=1. No additional localization.',
      'pivot':'Both exceptional charts have pivot 0; v0=1 on the finite chart.',
      'selected_column':6,'literal_zero_carriers':[0,5]}

class ExceptionalLower(base.Lower):
    def __init__(self,vertices):
        keys=[source_key(v) for v in vertices]
        if keys!=sorted(keys) or len(set(keys))!=3:raise ValueError('source-first distinct owners required')
        if tuple(v.standard_tag for v in vertices)!=STANDARDS:raise ValueError('selected staircase only')
        if not any(v.carrier in (0,5) for v in vertices):raise ValueError('exceptional domain required')
        if any(v.carrier not in range(6) for v in vertices):raise ValueError('physical carriers 0..5 only')
        authentication()
        self.g=base.DAG();self.vs=vertices;self.model=base.source.authenticate();self.factors={};self.blocks={}
        g=self.g;self.x=[g.node('coordinate',i) for i in range(4)]
        self.v=[g.c(1)]+[g.add(*(g.mul(*(self.x[i] for i in inds)) for inds in combinations(range(4),k))) for k in range(1,5)]
        a=g.mul(self.v[1],self.v[3],self.v[4])
        for v in vertices:
            H=a if v.carrier==5 else g.add(g.pow(self.v[v.carrier],5),g.mul(g.c(-1),*self.v))
            self.factors[self.key(v,'H')]=H
            self.factors[self.key(v,'D')]=g.mul(self.v[1],a) if v.carrier==5 else H
            for i in range(4):
                self.factors[self.key(v,'L',i)]=g.mul(self.x[i],g.add(g.pow(self.x[i],2),g.c(-1)))
                self.factors[self.key(v,'Z',i)]=self.x[i]
    def block(self,v,name):
        if name not in ('I','P'):raise ValueError('transition block only')
        key=(v,name)
        if key not in self.blocks:
            self.blocks[key]=[[self.rat(self.g.mul(self.g.c(-1),self.poly(p)),{self.key(v,'D'):1}) for p in row] for row in self.model['charts'][v.carrier][name]]
        return self.blocks[key]
    def edge_inverse(self,*args):raise ValueError('exceptional edge clearance not needed or licensed')
    def cancel(self,*args):raise ValueError('exceptional outer cancellation not needed or licensed')
    def quotient(self,*args):raise ValueError('use authenticated outer formula; old primary quotient not valid for star')
    def selected_contraction(self,kind,d):
        R=self.tracefree(self.current(kind,d));a=self.vs[0]
        I=self.block(a,'I');P=self.block(a,'P');out=self.rat(self.g.c(0))
        for u in range(2):
            for w in range(2):out=self.add(out,self.mul(self.mul(I[12][u],R[w][u]),P[w][6]))
        return out

def outer_maybe_active(c,m,t):
    bits=base.owned.decode_standard_tag(t);s=sum(bits)
    if any((m>>i)&1 and not bits[i] for i in range(4)):return False
    return c==5 or (c<=s and (s!=4 or c==4))

def partition():
    auth=authentication();counts={'full':0,'prior_primary':0,'remaining_exceptional':0,'exceptional_outer_literal_zero':0,'exceptional_outer_not_structurally_zero':0,'exceptional_selected_contraction_zero':0,'unresolved_exceptional':0}
    anchors={};active_sectors={}
    pairs=tuple((c,m) for c in CARRIERS for m in range(16))
    for triple in combinations_with_replacement(pairs,3):
        counts['full']+=1
        if all(c not in (0,5) for c,m in triple):counts['prior_primary']+=1;continue
        counts['remaining_exceptional']+=1
        a=triple[0][0]
        if a not in (0,5):raise AssertionError('exceptional source anchor escaped')
        anchors[str(a)]=anchors.get(str(a),0)+1
        counts['exceptional_selected_contraction_zero']+=1
        active=all(outer_maybe_active(c,m,t) for (c,m),t in zip(triple,STANDARDS))
        counts['exceptional_outer_not_structurally_zero' if active else 'exceptional_outer_literal_zero']+=1
        if active:
            k=','.join(str(c) for c,m in triple);active_sectors[k]=active_sectors.get(k,0)+1
    assert counts['full']==comb(98,3) and counts['prior_primary']==45760
    return {'schema':'exceptional-carrier-domain-v1','scope':{'seed':4,'row':2,'standards':STANDARDS,'kernel':'E12','source_carrier_order':CARRIERS,'ordering_provenance':'fresh consistent source definition; fresh_source_order_contract.py; no historical value import or newly authenticated historical mask ordering','not_covered':'E34, other seeds, rows, staircases, and global factorization'},'authentication':auth,'counts':counts,'anchor_counts':anchors,'potentially_active_carrier_sectors':active_sectors,
      'proof':'Every exceptional-containing increasing triple starts at star5 or carrier0. For either anchor, P[w][6]=0 for w=0,1 in the authenticated source, so sum_u,w I[12][u] tf(R)[w][u] P[w][6]=0 for every current R. This is the full transpose contraction, before scalar edge or outer multiplication.',
      'overlap_semantics':'No support overlap is labelled nonzero; all exceptional tuples vanish by an exact matrix-column identity.',
      'physical_polynomial_evaluation':False,'physical_polynomial_expansion':False,'physical_products_spent':0,'execution_release':False,'actual_factorization_accepted':False,
      'held_limits':{'private_resource_configuration_omitted':True}}

if __name__=='__main__':
    p=partition();Path(__file__).with_name('exceptional-carrier-domain-partition.json').write_text(json.dumps(p,sort_keys=True,indent=2)+'\n');print(json.dumps(p['counts'],sort_keys=True))
