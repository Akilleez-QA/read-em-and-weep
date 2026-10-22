# A global source-completion criterion with exact lift ambiguity

## Fixed input and scope

Work over the complex numbers on X=P^4, with nonzero fixed invariant
physical quadratic q. Retain the marked actual monad

    A0=S O(-1) --alpha--> E --beta--> A0* L,
    S=U+ A, rank S=5, E=U tensor Omega^2(2), L=Delta O(-1).

Here A denotes the negative quadratic representation, whereas A0 denotes the
left source bundle. E has its fixed nondegenerate alternating L-valued form.
The actual monad is exact at its ends, and its cohomology F is locally free of
rank two. Consequently alpha is a subbundle and its image is isotropic;
these assertions survive restriction to Q=(q=0), including its singularities.
No smoothness assumption on Q is used.

The degree-zero fixed-duality cochain C=(R,T,-R^dagger) has T skew. The
published convention is

    (dC)_left=T alpha-alpha R,
    (dC)_right=-R^dagger beta-beta T.

In particular R is an arbitrary End(S)-valued section, not trace-free. Its
AA, AU, UA and UU blocks must all be retained. The alternating trace of C
vanishes because its two end traces cancel and T is skew. This places no
additional condition on tr(R).

Let Z be the fixed closed degree-one cochain Z_a=k e_a, and put f=a h Z,
a degree-one cochain of twist four. We seek

    dC=f-q V,                     C of twist 4, V of twist 2.

No evaluation of the selected actual source or fourth Bockstein is made.

## 1. Necessary and sufficient fixed-middle criterion

Let T be any global skew middle endomorphism of twist four. Write pi for
E_Q -> E_Q/A0_Q and define

    r(T)=pi (T alpha-f_left)|Q.

Then the following are equivalent:

1. There exist global R of twist four and a closed fixed-duality degree-one
   V of twist two satisfying d(R,T,-R^dagger)=f-qV.
2. r(T)=0 as a section of Hom(A0_Q,E_Q/A0_Q)(4).

Proof. Necessity follows by reducing the left-arrow equation modulo q.
Conversely r(T)=0 means that T alpha-f_left factors through the subbundle
alpha_Q. Its factor R_Q is unique, as alpha_Q is injective. This factor is a
regular global section of End(A0_Q)(4), not a rationally defined expression.
Since End(A0)=End(S) O_X, the restriction exact sequence is

    0 -> End(S) O(2) --q--> End(S) O(4)
      -> End(A0_Q)(4) -> 0.

H^1(P^4,O(2))=0, so R_Q has a global lift R. Finite-group averaging supplies
a lift in the same equivariant family and physical-center parity whenever
the input family is equivariant.
The right-arrow identity follows automatically from the fixed duality of f
and C. For example, in a local marked alternating frame beta=alpha^t J and
T^t J+JT=0, one has

    (T alpha-alpha R)^t J=-beta T-R^t beta.

This is exactly the stated right-arrow differential, including its sign.
Thus f-dC vanishes on Q on both arrows. Multiplication by q is injective on
each locally free ambient cochain term, and its image is precisely sections
vanishing on Q. There is a unique global V=(f-dC)/q. Finally q dV=0 follows
from df=0 and d^2=0; local freeness gives dV=0. The fixed-duality projection
commutes with this division, so V lies in the required summand. QED.

This proves that there is no further end-arrow, source-globalization, or
closedness obstruction after the quotient equation for the chosen T. It does
not say that ramification/vertex tests imply that equation.

## 2. Exact ambiguity, including the induced change of V

For fixed T and f satisfying the criterion, the set of pairs (R,V) is an
affine space under End(S) tensor H^0(O(2)). Explicitly, for H in this space,

    R' = R+qH,
    C' = C+q(H,0,-H^dagger),
    V' = V-d(H,0,-H^dagger).

These are all possibilities because R_Q is unique. Its ordinary dimension is
25 times 15 =375. This is ambiguity of a divisible cochain solution, not of
solutions with a separately prescribed V. If V is fixed, the change above
must satisfy d(H,0,-H^dagger)=0; its left component is -alpha H, hence H=0.
Thus for fixed T,f,V the source completion is unique whenever it exists.
Moreover the ambiguity changes V by a global coboundary, so its ambient
cohomology class is independent of the lift. If a particular previously
chosen class v_h is required, the additional equality [V]=v_h must still be
checked. A source-lift change cannot repair a discrepancy of these classes;
the criterion supplies some divided class, not a prescribed Bockstein
representative or its normalization.

