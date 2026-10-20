> Historical prerequisite proof from 15 October 2026; recorded checks are not new runs. See the common PUBLICATION-SCOPE.md.

# Global rank-six Klein character algebra

## Result

Let H=< (12),(34),(13)(24)> and V=ker(sign|H)={1,(12)(34),(13)(24),(14)(23)}. Work over Q. Let T=Q[v0,v1,v2,v3,v4], with every vi of Segre degree1, and define

U=X1X2Y3Y4+Y1Y2X3X4,
a=(X1Y2-X2Y1)(X3Y4-X4Y3).

The V-invariant Segre ring is exactly

T[U,a]/(U³-sU²+tU-w, a²-(s²+2sU-3U²-4t)),

where s=v2, t=v1v3-4v0v4, and w=v0v3²+v1²v4-4v0v2v4.

It is globally free over T with basis

1,U,U²,a,aU,aU²,

of degrees0,1,2,1,2,3. There is no inversion of v0, a diagonal, or a discriminant. The degree-zero character of H/V is the first triple, and its sign character is the second triple. These are characters of coordinate permutations, distinct from deck characters.

## 1. Denominator-free global proof

Write R for the full Segre ring, whose degree-n part consists of multihomogeneous polynomials of degree(n,n,n,n). The independent cubic audit proves

R^H=T+TU+TU²

as a direct sum of graded free T-modules; its proof compares dimensions in every degree, rather than localizing a field interpolation formula. The cubic is monic and is the only relation in this rank-three algebra. See historical imported premise hm-cubic-resolvent-independent-audit-20261015/AUDIT.md. (see PUBLICATION-SCOPE.md)

Since V is normal of index2 in H, the transposition tau=(12) acts on R^V. Every F in R^V has the exact split

F_+=(F+tau F)/2, F_-=(F-tau F)/2.

The even part is H-invariant. The odd part transforms by sign on H: it is skew under(12) and(34), and fixed by(13)(24). Thus F_- vanishes on each pair diagonal, and the irreducible polynomials X1Y2-X2Y1 and X3Y4-X4Y3 both divide it. They are relatively prime in the polynomial ring, so their product a divides it. Exact division produces a polynomial G=F_-/a. Since numerator and a have the same H character, G is H-invariant.

This establishes the direct sum

R^V=R^H direct_sum a R^H.

It is direct because the two summands have different tau eigenvalues and2 is invertible. It is free because multiplication by the nonzero polynomial a is injective. In degree n, the second summand is a(R^H)_(n-1); no degree is discarded or supplied by a Laurent power of v0. This proves the claimed six basis elements and their degrees globally.

Direct homogeneous expansion gives

a²=v2²+2v2U-3U²-4v1v3+16v0v4=s²+2sU-3U²-4t.

The proposed presented algebra is monic in both U and a, reducing every element to the six basis elements. Their independence in R proves that no additional relation or torsion remains. The only division used in splitting the characters is the rational constant2. The diagonal factors are divided only after polynomial divisibility is proved, not inverted as functions.

## 2. Explicit complete multiplication table

Represent an element as E(U)+a O(U), where E and O have degree at most2 in U and coefficients in T. All multiplication takes place in the cubic algebra B=T[U]/(U³-sU²+tU-w). Put

Q(U)=s²-4t+2sU-3U².

Then the exact product rule is

(E,O)*(F,P)=(EF+Q OP, EP+OF),

with each resulting cubic expression reduced modulo the monic polynomial. This retains both characters. It neither projects away the even sector nor applies the trace early.

For an explicit six-by-six multiplication-table description, let e_i=U^i and f_i=aU^i for i=0,1,2. Define r0=1,r1=U,r2=U² and

r_(k+3)=s r_(k+2)-t r_(k+1)+w r_k.

Then all36 ordered basis products are specified by

e_i e_j=r_(i+j),
e_i f_j=f_i e_j=a r_(i+j),
f_i f_j=(s²-4t)r_(i+j)+2s r_(i+j+1)-3r_(i+j+2).

