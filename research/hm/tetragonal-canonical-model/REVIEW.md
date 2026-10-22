# Independent mathematical review

Verdict: **PASS**, conditional on the structural inputs pinned in PROOF.md to PR654 and PR655. No required mathematical correction remains in the reviewed version, including its exact-gonality corollary.

Reviewed file: `PROOF.md`

SHA256: `c252779f204b175938cd567c90291f2585a192bba1fa088f12cd6d76dd620ea2`

Review date: 2026-10-22 (UTC).

This is an independent mathematical argument review, not a proof-assistant certificate or a computer verification of an actual HM instance. The local copies of the two prerequisite proofs were also read for context; their stated pinned conclusions are accepted as inputs rather than independently re-established here. No selected HM coefficient, point, matrix, rank, scan, or large computation was evaluated. The hash records the reviewed bytes only; it does not certify mathematical truth.

## 1. Global complete intersection and generic fiber

The fixed nondegenerate pairing gives a smooth plane conic Q. Restricting O_P2(1) to Q gives O_P1(2), so the second quadric restricts to a divisor of bidegree (4,4). If that restriction vanished identically on a fiber, the two quadratic forms would be proportional, and polarization with the nondegenerate pairing would make M scalar. Both allowed fiber types rule this out. Consequently every fiber has length four; the relative Cartier divisor is flat, and properness with zero-dimensional fibers makes its map finite.

At the generic point, self-adjointness makes distinct eigenspaces orthogonal. None can be isotropic, since an isotropic eigenline would then be orthogonal to the whole three-dimensional space. After rescaling the eigenvectors, the displayed kernel calculation for the squared coordinates is valid. All three coordinates are nonzero and give four projective sign choices. Their gradients are independent: proportional gradients would force all three distinct eigenvalues to agree on nonzero coordinates. Thus the geometric generic fiber is reduced and has degree four.

## 2. Spectral evaluation and the component double cover

The evaluation map pi^*pi_*B -> B is surjective, including at ramification: locally it is the multiplication map from the pulled-back spectral module to itself. Its compatibility with the spectral action says precisely that evaluation, tensored by A, kills N. Dualizing this identity and using self-adjointness gives B^{-1} as a sub-line-bundle of ker N, with no omitted A twist. Since N has constant rank two, that inclusion identifies the two line subbundles everywhere.

The quotient U is locally free of rank two. Its determinant is B because pi^*E has trivial determinant, and the symmetric A-valued form descends to a nondegenerate form on U. Its two isotropic lines therefore form a finite etale double cover. Their inverse images in pi^*E are exactly the two planes whose projectivizations are the two components of the singular plane conic. This construction remains valid at the ramification points; it does not assume that the kernel of N is nonisotropic for b there.

The projective-bundle convention and determinant sign are correct. For the bundle of lines in U,

    omega_p = O_p(-2) tensor p^*(det U)^{-1},
    R^1 p_*O_p(-2) = det U.

Pushing the isotropic-divisor sequence and splitting by trace therefore identifies the trace-free line of its double-cover algebra as det(U) tensor A^{-1}, not its inverse by convention. This is exactly T. Etaleness makes the multiplication T^2 -> O_S a nowhere-zero trivialization. Any two such trivializations differ by a constant in C^*, since S is connected and projective; that constant has a square root. Thus the cover is isomorphic to the actual X_T cover over S, rather than merely sharing numerical invariants. Its connectedness follows from the nontriviality of T.

## 3. The six pairs recover the four-point splitting field

The pencil has exactly the three finite singular members indexed by the distinct spectral eigenvalues, and no singular member at infinity. Each has rank two and distinct line components. Its vertex is the corresponding eigenline and is not a base point. Each component contains exactly two of the four base points. Distinct singular members cannot produce the same partition: the two points of a pair determine its line, and the two lines determine the singular conic. The six components are therefore exactly the six two-element subsets, compatibly with Galois action.

