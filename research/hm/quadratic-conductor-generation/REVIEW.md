# Independent review of quadratic normalization-defect generation

## Verdict and scope

PASS. The proof establishes the claimed actual primary-S15 quadratic rank, nonvanishing at every node, and generation of the entire conductor-image graded module in degree two. The key lifting step is genuine cohomology and naturality, not the false assertion that global sections preserve an arbitrary sheaf surjection. No saturation or unproved ideal-sheaf H1 vanishing is needed for the all-degree statement.

This is an independent mathematical review, not formal proof-assistant certification. No actual HM/source coefficient, point, matrix or rank was evaluated; no numerical search or large computation was performed. Public sources and pinned repository files were read, with no public writes. The separate universal support-interpolation theorem is not reviewed here; consequences using it remain conditional in this review.

## 1. Exact sources inspected

The following files were fetched afresh through the repository connector at the exact named commits, not inferred from local copies or PR titles:

- PR570: e5e55594ef2b99cefb81c4c02b22cb45e1ff0025, research/hm/primary-surface-dictionary/PROOF.md, returned blob 61ec66e04320c9825247678abe2a2b8aceed0f7c.
- PR574: 3c92fdc469f6870520e7a9d905b5ab9199a5bf37, research/hm/primary-conductor/PROOF.md, returned blob 7d1c7f2695daafb35054f8ea9ff4465e4e029f4b.
- PR578: d3f1135f7c3c1104ec431fcc44fdb5e2d80bb078, research/hm/primary-postulation/PROOF.md, returned blob ebd673b5912a1630224aa8e7ca14c0c0ad1e8ad6.

Repository: https://github.com/Akilleez-QA/read-em-and-weep . These are credited premises; their entire upstream proof chain is not re-proved by this review. PR570 identifies the coordinate-copy primary surface rather than confusing the distinct initial ambient representations. PR574 specifies the genuine normalization quotient with one-dimensional fibers on the reduced thirty-point support. PR578 supplies the equivariant divisibility and strict-growth framework.

BHM was opened directly at https://mathweb.tifr.res.in/Documents/Publications/Studies/Vector-Bundles-On-Algebraic-Varieties.pdf . Section 3.4, printed pp.51–52 (zero-based PDF pages 58–59), defines S25 by the wedge-square equations and proves the equation-defined surface smooth. Section 4.5, printed pp.63–64 (PDF pages 70–71), identifies the projected image with S15 and gives the two-branch transverse-node description. These statements justify the specific Pfaffian scheme and finite normalization used here, not a surrogate with matching numerical invariants.

## 2. Pfaffian resolution and sheaf quotient

Put L=O_Y(1,1). The matrix entries lie in L, its submaximal Pfaffians in L², the middle differential has degree L, and the last differential again degree L². Thus the displayed complex has the correct twists:

0 → L^(-5) → L^(-3)^5 → L^(-2)^5 → J → 0.

Since the Pfaffian subscheme is smooth of codimension three in the smooth fivefold Y, its ideal has grade three locally. The grade-three Pfaffian exactness theorem therefore applies. There is no extra unproved genericity or saturation requirement: this is the locally exact sheaf resolution of the stated equation-defined X.

For K=coker(A→B), the resolution gives actual short exact sequences 0→A→B→K→0 and 0→K→C→J→0. Relative cohomological dimension one of p yields R¹p_*C→R¹p_*J→0. Pushing forward 0→J→O_Y→O_X→0 and using R¹p_*O_Y=0 identifies its last quotient with the actual normalization cokernel T. In particular this identification preserves the map ν_*O_X→T; it is not an arbitrary identification of two length-thirty sheaves.

Because R¹p_*O_Y(-2,-2)=O_P4(-2), one obtains the asserted sheaf surjection O_P4(-2)^5→T. After twisting by two the five constant sections generate every stalk. This by itself does not yet identify them with normalization differences, which is why the next step is essential.

## 3. The five sheaf generators genuinely lift

A(2,0)=O_Y(-3,-5) and B(2,0)=O_Y(-1,-3)^5 are acyclic by Künneth and the complete acyclicity of O_P4(-3), O_P4(-1). The first short exact sequence makes K(2,0) acyclic. The second then gives the natural isomorphism

H¹(Y,C(2,0)) → H¹(Y,J(2,0)),

whose source has dimension five. The defining ideal sequence gives a surjection H⁰(X,2H)→H¹(Y,J(2,0)), since H¹(Y,O_Y(2,0))=0.

The needed compatibility can be stated as two commuting diagrams. First, the maps induced by C→J commute with the Leray edge maps

H¹(Y,C(2,0)) → H⁰(P4,R¹p_*C(2,0)),
H¹(Y,J(2,0)) → H⁰(P4,R¹p_*J(2,0)).

The first horizontal map is an isomorphism because p_*C(2,0)=0. Second, the composite from H⁰(X,2H) through the connecting map and the second edge map is the map on global sections induced by ν_*O_X(2H)→T(2). This is standard functorial compatibility of the ideal-sequence boundary with derived pushforward; equivalently it follows by computing both boundaries in a compatible Čech double complex.

Consequently the image of H⁰(O_P4)^5→H⁰(T(2)) equals im(ρ₂), not merely an unspecified five-dimensional subspace. Every coordinate projection of this image is nonzero because the sheaf map is onto. Meanwhile dim im(ρ₂)≤5. The image is an H5-subrepresentation with nontrivial central character, so its dimension is a multiple of five. Hence r₂=5. This also shows that the five-dimensional nonambient normalization quotient injects into H⁰(T(2)). One need not prove the Pfaffian presentation itself equivariant: equivariance of ρ₂ suffices for the dimension argument.

