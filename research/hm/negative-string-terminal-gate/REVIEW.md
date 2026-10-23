# Independent mathematical review: PASS

Reviewed the complete proof and checker independently of their author on 2026-10-23. This review binds to:

- PROOF.md SHA-256: affb6a3e89fecfd9457c949a5dcd9082b8b23800845bb271f1a143d76d8163ae
- verify.py SHA-256: 642d83d9d6dcc0555e961ea3b49b4c45bce3a59ed05b512e4c235ab0f8fc8ec0
- INPUTS.json SHA-256: 122b27b3366454aa2cd2bd425875ad63db03de2a449e1cdac42082aed4fbf8d1

## Reviewed derivation

1. The positive plane parity is justified at bundle level. The central involution fixes the plane, and stability makes its automorphism of the restricted rank-two bundle scalar. Its conjugation action on the trace-free endomorphism bundle is therefore trivial. The plane line-bundle twists have positive central character. This removes both plane cohomology terms needed for the negative restriction comparison, rather than only removing the space of sections.

2. The negative part of the two-coordinate Koszul sequence is actually exact as stated. Its left obstruction vanishes because H0(I_R B(5))_- embeds in H0(B(5))_-=0; its right obstruction vanishes because H2(B(3))=0. Restriction to the plane then identifies H1(I_R B(5))_- with H1(B(5))_-. These are natural maps for the actual bundle. The determinant identification explains the sign/change-of-factor convention between the Koszul injection and the original pencil's simultaneous multiplication map.

3. The character M5=W'+3T6 follows independently from exactness: W V=T6, W P=W'+T6, and W D=S+T6 give W M4=4W'+3S+9T6; subtracting M3 gives the asserted character. The independent equivariant Euler calculation is consistent with H0(B(5))=1+P+D and the cited higher-cohomology vanishings. It yields total h1(B(5))=32 and negative dimension20. No Euler character is substituted for an actual section space.

4. Compatibility of the canonical string identifies the restriction W tensor U4 -> M5 with symmetric multiplication followed by f5. Its universal kernel is the selected U3 image under delta. Irreducibility of Sym5 W proves that a nonzero f5 is injective, but does not prove that f5 is nonzero. The entire degree-six group vanishes, so any nonzero degree-five string image is terminal under every coordinate.

5. In the zero branch, U*=delta^{-1}(W tensor U4) is an actual canonical subrepresentation, not a copy chosen by its character. Its decomposition S+T6 has no repeated constituent, and its S constituent is the pre-existing selected U3. Determinant contraction of the delta formula recovers the original pencil, hence its restriction is the Euler subpencil onto the actual selected U4. The degree-minus-two kernel consequently lies in the original E itself. The snake-lemma quotient uses the full original source and target and retains their maps; it is not inferred from equal K-classes or from an abstract weighted source presentation.

6. Both subpencil and original pencil are onto on every fiber, so the quotient presentation remains onto and E/(D O(-2)) is locally free. Its source and target ranks are44 and32, giving kernel rank12 and degree-44. This matches subtraction from rank17 degree-54 by rank5 degree-10.

7. H0(E(1))=0 forces all Birkhoff--Grothendieck degrees to be at most-2. Maps from O(-2) to lower-degree summands vanish. Thus the selected D O(-2) lies in the maximal-degree-minus-two coefficient space and splits by semisimplicity; averaging permits an equivariant splitting. The proof correctly does not claim a canonical complement.

8. The twist-six Koszul sequence gives the claimed actual joint-negative kernel because the relevant positive part of W tensor H0(B(5)) is zero. Character subtraction alone does not determine that kernel, and the proof explicitly retains the unevaluated restriction map. The compatible selected-U4 condition in the converse is necessary and is stated; the existence of an unmarked D O(-2) summand alone is not promoted to an equivalence.

## Reproduction and boundaries

Both `python3 verify.py` and `python3 -O verify.py` completed successfully against the hashes above. The checker uses explicit exceptions rather than removable assertions, verifies all five imported file byte counts and SHA-256/Git-blob identities, and checks only bounded fixed abstract character arithmetic and bookkeeping.

No mathematical correction is required for this version. This is an independent mathematical text and bounded-checker audit, not formal proof-assistant verification. It establishes the exact continuation and conditional actual Euler subpencil; it does not decide the f5 branch, an actual source/catalogue alternative, an opposite-bundle type, or any vertex/smoothing conclusion. No selected HM/source coefficient, parameter, point, jet, matrix, instance rank or large scan was evaluated during review. Nothing was published.
