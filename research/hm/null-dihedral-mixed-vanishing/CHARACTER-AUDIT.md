# Independent audit: the diagonal dihedral character of the pinned HM bundle

19 October 2026. Independent formal characteristic-zero representation and sheaf-cohomology audit of pinned sources; no new physical source or rank computation.

## Verdict

**Accepted, with explicit input dependency:** for the pinned normalized HM bundle H in the unscaled elementary-symmetric/binary-quartic coordinates, with the natural SL5 lift

    T(e_i)=ζ^(i−2)e_i,     R(e_i)=e_(4−i),

the representations H²(P4,End₀(H)(−2)) and H²(P4,End₀(H)(−3)) have no D5 invariants. The reflection trace at twist −2 is −4, not +4. The determinant factor in Serre duality is trivial for these particular lifts.

**Also accepted:** H²(P4,End₀(H)(−1)) has no D5 invariants; by equivariant Serre duality the same holds at twist −4. The additional ingredient is the five-dimensional H¹ at twist −1 and its nontrivial Heisenberg central character. No guessed reflection eigenvalue on H¹ is needed.

The ordinary cohomology ranks are an already published, independently corroborated input, not newly rerun here. I independently establish the vanishing of H⁰,H³,H⁴ at twists −1 and −2 below, and identify exactly the two rank inputs still imported from that certificate. This audit does **not** establish that the actual retained obstruction is invariant for this action, including all coefficient-line characters and source-naturalness comparisons. Target invariant vanishing is not by itself an obstruction-vanishing claim.

## 1. Actual coordinates and equivariant monad

The pinned carrier uses v_k=e_k(x₁,x₂,x₃,x₄), k=0,…,4, without binomial rescaling. Its monad columns are

    w_a⁺=e_(a+2)∧e_(a+3),    w_a⁻=e_(a+1)∧e_(a+4),

with indices modulo five, in

    U O(−1) → M ⊗ Λ²Q(−1) → U* O,

where dim U=5, M is the two-dimensional multiplicity space, Q=V/O(−1), and M is trivial for T and R. The last map is the alternating transpose of the first. Its pairing lands in det(V) O(−1), which is canonically O(−1) for the selected SL5 group, so the displayed U* really has no extra determinant character here.

For either sign label, direct ordered-wedge calculation gives

    R(w_a^±)=−w_(4−a)^±.

For example, the plus pair becomes (e_(2−a),e_(1−a)), the reverse of the plus pair for 4−a. Thus U_R=−R, not R. Both halves acquire the same minus, so M does not acquire a compensating sign. Under T, both w_a have eigenvalue ζ^(2a+1); these are all five fifth roots, and are compatible with R T R=T^−1.

The five-coordinate reversal has two transpositions, hence det R=+1 and trace R=1. Also det T=ζ^(−2−1+0+1+2)=1. For the binary-quartic action these are precisely the Sym⁴ images of diag(ζ²,ζ^−²) and [[0,i],[i,0]] in SL2: on x^(4−i)y^i the former has weight ζ^(8−4i)=ζ^(i−2), and the latter reverses the basis with scalar i⁴=1. A dual-coordinate convention replaces T by T^−1 and does not change any invariant calculation; it does not change R.

## 2. K-class signs and independent Euler calculation

The quotient Koszul sequence gives

    [Λ²Q(−1)]=[Λ²V O(−1)]−[V O(−2)]+[O(−3)].

Consequently

    [H]=2O(−3)−2V O(−2)+(2Λ²V−U)O(−1)−U*O.

These are signed K-class coefficients, not the dimensions of an ordinary four-term complex. At R, trace Λ²V=((trace V)²−trace(R²))/2=(1−5)/2=−2, trace U=trace U*=−1, so the four signed traces at degrees (−3,−2,−1,0) are

    c=(2,−2,−3,1).

For End(H)=H*⊗H the reflection coefficients are the autocorrelations

    a₀=18, a₁=−1, a₂=−8, a₃=2,

