# Cayley weak failure survives every finite abelian pullback to (P1)^4

## Theorem and scope

Work over C. Let X=(P1)^4, h_i=c1 O_X(e_i), H=sum_i h_i, and let g:X→Q5 be the explicit seven-section carrier in `rank7_construction.md`. For any normalized Cayley bundle C on Q5, put F=g*C. Thus rank(F)=2, det(F)=O_X(−H), and c2(F)=H².

The completed source calculation in `cayley_weak_reduction.md` proves, for all six pairs i<j,

    Δ_ij(F)=A_i(F) cup h_j − h_i cup A_j(F) ≠ 0
    in H²(X, End(F)⊗Ω_i⊗Ω_j),

where Ω_i=p_i*Ω¹_P1 and A_i(F) is the factor-i Atiyah component. Its proof applies to every Cayley C for this fixed g.

Let f:A→X be any finite morphism from a complex abelian fourfold. Then:

1. The actual morphism f factors as an isogeny q:A→B=E_1×E_2×E_3×E_4 followed by a product h=a_1×a_2×a_3×a_4 of finite morphisms a_i:E_i→P1 from elliptic curves.
2. For the natural ample rational class θ=f*H/2, the pullback f*F has six linearly independent nonzero commutative Atiyah evaluations on θ-polarized mixed tangent directions. The same holds for its centered Atiyah class.
3. If a line bundle L with L²≅f*O_X(H) exists, the actual determinant-normalized bundle V=f*F⊗L has c1(V)=0 and c2(V)=3θ². Its full HKR evaluation has rank 18 and kernel dimension 10; the Chern-character annihilator has dimension 16. Thus it fails the weak first-order kernel equality.
4. The centered assertions require no square root. Any further isogeny pullback on which determinant normalization becomes available still has the same failure. Actual isogeny descent cannot remove it.

There is no restriction on the degrees, branch data, elliptic curves, Galois properties, or initial presentation of A as a product. The claim concerns all finite abelian pullbacks of these F, not all rank-seven Segre carriers and not all rank-two bundles with the same Chern classes. This is a first-order weak-test exclusion, not an ambient higher-obstruction theorem.

## 1. Every finite f factors in the required direction

A finite morphism A→X is surjective: its closed image has dimension four. Set

    L_i=f*O_X(e_i),    λ_i=c1(L_i),    K_i=ker(φ_{L_i})^0,

where φ_{L_i}:A→A^∨ is the line-bundle homomorphism. The L_i are globally generated and nef. Their numerical dimensions are exactly one, since λ_i²=0 and λ_1λ_2λ_3λ_4=deg(f)>0. Hence each connected kernel K_i has dimension three, and the quotient E_i=A/K_i is an elliptic curve.

One can see the kernel and dimension statement directly on the complex torus. Average the semipositive curvature form of the globally generated L_i over translations. This gives an invariant semipositive Hermitian representative of λ_i. Its rank is one because λ_i²=0 and λ_i≠0. The radical is rational for the lattice because the underlying alternating form is integral; it therefore defines a three-dimensional abelian subvariety, precisely K_i. The sum of these invariant forms is positive definite because tensor_i L_i=f*O_X(H) is ample.

This also proves descent of the actual coordinate maps, not just of their numerical classes. Restrict L_i and its two defining sections to any coset of K_i. This restriction is numerically trivial and globally generated. A nonzero section cannot vanish on a nonzero effective divisor, since such a divisor has positive intersection with an ample class on the coset. Thus the restricted bundle is trivial, and all its sections are constants in a trivialization because the coset is connected and projective. Consequently the coordinate morphism f_i:A→P1 is constant on every K_i-coset. The quotient property gives an actual morphism a_i:E_i→P1 with

    f_i=a_i q_i,    L_i=q_i*(a_i*O_P1(1)).

Each a_i is nonconstant and hence finite, of degree m_i≥2. In particular, no unresolved Pic^0 correction is present in this factorization.

