"""Only invented rank-(1,3,1) rational examples; no source/model input."""
from fractions import Fraction as F
import json


def require(ok, message):
    if not ok:
        raise ValueError(message)


def mat(rows):
    return [[F(x) for x in row] for row in rows]


def mul(a, b):
    return [[sum((x*y for x,y in zip(row,col)),F(0)) for col in zip(*b)] for row in a]


def add(*args):
    return [[sum(values,F(0)) for values in zip(*rows)] for rows in zip(*args)]


def neg(a):
    return [[-x for x in row] for row in a]


def identity(n):
    return [[F(i==j) for j in range(n)] for i in range(n)]


def iszero(a):
    return all(not x for row in a for x in row)


# Coordinates F={0}, D={1}, S={2}. These are deliberately unrelated to HM data.
gamma=mat([[1],[2],[3]])
inclusion=mat([[0],[1],[4]])
h0=mat([[1,0,0]])
p=mat([[-2,1,0]])
eD=mat([[0,1,0]])
eS=mat([[0],[0],[1]])
N=mat([[1,0,0],[2,1,0],[3,4,1]])
Ninv=mat([[1,0,0],[-2,1,0],[5,-4,1]])
require(mul(N,Ninv)==identity(3) and mul(Ninv,N)==identity(3),'Invented inverse')
require(mul(h0,gamma)==identity(1),'Invented retraction')
require(p==mul(eD,add(identity(3),neg(mul(gamma,h0)))),'Invented quotient projection')
require(iszero(mul(p,gamma)),'Invented annihilation')
require(mul(p,inclusion)==identity(1),'Invented normalized inclusion')

base_delta=mat([[F(5,2),-2,F(1,2)]])
cases=[
    ('exact',F(2),base_delta,(False,False,False)),
    ('complex_gamma_defect',F(2),mat([[F(7,2),-2,F(1,2)]]),(True,False,False)),
    ('cycle_inclusion_defect',F(2),mat([[F(1,2),-1,F(1,2)]]),(False,True,False)),
    ('complement_inverse_defect',F(3),base_delta,(False,False,True)),
]
for name,h,delta,expected_nonzero in cases:
    h1=mat([[0],[0],[h]])
    require(iszero(mul(h0,h1)) and iszero(mul(p,h1)),'Invented homotopy support')
    R=add(mul(gamma,h0),mul(inclusion,p),mul(h1,delta),neg(identity(3)))
    transformed=mul(mul(Ninv,R),N)
    expected=mat([[0,0,0],[0,0,0],[
        h*mul(delta,gamma)[0][0],
        h*mul(delta,inclusion)[0][0],
        h*mul(delta,eS)[0][0]-1,
    ]])
    require(transformed==expected,f'Invented defect block: {name}')
    observed=tuple(bool(x) for x in expected[2])
    require(observed==expected_nonzero,f'Invented defect pattern: {name}')
    require(iszero(R)==(name=='exact'),f'Invented A comparison: {name}')

print(json.dumps({
    'status':'PASS',
    'invented_dimensions':{'gamma': [3,1], 'I':[3,1], 'H1':[3,1]},
    'exact_case':True,
    'separate_unresolved_family_countercontrols':3,
    'model_or_source_files_read':0,
    'physical_arithmetic':False
},indent=2))
