# The residual rank-seven bundle has a canonical intrinsic first-jet complement

## Statement and scope

Retain the complete actual-geometric hypotheses of PR1218 and PR1222, with all their transitive assumptions, in the residual simultaneous rank-seven k=2 case. Let Q1=F6^- and Q2=Q1^- be its actual backward kernels. Let Uj be the actual auxiliary degree-eighteen jets, and let L10=O(-10) be the canonical scalar line in G6=F6 intersect B7.

Then the actual subbundles satisfy

    Q1=U3 direct-sum L10,
    F6=U4 direct-sum Z,
    Z=L10^+=W(-9).                                      (1)

Here Z is the saturated intrinsic first-jet bundle of the actual line L10. It is the canonical highest-degree subbundle of F6, and its projection to the actual quotient F6/U4 is an everywhere isomorphism. Its construction does not assume complete degree-ten coefficients or appeal to the separate canonical-ten-line theorem.

The two actual coherent derivative columns separate on (1):

    beta_(F6)(U4)=O(-10), the lower coherent column,
    beta_(F6)(Z)=O(-8), the upper coherent column,
    ker(beta_(F6)|U4)=U3,
    ker(beta_(F6)|Z)=L10.                               (2)

These are actual coherent images, not their positive-degree saturations. The displayed bundle decompositions are not horizontal: each summand has the nonzero indicated derivative.

This constrains the embedded F6 and its predecessor; it does not exclude or realize the simultaneous image, the cyclic rank-seven alternative, original delta=12, either F18 form, or a whole branch/profile. It gives no original tenth jet or algebraicity. No selected actual coefficient, graph scalar, parameter, point, jet, tensor, matrix, instance rank, or invariant normalization is evaluated. Only fixed universal quartic and first-jet identities are used.

## 1. Complete immutable inputs and actual flag data

INPUTS.json records the complete freshly fetched originals, exact commits, repository paths, UTF8 lengths, SHA256 and Git blobs:

* PR1218 at f5895c822322b4ddab07e51a97874d4528fb5b88, research/hm/rankfour-profile11-triplet-rankseven-equality/PROOF.md.
* PR1222 at f7abba83fedd46a9d91f5abbd9e40d3b02ae65f1, research/hm/rankfour-profile11-triplet-nonsplit-quotient/PROOF.md.

We work over C with the physical binary-icosahedral action G=SL2(F5), det W=1. Set A=Sym2 W, S4=Sym3 W and D=Sym4 W. Distinguish the actual auxiliary jet bundles Uj from their abstract representation factors.

The lower-column k=2 flag in PR1218 supplies

    U2=Q2=A(-16), U3=S4(-15), U4=D(-14),
    U2 subset U3 subset Q1 subset F6,
    U3 subset U4 subset F6,
    Q1 intersect U4=U3,
    Q1/U2=O(-10) direct-sum O(-12),
    Q1/U3=O(-10), U4/U3=O(-10).                         (3)

The identification Q2=U2 is actual: PR1218 constructs its last rank-three tail as the second jets of its degree-eighteen scalar line, then constructs U3 and U4 from that same line. In particular it is not an arbitrary A(-16) inside a bundle with the same abstract type.

The complete later input retains the actual scalar complement and proves the nonsplit quotient

    G6=Q1+U4=U4 direct-sum L10,
    L10=O(-10), M=F6/U4=W(-9).                          (4)

For clarity, G6 is the kernel of the actual upper projection on F6, while Q1 is the kernel of the entire derivative. Thus G6/Q1 is the lower coherent line in I6. The exact lower-only surjection from U4 in (6) shows that its full inverse image is Q1+U4, proving the stated sum. Consequently

    G6/U3=(U4/U3) direct-sum L10=2O(-10).              (5)

Finally the actual derivative of F6 surjects onto the coherent image

    I6=O(-8) direct-sum O(-10),
    beta_(F6)(U4)=the full lower O(-10).                (6)

Its two summands embed into distinct actual normal lines, each with the simple D12 factor. No saturation is substituted for either target in the argument below.

## 2. A fixed universal quartic kernel

We will use the universal exact sequence

    0 -> A(-2) -> D O -> W O(3) -> 0.                  (7)

Here the map on the right is complete quartic first-jet evaluation, equivalently the first polarization of a formal binary quartic followed by its universal evaluation on the variable tautological line. The determinant identifies W with its dual.

To see the kernel directly, a formal quartic has zero value and zero first derivative on the variable line exactly when it is divisible by the square of its vanishing linear form. Multiplication by that variable square identifies the kernel with Sym2 W tensor O(-2). The two independent first-order functionals give the rank-two quotient everywhere. Equivalently the gradient polarization has values in W O(3), and Euler's degree-four identity identifies its two components with the value and first derivative. This proves (7) globally and equivariantly. It is a fixed universal polynomial identity, not evaluation of a selected actual source polynomial or a selected point.

Twisting (7) by -14 yields

    0 -> A(-16) -> D(-14) -> W(-11) -> 0.             (8)

Moreover the nonzero left map in (8) is unique up to scale as a G-equivariant morphism. Indeed

    Hom_G(A(-16),D(-14))
      =Hom_G(A,D tensor Sym2 W),
    D tensor Sym2 W=Sym6 W+Sym4 W+Sym2 W.

The physical restriction Sym6 W=V_alt+P contains no A, and Sym4 W=D contains no A. Thus the displayed Hom has dimension one. Any nonzero equivariant map with these source and target types is a nonzero scalar multiple of the universal saturated map (8), and has exactly the quotient W(-11). This does not choose its scalar.

