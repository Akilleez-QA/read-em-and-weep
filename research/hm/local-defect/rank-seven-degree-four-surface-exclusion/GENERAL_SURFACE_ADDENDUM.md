> Publication scope: preserved mathematical proof/audit. Historical statements that rank eight remains open are superseded only after the final assembly and all its prerequisites. No source-instance evaluation or formal verification is claimed here.

# Degree at least five: at most seven cubics without a fixed divisor

## Result

Let Z be a dimension-two closed subscheme of P4, of degree a>=5. Suppose its complete cubic system is nonzero and has no fixed divisor. Then

    h0(I_Z(3)) <= 7.

This applies to nonreduced schemes with embedded or lower-dimensional components and requires no arithmetic Cohen--Macaulay hypothesis. It closes the specific gap left in ../cubic-section-scheme-obstruction/PROOF.md and supplies an alternative exclusion of rank seven without the equivariant Riemann--Roch congruences.

## 1. A plane scheme with two quadrics

Let D be a finite subscheme of P2. Suppose there are two independent quadrics q1,q2 in I_D and the complete cubic system of D has no fixed curve. Then length(D)<=4.

If q1,q2 are coprime, their complete intersection is zero-dimensional of length four and contains D. This proves the bound.

Otherwise their greatest common divisor is a linear form l: a common quadratic factor would make them proportional. Write

    q1=l a,  q2=l b

for independent linear forms a,b. Put p=V(a,b). Since the cubic system has no fixed curve, choose C in I_D(3) not divisible by l. The zero-dimensional scheme

    W=V(l a,l b,C)

contains D. It is zero-dimensional because V(l a,l b) has support the line V(l), together with possibly p, and C does not contain that line.

If p is not on V(l), W agrees with the complete intersection V(l,C) along the line; its length there is three. At p the form l is a unit and the ideal contains (a,b), so the additional length is at most one. Thus length(W)<=4.

If p is on V(l), then away from p the schemes W and V(l,C) agree. At p use the regular local ring A=O_(P2,p), with maximal ideal m=(a,b). The quadrics generate l m. There is a surjection

    A/(l m,C) -> A/(l,C).

Its kernel (l,C)/(l m,C) is an image of (l)/(l m), which has length one: multiplication by the nonzero element l identifies it with A/m. Hence the local length of W at p exceeds that of V(l,C) at p by at most one. The complete intersection V(l,C) has total length three, including its possibly nonreduced intersection multiplicity at p. Therefore length(W)<=4 in this case as well. Since D is a closed subscheme of W, length(D)<=4.

This argument controls the overlapping multiplicities explicitly; it does not count only distinct points or reduced components.

## 2. Plane Hilbert-function bound

Let D be a finite subscheme of P2 of length a>=5 whose cubic system has no fixed curve. Section 1 implies

    h0(I_D(2)) <= 1.

Also h0(I_D(1))=0: a nonzero linear equation would give three linearly independent quadrics by multiplication with the three-dimensional space of linear forms, contrary to the preceding bound.

The Hilbert function H_D of the saturated coordinate ring therefore satisfies

    H_D(2)=6-h0(I_D(2))>=5.

Choose a linear form avoiding the support of D. It is a nonzerodivisor on the saturated coordinate ring, so H_D is nondecreasing. Thus H_D(3)>=5 and

    h0(I_D(3))=10-H_D(3)<=5.                    (1)

No assumption concerning reducedness is involved.

## 3. Restrict a surface to a general plane

Choose a general flag P2=L inside P3=H inside P4. Let C=Z intersect H and D=C intersect L scheme-theoretically. As detailed in PROOF.md, Section 2, the two hyperplane equations can be chosen successively as nonzerodivisors on O_Z and O_C. The plane section D is finite of length a, by taking two differences of the Hilbert polynomial. These facts hold even with embedded and lower-dimensional components.

The base scheme of H0(I_Z(3)) has dimension at most two. We can choose the same general plane so that its intersection with this base scheme is finite. The restricted global cubics therefore have no fixed curve in L. Since they belong to H0(I_D(3)), the complete cubic system of D also has no fixed curve. Section 2 applies.

The exact ideal-sheaf restriction sequences give, on global sections, the same inequalities used in PROOF.md, Section 3. In particular h0(I_D(1))=0 implies h0(I_C(1))=h0(I_Z(1))=0. Hence

    h0(I_C(2)) <= h0(I_D(2)),
    h0(I_Z(2)) <= h0(I_D(2)),
    h0(I_C(3)) <= h0(I_D(2))+h0(I_D(3)),
    h0(I_Z(3)) <= 2h0(I_D(2))+h0(I_D(3)) <= 2+5=7.

These use only upper bounds from exact sequences of sheaves, not surjectivity of section restriction or vanishing of intermediate cohomology. This proves the result.

## 4. Alternative rank-seven exclusion without RR

Suppose the remaining rank-seven determinant branch k=3 exists. Set E=F*. Then E has rank eleven and R has rank nine. Both have first Chern class 3, E is reflexive and generated outside codimension two, and R is globally generated and torsion-free. The established strict second-Chern positivity gives

    c2(E)>0, c2(R)>0, c2(E)+c2(R)=9.

Consequently at least one of these two second Chern classes is at least five.

Both sheaves have at least twenty independent global sections. For R, the invariant space H0(F) inside J is zero, since J is irreducible and rank(F)<20, so J injects into H0(R). For E, dualizing gives a map J* tensor O -> E with kernel R*. The invariant space H0(R*) inside J* is zero, since J* is irreducible and rank(R*)<20. Therefore J* injects into H0(E).

The established general-section quotient argument yields

    0 -> O^10 -> E -> I_(Z_E)(3) -> 0,
    0 -> O^8  -> R -> I_(Z_R)(3) -> 0.

The two surface degrees equal c2(E) and c2(R), respectively. The cubic systems have no fixed divisor: their ideal sheaves twisted by 3 are generated outside codimension two, as quotients of the corresponding generated sheaves there. Since H1(O)=0,

    h0(I_(Z_E)(3))=h0(E)-10>=10,
    h0(I_(Z_R)(3))=h0(R)-8>=12.

Choose the scheme whose degree is at least five. The result of Section 3 bounds its number of cubic sections by seven, contradicting either lower bound. Thus rank seven is impossible independently of the RR congruences.

This supersedes the remaining-gap statement of ../cubic-section-scheme-obstruction/PROOF.md: general plane-section Hilbert functions provide the bound there without an ACM hypothesis.

## Evidence boundary

Only universal scheme-theoretic intersection, local length, Hilbert-function, hyperplane-restriction, and sheaf arguments were used, with previously established equivariance and irreducibility inputs. No actual operation, HM source, matrix, selected input, product, rank instance, polynomial instance, jet, or residue was evaluated. Only this local addendum was written.
