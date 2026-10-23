# Complete cohomology-family observations detect supplied-source membership

Conditional structural continuation of PR894 and PR891, 2026-10-23.
Written mathematics, not Lean certification. No actual HM source, parameter,
point, coefficient, matrix, derivative, or instance rank is selected or
evaluated, and no primitive or physical trace row is constructed.

## Immutable inputs

1. PR894 at `c963b48d8bd28eaac1dc2db1116fc1c430ba18b4`, PROOF.md:
   https://github.com/Akilleez-QA/read-em-and-weep/blob/c963b48d8bd28eaac1dc2db1116fc1c430ba18b4/research/hm/physical-source-membership/PROOF.md
   SHA-256: `74d801f850d281658955f7583a838c90ff49fa2f9122dea8a2391e01a71dcc0b`.
   Its full-family, canonical-correction, actual-cohomology and global-complex
   premises are retained, as are its seven pinned source inputs.
2. PR891 at `eb83daa45fe4686a9f55da604fb2cc8c28d47fb0`, PROOF.md:
   https://github.com/Akilleez-QA/read-em-and-weep/blob/eb83daa45fe4686a9f55da604fb2cc8c28d47fb0/research/hm/generic-parameter-calibration/PROOF.md
   SHA-256: `98fa36fff78c35f5dc071bbc52aa5e44e045c5f3a8252672a63e1015d027eed9`.
   We use its multiplicity-free cyclic-support argument and its axis/square
   support patterns. We do not apply its physical trace observation to a
   source outside that trace observation's certified domain.

## 1. The cohomological defect is defined before membership is known

Use G=A5 on the even representations of 2.A5, with the actual distinct
negative A=Sym^2 W and positive V=Sym^2 U, U=Wprime. Set

    S=Sym^3 A=A+V+P4,     D=D5,     R=S tensor D,
    I=im(q:M2 -> M4)=2V+3P4+3D5,
    M=Hom_G(R,I),        dim M=27.

Assume the supplied global cochains Z,V_h,W_h are independently known to
be closed, and to form coherent equivariant polynomial families on the
ENTIRE homogeneous parameter/source module. Retain the fixed canonical Z,
the preceding full-family division q[v_h]=a h zeta_a, and the canonical
or independently compared canonical correction b. Their bidegrees and
physical twists are exactly those of PR894.

Then the closed cubic/linear family

    T_W(a,h)=a(V_h(a)-b(a,h)Z_a)-q W_h(a)

has an independently defined cohomology class, whether or not it belongs
to the image of the differential. The preceding canonical factorization
places that class in I, giving

    F_W=Omega(W)=[T_W] in M.

This construction uses closedness and the actual global-cochain/cohomology
comparison, not a presumed primitive E. PR894 proves

    F_W=0  iff  T_W=dE for a global equivariant polynomial family E.   (C1)

Thus cohomology-valued evaluation below is legitimate BEFORE source
membership is established. This is precisely what cannot be presumed
for a trace response whose domain is only im(d).

## 2. Exact membership-observation weights are 8,8,11

Let pi_A,pi_V,pi_P be the three isotypic projections on the primal S.
For nonzero a define J(a) by the nonzero components of a^3, as in PR891.
For F in M let

    Ev_a^I(F):D -> I,    h -> F(a^3 tensor h).

This is the complete h-family of actual cohomology classes. It is not
one source value, one scalar functional, or the ten-dimensional trace
family of PR889. Scaling a changes the evaluation by its cubic scalar;
zero observations are well-defined on the parameter line, with its
O(3) fiber retained.

The universal tensor decompositions give

    A tensor D=A+V+P4+D5,
    V tensor D=A+V+P4+D5,
    P4 tensor D=A+V+P4+2D5.

Pairing them with I=2V+3P4+3D5 yields

    dim Hom_G(A tensor D,I)=2+3+3=8,
    dim Hom_G(V tensor D,I)=2+3+3=8,
    dim Hom_G(P4 tensor D,I)=2+3+6=11.                    (C2)

Consequently PR891's cyclic-support argument gives the exact formula

    dim ker Ev_a^I = 8*[pi_A(a^3)=0] + 8*[pi_V(a^3)=0]
                       + 11*[pi_P(a^3)=0],              (C3)
    dim im Ev_a^I = 27 - dim ker Ev_a^I.

Here brackets denote indicators. These are structural dimensions of
spaces of equivariant maps, not ranks of selected actual instances.
No assertion is made that every formal support pattern occurs.

For completeness, the target-independent step is short: if Ev_a^I(F)=0,
equivariance gives F((g a)^3 tensor h)=g F(a^3 tensor g^-1 h)=0 for all
g and ALL h. Hence F vanishes on Gspan(a^3) tensor D. The multiplicity-free
decomposition of S identifies that cyclic submodule with the sum of its
nonzero isotypic components. The kernel therefore consists exactly of
the missing-component Hom spaces, whose dimensions are (C2).

## 3. Generic and special observation interfaces

PR891 proves that the same support-open

    O={ [a] : pi_A(a^3),pi_V(a^3),pi_P(a^3) are all nonzero }

is a nonempty G-stable Zariski-open subset of P(A). Equation (C3) shows
that Ev_a^I is injective for every [a] in O.

For a supplied admissible family satisfying Section 1, membership is
therefore equivalent to the entire h-family of classes [T_W(a,h)]
vanishing at ANY one abstract parameter line certified to lie in O.
This does not identify, select, or certify the availability of an actual
physical parameter, and supplies none of the class observations.

There is also a special-orbit alternative. PR891 identifies the supports
of any semisimple C5 axis p and any C5-fixed square s as

    J(p)={A,V},       J(s)={V,P4}.

Equations (C2)-(C3) consequently give

    axis:  kernel 11, image 16;
    square: kernel 8, image 19;
    joint axis-square observation: kernel 0, image 27.            (C4)

Thus both complete h-family cohomology observations vanishing is
equivalent to membership, without requiring p and s to be associated.
Neither special observation alone suffices on the unrestricted sector M.

The 16- and 19-dimensional images have an eight-dimensional shared
channel, Hom_G(V tensor D,I). Their joint image is the fiber product over
this channel, using the evaluation quotient identifications. This is a
compatibility relation, not a direct identification of raw coordinates
at two different parameter lines and not 35 independent conditions.

## 4. Why this does not circumvent the trace obstruction

The values in Sections 2-3 lie in the full actual cohomological image I.
Their complete family observation can carry all 27 multiplicity slots.
They have not been compressed through PR889's ten-dimensional trace-family
space. The lower bound of seventeen invisible directions for any such
independently defined linear trace detector therefore remains unchanged.

The logical order is:

1. Authenticate the full closed coherent polynomial source family and
   the preceding canonical division/correction, so F_W is defined in M.
2. Establish the complete cohomology-family zero observation in Section 3,
   or otherwise prove F_W=0. Then PR894 supplies global polynomial-source
   membership and an abstract primitive, unique only modulo boundaries.
3. Only afterward apply the separately authenticated physical contraction,
   global trace and reference-calibration interfaces of PR889/PR891.

In particular no eta outside its certified domain, no unknown physical
reference, no base-fiber multiplier cancellation, and no actual instance
evaluation is used to establish (C1). The new deduction is a sharp
cohomological observation interface for membership, not a physical packet
certificate, primitive construction, source exclusion, or theorem repair.
