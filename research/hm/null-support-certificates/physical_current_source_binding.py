"""Exact parameterized physical first-current ASTs. No polynomial arithmetic.

Pinned polynomial references remain references; derivatives act syntactically on
I/di and P/dp, never on a frozen value with its logarithmic jets discarded.
"""
from dataclasses import dataclass
from pathlib import Path
import hashlib
import json
import owned_scalar_denominator_binding as owned

MODEL_SHA256='635bb12d9986e0dcada161d4173c773c4f134b9225354a3bc74267840ca19926'
SOURCE_SHA256='c4f65ff831092d0e56b3e33a0357f44182169fda45943ea780c8c551b4023f94'


def authenticate(path=None):
    path=Path(path) if path is not None else Path(__file__).with_name('hm-pinned-model.json')
    raw=path.read_bytes()
    if hashlib.sha256(raw).hexdigest()!=MODEL_SHA256:raise ValueError('pinned model hash mismatch')
    model=json.loads(raw)
    if len(model['charts'])!=6:raise ValueError('six canonical carriers required')
    for chart in model['charts']:
        if len(chart['I'])!=15 or any(len(r)!=2 for r in chart['I']):raise ValueError('I shape')
        if len(chart['P'])!=2 or any(len(r)!=15 for r in chart['P']):raise ValueError('P shape')
    return model

@dataclass(frozen=True)
class Matrix:
    op:str
    args:tuple
    shape:tuple
    def data(self):
        def enc(x):
            if isinstance(x,Matrix):return x.data()
            if isinstance(x,tuple):return [enc(y) for y in x]
            return x
        return {'op':self.op,'shape':list(self.shape),'args':[enc(x) for x in self.args]}

def mul(a,b):
    if a.shape[1]!=b.shape[0]:raise ValueError('matrix multiplication shape')
    return Matrix('multiply',(a,b),(a.shape[0],b.shape[1]))
def add(a,b):
    if a.shape!=b.shape:raise ValueError('matrix addition shape')
    return Matrix('add',(a,b),a.shape)
def neg(a):return Matrix('negate',(a,),a.shape)
def inverse(a):
    if a.shape!=(2,2):raise ValueError('rank two inverse required')
    # General rational inverse, not an unproved det=1 substitution.
    return Matrix('adjugate_over_determinant',(a,),a.shape)
def transpose(a):return Matrix('transpose',(a,),tuple(reversed(a.shape)))
def partial(a,d):
    if type(d) is not int or d not in range(4):raise ValueError('derivative coordinate')
    return Matrix('partial',(a,d),a.shape)
def block(v,name):
    if not isinstance(v,owned.VertexLabel):raise ValueError('full vertex required')
    if name not in ('I','P'):raise ValueError('transition block required')
    return Matrix('pinned_rational_block',(MODEL_SHA256,v.data(),name,'di' if name=='I' else 'dp'),(15,2) if name=='I' else (2,15))
def core(a,b):return transpose(mul(block(a,'P'),block(b,'I')))
def frame(v):return Matrix('physical_diagonal_frame',(v.data(),),(2,2))
def log_frame(v,d):
    if type(d) is not int or d not in range(4):raise ValueError('derivative coordinate')
    return Matrix('logarithmic_diagonal_frame',(v.data(),d),(2,2))
def tangent(a,b,d):
    K=core(a,b)
    return add(add(partial(K,d),mul(log_frame(b,d),K)),neg(mul(K,log_frame(a,d))))
def normalized_current(kind,d,vertices):
    if kind not in ('L','U'):raise ValueError('first current kind')
    if len(vertices)!=3 or not all(isinstance(v,owned.VertexLabel) for v in vertices):raise ValueError('three complete owners required')
    a,b,c=vertices
    if len({(v.seed,v.owner) for v in vertices})!=3:raise ValueError('distinct owner occurrences required')
    A=core(a,b)
    inside=mul(inverse(A),tangent(a,b,d)) if kind=='L' else mul(mul(mul(inverse(A),inverse(core(b,c))),tangent(b,c,d)),A)
    return inside

