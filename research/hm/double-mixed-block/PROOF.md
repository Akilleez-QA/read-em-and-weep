# A canonical doubled mixed block in the actual opposite pencil

Work over C with G=SL2(F5), W the physical negative doublet, W' the other doublet, A=Sym2 W, S=Sym3 W, D=Sym4 W, T6=Sym5 W, and V=Sym2 W'. Write P for the even four-dimensional irreducible. All bundles are on the negative parameter line T=P(W*) with the standard equivariant linearization. No actual coefficient, point, parameter, matrix or instance rank is evaluated.

## 1. Immutable inputs and theorem

INPUTS.json authenticates three originals in Akilleez-QA/read-em-and-weep:

- FIRST, PR1060, commit13acb1a85a38e9d236069f41b21dd4cef70ab056, research/hm/positive-joint-embedding/PROOF.md: actual positive multiplication from the unique W in H1(B(1))_- selects a marked T6 in the full U=H1(B(2))_-. Its negative V channel is zero. The proof also authenticates the original opposite pencil's kernel A O(-6), and proves the two universal contraction-kernel obstructions used below.
- AMPLE, PR994, commit48727e1f5fd5ab079c21b8b39af608f7d91fabab, research/hm/opposite-ample-exclusion/PROOF.md, Sections2–3: the complete negative coefficient map W tensor U -> N=H1(B(3))_+ is onto. This is explicitly the original full cohomological map, not a reduced pencil after cancellations.
- MONAD, PR928, commit1a8fb75aa886f9bb6c07e357759d37630cdd127d, research/hm/profile11-source127-cdf-positive-factorization/PROOF.md, Section3: the actual full target character N=1+4A+2V+3P+3D, dimension46. No source-specific formal factorization in that original is used.

The full source is U=2W+2W'+3S+4T6, dimension44, as in FIRST. Let M=Hom_G(T6,U), a canonical four-dimensional multiplicity space. The actual negative V-channel induces a linear map

    f_V:M -> Hom_G(V,N),                         (1)

up to a harmless choice of generator of its one-dimensional universal intertwiner space. Its kernel K is canonical. We prove dim K=2, and that actual multiplication on the canonical source U_K=K tensor T6 has image in canonical target subspaces N_P,K and N_D,K of characters 2P and 2D. Its coefficient image is their direct sum, and the actual bundle block fits into

    0 -> U_K O(-1) -> (N_P,K + N_D,K) O
      -> K tensor V O(2) -> 0.                  (2)

Thus its quotient has rank6 and degree12. The named quotient identification is an equivariant isomorphism, not an assertion of scalar-normalized canonical coordinates. The actual source and target subspaces are canonical. The marked T6 of FIRST lies in U_K and supplies a marked line in K; no canonical complementary line is selected.

## 2. The actual V-channel is onto on multiplicities

Semisimplicity gives the canonical isotypic evaluation isomorphism M tensor T6 -> U_T6. Complete multiplication, followed by the canonical isotypic projections in N, restricts to three channels on this subspace. The fixed identities are

    W tensor W = 1+A,      W tensor W' = P,
    W tensor S = A+D,      W tensor T6 = V+P+D.   (3)

Each summand on the last right side has multiplicity one. Therefore, after choosing a nonzero universal intertwiner for each channel, the restricted coefficient map has multiplicity maps

    f_V:M->M_V, f_P:M->M_P, f_D:M->M_D,
    dim M=4, dim M_V=2, dim M_P=dim M_D=3,        (4)

where M_R=Hom_G(R,N). Rescaling an intertwiner rescales the associated map but changes neither its kernel nor its image.

Only the T6 source isotypic component can reach the V target in (3). AMPLE's full coefficient surjectivity therefore forces f_V onto. Consequently K=ker f_V has dimension2. This dimension is forced by actual surjectivity and characters, not an evaluation of any selected coefficient map.

## 3. Both remaining channel maps are injective on K

We show ker(f_P|K)=ker(f_D|K)=0. The argument treats an arbitrary abstract multiplicity direction, never a selected numerical HM value.

If a nonzero k in K also satisfied f_P(k)=0, the corresponding embedded T6 source could only map to D. If f_D(k)=0 as well, its entire T6 O(-1) would lie in A O(-6), impossible because Hom(O(-1),O(-6))=0. Otherwise its nonzero D component is the unique universal contraction T6 O(-1)->D O, with kernel O(-6). That line would inject equivariantly into the actual full kernel A O(-6), impossible since Hom_G(1,A)=0. Thus f_P|K is injective.

