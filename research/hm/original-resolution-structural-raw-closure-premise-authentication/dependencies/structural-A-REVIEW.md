Editorial scope: This is a mathematical source edition. Historical review and check statements describe the original artifact, not a fresh run. Supporting snapshots are dependencies, not additional new results. Later PR145 mixed-class vanishing supersedes historical unknown mixed-class status; it does not resolve the six pure diagonal conditions.

# Independent review: complete structural primitive A

## Decision and exact reviewed version

**ACCEPTED.** For the six precisely pinned rational carrier records, on their stated denominator localizations,

    gamma H0 + IP + H1 delta = Id15.

The integrated proof establishes this identity without assuming primitive A, an A-dependent contraction theorem, a determinant-one transition theorem, exactness, or a historical successful computation. Its subsequent full contraction and transition-determinant conclusions follow in the stated algebraic scope. No mathematical correction is required.

The reviewed integrated `PROOF.md` has SHA256

    bbb71d8eeb7dcb3e83ce333ac685c6ad64133c96e1703053273e2256800e6565.

The model has SHA256 `635bb12d9986e0dcada161d4173c773c4f134b9225354a3bc74267840ca19926` and Git blob `fcd48a9a22d40d55ce7a08b8aefcb4eaa2fdf761`. All inspected ingredient snapshots bind to these same 16,803 bytes. The decoder excerpt has SHA256 `c4f65ff831092d0e56b3e33a0357f44182169fda45943ea780c8c551b4023f94`. Exact hashes of the reviewed ingredient proofs, independent reviews, checkers, and source snapshots are recorded in `reviewed-pins.json`.

This review inspected the proofs and static implementations and repeated their allowed metadata checks. It did not newly fetch or authenticate a remote repository. The immutable-source provenance is inherited from the cited source packages; matching hashes establish byte identity, not mathematical truth or historical execution.

## 1. Dependency audit

The ingredient theorems used in the composition are their independent early results, not the later conditional normal-form or contraction discussions in the same documents.

1. **Retraction:** the four-cycle and auxiliary triangular solves identify the stored H0 with `gamma_F^-1 E_F^t`. These solves use only their selected gamma entries, H0 entries, and denominator records. In particular, their inverse existence and uniqueness do not require A or a determinant normalization. I checked the closing recurrence, denominator factor, and auxiliary signs against the handwritten tables.
2. **Projection:** the displayed normalized D-coordinate formula follows from that already proved inverse. Its factor `1/v_r` on the second primary row and its auxiliary normalization `-v1^2/v4` are retained. Complete P-entry binding identifies the actual P with this formula. This dependency is one-way from retraction to projection; neither proof assumes P gamma=0 as an input.
3. **Common complex:** the complete cyclic gamma/delta incidence pattern has three opposite signed, reversed-label path pairs per output. The pair list covers all six paths at every output, so delta gamma=0 follows from commutativity without an exactness or contraction premise.
4. **Inclusion cycles:** the primary four-step recurrence gives two independently normalized kernel columns, and the auxiliary triangular solve gives its two columns. All ten outputs are proved zero, including the two outputs omitted from the initial nonpivot solve. The primary second column has free B-coordinate v_r, not 1. The auxiliary second free C-coordinate is `-v4/v1^2`. Thus this proof neither assumes a complementary inverse nor silently uses ev delta or A to supply missing output equations.
5. **Complementary inverse:** the primary cycle plus forced-coordinate equations and the auxiliary triangular equations have a unique solution for every target. The identified coefficient table is therefore a two-sided inverse, proving both TM=Id8 and MT=Id8. This solve uses no I entry, A identity, contraction, or determinant-volume premise. The proof handles its unsorted cyclic ambient order and the increasing S order by the paired inverse permutations; there is no extra orientation sign in an equality of inverse maps.

The accepted cycle-inclusion proof has final SHA256 `e8425c8ea279c50d5682ca30f95a9ebf45ad2dc45e45a433585f28310c4fcdbe`, exactly the version identified by its independent review. The accepted complementary-inverse proof has SHA256 `0d92eedc1f58b9b09ac81672fc991e3079cb89edf3f0394cf42cc24ab3a4281f`. The other ingredient versions and their accepted reviews also agree with the pins recorded here.

