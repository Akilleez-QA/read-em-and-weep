# The tensor-quartic subsystem forces a longer backward plateau

## Result and dependencies

The remaining maximal profile-(1,2) labels

    G3.12.37914c53373c,
    G3.12.eed6acb13f3e

are impossible. The obstruction is a generic rank inequality for the original constant connection: their backward kernel K=E^- has Gauss rank at least three, whereas maximal backward index one requires that rank to be less than three.

The first dependency is the reviewed quadratic-block exclusion in PR796, commit d2b43060c83328dd5118aee6b9288fcfa0c873ac:

https://github.com/Akilleez-QA/read-em-and-weep/blob/d2b43060c83328dd5118aee6b9288fcfa0c873ac/research/hm/profile12-quadratic-block-exclusion/PROOF.md

It reduces the source lists to entry6 for the first label and entries6,13 for the second. The second dependency is the tensor-quartic constant-subsystem and sheaf-intersection theorem:

PR797, commit cdee9396133fb96d4a91babba87b1a7a35903635:

https://github.com/Akilleez-QA/read-em-and-weep/blob/cdee9396133fb96d4a91babba87b1a7a35903635/research/hm/profile12-tensor-quartic-block/PROOF.md

Its reviewed proof SHA256 is 863bb17be118558b5c6199d0b3b73a7257cdd1f6871cdd903be2a19128574c98.

The maximal-plateau convention is the one in ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md at db51525015bb7c5e825833d550d08dedf6f6ea96, under research/hm/order-four-quadratic-load. In particular, the generic Gauss rank of E is three, and a maximal profile-(1,2) has generic Gauss rank(E^-)<3. If its rank were three, the same plateau would extend backward by another step.

Relative to PR796's cumulative baseline of 22 labels with profile counts 19/2/1, these two exclusions leave 20 with counts 19/0/1. The distinct source2 label of profile (2,1) is untouched. Neither SF>=4, square rank>=28, nor completion of the original goal follows.

Work is over C. All representations and bundle linearizations are those of the cited binary-icosahedral setup. No actual source coefficients, parameters, selected points, derivatives, matrices, ranks, or model experiments are evaluated. Generic-rank arguments below are universal deductions under the formal branch hypotheses.

## 1. Inputs from the tensor-quartic theorem

The relevant source types are

    E6  = (P+D) O(-2) + T O(-3) + O(-8) + O(-10),
    E13 = (P+D) O(-2) + T O(-3) + W O(-9).

Their original quotient A_q=E/E^- is respectively one of

    O(14)+O(-8)+O(-10),
    O(14)+W O(-9).

Put F=(P+D)O(-2). The cited theorem constructs an actual invariant constant fifteen-space C0 inside H and identifies

    C0=V tensor Sym4 W,
    F=V tensor U_2^4,
    F^+=V tensor U_3^4,
    (C0 O)/F^+=V O(4).

Here U_j^4 is the complete quartic osculating bundle. There is an everywhere-surjective equivariant quotient

    V O(4) -> O(18),                                    (1)

whose composite with C0 O is the quotient defining

    Zplus=E^+ intersect (C0 O).

The intersections in this proof are intersections of sheaves in H O, not unproved identifications with the full intersections of fibers. The theorem gives

    (C0 O)/Zplus=O(18),
    N=E intersect (C0 O)=Zplus^-,
    N/F=P O(-4),
    N=(P+D) O(-2)+P O(-4)

as bundles in the last equality. It also gives the locally free image sheaf

    E/N=Wp O(-1)+L,                                     (2)

where L is the corresponding high-negative part of E. Its injection into (H/C0)O is known generically fiberwise injective. We do not assume that this entire injection is saturated.

The original top-block map F->A_q is onto its O(14) summand. All maps from the displayed blocks of N to the negative part of A_q vanish by degree. Hence the image of N in A_q is exactly O(14), with no divisor defect.

## 2. Remove the mismatched source entry

Entry6 cannot occur for G3.12.eed6acb13f3e. The genuine quotient E6->A_q must be onto its W O(-9) component. Every summand of E6 except O(-10) has degree greater than -9 and therefore maps to that component by zero. The remaining line can have generic image rank at most one, not the required two. This is a contradiction.

Only the matching pairs remain:

    G3.12.37914c53373c with E6 and L=O(-8)+O(-10);
    G3.12.eed6acb13f3e with E13 and L=W O(-9).

In both, L equals the negative part A_q/O(14).

## 3. The projected backward kernel is exactly Wp O(-1)

Write K=ker(E->A_q)=E^-. Since N maps onto O(14), the quotient map induces a surjection

    E/N -> A_q/O(14)=L.

Using (2), its restriction to Wp O(-1) is zero by degree. Its restriction from the L summand is an everywhere-surjective endomorphism of L, hence an isomorphism. Equivalently, its determinant is a nonzero constant, since source and target degrees agree. Therefore its kernel is precisely the top subbundle Wp O(-1).

