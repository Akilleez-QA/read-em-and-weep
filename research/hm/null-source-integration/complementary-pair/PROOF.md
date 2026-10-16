# Complementary-pair transfer on a fixed ordered source triple

## Result and scope

The finite whole-source construction at PR85 commit `82a8785d0a23e8d4e44e9ca4f52c8bb24fdadbdc` transfers from pair (0,1), called F12, to pair (2,3), called F34, by the coordinate involution σ=(0 2)(1 3). The transfer preserves the ordered triple, ordered matrix multiplication, sign, carrier IDs, and denominator occurrence identities. It permutes legal masks, standard tags, derivative coordinates, and multidegrees. In particular the carrier ledger is still (5,6,5), and the uniform polynomial degree bound is (210,210,217,217).

This is a theorem about a raw formula on any fixed ordered triple. It does NOT identify the source-first alternating F34 cochain with the coordinate rename of the source-first alternating F12 cochain. The necessary cover-order bridge is stated below. No physical polynomial expansion/evaluation, historical source checker, source coefficient, or obstruction value is supplied. The homogeneous geometric identification and actual standard B coefficient realization are separate obligations.

## 1. Inspected pins

Repository: https://github.com/Akilleez-QA/read-em-and-weep

At commit 82a8785d0a23e8d4e44e9ca4f52c8bb24fdadbdc:
- research/codex-swarm/whole-source-clearing/PROOF.md, Git blob 806fa33f3492aac3f89431b46c9b493c0945751b.
- research/codex-swarm/whole-source-clearing/clearing.py (see source-pins.json for fetched blob).

Its underlying source is pinned to 10810ee877fdaf291399198ad60d7dd0c316a42d:
- research/hm/null-operator-compiler/hm-pinned-source-formulas.js, Git blob 3dfed53a28b53b3c912a097971d89fc547330a5f, SHA256 c4f65ff831092d0e56b3e33a0357f44182169fda45943ea780c8c551b4023f94.
- The finite construction authenticates the model at SHA256 635bb12d9986e0dcada161d4173c773c4f134b9225354a3bc74267840ca19926. This transfer imports its primitive polynomial identities and bounds; it does not rerun that authentication or the historical checker.

The source excerpt's build2 forms elementary symmetric coefficients e_k from the four x variables. globalBuild2 sets q(i,j,a)=(mask_j[a]-mask_i[a])/x_a and bcoef(i,j,k,a,b)=(15/4)q(i,j,a)q(j,k,b). crossResidual defines μ(F,G,a,b)=(∂a F ∂b G-∂b F ∂a G)/2, with F on the later edge and G on the earlier edge. The finite construction uses precisely this orientation and its additional trace factor 1/2. Reading these expressions is sufficient to check orientation; none is executed here.

## 2. Exact renaming map

Use zero-based coordinate indices. Write σ=(2,3,0,1). Let Rσ be substitution x_i↦x_σ(i), and, for homogeneous coordinates and stripped deck symbols, (X_i,Y_i,y_i)↦(X_σ(i),Y_σ(i),y_σ(i)). For a fixed mask vector m, the corresponding relabelled mask is m'_j=m_σ(j), since σ is its own inverse. Thus Rσ f_m(x)=f_{m'}(x) whenever f is built coordinatewise by the displayed source operations.

Legal masks use low bits: m'_int=sum_i bit_i(m) 2^σ(i). Standard tags use high bits: e'_int=sum_i bit_(3-i)(e) 2^(3-σ(i)). Both happen to rotate the two-bit halves for this σ, but the encodings are defined separately and must not be conflated for other permutations.

A complete owner (seed, occurrence, carrier, mask, standard_tag) maps to (seed, occurrence, carrier, σmask, σtag). The seed is a provenance label, not a detector-symmetry claim. Source slots a,b,c stay in that order. Neither occurrences nor carriers are sorted or merged. Distinct owners remain distinct, even if their polynomial factors agree. Derivative index i maps to σ(i). Exponent and multidegree vectors map by d'_j=d_σ(j). A pair is ordered: (0,1)↦(2,3), with no reversal and no pair-orientation minus sign.

