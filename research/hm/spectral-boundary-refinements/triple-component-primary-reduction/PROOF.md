# Triple-component primary reduction and mandatory residual detectors

## 1. Setup and principal result

On Y=P⁴ let B=End₀(F), A=H²(B(-1)), T=A∨=H²(B(-4)), both dimension ten. The reduced triple-root component N is CI(t₂,t₃), of degrees two and three. The cofactor map is α:T→5H²(B), with transpose α*. Its quartic entries j_i generate I_Z, where Z=N∪W. Let U=im(r_W∨)⊂T; the degree-one-kernel exclusion proves dim U=w≤3.

The N-component detector is δ′:H⁰(N,B_N(1))→T, the transpose of r_N:A→H²(N,B_N(-1)). We construct a primary map P:T→C³⁰ and a secondary map σ:ker P→coker[C⁵→H¹(B(1))], proving im δ′=ker σ.

Crucially, the cofactor map factors through P itself. Consequently ker P⊂ker α, not merely ker σ⊂ker α. The secondary image produces a mandatory residual layer of the cofactor kernel after both component detectors are removed. If s=rank σ, at least max(0,s−3) residual detector dimensions survive the two components. Thus s≥4 excludes a component-only account of the cofactor kernel. No actual rank is evaluated.

## 2. Ordered Koszul maps and the finite reduction

Fix the order L=B(-2)⊕B(-1), H=B(1), K=I_N B(1), and maps

    u:T_sheaf=B(-4)→L,           u(x)=(t₂x,−t₃x),
    v:L→K⊂H,                    v(a,b)=t₃a+t₂b.

Then 0→T_sheaf→L→K→0 and 0→K→H→H_N→0 are exact. Changing the Koszul orientation changes δ′ by an overall sign, irrelevant to its image. We use positive connecting maps throughout and identify δ′ with their composition in this orientation.

Set

    P=H²(u):T→H²(L),       V=ker P,
    m=H¹(v):H¹(L)→H¹(H),  Q=coker m.

The verified negative-twist table gives H¹(B(-4))=H¹(B(-2))=0 and h¹(B(-1))=5. The relevant H² dimensions are h²(B(-2))=20 and h²(B(-1))=10. For the dimension twenty, the same negative H¹ vanishing and duality kill H¹,H³ of B(-2), stability kills H⁰,H⁴, and the established Riemann–Roch polynomial gives χ(B(-2))=20. Thus P is 10→30 and m is 5→h¹(B(1)). No endpoint vanishing is assumed: h¹(B(1))=55+h⁰(B(1))+h²(B(1))≥55 and h²(B(1))≤30. In particular dim Q≥50.

The first sequence gives

    0→H¹(L)→H¹(K) --b→ V→0.

For x∈V, choose y∈H¹(K) with b(y)=x and define σ(x)=[y mapped to H¹(H)] in Q. Lifts differ by H¹(L), so precisely im m is the unavoidable ambiguity. Exactness gives

    im δ′=ker σ=:D ⊂ V ⊂ T.

Writing p=rank P and s=rank σ yields

    dim D=rank r_N=10−p−s.

This is a complete finite test, not a claim that P alone computes r_N.

### Cochain signs and sufficiency

Use an affine acyclic cover and Čech differential d. For a closed T_sheaf two-cochain x representing x∈V, choose an L one-cochain ℓ with dℓ=u x. Then vℓ is closed and

    σ(x)=[vℓ] mod im m.

There is no minus sign here. Replacing ℓ by a closed L one-cochain z changes its representative by m[z]; replacing x by x+dh and ℓ by ℓ+u h changes nothing. If σ(x)=0, choose closed z with [vℓ]=[vz], and a zero-cochain h of H satisfying v(ℓ−z)=dh. The restriction h|N is a global section. Its first positive boundary is [v(ℓ−z)] in H¹(K), whose next boundary is x since d(ℓ−z)=u x. Conversely lifting any global N section through these two sequences produces such an ℓ. This proves both directions with all primitive ambiguities retained.

Let b₀=h⁰(B(1)) and a=rank m. Negative H⁰ vanishing and the first sequence imply H⁰(K)=0. The same chase gives

    h⁰(N,B_N(1))=b₀+(5−a)+(10−p−s).

Thus ker δ′ has dimension b₀+5−a. Equivalently coker r_N has that dimension, even though the component target itself is not computed numerically.

## 3. New dependence: quartic cofactors factor through the primary map

Since j_i∈H⁰(I_Z(4))⊂H⁰(I_N(4)), write

    j_i=t₂ a_i+t₃ b_i,     deg a_i=2, deg b_i=1.

These coefficients exist globally: the degree-four CI presentation is

    0→O(-1)→O(2)⊕O(1)→I_N(4)→0,