with a_−r=a_r. Dualization is legitimate here: R is an involution, so a representation and its dual have identical trace on R. There is no tensor-complex Koszul sign beyond the signed K-class coefficients already included.

The line-bundle Euler characters needed are

    χ_R O=1, χ_R O(1)=1, χ_R O(2)=3, χ_R O(−5)=1;
    χ_R O(k)=0 for −4≤k≤−1.

The O(2) value is (1²+5)/2=3. The O(−5) value is 1 because det R=1; its cohomology is in even degree four. Thus

    χ_R End(H)(−2)=a_−3+a₂+a₃=2−8+2=−4,
    χ_R End(H)(−1)=a₁+a₂+3a₃=−1−8+6=−3.

As a normalization cross-check, resolving the monad in the opposite direction yields signed traces (1,−3,−2,2) at line degrees (−1,0,1,2). Their autocorrelations are exactly the same, so neither the choice of Euler resolution nor an overall bundle twist changes this End calculation.

For every nonidentity T^j, the traces of V,U,U*,Λ²V are zero: the eigenvalues of V and U run through all fifth roots, and trace Λ²V=(trace(V)²−trace(T^(2j)))/2=0. The specialized K-character of H is therefore 2O(−3), and that of End(H) is 4O. Hence χ_(T^j)End(H)(−1)=χ_(T^j)End(H)(−2)=0. This is a virtual-character computation, not a claim of an isomorphism End(H)≅4O.

## 3. Cohomology concentration: what is independently proved and what is imported

The source-bound line complex is

    L^−1=5O(−1), L⁰=15O, L¹=10O(1), L²=2O(2),

whose only cohomology is the normalized HM bundle in degree zero in characteristic zero. Its maps are the pinned wedge/volume map, paired contraction, and paired evaluation. The source explicitly identifies this complex with the same monad by the Euler coresolution and cancellation of its constant surjection; the coefficients v_k are the unscaled elementary symmetric functions.

End(L)^r has line degree r and r ranges from −3 through 3. At twist −1, line cohomology survives only as H⁰ in internal degrees r=1,2,3. The finite complex is therefore

    245 → 400 → 150

in total degrees 1,2,3. There cannot be H⁰ or H⁴. The last differential is surjective without a rank computation: its restriction to postcomposition

    Hom(L^−1,L¹)(−1) → Hom(L^−1,L²)(−1)

is paired evaluation, taking arbitrary linear coefficients against all five coordinate variables to arbitrary quadratics, separately for each of the five source columns and the two target rows. Hence H³=0. The one imported rank is rank(245→400)=240, giving h¹=5 and h²=400−240−150=10.

At twist −2 the only surviving entries are H⁴(O(−5))¹⁰ in internal degree −3 and H⁰ in internal degrees 2,3. They give a transferred complex

    10 → 80 → 50

in total degrees 1,2,3. Again H⁰ and H⁴ are impossible. Postcomposition by paired evaluation maps the 50-dimensional constant-coefficient Hom(L^−1,L¹)(−2) subspace isomorphically onto the target linear polynomials, so H³=0 independently. The remaining imported rank is injectivity of the higher differential 10→80. The pinned certificate supplies an identity minor at rows 50,60,51,61,52,62,53,63,54,64 and an independent review corroborates it. This yields H¹=0 and H² of dimension 80−50−10=20.

Thus the Euler-to-H² step at twist −2 is justified, but crucially depends on that injective higher differential: retaining only the ordinary differential would be incorrect. This audit did not execute or reconstruct that physical matrix.

Over characteristic zero, trace splitting gives End(H)=O⊕End₀(H). O(t) is acyclic for t=−1,−2,−3,−4, so trace removal changes none of the cohomology groups used here, and in particular introduces no reflection sign.

## 4. Twenty-dimensional representation and duality

D5 has one identity, four nontrivial rotations, and five conjugate reflections. For M₂=H² End₀(H)(−2), the established character values are (20,0,−4), so

    dim M₂^D5=(20+4·0+5·(−4))/10=0.

