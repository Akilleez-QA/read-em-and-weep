# Independent mathematical review

**Verdict: PASS for the structural exclusion in Sections 1–5 and the pinned-input corollary in Section 6.** No mathematical gap was found. The argument proves that an integral degree-15 surface in projective four-space, invariant under the stated linear Heisenberg action, has no equations of degrees zero through four. The actual-primary identification and invariance remain the explicitly declared imported inputs. Section 6 then correctly proves ambient restriction isomorphisms in degrees zero through four using the independently reviewed lower-conductor theorem at immutable commit 80f302ddd7e0dd19f1c54b725f56e5f81bb47c69, research/hm/lower-conductor-ranks/PROOF.md. I read the matching local proof and its independent review; the cited lower-conductor theorem is treated as an independently reviewed input. This review does not rederive that upstream theorem.

Reviewed on 2026-10-21. This review checked the supplied proof directly, without selected HM/source coefficients, numerical rank evaluations, large computation, or public writes.

Final PROOF.md SHA-256: f6eeddf30045b3be2af85e8727d56275d139a731680f2986ffd6aa60e08ed794. The only post-review change was the status line recording this PASS.

## Checks of the potentially delicate steps

1. **Heisenberg divisibility.** On degree d, the commutator acts by epsilon^d. For d=1,2,3,4 this has exact order five. Diagonalizing tau, sigma permutes its eigenspaces in five-cycles, with equal dimensions within each cycle. Thus every invariant subspace, in particular I_d, has dimension divisible by five. No irreducibility classification or choice of representation-dual convention is needed.

2. **Minimal equations and complete intersection.** Primality of I makes every nonzero equation in its least positive degree irreducible. Two independent such equations are nonassociate, hence coprime. In the polynomial UFD, (f) is prime and g is regular modulo f, so K=(f,g) is indeed a regular sequence of height two and degree d^2. The height-two prime I is a minimal prime over K. Its multiplicity contribution is at least 15, excluding d<=3.

3. **Unmixedness is strong enough at the irrelevant ideal too.** A quotient of the regular ring R by this regular sequence has no embedded associated primes. One direct justification, avoiding conventions concerning the word “unmixed,” is to localize at an associated prime Q: the localized quotient has depth zero and projective dimension at most two, so Auslander–Buchsbaum gives ht(Q)<=2. Every prime containing K has height at least two. Consequently all associated primes have height exactly two, including any candidate irrelevant-ideal component being ruled out.

4. **Degree 16 implies the exact reduced union, not merely a cycle.** The associativity formula gives 16=15m plus the positive contributions of the other minimal primes. Hence m=1, and there is exactly one additional minimal prime P, of degree one and generic length one. For either minimal prime Q, local length one means K_Q=Q R_Q. An isolated Q-primary component is the contraction of its localization, so that primary component is Q itself. There are no other components by the preceding unmixedness check. Thus K=I intersect P as homogeneous ideals, not only after sheafification or reduction.

5. **The degree-one prime is linear.** Linear Noether normalization exists because A=R/P is standard graded over the infinite field C. For a finite inclusion B=C[y0,y1,y2] into the domain A with the y_i of degree one, comparison of leading Hilbert coefficients gives

   degree(A)=rank_B(A)=[Frac(A):Frac(B)].

   This equals one. Therefore B and A have the same fraction field; since A is integral over the integrally closed ring B, A=B. It follows that dim A_1=3, the kernel in R_1 has dimension two, and those two independent linear forms generate P. This last generation statement also follows by factoring R onto the polynomial algebra Sym(A_1)=A. No normality of A is assumed.

6. **Both colon identities are valid.** Distinct primes I and P of equal height are incomparable. Taking an element of I outside P proves P:I=P, and taking an element of P outside I proves I:P=I. Applying colons to K=I intersect P gives K:I=P and K:P=I. No local Cohen–Macaulay hypothesis on S has entered.

