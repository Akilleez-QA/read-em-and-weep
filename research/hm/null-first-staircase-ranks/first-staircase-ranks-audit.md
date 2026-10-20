# Independent audit: exact first-sector staircase ranks

20 October 2026. Formal result and existing review record; actual HM/source values are not evaluated here.

## Verdict

The candidate ranks and dimensions are correct, conditional on the explicitly imported classical line-resolution identification and accepted HM cohomology. In the sector S=(χ12,(12)=-,(34)=+), the two nonzero cohomology rows of the endomorphism hypercohomology spectral sequence reduce to

- Upper row: a 60-dimensional space at internal degree -3, sheaf degree 4, and zero elsewhere.
- Lower row: a 480-dimensional space at internal degree 2 mapping to a 300-dimensional space at internal degree 3, and zero elsewhere.

The lower differential has rank 300 and kernel dimension 180. The only cross-row differential d₅ is injective of rank 60 into that kernel. Thus the final degree-two space is a quotient of dimension 120. These exact ranks are forced by accepted sheaf-cohomology vanishings; they are not newly evaluated matrices.

## 1. Linearizations and lower-row dimensions

Use the actual normalized complex L=[5N⁻¹ → 15N → 10N³ → 2N⁵] in degrees -1,0,1,2. The canonical root cancels in End. Each internal-degree q summand is O(2q,2q,2q,2q), with multiplicities m₀=354, m₁=245, m₂=80, m₃=10, and m₋q=mq. The multiplicity spaces have trivial factor-permutation action because the complex is pulled back from P⁴. Ordinary line tensor factors introduce no permutation sign.

For q≥0 the one-factor H⁰ basis is 1,t,…,t^(2q). Its deck-odd part has dimension q, and its deck-even part has dimension q+1. The character χ12 selects the odd parts in factors 1,2 and the even parts in factors 3,4. In sheaf degree zero, active swap minus selects an exterior square and passive swap plus selects a symmetric square. Therefore

C^q_S = C^(mq) ⊗ Λ²(C^q) ⊗ Sym²(C^(q+1)).

In particular C⁰_S=C¹_S=0,

dim C²_S = 80·1·6 = 480,
dim C³_S = 10·3·10 = 300.

There are no further lower-row terms, including negative internal degrees. Here C^q denotes global endomorphism cochains, not their cohomology.

## 2. Upper-row dimensions and the indispensable Koszul sign

For q=-r, r≥1, H¹(P¹,O(-2r)) has Laurent representatives t^(-2r+1),…,t^(-1). With the inherited linearization its odd subspace has dimension r and its even subspace has dimension r-1. This is the action on line-sheaf cohomology, not on a differential-form basis; adding a differential-form character here would double-count a linearization adjustment.

Every upper-row Künneth factor has cohomological degree one. Interchanging two such factors therefore acts as minus the ordinary tensor flip. Consequently active swap minus selects Sym² of the odd Laurent space, while passive swap plus selects Λ² of the even Laurent space:

H⁴(End^(-r)L)_S = C^(mr) ⊗ Sym²(C^r) ⊗ Λ²(C^(r-1)).

For r=3 this has dimension 10·6·1=60. For r=2 it is zero because Λ²(C¹)=0. For r=1 it is zero because the passive deck-even space already vanishes. Thus the upper row has no nonzero row differential in this sector, and its degree -3 cohomology remains the entire 60-dimensional space. There is no preceding End⁻⁴ term.

This reconciles the geometric symmetric line-bundle linearization with the antisymmetric cohomological flip: the latter is a Künneth/Koszul sign, not an extra character imposed on L.

## 3. Independent final-cohomology input

The audited pair-character descent uses Y=(P¹_x)^4, x_i=t_i², and the coefficient line O_Y(-1,-1,0,0). Its natural odd generator t₁t₂ is active-swap even. Factoring the symmetric quotient through P²×P², the (-,+) summand is O(-2,0). Its finite pushforward to P⁴ splits as 6O(-2). Therefore, in every cohomological degree k,

Ext^k(E,E)_S ≅ H^k(P⁴,End H(-2))^(⊕6).

This ordinary vector-space splitting need not choose canonical bases. The sector itself is canonical. The accepted twist -2 HM values are h¹=0, h²=20, h³=0, hence

Ext¹_S=0, dim Ext²_S=120, Ext³_S=0.

The twist -2 h¹ and h² inputs import the previously audited injectivity of the source higher differential 10→80. This audit does not re-evaluate that physical source matrix. The prior audit separately explains h³=0 by the paired-evaluation surjection. Thus the present d₅ rank deduction is a transfer/consequence of accepted source information, not an independent new verification of that information.

