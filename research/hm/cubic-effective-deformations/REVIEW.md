# Independent mathematical review

Date: 2026-10-21 UTC.

Verdict: **PASS**, conditional on the pinned mathematical inputs. No substantive gap was found in effectivity, the uniform high-power embedding audit, formal faithfulness, or the application to the PR627 systems. One minor notation clarification was requested and incorporated before acceptance.

Reviewed artifact: `PROOF.md`.

Reviewed SHA-256: `4016af2001bb7c9952519007c82b7d9d71a296e6042185215e01e61aba0a3818`.

This is an independent human-readable mathematical audit, not proof-assistant verification. It does not establish the pinned inputs anew or certify their remote commit provenance. The local texts of the three named dependencies were inspected for consistency with the stated uses; the cited Stacks results were read directly.

## 1. Artin systems and properness

The convention A_n=C[[t]]/(t^(n+1)), beginning at n=0, is internally consistent. Compatibility means the specified reductions are cartesian, so X_0 is the base change of X_n along Spec C -> Spec A_n.

Each base inclusion is a finite-order thickening. [Stacks, Section 37.3, Lemma 37.3.3(7)](https://stacks.math.columbia.edu/tag/0CF2) therefore supplies properness of X_n from properness of V. The proof does not incorrectly assume properness merely from flatness. The stated finite-presentation hypothesis is sufficient throughout, and implies finite type over the Noetherian Artin bases.

## 2. Lifting the polarization

Flatness identifies the kernel of O_(X_(n+1)) -> O_(X_n) with

    O_V tensor_C (t^(n+1)A/t^(n+2)A).

It is annihilated by t and square-zero, including at n=0. This is the precise one-dimensional coefficient space needed in the obstruction argument. The original shorthand `(t^(n+1))` was potentially ambiguous as an ideal in A; the reviewed version now uses the quotient explicitly.

The multiplicative-to-additive identification of 1+J_n with J_n and the Picard obstruction in H^2(J_n) are valid. [Stacks, Section 37.4, Lemma 37.4.1](https://stacks.math.columbia.edu/tag/0C6Q) gives the required exact sequence. Since the underlying topological space is V and J_n is its structure sheaf up to the displayed one-dimensional factor, H^2(V,O_V)=0 ensures existence of a lift at every order. Choosing a reduction isomorphism at each successive stage gives the compatible polarized system. Nonvanishing H^1(O_V) affects uniqueness, not existence; the proof correctly does not claim uniqueness.

## 3. Effectivity and projectivity

[Stacks, Lemma 99.14.11, tag 0D4T](https://stacks.math.columbia.edu/tag/0D4T) applies directly. Its first ring and first scheme correspond to A_0 and X_0 here; all its successive kernels are nilpotent, its properness/flatness/finite-presentation hypotheses hold, and its first line bundle is ample. The inverse limit of these rings is A. The cited result supplies the algebraization, flatness, finite presentation, an ample line bundle, and the compatible reduction identifications, not merely an abstract formal object.

Properness plus an ample line bundle over the affine Noetherian base yields a projective morphism: a suitable power gives an immersion into finite-dimensional projective space, and properness makes it closed. No inference from generic-fiber projectivity is being used. [Stacks 089A](https://stacks.math.columbia.edu/tag/089A) is a valid secondary algebraization reference, while 0D4T is correctly chosen to obtain flatness explicitly.

## 4. One fixed high power and global sections

A single m can be chosen so that L_0^m is very ample and H^1(V,L_0^m)=0; [Stacks 0B5T](https://stacks.math.columbia.edu/tag/0B5T) supports the vanishing and the needed ample-power argument. Tensoring the flat structure-sheaf kernel sequence by the invertible sheaf gives exactly the displayed short exact sequence for every n.

The long exact sequences then give both H^1(X_n,L_n^m)=0 and surjectivity of the H^0 transitions. No H^2-vanishing for L_0^m is required for this step. One can lift a fixed ordered set of r sections successively, without assuming in advance that their lifts form bases. They generate each sheaf because their reductions generate L_0^m and t is nilpotent.

The later freeness argument is valid and avoids circularity. For n>=1, induction expresses the reduction of any section using the chosen sections. The difference lies in the copy of H^0(V,L_0^m) embedded by multiplication by t^n, which is spanned by t^n times those chosen sections. Thus A_n^r surjects onto H^0(X_n,L_n^m). Additivity in the short exact H^0 sequences gives complex dimension (n+1)r, proving the surjection is an isomorphism.

The compatible resulting maps f_n have a single fixed projective target dimension r-1. Each is proper because the target is separated over the base. Its topological fibers are those of f_0, hence finite; [Stacks 02OF, Lemma 30.21.1](https://stacks.math.columbia.edu/tag/02OF) makes it finite. On affine target opens, finite pushforward commutes with base change. The cokernel of the structure-algebra map vanishes modulo t and consequently vanishes by nilpotence. This proves a closed immersion, not merely a set-theoretic embedding.

The argument only lifts sections after passing to a sufficiently high power. It contains no unwarranted assertion that the original degree-one sections lift, nor that the original cubic embedding persists.

## 5. Proper formal faithfulness

The equalizer of f and g is a closed subscheme because Y is separated. X is Noetherian because it is proper over A, so its equalizer ideal I is coherent. Agreement on each infinitesimal reduction is precisely the containment I in t^(n+1)O_X for every n.

At a point of the special fiber, t is in the maximal ideal. [Krull intersection, Stacks 00IP](https://stacks.math.columbia.edu/tag/00IP) therefore forces I_x=0. The support of I is a closed subset of X, and can be endowed with a closed subscheme structure proper over A. Its image is closed. A nonempty such image in Spec A must contain the closed point, contrary to the support missing the entire special fiber. Hence I=0 and f=g.

The properness step is essential: checking stalks only at the special fiber would not otherwise control a subset confined to the generic fiber. The proof includes that step and is sound. It proves the asserted injectivity of Aut_A(X) into the inverse limit of the Artin automorphism groups; no surjectivity statement is needed.

## 6. Application and limits

The PR627 local text explicitly supplies compatible systems, trivial automorphism groups for every n>=1, and exclusion of the zero tangent vector from T_free. Its Artin rings C[t]/(t^(n+1)) identify canonically with the present A_n. Finite type over these Noetherian bases supplies finite presentation, so its systems meet the effectivity theorem's hypotheses.

Under the pinned inputs, each v in T_free thus yields a flat projective finite-presentation family over C[[t]] with trivial fixed-base automorphism group. Nonzero first-order class proves nonconstancy as a marked deformation. The argument does not infer uniqueness of the algebraization or of its polarization.

The scope warnings are correct and important. This audit accepts no conclusion about automorphisms of the generic or geometric generic fiber. It also accepts no claim of analytic convergence, descent to a finite-type C-curve, persistence of the original presentation, or resolution of the separate prescribed-source/full-adjoint/higher-lifting/Weil-class algebraicity questions.

## Final assessment

Accepted after the coefficient-space notation clarification. No further correction is required for the reviewed claims. No source-instance evaluations, selected coefficient/point/derivative/matrix computations, rank tests, or external writes were performed. File inspection, primary-source reading, and integrity hashing are the only non-mathematical audit operations.
