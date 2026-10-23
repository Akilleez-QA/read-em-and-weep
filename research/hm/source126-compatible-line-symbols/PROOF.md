# A single compatible radical suffices for the two-dimensional cubic gate

## Statement and scope

Assume an actual source126 occurrence in any constant template, and a nonzero Q-compatible radical element j. Use the single-line footprint notation

    im j2=uP+(δ+k)D, im j4=P+δD.

For the rows u=0,k=1, the internal annihilator complex has first symbol a·multiplication on A, zero on D; its internal second symbol is zero; and its internal third belongs to the same canonical two-dimensional cubic space previously established under full-J Type II compatibility. Its zero/nonzero alternative agrees with the original fourth on the generic surviving D kernel.

The applicable rows are Type I (5,4), Type II (5,4)/(10,9), and Type III (10,9). This removes the need for full-J compatibility in that reduction. It does not select the cubic, evaluate an actual instance, establish existence of a line or source, or remove a source-dual pair.

PR988 at commit7ceeaa0bb1942ed628f7a25fa2f5fd3c3a1fe49d, research/hm/source126-compatible-line-ranks/PROOF.md, supplies the single-line rank theorem. PR973,979,982 and966 are also pinned in INPUTS.json. Their universal constructions are invoked only after verifying below every actual-complex premise they use, not by dropping their original full-J assumptions silently.

## 1. Actual single-line cohomology and faithful connecting map

Set U=ker j2, Z=ker j4, S=[U→Z], M=[N2→N4], T=M/S. Commutation with Q and every actual negative T_a makes this a short exact sequence of whole families. Because j²=0, its maps descend to a chain map j:T→S for the whole family.

The companion rank theorem supplies the actual characters and quotient-Q maps, not only endpoint dimensions. For u=0,k=1 these give

    H0(S)=H0(M)=A+D, H1(S)=D,
    H0(T)=D, H1(M)=H1(T)=P.

The H0 inclusion is the identity on the actual kernel. The long exact sequence makes the connecting δ:H0(T)→H1(S) an isomorphism, and projection η:H1(M)→H1(T) an isomorphism; H1(S)→H1(M) is zero. Fix δ[xbar]=[Qx].

The induced j0:D→A+D lands in D by equivariance, and is NONZERO. In fact if a quotient cycle xbar satisfies j0 xbar=0, then its representative j2x is a genuine zero degree-zero cycle of S, since there are no degree-minus-one boundaries. Thus j2x=0, x∈U, and xbar=0. Hence j0 is an isomorphism onto the actual D kernel. The induced j1:P→D is zero by equivariance. Unlike the full-J proof, no choice of a second radical element is needed.

## 2. Internal first and original second

First-symbol naturality gives bS,a j0=j1 bT,a=0. Therefore bS vanishes on D in every direction. Its A component is a scalar λ times binary-quadratic multiplication, because Hom_G(A⊗A,D) is one-dimensional.

The scalar is nonzero. If λ=0, every original A cycle h admits a first correction w inside S: Qw=−T_a h. The next residual T_a w lies in S1, whose Q-cohomology maps to zero in the original cokernel P. Hence the actual original second symbol on A would vanish, contradicting the retained actual nonzero theorem. Independence from a different first correction follows from the original first vanishing. Thus λ≠0; normalize it into the A identification.

For this A cycle choose a first correction w in M. Its quotient is a Q_T cycle satisfying δ[wbar]=−bS,a(h). Passing the next residual to H1(T) gives the exact comparison

    η β2,M,a(h)=−bT,a δ^-1 bS,a(h).

Consequently bT is nonzero. Hom_G(A⊗D,P) is one-dimensional, and ordinary multiplication Sym2 W⊗Sym4 W→Sym6 W followed by quotient by V6 is nonzero. Thus bT is that channel up to scalar. PR966's universal theorem, independent of any source2 occurrence, gives generic rank4, rank3 at ten reduced directions, and rank4 at every square.

