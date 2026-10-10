#!/usr/bin/env python3
"""Portable synthetic sources: independent Fraction oracle, resume and guards."""
import contextlib,copy,hashlib,io,json,tempfile,sys
from fractions import Fraction as F
from math import lcm,prod
from pathlib import Path
import exact_oracle as O
import evaluate_quotient as M
import validate_quotient as V
if sys.flags.optimize: raise RuntimeError('Assertion-enabled Python is required')
H=Path(__file__).resolve().parent
def coeff(x):return [str(F(x).numerator),str(F(x).denominator)]
def make_case(label,exponent=2,cancel=False):
 first=[[coeff(F(1,3)),0,[[1,1],[2,1]]],[coeff(F(-2,5)),0,[[1,1],[3,1]]],[coeff(F(7,11)),1,[[2,2]]]]
 if cancel:first += [[coeff(-F(*map(int,c))),u,f]for c,u,f in list(first)]
 nodes=[{'sourceSymbol':16,'degree':1,'totalDegreeBound':2,'terms':first}]
 if exponent==2:
  nodes += [{'sourceSymbol':17,'degree':2,'totalDegreeBound':4,'terms':[[coeff(F(5,7)),0,[[16,2]]],[coeff(F(-13,17)),0,[[1,2],[2,1]]]]}]
  root={'coefficient':coeff(F(-3,19)),'reverseShift':0,'factors':[[1,162],[2,139],[17,1]]}
 else:
  root={'coefficient':coeff(F(-3,19)),'reverseShift':0,'factors':[[1,164-exponent],[2,141-exponent],[16,exponent]]}
 D={'sumNodes':nodes,'root':root};den={1:1,2:1,3:1};krows=[]
 for n in nodes:
  vals=[F(*map(int,c))/prod(den[j]**e for j,e in f)for c,u,f in n['terms']]
  d=lcm(*(x.denominator for x in vals));den[n['sourceSymbol']]=d
  krows.append({'sourceSymbol':n['sourceSymbol'],'denominator':str(d),'integerWeights':[str((d*x).numerator)for x in vals]})
 alpha=F(*map(int,root['coefficient']))/prod(den[j]**e for j,e in root['factors'])
 K={'nodes':krows,'root':{'denominator':str(alpha.denominator),'integerWeight':str(alpha.numerator)}}
 # Independent Fraction tuple evaluation of this tiny constructed fixture only.
 vals={1:{(0,0,0):F(1)},2:{(0,0,0):F(1)},3:{(0,0,1):F(1)}};meta={1:(1,1),2:(0,1),3:(0,1)}
 for n in nodes:
  out={}
  for c,du,f in n['terms']:
   a={(0,0,0):F(*map(int,c))}
   for j,e in f:a=O.mul(a,O.power(vals[j],e))
   dt=n['totalDegreeBound']-sum(meta[j][1]*e for j,e in f)
   for (r,w,z),v in a.items():
    if r+du<6 and w+dt<37:out[r+du,w+dt,z]=out.get((r+du,w+dt,z),0)+v
  vals[n['sourceSymbol']]={k:v for k,v in out.items()if v};meta[n['sourceSymbol']]=(n['degree'],n['totalDegreeBound'])
 expected={(0,0,0):F(*map(int,root['coefficient']))}
 for j,e in root['factors']:expected=O.mul(expected,O.power(vals[j],e))
 return D,K,expected


