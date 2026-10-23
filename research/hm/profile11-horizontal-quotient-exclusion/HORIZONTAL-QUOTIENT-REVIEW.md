# Exact-version review: horizontal constant-quotient exclusion

## Verdict and scope

**PASS.** The reviewed argument proves that the source tuple

    cf = (0,0,1,0,0,1,0,1)

is impossible for both original-zero-defect labels

    G3.11.863639aa192e, source index 69,
    A_q = O(-10) + O(4) + O(6),

    G3.11.73682b4c817f, source index 72,
    A_q = O(-10) + W O(5).

It also proves the stated independent exclusion of

    ce = (0,0,1,0,1,0,0,1)

for the split label, source index 69. The balanced ce exclusion cited as existing context is already a consequence of the pinned public polar obstruction. These are source-stratum exclusions only. Neither whole label, the remaining bf/bc/bb sources, nor the overall rank-three problem is excluded by this manuscript.

The delicate point passes: the projected image N is preserved by the actual regular trivial connection **as an image sheaf before saturation**. Its full generic rank alone is not used to infer saturation. The determinant-lattice lemma supplies that conclusion from differential preservation.

This is a mathematical audit of the exact text and its relevant public premises, not proof-assistant certification or an actual source-instance computation. No mathematical correction is required for the stated conclusions.

## 1. Reviewed version and public input pins

Reviewed manuscript:

    HORIZONTAL-CONSTANT-QUOTIENT-EXCLUSION.md
    SHA256 a637a5ba2c69b460bd2e058ea26100b4d2830e1b4f72fd823bae1dbba6e8701a

The conclusion of this review applies to that exact version.

The principal public dependency is PR814, commit

    1f94be65b3a470a1b594e61d56df7f6057c9d907

with proof SHA256

    f0bd13d85ae8a890dbec84e5f15b7ec8605b04f474d5c7d80faeb3aa08f4defc.

Public proof:
https://github.com/Akilleez-QA/read-em-and-weep/blob/1f94be65b3a470a1b594e61d56df7f6057c9d907/research/hm/profile11-low-positive/PROOF.md

The internal/external image argument is Section 3 of PR796, commit

    d2b43060c83328dd5118aee6b9288fcfa0c873ac.

Public proof:
https://github.com/Akilleez-QA/read-em-and-weep/blob/d2b43060c83328dd5118aee6b9288fcfa0c873ac/research/hm/profile12-quadratic-block-exclusion/PROOF.md

The inspected PR796 copy has Git blob hash

    46a0de762000f21182f6d3168f3ecfd63adaf75f.

The original inputs are fixed at commit

    db51525015bb7c5e825833d550d08dedf6f6ea96.

Directory:
https://github.com/Akilleez-QA/read-em-and-weep/tree/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load

Their inspected contents reproduce the following exact Git blob hashes recorded by PR814:

- ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md: b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3.
- NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md: d7506dae49b4be43230450c4132bd5db91f137ef.
- ONE-ONE-ENDPOINT-DEGREE-WINDOWS-AND-159-NECESSARY-PAIRS.md: dcacf0bcdef8377c1ed7654e5b82659ea409456e.
- one-one-endpoint-necessary-pairs.json: fe0afa410d89340d3082dc814277f89fbb582c19.
- rank-three-quotient-frontier-144.json: 8b5971092f9ef762584912609fd5e9301c4e271d.

The records at source indices 69 and 72 directly confirm the displayed A_q bundles, original defect zero, and the two tuples under discussion in their necessary source lists. In particular these are not positive-original-defect branches. No unpublished continuation, endpoint classification, or previous source-exclusion manuscript is needed.

All arguments below take place over C on P1, inside the same actual constant bundle H tensor O, with its regular trivial connection d and Omega^1 = O(-2).

## 2. Audit of the source and top-block premises

### 2.1 Correct decoding and the original saturated derivative

The original source formula specializes to

    cf: E = (V+P+D) O(-2) + V O(-4) + O(-8) + O(-10),
    ce: E = (V+2P) O(-2) + V O(-4) + Wp O(-5) + O(-10).

Both bundles have rank 17 and degree -54. The extra P in the ce top block is included. These are bundle decompositions, not horizontal decompositions.

Original defect zero identifies the derivative quotient A_q = E/E^- with the saturated subbundle B_q^*(-2) of (H O/E)(-2). Consequently its positive rank-two summand U is saturated there. The relevant U has degree 10 in both labels.

The top block F = H0(E(2)) O(-2) is saturated in E and in H O. Its ranks and degrees are

    cf: rank F = 12, degree F = -24;
    ce: rank F = 11, degree F = -22.

