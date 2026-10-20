# Extension: every canonical positive reflection plane avoids Z3

## Status and statement

This addendum extends PROOF.md; its independent PASS audit is recorded in AUDIT.md. Under the same hypotheses, rank Q≥4 at every point of P(T). Equivariance gives the same conclusion on all twenty-five canonical positive reflection planes. Combined with the already proved negative-reflection-line theorem, Z3 avoids every projective fixed point of every canonical reflection.

We retain q, the invariant conic C={q=0}, and the modules and coefficient maps of PROOF.md. No actual source operation is evaluated.

## 1. The only A5 orbit of size at most nine in P(T)

The effective A5 action on T is irreducible and orthogonal. By the elementary subgroup classification of A5, its proper subgroups of order greater than six are A4 (order twelve) and D5 (order ten). A point orbit of size at most nine has stabilizer order at least seven. The whole A5 fixes no line by irreducibility. Neither does an A4 subgroup: its elements comprise the identity, three involutions, and eight elements of order three. Every linear character is trivial on its normal four-group, and the inner product of any such character with the restriction of the T character is (3−3)/12=0, since the T character is zero on order-three elements. Thus T has no A4-stable line.

Each D5 subgroup is the normalizer of a Sylow-five subgroup. On T its order-five generator has eigenvalues 1,λ,λ^−1 with λ a primitive fifth root. A normalizing involution exchanges the latter two eigenspaces, so the only D5-stable line is the eigenvalue-one axis. The six Sylow-five subgroups yield exactly one orbit of six such axes; their stabilizers cannot be larger, by the previous exclusions. These are the only orbits of size at most nine.

This six-point orbit lies in the canonical thirty-point Heisenberg eigenpoint orbit: in the standard basis, T is the positive space of R e_j=e_−j, and D e_j=ζ^(j²)e_j acts on T with eigenvalues 1,ζ,ζ^4. Its eigenvalue-one axis is Ce0. Thus the six axes are Γ-translates of [e0]. The theorem `../heisenberg-eigenpoint-rank-parity/PROOF.md` gives rank Q≥4 at all six.

## 2. Orbits off the conic

Let O'⊂P(T) be an orbit outside C, other than the six-axis orbit. It has more than nine points and spans T.

There is no nonzero cubic vanishing on O'. Indeed the gcd argument from the ten-point proof works unchanged: the homogeneous gcd of the invariant space of vanishing cubics is invariant because A5 has no characters. The only possible positive-degree gcd of degree at most three is a scalar multiple of q, since the invariant form spaces in degrees one and three vanish and degree two is Cq. Because O' avoids C, dividing by q would give linear forms vanishing on the spanning orbit, impossible. With constant gcd, two suitable cubics have no common component and hence at most nine intersection points by Bezout, again impossible.

Now the two rank arguments in PROOF.md apply unchanged. Odd rank two on O' makes all three-minors identically zero on P(T), producing the impossible quotient O(-1)^6→O(-2)^2. Even rank four kills the T constituent of f|T³; the mixed coefficient map has image in its specific P5 image H because O' spans T; and its cubic annihilators vanish identically. The injectivity of multiplication on the T' coefficient constituent contradicts that vanishing. Hence even rank≥5 and odd rank≥3 on O', giving rank Q≥4.

## 3. Orbits on the conic

The A5 action on the smooth conic C≅P1 is faithful: an element acting identically on C is projectively scalar on its spanning plane. A point stabilizer in a finite subgroup of PGL2(C) is cyclic. The possible element orders in A5 are 1,2,3,5, so every orbit on C has at least twelve points. Every such orbit spans T by irreducibility.

Suppose first that the odd block has rank two at a point of C. It has rank two on that point's orbit. Each three-minor restricts to a section of O_P1(6), since O_P(T)(1)|C=O_P1(2). It vanishes at at least twelve points, hence identically. Thus the odd block has rank at most two everywhere on C, and repeated-input injectivity makes this rank exactly two. Its image bundle I on C is then simultaneously a quotient of O_P1(-2)^6 and, by the repeated-input map, isomorphic to O_P1(-4)^2. But Hom(O_P1(-2),O_P1(-4))=0. Contradiction. Therefore odd rank≥3 everywhere on C.

