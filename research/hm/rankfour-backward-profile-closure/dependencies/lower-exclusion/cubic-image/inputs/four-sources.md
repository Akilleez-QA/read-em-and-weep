# The primary terminal space lies in the canonical degree-minus-three slope piece

Work over C with the actual normalized HM module and fixed physical G=SL2(F5) marking. Write V and W for the positive three-space and negative two-space of coordinates, A=Sym2 W, P for the positive four-space, W' for the other negative doublet, and T6=Sym5 W. Let E be the actual rank17, degree−54 kernel on the fixed negative parameter line T=P(W*) in

    0 -> E -> M3 O(-1) -> M4 O -> 0,
    M4=H1(B(4))_+, M5=H1(B(5))_-.

## 1. Immutable assumptions and result

The complete originals used are:

- PR477 at ff87076794e97238150485b12183c3cd0f4711e4, research/hm/adjoint-primary-extension/PROOF.md: the actual injective graded polynomial-module map L_j=U tensor H1(F(j-3)) into K_j=H1(B(j-1)).
- PR486 at 0de9b4b71cbbf3c4492871d9835952a0dcb41e12, research/hm/level-section-resolution/PROOF.md: Soc(K)=K6.
- PR1120 at 62587a0adde566cac718ee13c28ee13c239389e5, research/hm/scalar-cyclic-module/PROOF.md: U=P, H1(F(2))=1+A+T6, H1(F(3))=W, with their actual physical parity, and P tensor W=W'+T6.
- PR1122 at 65c13bb9a3748a19eb8466f748bd29a5a849ecb5, research/hm/primary-terminal-source2-exclusion/PROOF.md: the independently reviewed preceding slice establishes the actual primary terminal evaluation pencil and its obstruction against the genuine source2 first block. Section2 below reconstructs its primary lemma from the same original maps, while the new argument replaces a source-specific projector by the canonical slope quotient.
- PR1056 at 875e86e2eec36a050e9a626735199681762e43ec, research/hm/restriction-socle-kernel/PROOF.md: the actual E above, H0(E(1))=0, natural identifications M4=H1(E), M5=H1(E(1)), and actual negative multiplication identified with parameter multiplication after one fixed determinant rotation. These are unconditional on the necessary source-pair ledger. Its Section5 describes E10,E13,E14 only conditionally.
- ACTUAL at db51525015bb7c5e825833d550d08dedf6f6ea96, research/hm/order-four-quadratic-load/ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md: an equivariant Birkhoff splitting E=direct sum R_j O(-j), j>=2, the genuine coefficient representations R_j, and the complete 28-type equations recalled below. This is necessary actual bundle data, not occurrence of every formal type.

Let E_{>=-3} be the canonical slope-filtration subbundle whose Birkhoff summands have degrees−2 and−3. Its quotient E_{<-3} has every summand of degree at most−4. Put R3=H0((E_{>=-3}/E_{-2})(3)); this is the canonical coefficient representation of the degree−3 slope quotient.

The actual primary terminal subspace U tensor H1(F(3))=P tensor W inside M5 lies in the canonical subspace

    H1(E_{>=-3}(1)) subset H1(E(1))=M5.                (1)

Moreover H1(E_{>=-3}(1)) is canonically isomorphic to R3, using the fixed determinant trivialization. Hence

    W'+T6 embeds equivariantly in R3.                 (2)

This is not deduced from an arbitrary injection 8O(-2)->E(1): such an injection alone would not imply (2), because maps to O(-1) exist. The proof uses BOTH coefficient arrows of the actual terminal pencil.

