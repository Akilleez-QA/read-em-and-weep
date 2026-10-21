# Smooth high-power Hilbert germs and all abstract deformation directions

Work over C. Let V=V51 and L0=O_V(1), the polarization of its cubic embedding in P9. The assertion below concerns the same abstract fourfold with a sufficiently high complete-power embedding, not the original primary surface or the full-adjoint problem.

## Pinned inputs

All numbered PRs are in https://github.com/Akilleez-QA/read-em-and-weep.

- PR611, commit 12b28d33627cc0e8b283d142dc16439a51bb5e00: V is integral and projective, h0(O_V)=1, h1(O_V)=60, and H2(O_V)=0. Its Hilbert polynomial for L0 is P_V(t)=binom(3t+4,4)-30 binom(t+3,4)-60.
- PR614, commit 73fbf75838c91804ca637b5916d6aac217240958: all abstract local-Artin deformations of V are locally trivial and lift across small extensions; H0(Theta_V)=0 and h1(Theta_V)=576. This is an explicit local-gluing unobstructedness theorem, not a claim that global cotangent Ext2 vanishes.
- PR615, commit 24bc9b741c287f8ac207bd9df4de4c07c50bea2f: the sheaf of first-order differential operators on a line bundle has symbol sequence 0 -> O_V -> A_M -> Theta_V -> 0. The local-gluing interpretation of H1(A_M) and the line-bundle lifting argument apply to any line bundle M.
- PR622, commit c6a7c691f8ecd8562505546f993c755fb03b24fb: the original P9 Hilbert germ is smooth of dimension 99, consisting locally only of projective-coordinate motion.
- PR628, commit f08ff9c2760e4aef074cfe716b923d29d5e7ebe8, and PR629, commit 3ad872801158107d8fa71fa578f2ea948efd9f25: effectivity and finite-jet curve realization establish related but different conclusions.
- PR630, commit 8024882d2129142fece5dbaf83b49e5f8e3817ca: finite polarized jets can retain L0 itself on an algebraic curve; nonzero abstract first-order motion then forces generic h0(L)<=9.

## 1. Statement

Choose m sufficiently large that M0=L0^m is very ample and H1(V,M0)=0. Serre vanishing supplies such m, and one may choose m large enough that all higher cohomology vanishes as well. Set n=h0(V,M0), and embed V by a fixed ordered basis of its complete system into P^(n-1). Let h_m denote its point in the Hilbert scheme of that projective space.

Theorem. The Hilbert scheme is smooth at h_m and has local dimension

    n^2+635.

Its completed local ring is noncanonically a formal power-series ring over C in n^2+635 variables. For m in the stated eventual range, n=P_V(m).

More precisely, on marked local-Artin deformation functors, forgetting the embedding and then the line bundle gives formally smooth maps

    Def_emb,m -> Def_(V,M0) -> Def_V.

Their relative tangent dimensions are respectively n^2-1 and 60. Consequently Def_emb,m -> Def_V is formally smooth with relative tangent dimension n^2+59, and its tangent map surjects onto all 576 abstract directions. These are functorial lifting assertions; no representability of Def_V or Def_(V,M0) is assumed.

## 2. Line bundles lift with the prescribed abstract lift

