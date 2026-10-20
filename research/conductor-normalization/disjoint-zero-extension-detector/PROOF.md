# Publication scope

This is a preserved theorem manuscript, with the exact hypotheses and held identifications listed in unit 08 INPUTS.md. Abstract geometry and formal conditional implications are distinct from identification with the actual HM module or retained source. Historical words such as “new,” “remaining,” or “previously verified” describe the source manuscript, not a claim about the current research frontier.

# Finite residue moments detect the surviving positive extension

## Setting and result

Work on W=P² over C. In the actual nonzero square-detector branch retain the actual sequence

    0 → O(a) → E → I_Z(−2−a) → 0,   a∈{0,1},

with E locally free, length(Z)=16 for a=0 and 19 for a=1. Assume Z is disjoint from the smooth conic C=(q=0). Put

    b=2a+2,   D_n=nC,   t_n=2n−b−3=2n−2a−5.

The actual inclusion restricts to a line subbundle on every D_n, with quotient O_Dn(−2−a). Its extension class is

    ξ_n ∈ H¹(D_n,O_Dn(b)).

There is one fixed, nondegenerate local-duality functional attached to the actual Serre extension,

    λ_e : H⁰(Z,O_Z(−b−3)) → C.

For every n its scalar moments on degree t_n plane forms give an exact criterion:

    ξ_n=0  ⇔  λ_e((p/q^n)|Z)=0 for every p∈H⁰(W,O(t_n)).       (1)

The quotient p/q^n has degree −b−3, so the expression is intrinsic and uses the invertibility of q|Z. Negative degree spaces of plane forms are zero. This is not a prescription to replace λ_e by an arbitrary functional: it is determined by the actual extension, including its inclusion and quotient identifications.

Using the imported actual-bundle vanishing H¹(E(u))=0 for u≥8, one obtains

    ξ_6 ≠ 0, and ξ_n ≠ 0 for every n≥6.                       (2)

Thus the first nonsplitting order is in [3,6] if a=0 and in [4,6] if a=1. All maximal-line lifting obstructions vanish in this branch; the bounded failure is entirely the positive extension class. No actual zero scheme, residue, HM entry, or selected rank is evaluated.

## 1. Defining the functional and proving the moments

Twist the actual sequence by a+2, giving 0→O(b)→E(a+2)→I_Z→0, and regard its class as

    e ∈ Ext¹_W(I_Z,O(b)).

Since H¹(O(b))=H²(O(b))=0, the ideal sequence gives an isomorphism

    Ext¹(I_Z,O(b)) ≅ Ext²(O_Z,O(b)).

Surface Serre duality identifies the latter space with H⁰(O_Z(−b−3))*; this is the local-duality functional, with a possible overall sign depending on the connecting-map convention. Local freeness of the middle term says its local Ext generator is a unit at each Artin local component of Z. Consequently λ_e is a Frobenius functional: after any trivialization of O_Z(−b−3), the pairing (x,y)↦λ_e(xy) is perfect on O_Z. This remains valid for nonreduced lci Z.

Here is a boundary-map proof of the precise dual restriction, including the sign. Set k=−b−3 and t=k+2n. Serre duality identifies the dual of restriction

    Ext¹(I_Z,O(b)) → Ext¹(I_Z,O_Dn(b))=H¹(O_Dn(b))

with the boundary δ_D in

    0 → I_Z(k) --q^n→ I_Z(t) → O_Dn(t) → 0.                 (3)

Indeed the two-term locally free resolution of O_Dn(b), followed by Hom(−,I_Z(−3)), gives exactly this boundary. On the source side the ideal boundary is an isomorphism

    δ_Z : H⁰(O_Z(k)) ≅ H¹(I_Z(k)),                         (4)

because k<0 and H¹(O(k))=0. Also every section of O_Dn(t) lifts uniquely to a plane form p: the divisor sequence has kernel O(k), with both H⁰ and H¹ zero.

With the Čech convention δf_ij=f_j−f_i, these boundaries satisfy the exact identity

    δ_D(p|D_n) = −δ_Z((p/q^n)|Z).                          (5)

To check it, choose local lifts f_i of p/q^n from Z to O(k). Then p−q^n f_i belongs to I_Z(t), lifts p|D_n, and its overlap difference divided by q^n is f_i−f_j. This proves (5), including its sign, without a rational-residue guess.

Specifically, if λ_e(s) is defined as the Serre pairing ⟨e,δ_Z(s)⟩, and the divisor-duality identification is the one in (3), then

    ⟨ξ_n,p|D_n⟩ = −λ_e((p/q^n)|Z).                        (6)

Defining the Ext² residue functional with the opposite connecting convention moves this common minus sign into λ_e. Criterion (1) is independent of either convention. The sign must be uniform across n; none of the following arguments depends on choosing it.

The divisor adjunction is normalized using the fixed equation q^n (and its two-term resolution). This fixes the scalar consistently at every order; no factor of n is introduced. The target duality can also be checked directly:

    ω_Dn=O_Dn(2n−3),
    H¹(O_Dn(b))*=H⁰(O_Dn(2n−b−3))=H⁰(W,O(t_n)).

