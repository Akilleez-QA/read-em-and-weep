# Actual rank-two Gauss exclusion by endpoint flags

## Result and scope

For the actual rank-17, degree -54 kernel bundle E inside the constant 30-space H, the generic second fundamental form has rank at least 3. Consequently the actual positive square endpoint satisfies

    rank(l^2 : M2,+ -> M4,+) >= 27

for general l. This does not prove rank 13 for the second fundamental form, positive-square surjectivity, a smoothing closure, or an improvement of the generic four-or-five section-count alternative.

The proof uses saturated Gauss flags, invariant divisors, complete-flag integer identities, and exact abstract G-characters. It uses no chosen HM coefficients, actual matrix or rank evaluations, local-model experiments, or horizontal direct-sum assumption. All earlier published files are left unchanged.

The inputs from the frozen notes are:

- E has rank 17 and degree -54, H0(E(1))=0, and the quotient Q is ample.
- E contains no nonzero constant subbundle and spans H.
- H=2A+2V+2P4+2D5; its center is even and it has no invariant vector.
- Every saturated Gauss stage is G-equivariant. Every line quotient of a complete rank-one flag has even degree.
- Every determinant derivative zero divisor is invariant and has degree in S=<12,20,30>.
- A hypothetical rank-two SF gives the plateau F0<...<Fm, Fk=E, m=k+l, rank Fi=p+2i, p=17-2k, q=13-2l. The endpoints have rank-one SF; all interior stages contain no constants and span H.
- The already proved orbit/endpoint exclusions leave only (k,l)=(1,1),(1,2),(2,1).

These inputs, including all saturation statements, are proved in RANK-ONE-GAUSS-FLAG-DEGREE-EXCLUSION.md, RANK-TWO-GAUSS-PLATEAU-NECESSARY-BOUND.md, TWIST-ONE-ACTUAL-SECTION-KERNEL-VANISHING.md, and GAUSS-DETERMINANT-ORBIT-RAMIFICATION.md.

Write A0=Fm^perp, of rank q, and let U in H and Z in H* be the constant spans of F0 and A0. Write n=dim U, n'=dim Z, A=-deg F0, B=-deg A0. The existing endpoint lemma gives n>=p+m and n'>=q+m.

## 1. A diagonal-contact lemma