Suppose next that the even block has rank four at a point of C, and let O' be its orbit. The arguments of Section 2 of PROOF.md do not require q(u)≠0: the P5 infinitesimal action has rank four even for isotropic u, and the invariant metric maps to a nonzero skew matrix for every u≠0. Thus the T constituent is killed, all mixed coefficients lie in the specific H≅P5, and their map g:T'⊗T→H is nonzero.

The cubic-annihilator map

    F:T'→Sym³T,    F(s)(u)=tr(g(s,u)K(u))

is nonzero and injective, by the multiplication argument of PROOF.md. Its image is therefore a copy of T'. Each F(s) vanishes at all points of O', at least twelve points on C. Its restriction has degree six, so it vanishes identically on C. Consequently every F(s) is divisible by q, and im F lies in q·T≅T. This is impossible because T' and T are inequivalent irreducibles. Hence even rank≥5 everywhere on C.

The parity ranks add to at least eight on C, so rank Q≥4 there.

## 4. Consequences and boundary

The six-axis points, all other off-conic orbits, and the conic exhaust P(T), proving rank Q≥4 throughout that plane. Normalizer equivariance covers its twenty-five translates.

The canonical reflection fixed locus in projective space is the union of its positive plane and negative line. The negative lines already have residual rank≥4 by `../canonical-line-parity-exclusion/PROOF.md`. Thus no point of Z3 is fixed by any canonical reflection. This is a stronger exclusion than the 250-point-orbit result; it still does not prove that Z3 itself is empty.

## 5. Remaining finite Z3 support: orbit sizes and cardinality

Assume in addition the previously established finiteness of Z3. Then every orbit in its support has size 600, 1000, or 3000. In particular

    |Z3,red| = 600a+1000b+3000c ≤ 4000

for nonnegative integers a,b,c. Thus a nonempty support has at least 600 points, and its cardinality is divisible by 200. These are necessary restrictions, not existence assertions.

Here are the group and degree details. Write N=A⋊K with A≅F5², K≅SL2(F5), and |N|=3000. Outside the canonical thirty eigenpoints E, the A action is free, as proved in the earlier point-orbit results. Since E has rank Q≥4, a stabilizer S of a Z3 point injects into K.

Every involution of N is conjugate by A to the central involution c of K. Indeed an involution must project to the unique involution c of K (its projection cannot be trivial because A has odd order), and c acts as −1 on A. Consequently its form is (a,c), and A-conjugation changes a by twice an arbitrary A element, allowing a to be set to zero. Its projective fixed locus is one canonical positive plane together with its canonical negative line. All these loci are disjoint from Z3 by the plane and line bounds. Therefore S has no involution and has odd order by Cauchy's theorem.

Its injective image in K has odd order dividing 120, hence order 1,3,5, or 15. The last is impossible. An odd-order subgroup of K injects into A5. A subgroup of A5 of order 15 would have a unique Sylow-five subgroup (its number divides three and is one modulo five), hence would be contained in the order-ten normalizer of that subgroup, a contradiction. Thus |S| is 1,3, or 5, giving N-orbit sizes 3000,1000,600.

Finally Z3 is the common zero locus of the degree-eight minors of the linear matrix b. Because this base locus is finite in P4, four general linear combinations of the minors cut out a zero-dimensional complete intersection containing it, of length 8^4=4096. One can choose these successively to avoid every positive-dimensional component of the preceding intersections; no such component is contained in the finite base locus. Hence |Z3,red|≤4096. The orbit-size formula makes that cardinality a multiple of 200, so it is at most 4000.

No conjugacy assertion about order-five stabilizers in N is used: in particular, this does not assume that their cocycles can be removed by A-conjugation.