More strongly, its C5-fixed subspace has dimension four and R acts on that subspace as −I. This also demonstrates why an untracked sign twist would matter: sign-twisting this representation would create four invariants. The sign cannot be discarded merely because the base projective involution is unchanged.

For projective space of lines P(V), ω=O(−5)⊗det(V)* equivariantly. End₀(H) is equivariantly self-dual via the trace pairing, without requiring a choice of self-duality of H. Since our D5 is inside SL(V), det(V)* is trivial. Therefore

    H² End₀(H)(−3) ≅ (H² End₀(H)(−2))*

as D5 representations, and both have no invariants. Replacing the selected lift R by −R would not be an innocuous step for odd twists or canonical-line identifications; the actual Sym⁴ SL2 lift fixes this ambiguity.

## 5. Ten-dimensional representation without guessing H¹ reflection

Let S(e_i)=e_(i+1). Together S,T generate the order-125 Heisenberg lift, with central fifth roots acting on V as scalars. The same ordered bivectors make the monad equivariant: S permutes their indices without an additional sign. A central scalar z acts on U as z², on O(−1) as z, and hence on every monad term and H as z³ (on U* it is z^−2=z³). It acts trivially on End(H) but as z on End(H)(−1).

Thus the five-dimensional H¹ End(H)(−1) has nontrivial Heisenberg central character. One can avoid invoking a classification theorem: if v is a T-eigenvector, its five translates under S have five distinct T-eigenvalues by the Heisenberg commutator. They span the entire five-dimensional space. Consequently its restriction to C5 is the regular representation and its C5 invariants have dimension one. In particular

    0≤dim(H¹)^D5≤1.

The invariant Euler characteristic computed above is

    χ^D5 End(H)(−1)=(5+5·(−3))/10=−1.

Only H¹ and H² survive, so, writing a=dim(H¹)^D5 and b=dim(H²)^D5,

    b−a=−1,    0≤a≤1,    b≥0.

It follows that a=1 and b=0. Equivariant Serre duality then gives vanishing of H² invariants at twist −4 as well. This proof checks the claimed refinement and does not assume an H¹ reflection eigenvalue.

## 6. Accepted scope and rejected shortcuts

- Accepted over characteristic zero with the explicitly selected natural SL5/SL2 linearisations and the two existing certified ordinary ranks.
- Not a claim that the normalized HM bundle is equivariant for all SL2; only the displayed finite diagonal subgroup is established.
- Not a proof that the actual source class or its weighted projections are D5-invariant. A coefficient line with the sign character would change the conclusion.
- Not a new characteristic-three result. Ordinary trace averaging over C is not by itself a characteristic-three multiplicity certificate; the field and geometric exactness must be separately stated.
- Not a new verification of the physical source, higher matrix, retained values, or reconstruction primitives. No such computation is claimed.

## Source binding

1. Actual coordinate and monad pin: https://github.com/Akilleez-QA/read-em-and-weep/blob/3bdc6cb28ecd75cfefb3cb0d85f42d5bcde8cc7f/research/hm-carrier-and-atlas.md (read).
2. Actual reduced line complex and its derivation: https://github.com/Akilleez-QA/read-em-and-weep/blob/add03476d9055aa00e1e00778eea6332cf8e01cc/research/hm/ext-model.md (read), with the first 30 lines of verify-hm-ext.js at that commit checked statically for the same wedge definitions and paired evaluation.
3. Exact small-rank statement: https://github.com/Akilleez-QA/read-em-and-weep/blob/f968b53943ba2312f09fbc3e8f9d462e86bcaa34/research/hm/d8-small-certificates/p4/Perfect-Complex-D8-F3.md and its certificate.json (read, not run).
4. Prior independent corroboration of the ranks: https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6130699166 (read). Its perfect-complex/positive-characteristic qualification was preserved rather than silently promoted.
5. Target weighted components and reconstruction scope: https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6277692474 and https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6279132359 (read).

The reflection signs, K-character arithmetic, total-degree vanishings, elementary Heisenberg argument, and determinant-line audit above are independent derivations, not copied from a representation table.
