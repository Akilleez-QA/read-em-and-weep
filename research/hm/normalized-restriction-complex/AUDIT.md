# Historical mathematical audit receipt

This is a preserved review of the source mathematical manuscript, not a fresh review of the publication bytes. Hashes quoted below identify the historical source versions. See [hm-normalized-restriction-PUBLICATION-CHECK.md](../hm-normalized-restriction-PUBLICATION-CHECK.md) for the final-publication review.

# Independent audit of the normalized restriction complex

## Verdict

The proposed line-bundle replacement of the normalized Horrocks–Mumford monad, the endomorphism multiplicities, the two collapsed cohomology rows, the supertrace splitting, and the three-term homological transfer formula are valid over C. They give a genuine finite-dimensional chain-level model of normalized restriction.

Three qualifications are essential:

1. The row-index comparison has degree **+2**, while its total cohomological degree is zero.
2. The primary row map is zero, but the two-homotopy comparison is only **potentially** nonzero. No nonvanishing or rank follows from the construction alone.
3. Ordinary Čech cochain spaces are infinite-dimensional. The final complexes and comparison matrices are finite; the contraction construction is an exact existence-level construction unless explicit splittings or denominator-bounded algorithms are supplied. No evaluated matrix entries are claimed here.

No source-app write, monad-instance evaluation, or matrix-rank computation was used in this audit.

## 1. The line-bundle complex is a valid replacement

Let Y=P^4 and let the normalized HM bundle F be the cohomology in degree zero of

    A=5O(-1) --a--> B=2Ω²(2) --b--> C=5O,

with a a subbundle injection and b a bundle surjection. Exterior powers of the Euler sequence give the exact coresolution

    0 → B --u--> Q0=20O --v--> Q1=10O(1) --w--> Q2=2O(2) → 0.

After dualizing, its two negative line-bundle terms are acyclic on P^4. Consequently restriction induces an isomorphism

    Hom(Q0,C) → Hom(B,C).

Thus b has a unique extension β:Q0→C. It is a constant matrix, and βu=b implies rank β=5. Its kernel K is a constant 15-dimensional vector space tensored with O, hence is isomorphic to 15O after choosing a basis.

The enlarged complex

    A → Q0 → C⊕Q1 → Q2,

has differentials ua, (β,v), and (0,w). The natural inclusion of the original monad is a quasi-isomorphism: its quotient is the exact quotient of the coresolution. Choose a constant splitting s:C→Q0 of β. Under Q0=K⊕s(C), the target automorphism

    (c,q) ↦ (c,q−vs(c))

splits off the contractible C→C pair. Since wvs=0, no extra differential survives. The resulting complex is precisely

    L = [5O(-1) → 15O → 10O(1) → 2O(2)]
          degrees −1,    0,       1,       2.

The first differential factors through K because bua=0, and the next two are v|K and w. Its only cohomology sheaf is F in degree zero.

The basis of K and the splitting s are choices. For a fixed monad this causes no problem. In a varying family of rank-5 constant matrices, a single global identification K≅15O over the entire parameter space need not exist; matrix formulas can instead be made on rank-minor patches, or K can be retained intrinsically.

## 2. Endomorphisms and the strict tracefree summand

Write L^i=r_iO(i), with (r_{−1},r_0,r_1,r_2)=(5,15,10,2). Then

    E=End(L)(−4),
    E^k=m_k O(k−4),
    (m_{−3},…,m_3)=(10,80,245,354,245,80,10).

For example m_0=25+225+100+4=354 and m_1=75+150+20=245. The differential is the graded commutator with d_L. Because L is a bounded locally free complex quasi-isomorphic to the locally free bundle F, E represents End(F)(−4). Pullback to S remains a valid replacement: the quasi-isomorphism to F is preserved by derived pullback, and these locally free complexes compute that derived pullback.

Supertrace is a chain map End(L)→O, concentrated in degree zero. The scalar identity is a chain map in the opposite direction and

    str(id_L)=−5+15−10+2=2.

Therefore P=id_L·str/2 is a strict idempotent chain map, and

    End(L)=ker(str) ⊕ O·id_L.

This is compatible with pullback. The supertrace on cohomology is ordinary trace on End(F), so ker(str) represents End_0(F). The tracefree coefficient in degree zero is 353, while every other m_k is unchanged. Coefficientwise Čech contractions respect this splitting; no homotopy-only replacement of the tracefree projector is necessary.

