#!/usr/bin/env python3
"""Independent exact checks of the invariant central criterion.

This deliberately does not import or test the fixed-presentation obstruction
tensor. The sheaf arguments are in central-criterion.md.
"""
from itertools import combinations
import sympy as sp


def zero(matrix):
    return all(sp.expand(entry) == 0 for entry in matrix)


ell, h, a = sp.symbols("ell h a")
J = sp.Matrix([[0, 1], [-1, 0]])
I, Z = sp.eye(2), sp.zeros(2)
L = sp.Matrix([[ell, h], [0, a]])


def mat(prefix):
    return sp.Matrix(2, 2, sp.symbols(prefix + "0:4"))


def sym(prefix):
    x, y, z = sp.symbols(prefix + "0:3")
    return sp.Matrix([[x, y], [y, z]])


def half(V):
    return V.T * J * V / 2


def cross(V, W):
    return (V.T * J * W - W.T * J * V) / 2


def g(V, S):
    return sp.BlockMatrix([[I, V.T * J, S + half(V)],
                           [Z, I, V], [Z, Z, I]]).as_explicit()


V, W, Ui, Uj, Q, R = [mat(p) for p in ("v", "w", "ui", "uj", "q", "r")]
S, T = sym("s"), sym("t")
Omega = sp.BlockMatrix([[Z, Z, I], [Z, J, Z], [-I, Z, Z]]).as_explicit()
G = g(V, S)
assert zero(G.T * Omega * G - Omega)
assert zero(g(V, S) * g(W, T) - g(V + W, S + T + cross(V, W)))
assert zero(g(V, S) * g(-V, -S) - sp.eye(6))
beta = L.row_join(Q).row_join(R)
assert zero(beta * Omega.inv() * beta.T - (R * L.T - L * R.T - Q * J * Q.T))
print("PASS full 6-by-6 symplectic convention, group law, inverse, and isotropy signs")

Qj = Q + L * V.T * J
Ri_new = R + Q * Ui + L * half(Ui)
# Rj is kept arbitrary: the claimed equality holds before the obstruction vanishes.
Rj = mat("rj")
Q_new = Q + L * Ui.T * J
Rj_new = Rj + Qj * Uj + L * half(Uj)
V_new = V + Uj - Ui
C = Rj - R - Q * V - L * half(V)
C_new = Rj_new - Ri_new - Q_new * V_new - L * half(V_new)
central_gauge = -cross(Ui, V) + cross(V, Uj) - cross(Ui, Uj)
assert zero(central_gauge - central_gauge.T)
assert zero(C_new - C - L * central_gauge)
print("PASS corrected obstruction is unchanged in N under arbitrary first-stage lift gauges")

residue_row = sp.Matrix([[a, -h]])
assert zero(residue_row * L - sp.Matrix([[a*ell, 0]]))
central_change = Q*V + L*(S+half(V))
assert zero((residue_row*central_change - residue_row*Q*V).subs(ell, 0))
print("PASS central changes preserve the regular cubic residue modulo the intrinsic quadrics on Y")

r, b, c, d, k, s = sp.symbols("r b c d k s")
Rsyz = sp.Matrix([[r, ell*b + h*c], [a*b + h*d, a*c - ell*d]])
assert zero(Rsyz * L.T - L * Rsyz.T)
reduced = sp.Matrix([[r-h*b, 0], [h*d, -ell*d]])
assert zero(Rsyz - L * sp.Matrix([[0, b], [b, c]]) - reduced)
P = sp.Matrix([[ell, h**2], [0, a]])
Rpair = lambda rr, dd: sp.Matrix([[rr, 0], [h*dd, -ell*dd]])
assert zero(Rpair(ell*s + h*h*k, a*k) - L*sp.Matrix([[s,h*k],[h*k,-ell*k]]))
assert sp.det(P) == a*ell
assert zero(sp.Matrix([[a, -h*h]]) * P - sp.Matrix([[a*ell, 0]]))
tau = sp.Matrix([0, ell])
assert zero(a*tau - P*sp.Matrix([-h*h, ell]))
Rt = Rpair(0, ell)
ordinary_gauge = sp.Matrix([[-h*h/a, h*ell/a], [h*ell/a, -ell*ell/a]])
assert zero(Rt - L*ordinary_gauge)
assert zero(Rt.subs(ell, 0))
print("PASS quotient relations, doubled-line image, torsion relation, and torsion rank invariance")

