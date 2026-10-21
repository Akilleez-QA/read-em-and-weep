# Local mismatch after polynomial ambiguity: no avoidance or injectivity premise

## Contribution and exact scope

PR532 proves a simultaneous-residue map into the corrected target ((I∩J)/IJ), its supported-section kernel with a colon correction, and an isomorphism under avoidance. This note determines its image without avoidance. It combines that ambiguity correction with PR465's local-mismatch mechanism, extends the latter to arbitrary nonnegative multiplier degree r, and proves that the mismatch descends through IJ. Both corrections are identified as coordinate-ring Tor groups, yielding one exact sequence from Tor₂ through the residue space to Tor₁ and local mismatch. It does not claim the local-mismatch idea itself is new.

The result is an algebraic theorem for a disjoint union of projective lines and globally coprime forms. No polynomial restriction is required to be injective. Its HM application retains PR532's explicit evaluation/duality premises and a separate primary subquotient. No selected form/source evaluation, numerical rank, or original-pair vanishing is asserted.

## 1. Setup

Let S=C[x₀,...,x₄], let C be a nonempty disjoint union of m projective lines, and let I=⊕_{j≥0}H⁰I_C(j). Fix nonzero globally coprime homogeneous forms u∈S_a, v∈S_b with a,b≥1, let J=(u,v), and fix r≥0. Set H_j=H⁰O_C(j), with restriction res_j:S_j→H_j. Define

W_r=ker[H_r/res S_r → (H_{r+a}/res S_{r+a})⊕(H_{r+b}/res S_{r+b})],
[λ]↦([uλ],[vλ]),
T_r=((I∩J)/IJ)_{r+a+b}.

A class [λ] belongs to W_r exactly when there are f∈S_{r+a}, g∈S_{r+b} with res f=u|C·λ, res g=v|C·λ. PR532's map is

Φ_r:W_r→T_r, [λ]↦[vf−ug].                       (1)

The ideal-section ambiguities f↦f+α, g↦g+β contribute vα−uβ∈(IJ)_{r+a+b}, so (1) is well-defined.

There is a canonical homological interpretation

T_r≅Tor₁^S(S/I,S/J)_{r+a+b}.                       (1a)

Tensor 0→I→S→S/I→0 with S/J. Since S is free, the resulting exact sequence injects Tor₁^S(S/I,S/J) into I/IJ, with image the kernel of I/IJ→S/J. That kernel is precisely (I∩J)/IJ. This is the coordinate-ring intersection Tor. It is not the primary-extension Tor₁^S(S/J,N) appearing when tensoring an extension of primary and residue cohomology modules, such as the correction mechanism of PR477. They have different modules and different roles and cannot be substituted for each other.

Let C₀ consist of the k lines on which both u and v restrict identically to zero. Let K_r⊂H_r be the subspace supported on C₀. Write

Q_r=K_r/(K_r∩res S_r),
κ_r=dim Q_r=k(r+1)−dim(I:J)_r+dim I_r.             (2)

The second coordinate-ring Tor group gives the other correction:

Tor₂^S(S/I,S/J)_{r+a+b}≅(I:J)_r/I_r.              (2a)

Indeed global coprimality makes u,v a regular sequence in S. Its Koszul resolution has terms S(−a−b)→S(−a)⊕S(−b)→S, with differentials (v,−u) and (u,v). Tensor with S/I. The degree-(r+a+b) second homology is exactly the degree-r classes annihilated by both u and v, namely (I:J)_r/I_r; there is no preceding term. Restriction embeds this group into K_r, with image K_r∩res S_r: annihilation by the pair means precisely that the restriction is supported on the common-contained components, and restriction has kernel I_r.

## 2. Intrinsic local mismatch spaces

For each component l, write u_l=u|l, v_l=v|l and define

Z_l={ (p,q)∈H⁰O_l(r+a)⊕H⁰O_l(r+b) : v_l p=u_l q },
E_l=Z_l/{(u_l λ_l,v_l λ_l): λ_l∈H⁰O_l(r)},
E=⊕_l E_l.                                       (3)

The denominator in (3) is its image subspace, not an assertion that the parameter map is injective; it is zero on a common-contained line. These definitions require no choices of coordinates or gcd generators.

