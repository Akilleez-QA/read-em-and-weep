# Heisenberg stabilizers and generic obstructions at the HM vertex

## Result and imported inputs

Work over C. Let V be the five-dimensional Schrödinger representation of H₅, S₅=Sym⁵V*, and U the two-dimensional HM space. Import the audited pairing, restriction, and orbit results in

- ../apolar-middle-module/{PROOF,AUDIT}.md;
- ../quintic-restriction-jump-loci/{PROOF,AUDIT,NONZERO-COROLLARY,NONZERO-COROLLARY-AUDIT}.md;
- ../jump-obstruction-pairing/{PROOF,AUDIT}.md.

In particular Ψ:S₅→Sym²U* is surjective, Φ=cΨ with c≠0, and

    K=ker Ψ, dim K=123,
    T=im Ψ* = K⊥ ⊂ (S₅*)^{H₅}, dim T=3.

Here T is the net of quintic FUNCTIONALS, not the two-dimensional cohomology space denoted T in some earlier files. Smooth quintics form a nonempty open subset Ω∩P(K). For p∈K define

    L_p:sl(V)→Sym²U*,  v↦Φ(v·p),
    (g·p)(w)=p(g⁻¹w).

We prove:

1. Every nonzero H₅-fixed q∈S₅* has infinitesimal stabilizer in sl(V) of dimension at most four. Thus dim(sl(V)·q)≥20.
2. The locus in P(K) where L_p is not surjective is closed and has codimension at least 18. The locus where im L_p has a common zero in P(U) is closed and has codimension at least 19.
3. Consequently a nonempty open dense subset of the smooth-quintic vertex has surjective L_p. At each such point, the ordinary bundle-deformation hull on the fixed quintic has dimension 24 and embedding dimension 26. It is singular and actually obstructed.
4. Wherever L_p is surjective, all primary obstructions admit the exact normal form in Section 6: their degree-two equations span a five-dimensional space, independent of the formerly undetermined normal cubic after a tangent-coordinate change.

The same hull conclusion holds outside the potentially smaller common-zero locus. These are generic, not pointwise-universal, results. No selected polynomial, HM/source/cofactor matrix, or rank instance is evaluated.

## 1. Universal Heisenberg weight matrices

Fix a primitive fifth root ζ. In the Schrödinger model, with indices j∈F₅, choose the standard generators

    X e_j=e_(j+1),  Z e_j=ζ^j e_j,  ZX=ζXZ.

For a=(r,s)∈F₅² set E_a=X^r Z^s. Conjugation by X and Z gives respective eigenvalues ζ^(−s) and ζ^r. Thus these 25 matrices have distinct characters for the conjugation action of H₅/Z(H₅)≅F₅²; they form a basis of End(V). The matrix E_0 is the identity, and each E_a with a≠0 has trace zero: for r≠0 it has zero diagonal; for r=0,s≠0 its trace is the sum of all fifth roots with a nonzero exponent. Therefore

    sl(V)=⊕_(a≠0) C E_a,

with all 24 nontrivial characters, each once. In particular there is no trivial character.

