"""Pinned, isolated invented-input controls. Never imports a production module."""
import ast
import builtins
import dataclasses
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import symtable
import sys
from types import MappingProxyType

EXPECTED = '0efb8eff9bacacc9cddad9f29a598479c2c6925cf6472e2733ce4d37e841cc1c'
DEFINITIONS = ('LimitExceeded', 'NotLaurentPolynomial', '_integer', '_exponent',
               '_axis', 'Limits', 'Execution', '_same', 'Poly', 'Rational',
               'LaurentContext', 'LaurentCertificate')
EXECUTION_METHODS = {'__init__','limits','counts','check','tick','observe','q','add',
                     'mul','div','poly','constant','xpoly','rational'}
SAFE_BUILTINS = ('__build_class__','RuntimeError','ValueError','TypeError',
                 'ZeroDivisionError','object','type','int','str','tuple','list',
                 'dict','len','any','all','isinstance','getattr','hasattr',
                 'max','min','abs','range','zip','sorted','bool','property','NotImplemented')

def require(condition, message):
    if not condition:
        raise RuntimeError(message)

def expect_error(kind, thunk):
    try:
        thunk()
    except kind:
        return True
    raise RuntimeError('expected ' + kind.__name__)

def extract(candidate_path):
    raw = Path(candidate_path).read_bytes()
    require(hashlib.sha256(raw).hexdigest() == EXPECTED, 'candidate hash mismatch')
    tree = ast.parse(raw, filename='pinned-inert-candidate-text')
    # Top-level evaluation is reviewed: only docstring, the exact stdlib imports,
    # ZERO, _LAURENT_SEAL and definitions. No source/module import is executed.
    imports = [ast.unparse(n) for n in tree.body if isinstance(n, (ast.Import, ast.ImportFrom))]
    require(imports == ['from dataclasses import dataclass, field',
                        'from fractions import Fraction',
                        'from types import MappingProxyType'], 'imports changed')
    selected, removed = [], []
    for n in tree.body:
        if isinstance(n, (ast.FunctionDef, ast.ClassDef)) and n.name in DEFINITIONS:
            if n.name == 'Execution':
                kept = []
                for child in n.body:
                    if isinstance(child, ast.FunctionDef) and child.name not in EXECUTION_METHODS:
                        removed.append('Execution.' + child.name)
                    else:
                        kept.append(child)
                n.body = kept
            selected.append(n)
        elif isinstance(n, ast.Assign) and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name) and n.targets[0].id in ('ZERO', '_LAURENT_SEAL'):
            selected.append(n)
    require({n.name for n in selected if isinstance(n,(ast.ClassDef,ast.FunctionDef))} == set(DEFINITIONS), 'definition set mismatch')
    extracted = ast.fix_missing_locations(ast.Module(body=selected, type_ignores=[]))
    canonical = ast.dump(extracted, include_attributes=False)
    require(hashlib.sha256(canonical.encode()).hexdigest() == 'cfda96f5c5403152853f2ff0952371072e7cd12347fc0b8b20f7e35580ee21a3', 'extraction hash mismatch')
    source = ast.unparse(extracted)
    # All unresolved globals must come from this explicitly bounded arithmetic closure.
    globals_used = set()
    def walk_symbols(table):
        for symbol in table.get_symbols():
            if symbol.is_global() and symbol.is_referenced():
                globals_used.add(symbol.get_name())
        for child in table.get_children():
            walk_symbols(child)
    walk_symbols(symtable.symtable(source, '<isolated-arithmetic>', 'exec'))
    permitted = set(DEFINITIONS) | set(SAFE_BUILTINS) | {'ZERO','_LAURENT_SEAL','dataclass','field','Fraction','MappingProxyType'}
    require(globals_used <= permitted, 'unreviewed globals: ' + str(globals_used-permitted))
    require(not any(isinstance(n,(ast.Import,ast.ImportFrom)) for n in ast.walk(extracted)), 'extracted import')
    env = {'__builtins__': {n:getattr(builtins,n) for n in SAFE_BUILTINS},
           '__name__': __name__, 'dataclass':dataclasses.dataclass,
           'field':dataclasses.field, 'Fraction':Fraction, 'MappingProxyType':MappingProxyType}
    exec(compile(extracted, '<isolated-pinned-pure-arithmetic>', 'exec'), env)
    return env, {'candidate_sha256':EXPECTED,
                 'extraction_ast_sha256':hashlib.sha256(canonical.encode()).hexdigest(),
                 'global_dependency_closure':sorted(globals_used),
                 'omitted_execution_methods':removed,
                 'retained_definitions':list(DEFINITIONS)}