If a nonzero k in K also satisfied f_D(k)=0, the just-proved injectivity makes f_P(k) nonzero. The unique P channel is W' times quadratic contraction A O(-1)->W O, because W' tensor A=T6 and W' tensor W=P. Its kernel W' O(-3) would inject into A O(-6), impossible since H0(O(-3))=0. Thus f_D|K is injective too.

Both contradictions use the kernel of the original 44-to-46 pencil. They do not use, or assert, a kernel for a different reduced presentation.

Define

    N_P,K = im(f_P|K) tensor P subset N,
    N_D,K = im(f_D|K) tensor D subset N.          (5)

These are canonical subspaces of dimensions8 and10. Changing the universal intertwiner scalars leaves them unchanged. The restricted coefficient map on W tensor U_K is onto their direct sum, and its coefficient kernel is exactly K tensor V.

## 4. Simultaneous normalization and saturation

The two injective maps f_P|K and f_D|K identify their own image multiplicity spaces with the SAME K. These are not arbitrary identifications of two unrelated two-dimensional spaces: the actual maps from K provide them. Thus there is no additional relative matrix left in the restricted block after using these maps as the target identifications.

The universal quadratic evaluation sequence, tensored by V, is

    0 -> (V tensor W) O(-1) -> (V tensor A) O
      -> V O(2) -> 0,                            (6)

with V tensor W=T6 and V tensor A=P+D. Both components of its complete coefficient map are nonzero: that map is V tensor (W tensor W -> A), onto V tensor A. Each channel has dimension one by (3). Choosing these two nonzero intertwiners as the normalizations in (4), the actual restricted map becomes exactly K tensored with (6). This proves (2), including fiberwise injectivity and a locally free quotient everywhere on T.

The quotient is independent of choices as the actual cokernel of the marked block; only its displayed identification with K tensor V O(2) depends on the harmless scalar conventions. In particular the result is stronger than a generic-rank or character assertion.

FIRST's marked T6 has zero V channel, hence its multiplicity line is contained in K. The theorem enlarges that actual marked subcomplex to a canonical two-copy subcomplex. It does not choose a second line or a direct-sum decomposition relative to the marked line.

## 5. An inherited weighted residual presentation

This subcomplex can be removed from the ORIGINAL opposite pencil without replacing any actual map. Put N_K=N_P,K+N_D,K and define intrinsically

    Z=(N O)/(U_K O(-1)).

The injection in (2) and a constant equivariant complement to N_K show that Z is locally free. More intrinsically it fits into

    0 -> K tensor V O(2) -> Z -> (N/N_K) O -> 0.  (7)

Its rank is34 and degree12. The source quotient is U/U_K, of character 2W+2W'+3S+2T6 and dimension32. Quotienting the original complex by its injective marked subcomplex gives an actual exact sequence

    0 -> A O(-6) -> (U/U_K) O(-1) -> Z -> C -> 0. (8)

For clarity the inherited kernel remains injective in the source quotient: its intersection with U_K O(-1) is zero, because the restricted marked map is injective. Exactness at the middle and the unchanged cokernel follow from the quotient diagram, or the snake lemma applied to images.

The extension (7) splits equivariantly since H1(O(2))=0 and invariants are exact for the finite group G. Its splitting is not asserted canonical. After such a choice, (8) has target

    (1+4A+2V+P+D) O + K tensor V O(2),

with constant rank28 and weighted rank6. The complete target has rank34, not28. The balances are rank(C)=34-32+3=5 and degree(C)=12-(-32)-18=26. All remaining actual off-diagonal maps are retained. In particular the rank-six term in (7) is not asserted to inject into the rank-five C: other source summands can meet it in Z.

## 6. Scope and verification

The conclusion concerns the original full opposite cohomological pencil and its actual embedded subspaces. It does not identify N_P,K or N_D,K with separately embedded im-h-generated subspaces, nor identify repeated representation labels across unrelated constructions. It selects no source pair, opposite bundle type, vertex scalar or terminal negative-string branch.

The verifier uses only fixed nine-class exact characters, the imported Euler formula for the full target, universal degree balances and immutable-input authentication. No actual HM/source tensor, point, parameter, coefficient or instance matrix is evaluated. REPRODUCE.md reconstructs the omitted audit copies. The authored proof requires the independent mathematical review recorded in REVIEW.md; it is not claimed to be proof-assistant formalization.
