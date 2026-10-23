# Balanced syzygies and sharp quadratic saturation of the icosahedral sextic net

## Scope and inputs

Work over C with G=SL2(F5), its defining two-dimensional representation W, and the nonstandard three-dimensional representation V. Fix the standard determinant identification W*=W. The multiplicity-one summand V in Sym6 W is an actual space of binary sextics, not an arbitrarily selected three-space. All maps below are its universal polynomial evaluation and multiplication maps, not maps obtained by evaluating the HM source. No actual source coefficients, parameters, points, jets or instance matrices are computed.

The complete proof of PR1145 at 2e2da6c1226b7671c79e55b3c9f8bb14a0f8719b is retained as context. Its Section 7 proves basepoint-freeness and quartic saturation for this net using a general independent sextic-net argument. The present result strengthens that universal net statement: the special equivariant net already saturates in multiplier degree two. It makes no further actual-profile exclusion and does not replace the actual endpoint/apolar application of PR1145.

Use the public character conventions A=Sym2 W, S=Sym3 W, D=Sym4 W, T=Sym5 W, and the other irreducibles P of dimension four and W' of dimension two. The needed identities, verified exactly by the retained character source, are

    Sym6 W=V+P,
    V tensor Sym2 W=P+D=Sym8 W,
    V tensor Sym3 W=S+T+W',   Sym9 W=S+T.

The group is perfect, so it has no nontrivial one-dimensional representations. The central element -1 acts trivially on V and by (-1)^d on the standard linearization of O(d).

## 1. Evaluation kernel

The sextics in V have no common zero. Indeed their common-zero divisor would be G-invariant, with degree at most six. On the projective parameter line the action is A5. Its point stabilizers are cyclic and have order at most five, so every orbit has at least twelve points. A nonempty invariant divisor of degree at most six is impossible. Thus there is an exact equivariant vector-bundle sequence

    0 -> T_V -> V tensor O -> O(6) -> 0.             (1)

The coefficient inclusion V->H0(O(6)) is injective, so H0(T_V)=0. The kernel has rank two and degree -6. Write its ordinary Birkhoff type as O(-a)+O(-b), with 1<=a<=b and a+b=6. The only possibilities are (1,5), (2,4), and (3,3).

If a<b, the highest-degree line O(-a) is canonical: it is the unique maximal-slope line subbundle. Consequently it is G-invariant. Its equivariant linearization differs from the standard one only by a character, which must be trivial. But T_V is a subbundle of V tensor O, on which the center acts trivially. Thus (-1)^a=1, excluding a=1.

For (a,b)=(2,4), H0(T_V(2)) is a one-dimensional trivial representation, because its unique top line is O(-2) with the standard linearization. Taking sections in the injection T_V(2)->V tensor O(2) would put the trivial representation into

    V tensor Sym2 W=P+D,

which contains none. Hence this case is impossible as well. Therefore

    T_V is ordinarily O(-3)+O(-3).                 (2)

No equivariant splitting of the unbalanced extension was presumed: only its canonical top line was used.

## 2. Exact equivariant kernel

The balanced bundle T_V(3) is trivial of rank two, and evaluation identifies it equivariantly with H0(T_V(3)) tensor O. Let U=H0(T_V(3)). Since H1(T_V(3))=0, twisting (1) by three yields an exact representation sequence

    0 -> U -> V tensor Sym3 W -> Sym9 W -> 0.

The displayed character identities give U=W'. Consequently the exact equivariant evaluation sequence is

    0 -> W' tensor O(-3) -> V tensor O -> O(6) -> 0. (3)

This identifies the doublet without choosing a basis or an actual source coefficient. The inclusion of the syzygy bundle in V tensor O is not being asserted to split.

## 3. Sharp multiplication threshold and all kernels/cokernels

For d>=0, let mu_d:V tensor Sym^d W -> Sym^(d+6) W be ordinary polynomial multiplication. Twisting (3) by d and taking cohomology gives

    0 -> W' tensor H0(O(d-3)) -> V tensor Sym^d W
      -> Sym^(d+6) W -> W' tensor H1(O(d-3)) -> 0,  (4)

because H1(V tensor O(d))=0. Thus:

- d=0: mu_0 is the inclusion V into V+P, with cokernel P.
- d=1: mu_1 is injective, with cokernel W'.
- d=2: mu_2 is an isomorphism V tensor Sym2 W -> Sym8 W.
- d>=3: mu_d is onto, with kernel W' tensor Sym^(d-3) W.

For d=0 the cohomological cokernel is W' tensor W, agreeing with P. The identification follows from W tensor W'=P and Serre duality; all representations here are self-dual. The dimension formula is

    rank(mu_d)=min(3(d+1),d+7),
    dim ker(mu_d)=max(2d-4,0),
    dim coker(mu_d)=max(4-2d,0).

In particular multiplier degree two is the minimal degree of surjectivity. Pure dth powers span Sym^d W in characteristic zero, so the constant span of l^d V over all parameter lines l is all Sym^(d+6) W for every d>=2. The quartic span needed in PR1145 follows as a special case, but the sharper threshold is the new conclusion.

## 4. Minimal graded resolution and finite quotient

Put R=Sym(W), with R_n=Sym^n W and R_n=0 for n<0, and let I=(V) be the homogeneous ideal generated by this sextic net. Formula (4) identifies the whole polynomial syzygy module with W' tensor R(-9): in degree n its elements are H0(T_V(n-6))=W' tensor R_(n-9). These identifications commute with multiplication, since they arise from the bundle isomorphism (3). Thus the graded equivariant sequence is exact:

    0 -> W' tensor R(-9) -> V tensor R(-6) -> I -> 0,

and adjoining R gives the minimal graded free resolution

    0 -> W' tensor R(-9) -> V tensor R(-6)
      -> R -> R/I -> 0.                            (5)

It is minimal because the first matrix has homogeneous degree three and the generators have degree six, both strictly positive. This statement is not based on an assumed matrix rank or a numerical Hilbert-series fit.

The quotient has Hilbert series

    (1-3t^6+2t^9)/(1-t)^2
      =1+2t+3t^2+4t^3+5t^4+6t^5+4t^6+2t^7.

Its length is 27. Equivariantly its graded pieces are Sym^n W for 0<=n<=5, then P in degree six and W' in degree seven, and zero in all degrees n>=8. In particular I contains every form of degree at least eight. This is an exact universal finite quotient, not an actual obstruction-space computation in the original proof repair.

## Evidence and boundaries

The bundle argument proves the balancing and exactness. The reproducible checker authenticates the complete pinned sources and independently checks the finite splitting possibilities, central parity, character identities, dimension/rank formulas, graded Hilbert numerator and universal multiplication kernel/cokernel characters over a bounded range. Normal and optimized Python give the same result. These checks support the proof but are not proof-assistant verification.

This packet proves a stronger universal statement about the unique equivariant sextic net. It does not claim historical novelty of the underlying vector-bundle method, does not identify new actual HM data, and does not prove full profile11 closure, global rank-three exclusion, full-adjoint invertibility, algebraicity or the original theorem.
