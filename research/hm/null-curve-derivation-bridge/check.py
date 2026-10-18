"""Static binding plus invented free differential-symbol controls; never executes source AST."""
import ast
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE/'inputs/field.py.txt'
CANDIDATE = HERE/'inputs/candidate-field.py.txt'
PINS = {
    'inputs/field.py.txt': '4dade295de59741ceb54eb4574c58ffc82c8a1a17063fd1c081656a8b2069b01',
    'inputs/candidate-field.py.txt': '0efb8eff9bacacc9cddad9f29a598479c2c6925cf6472e2733ce4d37e841cc1c',
    'reference-methods.txt': '217f52c04b2680287c9bc3d30cccac790f5fed8e6da913ac70dc5488cab07284',
}
checks = 0

def require(ok, message):
    global checks
    checks += 1
    if not ok:
        raise RuntimeError(message)

def methods(tree):
    return {f'{c.name}.{m.name}': m for c in tree.body if isinstance(c, ast.ClassDef)
            for m in c.body if isinstance(m, ast.FunctionDef)}

def shape(node):
    return ast.dump(node, include_attributes=False)

text = SOURCE.read_text()
for path, digest in PINS.items():
    require(hashlib.sha256((HERE/path).read_bytes()).hexdigest() == digest, 'pin: '+path)
m = methods(ast.parse(text))
cm = methods(ast.parse(CANDIDATE.read_text()))
# Explicit reviewed AST skeletons are separate reference text, not compiled/executed.
reference = ast.parse((HERE/'reference-methods.txt').read_text())
ref = methods(reference)
require(len(ref) == 8, 'exactly eight reviewed reference contracts')
for key, expected in ref.items():
    require(shape(m[key]) == shape(expected), 'reference AST mismatch: '+key)
# All non-terminal core methods match the inert published candidate. Added certificate
# entry points/legacy terminal changes are outside this derivation theorem.
shared = [k for k in m if not k.endswith('.laurent_coefficient')]
require(len(shared) == 53, 'exactly 53 original nonterminal class methods')
for key in shared:
    require(key in cm and shape(m[key]) == shape(cm[key]), 'candidate core mismatch: '+key)

# Reject independently specified semantic source mutations through exact AST contracts.
mutations = [
 ('xor-to-or', 'yield a ^ b, q', 'yield a | b, q', 'Element.__mul__'),
 ('overlap-to-union', 'if a & b & (1 << i):', 'if (a | b) & (1 << i):', 'Element.__mul__'),
 ('basis-sign', '(x * x).scale(3) - self.ex.constant(1)', '(x * x).scale(3) + self.ex.constant(1)', 'Element.V'),
 ('missing-half', 'Fraction(1, 2)', 'Fraction(1, 1)', 'Element.V'),
 ('missing-basis-toggle', 'pieces.append((mask ^ (1 << i),', 'pieces.append((mask,', 'Element.V'),
 ('quotient-sign', 'self.numerator.partial(i) * self.denominator -', 'self.numerator.partial(i) * self.denominator +', 'Rational.partial'),
 ('quotient-denominator', 'self.denominator * self.denominator)', 'self.denominator)', 'Rational.partial'),
 ('coefficient-exponent', 'self.ex.q(e[i])', 'self.ex.q(1)', 'Poly.partial'),
 ('jet-reset', 'result = result.V(i)', 'result = self.V(i)', 'Element.jet'),
 ('jet-reversed', 'for i in axes:', 'for i in reversed(axes):', 'Element.jet'),
]
for name, old, new, key in mutations:
    require(old in text, 'mutation precondition: '+name)
    mutant = methods(ast.parse(text.replace(old,new)))
    require(shape(mutant[key]) != shape(ref[key]), 'mutation escaped: '+name)

# Invented free commutative differential symbols only. A word contains abstract
# C_i, h_i, h'_i, ... tokens and exactly one c_multiindex token. No x-polynomial,
# source value, physical owner, field object or production jet is constructed.
def clean(p):
    return {w:a for w,a in p.items() if a}
def add(p,q):
    out=dict(p)
    for w,a in q.items(): out[w]=out.get(w,0)+a
    return clean(out)
def token_mul(p,t,n=1):
    return {tuple(sorted(w+(t,))): n*a for w,a in p.items()}
def scale(p,n): return {w:n*a for w,a in p.items() if n*a}
def partial(p,i):
    out={}
    for word,a in p.items():
        for j,t in enumerate(word):
            if t[0]=='c':
                ix=list(t[1:]); ix[i]+=1; replacement=('c',*ix); factor=1
            elif t[1] != i: continue
            elif t[0]=='C': replacement=('h',i,0); factor=2
            else: replacement=('h',i,t[2]+1); factor=1
            new=tuple(sorted(word[:j]+word[j+1:]+(replacement,)))
            out[new]=out.get(new,0)+factor*a
    return clean(out)
def action(mask,p,i):
    d=partial(p,i)
    if mask & (1<<i): d=add(token_mul(d,('C',i)),token_mul(p,('h',i,0)))
    return mask^(1<<i),d
base={(('c',0,0,0,0),):1}
# Exhaustively check the finite Boolean reduction for all basis pairs.
for a in range(16):
    for b in range(16):
        exps=[((a>>i)&1)+((b>>i)&1) for i in range(4)]
        require(a^b == sum((e%2)<<i for i,e in enumerate(exps)), 'XOR parity')
        require([i for i in range(4) if a&b&(1<<i)] == [i for i,e in enumerate(exps) if e==2], 'one curve per overlap')
for mask in range(16):
    for i in range(4):
        t,p=action(mask,base,i)
        t,p=action(t,p,i)
        expected=token_mul(partial(partial(base,i),i),('C',i))
        expected=add(expected,token_mul(partial(base,i),('h',i,0),3 if mask&(1<<i) else 1))
        if mask&(1<<i): expected=add(expected,token_mul(base,('h',i,1)))
        require(t==mask and p==expected, 'repeated derivative')
        for j in range(4):
            a,p=action(mask,base,i); a,p=action(a,p,j)
            b,q=action(mask,base,j); b,q=action(b,q,i)
            require(a==b and p==q, 'mixed commutation')
print(json.dumps({'status':'PASS','checks':checks,'reference_methods':sorted(ref),'candidate_identical_core_methods':len(shared),'mutations_rejected':[x[0] for x in mutations],'production_imports':False,'physical_evaluation':False,'actual_polynomial_products':False,'scope':'Static AST contracts and invented free differential-symbol controls, not a mechanized proof of prose or a production run'},indent=2,sort_keys=True))
