# The residual simultaneous image has a unique stationary graph

## Statement and boundary

Retain all actual-geometric hypotheses and conclusions of PR1222, including its complete transitive assumptions. In its residual simultaneous rank-seven k=2 case, use the unique actual quotient splitting

    B6/U4=A8 direct-sum R,
    A8=U5/U4=O(-8), R=W'(-3),
    L=G6/U4=O(-10) subset R,
    C4=R/L=O(4).

It induces the actual splitting

    B6/G6=A8 direct-sum C4.                              (1)

This is the splitting adapted to U5/U4, not the earlier one adapted to F6/G6. Both actual lines F6/G6 and B7/G6 project isomorphically onto A8. Write them as graphs of the actual morphisms

    phi, psi:A8 -> C4, respectively.                     (2)

Then

    phi = -(1/2) psi.                                   (3)

This is an equality of actual bundle maps in the specified splitting, not an evaluation or normalization of either graph scalar. It identifies the previously undetermined embedded graph from the original jet flag and the symmetric pairing.

More precisely, once both graphs in (2) vanish on D12, the first-order condition

    beta_(F6)|D12=0                                      (4)

is equivalent to (3). The sufficiency direction states only fiberwise vanishing of the intrinsic derivative on the reduced divisor, or at least simple coherent divisibility by that divisor. It does not prove the exact image I6=E6(-D12), generic rank, higher vanishing, or realization of the original branch. In the retained simultaneous case (4) is already known, so (3) is a necessary new embedded compatibility condition. Since psi is nonzero, (3) is consistent with phi nonzero and phi!=psi; it gives no branch exclusion.

No actual source coefficient, parameter, point, jet, tensor, matrix, instance rank, or invariant normalization is selected or evaluated. All derivatives below are formal local identities of the actual bundles, applied along the entire divisor. No quotient is given a connection, and no bundle splitting is asserted horizontal. No original tenth jet, algebraicity, occurrence, or whole-profile conclusion is claimed.

## 1. Complete immutable input and retained actual geometry

The sole direct input is the complete proof of PR1222 at

    f7abba83fedd46a9d91f5abbd9e40d3b02ae65f1,
    research/hm/rankfour-profile11-triplet-nonsplit-quotient/PROOF.md.

INPUTS.json records its freshly fetched full UTF8 bytes, SHA256 and Git blob. Its actual-geometric and transitive hypotheses remain assumptions, not newly verified premises.

We work over C on the physical binary-icosahedral line. The original jets Tj of the degree-eighteen curve in V O are globally separated through order nine, and

    Tj=Symj W(j-18), Bj=ann(Tj) subset V* O.

The actual constant nondegenerate symmetric map h:V->V* gives auxiliary jets Uj=h(Tj). We use only the orders through seven below. The norm on the saturated line T6/T5=O(-6) is a nonzero multiple of the fixed universal invariant f12, with reduced divisor D12. The pairings of original jets of total order at most eleven are zero.

In particular U4 lies in B7, U5 lies in B6, and

    G6=F6 intersect B7=U4 direct-sum L10,
    F6/G6=O(-8), B6/F6=O(4),
    rank B6=8, deg B6=-84,
    rank B7=7, deg B7=-88,
    rank G6=6, deg G6=-80.                              (5)

All these are actual saturated subbundles in the same constant V* O. The actual splitting (1), its factors and the given embedding L subset R are those established in PR1222. No canonical-degree-ten-line completeness result is needed here.

For use in the derivative argument, the original jet flag gives

    B6^-=B7,
    derivatives of B7 lie in B6,
    B6/B7=O(4).                                         (6)

These also follow directly by differentiating the annihilation identities: a local section of B6 whose derivative still annihilates T6 must annihilate the successive actual span T7; a section annihilating T7 has derivative annihilating T6. Consequently the second fundamental form of B7 has its actual normal direction in

    (B6/B7)(-2)=O(2).                                   (7)

We use (6)-(7) as actual inclusions and kernels, not as a connection on a quotient.

## 2. The two actual graph maps and their zero divisors

