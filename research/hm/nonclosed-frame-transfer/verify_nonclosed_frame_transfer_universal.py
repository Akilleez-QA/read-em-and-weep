#!/usr/bin/env python3
"""Exact free noncommutative polynomial checks, no samples or linear solves.
Run: python verify_nonclosed_frame_transfer_universal.py
Words reduce only adjacent U U^-1 pairs. Thus each identity holds under every
size-compatible matrix substitution (including rectangular off-diagonal blocks).
"""
from time import perf_counter

class P:
    def __init__(self, terms=None): self.v = {w:c for w,c in (terms or {}).items() if c}
    def __add__(self,b):
        out=self.v.copy()
        for w,c in b.v.items(): out[w]=out.get(w,0)+c
        return P(out)
    def __neg__(self): return P({w:-c for w,c in self.v.items()})
    def __sub__(self,b): return self+-b
    def __mul__(self,b):
        out={}
        for a,c in self.v.items():
            for w,e in b.v.items():
                stack=[]
                for s in a+w:
                    if stack and ((s.endswith('!') and stack[-1]==s[:-1]) or (stack[-1].endswith('!') and s==stack[-1][:-1])): stack.pop()
                    else: stack.append(s)
                key=tuple(stack); out[key]=out.get(key,0)+c*e
        return P(out)
    def __eq__(self,b): return self.v==b.v
Z=P(); O=P({():1})
def sym(s): return P({(s,):1})
def mat(n=5): return [[Z for _ in range(n)] for _ in range(n)]
def eye():
    a=mat()
    for k in range(5): a[k][k]=O
    return a
def add(a,b): return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def neg(a): return [[-x for x in r] for r in a]
def sub(a,b): return add(a,neg(b))
def mul(a,b):
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))),Z) for j in range(len(b[0]))] for i in range(len(a))]
def prod(*args):
    r=args[0]
    for a in args[1:]: r=mul(r,a)
    return r
checks=0
def eq(a,b,label):
    global checks
    assert a==b,label
    checks+=1

def contraction(tag):
    # S_0 = [[1,X,Y],[0,U,Z],[0,0,1]], S_-1=S_1=1.
    x,y,z,u,v=(sym(tag+s) for s in ('X','Y','Z','U','U!'))
    s=eye(); si=eye()
    s[1][2]=x; s[1][3]=y; s[2][2]=u; s[2][3]=z
    si[1][2]=-x*v; si[1][3]=x*v*z-y; si[2][2]=v; si[2][3]=-v*z
    eq(mul(s,si),eye(),tag+' inverse'); eq(mul(si,s),eye(),tag+' inverse reverse')
    eq(mul(d,s),mul(s,d),tag+' chain map')
    inc=prod(s,i0); pr=prod(p0,si); h=prod(s,h0,si)
    eq(mul(pr,inc),[[O]],tag+' retraction')
    eq(add(mul(d,h),mul(h,d)),sub(eye(),mul(inc,pr)),tag+' homotopy')
    eq(mul(d,inc),[[Z] for _ in range(5)],tag+' closed inclusion')
    eq(mul(pr,d),[[Z]*5],tag+' closed projection')
    return inc,pr,h

