# Finite rank-five support: a 784-point bound and six surviving sizes

## Statement and conditional inputs

Retain the standing complex projective Schrödinger normalizer N=A⋊K, A=F5², K=SL2(F5), of order 3000, and the actual equivariant linear 20-by-15 matrix b. Write Zj for the support of rank Q≤j, where rank b=4+rank Q. Import:

1. Z4 is empty, dim Z9≤2, and the span Lk of the degree-k minors of b has base support Z_(k−5). See ../mixed-minor-rank-four-exclusion/GLOBAL_EMPTINESS.md and PROOF.md.
2. Z5 has no curve components except possibly the canonical orbit of twenty-five conics: ../rank-five-curve-classification/PROOF.md.
3. Those conics are disjoint from Z5: ../rank-five-canonical-conic-exclusion/PROOF.md. This is a dependency to audit, not independently re-proved here.
4. The canonical negative lines and the thirty Heisenberg eigenpoints E are disjoint from Z5: ../rank-four-canonical-conic-exclusion/LINE_ADDENDUM.md and ../heisenberg-eigenpoint-rank-six/PROOF.md.
5. Outside E, A acts freely; all point orbits have size at least250; there is exactly one orbit O250 of size250. See ../normalizer-refined-point-gap/PROOF.md and ../normalizer-250-simple-defect/PROOF.md.

Then Z5 is finite and

    |Z5,red| ≤784.

There is a unique point orbit O375 of size375. Any orbit occurring in Z5 has size250,375,600, or750. The 250- and375-point orbits can each occur at most once. Consequently

    |Z5,red| ∈ {0,250,375,600,625,750}.

The600-point possibility is the unique nonzero-cocycle orbit M from the order-five classification. The case625 means exactly O250∪O375. Each of the other nonzero cases means one orbit of its displayed size. These are necessary alternatives, not existence assertions. In particular this argument does not exclude isolated rank-five points.

## 1. A finite complete intersection of degrees (10,10,14,14)

Inputs2–3 and dim Z5≤1 give dim Z5≤0. Choose f∈L10 nonzero and avoiding all positive-dimensional irreducible components of Z9. None is in the finite base support Z5. Thus V(f)∩Z9 has dimension at most one.

Choose g∈L10 avoiding both all three-dimensional components of V(f) and all curve components of V(f)∩Z9. Again no such component lies in Z5. Then f,g is a regular sequence, its zero set Y is a pure surface, and Y∩Z9 is finite.

Choose h∈L14 avoiding every surface component of Y. This is possible since its base support Z9 meets Y only in finitely many points. The complete intersection V(f,g,h) is a pure curve. Choose k∈L14 avoiding all its curve components; none is in Z9, since it is contained in Y. The Cohen–Macaulay and unmixed properties at each step give a regular sequence f,g,h,k and a zero-dimensional complete intersection

    W=V(f,g,h,k),    length(W)=10²·14²=19600.

All four equations vanish on Z5.

## 2. Local contribution at least25 at each point

At p∈Z5, R=O_(P4,p) is regular local of dimension four. Its residue matrix has rank9 (rank at most9 would also suffice). Splitting an invertible residue-rank block over R shows

    I10(b)R⊂m,    I14(b)R⊂m⁵.

