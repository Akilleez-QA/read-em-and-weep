# The actual ambient second-normal class is nonzero

## Theorem

Let F be normalized Horrocks–Mumford on P4, B=End_0(F), and R=P(V_+) the positive fixed plane of the standard inversion. Put W=V_-*, J=I_R, F_R=F|R, and B_R=End_0(F_R). Let

    zeta in (Sym^2 W tensor H1(R,B_R(-2)))^A5

be the actual second-normal projective comparison class defined using the canonical projection

    p:P4 minus P(V_-) -> R.

Then zeta is NONZERO. Its invariant class space is one-dimensional, so the actual ambient class is a nonzero member of that line. Equivalently, its coefficient map

    (Sym^2 W)* -> H1(R,B_R(-2))

is an injection of the actual irreducible three-dimensional representation.

This is proved by equivariant formal extension and an elementary restriction theorem for global sections along a linear plane. No formal algebraization theorem, extension of a vector bundle across the negative line, selected HM coefficients, or evaluated matrix rank is used. The theorem does not assert nonvanishing of zeta_C on every conic: its restriction to the invariant conic is known to vanish.

## 1. Required plane cohomology

The actual plane restriction has the stable Steiner presentation

    0 -> A tensor O_R(-3) -> D tensor O_R(-2) -> F_R -> 0,
    dim A=3, dim D=5.

Here A and D are irreducible normalizer coefficient representations. The established plane lemma gives

    H1(B_R(-4)) = V directsum A,

where V and A are three-dimensional A5 representations. The argument below only needs that this space contains no irreducible five-dimensional constituent.

Because det F_R=O_R(-1), the symmetric-square resolution is

    0 -> wedge^2 A tensor O_R(t-5)
      -> A tensor D tensor O_R(t-4)
      -> Sym^2 D tensor O_R(t-3)
      -> B_R(t) -> 0.                                  (1)

For every t>=2, the middle and last line-bundle terms have no H1 or H2, and the first has no H1. Its possible H2 contributes to H0 of the resolved bundle, not H1. Splitting (1) into two image sequences therefore gives

    H1(B_R(t))=0 for all t>=2.                         (2)

At t=2, the three terms have twists -3,-2,-1. Only the H2 of the first survives, so

    H0(B_R(2)) = wedge^2 A tensor H2(O_R(-3)),
    h0(B_R(2))=3.                                     (3)

Self-duality of B_R and Serre duality on R yield

    H1(B_R(-m)) = H1(B_R(m-3))* = 0 for m>=5.           (4)

Stability also gives

    H0(B_R(-m))=0 for every m>=0.                      (5)

For m>0 this is the absence of a morphism F_R -> F_R(-m) between stable bundles of strictly decreasing slope; for m=0 it is simplicity after removing scalars.

## 2. Formal comparison and its exact obstruction spaces

Let R_n be the n-th normal neighborhood with structure sheaf O_P4/J^(n+1), so R_0=R. All these schemes lie in the open domain of p. Write

    A_n=End(F)|R_n,
    A_n^ref=p*End(F_R)|R_n.

These are Azumaya O_Rn-algebras. Their reductions at n=0 are canonically identified. The normal graded pieces are

    J^n/J^(n+1)=Sym^n W tensor O_R(-n).                 (6)

Suppose a comparison A_(n-1) -> A_(n-1)^ref has been constructed. Its local lifts to order n exist because the automorphism group of a matrix algebra is the smooth group PGL_2. The sheaf of such lifts is a torsor under the additive vector bundle

    B_R tensor Sym^n W tensor O_R(-n).

Thus its obstruction class belongs to

    Sym^n W tensor H1(B_R(-n)).                        (7)

If that class is zero, the set of global lifts is a torsor under the corresponding H0, which vanishes by (5). Consequently every successful lift is UNIQUE.

Start with the identity on R. The actual bundle, projection, and identity comparison are equivariant under the finite normalizer subgroup preserving the inversion splitting. Inductively, uniqueness makes each comparison equivariant. Hence every obstruction class in (7) is an invariant tensor. This establishes invariance of the actual successive classes, not merely a choice of invariant representatives.

At n=1 the obstruction is zero by inversion parity. The central inversion acts trivially on R, B_R, and O_R(1), and acts by -1 on W. Therefore every odd-n obstruction space has negative central character and has no invariant vectors.

At n=2 the class in (7) is exactly zeta. Indeed, after the unique first-order comparison, passing to inversion invariants retains the full second-normal kernel Sym^2 W O_R(-2); its comparison torsor is the one used to define zeta on the invariant algebra of R_2. Thus there is no extra independent second-normal class discarded by taking invariants.

## 3. If zeta vanished, all higher projective obstructions would vanish

Assume, for contradiction, that zeta=0. The preceding argument gives the unique comparison through order two, and the odd third-order class vanishes by inversion.

For n=4, Sym^4 W is the irreducible A5 representation of dimension five. This needs no selected character realization: Sym^2 W is one of the irreducible A5 three-spaces, and

    Sym^2(Sym^2 W) = 1 directsum Sym^4 W,
    Sym^2(3)=1 directsum 5.

Therefore

    (Sym^4 W tensor H1(B_R(-4)))^A5
      = (5 tensor (V directsum A))^A5 = 0.             (8)

The fourth-order obstruction vanishes. For every n>=5, the entire cohomology group H1(B_R(-n)) is zero by (4), without needing equivariance. The comparisons consequently extend uniquely and compatibly to every order. Passing to the inverse limit gives an actual formal algebra isomorphism

    End(F)^hat_R = p*End(F_R)^hat_R.                    (9)