PR1222 proves that F6/G6 is the graph of a nonzero map phi in (1), with divisor D12. The same graph description holds for B7/G6, as follows.

The latter is a saturated line of degree -8 in B6/G6. Its projection to A8 is a scalar. If zero, its only possible nonzero component would be a degree-twelve section O(-8)->O(4); such a section must have zeros and cannot be a subbundle inclusion. Hence the projection to A8 is an isomorphism, giving the actual graph psi.

The quotient map B6/G6 -> B6/B7 restricts to an everywhere isomorphism

    C4 -> B6/B7.                                        (8)

Indeed the kernel is the graph of psi over A8, and its intersection with the complementary C4 is zero. Both lines have degree four, and the graph description identifies the quotient explicitly with C4. This is an actual isomorphism, not only a generic nonzero map.

To identify the zero divisor of psi and prepare the first-order calculation, use any formal affine coordinate t and any local lift v(t) of the original scalar curve. Put

    u_i=h(v^(i)), p_ij=<v^(i),h(v^(j))>, s=p_66.        (9)

All statements are identities of local sections; no value of t is selected. Since the jet maps are saturated, u_5 modulo U4 generates A8 locally, and v^(7) modulo T6 generates T7/T6. The local scalar s represents the norm of T6/T5 and has precisely the reduced divisor D12 in this trivialization.

Symmetry of h and the vanishing p_56=0 give the exact formal identities

    p_57=-s,  p_67=(1/2)s'.                            (10)

The first follows by differentiating p_56: its derivative is p_66+p_57. The second follows by differentiating p_66 and using p_76=p_67. These are universal identities in characteristic zero, not calculated values of actual jets.

Choose a local frame c of C4, lift it locally through the actual R summand to E=B6/U4, and lift further to a section r of B6. Let

    rho=<r,v^(7)>.

The isomorphism (8) implies that rho is a unit in these local trivializations. Adding a section of U4 to r does not change rho, because U4 annihilates T7. Write psi(u_5 mod U4)=b(t)c. The section u_5+b r belongs to B7 modulo, and hence also after adding, U4. Pairing it with v^(7) gives

    -s+b rho=0,  hence b rho=s.                        (11)

Thus psi is nonzero and has precisely the same simple zero divisor D12. In particular both graphs in (2) become the same A8 summand on D12, so

    F6|D12=B7|D12                                       (12)

as actual subbundles of the restricted constant ambient. Globally the two graphs are distinct, since the sheaf intersection F6 intersect B7 is exactly G6. This sheaf intersection does not commute with taking fibers here: on D12 the two rank-seven fibers coincide, while G6 has rank six.

## 3. All generators except one already satisfy the required condition

Let a(t)c=phi(u_5 mod U4). Locally the actual F6 is generated by U4, a local generator of L10, and

    sigma=u_5+a r.                                     (13)

These seven generators have the expected ranks: U4 has rank five, L10 adds one, and (13) maps to a generator of F6/G6.

Before testing the final normal direction, first note that derivatives of every section of F6 lie in B6 along D12. This follows from (12) and the equality B6^-=B7: the actual second fundamental form of B6 vanishes on the fibers B7, hence on F6|D12. Therefore checking that such a derivative remains in F6|D12 is equivalent, by (12), to its having zero image in B6/B7 along D12. Pairing with v^(7) tests precisely that final one-dimensional normal quotient by (8).

For the five U4 generators, derivatives lie in the actual U5. On D12, phi=0 and the F6 graph is A8, so U5|D12 is contained in F6|D12. These derivatives satisfy (4).

For the L10 generator, derivatives lie in B6 by (6). Its remaining projection is the actual restriction

    beta_(B7)|L10:O(-10) -> O(2).

It is equivariant, so its degree-twelve scalar section is either zero or a multiple of f12, since (Sym12 W)^G is one-dimensional. It therefore vanishes on D12. Thus the L10 derivative also lies in F6|D12. This argument does not assert that beta_(B7)|L10 is nonzero, nor use completeness of the degree-ten coefficient span.

