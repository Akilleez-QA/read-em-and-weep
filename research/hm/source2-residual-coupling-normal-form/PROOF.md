# A normal form for the source2 residual connection coupling

## Result and scope

Work over the complex numbers. Let G be the binary icosahedral group and W
its defining representation. Put A=Sym²W, S=Sym³W, D=Sym⁴W, T=Sym⁵W;
write V, P, W′ for the other three-, four-, and two-dimensional
irreducibles, as in the pinned sources. All these representations are
self-dual. Put X=P(W), using the invariant symplectic identification
W≅W* for binary forms and evaluation conventions.

Let M be the two-dimensional P-multiplicity space in H⁰(O_X(18)), and let
Σ=P(M). For t∈Σ let

    H_t=A⊕V⊕(P⊗t) ⊂ H⁰(O_X(18)),
    F_t=H_t*,
    c_t:C=O_X(-18) ↪ F_t⊗O_X

be its dual evaluation inclusion. Every member is basepoint-free by PR786,
so this is a saturated line inclusion for every t, not merely for the
balanced open locus B⊂Σ. Set

    V₁=Sym⁸W=P⊕D,
    U=U₂⁸=A⊗O_X(-6) ⊂ V₁⊗O_X,
    K=(V₁⊗O_X)/U ≅ T⊗O_X(3),
    H̄_t=V₁⊕F_t.

The theorem classifies G-equivariant saturated subbundles R⊂H̄_t⊗O_X for which

    R∩(V₁⊗O_X)=U,
    0 → U → R → C → 0                                  (1)

is exact, and the last map is induced by the stated constant projection
to F_t⊗O_X and its fixed endpoint c_t.

1. With the constant splitting V₁⊕F_t fixed, these subbundles are in
   bijection with the two-dimensional vector space

       A_coup=Hom_G(C,K).

   They are inverse images of graphs; no bundle splitting is
   differentiated.

2. Changing the equivariant constant complement to V₁ acts by translation
   by a nonzero line L_t⊂A_coup. It is exactly the image of the
   one-dimensional constant shear space Hom_G(F_t,V₁).

3. As t varies over the whole parameter line Σ, there is an exact sequence

       0 → O_Σ(-1) → A_coup⊗O_Σ → Q_coup → 0,          (2)

   with Q_coup≅O_Σ(1), up to a constant one-dimensional determinant
   factor. Thus the remaining additive coupling is a line of degree +1,
   not a second endpoint parameter.

4. For fixed t, under all G-equivariant constant ambient automorphisms
   over the identity of X preserving the vertical flag and the endpoint
   in the genuine quotient (H̄_t/V₁)⊗O_X, there are exactly two classes:

       coupling zero in Q_coup,t;
       coupling nonzero in Q_coup,t.

   Zero means that some equivariant constant complement splits R as
   U⊕C. A nonzero class cannot be made horizontally split by such a
   constant change of complement.

5. For every balanced t, both classes have the forced residual and
   annihilator bundle splittings of PR751 and the residual Gauss
   constraints of PR758 and PR785–787. Those residual constraints do not
   distinguish the two classes. PR788's displayed witness has zero
   coupling.

This is a classification of a specified residual constant-embedding
problem. It neither identifies the actual source's endpoint or coupling,
nor excludes source2, nor classifies the remaining extension into the
full 30-dimensional constant space. No actual HM realization is claimed.

## 1. Exact public inputs and novelty boundary

The following files were read at their stated immutable public pins in
Akilleez-QA/read-em-and-weep. The first four paths are under
research/hm/order-four-quadratic-load/.

