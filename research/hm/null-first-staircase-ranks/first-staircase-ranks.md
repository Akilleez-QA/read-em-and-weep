# Exact first-staircase ranks in the compensated pair sector

20 October 2026. Formal result and existing review record; actual HM/source values are not evaluated here.

## Result

Let X=(P¹_t)^4, N=O(1,1,1,1), and let

L=[5N⁻¹ → 15N → 10N³ → 2N⁵]

have internal degrees -1,0,1,2 and sole cohomology E. Write S for the χ12 deck character and internal-swap signs (a,b)=(-,+), where a=(12), b=(34). The actual first P-curvature R=C_P(d,d) lies in S.

The Čech/sheaf-cohomology transfer in S has exactly the three finite spaces

K¹=C⁶⁰ --T=d₅--> K²=C⁴⁸⁰ --B=∂--> K³=C³⁰⁰.

Its exact ranks and cohomology are

rank T=60, rank B=300, dim ker B=180,
H¹(K)=0, dim H²(K)=120, H³(K)=0.

In particular all 60 upper-row classes survive to the cross-row differential; none survives it. There is an exact sequence

0 → C⁶⁰ --T--> ker(B) → Ext²(E,E)_S → 0.

The imported actual first-order existence implies that R belongs to im T as an actual element of the global C² space, not merely modulo a nonzero lower-row boundary. Thus there is exactly one u_R in C⁶⁰ such that T u_R=R. This is a unique upper-row preimage, not a unique un-gauge-fixed Čech primitive and not an evaluated list of 60 coefficients.

## 1. Linearizations and the zero upper target

The root N cancels in End. Every End^q summand is N^(2q), with multiplicities m₀=354, m₁=245, m₂=80, m₃=10 and m₋q=m_q. Constant multiplicity spaces carry the trivial factor-permutation action because the classical complex is pulled back from P⁴. In a finite frame the deck action is t_i↦-t_i; there is no extra root character in End and no alternating sign on ordinary tensor products of line bundles.

For H¹(P¹,O(-2r)), the Laurent basis is t^j, -2r<j<0. Its deck-odd part has dimension r and its deck-even part dimension r-1. Swapping two H¹ factors introduces the Künneth sign (-1)^(1·1)=-1. Consequently an active geometric sign - selects Sym² of the odd subspace, while a passive geometric sign + selects Λ² of the even subspace.

It follows that

H⁴(End⁻³)_S = C¹⁰⊗Sym²(C³)⊗Λ²(C²), dimension 60;
H⁴(End⁻²)_S = C⁸⁰⊗Sym²(C²)⊗Λ²(C¹) = 0;
H⁴(End⁻¹)_S = C²⁴⁵⊗Sym²(C¹)⊗Λ²(C⁰) = 0.

There is no End⁻⁴ term. Thus the upper-row differential out of the 60-dimensional space is zero and it has no incoming differential. This promotes the earlier E₁ count to an E₂-through-E₅ source count, without evaluating a differential.

## 2. Lower row

For H⁰(P¹,O(2r)), the odd and even polynomial subspaces have dimensions r and r+1. There is no Künneth minus sign in degree zero. Therefore

C^r_S = C^(m_r)⊗Λ²(C^r)⊗Sym²(C^(r+1)), for r=1,2,3.

In particular

C⁰_S=0, C¹_S=0,
dim C²_S=80·1·6=480,
dim C³_S=10·3·10=300.

All negative internal degrees have zero H⁰. The C⁰ statement also follows directly because its constant sections have trivial deck character. The active-minus condition, not just deck parity, is essential for C¹_S=0.

## 3. Imported Ext computation and exact rank inference

For the square-cover pushforward, χ12 selects the coefficient line O(-1,-1,0,0) on (P¹_x)^4. Its local odd generator t₁t₂ is a-even. Taking the pair quotients p:(P¹)^4→P²×P², sector S selects O(-2,0). Under the multiplication map m:P²×P²→P⁴ the previously audited bundle splitting is

m_*O(-2,0) ≅ 6O_P⁴(-2).