The S4 action on these six subsets is faithful, so the kernel of the absolute Galois action on them equals its kernel on the four points. Their splitting fields agree. Identifying the six-sheeted cover with X_T->L consequently identifies this field with the pinned A4 normal closure Y. The resulting subgroup of S4 has order twelve and hence is A4, with its transitive four-letter action. The generic degree-four algebra is therefore a field whose point stabilizer has order three. Its smooth projective normalization is Y/H over L. This argument does not presuppose that Z is smooth or integral.

## 4. Integrality and smoothness

As a Cartier divisor on a smooth surface, Z is a pure one-dimensional Cohen--Macaulay scheme with no embedded associated points. Every component dominates L because the morphism is finite. Its integral and reduced generic fiber gives one generic component, with multiplicity one. There can be neither another component nor a nilpotent structure supported only in special fibers without an additional associated point. Thus Z is integral and reduced.

Its arithmetic genus is nine by the (4,4) adjunction formula. Its normalization has genus nine by the identified order-three quotient. The normalization exact sequence has a finite-length quotient of length p_a(Z)-g(normalization), hence length zero. Z is normal, and a normal curve over C is smooth. The branch data may therefore be transferred from the already identified quotient without a new branch-fiber calculation.

## 5. Canonical embedding and the quadrics bundle

The adjunction twists are consistent in both surfaces: omega_Z=O_Z(2,2) and omega_(Z/L)=O_Z(2,4) on Q times L, with the latter equal to O_Z(1,4) in P(V) times L.

Twisting the divisor sequence on Q times L yields left-hand term O(-2,0). Its only nonzero direct image is R^1 p_*O(-2,0)=O_L, giving the displayed residue sequence. Relative duality identifies its last arrow with the dual of the unit. Its kernel is therefore the Tschirnhausen bundle, here H^0(Q,O_Q(2)) tensor O_L(4)=O_L(4)^3. Evaluation is restriction of these three quadratic sections of Q, so the resulting plane map is the given degree-two Veronese embedding, including on the finite nonreduced fibers.

For the complete-intersection ideal I in P2 times L, the twisted Koszul sequence is explicitly

    0 -> O(-2,4)
      -> O(0,8) plus O(0,4)
      -> I(2,8) -> 0.

All cohomology of O_P2(-2) vanishes. Thus p_*I(2,8)=O_L(8) plus O_L(4), and R^1 p_*I(2,8)=0. Pushing the ideal restriction sequence identifies this bundle with the kernel of Sym^2 E_h -> h_*omega_(Z/L)^2 and proves that map is surjective. This establishes the stated F splitting with the correct twists, not merely its rank or total degree.

The second projection is finite of degree four: an integral divisor of bidegree (4,4) cannot contain a fiber as a separate curve component. Together the two projections are the existing closed embedding, as claimed.

## 6. Exact gonality

The added corollary is correct. The degree e of Z over the normalization of its image under a hypothetical degree-n map together with h divides both n and four. If e=1, the normalization genus is at most the arithmetic genus 3(n-1) of its integral image, contradicting genus nine for n=2 or 3. The only other possibility is n=e=2. The intermediate function field then has degree two over C(L), so Galois correspondence in Y would require an order-six subgroup containing H. Such a subgroup cannot exist in A4: its index would be two, whereas all three-cycles, which generate A4, map trivially to C2. Degree one is excluded by the genus. Hence the gonality is exactly four.

## Scope and conclusion

The proof rigorously identifies the actual Gram-conic construction with the pinned tetragonal quotient, proves its smooth (4,4) model, determines its relative canonical twists and F=O(8) plus O(4), and proves exact gonality four. The component-cover identification is essential and has been checked, rather than replaced by a degree or genus comparison. The stated exclusions concerning additional HM symmetry, Prym claims, the original genus-four support, and the unresolved R-class and Bockstein questions remain appropriate.

Two clarity improvements were incorporated before final review: the component cover is named X_comp to avoid conflict with the original support D, and the full vanishing of the Koszul relation's plane factor is explicit. These do not change the argument's mathematical content. No further correction is required.
