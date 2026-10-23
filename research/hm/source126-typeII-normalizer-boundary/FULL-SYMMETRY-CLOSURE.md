# The full ambient HM stabilizer closes the outside-normalizer loophole

## Result

For the fixed normalized actual Horrocks–Mumford bundle F,

       Aut_proj(F):={s∈PGL5(C):s*F≅F}=N5/μ5.          (1)

Thus its full projective stabilizer has order3000. Combining (1) with the fixed-quadric normalizer theorem gives

       Stab_Aut_proj(F)([Q0])=SL2(F5),                 (2)

and the same group stabilizes the pair of Q0 and the fixed negative pencil. There is therefore NO additional ambient projective HM automorphism, inside or outside the previously known normalizer, that preserves this pair and acts by a new nontrivial character on the canonical octic line.

This closes a symmetry loophole, not the octic scalar gate. The actual scalar remains unselected. No actual coefficient, parameter, HM matrix or rank is evaluated, no source or pair is excluded, and no higher internal symbol is computed.

## 1. Exact primary theorem, not an inference from a title

The source is W. Decker, Math. Z.188 (1984),101–110, DOI10.1007/BF01163877. Its public primary scan is https://gdz.sub.uni-goettingen.de/download/pdf/PPN266833020_0188/PPN266833020_0188.pdf . PRIMARY-SOURCE.json records the volume digest and exact page locators.

Section2.1, printedp103, identifies the normalized HM bundle. Definition4.1,p106, defines S(E) as all Θ∈SL5(C) for which (Θ^-1)*E≅E. Thus it is the full ambient pullback stabilizer, not just a chosen action or the group of vertical bundle maps. Section4.2,p107, defines the order125 Heisenberg group G_HB and its order15000 SL5 normalizer N_HB. Theorem4.2.3,p109, states:

       “Es ist S(𝓕(E))=N_HB.”

Its proof uses the monad-isomorphism criterion4.1.1 and Heisenberg characterization4.2.2 to show that every symmetry normalizes G_HB. The reverse inclusion is Lemma4.2.1. The primary page images, not merely OCR or a later citation, were read. No calculation from the paper is rerun on an actual instance here.

## 2. Passage to the projective group

Every projective transformation has an SL5 lift: multiply any GL5 representative M by a fifth root of det(M)^(-1). Two SL5 lifts differ by μ5. All these scalar lifts induce the identity on P4, so they lie in the pullback stabilizer. Therefore the full preimage of Aut_proj(F) under SL5→PGL5 is exactly Decker's S(F), and quotienting gives (1).

The inverse in Decker's pullback convention does not change the group: s*F≅F if and only if (s^-1)*F≅F. Twisting the normalized bundle by O(k) also leaves this stabilizer unchanged, since every projective transformation preserves O(k). Choosing another coordinate presentation conjugates both the stabilizer and the Heisenberg normalizer together. Consequently the equality applies in the same fixed HM coordinates as the retained pencil; it is not a statement only up to an unrelated group identification.

Vertical bundle automorphisms are a different group. Stability makes them scalar, and they do not supply additional base projective transformations. On the adjoint bundle End_0(F) their conjugation action is trivial. They cannot reopen the outside-normalizer loophole.

## 3. Consequence for the exact actual pencil

The retained normalizer theorem proves Stab_(N5/μ5)([Q0])=G, where G is the existing embedded SL2(F5). Its proof uses the actual rank-three vertex L, the25 distinct Heisenberg translates of L, and orbit–stabilizer. Equation(1) now makes this the FULL ambient stabilizer, proving (2). G preserves the negative parameter space A, so imposing preservation of the pair adds no element and removes none.

PR995 constructs the octic generator as a G-equivariant map D O(-8)→E. Its Hom-space vector is G-fixed. Hence (2) exhausts all ambient projective same-bundle, same-Q0 symmetry candidates for a new character. This is stronger than merely ruling out known Heisenberg translations or the order-four block scaling.

It does not classify automorphisms of only the cone restriction, formal neighborhoods, or abstract complexes that do not come from ambient projective automorphisms preserving F. Such different objects cannot be substituted into the actual-pencil naturality argument without their own compatibility theorem. No assertion about them is needed for the present closure.

## 4. Inputs and verification boundary

FULL-SYMMETRY-INPUTS.json authenticates the frozen normalizer proof and the immutable PR995 proof. The exact Decker theorem is a primary published input; it is not inferred from the phrase '15000 symmetries' or from finiteness of the stabilizer. No claim of novelty is made for Decker's full-group theorem. The new application is the removal of the outside-normalizer qualification from this fixed-octic symmetry route.

Run `python verify_full_symmetry.py` and `python -O verify_full_symmetry.py`. Optionally append `--primary-pdf PATH` to authenticate a separately downloaded copy of the public full-volume scan against PRIMARY-SOURCE.json. The checker verifies dependency bytes, exact source locators, SL-to-projective order conversion, scalar-kernel order and the stabilizer arithmetic. It does not machine-prove Decker's theorem or reproduce his actual monad calculations. The full-volume scan is not redistributed in this packet.