This is an honest vector-bundle splitting, not just a Hilbert-polynomial identity. One justification is finite flatness, vanishing of intermediate cohomology in every twist (the two P² offsets differ by only 2), and Horrocks splitting with the Hilbert polynomial. Projection formula gives, in every degree,

Ext^j_X(E,E)_S ≅ H^j(P⁴,End(H)(-2))^⊕6.

The imported pinned cohomology vector is (0,0,20,0,0). Hence the S-sector Ext vector is (0,0,120,0,0). The rank inference below uses precisely this imported result; it does not recertify it.

The spectral sequence has only sheaf rows 0 and 4. With internal degree horizontal, the only possible differential between them is d₅ of bidegree (+5,-4). In S the upper row consists solely of the degree -3 space of dimension 60. Therefore:

- Total degree 1 has only the possible piece ker(T). Ext¹_S=0 forces T injective.
- Total degree 3 has only coker(B), since H⁴End⁻¹_S=0 and the potential d₅ source H⁴End⁻²_S=0. Ext³_S=0 forces B surjective.
- Total degree 2 has only ker(B)/im(T). Its dimension is 480-300-60=120, agreeing with imported Ext².

There are no other filtration pieces in these total degrees and therefore no spectral-sequence extension ambiguity. No higher differential has room to act. The group projections are exact over C, so taking S before or after passing to pages/cohomology causes no discrepancy.

## 4. A concrete finite-length Čech contraction

Use the tensor product of the four standard two-chart Čech resolutions on P¹. It computes the required derived global sections and has Čech degrees 0 through 4. Factor permutations act by the usual graded permutation, producing exactly the signs in §1.

Here is an explicit monomial contraction for O(n) on one factor, written in the finite frame. Its two-chart complex is

V⁰=k[t] ⊕ t^n k[t⁻¹] --δ--> V¹=k[t,t⁻¹],
δ(a,b)=b-a.

For a monomial t^j:

- If 0≤j≤n, retain H⁰ with inclusion t^j↦(t^j,t^j) and projection (a,b)↦a; take h(t^j)=(0,t^j).
- If j≥0 and j>n, it occurs only in the first chart; take h(t^j)=(-t^j,0).
- If j<0 and j≤n, it occurs only in the second chart; take h(t^j)=(0,t^j).
- If n<j<0, retain H¹ represented by t^j and take h(t^j)=0.

The first case is empty when n<0; the last is empty when n≥-1. Directly, δh+hδ=id-ip, with hi=ph=h²=0. All maps preserve deck parity.

Tensor these contractions with Koszul signs. The tensor i and p commute with factor permutations; a standard ordered tensor homotopy need not. Average the homotopy over the finite swap/deck group, keeping i,p fixed. The average still satisfies the homotopy equation and hi=ph=0. If needed, replace the averaged h by hδh to restore h²=0. Thus the contraction can be chosen equivariant, and restricts to S. This is a construction of operators on finite-support Laurent cochains; it does not execute the actual HM maps.

Let Δ act on a Čech-degree-p cochain by (-1)^p[d,-]. Then D=δ+Δ, δΔ+Δδ=0, Δ²=0. The perturbation formulas are

I=(1+hΔ)⁻¹i,
P=p(1+Δh)⁻¹,
H=h(1+Δh)⁻¹,
d_K=pΔ(1+hΔ)⁻¹i.

Here inverse means the finite alternating geometric series. Every h lowers Čech degree by one, so at most four h factors can occur. These formulas give DI=Id_K and DH+HD=id-IP. On lower-row global sections I is ordinary inclusion because h vanishes in Čech degree zero.

All transferred terms except the row differential and the four-h cross-row term vanish by bidegree. In sector S this is exactly the displayed K, with

T = pΔ(hΔ)^4i, B = pΔi.

The cross-row sign is positive because the geometric-series term has four factors hΔ. Its representative depends on the contraction, but its induced spectral differential and exact rank do not. Since C¹_S=0, its target H²(C)_S identifies literally with ker(B), so there is no ambiguity from lower-row boundaries. A different choice of upper representative/homotopy can change the chosen cochain primitive, not the unique intrinsic preimage under the spectral differential after the natural identifications.