Strict-top vanishing H0(E^-(2)) = 0 gives the actual injection

    R = H0(E(2)) -> H0(U(2)) = V+2P+D.

### 2.2 The top maps are onto, not merely generically onto

For split cf, the V and D rows map nontrivially to the separate O(4) and O(6) summands. A common zero divisor of either row would be invariant and of degree at most 6 or 8, while every nonempty projective A5 orbit has at least 12 points. Thus each row is basepoint-free and F -> U is onto.

For split ce, the two source P multiplicities map isomorphically onto the two P multiplicities in H0(U(2)). After an invertible constant change of source multiplicity coordinates, there is one nonzero P system in each target row. The same invariant-divisor argument makes both rows basepoint-free.

For balanced cf, a saturated equivariant line L inside W O(5) has even degree at most 4 and h0(L(2)) at most 7. The injected 12-dimensional R cannot factor through such a line, so the top map has generic rank two. If its actual image S_top had a nonzero torsion quotient of length d in U, equivariance would give d at least 12. Since S_top(2) is a globally generated quotient of R O,

    h0(S_top(2)) = 2 + degree S_top(2) = 16-d <= 4,

contradicting the injection of R into this space. Thus the image is exactly U, with no divisor defect.

These arguments verify all top-map surjectivity needed by the reviewed manuscript. No selected map or parameter is required.

### 2.3 Relevant kernel lists and zero internal derivative

Let K0 = ker(F -> U). The cohomological budget H1(K0(2)) is P for cf and D for ce. Every splitting degree of K0 is at most -3.

For cf, a block below degree -3 contributing to the P budget can only be P O(-4) or Wp O(-5). This follows from the dimension bound (j-3) dim Z <= 4, central parity, and Wp tensor W = P. Matching the twist-three character T gives exactly

    T O(-3) + P O(-4),
    (Wp+T) O(-3) + Wp O(-5).

Their common rank and degree are 10 and -34.

For ce, the D budget permits only D O(-4) or O(-8). Matching the twist-three character Wp+T-S rules out the former, since it would require the nongenuine degree-minus-three coefficient Wp+T-S. The latter gives exactly

    K0 = (Wp+T) O(-3) + O(-8),

of rank 9 and degree -32.

The actual internal derivative is K0 -> (E/F)(-2). For cf all channels vanish by ordinary degrees: every K0 degree is at least -5, while all target degrees are at most -6. For ce only the O(-8) domain can raise a question. Its maps to V O(-6) and Wp O(-7) vanish equivariantly because V is absent from Sym^2 W and Wp is absent from W; its map to O(-12) vanishes by degree. Thus the internal image is zero in every relevant case.

The image lemma therefore gives the actual saturated exact sequence

    0 -> F -> F^+ -> U(2) -> 0,

and F^+ intersect E = F. It is legitimate to use the lemma for a rank-two external image: its proof is an exact-sequence argument about saturated subbundles and does not use the external image's rank-one specialization in PR796.

### 2.4 The constant parts and their full coefficient spans

First polars make F^+(1) globally generated, while F^+ is a subbundle of a trivial bundle. Hence its ordinary splitting degrees are 0 and -1. The resulting numerical data are

    cf: F^+ has rank 14, degree -10, constant part P O;
    ce: F^+ has rank 13, degree -8, constant part D O.

The constant parts are actual ambient constant sections, not abstract complements declared horizontal.

The public polar lemma projects F^+ along its actual constant part. The projected pure-linear bundle has generic derivative rank one: the projected image of F lies in its derivative kernel and has codimension at most one, while derivative rank zero would make the negative-degree saturated pure-linear bundle constant. Its first forward span is its full constant coefficient span. The standard evaluation-kernel conclusion therefore gives

    cf: Sym^9 W O(-1) in constant Sym^10 W;
    ce: Sym^7 W O(-1) in constant Sym^8 W.

This verifies the precise part of the polar conclusion used by the manuscript. For balanced ce, the same polar lemma would require a subbundle O(8) in W O(7), impossible by ordinary degrees, as cited in the scope statement.

Let C denote the full constant coefficient space of F^+, not merely H0(F^+). Projecting this space along the actual constant P or D gives exactly the full coefficient span of the projected pure-linear bundle. The kernel of this projection is exactly the P or D already contained in F^+. Thus

    cf: dim C = 4+11 = 15;
    ce: dim C = 5+9 = 14.

