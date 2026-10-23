# Independent review: the source127 a-c-f-f exclusion

## Verdict and exact scope

**PASS.** The frozen proof establishes the exclusion of the single original source edge consisting of source_index 127, label `G3.11.cce6e3ba4eeb`, and E-type `(1,0,1,0,0,2,0,0)`. In particular it excludes

    E = 2D O(-2) + Wp O(-3) + V O(-4) + 2O(-8)
    A_q = O(-8) + O(2) + O(16)
    B_q = O(-18) + O(-4) + O(6), original defect zero.

It does not exclude all E-types compatible with the catalog pair, the entire stable label, or the separate c-d-f family. It proves no larger generic-rank or section-count conclusion. No unpublished Wp-block reduction is used.

The review independently derives the sheaf-theoretic and representation-theoretic steps below. There is no mathematical correction required to the frozen proof. The source convention concerning defect zero is made explicit below so the actual Gauss quotient is not confused with an arbitrary bundle having the same splitting.

## Frozen files and authenticated inputs

Review date: 2026-10-23 UTC. The reviewed files have SHA-256 hashes:

    PROOF.md
    a886ede0c620726e422df8b897cdfaaa35da6d3698fb2130fa4d90d517c5e72d

    verify.py
    92259305ce90738278a8ea480af0a860556cf5f7bcbcd448bbb489338e3168d7

    REPRODUCE.md
    c1d043f85fb12dcee374045ba0fdf6080406a49bba421d7996036e3b8ddd7637

    audit-inputs/manifest.json
    cdec01cc7a1790cfa272ff3ad390f4b1117bff2ba3482ee92254152676387e26

The four immutable original inputs are at commit
`db51525015bb7c5e825833d550d08dedf6f6ea96` of
`Akilleez-QA/read-em-and-weep`, with exact source URLs and paths in the manifest. I read the actual-presentation and strict-top notes and independently inspected the relevant original records in both catalogs. Their Git blob hashes were authenticated using `SHA1("blob " + byte_length + NUL + bytes)`:

| Input | Git blob | SHA-256 of input bytes |
|---|---|---|
| ACTUAL.md | b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3 | a52685fc9e7c89abf26171a15989cedeaf3bd101a2edde790a24f9cfe0179256 |
| STRICT-TOP.md | d7506dae49b4be43230450c4132bd5db91f137ef | 53ff5daf7e656bb1ec2dcf5feebd2813e2dbfbd6489a3a65117960f492b4cc08 |
| pairs.json | fe0afa410d89340d3082dc814277f89fbb582c19 | 6002ad138a41d98c351130a29703722979f31b8da90d7c75a120f28bf89480eb |
| frontier.json | 8b5971092f9ef762584912609fd5e9301c4e271d | a6fc9ec680d1866782e0233c234c5d80d398e9fc77734b59e61040ffc92021ad |

The original pair at zero-based index 127 has exactly the displayed A, B and defect, and contains the displayed E-tuple. The frontier record has exactly the stated ID, source index, A, B and original defect. The review does not infer exclusion of its other compatible E-types.

Running `python3 verify.py` completed successfully with the stated PASS. Separately, without importing that verifier, I recomputed the required finite representation identities using the McKay multiplication rules in Section 3 below. I performed no selected actual HM/source coefficient, parameter, point, derivative, matrix, instance-rank, local-model, or scan evaluation. There was no large computation. The frozen proof and verifier were not edited.

## 1. Actual assumptions and the zero-defect convention

The actual-presentation note supplies a saturated full-span E in a constant thirty-space, with no constant subbundle, and the legitimate equivariant splitting formalism. Its presentations recover the ambient representation, if desired, without an additional input:

    [H] = [M3 tensor W] - [M2] - [M4]
        = 2A + 2V + 2P + 2D.

Here this is equivariant K-theory followed by Euler characteristic of the actual exact sequences, not an assumption that their splittings are horizontal. The displayed E-tuple has rank 17, degree -54 and top coefficient 2D at degree -2. The strict-top theorem gives H0(E^-(2))=0.

The catalog is used in its actual Gauss-quotient meaning: A_q is the source quotient of the second fundamental form, and original defect zero means that its injective map to the saturated derivative image has no torsion cokernel. Consequently

    E^+/E = A_q(2) = O(-6) + O(4) + O(18).

