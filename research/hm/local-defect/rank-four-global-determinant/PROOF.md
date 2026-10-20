> Publication scope: preserved mathematical proof/audit. Historical statements that rank eight remains open are superseded only after the final assembly and all its prerequisites. No source-instance evaluation or formal verification is claimed here.

# Generic quadratic rank four forces a degree-forty exceptional divisor

## Result

Under the existing canonical-operation, quadratic-flag, and full HM normalizer hypotheses, suppose the generic rank of the normal quadratic map Q is four. Then:

1. The saturated image F of the linear bundle map described below has rank eight and determinant O(-4).
2. Its rank drops in codimension at least two. Equivalently, Q has rank four at the generic point of every divisor of P(V).
3. The saturated image I of Q in C has determinant O(3).
4. The resultant of the four induced normal quadrics extends to a nonzero section of O(40). Its zero divisor is nonempty, and its support is precisely the union of the divisorial components of the exceptional quadratic-basepoint set E.

Thus generic rank four would force an actual divisorial exceptional locus of total resultant degree forty. This does not exclude rank four. In particular the existing bound dim E<=3 alone is compatible with this consequence. All arguments concern universal bundle constructions and group characters; no actual source matrices, operation values, ranks at inputs, or instances are computed.

## 1. A linear image bundle

Write X=P(V), L=O(-1), U=(V tensor O)/L. The outer-symmetric trilinear operation defines

    b: L tensor Sym^2(V tensor O) -> J tensor O,
    b(u tensor (p q)) = (f(p,u,q)+f(q,u,p))/2.

Outer reversal makes the symmetrization redundant, but fixes the polarization convention. The already established rank-four subbundle A=L^2 tensor U of J tensor O is contained in the image of b, since b(u tensor (u p))=f(u,u,p). Modulo A, b factors through L tensor Sym^2 U and equals Q.

Let F be the saturation of im(b) in J tensor O, and I the saturation of im(Q) in C=(J tensor O)/A. Saturation here means that the quotient is torsion-free. Since A is a subbundle contained in im(b), F is the inverse image of I and

    0 -> A -> F -> I -> 0.

Under the rank-four hypothesis, F has rank eight and I has rank four. Torsion-free sheaves on smooth X are locally free away from codimension at least two. All subsequent determinant calculations may be made on that open set and extended uniquely to X. Write det F=O(-k).

The inclusion F -> J tensor O gives a nonzero component of det F -> exterior^8 J tensor O, hence k>=0. The generically surjective map from L tensor Sym^2 V to F gives a nonzero component

    O(-8) -> det F=O(-k),

hence k<=8. No constant-rank assumption is used.

## 2. Central character fixes the determinant

Use the defining HM normalizer action N containing the Heisenberg group H5. Its central element c acts on V by the primitive fifth root c, and therefore acts on J by c^3: the nonzero equivariant cubic operation spans J by the already proved irreducibility theorem. Consequently it acts on det F by c^24.

The natural linearization on O(-k) has central character c^k. Any other linearization differs by a character of N. Every one-dimensional character is trivial on the center of H5, because that center lies in its commutator subgroup. Hence

    k = 24 modulo 5.

Combined with 0<=k<=8 this gives k=4.

Also c1(A)=c1(L^2 tensor U)=-8h+h=-7h. The determinant exact sequence therefore gives det I=O(3).

This calculation is independent of switching all actions to the opposite-group convention: both central characters then invert.

## 3. No divisorial rank drop

On the common locally free open set, the maximal minors of b, interpreted using det F=O(-4), are sections of O(4), indexed by exterior^8(Sym^2 V). They extend to X across codimension two. At least one section is nonzero. Their common divisorial zero part D is effective, N-invariant, and has degree at most four. Invariance follows because b and its saturated image are equivariant, so the common-zero ideal and its divisorial part are preserved.

Every N-invariant effective divisor on P(V) has degree divisible by five. Indeed its homogeneous defining polynomial spans a one-dimensional representation of N, hence the H5 center acts trivially on that span. On polynomials of degree d the center acts by c^(-d), so 5 divides d.

Therefore D=0. At a generic point of a divisor, b has full rank eight into F. Since A is already a subbundle of rank four contained in its image, Q has full rank four into I there. This proves the second conclusion, including the possible saturation issue rather than assuming it away.

## 4. The resultant line

On an open X0 whose complement has codimension at least two, I is locally free and Q is surjective. View Q as

    Sym^2 U -> T,  where T=I tensor L^*.

Both U and T have rank four. The four components of this map are quadrics in four variables. Their multivariate resultant is a canonical section, up to a fixed nonzero scalar, of

    (det T)^8 tensor (det U)^(-16).

For the twists: the resultant has degree 2^3=8 in each of four component equations, so changing the target frame contributes the eighth power of its determinant. Changing the variable frame contributes determinant weight 2^4=16, with the inverse sign because the equations are covariant forms on U. The formula also agrees with the rank-one case, where a quadratic map U^2 -> T is itself a section of T tensor U^(-2).

Here det T=det I tensor (L^*)^4=O(7), and det U=O(1). The resultant line is consequently O(56-16)=O(40).

The existing flag-nef theorem gives a generically empty quadratic base locus. Thus this resultant is not the zero section. Since X is smooth and X\X0 has codimension at least two, the section extends uniquely to X. A nonzero section of O(40) has a nonempty effective zero divisor of degree forty.

At every codimension-one point, the rank-four bundle description is valid, and the basic resultant criterion says its vanishing is equivalent to the four quadrics having a geometric projective common zero. Thus the support of this divisor equals the divisorial part of E. Multiplicities are resultant multiplicities; this does not assert that E is reduced or irreducible, or that the general fiber over any component has exactly one basepoint.

## Limits of the determinant approach

This gives the conditional implication

    generic rank(Q)=4 => dim E=3, with a resultant divisor of degree 40.

Therefore a future structural proof dim E<=2 would exclude generic rank four. The currently proved dim E<=3 does not. Nor does invariance exclude degree forty: forty is divisible by five. No smoothness, Picard-number-one property, or reduced-resultant assumption has been established that would allow applying the existing extremal Picard obstruction to rule this divisor out.

Sources: ../rank-one-quadratic-flag-nef/PROOF.md (bundles, generic basepoint-freeness); ../rank-one-normal-obstruction/PROOF.md (symmetry and quadratic map); ../../full-hm-image-symmetry/PROOF.md and ../../cubic-loci/cubic-structural-nonvanishing/cubic-structural-nonvanishing/PROOF.md (normalizer, central action, irreducibility and spanning).
