# The terminal negative string and its forced Euler subpencil alternative

Work over C with G=SL2(F5), negative coordinates W, positive fixed plane R=P(V), A=Sym2 W, S=Sym3 W, D=Sym4 W and T6=Sym5 W. The parameter line is T=P(W*); the determinant pairing fixes W≅W*. All maps are actual cohomological multiplications unless explicitly called universal. No selected actual coefficient, parameter or fiber is evaluated.

## 1. Immutable inputs and result

INPUTS.json authenticates five originals in Akilleez-QA/read-em-and-weep:

- STRING: PR1050 at ec18a0fd62c4a9495adf6aad9564d379afc42b62, research/hm/canonical-negative-string/PROOF.md. It constructs the canonical actual compatible negative-coordinate string U1=W, U2=A, U3=S, U4=D in H1(B(d)), d=1,...,4. It proves H0(B(5))=1+P+D, including its positive parity, and retains the actual everywhere-onto pencil

      0 -> E -> M3 O(-1) --m--> M4 O -> 0,
      M3=H1(B(3))_-=3W'+3S+6T6,
      M4=H1(B(4))_+=2V+4P+3D.                    (1)

  Here E is exactly that rank17 degree-54 kernel, not the opposite bundle C or global Jg. STRING also pins the normalized monad K-class and proves that the simultaneous map M3->W tensor M4 is injective.
- REGULARITY: PR167 at 063da90fc4543304e87e701cdefcc08225412f17, research/conductor-normalization/sharper-hm-regularity/SHARPEST-BOUND.md: H2(B(t))=0 for t>=2.
- ENDPOINT: PR450 at 54d1eafe617e042edc452cb66edb8e4f7c78d2bf, research/hm/endpoint-structural-vanishing/PROOF.md: H1(B(6))=0, structurally proved.
- TAIL: PR476 at 3aa461bc3581fb72fbf923fbe869ddee023b435a, research/hm/five-generator-module/PROOF.md: H3(B(t))=0 for t>=-1, with the authenticated subsequent cohomology support.
- PLANE: PR967 at 39c5f4fbc012f4ec57ffc56d5de18cedb3571d60, research/hm/fourth-normal-obstruction/PROOF.md, Section1: the actual restricted F_R is stable, with its equivariant plane Steiner presentation. Only its stability is used here.

There is an actual exact coefficient sequence

    0 -> M3 --delta--> W tensor M4 --mu--> M5 -> 0,
    M5=H1(B(5))_-=W'+3T6.                         (2)

The next canonical string arrow is an actual map

    f5:T6 -> M5.                                  (3)

Exactly one of the following holds, without selecting which:

(a) f5 is nonzero. It embeds a canonical terminal T6 in degree5; every coordinate kills it in degree6.

(b) f5 is zero. Then the actual source M3 contains a canonical subrepresentation U*=S+T6, containing U3, which identifies by delta with W tensor U4. Its parameter pencil is the universal Euler subpencil

    0 -> D O(-2) -> (W tensor D) O(-1) -> D O -> 0. (4)

