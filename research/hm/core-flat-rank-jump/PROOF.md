# Flat universal core family with both top-obstruction alternatives

Work over C on T=P(W*) with G=2I and the inherited standard linearizations. This is a universal countermodel to deductions from the reduced core alone. No selected actual HM/source coefficient, point, parameter, jet, matrix, or instance rank is evaluated, and no claim is made that the universal parameter below is an actual HM parameter.

## Immutable inputs

INPUTS.json authenticates the exact original bytes.

CORE is PR1017 at 7cd8baebbec29ad21def1f8b30e19c707a87aed5, research/hm/rank-three-opposite-core/PROOF.md. It supplies the one-dimensional channels and the universal sextic evaluation sequence

    0 -> V O(-2) -> P O -> O(6) -> 0.

TOP is PR1020 at 547a224a95bc16aa6642158ed2b3fd2124e026ab, research/hm/core-top-obstruction-channel/PROOF.md. It proves that every nonzero universal channel

    u: W' O(-3) -> S O(1)

is a rank-two subbundle, with quotient W' O(5). The fixed identities used below are Sym^6 W=V+P, Sym^7 W=W'+T6, Sym^10 W=A+V+D, A⊗A=1+A+D, S⊗W=A+D, and W'⊗A=T6. BRANCHES, PR1009 at 0d75f42c4e79654c8fbef57e6ce56a1f06cdf9a1, research/hm/common-target-branches/PROOF.md, proves the universal contraction sequence; twisting its sequence (3) by O(2) gives

    0 -> W O(-1) -> S O(1) --tau--> W O(3) -> 0.             (1)

All nonempty G-orbits on T have cardinality at least twelve. G has no nontrivial one-dimensional representations. The total central action of all core source and target bundles is even.

## 1. Two saturated universal channels

Choose nonzero universal generators

    v: W' O(-3) -> A O(2),
    c: O(-8) -> S O(1).

The choice is only of fixed universal equivariant Hom lines, not of an actual HM block.

The map v has generic rank two. Otherwise its saturated image would be a G-linearized line O(e) in A O(2), so e<=2. Its nonzero source factor would require W' in Sym^(e+3)W, impossible in degrees at most five (and there are no sections for a negative degree). The maximal minors of v have degree ten. A common-zero divisor would be G-invariant of degree at most ten, which the orbit bound forbids. Thus v is a subbundle and its line quotient, by rank and degree, is O(12):

    0 -> W' O(-3) --v--> A O(2) -> O(12) -> 0.             (2)

The entries of c have degree nine. The same orbit argument makes c nowhere zero, hence a subbundle. Let B=coker(c), of rank three and degree twelve. B(-1) is globally generated, so its ordinary degrees are at least one.

We show they are all at least four. Equivariant Birkhoff splitting permits consideration of an irreducible multiplicity summand of smallest degree. If that degree is less than four, a rank-three irreducible atom would exhaust B and contradict degree twelve. Thus only rank-one or rank-two atoms need consideration. The even central action forces scalar lines to have even degree and rank-two W/W' atoms to have odd degree.

* A degree-two line quotient of B would give S O(1)->O(2), impossible because Hom_G(S,W)=0.
* A degree-one doublet quotient would give a representation map S->W or S->W', impossible.
* A W' O(3) quotient would give Hom_G(S,W'⊗A)=Hom_G(S,T6)=0.
* The only remaining possibility, W O(3), uses the unique channel tau in (1). But tau c is nonzero: if it were zero then c would factor through W O(-1), whereas Hom_G(O(-8),W O(-1))=Hom_G(W,Sym^7 W)=0.

Consequently all degrees of B are at least four, and their sum is twelve, so B=R O(4) for a rank-three representation R. Twist the sequence of c by O(-4). Its cohomology gives

    R = Sym^10 W - S⊗W = (A+V+D)-(A+D)=V.

We have proved

    0 -> O(-8) --c--> S O(1) --q--> V O(4) -> 0.           (3)

## 2. The family is saturated for every universal parameter

On T×A^1, let t be the coordinate of the auxiliary affine line, with trivial G-action, and define

    F_t: W' O(-3) + O(-8) -> S O(1) + A O(2),
    F_t(x,z) = (t u(x)+c(z), v(x)).                         (4)

At any fiber, F_t(x,z)=0 implies x=0 by injectivity of v, then z=0 by injectivity of c. Thus F is a rank-three subbundle on all of T×A^1. Its cokernel Q_univ is a vector bundle, hence flat over A^1; every fiber has rank four and degree twenty-four. This argument proves saturation simultaneously for every t and never evaluates a chosen HM instance.

Equations (2) and (3), or the pushout diagram, produce

    0 -> V O(4) -> Q_t -> O(12) -> 0.                     (5)

Its equivariant extension class is, up to a fixed sign convention, t times the connecting image delta(q u) for (2).

