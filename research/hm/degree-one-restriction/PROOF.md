# Degree-one defect and simultaneous twist-four ramification interpolation

## Scope and dependencies

Work over C, retaining the marked nonzero monad scalars and determinant-valued skew pairing. Let Gamma be the binary icosahedral group, U and W its two binary representations, V=Sym^2 U, A=Sym^2 W, P the even four-dimensional irreducible, and D the five-dimensional irreducible. Put H=V+W and E=U tensor Lambda^2 ker(x) on P(H*).

Use [PR676](https://github.com/Akilleez-QA/read-em-and-weep/blob/b7fd2c946b39301bdb226af362674e1b2e755097/research/hm/global-skew-middle-presentation/PROOF.md) for global transvections, [PR677](https://github.com/Akilleez-QA/read-em-and-weep/blob/e8dc002a6de60d5feac936b2b291188fd2bdc6a9/research/hm/equivariant-middle-family/PROOF.md) for parameter-family dimensions, [PR678](https://github.com/Akilleez-QA/read-em-and-weep/blob/f47c81086e5bd17be4ba714e43fa7f6226d41beb/research/hm/ramification-family-target/PROOF.md) for the coefficient bundles and ramification geometry, [PR679](https://github.com/Akilleez-QA/read-em-and-weep/blob/17dce2263c2ad5ddc26d42c6aaeb21dfdfb7dacb/research/hm/linewise-operator-image/PROOF.md) for independence of B,C, and [PR680](https://github.com/Akilleez-QA/read-em-and-weep/blob/a49890600f8facfa752f15620c33b755ba7c0c21/research/hm/simultaneous-line-interpolation/PROOF.md) for the exact scope of the scalar-localization exclusion. The actual mixed-value dependency is pinned in PR678 at PR543 commit 8d8b5be4ce62c3055bb53be9e16d29cc63072f04.

The new result is simultaneous surjectivity of the center-even, vertex-zero global skew-operator map onto all three coefficient values on all twelve ramification joining lines, at the original twist four. This concerns the mixed functional alone. It does not solve the coupled monad/source equations, determine the fourth Bockstein, or establish higher lifting or algebraicity.

## 1. Degree-one transvections and their two coefficients

Write G=H0(E(1))=U tensor Lambda^3 H. Its center-even and center-odd parts are

    G+ = U tensor Lambda^2 V tensor W = A+P+D, dimension 12,
    G- = U tensor (Lambda^3 V + V tensor Lambda^2 W), dimension 8.

The symmetric-square resolution used in PR676, at twist one, has only its constant term in cohomology: the other terms are sums of O(-1),...,O(-4), acyclic on P4. Hence

    H0(sp(E)(1)) = Sym^2 G,
    H0(sp(E)(1))+ = Sym^2 G+ + Sym^2 G-, dimension 114.

For Omega in G set p_Omega=i_x Omega. A transvection associated to Omega,Psi is

    T_Omega,Psi(eta)=p_Omega beta(p_Psi,eta)+p_Psi beta(p_Omega,eta).

The ambient contraction identity in PR678 identifies beta(p_Omega,eta) with the constant functional b_Omega(eta), obtained by exterior multiplication Omega wedge eta and the alternating pairing on U. No rational denominator occurs.

At a ramification pair (r,w), let v=r^2 and retain

    Y=(t^2/s)C-c s B,  x=t v+s w,  c != 0.

Here B,C belong to the mixed sector U tensor V tensor W and are linearly independent. Their frame degrees in (r,w) are (1,1),(5,-1). The Cartan functional lambda_w on U tensor Lambda^2 V has degree (0,3). Define, for Omega in G+,

    alpha(Omega)=lambda_w(i_w Omega),
    b(Omega)=b_Omega(B),
    d(Omega)=b_Omega(C).

These are equivariant maps into H0 O(0,4), H0 O(1,1), and H0 O_R(5,-1), respectively. For Omega in G-, the pairing b_Omega with the entire mixed sector vanishes: the exterior product has either four V factors or three W factors. Consequently Sym^2 G- contributes zero.

For Omega,Psi in G+, lambda_w(i_x Omega)=s alpha(Omega). Thus the functional is exactly

    lambda_(s w)(T Y) = s^5 M0 + t^2 s^3 M2,
    M0 = -c [alpha(Omega)b(Psi)+alpha(Psi)b(Omega)],
    M2 = alpha(Omega)d(Psi)+alpha(Psi)d(Omega).       (1)

The two coefficient bundles are O_R(1,5), O_R(5,3), each with representation A+P+D.

## 2. Structural nonvanishing, not dimension inference

For each nonzero w, contraction G+ -> U tensor Lambda^2 V is onto, and lambda_w is nonzero. Therefore alpha is nonzero. Its target H0 O(0,4)=Sym^4 W* is irreducible D, so alpha identifies the D summand of G+ with all binary quartics and kills A+P.

The pairing

    (U tensor Lambda^2 V tensor W) x (U tensor V tensor W)
        -> det U tensor det V tensor det W

is perfect: it is the tensor product of the perfect alternating U and W pairings and Lambda^2 V x V -> det V. The nonzero section B therefore makes b nonzero. Since its global target H0 O(1,1)=U* tensor W*=P is irreducible, b identifies the P summand of G+ with all bidegree-(1,1) forms and kills A+D.

The ramification set R is a transitive reduced twelve-point orbit with stabilizer C10. On matched binary frames the stabilizer exponent of O_R(p,q) is 3p+q modulo ten (the fiber character is inverse). Therefore

    H0 O_R(5,-1) = V+P+D.

Multiplicity one and G+=A+P+D imply d kills A. The bundles O_R(4,-2) and O_R(5,-5) have trivial stabilizer character. Choose invariant nowhere-zero sections h,k of these two bundles. Such a section exists by induction from the trivial stabilizer character and is nowhere zero by transitivity. Multiplication by either is an equivariant isomorphism of the corresponding section spaces. Multiplicity one now gives constants a,b0 with

    d = a h b + b0 k alpha.                         (2)

Crucially, b0 != 0. If b0=0, equation (2) and the perfect pairing above imply C=a h B at every ramification pair, contradicting the proved linear independence of C,B. This is a structural nonvanishing proof; no actual point, scalar, or matrix is computed. The coefficient a is allowed to vanish.

## 3. Exact degree-one image: a graph plus octics

Equations (1)-(2) show that only the cross block D tensor P and the block Sym^2 D contribute. On D tensor P the lower coefficient is binary multiplication

    H0 O(0,4) tensor H0 O(1,1) -> H0 O(1,5),

which is onto by ordinary binary monomial multiplication. Restriction H0 O(1,5)->H0 O_R(1,5) is an isomorphism: the twisted CI resolution is

    0 -> O(-3,-1) -> O(-1,2)^2 -> I_R(1,5) -> 0,

whose first two terms have no cohomology. Thus the lower twelve-dimensional target is onto. The upper coefficient on this block is exactly rho times the lower, where rho=-(a/c)h, including the possible rho=0 case.

On Sym^2 D the lower coefficient is zero; the upper is a nonzero scalar times k times products of arbitrary binary quartics. These span H0 O(0,8). Evaluation at the twelve distinct negative projections is injective, since a nonzero binary octic has at most eight distinct zeros. Its image has dimension nine and representation P+D.

Consequently the exact pair image is

    {(u,rho u+v): u in H0 O_R(1,5),
                         v in k H0 O(0,8)|R}.      (3)

Its dimension is 21, its representation is A+2P+2D, and its cokernel in the 24-dimensional pair target is A. The degree-one center-even kernel has dimension 93. In particular, the proposed degree-one pair surjectivity is false; an exact three-dimensional defect remains. The graph statement includes an actual lift with upper coefficient exactly rho u for every u, not merely a quotient assertion.

## 4. Cubic multiplication removes the defect at twist four

All the following constructions use global degree-one skew operators from section 3 multiplied by ambient cubic polynomials. They therefore remain global skew operators at twist four. Each cubic has positive-coordinate degree at least one, so every constructed operator vanishes on the entire negative vertex Z=P(W*).

First use the upper-only octic subspace of (3), multiplied by pure positive cubics. Pure positive cubics restrict to all binary sextics H0 O(6,0): the Veronese multiplication Sym^3(Sym^2 U*) -> Sym^6 U* is onto. This produces only the highest coefficient L5, with value space

    k [H0 O(6,0) H0 O(0,8)]|R in H0 O_R(11,3).     (4)

This product is onto all twelve values. For any chosen ramification pair i, choose six other positive projections and a binary sextic vanishing exactly on those six. It is nonzero on the six complementary projections, including i. On these six distinct negative projections, binary octics interpolate arbitrary six values. Choose their values to vanish on the five other complementary points and to give the required value at i, after division by the nonzero sextic and k values. The product vanishes also on the original six points. Hence (4) contains every single-support value. This is a universal interpolation existence argument on distinct points, not a selected actual evaluation or computation.

Next choose a pure positive cubic whose restriction H is nonzero at all twelve pairs. It exists because its section space is basepoint-free and a finite union of proper hyperplanes cannot cover a complex vector space. No actual coefficient is selected or tested. Multiplication by H is therefore an isomorphism of the relevant twelve-dimensional value spaces. For any graph lift (u,rho u), multiplication gives

    t^3 s^5 H u + t^5 s^3 H rho u.

The middle coefficient is arbitrary; cancel the unwanted highest coefficient using (4). Thus all middle coefficients can be realized with the lowest and highest coefficients zero.

Finally choose a cubic of positive degree one and negative degree two whose coefficient L in O_R(2,2) is nonzero everywhere on R. The same finite-hyperplane argument applies because these ambient cubics are basepoint-free at every pair. Multiplying a graph lift gives

    t s^7 L u + t^3 s^5 L rho u.

The lowest coefficient is arbitrary, and its middle coefficient is removable by the preceding construction. By linearity all three coefficient sections on all twelve lines are arbitrary, simultaneously.

No scalar cubic isolates an entire joining line here. The single-support coefficients come from operator-valued graph lifts, and the sextic/octic argument is a product of operator coefficients with cubics. Thus there is no conflict with PR680's scalar-cutoff exclusion or its nonsplitting theorem.

## 5. Exact family consequences and limits

Let R4+ be the center-even global skew-operator space and R4+,Z its subspace vanishing along Z. The preceding construction proves both maps onto

    Q=H0[O_R(3,7)+O_R(7,5)+O_R(11,3)]
      =3(V+P+D), dimension 36.

Since dim R4+=2409 and dim R4+,Z=2229, their exact kernel dimensions are 2373 and 2193. The map and vertex condition are Gamma-stable. Over C, applying Hom_Gamma(P2,-) is exact, where

    P2=Sym^2 A tensor D=1+A+V+2P+3D.

Thus both the 1203-dimensional full family and the 1113-dimensional vertex-zero family map onto the complete eighteen-dimensional receiving space. Their exact kernel dimensions are 1185 and 1095. Equivalently, averaging a linear lift over Gamma yields the required equivariant parameter family; one does not average a single-line prescription and assume it stays fixed.

There is also an exact joint-prescription corollary. PR677 proves that the full 1203-dimensional family maps onto the 90-dimensional equivariant vertex-middle target, with kernel the 1113-dimensional vertex-zero family. Given any prescribed vertex value and any prescribed ramification coefficient family, first lift the vertex value, then correct its ramification discrepancy using the new surjection from that kernel. Thus the combined map onto the direct sum of the vertex and ramification targets is onto, with dimensions

    1203 -> 90+18=108, exact kernel dimension 1095.

This preserves any already-prescribed vertex middle value while imposing the mixed-functional conditions. It concerns vertex middle values, not an entire cochain defect. The ordinary center-even analogue has target dimension 180+36=216 and kernel dimension 2193.

In particular the prescribed middle-only forced functional has a global, center-even, Gamma-equivariant, vertex-zero skew-middle realization. This resolves the simultaneous mixed-functional operator-image dependency. It does not assert that this realization satisfies the other coupled primitive equations, preserves additional unproved gauge conditions, or determines beta4. Those remain distinct dependencies.

## Verification status

The proof is structural and uses no selected actual HM coefficients, points, matrices, ranks, or experiments. The bounded verifier checks abstract representation identities, ordinary binary monomial products, interpolation counts, and exact dimension arithmetic. It is not a formal proof assistant check and does not replace the geometric arguments above.