Consider two rank-one complete Gauss flags with first lines O(-h) and O(-h') in constant spaces U and Z. Their line maps give a pairing section

    P in H0(P1 x P1, O(h,h')).

If the rank-a and rank-b osculating stages pair to zero at the same parameter, then P vanishes along the diagonal to order at least a+b-1.

Here is a proof which also handles ramification. On the dense open where every adjacent derivative in the two complete flags is nonzero, choose coordinate t and local line lifts f(t),g(t). The rank-a stage is spanned by f,...,f^(a-1), and the rank-b stage by g,...,g^(b-1). This follows inductively from the regular derivative maps and their nonzero leading terms. Orthogonality gives

    <f^(i)(t),g^(j)(t)>=0   for 0<=i<a, 0<=j<b.

Put c_ij(t)=<f^(i)(t),g^(j)(t)>. Differentiation gives c_ij'=c_(i+1,j)+c_(i,j+1). Induct on total order s. If all c_ij with i+j<s vanish, the displayed recurrence makes all entries of total order s equal up to sign. For s<=a+b-2 at least one such entry belongs to the orthogonality rectangle, so all entries of that order vanish. In particular partial derivatives of P normal to the diagonal vanish through order a+b-2.

This proves the multiplicity at the generic point of the diagonal. Since P is a global regular section and the diagonal is a prime Cartier divisor, its divisor contains (a+b-1) times the entire diagonal. Equivalently P is the diagonal equation to that power times a section of O(h-a-b+1,h'-a-b+1). No poles or negative corrections arise at ramified parameters. Thus if min(h,h')<a+b-1, P=0. In that case U and Z are orthogonal constant spaces.

Apply this to the plateau. The j-th forward transform of F0 lies in Fj, including j=m. If n=p+m, that transform is U itself, so U is orthogonal to A0 and hence to Z. If n>p+m, its m-th transform is the rank-(p+m) osculating stage, and Fm annihilates A0. The preceding lemma gives diagonal order at least

    (p+m)+q-1 = 29-m.                              (1)

The same reasoning is available from the upper dual endpoint. Consequently exactly one of these alternatives holds:

1. U and Z are orthogonal. Since n+n'>=(p+m)+(q+m)=30, they must be complementary annihilator spaces, with n=p+m and n'=q+m.
2. They are not orthogonal. Then n>=p+m+1, n'>=q+m+1, and both first-line degrees h,h' are at least 29-m.

Evenness rounds the last bound to 28 when m=2 and to 26 when m=3.

## 2. Full rank-one flag arithmetic, including integrality

For a complete rank-one flag in a constant n-space, write its graded line degrees a1,...,an, and

    delta_j = a_(j+1)-a_j-2 in S.

For its rank-r stage of degree -D, put s=n-r. Then

    R := n(D-rs)
       = s sum_(j<r) j delta_j
         + r sum_(j>=r) (n-j) delta_j,             (2)

and, independently,

    h := -a1 = n-1 + (1/n) sum_(j=1)^(n-1) (n-j) delta_j
       must be an EVEN INTEGER.                  (3)

The other degrees are -h+2(i-1)+sum_(j<i)delta_j. Thus equations (2)-(3), rather than just the weighted degree equation, are retained below.

All finite arithmetic in this note can be checked by the accompanying exhaustive dynamic program. For fixed n,r,Dmax it enumerates the finitely many possible pairs

    (R,T) = (sum_j w_j delta_j, sum_j (n-j)delta_j),

with R<=n(Dmax-rs), each delta_j in S, and positive w_j as in (2). It retains exactly those pairs with R divisible by n, T divisible by n, and even D and h. Collapsing vectors with the same (R,T) loses no information for these degree/h tables. The optional full-character check later enumerates all vectors instead.

## 3. Nonorthogonal endpoints are impossible

The plateau identity gives

    lA+kB+sum_j w_j delta_j = 54m-2klm.            (4)

### Profile (1,2)

Here p=15,q=9,m=3. Nonorthogonality gives n>=19,n'>=13, hence A>=60,B>=36. But (4) requires 2A+B<=150, whereas its minimum is 156.

### Profile (2,1)

Here p=13,q=11,m=3. Nonorthogonality gives n>=17,n'>=15. Thus A>=52 and A+2B<=150, so B<=48. The upper rank-one degree bound forces n'=15 and B in {44,46,48}.

For B=46 the upper weight in (2) is 30, below the least positive invariant weight 48. For B=48 it is 60, which is not in <48,80,120,132,220,330>. Thus B=44. Equality forces its whole complete flag to be unramified, so h'=14. This contradicts (1), which requires h'>=26.

### Profile (1,1)

Here p=15,q=11,m=2. Nonorthogonality gives n>=18,n'>=14. Equation (4) reads

    A+B+delta=104,     delta in S.                 (5)

The rank-one bound and evenness force n in {18,19}, n' in {14,15,16}, A<=70, B<=58. Equations (2)-(3) give the following exhaustive degree lists:

| Stage | Span dimension | Possible degree magnitudes within the stated cap |
|---|---:|---|
| rank 15, cap 70 | 18 | 54, 60, 66 |
| rank 15, cap 70 | 19 | 60 |
| rank 11, cap 58 | 14 | 42, 48, 54 |
| rank 11, cap 58 | 15 | 44, 52, 56 |
| rank 11, cap 58 | 16 | none |

Combining the lists with (5) leaves only A=60,B=44,delta=0. The upper span is then 15 and its first-line degree is 14, again below the required diagonal order 27. Thus all three profiles have orthogonal, minimally dimensional endpoint spans.

## 4. Exact intersection and saturated projection

Assume this orthogonal alternative, so U=Z^perp, dim U=p+m, dim Z=q+m. Let C_i be the i-th forward transform of F0, and B_j the j-th forward transform of A0. They have ranks p+i and q+j, respectively, through i,j=m.

Set R_i=Fi intersect (U tensor O). These intersections are saturated in U tensor O: they are kernels of its maps to the locally free quotients by Fi. Differentiation gives dR_i subset R_(i+1) tensor Omega. Their endpoint ranks are p and p+m. Every one of the m rank increments is positive. Otherwise equal ranks and saturation give R_i=R_(i+1), so R_i would be a nonzero constant subbundle in the interior stage Fi, which is impossible. Their sum is m, so every increment is exactly one. Since C_i subset R_i and both are saturated in U, this proves

    Fi intersect U = C_i.                         (6)

The projection of Fi to Z* therefore has rank i. Its annihilator in Z has rank q+m-i and contains B_(m-i); equality follows from saturation and equal generic rank. Hence at i=k the saturation of the projected image of E is

    P = (Z tensor O / B_l)*.

Let I be the actual image and tau=length(P/I). Then I and P are locally free of the same rank and det(I)->det(P) is a nonzero regular equivariant map. Its divisor is invariant, with degree tau. Thus

    tau in S,     54 = D_C+D_B+tau,                (7)

where D_C=-deg C_k and D_B=-deg B_l. This allows all possible projection torsion; none is suppressed in obtaining the identity.

Now C_k subset E, so H0(C_k(1))=0 and D_C>=2(17-k). The upper stage B_l has rank 13-l in a span of dimension 13+k-l, so D_B>=(13-l)k. Also C_k is rank one in its own Gauss sense and spans U.

For (2,1), these bounds are D_C>=30,D_B>=24, so equality holds throughout (7). The upper rank-12 stage in a constant 14-space attains the rank-one degree minimum 24; its whole flag is unramified, whose line degrees are all odd. This contradicts center-evenness. Hence (2,1) is completely excluded.

For (1,1), tau<=10; for (1,2), tau<=11. The least positive element of S is 12, so tau=0. Equations (2)-(3), applied to C_k and B_l, now give:

| Profile | (rank C_k, dim U) | (rank B_l, dim Z) | Possible (D_C,D_B) |
|---|---|---|---|
| (1,1) | (16,17) | (12,13) | (32,22), (34,20), (36,18), (38,16), (42,12) |
| (1,2) | (16,18) | (11,12) | (38,16), (42,12) |

For (1,1) the individual lower list in the bounds 32<=D_C<=42 consists of all even values, and the upper list in 12<=D_B<=22 is 12,16,18,20,22. For (1,2) the lower list in 32<=D_C<=43 is only 38,42. These statements are independently reproduced by the verifier.

Since tau=0, there is an actual equivariant exact sequence

    0 -> C_k -> E -> (Z tensor O/B_l)* -> 0.        (8)

No splitting, horizontal or otherwise, is inferred from it.

## 5. The actual twist-one cohomology character

Use W for the negative two-space, W' for its other two-dimensional irreducible, S4=Sym^3 W, and T6=Sym^5 W. The actual, everywhere surjective kernel presentation gives

    0 -> E(1) -> M3,- tensor O
      -> M4,+ tensor O(1) -> 0,

    M3,- = 3W'+3S4+6T6,
    M4,+ = 2V+4P4+3D5.

Since H0(E(1))=0,

    H1(E(1)) = W tensor M4,+ - M3,- = W'+3T6.      (9)

This is a character identity of actual cohomology, not a dimension-only substitution. The O(1) factor is center-odd, as required. The self-duality of W removes any harmless dual convention for P(W*). All line bundles below have their unique G-linearization: G is perfect and admits no nontrivial character.

## 6. Exclude the orthogonal (1,1) case

Here U/C_k is a line O(D_C), and Z/B_l is O(D_B). Thus

    W tensor U injects into Sym^(D_C+1) W,
    Z injects into Sym^(D_B) W.                    (10)

The first follows by twisting 0->C_k->U O->O(D_C)->0 and using H0(C_k(1))=0. The second follows from H0(B_l)=0, since B_l subset E^perp and Q is ample.

The possible dimension-17 submodules U of H are precisely

    U1 = V+P4+2D5,
    U2 = A+P4+2D5,
    U3 = A+2V+2P4,
    U4 = 2A+V+2P4,
    U5 = 2A+2V+D5.

Since all constituents are self-dual, Z has the complementary character H-U. Exact binary-icosahedral character arithmetic gives:

| (D_C,D_B) | U allowed by first injection in (10) | U allowed by second injection |
|---|---|---|
| (32,22) | U2 | U1,U3,U4 |
| (34,20) | U1 | U3,U4 |
| (36,18) | U1,U3 | U5 |
| (38,16) | U1,U2 | U4 |
| (42,12) | U1,U2,U3,U4,U5 | none |

The columns never meet. Therefore (1,1) is impossible. The verifier reproduces the table from the exact Q(sqrt(5)) character ring, testing only whether representation differences have nonnegative integral irreducible multiplicities.

## 7. Exclude the orthogonal (1,2) case

The remaining pairs are (D_C,D_B)=(38,16),(42,12). Here dim U=18, dim Z=12, and the upper quotient Z/B_l is again a line O(D_B). The three possible dimension-18 submodules U of H are

    2P4+2D5,     A+2V+P4+D5,     2A+V+P4+D5.

The injection Z into Sym^(D_B)W, together with

    Sym^12 W = 1+A+P4+D5,
    Sym^16 W = V+P4+2D5,

forces

    (38,16): U=2A+V+P4+D5,
    (42,12): U=A+2V+P4+D5.                        (11)

Consider the complete flag of C_k, a rank-16 stage in U of dimension 18. Its ramification weight in (2) is 18(D_C-32), either 108 or 180. The term involving delta_17 has coefficient 16, so a nonzero such divisor would contribute at least 192. Therefore delta_17=0. The last two graded line degrees sum to D_C and differ by two, so R=(U O)/C_k has an equivariant filtration with line quotients

    O(D_C/2-1),     O(D_C/2+1).

Both have vanishing H1 after twisting by O(1). Consequently

    H0(R(1)) = Sym^(D_C/2) W + Sym^(D_C/2+2) W,
    H1(C_k(1)) = H0(R(1)) - W tensor U.           (12)

Meanwhile the projection line in (8) is O(-D_B), so

    H1(O(1-D_B)) = Sym^(D_B-3) W.                 (13)

This is equivariant Serre duality with K=O(-2) and det W=1. Since H0 of this negative line is zero, the long exact sequence of (8) gives a short exact sequence on H1; semisimplicity of finite G yields the character sum. Equations (11)-(13) predict

    (38,16): H1(E(1)) = W+W'+S4+2T6,
    (42,12): H1(E(1)) = W+3S4+T6.

Neither equals the actual character W'+3T6 in (9). Both cases are impossible.

For an independently checkable refinement, the complete-flag character identity [U]=sum_i chi(O(a_i)) also excludes the first pair directly. D_C=38 has exactly two full ramification vectors: (54,0,...) and (30,12,0,...), whose characters are 1+A+P4+2D5 and 1+V+P4+2D5. For D_C=42 there are eleven vectors satisfying (2)-(3). Exactly one matches the forced U in (11):

    delta=(30,12,12,0,...,0),
    a=(-66,-34,-20,-6,-4,-2,0,2,4,6,8,10,12,14,16,18,20,22).

The other ten have the wrong character. The preceding cohomology contradiction excludes this final vector without assuming that these integer data are geometrically realizable.

## 8. Conclusion and reproduction

All hypothetical rank-two plateau profiles are impossible. The already frozen rank-zero and rank-one exclusions therefore imply generic rank SF>=3. The actual comparison rank(l^2)=24+rank SF gives the claimed square lower bound 27.

Run `python verify_rank_two_gauss_exclusion.py`. The verifier checks bounded hypothetical flag integers, all stated small representation conditions, the complete-vector refinement, and the final actual cohomology-character contradiction. The geometric diagonal, saturation, intersection and projection arguments are proved in the text, not replaced by a computation.
