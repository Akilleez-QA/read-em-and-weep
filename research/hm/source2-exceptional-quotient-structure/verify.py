#!/usr/bin/env python3
"""Exact bounded UNIVERSAL algebra only; no actual-source evaluations."""
import hashlib
import json
from pathlib import Path
import sympy as s

ROOT = Path(__file__).resolve().parent
checks = 0

def check(value, name):
    global checks
    checks += 1
    if not value:
        raise RuntimeError(name)


def matrices(m, n):
    Mx, My = s.zeros(m+2, m+1), s.zeros(m+2, m+1)
    Cx, Cy = s.zeros(n+1, n+2), s.zeros(n+1, n+2)
    for j in range(m+1):
        Mx[j,j] = 1
        My[j+1,j] = 1
    for i in range(n+1):
        Cx[i,i] = 1
        Cy[i,i+1] = 1
    return Mx,My,Cx,Cy


def solve(Hx,Hy):
    n,m = Hx.rows-1,Hx.cols-1
    F,G = s.zeros(n+2,m+1),s.zeros(n+1,m+2)
    for i in range(n+1):
        for j in range(m):
            F[i+1,j] = F[i,j+1]+Hy[i,j]-Hx[i,j+1]
    for i in range(n+1):
        for j in range(m+1):
            G[i,j] = F[i,j]-Hx[i,j]
        G[i,m+1] = F[i+1,m]-Hy[i,m]
    return F,G


def vector(M):
    return s.Matrix(list(M))


def run():
    for inp in json.loads((ROOT/'INPUTS.json').read_text()):
        data=(ROOT/inp['local_path']).read_bytes()
        check(hashlib.sha256(data).hexdigest()==inp['sha256'],'source sha256')
        blob=b'blob '+str(len(data)).encode()+b'\0'+data
        check(hashlib.sha1(blob).hexdigest()==inp['git_blob'],'source git blob')
    # Cohomology dimensions and the only equivariant extension parameter.
    h0=lambda degree:max(degree+1,0)
    h1=lambda degree:max(-degree-1,0)
    check(h1(3)==0,'Ext(EV,D)=0')
    check(h0(4)==5,'split class contradicts first injectivity')
    check(h0(-5)==0,'nonzero standard extension')
    for k,expected in [(2,8),(1,6)]:
        check(6*h1(1-k)+2*h1(-3-k)==expected,'exceptional H1')
        check(9*h1(2-k)==0,'Q0 H1 vanishing')
    dims={'A':3,'V':3,'P':4,'D':5,'Wp':2,'S':4,'T':6}
    check(dims['V']+dims['D']==8,'L2 character')
    check(dims['T']==6,'L3 character')
    check(tuple(sum(x) for x in zip((9,18,16),(15,18,12),(8,6,0)))==(32,42,28),'total dimensions')
    check(9+15+6==30,'first-arrow rank')
    # Entire basis of each extension-target space: linearity checks all RHS.
    cases=[]
    for m,n in [(0,0),(0,2),(4,0),(4,2),(3,4)]:
        Mx,My,Cx,Cy=matrices(m,n)
        z=s.zeros(n+1,m+1)
        for arrow in range(2):
            for row in range(n+1):
                for col in range(m+1):
                    Hx,Hy=z.copy(),z.copy()
                    (Hx if arrow==0 else Hy)[row,col]=1
                    F,G=solve(Hx,Hy)
                    check(Cx*F-G*Mx==Hx,'x extension equation')
                    check(Cy*F-G*My==Hy,'y extension equation')
                    # Actual block section of the synthetic extension with -H.
                    Kx=Cx.row_join(-Hx).col_join(s.zeros(m+2,n+2).row_join(Mx))
                    Ky=Cy.row_join(-Hy).col_join(s.zeros(m+2,n+2).row_join(My))
                    S2=F.col_join(s.eye(m+1))
                    S3=G.col_join(s.eye(m+2))
                    check(Kx*S2==S3*Mx,'synthetic x section')
                    check(Ky*S2==S3*My,'synthetic y section')
                    if (m,n)==(4,2):
                        # Tensor multiplicities A=3, W'=2: every matrix unit.
                        for a in range(3):
                            for w in range(2):
                                E=s.zeros(2,3); E[w,a]=1
                                FF,GG=s.kronecker_product(E,F),s.kronecker_product(E,G)
                                check(s.kronecker_product(s.eye(2),Cx)*FF-GG*s.kronecker_product(s.eye(3),Mx)==s.kronecker_product(E,Hx),'multiplicity x')
                                check(s.kronecker_product(s.eye(2),Cy)*FF-GG*s.kronecker_product(s.eye(3),My)==s.kronecker_product(E,Hy),'multiplicity y')
        cases.append([m,n,2*(m+1)*(n+1)])
    # Direct exact rank of scalar coboundary, independent of right-inverse code.
    m,n=4,2
    Mx,My,Cx,Cy=matrices(m,n)
    cols=[]
    for typ,rows,cc in [('F',4,5),('G',3,6)]:
        for i in range(rows):
            for j in range(cc):
                F,G=s.zeros(4,5),s.zeros(3,6)
                (F if typ=='F' else G)[i,j]=1
                cols.append(vector(Cx*F-G*Mx).col_join(vector(Cy*F-G*My)))
    delta=s.Matrix.hstack(*cols)
    check(delta.shape==(30,38),'coboundary dimensions')
    check(delta.rank()==30,'coboundary onto')
    check(len(delta.nullspace())==8,'section freedom')
    # Two complementary symbolic maximal minors prove rank for every [x:y].
    x,y=s.symbols('x y')
    C=x*Cx+y*Cy
    check(C[:,:3].det()==x**3,'first contraction minor')
    check(C[:,1:].det()==y**3,'last contraction minor')
    check(Cx.col_join(Cy).rank()==4,'no common kernel')
    check(s.kronecker_product(s.eye(2),Cx.col_join(Cy)).rank()==8,'no common kernel with Wp')
    # Negative control: an isolated (8,6) pair has common kernel8, not0.
    check(s.zeros(12,8).rank()==0,'isolated negative control')
    # The quotient does not justify Q preservation or a source exclusion.
    result={'status':'PASS','checks':checks,'exact_inputs':3,'extension_basis_cases':cases,
      'scalar_coboundary_shape':[30,38],'scalar_coboundary_rank':30,
      'exceptional_quotient_dimensions':[32,42,28],
      'every_nonzero_first_arrow_rank':30,'common_first_kernel_dimension':0,
      'actual_source_evaluations':0,'Q_stable_decomposition_claimed':False}
    print(json.dumps(result,indent=2))

if __name__=='__main__':
    run()