Let A' -> A be a small extension of local Artin C-algebras, with residue field C and kernel J annihilated by the maximal ideal of A'. Given a flat abstract lift X' of an A-deformation X and a line bundle M on X, the units sequence has kernel

    1+J O_(X') = J tensor_C O_V

additively. Flatness justifies this identification. The obstruction to extending M is in H2(O_V) tensor J, which is zero. Thus M lifts on the given X', not merely on some replacement abstract lift. This proves formal smoothness of the second forgetful map. Ampleness persists through nilpotent thickenings.

For the tangent calculation, local triviality of abstract deformations and local triviality of line bundles identify first-order pair classes with H1(A_(M0)). The symbol sequence and H0(Theta_V)=H2(O_V)=0 give

    0 -> H1(O_V) -> T_pair,m -> H1(Theta_V) -> 0.

Hence dim T_pair,m=60+576=636, independently of m. This is a sequence of tangent spaces of isomorphism classes with a fixed special-fiber marking. Scalar line-bundle automorphisms are not discarded from the category, but act trivially on this H1 classification. The relative tangent space over the constant abstract deformation is exactly H1(O_V), of dimension 60.

Combining the prescribed-lift assertion with PR614 shows that the pair functor itself is formally unobstructed.

## 3. High-power sections and embeddings lift

For every Artin pair deformation (X_A,M_A) of (V,M0), one has

    H1(X_A,M_A)=0,       H0(X_A,M_A) is free of rank n over A.

Prove this by induction through small extensions. The short exact sequence for a small step is

    0 -> M0 tensor_C J -> M_(A') -> M_A -> 0.

It makes H0 restriction surjective and proves H1 vanishing from H1(M0)=H1(M_A)=0. Lift a basis over A to n sections over A'. Nakayama makes their map (A')^n -> H0(M_(A')) surjective. Exactness above shows that both modules have C-length n*length(A'); therefore the map is an isomorphism. This proves freeness without assuming base change in advance. The induction starts with M0.

Now consider a lifting diagram for Def_emb,m -> Def_(V,M0): an embedded A-deformation is given, together with a pair lift over A' and an identification of its reduction with the underlying pair over A. Its n ambient coordinate sections form an A-basis of H0(M_A): they reduce to the fixed complete basis, and the preceding freeness and Nakayama prove the assertion. Lift them to an A'-basis. Their evaluation generates M_(A') because it does so on V and the base ideal is nilpotent. Thus they define a morphism

    X_(A') -> P^(n-1)_(A')

restricting to the given embedding over A.

This morphism is a closed immersion. It is proper, since X_(A') is proper and its target is separated; properness of the Artin deformation follows from properness of its special fiber across nilpotent thickenings. It is quasi-finite because its underlying-point fibers are those of the special-fiber closed immersion. Proper quasi-finite therefore implies finite. The cokernel of O_(P^(n-1)) -> g_*O_(X_(A')) vanishes on the special fiber, so nilpotent Nakayama makes it zero. Finite pushforward commutes with this base change. Hence g is a closed immersion. Flatness over A' makes its image a Hilbert-scheme deformation with the required Hilbert polynomial.

This proves formal smoothness of Def_emb,m -> Def_(V,M0), including compatibility with a specified embedding over A.

## 4. Exact tangent dimension and smoothness

For a fixed first-order pair class, lifts of its fixed central ordered basis form a torsor under

    Hom_C(H0(M0),H0(M0)), dimension n^2.

Two such basis lifts determine the same marked embedded deformation precisely when related by a first-order automorphism of the pair reducing to the identity. An identity-reducing scheme automorphism would be a vector field on V, hence is zero by H0(Theta_V)=0. Remaining automorphisms are scalar line-bundle multiplications 1+epsilon c, since H0(O_V)=C. They identify precisely the one-dimensional common-scalar basis direction. Thus the tangent sequence is

    0 -> pgl_n -> T_(h_m)Hilb -> T_pair,m -> 0,

and dim T_(h_m)Hilb=(n^2-1)+636=n^2+635.

Equivalently, the kernel here is the infinitesimal projective-coordinate action. There is no extra infinitesimal stabilizer: an ambient vector field stabilizing V restricts to a vector field on V; if that restriction is zero, its matrix has every point of V as an eigenline. The integral nondegenerate V then lies in a single projectivized eigenspace, forcing the matrix to be scalar. This also verifies directly that the pgl_n arrow is injective.

Sections 2 and 3 lift every embedded deformation across every small Artin extension, since PR614 first supplies the abstract lift. The Hilbert scheme is of finite type over C. The infinitesimal local smoothness criterion therefore makes it smooth at h_m; its local dimension equals its computed tangent dimension. One precise reference is [Stacks, Lemma 37.12.1](https://stacks.math.columbia.edu/tag/02HX), the pointwise small-extension criterion over a locally Noetherian base. Smoothness at a C-point gives the stated noncanonical power-series completion.

The proof does not infer unobstructedness from a tangent dimension alone and does not assert H1 of a normal sheaf or global cotangent Ext2 vanishing.

## 5. Consequence: what changing the embedding actually restores

Composing the two formally smooth forgetful maps proves that every abstract Artin deformation of V can be equipped with an embedding lifting this high-power embedding. More generally, a specified high-power embedding over A can be continued over any prescribed abstract lift over A'. Its relative tangent kernel fits into

    0 -> pgl_n -> ker(T_(h_m)Hilb -> T1(V)) -> H1(O_V) -> 0,

of dimension n^2+59. This records the n^2-1 coordinate directions and 60 polarization directions without claiming a canonical splitting.

The PGL_n orbit has dimension n^2-1, so its tangent normal quotient at h_m has dimension 636. Unlike the original P9 orbit, it is not open in this high-power Hilbert germ. The 636 transverse tangent directions consist of 576 abstract and 60 line-bundle directions through the preceding exact sequences. The assertion is local and infinitesimal; no geometric quotient or moduli-space dimension is asserted merely by subtracting dimensions.

There is no contradiction with PR622 or PR630. In degree one H1(L0)=65, and the ten-section obstruction forces the P9 germ to have only coordinate motion. In the high-power range H1(M0)=0 removes that section-lifting obstruction at every Artin step. These are distinct Hilbert problems for the same abstract V.

## Boundaries

No effective numerical threshold m is computed. No selected HM/source coefficients, points, matrices, derivatives or ranks are evaluated, and no large computation occurs. No generic-fiber automorphism, global Hilbert component classification, entire formal-arc descent, original full-adjoint repair, prescribed-source membership, higher quantization or Weil-class algebraicity conclusion is made. This is an authored mathematical argument conditional on the pinned inputs, not a proof-assistant verification.
