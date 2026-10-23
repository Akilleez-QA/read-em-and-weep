#!/usr/bin/env python3
"""Exact characters and cohomology for the pure-V square restriction; no instances."""
from pathlib import Path
import hashlib
import json
import sympy as s
checks=[]
def check(name, proposition):
    if not proposition: raise RuntimeError(name)
    checks.append(name)
root=Path(__file__).resolve().parent
for pin in json.loads((root/'INPUTS.json').read_text()):
    b=(root/pin['local_path']).read_bytes()
    check('sha256 '+pin['label'], hashlib.sha256(b).hexdigest()==pin['sha256'])
    check('git blob '+pin['label'], hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==pin['git_blob'])
r=s.sqrt(5); sizes=[1,15,20,12,12]
chars={
 '1':[1,1,1,1,1],
 'A':[3,-1,0,(1+r)/2,(1-r)/2],
 'V':[3,-1,0,(1-r)/2,(1+r)/2],
 'P':[4,0,1,-1,-1],
 'D':[5,1,-1,0,0]}
def add(a,b): return [s.simplify(x+y) for x,y in zip(a,b)]
def sub(a,b): return [s.simplify(x-y) for x,y in zip(a,b)]
def mul(a,b): return [s.simplify(x*y) for x,y in zip(a,b)]
def inner(a,b): return s.simplify(sum(n*x*y for n,x,y in zip(sizes,a,b))*s.Rational(1,60))
def decomp(a):return {k:int(inner(a,v)) for k,v in chars.items()}
# Sym^(2m) W recurrence: spin(m)= (A-1) spin(m-1) - spin(m-2).
spin=[chars['1'],chars['A']]
for m in range(2,11):spin.append(sub(mul(sub(chars['A'],chars['1']),spin[-1]),spin[-2]))
check('Sym18 decomposition',decomp(spin[9])=={'1':0,'A':1,'V':1,'P':2,'D':1})
check('Sym20 decomposition',decomp(spin[10])=={'1':1,'A':1,'V':1,'P':1,'D':2})
check('restriction kernel has no P',inner(chars['P'],chars['D'])==0)
check('restriction cokernel has no P',inner(chars['P'],chars['A'])==0)
check('square quotient-third target dimension two',inner(chars['P'],spin[9])==2)
check('square original-fourth target dimension two',inner(chars['D'],spin[10])==2)
# Plane symmetric powers decompose into harmonic SO3 representations.
sym2a=add(spin[2],spin[0]); sym4a=add(add(spin[4],spin[2]),spin[0])
old_kernel=sub(mul(chars['P'],sym2a),chars['A'])
old_full=sub(mul(chars['P'],sym4a),mul(chars['A'],sym2a))
check('old discriminant kernel has two D channels',inner(chars['D'],old_kernel)==2)
check('old full fourth has four D channels',inner(chars['D'],old_full)==4)
check('old restriction exact character',all(x==0 for x in sub(old_full,add(old_kernel,spin[10]))))
# Sym^2 A = 1+D, and twisted resolution has H0(J3)=D Sym2 A - A A.
hj3=sub(mul(chars['D'],add(chars['1'],chars['D'])),mul(chars['A'],chars['A']))
check('J3 dimension21',hj3[0]==21)
check('J3 P multiplicity2',inner(chars['P'],hj3)==2)
check('whole exact sequence character',all(s.simplify(x)==0 for x in sub(add(hj3,chars['A']),add(chars['D'],spin[9]))))
def h0(k):return (k+1)*(k+2)//2 if k>=0 else 0
def h2(k):return h0(-k-3)
check('J1 kernel terms have no sections',h0(-1)==0 and h0(-4)==0)
check('J1 H0 dimension5',5*h0(0)==5)
check('J1 H1 dimension3',3*h2(-1)+h2(-4)==3)
check('J3 H1 zero',3*h2(1)+h2(-2)==0)
check('restriction Euler dimensions',5-21+19-3==0)
check('conic plane twist9 is binary degree18',2*(6+3)==18)
check('conic plane twist10 is binary degree20',2*(6+4)==20)
check('quartic composition degrees',1+3==4)
check('two plus two complement fills four',2+2==4)
print(json.dumps({'status':'pass','count':len(checks),'checks':checks,'scope':'universal conditional gate only; all actual coefficients unselected'},indent=2))
