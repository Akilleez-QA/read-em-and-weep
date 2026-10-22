# The exact full-automorphism linearization criterion for the cubic polarization

Work over C. Let V=V51, let L0=O_V(1), and let nu:M -> V be its normalization. Write M=Bl_Z(P4), H=pi*O_P4(1), E=sum_(z in Z) E_z, and D=nu*L0. Let Gamma=Aut(V) and U=(Z/5)^2 be its projective Heisenberg subgroup. All group actions on families fix the base. A linearization is a coherent action on a line bundle, not merely invariance of its isomorphism class.

## Pinned dependencies

All references belong to https://github.com/Akilleez-QA/read-em-and-weep.

- PR611, commit 12b28d33627cc0e8b283d142dc16439a51bb5e00: M is the normalization and H0(M,O_M)=H0(V,O_V)=C.
- PR615, commit 24bc9b741c287f8ac207bd9df4de4c07c50bea2f: D=3H-E.
- PR623, commit be95ac2c06a947ded324b8865a18abca577597da, research/hm/cubic-automorphisms/PROOF.md: Gamma is the order-3000 projective Heisenberg normalizer, with exact sequence 1 -> U -> Gamma -> SL2(F5) -> 1. The quotient acts on U=F5^2 by its natural representation.
- PR624, commit 4fc9f009922b51369bfcaf4953919cb2f4c6c334, research/hm/cubic-unpolarized-automorphisms/PROOF.md: normalization lifting identifies Aut(V)=Aut(M)=Gamma; every element preserves the class of L0; E is intrinsically characterized and preserved as a divisor. The canonical formula is K_M=-5H+3E.
- PR632, commit fcb0300e36bd3b023e00a872c78207901392e7c8: H0(X_R,O)=R for every Artin deformation of V.
- PR637, commit a5fd5de0044a12bc7bb33f3431b1aa7eae7031b6, research/hm/cubic-equivariant-polarization-splitting/PROOF.md: a Gamma-fixed marked pair class has a unique underlying Gamma-action extending the given central scheme action; scalar defects lie in H2(Gamma,R*). Its Section 5 proves that the full-Gamma fixed pair-class functor consists only of the constant class.
- PR638, commit e45aed7546876fcba949918232e7716283dd8f59, research/hm/cubic-linearization-obstruction/PROOF.md: L0^m is U-linearizable exactly when 5 divides m, for every integer m. Its U-obstruction has exact order five.

The new step is sufficiency for the full group Gamma. It does not infer that sufficiency from the corresponding result for U.

## 1. A canonical fifth-power action on the normalization

The canonical line bundle omega_M has its natural action under automorphisms, induced by differentials. Since every element of Gamma preserves the effective Cartier divisor E, O_M(E) also has its canonical action: view it as the sheaf of rational functions with poles bounded by E and use pullback. These actions are coherent, including when the components of E are permuted. Tensor products and duals therefore give a canonical Gamma-linearization on

    B = omega_M^(-3) tensor O_M(4E).

The two pinned divisor identities imply

    -3K_M+4E = 15H-5E = 5D.

Thus an ordinary line-bundle isomorphism theta:D^5 -> B exists. Transport the canonical action on B across theta. This gives a Gamma-linearization on D^5 independent of the choice of theta. Indeed any other theta differs by multiplication by a constant c in C*, because H0(M,O_M)=C. Every automorphism fixes c, and conjugating the transported action by c leaves it unchanged.

The independence just proved concerns the transported action, not the isomorphism theta: the latter still has a C* ambiguity. No preexisting equivariant isomorphism or lift of Gamma to a linear representation was assumed.

## 2. Scalar-alignment descent of the action

We use the following elementary descent statement.

Lemma. Let f:Y -> X be equivariant for a group G. Suppose L is a line bundle on X whose isomorphism class is G-invariant, and pullback on global units O(X)* -> O(Y)* is an isomorphism. Then every G-linearization of f*L descends to a unique G-linearization of the fixed underlying line bundle L.

Proof. For each g choose an isomorphism a_g:g*L -> L. Its pullback and the prescribed isomorphism g*(f*L) -> f*L differ by a unique global unit on Y. By the units hypothesis that unit is the pullback of a unique unit on X. Rescale a_g by that unit, with the orientation chosen to make its pullback equal the prescribed lift. This determines a_g uniquely, independently of the initial choice. The two sides of each cocycle identity downstairs are isomorphisms between the same two line bundles. Their ratio is a global unit. Its pullback is 1 by the upstairs cocycle identity, hence it is 1 by injectivity on units. The identity element is treated identically. Thus the adjusted isomorphisms form a linearization. Uniqueness holds by the same ratio argument. QED.

Apply the lemma to f=nu and L=L0^5. The normalization is Gamma-equivariant by functoriality; the class of L is invariant by PR624. Pullback on units is the identity C* -> C*. Section 1 supplies the required upstairs linearization. Hence L0^5 has a preferred Gamma-linearization, characterized by its canonical fifth-power pullback action.

This is not a claim that arbitrary line bundles on M descend to V, nor that Pic(V) -> Pic(M) is injective. The underlying line bundle L0^5 downstairs is specified throughout. Only the action is being descended.

