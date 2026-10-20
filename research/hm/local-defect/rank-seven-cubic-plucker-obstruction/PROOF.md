> Publication scope: preserved mathematical proof/audit. Historical statements that rank eight remains open are superseded only after the final assembly and all its prerequisites. No source-instance evaluation or formal verification is claimed here.

# Rank seven cannot have residual kernel degree three

## Result

Under the hypotheses of ../global-linear-image-plucker/PROOF.md and the representation and perfectness inputs audited in ../rank-nine-kernel-splitting/PROOF.md, generic rank(Q)=7 forces

    (k,d,e)=(3,0,8).

Both previously allowed residual-degree-three branches are impossible. The obstruction is the representation identity

    Hom_N(V, Lambda^3 Sym^2 V)=0.

No decomposability of an exterior lift, global basepoint-freeness, constant-rank assertion, or evaluation of an operation is used.

## 1. Notation and exact representation inputs

Let H=H5 and G=SL2(F5), with N=H semidirect G as in the existing proofs. Let V be the five-dimensional defining N-module of H-central character zeta, and A its five-dimensional module of central character zeta^2. Write P and Q for the two inequivalent irreducible two-dimensional G-modules called W and W' in ../../cubic-loci/canonical-cubic-extension/cubic-massey-module-reduction/PROOF.md. Set

    T_P=Sym^2 P,     T_Q=Sym^2 Q.

These G-modules are inflated to N when used in tensor products. The existing inputs are

    Lambda^2 V = A tensor P,
    Sym^2 V = A tensor T_Q,
    V tensor A = A* tensor (T_P direct-sum Q).                 (1)

The first two occur in Section 4 of ../../cubic-loci/canonical-cubic-extension/cubic-massey-module-reduction/PROOF.md, with their irreducibility consequences explained in Section 1 of ../rank-nine-kernel-splitting/PROOF.md. The third occurs in Section 3 of the cubic-module proof, where it is attributed to Horrocks–Mumford, Topology 12 (1973), Lemma 3.3(ix), printed page 70. The primary representation source and the character row for P are recorded in ../../full-hm-image-symmetry/PROOF.md, Sections 1 and 3. No actual source operation or matrix is used here.

The group N is perfect by the proof in ../rank-nine-kernel-splitting/PROOF.md. Thus all its representation determinants are trivial, as are all one-dimensional characters of G. The modules P and Q are self-dual via their determinant-one alternating forms. The modules T_P and T_Q are irreducible: the Schur-lemma argument in that same proof applies to each two-dimensional irreducible. They are inequivalent, as also follows directly from the character comparison below.

## 2. The Galois permutation has no unidentified twist

Choose an automorphism sigma of the algebraic numbers whose restriction sends zeta to zeta^2. Representations of this finite group can be realized over algebraic numbers, so sigma acts on their characters and tensor identities.

For each nontrivial central character of H, there is a unique irreducible five-dimensional H-module, by the finite Heisenberg representation theorem used in the existing isotypic arguments. Consequently sigma V and A have isomorphic restrictions to H, as do sigma A and V*. These isomorphisms extend to N without an unidentified character twist, for the following precise reason. If two N-representations restrict to the same irreducible H-representation, identify those restrictions. For every n in N the two representing operators then differ by a scalar, by Schur's lemma applied to their conjugation action on H. Those scalars form a character of N trivial on H, hence a character of G. G is perfect, so that character is trivial. This proves

    sigma V=A,    sigma A=V*,    sigma V*=A*,    sigma A*=V.   (2)

For P and Q there is a separate, direct character check; the preceding argument is not being used to identify arbitrary representations trivial on H. In the class order recorded in ../../full-hm-image-symmetry/PROOF.md, the character of P is

    (2,-2,0,-1,1, eta,eta',-eta,-eta'),

where eta=zeta+zeta^(-1) and eta'=zeta^2+zeta^(-2). The two numbers are distinct roots of x^2+x-1. The character of Q is the Galois-conjugate two-dimensional row, interchanging eta and eta'. Thus sigma P=Q and sigma Q=P. This conclusion depends only on the restriction of sigma to Q(zeta), not on its extension to the algebraic numbers. It also gives sigma T_P=T_Q and sigma T_Q=T_P. In particular, the characters of T_P and T_Q differ: at a class where P has trace eta and Q has trace eta', their symmetric-square traces are -eta and -eta'.

Applying sigma to (1) therefore gives the exact identities

    Lambda^2 A=V* tensor Q,
    Sym^2 A=V* tensor T_P,
    A tensor V*=V tensor (T_Q direct-sum P).                 (3)

Exterior duality and det A=1 also give

    Lambda^3 A=(Lambda^2 A)*=V tensor Q.                     (4)

## 3. Two small multiplicity spaces

Every representation in the following calculation has H-central weight zeta, so it is V tensored with its G-module multiplicity space. Define M_3 and M_21 by

    Sym^3 A=V tensor M_3,
    Schur_(2,1) A=V tensor M_21.

The standard decomposition A tensor Lambda^2 A=Schur_(2,1) A direct-sum Lambda^3 A, together with (3), (4), and the determinant-one two-dimensional Clebsch–Gordan identity, gives

    M_21=Sym^3 Q direct-sum (P tensor Q).                   (5)