The ancillary cohomology statements are consistent and justified. Acyclicity of K(2,0) also gives H⁰(J(2,0))=0, so the fifteen ambient quadratics inject. Together with the five-dimensional quotient this gives h⁰(X,2H)=20. Since r₂=5 and H¹(X,2H)=0, the normalization sequence yields h⁰(O_S(2))=15 and h¹(O_S(2))=25. Finally H¹(I_S(2))=0 follows because the fifteen ambient sections already exhaust H⁰(O_S(2)); this vanishing is a consequence, not an input to the lifting argument.

## 4. Whole graded image: no hidden saturation issue

For every integer n, Künneth and the absence of H¹,H²,H³ of all line bundles on P4 give

H²(Y,B(n,0))=0,  H³(Y,A(n,0))=0.

These two vanishings alone imply H²(Y,K(n,0))=0. Therefore H¹(Y,C(n,0))→H¹(Y,J(n,0)) is surjective. For n≥0, the ideal sequence identifies the latter with

Q_n := H⁰(X,nH) / im[H⁰(P4,O(n))→H⁰(X,nH)].

The maps for varying n commute with multiplication by R=Sym H⁰(P4,O(1)), and

H¹(Y,C(n,0))=R_(n−2)⊗H¹(Y,C(2,0)),

with R_k=0 for k<0. Since Q₂ is identified with H¹(Y,C(2,0)), this proves Q is generated by Q₂ as a graded R-module. The conductor map factors through Q, so its graded image M is a quotient graded R-module generated by M₂. Thus

M_n = R_(n−2) M₂ for every n≥2,

with M₀=M₁=0.

This is precisely the claim made in the proof. The kernel of Q_n→M_n may be nonzero in higher degrees and is H¹(P4,I_S(n)); its possible presence does not invalidate generation of a quotient. Conversely, neither vanishing of that kernel nor projective normality follows merely from generation. The module M must not be replaced by the complete section module Γ_*(T), whose low-degree pieces are all thirty-dimensional. No unjustified passage from a sheaf presentation to a presentation of Γ_*(T), or assumption that M is saturated, occurs.

## 5. Growth and interpolation interface

Once the quadratic image is nonzero at every node, PR578's diagonal-operator strict-growth proof starts in degree two. Its hypotheses use only the actual reduced support and the multiplication-stable image; those have been checked. The sequence

r₂=5, r₃≥10, r₄≥15, r₅≥16, r₆≥20, r₇≥25, r₈=30

is arithmetically correct, including the exceptional absence of the five-divisibility constraint in degree five. The resulting 9-regularity of O_S uses H¹(O_S(8))=0 and H²(O_S(7))=0, not ideal-sheaf regularity.

Over C, finite hyperplane avoidance in M₂ supplies one element w nonzero in every T_z(2). Multiplication by w is an isomorphism O_Z(d)→T(d+2). Therefore the image of ambient degree-d evaluation, multiplied by w, lies in M_(d+2) and retains its dimension. Conditional on independent quartic interpolation, r₆=30 follows, persists in every later degree by a linear form avoiding Z, and gives H¹(O_S(n))=0 for n≥6 and 7-regularity of O_S. No ideal-generation or original-target lifting conclusion follows without separate proof.

No correction required. Suggested editorial strengthening only: explicitly say that the quotient Q and its image M are distinct modules, and record the naturality diagram as above if this is incorporated into a combined proof.

## Final-version addendum: combined degree-six theorem

PASS for the revised PROOF.md with SHA-256 232c47887fd243321fc8370fdd66651f308ca43641b42dd170762de666cc5b4f, inspected on 2026-10-21. This addendum supersedes the earlier conditional status of the interpolation consequences, relative to the newly pinned interpolation theorem.

Fetched and read research/hm/eigenline-interpolation/PROOF.md at exact commit 865ab24e91333688d7ae76303d7d594aae8521f8 in Akilleez-QA/read-em-and-weep, returned blob 6582215ad524fd48e326aeea537f77c2421a30fc. Its Sections 2–4 supply cubic surjectivity on the twenty-five chirps, quartic surjectivity on all thirty eigenlines, and the actual-node identification. They do not use this quadratic-generation result. In particular its previous degree-seven conclusion is not being used circularly to prove degree six.

The revised Section 5 correctly multiplies the nowhere-zero quadratic normalization difference by ambient polynomials. Projection onto the twenty-five chirp fibers, together with cubic interpolation there, proves r5≥25; it does not assert independent control of the other five fibers. Quartic interpolation on the whole reduced support proves r6=30. Multiplication by a linear form avoiding that support propagates rank thirty to every n≥6. These statements retain the independently proved r2=5, r3≥10, and r4≥15.

The normalization sequence and the pinned H1(X,nH)=0 imply H1(O_S(n))=0 for n≥6. The revised proof explicitly checks the second regularity group: H2(O_S(5))=H0(X,K_X−5H)*=0, since (K_X−5H).F=−25 and F is nef. Cohomology above the support dimension vanishes. Therefore O_S is 7-regular, and complete-section multiplication is surjective for n≥7. These are correctly statements about O_S, not I_S or ambient polynomial surjectivity.

The revised Section 6 now explicitly distinguishes the nonambient normalization quotient from its conductor image and restricts their proven dimension equality to degree two. The possible higher-degree kernel H1(I_S(n)) is not assumed away. No correction required; all requested combined conclusions pass.
