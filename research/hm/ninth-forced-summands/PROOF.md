# Two forced summands of the actual ninth-neighborhood kernel

Work over C with G=SL2(F5), T=P(W*), A=Sym2 W, S=Sym3 W, D=Sym4 W, T6=Sym5 W, V the other three-space and P the even four-space. All line bundles on T retain their equivariant linearizations. B is the actual normalized HM adjoint bundle. Neighborhoods are ordinary Cartier neighborhoods of the positive plane inside each negative-pencil hyperplane.

## 1. Exact actual inputs

INPUTS.json authenticates three immutable originals in Akilleez-QA/read-em-and-weep:

- REPAIR, PR1026 at a97fbc0084d08da8ab362589e658082f3fcc0f52: the actual even seventh-neighborhood cohomology H7 is presented by the fiberwise injection

      Q=P O(2) plus W O(-1) -> U plus J,
      U=(A+V+P+D) O(4),   J=(V+P+D) O(6).

  Its U component is the actual secondary b, whose A row is identically zero. The J component retains the actual sixth-normal correction and changes by h b when its representative changes. There is the actual quotient phi:H7->A O(8) whose kernel is H9, the even ninth-neighborhood R1.
- CUP, PR974 at5ce277d0476224f9f3fdbc79d1750210a2169708: the actual quadratic commutator boundary for B(2) on the third neighborhood is the nonzero fiberwise injection

      c:A O -> (V+P+D) O(2),

  with image in D O(2), identified with the twisted dual of the actual y:D O->A O(2). The exact y sequence has kernel W O(-3). The nonzero scalar of this actual cup is already proved, not inferred from multiplicity.
- RANK, PR986 at2f3eb11a6f55582e17f56c8bc9b310db9a37424d: full-sheaf ninth-neighborhood duality gives canonically

      H9=(ker Theta)* O(8),

  with rank H9=18, degree102, rank ker Theta=18 and degree42.

No actual coefficient, parameter, point, jet, derivative, matrix or instance rank is selected here.

## 2. Result

The actual adjacent-layer restriction of phi to J is onto, with kernel

    J0=(V+P) O(6) plus W O(3).                       (1)

The W O(3) term consequently survives as a split summand of H9; the identically zero secondary A row also produces a split A O(4) summand. More precisely,

    H9 = W O(3) plus A O(4) plus R13,
    ker Theta = W O(5) plus A O(4) plus R13* O(8),   (2)

where R13 has rank13 and degree84. Its dual twist has degree20. There is an actual fiberwise injective reduced presentation

    0 -> Q -> (V+P+D) O(4) plus (V+P) O(6)
      -> R13 -> 0.                                 (3)

The existence of (3) does not canonically split the remaining positive-degree target extension or choose its coefficient maps. The two displayed summands in (2) are selected by the actual filtered presentation and its maps, not by an arbitrary Birkhoff-Grothendieck decomposition. Scalar-normalized identifications with the named representations remain unchosen.

## 3. Authenticate the actual J restriction by duality of adjacent layers

Let E_m(t) be the positive eigensheaf obtained by finite normal projection of B_H(t)|mR. The last step for B(3) is the actual extension

    0 -> B_R(-5) O(8) -> E_9(3) -> E_7(3) -> 0.

Pull this extension back along the normal degree-six layer B_R(-3) O(6) inside E_7(3). Its middle term consists exactly of normal degrees6 and8 in the positive part. Cartier multiplication identifies it with E_3(-3) O(6): twisting by the sixth power of the plane ideal changes B(3) to B(-3) and contributes O_T(6). The omitted degree7 part is odd. Naturality of connecting morphisms therefore identifies phi restricted to J with the ACTUAL quadratic boundary

    d:H1(B_R(-3)) O(6) -> H2(B_R(-5)) O(8).         (4)

This restriction involves only the original second-normal transition class. Higher transition terms have order at least4 and send a degree-six section beyond the ninth truncation. Thus no higher correction to (4) has been silently discarded, even though all corrections remain in the other components of phi.

Plane Serre duality and the trace form identify H1(B_R(-3))* with H1(B_R), and H2(B_R(-5))* with H0(B_R(2))=A. Under these identifications, the transpose of (4), twisted by O(8), is exactly c from CUP, up to the harmless nonzero sign of the boundary convention. This is naturality of cup products under the trace pairing: tr([z,s]t)=-tr(s[z,t]). Equivalently apply full-sheaf relative duality on the third Cartier neighborhood, whose relative canonical bundle is p*O(-1) O_T(-2); B(-3) is paired with B(2) O_T(-2). The normal degree0 and2 layers are exchanged. The third-neighborhood canonical factor has even inversion character, so positive parts pair with positive parts. Duality is applied to the full sheaf before taking eigenspaces.

CUP already proves c nonzero with its actual D component the twisted dual of y. Hence (4) is, on D O(6), a nonzero multiple of

    y(6):D O(6)->A O(8).

