# Positive joint injectivity and the actual mixed descendant constraint

Work over C with G=SL2(F5), coordinates H=V+W, where W is the negative doublet and V the positive three-dimensional representation. Put A=Sym2 W, S=Sym3 W, D=Sym4 W and T6=Sym5 W; W' is the other doublet. Let B=End_0(F) for the actual normalized HM bundle. Multiplication below is actual global cohomology multiplication. No selected coefficients, points, parameters, matrices or instance ranks are evaluated.

## 1. Immutable inputs and result

INPUTS.json pins four originals in Akilleez-QA/read-em-and-weep:

- STEINER, PR1045, 47d2832dd306f26eabcfa2a57450cea982c5a153, research/hm/global-steiner-reduction/PROOF.md: the unique W subspace U1 in H1(B(1))_- has actual negative multiplication onto the unique A subspace U2 in H1(B(2))_+, with precisely the determinant relation in W tensor W.
- QUADRIC, eeb1a11799ca38a60c37f6ba96f263ef8e20dd1c, research/hm/order-four-quadratic-load/POSITIVE-INVARIANT-VERTEX-RANK-33-PROVED.md: H0(B(4))=0. No assertion about its selected quadratic map is needed.
- CHAR, PR938, e5aa6e4695eee79cd0222d8f6b57aa60b7a0dab5, research/hm/opposite-source-weights/PROOF.md, Section 2 only: the full actual negative space

      H1(B(2))_- = 2W+2W'+3S+4T6, dimension44.

- KERNEL, db51525015bb7c5e825833d550d08dedf6f6ea96, research/hm/order-four-quadratic-load/EXACT-HYPERPLANE-ADJOINT-SYZYGY-BUNDLE.md: the actual full negative pencil has exact kernel A O(-6) in H1(B(2))_- O(-1) -> H1(B(3))_+ O, of dimensions44 and46. Only its exact kernel statement is needed, not its then-unresolved torsion alternatives.

The earlier conditional torsion discussion in CHAR is not used.

We prove both joint positive-coordinate maps

    H1(B(k)) -> V* tensor H1(B(k+1)), k=1,2,       (1)

are injective. In particular actual positive multiplication embeds V tensor U1, an irreducible T6, into the FULL 44-dimensional H1(B(2))_-. Its image U2,V is a canonical marked T6 subspace, not an arbitrary copy in its four-dimensional multiplicity space.

Actual negative multiplication on U2,V kills exactly the prescribed V summand of its DOMAIN as a necessary relation: more precisely it kills the canonical V subspace in W tensor U2,V=V+P+D and factors through P+D. Section5 proves the stronger conclusion: both P and D channels are nonzero, the coefficient kernel is exactly V, and the selected bundle block has quotient V O(2). The common mixed image is exactly V U2 = W U2,V inside H1(B(3))_+.

## 2. A three-coordinate Koszul injectivity lemma

Let E be any locally free sheaf on P4 and let V be a three-dimensional space of independent linear forms cutting out a line L. Assume H0(E(k+2))=0. Then the simultaneous multiplication map H1(E(k))->V* tensor H1(E(k+1)) is injective.

Indeed place the Koszul complex

    Lambda3 V tensor E(k) -> Lambda2 V tensor E(k+1)
      -> V tensor E(k+2) -> E(k+3)               (2)

in cohomological degrees -3,-2,-1,0. Since the forms are a regular sequence and E is locally free, (2) is quasi-isomorphic to E(k+3)|L in degree zero. Its hypercohomology in negative degrees is therefore zero. In the spectral sequence E1^(p,q)=Hq(K^p), the term E2^(-3,1) is the kernel of the first H1 differential: there is no incoming first differential. There are no incoming higher differentials, because their source columns are less than -3. The only possible outgoing higher differential with nonnegative second index is

    d2: E2^(-3,1) -> E2^(-1,0).

Its target vanishes since E1^(-1,0)=V tensor H0(E(k+2))=0. Higher outgoing targets have negative second index. Thus E2^(-3,1)=E_infinity^(-3,1)=0, as its total degree is -2. The first differential is, after the usual exterior identifications, exactly simultaneous multiplication. This proves the lemma. It uses no H2, H3 or H4 vanishing.

For the actual positive V, det V is trivial and Lambda2 V identifies with V*, so this first differential has the form (1), up to a harmless determinant identification. Its kernel consists of classes killed by every positive coordinate. No individual coordinate map is claimed injective.

QUADRIC gives H0(B(4))=0. Multiplication by any nonzero homogeneous linear form injects sections of a locally free sheaf on integral P4, hence H0(B(3))=0 too. Apply the lemma with E=B and k=1,2. This establishes (1), including both central parities.

## 3. The actual positive T6 is nonzero and embedded

Write mu:V tensor U1 -> H1(B(2))_- for actual multiplication. If mu vanished, every element of U1 would be killed by all positive coordinates, contradicting (1) for k=1. Thus mu is nonzero. The fixed representation identity V tensor W=T6, and irreducibility of T6, make mu injective. Define U2,V=im(mu). This subspace is canonical because U1 is the unique W-isotypic subspace and multiplication is canonical. An isomorphism U1=W may be rescaled without changing any of these images.

