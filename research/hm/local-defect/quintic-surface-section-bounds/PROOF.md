> Publication scope: preserved mathematical proof/audit. Historical statements that rank eight remains open are superseded only after the final assembly and all its prerequisites. No source-instance evaluation or formal verification is claimed here.

# Quintic systems on surfaces of degree at least seventeen

## Results

Work over an algebraically closed field of characteristic zero (the proofs below only need an infinite ground field after geometric base change). Let Z be a closed subscheme of P4 of dimension two and degree d. Allow nonreduced structure, embedded components, and lower-dimensional components. Assume the complete quintic system H0(I_Z(5)) is nonzero and has no fixed divisor.

1. If d >= 17, then h0(I_Z(5)) <= 8 and h0(I_Z(4)) <= 1.
2. If d = 20, then h0(I_Z(5)) <= 6.

Neither result requires Z to be arithmetically Cohen--Macaulay.

Consequently, in the established rank-six branch with two rank-ten sheaves E=F* and R, determinant O(5), at least twenty global sections each, and generation outside codimension two, the second-Chern pairs (5,20) and (20,5) are impossible. The only remaining pairs are

    (c2(F),c2(R)) = (10,15) or (15,10).

This is a necessary structural restriction, not an exclusion of rank six.

## 1. A plane-scheme lemma, with nonreduced residuals

Let D be any zero-dimensional closed subscheme of P2 of length d >= 17. Suppose there is a vector space W contained in H0(I_D(5)) whose common zero locus has no curve. Write i_j=h0(I_D(j)). We prove

    i_0=i_1=i_2=i_3=0,  i_4<=1,  i_5<=6.       (1)

For every nonzero plane form g, a member q of W can be chosen coprime to g. Indeed, for each of the finitely many irreducible factors p of g, the members divisible by p form a proper linear subspace of W, since W has no fixed curve. Over an infinite field their finite union does not exhaust W.

If a nonzero cubic f vanished on D, choose q in W coprime to f. Then D is a closed subscheme of the zero-dimensional complete intersection V(f,q), of length 3*5=15, contradicting d>=17. Thus i_3=0; multiplication by any nonzero form shows that i_j=0 also for j<3.

Suppose now that two independent quartics f,h vanish on D. Write

    f=g a,  h=g b,

where g is their homogeneous greatest common divisor, t=deg(g) belongs to {0,1,2,3}, and a,b are coprime forms of degree 4-t. Choose q in W coprime to g; when t=0 any nonzero q suffices.

Let T=D intersect V(g) and let D' be the residual scheme defined by I_D:g. For t=0 take T empty and D'=D. The standard multiplication-by-g sequence is exact:

    0 -> O_D'(-t) -> O_D -> O_T -> 0.

