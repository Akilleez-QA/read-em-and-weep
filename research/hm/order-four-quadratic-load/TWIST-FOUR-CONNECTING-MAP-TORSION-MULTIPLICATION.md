# The actual twist-four connecting map is torsion-divisor multiplication followed by trace

## Scope

Keep the common-open geometry and exact presentations pinned at a0540d89b6a8df1077251d320a0821c3a432706a and ddb6cd3e6f4bb0e24e1e5009ca95cb7e568f2c45, with coordination https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6317363735 . Write pi:W->S(5), J0 for the unmodified graph curve, p:J0->Y for its degree-four finite-flat map, and f for the modular projection. Put D=sum of the fifty torsion lifts on W. The established exact identities are

    O_W(D)=pi*O(5I),
    J0=h+pi*H,
    L4=pi*(10I+12F)-h,
    M=L4-J0,
    A4=O_Y(12F-H).

No rank of an instance matrix is computed. The goal is to identify the actual extension map, not replace it by a generic pairing.

## 1. A canonical multiplication diagram

Define B=O_W(12F-h), where F also denotes its pullback. Then

    L4=B(2D),    B|J0=p*A4.

The second equality uses the actual target hyperplane identity h|J0=p*H_Y and the common modular parameter. The canonical section s_D gives the commutative diagram of divisor sequences

    0 -> B(-J0) -> B -> p*A4 -> 0
         |s_D²     |s_D²     |s_D²
    0 -> M       -> L4 -> L4|J0 -> 0.

In particular, the inclusion of common values used to construct Kplus is precisely the bottom-right composition of the unit inclusion A4->p_*p*A4 and multiplication by s_D². This is not an arbitrary inclusion of a rank-ten bundle.

Consequently the actual beta0:H0(Y,A4)->H1(W,M) factors as

    H0(Y,A4) -> H0(J0,p*A4)
              -> H1(W,B(-J0))
              -- multiplication by s_D² --> H1(W,M).

Here H1(W,M)=H1(P1,R0) has dimension35. The first arrow is the pullback/unit map. The middle arrow is the boundary of the top divisor sequence.

The composite of the first two arrows is injective. Indeed B has negative degree -30 on a general smooth modular fiber of W, so H0(W,B)=0: a nonzero section would restrict nontrivially to the general fiber, contradicting that negative degree. Pullback along the finite-flat degree-four map is injective, since trace divided by four splits the unit.

Thus a vector in the forty-five-dimensional common-value space passes beta0 precisely when its canonical nonzero boundary class is killed by multiplication by the square of the actual torsion divisor. This is an exact geometric description of the unresolved radical.

## 2. The dual map is restriction, multiplication, and finite trace

Serre duality on W and finite duality for p identify the dual map beta0* with

    H1(W,omega_W tensor M^{-1})
      -> H1(J0,omega_{J0} tensor (L4|J0)^{-1})
      -- multiplication by s_D² --> H1(J0,omega_{J0} tensor p*A4^{-1})
      -- trace --> H1(Y,omega_Y tensor A4^{-1}).

The first arrow is restriction; the equality of its displayed target follows from omega_{J0}=(omega_W+J0)|J0 and M=L4-J0. The last arrow is the dualizing trace of the finite-flat Gorenstein curve map, not an identification of its trace-free bundle with End0(V). This formula is valid even when J0 is singular. Its source has dimension35 and its target has dimension45.

The appearance of trace alone does not imply symmetry: the two spaces have different dimensions, and the map also contains restriction and the specified torsion-square factor. No alternating or symmetric self-pairing has been established.

## 3. Relative placement explains why acyclicity alone does not settle the map

Let Fbundle=pi_*M and G=pi_*B(-J0). Since pi is finite flat,

    G=Fbundle tensor O(-10I).

On a general smooth elliptic modular fiber, Fbundle has rank2 and degree15, whereas G has rank2 and degree -85. The established fiberwise dual-injection argument gives R1 f_*Fbundle=0 and f_*Fbundle=R0. For G, H0 on the general fiber vanishes because B(-J0) has degree -70 on the integral genus16 double-cover curve; hence f_*G=0. The induced derived map therefore connects different cohomological degrees. It is an extension-class phenomenon, not a map between the ordinary direct-image bundles. Vanishing of R f_*End0(V) identifies R0 but does not force this extension class or its action on the common-value boundary classes to vanish.

No claim of beta0 surjectivity, a zero beta0, a numerical radical bound beyond the already known dimension10–45, or the final proof repair follows from this factorization.

## 4. A concrete four-hundred-fifty-dimensional torsion neighborhood

There are fifty, not twenty-five, disjoint curves D_i in D: the pullback of each of the twenty-five torsion sections splits into two copies of P1. They satisfy D_i²=-5, h.D_i=0, F.D_i=1, and pi*I.D_i=-1. Therefore

    M|D_i=O_P1(1),    M(-D)|D_i=O_P1(6).

The doubled-divisor sequence

    0 -> M(-D)|D -> M|2D -> M|D -> 0

gives h0(M|2D)=50*(7+2)=450 and H1(M|2D)=0. Since H0(W,M)=H0(R0)=0, the multiplication sequence gives the exact sequence

    0 -> H0(2D,M|2D) -> H1(W,B(-J0)) -> H1(W,M) -> 0.

Thus the middle space has dimension485, and the actual multiplication kernel is the specified space of sections on the first infinitesimal neighborhoods of the fifty torsion lifts. The forty-five-dimensional common-value boundary image from Section1 is injectively embedded in this space. Its intersection with the specified four-hundred-fifty-dimensional subspace is exactly H0(Kplus), not just a vector space of matching dimension.

This supplies an explicit geometric intersection model:

    H0(Kplus) = common-value boundary image intersect torsion-neighborhood boundary image,
                 inside H1(W,B(-J0)), of dimension485.

The dimension inequality gives at least ten, as before. Proving that this intersection has exactly ten dimensions is equivalent to beta0 surjectivity; the configuration is not asserted transverse. The later fifty reduced normal evaluations still have to be injective on this actual intersection to establish the remaining sufficient gate.
