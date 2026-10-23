# Independent review: forced quartic V subsystem

## Verdict and reviewed snapshot

**PASS**, conditional on the explicitly stated source, zero original determinant defect, profile (1,1), and nonzero internal channel J=O(-10). This is a structural missing-dependency resolution, not a source or stable-label exclusion.

Reviewed proof: `BF-SUBSYSTEM.md`.

Reviewed SHA256:

    087d0b78196b7c0d5e773375e603359450e0e9fb0ebb3003734c44eea4e133b9

This review concerns the mathematical claims in precisely the displayed proof snapshot, including its exact dependency pins and actual-connection argument. No mathematical blocker remains.

## Independent checks

### 1. Top quotient, kernels, and linear first transform

The strict-top vanishing makes the nine coefficient sections of F(2) independent. A generic rank-one image in W O(7) has saturated line degree at most seven and thus at most eight sections, a contradiction. In generic rank two, the globally generated image has h0=16-delta, so delta<=7. Its invariant torsion divisor must therefore be empty. This proves actual everywhere-surjectivity of p, not merely a necessary abstract Hom condition.

The representation identities give H1(K0(2))=V+P and chi_G(K0(3))=0. The four supported negative blocks in the cited bounded argument have respective twist-two contributions V, P, P, V+P. Matching their twist-three contributions yields exactly the three displayed kernels, each of rank seven and degree -28. The first two internal maps vanish by degrees and irreducibility. In the third, the only channels from O(-10) are the complete quintic tautological channel into T O(-5) and the scalar channel into O(-10). Each nonzero combination has saturated line image.

The saturated-image lemma applies without alteration to the rank-two external quotient. In the J=O(-10) branch it gives rank F^+=12 and degree -12. First-polar generation gives only degrees -1 and 0; the two Euler characters in the proof then force the pure linear bundle (Wp+S+T) O(-1). In particular, no endpoint section-freeness assumption was used.

### 2. Universal coefficient-kernel identity

Let L=O(-1) on P(W), let a:U tensor W -> C be the surjective coefficient map, and set K=ker a. The actual subbundle condition says that K O intersects U tensor L trivially at every fiber. In the tautological sequence

    0 -> U tensor L -> (U tensor W) O -> U tensor (W/L) -> 0,

the projection identifies K O with the kernel of U tensor (W/L) -> (C O)/(U tensor L). The canonical derivative identifies L with (W/L) tensor Omega1, since det W is trivial. Tensoring the preceding kernel statement with Omega1 gives exactly

    (U O(-1))^- = K tensor Omega1 = K O(-2).

This proves the twist, actual embedded kernel, and saturation. It is valid universally, without evaluating coefficients or a selected point.

For U=Wp+S+T, F lies in this kernel because F^+=M. Since both F and the kernel are pure degree -2, this is an injection of constant representations P+D -> K. A saturated negative rank-twelve subbundle cannot fill a twelve-dimensional constant span, so dim C>=13 and dim K<=11. The quotient after removing P+D is a subrepresentation of A+V+P+D, which has no nonzero representation of dimension at most two. Hence K=P+D and C=A+V+P+D, as claimed. The actual first forward transform of any linear bundle is its full coefficient span.

### 3. Exhaustive quotient classification and quartic flag

Q_C has rank three, degree twelve, and is globally generated. A degree-zero summand would give a nonzero constant functional on C annihilating M. Since C is the full span, no such summand exists. The cohomology of M gives C=H0(Q_C), so the quotient map really is the complete evaluation map.

For a positive equivariant splitting block R O(d), its evaluation kernel is R tensor Sym^(d-1) W O(-1), and its backward kernel is R tensor Sym^(d-2) W O(-2) when d>=2. The latter is zero for d=1. Under the complete evaluation identification, a d=1 block cannot be regained by the forward transform of M^-; thus (M^-)^+=M excludes it.

The rank-three center-even possibilities with all degrees at least two are exhausted as follows:

- Three trivial even lines: the partitions of total degree twelve are (2,2,8), (2,4,6), and (4,4,4).
- An odd two-dimensional irreducible and one even line: the degrees are (3,6) or (5,2), with the two-space W or Wp, giving four rows.
- One even three-dimensional irreducible: degree four, with representation A or V, giving two rows.

These are precisely the nine rows in the proof. Their listed H0(-1) representations are correct. For example Wp tensor Sym2 W=T, Wp tensor Sym4 W=S+T, A tensor Sym3 W=W+S+T, and V tensor Sym3 W=Wp+S+T. Therefore only V O(4) has the required Wp+S+T section representation.

