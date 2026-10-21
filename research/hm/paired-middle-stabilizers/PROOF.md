# Order-five stabilizers of the paired middle scalars

Work over C, with the actual normalizer-equivariant module H and parameter line P(W') of the pinned middle-obstruction construction. No selected parameter, matrix rank, or coefficient is evaluated.

## Exact dependencies

- [PR528, commit bd9a26837bb79b2e21cf35d6586d3ba3d6ca83fa](https://github.com/Akilleez-QA/read-em-and-weep/blob/bd9a26837bb79b2e21cf35d6586d3ba3d6ca83fa/research/hm/middle-family-parity/PROOF.md): the actual exact sequence
  0 -> End_0(T) O -> (E tensor Lambda3 T) O(2) -> F -> 0,
  the identification V=(F O(1))* and the symmetric actual obstruction Q:V -> V*.
- [PR531, commit 39671b0c8bf41a253c031336aed719f9d465ef9b](https://github.com/Akilleez-QA/read-em-and-weep/blob/39671b0c8bf41a253c031336aed719f9d465ef9b/research/hm/middle-trivial-nonvanishing/PROOF.md): the trivial block is nonzero, with reduced determinant divisor Omega, and b_generic belongs to {0,24}.
- The representation conventions Lambda3 T=E* tensor W0 and det W0=1 are those of PR528, from [Horrocks--Mumford (1973), Section 3.3](https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf). The quotient G=SL2(F5) acts naturally on the nonzero Heisenberg characters, a two-dimensional F5 vector space minus zero. Its action on P(W') factors through A5; the unique orbit of size twelve is Omega.

## 1. The coefficient twist cancels on an inverse pair

Fix a nontrivial character chi. Its stabilizer C in G has order five: in coordinates taking chi to (1,0), it consists of matrices [[1,t],[0,1]]. Set

U_chi=(End_0 T)_chi, L_chi=(End E)_chi.

Let C_tilde be the inverse image of C in the finite normalizer N. Both coefficient lines are one-dimensional C_tilde-modules; individually they need not descend to C, since Gamma acts through chi. Since E tensor Lambda3 T=(End E) tensor W0, the actual character summand of the sequence in PR528 is the C_tilde-equivariant sequence

0 -> U_chi O -> (L_chi tensor W0) O(2) -> F_chi -> 0.

Taking determinants, with their actual equivariant linearizations, gives

F_chi = L_chi^2 tensor U_chi^{-1} tensor O(4).

This formula does not assume a trivial coefficient character or choose a splitting of the normalizer extension. The trace pairings on End T and End E identify U_chi^{-1} with U_(chi^{-1}) and L_chi^{-1} with L_(chi^{-1}), equivariantly. Indeed trace is nondegenerate and invariant, and a character pairs only with its inverse. Consequently

F_chi tensor F_(chi^{-1}) = O(8)

as C_tilde-linearized bundles with the standard linearization on the right. The paired tensor has trivial Gamma action, so this identity descends to C without an additional character twist. By V=(F O(1))*, the inverse-pair coefficient of the symmetric form Q is therefore a C-invariant section of the standard O(10). Thus there is no hidden order-five character twist in this scalar.

## 2. Three-term normal form

Choose eigen-coordinates x,y for C on W'^*, with eigenvalues zeta^r,zeta^{-r}, where zeta is a primitive fifth root and r is nonzero modulo five. Every invariant binary form of degree ten has monomials x^(10-k)y^k satisfying 2rk=0 modulo five. Hence the actual inverse-pair scalar has the form

a_chi(x,y)=A_chi x^10+B_chi x^5 y^5+C_chi y^10.

The constants here are not computed or asserted nonzero. This is a restriction on the actual obstruction, not on an arbitrary replacement map. The zero polynomial remains possible.

If a_chi is nonzero, each of its zeros away from the two C-fixed points occurs in a C-orbit of five points, with equal multiplicity along that orbit. At a C-fixed point, its order of vanishing is either zero, five, or ten, by the displayed polynomial. In particular a nonzero paired scalar cannot have a simple zero at either fixed point.

The two fixed points lie in Omega. One way to see this is that their projective stabilizers contain C5. In A5 no larger cyclic subgroup contains C5, whereas a point stabilizer of a finite subgroup of PGL2(C) is cyclic (use the faithful tangent character). Their stabilizers therefore have order five, and their orbit has size twelve.

## 3. Exact root patterns

Equivalently a nonzero paired scalar is a binary quadratic in X=x^5,Y=y^5. Over C this quadratic factors into two linear factors, counted with multiplicity. Thus its zero divisor is the sum of two degree-five divisors, each of which is either five times one of the two stabilizer-fixed points or a reduced free C-orbit of five points. The two degree-five divisors may coincide.

In particular, outside its two fixed points, this scalar has at most two C-orbits of zeros, and every zero there has multiplicity one or two. At its fixed points the possible positive multiplicities are five and ten. These multiplicities concern one scalar section, not the radical dimension of the full obstruction at the same point.

## 4. A restriction on the middle Betti number on Omega

Assume the paired scalars are not identically zero. By transitivity on inverse pairs, all twelve are nonzero. Their total zero divisor

D = sum over inverse pairs {chi,chi^{-1}} of div(a_chi)

has degree 120 and is G-invariant. Thus its multiplicity n at each of the twelve points of Omega is the same, and 12n<=120 gives n<=10.

Fix p in Omega, with projective stabilizer C of order five. On the twelve inverse-character pairs, C has exactly two fixed pairs and two free orbits of size five: its fixed line in F5^2 has four nonzero vectors, giving two inverse pairs, and the other twenty vectors give two free orbits on inverse pairs. At p, the vanishing subset of pair scalars is C-invariant. Write s for the number of vanishing fixed pairs and t for the number of vanishing free orbits. Then

m = s+5t, with 0<=s<=2 and 0<=t<=2,

is the number of vanishing pair blocks. For each fixed pair, p is one of the two parameter fixed points of that pair's stabilizer. Section 2 shows that its vanishing multiplicity is at least five. A vanishing free orbit consists of five scalars, each contributing multiplicity at least one. Hence

5(s+t)<=n<=10.

Therefore s+t<=2 and

m belongs to {0,1,2,5,6,10}.

PR531 gives trivial-block corank exactly one at p. Each vanishing inverse-pair block contributes corank two. It follows that, in the paired-nonzero branch (generic b=0),

b(p) belongs to {1,3,5,11,13,21} for p in Omega.

The value is constant on Omega by equivariance. In the paired-zero branch all paired scalars vanish identically, so b is exactly 24 outside Omega and 25 on Omega. Consequently, without deciding the branch, the actual common value on Omega belongs to {1,3,5,11,13,21,25}. In particular 7,9,15,17,19 and23 are excluded there, not merely their parity determined.

## 5. Orbit-degree refinement

Still in the paired-nonzero branch, n is in fact in {0,5,10}. Indeed point stabilizers of A5 on P1 are cyclic, so their possible orders are 1,2,3,5. Apart from Omega the orbit sizes are therefore 60,30,20. The invariant divisor D-n Omega is supported away from Omega, so its degree 120-12n is divisible by ten. Hence five divides n, proving the claim.

If b on Omega is 5,13 or21, the corresponding values of m are 2,6 or10, respectively. Each forces s+t=2, hence n>=10. Consequently n=10 and D=10 Omega. In any of these three cases no paired scalar has a zero outside Omega; by the nonvanishing of the trivial block away from Omega, b is zero at every point outside Omega, not merely generically.

If b on Omega is1, no paired scalar vanishes there and n=0. The remaining values3 or11 allow n=5 or10 and are not further distinguished here.

This restricts the nontrivial-channel exceptional geometry beyond the ordinary degree-ten assertion. It does not establish that the twelve paired scalars are nonzero: the generic alternatives b=0 and b=24 remain unresolved. The conclusion is conditional on the pinned structural inputs, is authored mathematics awaiting independent review, and is not a formal proof-assistant check. It makes no claim about the original fixed source pair, higher-order lifting, or algebraicity.
