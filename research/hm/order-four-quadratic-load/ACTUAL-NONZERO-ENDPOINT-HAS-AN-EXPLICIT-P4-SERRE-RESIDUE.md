# The nonzero endpoint has an explicit P4 Serre residue

For a=t^2 and h=XY^3, the proved normalized endpoint class is

    gamma=(3k/(Bc))[Y/z] in H1(Wprime O_L(-3)).

The actual cubic quotient identifies this class with the following explicit P4 component of the pure-vertex Serre residue:

    r_P4 = -(keA/(Bc)) [XY s^2+(c/2)X^2t^2].             (1)

Here e is the fixed nonzero socle normalization in the actual quotient map Q. For the actual normal direction, multiply (1) by the same unknown nonzero c_eta as the endpoint theorem. This is an exact global residue representative in V tensor A, not an evaluation of the fourth Bockstein or a selected coefficient choice.

## 1. An exact connecting calculation

The actual cubic sequence is

    0 -> Wprime O(-3) --f--> D5 O --Q--> V O(2) -> 0.

On the z chart the actual Q has, in particular,

    Q(Y^4)=e[A XY/(2B)-Ac X^2z^2/(2B)],
    Q(X^3Y)=e[X^2z+(B/A)Y^2z^2]/4,
    Q(XY^3)=e[-(A/B)X^2+Y^2z]/4,
    Q(X^2Y^2)=-eXYz/2.

Take the local quartic lifts

    p_x=-BY^4-Ac X^3Yz+Bc XY^3z^2,
    p_y^x=A X^2Y^2/z.

Then the COMPLETE identities are

    p_y^x-p_x=fY/z,
    Q(p_x)=Q(p_y^x)=-(eA/2)XY.

The first lift is regular on the z chart; the second is regular in w=-1/z since D5 O has coefficient transition one. Thus the actual connecting homomorphism sends the global residue -(eA/2)XY s^2 to [Y/z]. Multiplying by 3k/(Bc) gives the endpoint residue modulo the actual polynomial D5 subspace Q(D5).

## 2. Its canonical P4 projection

Equip V=Sym^2 Wprime and A=Sym^2 W with their invariant apolar forms, using <x^i y^(2-i),x^j y^(2-j)>=(-1)^i/binomial(2,i) for i+j=2. On V tensor A use their product. The actual decomposition V tensor A=P4+D5 is multiplicity-free. Hence P4 is the invariant orthogonal complement of the nondegenerate D5 image Q(D5).

The vector

    R=XY s^2+(c/2)X^2t^2

is orthogonal to every Q(h), h in D5, by the actual displayed Q formulas. Furthermore

    XY s^2 = (2/3)R + (2B/(3eA)) Q(Y^4).

Consequently the canonical P4 projection of XY s^2 is (2/3)R. Applying this to the residue from Section1 gives precisely (1). All scalar constants are retained; e is not set to one. Nonzeroness follows from the nonzero global endpoint already proved, and also directly from (1) with its unassigned nonzero parameters.

This canonical projection removes only J=Q(D5). It does not assert that the full D5 restriction to the vertex open vanishes, nor remove higher-frame information from a subsequent normal division.

## Reproduction and dependencies

Run python verify_nonzero_endpoint_explicit_serre_residue.py. It checks both exact connecting lifts, all five apolar orthogonality identities, and the explicit projection constant 2/3. Every source parameter remains unassigned.

The actual scalar Q is in ACTUAL-TWO-ENDPOINT-INPUTS-HAVE-COMPATIBLE-CONE-OPERATORS.md. The exact global quotient is ACTUAL-ENDPOINT-QUOTIENT-IS-LOWEST-VERTEX-COHOMOLOGY.md. The actual nonzero class is ACTUAL-ENDPOINT-NORMAL-VARIATION-IS-NONZERO.md. These inputs establish that this is an actual residue calculation, not a dimension-only identification.