## 3. Exact divisibility and the full-group obstruction

Tensor powers of the linearization of L0^5, and duals for negative powers, prove sufficiency whenever 5 divides m. Conversely, any Gamma-linearization of L0^m restricts to a U-linearization. PR638 then forces 5 to divide m. Thus for every integer m,

    L0^m is Gamma-linearizable if and only if 5 divides m.       (1)

The case m=0 is included. The scalar obstruction alpha in H2(Gamma,C*) is additive under tensor powers. Section 2 gives 5 alpha=0. Its restriction to U is nonzero of order five by PR638. Therefore alpha itself has exact order five.

## 4. Gamma is perfect and the linearization is unique

First SL2(F5) is perfect. For a direct verification put t=diag(2,3). If u(x) is an upper elementary unipotent, then

    t u(x) t^(-1)=u(4x),   [t,u(x)]=u(3x).

As multiplication by 3 is bijective on F5, all upper elementary unipotents are commutators. Conjugation or the same calculation gives all lower elementary unipotents. These generate SL2(F5): elementary row operations reduce an invertible determinant-one matrix to a diagonal matrix, and diagonal determinant-one matrices are products of elementary unipotents. Hence the derived subgroup is the whole group.

Now let j in Gamma be any lift of -I in SL2(F5). Its conjugation action on U is inversion. In additive notation on U,

    [j,u] = -2u.

Since -2 is invertible in F5, this implies U is contained in [Gamma,Gamma]. The image of [Gamma,Gamma] in Gamma/U is all of SL2(F5), by its perfectness. Together these facts imply [Gamma,Gamma]=Gamma. No splitting of the group extension is needed.

Consequently Hom(Gamma,C*) is trivial. Any two Gamma-linearizations on the same invariant line bundle have ratio a scalar character, because all bundle automorphisms over the identity are constant scalars. Thus whenever (1) permits a linearization, there is exactly one on the fixed underlying line bundle, and exactly one isomorphism class if the underlying line bundle is specified only up to isomorphism.

Scalar automorphisms C* remain automorphisms of each linearized object. In particular this does not assert that equivariant isomorphisms between two representatives are unique. For L0^5 the unique action is the preferred one constructed in Sections 1–2. For all multiples of five it is its tensor or dual power.

This contrasts with U, where PR638 gives 25 linearization classes on each admissible fixed line bundle. Exactly one of those U-linearizations is the restriction of a full-Gamma linearization. This conclusion concerns restriction on the given scheme action, not a criterion for every subgroup of Gamma.

## 5. Artin persistence with the central action fixed

Let R be a local Artin C-algebra with maximal ideal m_R, and let (X_R,L_R) represent a Gamma-fixed marked pair class specializing to (V,L0). Use the unique underlying Gamma-action from PR637. Individual isomorphisms g*L_R^m -> L_R^m exist because the pair class is fixed. Their scalar two-cocycle has values in R*, by H0(X_R,O)=R. Gamma acts trivially on these scalars because it fixes the base.

There is a canonical decomposition

    R* = C* times (1+m_R).

The finite logarithm identifies 1+m_R with the additive C-vector space m_R. Averaging over the finite group Gamma gives Hq(Gamma,1+m_R)=0 for every q>0. Consequently reduction induces an isomorphism

    H2(Gamma,R*) -> H2(Gamma,C*).

The reduction of the obstruction of L_R^m is m alpha. Section 3 therefore gives the all-orders criterion

    L_R^m is Gamma-linearizable if and only if 5 divides m.     (2)

For an admissible m, its linearization reduces to the unique central one of Section 4. The relative obstruction and ambiguity groups H2(Gamma,1+m_R) and H1(Gamma,1+m_R) vanish, so a prescribed central linearization lifts uniquely up to equivariant isomorphism with that central identification. In fact Hom(Gamma,R*) is trivial because Gamma is perfect, so on any fixed representative the action is unique. Automorphisms of the marked linearized pair over the identity scheme are still the scalars 1+m_R; uniqueness of an isomorphism is not claimed.

These constructions commute with base change: pulling back a linearization gives one on the pulled-back representative, and uniqueness identifies it with the one already specified there. This gives compatible actions on every compatible formal system of such representatives. This is a statement about equivariant structures, not a claim of a unique choice of representatives or identifications.

By PR637 the full-Gamma fixed pair-class functor is already the constant class at every Artin order. Thus (2) resolves the scalar-sensitive structure on that fixed class; it does not produce new full-Gamma polarized deformations. It also does not linearize L_R on the twelve-dimensional U-fixed germ, nor change the nonzero U-obstruction there.

## Contribution and boundaries

The canonical-bundle identity on the normalization resolves the full-Gamma sufficiency left open in PR638. The full-group obstruction has exact order five. Perfectness of Gamma removes all character ambiguity, and logarithm plus averaging carries the criterion to every Gamma-fixed marked Artin pair class. The argument uses neither a Weil representation lift nor a selected coefficient or source-instance evaluation.

These results concern the cubic image V51 and its polarization. They do not settle the original adjoint/source problem, higher adjoint Bocksteins, or Weil-class algebraicity. The proof is mathematical and conditional on the pinned geometric inputs, not proof-assistant checked. No large computation is used.
