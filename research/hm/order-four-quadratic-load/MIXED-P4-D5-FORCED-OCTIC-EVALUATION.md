# Mixed P4+D5 profiles force complete octic evaluation

## Result and limits

For each of the following four surviving formal primal profiles of the hypothetical `(k,l)=(3,2)` Gauss plateau, the cubic pairing must vanish and the quadratic restricted derivative must have rank one:

    X: (0,1,0,0,0,1,0,1), E=(P+D)O(-2)+T O(-3)+O(-8)+O(-10);
    Y: (0,1,0,0,0,0,1,0), E=(P+D)O(-2)+T O(-3)+W O(-9);
    Z: (0,0,1,1,0,1,0,0), E=(P+D)O(-2)+(V+P)O(-4)+O(-8);
    U: (1,0,1,0,1,1,0,0), E=(P+D)O(-2)+Wp O(-3)+V O(-4)+Wp O(-5)+O(-8).

More precisely, `phi:(P+D)O -> Q` is the complete evaluation onto a saturated `O(8)` subbundle. Its kernel is `(Wp+T)O(-1)`. Thus its twist by minus two gives a subbundle `(Wp+T)O(-3)` of K.

Here P=P4, D=D5, Wp=Wprime and T=T6. This is a **new necessary condition**, not the exclusion of any of these four types: the zero-pairing branches `(a,b)=(1,1),(1,2)` remain open. The formal count remains at most ten of 28; SF rank at least three and square rank at least 27 remain unchanged. No smoothing closure is claimed.

Only hypothetical equivariant bundle geometry and universal representation arithmetic enter. There are no actual HM/source coefficients, selected points, source-instance matrices or ranks, parameter scans, local models, or consumed experiments.

## 1. Frozen inputs

Use `THREE-DOUBLE-P4-TYPES-EXCLUDED-BY-BACKWARD-GAUSS.md`, its verifier, and its unchanged dependencies. In particular the plateau

    F0 < K2 < K < E < F4 < F5

has ranks 8,11,14,17,20,23, with degree E=-54 and

    H0(K(2))=0, H0(K2(3))=0, H0(F0(4))=0.

Both backward derivatives have rank three. Q has largest degree at most eight and largest-two-degree sum at most fourteen. Any positive invariant torsion length is at least twelve. All four E above have the same equivariant Euler characters as the frozen single-P and double-P types.

Write `psi:T O -> E*(1)`, `B:(P+D)O -> T O(3)`, and let a,b,t be the respective ranks of phi,psi,B. The restricted maps are section-injective, `a+b-3<=t`, and B is either zero or has saturated image `Wp O(1)` with section module P.

## 2. Exclude every nonzero-pairing branch

If B is nonzero and a=2, the saturated kernels of phi and B coincide. But the section kernel of B contains D, contradicting section-injectivity of phi. Consequently a=3, b=2.

The actual full image I of `beta_E(2)` therefore fits into

    0 -> O(n) -> I -> Wp O(1) -> 0.

The line kernel contains D in sections. Its degree is even and at most eight, so the universal symmetric-power test gives n=4 or8. Both extensions split and

    A_n=E/K=O(n-2)+Wp O(-1).

Let delta be the invariant torsion colength of `K/K2` in `A_n(-2)`. Backward persistence gives precisely the frozen inequality

    15-2n+delta <= h0(K2(4)) <= h0(A_n)=n-1.

For n=4 this is impossible. For n=8 it forces delta<=8, hence delta=0. The exact quotients and Euler characters are now

    E/K=O(6)+Wp O(-1), K/K2=O(4)+Wp O(-3),
    chi_G(K2(3))=-(Wp+S+T),
    chi_G(K2(4))=-A+V+P-D.

These are exactly the frozen two-shape classification and rank-one endpoint hypotheses of Sections 5–6 of `THREE-P4-QUADRATIC-TYPES-EXCLUDED-BY-BACKWARD-GAUSS.md`. That exhaustive classification gives

    K2=(V+P)O(-4)+Wp O(-5)+Htail,
    Htail=W O(-9) or O(-8)+O(-10),

and its endpoint forces the impossible invariant-ramification membership

    104 in <96,160,240,60,100,150>.

The verifier executes that frozen classification and endpoint check unchanged and checks that all four new bundles have the required matching characters. Therefore B=0 for all four profiles.

## 3. Rank-two quadratic image: all necessary possibilities

Suppose a=2. Since B=0 and b>=1, necessarily b=1. The actual quadratic image J is globally generated, has rank two, embeds in Q and contains P+D in sections. The complete necessary overlist is

    W O(5), O(4)+O(6), O(4)+O(8), W O(7), O(6)+O(8).

