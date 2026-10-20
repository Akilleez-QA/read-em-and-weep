# Conditional exclusion of projective CM lifts

## Result and boundary

Work over the complex numbers. Let C be the elliptic curve, X=C^4, N=external_product O_C(infinity), and sigma the simultaneous CM automorphism in the [global-Hom proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/4659e4425c6b5ab6b1899e6af93656ac03ff0862/research/hm/null-cm-global-hom/PROOF.md). Assume its historical A-identity premise and physical-bundle identification. Thus the locally split complex

    K^a = (N^(2a+1))^(r_a),  a=-1,0,1,2;  r=(5,15,10,2)

has only degree-zero cohomology F, a rank-two vector bundle. Import also the preceding proof's conclusion Hom_X(F,sigma*F)=0. Then:

1. P(F) and P(sigma*F) are not isomorphic over X. Equivalently, P(F) has no global regular automorphism covering sigma.
2. F has no nontrivial line-bundle self-twist: F≅F⊗L implies L≅O_X.
3. More strongly, for every nontrivial L in Pic^0(X), both Hom_X(F,sigma*F⊗L) and Hom_X(F,F⊗L) vanish.

All conclusions are conditional on the imported A premise. This argument neither reauthenticates that premise nor strengthens the conclusion to rational/meromorphic maps, which are not excluded. It does not assert that all projective automorphisms over the identity are trivial.

## 1. Determinant, including the degree −1 sign

A locally split complex exact outside degree zero has the same determinant as its degree-zero cohomology, by cancellation of the adjacent exact pairs. Odd cohomological degrees, including −1, contribute inverse determinants. Therefore

    det F ≅ ⊗_a (det K^a)^((-1)^a)
          ≅ N^(−5·(−1)+15·1−10·3+2·5)
          ≅ N^0 ≅ O_X.

The alternating rank is −5+15−10+2=2. In particular det(sigma*F)≅O_X as well. These are line-bundle isomorphisms, not merely equalities of numerical first Chern classes.

## 2. Why a projective isomorphism gives an actual line twist

Use the quotient convention P(E)=Proj Sym(E). Suppose u:P(F)→P(G) is an X-isomorphism, with projections pi and rho. Every geometric fiber is P^1 and u restricts to an automorphism, so

    Q := u*O_{P(G)}(1) ⊗ O_{P(F)}(−1)

restricts to O on each fiber. Cohomology and base change (fiber H^0 of dimension one and H^1=0) gives a line bundle M=pi_*Q and an evaluation isomorphism pi*M≅Q; the latter is an isomorphism on every fiber and hence globally. Thus

    u*O_{P(G)}(1) ≅ O_{P(F)}(1)⊗pi*M.

Push forward along pi. The projective-bundle formula gives G≅F⊗M, hence F≅G⊗L for L=M^(-1). This also explains the harmless inverse convention. For G=sigma*F, taking determinants yields L^2≅O_X. The same argument applies to an assumed self-twist directly by taking its determinant. See [Stacks, Projective bundles, especially Example 27.21.3](https://stacks.math.columbia.edu/tag/01OA) for the convention and pushforward formula.

The line-descent step and the projectivization classification are also stated explicitly in [Vakil, Foundations of Algebraic Geometry, Proposition 2.4 and Exercise 2.6, PDF pages 50–51](https://math.stanford.edu/~vakil/0506-216/216Cjun2807.pdf#page=50).

No unrelated Brauer obstruction is left over: both projective bundles here already come from the specified vector bundles, and the fiberwise degree-zero quotient Q explicitly constructs the twisting line.

## 3. Torsion and the cohomology support

For an abelian variety A, NS(A)=Pic(A)/Pic^0(A) is torsion-free: it embeds by L↦phi_L into Hom(A,A-dual), which is torsion-free. Consequently every torsion line bundle on X belongs to Pic^0(X). Also Pic^0(C^4) is the product of the four Pic^0(C)'s, so any L in Pic^0(X) is an external product of degree-zero L_j. These facts are recorded in [Conrad, Abelian Varieties, Remark 4.2.11, Remark 5.2.3 and the discussion on printed p. 51](https://math.stanford.edu/~conrad/249CS15Page/handouts/abvarnotes.pdf).

On an elliptic curve a nontrivial degree-zero line bundle has no section: a nonzero section would have an effective divisor of degree zero and trivialize it. Its H^1 also vanishes by Serre duality. A positive-degree line bundle has H^1=0; a negative-degree line bundle has H^0=0. Thus, if L≠O_X, at least one L_j is nontrivial, and [Künneth](https://stacks.math.columbia.edu/tag/0BEC) gives

    H^q(X,L)=0 for all q;
    H^q(X,N^(2p)⊗L)=0 unless q=0, if p>0;
    H^q(X,N^(2p)⊗L)=0 unless q=4, if p<0.

The same positive/negative-degree support statements hold for L=O_X, but the all-degree vanishing at p=0 requires L nontrivial.

## 4. The amplitude argument has no total-degree-zero entry

Take tau=sigma or tau=id. Both preserve N, so the internal Hom complex

    A_L = Hom^bullet(K, tau*K⊗L)

has terms that are sums of N^(2p)⊗L in degrees −3≤p≤3. Bounded local freeness and K≃F[0] identify its hypercohomology in degree zero with Hom_X(F,tau*F⊗L). Use the [Čech hypercohomology spectral sequence](https://stacks.math.columbia.edu/tag/01FP)

    E_1^(p,q)=H^q(X,A_L^p) => H^(p+q)(RΓ A_L).

For nontrivial L in Pic^0(X), the p=0 column is entirely zero. For p>0 the only possible q is zero, giving total degree at least one; for p<0 the only possible q is four, again giving total degree at least one since p≥−3. Hence every E_1 entry of total degree zero vanishes. Every later entry at those positions is a subquotient of zero, and the finite convergent filtration gives H^0(RΓ A_L)=0. No degeneration assertion or new chain-map elimination is needed.

A projective CM lift would give F≅sigma*F⊗L with L^2≅O_X. If L is nontrivial the new vanishing excludes it; if L is trivial the imported untwisted Hom vanishing excludes it. An assumed self-twist similarly forces L^2≅O_X, and its nontrivial case is excluded by tau=id. This proves all three assertions.