CHAR gives the full negative coefficient space of dimension44. No assertion identifies U2,V with a subspace of the reduced 26-dimensional opposite source: that latter space is obtained through other actual quotients and cancellations, which have not been compared here.

## 4. Mixed commutativity kills the V channel

Use STEINER's coherent identification of negative multiplication W tensor U1 -> U2 with the nonzero symmetric projection W tensor W -> Sym2 W=A. Its kernel is Lambda2 W. For v in V and w in W, multiplication commutes on cohomology. Consequently the two actual composites from V tensor W tensor U1 agree:

    v tensor w tensor u |-> w(vu) = v(wu).        (3)

The right composite factors through V tensor U2, and annihilates V tensor Lambda2 W. The left is negative multiplication on U2,V after the injective identification mu. Therefore it kills the canonical V subrepresentation

    V tensor Lambda2 W subset W tensor (V tensor U1).

Since det W=1, the quotient domain is V tensor A=P+D. Equivalently W tensor T6=V+P+D, and the selected actual negative multiplication has its V channel zero. These are statements about the marked actual embedding, not about all T6 copies of the ambient space.

Equality (3), together with surjectivity W tensor U1 -> U2 and the identification V tensor U1=U2,V, gives equality of the two actual images V U2=W U2,V. This image is nonzero: otherwise U2 would be killed by all positive coordinates, contradicting (1) for k=2. Thus at least one of the two irreducible P and D channels is nonzero. Since P and D are nonisomorphic irreducibles, the mixed image has character P, D, or P+D. At this stage these are necessary alternatives; Section5 rules out the first two using the actual full pencil kernel. Moreover the joint positive map restricted to U2 is injective, so no nonzero element of that A is annihilated by every positive coordinate.

## 5. The actual full kernel forces both mixed channels

Write m for the full actual 44-to-46 pencil in KERNEL, over T=P(W*). Its sheaf kernel is A O(-6), with its actual inclusion. Restrict m to U2,V O(-1). By Section4 this restricted map has only P and D components. Each corresponding Hom channel has dimension one:

    Hom_G(T6,D tensor W)=C, Hom_G(T6,P tensor W)=C.

Multiplicity spaces in the full target remain allowed. A nonzero channel selects a single actual copy of the corresponding irreducible target.

Suppose its P component vanished. Its D component is nonzero by Section4, and up to nonzero target scaling is the universal binary contraction T6 O(-1)->D O, with kernel O(-6). This is the dual of complete quintic evaluation, twisted by -1. The resulting nonzero sheaf injection O(-6)->ker(m)=A O(-6) is impossible: its equivariant Hom space is Hom_G(1,A)=0. Hence the P component cannot vanish.

Suppose instead its D component vanished. The remaining unique P channel is the tensor by W' of quadratic binary contraction A O(-1)->W O. Using W' tensor A=T6 and W' tensor W=P, its kernel is W' O(-3). This is the dual quadratic evaluation sequence twisted by -1. It would inject into A O(-6), but even the ordinary Hom space is zero since H0(O(-3))=0. Hence the D component cannot vanish either. These contradictions use sheaf kernels and equivariance, not a fiber-rank evaluation.

Let U3,P and U3,D be the resulting actual target copies. Both are canonical images of the two irreducible factors of V tensor U2. The mixed coefficient map is therefore injective on P+D and has kernel precisely V on W tensor U2,V. In particular its image dimension is9.

To identify the bundle quotient, tensor the complete quadratic evaluation sequence by V:

    0 -> (V tensor W) O(-1) -> (V tensor A) O
      -> V O(2) -> 0.                            (4)

Its two target components P and D are both nonzero: the complete coefficient map is V tensor (W tensor W -> A), which surjects onto V tensor A=P+D. Each relevant Hom channel is one-dimensional. Therefore any pair of nonzero channels differs from (4) only by separate nonzero scalings of the two target factors and a compatible source identification. Applied to the actual selected block, (4) proves that it is injective on every fiber with quotient V O(2). The marked subspaces are canonical; the scalar identifications with named model representations are not.

## 6. Scope and reproducibility

The new constraint selects an actual T6 in the full degree-two negative cohomology and proves a zero V channel for its negative descendants, compatibly with the marked W-to-A string. It does not identify this subspace with null's separately embedded im-h-generated module, or select any source pair, opposite bundle type, terminal string value or vertex scalar. Repeated representation labels do not identify actual embeddings.

The verifier checks only exact nine-class fixed representation identities, the finite spectral-sequence index argument, and the four immutable input blobs. The cohomological and actual-map arguments above are structural proofs, not outputs of a selected-instance calculation. REPRODUCE.md reconstructs omitted audit copies before replay. REVIEW.md records fresh independent whole-proof review of the final bytes.
