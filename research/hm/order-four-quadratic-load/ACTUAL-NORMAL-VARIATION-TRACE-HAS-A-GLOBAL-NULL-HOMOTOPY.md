# The actual normal-variation trace has a global null-homotopy

## Result and exact limitation

For the corrected operator with symbol H D, H=k a h, let

    b1=[O,eta]+H rho eta,

be its actual first-normal variation, in the physical normal-frame convention. Retain BOTH invariant components of the square shadow of eta. Nevertheless its trace is exactly null-homotopic by a global multiple of the actual scalar inverse u:

    tr(N b1)=0 in H1(I_Z²(4)).                            (1)

This conclusion does not require determining the unknown nilpotent component of tr(N eta). It gives a unique lift of b1 to the actual H1(G) image Cplus=P4+D5. Modulo J=D5 xi_Q its remaining value is an explicit secondary residue in P4, described in Section5. The scalar null-homotopy alone does not compute that secondary residue.

No actual coefficient values, actual-instance matrices/ranks, or source experiments are used. The proof applies in particular to the uniform square input a=t²,h=X²Y², with every symbolic parameter unassigned. All existing artifacts remain unchanged.

## 1. The normal trace is NOT just the component idempotent

Use the actual trace/square sequence on the weighted stack,

    0 -> G(-4) --tau--> B_Q(-2) --q=tr(N·)--> I_Z² -> 0,     (2)

with the fixed Serre marking understood. NORMAL-QUADRATIC-BRACKET-COMPONENT-SHADOW-GATE.md proves that the invariant H1 of its right term has dimension TWO. Under

    H1(I_Z²)^G = H0(O_(2Z))^G / C,

one basis consists of the component idempotent e_v and a nonzero invariant nilpotent n8 in the top positive cover-degree-eight vertex layer. Thus

    q(eta)=delta(alpha e_v+beta n8),                         (3)

for actual scalars alpha,beta. There is no basis for setting beta=0.

The coefficient alpha is NONZERO, and its exact normalization can be stated without guessing a numerical scalar. Evaluation and wedge give a commuting diagram

    B_Q(-2) --eta mapsto eta sigma--> G(-2) --sigma wedge--> I_Z,
    B_Q(-2) ----------- -q -----------------------------> I_Z² -> I_Z.

Indeed sigma wedge(eta sigma)=-tr(N eta) identically. The actual map on invariant H1 from B_Q(-2) to G(-2) is an isomorphism by FIRST-NORMAL-ADJOINT-DEFECT-IS-INVARIANT-ACYCLIC.md. The Serre sequence identifies H1(G(-2))^G with the component-difference line H0(O_Z)^G/C. Since n8 restricts to zero on Z, this forces alpha nonzero.

More precisely, let kappa_eta be defined by

    [eta sigma]=kappa_eta delta_G(e_v)

in H1(G(-2))^G, with the chosen actual eta, sigma and Cech boundary convention. Then alpha=-kappa_eta. If eta is normalized by [eta,N]=xi_Q, this is equivalently the comparison of xi_Q with tau(delta_G(e_v)). The fixed tangent convention is [eta,N]=tau(eta sigma). This retains the actual normal-coordinate/probe scalar; it does not assign alpha=1 or beta=0.

The full block torus on the zero scheme does not remove beta automatically. The global Serre extension has conic and vertex residue characters mu^(-2) and mu², respectively. Only their order-four coincidence supplies the global cone-bundle symmetry used here. A local homogeneous vertex residue normalization is not a global full-torus marking of G.

## 2. The exact operator diagram

Write the trace-free cone connection as Aconn. In an actual physical equation frame,

    H D N+[Aconn,N]=Lambda N,
    Dqcone=rho qcone,
    Lambda=H rho-u.

The last equality is the actual scalar-inverse theorem with its determinant connection. Define the induced first-order maps

    L(E)=H D E+[Aconn,E]+H rho E,
    T(f)=H D f+u f.

A direct trace identity gives the EXACT commuting relation

    q L = T q.                                            (4)

In particular, this is H D+u, not H D-Lambda: the normal-equation term H rho cannot be omitted.

There is also a left lift of (4). With tau(v)=sigma v^tJ+v sigma^tJ and
H D sigma+Aconn sigma=(Lambda/2)sigma, set locally

    S(v)=H D v+Aconn v+(Lambda/2+H rho)v.

Then L tau=tau S. Consequently (2) maps to the actual twist-four sequence

    0 -> G --tau--> B_Q(2) --q--> I_Z²(4) -> 0.             (5)

The displayed connection terms are interpreted in the same transported physical frames; these identities define the global operator diagram, rather than asserting that its individual matrix entries are globally scalar functions.

## 3. Why T kills the additional invariant nilpotent

