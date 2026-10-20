# Independent audit of the triple-component primary reduction

## Verdict

**Pass.** The proof's ordered Koszul maps, cochain signs, finite primary/secondary reduction, quartic cofactor factorization, and canonical residual quotient are correct under the imported geometric and cohomological inputs. No correction is required. In particular, the new conclusion is genuinely

    ker P ⊂ ker α,

not merely ker σ ⊂ ker α. The residual lower bound is correctly an aggregate bound across the existing three residual layers; it is not assigned to an individual layer without additional hypotheses.

This audit independently checked the arguments in PROOF.md against the dependency proofs named below. It did not evaluate a cofactor, source, multiplication matrix, rank instance, actual splitting branch, or obstruction value.

## 1. Degrees, exactness, and duality

For the regular sequence of degrees (2,3), twisting the Koszul resolution by B(1) and choosing the displayed order gives

    0 → B(-4) --(t₂,-t₃)→ B(-2) ⊕ B(-1)
      --(t₃,t₂)→ I_N B(1) → 0.

All four multiplication degrees agree with their source and target twists; the composite is t₃t₂−t₂t₃=0. The alternative order of the two middle summands compared with the usual Koszul presentation causes no issue. The restriction sequence with B_N(1) is exact because B is locally free.

The component transpose has precisely the claimed source and target. Adjunction for the (2,3) complete-intersection surface gives ω_N≅O_N, so

    H²(N,B_N(-1))∨ ≅ H⁰(N,B_N(1)),
    H²(Y,B(-1))∨ ≅ H²(Y,B(-4)).

Compatibility with the Koszul fundamental class identifies the transpose with the two connecting maps, up to the conventional overall orientation sign. The proof explicitly fixes that orientation and only uses its image and ranks, which are unaffected. There is no unnoticed twist by the ambient canonical bundle in the component source.

The negative-twist inputs give H¹(B(-4))=H¹(B(-2))=0, h¹(B(-1))=5, h²(B(-2))=20, and h²(B(-1))=10. For an independent numerical consistency check, the stated Riemann–Roch polynomial at −2 gives χ(B(-2))=20; negative H⁰ and the negative H¹ table and their Serre duals eliminate all other cohomology there. At −1 it gives χ=5 and h¹=5, hence h²=10. Thus the primary map is correctly 10→30.

The endpoint estimate is used with its proper scope: h²(B(1))≤30 does not become a vanishing claim. At twist 1, χ=-55 and H³=H⁴=0 give h¹(B(1))=55+h⁰(B(1))+h²(B(1)). Therefore the secondary target has dimension at least 55−5=50, without providing any positive lower bound on the secondary rank.

## 2. The exact primary/secondary reduction

Writing K=I_NB(1), the first long exact sequence and H¹(B(-4))=0 give exactly

    0 → H¹(L) → H¹(K) --b→ ker P → 0.

For a lift y of x∈ker P, changing y changes its image in H¹(B(1)) by precisely the image of H¹(L). Hence σ has the stated quotient target and is well-defined. The equation σ(x)=0 is equivalent to adjusting y into the kernel of H¹(K)→H¹(B(1)); by the restriction sequence this is equivalent to y coming from a section of B_N(1). Consequently

    im δ′ = ker σ,
    rank r_N = 10−rank P−rank σ.

There is no unstated surjectivity onto the full secondary target.

The cochain formula has the correct positive sign. From dℓ=u x one obtains d(vℓ)=0, and the positive boundary of [vℓ] is [x]. If σ(x)=0, choosing closed z and h with v(ℓ−z)=dh gives a global h|N whose two positive boundaries are [v(ℓ−z)] and [x]. Replacing x by x+dk and ℓ by ℓ+uk preserves the value, and replacing ℓ by a closed cochain changes the value only by im m. These are exactly the required primitive ambiguities.

The global-section formula is also correct. Negative H⁰ and H¹(B(-4))=0 imply H⁰(K)=0. The kernel of the map from the first restriction boundary to D has dimension dim ker m=5−a. Therefore

    h⁰(N,B_N(1)) = h⁰(B(1))+(5−a)+(10−p−s),
    dim ker δ′ = h⁰(B(1))+5−a.

By finite-dimensional duality, this last quantity is dim coker r_N, as claimed.

## 3. Quartic cofactor factorization

The scheme inclusion N⊂Z implies I_Z⊂I_N, so each quartic cofactor is a section of I_N(4). The degree-four Koszul presentation is

    0 → O(-1) → O(2) ⊕ O(1) → I_N(4) → 0.

