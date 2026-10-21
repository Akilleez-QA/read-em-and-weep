# Cubic separation and a degree-nine normalization-defect bound

## Status and scope

Authored structural proof, independently reviewed; see REVIEW.md. No selected Horrocks–Mumford matrix, coefficient, or rank evaluation is used. The result concerns the actual primary evaluation surface S and its smooth normalization X, not the primary-bad parameter scheme, the full adjoint map, or algebraicity of a lift.

## Established inputs

Use PR574 at 3c92fdc469f6870520e7a9d905b5ab9199a5bf37 for the normalization sequence

0 → O_S → ν_*O_X → T → 0,

where T has length 30, supported at the distinct transverse double points Z. Its stalk at each point is the one-dimensional difference of the two normalization branches. Let H=ν^*O_S(1). Established modular geometry gives

H=I+2F, K_X=3F, C=5I,
I²=-5, I·F=5, F²=0.

Here C is the union of 25 distinguished sections, each of square -5, and each component of each singular I5 fiber meets five of these sections. The sections are pairwise disjoint: C²=-125 equals the sum of their self-intersections, so the sum of nonnegative pairwise intersection numbers is zero.

Use null's PR543 commits 93dffb999a3b1bb32e7cb8361980919580d4ec63 and 7f901e5a11fbfe994a77a3f08c580789f4b1dfdd for H¹(X,nH)=0 for n≥1 and the H5 linearizations. For a direct source check, Barth–Hulek–Moore, printed pp. 60–61, gives the primitive commutator action on O(I) and the trivial lift on O(F); printed p. 63 identifies H⁰(H) equivariantly with V*. Source: https://mathweb.tifr.res.in/Documents/Publications/Studies/Vector-Bundles-On-Algebraic-Varieties.pdf . Thus the center acts on H with a primitive fifth-root character, and acts trivially on X. The normalization exact sequence and its twists are equivariant. Consequently every image of the difference map

ρ_n: H⁰(X,nH) → H⁰(T(n))

has dimension divisible by 5 when 5 does not divide n. This is the usual finite Heisenberg representation fact: every irreducible representation with nontrivial central character has dimension 5.

## 1. A new geometric separation statement

**Theorem 1.** The complete linear system |3H| is very ample on X.

Set N=I+F. It is nef and N²=5. Indeed, each distinguished section has intersection zero with N. For an irreducible curve D not among these sections, I·D=C·D/5≥0 and F·D≥0. If N·D=0, then both intersections vanish; F·D=0 makes D vertical, but every fiber component meets C positively. Thus the only N-null curves are the 25 sections.

Apply Reider's theorem to L=3N. It has L²=45 and K_X+L=3H. Failure of base-point-freeness or length-two separation would give an effective nonzero divisor D with either L·D equal to 1 or 2, or L·D=0 and D²=-1 or -2. The positive intersections are impossible because L is divisible by 3. In the zero case, nefness forces every component of D to be N-null. Thus D=Σm_i C_i and

D²=-5Σm_i²,

which is neither -1 nor -2. All Reider exceptions are excluded. This proves the theorem, including tangent-vector separation.

Reference: Robert Lazarsfeld, *Lectures on Linear Series*, Theorem 2.1, printed p. 7 (PDF page 7, zero-based page 6): https://www.math.stonybrook.edu/~roblaz/Reprints/Lazarsfeld.LLS.pdf . The degree-nine exceptional boundary version of Reider is irrelevant because L²=45.

**Corollary.** For every node z in Z, projection of im(ρ_3) onto T_z is nonzero.

Indeed, very ampleness supplies a cubic section which vanishes at one of the two distinct points over z and not at the other. Its difference is nonzero independently of choices of branch-fiber trivializations.

## 2. A strict-growth lemma for the actual gluing defect

**Lemma 2.** Put r_n=rank(ρ_n). For n≥3, if r_n<30, then r_(n+1)>r_n.

Choose an ambient linear form ℓ nonzero at all 30 nodes. Multiplication by ℓ identifies all H⁰(T(n)) with the same 30-dimensional vector space V. Write V_n for the image of ρ_n after this identification. Multiplication of normalization sections by ambient coordinates gives

V_n ⊆ V_(n+1), and (x_i/ℓ)V_n ⊆ V_(n+1).

Suppose dim V_n=dim V_(n+1). Then V_n=V_(n+1) and V_n is invariant under all diagonal operators x_i/ℓ. Since the 30 support points are distinct in the affine chart ℓ≠0, these functions generate the full function algebra C^30 on Z. For completeness, for each ordered pair z≠w choose an affine linear function which vanishes at w and not z; multiplying such functions and normalizing constructs the characteristic idempotent of z. Thus V_n is invariant under every coordinate projector of V.

The preceding corollary and multiplication by ℓ^(n-3) show that V_n projects nontrivially onto every coordinate. Applying the coordinate projectors then places every coordinate axis in V_n, so V_n=V. This contradicts r_n<30 and proves the lemma.

This argument uses the actual branch-difference gluing and the distinct node support; it is not an abstract dimension count in the normalization section ring. It also proves that once rank 30 is reached, it remains 30 in every later degree.

## 3. Finite vanishing, with explicit intermediate bounds

**Theorem 3.** The actual primary surface satisfies H¹(S,O_S(n))=0 for every n≥9.

The cubic separation corollary gives r_3>0. Heisenberg divisibility and strict growth give successively

r_3≥5,
r_4≥10,
r_5≥11,
r_6≥15,
r_7≥20,
r_8≥25,
r_9=30.

In detail, at each stage rank 30 is already sufficient and persists. Otherwise Lemma 2 supplies strict growth, and at degrees 3,4,6,7,8,9 the next permitted rank is a multiple of 5. At degree 5 no divisibility is asserted.

The normalization long exact sequence and H¹(X,nH)=0 identify H¹(S,O_S(n)) with coker(ρ_n) for n≥1. Hence the corresponding upper bounds in degrees 3 through 9 are

25, 20, 19, 15, 10, 5, 0.

Together with the previously proved lower bounds in degrees 3,4,5 this yields

15≤h¹(O_S(3))≤25,
5≤h¹(O_S(4))≤20,
1≤h¹(O_S(5))≤19.

No exact low-degree rank is claimed. In particular the theorem does not establish projective normality, generation of the saturated ideal in degree six, or vanishing of H¹(P⁴,I_S(n)).

## 4. Next useful consequence: the sheaf regularity bottleneck is isolated

For n≥9, the normalization and its quotient have no positive-degree cohomological defect: H¹(O_S(n))=0, and H²(O_S(n))=H²(X,nH)=0. Thus O_S is 10-regular on P⁴: the required groups are H¹(O_S(9)) and H²(O_S(8)), and cohomology above degree 2 vanishes by dimension. Consequently multiplication

H⁰(O_S(n)) ⊗ H⁰(P⁴,O(1)) → H⁰(O_S(n+1))

is surjective for n≥10 by Castelnuovo–Mumford regularity. This is a finite-generation bound for the complete section module, not a claim that ambient polynomials already give all sections. The remaining projective-normality question is separately H¹(I_S(n)); regularity of O_S alone does not solve it.

The bound is structural and likely non-sharp. Exact ranks in degrees 2–8 still require additional information about the actual gluing map or its representations; the proof does not conceal that missing input.
