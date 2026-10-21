# Linear formal symmetry strata and delayed symmetry breaking

Work over C. Let V=V51, Gamma=Aut(V), and D=Def_V, the functor of marked abstract deformation isomorphism classes on local Artin C-algebras with residue C. Automorphisms and group actions always fix the base. This note concerns abstract V51 deformations, not the selected original HM/source instance.

## Pinned inputs

All PRs refer to https://github.com/Akilleez-QA/read-em-and-weep.

- PR614, 73fbf75838c91804ca637b5916d6aac217240958: H0(Theta_V)=0, T=H1(Theta_V) has dimension 576, and abstract Artin deformations are unobstructed.
- PR624, 4fc9f009922b51369bfcaf4953919cb2f4c6c334: the full unpolarized group Gamma has order 3000 and contains the normal subgroup U=(Z/5)^2.
- PR626, 8c25863b2c17de5c652fc2ced74163c0a6364a0a: T restricted to U is 24 Reg0(U); for the six order-five subgroups H of U, dim T^H=96, T is the direct sum of these six subspaces, and T^U=0.
- PR627, 7c3f76f2e55c5cc0c3356972b5d7d676544c943a: the Gamma-action on T is faithful; every nonidentity gamma has dim T^gamma<=288, with equality for the inversion involution; T_free, the complement of their union, is nonempty.
- PR628, f08ff9c2760e4aef074cfe716b923d29d5e7ebe8: every compatible abstract formal one-parameter system admits a compatible lift of L0=O_V(1) and is effective as a projective flat finitely presented family over C[[t]] with that ample line bundle. Proper formal faithfulness injects fixed-base automorphisms into those of all reductions.
- PR630, 8024882d2129142fece5dbaf83b49e5f8e3817ca, Section 1: every finite jet of such a polarized formal system is realized on a smooth pointed finite-type curve, etale over A1 near its distinguished point, with a projective flat family and actual relatively ample line bundle restricting to L0.
- PR634, 895e3a61098f50eccc0a4dc22b58606a28125355, research/hm/cubic-algebraic-deformation-slices/PROOF.md: D is prorepresented by a complete regular local ring R noncanonically isomorphic to C[[x_1,...,x_576]]. This represents the full marked Artin class functor, not merely its tangent space. The ring is the completion of an actual smooth algebraic slice carrying a family. Every marked scheme automorphism is identity, over every Artin base.

## 1. The full formal action is linearizable

Choose markings alpha:X_C -> V. Replacing alpha by gamma composed with alpha gives a left Gamma-action on D, natural under every base change. Prorepresentability gives an action on the formal scheme Spf R. On its functions use the left action gamma(r)=(gamma inverse)^*(r); its action on E=m_R/m_R^2 is dual to the specified tangent action on T=E^*.

Choose any C-linear section s:E -> m_R of the quotient map. This exists because E is finite dimensional. Define

    s_eq(e) = (1/|Gamma|) sum_gamma gamma(s(gamma inverse(e))).

This is still a section and is Gamma-equivariant. Its image consists of a regular system of parameters: in any power-series coordinates for R, their linear coefficient matrix is invertible. The formal inverse function argument, solving coefficients degree by degree, therefore makes the induced continuous map

    completed Sym_C(E) -> R

a Gamma-equivariant isomorphism. More explicitly it is surjective by completeness and topological Nakayama; expressing the original coordinates as power series in the lifted parameters supplies the inverse. We have obtained a noncanonical Gamma-equivariant isomorphism of pointed formal schemes between Spf R and the completion of the vector space T at zero.

Consequently, after this one choice, there is a natural Gamma-equivariant bijection for every A,

    D(A) = T tensor_C m_A.

The right side is a set of vector-valued nilpotent coordinates. This is not a canonical additive structure on D. The isomorphism is formal: it does not make the algebraic slice of PR634 Gamma-stable, nor prove an algebraic or analytic linearization of that slice.

## 2. Fixed classes are exactly equivariant deformations

For an arbitrary deformation X_A, reduction to the marked special fiber is an injection

    Aut_A(X_A) -> Gamma.

Indeed, filter A by small extensions. At a small extension with kernel J killed by the maximal ideal, the kernel of automorphism reduction is H0(Theta_V) tensor J=0. Induction proves the injection. This also shows uniqueness of a lift of any specified special-fiber automorphism, whenever it exists.