def current(kind,d,vertices):
    inside=normalized_current(kind,d,vertices)
    return mul(mul(frame(vertices[0]),inside),inverse(frame(vertices[0])))

def bind_instance(seed,branch):
    authenticate()
    kind,d,tail=branch['current']
    vertices=tuple(owned.label(seed,o) for o in tail)
    return {'id':branch['id']+':current','definition':'physical-first-current-source-v1',
        'owners':[v.data() for v in vertices],'kind':kind,'coordinate':d,
        'frame':'true physical first-owner, global finite stripped character',
        'source_ast':current(kind,d,vertices).data(),
        'normalized_source_ast':normalized_current(kind,d,vertices).data(),
        'adapter':'physical=D_first*normalized*D_first^-1; selector must apply matching inverse conjugation exactly once',
        'status':'exact parameterized source formula; physical frame normalization remains explicit'}

def definition():
    authenticate()
    return {'schema':'physical-first-current-source-v1','pinned_model_sha256':MODEL_SHA256,
        'source_excerpt_sha256':SOURCE_SHA256,
        'source_excerpt':'hm-pinned-source-formulas.js: build2 and globalBuild2 transition',
        'carrier_domain':list(range(6)),'carrier_identity':'5=star; -1 sorting key only, rejected as carrier',
        'block_rule':'choose charts[carrier]; I=I_numerator/di; P=P_numerator/dp',
        'polynomial_reference_rule':'stored exponent tuple is in (v1,v2,v3,v4); substitute vk=elementary_symmetric_k(x0,x1,x2,x3), v0=1; do not evaluate or expand',
        'partial_rule':'exact formal derivative of referenced rational function after elementary substitution; product, quotient, transpose rules; owner labels discrete',
        'inverse_rule':'adjugate(M)/det(M), on legal transition overlap; no determinant-one shortcut assumed',
        'physical_diagonal_frame':'D_a=diag(nu_a,nu_a^-1), owner-specific true physical frame; never set nu=1 as a moving function',
        'logarithmic_diagonal_frame':'Q_a,d=diag(ell_a,d,-ell_a,d); ell_a,d=legal_bit(mask_a,d)*(x_d^2+1)/(2*x_d*(x_d^2-1))',
        'bit_orders':{'legal':'low bit d','standard':'high bit 3-d'},
        'standard_rule':'standard tag retained as owner identity; these are global finite expressions restricted to each overlap, not local infinity-coordinate derivatives',
        'transition':'g_ab=D_b K_ab D_a^-1, K_ab=(P_a I_b)^t',
        'tangent':'T_ab,d=partial_d K_ab+Q_b,d K_ab-K_ab Q_a,d',
        'L':'D_a K_ab^-1 T_ab,d D_a^-1',
        'U':'D_a K_ab^-1 K_bc^-1 T_bc,d K_ab D_a^-1',
        'frame_obligations':['Physical absolute nu_a normalization is retained as a parameter; pinned nu[0]=1 fixes only a frozen-point gauge, not the moving physical frame value.',
            'Log derivative is mandatory. Locally nu_a^2=C_a product_d ((x_d^2-1)/x_d)^legal_bit(mask_a,d), with x-independent C_a fixed by the physical frame convention; do not assume C_a=1 from the frozen source.',
            'Inner endpoint roots cancel exactly in L/U. Outer conjugation has powers 0,+2,-2 only; prove same even parity after selector contraction before rational/Laurent lowering.',
            'Do not differentiate normalized moving core alone; retain both Q terms. Repeated derivatives require differentiating ell and the frame, not reusing squarefree nu jets.',
            'Source ordering and alternating transport remain external obligations; binding consumes already ordered full owner tuples and never sorts or merges them.'],
        'physical_polynomial_evaluation':False,'Laurent_admitted':False,'arithmetic_cost_certificate':False}

if __name__=='__main__':
    if not __debug__:raise SystemExit(2)
    print(json.dumps(definition(),sort_keys=True,separators=(',',':')))
