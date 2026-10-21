# Actual conductor descent as a bundle map on the modular parameter line

This follows the integral lci surface and finite normalization theorems in UNIFORM-FLAT-EVALUATION-FIBRATION.md and GLOBAL-GAMMA-CONDUCTOR-GRAPH.md. Write g:S -> Gamma=P1, nu:Wtilde -> S, and M_k=O_Xhat(2L+(k-5)H)|S. The normalized line is N_k=b*(pi*(10I+12F)+(k-5)h)-2 sum F_i. This note concerns k=3,4.

## 1. Universal Euler characteristics

For n>=0, put m=n+2. The projective-bundle pushdown before blowup is Sym^m(E)(k-5) on Q. If alpha,beta are the formal Chern roots of E, then alpha+beta=5H and alpha beta=10H². Write s²=-15 and a=k+5n/2, so the scalar roots are a+(j-m/2)s for j=0,...,m. Their power sums are

    p0=m+1, p1=(m+1)a,
    p2=(m+1)a²-15m(m+1)(m+2)/12,
    p3=(m+1)a³-15a m(m+1)(m+2)/4.

The Todd class of Q is 1+(3/2)H+(13/12)H²+(1/2)H³ and integral H³=2. The fifty fourfold point blowups subtract 50 binomial(n+3,4). Consequently

    P_k(n)=chi_Xhat(M_k+nA)
      =(n+3)(2k³+15k²n+9k²+30kn²-47k-105n²-210n-84)/6.

Here M_k in this formula denotes its ambient line bundle. Since ch(O_Gamma)=6a²-11a³ on P3 and f is flat, restriction to S gives

    chi_S(M_k)=12[n²]P_k(n)-66[n³]P_k(n)
              =15(2k²-10k+7).

These are -75 and -15 for k=3,4. The normalization Euler characteristics are -145 and35, from the unblown values5 and185 minus fifty length-three doublepoint conditions. Thus for T_k=(nu_*O_Wtilde/O_S) tensor M_k,

    chi(T_3)=-70, chi(T_4)=50.

The formulas are universal intersection-theoretic calculations, not selected evaluations of an HM instance.

## 2. Vanishing of the normalization higher direct images, including special fibers

Before the fifty blowups, the exact projective-bundle sequences in MODULAR-DOUBLE-COVER-EIGENCLASS-COHOMOLOGY.md give H1 of N_k on every modular fiber equal to zero. This includes the I5 fibers: the k3 argument embeds the dual pushdown in Sym²K and uses the invariant-constant-section dimension obstruction; the k4 argument embeds its dual in a sum of line bundles negative on every component. These arguments concern the fixed ruling bundle, not equivariance of the chosen quadric.

Impose one additional genericity condition: each of the fifty modified fibers of W is smooth, not merely its underlying modular elliptic curve. Here is the required uniform argument. For a fixed smooth modular parameter beta and a marked line i, restrict ambient quadrics through z_i(beta) to the normalized scroll R_beta. Their base locus consists exactly of the four preimages of z_i(beta), since ambient quadrics through one point have no other common zero. The established immersion lemma at all four branches makes their first-order linear systems surjective there; hence a general such quadric cuts smoothly at all four base points. Bertini gives smoothness away from them. The ample class 2h gives connectedness, and a smooth connected curve is integral of genus sixteen. For each marked line, the universal incidence of (beta,Q) with Q containing z_i(beta) is irreducible of dimension fourteen. Its bad locus is a proper closed subset after shrinking to the smooth modular locus, of dimension at most thirteen. Projection to quadric space therefore has proper closed image closure. Avoiding these images for all twenty-five lines, and the finitely many cusp and collision conditions, ensures that all fifty selected fibers are smooth simultaneously. Thus this is a genuine common open condition on Q; smoothness of the modular parameter alone was insufficient.

The fifty blowup points have distinct smooth modular parameters.  A modified total fiber consists of its smooth genus-sixteen strict transform and one exceptional P1 meeting at one node. The line N_k has degree38 or68 on the first component and degree2 on the second. Both have H1=0, and evaluation at the gluing node is onto. The normalization exact sequence for this nodal union therefore gives H1=0 on the total fiber as well. Cohomology and base change now proves R1(g nu)_*N_k=0 on all of P1.

The vector bundles G_k=(g nu)_*N_k have ranks25 and55. Their degrees, subtracting the ranks from their Euler characteristics, are

    rank G3=25, deg G3=-170;
    rank G4=55, deg G4=-20.

## 3. The actual conductor target bundles

The normalization quotient T=nu_*O_Wtilde/O_S is Cohen--Macaulay of pure dimension one. Indeed both O_S and nu_*O_Wtilde are maximal Cohen--Macaulay over the two-dimensional local Gorenstein rings of S, and the depth lemma gives depth at least one for their quotient. Its support is the image of J, which has no vertical components. Therefore its support is finite over P1. Multiplication by any nonzero local parameter on P1 is injective on T, since its associated primes are its horizontal one-dimensional components. Hence T is finite flat over P1.

The generic fixed-fiber discrepancy has length40. Thus E_k=g_*T_k are rank-forty vector bundles, with

    deg E3=-110, deg E4=10.

The normalization sequence pushes forward to the exact sequence

    0 -> g_*M_k -> G_k --d_k--> E_k -> R1g_*M_k -> 0.

This is an actual geometrically defined bundle map, not an arbitrary matrix with the displayed dimensions. In particular,

    H0(S,M_k)=ker[H0(P1,G_k) -> H0(P1,E_k)].

No generic rank, splitting balance, or independence of conductor conditions has been assumed. At a general parameter, d_k is the forty-dimensional first-jet discrepancy map derived from the ten four-branch singularities.

## 4. Relation to actual endomorphisms

The restriction from actual twist-k trace-free endomorphism sections to H0(S,M_k) is injective under the established fifty-point evaluation injection. To see this, a section vanishing on S restricts to zero on every exceptional E_i: its ambient line bundle is trivial on E_i=P3, so the restriction is constant, and S intersect E_i=Gamma is nonempty. The fifty constants therefore vanish. The pinned evaluation injection forces the original endomorphism section to vanish.

Consequently injectivity of the global-sections map induced by d_k is a sufficient condition for actual twist-k vanishing. It is not necessary without surjectivity of the restriction map from actual endomorphisms. Establishing the required injectivity is still open. The rank and degree data do not prove it, and no complete repair is claimed.