## 3. The backward kernel cannot have the nonzero graph

By (3)-(5), projection Q1->G6/U4=L10 induces an everywhere isomorphism

    Q1/U3 -> L10.                                      (9)

This follows from the actual sum Q1+U4=G6 and actual intersection Q1 intersect U4=U3, not merely from a generic intersection or an equal degree count. In particular Q1/U3 cannot be the U4/U3 axis: that would contradict the retained intersection Q1 intersect U4=U3. Use (9) to express Q1/U3 in (5) as a graph of an endomorphism between the two scalar O(-10) factors. Such an endomorphism is either zero or an isomorphism.

Suppose it is nonzero. Then the projection Q1->U4 from the actual splitting (4) restricts to the identity on U3 and is an isomorphism on the quotient by U3. It is therefore an everywhere equivariant isomorphism

    Q1 -> U4=D(-14).                                   (10)

Under (10), the actual inclusion U2=A(-16) into Q1 becomes a nonzero G-equivariant map to D(-14). By the unique-Hom statement in Section 2, its quotient must be W(-11). But the actual quotient in (3) is

    Q1/U2=O(-10)+O(-12),

which has different ordinary Birkhoff degrees from W(-11)=2O(-11). This contradiction excludes the nonzero graph.

The graph is therefore zero. Taking its actual inverse image in G6 proves

    Q1=U3 direct-sum L10.                              (11)

This is an equality of actual subbundles. It is not inferred merely from a zero abstract extension class, and no horizontal splitting is asserted.

## 4. The intrinsic first jets of L10 split the actual quotient

Because L10 subset Q1=F6^-, every local derivative of L10 lies in F6. Its intrinsic first-jet evaluation therefore defines a regular equivariant morphism

    j1:P^1(O(10))*=W(-9) -> F6.                        (12)

At this point (12) is not assumed injective, saturated, or generated by complete degree-ten coefficients. The displayed source type is the fixed principal-parts identity on P1. For order one, the dual principal-parts sequence is an extension of O(-8) by O(-10). Its transition off-diagonal is the logarithmic derivative of the degree-ten transition function, hence, up to the dualization sign, ten times the Euler extension class in H1(O(-2)), which is nonzero in characteristic zero. Its middle bundle is therefore W(-9). This is independent of the actual partial coefficient map.

Compose (12) with the actual quotient map F6->M=W(-9). The resulting morphism

    W(-9) -> W(-9)                                    (13)

is nonzero: on the zeroth-jet subline O(-10) of the source, (12) is the given inclusion L10->F6, whose projection to M is nonzero since L10 is disjoint from U4 in (4).

Every ordinary morphism between these equal-twist trivial multiplicity bundles is a constant linear map on W; equivariance and irreducibility give End_G(W)=C. Thus the nonzero map (13) is an everywhere isomorphism. It follows at once that (12) is an everywhere injective subbundle map, and its image Z is an actual splitting section of the quotient by U4:

    F6=U4 direct-sum Z, Z=W(-9).                       (14)

The intrinsic zeroth and first derivatives generate that image locally, so it is exactly the saturated first forward span L10^+. There is no separate completeness or normal-defect inference.

The splitting section is unique even ordinarily, since Hom(W(-9),D(-14))=0 by degree. The ordinary degrees of U4 and Z are respectively -14 and -9; hence Z is precisely the canonical highest-degree Harder-Narasimhan subbundle of F6. This supplies the claimed canonical meaning, rather than declaring an arbitrary Birkhoff complement canonical.

## 5. The coherent derivative blocks

Restrict the actual beta_(F6) to (14). On U4 its image is the full lower coherent O(-10) by (6), with kernel U3, because U4/U3=O(-10) and this actual quotient maps isomorphically onto that coherent line.

The lower component on Z=W(-9) vanishes by ordinary degree:

    Hom(W(-9),O(-10))=0.

The upper component on U4 is already zero by its exact lower-only image in (6). As the whole beta_(F6) surjects onto I6, the upper component on Z must therefore be onto the coherent O(-8). Its kernel has rank one and degree -10. It contains the actual L10 by (11); equality follows, or directly follows from the standard Euler quotient W(-9)/O(-10)=O(-8). Thus all four statements in (2) hold.

The ordinary ranks and degrees agree:

    rank F6=5+2=7, deg F6=5*(-14)+2*(-9)=-88,
    rank Q1=4+1=5, deg Q1=4*(-15)-10=-70,
    deg I6=-8-10=-18, deg F6-deg I6=-70.

These checks support the actual argument and are not substituted for it. Both nonzero derivative blocks can still lose fiber rank when embedded in their positive-degree normal saturations on D12. Coherent fullness onto O(-8) and O(-10) does not mean fullness onto O(4) and O(2).

## 6. Contribution and remaining problem

The new root-cause obstruction is the incompatible quotient of the unique equivariant A(-16) inside D(-14). It forces the actual scalar line into the backward kernel. The intrinsic first-jet map then splits the actual M quotient by a nonzero Schur endomorphism, rather than by assuming a connection-compatible or abstract Birkhoff splitting.

The resulting canonical embedded decomposition and its two coherent derivative blocks sharpen the residual simultaneous k=2 configuration. They do not exclude it, choose an actual instance, or assert realization. The stationary graph theorem, the complete degree-ten span theorem, higher original jets, and any parameter evaluation are not dependencies of this argument. The other rank-seven image, delta alternatives, e9, F18 alternatives, algebraicity and whole-profile questions remain outside its scope.