The intersection of the four K_i is finite, since their tangent radicals have zero intersection by positivity of sum_i λ_i. Therefore

    q=(q_1,q_2,q_3,q_4):A→B=product_i E_i

has finite kernel between abelian varieties of equal dimension, so it is an isogeny. With h=product_i a_i one has f=hq. Translations in the original f_i are absorbed in a_i; the original coordinate maps are not assumed to be homomorphisms.

For the torus/polarization and isogeny foundations see Milne, `Abelian Varieties`, I.2 and I.7: https://www.jmilne.org/math/CourseNotes/AV.pdf. The factorization above is the direct application needed here.

## 2. The derivative map has a regular differential-trace retraction

Fix any finite a:E→P1 from an elliptic curve, of degree m. Put D=a_*O_E. Choose invariant ω∈H⁰(E,Ω¹_E) and v∈H⁰(E,T_E) with ω(v)=1. There are sheaf maps

    ι:O_P1→D,                         the unit,
    ε=(1/m)Tr_a:D→O_P1,               normalized ordinary trace,
    φ:Ω¹_P1→D,   α↦ι_v(a*α),        derivative-contraction,
    τ:D→Ω¹_P1,   s↦Tr_a¹(sω),        regular differential trace.

The differential trace is regular across ramification. In the local tame model t=z^e, write sω=Σ_{r≥0} b_r z^r dz. Rewriting dz=z^(1−e)dt/e and summing over branches kills every negative power: among exponents r+1−e≥1−e, no negative exponent is divisible by e. The remaining terms are regular multiples of dt. This is also the finite-syntomic trace of Stacks, Lemma 50.19.2 and Proposition 50.19.3: https://stacks.math.columbia.edu/tag/0FK6 . Finite morphisms of smooth curves in characteristic zero satisfy those hypotheses.

Since a*α=φ(α)ω, the differential-trace projection formula gives the exact sheaf identities

    ε ι=Id,     τ φ=m Id_Ω,     τ ι=0.                 (2.1)

The last equality holds because Tr_a¹(ω) is a global holomorphic one-form on P1, and H⁰(P1,Ω¹)=0.

It is essential that (2.1) does NOT assert εφ=0. Ordinary trace of the derivative may be nonzero. For example, take the degree-three map t=℘′ on an elliptic curve with (℘′)²=4℘³−g₂℘−g₃ and invariant ω=dz. The three values x_r=℘ over t satisfy sum x_r²=g₂/2, so

    Tr_a(φ(dt))=sum_r (6x_r²−g₂/2)=3g₂/2,

which is generally nonzero.

For completeness, O⊕Ω is nevertheless an actual direct summand of D. Put r=εφ and φ̃=φ−ιr. Then εφ̃=0, τφ̃=m Id, and the inclusion (ι,φ̃) has left inverse (ε,τ/m). Equally, the original inclusion (ι,φ) has left inverse (ε−rτ/m,τ/m). The argument below retains the actual derivative maps φ throughout and does not identify them with a prescribed trace-zero or deck-character summand.

## 3. Six simultaneous pair retractors

Apply Section 2 to each a_i. Write D_i=(a_i)_*O_{E_i}, and use subscripts on ι_i, ε_i, φ_i, τ_i. Finite pushforward and the product formula give

    h_*O_B = D_1 ⊠ D_2 ⊠ D_3 ⊠ D_4 =: D.

For i<j define the actual sheaf map

    S_ij:Ω_i⊗Ω_j→D

by φ_i and φ_j on factors i,j and the unit ι_r on the two complementary factors. Define a retraction candidate

    R_ij:D→Ω_i⊗Ω_j

by τ_i/m_i and τ_j/m_j on factors i,j and ε_r on the other two factors. Then the exact sheaf identities are

    R_ij S_rs = Id       if {i,j}={r,s},
    R_ij S_rs = 0        otherwise.                    (3.1)

