# The exact c-d-f negative-pencil algebra and its full-module boundary

## Result and scope

Conditionally on an actual occurrence of the source127 c-d-f edge, its entire fixed-variable equivariant negative-pencil commutant is

    C times T(J), dimension J=1,

where T(J) is the two-vertex triangular scalar algebra with one arrow. Its full dimension is four, its Jacobson radical is one-dimensional and square-zero, its semisimple quotient is C^3, and its center is C^2. The units are a three-dimensional scalar torus acting on a one-dimensional additive shear.

These are exact conditional algebra statements, not a computed rank or commutant of a selected actual instance. Only the common scalar restriction can extend to a degree-zero endomorphism of the full actual HM cohomology module. Thus the quotient of this represented negative-pencil commutant by the scalar restriction image has dimension three. This is a quotient vector space, not an Ext group or algebra quotient.

No source is excluded. In particular scalar rigidity of the full module does not force every endomorphism of this smaller pencil to extend. The absent forced-lift premise is retained explicitly.

## 1. Exact source and dependency interface

All paths refer to Akilleez-QA/read-em-and-weep. The eight-input manifest records the exact immutable source URLs and Git blob hashes for the following dependency interface:

1. PR923, the source127 c-d-f lift-classification theorem at 91af637305fd0a76b4e68a889b2a2cb59f8f7067, research/hm/profile11-source127-cdf-lift-classification/PROOF.md, Git blob 6742093385b0aefc7b678151d90e7966bf4effa6. Its canonical-tower dependency is PR920 at 1528ff8ea56b21e03f7501a962bdaa6728a75904, research/hm/profile11-source127-cdf-normal-form/PROOF.md, Git blob 718b5245560a84568492874bab8d8c34730e8319. Both are included in the manifest.
2. PR862 at e103e25456897a1123f9636eb20080e8641ce66a, research/hm/profile11-degree28-pencil-algebra/PROOF.md, Section5 only: the general full-faithfulness theorem when H0(E)=0 and Q(-1) is globally generated. None of its degree-twenty-eight source-specific algebra types is imported.
3. PR790 at af0e03d26da5e47d18ae732291aca46f4d448dc5, research/hm/source2-first-constant-block/PROOF.md, Section6 only: simultaneous identification of the reconstructed pencils with both fixed actual multiplication tensors. No source2 splitting, rank or algebra is used.
4. The original actual-presentation, positive-double-hyperplane Gauss-gate, and uniform-twist-four-five hyperplane notes at db51525015bb7c5e825833d550d08dedf6f6ea96 under research/hm/order-four-quadratic-load. These authenticate the same actual maps and plane-section quotient used by the preceding universal bridge.
5. PR818 at f4a73af666900ad2cb34a756d24b88e19dd6feaa, research/hm/negative-truncation-extension/PROOF.md, Sections2-3: scalar degree-zero endomorphisms of the actual full module by its Euler relation, and its exact restriction-image boundary. Section5 gives the separate marked-submodule criterion recalled in the conclusion.

The classification gives, after a constant equivariant ambient identification over the fixed base,

    H=C10 direct-sum C11 direct-sum C9,
    C10=A+V+P, C11=Sym10 W=A+V+D, C9=Sym8 W=P+D,
    E=F direct-sum B direct-sum L,
    F=(P+D)(-2), B=U_6^10=(V+P)(-4), L=U_0^8=O(-8),
    0 -> F -> C10 O --q--> O(18) ->0.           (1)

The parameter of q belongs to Omega; no parameter is selected. Each source block spans its indicated constant space. The quotient is

    Q=O(18)+S O(7)+(Wp+T) O(1).                 (2)

Equation (2) is used solely to check the reconstruction hypothesis, not to make a new catalog or pair-count claim. In particular Q(-1) is globally generated, including its degree-zero summands, and H0(E)=0.

The other precise classification input is injectivity of the quartic restriction map

    R:Hom_G(C11,C10)->Hom_G(B,O(18)),
    R(w)=q w|B.                                 (3)

That theorem proves (3) is an isomorphism by the universal jet argument; equal dimensions alone would not justify its use here.

## 2. Every constant endomorphism, including singular ones

Let h be any constant G-equivariant endomorphism of H preserving E. No invertibility is assumed.

The source F of degree minus two has no map to B or L, of degrees minus four and minus eight. Thus h(F) is contained in F. Since F spans C10, h preserves C10 as a constant space. It induces an endomorphism of C10 O/F=O(18), which is a scalar a. Hence q h|C10=a q. The coefficient map C10->H0(O(18)) is injective because H0(F)=0, so

    h|C10=a identity.                            (4)

