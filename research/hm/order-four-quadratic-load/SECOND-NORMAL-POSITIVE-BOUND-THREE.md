# The actual second-normal positive kernel is at most three-dimensional

## Theorem

Let F be normalized Horrocks–Mumford, B=End_0(F), R=P(V) its positive inversion-fixed plane, and W the dual negative two-space. For a general smooth inversion-even quadric Q, set C=Q intersect R and I=I_(C/Q). Then

    h0(Q,I^2 B_Q(4))_+ <= 3.

More precisely, fix any smooth positive conic q_+ and any nondegenerate negative quadratic direction q_-. The bound holds outside finitely many nonzero scalar multiples of q_-. Thus it holds on a nonempty open of negative blocks for every smooth positive conic, and on a nonempty open of the smooth-even family.

The new input is a nonzero ACTUAL cup-commutator, proved using the balanced invariant conic and its actual restriction boundary. The first positive scaling obstruction has rank six, not merely a possible or generic rank. Its three-dimensional kernel is explicitly identified. This does not prove that all three kernel vectors lift, that the bound is attained, or that the total even corank is four.

## 1. Established geometric inputs and notation

Write B_R=B|R and use plane twists throughout. The actual stable Steiner presentation is

    0 -> A O_R(-3) -> D O_R(-2) -> F_R -> 0.

Here A is the irreducible A5 three-space different from V, D is the irreducible five-space, and Sym^2 W=A. The established plane cohomology gives

    S:=H0(B_R(2))=A,  H1(B_R(t))=0 for t>=2,
    H0(B_R)=0,  H1(B_R(-6))=0.                         (1)

Let C0=(q0=0) be the invariant smooth conic. Its balanced restriction and actual linearization give

    B_C0 = A tensor O_C0,
    H0(O_C0(2))=5.

Put

    K:=H0(B_C0)=A.                                     (2)

The argument below needs only the reduced balanced restriction and its actual linearization. It does not require splitting the doubled conic or its endomorphism algebra.

Finally the actual ambient second-normal comparison class is nonzero:

    zeta in (Sym^2 W tensor H1(B_R(-2)))^A5.

Its coefficient map i_zeta:(Sym^2 W)* -> H1(B_R(-2)) is an injection onto the unique A-constituent. Indeed

    H1(B_R(-2))=D* tensor A=V directsum A directsum 4 directsum 5.

These facts concern the actual bundle and linearizations, not a freely selected equivariant model.

## 2. Identifying the zeta coefficient space by an actual boundary

The restriction sequence of the invariant conic gives an injective boundary

    j:K -> H1(B_R(-2)),
    0 -> B_R(-2) --q0--> B_R -> B_C0 -> 0.             (3)

Its injectivity follows from H0(B_R)=0. It is a nonzero equivariant injection of A. Uniqueness of the A-constituent implies that j and i_zeta have the same image and differ only by a nonzero scalar after an equivariant identification of their domains.

This step uses BOTH the actual nonvanishing of zeta and its unique coefficient constituent. Nonvanishing of zeta alone would not prove nonvanishing of its action on sections.

## 3. The actual cup-commutator does not vanish

Consider the cup-commutator

    beta:S tensor K -> H1(B_R),
    beta(s,c)=[s,j(c)].                                (4)

The conic restriction sequence yields

    0 -> S -> H0(B_C0(2)) --delta_C--> H1(B_R) -> 0,   (5)

because H0(B_R)=0 and H1(B_R(2))=0. The exact naturality identity is

    beta(s,c)=delta_C([s|C0,c]).                    (6)

To check it, lift c locally to sections c_i of B_R and write their differences as q0 d_ij. Then j(c) is represented by d_ij. Local lifts of [s|C0,c] are [s,c_i], whose differences divided by q0 are [s,d_ij]. These are precisely the cocycle for (4), up to the same harmless common boundary-sign convention.

Suppose beta were zero. By (5)–(6), the three-dimensional image of S in

    H0(B_C0(2)) = sl_2 tensor H0(O_C0(2)) = A tensor 5

would be invariant under commutator with every constant element of sl_2. Since the adjoint sl_2 representation is irreducible, a three-dimensional sl_2 submodule of this isotypic module is necessarily sl_2 tensor L for a one-dimensional subspace L of H0(O_C0(2)). This follows directly from complete reducibility and Schur's lemma.

But S is also A5-stable. The A5 action on constant sl_2 normalizes its adjoint action, so stability of sl_2 tensor L forces L to be A5-stable. This is impossible in the irreducible five-dimensional representation H0(O_C0(2)). Therefore

    beta != 0.                                         (7)

In particular the actual action of the coefficient space of zeta on S is nonzero.

Equation (5) also identifies

    H1(B_R)=(A tensor 5)/A = V directsum 4 directsum 5.

Since A tensor A=1 directsum A directsum 5, beta has image exactly the unique five-dimensional constituent. It is a nonzero scalar multiple of the unique equivariant projection A tensor A -> 5. This proves the scalar nonvanishing geometrically, rather than assuming it from representation dimensions.

## 4. The actual first scaling obstruction and its necessary quotient

Fix Q:q_+(x)+q_-(y)=0 with both blocks nondegenerate. On the complement of the negative line, let p be projection to R and let

    g_epsilon(x,y)=(x,epsilon y).

As in the scaling theorem, work with the positive part, after finite pushforward to R, of the proper flat finite module

    (I^2/I^10) tensor g_epsilon*B(4).

