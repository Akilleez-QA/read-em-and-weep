# Exact affine two-pivot refinement experiment

The executable verify-affine-pivot-refinement.js reconstructs the known monad and normalized local contractions, then executes 18 additional exact polynomial assertions for a two-principal-open refinement on the all-finite chart. This is an affine-local scalar contraction applied entrywise to an actual rank-two transition matrix. It is not a global original-cover comparison and does not project the E residual.

## Actual chart domains

On v₀=1 write a=v₁,b=v₂,c=v₃,d=v₄, and put f=1−abcd and g=acd.

The primary β and α pivot determinants are −f and f. The auxiliary determinants are cd and −a²c. Thus the primary contraction exists on D(f), while the auxiliary contraction exists on D(g). The auxiliary symplectic normalization multiplies its second column by −d/a² and its second projection row by −a²/d; both are units on D(g).

The identity f+bg=1 proves D(f)∪D(g) covers this entire affine chart. Pulling back along a=e₁(x),b=e₂(x),c=e₃(x),d=e₄(x) preserves the identity, hence gives the corresponding cover on the all-finite chart of C⁴. The frame of N on that chart is 1.

## Fixed common denominator certificate

The direct normalized matrix is G₀*=P₀I_*, mapping auxiliary coordinates to primary coordinates (equivalently I_*=I₀G₀* in cohomology) in the common four-term basis. The reconstructed code checks that its displayed common denominator is

f²a⁴c²d.

Multiplying its numerator and denominator by f²c²d³ puts every entry over the single denominator f⁴g⁴.

One common exponent-four Bézout identity is obtained from (f+bg)^7=1. Define

A_f=Σ(k=4,…,7) binom(7,k) f^(k−4) b^(7−k) g^(7−k),
A_g=Σ(k=0,…,3) binom(7,k) f^k b^(7−k) g^(3−k).

Then f⁴A_f+g⁴A_g=1, checked as a polynomial identity. The same A_f,A_g are used for all four matrix entries.

For u=M/(f⁴g⁴), define the affine vertical contraction

h(u)=(−A_g M/f⁴, A_f M/g⁴).

The first component is regular on D(f), the second on D(g), and their difference is u. With weights λ_f=f⁴A_f and λ_g=g⁴A_g, the projection is p(a,b)=λ_f a+λ_g b. The executable verifies d h=1 and p h=0 on every actual normalized transition coefficient, together with the coefficient identity for h d+i p=1.

These calculations certify denominator clearing and the scalar contraction on this finite coefficient domain. Matrix entries are interpreted in the common rational coefficient field. Entrywise contraction alone is not a contraction of the twisted End(E) Čech complex; its frame transport and total-complex comparison remain necessary.

## General exponent formula and next use

For any required common denominator exponent n, expand (f+bg)^(2n−1). Assign terms with f exponent at least n to λ_f and the remaining terms to λ_g. This produces polynomial A_f,A_g with f^n A_f+g^n A_g=1. This formula is exact, but a larger n for the actual first- or second-order E residual has not been selected or executed here.

The local test supplies a genuine low-cost principal-cover contraction. Extending it globally still requires the other original elliptic intersections, line-frame refinements, common bounds for every residual and correction coefficient, and the horizontal double-Čech HPL correction. Neither the E calibration nor a second-order value follows from this experiment.


## Executed extension to the free End(K) coefficient module

On the all-finite chart, the four-term K has a global free basis with ranks (5,15,10,2) and N frame 1. The executable assembles its actual polynomial differential from γ,δ,ε in the reconstructed contraction certificate.

It then performs 5,120 additional exact assertions on all 1,024 homogeneous 32-by-32 matrix units:

- [d,[d,F]]=0, with the graded commutator signs;
- [d,wF]=w[d,F] for each fixed weight w=A_f,A_g,λ_f,λ_g.

Because the differential and these multiplication operators are R-linear, checking all homogeneous matrix units verifies these identities on the entire coefficient module over R and its localization. In particular, the affine scalar denominator-clearing contraction may be applied entrywise after converting a residual to the free End(K) basis. It is not necessary to contract twisted End(E) frame coordinates directly.

For refinement degree q, the total internal differential is (-1)^q[d,−]. The homotopy h lowers q by one. The checked ordinary commutation therefore becomes the required anticommutation D_internal h+h D_internal=0. Restriction/inclusion and the weighted projection commute with the internal differential. Thus no extra affine internal HPL correction is required for this R-linear scalar contraction.

For any finite numerator input space and a chosen denominator exponent n, a finite verification domain can be formed from its images under [d,−], h, i p, and their nonzero compositions. The identities [d,−]²=0, h²=0, h i=0, p h=0 and the checked commutations bound those compositions. Polynomial numerator degrees may increase under the fixed weights and the internal differential; the domain must include those images rather than imposing an unsupported fixed Laurent cutoff.

The exponent-four test certifies the displayed transition-coefficient domain and the End(K) module identities. It does not yet assert exponent four is sufficient for the actual transferred first-order E residual. That residual and its complete correction domain remain to be supplied and checked.

Run from the repository root: `node research/hm/verify-affine-pivot-refinement.js`.
