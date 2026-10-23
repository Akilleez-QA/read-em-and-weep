# The actual seventh-neighborhood correction absorbs every secondary torsion defect

Work over C with the actual normalized HM bundle F, B=End0 F, positive fixed plane R, and the negative hyperplane family over T=P(W*). All thickened neighborhoods below are ordinary Cartier neighborhoods mR inside a hyperplane H, not the ambient codimension-two thickening of R in P4. All representations and line-bundle twists retain their G=SL2(F5) linearizations.

## 1. Exact input and notation

INPUTS.json authenticates four immutable originals in Akilleez-QA/read-em-and-weep:

- FIFTH, PR983: the actual even fifth-neighborhood derived cohomology is [K --beta--> U] in degrees0,1, with U=(A+V+P+D) O(4), coker beta equal to its actual R1, and the A target row identically zero.
- TORSION, PR1024: K=T6 O(-1) plus A O(-2), its actual square subbundle is L=A O(-6), and Q=K/L=P O(2) plus W O(-1). The actual beta factors through b:Q->U. Its cokernel torsion is either zero or twelve simple factors, exactly on the reduced orbit Omega.
- LAYERS, PR974: the normal degree-k layer of B(t) is B_R(t-k) O(k), of inversion sign (-1)^k. The plane groups used here are H1(B_R(-3))=V+P+D, H1(B_R(-5))=0, H2(B_R(-5))=A, and H0(B_R(t))=0 for t<=1. The first identity also follows from its stated H1(B_R)=V+P+D by Serre duality. It proves H0(mR,B_H(2))=0 for m>=3.
- DUALITY, PR986: even H0(mR,B_H(3)) stabilizes after7R to the actual global square space; its bundle is L and its restriction is the actual square inclusion. It also proves the actual rank12 ninth-neighborhood map Theta, with ker Theta of rank18 and degree42, and the canonical identity R1(9R,B_H(3))_+=(ker Theta)* O(8).

Write E_m for the actual inversion-even pushforward of B_H(3)|mR to R times T under the finite normal projection, and q:R times T->T. Define

    C5=R1q_*E_5=coker beta,
    J=(V+P+D) O(6),
    H7=R1q_*E_7.

Thus U has rank15 degree60; J has rank12 degree72. The letters V and J are not interchangeable: V is an irreducible representation, J is this rank12 bundle.

## 2. Main result: an actual completed presentation

There exists a G-equivariant lift gamma:K->J, retaining the full actual sixth-normal correction, for which

    Rq_*E_7 = [K --(beta,gamma)--> U plus J]         (1)

in degrees0,1. Its choice is immaterial up to gamma -> gamma+h beta, with h:U->J. The map kills precisely the actual squares L and therefore induces a fiberwise injective bundle map

    Q -> U plus J.                                  (2)

Consequently H7 is locally free of rank21 and degree126. This is not an arbitrary extension of the secondary matrix: (1) presents the actual seventh neighborhood.

Let N=ker(b:Q->U), and let r be the generic rank of b. The restriction of gamma descends to a CANONICAL fiberwise injection

    delta:N -> J.

It does not depend on the choice of lift in (1). Its cokernel M is a vector bundle of rank6+r. There is an actual canonical exact sequence

    0 -> M -> H7 -> C5 -> 0.                         (3)

Let tau be the torsion subsheaf of C5. The saturation M^sat of M in H7 satisfies

    0 -> M -> M^sat -> tau -> 0,
    0 -> M^sat -> H7 -> C5/tau -> 0.                 (4)

If tau is nonzero, it has length12 by TORSION. Sequence (4) is necessarily nontrivial at every point of Omega: locally M->M^sat has Smith form diag(t,1,...,1), where t is any local uniformizer. Thus the actual later correction absorbs every secondary torsion factor in a forced elementary modification. It does not rule out the torsion alternative.

## 3. Construction from the actual thickening

Passing from5R to7R in the positive eigenspace adds exactly the even degree-six layer:

    0 -> B_R(-3) O(6) -> E_7 -> E_5 -> 0.           (5)

The degree-five layer is odd and contributes nothing here. The added layer has H0=0 and H2=H0(B_R)*=0, and its H1 is J. Applying Rq_* to (5) gives the triangle

    J[-1] -> Rq_*E_7 -> [K->U] -> J.                (6)

No associated-graded replacement of the actual bundle extension is used. In the derived category the last arrow is represented by a map K->J because

    Ext1_G(U,J)=0.

Indeed every line-bundle difference in this Ext group is6-4=2, with H1(O(2))=0. The exact Hom sequence for the two-term complex shows that all such representatives differ by h beta, h in Hom_G(U,J). Taking its homotopy fiber gives (1), up to a harmless sign convention for gamma. Finite-group invariants are exact in characteristic zero, so the construction and the lift can be taken equivariantly. This only splits the displayed cohomological presentation, not the geometric extension (5).

## 4. Uniform global squares force a subbundle, not merely a generic kernel

For every hyperplane, DUALITY proves that even sections stabilize after7R: subsequent even layers have degree k>=8 and H0=H1 of B_R(3-k) both vanish. Comparison with sufficiently large thickenings identifies the stable sections with global sections, which are exactly the three squares. This argument uses eventual Serre vanishing, not an unproved global-to-finite isomorphism at a prescribed negative twist.