## 4. Spectral-sequence indexing and exact rank deduction

Take E₁^(p,q)=H^q(X,End^p L), converging to Ext^(p+q)(E,E), with dᵣ of bidegree (r,1-r). Only q=0 and q=4 can occur. The spectral sequence is bounded and converges with no completion issue. Sector projection is exact over C and commutes with the differentials. The sole possible cross-row differential in this sector is

d₅: E₅^(-3,4) → E₅^(2,0).

Put u:C²_S→C³_S and K=ker u. Since C¹_S=0, the lower row at internal degree 2 has E₂^(2,0)=K, with no quotient by earlier boundaries. The upper source has E₂^(-3,4)=C⁶⁰. All d₂,d₃,d₄ vanish because their targets or sources lie in empty rows. The other potential cross-row arrow (-2,4)→(3,0) has zero source.

There is precisely one nonzero associated-graded slot in each total degree 1,2,3. Thus there are no hidden extension ambiguities:

Ext¹_S ≅ ker(d₅:C⁶⁰→K),
Ext²_S ≅ K/im d₅,
Ext³_S ≅ coker(u:C⁴⁸⁰→C³⁰⁰).

Ext³_S=0 implies rank u=300 and dim K=480-300=180. Ext¹_S=0 implies rank d₅=60. Consequently dim Ext²_S=180-60=120, agreeing with the independently imported h² value. In fact the two rank conclusions need only the Ext¹ and Ext³ vanishings once the cochain dimensions are established; Ext²=120 is then a consistency check.

Equivalently there is an exact sequence

0 → C⁶⁰ --d₅--> K → Ext²_S → 0,

and 0 → K → C⁴⁸⁰ --u--> C³⁰⁰ → 0.

No claim is made that d₅ maps onto all of K. Its image has codimension 120 there.

## 5. Precise consequences for the first lifting source

The actual first twisted curvature C_P(d,d) is a closed lower-row degree-two cochain in S, hence an element of K. Imported actual first-order existence implies that its class is zero in full Ext², so it belongs to im d₅. Since d₅ is injective, its upper-row preimage is unique, up to the global sign convention used to identify the staircase differential with the lifting equation.

This does not compute that preimage, a staircase primitive, or the curvature itself. It also does not prove the curvature is nonzero: zero curvature corresponds to zero upper-row preimage. The strict global first-lift criterion remains literal curvature vanishing, because C¹_S=0. The full model can cancel a nonzero curvature using this upper-row image. Neither the exact rank nor the 120-dimensional quotient gives a second-order vanishing theorem.

Exchanging the two pairs gives the identical conclusion for χ34 with swap signs (+,-). No claim about combining independent pure second-order equations into the diagonal problem is introduced here.

## 6. Sources and scope

Reviewed reports: ../null-normalized-monad-lifting/normalized-monad-lifting.md; ../null-normalized-monad-lifting/normalized-monad-lifting-audit.md; ../null-normalized-boundary-comparison/normalized-boundary-comparison.md; ../null-normalized-boundary-comparison/normalized-boundary-symmetry-audit.md; and ../null-dihedral-mixed-vanishing/CHARACTER-AUDIT.md, particularly its twist -2 cohomology discussion. The boundary audit's actual filename is ../null-normalized-boundary-comparison/normalized-boundary-symmetry-audit.md.

The source lineage and accepted rank premises remain as pinned in those reports. No fresh remote authentication or physical/source execution occurred. This report establishes a checked new conditional rank deduction and sharpens the first-order staircase description. It does not establish literal curvature vanishing, a constructed first or second lift, any remaining obstruction-coordinate vanishing.

## 7. Addendum: homological-perturbation staircase and signs

The proposed constructive specification also passes, with the SDR data stated explicitly. Choose a sector-equivariant contraction of the Čech differential onto its cohomology rows, with inclusion i, projection p, and degree -1 homotopy h satisfying

p i=1, δh+hδ=1-i p, h i=0, p h=0, h²=0.

These data can be chosen by equivariant vector-space splittings over C. Merely averaging arbitrary SDR data without checking the side conditions is not a substitute for this choice. In degree-zero Čech cohomology, choose i as the actual inclusion of global sections into Čech zero-cocycles. Let Δ be the totalized internal commutator, including the stated Čech-degree sign. Then D=δ+Δ, and the perturbation formulas are