def main():
    # Check the numerical body against its historical source digest after
    # removing only the declared checkpoint-codec/frontier adaptations.
    source = (H / 'evaluate_quotient.py').read_text()
    body = source[source.index('def evaluate('):source.index("if __name__ == '__main__':")].strip()
    body = body.replace("E/'checkpoint.json'", "E/'checkpoint.pickle'")
    body = body.replace('decode_checkpoint(checkpoint.read_bytes())', 'pickle.loads(checkpoint.read_bytes())')
    body = body.replace('encode_checkpoint(payload)', 'pickle.dumps(payload,protocol=5)')
    body = body.replace("  validate_frontier(S,nodes,D['root'],den,contract)\n", '')
    assert hashlib.sha256(body.encode()).hexdigest() == M.PINS['historicalEvaluationBodySHA256']
    real_loader = M.contract_and_inputs
    results, rejected = [], []
    for label, exponent, cancel, resume in [('signed-denominator', 2, False, False),
                                           ('checkpoint-resume', 2, False, True),
                                           ('cancellation', 2, True, False),
                                           ('ordinary-power71', 71, False, False)]:
        d, k, expected = make_case(label, exponent, cancel)
        with tempfile.TemporaryDirectory(prefix='hm-portable-fixture-') as temp:
            out = Path(temp)
            cfg = {'outputDirectory': str(out), 'clearingMetadataSHA256': 'synthetic-clearing',
                   'roles': [0, 1, 2, 3]}
            contract = {'field': 'Q', 'fixture': label, 'roles': [0, 1, 2, 3]}
            M.contract_and_inputs = lambda _: (cfg, d, k, contract)
            if resume:
                with contextlib.redirect_stdout(io.StringIO()):
                    M.evaluate('SYNTHETIC', -1)
                assert not (out / 'quotient.json').exists()
                checkpoint = out / 'checkpoint.json'
                state = M.decode_checkpoint(checkpoint.read_bytes())
                assert state['nextIndex'] == 1 and state['reason'] == 'budget'
                mutations = [('contract', {'field': 'F71'}), ('rootDenominator', -1),
                             ('denominatorMetadataSHA256', 'foreign'), ('liveDenominators', {}),
                             ('nextIndex', -1), ('nextIndex', len(d['sumNodes']) + 1),
                             ('refs', {})]
                for key, value in mutations:
                    bad = copy.deepcopy(state)
                    bad[key] = value
                    checkpoint.write_bytes(M.encode_checkpoint(bad))
                    try:
                        with contextlib.redirect_stdout(io.StringIO()):
                            M.evaluate('SYNTHETIC', 840)
                    except AssertionError:
                        rejected.append(key)
                    else:
                        raise AssertionError('Invalid checkpoint accepted: ' + key)
                checkpoint.write_bytes(M.encode_checkpoint(state))
            with contextlib.redirect_stdout(io.StringIO()):
                M.evaluate('SYNTHETIC', 840)
            q = json.loads((out / 'quotient.json').read_text())
            got = {tuple(row[:3]): F(int(row[3]), int(q['commonDenominator']))
                   for row in q['integerQuotientCoefficients']}
            assert got == expected
            receipt = V.validate('SYNTHETIC', expected=False)
            assert receipt['independentFractionTerminalMatched']
            assert M.decode_checkpoint((out / 'checkpoint.json').read_bytes())['reason'] == 'finished'
            if label == 'signed-denominator':
                mutations = [
                    ('result-schema', lambda x: x.update(schema='foreign')),
                    ('result-status', lambda x: x.update(status='unfinished')),
                    ('result-field', lambda x: x.update(field='F71')),
                    ('string-boolean', lambda x: x.update(homogeneousDegreesRemainSeparated='false')),
                    ('integer-boolean', lambda x: x.update(pairingAggregated=0)),
                    ('role-boolean', lambda x: x.update(roles=[0, True, 2, 3])),
                    ('contract-role-boolean', lambda x: x['contract'].update(roles=[0, True, 2, 3])),
                    ('shape-float', lambda x: x.update(quotientShape=[6.0, 37, 22])),
                    ('count-float', lambda x: x.update(retainedNonzeros=float(len(x['integerQuotientCoefficients'])))),
                    ('noncanonical-denominator', lambda x: x.update(commonDenominator='0' + x['commonDenominator'])),
                ]
                for name, mutate in mutations:
                    bad = copy.deepcopy(q)
                    mutate(bad)
                    (out / 'quotient.json').write_text(json.dumps(bad))
                    try:
                        V.validate('SYNTHETIC', expected=False)
                    except AssertionError:
                        rejected.append(name)
                    else:
                        raise AssertionError('Invalid result metadata accepted: ' + name)
                (out / 'quotient.json').write_text(json.dumps(q))
            results.append({'fixture': label, 'nodes': len(d['sumNodes']), 'nonzeros': len(got),
                            'resumeChecked': resume, 'fractionOracleMatched': True})
    M.contract_and_inputs = real_loader
    # The portable loader must not accept a caller's claim that unpinned JSON
    # is an accepted actual source, even when it has superficially valid roles.
    with tempfile.TemporaryDirectory(prefix='hm-portable-guard-') as temp:
        root = Path(temp)
        (root / 'source.json').write_text('{}')
        (root / 'clearing.json').write_text('{}')
        cfg = {'roles': [0, 1, 2, 3], 'input': 'source.json',
               'clearingMetadata': 'clearing.json', 'outputDirectory': '.'}
        path = root / 'config.json'
        path.write_text(json.dumps(cfg))
        try:
            real_loader(path)
        except AssertionError as error:
            assert 'byte pin mismatch' in str(error)
            rejected.append('unbound-source')
        else:
            raise AssertionError('Unpinned source accepted')
        for roles in ([0, 1, 2, 2], [True, 1, 2, 3], [0, 1, 2]):
            cfg['roles'] = roles
            path.write_text(json.dumps(cfg))
            try:
                real_loader(path)
            except AssertionError:
                rejected.append('invalid-roles')
            else:
                raise AssertionError('Invalid role permutation accepted')
    print(json.dumps({'status': 'PASS', 'historicalNumericalBodyMatched': True,
                      'fixtures': results, 'guardsRejected': rejected,
                      'checkpointFormat': 'JSON only', 'actualSourceNodesEvaluated': 0}, indent=2))


if __name__ == '__main__':
    main()
