# The actual lower-map family kernel and the six-to-two third gate

## Scope and inputs

This is a global-family consequence of ACTUAL-NEGATIVE-INVOLUTION-SECTOR-AS-SQUARE-QUOTIENT.md at 6c724c3b74e2ae4d6992d8c7b99b41c0715d69c0. That theorem identifies the actual lower multiplication with perfect contraction after its common kernel. The two-dimensional space of third gates was already established in POSITIVE-LAST-SMITH-FACTOR-AND-CUBIC-OBSTRUCTION.md; it is not claimed anew here.

Put P=P(A), the projective plane of negative quadratic directions. Let C be the actual thirty-dimensional lower positive cohomology space, Cminus its twenty-one-dimensional negative Serre-involution sector, and R its common kernel of dimension eighteen. The actual quotient is C/R=P4 tensor A*, where A*=H1(O_L(-4)). The finite Serre sign is retained as in the source theorem and does not change the G-representations below.

## 1. A uniform family with no exceptional directions

The actual family of lower multiplication maps is

    C tensor O_P -> P4 tensor O_P(1).

It is onto at every point, including square directions. After quotienting by R it is id_P4 tensored with the Euler evaluation A* O_P -> O_P(1). Therefore its kernel K has an exact sequence

    0 -> R O_P -> K -> P4 tensor Omega_P^1(1) -> 0.

A G-equivariant linear splitting of C -> C/R supplies a bundle splitting. Consequently

    K is isomorphic to R tensor O_P plus P4 tensor Omega_P^1(1).

The constant factor has underlying bundle 18 O_P, not eighteen trivial G-representations.

Its rank is twenty-six, with c1(K)=-4H and c2(K)=10H^2, directly from c(K)=(1+H)^(-4). The common kernel R is intrinsic; the displayed direct-sum splitting need not be canonical. On Cminus the constant factor is (P4+D5) tensor O_P, with underlying bundle 9 O_P; its full kernel has rank seventeen.

## 2. Pull back the actual second-symbol image

Let Sigma be the established length-twenty-four degeneracy scheme of the actual nonzero second symbol. Its Hilbert--Burch presentation, twisted by one, is

    0 -> A O_P(-1) -> P4 O_P(1) -> I_Sigma(7) -> 0.

Define E as the sheaf-theoretic inverse image of the first term under the contraction P4 tensor A* O_P -> P4 O_P(1). Because contraction is everywhere onto, this definition gives

    0 -> P4 tensor Omega_P^1(1) -> E -> A O_P(-1) -> 0. (1)

In particular E is locally free, including at Sigma. The extension group in (1) vanishes: it is a constant representation tensored with H1(Omega_P^1(2)), which is zero by the Euler sequence and surjectivity of multiplication of linear forms. Thus

    E is isomorphic to P4 tensor Omega_P^1(1) plus A O_P(-1).

Again, no canonical splitting is asserted. The intrinsic object is the sheaf-theoretic pullback kernel. Its inclusion into the trivial twelve-bundle is not a subbundle at Sigma: its fiber there must not be identified with the pointwise inverse image of the degenerate second-symbol fiber. Its Chern classes are c1(E)=-7H and c2(E)=25H^2, consistent with c2(I_Sigma(7))=24H^2.

## 3. Exact reduction of universal operator coefficients

An equivariant reduced quadratic operator family is a map

    D5 O_P(-2) -> P4 tensor A* O_P.

Its contraction, followed by the second-symbol quotient, is the actual type of third gate D5 O_P(-2) -> I_Sigma(7), equivalently D5 O_P(-3) -> I_Sigma(6).

Twist the kernel sequence defining E by two. H1(E(2))=0: (1) reduces this to H1(Omega_P^1(3))=0 and H1(O_P(1))=0. The first is again the Euler sequence and polynomial multiplication. Therefore the map on equivariant coefficient spaces is onto, with kernel Hom_G(D5,H0(E(2))). Universal character arithmetic gives

    dim Hom_G(D5,P4 tensor A* tensor Sym2 A*) = 6,
    dim Hom_G(D5,H0(E(2))) = 4,
    dim Hom_G(D5,H0(I_Sigma(9))) = 2.

For completeness, H0(Omega_P^1(3)) has character A+D5. Thus

    H0(E(2)) = P4 tensor (A+D5) plus A tensor A*,

with three D5 copies in the first term and one in the second. Their roles are distinct: the first three are invisible already under contraction; the last is removed by the second-symbol image. This decomposition uses a splitting of (1), while the four-dimensional kernel itself is canonical.

Before quotienting by the common nine-space in Cminus, the equivariant quadratic operator-family space has dimension eleven. Five dimensions land in that common kernel. Hence the exact coefficient reductions have dimensions

    11 -> 6 -> 2,

with kernels of dimensions five and four, respectively. This sharpens the bookkeeping for the actual operator calculation. It does not evaluate any of its coefficients. A nonzero reduced operator family may still belong to the four-dimensional kernel, and a vanishing third gate still leaves higher gates to examine.

## 4. The actual trace-free normalization still has two final gates

The actual quadratic family can be taken in the trace-free summand Sym4 W of Sym2(A)=1 plus Sym4 W. Indeed the Hamiltonian vector fields of binary quadratics satisfy

    s^2 D_(t^2) + t^2 D_(s^2) - 2st D_(st) = 0.

Equivalently, a D_a factors through the binary quartic a^2. Atiyah contraction is O-linear, so the actual right-hand side a h zeta_a has the same property. The proved second obstruction vanishes on h in D5; choose a fixed equivariant linear right inverse of q0 on its image to obtain v(a,h). That choice preserves the factorization. Changing this right inverse changes v by an original kernel vector. Since the entire first Bockstein vanishes for every direction, its lower restriction belongs to the common kernel of multiplication. Thus the reduced actual class in P4 tensor A* is independent of that choice and has zero quadratic trace channel.

Restrict v to the actual lower space C and project to Cminus. This linear projection preserves trace-freeness and does not change its class modulo R, since Cplus is contained in R. The trace-free universal spaces have dimensions nine before the common-kernel quotient and five afterward; the common-kernel coefficient space has dimension four. This removes the single trace coefficient from the six-space, but it does NOT remove a final third gate.

To see this last point without guessing ranks, use the invariant nondegenerate form on A and a nonzero equivariant map T:D5->P4 tensor A, unique up to scalar. For v=T(h), define the quadratic family

    B_v(a) = (a dot a)v - a tensor (contraction_a v).

Its contraction with a is identically zero, while its quadratic parameter Laplacian is 4v in dimension three. Hence the contraction kernel maps nontrivially, and therefore onto, the one-dimensional trace coefficient space. Any six-space family can have its trace removed by a zero-contraction family. The trace-free five-space still surjects onto the established two third-gate coefficients, with a three-dimensional kernel.

The independent operator-level formulation is recorded in ACTUAL-QUADRATIC-OPERATOR-HAS-A-TRACE-FREE-NORMAL-FORM.md. These are exact normalizations of the coefficient problem. They do not evaluate either remaining actual coefficient, prove that the cubic output is nonzero, or remove the need to examine higher gates if that output vanishes.

## Reproduction

Run verify_lower_map_family_gate.py. It checks the representation multiplicities and dimension identities using universal character arithmetic. The actual family identification, Euler sequences, and vanishing arguments above supply the geometric proof; no actual source coefficients, matrices, ranks, or scans are used.