i'=(1+hΔ)⁻¹i=Σ_j(-hΔ)^j i,
d_eff=pΔ(1+hΔ)⁻¹i.

The plus sign inside the inverse agrees with δh+hδ=1-ip. In particular D i'=i' d_eff. Every hΔ lowers Čech degree by one and raises internal degree by one. For an upper source z in (internal,sheaf)=(-3,4), the lift i'z has five possible components, in (Čech,internal) degrees

(4,-3), (3,-2), (2,-1), (1,0), (0,1),

with coefficients +,-,+,-,+. All subsequent terms vanish by degree. Projection onto cohomology annihilates the intermediate-row outputs. The upper-row same-row differential lands in a zero sector. The surviving transfer is therefore

d₅=pΔ(hΔ)^4i.

Its sign is positive because the fourth power in the alternating series has positive coefficient. This formula uses the totalized Δ, so one must not separately add another Čech sign to it. Under this contraction convention it represents the spectral-sequence d₅ previously identified, rather than evaluating it.

Let c be the literal global closed curvature, placed in the lower cohomology row and included as a Čech zero-cocycle. Since Δc=0, i'c=ic=c. Imported existence and d₅ injectivity specify a unique z satisfying d₅z=-c. The transferred differential on this z has no other component, and hence

D(i'z)=i'd_eff z=-i'c=-c.

Thus a=i'z is a formally specified full first primitive with all five staircase components. This is constructive relative to a chosen contraction and the solution of the injective linear equation. It is not a computed z, an available numerical inverse, or an explicit physical HM primitive. The lift a depends on the contraction; its required symmetry and uniqueness up to gauge follow from equivariance and the accepted Ext¹-sector vanishing. No second-order conclusion follows without evaluating the complete second residual and solving its equation.

## 8. Completed-author-report review: explicit contraction and middle projection

I subsequently reviewed §§4–5 of first-staircase-ranks.md. The added explicit constructions pass.

For the one-factor Čech convention δ(a,b)=b-a, the four monomial cases have the stated signs. In the overlap case 0≤j≤n, inclusion is the diagonal, projection retains the first coefficient, and h(b-a)=(0,b-a); this is precisely id-ip on degree zero. The first-chart-only and second-chart-only cases use (-t^j,0) and (0,t^j), respectively, and contract those summands. The gap n<j<0 gives the retained H¹. All side conditions hold monomial by monomial, and the maps preserve deck parity.

The tensor-product inclusion and projection are compatible with graded permutations. Averaging the tensor homotopy preserves δh+hδ=e=1-ip and hi=ph=0, though not necessarily h²=0. The proposed replacement k=hδh repairs this without changing i,p. Indeed δh²=h²δ, δhδ=δ, and e h=h e=h. Hence δk+kδ=e and k²=hδh²δh=0. Also ki=pk=0. This establishes a genuine equivariant normalized SDR, not just a homotopy equation.

The perturbation formulas for I,P,H and d_K have the correct signs and bounded series. The original Laurent Čech spaces are infinite-dimensional, but consist of finite-support cochains and have finite Čech length; the transferred K is finite-dimensional. The completed report correctly distinguishes these statements. Its internal-degree commutator is totalized with (-1)^(Čech degree), as required.

On the finite complex K¹ --T--> K² --B--> K³, T is injective and B is surjective. With any fixed Hermitian inner products, the Gram operators T*T and BB* are positive definite. Thus L_T=(T*T)⁻¹T* and S_B=B*(BB*)⁻¹ exist. The endomorphisms TL_T and S_BB are orthogonal projections onto im T and im B*, respectively, and their images are orthogonal because BT=0. Therefore

Π₂=id-TL_T-S_BB

is the orthogonal projection onto ker B∩ker T*, of dimension 120. With h_K=L_T on degree two and h_K=S_B on degree three, one gets d_K h_K+h_K d_K=id-Π. Moreover h_K²=0, since L_TS_B=0 follows from T*B*=(BT)*=0. This contracts the two exact summands while retaining the degree-two cohomology, rather than falsely contracting the entire complex.

The prescription u_R=L_T R and a_P=-Iu_R is valid because imported first-order existence places R in im T. It gives Da_P=-R. The author correctly notes that its Čech-degree-zero/internal-degree-one component is a local zero-cochain, not necessarily a global C¹ element, so C¹_S=0 causes no contradiction. The positive Gram inverses and resulting formulas are existence and symbolic prescriptions over C; they are not computed numerical inverse matrices or determined coefficient vectors. The final report retains this distinction and all second-order limitations.