The kernel diagram, using the surjectivity N->O(14), gives

    0 -> K intersect N -> K -> Wp O(-1) -> 0.            (3)

Since K is contained in E, K intersect N equals K intersect (C0 O). Thus the actual projected image of K in (H/C0)O is exactly Wp O(-1). This conclusion does not require saturation of E/N.

Let pi:H O->(H/C0)O denote the constant projection and put Kbar=pi(K). The nonzero equivariant map

    Kbar=Wp O(-1) -> (H/C0)O

is classified by a constant intertwiner

    Wp tensor W=P -> H/C0.

The representation P is irreducible, so any nonzero intertwiner is injective. Consequently the map is a constant injection after the tautological inclusion

    Wp O(-1) -> Wp tensor (W O)=P O.

It is saturated and its Gauss rank is two: its first forward span is the constant P O, and its quotient there is Wp O(1). This is a universal tautological-bundle fact, not a measured rank of an instance.

## 4. The internal backward kernel contributes another rank

The map (1) is a basepoint-free three-section system of degree fourteen. The composite C0 O->O(18) is its product with the complete degree-four system. At an arbitrary point, choose one nonvanishing local degree-fourteen section from (1). Multiplication by that section is an isomorphism on local jet spaces. The complete degree-four sections generate jets of orders zero through four. Hence the composite system generates all jets through order four at every point. No point or coefficient is selected for evaluation in this argument.

For this system define J_i to be the kernel of the order-i principal-parts evaluation

    C0 O -> P^i(O(18)).

The jet generation just proved makes these kernels saturated through i=4. The first two are J_0=Zplus and J_1=N. Standard differentiation of the jet constraints gives

    J_i^- = J_(i+1)

through the needed range. More explicitly, differentiating a section which annihilates the first i+1 derivatives gives a section annihilating the first i derivatives. The resulting map

    J_i -> (J_(i-1)/J_i)(-2)

is onto when the next jet is generated. In particular J_2 has a nonzero rank-one derivative into J_1/J_2.

Because C0 is constant, differentiation in it is the restriction of the original connection on H O. The kernel of the derivative of N modulo E equals its kernel modulo N: the derivative lies in C0, and E intersect C0 is N as a sheaf. Therefore

    K intersect (C0 O)=N^-=J_2.                         (4)

There is no need to identify the full fiberwise intersection at exceptional points. The derivative of J_2 contributes a nonzero generic rank-one image in

    (N/J_2)(-2) subset (H O/K)(-2),                      (5)

since N intersect K=J_2. Jet generation through order three is already enough for this nonzero contribution; the stronger order-four generation was obtained uniformly above.

For reference, ranks and degrees are

    rank J_1=13, deg J_1=-34;
    rank J_2=12, deg J_2=-48;
    J_1/J_2=O(14).

These follow from the usual successive principal-parts quotients O(18), O(16), O(14). They are not needed to substitute for the derivative argument.

## 5. Independence of the two derivative contributions

Work at the generic point, where all relevant sheaf inclusions are inclusions of vector spaces. The constant projection pi induces the quotient map

    H/K -> (H/C0)/Kbar.

The composition of the second fundamental form of K with this quotient is the second fundamental form of Kbar composed with the surjection in (3). It has rank two by Section3.

On the kernel J_2 of that surjection, Section4 gives a nonzero rank-one derivative image. This image lies in the kernel of the displayed quotient because it is represented inside C0, and it is nonzero modulo K by (5). It is therefore independent of the projected rank-two image. Elementary rank additivity gives

    generic rank beta_K >= 2+1 = 3.                     (6)

This argument uses only generic vector-space quotients. It neither assumes a globally saturated sum K+C0 nor upgrades the entire projected E/N to a subbundle.

## 6. Maximality gives the contradiction

For a maximal profile-(1,2), the rank-three Gauss plateau extends backward exactly one step from E. Hence the Gauss rank of K=E^- must be strictly smaller than three. Equation (6) contradicts this requirement. If the rank were three, the plateau would extend one step further backward; a larger rank is also incompatible with the monotonicity of successive Gauss increments.

Thus both matching pairs are impossible. Together with Section2 and the exhaustive source lists in PR796, this excludes both remaining profile-(1,2) labels.

## Verification boundary

The contribution is a complete exclusion of the remaining maximal profile-(1,2) branch. The key new step is the independent internal rank-one and projected tautological rank-two contributions to the original backward kernel's derivative. The proof does not infer a connection on an abstract bundle splitting, does not assume global projection saturation, and does not use a selected source evaluation.

The result depends on the separately reviewed tensor-quartic/intersection theorem and the earlier exhaustive source reduction. It is a written deductive proof, not proof-assistant certification. The profile-(1,1) frontier, the source2 profile-(2,1) label, higher lifting, and algebraicity remain separate unresolved questions.