Intersecting (2) with the authenticated 28-type equations leaves exactly four formal E types:

    D O(-2) + (W'+T6) O(-3) + V O(-4) + O(-8),
    P O(-2) + (W'+T6) O(-3) + V O(-4) + W' O(-5),
    V O(-2) + (W'+T6) O(-3) + 2V O(-4),
    (W'+2T6) O(-3) + V O(-4).                        (3)

No type in (3) is asserted realized. In particular E10,E13,E14 of PR1056 Section5 are incompatible with this actual primary terminal structure. These are exclusions of the specified necessary types, not a theorem that every possible source or HM bundle is impossible. Any conclusion about the rank-three source frontier additionally requires its separate geometric coverage/transfer theorems; that audit is not silently supplied by a ledger count.

## 2. Recover the actual primary terminal evaluation pencil

Set Y=H1(F(2))_+=1+A and Z=H1(F(3))=W. Positive-coordinate multiplication V tensor Y->Z is zero by physical parity. The actual curry

    c:Y -> Hom(W,Z),     c(y)(w)=w y

is injective. Indeed an element of its kernel is killed by W and by V; for nonzero u in U its image u tensor y in K5 under PR477 is then a degree5 socle element. PR486 excludes such a nonzero element, and PR477's injectivity forces y=0. Since dim Y=dim Hom(W,Z)=4, c is an actual isomorphism.

Use the original parameter line and the same fixed determinant identification for ALL pencils. Equivalently pull all diagrams by the same fixed isomorphism T=P(W*) to P(W), with tautological line O(-1) in W O. Evaluation of all Hom(W,Z) maps on this line is onto everywhere and has kernel Z O(-2). Tensor by U to get the actual coefficient-space subpencil

    0 -> (U tensor Z) O(-2)
      -> (U tensor Y) O(-1) -> (U tensor Z) O -> 0.     (4)

Its coefficient inclusions into M4 and M5 are injective by PR477 and intertwine the same negative variables. Source dimension is16, target dimension8. No scalar of an actual arrow was assigned or evaluated.

## 3. Actual terminal reconstruction is functorial for bundle quotients

For any bundle F on T with H0(F)=H0(F(1))=0, pushing the diagonal resolution tensored with F(1) gives the natural exact terminal evaluation sequence

    0 -> F(1) -> H1(F) O(-1) -> H1(F(1)) O -> 0.      (5)

The fixed determinant convention matters. If the original E pencil is u m_x+v m_y, PR1056 identifies cohomology multiplication by u with m_y and by v with−m_x. The diagonal equation produces v H1(mult_u)−u H1(mult_v), equal to v m_y+u m_x. Thus (5) for E is the ACTUAL original terminal pencil, not an unrelated isomorphic pencil with an independently rotated parameter. The construction is natural under every morphism of bundles, including the canonical slope quotient E->E_{<-3}.

H0(E(1))=0 implies all slopes of E are at most−2, and therefore every slope of E_{<-3} is at most−4. Both vanishings needed for (5) hold for this quotient. Consequently the quotient induces a coefficient-space morphism from the actual terminal E pencil to (5) for E_{<-3}. Composing with (4) retains the actual primary embeddings and both terminal coefficient maps.

## 4. Hom vanishing kills the lower-slope quotient, not merely its kernel

Let q1,q2 be this composite coefficient-space morphism from (4) to the quotient's (5). It induces a map of kernel bundles

    (U tensor Z) O(-2) -> E_{<-3}(1).

Every summand of the target has degree at most−3, so this map is zero by H0(O(n))=0 for n<0. Therefore q1:(U tensor Y) O(-1)->H1(E_{<-3}) O(-1) annihilates the entire kernel in (4), and factors through its quotient (U tensor Z) O. This factor is zero because Hom(O,O(-1))=0. Thus q1=0; commutation and the surjectivity in (4) give q2=0.

Now use 0->E_{>=-3}(1)->E(1)->E_{<-3}(1)->0. Its left cohomology map on H1 is injective because H0(E_{<-3}(1))=0, and H2 vanishes on the parameter line. Hence

    0 -> H1(E_{>=-3}(1)) -> H1(E(1))
      -> H1(E_{<-3}(1)) -> 0.                      (6)

The vanishing q2 puts the whole ACTUAL primary terminal image into the kernel in (6). This proves (1) as an embedded-subspace statement, not just a character relation.

The exact slope sequence

    0 -> E_{-2}(1) -> E_{>=-3}(1) -> R3 O(-2) -> 0

has acyclic left term R2 O(-1). Thus H1(E_{>=-3}(1))=R3 tensor H1(O(-2))=R3 canonically in the fixed determinant convention. The primary inclusion is equivariant and injective, and its domain has character W'+T6, proving (2). Semisimplicity allows its character subtraction from R3 only after this actual injection is proved.

## 5. Solve the existing universal splitting equations

ACTUAL gives nonnegative integers a,b,c,d,e,f,g,h, with

    a+d+g+h=1,
    b+c+d+e+f+2g+h=3,
    c+g+h>=1,                                      (7)

and blocks

    R3=a W'+b T6;
    R4=c V+d P; R5=e W'; R8=f 1; R9=g W; R10=h 1;
    R2=(c+g+h-1)V+(d+e+g+h)P+(f+g)D.               (8)

Equation (2) forces a>=1 and b>=1. The first equation in (7) then gives a=1 and d=g=h=0. The others reduce to

    b+c+e+f=3,       b>=1, c>=1, e,f>=0.

There are exactly four possibilities: (b,c,e,f)=(1,1,0,1), (1,1,1,0), (1,2,0,0), (2,1,0,0). Substitution in (8) gives (3). This is a bounded universal representation classification, not a scan of actual source instances.

PR1056's E10 and E14 have R3=0, while its E13 has R3=T6. None contains W'+T6; in particular the W' channel is already enough to distinguish E13. This argument needs no actual pure-V compatible radical, R=0, residual-large hypothesis or positive-coordinate projector extension. It uses the actual terminal reconstruction and canonical slope quotient instead.

## 6. Exact scope and open dependency

The new unconditional-on-source-ledger result is (1) and (2), relative to the pinned actual HM inputs. The four-type reduction (3) additionally uses ACTUAL's 28-type classification. All ordinary bundle projections in the argument are transported functorially to the ACTUAL negative terminal pencil; they are not assumed horizontal for an ambient Gauss connection, nor used as positive-coordinate or Q projectors.

The inherited four-pair ledger records only E10,E13,E14 on its residual rank-three frontier. Their incompatibility is therefore a new obstruction to those listed pairs. A global rank-three exclusion, and still more a repair of the original theorem, requires independent authentication and verification of the ledger's geometric completeness and actual-source transfer hypotheses. This proof neither promotes the JSON frontier to a coverage theorem nor concludes HM nonexistence.