It is zero on V and P: their possible degree-two coefficient maps to A vanish since A tensor A=1+A+D. The dual y exact sequence gives the actual kernel W O(3), proving (1). This uses authenticated nonvanishing and actual extension naturality, not just the one-dimensional Hom space.

## 4. Correct order of target elimination

Choose any equivariant representative of the actual seventh presentation from REPAIR, and compose its quotient U plus J->H7 with phi. Denote this onto map by ell and put F24=ker ell. Since ell on J is already onto, projection to U gives

    0 -> J0 -> F24 -> U -> 0.                       (5)

Every relevant ordinary Ext1 vanishes: the line differences for the degree-four constituents of U into (V+P) O(6) or W O(3) are2 and-1, respectively. Thus (5) splits equivariantly after averaging. In particular

    F24 ≅ U plus (V+P) O(6) plus W O(3),

with rank24 and degree108. This proof does NOT use Ext1((V+P) O(6),W O(3)); those groups need not vanish. The direct sum inside J0 comes from the actual D-block kernel, before (5) is split. Eliminating in the opposite order would introduce an unjustified extension assumption.

The actual map from Q lands in F24, and remains fiberwise injective. Its quotient is H9: a vector in U plus J maps into ker phi precisely when its ell value is zero. Thus

    0 -> Q -> F24 -> H9 -> 0.                       (6)

## 5. The forced W summand and its independence of choices

The intrinsic projection J0->W O(3) extends to a retraction rho:F24->W O(3) using any splitting of (5). This extension is unique, because Hom(U,W O(3))=0 already by line-bundle degrees. Its restriction to the actual W O(3) subbundle is the identity. Thus F24 has a uniquely selected W retraction extending the adjacent-layer projection.

Moreover

    Hom_G(P O(2),W O(3))=Hom_G(P,W tensor W)=0,
    Hom_G(W O(-1),W O(3))=Hom_G(W,W tensor D)=0,

using W tensor W=1+A and W tensor D=S+T6. Therefore rho kills the actual Q map in (6). It descends to a retraction of H9 onto the actual W O(3) subbundle. That subbundle injects into H9, since a Q vector mapping into it would have nonzero rho value unless it were zero. This proves its split survival.

Changes of the seventh representative act by triangular shears fixing J and the quotient U. They transport ell and F24 compatibly with the actual H7 and phi. The unique extension property of rho shows that its descended retraction and inclusion are unchanged. In particular the conclusion does not depend on a selected sixth-normal lift.

## 6. The secondary zero row gives the simultaneous A summand

The canonical A O(4) subspace of U has a unique equivariant lift into F24. Existence follows from the vanishing of Ext1 in (5). For uniqueness, its possible differences lie in Hom_G(A O(4),J0), which is zero: the W term has negative line degree, while

    Hom_G(A,(V+P) tensor A)=0

by A tensor V=P+D and A tensor P=V+P+D. Write this lift as i_A. The projection pi_A:F24->U->A O(4) is a retraction of i_A. Since the U component of Q is the actual secondary map and its A row is zero, pi_A kills Q and descends to H9. Consequently i_A injects into H9 as a split A O(4) summand.

These two splittings commute: pi_A kills W O(3), since the latter lies in J0, and rho i_A=0 because Hom(A O(4),W O(3))=0. Thus (2) holds simultaneously. Abstract Hom(W O(3),A O(4)) is not zero, but it is irrelevant to this conclusion: the actual projection pi_A has just been shown to annihilate the actual W subbundle. No unsupported vanishing in that direction is used.

The unique lift i_A in (5) is transported by the same triangular shears as in Section5, so its resulting inclusion is independent of the representative. Its selection uses the actual U-layer and actual ninth quotient. This is not a claim that every section of H9->C5 over the A summand is abstractly unique.

## 7. Residual presentation, degrees and limits

Let F19 be the common kernel of rho and pi_A in F24. The preceding construction gives

    0 -> (V+P) O(6) -> F19 -> (V+P+D) O(4) -> 0.

Its ordinary Ext1 is zero, so it has an equivariant splitting, without a uniqueness assertion. The actual Q map lies in F19. Quotienting yields (3), with all surviving actual corrections and complement choices retained. Its rank and degree are

    rank R13=19-6=13,
    deg R13=(7*6+12*4)-6=84.

The two eliminated summands have degrees6 and12; together with84 these total102, as required for H9. Dualizing the actual split decomposition and twisting by O(8) gives the second decomposition in (2); the residual degree is13*8-84=20. The full degree is10+12+20=42, as required for ker Theta.

The result forces actual direct summands and a smaller actual presentation from higher-neighborhood naturality. It does not compute the residual map, choose the actual secondary torsion alternative, identify global middle cohomology, select an opposite bundle type or top sigma, or exclude any source/catalogue alternative. No actual instance was evaluated and no geometric extension was replaced by its associated graded without the explicit argument above.
