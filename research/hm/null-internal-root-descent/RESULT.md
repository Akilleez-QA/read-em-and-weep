# Root inertia does not obstruct the internal transported Morita atlas

## Result and exact scope

The suspected obstruction is real for the **inter-ambient** root Morita equivalence, but it is not an obstruction to the **internal overlap bimodules of the new ambient**. These are different bimodules.

* The equivalence P from the root-transported ambient to the original ambient reduces to N. At an origin ramification point its residue inertia is nontrivial. It cannot satisfy the invariant-generator criterion or descend with its inverse evaluation maps to a coarse Morita equivalence.
* An internal new overlap is Q_i tensor B_ij tensor P_j, where Q_i is inverse to P_i and B_ij is the original overlap. Its residue character is the ratio of the two root characters, times the original overlap character. The two root characters are the action on the SAME intrinsic fiber N_x. They cancel. For the stipulated original regular overlap, the remaining character is trivial.
* Hence actual coherent root transport, followed by the supplied nilpotent strictification, DOES satisfy the missing local residue-inertia condition for its internal overlaps. This is independent of whether N itself descends. There is no root-inertia counterexample to this local conclusion.

This closes the local character premise, on a common geometric stabilizer chart or compatible orbit chart, for the actual root transport. It does not supply an effective global quotient atlas by itself, prove a comparison with the independently prescribed corrected ambient, or construct a quantum carrier module. Full unary maps and triple units through the mixed coefficient still have to be compared. All thirty retained physical values remain unknown.

Only static reading and universal formal algebra were used. No physical source/model/jet execution, imports, matrices, parameter search, experiment.

## Sources read

Historical context: [6266447817](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6266447817). The four relevant consecutive coordination updates 6263865869, 6264327093, 6265444022, and 6266447817 were read (the preceding supplied audits also retain their earlier source pins).

Mathematical dependencies:

1. [research/hm/null-actual-source-factorization/classical-root/RESULT.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/c9bb53d934ad86e50d8519a35d663f9a96fa481d/research/hm/null-actual-source-factorization/classical-root/RESULT.md): genuine N, its groupoid linearization, and χ_N,x(g)=product of ε_i for coordinates at O.
2. [research/hm/null-invariant-coefficient-ideal/RESULT.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/64b6c62a23db6189186896285c956133608ad3c7/research/hm/null-invariant-coefficient-ideal/RESULT.md): original invariant coefficient ideals and bracket; no assertion there identifies the root-transported ambient.
3. [research/hm/null-strictification-gluing/invariant-gluing-0841/RESULT.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/dcecef425c41063dc3ddc42f5285ee39c42e431e/research/hm/null-strictification-gluing/invariant-gluing-0841/RESULT.md): invariant-generator, tensor-comparison, and strictification-transport criteria.
4. [research/hm/null-pair-swap-coherence/RESULT.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/0050df8fa957b9f7f5e1b21137c63bffc646a1eb/research/hm/null-pair-swap-coherence/RESULT.md): genuine ambient action on the antisymmetrized square-zero representative, and exact transport back to the ordered representative.
5. [research/hm/null-root-morita-inertia/root-morita-0719/RESULT.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/711c6bf8c6248f46d73661be8a42ede671a3712b/research/hm/null-root-morita-inertia/root-morita-0719/RESULT.md): exact groupoid root gauge and inter-ambient bimodule formulas.
6. [research/hm/null-strictification-gluing/strictification-0736/RESULT.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/dcecef425c41063dc3ddc42f5285ee39c42e431e/research/hm/null-strictification-gluing/strictification-0736/RESULT.md): finite-group nilpotent strictification by gauges congruent to 1.

