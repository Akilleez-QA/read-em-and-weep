# Balanced conic restriction and fourth-order normal-jet detection

## Theorems and scope

Let R=P(V_+) be the positive fixed plane of HM inversion, let F_R be the actual normalized HM restriction, and let B=End_0(F). The fixed-plane theorem proves that F_R is stable and has the Steiner resolution

       0 -> A tensor O_R(-3) -> D tensor O_R(-2) -> F_R -> 0,
       dim A=3, dim D=5.

**Conic balance.** For a general smooth conic C in R, with C identified with P1,

       F_C = O_P1(-1) directsum O_P1(-1).

This is not an assertion for every smooth conic. The exceptional conics are cut out by the nonzero determinant of an actual symmetric three-by-three cohomology pencil, hence by a cubic equation in the conic parameter space, allowing multiplicity and reducibility.

**Normal jets.** On the corresponding nonempty open of smooth inversion-even quadrics Q, put C=Q intersect R, I=I_(C/Q), and G=B_Q(4). Then

       I^m G / I^(m+1) G = O_P1(8-2m)^(3(m+1)),
       H0(Q,I^5G)=0.

The graded piece has inversion character (-1)^m. Every even global section is detected through normal degree four; every odd global section is detected through normal degree three. The dimensions of the graded section spaces for degrees zero through four are

       27, 42, 45, 36, 15.

No splitting of the full higher-neighborhood filtration, lifting of arbitrary jets, maximal rank, or exact twist-four corank four is asserted.

## 1. The actual coefficient representations

The fixed-plane theorem identifies V_+ as an irreducible genuine three-dimensional A5 module. The actual U=H0(F(3)) is the standard four-dimensional A5 module, and its evaluation is onto on R. Since inversion acts trivially on U and on O_R(1), it acts trivially on F_R. Thus all coefficient spaces below are genuine A5 representations, not projective representations with an unexamined central sign.

Take the intrinsic minimal Steiner presentation. Its degree-two generators give D=H0(F_R(2)), and its degree-three relation space is A. Equivalently A=H1(F_R), by the Steiner resolution and H2(O_R(-3))=C. This last identification is equivariant: the canonical linearization of O_R(-3) has trivial determinant-character correction, since A5 has no nontrivial characters.

We claim A is irreducible. A three-dimensional A5 representation is either irreducible or a sum of three trivial representations, because A5 has no nontrivial irreducible representation of dimension two. Suppose A were trivial. An equivariant linear presentation map

       A tensor O_R(-3) -> D tensor O_R(-2)

then gives each of its three columns in Hom_A5(V_+,D). Since dim D=5 and V_+ is irreducible of dimension three, its multiplicity in D is at most one. All three columns would therefore be scalar multiples of the same V_+-valued linear column. The map would have rank at most one, contradicting its fiberwise rank-three subbundle inclusion. Thus A is one of the two irreducible three-dimensional A5 modules.

## 2. The symmetric conic cohomology pencil

For a conic equation q, the actual restriction sequence is

       0 -> F_R(-2) --q--> F_R -> F_C -> 0.

Since H0(F_R)=0, it identifies H0(F_C) with the kernel of

       mu(q):H1(F_R(-2)) -> H1(F_R)=A.

The rank-two determinant identity F_R*=F_R(1) and Serre duality on R give the actual equivariant identification

       H1(F_R(-2)) = A*.

Indeed the relevant dual is H1(F_R* tensor O_R(-1))=H1(F_R). Its two sides have dimension three. All determinant-line normalizations differ only by an overall scalar, which does not affect the argument.

Under this duality mu(q):A*->A is symmetric. For classes s,t in H1(F_R(-2)), the associated scalar pairing is obtained by cup product, the alternating rank-two wedge pairing, multiplication by q, and trace

       H2(O_R(-5)) --q--> H2(O_R(-3))=C.

Interchanging s,t contributes a minus sign from cohomological degree one and another minus sign from the alternating bundle pairing. The two signs cancel. Thus the entire actual conic pencil is an A5-equivariant linear map

       Sym^2(V_+*) -> Sym^2 A.

