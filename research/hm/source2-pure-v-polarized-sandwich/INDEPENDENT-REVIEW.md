# Independent review: polarized sandwich vanishing

## Verdict and scope

PASS. Under the retained actual source2 pure-V hypotheses, hT_a h=0 is proved as a literal map identity. All mixed endpoint products and the stated middle products then vanish literally. The alternating cross defect is correctly retained rather than declared zero, and its canonical 29-to-28 factorization is justified.

Reviewed PROOF.md SHA256:

    8ef5300690ee419123a318c6ede034cfedb2da20bff3b20cec23a07326918f66

Reviewed verify.py SHA256:

    3e5eddb7d85f713955c0ad7b77c0191dbd457017e3d9ae0a02d48fe62f556e4c

No actual coefficient, orbit representative, source realization, or higher-obstruction value is selected. In particular this result does not choose or exclude either actual quadratic-lift coefficient.

## 1. Fresh input authentication

All four inputs were independently fetched through the GitHub connector at their exact commit and repository path. Returned UTF-8 contents matched the retained bytes exactly; independently recomputed SHA256 and Git-blob SHA1 values matched INPUTS.json. Matching blobs are:

- PR1019 at 3fb2475ffb275c5789acbaa8f9f84ed272713785: bf63c14f76933d59fa7e3ac61aecb3366ac1b442.
- PR1022 at 5488bc153029391d647c3e18d9344e4e00e38a7f: ed25430f8e5ffb0f46c2b642d8d27467db492985.
- PR1025 at 09f1377f83b027ca27eea0b3a9f40a1b92c6c466: d036adcf5bc2bfc53e07cd752ff180c5993251f7.
- PR792 at 2f01f18960ce56b8b2a0c1260c277de3c5f916bf: 76bee93507d1a2d0840926d4e4e27edadfebb7d7.

This authenticates the direct dependencies; it is not a claim to have freshly replayed all transitive geometric proofs. The relevant exact identities and quotient-second statement were read in those retained sources.

## 2. Actual versus cohomological maps

The types are Q,T_a:N2→N4 and h:N4→N2. Thus H_a=hT_a h:N4→N2 is well typed. Using only the retained actual identities gives

    QH_a=j4 T_a h=T_a j2h=0,
    H_a Q=hT_a j2=h j4 T_a=0.

The first equation alone puts the image in ker Q, and the leading h also puts it in im h. Their exact intersection is D. The second equation makes H_a descend through coker Q=P. Since T_a depends linearly and equivariantly on a, the entire family is a global bundle map P O(−1)→D O. This is a deduction about actual maps, not a lift inferred merely from their action on cohomology.

The distinction is particularly important later for C_ab on ker Q. The complex starts in N2, so H0 is the actual kernel, with no incoming boundaries. Moreover PR1019 already puts hT_a(ker Q) in D. Its asserted H0 formula is consequently the exact equality hT_a(x+d)=mu a x in that embedded D, not equality modulo an unidentified boundary space.

## 3. The corrected quotient lift and the raw second class

For y∈N4, hy represents a quotient Q-cycle because Qhy=j4y lies in I1. Replacing y by Qv changes hy by j2v∈D, so the quotient-cycle class depends only on coker Q. Its connecting image is j4y. This identifies its domain isomorphically with the canonical P component of H0(U): equivariance and Hom_G(P,A)=0 rule out an A-valued mixing.

Because T_a h(N4)⊆im Q, a correction z satisfying Qz=−T_a hy exists. The quotient first differential vanishes globally, so [T_a z] is the raw quotient second class in H1(U). PR1022 says this class is zero on that P summand. This is stronger than being zero after quotienting by the A second image, and is exactly the premise needed here.

Applying the isomorphism induced by j4 gives the literal equation

    0=j4 T_a z=T_a j2z=T_a hQz=−T_a hT_a hy.

Since H_a y lies in D and T_a|D=L_a, the last expression is −L_a H_a y. The sign is correct. A change of correction cannot invalidate the conclusion because it computes the established raw second class; alternatively a fixed linear splitting of im Q can choose these corrections uniformly.

Thus L H=0 globally. The exact kernel sheaf is O(−4) for L:D O→P O(1). Any factorization of H:P O(−1)→D O through that kernel belongs to

    Hom(P O(−1),O(−4))=P*⊗H0(O(−3))=0.

