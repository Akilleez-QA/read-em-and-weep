> Scope: the projective lift, the explicit weighted-root-gerbe comparison, and the actual mixed-class covariance are distinct claims. The last remains conditional on the stated source identities and pair-character vanishing premises. It is not equality of raw cochains or a preferred same-object action. This packet extends the central comparison to a relative P39 family, not a new claim of the earlier central covariance theorem.

# A 39-dimensional inversion-fixed coefficient family

## Statement and separated inputs

Work in characteristic zero over a field containing i. Use X=C^4, Y=(P1)^4, q:X→Y, N, the normalized HM bundle H, and the actual source premises of ../relative-obstruction-locus/PROOF.md. Write p={0,1}, qpair={2,3}, and χ for the full deck sign. The symbol qpair distinguishes the pair from the covering map q.

Assume the geometric presentation P of that relative theorem. Its central-dimension input D is supplied by the independent classical-cohomology proof in ../../cubic-loci/foundation-p01/INVARIANT-COHOMOLOGY.md; no historical numerical certificate is required. Assume its separate actual-source premises S, together with the audited actual mixed-gauge identification [R]=tf([M]) and root-gerbe transport in ROOT-GERBE-TRANSPORT.md. The uniform literal-source purity and closure are supplied by ../relative-mixed-character-purity/PROOF.md. These remain inherited inputs, not newly authenticated computations.

There is a smooth connected affine neighborhood B+ of the elementary-symmetric tuple u in a projective linear space P39 inside the original P79 coefficient space such that:

1. Every tuple generates O_Y(1,1,1,1) and has five independent entries.
2. The actual family has a coherent projective order-four lift of simultaneous physical inversion a over the identity of B+.
3. The full-sign bundle V=(R²π_*End_0 E)_χ has rank352, commutes with arbitrary base change, and carries a regular involution A.
4. The actual relative mixed class r lies in V+=ker(A−1), including after arbitrary base change. This is actual cohomology-class covariance, not covariance of raw cochains or a selected contraction.

The independently audited theorem ../../cubic-loci/foundation-p03/INVERSION-EIGENSPACES.md, §§1–4 (review: ../inversion-eigenspaces/AUDIT.md), proves tr(A|V_u)=0 from the classical cohomology row, full-coefficient Kodaira–Spencer theorem, and projective lift. Consequently V+ and V− both have rank176. This representation-theoretic input is distinct from the actual-source transport inputs; conclusions 1–4 and constant-rank splitting do not depend on its numerical trace computation.

## 1. Scheme-theoretic fixed component

Let M=O_Y(1,1,1,1), W=H⁰(Y,M), and Vcoef=k^5⊗W. Choose homogeneous coordinates [s_d:t_d] on each P1. Simultaneous inversion a_Y exchanges s_d,t_d. Its natural order-two linearization on M induces J_W=swap⊗swap⊗swap⊗swap on W. Each two-dimensional swap has trace zero, so tr(J_W)=0 and dim W=16.

Let R reverse the five output coordinates, indexed 0,…,4. It has trace1 (two exchanged pairs and one fixed coordinate). Set J=R⊗J_W on Vcoef. Thus J²=1, dim Vcoef=80, tr J=1·0=0, and Vcoef=Vcoef,+⊕Vcoef,− with each summand dimension40. These are tensor-character identities, not a model-matrix calculation.

The projective fixed locus of J is scheme-theoretically P(Vcoef,+) disjoint union P(Vcoef,−). Indeed in characteristic different from two, a J-stable line is locally an eigenline: the induced involution on a line is multiplication by a unit λ with λ²=1, and (1±λ)/2 splits the base into open-and-closed plus/minus parts. This also proves the statement on nonreduced test schemes. Equivalently on a plus projective chart the mixed minus coordinates are cut out by twice themselves.

Write the elementary tuple as (E_0,…,E_4), where E_j is the sum of degree-four squarefree homogeneous monomials using t in exactly j factors and s in the others. Swapping s and t sends E_j to E_(4−j), so Ju=u. Consequently its fixed component is P(Vcoef,+)=P39, smooth of dimension39. Nothing here takes an S4 quotient or assumes permutation symmetry of arbitrary plus tuples.