## 3. The family realizes exactly the two desired splitting types

The map q u is nonzero because u has generic rank two whereas ker(q)=im(c) has rank one. Moreover

    Hom_G(A O(2),V O(4)) = Hom_G(V,A⊗A) = 0.

The long exact equivariant Hom sequence of (2) therefore makes its connecting homomorphism injective on Hom_G(W' O(-3),V O(4)). In particular delta(q u) is nonzero. Equivariant Serre duality gives

    Ext_G^1(O(12),V O(4)) = H^1(V O(-8))^G,
    dim Ext_G^1(O(12),V O(4)) = [V:Sym^6 W] = 1.

The universal sextic evaluation sequence from CORE, twisted by O(6), is

    0 -> V O(4) -> P O(6) -> O(12) -> 0.                 (6)

It is nonsplit, since Hom(O(12),P O(6))=0. All nonzero classes in the one-dimensional equivariant extension space have isomorphic middle bundles, by scalar automorphisms of an endpoint. Hence

    Q_t = P O(6)                   for t != 0,
    Q_0 = V O(4) + O(12)           for t = 0.             (7)

Every fiber has all splitting degrees at least four. Thus positivity, the exact rank-three core, its precise four universal Hom channels, fiberwise injectivity, and flatness all persist through the jump.

## 4. The original reduced evaluation interface persists in the family

Set C_univ=O(2) plus Q_univ. Its fibers are ample and globally generated of rank5 and degree26, and have the split canonical quotient to O(2). Indeed all degrees in Q_t are at least four, so Hom(Q_t,O(2))=0 and Hom_G(C_t,O(2))=C, generated by this onto projection.

Let p:T×A^1→A^1 be the projection. For every fiber, H1(C_t)=H1(C_t(-1))=0. Cohomology and base change therefore make H=p_*C_univ and E=p_*C_univ(-1) locally free of ranks31 and26, respectively, with formation commuting with arbitrary base change. The resolution of the relative diagonal on T×T×A^1 gives the natural complete-evaluation exact sequence

    0→p*E⊗O(-1)→p*H→C_univ→0.                         (8)

Here O(d) is the pullback from T, and det W=1 fixes the equivariant diagonal convention. This is an induced evaluation map, not a matrix chosen to reproduce its cokernel. Exactness follows by pushing the diagonal resolution: the only possible higher direct-image terms are the two H1 groups just shown to vanish. Its quotient is a vector bundle, so the pencil injects on every fiber of the full product.

The fixed character identities at both splitting types in (7) are

    H0(C_t)=H31=1+3A+V+2P+2D,
    H0(C_t(-1))=E26=2W+W'+2S+2T6.                       (9)

Explicitly these are A+P⊗Sym6 W and W+P⊗Sym5 W when t≠0, and A+Sym12 W+V⊗D and W+Sym11 W+V⊗S when t=0. The bounded verifier checks both equalities exactly.

Since G acts trivially on the auxiliary base, the isotypic multiplicity bundles of E and H are vector bundles over A^1. They are free over C[t], so equivariant trivializations identify (8), after choices only of multiplicity bases, with

    0→E26 O(-1)→H31 O→C_univ→0

throughout the auxiliary family. Those trivializations are not canonical; the complete evaluation map and its quotient family are canonical. Thus the family preserves even the original reduced-pencil character and fiberwise-injectivity interface, rather than only the final rank-three ranks and degrees.

Finally dim H0(C_t(-12))^G is zero for t≠0 and one for t=0. This is the cohomological alternative which TOP identifies with the actual top obstruction. No actual incidence map sigma_t is assigned to these auxiliary bundles.

## 5. What this proves, and what it does not

In the core coordinates (a,b,c,d) associated to u,v,c and any fourth-channel generator, (4) has (a,b,c,d)=(t,1,1,0). Therefore the inherited W'-to-S block vanishes at the special fiber and is nonzero on every other fiber. The family genuinely realizes both Q types relevant to the top obstruction within saturated universal cores. In particular no theorem using only the reduced exact core, the complete-evaluation character interface, positivity, saturation, and deformation/flatness can force that block to vanish or survive. An actual-row selection needs further information about the actual map, or a genuine additional geometric condition not implied by those interfaces.

The explicit core and the canonical complete-evaluation pencil are constructed on the same auxiliary C_univ. We do not establish that this explicit core is obtained from that pencil by the precise historical complement choices and reduction maps of the actual HM construction. Compatibility with those historical maps is not part of the no-go scope; an additional condition expressing such compatibility could distinguish the actual object.

This does not construct an HM family, does not prove that both alternatives occur among actual HM objects, and does not change the actual-row or frontier ledger. The auxiliary t is not an actual HM coefficient evaluation. The contribution is a sharp missing-dependency result, not an assertion that arbitrary core data equal the actual retained map.
