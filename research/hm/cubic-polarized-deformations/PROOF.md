# Polarization lifting and the 540-dimensional section obstruction

Status: independently mathematically reviewed (PASS); see REVIEW.md. Not formally checked. Work over C. No selected actual HM/source coefficients, matrices, point evaluations, numerical ranks, searches or computer algebra are used. All differential formulas are intrinsic, and their injectivity uses previously proved universal branch transversality.

## 1. Dependencies and statements

The scope and evidence boundaries are those of PR1 and research/README.md at 2531056eae05fdf31e8fb4ca3affc5907073ad73 in Akilleez-QA/read-em-and-weep. This concerns the cubic fourfold image, not the original full-adjoint or algebraicity claims.

Pinned inputs:

- PR614, 73fbf75838c91804ca637b5916d6aac217240958, research/hm/cubic-global-deformations/PROOF.md: V=V_51 has only locally trivial abstract Artin deformations, all lift over small Artin extensions. Its tangent sheaf has h0=0,h1=576,H2=0. For its normalization M, h0(Theta_M)=0,h1(Theta_M)=96,H2(Theta_M)=0; Theta_V=nu_*(Theta_M tensor I_Omega).
- PR611, 12b28d33627cc0e8b283d142dc16439a51bb5e00, research/hm/cubic-branch-transversality/PROOF.md: M=Bl_Z(P4), with thirty distinct centers; V is the reduced image in P9, with sixty reduced double values Sigma and 120 normalization marks Omega. Its structure algebra consists of functions with equal values at each paired mark, and its normalization quotient K has length60. The two four-dimensional projective branch tangent images at each double value intersect in zero. h(O_V)=(1,60,0,0,0), and h(O_M)=(1,0,0,0,0).
- PR604, a4a0b5ed6e9dd0c18e3a263d1b3f8d9a49f2bf8d, research/hm/cubic-embedding-locus/PROOF.md, as incorporated in PR611: L=O_V(1) pulls back to D=3H-E on M. The map M->P9 is the cubic system through Z.
- PR589, a1c77f791158cc0976df80220c958a50c2217ee3, research/hm/eigenline-postulation/PROOF.md: the exact cubic restriction image on Z has dimension25, hence h0(I_Z(3))=10 and h1(I_Z(3))=5. Its universal configuration input is PR587, 865ab24e91333688d7ae76303d7d594aae8521f8.

Write S=H0(V,L), and let T_pair denote first-order deformations of the pair (V,L), with the special-fiber identification fixed and with line-bundle isomorphisms allowed. Then:

1. h0(V,L)=10, h1(V,L)=65, and H^i(V,L)=0 for i>=2.
2. Forgetting L is formally smooth on Artin deformation functors. T_pair has dimension636 and fits into 0->H1(O_V)->T_pair->H1(Theta_V)->0. Pair deformations are unobstructed.
3. There is a canonical linear section-obstruction map

       B:T_pair -> Hom_C(S,H1(V,L)).

   All ten sections lift to a given first-order pair deformation if and only if its class belongs to ker B.
4. A canonical540-dimensional subspace F of T_pair satisfies B|F injective. More precisely,

       0 -> F -> T_pair -> H1(M,A_D) ->0,
       H1(M,A_D) = H1(M,Theta_M),   dim H1(M,A_D)=96,

   where A_D is defined below. Consequently dim ker B<=96 and rank B>=540. Every nonzero direction in F fails to preserve the complete ten-section system. In particular, no nontrivial pure line-bundle direction preserves all ten sections.

No exact dimension of ker B or unobstructedness of the section-preserving locus is claimed.

## 2. The complete section space and its cohomology

The blowup has pi_*D=I_Z(3) and R^i pi_*D=0 for i>0. To see the required twist directly, use 0->O_M(-E)->O_M->O_E->0. The blowup structure sheaf has no higher direct images, and E is a disjoint union of P3s with H^i(O_P3)=0 for i>0. The map O_P4->O_Z is surjective as sheaves; pushforward therefore gives pi_*O_M(-E)=I_Z and all its higher direct images zero. Projection formula proves the assertion for D. The cubic restriction sequence and PR589 give h0(D)=10,h1(D)=5,H^i(D)=0 for i>=2.

The ten coordinate sections defining the given cubic morphism are linearly independent: they are the full ten-dimensional cubic system through Z (equivalently the dual of its defining ten-dimensional quotient). Their restrictions to V remain independent, since their pullbacks are independent. Pullback injects H0(V,L) into H0(M,D). Both spaces therefore equal this ten-dimensional system. In particular every normalization section descends; this is not inferred merely from the normalization quotient length.

Tensor the normalization sequence by L:

       0 -> L -> nu_*D -> Q ->0,          Q=K tensor L.

