# Independent audit: primary/cofactor trace-pairing reduction

## Verdict

The identities, exact sequences, bounds, signs, and the unconditional lowest-generation/socle specialization in `PROOF.md` are correct. The two countermodels have the stated scope. They exclude deductions from the enumerated abstract module data; they do not replace the actual conductor, bundle, or multiplication maps.

I independently checked the equivariant-generator subsection of `https://github.com/Akilleez-QA/read-em-and-weep/blob/41ed82a75476057eb1a6222390bd96ccf5f88b27/research/conductor-normalization/discriminant-normalization-conductor/PROOF.md` and section 8 of its `AUDIT.md`. They supply the precise representation-theoretic premise needed for the linear cofactor coefficients to span the five-dimensional space of linear forms. No additional equivariance of the bundle or its cohomology is required.

## 1. Dualities, types, and signs

Put T=M_{−4}, E=M_{−3}. The trace identifications are T*=M_{−1}, E*=M_{−2}, and (M_0)*=M_{−5}. Multiplication by t₂ defines Q:T→E* and its transpose Q*:E→T*. Multiplication by t₃ defines the symmetric map R:T→T*.

For U=(M_{−5})^5 and the coefficient maps A:U→E, B_lin:U→T, adjointness gives exactly

    α*=Q*A+R B_lin.

If P=(Q,−R), then P*=(Q*,−R), so α*=P*∘(A,−B_lin). The sign changes the factorization map, not the image im P*=im Q*+im R or any kernel/rank statement. Symmetry of R is ordinary symmetry, not skew-symmetry: the cohomological degree is even, and cyclicity of trace supplies no minus sign.

Uniqueness of j_i=t₂a_i+t₃b_i in degree four follows from the regular sequence of degrees two and three. A homogeneous syzygy in total degree four would be a multiple of the Koszul syzygy by a degree-minus-one polynomial, hence zero.

## 2. The primary radical and its rank

Let C=im Q*, K=ker Q=C^⊥, H=im R, and V=ker P. Then

    V=K∩ker R=(C+H)^⊥.

Restriction identifies T*/C with K*. Consequently, if π:T*→T*/C, the map πR:T→K* is the transpose of R|K:K→T*, using symmetry of R. Thus

    c=dim πH=rank(R|K)=rank(R restricted to K×T),
    rank P=dim(C+H)=d+c,
    dim V=10−d−c.

The use of all T in the restricted pairing is essential. The radical of R|K×K can be larger than K∩ker R, so substituting that smaller test space would invalidate the primary criterion.

## 3. The exact cofactor filtration

Let W=im B_lin and J=im α*. Projection modulo C gives

    πJ=πR(W),

because A contributes only to C and B_lin is onto W by definition. Therefore, with e=dim πR(W) and h=dim(J∩C),

    rank α=dim J=h+e,
    q=rank P−rank α=(d−h)+(c−e).

Both terms are nonnegative: J∩C⊂C and πR(W)⊂πH. The exact sequence

    0→C/(C∩J)→(C+H)/J→πH/πR(W)→0

is canonical. The first arrow is induced by C⊂C+H; its image is (C+J)/J. The last arrow is induced by π and has precisely that kernel.

Perfect pairing also gives

    ((C+H)/J)* ≅ ker α/V.

Dualizing the sequence gives the sequence displayed in the proof. Its left term is canonically (ker α∩K)/V: inside ker α/V, it is the annihilator of C/(C∩J), namely the vectors also annihilating C.

For a direct check, let x∈K and η_i∈M_{−5}. Then

    ⟨j_i x,η_i⟩=⟨t₃x,b_iη_i⟩=R(x,b_iη_i),

since the quadratic term vanishes on K. Hence

    ker α∩K={x∈K:R(x,W)=0},
    rank(α|K)=rank(R restricted to K×W)=e.

Its dimension is 10−d−e; subtracting dim V yields c−e. Thus all the bounds in the proof follow, including

    rank α≤d+e≤d+c,
    dim ker α≥10−d−e,
    q≥c−e≥max(0,c−dim W).

The criteria for ker α=V and for α to be injective are also exact. No splitting of the filtration is implied.

## 4. Why the b_i span, and the socle interpretation

The verified normalization presentation establishes that the cofactor span is the irreducible SL₂ module V₄, while S₁ is likewise V₄. Since t₂ and t₃ are invariants and the degree-four decomposition is unique, taking the b-coefficient is an equivariant map V₄→V₄. If it were zero, every quartic generator would be divisible by t₂. Their ideal would then be contained in a height-one principal prime, contradicting its verified height two. The coefficient map is therefore a nonzero map of irreducibles, hence an isomorphism. Thus

    W=S₁M_{−5}.

For y∈M_{−1} and x∈S₁, η∈M_{−5}, adjointness gives

    ⟨y,xη⟩=⟨xy,η⟩.