## 2. The needed nonempty open

The generating locus is open: the universal common-zero incidence in Y×P(Vcoef) is closed, and its projection is closed because Y is proper. Its complement is the generating locus. It contains u by the symmetric quotient morphism Y→Sym⁴P1=P4. Independence is an open determinantal condition on the map k^5→W. It holds at u since the five E_j have disjoint nonempty monomial supports.

Intersect P39 with these two opens, with the rank352/base-change neighborhood B from the relative obstruction theorem, and with the open neighborhoods where

    H^j(X,End E_b)_χp=H^j(X,End E_b)_χqpair=0, j=0,1.

The last opens contain u by ../pair-character-vanishing/PROOF.md and upper semicontinuity for the two character summands of perfect proper pushforwards. Choose a projective affine chart containing u and normalize a plus tuple by ℓ(F)=1. One may choose ℓ on Vcoef,+ and extend it J-invariantly to Vcoef; then normalized universal tuples satisfy JF=F as an exact identity. Finally take a connected affine open neighborhood B+ of u in this intersection. It is smooth of dimension39.

This is an open-neighborhood theorem, not a claim that pair-character vanishing holds on the whole P39 generating locus. The restriction of V from B has rank352 and arbitrary-base-change compatibility. Scalar End contributions do not change this full-sign degree-two bundle: H²(X,O_X)_χ=0, because on each elliptic factor the minus deck character appears in H¹, so the full sign appears only in degree4. Thus End and End_0 give the same V.

For later use the pair-character derived pushforwards have no cohomology in degrees≤1, universally over B+. One way to see the required strengthening is to use local perfect complexes: fiber vanishing in degrees≤1 allows the low-degree terms to be split off by invertible minors, leaving a complex supported in degrees≥2. The character cohomology has no negative fiber degrees to begin with. Such local splittings survive arbitrary base change. On any affine parameter patch T, the corresponding absolute pair-character H¹(X×T,End E_T) is therefore zero, by the affine Leray spectral sequence. This avoids replacing universal gauge exactness by only a pointwise statement.

## 3. A genuine relative projective lift

Let f:Y×B+→P4 be the universal map. The coefficient identity JF=F says

    f(a_Y y,b)=R f(y,b)

as a scheme identity. Compose with the fixed covering q. The coherent target projective lift r of R, with r²=1, supplied by the audited HM chain theorem therefore defines

    (x,b,h) ↦ (a x,b,r h)

on P(E)= (X×B+)×_(P4)P(H). Its square is simultaneous deck inversion d_all and its fourth power is identity. This construction is relative algebraic, not a fiberwise choice of isomorphisms. It commutes with every individual deck transformation.

At bundle level a*N=N⊗Q, Q=external product O_C(T−O), so a*E≅E⊗Q over B+. The scalar twist Q is fixed over the parameter space. Projectivization and End conjugation eliminate it. The resulting algebra automorphism of the relative End object commutes with deck projection. On V its square is χ(d_all)=(-1)^4=1. Hence A²=1 globally, and the idempotents (1±A)/2 split V into locally free summands V±, compatible with every base change. On connected B+ their ranks are constant; the cited audited central trace-zero theorem makes both ranks176.

This family construction does not require proving uniqueness of every projective lift in every fiber. The explicit coherent target lift already supplies the specified action.

## 4. Uniform transport of the actual weighted problem

We explain why the audited transport is a relative identity, rather than just its application separately to geometric points. All physical geometry, legal root opens, derivations, and scalar gerbe data are constant over B+. On a common refinement of the legal cover and its a-pullback, with old/new masks m_i,n_i, put

    h_d,i=(m_i,d+n_i,d−1)y_d/x_d.

Exactly the audited pole argument proves these functions regular on the product opens, also over an arbitrary parameter base. The identity a*q_d^(n)=i(δh_d−q_d) holds as a regular cochain identity with coefficients over that base. For each pair r=(a,b), C=15/4 and

    k_r=C(−h_a∪q_b+q_a∪h_b+h_a∪δh_b)

