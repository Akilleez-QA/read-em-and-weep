# The invariant conic is a reduced spinor-defect component

## New result

For the actual saturated spinor inclusion S -> E=F_Q0(2) constructed in INVARIANT-CONE-SPINOR-FILTRATION-AND-NILPOTENT.md, the zero scheme is exactly the reduced invariant conic C0 in a neighborhood of C0. The defect T=S(2)/J has a canonical decomposition by disjoint support

    T = i_* O_C0(5) direct-sum T',
    Supp(T') intersect C0 = empty,
    chi(T'(t)) = 7t+21,
    h0(T')=21, H1(T')=0.

Here O_C0(1) denotes degree one on the parametrizing P1, not an ambient hyperplane. The remaining degree-seven defect has not been proved to lie on the negative vertex line L. No actual multiplication coefficient or matrix rank is evaluated.

## 1. Restrictions and the first normal jet

The actual balanced restriction is F_C0=W tensor O_P1(-1), as recorded in RESIDUAL-SMOOTHING-NONVANISHING-AND-EVEN-RANK.md, Section 3, with sources FIXED-PLANE-CONIC-BALANCE-AND-FOURTH-JETS.md and ACTUAL-CONIC-DISCRIMINANT-AND-JUMP-STRATA.md. Since O_Q0(1)|C0=O_P1(2),

    S|C0=O_P1(1), E|C0=W tensor O_P1(3).

The weighted-cone description identifies Q0 minus L with the total space of W tensor O_P1(2), and C0 with its zero section. Consequently

    N_C0/Q0=W tensor O_P1(2).

The central involution fixes C0 pointwise, acts negatively on S|C0 and positively on E|C0 (W and O(3) each have negative central character). Thus the equivariant map S->E vanishes on C0. Its first normal jet belongs to

    H0(C0, Hom(S,E)|C0 tensor N*)
      = W tensor W* tensor H0(O_P1),

whose invariant subspace is one-dimensional by irreducibility of W. Therefore the first jet is a scalar multiple of a fiberwise isomorphism N -> Hom(S,E)|C0. It remains essential to prove that scalar is nonzero, rather than select or evaluate it.

## 2. Formal nonvanishing forces the scalar to be nonzero

Suppose the first jet vanished. Then the map lies in I_C0^2 Hom(S,E) near C0. Its normal order-k term, if all previous terms vanish, is a global section of

    Hom(S,E)|C0 tensor Sym^k N*
       = W tensor Sym^k W* tensor O_P1(2-2k).

For every k>=2 this has no global section, because its line degree is negative. Induction therefore puts the map in every power of I_C0. At any point of C0, Krull intersection for the finite free local Hom module says the intersection of these powers is zero. Thus its germ is zero, and it vanishes on a nonempty open neighborhood. A morphism of torsion-free coherent sheaves on the integral Q0 that vanishes generically is zero globally. This contradicts the already proved nonzero spinor inclusion.

Hence the first normal scalar is nonzero. No assumption of convergence of a formal series is used: vanishing of all successive associated-graded terms and the local Krull intersection theorem suffice.

## 3. Scheme-theoretic transversality and exact defect contribution

On the smooth neighborhood Q0 minus L, S is invertible. The inclusion is a section of the rank-two bundle E tensor S^(-1). Its derivative on the two normal directions along C0 is the isomorphism from Section 1. In a local trivialization, its two components generate I_C0 modulo I_C0^2. Nakayama's lemma gives equality of these two ideals near each conic point. Thus its zero scheme there is exactly C0, reduced, with no additional or embedded component meeting it.

For a regular section of a rank-two bundle, the wedge map gives the quotient in the form

    J = I_C0 tensor det(E) tensor S^(-1)
      = I_C0 tensor S(2)

in this smooth neighborhood only. Thus

    T = S(2)/J = i_* (S(2)|C0) = i_* O_P1(5)

there. This local ordinary-ideal description is valid because C0 is disjoint from L; it makes no assertion of an ideal-times-line-bundle description at the non-Cartier vertex.

The other support of T is closed and disjoint from C0. Coherent sheaves with disjoint support decompose canonically into their support summands, giving T=i_*O_P1(5) direct-sum T'. Its first summand has Hilbert polynomial 2t+6, h0=6 and H1=0. Subtracting from the previously proved chi(T(t))=9t+27, h0(T)=27 and H1(T)=0 proves all claims in the opening statement.

## Scope

The argument determines a reduced degree-two component and an exact degree-seven residual defect, retaining any zero-dimensional contributions and all vertex non-Cartier behavior. Identifying the residual support, or excluding positive noncommuting adjoint sections, remains open. This is a new geometric deduction, not an evaluation of the positive rank33 condition.
