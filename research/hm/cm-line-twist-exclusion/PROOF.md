# Nontrivial line twists close the projective CM exclusion

## Hypotheses and precise contribution

Work over C with C: y²=x³−x, origin O, X=C⁴, N=⊠ O_C(O), and the elementary-symmetric x-coordinate morphism f:X→P⁴. Let H be the literal normalized rank-two HM bundle and E=N⊗f*H. Put τ(x_a,y_a)=(-x_a,i y_a) simultaneously on all four factors. Then τ*N≅N, fτ=Sf for S(v_j)=(-1)^j v_j (ordinary representatives j=0,…,4), and f*O(1)=N².

For every nontrivial P∈Pic⁰(X),

    Hom_X(E,τ*E⊗P)=0.

Together with the already established untwisted vanishing, this excludes both a global regular projective-bundle lift of τ and an O_X-algebra isomorphism End(E)≅End(τ*E). It does not exclude an isomorphism of the underlying End vector bundles without their multiplication.

## 1. Exact predecessors, not new coefficient claims

The [literal exact presentation](https://github.com/Akilleez-QA/read-em-and-weep/blob/8281ea90d8a1ffd14eaa10af76174b4c25a32742/research/hm/hm-presentation-independent/PROOF.md) supplies the complex L in degrees −1,0,1,2,

    5O(-1) → 15O → 10O(1) → 2O(2),

with sole locally free cohomology H. Its local splitting permits arbitrary pullback, so A=N⊗f*L has sole cohomology E and terms 5N⁻¹,15N,10N³,2N⁵.

The [unrestricted diagonal intertwiner classification](https://github.com/Akilleez-QA/read-em-and-weep/blob/97190240fa87b8ed68f2a90f701bda0e7236f0e7/research/hm/cubic-loci/foundation-p02/DIAGONAL.md), §§1–4, already excludes S: its normalized parameter a=s₁/s₀=-1 does not satisfy a⁵=1. No invertibility of the intertwiner blocks is assumed. The [global degree-gap Hom proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/4659e4425c6b5ab6b1899e6af93656ac03ff0862/research/hm/null-cm-global-hom/PROOF.md), §§3–5, supplies the passage from constant first-block obstruction to ordinary global Hom vanishing. For this same literal presentation, use the structural exactness above instead of that older proof's historical A premise, and use the diagonal classification instead of its computed rank premise. Thus Hom_X(E,τ*E)=0. This packet does not re-prove or re-publish those arguments, and does not authenticate prescribed rational contractions.

## 2. Full nontrivial-twist argument

Pic⁰(C⁴) is the product of the four Pic⁰(C)'s: analytically this follows by the product decompositions of H¹(O) and H¹(Z) in the exponential sequence. Hence P=⊠ P_a with degree-zero P_a, and at least one P_a is nontrivial. On an elliptic curve a nontrivial degree-zero line has H⁰=0 (a nonzero section would trivialize it) and H¹=0 by Serre duality. Therefore H*(X,P)=0 by Künneth.

The internal Hom complex B=Hom•(A,τ*A⊗P) computes derived Hom from E to τ*E⊗P. Each degree-r term is a sum of N^(2r)⊗P, with -3≤r≤3. For r>0 every elliptic factor has positive degree and cohomology only in degree zero; for r<0 every factor has negative degree and cohomology only in degree one. Künneth therefore puts their product cohomology in q=0 and q=4 respectively. For r=0 it vanishes altogether.

In the bounded spectral sequence E₁^(r,q)=H^q(X,B^r), no entry has total degree zero: positive r contributes total degree r≥1, negative r contributes r+4≥1, and r=0 is acyclic. Consequently its abutment in total degree zero vanishes. This proves the displayed Hom vanishing for every nontrivial P∈Pic⁰(X), not just one chosen twist.

## 3. Why this covers all determinant-compatible twists

Every two-torsion line on X lies in Pic⁰(X). Indeed its first Chern class is torsion, whereas H²(C⁴,Z) is torsion-free (the integral cohomology is the exterior algebra on the free lattice H¹). Thus c₁(P)=0 and the exponential sequence gives P∈Pic⁰(X). [GAGA](https://www.numdam.org/item/AIF_1956__6__1_0/) identifies the holomorphic and algebraic line bundles and morphisms here.

The determinant of the normalized presentation is det H=O(-1): the alternating determinant of its terms is O(5+0-10+4). Since E has rank two and f*O(1)=N², det E=N²⊗f*O(-1)=O_X. The same holds for τ*E.

For rank-two bundles E,F an O_X-algebra isomorphism End(E)≅End(F) makes F a module over End(E). Locally matrix units split F into two isomorphic summands of rank one. Thus P=Hom_End(E)(E,F) is a line bundle and evaluation E⊗P→F is an isomorphism; these constructions glue. With F=τ*E, taking determinants yields P²≅O_X. If P is trivial the isomorphism contradicts ordinary Hom vanishing. If not, its equivalent isomorphism E→F⊗P⁻¹ contradicts §2 because P⁻¹ is a nontrivial member of Pic⁰(X). This proves the algebra-bundle exclusion.

A projective-bundle isomorphism P(E)≅P(F) over X yields the associated matrix-algebra isomorphism: locally projective transitions act on Mat₂ by conjugation, independently of scalar representatives. Equivalently, projectivizations are isomorphic precisely when F≅E⊗P for a line P. The same determinant and twisted-Hom argument therefore excludes the projective lift. A proposed lift over Q(i) would extend to C, so nonexistence also holds over Q(i).

## 4. Boundaries

This result concerns global regular lifts of the stipulated carrier and simultaneous τ only. It makes no assertion about meromorphic or nongluing local maps, the full global normalizer, selected-source covariance, higher-order responses, algebraicity of a retained scalar, or accidental scalar covariance. Ordinary Hom vanishing alone would not imply the projective conclusion; the proof of every nontrivial determinant-compatible twist in §§2–3 is essential.
