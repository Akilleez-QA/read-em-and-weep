# Independent final review

Verdict: PASS for the abstract local scalar-slope theorem. The final proof establishes a nonzero slope for every regular pair, including cubics with repeated factors. It does not evaluate the actual base class or authorize an actual-global change of s.

## Frozen files

- PROOF.md SHA-256: 3fe0bf356b69647c590b4e779ed7eec1a4194a0a0c40c452233da3e2f72c6a26
- verify.py SHA-256: 999009e895413481e316600119ac908381f00a627a0dc09f058622f7c451ed5c

The final reread made two standalone exposition repairs: defined E explicitly, and replaced a dangling reference to Section 1 with the argument that K is independent of the choice of R. No other proof content was changed.

## Independent checks

1. Harmonic normalization. Direct chain-rule differentiation with Delta=partial_x partial_z-(1/4)partial_y^2 gives the stated operator on x^m H(t,Q). Hence the exact coefficients are c1(d)=1/[2(d-1)] and c2(d)=1/[8(d-1)(d-3)]. This fixes the B1 and B2 normalization, including signs. Ordinary multiplication is valid here because the zeroth and first square coefficients vanish: no lower coefficient feeds into the q^2 coefficient. For degrees r,s, the same chart gives B1(P,Q)=c1(r)P''Q+c1(s)PQ''-c1(r+s)(PQ)'', and B2 follows by subtracting c2(r+s)(PQ)'''' and c1(r+s-4)(B1(P,Q))'' from the ordinary second coefficient.

2. Slope. Trace-free rank-two polarization gives {n,Z}=tr(nZ) Id, with no missing factor of two. The square equation gives tr(nZ)=-A d2; the q^2 coefficient of {J,N} is consequently A d2. Thus the cubic change is lambda A d2, and the lambda^2 term starts at q^4. The q and q^2 equations are preserved. The weights and the quotient slope a lambda[d2] are correct.

3. Admissible-family existence. The regular-pair trace map has a two-dimensional kernel and dimensions 15 to 13, so is surjective. This constructs regular Z, and hence R, for every regular pair and every nonzero A. The original concern that the admissible locus might force the slope to vanish is therefore resolved, once divisibility is included.

4. Divisibility. Formula (10), including -tr(nV), is correct. Independently, J=F*N+q^2Z-q^3V implies

 J^2=F*[F*N^2+q^2{N,Z}-q^3{N,V}] modulo q^4.

The bracket starts at q^2 and its q^2 coefficient is A d2+tr(nZ)=0. Therefore it starts at q^3, and the cubic coefficient of J^2 is divisible by A. This proves h-divisibility for the entire abstract family without genericity assumptions or selected examples. The difference between two R choices is A Psi(D); the stated divisibility of Psi(D) by f proves quotient independence.

5. Lift independence. It also follows directly from the chart: for D=(lF/2,0,lG), the only possibly surviving ordinary q^2 change modulo F is lG*a1_upper, while a1_upper=-uFF''/2. The quadratic change l^2F^2/4 also vanishes modulo F. Thus using the canonical T loses no quotient information.

6. Every-pair nonvanishing. SL2 changes of binary coordinates preserve q and the invariant Laplacian. The canonical T numerators are multiples of the second transvectants with numerators 20F''G-16F'G'+6FG'', 12FF''-8(F')^2, and 40GG''-32(G')^2. Thus T, harmonic products, and d2 are equivariant. The existential chart with deg(F)=3 is legitimate and does not evaluate an actual point. For symbolic leading coefficient c3 nonzero, Q=3(F'')^2-8F'F''' is a quadratic with leading coefficient -36c3^2. It cannot be divisible by F. Since G is a unit modulo F, the displayed formula gives nonzero [d2] for every regular pair, without requiring squarefreeness. This avoids any incidence-domain or localization proviso.

7. Consequences and limits. For fixed other local inputs, the quotient moves injectively along the scalar lambda-line. At most one lambda can give K=0; a cancelling lambda need not exist. Neither the actual K nor its vanishing is determined. The proof provides no actual-global completion freedom, fourth-square vanishing, or later Bockstein conclusion.

## Verifier and restrictions

The final verifier was inspected before execution. It uses fixed-size formal product rules and free symbols, not actual form coefficients, selected pairs, roots, points, matrix ranks, or model evaluations. All four checks passed: free-jet identity; zeroth and first square coefficients; harmonic coefficient recurrence; arbitrary cubic expression. The recurrence assertion alone is algebraic, so the geometric chain-rule premise was independently checked above. No large computation or GitHub write was performed.

No mathematical error remains in the reviewed files. The pinned prior frame/setup statements are dependencies, not a claim that their full global proofs were re-audited here.
