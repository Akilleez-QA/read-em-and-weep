# An explicit generating set for the complete identity-W coefficient space

## Scope and prerequisites

This constructs every identity-on-W coefficient channel of the prescribed
bidegree: a generating set of87 Rq coefficients spanning a54-dimensional
space, and ten Rh coefficients spanning a10-dimensional space. The Rq
list is deliberately redundant. This is a construction, not an
actual-instance rank calculation. No exterior-presentation independence,
source completion, fourth value, or completeness among all middle
operators is claimed.

Use the notation and public foundation of
`COMPLETE-IDENTITY-W-SPIN-COEFFICIENTS-HAVE-SEVEN-EXPLICIT-SYMBOLS.md`.
In particular f:Sym³W→Sym³U is the actual G-equivariant symplectic cubic
marking up to nonzero scalar, with no source scale assigned a numerical
value. A=Sym²W and V=Sym²U are distinct. The six-space is C⊕U with
C=Sym³U. All matrices below are coefficient matrices; physical factors
in the eventual exterior action must still be retained.

## 1. The marked nonzero invariant of degree twelve

The transported negative Lie algebra f sl(W) f^-1 is the A summand
inside the positive rank-three part L6(Sym⁶U) of End(C). Let

    qe=L6^-1(f E f^-1),
    qf=L6^-1(f F f^-1),
    qh=L6^-1(f H f^-1),
    g12=qh²/20+qe qf/5.                                  (1)

The trace pairing on the cubic representation has tr(H²)=20 and
tr(EF)=10. Therefore (1) is independent of the negative sl2 basis and
is G-invariant. It is not asserted to be invariant under all SL(U).

In the complete C5 eigenframe shape of the preceding theorem, with
FB,FC,FD all free and nonzero, direct coefficient extraction gives

    g12 = ST [FB²FD² T¹⁰ +33 FB FC²FD S⁵T⁵ −9 FC⁴ S¹⁰]
           /(45 FB FC²FD).                               (2)

In particular its S⁶T⁶ coefficient is11/15. This proves nonvanishing
without selecting a source coefficient or actual point. The same
expression has the appropriate covariance under changing eigenframes.

## 2. Five explicit bridges between binary degrees

Write B_d=Sym^d U. The exact representation decompositions are

    B2=V, B4=D5, B6=A+P4,
    B8=P4+D5, B10=A+V+D5,
    dim B12^G=1.

The following maps are nonzero G-equivariant maps, each supported on
the indicated single common irreducible summand:

    B8 → B4,   p ↦ (g12,p)_8,     D5;
    B8 → B6,   p ↦ (g12,p)_7,     P4;
    B10→ B2,   p ↦ (g12,p)_10,    V;
    B10→ B4,   p ↦ (g12,p)_9,     D5;
    B10→ B6,   p ↦ (g12,p)_8,     A.                      (3)

Nonvanishing does not follow merely from nonzero legs. For each line,
the universal transvectant embeds the irreducible SL(U) representation
B12 into Hom(B_d,B_t): it is a nonzero Clebsch map, so its kernel is zero.
Consequently every nonzero g12 yields a nonzero operator. The displayed
G decompositions show that its only possible support is the stated
common summand, with multiplicity one. Thus each is an isomorphism on
that summand, up to its fixed nonzero normalization.

The verifier additionally checks the A and P4 output types by the full
transported negative Casimir, with all marking scales symbolic.

## 3. Negative inputs and all coefficient embeddings

The negative coefficient module is

    N=Sym²A⊗A=2A+V+P4+D5.

The five input covariants are exactly those of the preceding seven-symbol
construction: the two quadratic covariants d(d,n)_2 and n(d,d)_2,
the quartic (d²,n)_1, and the V/P4 components of the sextic d²n, transported
through f. Their positive binary realizations have degrees6,6,4,2,6,
respectively. They give the full two A copies and the single V,P4,D5
copies of N, not only the smaller a(w)D submodule.

For each irreducible output, use every available coefficient block:

- 1: the independent scalar CC and SS blocks;
- A and P4: the corresponding L6 operator in CC;
- V: L2 in CC, L2_spin in SS, and both mixed arrows CS and SC;
- D5: L4 in CC and both mixed arrows CS and SC.

The V mixed arrow sends a linear form z to p2 z. The D5 mixed arrow
sends z to (p4,z)_1/4. The reverse arrow is the determinant adjoint for
J_C=−J3/2 and J_U=−J1/3. These constructions exhaust

    End(C⊕U)=2·1+A+4V+P4+3D5.                            (4)

## 4. Why the formulas span

For Rq, multiply the positive quartic qH by each positive binary input
p_d using every transvectant order0 through min(4,d). This is the full
SL(U) Clebsch decomposition

    B4⊗B_d = direct sum B_(4+d−2j).

For output binary degrees0,2,4, use the direct realization above. For
degree6, split A and P4 using the transported negative Casimir. For
degrees8 and10, use all bridges (3). Then use every coefficient embedding
listed in §3.

For d=2,4,6 this supplies every G-intertwiner into (4): each summand of
the Clebsch decomposition is multiplicity-free as a G-module at the
binary degrees involved, and the listed direct maps/bridges realize
every common irreducible summand. On B6, restriction to its A or P4 input
summand remains onto the corresponding intertwiner space, because a
G-map on either summand extends by zero on its complement. Thus the
separate two A inputs and P4 input introduce no omitted maps.

For Rh there is no qH factor: apply directly all matching embeddings
from §3 to the five negative inputs.

Exact character arithmetic gives

    dim Hom_G(D5⊗N,End(C⊕U))=54,
    dim Hom_G(N,End(C⊕U))=10.                             (5)

The implementation emits87 Rq generators and ten Rh coefficients. The
87 contain repetitions and zero restrictions; no unsupported claim of
linear independence is made. Their span is (5) by the construction
above. In particular this fills all coefficient blocks, unlike an SS-only
or transported-aD-only enlargement.

## Reproduction and use

Run `python verify_complete_identity_w_coefficients.py`.
It builds all97 formulas, checks H/D/base degrees, the complete sextic
inverse, the marked nonzero invariant, the five bridge types, and exact
character decompositions/counts. It uses only universal symbolic
polynomials and representation identities.

`build_complete_identity_w_coefficients(f,H0)` returns the matrices in
balanced Cartan-four plus Spin-two frames. They must enter the complete
identity-W exterior action with its correct adjoint sign. They must not
be treated as independent middle operators or used to inherit U screens
from a smaller repair space. The full coupled source construction and
all c companions remain to be solved.