In particular h¹(O_Dn(b)) is zero for t_n<0 and is binomial(t_n+2,2) otherwise.

## 2. Exact threshold and transition

Define the moment functional M_n(p)=λ_e((p/q^n)|Z). The transition is literally

    M_{n+1}(q p)=M_n(p).                                  (7)

Under Serre duality, restriction ξ_{n+1}↦ξ_n is dual to multiplication by q on plane forms. Consequently a nonzero class can never disappear at a higher level.

The first possible nonzero group is n=a+3, when t_n=1 and its dimension is 3. Hence the actual extension splits automatically through 2C for a=0 and through 3C for a=1.

For the new layer D_m⊂D_{m+1}, the ratio is the fixed plane restriction O_Dn(b), not an undetermined Picard lift. Every section of O_Dm(b) comes from P² and lifts to D_{m+1}; thus its connecting map δ_m is zero. There is an exact sequence

    0 → H¹(C,O_C(b−2m)) → H¹(D_{m+1},O(b))
      → H¹(D_m,O(b)) → 0,                                (8)

where the twists written inside O_C are plane twists. Its new-layer dimension is max(4m−2b−1,0). If ξ_m=0, the next obstruction is exactly the element in this kernel, with no quotient by an unknown image of a connecting map. Dually, the new moments are tested on

    H⁰(O(t_{m+1})) / q H⁰(O(t_m)).                        (9)

When ξ_m=0, M_{m+1} descends to this quotient. These formulas give the finite mechanism that survives after all negative-root obstructions have vanished.

## 3. Evaluation-rank and Hilbert-function exclusions

Let ev_t:H⁰(O(t))→H⁰(O_Z(t)) be evaluation. Multiplication by q^(−n) identifies the degree-t_n target with H⁰(O_Z(−b−3)). Thus if ev_tn is surjective, λ_e≠0 immediately implies ξ_n≠0.

A weaker numerical test can be useful before evaluation is surjective. Write h_Z(r)=rank(ev_r), with r≥0. If ξ_n=0 and 0≤r≤t_n, then the Frobenius pairing makes the evaluation images in degrees r and t_n−r orthogonal. Therefore

    h_Z(r)+h_Z(t_n−r) ≤ length(Z).                        (10)

To formulate the pairing as a pairing of ordinary vector spaces, choose a linear form nonvanishing on the finite support of Z and use its powers to trivialize all twists. The weight from q^(−n) is a unit, so the pairing remains perfect. Products of the two evaluation images are restrictions of degree-t_n forms; (1) makes their pairings zero. This proves (10), including for nonreduced Z. Its contrapositive is a finite degree/rank exclusion; it does not assert an unevaluated Hilbert function.

## 4. Uniform bound for the actual bundle

The imported global theorem establishes H¹(E(u))=0 for u≥8. Twist the actual Serre sequence by u:

    0 → O(a+u) → E(u) → I_Z(u−2−a) → 0.

For u≥8, H²(O(a+u))=0, so

    H¹(I_Z(k))=0 for k≥6−a.                              (11)

The ideal sequence then says ev_k is surjective for every k≥6−a. At n=6,

    a=0: t_6=7≥6, rank(ev_7)=16, dim H⁰(O(7))=36;
    a=1: t_6=5=5, rank(ev_5)=19, dim H⁰(O(5))=21.

The nonzero Frobenius functional cannot annihilate either whole evaluation image. Hence ξ_6≠0. This proof supplies the rank of the evaluation maps from cohomology, not an actual HM/source computation.

For clarity, the first possibly nonzero orders are 3 and 4, respectively, but the moment test may vanish at some of those earlier orders. Nothing here selects the first nonzero moment or the actual first nonsplitting order.

## 5. Why nonsplitting means nonsplitting of the bundle

On C the actual sequence splits because H¹(C,O_C(b))=0. The positive summand O_C(a) has strictly greater P¹-degree than the other summand O_C(−2−a), and is the intrinsic maximal line. It has the actual compatible subbundle O_Dn(a) at every order. Embedded lifts of this maximal line are unique: their difference space at order m is

    H⁰(C,O_C(−b−2m))=0.

Any decomposition of E|D_n into two lines must contain the unique lifted maximal line, hence would split the actual sequence. Thus ξ_n≠0 excludes every line-bundle decomposition, not only one chosen complement. The existence of the global subbundle near C explains why every negative-root line obstruction is zero while the positive-root moments still force nonsplitting.

## Dependencies and scope

The line, lengths, and lci property are from prerequisite square-detector-factorization, document PROOF.md. (see the unit INPUTS.md) The actual-bundle cohomology bound is from prerequisite global-conic-splitting-exclusion, document PROOF.md (see the unit INPUTS.md), §2. The interpretation of the positive versus negative layers agrees with prerequisite higher-conic-lifting-obstruction, document PROOF.md (see the unit INPUTS.md), but here the ratio line is specified globally, so δ_m=0. Only local proof artifacts are written. No external mutation, actual source or HM evaluation, large computation, or local Codex task is used.
