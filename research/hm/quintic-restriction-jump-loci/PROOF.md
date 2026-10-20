# Restriction deformation jumps on smooth quintic threefolds

## Result and dependencies

Work over C. Let F be the literal normalized Horrocks–Mumford bundle on P(V)=P⁴, let B=End₀F, and let S₅=H⁰(P⁴,O(5)), of dimension 126. For p≠0 defining a smooth quintic Xₚ, write Eₚ=F|Xₚ. The independently established pairing theorem [PROOF](../quintic-pairing-representation/PROOF.md), [AUDIT](../quintic-pairing-representation/AUDIT.md) gives

    U=H²B(−5), dim U=2,
    Φ:S₅→Sym²U*, Φ=cΨ,

where Ψ is a fixed nonzero, hence surjective, N-equivariant map and c remains unresolved. H₅ acts trivially on U and Sym²U*. Set K=ker Ψ, a 123-dimensional subspace.

For EVERY smooth quintic, Eₚ is simple and

    dim Ext⁰_X(Eₚ,Eₚ)=dim Ext³_X(Eₚ,Eₚ)=1,
    dim Ext¹_X(Eₚ,Eₚ)=dim Ext²_X(Eₚ,Eₚ)=26−rank Φ(p).       (A)

In particular, if c=0 all these tangent/obstruction-space dimensions are 26. If c≠0, the dimensions are respectively 26, 25, 24 on the rank-zero, rank-one, rank-two strata of Ψ(p). Each stratum contains smooth quintics. More strongly, EVERY affine fiber of Ψ contains a nonempty Zariski-open set of smooth quintics. These are structural existence statements, with no polynomial selected or evaluated.

The numerical input is the established cohomology row for B and its Serre dual:

    h⁰B=h⁴B=0, h¹B=24, h²B=2, h³B=0;
    h⁰B(−5)=h¹B(−5)=h⁴B(−5)=0,
    h²B(−5)=2, h³B(−5)=24.

See [the End-cohomology audit](../pairing-foundation-inputs/COHOMOLOGY.md), items 4–6, for stability/simplicity, negative Hom vanishing, and the numerical row. The positive-middle-cohomology theorem [PROOF](../hm-low-degree-dependency/PROOF.md) is compatible with this argument but is NOT needed for (A) or smooth-fiber existence.

## 1. Restriction sequence and simplicity

Since B is locally free and p is a nonzero hypersurface equation,

    0→B(−5) --p→ B → i_*B|Xₚ →0.

The degree-zero segment and H¹B(−5)=0 give H⁰(B|Xₚ)=0. The middle segment is precisely

    0→H¹B→H¹(B|Xₚ)→U --mₚ→ H²B
      →H²(B|Xₚ)→H³B(−5)→0.                      (1)

There are thus canonical short exact sequences

    0→H¹B→H¹(B|Xₚ)→ker mₚ→0,
    0→coker mₚ→H²(B|Xₚ)→H³B(−5)→0.

No splitting is asserted. Under the perfect trace/Serre identification H²B=U*, mₚ corresponds to Φ(p), so both dimensions in the middle equal 24+(2−rank Φ(p)). Also H³(B|Xₚ)=0, from H³B=H⁴B(−5)=0.

The scalar sequence 0→O(−5)→O→O_X→0 gives

    (h⁰O_X,h¹O_X,h²O_X,h³O_X)=(1,0,0,1).

As End Eₚ=O_X⊕B|Xₚ and Eₚ is locally free, Extⁱ_X(Eₚ,Eₚ)=Hⁱ(X,End Eₚ). This proves simplicity and (A). The tangent space to the deformation functor of Eₚ ON THE FIXED Xₚ is Ext¹; Ext² is an obstruction space. The same tangent and obstruction spaces apply to fixed-determinant deformations because H¹O_X=H²O_X=0. We do not assert stability of Eₚ, vanishing of obstruction maps, smoothness of its moduli space, or equality between tangent dimension and local moduli dimension. Deformations of the pair (Xₚ,Eₚ) are a different problem.

## 2. Exact quadratic jump equation

Choose a basis of U and write the three independent linear forms defined by Ψ as

    Ψ(p) = [ a(p)  b(p) ]
           [ b(p)  d(p) ].

Define Q(p)=a(p)d(p)−b(p)². Its zero set is independent of these basis choices and of scaling Ψ. Q has quadratic rank three. If c≠0, then

    rank Φ(p)=0  ⇔  a(p)=b(p)=d(p)=0  ⇔  p∈K;
    rank Φ(p)=1  ⇔  Q(p)=0 and p∉K;
    rank Φ(p)=2  ⇔  Q(p)≠0.                       (2)

Equivalently, for the binary quadratic Ψ(p)(s,t)=a(p)s²+2b(p)st+d(p)t², its discriminant is 4(b(p)²−a(p)d(p)), and its vanishing is exactly the rank-at-most-one condition. This is the pairing discriminant, NOT the discriminant of the quintic hypersurface.

Let Ω⊂P(S₅)=P¹²⁵ be the open set parametrizing smooth quintics. For c≠0 the exact tangent-dimension jump loci inside Ω are

    dimension 26: Ω∩P(K),
    dimension 25: Ω∩(V(Q)\P(K)),
    dimension 24: Ω\V(Q).

