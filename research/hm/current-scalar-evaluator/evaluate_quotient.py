#!/usr/bin/env python3
"""Portable current-L exact-Q evaluator, with JSON-only checkpoint state.

The arithmetic evaluate() body is the historical v3 body apart from replacing
pickle serialization with the explicit JSON codec and checkpoint filename.
The input contract is new, portable and independently bound to all 12 accepted
source pairs. It does not impersonate a historical configuration or receipt.
"""
import hashlib
import json
import math
import os
from pathlib import Path
import resource
import sys
import time
from fractions import Fraction
from integer_quotient_ring import *

H = Path(__file__).resolve().parent
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
PINS = json.loads((H / 'expected.json').read_text())


def mathematical_hash(obj, keys):
    content = json.dumps({k: obj[k] for k in keys}, sort_keys=True, separators=(',', ':'))
    return hashlib.sha256(content.encode()).hexdigest()


def contract_and_inputs(config_path):
    if sys.flags.optimize:
        raise RuntimeError('Assertion-enabled Python is required')
    path = Path(config_path)
    cfg = json.loads(path.read_text())
    roles = cfg['roles']
    assert type(roles) is list and len(roles) == 4 and all(type(x) is int for x in roles)
    assert sorted(roles) == [0, 1, 2, 3]
    first, second, a, b = roles
    pair = ''.join(map(str, roles[:2]))
    pin = PINS['pairs'][pair]
    compact = Path(cfg['input'])
    clearing = Path(cfg['clearingMetadata'])
    if not compact.is_absolute(): compact = path.parent / compact
    if not clearing.is_absolute(): clearing = path.parent / clearing
    source_sha, clearing_sha = sha(compact), sha(clearing)
    assert source_sha == pin['historicalCompactSHA256'], 'Compact source byte pin mismatch'
    assert clearing_sha == pin['historicalClearingSHA256'], 'Clearing source byte pin mismatch'
    d, k = json.loads(compact.read_text()), json.loads(clearing.read_text())
    assert mathematical_hash(d, PINS['compactMathematicalKeys']) == pin['compactMathematicalSHA256']
    assert mathematical_hash(k, PINS['clearingMathematicalKeys']) == pin['clearingMathematicalSHA256']
    assert d['coefficientField'] == k['field'] == 'Q' and d['characteristic'] == 0
    assert d['firstEliminatedAxis'] == first and d['secondEliminatedAxis'] == second
    assert d['remainingAxes'] == sorted([a, b]) and d['truncationLength'] == 6
    assert d['normalizedSyntaxDegree'] == 164 and d['normalizedFactoredTotalDegreeBound'] == 305
    assert d['removedCoordinateFactor'] == 48 and d['root']['reverseShift'] == 0
    assert not d['homogeneousProjectionEvaluated'] and not d['dehomogenizationApplied']
    assert d['sourceSHA256'] == k['normalizedSourceSHA256']
    assert k['compactSourceSHA256'] == source_sha and len(d['sumNodes']) == pin['sumNodes']
    assert sha(H / 'integer_quotient_ring.py') == PINS['arithmeticSHA256']
    output = Path(cfg['outputDirectory'])
    if not output.is_absolute(): output = path.parent / output
    cfg = dict(cfg, outputDirectory=str(output), clearingMetadataSHA256=clearing_sha)
    contract = {'schema': 'hm-portable-Q-evaluator-contract-v1', 'field': 'Q',
                'mode': 'PORTABLE_FULL_EXACT_QUOTIENT', 'roles': roles,
                'quotientShape': [6, 37, 22], 'inputSHA256': source_sha,
                'clearingMetadataSHA256': clearing_sha,
                'evaluatorSHA256': sha(__file__), 'arithmeticSHA256': PINS['arithmeticSHA256'],
                'expectedPinsSHA256': sha(H / 'expected.json'),
                'configurationSHA256': sha(path)}
    return cfg, d, k, contract


def encode_checkpoint(payload):
    data = dict(payload)
    data['schema'] = 'hm-portable-Q-JSON-checkpoint-v1'
    data['rootDenominator'] = str(data['rootDenominator'])
    data['vals'] = [[j, [[q, str(c)] for q, c in sorted(poly.items())]]
                    for j, poly in sorted(payload['vals'].items())]
    data['refs'] = sorted(payload['refs'].items())
    data['liveDenominators'] = [[j, str(d)] for j, d in sorted(payload['liveDenominators'].items())]
    return (json.dumps(data, separators=(',', ':')) + '\n').encode()


