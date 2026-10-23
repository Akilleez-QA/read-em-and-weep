# The canonical negative quartic is the homotopy complement

## Result and scope

Retain the actual source2 pure-V compatible-radical hypothesis of PR1019.
Let Q:N2→N4 be the invariant quadratic, h:N4→N2 its unique equivariant
radical nullhomotopy, and I2=im j2=D⊂N2. Write D_can⊂N4 for the actual
canonical quartic subspace U4 constructed in PR1050, not for an arbitrary
copy of the character D. Then

    h|D_can : D_can → I2 is an isomorphism,
    ker h ⊂ im Q,
    im Q = ker h ⊕ D_can.                              (1)

These are equalities of actual equivariant subspaces. Their dimensions are
28+5=33. In particular the full degree-four part F4 generated from im h
by the fixed negative quadratic module satisfies

    F4 ⊂ ker h,       F4 ∩ D_can = 0.                  (2)

This gives an actual embedding comparison between the degree-one-generated
canonical string and the degree-two-generated homotopy module. It does not
select a source branch, evaluate a source coefficient, or determine the
marked quartic's degree-five descendants or terminal behavior.

## 1. Exact dependencies and novelty

INPUTS.json pins and authenticates these four complete proofs:

- PR1019, 3fb2475ffb275c5789acbaa8f9f84ed272713785: unique h, hQ=j2,
  Qh=j4, ker j4=im Q, im j2=I2, rank h=9, ker Q=A+D, and the literal
  secondary channel hT_a(x)=μ ax on A, with μ≠0.
- PR1048, 9eaed2dfadf9c4877327d21db5974b6c94d3863d: hT_a h=0 for every
  a∈A=Sym2 W, with W the fixed negative two-space.
- PR1054, 8732cb65fe0e72da59e785f3f85ad197a7092e6c: the actual generated
  module F2=im h, F3=W F2, F4=(Sym2 W)F2, with dimensions (9,14,≤16).
- PR1050, ec18a0fd62c4a9495adf6aad9564d379afc42b62: the actual canonical
  string U1=W, U2=A, U3=Sym3 W, U4=Sym4 W, with coherent embeddings f_d
  and usual negative-coordinate multiplication. Its proof establishes the
  needed actual nonvanishing and embeddings; they are not rederived here
  from characters.

The two strings and the still-unselected incidence of U4 with the
degree-four joint negative kernel remain distinct. Neither the earlier
generated-module theorem nor the
canonical-string theorem identifies the position of U4 relative to ker h.
Equation (1) supplies this missing compatibility, not another construction
of the string. In particular I2 and D_can are in different graded degrees.

## 2. Identification of the actual A and the normalization

PR1050's U2 is the unique A subspace of the actual N2=H1(B(2))_+.
The pinned source2 character is

    N2=A+2V+3P+4D.

Thus its A-isotypic component has multiplicity one. Since PR1019 gives
ker Q=A+D, the A appearing in its secondary channel is precisely U2,
not a freely chosen isomorphic subspace. Let

    f2:Sym2 W→U2,       f4:Sym4 W→D_can

be the coherent embeddings of PR1050. For all a,x∈Sym2 W, its actual
commutative multiplication gives the literal identity

    T_a f2(x)=f4(ax).                                  (3)

Choose a nonzero equivariant identification i_D:Sym4 W→I2. Adjusting the
nonzero scalar in PR1019 to this identification and the chosen f2 gives

    h T_a f2(x)=μ i_D(ax),       μ≠0.                  (4)

This is an equality in N2, not merely a class: PR1019's cohomology H0 is
ker Q itself, with no boundaries. The proof there also places T_a U2 in
im Q by original first-symbol vanishing. No value of μ is chosen here.
Changing the initial normalization of the canonical string rescales f2 and
f4 together; changing i_D only changes μ inversely. Nothing below depends
on either choice.

Ordinary multiplication Sym2 W⊗Sym2 W→Sym4 W is onto. For example its
image spans the five binary quartic monomials. Therefore (3) and (4) give

    h f4=μ i_D.                                       (5)

Both f4 and i_D are isomorphisms onto their actual images, so this proves
the first claim of (1). Also D_can is spanned by the T_a U2; hence
D_can⊂im Q. This last inclusion uses actual first-symbol vanishing, not a
character-compatible placement of a D copy.

## 3. The actual splitting and its intrinsic projector

If y∈ker h then j4 y=Qh y=0. Since ker j4=im Q, one obtains ker h⊂im Q.
On the other hand h(im Q)=im(hQ)=im j2=I2. Consequently restriction gives
an exact sequence of actual representations

    0→ker h→im Q --h--> I2→0.                          (6)

Equation (5) shows that its section is the inverse

    r=(h|D_can)^(-1): I2→D_can⊂im Q.

In particular h r=Id_I2 and (6) splits by this specific marked quartic.
The map

    π_can=r h|im Q

is an equivariant idempotent with image D_can and kernel ker h. It is
intrinsic to the marked D_can and h; rescaling the nonzero radical and h
rescales r inversely and leaves π_can unchanged. This does not define a
new Q-stable or horizontally stable decomposition of the full graded
module. The formula only asserts a projector on im Q⊂N4.

The dimensions are dim N4=37, rank h=9, dim im Q=33; thus dim ker h=28.
More precisely the character identities are

    im Q=2V+3P+3D,
    ker h=2V+3P+2D,
    D_can=D.

The subspace statement was proved before these checks and is not inferred
from them. Since im j4=I4⊂ker h, the marked quartic is also disjoint from
I4, consistently with their different characters.

## 4. Transport to the entire generated endpoint

By the sandwich theorem, for every a∈Sym2 W and y∈N4,

    h(T_a h y)=0.

By definition F4 is the span of all T_a h y, so F4⊂ker h. Combining this
with (1) proves (2) and π_can(F4)=0. In particular any D channel present
in F4 is disjoint from this specific canonical D_can. This is stronger
than noting that N4 has three D multiplicities, but it does not prescribe
which subspace of the remaining two-dimensional D multiplicity space F4
uses. No commutation between K_a and T_b for unrelated directions is used.

## 5. Certificate and limits

Run python verify.py (also python -O verify.py). It authenticates the four
retained inputs; verifies the exact universal binary multiplication span;
and checks the symbolic section/projector identities with an unevaluated
nonzero scalar, plus the dimension/character bookkeeping. Its block maps
are normal forms for (6) after the proved splitting, not actual HM matrices.
The actual identities (3), (4), first-symbol vanishing, and the sandwich
identity require the pinned written proofs and mathematical review. The
certificate does not replace them with synthetic evidence.

No actual source coefficients, parameter values, directions, jets or ranks
are evaluated. No source occurrence or exclusion follows. In particular
h|D_can being invertible gives no conclusion about multiplication from
D_can into degree five: h is an endpoint homotopy, not a graded-module
homomorphism for arbitrary subsequent arrows.