Hence H=0 as a global sheaf map and as a homogeneous linear polynomial family. This step correctly uses the actual kernel sheaf, including its behavior at rank-drop points. It does not assume that pointwise kernels vanish or use a generic rank calculation to kill a torsion ambiguity.

## 4. Mixed endpoint and middle products

Both endpoint products contain a consecutive vanishing sandwich:

    (hT_a)(hT_b)=(hT_a h)T_b=0,
    (T_a h)(T_b h)=T_a(hT_b h)=0.

The Q-chain property follows separately from QhT_a=T_a hQ. No cross-direction relation involving T_b is used. The parameter map A→End_Q(M) is injective because its action on the actual A part of ker Q is the nonzero scalar mu times multiplication by a; multiplication by a nonzero binary form is not the zero operator. Its image is therefore a three-dimensional square-zero subspace. Adjoining the identity gives the stated G-stable algebra C⊕A with zero radical product. It need not be an algebra of fixed-negative-pencil endomorphisms.

The middle types are X_l:N2→N3 and Y_m:N3→N4, so S_lm=X_l hY_m:N3→N3. Crucially, every linear factor belongs to the same fixed negative two-space W. Thus Y_m X_r=T_mr with mr∈Sym²W=A, exactly the family for which sandwich vanishing was proved. The product is consequently

    S_lm S_rs=X_l(hT_mr h)Y_s=0.

The explicit W-only restriction is essential. For unrestricted ambient linear forms the product need not lie in A, and the argument would not justify the same conclusion. The final proof contains the required restriction and makes no extension of h to a graded module map.

## 5. Cross defect and exact subquotients

For D_b(t)=Q+tT_b, direct expansion gives

    D_b(t)K_a^0−K_a^1D_b(t)=t(T_b hT_a−T_a hT_b)=t C_ab.

The Q terms cancel, but the remaining expression is not forced to vanish by the sandwich identities.

On x+d∈ker Q=A+D, the exact H0 formula and actual restricted multiplication yield

    C_ab(x+d)=mu([b a x]−[a b x])=0.

This uses ordinary multiplication in the pinned image module, not a hypothesized commutation of h with different T maps. Sandwich vanishing separately gives C_ab h=0 and h C_ab=0. Each term also lands in im Q because T_a h and T_b h do. These three statements prove the canonical factorization through N2/(ker Q+im h) into ker h∩im Q.

The source character calculation uses the exact intersection im h∩ker Q=D, giving ker Q+im h of character A+D+P. Subtracting from N2=A+2V+3P+4D gives 2V+2P+3D, dimension29. On im Q, h has image D, so the target character is (2V+3P+3D)−D=2V+3P+2D, dimension28. In fact ker h⊆im Q also follows from Qh=j4 and ker j4=im Q; the displayed intersection is therefore consistent with the dimension of ker h itself. No arbitrary splitting is needed for the factorization.

## 6. Independent synthetic control and its limits

The reviewer independently rebuilt the synthetic maps by their basis images and checked all polynomial identities with independent coefficients. In particular:

- The square-zero radical, Q-compatibility, negative multiplication compatibility, side conditions, and both sandwiches hold.
- The quotient connecting cycle admits the explicit first correction, and its next T-image is literally zero, verifying raw quotient-second vanishing there.
- C_ab annihilates the entire Q-kernel and im h, lands in im Q∩ker h, yet has the nonzero entry a0 b1−a1 b0.
- With four fully independent linear-factor pairs in the same W, the single symbolic middle product S_lm S_rs is zero; the contraction Y_m X_r is exactly T_mr.

This control demonstrates that the displayed formal chain/sandwich identities, even with commuting negative linear arrows and the illustrated quotient-second zero, do not by themselves imply cross-direction commutation. It lacks the actual source's characters and nonzero A-to-D channel and is correctly not offered as a source realization or as a counterexample to all possible additional geometric constraints. It also does not prove that an actual C_ab is nonzero.

## Reproducibility

The reviewer replayed `python verify.py` and `python -O verify.py`: all 37 checks passed with byte-identical output. The independent symbolic control described above also passed. These finite checks verify algebraic consistency and bookkeeping; the written corrected-lift and negative-twist argument, together with the authenticated geometric inputs, proves the actual sandwich theorem.

No unsupported cross-direction intertwining, actual coefficient equation, or source exclusion is asserted. No further correction is required.
