# The full lower family is determined by secant restriction and parameter trace

## Statement and scope

Work in the fixed actual canonical probe normalization over C. Write G=SL2(F5), A=Sym²W, D=D5, and X=P(A). The canonical correction is

    L_can(a,h)=γ S_h a,     γ≠0,

where h↦S_h is the fixed equivariant identification of D with trace-free self-adjoint endomorphisms of A. Its everywhere-surjective bundle map gives

    0 → K → D O_X → A O_X(1) → 0.

Let Cbar=C/J be the actual lower quotient. Its established involution decomposition is

    Cbar=Cminus ⊕ P4,     Cminus=V+2P4+2D,
    Cbar=V+3P4+2D,        dim Cbar=25.

For the space of equivariant quadratic lower families

    Q_lower=Hom_G(D,H0(Cbar O_X(2))),

the combined map of canonical secant restriction and parameter trace is an isomorphism

    Q_lower → Hom_G(K,Cbar O_X(2)) ⊕ Hom_G(D,Cbar),
    dimensions          13 → 11 + 2.                         (1)

For the endpoint P4 summand alone, restriction is already an isomorphism

    Hom_G(D,H0(P4 O_X(2))) → Hom_G(K,P4 O_X(2)),
    dimensions                         2 → 2.                (2)

Consequently restricting to K removes the canonical source correction but does NOT remove the unknown endpoint variation. The two endpoint channels remain fully detectable there. These are reconstruction statements about whole equivariant families, not evaluations of the actual family or of a fourth obstruction.

## 1. Exact restriction and its two-dimensional kernel

Apply global Hom(-,Cbar O_X(2)) to the secant sequence. The relevant extension group is

    Ext¹(A O_X(1),Cbar O_X(2))
      =Hom(A,Cbar) ⊗ H¹(X,O_X(1))=0.

Taking G-invariants is exact in characteristic zero. Thus restriction is onto and has kernel

    Hom_G(A,Cbar⊗H0(O_X(1)))=Hom_G(A⊗A,Cbar).               (3)

Self-duality of A is used throughout. Since

    A⊗A=1+A+D,

and Cbar has neither 1 nor A, every element of (3) is uniquely of the form

    R(a,b)=T((a⊙b)_0),

where T maps the trace-free symmetric tensors D to Cbar. There are exactly two such channels. Here a⊙b=(ab^t+ba^t)/2 and the subscript means removing its scalar trace.

The resulting kernel family is q(a,h)=R(a,L_can(a,h)).

## 2. Parameter trace detects the entire restriction kernel

Use the invariant nondegenerate symmetric form on A. For an orthonormal basis e1,e2,e3 define the parameter trace of a quadratic family by

    Tr_A(q)(h)=Σ_i q(e_i,h).

This definition is basis-independent and equivariant; it is contraction in the two parameter slots, not the trace of an adjoint bundle endomorphism. For the kernel family above,

    Tr_A(q)(h)=γ T(Σ_i(e_i⊙S_h e_i)_0)=γ T(S_h).             (4)

The middle identity follows because S_h is symmetric and trace-free. Since γ and h↦S_h are nonzero isomorphisms in the indicated representation slots, (4) maps the entire restriction kernel isomorphically onto Hom_G(D,Cbar).

Therefore (restriction,trace) is injective. Conversely, lift an arbitrary secant-restricted family using the surjectivity in Section1; adjust its trace arbitrarily by the unique kernel family supplied by (4). This proves surjectivity and (1), without choosing a splitting of the effective twelve-dimensional quotient.

## 3. Exact dimensions and the endpoint conclusion

The character identities are

    Sym²A=1+D,
    V⊗D=A+V+P4+D,
    P4⊗D=A+V+P4+2D,
    D⊗D=1+A+V+2P4+2D.

They give dim Q_lower=13 and dim Hom_G(D,Cbar)=2, hence the restriction target has dimension11.

Replace Cbar by P4 in the exact restriction sequence. There is no P4 in A⊗A, so the factoring kernel is zero. The extension group still vanishes. Also Hom_G(D,P4)=0, so parameter trace is automatically zero for every endpoint family. Finally Hom_G(D,P4⊗Sym²A) has dimension2. This proves (2).

## 4. Application to the actual corrected source

The uncorrected family [v_h] has zero parameter trace, while

    x(a,h)=[v_h−L_can(a,h)ζ_a]

has the established forced nonzero trace. Its correction is a family in the restriction kernel because L_can vanishes on K. Thus x and [v_h] have the same K-restriction, but their traces distinguish them exactly by (1).

The endpoint P4 component is unchanged by this correction, since aζ_b lies in Cminus. Equation(2) shows why a secant-restricted calculation cannot discard that endpoint datum unless its actual vanishing is proved. This does not assert that the endpoint component is nonzero, or that knowing the lower source suffices to evaluate the next ambient division.

The results concern the whole quadratic lower family in a fixed canonical normalization. They do not identify arbitrary Schur gauges, eliminate the actual secondary residue, or determine the fourth Bockstein, Smith exponent, full repair, or algebraicity.

## Dependencies and reproduction

Use the canonical secant-bundle theorem at 4e16e69c776bd85506341b5bb785f0d8a396bd3e, and the actual lower comparison and corrected-source trace theorem at c85c756d333281eccefdb77c4899db4f923d768e, all in research/hm/order-four-quadratic-load of Akilleez-QA/read-em-and-weep.

Run python3 verify_lower_family_secant_trace.py. It checks exact universal character multiplicities and the symbolic trace identity (4). The bundle exactness and actual-map comparisons are proved above or supplied by the pinned dependencies. No actual HM coefficient, point, source-instance matrix or rank experiment is selected.