It is not the zero map. The twist-minus-two Steiner sequence injects

       H1(F_R(-2)) -> A tensor H2(O_R(-5)).

Multiplication into H1(F_R)=A tensor H2(O_R(-3)) is componentwise contraction. The pairing

       H0(O_R(2)) tensor H2(O_R(-5)) -> H2(O_R(-3))

is perfect by Serre duality. Therefore a nonzero class in the displayed subspace cannot be killed by every quadratic q. This verifies nonzero actual multiplication, rather than assuming a generic rank for a matrix of the right size.

For either irreducible three-dimensional A5 representation T,

       Sym^2 T = 1 directsum 5.

For example the symmetric-square character is (6,2,0,1,1) on the classes of orders 1,2,3,5,5, namely the sum of the trivial and five-dimensional characters. Both domain and target of the pencil have this multiplicity-free decomposition. Its nonzero image is therefore 1, 5, or 1 directsum 5.

Each possibility contains an invertible symmetric form. The invariant form on the irreducible odd-dimensional A is nondegenerate and symmetric. The complementary five-space is its trace-zero symmetric subspace; after putting this universal invariant form into standard diagonal coordinates, diag(1,1,-2) is an invertible trace-zero form. This is an abstract representation-theoretic form, not an evaluation of any selected HM coefficients.

Consequently det mu is a nonzero homogeneous cubic. Its nonvanishing open meets the dense smooth-conic open in P5. For any smooth conic in that intersection, H0(F_C)=0. Since deg F_C=-2, its splitting O(a) directsum O(-a-2), a>=-1, must have a=-1. This proves balance.

## 3. Independent incidence proof with explicit descent

The preceding A5 argument already proves the actual assertion. The following argument verifies the proposed descent interface and shows the broader fact for any stable rank-two bundle E on P2 with c1(E)=-1.

Let S=P(H0(O_P2(2))) and let T subset P2 times S be the universal conic, with maps e:T->P2 and p:T->S. The map e is a P4-bundle. On a general smooth conic C, write E_C=O(a) directsum O(-a-2), a>=-1. Suppose the generic a is nonnegative, and shrink to an open S0 of smooth conics with constant splitting type.

There is a line subbundle L of e*E on T0=p^-1(S0) restricting to the unique maximal O(a) on every conic. To see existence without assuming a global square root of O_C(1), work etale-locally on S0 where the smooth conic family is a P1-bundle and has a relative degree-one line bundle. Twisting by its minus-a power gives fiber H0 dimension one; cohomology and base change gives a line bundle of sections, and evaluation recovers the maximal line subbundle. Uniqueness of that subbundle makes these local constructions agree and descend on overlaps.

Along a conic fiber, the relative tangent bundle for e is the kernel of the complete evaluation map

       0 -> T_(T/P2)|C -> H0(O_P1(4)) tensor O_C -> O_P1(4) -> 0.

Hence T_(T/P2)|C=O_P1(-1)^4. For example its rank is four, degree is minus four, and its H0 is zero; as a subbundle of a trivial bundle all splitting degrees are nonpositive, forcing all four to equal minus one.

The canonical connection on e*E in directions tangent to the fibers of e gives the second fundamental form

       L -> (e*E/L) tensor Omega_(T/P2).

Its Hom bundle restricts to O_P1(-2a-1)^4 on every conic in S0. It therefore vanishes. Equivalently, the map T0->P(E) defined by L has zero relative differential over P2.

Here descent can be checked directly rather than left as an unspecified lemma. Put K=C(P2). Since e is a projective-space bundle,

       C(T)=K(t1,t2,t3,t4).

After trivializing E at the generic point, the line L has a rational projective-coordinate ratio f in this field (or is the constant infinity line). Zero relative differential says df=0 in Omega_(C(T)/K). In characteristic zero the constants of this purely transcendental extension are exactly K, so f belongs to K. Thus L determines a rational line in E over P2 itself.