- [PR751, residual full span](https://github.com/Akilleez-QA/read-em-and-weep/blob/e21d50b6bd7d124dc419beeb8c27fa3b9ef3e169/research/hm/order-four-quadratic-load/TWO-ONE-INDEX-TWO-RESIDUAL-FULL-SPAN.md),
  commit e21d50b6bd7d124dc419beeb8c27fa3b9ef3e169, proves the genuine
  invariant constant V₁, its exact intersection U, the final saturated
  endpoint, and the forced balanced annihilator splitting.
- [PR751, preceding residual osculations](https://github.com/Akilleez-QA/read-em-and-weep/blob/e21d50b6bd7d124dc419beeb8c27fa3b9ef3e169/research/hm/order-four-quadratic-load/TWO-ONE-INDEX-TWO-RESIDUAL-OSCULATIONS.md)
  identifies the complete degree-eight osculating flag; this is not
  inferred merely from an abstract bundle splitting.
- [PR754, balanced degree-eighteen systems](https://github.com/Akilleez-QA/read-em-and-weep/blob/044add76ebb14043a0edf73171517c90b9ef0c13/research/hm/order-four-quadratic-load/ABSTRACT-DEGREE-EIGHTEEN-BALANCED-SYSTEMS.md),
  commit 044add76ebb14043a0edf73171517c90b9ef0c13, gives Σ=P(M) and
  its balanced locus B, the complement of two distinct parameters.
- [PR758, exact residual Gauss flag](https://github.com/Akilleez-QA/read-em-and-weep/blob/063216038f3aefd65617651c2426721efafc7f9b/research/hm/order-four-quadratic-load/TWO-ONE-INDEX-TWO-EXACT-RESIDUAL-GAUSS-FLAG.md),
  commit 063216038f3aefd65617651c2426721efafc7f9b, supplies the
  constant-projection backward-kernel lemma.
- [PR785, four-jet rigidity](https://github.com/Akilleez-QA/read-em-and-weep/blob/7ec3b8140abe6ee60f9d0dfee657e7b0be022fc3/research/hm/source2-four-jet-rigidity/PROOF.md),
  commit 7ec3b8140abe6ee60f9d0dfee657e7b0be022fc3, proves the
  endpoint four-jet theorem and transfers it using genuine constant
  projections, allowing nonhorizontal extensions.
- [PR786, endpoint Wronskian](https://github.com/Akilleez-QA/read-em-and-weep/blob/575c0720268af5bb4b305e29284f65614ba9f9ca/research/hm/source2-endpoint-wronskian/PROOF.md),
  commit 575c0720268af5bb4b305e29284f65614ba9f9ca, proves
  all-parameter basepoint-freeness and classifies endpoint jet branches.
- [PR787, fifth and sixth transforms](https://github.com/Akilleez-QA/read-em-and-weep/blob/19ec11c934cbba7be18dd1f465ba0d0cc547dcf8/research/hm/source2-fifth-sixth-conditional/PROOF.md),
  commit 19ec11c934cbba7be18dd1f465ba0d0cc547dcf8, transfers the
  endpoint defects without assuming a horizontal splitting.
- [PR788, universal constant flag](https://github.com/Akilleez-QA/read-em-and-weep/blob/941b7b3b77dc8ae8a19b1e000dddeb0438d05db7/research/hm/source2-universal-constant-flag/PROOF.md),
  commit 941b7b3b77dc8ae8a19b1e000dddeb0438d05db7, constructs the
  split constant witness U₈¹⁰⊕U₂⁸⊕C_t and explicitly does not classify
  all constant embeddings with its listed properties.

The existing notes distinguish actual constant projections from arbitrary
bundle splittings and establish the residual flag or endpoint behavior.
They do not compute A_coup, its constant-shear image, the relative
degree-+1 quotient, or the two residual constant-gauge classes. Those are
the additions here. This novelty statement is relative to these checked
sources and the local source2 notes, not an unrestricted literature claim.

## 2. The graph classification is intrinsic to the quotient

Let π:H̄_t⊗O_X→K⊕(F_t⊗O_X) be quotient by U. By (1), projection identifies
R/U with the already fixed subbundle C⊂F_t⊗O_X. Its first component is
therefore a unique bundle map α:C→K, and

    R/U = Γ_α = { (α(c),c_t(c)) : c∈C },
    R = π⁻¹(Γ_α).                                     (3)

Conversely every G-equivariant α defines (3), with intersection U and
the exact quotient (1). The graph is saturated: locally C is a direct
summand of F_t⊗O_X, and its graph is a direct summand of K⊕F_t⊗O_X.
Consequently its inverse image under π is a subbundle with locally free
ambient quotient. This proves the bijection.

In particular the parameter is an embedding map into an ambient quotient,
not an element of Ext¹(C,U). Indeed the latter extension group is zero:

    Ext¹(C,U)=A⊗H¹(O_X(12))=0.                        (4)

Every R splits as an ordinary bundle. Equation (4) says nothing about
whether such a splitting comes from a constant ambient complement, which
is the issue measured by (2).

The apolar pairing on Sym⁸W identifies ann(U) with
T⊗O_X(-3): at ℓ∈P(W) its fiber is ℓ³Sym⁵W, the annihilator of
ℓ⁶Sym²W. Duality gives K≅T⊗O_X(3). Hence

    A_coup=(T*⊗H⁰(O_X(21)))^G,
    dim A_coup= multiplicity of T in Sym²¹W = 2.        (5)

For a formal character derivation of the last equality, PR754 gives

    Sym¹⁸W=A+V+2P+D,
    Sym¹⁹W=W+S+W′+2T.

The standard Clebsch recurrence and the representation products

    W⊗A=W+S,    W⊗V=T,      W⊗P=W′+T,
    W⊗D=S+T,    W⊗T=D+V+P,  W⊗W′=P

give successively

    Sym²⁰W=1+A+V+P+2D,
    Sym²¹W=W+2S+2T.

The fifth product follows from W⊗Sym⁵W=Sym⁶W+Sym⁴W and
Sym⁶W=V+P. The last follows by comparing
W⊗Sym⁷W=Sym⁸W+Sym⁶W with Sym⁷W=W′+T. These are universal
representation identities, not numerical tests of a source.

## 3. A small Wronskian lemma prevents a zero shear direction

Let P₈⊂Sym⁸W be its unique P-summand. Define

    B_P=Hom_G(C,P₈⊗O_X),
    ρ:B_P→A_coup,

where ρ is composition with P₈⊗O_X↪V₁⊗O_X→K. The degree-eighteen
decomposition gives dim B_P=2. We prove that ρ is injective, hence an
isomorphism by (5).

We use the following elementary characteristic-zero fact. If L is a
four-dimensional subspace of H⁰(O_X(8)), its order-three jet determinant
is nonzero. To see this universally, at an arbitrary point choose a
basis adapted to its vanishing filtration, with distinct initial orders
a₀<a₁<a₂<a₃. The leading Wronskian coefficient is the product of their
nonzero initial coefficients and the nonzero Vandermonde
∏_{i<j}(a_j−a_i). Thus the determinant cannot vanish identically. Its
line bundle has degree 4·8−2(0+1+2+3)=20, but only nonvanishing is needed.
Outside its divisor, the order-three jet map is injective. In particular,
no nonzero section of L can vanish to order at least four there.

Apply the fact to L=P₈. Under the symplectic identification W≅W*, a
vector ℓ is the linear form v↦ω(ℓ,v), which vanishes at the projective
point [ℓ]. Therefore a form in ℓ⁶Sym²W vanishes to order at least six
at [ℓ]. This fixes the apolar point convention, rather than silently
identifying a vector with evaluation at the wrong dual point. We obtain

    P₈ ∩ (U₂⁸)_[ℓ] = 0

on a dense open subset of X. This is a generic statement for a fixed
representation subspace, not an evaluation at any selected point.

If β∈kerρ, then β(C) lies in both P₈⊗O_X and U. On the displayed
dense open subset the intersection is zero, so β is zero there, hence
zero everywhere. Thus

    ρ:B_P ≅ A_coup.                                    (6)

This also gives a useful normal form: every α has a unique lift
β:C→P₈⊗O_X. Its residual is

    R = U + { (β(c),c_t(c)) : c∈C }.                   (7)

The sum in (7) is direct as a bundle because projection to F_t identifies
the second term with C. Its uniqueness is relative to the distinguished
P₈ summand, not a claim that this generally nonconstant lift is horizontal.

## 4. The shear line and its parameter degree

For fixed t, an equivariant constant shear is

    g_b(v,f)=(v+b(f),f),  b∈Hom_G(F_t,V₁).

Since F_t≅A+V+P and V₁=P+D, Schur's lemma gives

    dim Hom_G(F_t,V₁)=1,

and every such map has image in P₈. It acts in (3) by

    α ↦ α + [(V₁⊗O_X→K)∘b∘c_t].                     (8)

A nonzero b has nonzero restriction to C: otherwise it kills the
constant span of C, which is all of F_t because the ten defining
sections are independent. Its restriction belongs to B_P. By (6), its
image in A_coup is nonzero. Thus the shear image L_t is exactly a line.

For the relative statement, choose an invariant identification of P₈*
with the irreducible P used in M. It identifies B_P with M; changing it
rescales this identification and does not alter the parameter lines.
Under this identification, restriction of the shear at t is precisely
the line t⊂M: it evaluates the P⊗t part of H_t and then contracts its
dual multiplicity line.

More formally, the universal system on Σ is

    H_univ=(A⊕V)⊗O_Σ ⊕ P⊗O_Σ(-1),
    F_univ=H_univ*.

Its universal dual evaluation has source O_X(-18) pulled back from X,
with no parameter twist. Thus the relative graph space is the constant
bundle A_coup⊗O_Σ, whereas

    Hom_G(F_univ,V₁⊗O_Σ) ≅ O_Σ(-1).

By (6), its image is the tautological line under a linear isomorphism
M≅A_coup. This proves (2). In determinant-sensitive form,

    Q_coup ≅ (det A_coup)⊗O_Σ(1),                    (9)

after the corresponding identification of tautological lines. The
constant determinant factor can be trivialized but has no preferred
nonzero generator. Restricting gives the same sequence over B.

Consequently change of constant complement removes exactly one of the
two graph directions, everywhere in parameter space. There is no
parameter where the shear unexpectedly becomes zero or removes both
directions. Nor is a canonical global nonzero coupling representative
asserted: a degree-one line on the full projective parameter line has
no nowhere-vanishing global section.

## 5. The complete constant stabilizer and the two classes

Let Γ_t consist of all invertible G-equivariant constant linear maps
on V₁⊕F_t, covering id_X, that preserve the vertical osculating flag
and preserve C as a subbundle in the quotient by V₁. In fact preserving
U₂⁸ alone suffices for the vertical condition.

First, the span of the fibers of U₂⁸ is V₁, because it contains the
Veronese line U₀⁸ whose fibers span Sym⁸W. Therefore every element of
Γ_t preserves the constant subspace V₁; no lower off-diagonal term
can occur. Write it uniquely as

    g(v,f)=(a(v)+b(f),d(f)).

The constant map a commutes with differentiation. Preservation of U₂⁸
therefore implies preservation of its backward transforms U₁⁸ and
U₀⁸, using the genuine complete osculating identities of PR758.

A constant endomorphism preserving every line of a full-span projective
curve is scalar. Indeed each such line lies in an eigenspace; the curve
is irreducible, so its image lies in one of the finitely many projective
eigenspaces. Full span makes that eigenspace the whole vector space.
Apply this to the Veronese curve U₀⁸ to obtain a=a₀·id_V₁, with a₀≠0.
Apply it to the full-span endpoint curve C⊂F_t⊗O_X to obtain
d=d₀·id_F_t, with d₀≠0. This latter argument is for the fibers of one
fixed endpoint as x varies in X; it does not assume simultaneous
preservation of all endpoint parameters.

There is no further restriction on b: every b∈Hom_G(F_t,V₁), together
with nonzero a₀,d₀, gives such an automorphism. Thus we have described
the full stabilizer, not merely a convenient subgroup. Its action is

    α ↦ (a₀/d₀)α + (1/d₀)ρ(b∘c_t).                   (10)

Modulo the shear line, (10) is arbitrary nonzero scalar multiplication
on the one-dimensional vector space Q_coup,t. This has exactly two
orbits, zero and nonzero. Every two lifts of the same quotient vector
differ by a realizable shear. This proves the claimed exhaustive
two-class statement.

The zero class is equivalent to α∈L_t, which by (8) is equivalent to
a constant shear sending R to U⊕C. It is therefore precisely the
existence of a horizontally split residual lift. The nonzero class is
the failure of that property, despite the ordinary bundle splitting (4).

The word “endpoint” in this statement is essential: it is the endpoint
in the genuine quotient by V₁, not a chosen lift (0,C) in a distinguished
constant complement. If the complement or horizontal lift is additionally
fixed, shears are forbidden. Then this two-orbit theorem does not hold;
with scalar changes still allowed, the nonzero graph directions are
parameterized by P(A_coup). No such extra choice is intrinsic to the
source2 constant quotient.

## 6. Why the already proved residual constraints do not remove a class

Fix t∈B and any α. Equation (4) and averaging over the finite group give

    R≅A O_X(-6)⊕O_X(-18)

as equivariant bundles. Let E′=ann(R)⊂(V₁*⊕F_t*)⊗O_X. The exact
intersection and endpoint projection give an exact annihilator sequence

    0 → ann_F_t*(C) → E′ → ann_V₁*(U) → 0.

Because t is balanced and K*=T O_X(-3), this is

    0 → (P+D)O_X(-2) → E′ → T O_X(-3) → 0.            (11)

Its extension group is a constant coefficient space tensored with
H¹(O_X(1))=0. Averaging again gives

    E′≅T O_X(-3)⊕(P+D)O_X(-2).                        (12)

These are exactly the forced PR751 residual splittings. In particular,
both R and E′ are negative. Their constant spans are full: a proper
constant span would yield a nonzero constant section of the negative
annihilator. Alternatively, U spans V₁ and the endpoint spans F_t,
which directly proves full span of R.

PR758's constant-projection kernel lemma applies to (1), since the
negative saturated endpoint has zero backward kernel. Consequently,
for every α,

    R⁻=U₁⁸,    R⁻⁻=U₀⁸,    R⁻⁻⁻=0.                  (13)

For k≤4, the proof in PR785, Section 5, uses only (1), the complete
vertical flag, and the endpoint's four-jet spanning. Its local lifts
are allowed to be nonhorizontal; nothing in that proof depends on α
being zero. It therefore gives, for all couplings,

    0 → U_(k+2)⁸ → R^(k) → C^(k)=U_k¹⁸ → 0,
    0≤k≤4,                                          (14)

with its sheaf-surjectivity and saturation assertions. In particular
the ranks, degrees and consecutive bundle quotients there are unchanged.

Similarly PR787's residual arguments use (14), the constant quotient,
equivariance, and the endpoint jet branch. In its exceptional fifth
step, the possible vertical repair is forced to vanish by the distinct
stabilizer characters of its source and vertical target lines; that
argument already allows arbitrary residual extension data. At the sixth
step the complete constant V₁ is present, so the residual is the full
inverse image of the saturated endpoint transform. Thus its three
residual fifth/sixth branches apply to every α, with the same endpoint
t. This observation does not import its separate full-HM conclusions
without their own hypotheses.

Equations (11)–(14), together with those residual branch statements,
show directly that both constant-gauge classes survive these known
residual constraints. They are not distinguished by replacing a bundle
splitting with a more careful proof of the already stated residual
flags. An additional condition, if it is to decide the coupling of the
fixed source, must carry information beyond those residual invariants.

## 7. Relation to PR788 and the still-open source problem

PR788 takes, in its genuine constant three-block sum,

    R_t=U₂⁸⊕C_t.

In the graph chart this is α=0, hence the zero class of Q_coup,t. The
proof that all listed abstract interfaces are jointly feasible remains
valid. It is an existence witness, not evidence that a hypothetical
actual source must have zero coupling.

Conversely, the present theorem makes the missing residual datum small
and precise: after the endpoint and complete vertical flag are fixed,
there is one additive coupling line modulo constant complement changes,
and only its zero/nonzero status remains under the full constant
stabilizer specified above. It is genuine constant-embedding data,
although all the associated ordinary extensions split.

For an actual constant extension

    0 → V₁ → H̄ → F_t → 0,

semisimplicity supplies an equivariant constant splitting. Different
choices differ by exactly the shears used above. Therefore its quotient
coupling and, independently of scalar identifications, its zero/nonzero
class are well-defined. No construction or calculation in this note
determines that class for the fixed HM problem. Nor does fixing it
identify the remaining lift through the first constant quotient,
the original multiplication tensors, or their full module structure.

## Method boundary

This is a universal representation-and-bundle proof over the entire
abstract endpoint parameter line, with a balanced restriction only where
the balanced splitting is invoked. No parameter, invariant-form
coefficient, actual source point, derivative, matrix, rank, or
source-instance evaluation is selected or computed. No scan, selected
model, or large computation is used. The Wronskian is a universal
nonvanishing argument, and the character arithmetic is symbolic. This is
a written proof, not proof-assistant certification.