The source-bound classical carrier is [the pinned carrier definition](https://github.com/Akilleez-QA/read-em-and-weep/blob/3bdc6cb28ecd75cfefb3cb0d85f42d5bcde8cc7f/research/hm-carrier-and-atlas.md#L11-L15), as already inspected in item 1. No new certification of physical formula inputs is claimed here.

## 1. Local datum and the three different objects

Work in characteristic zero. Fix a geometric point x and its finite stabilizer H. On a common local chart let D_i be the original local deformation algebras, with nilpotent reduction ideals J_i and reduction the geometric local structure ring. The residue field is fixed pointwise by H. For the specified mixed truncation J=(s,t) has J^3=0, even though st need not vanish.

Use the original coherent action and internal rank-one overlap B_ij. In the antisymmetrized presentation these overlaps are regular, their group operators are coefficientwise, and their reductions have invariant generator 1. The central swap gauges of the ordered presentation are congruent to 1, so the same residue assertion holds there. Actual triple units and their pentagon, rather than only inner automorphisms, are part of the stipulated input.

There are three objects to keep distinct:

(1) A candidate carrier M reducing to F=N tensor p*E. Its residue inertia is χ_N times the identity.

(2) The inter-ambient invertible bimodule P_i, reducing to the local root line N_i, and its inverse Q_i, reducing to N_i inverse. The transported carrier Q_i tensor M therefore has trivial classical inertia, conditionally on M and its specified equivariance existing.

(3) The INTERNAL overlap of the transported ambient:

    B'_ij = Q_i tensor_(D_i) B_ij tensor_(D_j) P_j.

It is a (D'_i,D'_j)-bimodule. Both a left and a right root factor occur. Forgetting either factor confuses (3) with (2).

Composition of the B'_ij is obtained from original composition of the B_ij and evaluation P_j tensor Q_j -> D_j. Associativity follows from original associativity and the Morita evaluation identities. This construction uses actual equivariant/weak-equivariant tensor data; it is not a proposed operation on invariants.

## 2. Exact residue cancellation

At x the original overlap has character 1. The inverse and direct root factors have characters χ_N,x inverse and χ_N,x. Therefore

    χ_(B'_ij),x(g) = χ_N,x(g)^(-1) · 1 · χ_N,x(g) = 1

for EVERY element of H. This includes decorated permutations, higher stabilizer intersections, and the origin branch locus. It is not enough to check only generic reflections, but the displayed identity already holds for the entire stabilizer.

The equality of the two characters is intrinsic. Two root charts do not define different root lines at x: they are two trivializations of the same genuinely linearized N. For example, if n_j=f_ij n_i, with f_ij a unit on the overlap, and

    g(n_i)=c_i(g)n_i,

then

    c_j(g)=g(f_ij)c_i(g)/f_ij.

At a fixed geometric point g(f_ij)(x)=f_ij(x). Thus c_i(g)(x)=c_j(g)(x), even though the functions c_i(g), c_j(g) need not agree on the whole overlap. The reduction of B'_ij is the corresponding Hom line, with character c_i inverse c_j, and has trivial fiber inertia. In this elementary presentation f_ij inverse times the Hom-frame is invariant.

For a general original overlap character β_ij,x, root transport gives β_ij,x, not automatic triviality. Thus this conclusion uses the original ambient's regular residue-trivial overlap. A genuine root cannot repair an unrelated preexisting overlap inertia obstruction.

If the group permutes chart labels, take the full action/Čech groupoid and transport the labels as well. The above calculation is at an actual stabilizer arrow after identifying both root fibers with N_x. It does not assert that a group element moving x acts on the single local ring at x.

## 3. Weak actions, strictification, and invariant generators

For specificity, a local root gauge with units q_i(g) lifting c_i(g) changes the chart action to

    α'_i(g)=Ad(q_i(g)^(-1)) α_i(g).

The inter-ambient operator on P_i is p -> α_i(g)(p)q_i(g). On Q_i it is p -> q_i(g)^(-1)α_i(g)(p). Accordingly the operator on B'_ij is obtained by the ordered left/right rule

    σ'_ij(g)(b)=q_i(g)^(-1) σ_ij(g)(b) q_j(g),

using the underlying regular local identifications. The resulting chart group coherence units need not equal 1. They DO reduce to 1, because the classical c_i are the cocycle of a genuine line. All weak bimodule identities are the exact identities inherited from the groupoid gauge, including central coherence.

Apply nilpotent strictification to each chart. It supplies d_i(g) in 1+J_i, and changes overlap operators by

    σ''_ij(g)(b)=d_i(g) σ'_ij(g)(b) d_j(g)^(-1).

The exact weak bimodule identity then gives a genuine group action on each overlap, and the same composition maps remain equivariant: the adjacent d_j inverse and d_j cancel in balanced tensor products. Since d_i and d_j reduce to 1, residue inertia is unchanged. In particular it remains trivial on B'_ij; it remains nontrivial on P_i wherever χ_N is nontrivial.

Now average a lift of a nonzero invariant residue generator of B'_ij over H. Its residue is unchanged, so the average is still a left basis by the local Nakayama argument. Thus B'_ij has an invariant local generator. Its invariants are an invertible bimodule between the chart invariant rings; the canonical tensor comparisons and all given compositions are isomorphisms, exactly by the invariant-gluing proof.

No equality of the different chart gauges d_i is needed. No choice of a quantum module quantizing N in the original ambient is needed. The bimodules are the formal change-of-ambient equivalence and its internal composites.

This proves the needed LOCAL condition for actual coherent root transport. A global application still has to exhibit sheaf charts/restrictions or a valid orbit/stabilizer construction on the chosen downstairs site. A collection of unrelated formal-completion calculations is not, by itself, an effective sheaf atlas.

## 4. Reflection chart: the real obstruction and why it is not a new-ambient obstruction

Here is a completely synthetic classical example. Put

    R=k[[z,w]],  g(z)=-z,  g(w)=w,
    A=R^H=k[[u,w]],  u=z²,  H={1,g}.

Let P=R e be the regular invertible (R,R)-bimodule with g(e)=-e, and Q=R e* its inverse with g(e*)=-e*. Their evaluation is e tensor e* -> 1. Then

    P^H=A·(z e),     Q^H=A·(z e*).

Each invariant module happens to be abstractly free of rank one over A. That observation does NOT make invariant formation a Morita transport: the canonical invariant evaluation sends

    (z e) tensor (z e*) -> u.

It is multiplication by the branch equation u and is not an isomorphism. Likewise R tensor_A P^H -> P has image zP, so P is not recovered from its invariants. This is the precise failure of ordinary coarse descent of the sign root. It is stronger and more accurate than saying its invariant module must fail to be abstractly free.

In contrast, the internal transported overlap with the SAME root on both sides is

    Q tensor_R R tensor_R P.

Its generator e* tensor 1 tensor e is invariant, its character is (-1)(-1)=1, and its evaluation identifies it equivariantly with R. Its invariant overlap is the regular A-bimodule with unit evaluation. The carrier example M=P tensor_R R^r likewise untwists to R^r, whereas P itself still has sign inertia.

The same distinction persists under any nilpotent deformation meeting the earlier coherent-action hypotheses. A deformation or a gauge congruent to 1 cannot change a nontrivial residue sign. Conversely, the paired internal factors already have trivial residue, and strictification plus averaging lifts that triviality to an invariant quantum basis.

At an origin branch chart the root coefficient c(g)=-1 can be lifted literally to the central unit -1. Its inner conjugation is the identity: α'=Ad(-1)α=α. Thus the nontrivial root fiber character can coexist with an entirely ordinary chart algebra action. It lives in P and in the carrier's representation sector, not in a nontrivial automorphism of scalar residue algebras.

## 5. What can and cannot be absorbed

A change of root frame multiplies c_i(g) by g(f)/f. At a fixed point this ratio is 1. Therefore a regular frame change cannot remove the root sign from P. Nilpotent inner strictification cannot remove it either. Multiplying an algebra action itself by a scalar character is not an alternative: it sends 1 to that scalar and fails to be a unital algebra automorphism. Conjugation by the scalar -1 is the identity and consequently does not remove the sign from P's operator.

One CAN tensor an equivariant module by an inverse character locally. But doing so changes its equivariant representation sector. It is exactly the root cancellation operation, not a descent of the original P with its specified equivariance. Globally the actual root's character is +1 at finite branch points and -1 at O; the supplied root-line audit proves that no single global character twist removes both.

A stack/action-groupoid formulation is therefore the natural place to retain the full inter-ambient equivalence P and all inertia sectors. A new nontrivial projective gerbe is NOT forced by this sign: the actual root linearization is genuine. Conversely, the new ambient's internal overlaps are already character-neutral, so their local coarse invariant descent does not require retaining root inertia in the target. Failure to descend the equivalence P is not failure to descend the new ambient.

## 6. Precise remaining work

The local invariant-overlap residue premise is now proved from the supplied genuine root and coherent original ambient, with the stated local chart hypotheses. It should no longer be listed as an unexplained potential root-character obstruction.

Still separate:

* An effective global quotient-site atlas with the actual algebras, overlaps, all restrictions, orbit transport, and composition maps.
* The complete comparison of that invariant root-transported atlas to the prescribed corrected downstairs ambient, including unary maps, full triple units, and mixed st terms.
* Existence of a candidate quantum carrier with the intended equivariance, and its remaining mixed obstruction.

Matching original coefficient ideals and brackets does not perform the second comparison. Carrier inertia cancellation alone did not prove the present result; the two-sided internal-overlap calculation does.