Indeed T_Q tensor Q=Sym^3 Q direct-sum Q, and the final Q cancels the multiplicity in Lambda^3 A.

Likewise A tensor Sym^2 A=Sym^3 A direct-sum Schur_(2,1) A gives

    M_3 direct-sum M_21=(T_Q direct-sum P) tensor T_P.       (6)

The right side has no G-invariants. The summand T_Q tensor T_P has none because T_Q and T_P are distinct irreducible self-dual modules. The summand P tensor T_P has negative parity under the central involution of G. Semisimplicity and (6) consequently imply

    M_3^G=0.                                               (7)

## 4. The only additional small character calculation

The G-module F=Sym^4 Q is irreducible of dimension five. This can be checked without any operation computation. For a determinant-one two-dimensional representation of trace t, its fourth symmetric power has trace t^4-3t^2+1. Applying this to the row for Q in Section 2 gives

    (5,5,1,-1,-1,0,0,0,0).

The class sizes in this order are

    (1,1,30,20,20,12,12,12,12).

These are also obtained directly from centralizers in SL2(F5): the trace-zero class has centralizer order four, the two noncentral order-three/six classes have centralizer order six, and the four remaining noncentral unipotent-sign classes have centralizer order ten. The squared character norm is

    (25+25+30+20+20)/120=1,

proving irreducibility.

The module D=P tensor Q has dimension four and has no invariant vector, since P and Q are inequivalent and self-dual. It cannot contain the irreducible five-dimensional F. It cannot contain the irreducible three-dimensional T_Q either: the complementary one-dimensional representation would be trivial because G is perfect, contradicting D^G=0. Therefore

    Hom_G(D,T_Q)=Hom_G(D,F)=0.                              (8)

All representations in (8) are self-dual; alternatively dualize the displayed Hom statements where necessary.

## 5. Exterior Cauchy proves the vanishing

Put S=Sym^2 V=A tensor T_Q. The characteristic-zero exterior Cauchy decomposition is

    Lambda^3 S
      = Sym^3 A tensor Lambda^3 T_Q
        direct-sum Schur_(2,1) A tensor Schur_(2,1) T_Q
        direct-sum Lambda^3 A tensor Sym^3 T_Q.

The determinant Lambda^3 T_Q is trivial. Furthermore

    Schur_(2,1) T_Q=T_Q direct-sum F.

For the latter identity, Lambda^2 T_Q=T_Q and Lambda^3 T_Q=1, while T_Q tensor T_Q=Sym^4 Q direct-sum T_Q direct-sum 1; cancel 1 in the standard Schur decomposition.

Taking the V-isotypic multiplicity and then G-invariants gives three contributions:

1. M_3 contributes zero by (7).
2. M_21 tensor (T_Q direct-sum F) contributes zero. Its Sym^3 Q part has negative central-involution parity, while T_Q and F have positive parity. Its D part contributes zero by (8).
3. Q tensor Sym^3 T_Q contributes zero by negative central-involution parity.

The Heisenberg-isotypic tensor-Hom correspondence therefore proves

    Hom_N(V,Lambda^3 Sym^2 V)=0.                            (9)

## 6. Applying the vanishing to the primitive cubic kernel

Suppose generic rank(Q)=7 and residual kernel Plucker degree e=3. The kernel rank is four. Its primitive Plucker vector kappa is a degree-three polynomial with values in Lambda^4 S and satisfies

    u^2 wedge kappa(u)=0.

The lifting theorem in ../low-degree-kernel-lifting/PROOF.md supplies a degree-one polynomial a with values in Lambda^3 S such that

    kappa(u)=u^2 wedge a(u).

The lift is unique. A difference of two lifts is a degree-one Lambda^3 S-valued polynomial annihilated by wedge with u^2. Applying the same lifting theorem with m=3 and e=1 makes that polynomial zero, because its proposed lift would have negative degree.

The saturated kernel determinant has its N-equivariant structure. Its underlying line bundle is O(-3), and its linearization agrees with the natural one because N has no characters. Thus kappa can be taken N-equivariant. The wedge map is equivariant, and uniqueness then makes a equivariant as well. A degree-one equivariant polynomial a is an element of Hom_N(V,Lambda^3 S), which is zero by (9). This contradicts kappa being nonzero.

The rank-seven table previously allowed (k,d,e)=(8,0,3), (3,5,3), and (3,0,8). The first two are excluded, leaving precisely

    (k,d,e)=(3,0,8).

In particular there is no divisorial rank-drop factor in this remaining rank-seven branch, and det I=O(7-k)=O(4). This is a conditional restriction, not a claim that rank seven occurs or is completely excluded.

## Evidence boundary

Only existing local proof texts, universal finite-group representation identities, the nine-entry abstract character calculation, exterior Cauchy and Clebsch–Gordan identities, and the established bundle-lifting theorem were used. No actual HM source matrix, operation product, selected input, polynomial instance, rank instance, jet, or residue was evaluated. There was no large computation or external write; this local proof file is the deliverable.