Equivalently this is the actual input in display (1) of PROOF.md. Merely postulating three abstract line bundles with those degrees would not suffice. The high line L=O(18) is a saturated subbundle of Q: it is a direct summand of E^+/E, which is saturated in Q because E^+ is saturated in the constant ambient bundle. The rest of the argument uses this actual quotient and never a presumed horizontal splitting.

## 2. The image and saturation lemma is valid

For the saturated F under discussion let beta_F have raw image I in (H O/F)(-2). Under projection to Q(-2), its image is L0 and its kernel is precisely the internal image J of K=ker(beta_E|F) in (E/F)(-2). Thus

    0 -> J -> I -> L0 -> 0.

If J and L0 are saturated in their respective targets, the quotient by I fits into

    0 -> (E/F)(-2)/J
      -> (H O/F)(-2)/I
      -> Q(-2)/L0 -> 0.

Both ends are locally free, so the middle is locally free. Therefore I is saturated. The preimage M of I(2) in H O is the raw first span, is already saturated, and satisfies

    0 -> F -> M -> I(2) -> 0.

For quadratic F the first polars give a surjection from D tensor W tensor O(-1) onto this raw M; Euler's identity also includes the values of F. Hence M(1) is globally generated. A subbundle of a constant bundle has no positive splitting degree, so every degree of M is 0 or -1. Its degree-zero part is its actual constant subspace H0(M), not just a virtual character.

Most importantly, if N=E intersection M, then as an actual subbundle of E/F,

    N/F = J(2).

This follows by taking the kernel of M/F=I(2) -> Q. It identifies the location of N/F, not only its abstract isomorphism type.

## 3. Independent fixed representation calculation

I used the following multiplication-by-W rules, independently of the supplied quadratic-field character-table implementation:

    W one = W          W W  = one+A       W Wp = P
    W A   = W+S        W V  = T           W P  = Wp+T
    W S   = A+D        W D  = S+T         W T  = D+V+P.

For each fixed irreducible U, the recurrence

    U Sym^(n+1) W = W(U Sym^n W) - U Sym^(n-1) W

gives all products needed here. In particular:

    Sym6  W = V+P
    Sym12 W = one+A+P+D
    Sym14 W = A+V+P+D
    Sym16 W = V+P+2D
    Sym17 W = Wp+S+2T
    Sym18 W = A+V+2P+D
    Sym19 W = W+Wp+S+2T

and

    Wp Sym3 W = V+D,       A Sym3 W = W+S+T.

This check uses only fixed abstract irreducible multiplicities, with small degree bounds forced by the proof.

## 4. Forced high-only D and its exact kernel

Strict-top makes the section map

    2D = H0(E(2)) -> H0(A_q(2)) = Sym4 W + Sym18 W

injective. There are precisely two D copies in the target, one in each of its low and high rows. The resulting map on two-dimensional multiplicity spaces is therefore an isomorphism. The low-row kernel is one constant D multiplicity subspace and gives a saturated F=D O(-2); its high row is nonzero and its five coefficient sections are independent.

The high row is a degree-18 D covariant. Its common divisor is G-invariant. Independence bounds its degree by 14, since after removing a divisor of degree d one needs at least five independent sections of O(18-d). A nonempty invariant effective divisor on the icosahedral projective line has degree at least 12; the center excludes odd invariant polynomial degrees and Sym14 has no invariant. The remaining possible degree 12 would leave a D in Sym6=V+P, impossible. Thus F -> O(16) is surjective as a sheaf, not merely generically surjective. There are no other external rows for F.

From this exact sequence the kernel K has rank 4, degree -26, H0(K(2))=0,

    H1(K(2)) = A+V+2P,
    chi(K(3)) = -W-Wp-T.

All its degrees are at most -3. For an irreducible atom U O(-j), j>=4, the H1(K(2)) contribution is U Sym^(j-4) W. Positivity gives dim U<=4 and (j-3)dim U<=14. Thus j<=17, with central parity also imposed. Independent recurrence enumeration gives exactly:

| Atom | H1 at twist 2 | H1 at twist 3 |
|---|---|---|
| A(-4) | A | 0 |
| V(-4) | V | 0 |
| P(-4) | P | 0 |
| Wp(-5) | P | Wp |
| one(-6) | A | W |
| one(-10) | V+P | T |

Degree -3 atoms contribute only positively to chi(K(3)). Its negative T therefore forces one one(-10), and its negative W forces at least one one(-6). After these consume V, one P and A in the twist-two budget, only one P remains. The negative Wp then forces Wp(-5). These required atoms already have total rank four, so there can be no additional atom, positive cancellation, or degree -3 summand. Their total degree is -26. Consequently

    K = O(-6) + Wp O(-5) + O(-10).

The independent twist-one check is chi(K(1))=-Wp-S-2T=-Sym17 W. This is a complete kernel determination, not a necessary candidate selected without excluding alternatives.

## 5. Exhaustive internal images and first spans

The actual internal target is

    (E/F)(-2) = D(-4) + Wp(-5) + V(-6) + 2O(-10).

For each of the three kernel atoms I independently checked every target using

    Hom_G(U O(d), V O(e))
      = Hom_G(U, V Sym^(e-d) W) if e>=d,

and zero otherwise. The only channels are the scalar endomorphism of Wp(-5) and a scalar map O(-10)->2O(-10). Thus every nonzero image is a full direct-summand row or one constant scalar multiplicity line. All four possibilities for J are saturated. This is an exhaustive list even if some allowed maps cannot actually occur; no possible internal image was discarded without a reason.

The four first spans have (rank,degree) respectively (6,8), (8,2), (7,0), (9,-6). The first two cannot embed in a constant bundle. The last two, together with the 0/-1 degree restriction and their Euler characters, give exactly

    J=O(-10):              M=(A+P) O;
    J=Wp(-5)+O(-10):       M=A O+T O(-1).

For the latter case chi(M)=A and chi(M(1))=W+S+T; subtracting A W=W+S leaves the actual linear coefficient T. These identifications require no horizontal splitting.

## 6. Constant seven-space branch

M maps onto L in Q, and the image-preimage calculation in Section 2 gives N/F=J(2), exactly a scalar multiplicity line in the original 2O(-8). Choosing a complement to F in the top 2D block is legitimate, so the actual constant projection has source quotient

    E/N = D(-2)+Wp(-3)+V(-4)+O(-8)

inside (H/M) O. Its ambient quotient is Q/L and is locally free; its external derivative image is the lower part O(2)+O(-8). The high part has been removed as an actual saturated quotient.

The surviving original Wp(-3) summand is saturated. Its external derivative is zero because Wp is absent from Sym5 W=T and the other row is too negative. Its internal derivative into D(-4)+V(-6)+O(-10) is zero by ordinary degrees. It is therefore a horizontal subbundle of the constant ambient bundle. In characteristic zero its Grassmannian map is constant, and saturation makes the bundle constant, contrary to its degree -6. This excludes the branch.

## 7. Constant-A capture and the exact second projection

In the other branch A O is the canonical constant subspace of M. It maps to E^+/E. Its maps to O(-6) and O(4) vanish by degree and the absence of A in Sym4=D. If its high map vanished too, A O would lie in E, contradicting H0(E)=0.

The nonzero map A O -> O(18) has three independent coefficient sections, so a common divisor has degree at most 16. The same invariant-divisor argument leaves only degree 12; Sym14 and Sym16 have no invariant and A is absent from Sym6. It is therefore surjective everywhere. Thus

    N_A=E intersection A O,     A O/N_A=L,
    rank N_A=2,                degree N_A=-18.

Constant projection gives E'=E/N_A in (H/A) O with ambient quotient Q/L, hence E' is saturated. Its external derivative image is exactly O(2)+O(-8).

Now N=E intersection M satisfies, as actual subbundles of E/F,

    N/F=Wp(-3)+O(-8).

The first term is the whole original R=Wp(-3) summand and the second a scalar multiplicity line, because J was located precisely in those rows. Consequently

    E/N = D(-2)+V(-4)+O(-8).

Moreover E+A O is the full preimage of L in H O. Since M also maps into L, M is contained in E+A O. This proves the actual inclusion and quotient

    M/A O = T(-1) subset E',
    E'/T(-1) = E/N = D(-2)+V(-4)+O(-8).

