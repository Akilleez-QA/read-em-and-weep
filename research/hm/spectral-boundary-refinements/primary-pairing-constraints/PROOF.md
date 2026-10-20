# Trace-pairing reduction of the primary and cofactor defects

## 1. Scope and notation

Work over C with the graded S-module M_k=H²(B(k)) and trace/Serre pairings M_k × M_{−5−k}→C. These pairings are perfect, symmetric on interchanged arguments, and polynomial multiplication is adjoint to itself. Symmetry follows from cyclicity of trace and the even cohomological degree 2; no alternating-form parity restriction applies.

Set T=M_{−4}, E=M_{−3}, so T*=M_{−1}, E*=M_{−2}, with dimensions 10,20,10,20. Write Q=t₂:T→E*, R=t₃:T→T*, and P=(Q,−R). Thus R is symmetric and Q*=t₂:E→T*. No identification of E and E* is chosen.

The established cofactor decomposition is unique:

    j_i=t₂a_i+t₃b_i,  a_i∈S₂, b_i∈S₁, i=1,…,5.

Indeed (t₂,t₃) is a complete intersection of degrees (2,3), and the degree-four Koszul relation space is S_{−1}=0. Let U=5M_{−5}, whose dimension is ten. Define A:U→E by A(η)=Σa_iη_i and B_lin:U→T by B_lin(η)=Σb_iη_i. Then

    α*=Q*A+R B_lin.

The plus sign agrees with P=(Q,−R), since the transpose factor after P has second component −B_lin.

## 2. Exact radical criterion for P

Put C=im Q*⊂T*, H=im R⊂T*, K=ker Q=C^⊥ and V=ker P. Then

    V=K∩rad R=(C+H)^⊥.

Let π:T*→T*/C and define

    d=dim C=rank Q,
    c=dim πH=rank(R restricted to K×T).

Perfect duality identifies T*/C with K*, so the last rank equality follows by transpose. Consequently

    rank P=d+c,    dim V=10−d−c.

The relevant radical is the radical against ALL T. Replacing it with the radical of R|K×K is generally false: a vector can pair trivially with K but nontrivially with a complement. Symmetry alone neither forces a kernel nor forces an even rank.

## 3. A new exact two-defect filtration for α

Define W=im B_lin=Σb_iM_{−5}⊂T and J=im α*⊂C+H. Projection kills the entire quadratic-coefficient contribution:

    πJ=πR(W).                                      (1)

Set e=dim πR(W)=rank(R|K×W), and h=dim(J∩C). Equation (1) gives

    rank α=h+e,
    q:=rank P−rank α=(d−h)+(c−e).                 (2)

Both summands are nonnegative. More intrinsically there is a canonical exact sequence

    0→C/(C∩J)→(C+H)/J→πH/πR(W)→0.             (3)

This refines the previous undifferentiated cofactor defect q. Its right-hand quotient uses only t₂,t₃ and the LINEAR cofactor coefficients b_i; all a_i disappear from this quotient. The left term measures the remaining quadratic-image deficit after all cubic/linear contributions have been retained. No splitting is asserted.

Dualizing (3), using (C+H)/J ≅ (ker α/V)*, gives

    0→(πH/πR(W))*→ker α/V→(C/(C∩J))*→0.       (4)

The left term is canonically (ker α∩K)/V. In direct pairing terms,

    ker α∩K={x∈K : R(x,w)=0 for every w∈W},
    dim((ker α∩K)/V)=c−e.                       (5)

Proof of (5): for x∈K, α(x)_i=b_i t₃x because t₂x=0. Pairing this vector with η∈U gives R(x,B_linη). Its kernel is therefore the displayed restricted radical. Its dimension is dim K−e; subtracting dim V=dim K−c gives c−e.

Useful unconditional bounds and criteria are

    rank α≤d+e≤rank P,
    dim ker α≥10−d−e,
    q≥c−e≥max(0,c−dim W),
    ker α=V iff πR(W)=πH and C⊂J.

In particular, even after P is determined, an independent loss can be certified solely from the restricted cubic pairing. Cofactor injectivity is equivalent to d+c=10, e=c, and h=d. This replaces one opaque restriction rank with two canonically separated deficits; it does not evaluate any of them.

## 4. Lowest-degree generation specialization

For the actual conductor cofactors, b_1,…,b_5 span S₁, as proved below. Thus W=S₁M_{−5}, the image of the lowest multiplication map μ:S₁⊗M_{−5}→M_{−4}. Both source and target have dimension ten, but their dimensions do NOT establish that μ is an isomorphism.

The first defect therefore vanishes precisely when

    R(T)⊂C+R(S₁M_{−5}).                           (6)

This is strictly weaker than requiring μ surjective: generation need only hold after the cubic image is projected modulo the quadratic image. If μ is surjective, then c=e, ker α∩K=V, and q=d−h≤d. Without generation, the exact quantity c−e remains.

The spanning assertion follows from the verified equivariant generator theorem in https://github.com/Akilleez-QA/read-em-and-weep/blob/41ed82a75476057eb1a6222390bd96ccf5f88b27/research/conductor-normalization/discriminant-normalization-conductor/PROOF.md, §3, independently audited there in AUDIT.md, §8. The five-dimensional cofactor span is the irreducible SL₂ representation V₄, its quartic ideal inclusion is equivariant, t₂,t₃ are the binary-quartic invariants, and S₁=V₄ with the natural linearization. Uniqueness of decomposition makes j↦b an equivariant V₄→V₄ map. If this map were zero, all five ideal generators would be divisible by t₂, contradicting the height-two conductor ideal. Hence it is an isomorphism by irreducibility. This argument uses only the universal binary-quartic action on polynomials, and requires NO SL₂ action on the HM bundle or its cohomology. The representation identification is established by that normalization presentation, so this specialization is unconditional in the present geometric setup.