We have verified ALL actual first-page interfaces used in PR979/982. In particular the rank-two bundle E is intrinsically

    0→A O(-1) --multiplication a-->D O→E→0,

and quotient first kernel is κ:O(-5)→D O(-1). This uses no equality U=F2 and no joint-annihilator assertion.

## 3. Transfer of the internal second vanishing

For completeness, the mechanisms of PR979 apply as follows. Choose an equivariant constant Q_S right inverse on its image. For h∈D, solve Q_S w=−T_a h. Its residual modulo aA is a global quadratic bundle map s:D O(-2)→E, independent of right inverse. The single chain map j has j0 a nonzero scalar and j1=0, so naturality on the quotient FIRST kernel gives sκ(-1)=0. No higher naturality on all of D is assumed.

The universal representation dimensions and rank-one exclusion of PR979 Sections2–3 depend only on A,D,E, not on Type II or full-J. They give Hom_G(D O(-2),E) dimension2 and show every nonzero member has generic rank2. The original third comparison is the same representative calculation: solve the S residual in M and use the connecting δ. It gives

    η β3,M=−bbarT δ^-1 s,

where bbarT is quotient by the original second image bT(aA). On the generic open this map has rank1 from E to the original remaining cokernel line, since bT has rank4 and the original second has rank3. The imported actual original third is zero. Hence s has generic rank at most1, forcing s=0 by the universal rank-one exclusion. This proves internal second vanishing globally, not just at a generic direction.

## 4. Transfer of the cubic gate and fourth comparison

PR982 Section1's normalized correction construction uses only the first-page interfaces and s=0, now proved. It therefore constructs a canonical global cubic

    r:D O(-3)→E.

Explicitly choose w1=-H T_a h, remove its unique A-valued linear correction so that its next residual vanishes already in H1(S), then choose w2=-H T_a w1. The class of T_a w2 modulo aA is r. Choice independence follows from s=0 and injectivity of multiplication by a, exactly as in that construction.

On the dense open where bT is onto, every quotient first kernel vector lifts through arbitrary finite order: after cancelling constant Q-pairs its differential is t times a matrix with surjective leading term. Applying the single j to those lifts gives

    rκ(-2)=0:O(-7)→E.

The nonzero scalar j0 is essential here; j1=0. This is naturality ONLY on the quotient first kernel. Polynomial continuation extends the equality globally. PR982's universal representation computation and nonflex-square witness show that the raw cubic Hom space has dimension3 and restriction along κ has rank1. Therefore r lies in its canonical two-dimensional kernel.

Finally, the original fourth comparison uses the normalized two S corrections and a third correction in M. It gives

    η β4,M=−bbarT δ^-1 r

on the generic surviving D kernel. The coefficient has degree4. PR982's universal rank-one exclusion for cubic maps into E shows each nonzero r is generically onto E; hence the displayed composition vanishes if and only if r=0. None of these arguments needs another radical element or a specific Type II endpoint dimension.

## 5. Acyclic rows and precise limits

For u=1,k=0, the companion theorem gives quotient Q with zero kernel and zero cokernel. Thus it is invertible and can be removed by filtered formal chain contraction. The full original Bocksteins transfer directly to the restricted annihilator complex. Its dimensions are37→33 for pair(4,4), or32→28 for pair(9,9). This is different from the non-acyclic rows studied above and does not imply their cubic gate.

For u=k=1, the companion top-quotient obstruction already forces generic rank36 and all later original generic symbols zero. Thus the single-line rank partition separates acyclic reductions, non-acyclic cubic-gate reductions, and generic all-orders rank obstructions.

No secondary-homotopy scalar ν is supplied in the present u=0,k=1 rows: the one radical generator has NONZERO cohomology map, so there is no cohomologically null kernel line to which PR980 can be applied. Neither the full-J collective-image argument nor its resulting r=0 is imported. The two-dimensional cubic gate remains genuinely unselected here.
