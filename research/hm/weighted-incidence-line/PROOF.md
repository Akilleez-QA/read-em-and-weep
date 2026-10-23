# A forced weighted incidence line and two canonical cubic source directions

Work over C with G=SL2(F5), W the physical negative doublet, W' the other doublet, A=Sym2 W, S=Sym3 W, D=Sym4 W, T6=Sym5 W, V=Sym2 W', and P the even four-dimensional irreducible. All bundles are on the negative parameter line T=P(W*) with standard linearizations. No selected actual HM coefficient, point, parameter, matrix or instance rank is evaluated.

## 1. Immutable interface and theorem

INPUTS.json pins three originals in Akilleez-QA/read-em-and-weep:

- BLOCK: PR1062, commit2a7565f5828447907ad860c861891ec2fdb4f7cb, research/hm/double-mixed-block/PROOF.md. It supplies canonical K of dimension2, with trivial G action, and the actual exact sequences

      0 -> A O(-6) -> R O(-1) --d--> Z -> C -> 0,   (1)
      0 -> K tensor V O(2) -> Z -> H O -> 0,        (2)
      R=2W+2W'+3S+2T6, dim R=32,
      H=1+4A+2V+P+D, dim H=28.

  Here R is the actual source quotient, Z the actual target quotient, and C the original opposite cokernel, not an abstract replacement. Their marked embeddings are retained; (2) is not given a canonical splitting.
- TYPES: PR996, commit54dc2b2b301f8a7e453b3101d5813c643beed71a, research/hm/opposite-second-degree-bound/PROOF.md, Sections5–6. The actual C is a globally generated vector bundle and is necessarily one of the seven types displayed below. The list is exhaustive as a necessary condition, not a realization assertion.
- SEXTIC: PR1017, commit7cd8baebbec29ad21def1f8b30e19c707a87aed5, research/hm/rank-three-opposite-core/PROOF.md, Section2. Its fixed universal sextic sequence, twisted by O(4), is

      0 -> O(-4) --i--> V O(2) --q--> W' O(5) -> 0. (3)

  Only this universal sequence is imported, not the later actual core choices.

Let eta:K tensor V O(2)->C be the actual map induced by (1)–(2). We prove eta is nonzero. Its multiplicity map selects a canonical line K0 in K, with the property eta(K0 tensor V O(2))=0. The preimage of this subbundle under d is a saturated rank-six subbundle L of R O(-1), in a nonzero equivariant extension

    0 -> A O(-6) -> L -> K0 tensor V O(2) -> 0.   (4)

The relevant equivariant Ext space has dimension one, and the embedding forces the exact equivariant splitting L=W' O(-1)+V O(-2)+O(-4). Moreover eta kills the entire canonical K tensor O(-4) from (3). The preimage of this smaller subbundle has a UNIQUE equivariant splitting, selecting an actual canonical K tensor O(-4) inside R O(-1). Its cubic coefficient directions select a two-dimensional subspace of the three S multiplicities in R. These are incidence and source-embedding constraints, not a determination of C's row or of an actual scalar value.

## 2. Two one-dimensional Hom spaces for every necessary row