Saturate that rational line in E. The resulting rank-one saturated subsheaf on the smooth surface is reflexive, hence O_P2(d). Its quotient is torsion-free and its failure to be a line subbundle is supported at finitely many points. A general conic avoids those points. On the incidence over their complement, the two line subbundles agree because their maps to P(E) agree generically and P(E) is separated. Restricting to a general conic therefore gives 2d=a>=0. This contradicts stability of E, whose slope is -1/2. Hence the generic a is -1.

A primary-source confirmation is Al Vitter, Restricting Semistable Bundles on the Projective Plane to Conics, arXiv:math/0310076v2, Theorem 1 and Corollary 1, printed pages 4–5: https://arxiv.org/pdf/math/0310076 . Its theorem applies to slope-semistable bundles over C and gives exactly this generic balanced rank-two restriction. The explicit rational descent above supplies the interface that its incidence proof cites as a descent lemma.

## 4. Passing to actual even quadrics

Restriction of an even quadric equation to R is its arbitrary positive symmetric block. Thus every smooth conic in R occurs as Q intersect R for some smooth even Q: choose any nondegenerate negative block as well. The preimage of the balanced smooth-conic open is a nonempty open in the irreducible smooth-even family. It can also be intersected with the independently proved lower-twist-good even open. No generic open outside the even subsystem is used.

For such Q, the ideal I is generated by the two odd linear forms W=V_-*. They form a regular sequence, and

       I/I^2 = W tensor O_C(-1)=W tensor O_P1(-2).

Balance gives B_C=O_C^3, and inversion acts trivially on it. Regular immersion therefore gives the canonical graded formula

       I^mG/I^(m+1)G
         = B_C(4-m) tensor Sym^m W
         = O_P1(8-2m)^(3(m+1)).

It has pure parity (-1)^m. The splitting formula is an isomorphism of bundles; no particular trivialization or splitting of the full filtered neighborhood is claimed.

## 5. Exact finite-jet consequences

The companion FIXED-CONIC-PARITY-JETS-AND-POSITIVE-GATE.md proves, uniformly for every smooth even Q,

       H0(Q,I^7G)=0.

Its proof uses the actual ideal-power resolution, H0(B_Q(-3))=0 and H1(B_Q(-4))=H2(B_Q(1))*=0. The present argument imports that proved result, not any unstated infinite-order separation principle.

On the balanced-conic open the sixth and fifth graded pieces have no sections: they are respectively O(-4)^21 and O(-2)^18. The two exact ideal-power quotient sequences therefore give

       H0(I^5G)=H0(I^6G)=H0(I^7G)=0.

This proves injectivity of H0(G)->H0(G/I^5G). Since the fourth graded piece is even, H0(I^4G)_-=H0(I^5G)_-=0; odd sections are already detected modulo I^4. Thus allowed nonzero leading orders are 0,2,4 for even sections and 1,3 for odd sections.

For m=0,1,2,3,4 the graded pieces have H1=0 and the section dimensions are 27,42,45,36,15. Iterating their exact sequences gives

       H1(G/I^5G)=0,
       h0(G/I^5G)_+=87,  h0(G/I^5G)_-=78.

These are dimensions of finite-neighborhood section spaces, not dimensions of the actual global adjoint section spaces. The canonical injective restriction retains all compatibility and extension conditions. In particular neither the actual 34-to-38 odd Koszul map nor the positive excess boundary is proved maximal rank by this calculation.

## Dependencies

- INVERSION-EVEN-TWIST-THREE-VANISHING.md: actual stable Steiner fixed plane and A5 representations.
- FIXED-CONIC-PARITY-JETS-AND-POSITIVE-GATE.md: equivariant ideal powers and uniform seventh-power vanishing.
- Horrocks–Mumford's actual normalizer representation and its character table; Vitter's primary conic restriction theorem as cited above.

No selected HM/source coefficients, actual matrix ranks, scans, experiments, or public posts enter the proof.