Algebra isomorphisms preserve the reduced trace. Removing scalars therefore gives a formal isomorphism of trace-free adjoint bundles. On the projection domain there is also the canonical line-bundle identification p*O_R(1)=O_P4(1). After twisting by two, (9) produces

    B(2)^hat_R = p*(B_R(2))^hat_R.                     (10)

Every section in the nonzero three-dimensional space (3) pulls back to a compatible formal section on the right. These formal sections are independent, since their restrictions to R recover the original sections. Hence zeta=0 would imply

    h0(formal R, B(2)^hat_R) >= 3.                     (11)

Neither a splitting of the geometry of a conic neighborhood nor a lift of projective comparisons to vector-bundle comparisons is needed.

## 4. Elementary global-to-formal comparison along a linear P2

We prove the needed statement directly. For any vector bundle E on P4, restriction induces an isomorphism

    H0(P4,E) -> lim_m H0(P4,E tensor O_P4/J^m).         (12)

The ideal J is generated by two independent linear forms. Its powers have the exact resolution

    0 -> O(-m-1)^m -> O(-m)^(m+1) -> J^m -> 0.

Tensoring with the locally free E remains exact. For sufficiently large m,

    H0(E(-m))=0,
    H1(E(-m-1))=H1(E(-m))=H2(E(-m-1))=0.

The first assertion is eventual absence of sections after sufficiently negative twisting. The others follow from Serre duality on P4 and positive Serre vanishing for E*. The power resolution then gives

    H0(J^m E)=H1(J^m E)=0

for all sufficiently large m. Restriction H0(E)->H0(E/J^m E) is therefore an isomorphism for every sufficiently large m, proving (12), with compatibility under the actual restriction maps.

This proof applies to E=B(2). It uses only finite locally free resolutions and cohomology, not a formal-Lefschetz existence theorem.

## 5. The actual ambient H0(B(2)) is zero

This vanishing is an immediate consequence of the pinned actual exterior-symmetric evaluation resolution. Let U=H0(F(3)), d=det U, and let ell be the rank-one evaluation cokernel on the twenty-five disjoint HM lines L. Twisting that resolution gives

    0 -> d O(-8) -> wedge^2 U O(-3)
      -> U tensor F -> B(2) -> ell^2(-3) -> 0.          (13)

On each line ell has degree -1, so the tail in (13) is O_P1(-5) and has no global sections. Let K1 and K0 be the two intermediate image sheaves. The sequence

    0 -> d O(-8) -> wedge^2 U O(-3) -> K1 -> 0

gives H1(K1)=0. Since normalized F is stable, H0(F)=0, and

    0 -> K1 -> U tensor F -> K0 -> 0

gives H0(K0)=0. Finally

    0 -> K0 -> B(2) -> ell^2(-3) -> 0

proves

    H0(P4,B(2))=0.                                    (14)

No surjectivity of a tail boundary, no rank of the quadric multiplication pencil, and no equation-degree statement for the twenty-five lines is needed for (14).

Combining (12) and (14) contradicts (11). Therefore zeta is nonzero, proving the theorem.

## 6. Exact consequence and limitations

The already established representation calculation is

    H1(B_R(-2)) = D* tensor A,
    dim (Sym^2 W tensor H1(B_R(-2)))^A5 = 1.

Since Sym^2 W is irreducible, the nonzero invariant tensor just proved identifies its dual with the corresponding irreducible three-dimensional summand of H1(B_R(-2)). This fixes the zero-versus-nonzero ambiguity in the actual ambient normal extension; it does not choose a scalar normalization or a matrix presentation.

Restriction to a conic is a different operation. In particular, the invariant conic has zeta_C0=0 despite the ambient nonvanishing. No rank, noncommutativity, or lifting statement for every conic follows from the ambient coefficient injection alone. The theorem does not establish a remaining global positive or odd full-adjoint gate.

## Sources and dependencies

- ACTUAL-SECOND-NORMAL-AFFINE-LAW.md, published at 028320f238a8a8cae5f14faf6b6836201baa496d, defines the actual comparison torsor and proves its one-dimensional invariant class space.
- ACTUAL-CONIC-DISCRIMINANT-AND-JUMP-STRATA.md, at 313c54bec3f2556518dd531a8ce71f7a8ce22461, supplies the actual stable Steiner restriction and its representation spaces.
- INVARIANT-CONIC-SECOND-NORMAL-COLLAPSE.md, Section 5, proves H1(B_R(-4))=V directsum A by the coefficient-free Steiner argument. Its other-three identification is not needed beyond the displayed absence of a five-dimensional constituent.
- The actual exterior-symmetric evaluation resolution is at d5d9bd997145b0ecf7d7bd659a19fb7845afb75f. Its compatible version is also reproduced in PR463, Section 2, at 8ec3631dcd6937e6cc7491d0200c1c78b5d21434, research/hm/order-four-residue/PROOF.md, read directly for this proof:
  https://github.com/Akilleez-QA/read-em-and-weep/blob/8ec3631dcd6937e6cc7491d0200c1c78b5d21434/research/hm/order-four-residue/PROOF.md

The new content is the forced equivariant formal extension under zeta=0 and the elementary global-section contradiction. All statements concern the actual HM bundle and actual normalizer action. No selected coefficients, actual evaluated ranks, scans, or public writes are used.