This follows directly from the kernel and image of multiplication by g, and imposes no reducedness, transversality, or disjointness requirement. Hence

    length(D)=length(T)+length(D').

Because g and q are coprime and both vanish on T, T is a closed subscheme of their complete intersection, so length(T)<=5t. Because ga and gb vanish on D, a and b belong to I_D:g. Their coprimeness implies

    length(D') <= (4-t)^2.

Consequently

    d <= 5t+(4-t)^2 = 16,14,14,16

for t=0,1,2,3 respectively. This contradicts d>=17. Thus i_4<=1.

For completeness, let A be the saturated homogeneous coordinate ring of D, with Hilbert function H(j)=dim A_j. A linear form l avoiding every point in the finite support of D is a nonzerodivisor on A. To see this directly, a form annihilated by l restricts to zero on D because l is invertible there; saturation then puts that form in I_D. Thus

    H(j)-H(j-1)=dim(A/lA)_j.

The algebra A/lA is standard graded and Artinian. Once one of its graded pieces vanishes, all later ones vanish. Since H eventually equals d, H must strictly increase at every step until it reaches d. Now H(4)=15-i_4>=14, while H(4)<=15<d. Hence H(5)>=15 and

    i_5=21-H(5)<=6.

This establishes (1) for arbitrary D, including nonreduced schemes with overlapping residual and trace supports.

## 2. Sharper plane bound when d=20

There are two cases.

If i_4=0, then H(4)=15<20, so H(5)>=16 and i_5<=5.

If i_4=1, take a nonzero quartic f vanishing on D and choose q in W coprime to f. Then D is a closed subscheme of V(f,q), and both schemes have length twenty. A closed inclusion of finite schemes of the same length is an equality: the kernel of the quotient of structure sheaves has length zero. Thus D is the complete intersection of f and q. Its ideal has the Koszul resolution

    0 -> O_P2(-9) -> O_P2(-4) plus O_P2(-5) -> I_D -> 0.

In degree five this yields i_5=3+1=4, using H1(O_P2(-4))=0. Equivalently, its saturated homogeneous ideal in degree five is f*S_1 plus the one-dimensional span of q, a direct sum since q is not divisible by f.

Therefore, when d=20,

    2i_4+i_5 <= 6.                              (2)

More precisely this expression is at most five if i_4=0 and equals six if i_4=1.

## 3. General plane sections without an ACM assumption

Choose a general hyperplane H=P3 in P4, and then a general plane L=P2 in H. Set C=Z intersect H and D=C intersect L scheme-theoretically.

The first equation can be chosen to avoid every associated point of O_Z, and the second to avoid every associated point of O_C. These equations are therefore nonzerodivisors on the corresponding structure sheaves. Zero-dimensional associated points are avoided by choosing hyperplanes not passing through them. Properness of the sections and two successive differences of the Hilbert polynomial show that D is zero-dimensional of length d. In fact the leading term d*t^2/2 of the surface polynomial has constant second difference d; all lower-degree terms disappear.

Let B be the base scheme of H0(I_Z(5)). The absence of a fixed divisor means dim(B)<=2. A general plane L meets B in dimension at most zero, so the image W of the restriction

    H0(I_Z(5)) -> H0(I_D(5))

has no fixed curve in L. In particular W is nonzero. All the regularity and proper-intersection conditions can be imposed simultaneously: each holds on a dense open set in the relevant flag parameter space.

The regular-section choices give exact ideal-sheaf sequences

    0 -> I_Z(j-1) -> I_Z(j) -> I_C,H(j) -> 0,
    0 -> I_C,H(j-1) -> I_C,H(j) -> I_D,L(j) -> 0.

One obtains these by tensoring the structure-sheaf sequences with the respective hyperplane quotients. The nonzerodivisor conditions kill Tor_1. No surjectivity on global sections or vanishing of intermediate cohomology is assumed.

Put z_j=h0(I_Z(j)) and c_j=h0(I_C,H(j)). Both z_0 and c_0 vanish since Z and C are nonempty. Taking global sections gives only the needed inequalities

    z_j <= z_(j-1)+c_j,
    c_j <= c_(j-1)+i_j.

By (1), z_j=c_j=0 for j<=3. Hence

    c_4 <= i_4,
    c_5 <= i_4+i_5,
    z_4 <= i_4,
    z_5 <= 2i_4+i_5.

Using (1) proves z_4<=1 and z_5<=8 for d>=17. Using (2) proves z_5<=6 when d=20.

## 4. Rank-six application

The local source ../full-support-equivariant-chern-congruences/PROOF.md establishes that the rank-six branch has n=10, k=5, and

    (c2(F),c2(R)) in {(5,20),(10,15),(15,10),(20,5)}.

We first justify the dual-Chern identity. In the saturated-image sequence

    0 -> F -> J tensor O_P4 -> R -> 0,

R is torsion-free. At any point of codimension e>=2 the depth lemma gives depth(F)>=min(e,depth(R)+1)>=2. Thus F is torsion-free and S2, hence reflexive. On the smooth ambient space it is locally free outside a closed set of codimension at least three. There dualization preserves c2, and deleting a codimension-at-least-three subset does not change the codimension-two Chow group. Consequently

    c2(F*)=c2(F).

The same sequence shows R is globally generated. At every codimension-one point R is free, so the sequence locally splits and the dual evaluation J* tensor O -> F* is surjective. Thus F* is generated outside codimension two. Both M=F* and M=R have rank ten and first Chern class five.

The irreducibility of J gives H0(F)=0: it is an invariant subspace of J, and cannot equal J because F has rank ten. Hence J injects into H0(R). Likewise H0(R*) is an invariant subspace of J*, cannot be all of J* because R* has rank ten, and therefore vanishes. Dualizing the sequence and taking sections now injects J* into H0(F*). In particular each M has at least twenty global sections.

The general section-quotient lemma in ../rank-nine-defect-two-sided/PROOF.md, Section 1, applies to a torsion-free sheaf of any rank generated outside codimension two. Applied with rank ten, nine sufficiently general sections give

    0 -> O_P4^9 -> M -> I_Z(5) -> 0,

where Z has codimension at least two and its surface cycle has degree c2(M). The quotient is generated outside codimension two, so its complete quintic system has no fixed divisor. This use of the lemma requires neither local freeness of M nor generation at codimension-two points.

Because H1(O_P4)=0,

    h0(I_Z(5))=h0(M)-9>=11.

The surface cycle degree of Z is c2(M). In either pair involving twenty, choose the corresponding M with c2(M)=20. Then Z has dimension two and degree twenty. Section 3 gives h0(I_Z(5))<=6, contradicting the lower bound eleven. Thus both pairs involving twenty are excluded, leaving only (10,15) and (15,10).

## Evidence boundary

Only the existing local proof files, universal plane complete-intersection and residual-scheme algebra, elementary Hilbert functions, and regular hyperplane restriction sequences were used. No actual source or operation matrix, rank instance, selected input, jet, residue, or other problem-specific evaluated object was inspected or computed. The only new write is this local proof deliverable.