No arrow in this dependency chain goes backward through the integrated A theorem. The earlier determinant package is used only after A and the full contraction have been established; its sparse matching statements are themselves independent of those conclusions.

## 2. Support, normalization, and legal units

The literal support statements used in the composition are genuinely covered by the inspected checkers:

    H0 outside F = 0,
    I_F = 0,
    H1 outside S = 0,
    P_S = 0,
    I_D = J, P_D = J^-1,
    H1 in both evaluation-pivot columns = 0.

Here `(F,D,S)` partitions the 15 coordinates with sizes `(5,2,8)`, with increasing F and S and the specified order on D. It follows directly that H0I=H0H1=PH1=0 and PI=Id2. In particular, PI is not deduced from A. The complementary-inverse binding checks all 900 H1 cells, including all off-S rows and both pivot columns. The retraction and projection checks independently cover their needed inclusion/projection supports and D-normalizations.

For a primary carrier the denominator is

    d_r=v_r(product_(j != r) v_j-v_r^4),

with v0=1. In a commutative ring, if a product is a unit, each factor is a unit. Thus localizing at d_r supplies both the pivot v_r and the closing-cycle factor. On the auxiliary carrier, inverting `-v1^2 v3 v4` supplies v1,v3,v4. Every inverse and every pivot division used by the proofs is therefore legal on the stated carrier localization. No additional unspecified generic-open restriction is needed.

The same checkers identify the stored denominators dh, di, and dp with the same polynomial on every carrier. The auxiliary J entry `-v4/v1^2` and the primary entry v_r are units there. Consequently N=[gamma,I,E_S] is independently invertible by its lower triangular coordinate form with diagonal blocks gamma_F,J,Id8. This observation is consistent with, but not needed as a black box for, the direct residual proof.

## 3. Direct evaluation identity and the pivot splitting

The full literal ev pattern is checked by the determinant package's `check_literal_dependencies.py`: it is exactly the two weighted sums with weights v0,...,v4 and zero on the other block. Thus the integrated proof's ev is the pinned ev, not a newly selected functional.

I checked the reindexing in Section 2 independently. In the first weighted sum, the two A_k coefficients are

    +v_(k-2)v_(k+2), -v_(k+2)v_(k-2),

and the two C_k coefficients are

    +v_(k-1)v_(k+1), -v_(k+1)v_(k-1).

In the second weighted sum, B_k has the second pair and C_k has the first pair. All cancellations use only commutativity and indices modulo five. Hence ev delta=0 before localization, without using A or any primitive entry.

For each pinned pivot p, W inserts each nonpivot coordinate and adds the compensating pivot coordinate `-v_r/v_p`; L reads those same nonpivot coordinates in cyclic order. Eta inserts the two pivot coordinates divided by v_p. These definitions prove directly

    LW=Id8, evW=0, Leta=0, eveta=Id2,
    WL+eta ev=Id10.

The literal zero pivot columns imply H1eta=0 and H1=H1WL. Independently, ev delta=0 gives delta=WLdelta. Since H1 has rows only in S, its defined submatrix T therefore satisfies H1=E_S T L. The identification of T from stored H1 is just nonpivot-column selection: the corrective pivot columns of W hit literal zeros.

## 4. The generic-vector proof of A

Let z be arbitrary over the carrier localization, and set

    r=z-gamma H0z-IPz.

The retraction in its stronger coordinate-supported form gives

    E_F^t gamma H0=E_F^t.

Together with I_F=0 this forces r_F=0. The independently established projection formula gives

    JPz=E_D^t(z-gamma H0z),

so r_D=0. Thus r=E_S r_S. This step uses the actual projection identity on the whole ambient module, not merely its restriction to cycles.

The two independently proved cycle identities give delta r=delta z. Substitution now yields

    H1 delta z
      =E_S T L delta r
      =E_S T(Ldelta E_S)r_S
      =E_S(TM)r_S
      =E_S r_S=r.

This proves A for every z. It requires TM=Id8 in precisely the order supplied. There is no appeal to surjectivity, cohomological exactness, a determinant comparison, a historical entry computation, or a previously asserted A-dependent normal form. The proof also works over the stated commutative localizations, not just at generic numerical points.

## 5. Full contraction and inverse direction