The image is precisely the stabilizer of the marked class x in D(A). With the marking convention above, gamma fixing x means an isomorphism from (X_A,alpha) to (X_A,gamma alpha), whose special-fiber automorphism under alpha is gamma inverse. Inverting this isomorphism supplies the lift of gamma itself. Conversely a lift of gamma gives such an isomorphism after inversion. Since a stabilizer is closed under inverses, the image is exactly Stab_Gamma(x), and reduction identifies the two groups.

For any subgroup H of Gamma, a class fixed by every h therefore has unique lifts of all h. Their composites are the unique lifts of the corresponding products, so they satisfy the group law. Thus the functor D^H of fixed classes is exactly the functor of marked deformations carrying an action of this specified H, extending its original action on V. There is no additional choice of action and no hidden group-cohomology obstruction here: uniqueness of lifts supplies coherence.

Let I_H be the closed ideal of R generated by h(r)-r for all h in H and r in R. Then D^H is prorepresented by R/I_H. In the linear coordinates of Section 1, I_H is generated by the linear differences h(e)-e for e in E: the corresponding difference for a product is in the ideal of the linear differences, and passage to formal limits gives the assertion for series. Hence

    R/I_H = completed Sym_C(E / span{h(e)-e})
          = completed Sym_C((T^H)^*).

Every specified-subgroup symmetry functor is therefore a smooth linear formal germ of dimension dim T^H, to every Artin order. For H,K, the intersection D^H intersect D^K is D^<H,K>, equivalently its ideal is I_H+I_K.

In particular the six cyclic order-five fixed germs have dimension 96 and any two meet only at the constant formal germ; the U-fixed germ is the single constant germ. These conclusions upgrade the earlier smooth-functor statements to explicit representing formal subschemes. The linear coordinate choice is simultaneous for all subgroups, not a different unrelated choice for each one.

## 3. The symmetry arrangement and its precise meaning

Inside the completed tangent space take the reduced formal union of the fixed germs for nonidentity gamma, defined by

    I_B = intersection_{gamma != 1} I_<gamma>.

Each component ideal is generated by linear forms and is prime. By PR627 their largest dimension is exactly 288; the inversion involution attains it. Thus dim R/I_B=288 and this reduced formal arrangement has codimension 288 in the 576-dimensional universal germ. This is an all-order linear arrangement, not merely the tangent cone of an unknown nonlinear symmetry locus.

There are two necessary functorial cautions. First, the formal spectrum completed at the origin has only its closed origin as an underlying topological point. The complement of these fixed subfunctors is not being asserted to be a nonempty open formal subscheme. Second, for nonreduced A, factoring a map through the scheme-theoretic union R/I_B need not mean factoring it through any one component. Therefore the actual condition of retaining some nonidentity automorphism is the set-theoretic union of the fixed sets D(A)^gamma, not an unproved identification with Hom(R/I_B,A). Exact stabilizers are given by Section 2, or by the finite set of linear equations gamma(x)=x in T tensor m_A.

## 4. Symmetry can first disappear at any prescribed order

Fix an integer k>=1 and choose v in the nonempty set T_free. In the coordinates of Section 1 take the continuous formal arc

    x(t)=t^k v in T tensor t C[[t]].

Pulling back the universal formal family, or the completed actual family of PR634, gives a compatible marked system X_n over A_n=C[t]/(t^(n+1)). Its nilpotent coordinate is t^k v modulo t^(n+1). For n<k this is zero, so X_n is the constant marked deformation and

    Aut_(A_n)(X_n) = Gamma.

For n>=k, if gamma fixes x_n, then t^k(gamma(v)-v)=0 in T tensor A_n. Since t^k is a nonzero C-vector in A_n, this implies gamma(v)=v and hence gamma=1. Section 2 now gives

    Aut_(A_n)(X_n) = {1} for every n>=k.

The order-k class is nonzero, so this system is not constant. For k>=2 its first-order Kodaira-Spencer class is nevertheless zero. Thus vanishing first-order variation does not force even one nonidentity special-fiber automorphism to survive to all orders. One can prescribe exactly the first order at which all of them fail to extend, without evaluating a selected vector or source instance. The compatible formal automorphism group is trivial, since its restriction at every level >=k is trivial.

