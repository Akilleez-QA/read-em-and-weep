# Exact component-ideal transfer to the original fourth D row

**Craig Ward · 23 October 2026 · PR1046**

[Immutable full proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/56c1ee605ba1886d7e837d6a686b3e8a00af1dc9/research/hm/source2-pure-v-fourth-axis/PROOF.md).

## Actual map and the precise completed bridge

For the conditional pure-V gate, let F=NLR be its degree-nine nonic row and H=FL its degree-ten row. The corrected-lift identity identifies −H with the determinant-embedded original fourth on surviving D, up to a fixed common nonzero normalization. PR1046 proves equality of projective component ideal sheaves

    (H)~= (F)~.

Thus the complete five-stratum classification transfers to this original-fourth D row, including all local ideals, not merely support. This closes the specific rank-drop gap left in PR1044.

The underlying original map has degree four, D O(-4)→coker B; its determinant embedding into O(6) produces degree-ten polynomial entries. The quotient-third determinant row has degree nine. These degree conventions are compatible, not different obstruction orders.

## Why generic surjectivity was insufficient

The inclusion (H)⊂(F) is automatic from H=FL. Away from the ten order-three axes, L is locally a split surjection, so a local right inverse gives F=HS and equality. At those axes L has rank three, with reduced maximal-minor scheme. Its local normal form alone does not preserve an arbitrary row ideal, so the result requires additional identities for this universal pencil.

## Whole-orbit certificates and every coefficient pair

Let I be the reduced ten-axis ideal on the entire p=1 chart, which contains the whole orbit. The quotients by I,I²,I³ have dimensions 10,30,60. For H_i=F_i L, exact polynomial computations prove

    H₁,H₂⊂I,
    rem_(I²)(H₂)=½ rem_(I²)(H₁),
    (H₁)+I²=I,
    (H₁−2H₂)+I³=I².

Membership and equality are verified componentwise and by complete reduced-basis equality, with no selected axis or coefficient value. For H=αH₁+βH₂ the leading remainder is (α+β/2)H₁. Off 2α+β=0, localization and Nakayama therefore give (H)=m at every order-three axis. On that line, a nonzero pair gives (H)=m², including all higher local terms. These are precisely the already known ideals of F. Combining them with the local right inverse elsewhere proves global ideal-sheaf equality without any hidden additional coefficient direction.

## Transferred classification and retained limits

For nonzero pairs, ratios −2,−1,0,+2 yield the exact determinant-fourth component schemes of lengths 54,49,46,46; every other ratio, including infinity, yields exactly Z of length 34. The two length 46 schemes remain different. At the zero pair both rows vanish and the base scheme is the whole plane. These are consequences of the [completed nonic classification](82-pure-v-complete-nonic-classification.md), not new nonic local computations.

No equality of raw unsaturated graded ideals with different generator degrees is asserted. The statement does not imply fiberwise injectivity of the ideal-sheaf target at its singular points. It does not cover extra specialized A-kernel classes or the quadratic lift's rank-drop scheme. It does not select whether the actual gate is zero, determine its ratio, establish compatible-source occurrence or repair the original proof.

The packet reports independent review and 30 ordinary/optimized checks. The actual endpoint identification, exact local ideals and Nakayama interpretation are written mathematical arguments, not consequences of test counts alone.