## 3. Ambient and normalized finite complexes

The line-bundle cohomology calculation is the standard projective-space formula, directly checkable by Laurent monomials on the standard cover: [Stacks Project, Section 30.8](https://stacks.math.columbia.edu/tag/01XS).

On Y, among O(k−4), −3≤k≤3, only k=−3,−2,−1 contribute, all in H^4. Their dimensions are

    10·h^4(O(−7))=150,
    80·h^4(O(−6))=400,
    245·h^4(O(−5))=245.

Thus the ambient finite complex is

    150 → 400 → 245,

in total degrees 1,2,3. The scalar O(−4) is acyclic, so exactly the same dimensions apply to the tracefree complex.

For ν:S=P^1×P^1→Y, ν(l,m)=l³m, the hyperplane pullback is O(3,1). Therefore

    ν*E^k=m_k O(3k−12,k−4).

For k=−3,…,2, both factors have negative degree at most −2, and Künneth gives only H^2, of dimension m_k(11−3k)(3−k). At k=3 the second factor has degree −1 and is acyclic. The complete row dimensions are

    k:          −3     −2      −1       0       1      2
    full End: 1200   6800   13720   11682    3920    400.

These lie in total degrees −1,0,1,2,3,4. The scalar contribution is H^2(O(−12,−4)), of dimension 11·3=33, entirely at k=0. Hence the tracefree target is

    1200 → 6800 → 13720 → 11649 → 3920 → 400,

in those same total degrees. The scalar summand has zero horizontal differential because the identity is closed and the supertrace kills commutators.

The one-row property implies that the transferred differentials within each collapsed complex are just the induced horizontal differentials. All higher perturbation corrections to those differentials vanish by vertical degree.

## 4. A strict common-cover restriction map exists

Take the standard five affine opens U_i=D_+(x_i) of Y, and V_i=ν^{-1}(U_i) in S. The map S→Y is finite: normalization is finite here, and its composition with the closed immersion of the triple-root surface is finite. Consequently every V_i and every indexed intersection is affine. This is exactly the affine-preimage property of finite morphisms; see [Stacks Project, finite morphisms](https://stacks.math.columbia.edu/tag/01WG) and [affine morphisms](https://stacks.math.columbia.edu/tag/01S5).

These covers therefore compute coherent cohomology. Although the target is a surface, the five-open Čech complex has cochain degrees through four; its terms in degrees three and four are generally nonzero and acyclic in cohomology. Pullback is a strict map R between the two Čech double complexes, preserving internal degree k and Čech degree q.

One must not first discard the target's acyclic Čech degrees and then attempt literal termwise restriction: those discarded degrees carry exactly the homotopies needed for the comparison.

## 5. Transfer formula and signs

Use a consistent totalization D=d_v+δ in which d_v and δ anticommute. Here δ raises k by one and d_v raises q by one. On each vertical complex choose a normalized contraction

    id−ip=d_v h+h d_v,
    h²=0, hi=0, ph=0.

For example, choose a vector-space decomposition into boundaries, chosen cohomology representatives, and a complement whose differential is isomorphic to the boundaries in the next degree. The inverse of that differential defines h on boundaries and h is zero on the other two summands. Absorb the totalization sign into h and d_v consistently.

With this sign convention the perturbed inclusion and projection are

    I_A=(1+h_Aδ_A)^−1 i_A,
    P_B=p_B(1+δ_Bh_B)^−1.

The series are finite because h preserves k, δ raises k, and −3≤k≤3. The exact comparison is

    T=P_B R I_A.

The ambient retained row has q=4 and the target retained row q=2. A term with a target homotopies and b ambient homotopies can survive only when a+b=2. Thus the entire comparison is the three-term expression

    T = p_B [ (δ_Bh_B)² R
              + δ_Bh_B R h_Aδ_A
              + R(h_Aδ_A)² ] i_A.

All three signs are positive because the total expansion order is two. This formula is not an approximation. The perturbation identities imply the strict chain identity D_B T=T D_A.

Its internal degree is +2. Its only possibly nonzero components, in the tracefree model, have sizes

    T_{−3}: C^150 → C^13720,
    T_{−2}: C^400 → C^11649,
    T_{−1}: C^245 → C^3920.

These preserve total degree because the retained vertical degree drops from four to two. Explicitly the chain identities are

    d^S_{−1}T_{−3}=T_{−2}d^Y_{−3},
    d^S_0T_{−2}=T_{−1}d^Y_{−2},
    d^S_1T_{−1}=0.

The two-homotopy operator may or may not vanish for the specified HM monad. Its form alone does not settle this. The primary operator p_B R i_A vanishes by bidegree, not because normalized restriction on hypercohomology vanishes.

## 6. Exact meaning of finiteness and canonicity

The retained cohomology spaces have the finite dimensions displayed above, so T consists of three finite matrices after choosing bases. The auxiliary Čech vector spaces and the abstract contractions on them need not themselves be finite-dimensional or effectively specified by the present argument.

There is nevertheless no hidden infinite sum in the construction. Each matrix column requires only finitely many applications of the chosen restriction, differential, homotopy, inclusion, and projection maps. One can also isolate a finite-dimensional auxiliary subcomplex: start with finite bases of all retained cohomology representatives, then close under d_v, h, δ, and the one-way map R. The normalized contraction relations reduce words in d_v and h to finitely many forms, while each δ raises the bounded internal degree and R is used at most once. The resulting closure is finite-dimensional, is stable under the needed maps, and retains the contraction onto all of the finite vertical cohomology spaces.

This last observation proves existence of a finite auxiliary comparison; it is not a supplied algorithm for locating all primitive cochains or evaluating their coefficients. A computational claim would require explicit contractions or an explicit bounded algebraic model.

Different choices of splittings and cohomology representatives yield chain-homotopic comparisons under the corresponding identifications. The induced map on hypercohomology is canonical normalized restriction. By choosing scalar-compatible contractions from the start, the entire construction takes place strictly in the tracefree summand.

## 7. What this does and does not establish

For x representing an ambient H^2 class in the middle term C^400, normalized restriction is represented by T_{−2}x in C^11649. It vanishes precisely when

    d^Y_{−2}x=0 and T_{−2}x belongs to im(d^S_{−1}),

with ambient representatives identified modulo im(d^Y_{−3}). This is an exact finite-complex criterion.

The dimensions of terms do not determine the ranks of their differentials, the rank of normalized restriction, or the separate cusp-gluing correction in the preceding normalization/Gysin proof. Those remain unevaluated. In particular no conclusion about injectivity, vanishing, or the first-ten fourth-power problem follows merely from the construction.

## 8. Audit of the saved proof's exact-tail compression

The completed PROOF.md was read after the independent construction above. No further mathematical error was found. In particular, its row indexing and its additional exactness statements are correct.

The target D has total degree k+2, so it is forced to be exact at k=−3,1,2 because its hypercohomology is the ordinary cohomology of a bundle on a surface. Exactness is **not** automatic at k=−2, which represents H^0 of that bundle. Consequently:

- D^−3→D^−2 is injective, of rank 1200.
- D^1→D^2 is surjective, of rank 400.
- ker(D^1→D^2) has dimension 3920−400=3520.
- Exactness at D^1 gives rank(D^0→D^1)=3520.
- Z_S=ker(D^0→D^1) has dimension 11649−3520=8129.
- H^2(S,G)=Z_S/im(D^−1→D^0); the dimension 8129 belongs to the cycle space, not to the cohomology group.

The previous verified HM input, explicitly recorded in historical-source:fourth-power-cohomology/PROOF.md, is h^1(B_0(−4))=0 and h^1(B_0(−1))=5. Serre duality on P^4 gives h^3(B_0(−4))=5. Applied to C, these imply that its first arrow has rank 150 and its second rank 245−5=240. Therefore Z_Y has dimension 400−240=160, its boundary subspace has dimension 150, and H^2(Y,B_0(−4)) has dimension 10. These rank values are forced by imported cohomology; they are not evaluations of an instantiated monad matrix.

The induced restriction map Z_Y(160)→Z_S(8129), followed by quotienting by the corresponding boundaries, is exactly the same map described in Section 7. Finally,

    −1200+6800−13720+11649−3920+400=9,

which is χ(S,G)=h^0(G)−h^1(G)+h^2(G). Neither h^0 nor h^1 can be discarded solely from this identity.