The full evaluation sequence of V O(4), not an arbitrary abstract splitting, now identifies the embedded subsystem. Its canonical successive kernels are obtained from the powers of the tautological line in Sym4 W:

    M=V tensor Sym3 W O(-1),
    F=V tensor Sym2 W O(-2),
    F^-=V tensor W O(-3),
    F^{--}=V O(-4).

The corresponding representation decompositions in the proof are correct. No horizontal splitting of E has been inferred.

### 4. Endpoint image and final connection argument

The degree -3 part of K0=T O(-3)+O(-10) is canonical, and the inclusion F^-=T O(-3) into it is an isomorphism on that part. Consequently K0/F^-=O(-10), while the standard quartic quotient gives F/F^-=V O. This proves the exact sequence (8).

The quartic derivative F^- -> (F/F^-)(-2) is onto as a bundle map. Composing with (8) yields an everywhere-surjective map onto W O(3) in (E/E^-)(-2). Its negative component vanishes because it comes through F, whose map to O(-10) is zero. Since the full endpoint derivative has generic rank at most two, its image cannot contain anything further: modulo the exhibited W O(3), any extra image would be a torsion subsheaf of the line O(-12), hence zero. This proves the exact quotient W O(3) and the absence of a torsion correction.

The actual forward transform of E^- is therefore the preimage of W O(5) under E -> E/E^-. That is precisely E', the kernel of the negative quotient E -> O(-10). Only the O(-10) summand of E can map to that target, and the quotient is onto, giving the asserted splitting of E'.

Writing K=E^-, actual derivatives of K lie in E'=(E^-)^+. Thus beta_(E') kills K. Its projection to Q(-2) induces the saturated injection E'/K=W O(5) -> Q(-2), so beta_(E') has kernel exactly K and image isomorphic to W O(5). Saturation of the full image follows, for example, from the locally free quotient extension

    0 -> (E/E')(-2) -> ((H O/E')(-2))/image(beta_(E'))
      -> Q(-2)/(W O(5)) -> 0.

This checks the final connection step using only the actual ambient connection. It yields (E')^-=E^-, E'/E^-=W O(5), and (E')^+/E'=W O(7). No connection on a chosen abstract complement is used.

## Exact inputs checked

The stable-label JSON record identifies G3.11.73682b4c817f with source_index72, A_q=O(-10)+W O(5), B_q=W O(-7)+O(8), and original defect zero. The source_index72 quotient record contains the tuple (0,1,0,0,0,1,0,1), which gives the stated source through the original splitting formulas.

The following immutable input bytes were read and their Git blob hashes independently recomputed. They match the dependency manifest.

At original commit `db51525015bb7c5e825833d550d08dedf6f6ea96`, under `research/hm/order-four-quadratic-load/`:

- ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md: b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3
- NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md: d7506dae49b4be43230450c4132bd5db91f137ef
- ONE-ONE-ENDPOINT-DEGREE-WINDOWS-AND-159-NECESSARY-PAIRS.md: dcacf0bcdef8377c1ed7654e5b82659ea409456e
- one-one-endpoint-necessary-pairs.json: fe0afa410d89340d3082dc814277f89fbb582c19
- rank-three-quotient-frontier-144.json: 8b5971092f9ef762584912609fd5e9301c4e271d

Public original input directory:

https://github.com/Akilleez-QA/read-em-and-weep/tree/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load

PR796 proof at commit `d2b43060c83328dd5118aee6b9288fcfa0c873ac`, blob `46a0de762000f21182f6d3168f3ecfd63adaf75f`:

https://github.com/Akilleez-QA/read-em-and-weep/blob/d2b43060c83328dd5118aee6b9288fcfa0c873ac/research/hm/profile12-quadratic-block-exclusion/PROOF.md

PR799 proof at commit `2172e4a7abbbe232f9f448bea6fa01dee7927460`, blob `a62a56f6b8f97e02b3eab6fe3a47ec3bedb6c6b1`:

https://github.com/Akilleez-QA/read-em-and-weep/blob/2172e4a7abbbe232f9f448bea6fa01dee7927460/research/hm/profile11-quadratic-polar-obstruction/PROOF.md

The reviewed result does not depend on PR802. No selected actual HM/source coefficients, parameters, points, derivatives, matrices, instance ranks, model experiments, large computation, or external writes were used in this review. This is a mathematical written review, not proof-assistant certification.