For [h]∈T_r choose h∈(I∩J)_{r+a+b} and a representation h=vf−ug with f∈S_{r+a}, g∈S_{r+b}. Since h vanishes on C, each (f_l,g_l) belongs to Z_l. Define

ε_r([h])=(([f_l,g_l]))_l∈E.                       (4)

There are two independent choices to check:

1. For a fixed polynomial h, two representations differ by (u p,v p) with p∈S_r. This follows from global coprimality and the homogeneous degree bounds: vΔf=uΔg forces Δf=up, Δg=vp. Their restrictions lie in the local denominators in (3).
2. Replacing h by h+vα−uβ for α∈I_{r+a}, β∈I_{r+b} changes a chosen representation to (f+α,g+β). The restrictions are unchanged. Every change by (IJ)_{r+a+b} has this form. Any other representation is handled by step 1.

Thus ε_r is a well-defined linear map on the quotient T_r. The global Koszul ambiguity and the ideal-product ambiguity are both necessary parts of this proof.

## 3. Exactness without avoidance

There is an exact sequence

0→Q_r→W_r --Φ_r→ T_r --ε_r→ E.                    (5)

Exactness is asserted at Q_r, W_r and T_r, not surjectivity onto E.

Using (1a) and (2a), this unfolds into the natural exact sequence

0→Tor₂^S(S/I,S/J)_{r+a+b}→K_r→W_r
  →Tor₁^S(S/I,S/J)_{r+a+b} --ε_r→ ⊕_l E_l.       (5a)

The first map is restriction under the annihilator identification (2a); K_r→W_r is passage to the class modulo global restrictions; W_r→Tor₁ is (1) under (1a). There is again no assertion of surjectivity at the final term. Both Tor groups in (5a) concern the coordinate rings S/I and S/J, not a primary-cohomology extension.

For the left part, if Φ_r([λ])=0, adjust f,g by ideal sections so that vf=ug. Global coprimality then gives f=up, g=vp for p∈S_r. On every line outside C₀, multiplication by at least one nonzero restriction is injective in the binary polynomial ring; hence λ−res p vanishes there. Its class therefore comes from K_r. Conversely, a section supported on C₀ has uλ=vλ=0 and admits f=g=0. Its class maps to zero. Quotienting by K_r∩res S_r proves the left exactness. Finally K_r∩res S_r=res((I:J)_r), with restriction kernel I_r, proving (2).

For exactness at T_r, ε_r([h])=0 means that for the chosen global representation h=vf−ug there is, on every line, a section λ_l∈H⁰O_l(r) such that f_l=u_lλ_l and g_l=v_lλ_l. Because the lines are disjoint, these sections assemble into λ∈H_r. Then [λ]∈W_r and Φ_r([λ])=[h]. On common-contained lines the vanishing mismatch condition forces f_l=g_l=0 and λ_l can be chosen freely. Conversely a residue representation from W_r has zero local mismatch by definition. Therefore im Φ_r=ker ε_r.

## 4. Local dimensions, including zero restrictions

If u_l and v_l are both nonzero, choose a homogeneous gcd h_l of degree δ_l and write u_l=h_l u'_l, v_l=h_l v'_l, where the reduced pair is coprime. Binary unique factorization gives

Z_l={ (u'_l b_l,v'_l b_l): b_l∈H⁰O_l(r+δ_l) }.

The parametrization is injective; the denominator in (3) corresponds precisely to b_l∈h_l H⁰O_l(r). Hence

E_l≅H⁰O_l(r+δ_l)/(h_l H⁰O_l(r)),
dim E_l=δ_l.                                      (6)

The dimension equality uses r≥0 and multiplication by a nonzero h_l. Equivalently, for the degree-δ_l divisor D_l cut out by h_l, the quotient is H⁰(O_{D_l}(r+δ_l)), since H¹O_l(r)=0. Thus multiplicities of common roots are retained. The concrete isomorphism depends on the scalar chosen for h_l; E_l and ε_r do not.

The zero-restriction cases must be treated separately:

- If u_l=0 and v_l≠0, the relation forces p=0 while q is arbitrary. Thus E_l=H⁰O_l(r+b)/(v_l H⁰O_l(r)), dimension b. This agrees with δ_l=deg gcd(0,v_l)=b.
- If v_l=0 and u_l≠0, the relation forces q=0 while p is arbitrary. Thus E_l=H⁰O_l(r+a)/(u_l H⁰O_l(r)), dimension a. This agrees with δ_l=deg gcd(u_l,0)=a.
- If both vanish, the relation is vacuous and the denominator is zero. Thus E_l=H⁰O_l(r+a)⊕H⁰O_l(r+b), dimension 2r+a+b+2. There is no finite common-divisor degree to substitute in this case.

Consequently

e_r:=dim E=k(2r+a+b+2)+Σ_(l outside C₀)δ_l,        (7)

where the sum uses the one-zero conventions just stated.

## 5. Exact dimension formula and bounds

Let t_r=dim T_r. From (5),

dim W_r=κ_r+dim ker ε_r=κ_r+t_r−rank ε_r.           (8)

In particular,

κ_r+max(0,t_r−e_r) ≤ dim W_r ≤ κ_r+t_r.            (9)

There is also the independent ambient bound

dim W_r≤dim(H_r/res S_r)=m(r+1)−dim S_r+dim I_r.   (10)

Combining (8) and (10) gives a necessary lower bound on the mismatch rank when useful. None of these bounds asserts ε_r is onto. Local dimension counts alone never determine its global rank.

The exact residual vanishing criterion is

W_r=0 ⇔ Q_r=0 and ε_r is injective.                (11)

When polynomial restrictions have kernels, Q_r=0 cannot generally be replaced by k=0: supported sections might already be global restrictions. When the relevant restriction maps are injective, κ_r=k(r+1), recovering that simplification.

## 6. Specializations and comparison with the pinned predecessors

Under C∩V(u,v)=∅, no component is common contained and all gcd degrees are zero, so E=0 and Q_r=0. Sequence (5) yields W_r≅T_r, recovering PR532's avoidance theorem.

If I_{r+a}=I_{r+b}=0, then (IJ)_{r+a+b}=0 and Q_r=K_r, since up∈I_{r+a}=0 forces p=0. Thus T_r is the unquotiented intersection and κ_r=k(r+1). With a=4,b=3,r=0, (5) becomes precisely PR465's septic mismatch sequence, and (7) becomes 9k+Σδ_l. In the ordinary quadratic/cubic channel a=2,b=3, the both-zero contributions are 7 at r=0 and 9 at r=1; the supported kernel contributions before global correction are respectively k and 2k.

New relative to PR465: the target and mismatch map descend through IJ, the common-supported kernel retains its global/colon correction, and arbitrary r and a,b are allowed. New relative to PR532: no avoidance assumption is needed to characterize im Φ_r; it is exactly ker ε_r with explicit local obstruction spaces and bounds. Sequence (5a) packages the colon correction and intersection ambiguity as Tor₂ and Tor₁ of the same two coordinate rings. Neither predecessor is being corrected in the scope it actually proves.

For the HM realization, when r+max(a,b)≤4, PR532 identifies the residual dual in degree n=5−r with D*⊗W_r. The full quotient additionally has the primary term P_n/(P_n∩U). Thus (11) describes only residual vanishing; full vanishing also needs primary coverage. No local gcd, mismatch rank, primary coverage or resulting quotient has been evaluated for the original pair.

## Pinned sources

- PR532 at 5f08a072fa8d3bdf12007a6aab2f374c85c5e503, the corrected quotient target and supported/colon kernel:
  https://github.com/Akilleez-QA/read-em-and-weep/blob/5f08a072fa8d3bdf12007a6aab2f374c85c5e503/research/hm/residue-restriction-ambiguity/PROOF.md
- PR465 at c990d553bc12aae7d979bf1ccda996449fcea910, §3, the original squared-quadratic local-mismatch mechanism under injective restrictions:
  https://github.com/Akilleez-QA/read-em-and-weep/blob/c990d553bc12aae7d979bf1ccda996449fcea910/research/hm/squared-quadratic-residue/PROOF.md

This is authored mathematical reasoning for independent checking, not formal machine verification.
