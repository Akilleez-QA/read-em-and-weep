# Generic surjectivity of the twist-four value map

## 1. Exact Picard bookkeeping on one smooth ruled fiber

Let R=P_E(E0) be a smooth normalized beta scroll, where E0 is the stable normalized rank-two degree-one bundle on its elliptic base E. Put A=O_R(1), D=det(E0), and write the actual line bundles

    h=A tensor pi*B,  J=A tensor pi*T,

with deg B=7 and deg T=12. Write C25 for the degree-twenty-five line bundle of the torsion ruling fibers. The exact conductor identity gives

    C25 = D tensor T^2.

Take a smooth normalized quadric section C in |2h|, and let sigma be its degree-two covering involution over E. Finite duality or the relative projective-bundle sequence gives

    pi_*O_C = O_E direct_sum (D tensor B^2)^{-1},
    pi_*(A|C)=E0,
    Norm(A|C)=D^2 tensor B^2,
    omega_C=pi*(D tensor B^2).

These are line-bundle identities, not just numerical degrees. The normalized twist-four eigenline is L4=A^{-1} tensor pi*(C25^2 tensor B^{-1}), restricted to C. Therefore the Serre dual of (L4-J)|C is

    (A|C tensor (sigma*(A|C))^{-1}) tensor pi*P,
    P=D tensor B^5 tensor T^{-3}.

A numerical degree calculation only says deg P=0 and would not suffice.

## 2. The potential Picard-zero twist is actually trivial

Use the established exact global identities h=xi_V+I, J=h+H, det V=I+3F. On one elliptic fiber put I0=O(I)|E=O(H)|E; a line pulled back from the parameter base is trivial on this fiber. Choose a degree-minus-two line bundle R0 and normalize E0=V|E tensor R0. Then

    B=R0^{-1} tensor I0,
    T=R0^{-1} tensor I0^2,
    D=I0 tensor R0^2.

Substitution gives

    P=D tensor B^5 tensor T^{-3}=O_E

exactly: the R0 exponent is 2-5+3=0 and the I0 exponent is 1+5-6=0. This proves the identity independently of a theta normalization, a choice of origin divisor, or merely numerical equivalence.

## 3. Non-invariance and surjectivity

The degree-zero line A|C tensor (sigma*(A|C))^{-1} is nontrivial. If it were trivial, A|C would admit a sigma-linearization: an isomorphism with its pullback can be rescaled to make its square the identity over C. The resulting involution on pi_*(A|C)=E0 has generic plus and minus eigenspaces of rank one. Its idempotent projectors split E0 as a sum of two line bundles, contradicting stability of the rank-two degree-one normalized bundle.

Hence H0 of that degree-zero line is zero. Serre duality proves

    H1(C,(L4-J)|C)=0.

The restriction map from H0(C,L4) to the forty graph values is therefore surjective. Quotienting these values by the ten common-value subspaces gives surjectivity onto the rank-thirty value-discrepancy target. This holds on the nonempty open of smooth modular fibers with smooth C and distinct graph intersections. In particular it proves generic surjectivity of the actual value map G4 -> V4 from CONDUCTOR-VALUE-DERIVATIVE-FILTRATION.md.

## 4. Kernel bundle and the unresolved special-fiber correction

Globally on P1, let Tors be the torsion cokernel of G4 -> V4 and let ell=length(Tors). The kernel K4 is a vector bundle, with

    rank K4 = 55-30 = 25,
    deg K4 = (-20)-45+ell = -65+ell.

There is an exact sequence

    0 -> K4 -> G4 -> V4 -> Tors -> 0.

The torsion length has not been computed. In particular one must not replace deg K4 by -65 without proving surjectivity at every special parameter. The earlier derivative-layer vanishing identifies the actual global conductor-descent kernel with H0(P1,K4). Actual endomorphism sections inject into this space. Neither generic surjectivity nor its degree formula establishes H0(K4)=0; the splitting and special-fiber correction remain open.

All calculations use exact line bundles and symbolic source geometry. No selected HM coefficients, rank tests, or external writes are used.

## 5. Direct cohomological strengthening away from modified parameters

There is a shorter route which does not require the quadric curve C itself to be smooth. Before the fifty point blowups, the exact global identity is L4-J_W=L3-pi*H. Let E3=pi_*L3 from MODULAR-DOUBLE-COVER-EIGENCLASS-COHOMOLOGY.md. Its exact sequence and determinant give an injection E3^dual -> Sym²V^dual. Restrict to a smooth elliptic modular fiber E. Since H|E=det(V|E),

    E3^dual tensor H|E -> Sym²(V|E)^dual tensor det(V|E)
                      = End_0(V|E).

Stability gives H0 of the right-hand side zero. Elliptic Serre duality and finite pushdown therefore give H1(C,L4-J_W)=0 for every such fiber, even if C is singular. The graph intersection is finite: a general ambient Q contains none of the one-parameter family of elliptic normal quintics, because for each such curve the containing quadrics form P4, giving an incidence of dimension at most five in P14. The restriction exact sequence consequently gives surjectivity onto the scheme-theoretic graph values. Quotienting by the common-value subspace again gives surjectivity onto the value target.