Multiplication and the bracket satisfy

    E_(r,s) E_(r',s')=ζ^(sr') E_(r+r',s+s'),
    [E_a,E_b]=(ζ^(sr')−ζ^(s'r)) E_(a+b).

The coefficient is nonzero exactly when det(a,b)=rs'−sr'≠0 in F₅. In that event a+b≠0. Consequently any H₅-stable Lie subalgebra of sl(V) is the direct sum of a subset of these weight lines, and its support is closed under addition of two supported vectors whose determinant is nonzero. The direct-sum assertion follows from the character projections for the finite abelian conjugation group, over characteristic zero.

## 2. Two independent supported weights generate all 24

Let Σ⊂F₅²\{0} be closed under the above nonorthogonal additions. Suppose it contains independent a,b. We show Σ=F₅²\{0} without enumeration.

First, b+ka belongs to Σ for every k∈F₅: starting with b, repeatedly add a. Each addition is allowed because det(a,b+ka)=det(a,b)≠0. The five successive additions traverse all k modulo five.

Inductively suppose all (m−1)b+ja lie in Σ, where m=2,3,4, and j ranges over F₅. Fix k∈F₅. Choose i∈F₅ such that mi−k≠0; this is possible because m≠0. Put j=k−i. The vectors b+ia and (m−1)b+ja are already supported, their sum is mb+ka, and their determinant is

    (mi−k) det(a,b),

which is nonzero. Hence every mb+ka is supported for m=1,2,3,4 and all k.

Finally, for k≠0 choose any i and put j=k−i. The supported vectors b+ia and 4b+ja sum to ka, and their determinant is

    (4i−j) det(a,b)=−k det(a,b)≠0.

All four nonzero multiples of a are therefore supported as well. These 20 vectors with nonzero b coefficient and four vectors with zero b coefficient exhaust F₅²\{0}.

It follows that every proper H₅-stable Lie subalgebra of sl(V) has support contained in a single one-dimensional F₅-subspace, and thus has complex dimension at most four. Such a subalgebra is abelian since every pair of its supported weights has determinant zero. We need only the dimension bound, not existence or classification of stabilizers of each size.

## 3. Stabilizer bound for every nonzero invariant functional

Let 0≠q∈(S₅*)^{H₅}, and define

    h_q={v∈sl(V):v·q=0}.

This is a Lie subalgebra because the action is a representation. It is H₅-stable: (Ad h v)·q=h·(v·q) for h∈H₅, since h fixes q. It is proper. Indeed if all of sl(V) killed q, q would be fixed by the connected group SL(V), whereas S₅*=Sym⁵V is the nontrivial irreducible representation of highest weight 5ω₁ and has no fixed vector. This uses only the standard symmetric-power representation, not any special quintic evaluation.

Section 2 gives dim h_q≤4, whence

    D_q:=sl(V)·q has dimension 24−dim h_q≥20.       (1)

There is a useful stronger fact than a crude quotient dimension estimate. The map

    sl(V)→S₅*,  v↦v·q

is H₅-equivariant. Since its source contains only nontrivial conjugation characters, its image D_q contains only nontrivial characters as well. But T consists entirely of trivial characters. Consequently

    D_q∩T=0.                                      (2)

This holds for every nonzero invariant q, whether or not q lies in T.

## 4. Restricted derivative duality and incidence bounds

For 0≠q∈T define

    A_q:K→sl(V)*,  A_q(p)(v)=q(v·p).

The contragredient infinitesimal action is

    (v·q)(p)=−q(v·p).

Thus the transpose of A_q is the map v↦−(v·q)|_K. Restriction S₅*→K* has kernel K⊥=T, so (2) implies it is injective on D_q. Therefore

    rank A_q=dim D_q≥20,   dim ker A_q≤103.         (3)

No equivariance of Ψ under the whole SL(V) is claimed or needed: only its H₅-equivariance and the usual SL(V) action on S₅ enter this computation.

Identify P(T) with P(Sym²U) via the injective Ψ*. The projective incidence

    I={( [p],[q])∈P(K)×P(T):q(v·p)=0 for all v∈sl(V)}

is closed: for a basis of sl(V), its equations are bilinear in p and q. Its fiber over [q] is P(ker A_q), of dimension at most 102 by (3). Hence dim I≤102+2=104. Projection to P(K) is proper because P(T) is projective, so its image B is closed and has dimension at most 104. Since dim P(K)=122,

    codim_(P(K)) B≥18.                            (4)

For p∈K, the map L_p is not surjective exactly when a nonzero α∈(Sym²U*)*=Sym²U annihilates it. With q=Ψ*(α),

    α(L_p(v))=c q(v·p).

The scalar c≠0, so this is exactly the incidence condition. Thus B is precisely the nonsurjectivity locus, not just a containing set.

Similarly consider the Veronese conic

    C={ [Ψ*(u²)] : [u]∈P(U)} ⊂ P(T).

Every displayed q is nonzero because Ψ* is injective. Restricting I to P(K)×C gives a closed incidence of dimension at most 102+1=103. Its closed image B₀⊂P(K) therefore has codimension at least 19. The condition defining B₀ is exactly

    there exists [u]∈P(U) with Φ(v·p)(u,u)=0
    for every v∈sl(V),

that is, the binary quadratics in im L_p have a common projective zero. In particular B₀⊂B. The bounds mean upper bounds for dimensions of the bad loci; no claim of equality or nonemptiness is made.

## 5. Actual vertex obstructedness

The complement P(K)\B is nonempty open dense by (4). The smooth-quintic locus Ω∩P(K) is also nonempty open, by the imported basepoint-free Bertini proof. Since P(K) is irreducible, the intersection of these two opens is nonempty open dense in Ω∩P(K). On it L_p is surjective. More generally the same conclusion below holds on (Ω∩P(K))\B₀.

We recall precisely how the imported obstruction criterion applies. At p∈K, put E=F|X_p, A=H¹(End₀F), with dim A=24. The restriction sequence gives a tangent-space splitting

    Ext¹_X(E,E)=A⊕U,   dim Ext¹_X(E,E)=26.

Writing z∈U and a_v∈A, the primary cyclic cubic has the form

    W₃(a_v+z)=Φ(v·p)(z,z)/2 + G(z,z,z)/6,

where G∈Sym³U* is the remaining unknown normal cubic. Its derivatives along the A coordinates are exactly the binary quadratics from im L_p, up to a factor 1/2. If p∉B₀, these have no common nonzero zero, so their ideal in C[z₁,z₂] has radical (z₁,z₂). If p∉B, they even span all three binary quadratics.

The associated graded minimal hull is consequently a quotient of a polynomial ring in 24 orbit variables and two normal variables modulo those quadratic forms, a ring of Krull dimension 24. The hull therefore has dimension at most 24. The imported embedded smooth orbit germ supplies the reverse inequality, so its dimension is exactly 24. Its embedding dimension is 26, making it nonregular and not formally smooth. Thus the restriction is actually obstructed, independently of G and all higher Kuranishi terms.

For p∉B the degree-two initial ideal contains (z₁,z₂)². This is a containment, not a proposed full list of quadratic equations: mixed orbit-normal components also occur. We make no claim about the full ideal, reducedness, multiplicity, or other components.

## 6. Exact primary normal form at a surjective vertex

Assume L_p is surjective. Choose linear coordinates t₁,t₂,t₃ among the 24 orbit coordinates, and z₁,z₂ on U, such that the cyclic cubic is

    W₃=1/2(t₁z₁²+2t₂z₁z₂+t₃z₂²)+G(z₁,z₂)/6.

Every binary cubic is a sum of linear forms times z₁², 2z₁z₂, z₂²: the multiplication map U*⊗Sym²U*→Sym³U* is surjective. Choose linear forms ℓ₁(z),ℓ₂(z),ℓ₃(z) with

    ℓ₁z₁²+2ℓ₂z₁z₂+ℓ₃z₂²=G/3.

The invertible linear tangent-coordinate change tᵢ'=tᵢ+ℓᵢ(z), for i=1,2,3, with all other coordinates unchanged, preserves the orbit subspace z=0 and gives

    W₃=1/2(t₁'z₁²+2t₂'z₁z₂+t₃'z₂²).

Under an invertible linear change of tangent coordinates the gradient components transform by the invertible transpose Jacobian, so their linear span transforms as the degree-two obstruction space should. Dropping primes, the gradient components therefore span precisely

    z₁², z₁z₂, z₂²,
    t₁z₁+t₂z₂, t₂z₁+t₃z₂.                       (5)

These five quadratics are linearly independent: the first three are independent pure normal quadratics, while the last two have independent orbit-normal monomial supports. The other 21 orbit derivatives vanish. The imported minimal Kuranishi construction identifies the degree-two part of its ideal exactly with the span of the gradient components of W₃, so (5) is the entire degree-two initial space, not merely five known elements of it.

Equivalently, the ideal generated by the quadratic initial equations is

    ((z₁,z₂)², t₁z₁+t₂z₂, t₂z₁+t₃z₂).

Its radical is (z₁,z₂). Higher-degree initial equations or higher Kuranishi terms are not determined. The removal of G is a choice of splitting and tangent coordinates, not an assertion that its original coefficients vanish geometrically. Thus the primary obstruction normal form is fixed at every surjective vertex even though the full formal hull remains undetermined.

## Scope and dependencies

All new computations are universal Heisenberg-matrix identities, finite-field closure arguments, representation-theoretic stabilizer bounds, duality, and projective incidence dimensions. The result closes the previously conditional GENERIC vertex criterion; it does not decide every individual vertex. The scalar nonvanishing, tangent dimensions, smooth-member existence, exact mixed obstruction pairing, and embedded orbit germ are explicitly imported audited facts. No selected polynomial, HM/source/cofactor rank instance, or large computation is used. Only local proof files are written; no external application is changed.