# On a=1, impose isotropy and expose the actual determinantal ideal.
q1,q2,d1,d2,rho,v,w = sp.symbols("q1 q2 d1 d2 rho v w")
Qord = sp.Matrix([[q1+h*d1,q2+h*d2],[d1,d2]])
Rord = sp.Matrix([[rho+h*v,ell*v+h*w+q1*d2-q2*d1],[v,w]])
Bord = L.subs(a,1).row_join(Qord).row_join(Rord)
assert zero(Rord*L.subs(a,1).T-L.subs(a,1)*Rord.T-Qord*J*Qord.T)
minor = lambda i,j: sp.expand(Bord[:,[i,j]].det())
assert minor(0,1)==ell
assert minor(1,2)==-q1 and minor(1,3)==-q2 and minor(1,4)==-rho
for i,j in combinations(range(6),2):
    assert sp.expand(minor(i,j).subs({ell:0,q1:0,q2:0,rho:0}))==0
print("PASS localized rank-minor ideal equals (ell, q1, q2, rho)")


def monomials(n, variables=4):
    if variables == 1:
        return [(n,)]
    return [(i,)+rest for i in range(n+1) for rest in monomials(n-i,variables-1)]


def cohomology_basis(base, relative):
    return [(e,m) for e in range(base+1,0) for m in monomials(relative)]


def multiply_add(M, row_map, col, e, mon, terms, offset=0):
    for power, spatial, coefficient in terms:
        out = (e+power, tuple(x+y for x,y in zip(mon,spatial)))
        if out in row_map:
            M[offset+row_map[out], col] += coefficient


# An unrelated balanced presentation: ell=s^4*x0+s^3*t*x1+s*t^3*x2+t^4*x3.
# Its two linear and one quadratic syzygies certify U=(2,1,1).
x = sp.symbols("x0:4")
st, tt = sp.symbols("s t")
coefficients = sp.Matrix([[st**4, st**3*tt, st*tt**3, tt**4]])
syz = sp.Matrix([[tt,0,0],[-st,tt**2,0],[0,-st**2,tt],[0,0,-st]])
assert zero(coefficients*syz)
# Delete rows only, since syz is 4-by-3.
maxmin = [sp.expand((-1)**i*syz[[j for j in range(4) if j!=i],:].det()) for i in range(4)]
assert all(sp.expand(maxmin[i]+coefficients[i])==0 for i in range(4))
unit = [tuple(int(i==j) for i in range(4)) for j in range(4)]
ell_terms = [(power,unit[j],1) for j,power in enumerate([0,1,3,4])]
src0,src1 = cohomology_basis(-12,2),cohomology_basis(-8,1)
dst0,dst1 = cohomology_basis(-8,3),cohomology_basis(-7,1)
row0,row1 = {b:i for i,b in enumerate(dst0)},{b:i for i,b in enumerate(dst1)}
assert (len(src0)+len(src1),len(dst0)+len(dst1)) == (138,164)


def induced_h1(h_coeff):
    hsquare=[]
    for i in range(4):
        for j in range(i,4):
            cij=h_coeff[i]*h_coeff[j]*(1 if i==j else 2)
            if cij:
                hsquare.append((0,tuple(unit[i][z]+unit[j][z] for z in range(4)),cij))
    M=sp.zeros(164,138)
    for col,(e,mon) in enumerate(src0):
        multiply_add(M,row0,col,e,mon,ell_terms)
    for relcol,(e,mon) in enumerate(src1):
        col=len(src0)+relcol
        multiply_add(M,row0,col,e,mon,hsquare)
        multiply_add(M,row1,col,e,mon,[(1,(0,0,0,0),1)],len(dst0))
    tau_boundary=sp.zeros(138,1)
    for _,mon,cij in hsquare:
        tau_boundary[src0.index((-1,mon))]=-cij
    tau_boundary[len(src0)+src1.index((-1,unit[0]))]=1
    assert M*tau_boundary==sp.zeros(164,1)
    assert M.rank()==137
    assert len(M.nullspace())==1
    return len(src0)+len(src1)-137,len(dst0)+len(dst1)-137


for hcoeff in [(0,1,0,0),(2,3,5,7)]:
    assert induced_h1(hcoeff)==(1,27)
    print("PASS direct rational Cech matrix 164-by-138 has rank 137 for h =",hcoeff)

# Independently enumerate all symmetric-power summands and doubled-line monomials.
degrees2=[sum(w*m for w,m in zip((2,1,1),mon))-1 for mon in monomials(2,3)]
degrees3=[sum(w*m for w,m in zip((2,1,1),mon))-7 for mon in monomials(3,3)]
assert sum(max(d+1,0) for d in degrees2)==16
assert sorted(degrees3)==[-4]*4+[-3]*3+[-2]*2+[-1]
assert sum(max(-d-1,0) for d in degrees3)==20
doubled=[mon for mon in monomials(3,3) if mon[0]<2]
reduced=[mon for mon in monomials(3,3) if mon[0]==0]
assert (len(doubled),len(reduced))==(7,4)
assert 20+len(doubled)==27
print("PASS symmetric-power cohomology and doubled-line length: radicalizing would lose 3 conditions")
print("VERDICT: invariant central criterion and its 1/27 dimensions pass; no existence claim")
