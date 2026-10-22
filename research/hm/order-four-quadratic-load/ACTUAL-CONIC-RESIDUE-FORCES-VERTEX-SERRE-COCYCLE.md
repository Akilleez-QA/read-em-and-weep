# The actual conic residue forces a nonzero vertex Serre cocycle

## Result

The extra vertex-open Serre extension channel is not merely available. The actual nonzero CONIC residue forces a nonzero component in it. In the natural block-torus decomposition, that component is exactly a nonzero multiple of

    [1/(uv)] in H1(U,O_U(-2)),     U=X minus C.

It has cover degree zero and block-torus weight mu^(-2). No higher-cover-degree kernel term can mix with it, and none can mix with the vertex residue of weight mu^2.

Consequently the actual marked Serre bundle on U differs from the canonical vertex-residue eigenextension by an actual nonzero section-preserving cocycle I+tN. This result does not evaluate the normal-trace coefficient beta/alpha or any fourth Bockstein value. In particular this O(-2) extension cocycle must not be identified without calculation with the O(-1) cocycle in the dual trace calculation.

## 1. The global pure-conic extension is explicit

Use X=P_stack(1,1,2,2), physical O(1)=O_wt(2), positive coordinates a,b, and negative coordinates u,v. The reduced conic C is the regular intersection (u,v)=0; the vertex component Z_v is disjoint from it. The established actual zero scheme is Z=C disjoint union Z_v.

The conic Koszul sequence, with determinant orientation fixed, is

    0 -> O_X --(u,v)--> W tensor O_X(1)
      --(A,B) |-> uB-vA--> I_C(2) -> 0.             (1)

Here W denotes the equivariant two-dimensional coefficient space, identified with its dual by its determinant form. Formula (1) can also be read in an oriented local coefficient basis. Its residue on C is a nonzero constant. The residue line is

    det(N_(C/X)) tensor O_C(-2)=O_C,

since the two conic equations each have physical degree one.

Pull back (1) along I_Z(2) -> I_C(2). The resulting global extension class xi_C in Ext^1_X(I_Z(2),O_X) has nonzero conic residue and zero vertex residue: near C the two ideals coincide, while near Z_v the conic ideal is O and (1) is locally split. Normalize xi_C to have conic residue one in this Koszul orientation.

The established vanishings H1(X,O_X(-2))=H2(X,O_X(-2))=0 identify global Ext with its residue sections. Therefore xi_C is precisely the unique pure-conic residue class, not an arbitrary extension with the same local behavior.

## 2. Restriction to the vertex open gives the Euler class

On U=X minus C, the conic ideal is O_U. Thus (1) becomes

    0 -> O_U -> W tensor O_U(1) -> O_U(2) -> 0.   (2)

Its class belongs to H1(U,O_U(-2)). Cover U by u!=0 and v!=0. For a local section h of O(2), splittings of its right arrow are

    s_u(h)=(0,h/u),     s_v(h)=(-h/v,0).

Their difference is exactly

    s_u(h)-s_v(h)=(u,v) h/(uv).                  (3)

Hence the class of (2) is [1/(uv)], with the sign fixed by this ordering.

It is NONZERO. Restriction to the negative line L=P(W) gives the ordinary equivariant Euler extension

    0 -> O_L -> W tensor O_L(1) -> O_L(2) -> 0.

It cannot split, since Hom(O_L(2),W tensor O_L(1))=0. Equivalently [1/(uv)] generates H1(L,O_L(-2)). This also checks that the class lies in the cover-degree-zero summand, not merely in a filtered quotient.

The restriction of xi_C to U is the pullback of (2) along I_Z(2)->O_U(2). Under the natural injection

    H1(U,O_U(-2)) -> Ext^1_U(I_Z(2),O_U),          (4)

it is therefore precisely the nonzero class (3). The injection follows from local-to-global Ext for the regular codimension-two ideal, or from the ideal sequence and vanishing of Ext below codimension two for O_Z.

## 3. The local-cohomology comparison is genuinely nonzero

Localization for O_X(-2), together with its global H1 and H2 vanishing, gives

    H1(U,O_U(-2)) = H2_C(X,O_X(-2)).              (5)

The natural map

    Ext^2_X(O_C(2),O_X) -> H2_C(X,O_X(-2))         (6)

sends the conic Koszul residue to its generalized fraction 1/(u,v). Under (5), this is the Cech class (3), up to the common localization sign convention. This follows either by comparing the two-generator Koszul complex with the localization Cech complex, or directly from the splittings (3).

The source of (6) is H0(C,O_C)=C: sheaf Ext is concentrated in codimension two and is the residue line computed in Section 1. Section 2 proves the image nonzero, hence (6) is injective. Thus the actual conic residue cannot disappear on passing to local cohomology. No support-only inference is used.

## 4. Full line factors and the canonical weight separation

Let phi_mu fix a,b and send u,v to mu u,mu v. It acts on the IDEALS and their Ext spaces; no action on the actual middle bundle is assumed. On a root cover of u!=0, transverse coordinates x=a/sqrt(u), y=b/sqrt(u) have weight mu^(-1/2), while the physical O(-2) frame u^(-2) has weight mu^(-2). Therefore the cover-degree-d term of the kernel in (4) is

    H1(L,Sym^d(Wprime) O_L(-2-d/2)),

