"""Factored actual denominator definitions; purely syntactic, never polynomial evaluation."""
from dataclasses import dataclass
from itertools import combinations

@dataclass(frozen=True)
class VertexLabel:
    seed: int
    owner: int
    carrier: object
    legal_mask: object
    standard_tag: object
    def __post_init__(self):
        if type(self.seed) is not int or type(self.owner) is not int or self.owner<0:raise ValueError('owner label')
        if not isinstance(self.carrier,tuple) and (type(self.carrier) is not int or self.carrier not in (0,1,2,3,4,5)):raise ValueError('canonical carrier ID required; -1 is only a sorting key')
        for value in (self.legal_mask,self.standard_tag):
            if not isinstance(value,tuple) and (type(value) is not int or not 0<=value<16):raise ValueError('mask or standard tag')
    def data(self):return (self.seed,self.owner,self.carrier,self.legal_mask,self.standard_tag)

def label(seed,owner):
    # The tags belong to the source-first sorted tuple, not necessarily the
    # same position in the staircase before sorting. Keep all three fields.
    return VertexLabel(seed,owner,('carrier',seed,owner),('legal_mask',seed,owner),('standard_tag',seed,owner))

@dataclass(frozen=True)
class Factor:
    op: str
    args: tuple
    def __post_init__(self):
        arities={'integer':1,'coordinate':1,'add':2,'multiply':2,'power':2,'choice':2}
        if self.op not in arities or len(self.args)!=arities[self.op]:raise ValueError('factor node')
        if self.op=='integer' and type(self.args[0]) is not int:raise ValueError('integer')
        if self.op=='coordinate' and (type(self.args[0]) is not int or not 0<=self.args[0]<4):raise ValueError('coordinate')
        if self.op in ('add','multiply') and not all(isinstance(a,Factor) for a in self.args):raise ValueError('factor operands')
        if self.op=='power' and (not isinstance(self.args[0],Factor) or type(self.args[1]) is not int or self.args[1]<0):raise ValueError('power')
        if self.op=='choice' and (not isinstance(self.args[0],tuple) or not isinstance(self.args[1],tuple) or not all(isinstance(a,Factor) for a in self.args[1])):raise ValueError('choice')
    def __add__(self,b):return Factor('add',(self,b))
    def __mul__(self,b):return Factor('multiply',(self,b))
    def power(self,n):return Factor('power',(self,n))
    def data(self):
        def enc(a):
            if isinstance(a,Factor):return a.data()
            if isinstance(a,tuple):return tuple(enc(x) for x in a)
            return a
        return (self.op,*map(enc,self.args))

def integer(n):return Factor('integer',(n,))
def product(xs):
    out=integer(1)
    for x in xs:out=out*x
    return out

def elementary(xs,k):
    out=integer(0)
    for inds in combinations(range(len(xs)),k):out=out+product(xs[j] for j in inds)
    return out

def derivative(node,i):
    if type(i) is not int or not 0<=i<4:raise ValueError('derivative coordinate')
    op=node.op;a=node.args
    if op=='integer':return integer(0)
    if op=='coordinate':return integer(int(a[0]==i))
    if op=='add':return derivative(a[0],i)+derivative(a[1],i)
    if op=='multiply':return derivative(a[0],i)*a[1]+a[0]*derivative(a[1],i)
    if op=='power':return integer(0) if a[1]==0 else integer(a[1])*a[0].power(a[1]-1)*derivative(a[0],i)
    if op=='choice':return Factor('choice',(a[0],tuple(derivative(b,i) for b in a[1])))
    raise ValueError('unknown derivative node')

def denominator(v):
    if not isinstance(v,VertexLabel):raise ValueError('complete vertex label required')
    xs=tuple(Factor('coordinate',(i,)) for i in range(4))
    es=(integer(1),)+tuple(elementary(xs,k) for k in range(1,5))
    prod=product(es)
    carriers=(es[0]*es[1]*es[3]*es[4],)+tuple(e.power(5)+integer(-1)*prod for e in es)
    H=Factor('choice',(('carrier',v.data(),(5,0,1,2,3,4)),carriers))
    legal=[];standard=[]
    for i,x in enumerate(xs):
        legal.append(Factor('choice',(('legal_bit',v.data(),i),(integer(1),x*(x.power(2)+integer(-1))))))
        standard.append(Factor('choice',(('standard_bit',v.data(),i),(integer(1),x))))
    return H.power(14)*product(legal)*product(z.power(5250) for z in standard)

def character_conversion(derivative_pair,input_pair,coordinate):
    if tuple(sorted(derivative_pair)) not in ((0,1),(2,3)) or tuple(sorted(input_pair)) not in ((0,1),(2,3)):
        raise ValueError('unsupported character pair')
    if set(derivative_pair)&set(input_pair) or coordinate not in derivative_pair:raise ValueError('not complementary zero-character derivative')
    return {'c':1,'alpha':1,'beta':0,'input_character':tuple(-2 if i in input_pair else 0 for i in range(4)),
        'frame':'global-finite-product-frame','identity':'V_i=y_i partial_xi; strip newly introduced output y_i; input character i=0',
        'infinity_chart_local_derivative_substitution':False}

def decode_legal_mask(mask):
    if type(mask) is not int or not 0<=mask<16:raise ValueError('legal mask')
    return tuple((mask>>i)&1 for i in range(4))

def decode_standard_tag(tag):
    if type(tag) is not int or not 0<=tag<16:raise ValueError('standard tag')
    return tuple((tag>>(3-i))&1 for i in range(4))

def choice_index(key):
    """Discrete label selection only; never evaluates a physical polynomial."""
    kind,fields,arg=key
    v=VertexLabel(*fields)
    if kind=='carrier':
        if type(v.carrier) is not int or v.carrier not in arg:raise ValueError('unbound carrier')
        return arg.index(v.carrier)
    if kind=='legal_bit':return decode_legal_mask(v.legal_mask)[arg]
    if kind=='standard_bit':return decode_standard_tag(v.standard_tag)[arg]
    raise ValueError('choice key')

def definition():
    v=label(-1,0)
    return {'schema':'owned-scalar-denominator-factored-v1','vertex_label_fields':['seed','owner','carrier','legal_mask','standard_tag'],
        'carrier_domain':[5,0,1,2,3,4],'carrier_identity':'canonical source IDs: 5=star; 0..4=primary; -1 is only a sorting key, never a carrier ID','legal_mask_bit_order':'coordinate i is low bit i', 'standard_tag_bit_order':'coordinate i is high bit (3-i)',
        'legal_mask_domain':[0,15],'standard_tag_domain':[0,15],
        'vertex_domain':'all 6*16*16 common vertices, including finite-standard/legal-mask1 opens; zero active weight does not delete a column',
        'coordinate_frame':'Y_i=1,X_i=x_i','v_definition':'v0=1; vk=elementary_symmetric_k(x0,x1,x2,x3)',
        'template_label':v.data(),'factored_ast':denominator(v).data(),
        'derivative_rule':'exact recursive sum/product/power rule; choice labels are discrete constants',
        'edge_definition':'D_uv=d_u*d_v; partial_iD=(partial_i d_u)d_v+d_u(partial_i d_v)',
        'physical_polynomial_evaluation':False}
