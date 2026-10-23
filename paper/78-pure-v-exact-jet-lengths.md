# Exact local ideals on the two exceptional jet lines

**Craig Ward · 23 October 2026 · PR1037**

[Immutable full proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/6527465d81b7be4176ff57a0135a0a7f1ee756fd/research/hm/source2-pure-v-exact-jet-lengths/PROOF.md).

The earlier lower bounds are now exact. For any nonzero universal gate on ℓ₅=[1:2], the base ideal is m³ at each of the six order-five axes and m at each of the ten order-three axes, giving total length 46. On ℓ₃=[1:−2], the six ideals equal the prescribed (u²,v²) ideals of Z and the ten ideals are m², giving total length 54. In both cases the support is exactly those sixteen axes, with no extra points.

These are statements about distinguished lines of the universal conditional gate. They do not choose an actual coefficient, prove actual nonvanishing, or realize an actual compatible source.

## 1. Whole-orbit ideal identities

Retain the normalized nonic rows F₁=NLR₁ and F₂=NLR₂ and reduced axis ideals I₅,I₃ from PR1036. On the entire symbolic chart p=1, over K=Q(√5), the new exact certificates are

    (F₁+2F₂)+I₅⁴=I₅³,
    (F₁−2F₂)+I₃³=I₃².

Parentheses around a row mean its component ideal. The checker establishes equality of complete reduced Gröbner bases, not just dimensions, leading support or sampled ranks. The finite quotient dimensions are 60 and 36 for I₅⁴,I₅³ and 60 and 30 for I₃³,I₃². The underlying reduced orbit ideals have lengths 6 and10, accounting for every relevant axis; none lies outside the chart.

## 2. From leading jets to the complete local ideal

Localize the first identity at an order-five axis or the second at an order-three axis. The relevant reduced orbit ideal becomes the maximal ideal m. For the nonic component ideal J, with r=3 or 2, one obtains

    J⊂m^r,   J+m^(r+1)=m^r.

The finite module M=m^r/J satisfies M=mM, so Nakayama gives M=0. Thus J=m^r exactly, including higher-order terms. This upgrades the previous jet containment into the whole local ideal. The lengths of R/m³ and R/m² on a smooth surface are 6 and 3.

At the other orbit the two jet lines are distinct, so the earlier theorem already gives the prescribed ideal. The notation (u²,v²) means equality with the old Z ideal in its supplied local coordinates, not a newly chosen actual axis evaluation.

## 3. Total lengths and boundary

PR1035 excludes additional off-conic support on both jet lines; PR1036 places them away from the conic-base line. Therefore the exact totals are

    ℓ₅: 6·6+10·1=46,
    ℓ₃: 6·4+10·3=54.

These exact nonic schemes are not the older source126 octic scheme, even where the numerical length 46 coincides. They do not determine the conic line's transverse thickness, occurrence of any off-jet support alternative, or a location for a possible thirty-point orbit. Nor do they identify lift rank with original-fourth rank.

The packet has independently reviewed exact reconstruction and 26 ordinary/optimized checks. Its universal polynomial certificates and written local-algebra arguments do not evaluate any actual HM coefficient or certify the full proof repair. Four necessary source-dual pairs across three stable labels remain.
