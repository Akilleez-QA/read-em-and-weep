> Mathematical update: BEILINSON-AMBIENT-RESTRICTION-ISOMORPHISM.md at8b35dbc5359e69c9317cedf3c9a452b533dbe05a proves H1(M4 I_S)=0 and that restriction on sections is an isomorphism. The extension boundary below is therefore zero, not an additional open gate. The cubic and Rao calculations remain valid.

# Actual ambient extension reduces uniquely to a cubic containing Gamma

## Scope and notation

Let X=P_Q(E), E=F_Q(3), and let b:Xhat->X blow up the fifty simple evaluation base points. Write L=b*O_X(1), H for the source quadric hyperplane class, Zexc for the sum of the exceptional divisors, and A=L-Zexc=f*O_P3(1). The resolved evaluation map f is flat by UNIFORM-FLAT-EVALUATION-FIBRATION.md. Gamma is its smooth rational sextic curve in P3. Put S=f^{-1}(Gamma) and M=O_Xhat(2L-H), the actual twist-four eigenline.

The known injection of actual endomorphisms into the descended section space is not assumed surjective. This note adds an ambient extension condition, retaining the actual maps. The common open includes the actual Rao injection q:M1->M3, equivalently H0(Q,I_{Z,Q}(3))=0, as pinned in QUADRIC-FIFTY-POINT-BOUNDARY.md. No coefficient or rank experiment is used.

## 1. Two acyclic twists

For d=2,3 one has

    M(-dA)=(2-d)L-H+d Zexc.

For the blowup of a smooth fourfold at points, b_*O(d Zexc)=O_X and all positive higher direct images vanish for 0<=d<=3. This follows successively from the exceptional quotient O_P3(-d), which is acyclic for d=1,2,3. Therefore

    R b_*M(-2A)=O_X(-H),
    R b_*M(-3A)=O_X(-L-H).

The first is acyclic because O_Q(-1) is acyclic. The second is acyclic because O_P(E)(-1) has zero relative cohomology. Consequently

    H^i(Xhat,M(-2A))=H^i(Xhat,M(-3A))=0 for every i.

## 2. A cubic always exists, and its extension is unique

The restriction map from cubics on P3 to Gamma has source dimension20 and target h0(P1,O(18))=19. Hence choose any nonzero cubic c in I_Gamma(3). No smoothness, irreducibility, or uniqueness of this cubic is needed. Its pullback cuts the Cartier divisor T=f^{-1}(V(c)) on Xhat. Flatness preserves the non-zero-divisor equation.

The exact sequence

    0 -> M(-3A) --c--> M -> M|T -> 0

and Section1 give isomorphisms

    H^i(Xhat,M) -> H^i(T,M|T) for every i.

In particular a section on S extends to the actual ambient eigenline if and only if it extends to T, and such an extension to T determines the ambient section uniquely. This is stronger than merely requiring descent from the normalization of S. It is not a claim that every descended section extends.

## 3. The exact remaining obstruction inside the cubic

Let J=I_{Gamma/V(c)}. The exact sequence on P3 is

    0 -> O_P3(-3) --c--> I_Gamma -> i_*J -> 0,

where i:V(c)->P3. Flat pullback and tensoring by M identify the obstruction sheaf on T as

    M|T tensor I_{S/T}.

Since the first term M(-3A) is acyclic, the sequence gives canonical cohomology isomorphisms

    H^i(Xhat,M tensor f*I_Gamma)
       = H^i(T,M|T tensor I_{S/T}).

The actual extension obstruction is therefore the boundary

    H0(S,M|S) -> H1(T,M|T tensor I_{S/T}).

Its kernel is exactly the image of H0(Xhat,M). The kernel on the left of the restriction map is zero: H0(Xhat,M tensor f*I_Gamma)=0 by the previously checked fifty-point restriction injection. The curve Gamma need not be Cartier in the possibly singular cubic, so J must not be replaced by an invertible sheaf without an additional proof.

## 4. The first non-acyclic higher twist retains actual cubic interpolation

For d=4, the only new exceptional contribution is R3 b_*O(4 Zexc), one copy of the residue field at each of the fifty points. The blowdown term is O_X(-2L-H). Its relative projective-bundle cohomology is O_Q(-6)[-1]. Thus its only nonzero cohomology is H4, of dimension h0(Q,O_Q(3))=30.

The resulting connecting map from the fifty exceptional classes to this thirty-dimensional group is dual, up to the natural one-dimensional determinant factors, to ordinary cubic evaluation on Z. One can verify this identification by Serre duality: K_Xhat= -2L+2H+3 Zexc, so

    K_Xhat - M(-4A)=3H-Zexc.

Its global sections are exactly cubics on Q vanishing at Z. The common-open Rao injection makes this space zero, so H4(M(-4A))=0. The same blowup sequence then gives

    h3(Xhat,M(-4A))=20,
    H^i(Xhat,M(-4A))=0 for i other than3.

Without that Rao hypothesis the exact cubic evaluation kernel/cokernel must be retained instead of these dimensions. This twist table shows why the actual ideal and its syzygies matter for ambient extension; acyclicity of degrees2 and3 does not imply acyclicity of the whole Gamma ideal.

This identifies a new necessary-and-sufficient ambient extension interface. It neither assumes that the smooth 45-intersect-400 space consists of actual endomorphisms nor proves the remaining extension obstruction zero.

## 5. The twenty-dimensional group is the actual residual kernel

The twist-four higher cohomology is more than a numerical match. Serre duality and the exact canonical calculation in Section4 give

    H3(Xhat,M(-4A))* = H1(Xhat,O(3H-Zexc))
                     = H1(Q,I_{Z,Q}(3)).

For the second equality, blowdown sends O(-Zexc) to the ideal of the fifty base points with no higher direct images. Projection X=P_Q(E)->Q then sends that ideal, twisted by 3H, to I_{Z,Q}(3), again with no higher direct images: apply projection to its exact sequence with the fifty point skyscrapers. The evaluation map O_Q(3)->O_Z(3) is surjective as a sheaf map.

The actual curve ideal sequence

    0 -> I_C(1) --q--> I_C(3) -> I_{Z,Q}(3) -> 0

gives

    H1(Q,I_{Z,Q}(3)) = coker[q:M1->M3],

because H2(I_C(1))=H1(O_C(1))=0 for the disjoint union of twenty-five lines. Therefore H3(Xhat,M(-4A)) is the dual of the actual Rao cokernel. In the previously pinned convention N_t=det(U) tensor M_{5-t}*, this reads

    ker[N2->N4] = det(U) tensor H3(Xhat,M(-4A)),

after the same fixed canonical-line normalizations used to identify omega_Q with O_Q(-3). If canonical volume forms are not fixed, retain their single global determinant lines throughout. No point-dependent rescaling is introduced.

Thus the first non-acyclic twist appearing in an ambient Gamma-ideal resolution carries exactly the actual twenty-dimensional residual input. This does not identify an unspecified syzygy map in such a resolution with the remaining adjoint boundary, or prove that boundary injective.