With the physical parity of the actual source channels, the center-even
ambiguity representation is

    6*1 +12*A +9*V +10*P +16*D,                 dimension 189.

Indeed End(S)=2*1+A+V+D+2*T6; its diagonal part is physical-even and its two
six-dimensional off-diagonal blocks are odd. Sym^2 H=1+A+D+T6 has even
part 1+A+D and odd part T6. Exact abstract character multiplication gives
the displayed decomposition. For P2=Sym^2 A tensor D=1+A+V+2P+3D, the
Gamma-equivariant family ambiguity therefore has dimension

    6+12+9+2*10+3*16=95.

This 95 is independent of, and must not be confused with, the 1095-dimensional
middle-family kernel of the joint vertex/ramification map in PR681. It is
not an extra Serre-involution eigenspace calculation.

## 3. The remaining obstruction is a specific parabolic connecting class

All bundles in this section may be restricted to Q. Define D to be the kernel
of the alternating pairing constraint on Hom(A0,E/A0): a quotient-valued
map u lies in D exactly when alpha^t J u is symmetric. The expression is
well-defined because A0 is isotropic. It gives exact sequences

    0 -> D -> Hom(A0,E/A0) -> Lambda^2 A0* tensor L -> 0,
    0 -> Hom(A0,F) -> D -> Sym^2 A0* tensor L -> 0.

The ranks are respectively 25 inside 35 with quotient 10, and 10+15=25.
The first map to alternating forms is surjective locally. The second uses
E/A0 -> A0* L with kernel A0-perp/A0=F.

Restriction of an infinitesimal symplectic endomorphism to A0, modulo A0,
is a surjective bundle map

    0 -> P -> sp(E) -> D -> 0,                  ranks 53,78,25.

Here P is the parabolic Lie algebra bundle preserving A0. To check
surjectivity without a global splitting, choose a local symplectic splitting
E=A0+F+A0*L. The component into F is arbitrary, and the component into
A0*L is precisely a symmetric bilinear form. These are exactly the freely
assignable lower blocks of a symplectic endomorphism; all remaining paired
blocks can be supplied. This local argument establishes sheaf exactness,
not a global splitting. P has Levi quotient End(A0)+sp(F) and nilradical
with associated graded Hom(F,A0) and Sym^2 A0 tensor L^{-1}.

Closedness and fixed duality of f imply that u_f=pi f_left lies in D(4):
the degree-two closedness equation is beta f_left+f_right alpha=0, and
f_right=f_left^t J, which says alpha^t J f_left is symmetric.
Consequently the exact obstruction to a skew solution ON Q is

    delta_Q(u_f) in H^1(Q,P_Q(4)),

where delta_Q is the connecting map of the displayed parabolic sequence.
It vanishes if and only if a T_Q with pi T_Q alpha=u_f exists. When it
vanishes, the choices of T_Q form a torsor under H^0(Q,P_Q(4)). No vanishing
of H^1(P_Q(4)) is asserted.

There is no extra middle restriction obstruction from Q to X in this degree:
0 -> sp(E)(2) --q--> sp(E)(4) -> sp(E)_Q(4) ->0 has H^1(sp(E)(2))=0.
Indeed, the exterior Euler resolution of E has terms G_i O(-1-i),
G_i=U tensor Lambda^(3+i)H for i=0,1,2. Its graded symmetric square,
tensored by L^{-1} O(2), resolves sp(E)(2) with line twists
1,0,-1,-2,-3. All these line bundles have zero positive cohomology on P^4;
the resolution is in nonpositive degrees, so it gives H^1=0. Thus the same
connecting class is the full obstruction to SOME global middle-and-source
completion, with no previously fixed vertex or ramification data imposed.
For a previously chosen T, the stronger fixed-middle criterion in Section 1,
not merely vanishing of this connecting class, is required.

## 4. The parabolic obstruction group is canonically the adjoint group

The parabolic group in Section 3 introduces no mysterious new cohomology
group. There is a canonical exact sequence

    0 -> N -> P -> sp(F) -> 0,

where N is the image of A0 tensor E tensor L^{-1} in
sp(E)=Sym^2 E tensor L^{-1}. Symmetric multiplication gives

    0 -> Lambda^2 A0 tensor L^{-1}
      -> A0 tensor E tensor L^{-1} -> N -> 0.