Both H⁰(O(-1)) and H¹(O(-1)) vanish on P⁴. Thus every j_i has a unique expression

    j_i=t₂a_i+t₃b_i,  a_i∈H⁰(O(2)), b_i∈H⁰(O(1)),

relative to the fixed generators t₂,t₃. The map f(a,b)_i=a_i a−b_i b is a genuine sheaf map B(-2)⊕B(-1)→5B, and

    f(u(x))_i=a_i t₂x−b_i(-t₃x)=j_i x.

Thus α=FP holds exactly with the proof's signs. It immediately implies V⊂ker α. Restricting P gives a surjection ker α→ker(F|im P), with kernel V, proving the stated short exact sequence and the formulas

    dim ker α=10−p+q,  rank α=p−q.

In particular, injectivity of σ on V cannot substitute for injectivity of P. This conclusion uses actual ideal membership, not an inference from the secondary map alone.

## 4. Canonical residual quotient and the lower bound

The component-gluing filtration identifies D+U with the image of r_comp∨ inside ker α. More explicitly, if J=im α* and A₁=ker r_comp, then

    ker α=J⊥,  D+U=A₁⊥,
    ker α/(D+U) ≅ (A₁/J)∨.

The existing filtration of A₁/J therefore gives its dimension as g+n+ℓ. This does not require a splitting of the filtration or extension of individual restricted detectors to all of T.

Since U⊂ker α, P(U)⊂ker F_P. On the quotient ker α/(D+U), P induces a surjection onto ker F_P/P(U). Its kernel is

    (V+U)/(D+U) ≅ V/(D+U₀),  U₀=U∩V.

Since D=ker σ, the first isomorphism theorem identifies this canonically with im σ/σ(U₀). Equivalently, the injection sends σ(v) modulo σ(U₀) to v modulo D+U; changes of preimage differ by D, and changes by σ(U₀) differ by U₀. Hence the entire sequence (★) is well-defined and exact, without a choice of splitting.

Dimension bookkeeping gives

    dim U₀=w−e,
    dim(U₀∩D)=i,
    v₀=dim σ(U₀)=w−e−i.

In particular 0≤v₀≤min(s,w)≤min(s,3), and 0≤e≤q. Taking dimensions in (★) gives

    g+n+ℓ=(s−v₀)+(q−e)≥s−v₀≥max(0,s−3).

Both nonnegative summands and the final maximum are justified. The formula for rank r_comp is also correct:

    dim(D+U)=10−p−s+w−i.

All four stated consequences follow. Residual vanishing is equivalent to im σ=σ(U₀) and ker F_P=P(U); when r_W=0 the residual dimension is s+q; and only after g=ℓ=0 may the lower bound be assigned to the nilpotent gluing rank alone.

## 5. Scope and distinction from the older criterion

The older fourth-power criterion uses B_N(4), target H²(B(-1)), middle sheaves B(2)⊕B(1), and secondary target involving H¹(B(4)). The present component transpose uses B_N(1), target H²(B(-4)), and middle sheaves B(-2)⊕B(-1). Equal target dimensions do not identify these constructions.

The proof correctly combines two independent inputs absent from a bare secondary-map criterion: quartic membership in I_N and the bound dim U≤3. It makes no claim that the ≥50-dimensional target forces σ nonzero, and no claim that any actual cofactor or residual rank has been determined.

## Dependencies read

- PROOF.md in this directory.
- ../component-gluing-detector/PROOF.md.
- https://github.com/Akilleez-QA/read-em-and-weep/blob/21b252420c0011b2cbc119cab2983a6d4ad2e966/research/conductor-normalization/simple-pole-cofactor-comparison/PROOF.md.
- https://github.com/Akilleez-QA/read-em-and-weep/blob/f3f85ffc04213778c8c4fbd60e1e7e04b56cfd65/research/conductor-normalization/fourth-power-cohomology/PROOF.md.
- https://github.com/Akilleez-QA/read-em-and-weep/blob/1d60973dd27a921a43bf6d9e71a06caa0cca0350/research/conductor-prerequisites/degree-one-kernel-exclusion/PROOF.md.
- https://github.com/Akilleez-QA/read-em-and-weep/blob/063da90fc4543304e87e701cdefcc08225412f17/research/conductor-normalization/sharper-hm-regularity/SHARPEST-BOUND.md.

The imported primary cohomology and geometric statements were checked for consistency and correct application through these proofs; this audit does not claim a fresh inspection of their external primary-source scans.

## Status of this record

This is a historical mathematical audit, not a new formal verification or a new execution of tests.
