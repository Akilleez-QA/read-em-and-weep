# Component constants do not give a two-open representative of the normal class

## New conclusions

Let X=P_stack(1,1,2,2), with coarse quadric Q, and use physical twists O_Q(t). Write B_X for the pullback of B_Q. The actual regular spinor zero scheme has disjoint support C union L, where C is the reduced conic and L is the vertex line. Set R=pi_*O_(2Z) and J=pi_*I_Z^2.

For the invariant first-normal class eta in H1(B_Q(-2))^G=C, the negative square sequence gives an exact sequence

    0 -> C eta -> H1(J)^G -> C -> 0,
    dim H1(J)^G=2.                                        (1)

The two shadow dimensions arise from the difference of the conic and vertex constants, and an additional invariant nilpotent vertex section. The actual linear relation selecting eta between these two shadows is not determined by disconnectedness of the support.

Moreover, the cover U_C=X minus L, U_L=X minus C cannot represent eta by a single adjoint section on its overlap: that overlap has NO sections of B_X(-2). In particular the tempting two-open, single-cocycle argument for [eta,eta]=0 does not apply.

These statements do not determine the quadratic coefficient d=one-half[eta,eta] in the normal lifting obstruction. They isolate a concrete missing map rather than assert vanishing from support geometry.

## 1. The primary term at negative twist

Twist the established square sequence

    0 -> P0 -> B_Q(2) -> pi_*I_Z^2(4) -> 0,
    P0=F_Q tensor S(1),

by minus four. Put Pminus4=P0(-4). The actual ambient spinor presentation gives

    0 -> Wprime F(-4) -> Wprime F(-3) -> i_*Pminus4 -> 0.

The primary cohomology support, and F*=F(1), give

    H3(F(-4))=H1(F)*=N*=N=A+Wprime,
    H^j(F(-3))=0 for all j,
    H^j(F(-4))=0 for j!=3.

Hence H1(Pminus4)=0 and H2(Pminus4)=Wprime tensor N. This last representation has exactly one invariant. The square sequence is therefore

    0 -> Pminus4 -> B_Q(-2) -> J -> 0.                    (2)

The previously proved invariant cone groups are H1(B_Q(-2))^G=C and H2(B_Q(-2))^G=0. For the second assertion use the ambient restriction sequence, H2(B(-2))^G=0 from the negative-monad nonzero scalar theorem, and H3(B(-4))^G=H1(B(-1))^{G,*}=0 because H1(B(-1))=V+W. The invariant long exact sequence of (2) proves (1).

## 2. Independent square-shadow calculation

The positive vertex filtration at physical twist zero, from POSITIVE-SECOND-BOCKSTEIN-SQUARE-FILTRATION.md, has graded pieces

    O_L,  D5 O_L(-2),  V8,
    0 -> P4 O_L(-8) -> Sym^8 Wprime O_L(-4) -> V8 -> 0.

The intervening odd pieces have negative central character, so have no G invariants. On L=P(W), the degree-one cohomology of the left term in the last sequence is P4 tensor Sym^6 W, with one invariant since Sym^6 W=P4+V. The degree-one cohomology of its middle term is Sym^8 Wprime tensor Sym^2 W=(P4+D5) tensor A, with no invariants. Both terms have no H0. Thus

    H0(V8)^G=C,  H1(V8)^G=0.

Also H0(D5 O_L(-2))=0 and H1(D5 O_L(-2))^G=0. It follows through the actual filtration, without a sheaf splitting assumption, that

    dim H0(R_L)^G=2,  H1(R_L)^G=0.

One of these two sections is the constant function; the other lies in the highest positive filtration and is nilpotent. On the conic component, the positive quotient is O_C and its conormal part is odd. Therefore dim H0(R_C)^G=1. The supports are disjoint, so dim H0(R)^G=3. Finally

    0 -> J -> O_Q -> R -> 0

and H1(O_Q)=0 identify H1(J)^G with H0(R)^G/C. The quotient has dimension2. The constant image is diagonal on the two reduced components. Thus its quotient retains one component-difference class and one nilpotent vertex class. They are independent as subquotients; no canonical splitting or identification of eta with either one is asserted.

The companion verifier checks the representation multiplicities, including the ones controlling primary H2 and V8. It does not evaluate the boundary H1(J)^G -> H2(Pminus4)^G.

## 3. Hartogs rules out the proposed two-open cocycle

The overlap U=U_C intersection U_L is X minus (C union L). Its complement has codimension two in the smooth normal stack X. Hartogs extension for locally free sheaves, checked on smooth local charts and descended, gives

    H0(U,B_X(-2))=H0(X,B_X(-2))=H0(Q,B_Q(-2)).