with character mu^(-2-d/2). Odd d has nontrivial gerbe stabilizer and does not contribute to this ordinary line-bundle cohomology after exact tame pushforward. For d=2j the character is mu^(-2-j), j>=0.

In particular:

- the character mu^(-2) occurs only in degree zero, with kernel C=H1(O_L(-2));
- the character mu^2 never occurs in this kernel;
- all higher-degree invariant kernel pieces, whether present or absent, have strictly different characters.

The actual homogeneous vertex zero scheme is preserved by the block torus. Its invariant residue line has character mu^2, whereas the conic residue line has character mu^(-2), as established with determinant factors in the Serre double-cover theorem. These characters agree with the explicit fraction 1/(uv) above.

On U the exact equivariant sequence is

    0 -> H1(U,O_U(-2))^G
      -> Ext^1_U(I_Z(2),O_U)^G
      -> H0(Z_v,Lres)^G -> 0.                    (7)

The last term is a line of weight mu^2. All maps are torus-equivariant because they concern the fixed ideals and naturally linearized outer line bundles. Rational torus representations decompose into weight spaces. Consequently (7) has a UNIQUE weight-mu^2 lift of a specified vertex residue. This is the canonical vertex eigenextension. Its existence also follows by restricting the global pure-vertex class xi_v; its uniqueness follows because the kernel has no such weight.

This argument is valid even if the invariant kernel has infinitely many other weights: its coordinate algebra is a direct sum of nonnegative graded pieces, and each of those pieces has the displayed character. It does not replace a direct sum by an unproved completion.

## 5. The actual extension necessarily contains both components

The actual globally locally free Serre extension has invariant residues rho_C and rho_v, both nonzero. In the Koszul and vertex residue markings its global class is

    xi_actual = rho_C xi_C + rho_v xi_v.          (8)

Global Ext equals the residue space, so (8) is an equality of actual extension classes. Restricting to U and using Sections 2 and 4 yields

    xi_actual|U = rho_v xi_v|U + i(rho_C [1/(uv)]).
                                                               (9)

The first term is the weight-mu^2 eigenextension. The second is a NONZERO weight-mu^(-2) kernel class. No higher-degree invariant kernel term is hidden in (9): both global summands have the specified pure characters, and their possible kernel weights were exhausted above.

Thus the actual marked extension is not the pure homogeneous vertex eigenextension. This is a statement about the marked extension and section, not a claim about every possible unmarked isomorphism of its middle bundle.

On the chart u!=0, put z=v/u. The kernel representative is

    t = rho_C u^(-2)/z,                           (10)

so its coefficient in the physical O(-2) frame is rho_C/z. The magnitude of rho_C depends on the fixed residue normalization; its nonzeroness does not.

## 6. Exact section-preserving transition form

Let E_v be the vertex eigenextension with residue rho_v and actual section sigma, with its determinant identified with O(2). On local oriented frames write

    N = sigma sigma^t J,     J=[[0,1],[-1,0]].

Intrinsically N is the composite of the Serre projection E_v->O(2) with its section O->E_v, so N is a section of End(E_v)(2). It satisfies N^2=0, tr N=0, and N sigma=0. Multiplying by the O(-2) Cech class t makes a genuine endomorphism cocycle.

Changing an extension by the kernel class in (4) is exactly the usual change of splittings by sigma t times the Serre projection. Therefore, after compatible local identifications of the two marked extensions, its transition correction is

    I+t_ij N,                                    (11)

composed with the transitions of E_v. These corrections have determinant one and inverse I-t_ij N. Their cocycle law is additive because N^2=0 and because N transports with its indicated determinant line. Formula (11) is exact, not a first-order approximation. Refining the cover to trivialize the actual Serre presentations does not alter the nonzero class (10).

The marked transition correction (11) is the established structural output. To use it in the dual normal trace one still has to compute the transported cocycle representing theta and its residue. In particular nonzero rho_C is not by itself a value of beta or of the fourth obstruction.

## Inputs and verification

The actual scheme homogeneity, two residue lines and characters, and global Serre Ext identification are from NORMAL-QUADRATIC-NONZERO-BY-SERRE-RESIDUE-DOUBLE-COVER.md. The vertex-open extension ambiguity and dual trace distinction are isolated in NORMAL-TRACE-DUALITY-HAS-A-SECTION-LINE-RESIDUE.md. The physical determinant and stack conventions are in WEIGHTED-STACK-SQUARE-SHADOW-AND-PRIMARY-SCALAR.md.

Run python verify_conic_residue_vertex_serre_cocycle.py. It checks universal Koszul splittings, the nilpotent transition identities, and the exact symbolic weight separation. The geometric cohomology and actual residue inputs are explicitly dependencies. No frozen file is changed, no actual source coefficients are selected, and no actual-instance rank evaluation or model experiment is performed.

## Companion result

The argument in this note does not evaluate beta. The separate ACTUAL-NORMAL-TRACE-HAS-NONZERO-NILPOTENT-COMPONENT.md now proves beta!=0 by restricting the actual global dual class to the first conic neighborhood and checking its duality trace. That additional comparison does not change any of the distinctions or local calculations above, and does not evaluate the fourth Bockstein.
