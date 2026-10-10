# Cayley–spinor acyclicity on the five-dimensional quadric

Work over a field of characteristic zero. Let Q = G2/P1 be the smooth five-dimensional quadric, C its normalized Cayley bundle, and S the negative rank-four spinor bundle, so that C is the cohomology of O(-1) -> S -> O. Then

\[
H^i(Q,\operatorname{End}(C)\otimes S(-2))=0\qquad\text{for all }i.
\]

The proof below computes the previously undetermined scalar connecting the two one-dimensional cohomology groups. No choice that this scalar is generically nonzero is made.

## 1. Bott reduction

Write E = End_0(C) = Sym^2(C)(1). The trace part S(-2) is acyclic. The G2-equivariant filtration of S has associated graded O(-1), C, O. Consequently E tensor S(-2) has associated graded

\[
E(-3),\quad E\otimes C(-2),\quad E(-2).
\]

In fundamental-weight coordinates, C has highest weight (-2,1), E has highest weight (-3,2), and O(1) has weight (1,0). Thus

- E(-2) has highest weight (-5,2). Adding rho and reflecting gives (-4,3) -> (4,-1) -> (1,1), so its only cohomology is H^2 = k, the trivial G2 representation;
- E(-3) has highest weight (-6,2). Adding rho and reflecting gives (-5,3) -> (5,-2) -> (-1,2) -> (1,1), so its only cohomology is H^3 = k, the trivial G2 representation;
- E tensor C(-2) = Sym^3(C)(-1) direct-sum C(-2) is acyclic.

For the last assertion the highest weights are (-7,3) and (-4,1). After adding rho, (-6,4) reflects to (6,-2) and then (0,2), a wall; (-3,2) reflects to (3,-1) and then (0,1), also a wall. We use s1(a,b)=(-a,b+a) and s2(a,b)=(a+3b,-b).

It follows that all possibly nonzero cohomology of E tensor S(-2) consists of trivial G2 representations in degrees 2 and 3. Computing the G2-invariant part therefore computes the full cohomology.

## 2. Relative Lie-algebra model

Choose the negative parabolic P, with Levi factor L, whose semisimple part is SL2 for the long root. Its nilradical n is the free three-step nilpotent Lie algebra on two generators. Choose a basis x,y,z,u,v with

\[
[x,y]=z,\qquad [x,z]=u,\qquad [y,z]=v,
\]

all other brackets zero. The coefficients can all be normalized to 1 by rescaling z,u,v. Under the Levi SL2, (x,y) and (u,v) are standard doublets, and z is trivial. Their central degrees are respectively (-1,-1,-2,-3,-3); degree denotes the coefficient of the short root in the weight. A line bundle O(-1) has central degree -2.

As an L-module, S has a basis s,a,b,c, where s and c are SL2 singlets and (a,b) is standard. Their central degrees are 0,-1,-1,-2. The nilradical action is

\[
xs=a,\quad ys=b,\quad xb=c,\quad ya=-c,\quad zs=2c,
\]

with all remaining actions zero.

Here is why this is the actual restricted spinor representation, rather than a trial representation. Its filtration has O(-1) at the bottom, C in the middle, and O at the top. Both adjacent extensions are nonzero. The first, 0 -> O(-1) -> G^* -> C -> 0, is the nonzero class in Ext^1(C,O(-1))=H^1(C)=k constructed in Ottaviani, section 2. Equivalently, it cannot split because G^* is slope-stable of slope -2/3 whereas C has slope -1/2 and would be a destabilizing direct summand. The second extension projects to the nonzero class in Ext^1(O,C)=H^1(C)=k, as follows from H^0(S)=H^1(S)=0 and the acyclicity of O(-1). These are the two nontrivial extensions of the Cayley monad. Central weights show that the only maps responsible for these adjacent extensions are the degree -1 nilradical actions. Levi equivariance makes the first map a nonzero multiple of the identity on the standard representation and the next a nonzero multiple of its alternating determinant pairing. Rescaling a,b,c gives the displayed action; the bracket [x,y]=z then forces zs=2c. Degree -3 generators u,v act zero for weight reasons.

For completeness, one can see the first adjacent extension is nonzero without referring to the uniqueness statement: its dual, twisted by O(-1), is the quotient extension 0 -> C -> S/O(-1) -> O -> 0. This follows from the twisted symplectic self-duality S^* = S(1), and the induced rank-two symplectic reduction is C. The latter quotient extension is nonzero by H^0(S)=H^1(S)=0 and the acyclicity of O(-1).