def run_toys(candidate_path):
    g, report = extract(candidate_path)
    Execution, Limits = g['Execution'], g['Limits']
    Context, Cert = g['LaurentContext'], g['LaurentCertificate']
    Z = (0,0,0,0)
    def e(k): return (k,0,0,0)
    # Every test meter has small finite algorithmic limits. All inputs invented here.
    def ex(): return Execution(Limits(products=10000,storage_events=20000,bit_height=64,steps=20000))
    results = []
    def check(name, value=True):
        require(value, name)
        results.append(name)
    a = ex(); x = a.xpoly(0); one = a.constant(1)
    numerator = a.poly(((e(2),3),(e(1),5),(Z,7))) * (x + one)
    denominator = x * (x + one)
    r = a.rational(numerator, denominator); ctx = Context(a, ('invented','frame'))
    before = dict(a.counts)
    cert = r.certify_laurent(ctx)
    after = dict(a.counts)
    check('certificate_retains_exact_rational_context_execution', cert.rational is r and cert.context is ctx and cert.ex is a and cert.quotient.ex is a)
    check('full_division_removes_nonmonomial_factor', cert.shift == e(1) and cert.quotient == a.poly(((e(2),3),(e(1),5),(Z,7))))
    check('invented_laurent_coefficients', [cert.coefficient(r,ctx,e(k)) for k in (-1,0,1,20)] == [7,5,3,0])
    p0 = a.counts['products']
    value = cert.weighted_coefficients(r,ctx,((e(-1),1),(e(0),2),(e(1),1)))
    p1 = a.counts['products']
    check('weighted_1_2_1_terminal_equals_20', value == Fraction(20))
    check('weighted_reads_reuse_quotient_only_three_weight_products', p1-p0 == 3)
    equivalent = a.rational(numerator,denominator)
    check('equal_but_distinct_rational_rejected', expect_error(ValueError,lambda:cert.coefficient(equivalent,ctx,Z)))
    same_labels = Context(a,('invented','frame'))
    check('same_labels_distinct_context_rejected', expect_error(ValueError,lambda:cert.coefficient(r,same_labels,Z)))
    foreign = ex()
    check('foreign_execution_context_rejected', expect_error(ValueError,lambda:r.certify_laurent(Context(foreign,('invented','frame')))))
    check('unsealed_construction_rejected', expect_error(TypeError,lambda:Cert(object(),r,ctx,e(1),cert.quotient)))
    check('certificate_immutable', expect_error(dataclasses.FrozenInstanceError,lambda:setattr(cert,'shift',Z)))
    check('context_immutable', expect_error(dataclasses.FrozenInstanceError,lambda:setattr(ctx,'frame',('changed',))))
    check('mutable_weight_requests_rejected', expect_error(TypeError,lambda:cert.weighted_coefficients(r,ctx,[(Z,1)])))
    # Missing requested support does not short-circuit full division.
    bad = a.rational(one,x+one)
    check('nonlaurent_certificate_rejects_remainder', expect_error(g['NotLaurentPolynomial'],lambda:bad.certify_laurent(ctx)))
    check('out_of_support_nonlaurent_legacy_read_still_rejects', expect_error(g['NotLaurentPolynomial'],lambda:bad.laurent_coefficient(e(20))))
    # The long division must continue after placing an irreducible lead in remainder.
    y = a.xpoly(1)
    q, rem = (x+y).divide(y)
    check('complete_division_after_irreducible_lead', q == one and rem == x)
    zero = a.rational(0,x+one); zc = zero.certify_laurent(ctx)
    check('canonical_zero_coefficient', zc.coefficient(zero,ctx,e(-10)) == 0)
    # Lifetime is tied to aggregate execution: poison invalidates old objects/certs.
    for cap in ('products','storage_events','steps','bit_height'):
        b=ex(); br=b.rational(2); bc=Context(b,('poison',cap)); old=br.certify_laurent(bc)
        trigger = (lambda: b.observe(Fraction(1<<65))) if cap == 'bit_height' else (lambda cap=cap:b.tick(cap,getattr(b.limits,cap)+1))
        check('poison_trigger_'+cap, expect_error(g['LimitExceeded'],trigger))
        for label, action in (
            ('certificate_read',lambda:old.coefficient(br,bc,Z)),
            ('weighted_read',lambda:old.weighted_coefficients(br,bc,((Z,1),))),
            ('recertify',lambda:br.certify_laurent(bc)),
            ('old_poly',lambda:br.numerator.is_zero()),
            ('new_arithmetic',lambda:b.constant(0))):
            check('permanent_poison_'+cap+'_'+label,expect_error(g['LimitExceeded'],action))
    # Exceed aggregate budget naturally during certification, not through test tick.
    trial=ex(); tr=trial.rational(trial.constant(1),trial.xpoly(0)+trial.constant(1)); tc=Context(trial,('short',))
    spent=trial.counts['steps']
    limited=Execution(Limits(products=10000,storage_events=20000,bit_height=64,steps=spent+1))
    lr=limited.rational(limited.constant(1),limited.xpoly(0)+limited.constant(1)); lc=Context(limited,('short',))
    check('certification_budget_failure_precedes_any_answer',expect_error(g['LimitExceeded'],lambda:lr.certify_laurent(lc)))
    check('certification_failure_poison_persists',expect_error(g['LimitExceeded'],lambda:lr.certify_laurent(lc)))
    report.update(status='PASS', tests=results, test_count=len(results),
                  invented_weighted_result=str(value), certificate_count_delta={k:after[k]-before[k] for k in after},
                  scope='isolated AST extraction only; no production import, physical data, actual ID0, source/model/owner or jets executed')
    return report

if __name__ == '__main__':
    # Guard is checked before reading candidate text or extraction, unconditionally.
    if len(sys.argv) < 2 or sys.argv[1] != 'invented-controls':
        print('REFUSED: actual_id0 and every mode other than invented-controls are disabled.',file=sys.stderr)
        raise SystemExit(2)
    if len(sys.argv) != 4 or sys.argv[2] != '--candidate-path':
        print('USAGE: test_extracted_arithmetic.py invented-controls --candidate-path FILE',file=sys.stderr)
        raise SystemExit(2)
    print(json.dumps(run_toys(sys.argv[3]),indent=2,sort_keys=True))
