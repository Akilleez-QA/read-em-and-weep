# All universal cofactor corank strata and the small crepant resolution

## Scope and theorem

Work over C. Import the abstract operator definition and the divisor/resolution theorem from `../universal-cofactor-normal-form/PROOF.md` and its independent audit. Set dim V=5, dim U=2, E₀=V⊗sl(U), and G=Gr(5,E₀), of dimension 50. For J∈G let β_J:J⊗U→V⊗U be evaluation. Let D_c be the **reduced** closed locus of corank β_J at least c, and S_c=D_c∖D_(c+1) its exact-corank stratum.

Then:

- D_c and S_c are nonempty irreducible for every 1≤c≤6, with dimension 50−c². Every S_c is smooth. Their dimensions are respectively 49, 46, 41, 34, 25, 14.
- At each J∈S_c, the complex-analytic germ of D_1 is the generic c-by-c determinant hypersurface at its zero matrix times a smooth germ of dimension 50−c². More generally all rank loci have the corresponding generic determinantal local models.
- D_7 is empty. Thus every effective five-plane has evaluation rank at least four, and rank four occurs.
- The previously constructed incidence resolution π:Z→D_1 is small. More precisely, the inverse image of S_c has dimension 49−c(c−1); its codimension in Z is c(c−1).
- The resolution is crepant, and ω_Z≅π*ω_(D_1)≅π*O_(D_1)(−13). The divisor D_1 has terminal, hence canonical, singularities and also rational singularities.

For c≥2, D_c denotes reduced support throughout the global incidence arguments. Section 4A additionally proves a complex-analytic local model for the actual ideals of minors. No global smoothness of D_c is asserted; the exact stratum S_c is smooth. The corank-two part of INCIDENCES.md gives the ordinary-node specialization and additional incidence geometry. This is an abstract operator theorem; no geometric-family identification is used.

## 1. The exact constraint rank for an arbitrary cokernel plane

Put W=(V⊗U)*=V*⊗U*. Fix C∈Gr(c,W) and define

    L(C)={ℓ∈V*: ℓ⊗U*⊂C},       k=dim L(C),
    K_C={a∈E₀: λ(a(u))=0 for every λ∈C and u∈U}.

Thus C⊂ker β_J* iff J⊂K_C. In particular 0≤k≤floor(c/2) and k≤5.

Consider the restriction map

    r_C:E₀→Hom(U,C*)=C*⊗U*.

Its dual is the inclusion C⊗U⊂W⊗U followed by restriction to E₀*. The ambient operator space is M=Hom(U,V⊗U)=V⊗End(U). Under its natural dual pairing, the annihilator of E₀=V⊗sl(U) is the five-dimensional scalar space V*⊗id_U. For ℓ∈V*, the scalar tensor ℓ⊗id_U lies in C⊗U exactly when ℓ⊗e₁* and ℓ⊗e₂* both belong to C, as seen by taking its coefficients in any basis of the final U factor. This is exactly ℓ∈L(C). Hence

    ker(r_C*)=(C⊗U)∩(V*⊗id_U)≅L(C),
    rank(r_C)=2c−k,
    dim K_C=15−2c+k.                                      (1)

The scalar identity is a tensor in U*⊗U, so this argument uses only the natural trace pairing and does not make a choice-dependent identification of U with U*.

## 2. Parameter spaces with fixed scalar intersection

Let B_(c,k)⊂Gr(c,W) be the locally closed locus dim L(C)=k. When nonempty it is smooth irreducible of dimension

    k(5−k)+(c−2k)(10−c).                                 (2)

To prove this, first choose L∈Gr(k,V*). Planes C containing L⊗U* correspond to (c−2k)-planes C' in (V*/L)⊗U*, a space of dimension 10−2k. These form a relative Grassmannian over Gr(k,V*) of dimension (2). Impose the open condition that C' contains no nonzero full subspace ℓ'⊗U*. Its openness follows, for example, by projecting the closed incidence of such ℓ' from the projective bundle P(V*/L). This condition is equivalent to L(C)=L: if a complete factor occurs modulo L, lifting it and subtracting elements of L⊗U* gives the corresponding complete factor in C. The open subset is precisely B_(c,k), with the unique L=L(C).

