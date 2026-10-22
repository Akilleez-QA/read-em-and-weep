# The actual normal trace has a nonzero nilpotent component

## Theorem

For the actual invariant normal class eta, write its square shadow as

    q(eta)=delta(alpha e_v+beta n8).

The previously established alpha is nonzero. In fact beta is NONZERO as well.

The proof computes the vanishing status of the dual component-constant functional by restriction to the FIRST conic neighborhood 2C. It retains the full global Serre lift, the nonsplit vertex geometry, and the possible H0 connecting map on 2C. It does not evaluate beta/alpha numerically, any normal-variation secondary residue, or the fourth Bockstein.

## 1. Exact actual low-twist cohomology

Let X=P_stack(1,1,2,2), physical O(1)=O_wt(2), omega_X=O(-3), and let E=G be the actual Serre bundle with det E=O(2). Its section sequence is

    0 -> O_X -> E -> I_Z(2) -> 0,

where Z=C disjoint union Z_v and C is the reduced conic. The physical twists O(-1) and O(-2) are acyclic; all intermediate cohomology of every line bundle on X vanishes.

The actual homogeneous vertex algebra, after exact tame pushforward to L=P(W), has even cover-degree pieces

    degree 0: O_L,
    degree 2: V O_L(-1),
    degree 4: V O_L,
    degree 6: O_L(-1),

and no higher pieces. Odd pieces have nontrivial stabilizer and do not contribute to the ordinary O_Z twists in question. Here V=Sym^2 Wprime is NOT A=Sym^2 W.

The degree-two statement is the free coordinate piece below the first cubic relation. The actual degree-four piece is the established cubic quotient

    0 -> Wprime O_L(-5) -> D5 O_L(-2)
      -> V O_L -> 0.

The degree-six piece is the actual socle line O_L(-1), including its Serre determinant normalization. These are actual graded sheaves, not a splitting guessed from dimensions.

Every piece of O_Z(-1) has no global sections: on the vertex they are O(-1), V O(-2), V O(-1), O(-2); on C it is O_P1(-2). Consequently

    H1(E(-3))=H1(I_Z(-1))=H0(O_Z(-1))=0.         (1)

The first equality uses intermediate line-bundle vanishing, so no assumption that O_X(-3) is fully acyclic is made.

At twist one the conic contributes V=H0(O_P1(2)); the vertex pieces contribute respectively W,V,V tensor W,1. Global linear sections are H0(O_X(1))=V+W. Their V component restricts isomorphically onto the conic and their W component onto the reduced vertex. Thus their restriction is injective, and its quotient has character

    H1(E(-1)) = H0(O_Z(1))/H0(O_X(1))
              = 1+V+(V tensor W)=1+V+T6.        (2)

The coordinate V may have another component on the vertex; this does not affect the quotient character or injectivity. Exactness of finite-group invariants supplies the stated decomposition. In particular (2) has ONE invariant and NO copy of W.

Serre duality and E^*=E(-2) now give

    H2(E(-4)) = H1(E(-1))^*,
    [W tensor H2(E(-4))]^G=0.                    (3)

## 2. Restriction to 2C is injective on the actual invariant class

The conic is the regular intersection of the negative linear coordinates u,v. Its ordinary square ideal has the equivariant Hilbert--Burch resolution

    0 -> W tensor O_X(-3)
      -> Sym^2 W tensor O_X(-2) -> I_C^2 -> 0.    (4)

Dual conventions for W make no difference because its determinant pairing identifies W with W^*. Tensor (4) by the locally free E(-1). In its cohomology sequence, H1(E(-1)I_C^2) lies between

    Sym^2 W tensor H1(E(-3))
    and W tensor H2(E(-4)).

The first space is zero by (1), and the second has no invariants by (3). Hence

    H1(E(-1)I_C^2)^G=0.                          (5)

The restriction sequence therefore gives an injection

    H1(X,E(-1))^G -> H1(2C,E(-1)|_(2C))^G.       (6)

This uses a kernel vanishing, not an assertion that restriction maps between equal-dimensional spaces are automatically nonzero.

## 3. The first conic layer has exactly one surviving invariant

Write O_C0(k) for degree k on the parametrizing P1. The actual balanced conic restriction and regular first jet of the Serre section give

    E(-1)|C = W tensor O_C0,
    I_C/I_C^2 = W^* tensor O_C0(-2).

The second equality is the actual conormal bundle; the first follows from F|C=W O_C0(-1), physical O(1)|C=O_C0(2), and the spinor twist. Equivalently E|C is the normal bundle of the regular Serre zero section, W O_C0(2).

The first-layer sequence is

    0 -> (W tensor W^*) O_C0(-2)
      -> E(-1)|_(2C) -> W O_C0 -> 0.              (7)

Its potential H0 connecting map MUST be retained. But its source has no invariants:

    H0(W O_C0)^G=W^G=0.

