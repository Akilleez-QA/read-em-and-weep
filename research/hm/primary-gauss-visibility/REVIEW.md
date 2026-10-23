# Independent review: canonical primary cubic Gauss visibility

## Verdict and binding

PASS at the precise scope stated in PROOF.md. The universal near-top visibility lemma is valid, its use on the actual canonical primary subbundle is valid, and the fixed historical 182-row computation rejects exactly 30 rows, distributed 25/1/4 across profiles 11/12/21. I independently reproduced the entire rejected-row data and ordered 152-row pass list by character inner products, not by importing the supplied checker or its tensor adjacency recursion.

This review binds these exact SHA256 hashes:

- PROOF.md: f7f267098d561de91e216f34588d1ab983947c2363b5a2dd4b0bd59104b39eed
- verify.py: 88f726b70292b6691d2b3868c9af8bcb461def22adfbdd3902d1472fe8a44cf7
- RESULT.json: 96321ebd7ba1936cabadb50b84b1f06b6bea6edbd36a9216b90a6de33d3d4701
- INPUTS.json: 9acf619d1c901d2a0966e2824f2b0bb09da8462378cdeb80261be1edb79fe4f4

I did not edit the frozen proof, checker, result, manifest, or included originals. The present review is the only added artifact in this slice.

## Geometric review

For a killed nonzero coefficient u in U, L=(C u) tensor O(-d-1) is a subbundle of C. The extension sequences through F and the ambient trivial bundle make L saturated in each, not merely generically injective. Twisting

    0 -> (U/C u) O(-d-1) -> F/L -> F/C -> 0

by d-1 proves H0((F/L)(d-1))=0 directly. This avoids any unjustified assumption that an arbitrary quotient of a negative bundle retains the slope bound.

Because beta_F kills L, the actual second fundamental form of L factors through (F/L)(-2). Its Hom space from L is exactly H0((F/L)(d-1)), which vanishes. Thus L has zero second fundamental form in the ambient constant bundle. In characteristic zero its classifying map is constant; saturation makes the line bundle itself constant, contradicting degree -d-1<0. The proof works for every d>=0, including d=0. All twists and saturation arguments are correct.

The actual application uses the right ambient inclusion. PR1124 constructs a saturated C=(W'+T6) O(-3) inside the same actual E, and proves the quotient bound H0((E/C)(1))=0 from an actual quotient pencil. The Gauss derivative remains the one from the plane-section constant thirty-space. Nothing identifies that derivative with the derivative of the separate terminal-pencil embedding, nor assumes a chosen complement of C is horizontal.

The map through A_q=E/ker(beta_E) is legitimate: this locally free quotient injects as a sheaf into Q(-2), even if its image is not saturated there. The near-top lemma makes the composite on cubic global sections injective, hence gives

    W'+T6 -> H0(A_q(3))

as an injective G-map. This is coefficient-space injectivity only, not a sheaf or generic-fiber rank-eight injection into a rank-three quotient.

The two example exclusions are correct: W' O(-1)+O(2) has cubic sections 2T6, while O(-8)+O(2)+O(6) has S4+2T6. Both lack W'. The derivation is a genuine new application of the canonical primary input, while the proof accurately avoids claiming the horizontal-negative-subbundle method itself is new. The strict-top theorem as originally stated does not by itself give the cubic primary coefficient injection.

## Reproduction and independent finite verification

I ran both

    python verify.py
    python -O verify.py

without --write. Both succeeded, including their internal exact-byte replay of RESULT.json. Both emitted JSON equal to RESULT.json; print adds one extra final newline to stdout, which is immaterial. The stored RESULT.json is unchanged.

For an independent path I used the nine abstract conjugacy classes with sizes

    1,1,12,12,12,12,20,20,30

and W traces

    2,-2,phi,-phi,phi',-phi',1,-1,0,
    phi=(1+sqrt(5))/2, phi'=(1-sqrt(5))/2.

I computed symmetric-power characters directly from s0=1, s1=t, s(n)=t s(n-1)-s(n-2), using exact arithmetic in Q(sqrt(5)). The irreducible characters are Sym0 through Sym5 for 1,W,A,S4,D,T6, together with P=(4,4,-1,-1,-1,-1,1,1,0), V=Sym6-P, and W'=W P-T6. I checked all 81 pairwise character inner products, obtaining the identity matrix.

For each fixed quotient row I formed its section character directly on those conjugacy classes, summing chi_R times s(e+3), with negative degree contributing zero. Inner products with all nine irreducible characters gave the full decomposition. Every multiplicity was a nonnegative integer, and every reconstructed dimension matched the section character at the identity. This route does not use the checker’s tensor-by-W table or product recurrence.

The independent result matches every entry of RESULT.json's cut list, including stable ID, profile, source index, ordered A blocks, full cubic section character, and missing constituent. It also matches the complete ordered survivor ID list. The excluded original source indices are:

- Profile 11: 47,57,58,59,63,64,65,66,68,70,71,74,75,79,90,91,92,93,97,101,103,107,108,110,111.
- Profile 12: 8.
- Profile 21: 0,1,8,12.

Thus the independent totals are 25+1+4=30 rejected, and 134+9+9=152 passing. Every rejection lacks W'; none is solely a T6 deficit. The largest symmetric-power index used is 31. Repeated blocks and their multiplicities are correctly retained.

I separately recomputed the byte lengths, SHA256 digests and Git blob SHA1 identities of all seven included original files; all match INPUTS.json. The manifest records their immutable public commit URLs. The source texts support the imported actual-bundle facts and distinguish the historical coverage theorem from finite-list integrity.

## Scope and limitations

The proof is a new necessary condition on the actual derivative quotient. The checker evaluates that condition on a fixed historical necessary list. It does not prove that list's geometric completeness from scratch, rerun its source enumeration, establish actual realizability of a passing row, or validate subsequent frontier bookkeeping.

The packet correctly labels its 30 eliminations as cuts of historical rows, not 30 newly live exclusions. The number 152 is therefore not an independently established current frontier or completion metric. The stated unresolved coverage and actual-source transfer obligations remain unresolved by this slice.

No selected HM/source coefficient, parameter, point, tensor, derivative evaluation, matrix, actual-instance rank, or instance scan was used. The computation is a bounded calculation in the fixed abstract character table. The geometric lemma and its actual-input bridge are established by the proof, not by the arithmetic checker.