Thus the torsion cokernel in Section4 is supported only at cusp parameters and the fifty parameters changed by point blowups. The latter require a separate argument: on such a fiber N4-J involves a subtraction of one point, so the preceding unmodified cohomology proof cannot simply be reused. No length bound or zero-cokernel assertion at those parameters is made here.

## 6. A simple bound for the fifty modified-parameter contributions

Over the noncuspidal parameter open, put M=L4-J_W on W. The preceding argument proves R1 f_*M=0. On Wtilde,

    N4-J = b*M - sum F_i.

Ordinary point-blowup pushdown gives b_*O(-sum F_i)=I_{P_1,...,P_50} and R1 b_*O(-sum F_i)=0. The exact sequence of the fifty reduced points, pushed to the parameter line, therefore shows that R1(f b)_*(N4-J) is a quotient of the direct sum of the fifty residue-field skyscraper sheaves. The graph-restriction exact sequence shows that the value-map cokernel is a quotient of this higher direct image. Thus at each modified parameter its length is at most one and it is annihilated by the local parameter. The total contribution from the fifty modified parameters is at most fifty.

This bounds only those contributions. The remaining possible torsion is supported at the twelve cusps; its length has not been computed. In particular the degree formula remains -65+ell_modified+ell_cusps, with 0<=ell_modified<=50, not a proved global vanishing statement.

## 7. Cusp acyclicity removes every cusp contribution

CUSP-RULING-BUNDLE-SIMPLICITY.md proves H0(End_0(V)|E)=H1(End_0(V)|E)=0 also on each I5 cusp fiber, using the actual component splittings, nonmatching positive sublines, and the Heisenberg action. The dual injection in Section5 remains exact under restriction to every fiber: it comes from an exact sequence of vector bundles with line-bundle quotient on S(5). Elliptic-fiber duality therefore kills H1(C,L4-J_W) at the cusps as well. The finite graph-restriction sequence then gives surjectivity onto the value target at every unmodified parameter, cusps included.

Thus the only possible cokernel is supported at the fifty reduced modified parameters. Write its length epsilon. Section6 proves 0<=epsilon<=50, with each local contribution at most one and annihilated by that reduced parameter. The final kernel constraints are

    rank K4=25,
    deg K4=-65+epsilon,     -65<=deg K4<=-15.

The negative total degree does not imply H0(K4)=0. Its splitting can still contain nonnegative summands. Earlier references in Sections4--6 to unresolved cusp torsion are superseded by this acyclicity result.

## 8. A symbolic degeneration eliminates the modified contributions generically

Fix a smooth modular parameter beta and its distinguished graph point p over the marked source point z. We prove that the line M=(L4-J)|C is generated at p for a general ambient quadric through z. No special coefficients are evaluated.

Choose an ambient hyperplane H1 through z which contains no ruling line of R. Such hyperplanes exist: the four rulings through z impose four proper P2 subsets inside the P3 of hyperplanes through z; each other ruling, together with z, imposes a P1 of hyperplanes, whose one-parameter union has dimension at most two. Choose also a general hyperplane H2 avoiding z and containing no ruling. Their pullbacks C1,C2 in |h| are sections of the projective-line bundle R->E, hence smooth elliptic curves. General H2 meets C1 transversely in fifteen points, none equal to p. Their union C is the pullback of the reducible quadric H1 H2. It is still a finite-flat degree-two cover of E.

By the exact Picard identity in Section2,

    M = A^{-2} tensor pi*(D³ B⁴).

A section Ci with class A tensor pi*B has A|Ci=D tensor B. Therefore

    M|Ci = D tensor B² = O_Ci(C1 intersect C2).

On C1 take the canonical section vanishing on all fifteen intersection points; on C2 take the zero section. They agree at every node and hence glue to a global section of M on C. Its value at p is nonzero, since p is not on C2.

The dual-injection proof in Section5 applies to this reducible finite-flat cover as well and gives H1(C,M)=0. Surjectivity of evaluation at p now gives H1(C,M(-p))=0. Upper semicontinuity in the family of quadric pullbacks through z proves the same vanishing on a nonempty open set of that linear system. Intersect with its smooth-quadric and smooth-section open sets.

For each marked line the universal incidence of (beta,Q) with Q containing z_i(beta) is irreducible of dimension fourteen. The bad locus for this vanishing is proper, hence has dimension at most thirteen. Avoid its image closure in quadric space, for all twenty-five marked lines. The finitely many collision and cusp conditions can be excluded at the same time. Thus, on a common nonempty open of quadrics, all fifty modified evaluations are onto simultaneously.

On that open, R1 of the modified line N4-J is zero also at the fifty modified parameters, by the blowup pushdown exact sequence of Section6. Combined with cusp acyclicity, the value map is everywhere surjective on P1. Its exact sequence is therefore

    0 -> K4 -> G4 -> V4 -> 0,
    rank K4=25, deg K4=-65.

The epsilon correction in Section7 is zero on this smaller common open. This conclusion strengthens that earlier bound; it does not prove H0(K4)=0. Negative total degree remains insufficient, and the splitting of this actual kernel bundle remains the unresolved global gate.