def decode_checkpoint(raw):
    data = json.loads(raw)
    assert data['schema'] == 'hm-portable-Q-JSON-checkpoint-v1'
    def integer(s):
        assert type(s) is str and str(int(s)) == s
        return int(s)
    def key(n):
        assert type(n) is int and n >= 0
        return n
    vals = {}
    for j, entries in data['vals']:
        key(j); assert j not in vals
        poly = {}
        for q, text in entries:
            key(q); c = integer(text)
            assert valid(q) and c and q not in poly
            poly[q] = c
        vals[j] = poly
    refs = {}
    for j, n in data['refs']:
        key(j); key(n); assert j not in refs
        refs[j] = n
    den = {}
    for j, text in data['liveDenominators']:
        key(j); d = integer(text); assert d > 0 and j not in den
        den[j] = d
    data['vals'], data['refs'], data['liveDenominators'] = vals, refs, den
    data['rootDenominator'] = integer(data['rootDenominator'])
    assert data['rootDenominator'] > 0 and type(data['nextIndex']) is int
    assert type(data['elapsedSeconds']) in (float, int) and 0 <= data['elapsedSeconds'] < float('inf')
    assert type(data['operations']) is dict
    assert all(type(n) is int and n >= 0 for n in data['operations'].values())
    return data


def validate_frontier(state, nodes, root, den, contract):
    """Recompute liveness from the unevaluated suffix before accepting resume."""
    index = state['nextIndex']
    assert state['contract'] == contract and 0 <= index <= len(nodes)
    leaves = set(contract['roles'][1:])
    refs = {}
    for node in nodes[index:]:
        for _, _, factors in node['terms']:
            for j, exponent in factors:
                refs[j] = refs.get(j, 0) + 1
    for j, exponent in root['factors']:
        refs[j] = refs.get(j, 0) + 1
    assert all(n == refs.get(j, 0) for j, n in state['refs'].items())
    assert all(state['refs'].get(j, 0) == n for j, n in refs.items())
    computed = {node['sourceSymbol'] for node in nodes[:index]}
    required = {j for j in computed if refs.get(j, 0)} | leaves
    assert required <= state['vals'].keys() <= computed | leaves
    assert state['liveDenominators'] == {j: den[j] for j in state['vals']}