In the constant quotient H/C10, the degree-minus-four B has no map to L, so its image stays in B. Since B spans C11, the induced constant map preserves C11. It follows that the original constant blocks C10->C11, C10->C9, and C11->C9 all vanish.

An arbitrary constant endomorphism preserving a subbundle carries its actual negative Gauss kernel into itself. To see this without inverses, write the second fundamental form as the connection followed by projection to the quotient. A constant map commutes with the trivial connection, and the induced quotient map gives a commuting square of second fundamental forms. A vector in the kernel therefore maps into the kernel. This argument iterates through all actual saturated kernels, without inferring any equality of ranks.

Apply it to the induced endomorphism of C11 preserving B. The full actual negative-kernel flag terminates in the full degree-ten Veronese line O(-10). The induced endomorphism of that line is multiplication by a scalar b, possibly zero. Its full coefficient span is C11, so the constant endomorphism of C11 is b identity.

In the quotient by C10+C11, the projected L is the full degree-eight Veronese line in C9. The same coefficient-span argument gives the scalar d identity on C9, again allowing d=0.

There remains a possible block z:C9->C11. Its composite with L must lie in B, because h preserves E modulo C10. But

    Hom_G(O(-8),(V+P)(-4))
       =Hom_G(1,(V+P) tensor Sym4 W)=0,

since Sym4 W=D. Thus z|L=0, and full span of L forces z=0 as a constant map.

The block w11:C11->C10 must take B into F. Thus R(w11)=0, and injectivity (3) forces w11=0. The only possible off-diagonal block is

    w:C9->C10.

This Hom space is one-dimensional, the common P constituent. Every such w does preserve E: the composite

    L=O(-8) -> C9 O --w--> C10 O --q--> O(18)

is an invariant scalar form of degree26, and

    Sym26 W=A+2V+2P+2D

has no invariant. Therefore w(L) is contained in the actual kernel F. This uses exact kernel factorization, not a zero generic component promoted to an unproved bundle splitting.

We have exhausted all blocks and proved the exact description

    h(c,x,y)=(a c+w(y), b x, d y),
    a,b,d in C, w in J=Hom_G(C9,C10), dim J=1.   (5)

Conversely every map (5) preserves E by the same calculation. A nonzero w is a nonzero actual constant map, and cannot vanish on the whole L because L spans C9. Thus the radical arrow is genuine, not merely a character possibility.

## 3. Multiplication, radical and framing ambiguity

