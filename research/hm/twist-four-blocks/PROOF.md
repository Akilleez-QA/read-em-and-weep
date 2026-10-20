# Twist four: five multiplicity-free irreducible obstruction blocks

Let F be the normalized Horrocks–Mumford bundle on complex P4, and B=End_0(F). Use the normalizer representations of the audited twist-three proof, and write Q=χ4# (the spinorial four-space), C=χ4 (the other four-space), W=χ2, W'=χ2'. Then

    H0 B(4) is a multiplicity-free subrepresentation of
    V ⊗ (χ4 ⊕ χ5 ⊕ W ⊕ Q ⊕ χ6).                 (1)

Each listed block is irreducible for N. Its dimension is respectively20,25,10,20,30, and each either occurs wholly or does not occur. More intrinsically, (1) is a kernel in a canonical trace-quotient of the section-resolution spectral sequence. There are exactly five possible irreducible obstruction restrictions; a restriction is zero or injective, not necessarily a scalar map. In addition,

    h1 B(4)=85+h0 B(4),    Hi B(4)=0 for i≥2.    (2)

The χ6 block, if present, is necessarily a new minimal quartic generator of the trace-free section module, even if the unresolved fifteen-dimensional cubic section space is nonzero. No value of any of these five maps is determined here.

## 1. Sources, inputs and conventions

The prerequisite [twist-two vanishing](../twist-two-vanishing/PROOF.md) and [twist-three reduction](../twist-three-reduction/PROOF.md) are public companion proofs. The refined coefficients and conventions are derived in [the primary-source input note](../twist-three-reduction/INPUTS.md), not assumed from the numerical twist-two proof. Its inputs include the equivariant resolution

    0 → A O(-8) → D O(-6) → G O(-5)
      → P O(-4) ⊕ C O(-3) → F → 0,

with A=W', D=V1⊗Q and C=χ4. The remaining coefficient dimensions are dim G=35, dim P=15. We use H1F=V3, H1F(1)=V1⊗W', H1F(3)=W', H2F(-2)=W, and the facts that H2F(t)=0 otherwise, H1F(t)=0 outside0,1,2,3 and H0F(t)=0 for t<3. Also F*=F(1), so H3F(t)=H1F(-t-4)* and H4F(t)=H0F(-t-4)*.

Primary sources freshly opened on 2026-10-20:
- W. Decker, Monads and cohomology modules of rank2 vector bundles, Compositio76(1990), pp14–16: https://www.numdam.org/article/CM_1990__76_1-2_7_0.pdf
- G. Horrocks and D. Mumford, A rank2 vector bundle on P4 with15,000 symmetries, Topology12(1973), Lemmas2.4,3.3 and appendix: https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf

Decker supplies the resolution; HM supplies the finite representation identities. Their statements are not being treated as a direct computation of H0B(4). The appendix character table was visually inspected locally. The small accompanying characters.py only checks universal character identities across its nine conjugacy classes. It does not evaluate a bundle differential or any chosen section.