There is also an exact socle interpretation. Put

    Soc(M)_{−1}={y∈M_{−1}: xy=0 in M₀ for every x∈S₁}.

Adjointness and perfect pairing M₀×M_{−5} identify this space with W^⊥⊂T*. Hence

    c−e=dim(t₃K∩Soc(M)_{−1}),                    (7)
    ker α∩K={x∈K:t₃x∈Soc(M)_{−1}}.

Indeed R:K→T* has rank c, and restriction of its image to W has rank e. Equation (7) identifies its lost rank exactly with the intersection with W^⊥. Thus the first defect is the cubic image landing in the degree-minus-one socle. Its vanishing is weaker than absence of that socle altogether. The independent missing generation condition is equivalently Soc(M)_{−1}=0, since μ has equal-dimensional source and target.

## 5. Bounded countermodels and excluded inferences

These are abstract selfdual commutative graded modules, not alternate HM computations and not claimed geometric realizations of B.

### 5A. Hilbert function plus selfduality does not imply lowest generation

Let S act through C[x₀], and take the direct sum of two length-six strings supported on degrees [−5,0], eight length-four strings on [−4,−1], and ten length-two strings on [−3,−2]. Each string has basis e_a,…,e_b, x₀e_i=e_{i+1}, and all other variables act by zero. Pair e_i with e_{−5−i} with value one within its string. This pairing is perfect, symmetric, and multiplication-selfadjoint. The dimensions are exactly (2,10,20,20,10,2), whereas S₁M_{−5} has dimension two, not ten.

For the regular polynomial pair t₂=x₀², t₃=x₀³+x₁³, the cubic map R:T→T* is nevertheless an isomorphism: it carries the degree −4 basis vector to degree −1 in each of the ten strings meeting those degrees. Hence symmetry does not force primary degeneracy, and failure of lowest generation does not alone force a primary kernel. The polynomial regular-sequence requirement is preserved even though the module action factors through a quotient.

### 5B. Symmetric module data permit a square invertible cofactor map

Let A₀=C[x₀,…,x₄]/(x₀²,…,x₄²), and take M_k=(A₀)_{k+5}⊕(A₀)_{k+5}. The socle coefficient pairing gives the required selfduality and exact Hilbert function. Let L=Σx_i, t₂=L², t₃=x₀³, and

    a_i=Lx_i+x_i², b_i=x_i,
    j_i=t₂a_i+t₃b_i=x_i[L²(L+x_i)+x₀³].

The pair (t₂,t₃) is regular in S, the degree-four decomposition is unique, and the b_i form a basis of S₁. In A₀, j_i acts as L³x_i: the square and cube terms vanish. This has coefficient 6 on each square-free degree-four monomial containing i and zero on the monomial missing i. Multiplication by the five j_i from A₀₁ to five copies of A₀₅ has matrix 6(J₅−I₅), whose eigenvalues are 24,−6,−6,−6,−6. Therefore α is invertible on two copies. This bounded exact calculation is a countermodel only, not an evaluation of any actual cofactor or HM map.

Even the ideal (j_i) has height two. To check this, write g_i=L²(L+x_i)+x₀³, so j_i=x_i g_i. The two brackets g₀,g₁ are coprime: their difference L²(x₀−x₁) shows a common irreducible factor would be L or x₀−x₁, and neither divides g₀. Also x₀ does not divide g₁, and x₁ does not divide g₀. Thus j₀,j₁ are coprime, giving height at least two; containment in (t₂,t₃) gives height at most two. This countermodel preserves height two and the b-spanning property, but does NOT claim the genuine conductor's specific determinantal resolution or SL₂ equivariance. It excludes forced α degeneracy from the listed selfdual module, decomposition, spanning, and height data alone.

Even with all variables acting by zero on each graded piece, the same graded vector dimensions admit a perfect compatible symmetric pairing and both P and α vanish. Thus the bare listed module axioms do not determine either rank. No strong Lefschetz, minimal generation, or positivity claim follows from them.

## 6. Relation to the existing secondary obstruction

The map σ:V→Q_secondary remains a separately defined derived/cochain obstruction. The above trace pairing concerns middle-cohomology multiplication and yields no identification of Q_secondary with V*. In particular, no parity, self-adjointness, or rank bound for σ is inferred merely from symmetry of R. Its domain V is now the exact simultaneous radical above. Equations (3)–(5) refine the complementary cofactor defect q, and may be substituted unchanged into the earlier residual-detector dimension formulas. They do not discard σ or assign a defect to a particular conductor layer.

## Dependencies and scope

Read: ../triple-component-primary-reduction/PROOF.md; https://github.com/Akilleez-QA/read-em-and-weep/blob/21b252420c0011b2cbc119cab2983a6d4ad2e966/research/conductor-normalization/simple-pole-cofactor-comparison/PROOF.md; https://github.com/Akilleez-QA/read-em-and-weep/blob/063da90fc4543304e87e701cdefcc08225412f17/research/conductor-normalization/sharper-hm-regularity/SHARPEST-BOUND.md. No actual source, HM multiplication, cofactor matrix, spectral-sequence differential, or obstruction rank has been evaluated. The exact quotient reduction and its lowest-generation/socle specialization are unconditional in the verified binary-quartic conductor setup. The additional dependency https://github.com/Akilleez-QA/read-em-and-weep/blob/41ed82a75476057eb1a6222390bd96ccf5f88b27/research/conductor-normalization/discriminant-normalization-conductor/PROOF.md and its AUDIT.md were read to verify the cofactor representation and height-two input.