This is a finite-dimensional reduction and a finite-length homotopy prescription, not a claim that the full Laurent Čech spaces are finite-dimensional. Every application to finitely supported inputs uses only finitely many terms. No numerical or source-matrix computation is needed to prove the identities.

## 5. Constructive finite-dimensional contraction and the actual first primitive

Choose arbitrary Hermitian inner products on K¹,K²,K³. Formal ranks above guarantee that the following inverses exist:

L_T=(T* T)⁻¹T*: K²→K¹,
S_B=B*(B B*)⁻¹: K³→K².

An asterisk here denotes adjoint, not the Moyal product. These are exact algebraic prescriptions in the unevaluated matrices; they are not provided as numerical matrices. Set

Π₂=id-TL_T-S_BB.

Because BT=0, the three orthogonal pieces of K² are im(T), ker(B)∩ker(T*), and im(B*). Thus Π₂ projects onto a 120-dimensional representative of Ext²_S. Setting the degree -1 homotopy to L_T on K² and S_B on K³ gives

d_K h_K+h_K d_K=id-Π,

where Π is Π₂ in degree 2 and zero in the other degrees. This contracts the two acyclic portions, not the entire complex: the 120-dimensional middle cohomology is not removable.

Associativity makes the actual first curvature R=C_P(d,d) B-closed. The imported actual first-order existence gives [R]=0 in Ext²_S after symmetry projection. Since C¹_S=0, the preceding exact sequence implies R∈im(T) as an actual global element. Consequently

u_R=L_T R, T u_R=R,
a_P=-I u_R,
D a_P=-R.

Equivalently a_P is the finite alternating sum -Σ_(k=0)^4(-hΔ)^k i(u_R). It has Čech/internal bidegrees (4,-3),(3,-2),(2,-1),(1,0),(0,1). Its (0,1) component is generally a collection of local sections, not a global section of C¹_S. Therefore C¹_S=0 does not force this component to vanish and creates no contradiction.

The formula gives the exact unique upper preimage and a contraction-gauge representative in terms of unevaluated data. It does not give its coefficients without evaluating R,T. No coordinate vector is determined solely by the dimensions or first-existence theorem. If R vanishes literally then u_R=0 and this representative is zero; if R is nonzero then u_R is nonzero. Neither alternative is established here.

Any two actual first primitives differ by a D-boundary because Ext¹_S=0. Thus the symmetry-preserving boundary comparison applies, with all induced order-two gauge terms retained. This constructs a formal first-order procedure only; it supplies neither a second-order primitive nor vanishing of any remaining obstruction coordinate.

## 6. Provenance and scope

Sources: ../null-normalized-monad-lifting/normalized-monad-lifting.md; ../null-normalized-monad-lifting/normalized-monad-lifting-audit.md; ../null-normalized-boundary-comparison/normalized-boundary-comparison.md; ../null-normalized-boundary-comparison/normalized-boundary-symmetry-audit.md; ../null-dihedral-mixed-vanishing/CHARACTER-AUDIT.md; and https://github.com/Akilleez-QA/read-em-and-weep/blob/f968b53943ba2312f09fbc3e8f9d462e86bcaa34/research/hm/d8-small-certificates/p4/Perfect-Complex-D8-F3.md, especially §1.

Pinned source lineage, not newly remote-authenticated:

- Classical line complex: commit add03476d9055aa00e1e00778eea6332cf8e01cc, research/hm/ext-model.md.
- Imported cohomology (twist -2 vector (0,0,20,0,0)): commit f968b53943ba2312f09fbc3e8f9d462e86bcaa34, research/hm/d8-small-certificates/p4/Perfect-Complex-D8-F3.md.
- Actual carrier identification: commit 3bdc6cb28ecd75cfefb3cb0d85f42d5bcde8cc7f, research/hm-carrier-and-atlas.md.

The new result is the exact sector staircase, its ranks forced by imported cohomology, and a finite constructive contraction prescription. No fresh physical rank, curvature entry, first-preimage coordinate, second-order residual, or six-coordinate obstruction value has been evaluated. All source identifications, actual first-existence, and boundary comparison remain their explicit imported premises.