def main():
    global d,h0,i0,p0
    start=perf_counter()
    d=mat(); d[1][0]=O; d[4][3]=O
    h0=mat(); h0[0][1]=O; h0[3][4]=O
    i0=[[Z],[Z],[O],[Z],[Z]]; p0=[[Z,Z,O,Z,Z]]
    C=[contraction('C'+a) for a in 'abc']; D=[contraction('D'+a) for a in 'abc']
    E=mat(); E[0][0]=sym('Eminus'); E[4][4]=sym('Eplus')
    for j in range(3):
        for k in range(3): E[j+1][k+1]=sym('E'+str(j+1)+str(k+1))
    T=sub(mul(d,E),mul(E,d))
    def g(fr,b,a): return mul(fr[b][1],fr[a][0])
    M=[prod(D[a][1],E,C[a][0]) for a in range(3)]
    defects={}
    for b in range(3):
        for a in range(3):
            defect=sub(mul(M[b],g(C,b,a)),mul(g(D,b,a),M[a]))
            rhs=prod(D[b][1],add(mul(T,C[b][2]),mul(D[a][2],T)),C[a][0])
            eq(defect,rhs,f'typed transfer {b}{a}'); defects[b,a]=defect
            for frames in (C,D):
                eq(mul(g(frames,a,b),g(frames,b,a)),[[O]],'transition inverse')
                for c in range(3): eq(mul(g(frames,c,b),g(frames,b,a)),g(frames,c,a),'transition cocycle')
            for c in range(3):
                lhs=sub(mul(M[c],g(C,c,a)),mul(g(D,c,a),M[a]))
                rhs=add(mul(sub(mul(M[c],g(C,c,b)),mul(g(D,c,b),M[b])),g(C,b,a)),mul(g(D,c,b),defect))
                eq(lhs,rhs,'three-chart typed defect cocycle')
    # Closed degree-zero cochain: endpoint-compatible triangular middle block.
    F=mat(); F[0][0]=sym('P'); F[4][4]=sym('Q')
    F[1][1]=F[0][0]; F[3][3]=F[4][4]
    F[1][2]=sym('R'); F[1][3]=sym('V'); F[2][2]=sym('W'); F[2][3]=sym('J')
    eq(mul(d,F),mul(F,d),'closed cochain including endpoints')
    for b in range(3):
        for a in range(3): eq(prod(D[b][1],F,C[b][0],g(C,b,a)),prod(g(D,b,a),D[a][1],F,C[a][0]),'closed transfer')
    # Adjoint vanishing cannot remove the central closed cochain s*identity.
    central=mat()
    for k in range(5): central[k][k]=O
    eq(mul(d,central),mul(central,d),'identity is closed')
    eq(prod(p0,central,i0),[[O]],'closed scalar transfer survives')
    assert prod(p0,central,i0)!=[[Z]],'adjoint vanishing is not full vanishing'
    # Scalar example is also checked as a NONCOMMUTATIVE identity, stronger
    # than commutative scalar evaluation. Set the frame's U=1 algebraically.
    x,y,z=(sym(s) for s in ('x','y','z'))
    s=eye(); si=eye(); s[1][2]=x; s[1][3]=y; s[2][3]=z
    si[1][2]=-x; si[1][3]=x*z-y; si[2][3]=-z
    ib=mul(s,i0); pb=mul(p0,si); hb=prod(s,h0,si)
    lhs=sub(prod(pb,E,ib),prod(pb,i0,p0,E,i0))
    # Here g_ba=1, but M_b must multiply g_ba and a is the base chart.
    term_b=prod(pb,T,hb,i0); term_a=prod(pb,h0,T,i0)
    # In noncommutative order M_b-M_a=E21*x-z*E31*x-z*E32.
    expected=sym('E21')*x-z*sym('E31')*x-z*sym('E32')
    eq(lhs,[[expected]],'base-to-triangular explicit expression')
    eq(term_b,[[sym('E21')*x-z*sym('E31')*x]],'h_b contribution')
    eq(term_a,[[-z*sym('E32')]],'h_a contribution')
    eq(lhs,add(term_b,term_a),'two-term regression oracle')
    assert lhs!=term_a and lhs!=term_b,'missing-term mutations must fail'
    assert lhs!=sub(term_b,term_a) and lhs!=sub(term_a,term_b),'sign mutations must fail'
    elapsed=perf_counter()-start
    assert elapsed<60,'bounded test exceeded 60 seconds'
    print(f'PASS: {checks} exact free-word identities; 4 negative mutation tests; {elapsed:.3f}s')
    print('PASS: independent source/target frames, endpoint blocks, all 27 triple overlaps, closed limit')
    print('SCALAR COMMUTATIVE SPECIALIZATION: x E21 - z E32 - x z E31')
    print('SCOPE: universal transfer identity only; no actual HM row-factorization or affine-square claim')
if __name__=='__main__': main()
