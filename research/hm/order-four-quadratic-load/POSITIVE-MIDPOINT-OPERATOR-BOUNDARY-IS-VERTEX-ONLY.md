# The positive midpoint operator boundary is determined by the vertex component

## Result

Let delta:H0(M(4))_+ -> H1(B_Q(4))_+=P4 be the actual midpoint operator boundary, with M=omega_(2Z)(1). Its restriction to the conic-supported summand is zero. Therefore delta, and hence the unquotiented fixed-probe third value, is determined entirely by the vertex component of the ACTUAL corrected operator defect.

This does not identify nonzero local residues with nonzero global boundaries. The vertex class must still be taken modulo restrictions of global H0(G(4))_+ sections and then modulo the actual second-symbol image.

## 1. The positive conic part of M(4)

The conic C and vertex components of Z are disjoint. Their ordinary square thickenings are also disjoint, so M and its cohomology split into these two support summands. The intrinsic exact filtration is

    0 -> O_Z -> M -> G|Z -> 0,

where the first arrow is the class of N and corresponds to sigma/2 under the fixed tangent convention tau(sigma)=2N.

Because sigma is regular, G|C is the normal bundle of C in the smooth weighted stack. The two negative coordinate directions give

    G|C=N_(C/X)=W tensor O_C(2),

where O_C(2) here is the ordinary degree-two line on C=P(Wprime), equal to physical O_X(1)|C. The central involution fixes C, acts negatively on W, and acts positively on the physical line. Thus G|C is odd, whereas O_C is even. Taking the even part of the filtration yields

    M(4)|_(2C),+ = O_C(8).                          (1)

This uses the full nonreduced filtration, not an assertion that M is supported only on reduced C.

## 2. Every conic section is a global image with zero vertex component

Every section of O_C(8) lifts to a pure-positive ambient quartic rho. Indeed, restriction is the onto Cartan multiplication

    Sym^4(V) -> Sym^8(Wprime),   V=Sym²(Wprime).

Equivalently every binary monomial of degree8 is a product of four of u²,uv,v².

On the vertex component, rho has cover degree8. The ACTUAL homogeneous regular (3,5) complete-intersection algebra has socle degree3+5-2=6. Therefore rho restricts to zero on the entire vertex zero scheme Z_v, not merely on its support. Flatness of the established homogeneous family ensures this fiberwise graded vanishing is a sheaf vanishing.

The global section rho sigma/2 of G(4) maps to rho times the class of N in M(4). On the conic this is the prescribed section of (1); on the vertex it is zero, since the class-of-N submodule is O_Z and rho|Z_v=0. Hence

    H0(M(4)|_(2C))_+ is contained in im H0(G(4))_+.  (2)

Exactness of the midpoint commutator sequence gives delta=0 on (2).

## 3. The remaining vertex quotient is still global

Let r_v be the vertex component of the actual defect. Then

    Psi(a,h,t(a))=delta(r_v),

with the fixed normalization and boundary convention from the midpoint comparison. Moreover delta(r_v)=0 exactly when r_v is the vertex restriction of a global positive section of G(4). For the reverse implication, any unwanted conic component of such a global image can be removed using Section2.

Thus the corrected Hessian vertex-symbol calculation is sufficient for the support of the remaining computation. Neither a nonzero representative in I/(f²,g²), nor a nonzero degree-eight polynomial on one chart, proves that its image under this global quotient is nonzero.

## Reproduction and dependencies

Run verify_positive_operator_conic_boundary.py. It checks the actual complete-intersection Hilbert degree bound symbolically and the universal quartic-to-octic monomial surjection. The geometric inputs are the published regular Serre presentation, homogeneous vertex (3,5) algebra, the intrinsic M filtration, and the exact midpoint commutator boundary. No actual HM coefficient or rank evaluation is used.