The final term also has H1=0. Taking invariant cohomology in (7) therefore proves the actual isomorphism

    H1((W tensor W^*) O_C0(-2))^G
       -> H1(E(-1)|_(2C))^G = C.                 (8)

The source invariant is the identity in End(W) times the generator of H1(O_C0(-2)). Under the nonzero first jet of sigma it is exactly the section-line class sigma t, with t a nonzero Cech class in O_C0(-2).

Combining (2),(6),(8), a nonzero actual theta in H1(X,E(-1))^G restricts NONTRIVIALLY to this scalar first-layer class. There is no freedom here to replace the global theta by a convenient local lift.

## 4. Duality has nonzero trace on this actual restriction

Dualizing the actual trace/square sequence

    0 -> E(-4) -> B(-2) -> I_Z^2 -> 0

gives its canonical sheaf map

    r:E(-1) -> omega_(2Z).

On the conic component this factors through E(-1)|_(2C). In an actual oriented regular Serre frame sigma=(f,g), the dual Hilbert--Burch calculation gives

    r(v)=(g v1+f v2)/2 modulo (f^2,g^2),          (9)

with its canonical and determinant frames attached. This is the canonical module represented inside the complete-intersection duality algebra, not an assertion that omega_(2C) is a scalar function sheaf. The regular first conic jet permits f,g to be the two conic normal parameters, up to an invertible oriented frame change.

For the scalar first-layer vector v=sigma t, (9) becomes

    r(sigma t)=fg t,
    Res_(f^2,g^2)(fg t)=Res_(f,g)(t).             (10)

After the conic base trace, (10) is the ordinary nonzero trace H1(O_C0(-2))->C. The actual first-jet and determinant normalization can rescale it only by a nonzero scalar. Thus (8) maps NONTRIVIALLY under conic duality, and the global theta satisfies

    Tr_(2C)(r(theta)|_(2C)) != 0.                (11)

No hidden H0 quotient can kill this trace: (8) already checked the relevant connecting map on invariants. This is an actual comparison of the invariant class with the residue map, rather than multiplication of two unspecified nonzero legs.

## 5. Both coefficients of the actual trace kernel are nonzero

Under Serre duality the connecting map

    H1(I_Z^2)^G -> H2(E(-4))^G

is the functional induced by r(theta) on H0(O_(2Z))^G modulo constants. The total trace of r(theta) annihilates the global constant. Since 2Z is the disjoint union of its conic and vertex components,

    Tr_vertex(r(theta)) = -Tr_(2C)(r(theta)|_(2C)).

Let

    A_theta = Tr_vertex(r(theta)),
    B_theta = Tr_vertex(n8 r(theta)).

Equation (11) proves A_theta!=0. The actual square-shadow kernel is the line spanned by alpha e_v+beta n8, so

    alpha A_theta+beta B_theta=0.                (12)

Here alpha!=0 by the previously proved actual first-normal Serre comparison. If beta were zero, (12) would contradict A_theta!=0. Therefore beta!=0. Equation (12) then also implies B_theta!=0, consistently with the previously known surjectivity of the invariant connecting map.

Thus neither shadow basis vector alone generates the actual kernel. Its coordinate ratio remains

    beta/alpha=-A_theta/B_theta,

with both numerator and denominator now proved nonzero. This theorem determines nonvanishing, not a chosen numerical normalization.

## Sources and verification

The actual vertex homogeneity is in NORMAL-QUADRATIC-NONZERO-BY-SERRE-RESIDUE-DOUBLE-COVER.md. The globally identified degree-four quotient is recorded in ACTUAL-LOWER-COHOMOLOGY-SERRE-INVOLUTION-SPLITTING.md and POSITIVE-SERRE-RESIDUE-AND-CANONICAL-CONE-OPERATOR-CORRECTION.md, with its proof in UNIVERSAL-CUBIC-EVEN-DEFECT-QUOTIENT-IS-TRIVIAL-V.md. The degree-six socle line is proved in ACTUAL-POSITIVE-ATIYAH-MULTIPLICATION-SURJECTS-ONTO-NINE-SPACE.md. Conic balance, conormal bundle and the nonzero actual first jet are in INVARIANT-CONE-CONIC-FIRST-JET-AND-RESIDUAL-DEFECT.md. The dual residue formula is checked in NORMAL-TRACE-DUALITY-HAS-A-SECTION-LINE-RESIDUE.md. The actual alpha!=0 and two-dimensional shadow are in ACTUAL-NORMAL-VARIATION-TRACE-HAS-A-GLOBAL-NULL-HOMOTOPY.md and NORMAL-QUADRATIC-BRACKET-COMPONENT-SHADOW-GATE.md.

Run python verify_actual_normal_trace_nilpotent_nonzero.py. It checks exact finite-group characters, the ideal-square syzygies, the universal dual residue identity, and the cohomological dimension implications after the stated geometric inputs. It does not evaluate any actual coefficients or actual-instance matrices or ranks. All previously published files remain unchanged.