For equal pairs this is (τ_iφ_i/m_i)(τ_jφ_j/m_j) times ε_rι_r on the other factors. For distinct pairs, choose an index t∈{i,j}\{r,s}; the composite on that factor contains τ_tι_t=0. This argument does not require ε_tφ_t=0.

Thus the direct-sum map

    S: direct_sum_(i<j) Ω_i⊗Ω_j → D

has left inverse R=(R_ij). Tensoring with End(F), taking actual H², and using the projection formula preserves this split injection. In particular the six classes

    S_ij,* Δ_ij(F) ∈ H²(B,End(h*F))

are linearly independent and nonzero. Explicitly, R_ij,* applied to their linear combination isolates its coefficient times the already proved nonzero Δ_ij(F).

This is stronger than a numerical or spectral-sequence argument. It proves independence in actual End-valued cohomology for arbitrary finite maps. The classes need not lie in distinct eigenspaces or even in the naive pure summands of an independently chosen splitting of D.

## 4. The classes are exactly the polarized mixed evaluations

On B put λ_i=a_i*h_i, λ=sum_i λ_i=h*H, and θ_B=λ/2. Choose invariant dual ω_i,v_i on E_i and set

    η_i = ι_{v_i} λ_i ∈ H¹(E_i,O_Ei).

Thus λ_i=ω_i⊗η_i, and η_i≠0. Naturality for the Atiyah class of O_P1(1) identifies η_i with H¹(φ_i)(h_i). The four diagonal and six mixed vectors

    d_i = v_i⊗η_i,
    κ_ij = (1/2)(v_i⊗η_j + v_j⊗η_i),  i<j,

form a basis of the ten-dimensional θ_B-polarized tangent space. Indeed contraction with θ_B sends the two mixed terms to opposite degree-two products of η_i and η_j; the η_i form a basis of H¹(B,O_B). The factor 1/2 matches θ_B=λ/2; omitting it merely rescales the chosen six vectors.

Put W=h*F. Naturality of the Atiyah class, exact finite pushforward, and the projection formula give

    ob_W(κ_ij) = ±(1/2) S_ij,* Δ_ij(F).              (4.1)

The overall sign depends on the uniform convention for Atiyah/Kodaira–Spencer evaluation. The relative minus sign in Δ_ij is forced by moving the factor-i degree-one class past the factor-j Atiyah class. No independent degree factor appears: the degrees are already incorporated in η_i=H¹(φ_i)(h_i).

One way to check (4.1) explicitly is to evaluate the first mixed summand as the image of A_i(F) cup h_j under φ_i⊗φ_j. The other mixed summand gives the image of −h_i cup A_j(F), after ordering the cohomological factors. Units occupy the two untouched factors. This is precisely S_ij applied to Δ_ij.

The centered Atiyah class of any rank-two bundle U is

    a(U)=At(U)−(1/2)Id_U c1(U).

It is invariant under every line-bundle twist. Here c1(W)=−λ, hence a(W)=At(W)+θ_B Id. Since κ_ij preserves θ_B, its contraction with the added scalar class vanishes. Therefore (4.1) is also the centered mixed evaluation. Equivalently, replacing each A_i(F) by A_i(F)+(1/2)h_i Id leaves Δ_ij(F) unchanged because the two added scalar terms cancel.

Together with (3.1), this gives the particularly transparent detector equation

    R_ij,* ob_W(κ_rs) = ±(1/2)δ_{ij,rs} Δ_ij(F).   (4.2)

All six actual polarized mixed obstructions are therefore independent.

## 5. Four diagonal vanishings and determinant normalization

The four diagonal commutative directions genuinely extend the bundle. Deform one elliptic curve E_i in its one-dimensional deformation space. The positive-degree bundle M_i=a_i*O_P1(1) extends because a curve has no H²(O); its two chosen generating sections lift because H¹(E_i,M_i)=0. They remain generating to first order by Nakayama's lemma, yielding a deformation of the actual morphism a_i. Keep the other three maps fixed and pull back the fixed F. This constructs a deformation of W along d_i, proving ob_W(d_i)=0. It also proves centered vanishing, since d_i preserves θ_B.