The fixed coefficients v_k=e_k(x0,x1,x2,x3), v0=1, are invariant under σ: the permutation bijects k-element subsets. Therefore every rational matrix with coefficients in the v_k, including each I_c and P_c in the pinned catalog, is invariant. No permutation of matrix rows, columns, or carrier IDs is needed. In particular

    H_c=v_c^5-product(v0,...,v4), c=0,...,4;
    H_5=v1*v3*v4

are individually invariant in the finite chart v0=1. The homogeneous auxiliary equation is v0*v1*v3*v4, of multidegree (4,4,4,4); its finite restriction is the displayed H5. The homogeneous primary equations have multidegree (5,5,5,5). Their assigned homogeneous degrees 5 and 4 are therefore unchanged. The omitted finite-chart v0 factor must be restored for the homogeneous owner equation. This is a symbolic symmetric-coefficient argument, not an expansion of their x-polynomials.

For finite legal factors ell_(v,i)=1 for mask bit0 and x_i(x_i²-1) for bit1, Rσ ell_(v,i)=ell_(σv,σi). Their homogenizations are Y_i and X_i(X_i²-Y_i²), so the same identity holds homogeneously. The frame monomial product_(i:e_i=1) x_i^n_i transports to the identical product with e,n permuted. This verifies the formal frame-renaming rule only; it does not certify that a particular physical representative has that frame.

## 3. Ordered-triple theorem and proof

For any ordered source triple u=(u0,u1,u2), without sorting, put

    K_ab=(P_(carrier a) I_(carrier b))^t,
    Q_a,i = m_a,i (x_i²+1)/(2 x_i(x_i²-1)) diag(1,-1),
    T_ab,i = ∂i K_ab + Q_b,i K_ab - K_ab Q_a,i,
    q_ab,i = (m_b,i-m_a,i)/x_i.

The underlying contraction identity K02^-1=K20 is imported from the pinned finite construction. For an ordered coordinate pair (i,j), define

    Fraw_(i,j)(u) = (15/4) q01,i q12,j
                  - (1/4) tr[K20 (T12,i T01,j - T12,j T01,i)].       (1)

Then, exactly in the rational function field,

    Rσ Fraw_(0,1)(u) = Fraw_(2,3)(σu0,σu1,σu2).                    (2)

Proof. Substitution is a ring automorphism, commutes with transpose and trace, and obeys Rσ ∂i=∂σ(i) Rσ. Symmetric coefficients fix K. Coordinatewise mask transport gives Rσ Q_a,i=Q_σa,σi and the identical q relation. Consequently the same relation holds for T. Substitute in (1), keeping every product in its original order. The gerbe becomes +(15/4)q01,2 q12,3. The trace becomes -(1/4)tr[K20(T12,2 T01,3-T12,3 T01,2)]. Neither the μ edge ordering B,A nor either scalar factor 1/2 changes. No commutation of matrix factors and no tuple permutation is used. The stripped character y0*y1 maps to y2*y3; this operation contributes no sign.

The hypothesis is not that u was increasing. Formula (1) is a well-defined raw rational expression for every ordered triple. The finite clearing proof uses only endpoint identities, binary masks, and source-slot counts, not inequalities between owner labels. Therefore its finite identity and degree proof apply to arbitrary ordered u. This extension of the algebra's domain must not be described as alternating extension of the nonlinear formula.

## 4. Cleared numerator, degree and ownership

For pair p define C_a^p=H_a^14 product_(i in p)ell_a,i. Let P12(u)=C0^(0,1) C1^(0,1) C2^(0,1) Fraw_(0,1)(u), using the pinned actual finite polynomial identity. Then define P34(σu)=Rσ P12(u). Equation (2) proves

    P34(σu)=C0^(2,3) C1^(2,3) C2^(2,3) Fraw_(2,3)(σu).             (3)