The last equality uses exact tame coarse pushforward and the pullback description of B_X. The ambient restriction sequence gives

    H0(B(-2)) -> H0(B_Q(-2)) -> H1(B(-4)).

Both outside groups vanish, by stability and the established H3(B(-1))=0 with Serre duality. Thus the overlap section space is ZERO. Since eta is nonzero, it is not a Cech 1-cocycle on this two-open cover with coefficients B_X(-2).

By contrast, the component-difference shadow in H1(I_Z^2) does have a single-overlap representative: on U the ideal is O_U and the difference of the two constant lifts is 1. The quotient B_X(-2)->I_Z^2 is surjective as a sheaf, but its map on H0(U) is not surjective. Indeed its source is zero and its target contains 1. Thus the required lift fails at the level of sections on the overlap, even though it exists locally on finer affine charts. Replacing sheaf surjectivity by this false global surjectivity would erase exactly the extra gluing data needed for the bracket.

The cover is not acyclic for B_X(-2). Its Mayer-Vietoris sequence instead embeds H1(X,B_X(-2)) in H1(U_C,B_X(-2)) plus H1(U_L,B_X(-2)); eta has nonzero local cohomology on at least one of these two opens. Refinement introduces additional cochains and their brackets, so the lack of triple intersections in the coarse two-open cover is not a self-square vanishing proof.

## 4. A different actual low-twist scalar test

There is an exact replacement for the quadratic bracket test that does not rely on component constants. Q is Gorenstein with omega_Q=O_Q(-3), and the trace pairing makes B_Q self-dual. Hence

    R=H1(B_Q(1))^G is dual to H2(B_Q(-4))^G,
    H2(B_Q(-1))^G is dual to T=H1(B_Q(-2))^G.

All four spaces are one-dimensional. For R, this also follows directly from the restriction sequence: H1(B(1))^G=0, H2(B(-1))^G=C and H2(B(1))=0. These inputs were independently checked in the finite-normal-tower note and its character verifier.

The class eta defines the actual adjoint cup map

    ad_eta:R -> H2(B_Q(-1))^G,
    theta |-> [eta,theta].                              (3)

With the usual cohomologically graded bracket, eta and theta both have degree1, so [eta,theta]=eta theta+theta eta. Cyclicity of the trace with its Koszul signs gives

    Tr([eta,eta] theta)=Tr(eta [eta,theta]).

Here both sides have total twist -3 and cohomological degree3, so Tr includes the Serre trace H3(omega_Q)->C. Therefore, writing Qeta=[eta,eta]/2 for the quadratic obstruction coefficient,

    <Qeta,theta> = (1/2)<eta,ad_eta(theta)>.             (4)

The trace-free bracket is understood; its scalar trace part vanishes in cohomology. Exactness of invariants makes the restricted Serre pairings nondegenerate. Since eta generates T, (4) proves

    d=0 if and only if the actual map (3) is zero.

For a nonzero theta, normalize the known nonzero linear coefficient by <Deta,theta>. The coordinate-dependent ratio is explicitly

    d/c = Tr(eta [eta,theta]) / (2 Tr(Deta theta)).       (5)

The denominator is NONZERO by the proved derivative isomorphism and Serre duality. Changing theta rescales numerator and denominator equally. Scaling eta has exactly the expected effect of rescaling the affine normal coordinate.

This gives another authorized route: determine the actual low-twist invariant adjoint cup map (3). Its value is not fixed by the one-dimensional source and target, and is not inferred from the nonzero derivative D. The component-cover obstruction in Section3 cannot dispose of this map.

## Sources and remaining gate

The square sequence, actual filtered vertex quotient and physical parity are in POSITIVE-SECOND-BOCKSTEIN-SQUARE-FILTRATION.md and LOWER-CONE-COHOMOLOGY-PERFECT-NEGATIVE-ACTION.md. The ambient negative groups are in FIRST-NORMAL-NONUNIQUENESS-INDEPENDENT-MONAD-CHECK.md and NEGATIVE-MONAD-INVARIANT-SCALAR-IS-NONZERO.md. The primary support statements and actual resolutions have the immutable source d5d9bd997145b0ecf7d7bd659a19fb7845afb75f, research/hm/actual-primary-image-extension/PROOF.md. Normal obstruction conventions are retained from the frozen normal-derivative note.

To evaluate d one still needs the actual adjoint lift and its cochain bracket, or another genuine geometric argument. Disconnected support, the two shadow dimensions, and existence of a sheaf quotient do not supply that argument. No frozen note was changed and no actual coefficient or matrix was evaluated.