The second inverse direction is used separately and correctly:

    delta H1
      =delta E_S T L
      =W(Ldelta E_S)T L
      =W(MT)L
      =WL=Id10-eta ev.

The insertion of W here uses the separately proved evaluation identity. TM alone is the explicit input used for A; MT is the explicit input used in this displayed output contraction. The sparse unique-solution theorem supplies both directions, so no unproved inverse reversal is present.

All the other listed contraction relations follow from the independently proved retraction, projection, cycles, supports, and pivot splitting. For example Pgamma=0 follows from the projection formula and H0gamma=Id5. The proposed inverse of U=[gamma,I,H1W] has block rows `[H0;P;Ldelta]`: the diagonal blocks of its product with U are Id5,Id2,Id8, and all off-diagonal blocks vanish by these relations. Its lower-right block is Ldelta H1W=LWLW=Id8. Both a square inverse argument over a commutative ring and the already known split-basis decomposition justify the stated inverse identity. V=[W,eta] and `[L;ev]` are visibly two-sided inverses.

## 6. Determinant consequence

The prior determinant proof first expresses the transition determinant as a ratio of split volumes,

    det(P_i I_j)=lambda_j/lambda_i,
    lambda_i=det[gamma,I_i,H1_iW_i]/det[W_i,eta_i].

Its change-of-basis matrices have diagonal blocks `(Id5,P_iI_j,L_iW_j)` and `(L_iW_j,Id2)`. These assertions are now justified by the newly proved contraction. They do not need to be assumed to prove any ingredient above.

The prior sparse calculations identify the fixed-lift numerator and denominator determinants as the same unit: `-v_r d_r` on a primary carrier and `-v3 v4` on the auxiliary carrier. Their oriented support matching proof uses only gamma, delta, selected I normalization entries, and coordinate-order signs. I checked the argument and reran its matching certificate. The cyclic nonpivot row permutation occurs in both five-coordinate blocks, so its total sign is even; it introduces no missing sign. Thus lambda_i=1 on all six carriers and det(P_iI_j)=1 on every common carrier localization.

The common-ambient physical interpretation remains a separate premise. Under the specified reciprocal rank-two line/frame change and transpose, determinant one is preserved. The rank-two adjugate is then an inverse, and the correctly interpreted logarithmic current is traceless by the determinant derivative identity. This establishes those algebraic consequences without either historical A or historical determinant execution receipts. It does not establish the physical-frame premise itself, the existence of regular transitions on a larger cover, or correct implementation of the derivations.

## 7. Reproduced checks and independent controls

I read the complete seven static checkers before running them. Ordinary and optimized Python runs all pass with byte-identical stdout:

- retraction metadata;
- projection metadata;
- common-complex incidence and path pairing;
- independent complementary-inverse binding;
- independent cycle-inclusion binding;
- determinant source/literal dependencies, including ev and pivot zeros;
- determinant support matchings and orientation signs.

The retraction certificate was redirected into this review's artifact directory. The determinant matching checker was run on a temporary copy of itself and its pinned inert model, avoiding changes to the prior package. Logs and certificates are retained in `review-artifacts/`. Their PASS results establish the described source bindings; they do not replace the handwritten mathematical proofs.

The new `check_independent_composition.py` uses entirely invented rational matrices of ranks `(1,4,2,1)`, with nontrivial lower coordinate blocks and rank-two middle cohomology. It reads no source files. It verifies the direct residual argument on a full basis and the output contraction, then isolates countercontrols for missing delta gamma, delta I, TM, and the projection formula. A fifth control retains A while breaking ev delta and the output contraction, confirming where the latter premise is needed. Both normal and optimized runs pass identically. These are controls of the abstract composition logic, never specializations of the pinned source.

## 8. Limits

No actual source matrix product, actual polynomial expansion, physical source specialization, source jet, detector, historical verifier was performed. The only matrix arithmetic executed in this review belongs to the independent tiny invented controls.

The accepted theorem is for the exact decoded source records and the stated algebraic localizations. It removes the historical primitive-A premise and, through the previously reviewed volume proof, the historical determinant premise from this algebraic chain. It does not settle physical-frame identification, geometric carrier coverage, all-chart regular extension or pole bounds, arithmetic implementation correctness, terminal detector values, obstruction vanishing, or algebraicity. Those remain separate questions exactly as the integrated proof states.