At epsilon zero its global section space is canonically

    S tensor Sym^2 W,                                  (8)

of dimension nine. The map sends s tensor p(y) to the actual polynomial normal-degree-two section. It includes the q_- direction, which becomes -q_+ under the quadric equation. The exact harmonic decomposition identifies the resulting index-zero and index-two pieces with the three copies of B_R(2)|4C; all other summands have no sections.

Inversion-equivariant local frames can be chosen even along R. Their projective transition functions have no first normal term, and their second-normal term represents zeta. Pulling back by g_epsilon therefore gives no epsilon-linear deformation and an epsilon-squared adjoint deformation represented by ad(zeta(y)). The first possible lifting obstruction on (8) is consequently

    s tensor p |-> [zeta(y),s] p(y),                   (9)

initially a class in H1(B_R) tensor Sym^4 W. Changing frames changes this cocycle by a coboundary, so (9) is the actual deformation boundary, not a chosen representative-dependent map.

The target on the fixed quadric is NOT the full quartic space. A term divisible by q_- becomes a multiple of -q_+. Its cohomology factors through H1(B_R(2)) or H1(B_R(4)), both zero. Thus (9) factors through

    L_q:S tensor Sym^2 W
        -> H1(B_R) tensor (Sym^4 W / q_- Sym^2 W).      (10)

Conversely the harmonic-degree-four part maps by restriction into

    H1(B_R|3C) tensor (Sym^4 W / q_- Sym^2 W).

The restriction H1(B_R)->H1(B_R|3C) is injective by H1(B_R(-6))=0. Hence no further quotient in the actual finite-module obstruction group lowers the rank of (10). All of its image lies in the five-dimensional constituent of H1(B_R).

## 5. Exact universal kernel of the nonzero obstruction

Identify A=Sym^2 W and the target five-space with Sym^4 W. Multiplicity one implies that the nonzero beta is a scalar multiple of binary multiplication Sym^2 W tensor Sym^2 W -> Sym^4 W, using the invariant symplectic form to identify the dual coefficient space.

Use two formal binary-variable sets x,y, and let Delta(x,y) be their invariant alternating pairing. The coevaluation tensor of Sym^2 W is a nonzero scalar multiple of Delta(x,y)^2. Accordingly the map before the quotient in (10) has the universal polynomial expression

    F(x,y) |-> c Delta(x,y)^2 F(x,y),  c!=0,
    F in Sym^2 W_x tensor Sym^2 W_y.                  (11)

This is an identity of intertwiners, not a selected HM coefficient calculation.

After quotienting the y-degree-four factor by q_-(y) Sym^2 W_y, the image is zero exactly when q_-(y) divides Delta(x,y)^2 F(x,y). The irreducible polynomial Delta genuinely depends on x and is coprime to every nonzero polynomial q_-(y). Unique factorization therefore implies q_-(y) divides F(x,y). Bidegree (2,2) then gives precisely

    ker L_q = S tensor <q_->,
    dim ker L_q=3,  rank L_q=6.                       (12)

The universal kernel calculation is valid for every nonzero quadratic q_-, even singular ones. The scaling theorem itself uses nondegenerate blocks so that the quadrics are smooth. For such a block, an equivalent description is evaluation at its two roots: each root contributes an injective three-dimensional multiplication map, and the common kernel is exactly the quadratic multiple in (12).

## 6. From the first obstruction to the actual bound

Localize the scaling parameter line at zero. Properness and flatness make the module of relative global sections finite and torsion-free over this discrete valuation ring, hence free. Its reduction injects into the limiting section space (8), and its dimension is the generic fiber dimension.

Every relative section has zero epsilon-squared obstruction, since the epsilon-linear deformation is zero. Its reduction therefore lies in ker L_q. Equations (10)–(12) bound the generic positive finite-module section dimension by three. Upper semicontinuity then gives the same bound outside a finite set of scaling parameters.

For epsilon nonzero, g_epsilon identifies the fixed Q with the actual quadric

    q_+ + epsilon^(-2) q_- = 0.

The established uniform seventh-power vanishing implies H0(I^10 B_Q(4))=0, so H0(I^2 B_Q(4)) injects into the finite-module section space. This proves the theorem along the scalar family. The finite map epsilon -> epsilon^(-2) on C* preserves the stated finite-exception conclusion. Openness in the smooth-even parameter space gives the remaining generic assertions.

The explicit three-dimensional kernel in (12) consists of possible first-order survivors only. Higher deformation obstructions may remove some or all of it. No equality or lifting statement is inferred.

## Dependencies and scope

- INVARIANT-CONIC-SECOND-NORMAL-COLLAPSE.md supplies the actual opposite-three representation, balanced C0 and its adjoint linearization, and the plane cohomology.
- ACTUAL-AMBIENT-SECOND-NORMAL-NONVANISHING.md supplies zeta!=0 and its unique coefficient constituent. ACTUAL-SECOND-NORMAL-AFFINE-LAW.md defines the actual comparison torsor and its scaling naturality.
- THIRD-NORMAL-VANISHING-BY-SCALING.md supplies the proper flat finite module, exact harmonic decomposition, nine-dimensional limiting space, and uniform ideal-power input.

The new deductions are the conic boundary proof that the actual cup scalar is nonzero, the precise harmonic quotient of its deformation target, and the resulting bound three. No selected HM/source coefficients, evaluated actual matrix ranks, scans, or experiments are used. The lower positive excess boundary, first-order odd global gate, and complete proof repair are not asserted here.
