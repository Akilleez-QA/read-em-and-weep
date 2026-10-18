"""Formal coefficient tests only. No model imports or source-point values."""
from fractions import Fraction as F

def forms(x):
    ell,p,b=x[:3],x[3:6],x[6:]
    gamma=[ell[i]-b[i]/2 for i in range(3)]
    a=[ell[i]-p[i]/2 for i in range(3)]
    d=[gamma[i]-a[i] for i in range(3)]
    tau=[8*ell[i]-4*p[i]+30*gamma[i] for i in range(3)]
    return ell,p,b,d,tau

def coefficients(x):
    ell,p,b,d,tau=forms(x)
    eta01=b[1]-b[0]+2*(d[1]-d[0])
    trace12=tau[2]-tau[1]+15*(b[2]-b[1])
    return eta01,trace12,p[1]-p[0],ell[2]-ell[1],p[2]-p[1]

def main():
    basis=[[F(int(j==k)) for j in range(9)] for k in range(9)]
    for x in basis:
        ell,p,b,d,tau=forms(x)
        for i,j in ((0,1),(1,2),(0,2)):
            eta=b[j]-b[i]+2*(d[j]-d[i])
            if eta!=p[j]-p[i] or tau[j]-tau[i]+15*(b[j]-b[i])!=38*(ell[j]-ell[i])-4*eta:
                raise RuntimeError('linear coefficient mismatch')
    for x in basis:
        for y in basis:
            a,t,u,r,v=coefficients(x);A,T,U,R,V=coefficients(y)
            if (a*T-A*t)/2 != 19*(u*R-U*r)-2*(u*V-U*v):
                raise RuntimeError('wedge coefficient mismatch')
    print('PASS: 27 linear edge checks and 81 wedge basis checks; no source evaluation')

if __name__=='__main__':main()