This constructs a polynomial numerator without evaluating it. K20 contributes carrier exponents (2,0,2); the two tangents contribute (0,3,3) and (3,3,0). Their sum is (5,6,5). The middle slot is still the middle slot after σ. The gerbe fits this same common denominator. Each derivative uses a distinct pair coordinate, so each pair-legal factor has exponent at most one per owner. Padding to carrier14 remains H0^9 H1^8 H2^9. Those H subscripts identify slots, not carrier IDs.

For each tuple the homogenization target is

    D_i^p = 14 sum_(a=0..2) d_a
            + 1_(i in p)(sum_(a=0..2) deg_hom ell_a,i - 2).         (4)

It transports by σ. Thus the uniform bound (217,217,210,210) becomes (210,210,217,217). The imported leading-weight cancellation proving 217 rather than 218 transports too: all carriers1..4 and all three bits1 in coordinate i maps to exactly the same critical condition in σi; rf_i=1/(2x_i)+O(x_i^-3) transports to rf_σi, and the cancellation ∂K-(r-s)K/x is unchanged. Exceptional-carrier counts, zero-bit counts, and the slack inequality 1-12 count(c0)-10 count(c5)-count(bit0) are preserved.

Since σ is bijective on labels, arbitrary increasing target triples have ordered inverse images. Hence (3) and (4) establish the finite polynomial/degree property for freshly evaluated F34 on every source-first increasing triple, even when that inverse image is not increasing. This is a universal local construction/property transfer, not equality of two alternating cochains or their sums. No full-cover coefficient or value follows.

The homogeneous formal candidate obtained by homogenizing (3) at (4) is the renaming of the F12 candidate. Conditional on an authenticated physical homogeneous-frame identification compatible with this coordinate renaming, it gives the corresponding homogeneous source identity. That physical identification remains outside this artifact, as does actual complete B coefficient realization.

## 5. The source-order boundary

Let O order vertices by (auxiliary-first carrier rank, numeric low-bit mask, standard tag), and define the cochain F^O by evaluating (1) on O-increasing triples and extending alternatingly. Define Oσ as the transported order: σu <_(Oσ) σv iff u <_O v. Equation (2) yields an exact cochain identity between F12^O and F34^(Oσ) after renaming coordinates and labels. It does not identify F34^(Oσ) with F34^O.

Indeed, within one carrier block, masks 1<4 map to 4>1. On the increasing same-carrier triple (1,2,4), mapped masks are (4,8,1), so a fresh O evaluation sorts them differently. If ρ is the permutation sorting a mapped triple w into O order, the already-defined cochain is

    F34^O(w)=sign(ρ) Fraw34(w_ρ0,w_ρ1,w_ρ2),

whereas the transfer proves equality with Fraw34(w0,w1,w2). Their equality requires a separate identity for that raw nonlinear source. Alternating extension alone supplies no such identity. Coordinate permutation has not supplied a vertex-reordering sign; inserting one by hand is invalid.

One may safely transfer the polynomial property to F34^O by the arbitrary-ordered-triple argument in section 4, with ledger (5,6,5) attached to the actually evaluated increasing triple's slots. One may not attach that ledger to unsorted occurrences after re-evaluation without recording the vertex permutation. The inverse-image formula and the newly sorted formula can have different middle owners.

For an equality of full-cover values a sufficient additional bridge must identify the order-rebuilt sources in the admitted domain, and transport partitions, tags, chain maps, orientations, weights, and terminal functionals consistently. A cohomological bridge may suffice for a complete closed detector, but is not automatically a seedwise equality. This artifact claims none of these absent comparisons and changes no admission/value flag.

## Replay and controls

Run `python -m unittest discover -s . -v`. The independent abstract controls use only label bijections, ordered expression trees, subsets representing elementary coefficients, integer owner/degree bookkeeping, and artificial matrix symbols. They neither import nor execute the copied source files. They check involution, both bit encodings, derivative/gerbe/μ orientation, no matrix product reversal, carrier invariance, finite and homogeneous legal equations, arbitrary tuple ordering, degree bounds, and a negative source-order control. Passing controls supports this theorem's algebra and mapping; it does not discharge physical frame, B, source-order, or evaluation obligations.