There is no assumption that F^+ splits horizontally. Because F^+ is saturated in H O, the quotient C O/F^+ is locally free: it embeds in H O/F^+. Its rank and degree are consequently

    cf: rank 1, degree 10;
    ce: rank 1, degree 8.

## 3. Audit of the horizontal-lattice lemma

Let N be a locally free coherent subsheaf of Q O, of full generic rank, and suppose

    dN subset N tensor Omega^1.

The ambient connection induces the determinant connection and preserves det N. At any point, the image of det N in det Q O is t^m O times a constant volume form, with m nonnegative. A local parameter t has dt as a local generator of Omega^1 on a smooth curve. If m is positive, differentiating the section t^m times that volume form gives

    m t^(m-1) dt times the same volume form,

which is not in t^m O tensor Omega^1 in characteristic zero. A unit multiplying an initial determinant generator causes no issue: the determinant image is the whole principal ideal t^m O, so t^m times the fixed volume form itself is a local section. Hence m is zero everywhere. The inclusion has invertible determinant and is an isomorphism.

This proves N = Q O without assuming N was saturated. The lemma uses the regular connection d, not merely stability under a logarithmic vector field such as t times partial/partial t. That distinction is essential and is respected in the application.

The use of characteristic zero is genuine. The argument is not a claim about arbitrary differential lattices in positive characteristic or meromorphic/logarithmic connections.

## 4. Removing O(-10): the exact forward transform of E'

Set

    E' = ker(E -> A_q -> O(-10)),
    K = E^-.

The composite to O(-10) is onto. All other source summands have larger ordinary degree and therefore admit no map to O(-10). Its restriction to the single O(-10) block is consequently an isomorphism. Thus, as bundles,

    rank E' = 16, degree E' = -44,
    E'/K = U,

    E'/F = N0 = V O(-4) + O(-8)                 in cf,
    E'/F = N0 = V O(-4) + Wp O(-5)              in ce.

The fact that F -> U is onto gives the exact sequence

    0 -> K0 -> K -> N0 -> 0.

All terms are genuine sheaves in the actual diagram; surjectivity K -> N0 follows by locally subtracting a lift in F of the U-image of a section of E'.

The manuscript's global-generation proof of Hom(K,O(-12)) = 0 is valid. K0(8) and N0(8) are globally generated and H1(K0(8)) = 0. Sections of N0(8) therefore lift to K(8), and together with sections of K0(8) generate every fiber of K(8). Every K degree is at least -8, giving the asserted Hom vanishing.

There is also a shorter check of the same vanishing: both Hom(N0,O(-12)) and Hom(K0,O(-12)) vanish by their displayed degrees; left exactness of Hom(-,O(-12)) applied to the exact sequence gives Hom(K,O(-12)) = 0 directly. Neither argument requires the extension to split horizontally, or even to split as the displayed extension.

Since K is the kernel of the original second fundamental form, dK lies in E tensor Omega^1. Projecting to (E/E') tensor Omega^1 gives an O-linear map

    K -> O(-12).

It is O-linear because the Leibniz term for a section of K lies in E' and disappears in this quotient. The map therefore vanishes.

Now write I for the actual image of the second fundamental form of E' in (H O/E') tensor Omega^1. Its external image in (H O/E) tensor Omega^1 is U, supplied surjectively by F. Its internal image, obtained from the kernel K of that external map, is zero by the preceding paragraph. Hence I -> U is an isomorphism of sheaves.