Its degrees j are 10,12,14. The list is obtained by enumerating every eligible irreducible rank-two block and every pair of equivariant lines, imposing the target Hom condition, section-character containment and degree at most fourteen. The companion verifier does this against all five Q profiles; these are necessary shapes, not asserted realizations.

J is saturated in Q: its defect is at most 14-j<=4<12. The complete necessary list of line images of psi is

    X: O(9) or O(11); Y,Z,U: O(9).

Write this line as O(e). It is saturated since its possible defect in E*(1) is at most two. Duality gives the projected image of I in T O(3) as O(3-e). The rank-two kernel contains saturated J, so equals J. The extension splits by H1 vanishing, and the actual first quotient is

    E/K=J(-2)+O(1-e).                                  (1)

This uses saturation to identify actual image sheaves; no unproved equality of images with saturations is used.

## 4. A uniform lower bound on the first kernel

Let N0 be the kernel of the surjection `(P+D)O -> J`, and put N=N0(-2). Section injectivity makes all seven ordinary degrees of N0 at most -1. Their sum is -j. Each is therefore at least 6-j, and every degree of N is at least

    4-j >= -10.                                        (2)

Write E=(P+D)O(-2)+H. The line quotient in (1) is obtained from H; let Htail be its kernel. Direct degree and universal evaluation give

    e=11, X: Htail=T O(-3)+O(-8);
    e=9, X or Y: Htail=T O(-3)+O(-10);
    e=9, Z: Htail=(V+P)O(-4);
    e=9, U: Htail=Wp O(-3)+V O(-4)+Wp O(-5).

For Y this is the complete evaluation `W O(-9)->O(-8)` with kernel O(-10). For X at e=9 the O(-8) summand cancels; the map from O(-10) to O(-8) vanishes since Sym^2 W has no invariant. All other claimed vanishings follow by degree. At e=11 only the O(-10) summand can contribute and cancels.

There is an exact sequence `0 -> N -> K -> Htail -> 0`: surjectivity of the quadratic map onto J(-2) allows the other components of Htail to be lifted to K. Both N(10) and Htail(10) are globally generated, and H1(N(10))=0. Hence K(10) is globally generated. This establishes the needed high-line bound independently of earlier high-line arguments and includes the case with both O(-8) and O(-10).

## 5. Exclude both high-line degrees

If e=11, the next derivative has target `J(-4)+O(-12)`. Rank three forces a nonzero projection from K to O(-12), whereas K(10) is globally generated. This is impossible.

If e=9, the target is `J(-4)+O(-10)`. Every ordinary summand of K has degree at least -10. A nonzero projection to O(-10) must therefore be a nonzero constant map from an O(-10) summand, and is a split surjection. Choose one such summand and subtract its graph in the target. The actual full image then has the form

    K/K2=C+O(-10), C subset J(-4), rank C=2,
    deg C=j-8-delta,
    deg K2=-24-2j+delta,                               (3)

where delta>=0 is the torsion colength. No splitting assertion about an arbitrary extension of C by a line is needed: the splitting comes from the actual O(-10) summand of K.

The next derivative has rank three and target `C(-2)+O(-12)`, so K2 has an ordinary summand of degree at most -12. All its eleven degrees are at most -4 by H0(K2(3))=0. Thus deg K2<=-52. Comparing with (3) excludes j=10 and12. For j=14 it forces delta=0 and exactly

    K2=U0 O(-4)+O(-12), dim U0=10.

For either degree-fourteen shape of J, subtracting the two now-exact quotients in equivariant K-theory gives chi_G(K2(4))=V. Since H1(O(-8))=Sym^6 W=V+P, necessarily U0=2V+P. But persistence would require an injection

    H0(K2(4))=2V+P -> H0(J(-2)+O(-8))=V+P+D,

which is impossible on V multiplicities. This excludes all a=2 branches.

## 6. The remaining necessary octic evaluation

With B=0, a+b<=3 and b>=1; after excluding a=2 we obtain a=1. Its globally generated line image has even degree at most eight and contains P+D in sections. The only possibility is O(8), and `Sym^8 W=P+D`. Section injectivity is thus an isomorphism on the complete section module, so phi is complete evaluation, with kernel `Sym^7 W O(-1)=(Wp+T)O(-1)`. The line is saturated because it already has the maximum possible degree in Q.

No assertion excluding b=1 or b=2 in this remaining branch is made.

## Reproduction

Run `python3 verify_mixed_p4_d5_gauss_reduction.py`. It executes the frozen preceding verifiers unchanged and checks the four profiles, common Euler characters, both nonzero-pairing possibilities, the exhaustive necessary image lists, saturation and extension bounds, high-tail identities, the uniform kernel-degree bound, the two second-kernel bottlenecks and the final multiplicity contradiction.