Perfect pairing between M₀ and M_{−5} now proves

    W^⊥={y∈M_{−1}:S₁y=0}=Soc(M)_{−1}.

The map R|K has image R(K) of dimension c. Restricting its image to W has rank e. Its kernel is exactly R(K)∩W^⊥. Therefore

    c−e=dim(R(K)∩Soc(M)_{−1}),
    ker α∩K={x∈K:t₃x∈Soc(M)_{−1}}.

Lowest-degree multiplication μ:S₁⊗M_{−5}→T is surjective exactly when this degree-minus-one socle vanishes. Equal source and target dimensions are needed only to strengthen surjectivity to isomorphism. The proof's intended conclusion is correct; these two logical steps should remain distinct.

The weaker condition c=e is exactly R(T)⊂C+R(W). It does not require W=T or the entire socle to vanish.

## 5. Countermodel checks

### 5.1. Failure of lowest generation with an invertible cubic map

Each string [a,b] used in the proof satisfies a+b=−5. Pair the basis vectors in complementary degrees within that string. This gives a perfect symmetric pairing, and multiplication by the shift variable is selfadjoint, including at the endpoints. Direct sums preserve these properties.

Two strings [−5,0], eight [−4,−1], and ten [−3,−2] give exactly the dimensions (2,10,20,20,10,2). Only the two length-six strings meet degree −5, so S₁M_{−5} has dimension two. The regular pair x₀², x₀³+x₁³ acts as the square and cube of the shift. The cubic is an isomorphism from degree −4 to degree −1 on every string meeting those degrees. Its polynomial regularity is unaffected by the fact that x₁ acts as zero on this module.

### 5.2. Invertible cofactor map, with height two and b-spanning

For A₀=S/(x₀²,…,x₄²), the square-free monomial basis shows that its socle degree is five, its Hilbert function is (1,5,10,10,5,1), and the top-monomial coefficient pairing is perfect. Two shifted copies give the required M.

With the choices in the proof, t₂=L² and t₃=x₀³ are coprime, hence regular, and b_i=x_i is a basis. In A₀ the j_i act as L³x_i. Writing m_j for the product of every variable except x_j,

    L³x_i=6 Σ_{j≠i}m_j.

Thus the map A₀₁→(A₀₅)^5 has matrix 6(J₅−I₅), with eigenvalues 24 and −6 (four times). It is invertible, so α is invertible on M. In particular P is injective as well. Independently, Q is injective: if L²Σv_i x_i=0, every triple of distinct indices has coefficient 2(v_i+v_j+v_k)=0; comparison makes all v_i equal and then zero.

For the height assertion, the displayed brackets g₀,g₁ differ by L²(x₀−x₁). Neither L nor x₀−x₁ divides g₀, so the brackets are coprime. The two cross-coordinate divisibilities also fail. Therefore j₀,j₁ are coprime; the ideal they belong to has height at least two. Containment in the regular ideal (t₂,t₃) gives height at most two. The proof correctly states what this model does not preserve: the actual determinantal resolution and SL₂-equivariant cofactor identities.

### 5.3. Optional explicit witness against an even-q inference

There is also an abstract example with q=9, preserving the same Hilbert function, symmetric selfduality, polynomial regular sequence, unique decomposition, b-spanning, and height-two quartic ideal.

Set L=Σx_i, t₂=L², t₃=x₀³, b_i=x_i, and

    a_i=Lx_i−2x_i²,
    j_i=x_i[L²(L−2x_i)+x₀³].

Use the same numbers and lengths of selfdual strings. On one length-six string let x₁ act as the shift and all other variables act as zero. On every other string let x₀ act as the shift and all other variables act as zero.

On both coordinate lines t₂ acts as the square of the shift, so Q is injective and rank P=10. On the x₀ line every j_i is zero. On the x₁ line j₁ acts as minus the fourth power of the shift and the other j_i vanish. Thus rank α=1 and q=9. The cubic R has rank nine as well.

The same gcd argument proves height two: if f_i=L²(L−2x_i)+x₀³, then f₀−f₁=−2L²(x₀−x₁); neither possible common factor divides f₀, and neither cross-coordinate factor divides the other bracket. Regularity and decomposition uniqueness are unchanged.

This example is only a countermodel to abstract parity deductions, not a claim about the actual conductor or HM module. Symmetry supplies no alternating-form even-rank rule.

## 6. Scope and secondary obstruction

The reduction identifies the exact primary radical and a canonical two-step filtration of the cofactor defect. It does not evaluate d,c,e,h, the actual maps, or a retained obstruction. It supplies no identification of the separate secondary-obstruction target with V*, and therefore no new parity or rank theorem for that secondary map follows.

No correction to the mathematical statements in the final proof was required. The only logical nuance is to distinguish μ-surjectivity from μ-isomorphism as noted above.

## Status of this record

This is a historical mathematical audit, not a new formal verification or a new execution of tests.