give b'_r−b_r=δk_r. All these cochains have the same pairwise physical support as before. Therefore z=exp(t k_p+u k_qpair) supplies the exact weighted scalar gerbe correction c'=c·δz, including the mixed term. The apparent centrality is the weighted truncated identity: a same-pair derivative is killed by t² or u², and complementary derivatives vanish by support. No unweighted global centrality claim is made.

The chain rule V_d a*=i a*V_d gives the relative star-algebra isomorphism with t↦−t,u↦−u. Physical fields kill all base functions. The constant-family two-torsion line Q has the same flat algebraic μ2 descent as in the audited theorem, so tensoring by Q⁻¹ preserves the same star algebra and weighted gerbe uniformly. On étale local trivializations, ordinary bundle identifications lift by the usual star-gauge conjugation, retaining derivative corrections. Their inverses exist in the nilpotent star extension. The algebraic descent is unchanged after base change.

Thus semilinear pullback, z⁻¹, flat Q⁻¹ tensoring, and the relative bundle identification transport the actual family deformation problem to itself. Deck equivariance follows from the same mask signs and pair characters. Choose the global bundle isomorphism a*E≅E⊗Q supplied by the fixed target-chain isomorphism and the fixed line identity. Compare this global isomorphism with its deck conjugate, using the induced deck structures on the line identity and Q. Their projectivizations agree, so their ratio is a global scalar unit on X×B+. That scalar is a base unit: π_*O_(X×B+)=O_B+ since X is proper geometrically connected. Physical derivations kill it. Arbitrary local re-framings need not have base-constant scalar ratios and are not used for this argument. This is the relative replacement for the central-fiber 'constant scalar' argument.

## 5. Relative gauge matching and actual class equality

The actual source theorem supplies regular prescribed first lifts and their closed mixed residual throughout the normalized generating family. Restrict these to B+. The transport in §4 supplies another pair of first lifts for the same branch equations and same gerbe. Their normalized differences are regular pair-character Čech one-cocycles. On affine parameter patches the universal H¹ vanishings from §2 make these cocycles exact, not merely exact at each geometric point. Choose the corresponding degree-zero gauges and apply their simultaneous lift in k[t,u]/(t²,u²).

After this gauge, the two first-order branches coincide. The mixed transition discrepancy is then a tu edge term, so the audited actual mixed-curvature identity makes the difference of normalized mixed classes a Čech boundary. Trace-free projection commutes with the construction. By the imported uniform source identity [R]=tf([M]), this comparison identifies the actual residual classes, rather than an unrelated abstract obstruction.

Because tu is fixed by t,u↦−t, we obtain A(r)=r. The local comparisons glue as equalities of sections of V. Together with the uniform full-sign purity theorem this proves r∈Γ(B+,V+), not merely that its χ projection is fixed. All data and cochain identities are regular; the resulting section identity pulls back under every map T→B+, including nonreduced T. The cohomological interpretation is preserved by the established arbitrary base change for V and its eigensummands. There is no inference from equality at reduced geometric points.

On affine T the section is the entire absolute mixed class under affine Leray. For general nonaffine T retain the relative-section formulation; no new assertion removes the absolute Leray caveat.

## 6. Bounded consequence and limits

Using the independently audited central trace-zero theorem, total relative mixed-class vanishing on B+ is cut out by the 176 local coordinates of r in V+. This is a bound on generators of an ideal, not their independence, codimension, existence of a zero, or nonzero behavior. At a zero the intrinsic section derivative lands in V+; the corrected derivative of the preceding relative theorem is still required in moving cochain coordinates.

The family has coefficient dimension39, not a claimed 39-dimensional moduli quotient. No S4 or D8 retained sector is transported to a general tuple, no comparison with thirty retained tests is made, and no operational elimination follows. The result proves neither zero nor nonzero value of the central actual class. It supplies no raw representative covariance, selector covariance, or higher star-order solution.

