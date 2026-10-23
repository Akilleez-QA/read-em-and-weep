# The invariant positive product removes every source126 semisimple separation

## Statement and boundary

Assume an actual occurrence of source126, the remaining source E10 of label G3.11.8ae96830fd21, with the fixed negative-pencil algebra of PR862. Let Q:M2→M4 be multiplication by the canonical invariant positive quadric, and let D_Q be the subalgebra of that fixed negative-pencil commutant satisfying e4 Q=Q e2. Then

    D_Q = C·1 ⊕ J_Q,    J_Q ⊂ J,    J_Q²=0,
    dim J_Q ∈ {0,1,2}.

Here J is the two-dimensional radical of PR862. In particular D_Q is commutative and local, has only the idempotents 0 and1, and has semisimple quotient C. This holds in all three residual constant templates, including every radical shear of every vertex projector.

This does NOT prove J_Q=0, remove source126, select its residual template, realize a source, or prove the full multiplication/lifting objective. Scalar compatibility is allowed. No actual coefficients, points, derivatives, parameters, matrices or selected-instance ranks are evaluated. The bounds below are universal representation-theoretic upper bounds compared with an imported geometric theorem.

## 1. Immutable hypotheses

All files are in Akilleez-QA/read-em-and-weep; exact original bytes and Git blob hashes are retained in inputs/ and INPUTS.json.

- PR856, cee45480686c39a321feaa77d4b669682cc71efe, research/hm/profile11-degree28-constant-separation/PROOF.md: genuine constant separation, source/target characters and simultaneous original-pencil reconstruction.
- PR858, d3b3134e23d0aa4c4b58fd1457f040856d2d0655, research/hm/profile11-degree28-residual-templates/PROOF.md: three exhaustive actual constant templates.
- PR862, e103e25456897a1123f9636eb20080e8641ce66a, research/hm/profile11-degree28-pencil-algebra/PROOF.md: entire covariant fixed-negative-pencil algebra, its two-dimensional square-zero radical, and full faithfulness when Q_bundle(-1) is globally generated.
- eeb1a11799ca38a60c37f6ba96f263ef8e20dd1c, research/hm/order-four-quadratic-load/POSITIVE-INVARIANT-VERTEX-RANK-33-PROVED.md: actual canonical invariant positive product has kernel A+D, image 2V+3P+3D, cokernel P. This is an imported geometric theorem, not a new experiment.
- PR929, ad998827320a2302418730102cd2421943935784, research/hm/profile11-source127-cdf-invariant-branch/PROOF.md, supplies the explicit same-product convention and constituent bottleneck; its c-d-f-specific decomposition is not used.

Write dimensions A=V=3, P=4, D=5. W is the defining binary-icosahedral two-space, Wp the other two-space, S=Sym³W, T=Sym⁵W. All irreducibles are self-dual. The actual total representations are

    M2=A+2V+3P+4D,     M4=2V+4P+3D.

The invariant map Q has image 2V+3P+3D, dimension33. The quadratic representative can be scaled without changing compatibility or its image.

## 2. Reconstruct all diagonal blocks without a quotient-type assumption

PR856 gives E=F⊕R in H=C⊕Hbar, with C=Hbar=A+V+P+D,

    F=(P+2D)O(-2), C O/F=O(28),
    R=X⊕Y, X=O(-8), Y=W O(-9).

For an actual direct constant block (H_i O,E_i), put B_i=H_i O/E_i. PR862 identifies its pencil spaces covariantly as

    N2_i=H0(B_i(-2)), N3_i=H0(B_i(-1)), N4_i=H1(E_i).

The total B(-1) is globally generated. Every direct block B_i(-1) is therefore globally generated, so H1(B_i(-2))=0. Twisting the defining sequence by -2 gives an exact sequence of representations

    0→N2_i→H1(E_i(-2))→H_i→0.

The equality uses H0(H_i O(-2))=0 and H1(O(-2))=C with its trivial G-character. Consequently N2_i is computed by subtraction, without assuming any new equivariant quotient splitting. At twist -1 both cohomology groups of H_i O(-1) vanish, so N3_i=H1(E_i(-1)).

The F block is already pinned by PR856:

    N2_F=A+2V+2P+2D,  N3_F=Wp+2S+3T, N4_F=P+2D,
    dimensions (27,28,14).

The residual complement has N2_R=P+2D, N4_R=2V+3P+D, dimensions (14,26,23).

Type II has no further diagonal constant separation. Types I and III have the additional X and Y vertices, with disjoint constant spans as specified by PR858:

    Type I: H_X=P, H_Y=A+V+D;
    Type III: H_X=P+D, H_Y=A+V.

Serre duality and the fixed McKay rules give

    H1(X(-2))=Sym⁸W=P+D,
    H1(X)=Sym⁶W=V+P,
    H1(Y(-2))=W⊗Sym⁹W=A+V+P+2D,
    H1(Y)=W⊗Sym⁷W=V+2P+D.

Subtracting the constant spans proves the complete endpoint table:

| Template | Block | N2 | N4 | dimensions (N2,N3,N4) |
|---|---|---|---|---|
| I | X | D | V+P | (5,8,7) |
| I | Y | P+D | V+2P+D | (9,18,16) |
| III | X | 0 | V+P | (0,8,7) |
| III | Y | P+2D | V+2P+D | (14,18,16) |