def evaluate(config_path,seconds=840):
 start=time.monotonic();CFG,D,K,contract=contract_and_inputs(config_path);I,J,AA,BB=CFG['roles'];E=Path(CFG['outputDirectory']);E.mkdir(parents=True,exist_ok=True)
 assert not (E/'quotient.json').exists(),'Finished output is immutable'
 nodes=D['sumNodes'];assert len(nodes)==len(K['nodes'])
 meta={n['sourceSymbol']:(n['degree'],n['totalDegreeBound'])for n in nodes};meta.update({J:(1,1),AA:(0,1),BB:(0,1)})
 den={J:1,AA:1,BB:1}
 for n,k in zip(nodes,K['nodes']):
  s=n['sourceSymbol'];assert k['sourceSymbol']==s and len(k['integerWeights'])==len(n['terms'])
  den[s]=int(k['denominator']);assert den[s]>0
  for(c,du,f),w in zip(n['terms'],k['integerWeights']):
   alpha=Fraction(int(c[0]),int(c[1]))
   for j,e in f:alpha/=den[j]**e
   value=den[s]*alpha;assert value.denominator==1 and value.numerator==int(w)
   assert du>=0 and du==n['degree']-sum(meta[j][0]*e for j,e in f)
   assert n['totalDegreeBound']-sum(meta[j][1]*e for j,e in f)>=0
 rootD=int(K['root']['denominator']);rootW=int(K['root']['integerWeight']);assert rootD>0
 a=Fraction(*map(int,D['root']['coefficient']))
 for j,e in D['root']['factors']:a/=den[j]**e
 assert a*rootD==rootW
 assert(sum(meta[j][0]*e for j,e in D['root']['factors']),sum(meta[j][1]*e for j,e in D['root']['factors']))==(164,305)
 refs={}
 for n in nodes:
  for c,du,f in n['terms']:
   for j,e in f:refs[j]=refs.get(j,0)+1
 for j,e in D['root']['factors']:refs[j]=refs.get(j,0)+1
 vals={J:ONE,AA:ONE,BB:make({QZ:1})};cache={};nextindex=0;priorElapsed=0;checkpoint=E/'checkpoint.json';lastsave=time.monotonic()
 if checkpoint.exists():
  S=decode_checkpoint(checkpoint.read_bytes());assert S['contract']==contract
  validate_frontier(S,nodes,D['root'],den,contract)
  assert S['denominatorMetadataSHA256']==CFG['clearingMetadataSHA256']and S['rootDenominator']==rootD
  assert S['liveDenominators']=={j:den[j]for j in S['vals']}
  assert 0<=S['nextIndex']<=len(nodes)
  vals={j:make(p)for j,p in S['vals'].items()};refs=S['refs'];nextindex=S['nextIndex'];priorElapsed=S['elapsedSeconds'];OP.update(S['operations'])
 def save(i,reason):
  nonlocal lastsave
  payload={'schema':'hm-exact-Q-integer-quotient-checkpoint-v1','contract':contract,'denominatorMetadataSHA256':CFG['clearingMetadataSHA256'],'rootDenominator':rootD,'nextIndex':i,'vals':{j:a.p for j,a in vals.items()},'liveDenominators':{j:den[j]for j in vals},'refs':refs,'elapsedSeconds':priorElapsed+time.monotonic()-start,'operations':dict(OP),'reason':reason}
  tmp=checkpoint.with_suffix('.tmp');tmp.write_bytes(encode_checkpoint(payload));os.replace(tmp,checkpoint);lastsave=time.monotonic()
 def event(i,status='RUNNING'):
  e={'status':status,'processedSumSymbols':i,'totalSumSymbols':len(nodes),'elapsedSeconds':priorElapsed+time.monotonic()-start,'liveSymbols':len(vals),'liveCoefficientSlots':sum(len(a.p)for a in vals.values()),'peakRSSKiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'operations':dict(OP)}
  with(E/'progress.jsonl').open('a')as f:f.write(json.dumps(e)+'\n')
  print(json.dumps(e),flush=True)
 def factor(j,e):
  if e==1:return vals[j]
  per=cache.setdefault(j,{})
  if e not in per:per[e]=power(vals[j],e)
  return per[e]
 for index in range(nextindex,len(nodes)):
  n=nodes[index];k=K['nodes'][index];C={}
  for(_,du,f),weight in zip(n['terms'],k['integerWeights']):
   dt=n['totalDegreeBound']-sum(meta[j][1]*e for j,e in f)
   if dt<W and du<V:
    A=ONE
    for j,e in f:A=mul(A,factor(j,e))
    add_shift(C,A,int(weight),du,dt)
   for j,e in f:
    refs[j]-=1
    if not refs[j]and j>=16:vals.pop(j,None);cache.pop(j,None)
  vals[n['sourceSymbol']]=make(C);i=index+1
  if i%250==0:event(i)
  if i%1000==0 or time.monotonic()-lastsave>=30:save(i,'periodic')
  if time.monotonic()-start>=seconds:
   save(i,'budget');event(i,'CHECKPOINTED_BUDGET_EXIT');return
 save(len(nodes),'source-finished-before-terminal')
 A=ONE
 for j,e in D['root']['factors']:A=mul(A,power(vals[j],e))
 C={};add_shift(C,A,rootW,D['root']['reverseShift'],0);A=make(C)
 rows=sorted([[q%RV,(q//RV)%RW,q//QZ,str(c)]for q,c in A.p.items()]);canonical=json.dumps(rows,separators=(',',':')).encode()
 result={'schema':'hm-exact-Q-full-quotient-v1','status':'EXACT_FULL_QUOTIENT_EXPORTED','field':'Q','roles':CFG['roles'],'quotientShape':[V,W,Z],'contract':contract,'commonDenominator':str(rootD),'integerQuotientCoefficients':rows,'integerCoefficientSHA256':hashlib.sha256(canonical).hexdigest(),'retainedNonzeros':len(rows),'operations':dict(OP),'elapsedSeconds':priorElapsed+time.monotonic()-start,'peakRSSKiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'homogeneousDegreesRemainSeparated':True,'pairingAggregated':False}
 out=E/'quotient.json';out.write_text(json.dumps(result,indent=2)+'\n');save(len(nodes),'finished');event(len(nodes),'FULL_QUOTIENT_FINISHED')

if __name__ == '__main__':
    if sys.flags.optimize:
        raise RuntimeError('Assertion-enabled Python is required')
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', required=True)
    parser.add_argument('--seconds', type=float, default=840)
    args = parser.parse_args()
    assert 0 < args.seconds <= 840
    evaluate(args.config, args.seconds)