Here P(K)=P¹²² has codimension three. V(Q) is an irreducible quadric hypersurface of dimension 124 whose singular locus and vertex are exactly P(K). The rank-one stratum is smooth as a parameter-space stratum, and the rank-two stratum is open in P¹²⁵. Section 4 proves none disappears upon intersecting Ω. If c=0, det Φ vanishes identically and every point of Ω has tangent dimension 26; the auxiliary Ψ-strata still exist but no longer measure actual restriction jumps.

## 3. Why K is basepoint-free: dual action checked

Use the line convention P(V), so S₅=Sym⁵V*. The polynomial action is (h·p)(v)=p(h⁻¹v). Its dual action on λ∈S₅* is (h·λ)(p)=λ(h⁻¹·p). For v≠0 let ev_v(p)=p(v). Then

    h·ev_v=ev_(hv).

The central element ζI acts on V by ζ, on V* by ζ⁻¹, and on S₅ and S₅* trivially, since ζ⁵=1. Reversing all conventions replaces V by V* but changes none of the reasoning. This accounts explicitly for the central weight; there is no degree-five scalar-character discrepancy.

Dualizing the surjection Ψ gives

    K^⊥=im Ψ* ⊂ (S₅*)^H₅.                       (3)

Indeed its domain (Sym²U*)* is an H₅-trivial module and Ψ* is equivariant. Crucially, (3) is a space of invariant FUNCTIONALS, not a subspace of quintic sections being confused with its dual.

Suppose x=[v] were a base point of K. Then ev_v annihilates K, so lies in K^⊥ and is H₅-fixed. Its projective class is the degree-five Veronese image ν₅(x)∈P(S₅*). Equivariance and injectivity of ν₅ imply hx=x for every h∈H₅. Thus Cv would be an invariant line in the five-dimensional Schrödinger representation V. That representation is irreducible, so no such line exists. This is a contradiction. Consequently K globally generates O(5).

The weaker conclusion that the evaluation LINE is invariant would already suffice; (3) gives actual invariant vectors. Irreducibility here is linear irreducibility of H₅, and projective fixedness of a point means exactly preservation of a one-dimensional subspace. Individual group elements may have fixed points; there is no COMMON fixed point.

## 4. Smoothness in every affine fiber, with the translation issue resolved

We use the characteristic-zero basepoint-free Bertini theorem. For completeness its applicable form follows from the universal divisor: for a basepoint-free space L⊂H⁰(P⁴,O(5)), the incidence

    I_L={(x,[s]): s(x)=0} ⊂ P⁴×P(L)

is the projective bundle over P⁴ of the kernel of the surjective evaluation L⊗O→O(5), hence smooth. Its projection to P(L) is proper and dominant, as every nonzero homogeneous quintic has a zero. Its generic fiber is regular (localization of regular rings); its characteristic-zero function field is perfect, so this fiber is smooth. The non-smooth locus is closed, and properness makes its image closed; it misses the generic point. Removing that image gives a nonempty open set of smooth members. The regular-to-smooth and openness facts can be found in the Stacks Project, [schemes smooth over fields](https://stacks.math.columbia.edu/tag/04QM) and [smooth morphisms](https://stacks.math.columbia.edu/tag/01V4). This proof does not require that the linear system define an immersion.

Apply this first to L=K: there is a nonempty open subset of P(K) consisting of smooth quintics. Thus the zero fiber of Ψ contains smooth nonzero members.

For a nonzero target q∈Sym²U*, choose any preimage p₀ abstractly and set L=K⊕Cp₀. Since L contains the basepoint-free K, it too is basepoint-free. The smooth-member open subset of P(L) intersects the nonempty open chart P(L)\P(K). Every point of that chart has a UNIQUE representative p₀+k with k∈K, obtained by rescaling the nonzero p₀ coefficient to one. The chart is thus isomorphic to the affine fiber Ψ⁻¹(q)=p₀+K, and the smoothness open set becomes a nonempty open set in this fiber.

This is the correct translation-family argument: Bertini is applied to the enlarged LINEAR system, followed by passage to an affine chart. A translate p₀+K is not itself a vector subspace and is not silently treated as one. For q=0 the first argument applies. Since Ψ is surjective and symmetric two-by-two forms have all ranks 0,1,2 over C, every Ψ-rank stratum contains smooth quintics. No p₀ coefficients or q values have been evaluated.

## 5. Geometric meaning of the unresolved scalar

The following are equivalent:

    c=0;
    every smooth quintic restriction has dim Ext¹=26;
    no smooth quintic restriction has dim Ext¹=24;
    no smooth quintic restriction has dim Ext¹=25.

The implications using existence are supplied by Section 4. Thus c≠0 is also equivalent to the existence of a smooth restriction with either tangent dimension 24 or tangent dimension 25. If c≠0, a general smooth quintic has tangent/obstruction dimensions 24, with exactly the quadratic and linear jump loci above; if c=0, the common value is 26. These equivalences connect the scalar to actual restriction deformation theory without resolving it.

One must not replace “every smooth quintic” by “some smooth quintic” in the dimension-26 criterion: even when c≠0 there are smooth quintics in P(K) with dimension 26. Similarly, this computation says nothing about whether the restrictions' deformations are obstructed in actuality. It determines their tangent spaces and the dimensions of their natural obstruction spaces.

## Scope

Only existing proved cohomology/representation inputs, finite-group duality, exact sequences, elementary determinantal geometry, and the characteristic-zero Bertini argument were used. No selected quintic, section, HM map, physical source, or multiplication rank was evaluated; no scalar nonvanishing was assumed. All writes were local proof files. Independent audit is recorded in AUDIT.md.
