# A uniform top-section obstruction to both lower cubic-image branches

## 1. Result and scope

Retain the actual geometric, primary-module and physical-marking hypotheses in the six complete original sources of the vendored frozen lower-image packet. Suppose the actual generic second fundamental form has rank four and its maximal ordered plateau is (k,l)=(3,1). For any chosen T6 copy in H0(Q*(3)), its restricted dual cubic derivative cannot have image rank two or three.

This excludes all thirteen necessary image/quotient pairs and all 96 torsion-partition rows of the previous packet, including all 83 rows with positive plateau defects. It uses a uniform representation obstruction at the opposite endpoint, not an unproved splitting of an inverse-image extension. In particular, delta1 and delta2 are not set to zero.

Combined with the separately established nonzero-image and rank-at-most-three theorem, only the rank-one O(9), source-D branch remains. That preceding image-bound theorem is imported explicitly from the full frozen cubic-image/ packet, whose verifier is rerun here. The present result does not exclude the whole (3,1) profile, reduce a coarse profile count, prove SF>=5, square surjectivity, full-adjoint invertibility, or the original repair. No actual coefficients, parameters, jets, matrices, instance ranks, or historical candidate enumeration are evaluated.

The useful uniform inequality is

    chi_G(Z(4)) <= H0(B*)                            (1)

for the actual opposite endpoint Z=F4^perp and B=E/F2, once the last plateau map is known to have zero determinant defect. Every one of the thirteen pairs violates (1) at the physical representation V, by exactly one copy.

## 2. Actual input and what is already proved

The original unequal bundles and their marking remain

    rank E=17, rank Q*=13, deg E=deg Q*=-54,
    0 -> E -> H O -> Q -> 0,
    H=2A+2V+2P+2D,  dim H=30,
    A=Sym2 W,  V != A.

The actual dual Euler presentation is

    chi_G(Q*(t))=chi_G(M3 O(t-1))-chi_G(M2 O(t)),
    M3=3W'+3S4+6T6,
    M2=A+2V+3P+4D.

In particular

    chi_G(Q*(4))=-1-A+D+P+2V.                       (2)

The ordered saturated stages and their rank-four quotients are

    F0 < F1 < F2 < F3=E < F4,
    ranks 5,9,13,17,21,
    Li=Fi/F(i-1), B=L3.

All maps Li -> L(i+1)(-2) are regular and generically invertible. Write delta_i for their determinant torsion lengths. The preceding lower-image theorem, with its complete source audit and actual torsion-sensitive inverse-image construction, proves:

- If the chosen image has rank two or three, it is saturated.
- The actual quotient B belongs to the thirteen pairs below.
- All thirteen pairs force delta3=0. This is a conclusion of their complete numerical ledger, not an initial assumption.
- The earlier defects remain: the 50 numerical case rows include 37 positive-defect rows, and the 96 inverse-image torsion partitions include 83 positive-defect rows.
- No lower-rank image is identified with the whole rank-four annihilator, and no inverse-image extension is assumed split.

The complete frozen dependency is reproduced at lower-image/, including its proof, portable verifier, six full originals, all result projections and authenticated manifest. Its manifest SHA-256 is 089d7283e3fcaa626a479170fdd2b56d21028b3e57dd6249327e2d0e6ca658e7. The full earlier image-bound packet at cubic-image/ has manifest SHA-256 7398660b9d9a394ac2aaa19d9d68fdadcc6484c53922f92b1de56b3c1f49a7a7; it supplies the nonzero image, rank-four exclusion, and rank-one O(9)/source-D corollary, with all of its own original premises retained. The verifier derives the thirteen pairs and all 96 rows again from that dependency, rather than accepting a manually shortened list.

Endpoint persistence gives maxdeg Z<=-4 for Z=F4^perp. For clarity, this is the endpoint application of the arbitrary-rank persistence lemma, not the false inference l=1 implies source Z: reverse the entire four-block plateau. A section of Z(d) with d<=3 reaches a nonzero constant span within at most three forward transforms, inside an interior reversed stage, contrary to the rank-independent constant-subbundle propagation. Thus H0(Z(3))=0, equivalently every ordinary splitting degree of Z is at most -4.

## 3. A top-section derivative lemma

Let S be a saturated subbundle of a constant bundle on P1, with every ordinary splitting degree at most -d, where d>0. Suppose its second fundamental form factors through a locally free subbundle T of the ambient quotient:

    beta_S:S -> T(-2).

Then the induced map

    H0(S(d)) -> H0(T(d-2))                          (3)

is injective.

Proof. If a nonzero section lies in its kernel, all degrees of S(d) are nonpositive, so the section lies in the degree-zero direct summand and is nowhere zero. It defines a saturated line K=O(-d) inside S, and K is saturated in the constant ambient bundle as well. The vanishing beta_S|K says that the derivative of K lands in S. Its second fundamental form therefore factors through (S/K)(-2). But all degrees of this target are at most -d-2, so

    Hom(O(-d),(S/K)(-2))=0.