For completeness N3_X=Sym⁷W=Wp+T and N3_Y=W⊗Sym⁸W=Wp+S+2T, in both templates. Together with F each row pair recovers all three total pencil spaces. These calculations use only the actual constant decomposition and natural reconstruction, not a choice of abstract quotient coordinates.

## 3. Every idempotent, including radical shears

In all three PR862 algebras the semisimple diagonal vertices are F,R (Type II) or F,X,Y (Types I and III). Every radical arrow has target F. In Type I both arrows have source Y, in Type II both have source R, and in Type III one has source X and one source Y. Products of radical arrows vanish.

Let e=d+b be an idempotent. Its diagonal coordinates ε_i satisfy ε_i²=ε_i, so each is0 or1. For an arrow with target coordinate a and source coordinate s, idempotence says

    (a+s-1)b_arrow=0.

Thus b_arrow=0 when a=s, whereas an arbitrary arrow is allowed when a≠s. Define c_arrow=b_arrow/(s-a) in the latter case and zero otherwise. Because J²=0,

    (1+c)d(1-c)=d+cd-dc=d+b=e.

This is an exact algebra identity for every radical shear, not a generic classification. It follows that every idempotent is conjugate to a diagonal vertex-subset projector by an actual unit1+c of the fixed-pencil algebra. In particular an all-zero or all-one diagonal gives only0 or1. Every nontrivial idempotent corresponds to a nonempty proper vertex subset.

The reconstruction is covariant and1+c induces invertible G-maps on all pencil spaces. Therefore image and kernel characters of e2,e4 equal those of its diagonal vertex-subset projector. We do NOT assume1+c commutes with Q. It need not: only the image/kernel characters are transported, and the next argument applies directly to e.

## 4. Exhaustive invariant-product bottlenecks

If an equivariant idempotent triple e is Q-compatible, Q carries im e2 into im e4 and ker e2 into ker e4. For each irreducible ρ its image multiplicity is bounded by the sum of the two endpoint minima. This follows from semisimplicity and the dimension bound on each multiplicity-space map. It is invariant under the radical shears just treated.

For a vertex subset S, let x_S,y_S be its N2,N4 characters and x,y the totals. Define

    β(S)=min(x_S,y_S)+min(x-x_S,y-y_S),

where min is constituentwise. β(S)=β(S-complement), so it suffices to check F for Type II and F,X,Y for Types I and III. The exact upper characters and dimensions are:

| Template | isolated vertex | upper image character β | dimension |
|---|---|---|---|
| I,II,III | F | 2P+3D | 23 |
| I | X | V+3P+3D | 30 |
| I | Y | V+3P+3D | 30 |
| III | X | V+3P+3D | 30 |
| III | Y | V+3P+3D | 30 |

For example the F-side bound is P+2D, while its residual side has source P+2D and target2V+3P+D, giving P+D. For Type I's X block, D→V+P has zero equivariant image; its complement contributes V+3P+3D. For either Y block the bound is P+D; its complement contributes V+2P+2D. For Type III's X block the source iszero and the complement contributes V+3P+3D.

Every dimension is strictly below the actual33. Equivalently every upper character lacks at least one of the two actual V constituents. Thus no nontrivial idempotent in the full fixed-negative-pencil algebra can commute with Q. Since the enumeration includes every proper subset and every radical shear, no diagonal-normal-form assumption is left unproved.

## 5. Exact remaining algebra shape

D_Q is a unital finite-dimensional subalgebra: its condition e4Q=Qe2 is linear and preserved by composition. Let π be the projection of the negative-pencil algebra to its diagonal quotient C^k. We prove π(D_Q)=C·1 without assuming that a subalgebra's radical is the ambient radical.

If h∈D_Q has two distinct diagonal values, let Λ be its finite set of distinct diagonal values. The product p(h)=∏_{λ∈Λ}(h-λ) lies in J, so p(h)²=0. Choose a polynomial f with prescribed values0 or1 on Λ, not all equal, and f'(λ)=0 for every λ. Such f exists by the Chinese remainder theorem for the pairwise coprime ideals(t-λ)². Then f²-f is divisible by p², hence f(h) is an idempotent in D_Q with nonconstant diagonal. This contradicts Section4.

Thus every h∈D_Q has constant diagonal λ and h-λ1∈J. Conversely the unit is compatible, so

    D_Q=C·1⊕(D_Q∩J).

Set J_Q=D_Q∩J. Its square iszero, it has dimension at most2, and every λ1+j with λ≠0 has inverse λ⁻¹1-λ⁻²j. Therefore J_Q is exactly the radical and the algebra is local and commutative. Its possible dimensions are1,2,3; no assertion is made that every possibility occurs in the actual geometry.

The same conclusion applies to any unital subalgebra imposing further multiplication compatibilities, since it is contained in D_Q. There is no implication that any nonscalar negative-pencil endomorphism must survive those conditions. In particular this result removes semisimple compatibility alternatives, not any source-dual catalogue pair.

## Verification boundary

verify.py authenticates all five original inputs, derives the needed symmetric-power characters from the nine fixed McKay rules, recomputes endpoint subtraction, exhausts all14 nontrivial vertex-subset projectors across the three types, and checks formal shear identities for each radical arrow. Its negative controls reject an overlarge image bound and retain a nonzero square-zero local algebra, preventing the false scalar conclusion. Run python verify.py and python -O verify.py. These bounded checks support the written proof; they are not proof-assistant verification and do not evaluate actual-instance data.
