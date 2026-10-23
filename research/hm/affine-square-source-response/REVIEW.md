# Independent affine-square review

Verdict: PASS for the stated conditional theorem and missing-certificate boundary. No blocking mathematical correction found. This is an authored mathematical review, not formal proof-assistant certification or an actual-source evaluation.

Reviewed final file: `work/swarm/affine-square/PROOF.md`, SHA256 `78a0f462ffd0710d248658aaf95926f926297b0bae43aade85eb4c7fc934d236`.

## Sources actually read

Read the full pinned PR780–783 proofs and PR685, already saved in this reviewer directory, and fetched the exact PR683 proof at `d4008b924e9ddff9726f86ccccc1574677da9218`. Also fetched the actual fifth-neighborhood ladder and cyclic Rao vanishing note at `8d8b5be4ce62c3055bb53be9e16d29cc63072f04`.

The three new exact local copies and SHA256 hashes are:

- `affine-pr683.md`: `bb8635e4f411cdd4e810ee73ac24db949b45fc4ace521cfc9c8b16b0f9f7e88e`.
- `affine-ladder.md`: `1827de5e5358d10c7a7d498b7b8ca767da8510cd632b40818fb5add1356e5c1d`.
- `affine-vanishing.md`: `03a0c6a6f52dbfeeb44003f4a29bff2fb150cb29516916007dd5ec53d33adcab`.

These sources explicitly support actual ambient H0(B(4))=0, termwise acyclicity of the full monad endomorphism complex at twists at least two, full-cochain comparison on thickened quadrics, and the precise signs of the C_h/E_h source equations. No supported-middle exclusion is substituted for them.

## Affine transport and square compatibility

1. The weight-twelve ladder has coefficient weights 12,8,4,0 and twists 10,8,6,4. Its exact homogeneous reference gluing follows because a remaining q^4 discrepancy would have matrix weight -4. The next layer begins at weight sixteen and has no q^0 term in the normalized N frames. The distinction e in twist four versus a e=B3 in twist six is preserved.
2. qZ raises matrix weight by four, so its action on the entire leading ladder contributes at precisely the layer under review. Its q^3 coefficient contains c0 at harmonic order two, c1 at order one, and c2 at order zero. c3 starts at q^4. In particular, c2 has weight four and can have an upper entry. Copying the old weight-zero N0 formula would be false here.
3. The displayed full conjugated commutator (10) has the correct diagonal, upper, and lower terms. The affine shift F and its sign follow directly by extracting the q^3 coefficient of (5). Equation-line factors are transported before extraction. Exact reference transport plus the first actual transition cocycle gives the affine composition law; it does not require kappa to vanish.
4. At total weight twenty-eight the norm tr(J4^2)/2 contributes tr(LD), with no remaining factor two. The five lower harmonic terms are exactly (c0,s,order2), (c1,s,order1), (c2,s,order0), (c0,r,order1), (c1,r,order0). Only c0 couples with q^3 e. All terms have cover degree sixteen and physical twist fourteen. A=a^3 h has degree four/twist eight; tau(e) has degree twelve/twist six, hence coefficient line O(6-12/2)=O.
5. tr(L[Z,L])=0 gives scalar compatibility only after the full matrix law has been retained. Vanishing of the lower scalar q coefficients is necessary to obtain the pure scalar transition at order three; the draft explicitly imposes this for hypothetical data. The sign A tau(F)=lambda(Q_j)-Q_i is correct.
6. Regular image membership is a sheaf statement, not division at individual source fibers. Multiplication by nonzero a^3 h is injective over each integral base-open polynomial ring even where its fiber vanishes. Once the supplied scalar datum lies in this image, the old surjective trace sequence supplies local preimages; the affine defects lie in U O(-1), and H1=H0=0 gives existence and uniqueness. This remains conditional on independently supplied rho16 and valid lower compatibility.

## Full-source factorization and scope

The complete global twist-four complex has ker d=im d by the stated cohomology comparison and ambient vanishing. For an authenticated local monad contraction, p d_M=0 and d_M i=0 imply p(dY)i=0 with the Hom-complex signs. Thus the actual projection P kills all global closed cochains, not merely the chosen primitive ambiguity. The trace-extraction map ell therefore factors uniquely through the actual image of D. No extension off this image or H1 factorization is claimed.

Applying P to nonclosed aJ3 is legitimate as a local cochain projection, but it need not give an intrinsic global adjoint. The draft explicitly preserves that limitation. Applying the same P to J4 does give the actual section modulo q^4 because dJ4=q^4 W_h. O-linearity of the same contraction, and compatibility with q, then give e=y-[P(E_h)|Q]_[4]. Substitution yields the minus sign in (24) and retains both -a b Z_a and -q W_h.

The certificate is not tautological provided L is independently assembled from the physical contraction on the complete degree-zero basis, then checked as L=Lambda D. Its evaluation still needs the corrected differential input, lower cochain y, fixed physical normalization, and overlap checks. The draft calls all of these missing; it supplies neither an actual physical P nor a value of rho16/beta4. No invariance under changing a nonclosed contraction, no computation-size benefit, and no fifth-boundary conclusion are inferred. This avoids overlap with null's separate contraction-change investigation.

## Counterexample-oriented checks

The reviewer-owned `affine-formal-review.py` uses only Python standard-library exact sparse Laurent polynomials with free coefficients. It verifies (10), trace cyclicity, the norm cross-term normalization, the five harmonic-index pairs, and nonzero entries lost by the weight-zero shortcut. It passed. No actual source coefficient, derivative, rank, or instance was used. An initial attempted SymPy invocation failed at import because system Python lacks SymPy; the replacement checker has no such dependency.

The review also tested the logical failure modes: omitting the c2 upper entry, dropping qZ because its scalar pairing vanishes, cancelling a on a zero fiber, applying H0 vanishing to only a supported middle block, treating arbitrary nonclosed projections as global, or obtaining rho16 from the unknown J4 itself. Each is excluded by the current statement or required certificate. The final stopping point is accurate.
