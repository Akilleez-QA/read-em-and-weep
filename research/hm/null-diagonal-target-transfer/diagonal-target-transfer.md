# Exact diagonal-target transfer and regular six-condition extraction

20 October 2026. Formal result and existing review record; actual HM/source values are not evaluated here.

## 1. Finite complex and rank theorem

Use the normalized resolution L=[5N⁻¹→15N→10N³→2N⁵], in degrees -1,0,1,2, with N=O(1,1,1,1). Let J denote the sector invariant under the four decks, a=(12), b=(34), and e=(13)(24). This is the pure DIAGONAL sector, not the separate PP and QQ problems. The multiplicity spaces of End^q L are trivial permutation representations and have dimensions m=(354,245,80,10) for q=0,1,2,3.

In sheaf degree zero, deck invariants in one O(2q) factor have dimension q+1. Taking both pair invariants and then block invariants gives

C^q_J = C^(m_q) ⊗ Sym²(Sym² C^(q+1)).

Thus dim(C⁰,C¹,C²,C³)=(354,1470,1680,550). For negative internal degree -r the even Laurent part of H¹ O(-2r) has dimension r-1. Each internal swap contributes a Künneth minus sign, so the upper row is

H⁴(End^(-r)L)_J = C^(m_r) ⊗ Sym²(Λ² C^(r-1)).

Block interchange exchanges two degree-two factors and has positive Koszul sign. This upper row is U=C¹⁰ at r=3 and zero at r=2,1. There are no other sheaf-cohomology rows.

Choose the equivariant normalized Čech contraction (i,p,h) of ../null-first-staircase-ranks/first-staircase-ranks.md and its audit. With Δ the totalized internal commutator, D=δ+Δ, the transferred complex is exactly

K⁰=C³⁵⁴ → K¹=C¹⁴⁷⁰ ⊕ U → K²=C¹⁶⁸⁰ → K³=C⁵⁵⁰,

d⁰_K(x)=(A₀x,0), d¹_K(y,u)=A₁y+Tu, d²_K(z)=A₂z,

A_q=pΔi on the lower row, T=pΔ(hΔ)⁴i on U.

Here A₁A₀=0, A₂A₁=0, A₂T=0. There is no claim that T itself is canonical independently of contraction; its map U→ker(A₂)/im(A₁) is the spectral d₅.

## 2. Why rank(d₅)=10 is justified

Total Ext¹ has dimension 29, so total dimensions alone do NOT force d₅ injective. An extra structural splitting is essential.

Let F be the underlying four-term line resolution on P⁴, with terms 5O(-1),15O,10O(1),2O(2). Its pullback and root twist give L, and End^q F=O(q)^(m_q). Quotienting first by decks and then by the pair/block group gives the finite compact coefficient algebra

A=O ⊕ W O(-1) ⊕ W² O(-2).

The canonical regular splitting is an O_P⁴-module splitting. Since the differential is pulled back from F, its action on End F⊗A is the identity on A. Therefore this is a splitting of the ENTIRE complex of sheaves, not merely a decomposition of its final cohomology or Hilbert polynomial. Its hypercohomology spectral sequence splits into the three twists j=0,1,2.

The sole upper entry is H⁴(O(-5))^10 in internal degree -3 of the j=2 summand. The j=0 and j=1 summands have no upper entry, since their most negative line is O(-3) or O(-4). Import the accepted H¹(End H(-2))=0. In the j=2 spectral sequence the surviving upper kernel is an associated-graded piece of this zero group. Hence d₅ is injective on all ten dimensions. This is a structural transfer of accepted source cohomology, NOT a fresh verification of the physical HM higher differential.

Consequently rank T=10 and im T∩im A₁=0: if Tu were a lower-row boundary, its spectral d₅ class would vanish, forcing u=0.

The accepted compact Ext vector is (1,29,32,0,0), assembled from twists 0,-1,-2. Ext⁰=1 gives rank A₀=353. Ext³=0 gives rank A₂=550 because there is no other upper source into degree 3. Ext²=32 then gives rank d¹_K=1680-550-32=1098. Subtracting the independent ten-dimensional T image gives rank A₁=1088.

Thus ker A₂ has dimension1130, H²(C_J)=ker A₂/im A₁ has dimension42, and

0 → U --d₅--> H²(C_J) → H²(K) → 0

has dimensions 10→42→32. Degree one checks as (1470-1088)-353=29. The 1480-dimensional K¹ does NOT consist of 1480 gauge-inequivalent choices.

## 3. Full-source projection, with all upper cochains retained

The exact homological perturbation maps are

I=(1+hΔ)⁻¹i, P=p(1+Δh)⁻¹,
H=h(1+Δh)⁻¹, d_K=pΔ(1+hΔ)⁻¹i.

They obey PI=1, PD=d_KP, DI=Id_K, and DH+HD=1-IP. All series are finite because h lowers Čech degree. The sign convention is δh+hδ=1-ip; therefore the inverses are alternating series and the four-h term T has positive sign.

Take the actual symmetry-homogeneous first lifts a_P,a_Q supplied by the first-staircase construction and accepted boundary comparison, retaining all five bidegrees. Form the FULL total-algebra sources

R_PP=a_Pa_P+C_P(d,a_P)+C_P(a_P,d)+C_PP(d,d),
R_QQ=a_Qa_Q+C_Q(d,a_Q)+C_Q(a_Q,d)+C_QQ(d,d).