Each r has degree at most2 in U after recurrence. The largest index required is6. The recurrence uses only polynomial coefficients; all degrees are preserved.

Equivalently, use coefficient columns in basis(1,U,U²). Multiplication by U is

M = [[0,0,w],[1,0,-t],[0,1,s]].

Multiplication by Q is

K = [[s²-4t,-3w,-sw],
     [2s,s²-t,st-3w],
     [-3,-s,-t]].

Here K=(s²-4t)I+2sM-3M². In six-coordinate order(e0,e1,e2,f0,f1,f2), multiplication by U is diag(M,M), and multiplication by a is the block matrix [[0,K],[I,0]]. These matrices commute and obey the two displayed algebra relations, supplying another fully explicit multiplication table.

## 3. Exact alternating trace and its kernel

Fix the same oriented Delta=product_(i<j)(xi-xj), q=x3²x4² and unnormalized Alt=sum_(S4) sign(sigma)sigma. For a symmetric denominator D and a V-invariant numerator N=E(U)+aO(U), define the previously authenticated finite trace through Alt(qN)/Delta, with the same section frames and domain as that trace theorem. Purely algebraically, its even part is zero: E and q are invariant under(12), so the alternating sum cancels in pairs.

Write O=A+UB+U²C and h=v0v4. The odd part has exactly the cubic trace proved independently:

Alt(q aO)/Delta=4[A+sB+(s²-t-2h)C].

Thus with denominator D the answer is

4[A+v2B+(v2²-v1v3+2v0v4)C]/D.

The factor4 is8 from the signed wreath subgroup times1/2 from q_sym. It is not a normalized field trace or an average divided by24. In basis order above, the T-linear functional has row

(0,0,0,4,4s,4(s²-t-2h)).

It lowers Segre degree by1. For numerator degree n the A,B,C grades are n-1,n-2,n-3, so its output has degree n-1. For a rational O(-4)^4 source N/D this becomes the correct degree-5 section on P4.

Crucially, this linear functional is NOT an algebra quotient, and its kernel is NOT an ideal. For example, the even element1 has trace zero, while1*a=a has trace4. Even within the odd sector, a(U-s) has trace zero, but its product with U has trace -4(t+2h), a nonzero polynomial. These are manufactured algebra controls, not source values. Therefore retaining only the final traced scalar at intermediate multiplication is invalid. The full six coordinates preserve precisely the data this loss would destroy.

## 4. Scope for actual suppliers

An individual raw source branch, differentiated factor, or coordinate-local seed need not be V-invariant. This theorem does not place it in the rank-six algebra by assertion. A supplier must authenticate invariance of the exact expression it encodes, or use a larger representation until the required invariant grouping has been formed. Differentiation in a distinguished coordinate generally leaves this ring unless organized in an equivariant completed operator.

The scalar trace of a completed normalized old Y belongs to the odd sector. Intermediate invariant products may need both sectors, as the multiplication rule shows. Matrix-valued expressions can use the algebra entrywise only when each encoded entry has the stated coordinate action in the fixed original frame. Noncommutative matrix products remain ordered; the six-coordinate formulas concern their commutative coefficient ring.

Localization at already authorized symmetric denominator factors is compatible with this free module structure: use T[D^-1] and the same six basis elements. This does not authorize any new denominator or prove that a proposed D clears the actual source. Global polynomial generation alone does not acquire source coefficients, price a DAG, certify memory, or prove obstruction vanishing.

## 5. Manufactured controls

check.py verifies all36 basis products against the companion matrices and independent monic remainders, the global homogeneous a² identity, six generator character checks, three trace-basis identities, and the non-ideal trace-kernel example. It also checks both companion algebra relations and commutation. All passed; receipt.json records the result. Only low-degree formal polynomials are used. No HM source value, jet, partition coefficient, section coefficient or detector value was evaluated.