For the original f=hq, set θ_A=f*H/2=q*θ_B. If L²≅f*O_X(H), put V=f*F⊗L. Then

    det(V)=O_A,
    c1(V)=−f*H+2θ_A=0,
    c2(V)=f*H²−(f*H)θ_A+θ_A²=3θ_A²,
    At(V)=a(f*F)=q*a(W).

A square root on A is sufficient; none is assumed to descend to B. This last equality, together with the isogeny comparison in Section 7, transfers both the six independent mixed evaluations and the four diagonal vanishings to the actual normalized V.

If the square root is unavailable, V is not an actual bundle and should not be claimed to exist. The centered class and all preceding polarized nonvanishings still exist. Pulling back by multiplication by two makes the Chern class of f*O_X(H) divisible by two; the remaining Pic^0 discrepancy has a square root because multiplication by two on Pic^0 is surjective. Hence normalization becomes possible after an isogeny, but the obstruction persists.

## 6. Exact full-HKR kernel: 10 rather than 16

Assume actual normalization V as above. Let a=At(V), and use the standard convention

    ev_V(b,κ,β) = b Id + κ contraction a + (1/2)β contraction a²,
    HH²(A)=H²(O_A) ⊕ H¹(T_A) ⊕ H⁰(Λ²T_A).

Its three source summands have dimensions 6,16,6. The trace-free rank-two matrix identity gives

    a²=(tr(a²)/2)Id=−c2(V) Id.

For instance use a determinant-compatible Chern connection: its curvature matrix is trace-free, its entries have even total degree, and Cayley–Hamilton gives the displayed identity already at the differential-form level. Thus the six-dimensional compensated-Poisson graph

    (b,κ,β)=((1/2)β contraction c2(V), 0, β)

lies in ker(ev_V). All Poisson images are scalar; no assumption about simplicity is needed.

We next determine the kernel of the commutative map κ↦κ contraction a. If that evaluation is zero, compatibility with Chern characters gives κ contraction c2(V)=0. Since c2(V)=3θ_A² and κ acts as a derivation, this says

    6θ_A wedge (κ contraction θ_A)=0.

Multiplication by θ_A is injective on H^{0,2}(A), either by hard Lefschetz or directly by the exterior algebra of a positive Hermitian form. Hence κ preserves θ_A. Inside its ten-dimensional polarized tangent space, Section 5 gives four independent diagonal kernel vectors and Sections 3–4 give six independent mixed images. The commutative kernel is exactly the four-dimensional diagonal space, and the commutative map has rank 12.

The commutative image is trace-free because tr(a)=0. The scalar inclusion H²(O_A)→H²(End V) is injective and split by half the trace. Therefore it contributes another independent six image dimensions. Consequently

    rank(ev_V)=12+6=18,
    dim ker(ev_V)=28−18=10,

and the kernel is exactly the direct sum of the four diagonal commutative directions and six compensated-Poisson directions.

For comparison,

    ch(V)=2−3θ_A²+(3/4)θ_A⁴.

More generally, if ch=2−dθ²+(d²/12)θ⁴ with d>0, define Π=(β contraction θ²)/2. Its HH² annihilator consists exactly of

    κ contraction θ=0,    b=dΠ,

with β arbitrary. The degree-(0,2) component imposes b=dΠ, and the degree-(1,3) component imposes θ wedge (κ contraction θ)=0. These conditions suffice for the last component because β contraction θ^k=k(k−1)Πθ^(k−2). Hence the character annihilator has dimension 10+6=16 for every ample θ, whether principal, nonprincipal, integral, or rational. Here d=3.

Thus the six mixed vectors belong to the Chern-character annihilator but have independent nonzero actual evaluations. The weak kernel equality fails by exactly six dimensions.

## 7. Isogenies and actual descent cannot erase the failure