For completeness the identification is algebraic, not just set-theoretic. L(C) is the kernel of the bundle map V*→Hom(U*,W/C), ℓ↦(φ↦ℓ⊗φ mod C). On a constant-k stratum this kernel is a subbundle, giving the regular inverse C↦(L(C),C'). A nonempty open subset of the irreducible relative Grassmannian is irreducible and has its full dimension, proving (2).

On B_(c,k), equation (1) has constant rank, so K_C forms a vector bundle of rank m=15−2c+k. The incidence

    I_(c,k)={(C,J): C∈B_(c,k), J∈Gr(5,K_C)}

is empty if m<5. Otherwise, when its base is nonempty, it is a smooth irreducible relative Grassmannian. Its dimension is

    k(5−k)+(c−2k)(10−c)+5(10−2c+k)
      =50−c²+k(2c−10−k).                                 (3)

## 3. Feasible coranks, dimension bounds, and witnesses

If J has corank at least c, choose any c-plane C in its dual kernel. Since dim K_C≥5, equation (1) requires

    2c−k≤10,       k≤floor(c/2).

For c≥7 these inequalities are incompatible: 2c−floor(c/2)>10. Consequently D_7 is empty.

For 1≤c≤5, the final term k(2c−10−k) in (3) is nonpositive and is zero precisely at k=0. For c=6 the first feasibility inequality gives k≥2, while k≤3; the correction term is k(2−k), zero for k=2 and −3 for k=3. Therefore

    dim D_c≤50−c²,       1≤c≤6.                          (4)

Indeed every J in D_c occurs in one of the finitely many incidences I_(c,k), and projection cannot increase dimension.

The following abstract operators certify nonempty exact-corank loci on the unique maximizing incidence stratum. Fix bases v₁,…,v₅ of V and e₁,e₂ of U, with

    H=diag(1,−1), E(e₂)=e₁, E(e₁)=0,
    F(e₁)=e₂, F(e₂)=0.

For 1≤c≤5 let J be spanned by v_i⊗E for i≤c and v_i⊗H for i>c. The five generators are independent; the image of evaluation has dimension c+2(5−c)=10−c. Its annihilator is spanned by v_i*⊗e₂*, i≤c, and contains no full ℓ⊗U*. Thus its exact corank is c and k=0.

For c=6 use the five-dimensional subspace

    J=(v₁⊗span(F)) ⊕ (v₂⊗span(E)) ⊕ (v₃⊗sl(U)).

Its evaluation image is

    span(v₁⊗e₂) ⊕ span(v₂⊗e₁) ⊕ (v₃⊗U),

of dimension four. Its dual kernel is

    C=span(v₁*⊗e₁*, v₂*⊗e₂*)
       ⊕ (span(v₄*,v₅*)⊗U*).

Exactly the last summand consists of full factors, so L(C)=span(v₄*,v₅*) and k=2.

In each maximizing incidence, the exact-corank-c condition is open and nonempty by these witnesses. There C is necessarily the whole dual kernel, hence unique. Moreover it varies regularly in J on S_c by the constant-rank kernel construction. Projection from that open incidence is therefore an isomorphism onto its image. Formula (3) proves that this image has dimension 50−c². Combined with (4), this gives the asserted exact dimensions.

## 4. Irreducibility of every reduced rank-drop locus

We include the component lower-bound argument to rule out smaller extra components. On any smooth affine trivialization X⊂G of the rank-ten bundles, β is a regular matrix map B:X→Mat₁₀. Let Y_c⊂Mat₁₀ be the usual rank-at-most-(10−c) variety. It is irreducible of codimension c², hence dimension 100−c². The rank-locus support is the intersection

    Γ_B ∩ (X×Y_c) ⊂ X×Mat₁₀.

The ambient variety is smooth of dimension 150, while Γ_B has dimension 50 and X×Y_c has dimension 150−c². Every irreducible component of their intersection has dimension at least 50−c². One standard justification of this intersection inequality uses the diagonal: in the product of the smooth ambient variety with itself its diagonal is a regular embedding of codimension 150, locally cut out by 150 equations. Restrict these equations to the product Γ_B×(X×Y_c), which is irreducible of dimension 200−c². The principal ideal theorem applied successively gives the stated lower bound on every component. This local argument applies to every component of D_c.

On the other hand, D_c is covered by projections of the finitely many I_(c,k), so it is covered by the finite union of their image closures. Each such closure is irreducible when nonempty. For c≤5, all k>0 have dimension strictly less than 50−c². For c=6, only k=2 can have this dimension, with k=3 strictly smaller. These smaller closures cannot supply any irreducible component of D_c by the lower bound just proved. The unique maximizing incidence has an image closure of dimension 50−c² by Section 3. Therefore this single irreducible closure equals D_c. Its nonempty open subset S_c is likewise irreducible.

This argument uses only supports, so it makes no unwarranted assertion that the ideal of minors remains reduced under this special linear-family pullback.

## 4A. Transversality at every corank and local determinantal models

This argument generalizes the corank-two proof in INCIDENCES.md. Fix J∈S_c and write T=V⊗U, R=ker β_J, Q=coker β_J, with quotient p:T→Q. Both R and Q have dimension c. The intrinsic normal derivative of the matrix family is

    ν:Hom(J,E₀/J)→Hom(R,Q),
    ν(h)(Σ a_j⊗u_j)=p(Σ δa_j(u_j)),

where a₁,…,a₅ is a basis of J and δa_j lifts h(a_j) to E₀. It is well defined because changing a lift by an element of J changes evaluation by an element of im β_J.

We prove ν is surjective by showing its dual has zero kernel. Under the trace pairing a dual functional is q:Q→R. Include R⊂J⊗U and write the components of q as q_j:Q→U. The trace pairing with ν(h) is

    Σ_j tr_U(q_j p δa_j).

The δa_j can vary independently over E₀. Thus if q annihilates all ν(h), each q_j p:T→U lies in the annihilator of E₀⊂Hom(U,T). By the same scalar trace-annihilator calculation as Section 1,

    q_j p = ℓ_j⊗id_U   for some ℓ_j∈V*.

Since q lands in R, β_J q=0. Precomposing this identity with p gives the identity of endomorphisms of T

    0 = Σ_j a_j(q_j p) = Σ_j a_j∘(ℓ_j⊗id_U).

Under Hom(T,T)=V*⊗Hom(U,T), the final sum is Σ_j ℓ_j⊗a_j. The a_j are linearly independent in Hom(U,T), since E₀ is an actual operator subspace and J is a five-plane. Applying coefficient functionals on their span forces each ℓ_j=0. Since p is onto, q_j p=0 implies q_j=0, so q=0. Therefore ν is onto for every corank c.

To extract the local geometry, trivialize the bundles near J and choose domain and target bases making β_J an invertible (10−c)-block and a zero c-block. On a neighborhood where that first block A remains invertible, write the matrix as

    [ A  B ]
    [ C  D ].

Invertible row and column operations reduce it to diag(A,F), with Schur complement F=D−CA⁻¹B. Here F(J)=0 and dF_J is exactly ν in the chosen kernel and cokernel bases. Since ν is onto, the holomorphic submersion theorem supplies local analytic coordinates consisting of the c² entries of F and 50−c² additional coordinates.

The determinant is det(A)det(F), with det(A) a unit. Hence the germ of D_1 at J is

    ({det X=0}⊂Mat_c,0) × (C^(50−c²),0).

Likewise, for 1≤d≤c, the ideal of (11−d)-minors of β becomes the ideal of (c−d+1)-minors of F, so the actual local determinantal scheme for corank at least d has the generic rank-at-most-(c−d) matrix model times the same smooth factor. This minor-ideal identity follows from the invertibility of A and the displayed block diagonal reduction; its invertible diagonal block can be reduced to an identity block. In particular D_c near an exact-corank-c point is F=0, proving that S_c is smooth of dimension 50−c². No claim of a Zariski-local product is needed: the product assertion is complex analytic (and also yields the corresponding completed-local-ring description).

## 5. Smallness of the incidence resolution

The imported construction is

    Z={(J,[λ]): J⊂ker(λ∘−)} → D_1,

a smooth irreducible 49-fold, isomorphic over S₁, with fiber P^(c−1) over S_c. On S_c the dual kernels form a rank-c vector bundle, so this inverse image is a projective bundle. Consequently

    dim π⁻¹(S_c)=50−c²+(c−1)=49−c(c−1).

For c≥2 its codimension in Z is at least two, with equality for c=2. The exceptional set is their finite union and has no divisorial component: π is a small resolution. It also satisfies the strict dimension-theoretic small-map inequality

    codim_(D_1)(S_c)=c²−1 > 2(c−1),       c≥2.

Equivalently, for every r≥1 the locus with fiber dimension at least r is D_(r+1), of codimension (r+1)²−1>2r when nonempty.

## 6. Crepancy, with an independent canonical-bundle check

The imported D_1 is normal and is a Cartier divisor in smooth G, so its dualizing sheaf is invertible. Since G=Gr(5,15) has canonical line O_G(−15) and D_1 has class O_G(2), adjunction gives

    ω_(D_1)=O_(D_1)(−13).

Over S₁, π is an isomorphism, so ω_Z and π*ω_(D_1) agree there via the natural canonical identification. Their complement in smooth Z has codimension at least two by Section 5. The resulting rational isomorphism of line bundles has no possible zero or pole divisor and therefore extends to an isomorphism everywhere. This proves crepancy in the canonical-divisor sense, not merely an abstract coincidence of line-bundle classes.

A direct bundle computation confirms it. Write q:Z=Gr_(P⁹)(5,K)→P⁹, where

    0→K→E₀⊗O→U*⊗O(1)→0.

Thus rank K=13 and det K=O(−2), up to constant lines. For its tautological rank-five subbundle S, the relative tangent bundle is S*⊗(q*K/S). Taking its determinant gives

    ω_(Z/P⁹)=(det S)^13⊗q*(det K)^(-5).

Because ω_(P⁹)=O(−10), the two base factors cancel:

    ω_Z=(det S)^13=π*O_G(−13)|Z.

### Terminal and rational singularities

For the precise discrepancy criterion, see János Kollár, [author-hosted Chapter 2, Corollary 16 and its proof, printed page 10](https://web.math.princeton.edu/~kollar/book/chap2.pdf#page=10), with discrepancy invariance under crepant pullback in Lemma 12. On a smooth resolution, positivity of every exceptional-divisor discrepancy characterizes terminal singularities. Here π has no exceptional divisors. More explicitly, any divisorial valuation exceptional over D_1 must also be exceptional over Z, because no divisor on Z is contracted by π. Its discrepancy over D_1 equals its discrepancy over smooth Z by crepancy, and the latter is positive. Thus D_1 is terminal, in particular canonical. This does not imply or assert Q-factoriality.

Rational singularities follow directly from crepancy and Grauert–Riemenschneider vanishing, without an additional classification theorem. The needed vanishing is stated in [Mihnea Popa, author-hosted Hodge-theory notes, Exercise 1.2.5(ii), printed page 7](https://people.math.harvard.edu/~mpopa/265/Math265-notes.pdf#page=11): for a projective birational morphism from a smooth complex variety, Rⁱπ*ω_Z=0 for i>0. Our π is projective, Z is smooth, and ω_Z=π*ω_(D_1). The projection formula and invertibility of ω_(D_1) give

    Rⁱπ*O_Z ⊗ ω_(D_1) = Rⁱπ*ω_Z = 0,       i>0.

Also π_*O_Z=O_(D_1) because π is proper birational and D_1 is normal. This is precisely the rational-singularity condition. Rationality of the variety, proved in the earlier packet, is a different statement.

## 7. Boundary of application

These are statements about abstract five-planes in V⊗sl(U). They do not identify a geometric module with that operator space or determine the span or evaluation rank of a conductor family. All witnesses are abstract operators.