and H¹(O(-1))=0. They are unique because H⁰(O(-1))=0. Define

    f:L→5B,   f(a,b)_i=a_i a−b_i b.

Then f u=j, exactly with the displayed signs. Put F=H²(f) and let F_P:im P→5H²(B) be its restriction. Therefore

    α=F P,       V⊂ker α,
    0→V→ker α --P→ker F_P→0.

If q=dim ker F_P, then

    dim ker α=10−p+q,       rank α=p−q≤p.

In particular invertibility of α requires injectivity of P (and injectivity of F_P); σ injective on V is insufficient. More sharply, if p<10 and σ is injective on V, then r_N=0 but ker α still has dimension at least 10−p. This excludes inferring cofactor injectivity from absence of N-component detectors.

This factorization uses the degree-four cofactors and the actual scheme inclusion N⊂Z, not just abstract exact-sequence formalism. It does not select or evaluate their polynomial coefficients or cohomology matrices.

## 4. Both components removed: a mandatory secondary quotient

The cofactor-filtration theorem identifies the component detector image with D+U⊂ker α. Set

    U₀=U∩V,    i=dim(U∩D),    e=dim P(U),
    v₀=dim σ(U₀)=w−e−i ≤3.

Here P(U)⊂ker F_P because U⊂ker α. There is a canonical short exact sequence

    0→im σ/σ(U₀)→ker α/(D+U)
      --P→ker F_P/P(U)→0.                         (★)

Indeed the kernel of its right map is (V+U)/(D+U), canonically V/(D+U₀), and σ identifies this with im σ/σ(U₀). This is a quotient identification, with no chosen splitting or extension of restricted detectors.

Let g,n,ℓ be the ranks of the reduced-conic and nilpotent-ribbon gluing maps and the dimension of V_Z, respectively, in the existing cofactor filtration. Its dual identifies the total residual dimension with dim ker α/(D+U). Hence (★) gives the exact formula and lower bound

    g+n+ℓ = (s−v₀)+(q−e) ≥ s−v₀ ≥ max(0,s−3).

Also

    rank r_comp=10−p−s+w−i,
    dim ker α=rank r_comp+g+n+ℓ.

Consequences:

1. If s≥4, at least one reduced-gluing, nilpotent-gluing, or Hilbert–Burch lift obstruction is nonzero. Components alone cannot account for ker α.
2. If all three residual layers vanish, then im σ=σ(U₀), so s≤3, and ker F_P=P(U). These are necessary and sufficient conditions for residual vanishing, by (★).
3. If r_W=0, the residual dimension is s+q, and im σ injects canonically into the residual detector quotient. Every nonzero secondary class forces a residual obstruction, even when r_N=0.
4. If independently g=ℓ=0, then rank β_nil≥s−v₀. Without those extra hypotheses one must not assign this lower bound to the nilpotent layer alone.

The injection in (★) supplies a new aggregate detector subquotient; it is not a canonical splitting into the three residual layers. Their existing successive restrictions remain essential.

## 5. Why this is different from the fourth-power criterion

The prior fourth-power map starts from sections of B_N(4) and lands in A=H²(B(-1)); its middle sheaves are B(2)⊕B(1), and its secondary target uses H¹(B(4)). The present δ′ starts from B_N(1), lands in the dual ten-space T, and controls r_N on A, the actual component restriction in the cofactor filtration. Its middle groups have fixed dimensions five and thirty. Identifying A with T by an arbitrary vector-space isomorphism would not identify these maps.

Most importantly, the old secondary criterion by itself does not furnish α=FP, nor (★), nor the mandatory bound max(0,s−3) for residual cofactor detectors. These follow here from quartic ideal membership and the separate ≤3 square-component theorem. The ≥50-dimensional secondary target is not itself an obstruction rank; s≤10−p and only its actual image enters any conclusion.

## Dependencies and scope

Read and used: ../component-gluing-detector/PROOF.md; https://github.com/Akilleez-QA/read-em-and-weep/blob/21b252420c0011b2cbc119cab2983a6d4ad2e966/research/conductor-normalization/simple-pole-cofactor-comparison/PROOF.md; https://github.com/Akilleez-QA/read-em-and-weep/blob/f3f85ffc04213778c8c4fbd60e1e7e04b56cfd65/research/conductor-normalization/fourth-power-cohomology/PROOF.md; https://github.com/Akilleez-QA/read-em-and-weep/blob/063da90fc4543304e87e701cdefcc08225412f17/research/conductor-normalization/sharper-hm-regularity/SHARPEST-BOUND.md; https://github.com/Akilleez-QA/read-em-and-weep/blob/1d60973dd27a921a43bf6d9e71a06caa0cca0350/research/conductor-prerequisites/degree-one-kernel-exclusion/PROOF.md.

No actual cofactor, source, multiplication matrix, rank instance, splitting branch, or obstruction value has been evaluated.
