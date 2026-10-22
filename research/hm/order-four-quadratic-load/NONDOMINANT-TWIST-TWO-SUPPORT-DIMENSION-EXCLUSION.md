# Generic exclusion of the nondominant twist-two eigenquotient alternative

## Conditional interface being closed

Use the established reduction for a primitive twist-two obstruction on a general smooth quadric Q transverse to C. In the remaining nondominant eigenquotient case, there is a nonzero d∈Sym²U defining a quadric in P(U*), and a nonzero cubic section g∈H0O_Q(3), such that the actual global product section

S_d∈H0(P4,Sym²(F(3)))=H0(P4,B(5))

restricts to gψ on Q. The pinned preceding argument additionally says g vanishes at45 of the fifty marked points Z=C∩Q (indeed to order at least two) and is nonzero at the other five. Only vanishing at45 is used here. This note does not reprove that interface, and its conclusion is conditional on it.

We prove these configurations occur only over a subset of dimension at most10 in the14-dimensional space of quadrics. Thus they cannot support a generic-Q obstruction.

## 1. A nonzero global product has no divisorial zero

The exterior-symmetric evaluation resolution gives H0(B(4))=0. Explicitly, twist by -1: its U⊗F(2) term has no sections, intermediate line-bundle cohomology vanishes, and its evaluation-cokernel term is ell²(-1), with no sections on C. Thus H0(B(t))=0 for every t≤4, by multiplication with a nonzero homogeneous polynomial to twist four.

If a nonzero S_d had a divisorial zero of degree a≥1 on P4, division by its equation would give a nonzero section of B(5-a), contradiction. Hence Z(S_d) has dimension at most two.

The nonzero d does give a nonzero S_d: in twist zero the same resolution identifies H0(Sym²E) with (U⊗U)/Λ²U=Sym²U. Here H0ell²=0 and the necessary intermediate line-bundle groups vanish. Thus the product map has no kernel. In particular the zero scheme has only finitely many surface components for each fixed [d]∈P9.

## 2. A hyperplane contains at most41 of the fifty marked points

No hyperplane can contain17 of the25 lines C. Otherwise at most8 lines remain, and cubic polynomials through these remaining lines form a nonzero vector space: h0O_P4(3)=35, while each line imposes at most4 linear conditions, so the dimension is at least35-32>0. The hyperplane equation times such a cubic would be a nonzero quartic vanishing on all C, contradicting I_C(4)=0.

Therefore a hyperplane contains at most16 whole component lines. Each such line contributes its two marked points; each other line contributes at most one marked point to the hyperplane. Consequently every hyperplane contains at most 2·16+(25-16)=41 points of Z.

Let T be the reduced support of the cubic divisor (g=0) on Q. Since Q is smooth and Pic(Q)=Z·H, write [T]=rH. Here r is an integer with1≤r≤3. If r=1, T is a hyperplane section, because every section of O_Q(1) is an ambient linear form. It could not contain the45 marked zeros of g. Thus r≥2 and deg T=2r is4 or6.

This handles nonreduced g: in particular a triple hyperplane section is excluded, without assuming that the cubic divisor is reduced or irreducible.

## 3. Fixed support permits at most a pencil of quadrics

T is a reduced union of surface components of Z(S_d): it is a pure two-dimensional closed subset there and the latter has dimension at most two. Hence for a fixed d there are only finitely many possible supports T.

For any one such T which lies on a smooth quadric Q as above, restrict quadrics containing T to Q. The kernel is the one-dimensional span of q. The image lies in

H0(Q,I_{T,Q}(2))=H0(Q,O_Q((2-r)H)).

Indeed T is a reduced effective divisor on the smooth Q. For r=2 this space has dimension one, while for r=3 it is zero. Thus h0(P4,I_T(2))≤2, so the space of quadrics containing this fixed support has projective dimension at most one.

## 4. Parameter dimension

The parameter [d] lies in P(Sym²U)=P9. Choices of a reduced union T of its surface components of degree4 or6 form a finite-fiber algebraic correspondence over that parameter space. One may formalize it using the projective Chow spaces of degree4 and6 effective surface cycles, retaining reduced cycles supported in the universal zero scheme of S_d. For each fixed d only finitely many such cycles exist. Therefore the correspondence has dimension at most9.

For each retained T, its space of possible Q has dimension at most one by §3. The total incidence of these triples therefore has dimension at most10. Its image in P(H0O_P4(2))=P14 is contained in a proper closed subset after taking closure.

Consequently the nondominant twist-two alternative described in the interface cannot occur for general Q.

## Scope and checks

The proof uses the actual global product S_d, its absence of divisorial zeros, the45 marked zeros, and ordinary parameter dimension. It does NOT infer dimensions of exceptional fibers from generic finiteness of the Plücker map. It does NOT require g reduced, T irreducible, symmetry of Q or ψ, or an equivariant choice of g. It does not exclude the dominant twist-two eigenquotient alternative.

Inputs: actual exterior-symmetric evaluation resolution and I_C4=0; the nondominant interface is pinned at f716f3b66c93d12217f953850150a11be1dccc4e and its high-image-degree exclusions at a2bfa736a2ff29d4186e70dc3e1ab4b8e3f79621 in PR543. No selected evaluations, matrices, ranks, or external writes were used.