For a target atom L O(d), the Hom spaces from V O(2) and W' O(5) are, respectively,

    Hom_G(V,L tensor Sym^(d-2)W),
    Hom_G(W',L tensor Sym^(d-5)W),                (5)

with contribution zero when the displayed exponent is negative. All named representations are self-dual. The fixed character calculation gives the following complete table. In each row the listed target atom is the unique one contributing, and each Hom dimension is1:

    row  C type                                contributing atom
      9  O(2)+O(12)+V O(4)                    O(12)
     10  O(2)+O(18)+A O(2)                    O(18)
     14  O(2)+W' O(5)+W' O(7)                 W' O(5)
     15  O(2)+P O(6)                          P O(6)
     17  O(14)+W O(1)+W' O(5)                 W' O(5)
     18  O(18)+W O(1)+W O(3)                  O(18)
     20  W O(1)+V O(8)                        V O(8).

Thus, for the actual C,

    dim Hom_G(V O(2),C)=dim Hom_G(W' O(5),C)=1. (6)

These are cohomological Hom spaces of bundles, not assertions that their nonzero morphisms are injective or surjective. Since q in (3) is a sheaf surjection, precomposition defines an injective map

    q*:Hom_G(W' O(5),C)->Hom_G(V O(2),C).

By (6) it is an isomorphism. Every equivariant map V O(2)->C therefore kills i(O(-4)); this conclusion does not require identifying the other parts of its sheaf kernel or image.

## 3. Nonvanishing and the marked incidence line

The multiplicity form of eta is the actual linear map

    ell:K -> Hom_G(V O(2),C).                    (7)

The target is one-dimensional by (6). We prove ell is nonzero by the original kernel geometry.

Set J=ker(Z->C). Since both Z and C are locally free and Z->C is onto, J is locally free and R O(-1)->J is onto with kernel A O(-6). If eta were zero, K tensor V O(2) would be a subbundle of J. Indeed it is a subbundle of Z by (2), and J/(K tensor V O(2)) is the kernel of the induced surjection H O->C, so is locally free. Its preimage L_all in R O(-1) would therefore be a vector bundle extension

    0 -> A O(-6) -> L_all -> K tensor V O(2) -> 0. (8)

The equivariant extension space for one V copy is

    Ext1_G(V O(2),A O(-6))
      = (V* tensor A tensor H1(O(-8)))^G
      = Hom_G(V,A tensor Sym6 W) = C.            (9)

Here Serre duality uses det W=1, Sym6 W=V+P, and A tensor(V+P)=V+2P+2D. Consequently the class of (8) is a linear map from the two-dimensional K to the one-dimensional space (9). It has a nonzero kernel direction. Pulling (8) back to that direction splits equivariantly, giving an injection V O(2)->L_all->R O(-1). This is impossible even nonequivariantly, because H0(O(-3))=0. Thus eta and ell are nonzero.

Define K0=ker ell. It is a canonical line, independent of any scalar generator of the Hom space in (6). Its subbundle K0 tensor V O(2) is killed by eta, so its preimage L gives (4). The same kernel-of-a-surjection argument shows L is a saturated subbundle of R O(-1). Its extension class cannot vanish, or a splitting would again inject V O(2) into R O(-1). Its rank is6 and its degree is -18+6=-12. After identifying the one-dimensional factor K0, it is a nonzero member of the one-dimensional Ext space (9); uniqueness is only up to the relevant scalar identifications, not a canonically normalized injection.

We do not identify ker eta as K0 tensor V O(2): a nonzero generator V O(2)->C can itself have a sheaf kernel. Only its multiplicity kernel is K0. In particular none of the proof assumes that generator is injective.

## 4. Universal factorization forces two cubic source directions

Section2 makes eta kill the whole subbundle K tensor O(-4) embedded in K tensor V O(2) by i. Denote its preimage under d by Ppre. As above it is a saturated vector subbundle of R O(-1), with exact sequence

    0 -> A O(-6) -> Ppre -> K tensor O(-4) -> 0.  (10)

Here local freeness can be seen directly: Z/(K tensor O(-4)) is locally free by (2)–(3), it still surjects onto C, and its kernel is J/(K tensor O(-4)).

Both relevant equivariant groups vanish:

    Hom_G(O(-4),A O(-6))=0,
    Ext1_G(O(-4),A O(-6))
       =(A tensor H1(O(-2)))^G=A^G=0.           (11)

The first follows from H0(O(-2))=0; the second uses the trivial representation H1(O(-2)) and A^G=0. Thus (10) splits equivariantly and its splitting is UNIQUE. In particular the actual maps, not chosen complements, select a canonical lift

    j:K tensor O(-4) -> R O(-1).                 (12)

Its image is saturated: R O(-1)/Ppre is locally free, and quotienting Ppre by this split summand leaves A O(-6). Scalar choices identifying the line in (3) with the named O(-4) do not change the selected image.

The space of cubic coefficient maps is

    Hom_G(O(-4),R O(-1))=(R tensor Sym3 W)^G
       =Hom_G(S,R),                              (13)

a three-dimensional space because R has exactly three S copies. Under (13), j is a linear map K->Hom_G(S,R). It is injective: a nonzero multiplicity direction in its kernel would make the corresponding O(-4) summand map identically to zero, contradicting the sheaf injection (12). Hence it selects two of the three S multiplicity directions canonically, without choosing a complementary direction.

Equivalently, let R_S,selected be the evaluation image of this two-dimensional subspace tensored with S. Then R_S,selected is an actual 2S subspace of R, and (12) factors through R_S,selected O(-1) as two copies of the universal cubic Veronese inclusion O(-4)->S O(-1). This universal inclusion is fiberwise injective. The quotient from the original U to R removed only T6 isotypic directions in BLOCK, so the S isotypic spaces are canonically identified: the selected 2S also specifies a subspace of the original full U=H1(B(2))_-.

## 5. The nonsplit preimage has a determined equivariant splitting

The rank-six L in (4) has all ordinary splitting degrees at most -1: an atom O(d) with d>=0 cannot inject into R O(-1). We use equivariant Birkhoff–Grothendieck splitting. It follows from the usual splitting and the canonical degree filtration: each ordinarily split filtration extension can be split equivariantly by averaging a splitting over the finite group. Thus L is a sum of irreducible coefficient representations tensored with line bundles.

Its central action on each fiber is even, since this is true of A O(-6) and K0 tensor V O(2). In an atom Rho O(-d), the coefficient Rho consequently has central parity (-1)^d. Tensoring (4) by O(1) and O(2), then using Euler characters, gives

    chi_G(L(1)) = V tensor S - A tensor S = W'-W,
    chi_G(L(2)) = V tensor D - A tensor A = V+P-1. (14)

All multiplicities in H1 are nonnegative. The first identity therefore forces at least one W' in H0(L(1)), even if further H0/H1 cancellation is present. Because all L degrees are at most -1, H0(L(1)) receives contributions ONLY from degree -1 atoms, with their coefficient representations unchanged. Thus an equivariant direct summand W' O(-1) exists. Remove one such summand and call the remaining bundle F. It has rank4, degree -10, all degrees at most -1, and

    chi_G(F(2)) = V-1,                           (15)

since H0(W' O(1))=W' tensor W=P and its H1 vanishes.

Again (15) forces a V in H0(F(2)), regardless of any cancellation. Degree at most -3 contributes no H0 here. A degree -1 atom has an odd irreducible coefficient of dimension at most rank(F)=4. The complete list is W,W',S, and their products with W are respectively 1+A, P, A+D; none contains V. Therefore a degree -1 atom cannot supply the required V. A degree -2 atom contributes its coefficient representation unchanged, so F must contain a direct summand V O(-2).

These two forced summands consume rank5. The remaining rank-one summand has degree -12-(-2)-(-6)=-4. Its coefficient character is trivial because G is perfect. This proves

    L ≅ W' O(-1) + V O(-2) + O(-4).              (16)

This argument permits arbitrary H0/H1 cancellation until the rank bound exhausts the remaining possibilities; it does not infer a splitting merely from Euler characters.

The splitting in (16) is intrinsic as an equivariant decomposition by its three distinct degrees. All possible maps from lower to higher degree vanish equivariantly: the tests are V against W' tensor W=P, W' against Sym3 W=S, and V against Sym2 W=A. Maps from higher to lower degree vanish already by negative line degree. Hence the degree filtration admits a unique equivariant splitting; the named irreducible identifications still carry scalar choices.

The W' O(-1) summand embeds into R O(-1) by a constant map and selects a canonical W' multiplicity line among its two copies. The V O(-2) summand can reach only the two T6 copies: (3) of BLOCK gives W tensor W=1+A, W tensor W'=P, W tensor S=A+D, W tensor T6=V+P+D. Thus its nonzero actual map selects a canonical T6 multiplicity line, through the tensor Euler inclusion V O(-2)->T6 O(-1). It is nonzero since L embeds in the source.

Finally Hom_G(O(-4),L) is one-dimensional by the same cross-Hom tests. The O(-4) summand in (16) is therefore precisely the K0 restriction of the unique doubled cubic lift from Section4. Its S coefficient direction lies in the canonical two-dimensional S multiplicity subspace already selected there. These incidence relations do not select the position of K0 within K or a complementary S direction.

## 6. Scope and reproducibility

The two new incidences are complementary: the nonzero weighted-to-C map selects K0, while universal sextic factorization supplies the unique lifted cubic directions for all of K. The actual position of K0 relative to BLOCK's previously marked line is not determined. Nor is a particular remaining C type selected. The argument uses the seven types only as exhaustive necessary possibilities for the actual C; it asserts no abstract type is realized.

All kernel, preimage and lifting maps above come from the actual full opposite presentation. No comparison is made with another separately embedded P/D or S subspace, including conditional im-h-generated modules or the marked degree-three negative string. Identical representation names do not identify their actual embeddings.

verify.py authenticates the three immutable originals, checks the two Hom dimensions atom by atom for the seven fixed types, verifies the Ext character and cubic multiplicity, and checks rank/degree balances. It does not evaluate an actual HM/source tensor or a selected instance. REPRODUCE.md reconstructs the omitted audit inputs; REVIEW.md binds an independent whole-proof review to final bytes.
