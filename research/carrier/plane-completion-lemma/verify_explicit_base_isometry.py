#!/usr/bin/env python3
"""Exact symbolic checks for the constructed plane completion only."""
import json
from pathlib import Path
import sympy as s

X,Y,W,z=s.symbols('X Y W z')
S=X**2+Y**2; F=X*Y; a=X**3+Y**3; w=W**6
g=S-z*W**2; C=S**2+z*S*W**2+z**2*W**4; T=-3*S+2*F
rF=s.Matrix([-a,w,-g,F,0]); rI=s.Matrix([-a,S**3,-g/z,F,0])
TB=s.diag(z**3,1,z**4,z**3); TB[1,2]=z*C
checks=[]

def zero(label, entries):
    values=list(entries) if isinstance(entries,s.MatrixBase) else [entries]
    bad=[str(s.factor(s.cancel(v))) for v in values if s.cancel(v)!=0]
    if bad:
        raise ValueError((label,bad))
    checks.append({'check':label,'entries':len(values),'result':'exact_zero'})

def J(i):
    return s.eye(5)[:,[j for j in range(5) if j!=i+1]]

def R(r,i):
    # Projection onto (P, remaining E coordinates in their order, q).
    return J(i).T*(s.eye(5)-r*s.eye(5)[i+1,:]/r[i+1])

def O(r,i):
    r1,r2,r3=r[1:4,0]
    o=s.zeros(5)
    o[1,2]=r3;o[1,3]=-r2;o[2,3]=r1
    o[0,4]=1;o[i+1,4]=a/r[i+1]
    return o-o.T

def M(r,i,j,infinity=False):
    if i==j:return s.eye(5)
    if (i,j) not in [(0,1),(1,2),(2,0)]:
        return 2*s.eye(5)-M(r,j,i,infinity)
    r1,r2,r3=r[1:4,0]
    if (i,j)==(0,1):
        b=s.Matrix([0,0,0,a/(r1*r2),0]); c=-T*F/(r1*r2) if infinity else T*F/(w*g)
    elif (i,j)==(1,2):
        b=s.Matrix([0,a/(r2*r3),0,0,0]); c=-1/(r2*r3) if infinity else z**3/(g*F)
    else:
        b=s.Matrix([0,0,a/(r3*r1),0,0]); c=0 if infinity else C/(w*F)
    b[0]=c
    return s.eye(5)+b*s.eye(5)[4,:]

def G(r,i,j,infinity=False):
    return R(r,i)*M(r,i,j,infinity)*J(j)

cross=[]
for i in range(3):
    m=s.zeros(5);m[:4,:4]=TB;m[4,4]=z
    if i==0:
        m[0,4]=z*C*T*F/(w*S**3)
        m[3,4]=-z*C*a/(w*S**3)
    cross.append(m)

tau=[R(rF,i)*cross[i]*J(i) for i in range(3)]
expected=[
    s.Matrix([[z**3,z*C*a/w,0,z*C*T*F/(w*S**3)],
              [0,z*S**3/w,0,0],
              [0,-z*C*F/w,z**3,-z*C*a/(w*S**3)],
              [0,0,0,z]]),
    s.diag(z**3,1,z**3,z),
    s.Matrix([[z**3,0,0,0],[0,1,z*C,0],[0,0,z**4,0],[0,0,0,z]])
]
zero('numerator_identity_finite',a*a-g*C-z**3*w-T*F**2)
zero('numerator_identity_infinity',a*a-S**3-T*F**2)
for tag,r,inf in [('finite',rF,False),('infinity',rI,True)]:
    for i in range(3):
        zero(f'{tag}_projection_{i}',R(r,i)*J(i)-s.eye(4))
        zero(f'{tag}_relation_{i}',R(r,i)*r)
        zero(f'{tag}_radical_{i}',O(r,i)*r)
        oi=J(i).T*O(r,i)*J(i)
        zero(f'{tag}_pfaffian_determinant_{i}',oi.det()-r[i+1]**2)
        for j in range(3):
            gij=G(r,i,j,inf)
            oj=J(j).T*O(r,j)*J(j)
            zero(f'{tag}_form_{i}{j}',gij.T*oi*gij-oj)
            zero(f'{tag}_inverse_{i}{j}',gij*G(r,j,i,inf)-s.eye(4))
            for k in range(3):
                zero(f'{tag}_cocycle_{i}{j}{k}',gij*G(r,j,k,inf)-G(r,i,k,inf))
for i in range(3):
    zero(f'cross_relation_{i}',cross[i]*rI-z**3*rF)
    zero(f'cross_full_form_{i}',cross[i].T*O(rF,i)*cross[i]-z**4*O(rI,i))
    zero(f'cross_explicit_matrix_{i}',tau[i]-expected[i])
    zero(f'cross_quotient_form_{i}',tau[i].T*(J(i).T*O(rF,i)*J(i))*tau[i]-z**4*(J(i).T*O(rI,i)*J(i)))
    det_expected=[z**8*S**3/w,z**7,z**8][i]
    zero(f'cross_determinant_{i}',tau[i].det()-det_expected)
    for j in range(3):
        zero(f'cross_mixed_cocycle_{i}{j}',tau[i]*G(rI,i,j,True)-G(rF,i,j,False)*tau[j])
    # P and the descended E0 section use projection, not a fictitious frame on U1.
    zero(f'cross_P_{i}',tau[i]*(R(rI,i)*s.eye(5)[:,0])-z**3*(R(rF,i)*s.eye(5)[:,0]))
    zero(f'cross_E0_{i}',tau[i]*(R(rI,i)*s.eye(5)[:,1])-(R(rF,i)*s.eye(5)[:,1]))

# Homogeneity as rational identities after an independent torus scaling.
t=s.symbols('t',nonzero=True)
scaling={z:t**2*z,X:t*X,Y:t*Y,W:W}
df=[3,0,2,2,1];di=[3,6,0,2,5]
for i in range(3):
    keep=[j for j in range(5) if j!=i+1]
    for m in range(4):
        for n in range(4):
            if expected[i][m,n]!=0:
                wt=df[keep[m]]-di[keep[n]]+6
                zero(f'cross_character_{i}_{m}{n}',expected[i][m,n].subs(scaling,simultaneous=True)-t**wt*expected[i][m,n])

receipt={'scope':'Exact identities for our constructed plane completion; no ancestor, normal-jet, carrier or defect identification.',
         'coefficient_ring':'Q(z,X,Y,W), with regularity restricted to the stated homogeneous overlap localizations',
         'checks':checks,'count':len(checks),'all_passed':True,
         'cross_determinants':['z^8 S^3/W^6','z^7','z^8']}
Path(__file__).with_name('EXPLICIT_BASE_ISOMETRY_CHECKS.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'count':len(checks),'all_passed':True,'scalar_matrix_entries_checked':sum(q['entries'] for q in checks)},indent=2))