The family E_7 is a vector bundle on R times T with its finite filtration, so derived base change applies. Its fiber H0 is always the actual three-dimensional square space. Its H2 is zero: this is true for E_5 by FIFTH and for the added layer in (5). Presentation (1) is therefore a two-term complex of bundles computing every fiber, with a kernel of dimension3 at every fiber. The map has constant rank6. The actual global square bundle L maps into that kernel and restricts fiberwise to the full kernel. Hence the kernel bundle is exactly L, with its actual inclusion in K, and (2) is fiberwise injective. Its cokernel is H7 and is locally free. Since rank Q=6 and deg Q=6, (2) gives

    rank H7=27-6=21,
    deg H7=(60+72)-6=126.

This establishes every base-change assertion used below before appealing to the ordinary long exact sequence.

## 5. The canonical correction and torsion absorption

N is a subbundle of Q: the image of a bundle map on the smooth curve T is torsion-free and hence locally free, so Q/N is locally free. Restricting (2) to N sets its U component to zero. The remaining component delta:N->J is consequently fiberwise injective. Its lift ambiguity h b vanishes on N, proving that delta and its cokernel M are canonical actual objects. The actual boundary H0(E_5)->J factors through H0(E_5)/L=N and is precisely delta.

The cohomology sequence of (5), or the quotient diagram for (2), gives (3). The bundle H7 is torsion-free, but C5 is a QUOTIENT of it; there is no reason for that quotient to be torsion-free. The inverse image of tau under H7->C5 is precisely M^sat. Its quotient is C5/tau, a vector bundle, so M^sat is a subbundle of H7 and has the same rank as M. This proves (4).

At a point where tau is the length-one residue-field module, M^sat is free and its quotient by M has length1. The elementary-divisor theorem over the local discrete valuation ring gives diag(t,1,...,1). A split extension there would contain a nonzero torsion direct summand in the free module M^sat, impossible. Thus each local extension is forced nonzero. Globally, when tau is present,

    deg M^sat=deg M+12.

This is an actual constraint on the subsequent extension class. It cannot be replaced by a claim that tau injects into the torsion-free bundle H7 or that tau must vanish.

## 6. What happens to the extra fifth-neighborhood fiber sections

For a point x of T, write k(x) for its residue field. Derived base change of [K->U] gives the canonical exact sequence

    0 -> (ker beta) tensor k(x)
      -> H0(E_5|x)
      -> Tor1(C5,k(x)) -> 0.                        (7)

These extra sections are not fibers of the kernel sheaf. Quotienting the fiber boundary H0(E_5|x)->J tensor k(x) by delta(N tensor k(x)) identifies the induced map on the last term of (7) with the connecting injection obtained by tensoring (3):

    Tor1(C5,k(x)) -> M tensor k(x).                  (8)

To see this directly, tensor the diagram (2) and its U projection. The fiber kernel of b maps under its J component into J; its subspace N tensor k(x) maps to delta(N tensor k(x)). The quotient of the former by the latter is Tor1(C5,k(x)), and the combined fiber injection (2) makes its map to M tensor k(x) injective. This is also the snake-lemma description of (8).

Consequently, if secondary torsion is present, its one-dimensional extra section at every orbit point is killed by the actual sixth-normal boundary. If r is the generic secondary rank, that fiber boundary has rank6-r off Omega and7-r on Omega. The sheaf map delta itself has constant rank6-r; there is no contradiction, since its domain omits exactly the Tor contribution at the exceptional fibers. Without torsion the fiber boundary has rank6-r everywhere.

## 7. A compatible ninth-neighborhood quotient

The next positive step from7R to9R adds B_R(-5) O(8), whose only nonzero cohomology is H2=A O(8). Moreover R2q_*E_9=0. For the latter assertion apply full-sheaf relative duality on the Cartier ninth neighborhood before taking parity, exactly as in DUALITY. Its canonical bundle is B-independent and equals p*O(5) O_T(-8); hence H2(B_H(3)|9R)_+ is dual to H0(B_H(2)|9R)_+, with the corresponding base twist. The latter vanishes by LAYERS. There is no parity swap because the ninth-neighborhood canonical factor has even inversion character.

The actual cohomology sequence therefore gives a surjection and a canonical kernel:

    0 -> (ker Theta)* O(8) -> H7 -> A O(8) -> 0.    (9)

The kernel has rank18 and degree18*8-42=102, consistent with126-24=102. Equation (9) is a further actual quotient constraint on the bundle in (3), not a claim that either extension splits. It links the new secondary repair directly to the already authenticated ninth-neighborhood gate with all twists retained.

## 8. Contribution and limitations

The new conclusion is an actual finite-neighborhood completion of the secondary map: a fiberwise embedding Q into a rank27 target, a canonical order-six obstruction on its kernel, and a forced nontrivial elementary extension absorbing any of its twelve simple torsion factors. It explains why the universal torsion alternative is compatible with uniform global square exhaustion and identifies precisely how the exceptional extra sections disappear. The subsequent ninth-neighborhood quotient is retained canonically.

Nothing selects the actual secondary coefficients, its generic rank, or whether tau vanishes. No extension in (3), (4), (5) or (9) is declared split without proof. No global H1 identification, global odd-quadric conclusion, top sigma, vertex scalar or source/catalogue exclusion follows. No selected actual HM/source coefficient, point, parameter, derivative, jet, matrix, instance rank or large scan is used.