These assertions can be checked in a local symplectic splitting and hence
glue without selecting a global splitting. An A0-symmetric tensor preserves
A0 and induces zero on A0-perp/A0. Conversely the preserving endomorphisms
inducing zero on F have precisely those tensors. The ranks are
60-10=50 for N and 53-50=3 for sp(F). The map P -> sp(F) is the intrinsic
induced endomorphism on the quotient, so this exact sequence is canonical.

After twisting by four, the resolution of N becomes, up to the retained
constant determinant line Delta^{-1},

    0 -> Lambda^2 S O(3) -> S tensor E(4) -> N(4) -> 0.

The same sequence remains exact on Q because all its terms are locally
free. Both O_Q(3) and E_Q(4) have vanishing positive cohomology:
use respectively 0 -> O(1) -> O(3) -> O_Q(3) -> 0 and
0 -> E(2) -> E(4) -> E_Q(4) -> 0. The line bundles are positive, and
E(2)=U tensor Omega^2(4), E(4)=U tensor Omega^2(6) have positive Bott
vanishing. Thus H^i(Q,N_Q(4))=0 for every i>0. Consequently

    H^1(Q,P_Q(4)) -> H^1(Q,sp(F)_Q(4))

is a canonical isomorphism, and H^0(P_Q(4)) -> H^0(sp(F)_Q(4)) is onto.
The ordinary dimension of the acyclic kernel is explicit:
h^0(E(4))=560, h^0(E(2))=90 and h^0(O_Q(3))=30, so

    h^0(N_Q(4))=5(560-90)-10*30=2050,
    h^0(P_Q(4))=2050+h^0(B_Q(4)).

These dimensions follow from the exterior Euler sequence and Bott vanishing,
not from an actual-instance rank calculation.

For rank-two symplectic F, sp(F)=End_0(F)=B. Hence the precise obstruction
from Section 3 may be viewed canonically in the familiar H^1(Q,B_Q(4)),
not in an additional independent obstruction group. The pinned actual
fifth-neighborhood note already proves abstract existence of C_h for this
actual f; in particular its obstruction vanishes. What remains here is a
constructive whole-Q test for a chosen middle operator, not an unknown
abstract existence assertion. This is an identification
of obstruction groups and their natural map; it does not evaluate the actual
class delta_Q(u_f), or remove constraints on a previously specified T.

## Contribution and boundary

PR681 supplies unrestricted compatibility of vertex-middle values and the
three simultaneous mixed-functional coefficients. The criterion here shows
exactly what remains: a quotient-bundle equality on the whole singular
quadric. Once it holds, all four source blocks globalize, the right arrow
follows with its actual sign, the divided closed representative exists, and
its cohomology class is independent of the 95-dimensional family lift
ambiguity. No actual correction, beta4, higher-order extension, or
algebraicity conclusion follows from these structural statements alone.

## Pinned dependencies and verification

[Full actual cochain signs and source blocks](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/ACTUAL-MULTIPLIED-NILPOTENT-HAS-A-CANONICAL-SQUARE-ZERO-LIFT.md).

[Actual divided equation and abstract primitive existence](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/ACTUAL-FOURTH-BOCKSTEIN-AS-A-FIFTH-NEIGHBORHOOD-ADJOINT-BOUNDARY.md).

[Joint vertex and ramification compatibility](https://github.com/Akilleez-QA/read-em-and-weep/blob/a930f9cc295d79c2342b4eebe6f34efc04ccf05d/research/hm/degree-one-restriction/PROOF.md).

- PR543 at 8d8b5be4ce62c3055bb53be9e16d29cc63072f04:
  ACTUAL-MULTIPLIED-NILPOTENT-HAS-A-CANONICAL-SQUARE-ZERO-LIFT.md
  supplies the full source blocks, fixed duality, and differential signs.
- Same pin: ACTUAL-FOURTH-BOCKSTEIN-AS-A-FIFTH-NEIGHBORHOOD-ADJOINT-BOUNDARY.md
  supplies the actual divided equation and positive-twist Bott vanishing.
- PR681 at a930f9cc295d79c2342b4eebe6f34efc04ccf05d supplies only the
  vertex/ramification compatibility, not the quotient equation.
- verify.py checks universal ranks, twists, exact abstract characters and
  the ambiguity representation; it does not evaluate actual HM data.
