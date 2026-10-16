"""Tiny exact controls for the analytic E(delta f)=delta B(f) identity.

No HM model, source evaluator, jet payload, polynomial, or fiber is loaded.
The matrices here are arbitrary artificial rational2-by-2 values only.
"""
from fractions import Fraction as Q

def need(ok,message):
    if not ok:raise ValueError(message)
def mat(a):
    need(type(a)in(tuple,list)and len(a)==2 and all(type(r)in(tuple,list)and len(r)==2 for r in a),'two by two artificial matrix')
    need(all(type(x)is int or isinstance(x,Q)for r in a for x in r),'exact rational artificial entries')
    return tuple(tuple(Q(x)for x in r)for r in a)
ZERO=mat([[0,0],[0,0]])
ID=mat([[1,0],[0,1]])
def add(a,b):return mat([[a[i][j]+b[i][j]for j in range(2)]for i in range(2)])
def scale(c,a):return mat([[c*x for x in row]for row in a])
def sub(a,b):return add(a,scale(-1,b))
def mul(a,b):return mat([[sum((a[i][k]*b[k][j]for k in range(2)),Q(0))for j in range(2)]for i in range(2)])
def trace(a):return a[0][0]+a[1][1]
def tf(a):return sub(a,scale(trace(a)/2,ID))
def determinant(a):return a[0][0]*a[1][1]-a[0][1]*a[1][0]
def inv(a):
    d=determinant(a);need(d!=0,'invertible artificial frame')
    return mat([[a[1][1]/d,-a[0][1]/d],[-a[1][0]/d,a[0][0]/d]])
def conjugate_inverse(g,x):return mul(mul(inv(g),x),g)

def E(tij,tjk,La,Lb,Ua,Ub):
    """Actual source operator formula; t arrays contain (Va t,Vb t)."""
    return scale(Q(1,2),add(add(scale(tjk[0],Lb),scale(-tjk[1],La)),
        add(scale(tij[1],Ua),scale(-tij[0],Ub))))

def B(fi,fj,La,Lb):
    """Explicit row-End edge primitive for a scalar vertex coboundary.

    fi,fj contain (Va f_i,Vb f_i), in the same physical character frame.
    """
    return scale(Q(1,2),sub(scale(fi[1]+fj[1],La),scale(fi[0]+fj[0],Lb)))

class ArtificialCurrents:
    """Tangent data of arbitrary formal SL2 vertex frames, at one toy point.

    S_i(x)=S_i exp(x_a A_i+x_b B_i) realizes these first jets formally.
    Only supplied rational constants are used; no physical jet is sampled.
    """
    def __init__(self,frames,charges):
        need(type(frames)is dict and 1<=len(frames)<=4,'tiny artificial vertex domain')
        need(type(charges)is dict and set(frames)==set(charges),'artificial charge domain')
        self.frames={i:mat(s)for i,s in frames.items()};self.charges={}
        for i in frames:
            need(type(i)is int,'artificial vertex index');need(determinant(self.frames[i])==1,'SL2 artificial frames')
            need(type(charges[i])in(tuple,list)and len(charges[i])==2,'two current directions')
            pair=tuple(mat(a)for a in charges[i]);need(all(trace(a)==0 for a in pair),'traceless SL2 tangent')
            self.charges[i]=pair
    def g(self,i,j):return mul(self.frames[j],inv(self.frames[i]))
    def L(self,i,j,d):
        need(type(d)is int and d in(0,1),'toy direction')
        return mul(mul(self.frames[i],sub(self.charges[j][d],self.charges[i][d])),inv(self.frames[i]))
    def U(self,i,j,k,d):return conjugate_inverse(self.g(i,j),self.L(j,k,d))
    def delta_edge(self,edge_values,i,j,k):
        return add(sub(conjugate_inverse(self.g(i,j),edge_values(j,k)),edge_values(i,k)),edge_values(i,j))
    def E_triangle(self,edge_derivatives,i,j,k):
        return E(edge_derivatives(i,j),edge_derivatives(j,k),self.L(i,j,0),self.L(i,j,1),self.U(i,j,k,0),self.U(i,j,k,1))
    def B_edge(self,vertex_derivatives,i,j):return B(vertex_derivatives[i],vertex_derivatives[j],self.L(i,j,0),self.L(i,j,1))

def scalar_difference(values,i,j):return tuple(values[j][d]-values[i][d]for d in range(2))