The vertex ideal is the ACTUAL homogeneous regular pair of degrees3 and5. Its ordinary square has Hilbert series

    (1-t^6-t^8-t^10+t^11+t^13)/(1-t)^2.

Its degree0 through degree11 dimensions are

    1,2,3,4,5,6,6,6,5,4,2,1,

and every degree at least12 is zero. This follows from the regular-pair square resolution, not from reduced support or an actual-instance rank test.

Both H and u have positive cover degree4. The actual D preserves positive cover degree, including its Euler and coefficient-line terms. Thus T raises that degree by four. The extra invariant n8 lies in the actual top positive degree-eight filtration, so

    T(n8)=0 in O_(2Z)(4).                                (6)

Filtration suffices: the result lies in the zero degree-at-least12 layer. The intervening odd layers do not invalidate (6).

The symbol H D preserves I_Z, hence its ordinary square, so it descends to the quotient. A derivation kills every idempotent in characteristic zero: D_H(e²)=2e D_H(e) and 2e-1 is invertible. Therefore H D(e_v)=0 and

    T(e_v)=u e_v.

## 4. The actual global scalar gives the null-homotopy

The scalar u is a GLOBAL section of D5_positive tensor A_negative inside H0(O_Q(4)). Every summand has negative-coordinate degree TWO. The conic ideal is generated by the negative coordinates, so

    u belongs to I_C²(4).

This is vanishing on the DOUBLE conic, not merely on its reduced support. Since 2Z is the disjoint union of its vertex and conic components, it follows that

    u e_v = u|_(2Z).

Combining this with (3),(4),(6) yields

    q(b1)=delta T(alpha e_v+beta n8)
          =delta(alpha u|_(2Z))=0,

where the null-homotopy is the actual global section alpha u. This proves (1) with both invariant shadows retained.

For the particular square input, u is the nonzero tensor already pinned in ACTUAL-MIDPOINT-ABSOLUTE-SECTION-FOR-THE-FOURTH-SQUARE-INPUT.md. Its nonzeroness does not imply nonzeroness of the remaining variation residue.

## 5. The precise remaining secondary residue

The actual H0(I_Z(4))_+ is zero, so H0(I_Z²(4))_+=0. Sequence(5) therefore makes

    H1(G)_+ -> H1(B_Q(2))_+

injective. The Serre sequence and the actual vertex/conic residue calculation identify its image, with the extra Serre marking, as Cplus=P4+D5. Consequently (1) gives a UNIQUE class gamma with tau(gamma)=b1.

Here is the exact Cech construction, retaining all data. Choose local scalar lifts t_i of s=alpha e_v+beta n8, and representative eta_ij, compatibly so q(eta)=delta t. Because T(s)=alpha u|_(2Z),

    v_i=T(t_i)-alpha u

belongs to I_Z²(4). Choose local adjoint lifts K_i with q(K_i)=v_i. Then

    L(eta)_ij-(delta K)_ij=tau(gamma_ij)                   (7)

defines a G cocycle. Its class is the unique gamma above. Altering K_i by a tangent zero-cochain changes gamma by a coboundary. Altering compatible representatives produces the same class. Thus there is no new free choice in this construction, but (7) still depends on the ACTUAL adjoint lifts and operator action, not merely on the scalar identity T(s)=alpha u.

Next use 0->O_Q->G->I_Z(2)->0. The class of sigma wedge gamma corresponds to a section of O_Z(2) modulo global quadratics. Subtracting those global sections removes its reduced-vertex A component and conic D5 component uniquely. What remains is the actual pure-vertex degree-four residue

    r_var in H0(V O_L(2))=V tensor A=P4+D5.

The already-proved actual multiplication J=D5 xi_Q is precisely the image Q(D5) in this residue space. Hence the remaining endpoint datum is exactly

    [r_var] in (V tensor A)/Q(D5)=P4.                    (8)

Formula(7), followed by the Serre residue and (8), is a precise secondary connecting diagram for the missing variation. The trace null-homotopy alpha u establishes its existence but does NOT calculate it. The relevant target map q on H1 has a nonzero kernel Cplus of dimension9; knowing its zero value cannot distinguish any of those kernel classes. Modulo the actual J, the unresolved class is exactly (8), not an arbitrary larger ambient ambiguity.

This also explains why annihilating the nilpotent square shadow in (6) does not on its own license dropping beta from an adjoint-level computation: killing the quotient under T need not kill the secondary lift in (7). No zero or nonzero value of (8) is asserted.

## Verification

Run python verify_normal_variation_trace_nullhomotopy.py. It checks the universal trace/operator and tangent/operator diagrams, the exact wedge normalization, and the regular-pair square Hilbert series and annihilation degree. The actual scalar and global cohomology identifications are supplied by the stated geometric inputs; no inference from nonzero composite legs or from dimensions alone is made.