7. **The determinant lies in I.** The identities x Delta=d f-b g and y Delta=a g-c f are correct. There are no linear equations in I, so x is not in I. Primality then gives Delta in I from x Delta in I. Thus K is contained in L=(f,g,Delta), and L is contained in I. The resulting height bounds force ht(L)=grade(L)=2.

8. **Hilbert–Burch signs, grade, and shifts.** For the displayed matrix with rows (a,b), (c,d), and (-y,x), the signed maximal minors, in order, are (g,-f,Delta). Their product with either column is zero. The ideal of maximal minors is exactly L, whose grade is already verified to be two; this is the sufficient converse Hilbert–Burch hypothesis. The source is R(-7)^2 because the first two target summands are R(-4) and the corresponding entries are cubics, while the last target summand is R(-6) and its entries are linear. The displayed resolution is therefore exact with precisely the stated twists. It is also minimal, because every matrix entry and every generator has positive degree. No genericity or initial Cohen–Macaulay property of S is used. The cited Bruns–Vetter appendix is an appropriate standard reference for this theorem; its indexed contents identify Appendix F at printed page 217: https://www.home.uni-osnabrueck.de/wbruns/brunsw/detrings.pdf . Hilbert–Burch is used as a standard theorem; this review does not reprove it.

9. **The degree computation and equality L=I are sound.** The numerator N(t)=1-2t^4-t^6+2t^7 has N(1)=N'(1)=0 and N''(1)=-24-30+84=30, giving degree 15. The resolution gives projective dimension at most two. The same localized Auslander–Buchsbaum argument as in item 3 shows that all associated primes of R/L have height two. Since I is one such minimal prime and already has degree 15, multiplicity associativity leaves no other minimal prime and forces local length one at I. Thus L has only the I-primary component, whose localization and contraction identify it with I. In particular, equality of degrees alone is not being misused: it is combined with the essential verified unmixedness.

10. **The contradiction follows without the node input.** In degree four the resolution, or simply the generators of L=I, gives I_4=span_C(f,g), of dimension exactly two. This contradicts the divisibility by five from item 1. The degree-six determinant cannot contribute in degree four. This proves the claimed exclusion, with degree zero excluded because S is nonempty.

## Optional node contradiction

Conditional on the quoted completed-local-ring identification, the second contradiction is also correct. The ring is the fiber product of C[[u1,u2]] and C[[v1,v2]] over C. The difference-of-constant-terms map gives the stated exact sequence. The middle module has depth two over the fiber-product local ring and the final residue-field module has depth zero. The depth lemma therefore gives depth one for the fiber product; its dimension is two. Completion preserves depth and dimension. Hence it cannot be a local ring of the Cohen–Macaulay surface forced by L=I. The node identification itself was not independently rederived, and is unnecessary for the main result.

## Boundaries and nonblocking editorial points

- The named PR inputs are treated as assumptions here; this review does not replace review of the actual scheme identification or group-invariance pins.
- Section 6 correctly combines, rather than confuses, injectivity with equality of dimensions. The lower-conductor theorem at the immutable pin above gives h0(O_S(d))=(1,5,15,35,70,126) for d=0,...,5. In degrees zero through four these equal dim H0(P4,O(d))=binomial(d+4,4). The newly proved vanishing of I_d makes the restriction injective and therefore an isomorphism; the ideal-sheaf exact sequence then gives H1(P4,I_S(d))=0. The previously missing publication pin has been supplied. There is no remaining publication-dependency gap for this corollary.
- The degree-five limitation is correct: the center has trivial weight then, so the five-divisibility argument does not apply. Equal dimensions alone imply neither injectivity nor surjectivity.
- For maximal self-containment, the one displayed rank/degree identity in item 5 and the associated-prime justification in items 3 and 9 could be inserted into the proof, but both are standard valid steps, not gaps.

**Conclusion:** the new structural exclusion is rigorous under its declared degree, integrality, and Heisenberg-invariance inputs. It does not assume the Cohen–Macaulay property that it eventually derives in the impossible quartic case, and it closes the low-degree equation/injectivity dependency without source-membership calculations.