It remains only to test the generator sigma in (13). The preceding arguments check every other generator of F6, not merely a selected vector.

## 4. The remaining normal equation is the differential of phi+psi/2

Differentiate (13) in the constant ambient and pair with v^(7). Using the formal identities (10), one obtains modulo the ideal of D12

    <sigma',v^(7)>
      = p_67+a' rho+a<r',v^(7)>
      = (1/2)s'+a' rho,                                (14)

because a vanishes on D12. Differentiating (11) and reducing modulo the same ideal gives

    s'=b' rho,                                         (15)

since b also vanishes there. Combining (14)-(15) yields

    <sigma',v^(7)> = rho (a'+b'/2) modulo D12.          (16)

The comparison factor rho is a unit. By Section 3 the derivative is already in B6 along D12, and pairing with v^(7) is its entire remaining normal component. Equations (13)-(16) therefore prove the all-generator equivalence

    beta_(F6)|D12=0
      iff the first normal derivative of phi+psi/2
          vanishes along D12.                          (17)

The phrase "first normal derivative" in (17) means the canonical first-order class of a section that already vanishes on a Cartier divisor. It does not assign a connection to Hom(A8,C4) or to any quotient.

## 5. Frame independence and passage to the global equality

Set eta=phi+psi/2, a section of Hom(A8,C4)=O(12). Both summands vanish on D12. Thus eta has a well-defined leading class

    eta mod I_D^2 in I_D/I_D^2 tensor Hom(A8,C4)|D12,

where I_D is the ideal of the reduced divisor. Because D12 is reduced on a smooth characteristic-zero curve, the differential of a local equation is nonzero in its conormal line. The vanishing of the local differential in (17) is therefore exactly the invariant statement eta lies in I_D^2 Hom(A8,C4).

All possible local choices leave this statement unchanged:

* Replacing a local frame multiplies the coefficients of a section vanishing on D12 by a unit. Its differential modulo D12 is multiplied by the same unit; terms differentiating the unit contain the vanishing section.
* Changing the formal coordinate multiplies the first differential by an invertible coordinate derivative.
* Replacing r by another lift from R changes it by L10 or U4. In sigma this change is multiplied by a, which vanishes on D12; differentiating the product contributes a' times a vector already in F6. The remaining normal component is unchanged. The identity (8) also makes the quotient comparison intrinsic.
* A different lift of a generator modulo U4 changes sigma by a section of U4, whose derivative has already been checked in Section 3.

Thus (17) is independent of lift, coordinate and frame. No actual scalar has been normalized.

Now a section eta vanishing twice on D12 would belong to

    H0(Hom(A8,C4)(-2D12))=H0(O(12-24))=0.              (18)

Hence (17) implies eta=0 globally, which is exactly (3). Conversely, eta=0 makes (16) zero, and the complete generator check in Section 3 proves (4). This proves the stated equivalence, with only the first-order scope specified there.

Finally rescaling h by any nonzero constant does not change the subbundles Uj, A8, R, L, or the unique actual splitting (1). It therefore does not change phi or psi as bundle morphisms. In the local formulas it rescales u_5, s and the corresponding coefficient functions consistently, multiplying (11) and (16) by the same unit. Thus (3) is independent of the remaining scale of h.

## 6. Contribution and exact limit

PR1222 determined the abstract nonsplit quotient M=W(-9) but retained its embedded nonzero graph. The present argument determines that actual graph uniquely relative to the original B7 graph, by an intrinsic first-order condition on the full reduced divisor. The factor -1/2 comes from the formal derivative of a symmetric norm, not from an evaluated parameter or chosen invariant formula.

The equality is consistent with the previously required nonzero and distinct graphs. It does not contradict or realize the residual simultaneous case. Even the converse proves only vanishing of beta_(F6) on D12, not exact coherent image, further derivatives, original tenth jets, algebraicity, or an original source instance. Original t, local delta, the separate e9 endpoint, the cyclic rank-seven alternative, both F18 forms, and all whole-branch/profile questions remain separate.