Consequently E contains a canonical D O(-2) subbundle, and quotienting the actual pencil gives

    0 -> E/D O(-2) -> (3W'+2S+5T6) O(-1)
      -> (2V+4P+2D) O -> 0.                       (5)

Its right arrow is onto on every fiber; its kernel has rank12 degree-44. The D O(-2) summand of E splits equivariantly, but no complementary summand is canonical or selected.

This sharpens the possible termination of the canonical string to a forced geometric change in the actual source pencil. It is not an assertion that T6's mere presence in M5 forces (a).

## 2. Actual degree-five cohomology and the endpoint

For completeness compute the needed character, not just its dimension. Use STRING's normalized monad notation H=V+W, Nmon=A+W', L2=Lambda2 H and

    c_-1=-Nmon, c_0=W' L2-Nmon, c_1=-W'H, c_2=W'.

As B(5)=Sym2 F(6), its equivariant Euler character is

    chi_G(B(5)) = 1/2 sum_(i,j=-1)^2 c_i c_j Sym^(i+j+6)H
                 +1/2 sum_(i=-1)^2 psi2(c_i) Sym^(2i+6)H
               = P-A-V-W'-3T6.                   (6)

The last equality is checked on the fixed nine abstract conjugacy classes; the exponents range only from4 to10. No differential is evaluated. REGULARITY and TAIL kill H2 and H3. H4(B(5))=H0(B(-10))*=0 by stability of F and decreasing-slope Hom vanishing. With STRING's actual H0(B(5))=1+P+D this gives

    H1(B(5))=1+A+V+D+W'+3T6.                      (7)

Thus T6 is indeed present, three times. A proposed proof that it is absent would be false. ENDPOINT kills the whole H1(B(6)), not just its negative-coordinate descendants. Therefore any nonzero image in (3) is terminal under every coordinate.

## 3. Exactness of the complete two-coordinate continuation

The central involution acts identically on R and by a scalar on F_R: its induced bundle automorphism is scalar since F_R is stable and hence simple. Conjugation on End0(F_R)=B_R is therefore trivial. Also O_R(1) has positive central character because R=P(V). Every cohomology group of B_R(t) is consequently positive. In particular

    H0(B_R(5))_-=H1(B_R(5))_-=0.                  (8)

The two negative coordinates form a regular sequence cutting out R. Their sheaf Koszul sequence is

    0 -> Lambda2 W tensor B(3) -> W tensor B(4)
      -> I_R B(5) -> 0.                           (9)

Use Lambda2 W=1. STRING gives H0(B(4))=0 and H0(B(5))_-=0, so H0(I_R B(5))_-=0. REGULARITY gives H2(B(3))=0. The negative part of the long exact sequence of (9) is thus

    0 -> M3 -> W tensor M4 -> H1(I_R B(5))_- -> 0.

The restriction sequence 0 I_R B(5)->B(5)->B_R(5)->0 and (8) identify its last space with M5. This proves (2) with its actual multiplication maps. In a universal coordinate notation x,y for W, delta(s)=x tensor (ys)-y tensor (xs), up to the fixed determinant convention, and mu is multiplication. These are formal identities for a regular two-coordinate sequence, not selected HM evaluations. The character check W M4-M3=W'+3T6 agrees with (7), but is not the proof of exactness.

## 4. The zero branch forces an Euler subpencil

STRING constructs f1,...,f4 compatible with symmetric multiplication. Polynomial commutativity extends this construction to f5: the determinant relation already killed in degree2 has all its multiples killed. Restrict mu in (2) to W tensor U4. Since U4 is the selected image of Sym4 W, this restriction is

    W tensor Sym4 W -> Sym5 W --f5--> M5.          (10)

The first map is the universal symmetric multiplication, whose kernel is Sym3 W=S. The injection delta maps U3 onto exactly this S kernel: the formula after (9) and the compatibility of STRING identify it, and both spaces have dimension4.

Sym5 W=T6 is irreducible, so any nonzero f5 is injective and gives case(a). Its image is independent of rescaling the coherent initial identification W->U1.

Suppose instead f5=0. Equation (10) says W tensor U4 lies in ker mu=im delta. Since delta is injective, its inverse image

    U* := delta^(-1)(W tensor U4) subset M3        (11)

is canonical and maps isomorphically onto W tensor U4=S+T6. The S-isotypic part is the already selected U3. The complementary T6-isotypic part of U* is unique, although M3 itself contains six T6 copies. It is selected by the actual kernel equation, not by choosing a multiplicity direction.

Under (11), the actual pencil m restricted to U* O(-1) is determinant contraction of the W factor with the parameter line. Indeed delta(s)=x tensor ys-y tensor xs, so recovering any multiplication ell*s from delta(s) is that universal contraction. Consequently the restricted pencil is the tensor product of U4 with the Euler sequence

    0 -> O(-2) -> W O(-1) -> O -> 0,

which proves (4). In particular it is onto U4 O everywhere. Quotient the subpencil (4) inside (1). The snake lemma gives (5), with the actual inherited map on the coefficient quotients. The source character is M3-(S+T6)=3W'+2S+5T6, and the target is M4-D=2V+4P+2D. Its source rank is44, target rank32 and kernel degree-44. Both the original and the subpencil are fiberwise onto, so the quotient is also fiberwise onto and its kernel is a vector bundle. Thus D O(-2) is a subbundle of E, not merely a sheaf injection with possible torsion quotient.

Conversely, the existence of a subrepresentation U* as in (11) mapping by delta onto W tensor U4 forces (10) to vanish, hence forces f5=0. We do not assert that the existence of some unmarked abstract D O(-2) summand in E alone proves this branch: its compatibility with the selected U4 is essential.

## 5. Splitting precision and the remaining geometric dependency

Twist (1) by O(1). Its map on global sections M3->W tensor M4 is delta after the invertible determinant identification. It is injective by (2), so H0(E(1))=0. Birkhoff--Grothendieck therefore makes every ordinary slope of E at most-2. An equivariant version of the splitting exists: take the canonical maximal-slope filtration and split its extensions using H1 of nonnegative line-bundle degrees, then average splittings over G.

In such a splitting, every map from D O(-2) to a summand of smaller degree is zero. Hence the selected subbundle in case(b) lies in the maximal slope -2 part, which is its coefficient representation tensored with O(-2). Semisimplicity splits the selected D coefficient subspace there. This proves the asserted equivariant direct-summand statement, without a canonical complementary bundle.

The next Koszul test does NOT automatically select a branch. At twist6 it gives

    H0(I_R B(6))_+ ≅ ker[M4 -> W tensor M5],        (12)

because W tensor H0(B(5)) is negative and H0(B(4))=0. Thus vanishing of f5 is equivalent to the selected U4 lying in this actual joint-negative kernel. The left side is the actual kernel of restriction H0(B(6))_+->H0(B_R(6)). The imported character calculations and symmetric-square exhaustion at twist5 do not prove this restriction injective. Matching character differences cannot replace that missing map-level statement.

In particular (12) has source M4=2V+4P+3D and target W M5=3V+4P+3D. The formal difference V does not imply the kernel is zero. We retain (3) as an actual unselected three-dimensional multiplicity vector. No choice among current source/catalogue alternatives follows just from this theorem.

## 6. Contribution and boundary

The new result identifies degree5 negative multiplication as an exact actual Koszul cokernel and ties termination of the selected string to a canonical Euler subpencil and a smaller ordinary source presentation. The zero branch is geometrically restrictive; the nonzero branch selects a terminal T6. Neither branch is inferred from character availability.

No actual HM/source coefficient, point, parameter, derivative, jet, matrix, instance rank or large scan was used. No catalogue cut, selected opposite type, vertex scalar or smoothing conclusion is claimed. The arithmetic checker is bounded and does not substitute for independent mathematical review of the exact sequences and inherited maps.