Thus K is horizontal. A saturated derivative-invariant subbundle of a trivial connection is constant in characteristic zero, hence has degree zero. This contradicts deg K=-d<0.

The lemma does not assume the splitting of S is horizontal. It derives horizontality only for the particular kernel line. All maps in (3) are G-equivariant when the data are, so (3) is also an injection of G representations. Equivalently, if a physical irreducible has too many top-slope copies, a kernel copy is horizontal by the same proof; for V O(-4), the contradictory degree is -12.

## 4. The genuine upper quotient and derivative target

The conclusion delta3=0 makes the regular generically invertible map

    B=L3 -> L4(-2)

an isomorphism of bundles: its determinant has no zero divisor. Hence L4=B(2). Dualizing the actual exact sequence 0->L4->Q->(H O)/F4->0 gives

    0 -> Z=F4^perp -> Q* -> B*(-2) -> 0.            (4)

This is a sheaf identity at every parameter, not just a generic fiber equality.

Moreover differentiation of the pairing between Z and E proves

    dZ subset E^perp tensor Omega = Q*(-2),

because dE is contained in F4 tensor Omega and Z annihilates F4. Therefore the second fundamental form of Z factors through the actual quotient in (4):

    beta_Z:Z -> (Q*/Z)(-2)=B*(-4).                 (5)

Apply the top-section lemma to S=Z, d=4, and T=Q*/Z=B*(-2). It gives the equivariant injection

    H0(Z(4)) -> H0(B*).                            (6)

Since H1(Z(4)) is a genuine representation,

    chi_G(Z(4)) <= H0(Z(4)) <= H0(B*).

This proves (1). No H1 vanishing is asserted. A positive coefficient in chi_G(Z(4))-H0(B*) is already a contradiction, because adding H1(Z(4)) can only increase that coefficient.

Finally, exact Euler additivity in (4) gives

    chi_G(Z(4))=chi_G(Q*(4))-chi_G(B*(2)).          (7)

Equations (2), (6) and (7) use the actual dual Euler input. They do not exchange E and Q*.

## 5. The uniform physical-V contradiction

Write J for the chosen saturated image and N for the actual complementary kernel in the preceding theorem. That theorem proves B=N+J*(1) as an equivariant bundle only after checking the applicable extension spaces. Here its thirteen final cases divide into three families:

| J | N | [V:chi(Z(4))] | [V:H0(B*)] |
|---|---|---:|---:|
| W' O(2) | O(2)+O(4), O(2)+O(6), W O(3), 2O(4), O(4)+O(6), W O(5) | 1 | 0 |
| W' O(4) | O(2)+O(6), 2O(4), O(4)+O(6), W O(5) | 2 | 1 |
| V O(1) | O(2), O(4), O(6) | 2 | 1 |

These are all thirteen pairs, in the fixed physical marking. Every N has strictly positive ordinary degrees, so H0(N*)=0. The simple target identities are

    H0(W' O(1))=P,
    H0(W' O(3))=D+V,
    H0(V O)=V.

Computing chi(B*(2)) from the actual splitting and using (2) gives the third column. Thus in all thirteen cases

    [V:chi_G(Q*(4))-chi_G(B*(2))-H0(B*)]=1.         (8)

This violates (1) in every case. The exact full vectors, not only their dimensions, are recorded in OBSTRUCTIONS.json and reproduced by the verifier with both the physical McKay recurrence and independent exact conjugacy-class arithmetic over Q(sqrt5).

The contradiction is not a dimension count. For example, with J=W' O(2) and N=O(2)+O(4), the obstruction is -1-A+V, whose dimension is -1, yet whose V coefficient is +1. Replacing V by A or weakening representation order to dimension order loses the argument.

## 6. Defects and retained scope

The argument uses only the previously proved local conclusion delta3=0 for these image families. It does not split Ni/Ci inverse-image extensions, set nu_i or tau_i to zero, identify their torsion sheaves, or discard positive lengths. The new verifier crosses every obstruction with all 50 case rows and all 96 torsion-partition rows, retaining and rejecting all 37 and 83 positive-defect rows respectively.

The earlier exploratory endpoint shape search is unnecessary for this final proof and is not a premise. This packet does not claim a 96-to-37 result; its uniform final result excludes all 96 rows. There is no full (3,1) exclusion because the separate rank-one O(9), source-D branch has not been analyzed here.

Run python3 verify.py and python3 -O verify.py from any working directory. The output must agree with RESULT.json. Authentication establishes byte identity, not the truth of the retained actual geometric and primary-module hypotheses. The certificate checks exact universal character algebra and dependency coverage; it is not an evaluation of an actual HM instance or a formal proof-assistant verification of the geometric lemmas.
