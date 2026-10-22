# An explicit generating set for the complete traceless-W coefficient space

## Scope and result

The prescribed traceless-W coefficient target is

    T = End(C ⊕ U) ⊗ A,     C = Sym³U,     A = Sym²W.

Here W is the negative spinor, U the positive spinor, and A and V=Sym²U
are inequivalent G-representations. The actual cubic marking
f:Sym³W→C is G-equivariant and symplectic up to a nonzero scalar. It is
not an arbitrary identification of the two adjoint representations.
The negative coefficient source and positive H representation are

    N = Sym²A ⊗ A = 2A + V + P4 + D5,     H ∈ D5.

This note constructs an explicit finite spanning set for both

    Hom_G(D5 ⊗ N, T),       Hom_G(N, T),

of dimensions162 and33 respectively. The actual lists are deliberately
redundant:607 Rq and71 Rh coefficients after representation-theoretic
zero-type pruning. Neither their independence nor the dimension of their
exterior presentations is asserted. Together with the complete identity-W
coefficient spaces54+10, they span the supported coefficient space of
size259. This is not completeness among unrestricted middle cochains,
not a source solution, and not a value of any obstruction.

Only the existing universal/public source helpers are imported. No actual
source coefficient, actual point, instance matrix rank, or coefficient
solve enters the construction. In the universal C5 eigenframe, FB,FC,FD
remain arbitrary nonzero symbols throughout.

Pinned immutable public prerequisites:

- [The marked input, balanced frame and seven spin symbols, PR727](https://github.com/Akilleez-QA/read-em-and-weep/blob/77b6603c057e2b782387a24185ee7eae40cd8df6/research/hm/order-four-quadratic-load/COMPLETE-IDENTITY-W-SPIN-COEFFICIENTS-HAVE-SEVEN-EXPLICIT-SYMBOLS.md), commit `77b6603c057e2b782387a24185ee7eae40cd8df6`.
- [The complete identity-W coefficient construction and invariant bridges, PR730](https://github.com/Akilleez-QA/read-em-and-weep/blob/a79c896439bc141dcb07a8891ba391ee8b38fcc9/research/hm/order-four-quadratic-load/COMPLETE-IDENTITY-W-COEFFICIENTS-HAVE-AN-EXPLICIT-MARKED-GENERATING-SET.md), commit `a79c896439bc141dcb07a8891ba391ee8b38fcc9`.

## 1. Existing canonical typed inputs

Use `universal_complete_identity_w_coefficients.py`, whose input construction
and completeness proof are in
`COMPLETE-IDENTITY-W-COEFFICIENTS-HAVE-AN-EXPLICIT-MARKED-GENERATING-SET.md`.
Put B_d=Sym^d U. The canonical irreducible realizations are

    1 ⊂ B0,   V = B2,   D5 = B4,   A ⊕ P4 = B6.

The five negative input covariants are the two A covariants, the V and P4
parts of the transported negative sextic, and the transported negative
quartic. They realize2A+V+P4+D5. For Rq, combine each with the positive
quartic qH by all Clebsch transvectants and then use the existing typed
output bridges. This gives38 canonical typed source maps, with redundant
multiplicities

    1 + 8A + 8V + 9P4 + 12D5.

Their span has actual source multiplicities

    D5 ⊗ N = 1 + 5A + 5V + 6P4 + 7D5.

For Rh use the five negative inputs directly. Every canonical source
polynomial has degree2 in (h,k,l) and degree2 in (u,w); Rq is linear in H
and Rh is independent of H. The new helper uses exactly these existing
source formulas, not a smaller transported-aD source module.

## 2. All canonical upward bridges through degree twelve

Let g12 be the nonzero marked invariant constructed from f:

    qe = L6^-1(f E f^-1),  qf = L6^-1(f F f^-1),
    qh = L6^-1(f H f^-1),
    g12 = qh²/20 + qe qf/5.

The complete all-scale eigenframe computation has g12's S⁶T⁶ coefficient
11/15, so nonvanishing is uniform, with no numerical scale assignment.
The relevant G-decompositions are

    B0 = 1,                B2 = V,
    B4 = D5,               B6 = A + P4,
    B8 = P4 + D5,          B10 = A + V + D5,
    B12 = 1 + V + P4 + D5.

In particular B12 has no A summand. Each listed binary representation is
G-multiplicity-free. Use the identity in the same degree, with the typed
A or P4 projector on B6. The additional bridges are

    1(B0) → B12:          p ↦ g12 p;
    V(B2) → B10,B12:      p ↦ (g12,p)_2, (g12,p)_1;
    D5(B4)→ B8,B10,B12:   p ↦ (g12,p)_4, (g12,p)_3, (g12,p)_2;
    A(B6) → B10:          p ↦ (g12,p)_4;
    P4(B6)→ B8,B12:       p ↦ (g12,p)_5, (g12,p)_3.

These are all possible canonical common-component bridges. In particular,
the A restrictions of B6→B8 and B6→B12 vanish, as does the P4 restriction
of B6→B10; they are not counted as generators.

For each nonidentity transvectant above, the universal Clebsch map
B12→Hom(B_d,B_j) is a nonzero SL(U)-map out of an irreducible
representation, hence injective. Thus nonzero g12 gives a nonzero
operator. The displayed decompositions show that its only possible
G-support is the stated common irreducible component, with multiplicity
one. It is therefore an isomorphism on that component up to nonzero
normalization. Multiplication from B0 is immediate. The verifier also
checks every bridge as a full symbolic polynomial and checks that all
sextic bridges kill the complementary type.

## 3. Explicit two-variable Clebsch inclusions

To couple a first binary coefficient of degree k to the W-factor, where
k∈{0,2,4,6}, use

    B_k ⊗ B6 = direct sum over 0≤r≤min(k,6) of B_(k+6−2r).

Set a=k−r, b=6−r, j=a+b and Δ=XQ−YZ. For p∈B_j define

    i_(k,r)(p) = Δ^r / binomial(j,a)
                 × [t^a u^b] p(tX+uZ,tY+uQ).

The first pair (X,Y) has total degree k and the second (Z,Q) degree6.
The two pairs are independent; no diagonal substitution replaces this
inclusion. It has the exact normalization

    i_(k,r)(S^j) = X^(k−r) Z^(6−r) Δ^r.

Consequently it is nonzero, and its simultaneous SL2-equivariance is
immediate from polarization and determinant invariance. The verifier
checks this on the complete arbitrary polynomial p with all coefficients
free, for E,F,H, for all16 inclusions, and checks both homogeneous degrees.

For reproducibility the helper implements the explicit monomial formula.
For p=S^(j−i)T^i, sum over all valid t and0≤z≤r the coefficient

    binomial(j−i,a−t) binomial(i,t) / binomial(j,a)
        × (−1)^z binomial(r,z)

times the tensor monomial whose first T exponent is t+z and whose second
T exponent is i−t+r−z. These rational coefficients never use source data.

## 4. Project and embed both coefficient factors

Let Cminus be the Casimir for the transported negative Lie algebra
f sl(W) f^-1 acting by commutators on End(C). On the positive sextic
L6(B6), its two eigenvalues are2 on A and12 on P4. Therefore

    P_A(p) = L6^-1((12 L6(p) − Cminus(L6(p)))/10),
    P_P4(p) = p − P_A(p).

The negative W coefficient map is

    B6 --P_A--> A --L6--> f sl(W) f^-1
       --conjugation by f^-1--> sl(Sym³W) --cubic inverse--> sl(W).

If R is the resulting negative rank-one cubic operator, its final2×2
matrix is

    [[R00/3, R01], [R10/3, −R00/3]].

The verifier checks this formula on the complete generic sextic, including
reconstruction of its cubic action, annihilation of P4, and recovery of
each of E1,F1,H1. It does not use the inequivalent positive V as a
negative W action.

On the first leg use all existing six-space coefficient embeddings:

- k=0: independent C and U scalar blocks;
- k=2: C_V, S_V and both V mixed arrows;
- k=4: C_D5 and both D5 mixed arrows;
- k=6: first project to A or P4, then put L6 in the matching C block.

The mixed reverse arrows use the determinant adjoint for
J_C=−J3/2, J_U=−J1/3, exactly as in the identity-W helper. Thus all first
embeddings are in the same balanced Cartan4+Spin2 coordinates.

The emitted12×12 matrices are W-major: the first6 coordinates are
W-index0 tensored with C⊕U, and the last6 coordinates W-index1 tensored
with C⊕U. For an elementary tensor the matrix is L_W⊗M_6. Equivalently,
its four6×6 blocks have indices (W output,W input). The two diagonal
blocks sum to zero.

For J_b=diag(−J3/2,−J1/3) and J12=J1⊗J_b, the ordinary tensor adjoint is

    Adj_J12(L_W ⊗ M) = − L_W ⊗ Adj_Jb(M),

because every traceless W matrix satisfies Adj_J1(L_W)=−L_W. The test
checks this with every one of the36 entries of M free and all three
entries of L_W free. This fixes coefficient order and sign; the physical
exterior action, its own signs and scales still must be retained by the
later source assembler. This test does not assert an exterior solve.

## 5. Spanning proof and safe pruning

Fix a canonical irreducible τ and a desired first coefficient block of
type σ⊂B_k. Any G-map τ→σ⊗A extends into B_k⊗B6 using the inclusions of
σ and A. Decompose that extension through every CG summand B_j. Since
B_j is G-multiplicity-free, each resulting map τ→B_j is a scalar multiple
of the corresponding bridge in §2, or is zero if τ does not occur there.
Applying the first σ projector and the second A projector recovers the
original map. Hence the projected CG routes span every
Hom_G(τ,σ⊗A), whether some individual restrictions vanish or repeat.
This is a split-projection/semisimplicity argument, not the false assertion
that a composite of nonzero maps must be nonzero.

Perform this for every available first coefficient embedding and every
canonical source map in §1. Semisimplicity and Schur's lemma show that
composing spanning source maps with spanning output maps spans the full
Hom-space, including all input multiplicities. This proves completeness.

Only the following character-forced zero-type routes are pruned:

    A⊗1 = A,
    A⊗V = P4+D5,
    A⊗D5 = A+V+P4+D5,
    A⊗A = 1+A+D5,
    A⊗P4 = V+P4+D5.

The retained output route counts by source type are

    1:2, A:10, V:9, P4:17, D5:25.

Thus the list lengths are

    Rq: 1·2 + 8·10 + 8·9 + 9·17 + 12·25 = 607,
    Rh: 2·10 + 1·9 + 1·17 + 1·25 = 71.

No further minimality or independence claim is needed.

## 6. Exact coefficient dimensions and implementation

The old first target has character

    End(C⊕U) = 2·1 + A + 4V + P4 + 3D5.

Tensoring with the negative A gives

    T = 1 + 6A + 4V + 8P4 + 9D5.

Exact A5 character inner products then give

    dim Hom_G(N,T) = 2·6+4+8+9 = 33,
    dim Hom_G(D5⊗N,T) = 1+5·6+5·4+6·8+7·9 = 162.

Together with the identity-W counts54+10 this gives259 supported
coefficient channels. This count precedes exterior presentation and may
not be transferred to independent middle operators.

Artifacts:

- `universal_complete_traceless_w_coefficients.py`: complete formula
  generator; `TracelessWBuilder.iter_coefficients(f,H0)` lazily emits
  `(category,label,12x12 matrix)`. It caches output templates on canonical
  monomial bases. `build_complete_traceless_w_coefficients` forces lists.
- `verify_complete_traceless_w_coefficients.py`: all16 generic two-variable
  CG inclusions, all14 typed bridges, full projector/marking/adjoint checks,
  exact character arithmetic, all43 typed source degree/type checks, and
  seven nonzero completely assembled universal coefficient formulas, including
  Rq and both mixed-arrow directions.
- `verify_complete_traceless_w_coefficients.log`: default verification log.

Run `python verify_complete_traceless_w_coefficients.py`. The optional
`--build-all` additionally expands and audits all678 output formulas; that
larger expansion is not necessary for the spanning theorem, and is not
claimed to have run by the default test. The explicit maps and structural
checks ensure all resulting coefficients have the required degrees: the
output templates are linear and depend only on f, not on H,D or the base.
All source balance and c-companion equations remain separate next tasks.