Let z=e_J(R_PP+R_QQ), where e_J is the finite-group averaging idempotent. The raw class is already in J under the accepted comparison; averaging chooses a J-valued representative and does not alter that class. D z=0. These expressions are used only after the accepted full cusp normalization/ambient gauge and actual first-boundary transport. They are not substitutes for an ungauged PR16 residual with its T(g)g, -μ(b,g), root transport or induced second-order gauge terms omitted.

The transferred source is q=Pz∈K²=C¹⁶⁸⁰, not merely the global component of z. Explicitly decompose z=Σ_(p=0)^4 z_(p,2-p), where the indices are (Čech,internal). Then

q=Σ_(p=0)^4 (-1)^p p₀(Δh)^p z_(p,2-p).

Here p₀ is projection to the lower sheaf-cohomology row. The possible upper projection in degree two is zero since H⁴(End⁻²)_J=0, but intermediate Čech components still contribute through the displayed staircase. In particular one must NOT discard z_(4,-2) or replace P by p. All terms land at internal degree 2 and sheaf degree zero. A₂q=0.

## 4. Exact quotient and primitive contract

The required finite obstruction is

[q] ∈ ker A₂ /(im A₁ + im T), dimension32.

For an explicit representative, choose fixed Hermitian inner products on the finite K spaces. Write J₁=(A₁,T):K¹→K², and let J₁† be its Moore–Penrose inverse (ordinary linear algebra, not the star product). Since A₂ is surjective, set S₂=A₂*(A₂A₂*)⁻¹. Then

Π₂=1-J₁J₁†-S₂A₂

is the orthogonal projector onto ker A₂∩ker J₁*, of dimension32. Its use is purely a symbolic prescription in fixed unevaluated matrices. It requires neither a branch discriminant inverse nor a physical rank evaluation.

The exact test is Π₂q=0. When it holds, v₁=J₁†q satisfies d_Kv₁=q and

b_pure=-I v₁-Hz

satisfies D b_pure=-z. Indeed DHz=z-IPz and DIv₁=Iq. This is an actual primitive contract including the HPL homotopy correction, not merely a restatement that an Ext class should vanish. It is conditional: no q, v₁ or b_pure coefficient is evaluated here.

For the unaveraged pure source, retain a comparison cochain c with z_raw=z+Dc; then b_raw=b_pure-c. Such a c exists from the established class membership and exact sector decomposition; it is not numerically supplied. For the full diagonal add the retained primitive for the separately accepted mixed source. This does not assert that PP and QQ are separately exact or that a two-parameter second lift exists.

## 5. Regular extraction of precisely six remaining conditions

The canonical descent quasi-isomorphisms induce

κ:H²(K) ≅ M=H²(P⁴,End₀H⊗A).

Trace removal changes no H² here. Use the actual regular coefficient map Φ⁻¹ for Φ=(1,σ,τ), τ=σ²-2I, to extract the three summands M₀, W M₁, W² M₂. The constant coefficient is Tr₆/6; the other two are NOT inverse-discriminant trace pairings. These are globally regular coefficient maps, including the branch boundary.

Import the audited actual family polynomiality, D5 covariance and faithful cusp normalization. The normalized cusp diagonal pure class is v=Q(1,0,0) and equals κ[q]. Let λ be the rotation eigenvalue of the A² coefficient in that convention. It is one of the two distinct nontrivial weights of ρ₂. Define the finite Fourier projector

E_λ=(1/5)Σ_(k=0)^4 λ^(-k)T_rot^k.

Avoid confusing T_rot with the staircase map T. With pr_j the regular compact projections, define the six-condition vector

E₆(q)=(pr₁ E_λ κ[q], pr₂ E_λ κ[q])

in (W M₁)_λ ⊕ (W² M₂)_λ, of dimensions 2+4. For the ACTUAL cusp source, the accepted polynomial covariance puts κ[q] wholly in this six-dimensional space, so E₆(q)=0 ⇔ [q]=0. This implication is NOT true for an arbitrary closed q of the 32-dimensional target: it depends on the actual source restriction, and E₆ must not be used to throw away unsupported components.

At the original smooth parameter F₀=(1,0,-1), the pure diagonal class is v+R v. The map v↦v+Rv is injective on this λ eigenspace since Rv has the distinct inverse weight. Therefore these six cusp conditions are equivalent to the original remaining diagonal obstruction test. They are not six new vanishings and do not shrink the ambient Ext² dimension32.

All extraction maps are fixed linear maps on cohomology, with only constant group-order denominators. The optional Hermitian representative above is fixed once the normalized complex is fixed; it is not asserted to be a holomorphic pseudoinverse of a varying family of matrices. The regular family assertion belongs to κ, Φ⁻¹, finite character projectors and the accepted polynomial class, not to a varying adjoint construction.

## 6. Dependencies and limits

Directly reviewed: ../null-normalized-monad-lifting/normalized-monad-lifting.md; ../null-first-staircase-ranks/first-staircase-ranks.md and ../null-first-staircase-ranks/first-staircase-ranks-audit.md; ../null-pure-square-reduction/pure-target-next.md; ../null-branch-polynomial-extension/branch-boundary-extension.md and its actual audit filename ../null-branch-polynomial-extension/branch-boundary-audit.md; ../null-cusp-normalization/cusp-normalization-audit.md. Their pinned source lineages and accepted HM cohomology, actual first-order existence, boundary comparison, compact splitting and polynomial covariance remain imported premises.

Established here: the full diagonal-sector finite complex; the structurally justified d₅ injection; exact conditional ranks; full-source projection; 32-dimensional quotient/projector; regular 2+4 extraction under the accepted actual-source restriction; and a conditional diagonal primitive formula. Not established: any actual source coordinate, literal curvature vanishing, six-condition vanishing, a computed second primitive or a second-order lift.