Using rightmost-first composition, (5) gives

    (a,b,d,w)(a',b',d',w')
      =(aa',bb',dd',a w'+d' w).                 (6)

The b factor is isolated, while w is an arrow from C9 to C10. Thus this is C times T(J), not an opposite-algebra claim. The ideal J has square zero and the quotient is C^3, so J is exactly the Jacobson radical. A central element has w=0 and a=d; b is independent. Hence the center is C^2.

A map is invertible exactly when a,b,d are nonzero. The scalar torus acts on J by a/d. In particular there is a nontrivial one-dimensional unipotent family preserving the embedded E even when its balanced parameter is fixed. The abstract parameter therefore does not specify a unique ambient frame. No moduli-scheme or family-level trivialization is inferred from this group calculation.

## 4. Simultaneous reconstruction of both actual negative pencils

The fixed actual maps are multiplication by the same negative variables,

    A_l:M2 -> M3, B_l:M3 -> M4, l in W,

with A_l injective, B_l surjective, and B_u A_v=B_v A_u. The original Gauss-gate and uniform-cohomology notes give the actual sequences

    0 -> M2 O(-1) --A--> M3 O -> D_lin ->0,
    Q=D_lin(1),
    H=ker(B_u,B_v)/im(A_v,-A_u),
    0 -> E -> H O -> Q ->0.                     (7)

These are actual maps, not independently chosen representation isomorphisms. PR790 Section6 proves the following natural reconstruction, with the single invariant determinant convention on W:

    N2=H0(Q(-2))=M2,
    N3=H0(Q(-1))=M3,
    N4=H1(E)=M4,
    A_rec,t(s)=t s,
    B_rec,t(u)=boundary(t u).                    (8)

For completeness, in arbitrary homogeneous symbols a,b and basis symbols u,v, the actual quotient sends [(x,y)] to [a y-b x]. If l=alpha u+beta v, its associated vanishing linear form is t_l=beta a-alpha b. The universal representatives in PR790 give A_rec,t_l=A_l; the actual boundary is the descended (B_u,B_v), giving B_rec,t_l=B_l. Both identities use the same original maps, so the identification is simultaneous and fixed-variable. No actual parameter or point is evaluated.

Define the entire equivariant fixed-variable pencil commutant

    C_N={ (e2,e3,e4) : e3 A_l=A_l e2,
                         e4 B_l=B_l e3 for all l in W }.

PR862 Section5 applies to (7), because H0(E)=0 and Q(-1) is globally generated by (2). Its natural evaluation and Koszul reconstruction recovers the exact quotient and constant H from any intertwining triple, including singular triples. Thus the correspondence with constant endomorphisms preserving E is fully faithful and covariant, respecting addition and composition. No degree-at-most-minus-two hypothesis on Q* is imported; its actual degree-minus-one summands are allowed.

Consequently (5)-(6) identify the entire represented commutant C_N with C times T(J). No source2 algebra dimensions, unrelated finite commutant-system sizes, or evaluated ranks have entered this conclusion.

## 5. The exact full-module boundary

Use the notation of PR818: S_coord=Sym(T_coord), and

    K_d=H1(End_0(F_HM)(d-1)),
    N2=K3^+, N3=K4^-, N4=K5^+.

The module K is generated in degree zero by a five-dimensional space dual to T_coord, with unique degree-one Euler relation epsilon. A degree-zero S_coord-linear endomorphism is determined by its generator map f0. Preservation of the line C epsilon forces

    (1 tensor f0) epsilon=c epsilon,

hence f0=c identity and, by generation, f=c identity on all K. This is PR818's actual Euler-relation theorem, not a simplicity assertion about the bundle F_HM and not a statement about a five-variable window alone.

Restriction therefore has the exact image

    res:End_(S_coord,G)^0(K) -> C_N,
    im(res)=C identity_N, ker(res)=0.             (9)

Every negative-pencil element lifts to such a full-module endomorphism if and only if it is the common scalar, and then its lift is unique. Define explicitly the quotient vector space

    Ob_full(N)=C_N/(C identity_N),
    ob_full(e)=[e].                              (10)

It has dimension three by (6), and ob_full(e)=0 is exactly the lifting criterion in (9). This notation does not identify (10) with an Ext group, an algebra quotient, or the rank of an evaluated compatibility matrix. The scalar line need not be a two-sided ideal.

Each nonzero element of J is square-zero and nonscalar, so does not lift. The three proper block projectors are likewise nonscalar and do not lift. These are failed extension routes, not contradictions to actual occurrence of the c-d-f source.

The logically different marked-subpencil extension problem requires additional actual action. For a negative subpencil U=(U2,U3,U4), PR818's universal criterion is

    q_+(Sym2(T_+) tensor U2) subset U4,
    q_+(pq tensor x)=m_p m_q x,                  (11)

where T_coord=T_+ direct-sum W. This condition is necessary and sufficient for extending the marked intersections as a graded S_coord-submodule, with no splitting projector asserted. The actual positive-quadratic action and relation embeddings are not determined by the constant Gauss classification. No value of q_+ is selected or computed here.

A new exclusion would require a separate theorem forcing a nontrivial full-module lift or forcing/forbidding a specific condition (11) under actual HM hypotheses. Neither the abstract classification nor (9) supplies that premise. The result therefore ends at a precise additional compatibility condition, not at a source or label exclusion.

## 6. A precise conditional positive-quadratic certificate

The actual covariant functor (8) gives block decompositions indexed by F,B,L. In N2 the characters are

    (V+P+2D), (A+V+2P+2D), 0;

in N4 the characters are

    (P+D), (V+2P+2D), (V+P).                    (12)

These follow directly from H0(Q(-2)) and H1(E), respectively. We do not replace N2 by an unmarked self-dual identification with H1(Q*), which would risk reversing the induced maps. The dimensions sum to the actual 41 and 37.

Let j be any nonzero radical shear, viewed through the exact covariant correspondence as a triple (j2,j3,j4). The induced quotient map goes from the scalar quotient block Q_L to the top Q_F. Since H0(Q_L(-2))=0, we have j2=0.

On E itself, the only nonzero block of j is a map L->F. It is nonzero because the original constant shear is nonzero on C9 and L spans C9. Its P(-2) component is the only possible one:

    Hom_G(O(-8),D(-2))=0,
    Hom_G(O(-8),P(-2)) is one-dimensional,

since Sym6 W=V+P. By Serre duality the induced H1 map is dual to the nonzero complete P coefficient injection P->H0(O(6))=V+P. Consequently j4 is a nonzero scalar multiple of

    rho: N4,L=V+P -> P subset N4,F=P+D,        (13)

and is zero on the other blocks. In particular its kernel on N4,L is precisely V. This is a universal consequence of the actual bundle map, not an evaluation of the fixed HM tensor.

For every e in C_N define the positive-quadratic commutator

    Theta_+(e)=e4 q_+-q_+(1 tensor e2).          (14)

It vanishes on the common scalar, so factors through the three-dimensional vector space Ob_full(N) of (10). No rank of this factored map is asserted. For the radical element,

    Theta_+(j)=j4 q_+,

so its vanishing is exactly the vanishing of the P component of the scalar-block part of q_+, in any chosen normal form. Intrinsically it is the condition that q_+ land in the common radical kernel on N4. The vanishing condition is independent of rescaling j and of the choice of normal-form coordinates.

The same formula describes diagonal constraints. For e=(a,b,d,0), the two N2 blocks carry a,b and the three N4 blocks carry a,b,d. If q_+,YX denotes the component from N2,X into N4,Y, equation (14) is

    (lambda_Y-lambda_X) q_+,YX,
    lambda_F=a, lambda_B=b, lambda_L=d.

The full e adds the radical term (13). This is an exact linear compatibility map on the represented four-dimensional algebra, or its three-dimensional scalar quotient; it is not a numerical substitute for any unperformed actual map calculation.

Finally let U=JN and Vker=Ann_J N be the radical-image and common-kernel subpencils. Their subpencil property follows from the commuting pencil equations. Since j2=0, U2=0 and (11) holds automatically for U. Thus the radical-image subpencil always extends to its minimal graded S_coord-submodule with the prescribed marked intersections. For Vker, Vker2=N2 and Vker4=ker j4, so (11) holds exactly when Theta_+(j)=0. The resulting nested pair of submodules exists exactly under this one conditional P-channel vanishing.

Neither that vanishing nor its failure is proved here. Even if it vanishes, the remaining positive/negative window squares and the lower Euler/full-module relations are separate conditions. In particular full-module scalar rigidity does not imply Theta_+(j) is nonzero. A positive-quadratic compatibility check is not a full-module lifting theorem, and this certificate supplies no source exclusion.

## 7. Corollary: the entire represented radical rank triple

The middle action also has a forced rank, proved without an actual-source evaluation. Twist (7) by O(-1). Since H O(-1) is acyclic, the connecting map gives a natural isomorphism

    N3=H0(Q(-1)) isomorphic to H1(E(-1)).       (15)

Its naturality identifies j3 with H1 of the same nonzero map L->P(-2) from Section6, twisted by O(-1). By Serre duality, the only nonzero component of the dual map is polynomial multiplication

    P tensor W -> Sym7 W,                      (16)

where P embeds nontrivially in Sym6 W through the degree-six coefficient map of L->P(-2). This embedding is injective because P is irreducible.

The kernel of the full multiplication

    Sym6 W tensor W -> Sym7 W

is Sym5 W=T, by the universal Clebsch-Gordan sequence. Since P tensor W=Wp+T and Wp is absent from that kernel, (16) is nonzero on its Wp summand. Naturality and duality therefore show that j3 has a nonzero Wp channel.

Its T channel is nonzero as well. For every nonzero negative variable l, the actual map B_l is surjective and the commutant equation gives

    B_l(im j3)=im(j4 B_l)=im j4.

The latter has dimension four by (13). If j3 had only its Wp channel, its image would have dimension two and could not map onto this four-space. The domain block of j3 is precisely N3,L=Wp+T, so both irreducible summands map nontrivially and their images have total dimension eight. Hence every nonzero radical element has the universal rank triple

    (rank j2, rank j3, rank j4)=(0,8,4).        (17)

Because J is one-dimensional, its joint images and common kernels are those of any nonzero j. The actual spaces have dimensions (41,54,37), giving

    dim JN=(0,8,4),
    dim Ann_J N=(41,46,33).                    (18)

No parameter, point, derivative value or actual matrix was chosen to obtain these dimensions. Equations (17)-(18) sharpen the necessary represented filtration, while the conditional q_+ and full-module boundaries in Sections5-6 remain unchanged.
