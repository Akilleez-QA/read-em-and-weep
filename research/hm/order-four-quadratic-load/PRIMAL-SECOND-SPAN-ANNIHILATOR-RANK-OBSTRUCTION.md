# The second constant span excludes both remaining primal equality labels

## Result

The two remaining primal equality labels

    G3.11.942927348917 (profile11),
    G3.12.8e9af2d08af9 (profile12)

are impossible.

The preceding actual residual-osculation theorem forces a full second constant span V1=Sym10 W inside U=H/V0. Its sixth osculating bundle Y lies in the rank8 projected actual bundle Z. Restricting the actual annihilator Qprime of Z to V1* has rank at least3. However complete equivariant Hom support and a single irreducible cohomology budget force its rank at most2. This is the contradiction.

Neither exact intersection Z intersect V1=Y nor surjectivity onto Y^perp is assumed. In particular, the possible rank3 alternative does not need a separate geometric saturation argument: it is already prohibited by the rank-at-most2 bound. No actual-instance matrix, coefficient or rank evaluation is used.

## 1. The actual second span and its annihilator

The frozen primal exact-intersection theorem gives the exact bundle sequence

    0 -> Z -> U O -> Qprime* -> 0,     dim U=19,
    rank Z=8,   deg Z=-36.

Thus Qprime is the actual fiberwise annihilator of Z in U* O, not merely a bundle with a matching Euler character. It is the kernel of the split-surjective restriction Q*->W O(-9), hence as equivariant bundles

    Q*=W O(-9) plus Qprime.

The subsequent residual-osculation theorem proves a full invariant constant span

    V1=Sym10 W subset U,       dim V1=11,

whose complete degree-ten curve has sixth osculating bundle

    Y=Sym6 W O(-4) subset Z intersect (V1 O).

For a parameter line l in W, the fiber of Y is l^4 Sym6 W. Under the invariant apolar pairing on Sym10 W its annihilator is l^7 Sym3 W. Consequently

    Y^perp=Sym3 W O(-7)=S O(-7) subset V1* O.             (1)

Since Qprime annihilates Z and hence Y, its actual restriction factors through (1):

    r: Qprime -> S O(-7) -> V1* O.                      (2)

At every point, the annihilator in V1 of the image of (2) is exactly Z intersect V1. That intersection has dimension at most rank Z=8. Elementary fiberwise duality therefore gives

    rank r = 11-dim(Z intersect V1) >=3.                (3)

This lower bound requires no constant-rank assertion about the intersection and no second exact-intersection theorem.

## 2. Complete source support for the restriction

The actual cohomology presentation, after subtracting the forced W O(-9) block, gives

    H1(Qprime(-1))=M3-W Sym8 W=2Wp+2S+4T,
    H1(Qprime)=M2-W Sym7 W=A+V+P+3D.                    (4)

Every irreducible block of Qprime is among the21 possible co-blocks enumerated in the residual-osculation theorem. Completeness follows by exhausting the original Q* degree window[-42,-1], center parity, the rank-degree bound and the two remaining componentwise H1 budgets(4). Every direct-sum contribution is a genuine representation, so multiplicities cannot cancel.

Among that complete overlist, the only blocks with nonzero equivariant Hom into S O(-7) are

    O(-18),   O(-16),   Wp O(-11),   O(-10),             (5)

and each Hom space has dimension1. Their respective twist-zero H1 characters are

    H1(O(-18))       = V+P+2D,
    H1(O(-16))       = A+V+P+D,
    H1(Wp O(-11))    = A+V+P+2D,
    H1(O(-10))       = P+D.                             (6)

These finite character identities and all the zero Hom spaces outside(5) are independently recomputed by the accompanying exact Q(sqrt5) verifier.

## 3. The single-P budget bounds the actual rank

The actual H1(Qprime) in(4) contains exactly one P. Every supported block in(5), including every repeated copy if one were present, contributes one P by(6). Hence the sum of the multiplicities of all supported blocks is at most1.

All other source blocks map to S O(-7) by zero. Thus any equivariant map Qprime->S O(-7), including the actual restriction r, factors through at most one irreducible block from(5). Its ordinary rank is at most the largest source rank in that list, namely2 from Wp O(-11). Therefore

    rank r <=2.                                        (7)

This is a universal upper bound for every map in the relevant Hom space, not an instance computation. It holds regardless of which scalar coefficients vanish and independently of the behavior of the target image at individual points.

The contradiction between(3) and(7) excludes both stated labels. Their profile distinction does not change this argument: the frozen residual-osculation theorem applies to the common heights(8,6,0) and the same actual source presentation. The already-excluded profile21 primal label and the different source2 dual label are not used here.

## Reproduction and scope

Run `python3 verify_primal_second_span_annihilator_rank_obstruction.py`. It pins the actual source, primal exact-intersection theorem and mixed-Z5 osculation package. It independently exhausts all21 possible Qprime blocks in the complete degree window, computes every Hom space into S O(-7), checks the four supported blocks and their single-P costs, and records the rank inequalities2<3 in `primal-second-span-annihilator-rank-obstruction.json`.

The geometric input is the actual second constant span and embedded Y, not merely the abstract splitting Z=Z5. No N=Z^- identification, second quotient connection, exact second intersection or actual-instance evaluation is assumed. No frozen source file is modified.