This goes beyond PR627's free first-order directions: all positive jets below the chosen threshold are constant and have the full 3000-element group. It makes no assertion about automorphisms of a geometric generic fiber or automorphisms allowed to move the base parameter. In particular reparametrizations t -> zeta t are outside the fixed-base statement.

## 5. Effective and finite-type realizations of the threshold

Apply PR628 to the system in Section 4. It is the completion of an actual projective flat finitely presented X over C[[t]], with an ample line bundle restricting to L0. Its fixed-base automorphism group is trivial: a global automorphism restricts to identity at every order n>=k, then at all lower orders, and proper formal faithfulness makes it identity. This is effectiveness over the formal DVR, not descent of the chosen entire arc to a finite-type C-curve.

There is also a finite-type realization of the same exact symmetry threshold. Choose compatible polarizations and apply PR630 with N=k+1. Obtain (Y,M) over a smooth integral pointed curve (B,b), with parameter t and matching marked pair modulo t^(k+1). For n<k its abstract Artin reduction is constant and has automorphism group Gamma; at n=k the group is trivial. For every n>k, any automorphism restricts to identity at n=k. Its successive reduction kernels are zero by H0(Theta_V)=0, so it too is identity. Thus the entire threshold, not only its first nonconstant jet, survives arbitrary higher terms in this algebraic approximation.

The fixed-base automorphism group of Y over the local DVR O_(B,b) is also trivial, by the same proper formal faithfulness argument of PR628 (Krull intersection at the special fiber and properness of the support). After restricting B to its integral component and shrinking as in PR630, Aut_B(Y) is trivial as well: an automorphism is identity over the local DVR, in particular on the generic fiber, and flatness over the integral base makes that generic fiber schematically dense. The equalizer ideal is therefore zero. These statements concern scheme automorphisms; scalar automorphisms of a line bundle paired with the identity scheme map still exist.

For k>=2 these finite-type families have zero first-order abstract class while being nonconstant at the prescribed kth order. No conclusion about the automorphism group of their geometric generic fiber is made: its automorphisms need not extend over B or its local DVR. No conclusion about persistence or loss of the ten original sections is imported from a theorem requiring a nonzero first-order class.

## 6. Forgetting the marking: orbits, not invariant-ring Artin points

For each A, let C_A be the groupoid of abstract deformations whose special fiber is isomorphic to V, with no chosen identification. A marking always exists by this definition. Choose representatives for the marked classes D(A) and forget their markings. Given two such representatives, every unmarked isomorphism determines its special-fiber element of Gamma. For a prescribed element there is at most one such isomorphism, by the zero marked-automorphism statement. Existence is exactly the equality of the corresponding re-marked classes. Composition corresponds to multiplication of the special-fiber elements, using the inverse convention noted in Section 2 where needed. This proves an equivalence of C_A with the action groupoid of Gamma on D(A); choices of representatives affect the equivalence, not the orbit or stabilizer descriptions.

In particular unmarked isomorphism classes are D(A)/Gamma and automorphism groups are the stabilizers computed above. This is an Artin-base groupoid assertion, not a construction of an unmarked global algebraic moduli space.

One must not replace D(A)/Gamma by Hom_cont(R^Gamma,A). A universal elementary counterexample is the sign action on C[[z]], whose invariant ring is C[[w]] with w=z^2. Over A=C[epsilon]/(epsilon^2), every z=a epsilon maps to w=0, while the invariant-ring point w=epsilon has no preimage. Distinct sign orbits can also have the same invariant-ring image. This example illustrates the functorial error; it is not a selected V51/source computation.

## Contribution and limits

The new result simultaneously linearizes the full finite-group action on the universal marked formal germ, represents every fixed-subgroup deformation functor, identifies all Artin automorphism groups exactly, and constructs delayed complete symmetry breaking with zero first-order class. The arrangement codimension is inherited from the pinned character calculation, now valid for the actual formal fixed germs. No algebraic Gamma-slice, generic-fiber automorphism theorem, convergence of arbitrary arcs, original HM/full-adjoint conclusion, Weil-class algebraicity, selected source evaluation, or large computation is claimed. This is an authored mathematical proof conditional on the pinned inputs, not proof-assistant verification.