T(-1) is saturated in the projected ambient bundle because M was saturated before the constant projection. These facts are stronger than coincident ranks, degrees or abstract splitting types.

## 8. Why the actual linear coefficient kernel contains D

Project F to M/A O=T(-1). The map cannot vanish, since a rank-five bundle cannot lie in A O of rank three. Its equivariant Hom space has dimension one, since T W=D+V+P. The nonzero map is therefore the universal multiplication-by-the-tautological-line inclusion

    Sym4 W O(-2) -> Sym5 W O(-1),

which is injective at every fiber. This invokes an identity for arbitrary binary forms, not a selected actual parameter or fiber evaluation.

Because every derivative of F lies in its actual first span M, constant projection implies that the second fundamental form of T(-1) kills this projected D(-2).

For completeness, the relevant coefficient-kernel fact is exact. Write the actual inclusion of a linear bundle U O(-1) into constants using its coefficient map c:U tensor W -> C. The first derivatives and values of the linear sections span C O. If K_c=ker(c), the elementary tautological/Euler calculation identifies

    ker(beta_(U O(-1))) = K_c O(-2).

The map from K_c O(-2) to U O(-1) is the usual contraction along the tautological line. Fiberwise injectivity follows from the original inclusion: a relation whose contraction vanished would give a vector in a fiber-kernel of that inclusion. The ranks and the universal first-span sequence then give the stated equality, equivariantly.

Applying this with U=T, the killed actual D(-2) embeds in K_c O(-2). The resulting map between equally twisted coefficient bundles is constant, so D is a genuine constituent of K_c. Thus the actual constant coefficient span C_T is a quotient of

    (T W)/D = V+P.

Its dimension is at least seven: a saturated negative rank-six bundle cannot occupy a six-dimensional constant space as a same-rank subbundle. Equivalently, the possible quotient dimensions of V+P are 0,3,4,7 and rank six already forces the last. Hence C_T=V+P exactly.

## 9. Why R survives injectively, has span V, and gives the contradiction

R=Wp(-3) is the original direct summand of E contained in N, hence in M. Choose any equivariant splitting M=A O+T(-1). Its A component is zero because

    Hom_G(Wp(-3), A O)=0,
    A Sym3 W=W+S+T.

Thus projection by the actual constant A preserves the injection of R, including at every fiber; it is not merely generically injective. It remains saturated in T(-1) and in the projected constant ambient bundle. Indeed, before projection R was a direct summand of E and thus saturated in H O, and the zero A component identifies its quotient within M with A O plus the quotient within T(-1).

Its coefficient span C_R is a nonzero quotient of Wp Sym3 W=V+D and, because it lies in T(-1), a subrepresentation of C_T=V+P. Semisimplicity forces C_R to be the actual three-dimensional V subspace.

R is a saturated rank-two subbundle of V O with negative degree. Its Grassmannian map cannot be constant. In characteristic zero its derivative is generically nonzero, so its first span has rank three, since the quotient in V O has rank one. Its saturated first span is therefore the entire constant V O.

But R has zero external derivative in E': the high quotient has already been removed by the saturated constant-A projection, and the low rows admit no map. Its remaining derivative toward E'/T(-1) takes values in

    (E'/T(-1))(-2)=D(-4)+V(-6)+O(-10),

and is zero by ordinary degrees from Wp(-3). Consequently every actual derivative of R stays in T(-1). Since T(-1) is saturated in the projected ambient constant bundle, it must contain the saturated first span V O. This contradicts H0(T(-1))=0.

Both exhaustive first-span branches are impossible. This completes the claimed source-edge exclusion.

## Final assessment

The decisive improvement is an actual high-only D kernel and actual constant capture of the high quotient, followed by a coefficient-span contradiction. It neither assumes an abstract splitting is horizontal nor imports an unpublished cubic classification. The frozen verifier is an appropriate finite-character and input-authentication check; its scope is not confused with verification of saturation, projection or connection claims. Those claims have been independently checked above.

No correction to the frozen mathematical argument is required. Preserve the stated source-edge scope and the zero-defect actual-quotient convention in any publication or ledger update.
