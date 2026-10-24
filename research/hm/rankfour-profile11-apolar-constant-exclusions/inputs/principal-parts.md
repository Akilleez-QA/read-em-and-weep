# Deep triplet images and rigidity of the sharp two-column endpoint

## Statement and assumptions

Use the actual setting and five-kernel theorem retained as inputs/five-kernels.md, exact proof SHA256 4d06da768074a6e813ed295a088d862ce328a4cd33b739e88e20ac1f315de36a. Its complete PR1194/PR1185 inputs are also retained. Work on the physical binary-icosahedral line with its fixed determinant convention and the original saturated rank-thirty constant ambient. The actual source is

    E=D(-2)+(W'+T6)(-3)+V(-4)+O(-8),
    A_q=A_std(4)+O(-8),  K=E^-,  rank K=13, deg K=-58.

The maximal rank-four plateau (1,1) gives rank beta_K<=3. The section gates and the five necessary K forms are imported, not bypassed. Let J=W(1) be the canonical kernel of A_std(2)->O(4). The preceding theorem proves that the actual V(-4) derivative row maps onto J everywhere, so J is contained in the coherent image I=im beta_K. It proves I=A_std(2) for K1,K2.

For the other three necessary kernels, this theorem gives exactly the following necessary image alternatives:

    K3=(V+P+D)(-4)+O(-10):
        I=A_std(2), or I=J+O(-10).

    K4=S4(-3)+(V+P)(-4)+W(-9),
    K5=S4(-3)+(V+P)(-4)+O(-8)+O(-10):
        I=A_std(2), or I is the preimage of f12 O(-8) in A_std(2),
        under A_std(2)->O(4).

Here f12 is any nonzero degree-twelve invariant, unique up to scalar. In the latter alternative I is equivariantly isomorphic to J+O(-8); its actual embedding has torsion quotient O_Delta(4), where Delta is the invariant divisor of f12. We do not replace this coherent image by its saturation. Every alternative has actual derivative rank three. None is asserted realized.

Moreover, whenever I=J+O(-10), the actual successive derivative kernels F1=K^-, F(j+1)=Fj^- have the forced complete flag

    F1=(S4+T6)(-5),
    F2=(A_std+D)(-6),
    F3=(W+S4)(-7),
    F4=(1+A_std)(-8),
    F5=W(-9),  F6=0.

The equalities are equivariant bundle isomorphisms of the actual subbundles; every intervening rank-two graded derivative is an everywhere isomorphism. This is compatible with K3. It excludes the negative-image alternative for K5 because K5^- contains an actual A_std(-4) subbundle. K4 has no negative component already by degree.

No kernel splitting or whole triplet quotient is excluded; the additional exclusion concerns one actual endpoint-image alternative. The original t=0 theorem is not needed. No complete coefficient span is assumed for F5.

## 1. A common rank-two image cannot be the whole endpoint

If I=J alone, K^- has rank eleven and degree -60. The terminating two-column actual kernel capacity gives degree at most -61, because the heights sum to eleven and the degree bound is -h1^2-h2^2. This contradiction, proved in the preceding theorem, uses only the common rank/degree data and therefore applies to every one of the five K forms. Any rank-two I containing J would equal J: its rank-zero quotient I/J embeds in the locally free quotient A_q(-2)/J. Therefore I has rank three.

## 2. Nonzero negative component forces the same split image

For K3 or K5, only the O(-10) summand can map to the negative O(-10) target; the map is a scalar. If this component is nonzero, it is onto. The same source summand has no component in O(4), because H0(O(14))^G=0. Hence its image modulo the already-contained J is the full negative-coordinate line in O(4)+O(-10).

The endpoint rank bound is three. A further nonzero O(4) image would raise the image modulo J to rank two, making total rank four. Therefore the entire O(4) composition vanishes. Since J is already in I and the negative projection is onto, the exact coherent image is

    I=J+O(-10).

For K4 the negative component is zero by ordinary degree. No assumption about a horizontal splitting is involved.

## 3. Exact all-height equality for this negative image

Assume I=J+O(-10). Put F1=K^- and F(j+1)=Fj^-. The same actual derivative construction as PR1185 provides coherent injections

    Gj=Fj/F(j+1) -> I(-2j).

The ranks qj are nonincreasing, at most three, and sum to rank F1=10. Also deg F1=-58-(-8)=-50. With h1>=h2>=h3>=0 and sum ten, the all-height bound from the ordinary top degrees (1,1,-10) of I is

    deg F1 <= -h1^2-h2^2-h3^2-11h3
            <= -50-h3-(3/2)h3^2.

The second inequality is the exact square estimate h1^2+h2^2>=(10-h3)^2/2. Since deg F1=-50, equality forces h3=0 and h1=h2=5. Hence qj=2 for j=1,...,5 and zero afterward. Every individual determinant-degree deficit vanishes, so

    rank Gj=2,  deg Gj=2-4j.

In fact each actual image in I(-2j) is exactly W(1-2j). To see this, project to the top rank-two block W(1-2j). The determinant of Gj has degree 2-4j. The other terms in wedge^2 I(-2j) have degree -9-4j and cannot receive its determinant by ordinary degree. Thus the projected determinant is a nonzero constant and the projection is an isomorphism of rank-two bundles. Its graph component into O(-10-2j) vanishes by degree. The same argument shows that each successive rank-two graded injection Gj->G(j-1)(-2), j>=2, is an isomorphism. In particular F5=G5=W(-9), and the actual saturated forward transforms satisfy

    F5^+=F4,  F4^+=F3,  F3^+=F2,  F2^+=F1.

These are conclusions from equality, not assumptions that intermediate images were saturated.

## 4. Universal principal-parts reconstruction, without a complete actual coefficient system

We record the required universal identity. For n>=k>=0 on P(W*),

    P^k(O(n)) = Sym^k W tensor O(n-k),
    P^k(O(n))^* = Sym^k W tensor O(k-n).

Here P^k denotes principal parts of order k, of rank k+1. The equivariant identification follows directly from complete polynomial evaluation. The natural map Sym^n W tensor O -> P^k(O(n)) sends a homogeneous form to its order-k restriction. Its kernel at a formal covector ell is precisely the forms vanishing to order k+1 there. Polarization gives another surjective map from the same complete system to Sym^k W tensor O(n-k), by contracting n-k factors with ell. It has exactly that kernel: in formal coordinates at ell=(1,0), the killed monomials are those divisible by the transverse variable to power k+1, while the remaining k+1 monomials map to a basis of Sym^k W with nonzero factorial coefficients. This is a proof of the universal polynomial-bundle identity, not an evaluation of any actual HM parameter or coefficient. The two quotients are thus equivariantly identical. Duality uses the fixed determinant pairing on W.

Now let U=F5=W(-9) be its actual saturated inclusion in the original constant H. Its dual gives a coefficient-system map H* tensor O -> U*. Taking jets of these constant coefficient sections produces the canonical O-linear map

    H* tensor O -> P^4(U*),

and dualizing gives P^4(U*)^* -> H tensor O. Locally its image is the span of U and its derivatives through order four; intrinsically this is the usual differential-evaluation map. Section 3 says that its saturated generic image is exactly F1, of rank ten.

Because F1 is saturated in H tensor O, the differential-evaluation map factors regularly through F1: its map to the torsion-free quotient H tensor O/F1 vanishes generically and therefore vanishes identically. The universal identity gives

    P^4(U*)^*=W tensor Sym^4 W tensor O(-5)
               =(S4+T6)(-5).

This source and F1 both have rank ten and degree -50. Their generically full-rank map therefore has determinant of degree zero and nonzero generic value, hence is an everywhere isomorphism. This proves F1=(S4+T6)(-5).

The same argument at orders three, two, one and zero, with the exact degrees from Section 3, gives all remaining Fj displayed in the statement. No injectivity or completeness of the actual map H* -> H0(U*) is assumed. The full complete polynomial system was used solely to prove the universal principal-parts identity; the actual differential-evaluation map may begin with a proper coefficient system.

## 5. The cubic-S4 kernel supplies an incompatible quartic subbundle

For K5, the actual top cubic subbundle U3=S4(-3) lies in the D(-2) row of E alone: all other source projections vanish by degree or irreducible inequivalence. Its inclusion is the canonical evaluation kernel, since Hom_G(S4,D tensor W) has dimension one:

    0 -> U3 -> D(-2) -> O(2) -> 0.

The actual quotient D-row factors through a map j:O(2)->A_std(4). It is nonzero; otherwise D(-2) would lie in K, contradicting H0(K(2))=0. This Hom space is one-dimensional. The map is the canonical dual quadratic evaluation inclusion, hence saturated, with cokernel W(5).

The derivative of U3 in the original constant ambient lands in (E/U3)(-2), since U3 is in E^-. Its projection to (E/D(-2))(-2) vanishes by degree: that target has top at most -5 while U3 has degree -3. Thus it factors through (D(-2)/U3)(-2)=O. This factor is nonzero, since otherwise U3 would be a forbidden negative horizontal subbundle. The only nonzero equivariant map S4(-3)->O is cubic evaluation, up to scalar, with kernel A_std(-4). Projecting into E/K gives

    beta_K|U3 = j(-2) composed with nonzero cubic evaluation.

Since j is an inclusion, its kernel is exactly A_std(-4). Hence there is an actual saturated injection A_std(-4)->K^-.

If K5 had a nonzero negative endpoint component, Sections 2-4 would give K^-=(S4+T6)(-5). No nonzero ordinary map from A_std(-4) to a bundle of pure degree -5 exists. This contradiction proves that the negative component vanishes for K5.

## 6. The remaining positive coherent-image alternatives

All remaining derivatives under consideration now land in A_std(2), with J already contained. For K3, its V row has zero O(4) composition; its P and D rows, if nonzero, have polynomial degree eight and are onto O(4) by the invariant-divisor minimum twelve. Its O(-10) row has no O(4) component. Therefore, when the negative component is zero, the rank-two-image contradiction of Section 1 forces some positive row nonzero and hence I=A_std(2). This completes K3's dichotomy.

For K4 and K5, the S4(-3) row has no O(4) component, because Sym7 W=W'+T6 contains no S4. The V row also has none. A nonzero P(-4) row is onto O(4), again giving I=A_std(2).

If that P row vanishes in O(4), the only possible surviving scalar-target row for K4 is W(-9)->O(4). The fixed products are

    (Sym12 W)^G=C f12,
    multiplicity of W in Sym13 W =1.

The nonzero composite W(-9)->O(-8), the standard linear evaluation, followed by multiplication by f12, spans this Hom space. Thus every nonzero such row has coherent image f12 O(-8). For K5 the corresponding row is O(-8)->O(4), likewise multiplication by f12; its O(-10) row has no scalar-target component because Sym14 W has no invariant. Section 1 prevents all these rows from vanishing.

Consequently I is precisely the preimage of f12 O(-8) under A_std(2)->O(4). The sequence

    0 -> J -> I -> O(-8) -> 0

splits equivariantly, because Ext^1(O(-8),J)=H1(W(9))=0 and averaging gives equivariance. The embedded image is nevertheless not A_std(2): its torsion quotient is O_Delta(4). The invariant degree-twelve divisor Delta is the reduced twelve-point orbit, since no smaller orbit exists. We retain the inherited equivariant line character on that torsion sheaf, not twelve arbitrarily trivial fibers.

## Contribution and limits

The new step is the sharp actual-filtration rigidity proved through the universal principal-parts construction, together with its exclusion of K5's negative-image branch. It yields the complete necessary endpoint-image alternatives for all five previously derived kernels and an explicit unramified five-stage flag in the surviving K3 negative-image branch.

No actual coefficients, parameters, points, jets, tensors, matrices, instance ranks, broad candidate search, historical enumeration, or scan of heights is selected or computed. Universal principal parts are proved symbolically for every binary polynomial system; they are not actual jet data. No full actual coefficient span is assumed. No whole K splitting, triplet quotient, profile or coarse bin is removed or realized. The stated original actual-geometric hypotheses remain imported.
