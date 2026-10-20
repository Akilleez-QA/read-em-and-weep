# Essential predecessor derivations

These are mathematical extracts from earlier authored proofs and historical reviews. They preserve the essential finite-duality and sign derivations; they do not carry forward an independent-review verdict for the new transport note. Notation is retained: the earlier retained-comparison proof calls P⁴ “B” and the ordered-root product “Y”; PROOF.md here instead calls those Y and Z. The source-level coefficient identification mentioned by the historical constant-projection audit remains a separate premise.

## A. Finite-trace-target source audit, numbered paragraph 4

Public mathematical source: https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6260407782

4. The unit and normalized trace give canonical complementary projectors on m_*O; duality gives the corresponding canonical canonical-sheaf projectors. On the full ordered-root quotient, the original full deck-sign line and the canonical line differ by the ordinary permutation sign. Thus alternation of the original coefficient becomes invariance of canonical forms. Finite-quotient invariant canonical forms are exactly the dual-trace summand from the canonical sheaf of P4. Restricting this full averaging projector to the intermediate invariant space is legitimate; it does not manufacture an S4 action on P2×P2. Consequently the imported alternating two-space is precisely the trace summand, and the retained thirty-space its canonical complementary kernel. Only splitting that kernel into the two twist contributions requires a choice.

## B. Retained-obstruction comparison, complete §§3–5

This is the earlier independent authored derivation, retained as a mathematical dependency rather than asserted to have an older repository commit. Its finite-trace public input is the comment linked in A.

## 3. The intrinsic finite-trace projector

Put A=m_*O_X. Let

    u:O_B→A,                 u(1)=1,
    t:A→O_B,                 t=Tr_func,m/6.

Finite flatness gives t u=Id. Thus p=u t is the canonical projection onto the unit summand, and A=im(p)⊕ker(t). This does not split ker(t) into chosen line summands.

Finite duality gives

    C=m_*ω_X = Hom_B(A,ω_B).

Define

    e:C→ω_B,                 e(f)=f(1),
    i:ω_B→C,                 i(η)(a)=t(a)η.

Then e i=Id, and

    P_tr=i e,                P_ret=Id_C−i e

are complementary canonical idempotents. The map e is Grothendieck canonical trace. On the étale locus i is pullback of top forms divided by six; the everywhere-regular formula f(a)=t(a)η is the definition also at ramification. No naive identification of ω_X with m*ω_B is used.

Write D=End(H). Projection formula gives

    m_*(End(E)⊗ω_X)=D⊗C.

The projectors on this sheaf are Id_D⊗P_tr and Id_D⊗P_ret. Finite pushforward is exact, so they define the same projectors on the obstruction cohomology. The rank-two q₀ acts on D, while P_tr and P_ret act on C. They commute identically. The three normalizations r=2, deg(m)=6, and upstairs coefficient normalization 64 have distinct meanings and must not be substituted for one another.

## 4. Block exchange and its signs

Let c:X→X exchange the two P² factors. Then m c=m, so c acts on A as an O_B-algebra automorphism fixing u and preserving the function trace t. Its induced action on C=Hom(A,ω_B) is the dual action; hence it fixes i, preserves e, and commutes with both finite-trace projectors.

On ω_X=ω_P²⊠ω_P² the canonical exchange sign is (-1)^(2·2)=+1. Equivalently, exchanging two local two-forms introduces no minus sign. On the mixed ideal, exchange of the two ordinary square-zero parameters sends st to ts=st. No odd/super parameter convention is part of this ambient.

The bundle E=m*H has its canonical c-linearization. Together these structures define an involution on K and H²(K). All projectors q₀, (Id+c)/2, (Id−c)/2, P_tr and P_ret commute. The trace summand i(ω_B) is block-even.

The imported splitting types are

    A⁺ ≅ O ⊕ O(-1) ⊕ O(-2),
    A⁻ ≅ O(-1)³.

Duality yields, additively,

    C⁺ ≅ O(-5) ⊕ O(-4) ⊕ O(-3),
    C⁻ ≅ O(-4)³.

The O(-5) in C⁺ is intrinsically im(i). The retained complement in C⁺ is intrinsically ker(e|C⁺), although writing it as O(-4)⊕O(-3) chooses an additive splitting. The imported dimensions give

    dim H²(D⊗C⁺)=2+10+20=32,
    dim H²(D⊗im(i))=2,
    dim H²(D⊗ker(e|C⁺))=30,
    dim H²(D⊗C⁻)=3·10=30.

Only the first thirty-space is the retained target. On the entire obstruction group its canonical retained projector is

    Π_ret = (Id_D⊗P_ret) (Id+c)/2.

Its image equals the kernel of the trace projection inside the block-even subspace. The whole ker(e) also contains the block-odd sector and is larger.

## 5. Why this trace summand is the alternating sector

This identification concerns the classical representation and coefficient geometry, not symmetries of a fixed mixed quantum ambient.

On Y=(P¹)^4 the original full-deck line is L⁻² with ordinary factor-permutation linearization. The canonical sheaf is L⁻²⊗sgn. Therefore tensoring the coefficient interpretation by the canonical-volume identification turns the original S4-sign sector into the invariant canonical-form sector. The paired D8 character (-,-,+) becomes the trivial D8 character on canonical forms, because it is exactly sgn restricted to D8.

The ordered quadratic-factor quotient X=Y/(S2×S2) has a residual block exchange, and its block-even canonical-form sector is the D8-invariant intermediate sector. The canonical inclusion of forms from B=Y/S4 and Grothendieck trace give exactly the invariant averaging idempotent restricted to that intermediate sector. On a generic orbit this is average over the six ordered pair decompositions, namely the unit/normalized function-trace dual projector in §3; equality of regular sheaf maps extends across the branch locus.

Thus original full alternation corresponds to P_tr. The original retained sign-kernel corresponds to Π_ret. No S4 action on X, or on the fixed two-axis ambient, has been constructed or needed. Nor has any claimed full-alternation boundary of a particular class been used in defining the projector.

## C. Constant-projection source audit, coefficient-projector portion of §5

Public mathematical source: https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6274541018

The excerpt starts after the actual-source primitive discussion and ends before the class-level vanishing inference. Neither the primitive nor the actual-source identification is needed or newly established by PROOF.md.

Let A=m_*O_X and t=Tr/6, u(1)=1. Finite duality identifies m_*omega_X with Hom(A,omega_P4). Dualizing u t gives the idempotent

P_const(lambda)(f)=lambda(1)Tr(f)/6.

Its normalization follows from Tr(1)=6. The original coefficient-line sign representation becomes the invariant canonical-form representation after the canonical-volume twist. Full S4 alternation on the pair sector is therefore exactly this projector, as checked on the dense etale locus and extended as equality of regular sheaf maps.

The map j on cohomology is injective because finite pushforward is exact and finite invariants are a split exact summand, with the specified invariant coefficient sheaf identification. This does not follow merely from an arbitrary injective sheaf map; that would not suffice on H². Ramification is handled by the actual invariant coefficient sheaf and finite duality, without dividing by a branch equation.
