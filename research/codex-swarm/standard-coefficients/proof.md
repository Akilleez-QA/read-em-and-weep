# Finite standard-B coefficient program and conditional source bridge

## 1. Mathematical inputs and exact maps

The regular-cover comparison at commit `10810ee877fdaf291399198ad60d7dd0c316a42d`, sections 2–3, fixes the Alexander–Whitney map A, the signed staircase S, and the rectangle-cone K. `source-pins.json` records their exact blobs, the combined-pole proof, reviewed PR85, the uniform scalar transport, and the complementary-pair transfer. These are proof dependencies; no physical source formula is executed by this package.

For a canonical standard simplex s, `aw_cells` enumerates increasing active-coordinate sets with total degree dim(s). Each active coordinate uses the corresponding adjacent cut vertices; a constant active edge vanishes and a reversed active edge supplies a minus sign. `stairs` sums all permutations of the active coordinates with permutation sign, starting each active coordinate at zero. This gives S A = 1. On chains G is the composition of these two constructions. The recurrence is exactly

    k(s) = cone_b(s - G(s) - k(boundary(s))),

where b is the coordinatewise minimum (bitwise AND) of the vertices. Sorting gives the orientation and repeated vertices vanish. The inductive cone identity gives `boundary k + k boundary = 1-G`. All terms remain in the rectangle of s, so the required coefficient restrictions are legitimate on its standard target. Dualizing gives `delta K + K delta = 1-A S`. The test of all 560 triangles is an independent finite control of these signs, not a substitute for that inductive proof.

## 2. Tensor homotopy and the retained harmonic coordinate

Each coordinate uses the two-open complex for O(n), with delta(f_A,f_B)=f_B-f_A. Here n is 0 or -2. In the global finite frame, the one-factor h is the signed split of C Laurent monomials into A exponents at least zero (minus sign) and B exponents at most n and negative (plus sign). For n=0 the projection picks the B constant; inclusion gives that constant on either vertex. For n=-2 it picks C exponent -1 and inclusion keeps C. Their tensor product gives

    delta h + h delta = 1-I P.

The j-th summand of h has projections on all preceding factors and Koszul sign `(-1)^(number of preceding C states)`. `h_requests` implements this transpose explicitly. The prefix tests are exponent zero with A/B for n=0, and exponent -1 with C for n=-2. It does not replace a prefix projection by support overlap.

For the pair twists (-2,-2,0,0) and (0,0,-2,-2), the tensor H2 has dimension one. Thus

    delta(K + A h S) + (K + A h S)delta = 1-A I P S.

For a closed F this yields `delta B=R Pi F-R A I P S Pi F`, not universal exactness. The actual source's harmonic coordinate has not been computed or proved zero here. The artificial harmonic fixtures have that coordinate equal to one and give a nonzero F with zero delta B; both twists are tested. An actual primitive identity must therefore come from a separate authenticated source theorem or source-specific harmonic witness. A Boolean metadata assertion cannot supply it.

## 3. Exact finite Pi requests

Write the complete cleared numerator on a source-increasing triple as

    P(u0,u1,u2) = C_u0 C_u1 C_u2 F(u0,u1,u2),
    Qhat_u = rho_u/C_u.

For a standard target triple s, the program sums over the bounded artificial owner fibers of its three slots. It binds the occurrence ID `('Pi',s,j)` in every slot and keeps each complete owner. It sorts the source owners once, multiplies by its alternating sign, and asks the already sorted source oracle for P without an additional sign. The resulting coefficient request is

    sum_owners sign(owners) sum_(a0,a1,a2)
      Qhat_u0[a0] Qhat_u1[a1] Qhat_u2[a2]
      P(sorted owners)[e-a0-a1-a2].

Negative or beyond-degree numerator requests are zero by the polynomial premise. This is a finite sum of coefficient demands; it is neither a Laurent-box expansion nor a physical cover enumeration. The enclosure `support_box` uses only degree bounds and extrema of the three finite Qhat supports, and asks no numerator coefficient. Cancellation may make the enclosure loose. All chain operations preserve the finite exponents, so it also encloses B.

The exact formula for Pi requires the supplied Qhat factors to represent the fixed partition quotients. That identity is an explicit oracle premise. The producer fixture realizes it nontrivially: two fibers of weight 1/2, owned C=x0*x1, and Qhat=(x0*x1)^-1/2. Its P=C^3 F is a polynomial. All 560 Pi coefficients agree with an independently supplied whole standard cochain, including negatively oriented source permutations. This control authenticates only the artificial fixture.

Every non-repeated assignment must have a whole-standard-target extension witness bound to all owned clearings and the target triple. The current interface accepts synthetic evidence only. Direct complete tiny Laurent data are separately checked monomial by monomial: a coordinate finite at every target vertex requires exponent >=0; a coordinate at infinity at every vertex requires exponent <=n. Mixed coordinates have no restriction. This checks the complete supplied synthetic coefficient, not a fragment on a smaller common open.

Repeated physical source vertices vanish in the pullback of the already alternating source F. This rule is local to the Pi-F adapter. Equal physical labels with distinct standard tags remain distinct for a general common cochain or output B edge. Output restriction R retains both complete owners; only repetition of the standard tag itself forces the alternating standard cochain to vanish.

## 4. Derivatives, both branches, and the source gate

The K branch is the signed sum over k(edge). The AhS branch takes each AW output cell, executes the tensor-h transpose on the demanded exponent, then its signed input staircases. Both call the same Pi coefficient program. For the fixture F=delta t with t_(0,8)=1 and t_(0,12)=2 at exponent zero, the K contribution on (0,12) is 2 and the AhS contribution on (0,1) is -1. Their sum has delta B=F on every triangle; each branch separately fails. No prism can replace this complete B.

For a complementary derivative d,

    [x^e] partial_d B = (e_d+1) [x^(e+unit_d)] B.

The factor can vanish. Otherwise the shift occurs before any h predicate or branch request. This is a coefficient identity in the finite frame; geometric frame transformations remain an external binding obligation.

The complementary-pair theorem at `02d0e727ffb95dfd9281906cc284c56e8bffd018` supplies an ordered raw F12-to-F34 axis-renaming construction. Its inverse-image raw triple must remain unsorted before nonlinear evaluation. The present structural F34 tests do not establish equality of two source-first alternating cochains, historical values, or source-order changes. A future F34 oracle must implement the freshly evaluated source and the exact shared sorted-source contract, using that ordered theorem correctly.

All oracle modes must be synthetic. Per-request and aggregate query caps bound artificial execution; production fibers cannot pass them. `contract.json` leaves actual numerator identity, partition identity, standard extension, source closure, source harmonic vanishing/primitive identity, physical frame binding, and physical execution unaccepted. The complete coefficient program is executable behind that gate. It supplies no value of the complete closed Rsharp or its obstruction class.