Let A,B,D be a basis of the Levi representation E = Sym^2(k^2), with raising operator e satisfying eB=A, eD=2B and eA=0. It has central degree zero, and n acts trivially on E. The coefficient module for the calculation is

\[
V=E\otimes S(-2).
\]

The negative central degrees occurring in V are -4,-5,-6.

The invariant cohomology of the homogeneous bundle is computed by

\[
H^i(Q,\widetilde V)^{G_2}
=H^i(P,V)
=H^i\big((\Lambda^\bullet n^*\otimes V)^L,d\big).
\]

Indeed derived induction from P to G2 gives sheaf cohomology, taking G2 invariants is exact in characteristic zero, and the Levi factor is linearly reductive. Algebraic cohomology of the unipotent radical agrees with its Chevalley–Eilenberg cohomology.

## 3. The complete invariant complex

Let X,Y,Z,U,W be dual to x,y,z,u,v, respectively. The letter W avoids confusing a dual form with the coefficient module V. Omit wedge symbols in products of forms. The form differential is

\[
dX=dY=0,\qquad dZ=-XY,\qquad dU=-XZ,\qquad dW=-YZ.
\]

The invariant cochains vanish except in degrees 2 and 3, where each space has dimension 2. Explicit bases are:

\[
\begin{aligned}
p &= As\,XU + Bs\,(XW+YU)+Ds\,YW,\\
q &= -Ab\,ZU + Ba\,ZU - Bb\,ZW + Da\,ZW,
\end{aligned}
\]

in degree 2, and

\[
\begin{aligned}
r &= -Ab\,XYU + Ba\,XYU - Bb\,XYW + Da\,XYW,\\
t &= Ac\,XZU + Bc\,(XZW+YZU)+Dc\,YZW,
\end{aligned}
\]

in degree 3. The suppressed O(-2) factor is common to all terms.

The dimension count can be checked without software. Degrees 0 and 1 have insufficient positive central weight in the exterior forms; degrees 4 and 5 have too much. In degree 2 the forms of central degrees 4,5,6 transform under SL2 as (Sym^2 standard direct-sum k), standard, and k, respectively. Tensoring with the corresponding coefficient pieces E tensor s, E tensor (a,b), and E tensor c gives one invariant in each of the first two pieces and none in the last. In degree 3 the form pieces of degrees 4,5,6 transform as k, standard, and (Sym^2 standard direct-sum k), giving zero, one, and one invariant, respectively.

The Chevalley–Eilenberg differential is an immediate calculation:

\[
dp=r-2t,\qquad dq=-r-t.
\]

For example, the module action on As XU contributes -Ab XYU - 2Ac XZU; the two form-differential contributions from Bs XW and Bs YU cancel. The formula for dq follows from xb=c, ya=-c, and dZ=-XY.

Therefore the entire invariant complex is

\[
0\longrightarrow k^2
\xrightarrow{\begin{pmatrix}1&-1\\-2&-1\end{pmatrix}}
k^2\longrightarrow0,
\]

in degrees 2 and 3. Its determinant is -3, hence it is an isomorphism in characteristic zero. Equivalently, cancel the acyclic pair q -> -r: replacing p by p+q leaves d(p+q)=-3t. This explicitly computes the one-dimensional connecting scalar as -3 in these normalizations. If the two adjacent spinor action maps are instead scaled by beta and alpha, respectively, the reduced scalar is -3 alpha beta; both factors are nonzero. This proves the claimed acyclicity. In particular, the connecting map H^2(End(C)(-2)) -> H^3(End(C) tensor G^*(-2)) is nonzero, and hence an isomorphism.

## 4. Reproducible arithmetic check

The accompanying Python/SymPy file `verify_spinor_cohomology.py` constructs the weight-zero Chevalley–Eilenberg differential, checks d^2=0 exactly, takes the kernel of the Levi raising operator, and computes all ranks over Q. Its final output is:

```
Degree, torus-zero dimension, invariant dimension, differential rank
0 0 0 0
1 0 0 0
2 9 2 2
3 9 2 0
4 0 0 0
5 0 0 0
Cohomology dimensions [0, 0, 0, 0, 0, 0]
```

Sources for the Cayley monad, its homogeneous interpretation, and the filtration: G. Ottaviani, *On Cayley Bundles on the Five-Dimensional Quadric*, Bollettino UMI (7) 4-A (1990), 87–100, especially sections 1–2 and Theorem 3.1; https://people.dimai.unifi.it/ottavian/pubblic/cayleybundle.pdf. The monad and weight normalization are also recorded in D. Faenzi, *A geometric construction of Tango bundle on P5*, section 2; https://arxiv.org/abs/math/0111207.