Thus the parameter ideal q=(f,g,h,k)R has orders at least(1,1,5,5). The parameter ideal q'=(f⁵,g⁵,h,k)R is contained in m⁵. Since (q')^n⊂m^(5n), the regular-sequence colength formula yields

    length(R/q') binom(n+3,4) ≥ binom(5n+3,4).

Leading coefficients give length(R/q')≥625. Powers of members of a parameter regular sequence multiply colengths, by the nonzerodivisor filtration after permuting the sequence. Hence

    length(R/q')=25 length(R/q),    length(R/q)≥25.

Summing over the distinct points of Z5 proves 25|Z5,red|≤19600 and therefore |Z5,red|≤784. This bounds the reduced support; it does not assert a bound or a formula for the determinantal scheme's length.

## 3. Exhaustion of the orbit sizes in range

Outside E a stabilizer S injects into K. Therefore its point orbit has size25k with k=[K:L] dividing120, where L is the projected subgroup. The gap k≥10 and the bound25k≤784 leave precisely

    k=10,12,15,20,24,30,
    orbit sizes250,300,375,500,600,750.

If |S| is even, its projection contains the unique involution c=−I of K. The central-involution cocycle argument conjugates S by an element of A into K: for its cocycle t,

    2t(g)=t(c)−g t(c),

so t(g)=a−ga with a=t(c)/2. We may then analyze the standard splitting V=T⊕W, dim T=3 and dim W=2, with c positive on T and negative on W. T has its nondegenerate K-invariant quadratic form q, whose zero conic C is canonical. P(W) is the canonical negative line.

## 4. No orbit of size500 can occur

Such a stabilizer has order6. Its subgroup in K is C6: it contains c and an order-three element a, and these commuting elements already generate the subgroup. The universal character calculation in ../normalizer-250-simple-defect/PROOF.md, Section3, gives

    Spec(a|T)={1,ω,ω²},    Spec(a|W)={ω,ω²}.

A line stable under both a and c is one of these five simple eigenlines, since it lies in T or W. The two W lines lie on the excluded negative line. The two nonunit T eigenlines are isotropic: q(av)=q(v) and av=λv imply (λ²−1)q(v)=0, and λ=ω orω² has λ²≠1. Thus they lie on the excluded conic C.

The remaining T eigenline is the unique a-fixed axis. It is stabilized by the full order12 normalizer of ⟨a⟩ in K: every normalizer element preserves the one-dimensional a-fixed space in T. It is precisely a point of O250, by the cited unique-axis proof. In particular it cannot have stabilizer order6. Hence the fixed points of C6 offer no eligible genuine500-point orbit.

## 5. No orbit of size300 can occur

Such a stabilizer has order10. Its projection is C10: c is central and commutes with a Sylow-five subgroup, and together they generate all ten elements. After conjugacy in K, use the universal Schrödinger model

    D e_j=ζ^(j²)e_j,    c e_j=e_−j.

Scalar normalizations of D do not change its eigenlines. Simultaneous D,c eigenlines are

    Ce0,  C(e1+e−1),  C(e2+e−2),  C(e1−e−1),  C(e2−e−2).

The first point lies in E. The last two lie in W, so are excluded. The two remaining positive lines lie on C. Here is a scalar-safe verification. The honest order-five shear lift in K differs from the displayed D by a scalar η. Since its fifth power is the identity, η⁵=1. On T the displayed D has eigenvalues1,ζ,ζ⁴ and determinant1. The determinant of the honest T representation is a character of perfect K, hence trivial. Thus η³=1 as well, forcing η=1. Therefore the honest positive eigenvalues are1,ζ,ζ⁴. Invariance of q makes the latter two eigenlines isotropic, since neither eigenvalue squares to1.

Thus all C10 fixed points lie in E, a canonical conic, or a canonical negative line. No300-point orbit can occur.

## 6. The unique375-point orbit

An order8 subgroup L of K is quaternion Q8. Indeed its quotient by c is an order4 subgroup of A5, hence V4, while K has a unique involution; the inverse image is Q8. All such subgroups are conjugate by Sylow conjugacy.

On T, the restricted character on V4 is3 at identity and−1 at each nonidentity element, by the universal order-four trace calculation. Thus T is the direct sum of the three distinct nontrivial V4 characters. There are exactly three L-stable lines in T. There is no L-stable line in W, because c is a commutator in Q8 but acts by−1 on W, whereas a one-dimensional character is trivial on commutators. Hence these three are all projective fixed points of L.

They are not in E, since an E-stabilizer has order100, not divisible by8. Each has stabilizer order divisible by8 and orbit size at least250 and at most375. From the enumerated possibilities in this interval, only375 has stabilizer order divisible by8. Thus each point has stabilizer exactly8.

The normalizer of V4 in A5 is A4. Its order-three quotient cyclically permutes the three nontrivial characters, hence cyclically permutes the three fixed lines. Its inverse image in K does the same. Sylow conjugacy, followed by this transitivity and the A-cocycle conjugation, proves that all375-point orbits coincide. Denote the resulting unique orbit by O375.

For geometric clarity, the three lines in T are pairwise q-orthogonal, because their V4 characters are distinct and self-inverse. Nondegeneracy of q therefore makes each nonisotropic. They avoid the standard conic and negative line. Moreover a point outside E can be fixed by at most one projective involution of N: distinct involutions have form(a,c),(b,c), and their product is the nonzero translation a−b, contradicting free A-action. Thus O375 avoids all the translated canonical conics and negative lines as well. This does not itself prove it belongs to Z5.

## 7. Remaining support types and locations

Removing300 and500 from Section3 leaves250,375,600,750. Since250 and375 each have exactly one orbit, the bound784 permits only

    empty; O250; O375; one600-point orbit; O250∪O375; one750-point orbit.

No two600-point orbits fit. A600-point orbit cannot be combined with any other eligible orbit. A750-point orbit cannot be combined with any other eligible orbit. Neither three250-point orbits nor two375-point orbits are available, because these orbits are unique.

The600-point stabilizer has order5. The following refinement excludes every zero-cocycle class, leaving only the unique nonzero-cocycle orbit M of ../order-five-rank-three-classification/PROOF.md, Sections1,3,4.

### 7.1. No point of Z5 lies on an eigenpair line

Consider L=P(U), where U=⟨e_j,e_−j⟩ for j=1 or2. The universal two-dimensional image lemma in ../order-three-rank-point-bound/PROOF.md, Section1, applies to every two-dimensional U. For clarity, choose a nonzero alternating form det on U. Outer symmetry and cyclic zero imply

    f(x,u,y)=h(det(x,u)y+det(y,u)x),

for a linear h:U→J. Repeated-input injectivity makes h injective: if h(v)=0 for nonzero v, choose w independent of v and obtain f(v,v,w)=det(w,v)h(v)=0, a contradiction. Thus H=im h has dimension2, and b_u(Sym²U)=H for every nonzero u∈U (use the inputs uw and w² for w independent of u).

Project b to J/H, obtaining the linear pencil

    B: O_L(−1)⊗(Sym²V/Sym²U) → (J/H)⊗O_L,
    rank B_u=rank b_u−2.

At either coordinate endpoint, which lies in E, rank b≥10, so rank B≥8. Some8-minor of B is therefore a nonzero degree-eight polynomial on L. At any point in Z5, rank b≤9 and rank B≤7, so that minor vanishes. Consequently |Z5,red∩L|≤8.

The clock Z and inversion R preserve L and act effectively as D10. Away from the two coordinate endpoints, the nonfree points are exactly the reflection-fixed points of Z^kR. The shear D commutes projectively with both Z and R and fixes L pointwise, so every such reflection-fixed point is fixed by an order10 subgroup generated by D and Z^kR. Section5 excludes it from Z5. Equivalently the negative reflection eigenpoint lies on its canonical negative line and the positive eigenpoint lies on its canonical conic. The endpoints are already excluded by E.

Every remaining point of L has a ten-point D10 orbit. Equivariance would place that entire orbit inside Z5∩L, contradicting the bound8. Hence Z5∩L is empty. Normalizer equivariance proves the same for all translates of these eigenpair lines.

A zero-cocycle order-five subgroup is conjugate to ⟨D⟩, whose fixed locus is Ce0 plus these two lines. All are now excluded. The order-five classification proves that all nonzero-cocycle subgroups' eigenpoints comprise one unique600-point orbit M; its proof is purely group-theoretic and does not require the rank-three-specific exclusions. Thus the600-point case here is exactly M.

This argument genuinely uses the quotient pencil and its degree-eight minors. The original degree-ten minors alone would not exclude a ten-point orbit on P1.

In the750-point case, the stabilizer has order4 and is A-conjugate to C4≤K. An order-four generator u has spectrum on T equal to{1,−1,−1} and on W equal to{i,−i}. The W eigenpoints are excluded. The T eigenvalue1 axis is one of the three Q8-fixed lines of Section6, hence has orbit375. Therefore a genuine750-point candidate must lie on the line P(T_(u=−1)) in the positive reflection plane, with all points already in excluded loci removed. This is a location constraint, not a rank assertion.

## Scope and requested audit

The argument uses universal finite-group representations, finite prime avoidance, and local regular-sequence multiplicities only. No actual operation coefficients, source tensors, chosen-input values, rank instances, jets, or residues were evaluated. No actual source-instance evaluation is claimed.

Audit priorities: the dependency on the new pointwise conic theorem; the four-equation avoidance construction; the local25 contribution; the C6/C10 fixed-point exclusions; quaternion fixed-line uniqueness; and the constant binary-image quotient supplying genuine degree-eight equations for Z5 on each eigenpair line.