This image I is saturated. Indeed, for

    A = (E/E') tensor Omega^1,
    T = (H O/E') tensor Omega^1,
    B = (H O/E) tensor Omega^1,

the sequence 0 -> A -> T -> B -> 0 is exact, I intersect A = 0, and I maps isomorphically onto the saturated subbundle U in B. Thus

    0 -> A -> T/I -> B/U -> 0

is exact with locally free outer terms, and T/I is locally free.

Consequently

    (E')^+/E' = U(2),
    rank (E')^+ = 18, degree (E')^+ = -30.

Finally, equality of the forward span with E'+F^+ is genuinely sheaf-level. The image of F under the second fundamental form of E' surjects onto I, because its projection to U is onto and I -> U is an isomorphism. Thus F supplies every section of the raw derivative image of E' locally. The already-established raw-image saturation for F identifies its forward span with F^+, with no added divisor. It follows that

    (E')^+ = E'+F^+

as actual subsheaves of H O. This is stronger than equality at the generic point and justifies every later local derivative assertion.

## 5. The stable sum, its rank, and the exact intersection

Let S0 = E'+C O and let S be its saturation in H O. The preceding identity gives

    dE' subset (E'+F^+) tensor Omega^1.

Since F^+ is contained in C O and C O is constant, Leibniz's rule yields

    dS0 subset S0 tensor Omega^1.

This holds for arbitrary local sections of the sum, not merely for a chosen set of generic generators.

The saturation S is horizontal. For example, its second fundamental form vanishes on the dense open set on which S0 = S, hence vanishes identically as a morphism of locally free sheaves. A saturated horizontal subbundle of a trivial bundle in characteristic zero has constant Grassmannian classifying map, so S = H' O for a fixed vector space H' inside H.

The inclusion (E')^+ subset S0 and the rank-one quotient C O/F^+ show that rank S0 is 18 or 19. If it were 18, the quotient S0/(E')^+ would have rank zero and embed in the locally free H O/(E')^+, so it would vanish. Equivalently their saturations would agree. Then (E')^+ itself would be horizontal and constant, contradicting degree -30. Therefore dim H' = 19.

The generic dimension formula now gives

    rank(E' intersect C O) = 12 in cf,
    rank(E' intersect C O) = 11 in ce.

These are exactly the respective ranks of F. Since F is contained in the intersection, the quotient (E' intersect C O)/F has rank zero and embeds in the locally free E'/F. A rank-zero subsheaf of a locally free sheaf on this integral curve is zero. Thus

    E' intersect C O = F

as sheaves, not just generically. No saturation of a projected image is smuggled into this step.

## 6. The projected image is stable before saturation

Consider the constant quotient projection

    pi: H' O -> (H'/C) O.

Its restriction to E' has kernel F by the exact intersection just proved. Let N be its image sheaf. Then

    N = E'/F = N0

as locally free sheaves. Its rank equals the rank of the ambient constant quotient:

    cf: rank N = 4 = 19-15, degree N = -20;
    ce: rank N = 5 = 19-14, degree N = -22.

At this point N need not be presumed saturated, and the argument does not presume it.

Every local section n of the image sheaf N lifts locally to a section e of E'; this follows from the sheaf-surjective map E' -> N. Then

    dn = d(pi(e)) = pi(de),

because pi is a projection of constant bundles. The sheaf-level forward identity proved above gives

    de in (E'+F^+) tensor Omega^1.

Projection kills F^+ and maps E' onto N. Tensoring with the line bundle Omega^1 is exact. Consequently

    dn in N tensor Omega^1.

This verifies the exact hypothesis of the lattice lemma, including at points where the image could have had a divisor defect. Changing the local lift changes e by a section of F inside C O and hence does not change the projected derivative. No generic-only lifting or differentiation assertion is being used.

The lemma therefore forces N = (H'/C) O. This contradicts degree N = -20 in cf and degree N = -22 in ce. The two cf exclusions and the split-ce exclusion follow.

## 7. Independent numerical cross-check using the stable sum

The same determinant lemma offers a second check of the final contradiction, without identifying E' intersect C O.

After establishing S = H' O and rank S = 19, apply the lemma directly to the full-rank stable lattice S0 inside S. It forces S0 = S. Because (E')^+ is saturated in H O, the quotient S/(E')^+ is a line bundle of degree 30. The identity S0 = E'+C O, together with (E')^+ = E'+F^+, induces a surjection

    C O/F^+ -> S/(E')^+.

Both sides have rank one and are locally free. Such a surjection is an isomorphism, but their degrees would have to satisfy 10 = 30 for cf or 8 = 30 for ce. This reproduces exactly the degree discrepancies 20 and 22 found in the projected-image proof.

This is an audit cross-check, not an additional dependency or a required modification of the reviewed manuscript.

## 8. Boundaries and final assessment

- All ordinary degrees, ranks, and coefficient-space dimensions used above are forced formal bundle data, not selected-instance measurements.
- The proof uses the original actual connection throughout. No abstract splitting is treated as horizontal.
- No absence of global sections in E^+ is assumed. Such an interior-stage hypothesis would be inappropriate to import without proof here, and is unnecessary.
- The relevant original determinant defect is explicitly zero. No unstated condition on a later or dual endpoint defect is imposed.
- The projected image's possible nonsaturation is addressed rather than discarded: differential stability rules it out.
- No chosen source coefficients, parameters, points, derivative evaluations, matrices, source-instance ranks, searches over examples, or large computation occur in this review.
- The work consisted of reading the exact manuscripts and pinned input records, verifying content hashes, and checking universal sheaf, connection, representation, rank, and degree arguments. No external state was changed.

The manuscript is mathematically sound on its stated pinned public inputs. Its claimed source-stratum exclusions, and only those exclusions, are supported.