The map on global sections into H0(Q) is zero by the preceding equality. Thus

       0 -> H0(Q) -> H1(V,L) -> H1(M,D) ->0.              (1)

Here Q has length60, so h1(L)=60+5=65; higher cohomology is unchanged and zero. No splitting of (1) is asserted.

## 3. Lifting L and the tangent space of pairs

For a small extension A'->A with kernel J, and any chosen flat lift V_A' of V_A, the sheaf of units has exact sequence

       1 -> 1+J O_V -> O_(V_A')^* -> O_(V_A)^* ->1.

Flatness identifies the first term additively with J tensor_C O_V. The obstruction to extending a line bundle lies in H2(O_V) tensor J, which is zero. Lifts form a torsor under H1(O_V) tensor J, up to the usual preceding unit map. This proves formal smoothness of the forgetful map; combined with PR614 it proves existence of lifts for all pair deformations. Ampleness persists under nilpotent thickenings, so these remain polarizations, but very ampleness in degree one does not follow.

For a line bundle N on a scheme X let A_N be the sheaf of C-linear operators P:N->N for which there exists a derivation delta of O_X satisfying P(fs)=fP(s)+delta(f)s. There is an exact sequence of coherent O_X-modules

       0 -> O_X -> A_N -> Theta_X ->0.                   (2)

Local frames split the symbol map, even when X is singular. Infinitesimal automorphisms of the pair are precisely these operators. Since all abstract deformations of V are locally trivial and line bundles trivialize locally, Cech gluing identifies T_pair=H1(V,A_L). Scalar automorphisms are included in H0(A_L); they do not change this H1 tangent classification. The long exact sequence of (2), H0(Theta_V)=0 and H2(O_V)=0 give the asserted exact tangent sequence and dimension60+576=636.

An operator acts on each fixed global section. Thus evaluation yields an O_V-linear morphism

       A_L -> Hom_C(S,L)=S* tensor L.

Its H1 map is B. Explicitly, for a transition cocycle P_ij representing a pair deformation, the defects of the constant local lifts of s are P_ij(s), up to a uniform sign convention. They are coboundaries exactly when s lifts. Linearity then proves the simultaneous assertion for S. At higher Artin steps individual sections similarly have obstruction in H1(L) tensor J, but no higher simultaneous unobstructedness is inferred here.

## 4. A normalization exact sequence for differential operators

There is a natural injective map A_L->nu_*A_D. For its construction use a local frame of L, so P=delta+a. By PR614 delta extends uniquely to the normalization as a vector field vanishing at all paired marks, and a pulls back as multiplication. Changing the frame gives the usual derivative correction upstairs as well, so these extensions glue. Injectivity follows on the dense smooth locus or in these frames.

Its quotient C is supported on Sigma, and there is an exact sequence

       0 -> A_L -> nu_*A_D -> C ->0.                    (3)

At a double value y with paired marks p,q, choose a frame of L near y and pull it back. A normalization operator has local branch forms delta_p+a_p and delta_q+a_q. It descends precisely if

       delta_p(p)=0,   delta_q(q)=0,   a_p(p)=a_q(q).      (4)

Necessity and sufficiency follow from the tangent-sheaf description and the equal-residue description of O_V. Therefore C_y has dimension4+4+1=9, with coordinates (u,v,a) in T_pM direct-sum T_qM direct-sum C in this frame. Arbitrary such data lift locally, since M is smooth. These coordinates change under frame replacement, so no canonical splitting is asserted. Multiplication by a function vanishing at y kills the quotient, hence C is a reduced skyscraper module of total length540. The calculation can equally be made in the completed rings and descended by faithful flatness; the operator sequence is defined algebraically before completion.

On M, (2) and h0(Theta_M)=0,H1(O_M)=H2(O_M)=0 give

       H0(A_D)=C,    H1(A_D)=H1(Theta_M),    H2(A_D)=0.

The same H0 calculation gives H0(A_L)=C. The map between these H0 spaces is the identity on scalar operators. Since C is a skyscraper, (3) yields

       0 -> H0(C) -> H1(A_L) -> H1(A_D) ->0.             (5)

Set F equal to the image of H0(C). This defines F intrinsically and proves its dimension540, without assuming existence or uniqueness of simultaneous normalization for arbitrary Artin deformations. Its quotient by the pure Picard60 directions is the480-dimensional marked-normalization kernel of PR614, by the diagram of symbol sequences. Thus the informal interpretation as marked-point motions plus line-gluing changes is consistent, but (5), not that interpretation, is its definition.

## 5. Transversality makes the section obstruction injective on F

Operators upstairs act on S=H0(M,D). Together with their action downstairs this gives a commutative diagram whose top row is (3), bottom row is

       0 -> Hom_C(S,L) -> Hom_C(S,nu_*D) -> Hom_C(S,Q) ->0,

and whose vertical arrows are evaluation. Let e:C->Hom_C(S,Q) be the quotient map. Naturality of connecting homomorphisms identifies B on F with

       H0(C) --H0(e)--> Hom_C(S,H0(Q))
              --> Hom_C(S,H1(L)).                       (6)

The last arrow is injective by (1). It remains to prove e injective, and this is precisely where the branch transversality input is used.

At y fix the same common frame as above; represent a section s by f_p on the first branch and f_q on the second, with f_p(p)=f_q(q)=s(y). Then

       e_y(u,v,a)(s)=d f_p(u)-d f_q(v)+a s(y).            (7)

No actual values or coefficients are computed in (7). It is the universal derivation rule. Write ev_y:S->L_y for the nonzero evaluation functional, with a frame identifying its target with C. Modulo its value line C ev_y in S*, the derivative functional d f_p(u) is the differential of the projective morphism Phi:M->P(S*) at p, and likewise for q. If (7) is zero, quotienting by that value line gives equality of the two projective tangent vectors. PR611 says the two branch tangent images have zero intersection and each branch differential is injective. Hence u=v=0. Then a ev_y=0, and global generation gives ev_y nonzero, so a=0.

Thus e_y is injective at all sixty nodes. This argument is unchanged by a local frame change: derivative functionals change by multiples of ev_y, compensated by the a-coordinate. Since the skyscraper supports are distinct, e is injective, as is H0(e). Equation (6) proves B|F injective. Consequently the quotient map in (5) embeds ker B into H1(A_D), proving dim ker B<=96 and rank B>=540. This is an exclusion theorem, not a selected-instance evaluation-rank computation.

## 6. The exact residual 96-to-110 compatibility map

Put W=Hom_C(S,H1(L)) and R=B(F), so dim W=650 and dim R=540. Since B induces an injective identification F->R, it induces a canonical residual map

       b:H1(M,A_D)=T_pair/F -> E=W/R,    dim E=110.       (8)

The projection ker B->ker b is an isomorphism. Injectivity follows from B|F injective. For surjectivity choose any lift t of a class in ker b. Then B(t) belongs to R, so there is a unique f in F with B(f)=B(t); t-f is in ker B. It is independent of the chosen lift. This does not assert a canonical splitting of (5).

Moreover R lies in Hom_C(S,H0(Q)) by (6). Applying Hom_C(S,-) to (1) and quotienting by R gives the exact target filtration

       0 -> Hom_C(S,H0(Q))/R -> E
         -> Hom_C(S,H1(D)) ->0,                         (9)

whose outer dimensions are600-540=60 and10*5=50. Thus b is an intrinsic96-to110 map, with a60-dimensional residual descent channel and a50-dimensional normalization-section channel. Their decomposition is not asserted to be canonical. The unresolved exact tangent dimension is precisely dim ker b. This eliminates all540 correction variables exactly; it does not compute or assume a maximal rank for b.

## 7. Consequence for first-order embedded deformations

The given embedding uses the complete S. A first-order pair deformation supports a lift of this embedding precisely when its class is in ker B. Indeed lift a basis of S; Nakayama gives relative generation. The resulting map to P9 over the dual numbers is a closed immersion: it is proper, has a closed immersion on the special fiber, is quasi-finite and hence finite, and its map on structure sheaves is surjective by Nakayama. Conversely an embedding lifting the given one supplies the line bundle and ten lifted coordinate sections.

For a pair class in ker B, lifts of a fixed ordered basis differ by Hom_C(S,H0(L)), of dimension100. Scalar automorphisms of the lifted line bundle identify the one-dimensional common-scalar direction. There are no infinitesimal automorphisms of V because H0(Theta_V)=0. Hence the tangent space of embedded deformations in fixed P9 has dimension

       99 + dim ker B = 99 + dim ker b <=195.            (10)

Equivalently the99-dimensional projective-coordinate directions account for the fiber over section-preserving pair classes. This is only a tangent bound. It does not say that all96 normalization deformation directions extend to embedded directions, or that any positive-dimensional embedded family or Hilbert component is smooth.

## 8. Contribution and remaining dependency

The abstract deformation tangent space576 and pair tangent space636 do not measure the tangent space preserving the cubic embedding. A canonically identified540-dimensional subspace of pair directions is ruled out, with an explicit intrinsic obstruction map and proof of injectivity. The remaining section-preserving tangent space injects into the96-dimensional normalization-deformation space. Determining its exact dimension requires the coupling of normalization deformations to the ten sections and paired descent conditions; no such remaining rank or exact kernel is claimed here. Formal polarization lifting does not itself prove preservation of the original complete section system, its HM presentation, the original full-adjoint claim, higher quantization, or algebraicity.