Let r:A'→A be any isogeny of degree e. It is finite étale over C. Its differential and pullback identify the three HKR degree-two source summands, hence give an isomorphism

    r^sharp:HH²(A)→HH²(A').

Atiyah classes and their powers are natural, and evaluation satisfies

    ev_(r*V)(r^sharp ξ)=r*ev_V(ξ).

Projection formula and ordinary trace show that (1/e)Tr is a left inverse to

    H²(A,End V)→H²(A',End(r*V)).

Thus this target map is injective and the two evaluation kernels correspond exactly. The same is true for centered evaluation before determinant normalization. Nonvanishing, linear independence, rank, kernel dimension, and failure of kernel equality are preserved.

If a bundle is an actual isogeny pullback r*V_0, the same argument read in reverse proves that V_0 cannot escape the failure. A choice of equivariant structure does not alter that conclusion. If det(V_0) becomes trivial after the isogeny, it is torsion; normalizing it by a Pic^0 square-root twist has zero Atiyah effect. Projective/twisted descent and replacing the bundle by an unrelated one downstairs are outside this assertion.

Finally, changing the polarization cannot evade the result within the scalar-square Chern-character architecture. If another ample class ψ satisfies c2(V)=dψ², then θ_A²=(d/3)ψ². Diagonalize the invariant positive Hermitian form of θ_A relative to ψ. Equality of squares says that all six pairwise products of the four positive eigenvalues equal d/3. Hence all four eigenvalues are equal, so θ_A is proportional to ψ and their polarized tangent spaces coincide.

## Final exclusion

For every Cayley bundle C on Q5 and the fixed explicit g:(P1)^4→Q5, no choice of finite f:A→(P1)^4, ramification, degree, elliptic factors, isogeny presentation, determinant-normalizing line twist, further isogeny pullback, or actual isogeny descent can make this construction pass the weak first-order test. The exact normalized result is kernel dimension 10 against character-annihilator dimension 16.

The substantive source input remains the six proved Δ_ij(F)≠0. This extension introduces no deck-character assumption and does not assert that all rank-seven Segre carriers have that input.

## General source criterion proved by the same argument

The trace/factorization argument does not use the Cayley origin of F. For any rank-two bundle F on (P1)^4 with c1(F)=−H and c2(F)=H², let r be the number of its six actual classes Δ_ij(F) that are nonzero. Then every finite abelian pullback, when determinant-normalized, has

    rank(ev)=12+r,    dim ker(ev)=16−r.

Indeed the four diagonal directions always extend, and the pair retractions make the r nonzero mixed images independent; the remaining six−r mixed directions vanish by the exact evaluation formula. The polarized commutative kernel therefore has dimension 10−r. The Chern-character argument excludes additional nonpolarized kernel vectors, and scalar/compensated-Poisson bookkeeping is unchanged.

Consequently all finite maps give the same weak-test verdict for such a source F:

    weak kernel equality holds  ⇔  Δ_ij(F)=0 for every i<j.

This criterion does not assert that a source satisfying all six vanishings exists, nor that pairwise vanishing settles the full four-factor Segre first-neighborhood obstruction. It identifies the precise first-order source test that cannot be improved by changing the finite abelian pullback.

## Reproducible normalization check

`verify_finite_pullback_character.py` performs exact rational exterior algebra with unequal degrees (2,3,5,7), θ=(sum_i m_i e_i∧f_i)/2, and centered c2=3θ². It verifies character-action rank 12; annihilator dimension 16; independence of the six compensated-Poisson plus four diagonal directions; and that κ_ij=(m_j v_i⊗f_j+m_i v_j⊗f_i)/2 supplies the remaining six annihilator directions. Its recorded output is `finite_pullback_character_certificate.txt`.

This certificate checks the finite-degree and one-half source normalization only. It does not compute an actual End-valued obstruction. The exact sheaf retractors and source Δ_ij calculation supply that essential step. Odd degrees in this check are intentional: the centered character exists whether or not the intermediate product itself admits the determinant-normalizing square root.