Put X=V*=S1. HM's identities, their duals and Galois conjugates give

    V⊗V1 = V3⊗(χ3⊕W'),
    V⊗V3 = X⊗(χ3'⊕W),
    V1⊗V1 = X⊗(χ3⊕W'),
    V3⊗V3 = V⊗(χ3⊕W'),
    X⊗V1 = V⊗(χ3'⊕W),
    Sym2 V = V1⊗χ3',
    Sym3 V = V3⊗(χ5⊕W'),
    Sym4 V = X⊗(χ4⊕Q⊕χ3⊕χ3').

All quotient-group representations displayed are self-dual. The H5-isotypic equivalence in HM(2.2) says that Vi⊗U is irreducible for N whenever U is irreducible for SL2(F5). Distinct such U remain inequivalent. These are finite-group identities, not continuous SL2 representation assumptions.

## 2. Determine G by the twist-zero cohomology complex

In twist zero of the resolution, only H4 of its first three terms can survive. Their vector-space complex is

    A⊗Sym3 V → D⊗V → G,

at total cohomological degrees1,2,3. It has cohomology V3,0,0 respectively. Therefore its representation-valued Euler characteristic gives

    [G]=[D⊗V]−[A⊗Sym3 V]+[V3].

Substituting the identities above, the quotient-group coefficient is

    (χ3+W')Q − W'(χ5+W') + 1 = χ5+W.

For transparency, the character products used are

    χ3 Q=W+Q+χ6,  W'Q=χ3'+χ5,
    W'χ5=Q+χ6,    W'^2=1+χ3'.

Thus semisimplicity identifies the actual coefficient

    G=V3⊗(χ5⊕W).                                (3)

## 3. Determine P by the acyclic twist-minus-one complex

F(-1) is acyclic by the imported table and duality. The only nonzero entries of the resolution's line-bundle cohomology are the H4 complex

    A⊗Sym4 V → D⊗Sym2 V → G⊗V → P.

It is exact, and hence

    [P]=[G⊗V]−[D⊗Sym2 V]+[A⊗Sym4 V].

Extracting X with the displayed tensor identities gives the character identity

    (χ3'+W)(χ5+W) − (χ3+W')Qχ3'
       + W'(χ4+Q+χ3+χ3') = χ3.

This equality can be checked on each of the nine appendix columns; the check is recorded in characters.py. Therefore

    P=X⊗χ3.                                      (4)

Twist two of the resolution has only A⊗H4O(-6) at total degree1, so it also determines the previously implicit input

    H1F(2)=V⊗W'.                                 (5)

No virtual subtraction is being interpreted as an arbitrary choice of actual maps: these coefficient identifications follow from exact complexes and semisimplicity.

## 4. The twist-four spectral sequence has one row and one map

Tensor the resolution by F*(4)=F(5). In columns -3,-2,-1,0 its terms are

    A F(-3), D F(-1), G F,
    P F(1) ⊕ C F(2).

F(-3),F(-1) are acyclic; F,F(1),F(2) have only H1 nonzero. Thus the entire E1 page is

    L=G⊗V3  --d1-->  R=P⊗(V1⊗W') ⊕ χ4⊗(V⊗W'),

in positions(-1,1) and(0,1), with dimensions175 and190. There is no other row, incoming map, or higher differential. Hence canonically

    H0End(F)(4)=ker d1,    H1End(F)(4)=coker d1,
    HiEnd(F)(4)=0 for i≥2.                        (6)

Using(3)–(5) and the appendix products gives

    L=V⊗(χ5⊕χ6⊕2χ4⊕2Q⊕χ3⊕χ3'⊕W),
    R=V⊗(χ5⊕3χ6⊕χ4⊕Q⊕χ3'⊕2W).                 (7)

These dimensions are5·35=175 and5·38=190.

## 5. Scalar cancellation leaves precisely five blocks

The trace splitting injects the scalar space

    S4=V⊗(χ4⊕Q⊕χ3⊕χ3')

into ker d1 and thus into L. Since the embedding is canonical, d1 descends to

    δ4:L/S4 → R.

Exactness of taking the quotient and the trace splitting give

    ker δ4=(ker d1)/S4 ≅ H0B(4).

The quotient's representation is

    L/S4 ≅ V⊗(χ4⊕χ5⊕W⊕Q⊕χ6).

This quotient, rather than a chosen complementary subspace, is the canonical object. It is multiplicity-free. Its kernel is therefore a sum of a subset of the five inequivalent irreducibles, proving(1). The target has multiplicities1,1,2,1,3 for these five respective types; therefore the theorem does NOT assert that every block map is a scalar.

The Euler characteristic in(6) is175−190=−15. Subtract χO(4)=70 to obtain χB(4)=−85. Higher cohomology vanishes and(2) follows. In particular h0 is a subset sum of20,25,10,20,30, not an arbitrary multiple of five in[0,105].

## 6. Next useful consequence: the thirty-dimensional block cannot be inherited from cubics

Let M=⊕t H0B(t), a graded S-module. We know M_t=0 for t≤2 and M3=0 or V1⊗χ3. If M3 is nonzero, then

    S1⊗M3 = V⊗(χ3'⊕W)⊗χ3
           = V⊗(χ4⊕χ5⊕W⊕Q),                    (8)

because χ3'χ3=χ4+χ5 and Wχ3=W+Q. If M3=0 its multiplication image is of course zero. In both cases, S1M3 has no V⊗χ6 constituent. The minimal quartic generator space is

    M4 / S1M3.

Consequently its V⊗χ6 isotypic summand equals that of M4. Thus presence of the thirty-dimensional χ6 block in H0B(4) is equivalent to presence of that exact new minimal quartic-generator block. It cannot be explained away as multiplication of the unresolved cubic sections. This is a structural root-cause separation, not a proof that the block is present or absent.

There is also a small numerical compatibility restriction: if M3≠0, multiplication by any fixed nonzero x∈S1 is injective on M3, since B is locally free and x is nonzero on a dense open subset. Thus dim(S1M3)≥15. By(8), its possible dimensions are subset sums of20,25,10,20, and the smallest such sum at least15 is20. Hence the nonzero cubic alternative forces h0B(4)≥20. Conversely h0B(4)=0 or10 forces H0B(3)=0.

## Evidence boundary

The result makes genuine progress beyond the twist-three dichotomy and prior spectral-cover exclusions: it identifies two further equivariant resolution coefficients, gives the entire twist-four obstruction map with its five possible kernel types, gives exact companion cohomology, and isolates an independent new-generator channel. It does not determine any of the five map values, prove twist-four vanishing, or settle any selected source, cofactor, pairing, collision-order, or physical-obstruction question. No actual HM instance was computed and no external service was changed.
