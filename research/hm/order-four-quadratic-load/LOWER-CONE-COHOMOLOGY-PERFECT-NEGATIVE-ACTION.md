# The exact lower cone cohomology quotient for quadratic multiplication

## Result

For the actual invariant cone and the established positive rank33 closure, there is a canonical surjection

    Psi: H1(B_Q0(2))_+ -> P4 tensor H0(O_L(2))*,

with source representation V+3P4+3D5 and kernel representation 2P4+2D5. Actual multiplication to H1(B_Q0(4))_+=P4 is zero on positive-coordinate quadratics D5, and on negative-coordinate quadratics A=H0(O_L(2)) it is precisely evaluation against Psi. Thus its effective source quotient has dimension12 and its kernel has dimension18. This statement describes an actual cone cohomology module action; it does not select the second-Bockstein scalar.

## Proof

Use the ordinary stack-square notation and canonical normalization in POSITIVE-SECOND-BOCKSTEIN-SQUARE-FILTRATION.md. Its lower exact sequence is

    0 -> P0 -> B_Q0(2) -> Q4 -> 0,
    P0=F_Q0 tensor S(1), Q4=pi_*I_Z^2(4).

Here Q4 denotes the sheaf in this display, while the vertex degree-eight quotient below is written V8 to avoid a notation collision. The ambient spinor resolution tensored by F(1) gives

    0 -> W' F -> W' F(1) -> i_*P0 -> 0.

The actual primary groups are H0(F)=H0(F(1))=0,

    H1(F)=A+W',
    H1(F(1))=P4+W+S4,

and their higher cohomology vanishes. Therefore H2(P0)=0. The physical inversion-positive source and target of the H1 map are

    1+V -> P4+V+D5.

Its only allowed channel is a scalar on V. Since H0(P0)_+ injects into H0(B_Q0(2))_+=1, that scalar is necessarily nonzero. Consequently

    H0(P0)_+=1,
    H1(P0)_+=P4+D5,
    H2(P0)=0.

The canonical quartic normalization proves H0(Q4)_+=0 and

    H1(Q4)_+=H0(V8(4))=V+2P4+2D5.

The long exact sequence therefore gives

    0 -> P4+D5 -> H1(B_Q0(2))_+
      -> H0(V8(4)) -> 0.                         (1)

In particular the source is V+3P4+3D5, of dimension30. This also agrees with the actual ambient quadric restriction sequence, where q0 has invariant one-dimensional kernel on H1(B)_+.

The vertex relation is

    0 -> P4 O_L(-8) -> Sym^8 W' O_L(-4) -> V8 -> 0.

At twist four its boundary gives

    0 -> Sym^8 W' -> H0(V8(4))
      -> H1(P4 O_L(-4)) -> 0.                    (2)

Compose the surjection in (1) with that in (2) to define Psi. Serre duality identifies the target with P4 tensor H0(O_L(2))*, using the canonical trace H1(O_L(-2))=C. Since Sym^8 W'=P4+D5, the kernel in (1)-(2) has representation 2P4+2D5 and dimension18.

The multiplication theorem in POSITIVE-SECOND-BOCKSTEIN-SQUARE-FILTRATION.md says that D5 kills H1(Q4)_+ and that A multiplication is exactly the boundary contraction. The target primary kernel has H1=H2=0, so the square-shadow identification with H1(B_Q0(4))_+ is an isomorphism. Naturality proves both assertions for actual adjoint cohomology, completing the proof.

## Scope

The two exact quotient maps are canonical; a splitting of their representation sequences is not chosen. Finite-group semisimplicity is used only to name the kernel and source representations. The actual quadratic second obstruction theta_a maps to Psi(theta_a); its value is still undetermined. No source coefficient, selected matrix, or actual rank is evaluated.
