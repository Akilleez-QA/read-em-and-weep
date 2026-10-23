# A canonical constant tower for the surviving source127 c-d-f edge

## Result and boundary

Consider any actual saturated full-span inclusion with the original data

    G3.11.cce6e3ba4eeb, source_index127,
    (0,0,1,1,0,1,0,0), original defect zero,
    E=F direct-sum B_src direct-sum L_-,
    F=(P+D) O(-2), B_src=(V+P) O(-4), L_-=O(-8),
    A_q=O(-8)+O(2)+O(16), B_q=O(-18)+O(-4)+O(6).

There is a canonical actual constant tower A subset C10 subset H, with

    C10=A+V+P, E intersect C10 O=F,
    0 -> F -> C10 O -> O(18) ->0.

The last quotient is a member of the balanced open family Omega from PR876, without selecting its parameter. Projection by C10 gives an actual constant decomposition

    H/C10 = C11 direct-sum C9,
    C11 isomorphic to Sym10 W, C9 isomorphic to Sym8 W,
    E/F = U_6^10 direct-sum U_0^8,

where both inclusions are the standard universal osculating inclusions in their respective constant summands. Every image used to obtain this statement is proved saturated; the complete negative-kernel flag reconstructs the U_6^10 block.

This is a necessary normal form, not an exclusion, a realization in actual HM, or a proof that all permitted lifts belong to PR876's one-parameter family. Off-diagonal lifts across C10 are retained explicitly in Section9. No selected actual source coefficient, parameter, point, derivative, matrix, instance rank, scan or large computation is used.

## 1. Immutable actual interface

The four original inputs are the actual-presentation note, strict-top theorem and two catalogs at commit db51525015bb7c5e825833d550d08dedf6f6ea96, under research/hm/order-four-quadratic-load in Akilleez-QA/read-em-and-weep. Their immutable URLs and Git blob hashes are in audit-inputs/manifest.json. They give a saturated full-span E in H O, with

    H=2A+2V+2P+2D, rank E=17, degree E=-54,
    H0(E)=0, H0(E^-(2))=0, Q=H O/E,
    E^+/E=O(-6)+O(4)+L, L=O(18) saturated in Q. (1)

The last equality uses the original defect-zero convention. Work over C with binary icosahedral G. Here W is its defining two-space; A=Sym2 W, S=Sym3 W, D=Sym4 W, T=Sym5 W; Wp,V,P are the other irreducibles of dimensions2,3,4. All are self-dual. There are no nontrivial line characters. Every nonempty invariant effective divisor has degree at least twelve. We write U_k^n=Sym^k W O(k-n) for the universal k-th osculating subbundle of the degree-n Veronese line in Sym^n W O.

The independently published compatibility family is PR876 at

    7c7f25911ae1df3590c2b4ffe541c21bae9b1574,
    research/hm/profile11-source127-cdf-open-family/PROOF.md,
    Git blob 659a90911244172b222f366d8b7dea9b88e88814.

https://github.com/Akilleez-QA/read-em-and-weep/blob/7c7f25911ae1df3590c2b4ffe541c21bae9b1574/research/hm/profile11-source127-cdf-open-family/PROOF.md

We use its exact definition and nonemptiness proof of Omega in Section9, not an assumption that this family exhausts actual inclusions. The forced-A, quotient and reconstruction arguments below are self-contained.

## 2. The positive Gauss preimage forces an actual constant A

Let E_pos be the inverse image in H O of the positive Harder-Narasimhan part O(4)+L of the actual quotient (1). It is a saturated subbundle, with

    0 -> E -> E_pos -> O(4)+L ->0.

The displayed source splitting gives

    chi_G(E)=-2V-4P-3D,
    chi_G(E_pos)=A-V-2P-D.                    (2)

The coefficient of A in (2) is positive. Since H0 and H1 are genuine representations, H0(E_pos) contains an A. Its sections are actual constant vectors in H, because E_pos is a subbundle of H O. Moreover, this A-isotypical component has multiplicity exactly one: it maps only to H0(L), since Hom_G(A O,O(4))=0; its kernel would lie in H0(E)=0; and the A multiplicity of H0(L)=Sym18 W is one. Thus we obtain a canonical actual constant subspace A O contained in E_pos, with a nonzero map to L.

That map is onto everywhere. Its three independent degree-eighteen coefficients bound any common divisor by sixteen. Only invariant degree twelve could occur in that range: odd degrees are excluded by the center, and Sym14 and Sym16 have no invariant. Removing a degree-twelve factor would require A in Sym6 W=V+P, absent. Consequently

    A O -> L=O(18) is onto,
    N_A=E intersect A O has rank2, degree-18.  (3)

In particular A captures the saturated high quotient, without any assumption about the rows of the original top block.

## 3. The exact A kernel is W(-9), and the scalar summand survives

The onto sequence in (3) gives

    H0(N_A)=0,
    H1(N_A)=Sym18 W-A=V+2P+D.                 (4)

All its splitting degrees are negative. A rank-two equivariant splitting is either two scalar lines or a W/Wp coefficient at a single degree. Central parity and degree minus eighteen leave the scalar pairs

    O(-2)+O(-16), O(-4)+O(-14),
    O(-6)+O(-12), O(-8)+O(-10),               (5)

or W(-9), Wp(-9). The first three pairs fail (4): respectively they introduce a trivial constituent, an A constituent, or the character A+V+2D. Wp(-9) also introduces a trivial constituent. Both W(-9) and the final scalar pair have H1 character V+2P+D, but the scalar pair cannot inject into A O: its O(-8) summand has no map there, because A is absent from Sym8 W=P+D. Thus the actual kernel is uniquely

    N_A=W O(-9).                              (6)

Write F=(P+D) O(-2), B_src=(V+P) O(-4), and L_-=O(-8) for the three original source blocks. The original negative external row is supplied only by L_-, and its restriction is a nonzero scalar isomorphism: every other source degree is greater than minus eight. Differentiating N_A stays in the constant A, whose image modulo E is only the high L. Thus its negative external derivative is zero. This forces the original L_- component of N_A->E to vanish.

Define E_hat=F direct-sum B_src, so E=E_hat direct-sum L_-. We have proved that N_A lies in E_hat as a coherent subbundle. Projection by constant A therefore gives an actual direct splitting

    E'=E/N_A=E0 direct-sum L_-,
    E0=E_hat/N_A, rank E0=14, degree E0=-28.    (7)

The image E' is saturated in (H/A) O, because A captures the saturated L in Q. Its direct summand E0 is therefore saturated in the same ambient constant bundle. No direct splitting is being inferred merely from Euler characters.

## 4. The standalone derivative of E0 requires an extension calculation

Since E_hat(4) is globally generated and E0 is its quotient, E0(4) is globally generated. Since E0 embeds in a constant bundle, all its splitting degrees are at most zero. Therefore every degree of E0 lies in

    [-4,0].                                   (8)

The derivative of E' in the projected ambient space has complete image O(2)+O(-8), with high O(16) removed by constant A. The E0 component has zero external O(-8) row, while its O(2) row is onto: the entire projected external image contains that saturated line, and the scalar L_- has no O(2) row because invariant degree10 is absent. This does not assume any nonzero low row of F.

This external statement alone does not justify ignoring a possible internal derivative toward L_-. Put H'=H/A, Q0=H' O/E0, and Q'=H' O/E'. The preimage Z of the actual low O(2) line in Q'(-2) is an equivariant extension

    0 -> O(-10) -> Z -> O(2) ->0.              (9)

It splits uniquely. Indeed equivariant extensions are the invariant part of ordinary extensions in characteristic zero, and

    Ext^1_G(O(2),O(-10))
       =H1(O(-12))^G=(Sym10 W)^G=0,
    Hom(O(2),O(-10))=0.

Here Sym10 W=A+V+D. The actual derivative E0->Q0(-2) lands in Z. Under the unique splitting (9), its O(-10) component is a regular sheaf map from E0, and vanishes by (8). Thus its complete standalone derivative image is exactly the O(2) summand. It is saturated in Q0(-2): its quotient inside Z is O(-10), while the outer quotient is locally free because the low row is saturated in Q'(-2).

We have therefore proved, rather than assumed,

    E0 has the single actual derivative quotient O(2). (10)

## 5. Exact cohomology leaves only three negative bundles

The exact kernel (6) has

    H1(N_A(1))=Wp+2T.

Applying cohomology to 0->N_A->E_hat->E0->0 gives

    chi_G(E0)=-P-2D,
    chi_G(E0(1))=0,
    chi_G(E0(2))=P+2D,
    H0(E0(1)) injects into Wp+2T.              (11)

The injection uses H0(E_hat(1))=0.

By (8) write the equivariant splitting as

    E0=C0 O+C1 O(-1)+C2 O(-2)+C3 O(-3)+C4 O(-4).

C0 is an actual constant subspace. The H0 budget in (11) says C0 W+C1 is a subrepresentation of Wp+2T. The even irreducible products

    1 W=W, A W=W+S, V W=T,
    P W=Wp+T, D W=S+T

show that C0 uses only V,P and C1 only Wp,T. The subbundle C0 O+C1 O(-1) has zero external derivative by (10), since Wp,T are absent from Sym3 W=S. Its internal derivative toward the degree-at-most-minus-two complement, twisted by -2, vanishes by degree. Thus this entire saturated subbundle is preserved by the trivial connection. A preserved saturated subbundle of a constant bundle is constant in characteristic zero, so its degree is zero. Hence C1=0.

Quotient by the actual constant C0 and let E1=E0/C0. It is a saturated negative subbundle of a constant quotient, still with the single derivative quotient O(2). Its degree-minus-two coefficient must inject into H0(O(4))=D. Otherwise a nonzero coefficient-kernel subbundle U(-2) would have zero external derivative and no internal map toward the remaining degrees, all at most minus two before twisting by -2. It would be a forbidden preserved negative subbundle. Consequently

    C2=0 or D.                                (12)

Write C0=pV+qP. The H0 budget permits exactly

    (p,q)=(0,0),(1,0),(2,0),(0,1),(1,1).

Equation chi(E0(1))=0 now gives C3+C4 W=C0 W. It forces C4=uV+vP, because the other even irreducibles introduce W or S. Using V A=P+D and P A=V+P+D, the remaining Euler equation becomes

    C2=P+2D-C0 A+C4
       =(1-p-q+v)P+(2-p-q)D+(u-q)V.           (13)

Conditions (12) force u=q and v=p+q-1. Of the five possibilities for C0, the zero case has v=-1, and the 2V case would give C3=T-Wp, not genuine. The complete remaining list is

    C0=V:   E1=D(-2)+T(-3);
    C0=P:   E1=D(-2)+Wp(-3)+V(-4);
    C0=V+P: E1=(V+P)(-4).                     (14)

No extension splitting was used to obtain the constant quotient E1; C0 is its actual space of constant sections.

## 6. The original top P forces the third residual alternative

The original P(-2) direct summand in F remains injected after projection by A. Indeed

    Hom_G(P(-2),A O)=0,

since A tensor Sym2 W=1+A+D contains no P. Choose an equivariant constant complement to A in H; the component of the original P(-2) into A is zero, so its projection into E0 is an actual sheaf injection.

In either of the first two alternatives in (14), this P(-2) has zero map to E1: there is no equal-degree map to D(-2), and every other target has strictly lower degree. Hence it would inject into C0 O. For C0=V, its rank four exceeds the target rank three. For C0=P, a rank-four injection P(-2)->P O would have a nonzero determinant, an invariant scalar form of degree eight. The determinant characters are trivial, and no such invariant exists. Thus both alternatives are impossible. Necessarily

    C0=V+P, E1=(V+P) O(-4).                    (15)

This uses the actual injected P, not a nonexistent nonzero low row of the top D. In fact that low row will be forced zero.

The whole F=(P+D)(-2) has zero map to E1 by degree, so its image in E0 lies in C0 O. The kernel has rank at least two, and is contained in N_A, whose rank is two. Because F is a saturated direct summand of E_hat, this generic containment implies N_A subset F as coherent sheaves: the induced N_A->E_hat/F vanishes generically and has torsion-free target. Moreover N_A is saturated in F, since it is saturated in E_hat. Therefore

    F/N_A -> C0 O

is an actual rank-seven degree-zero injection and hence an isomorphism. Quotienting E_hat=F direct-sum B_src gives the actual direct sum E0=(F/N_A) direct-sum B_src. Its first summand is exactly the constant C0, so E1 is the actual projection of the original B_src, not just a bundle with its character.

Let C10 be the inverse image of the constant C0 under H->H/A. Then C10 is an actual constant representation A+V+P, with

    E intersect C10 O=F,
    C10 O/F=L=O(18).                            (16)

For the second statement, every vector of C10 differs from a section of E by a vector of A, so its image in Q is exactly the saturated high L captured by A. Thus (16) is an exact sequence of bundles. The original F differentiates only into that high quotient; its low and negative external rows are zero.

The constants A and C0 were respectively the unique A-isotypical space in H0(E_pos) and H0(E0). Consequently the tower A subset C10 subset H is canonical for the given inclusion.

## 7. Reconstructing the actual residual osculating bundle

Project by C10. We obtain a saturated full-span inclusion

    E''=B direct-sum L_- subset H'' O,
    B=(V+P) O(-4), H''=H/C10=A+V+P+2D.

By the actual construction of E1 in Section5, B is saturated in H'' O and has the single saturated standalone derivative image O(2). This assertion includes the unique pullback splitting in Section4; it is not inferred merely from the external row of E''.

Both irreducible components of B->O(2) are nonzero. If U=V or P had zero component, U(-4) would have zero external derivative. Its internal derivative into the complementary degree-minus-four summand, twisted by minus two, is zero by degree. It would be a preserved negative subbundle of a constant bundle, impossible. Since Sym6 W=V+P, the coefficient map is therefore an isomorphism with the complete degree-six system, up to an equivariant coefficient isomorphism. The actual kernel is

    K5=T O(-5),
    0 -> K5 -> B -> O(2) ->0.                  (17)

The kernel is saturated in B and hence in H'' O.

We now reconstruct every lower kernel and every reverse first span. For K5, differentiation lands inside B(-2), because it is the actual kernel of B's second fundamental form. Its derivative modulo K5(-2) consequently has target (B/K5)(-2)=O. It cannot vanish: otherwise K5 would be preserved by the constant connection. The nonzero equivariant map T(-5)->O is the complete degree-five evaluation, so it is onto and has kernel D(-6). Repeating exactly this argument gives the following list. Each row is the actual derivative map of the bundle in its first column, and the displayed target is the quotient in the preceding row twisted by minus two:

    bundle          derivative target    actual kernel
    B=(V+P)(-4)     O(2)                 T(-5)
    T(-5)           O                    D(-6)
    D(-6)           O(-2)                S(-7)
    S(-7)           O(-4)                A(-8)
    A(-8)           O(-6)                W(-9)
    W(-9)           O(-8)                O(-10).

At each step, zero derivative would make that whole negative bundle preserved. The nonzero map is the complete evaluation of Sym^j W for j=5,4,3,2,1, respectively; the relevant Hom space has dimension one. Its standard Euler kernel is the next listed bundle. Hence every map is onto everywhere, every kernel is saturated in its predecessor and in H'' O, and no defect divisor has been dropped.

Let ell=O(-10) be the final kernel. Its derivative lands in W(-9)(-2), and modulo ell(-2) has target (W(-9)/ell)(-2)=O(-10). It is nonzero for the same preserved-line reason, and thus is an isomorphism. The raw first span of ell is exactly W(-9). Similarly each of the previous surjections identifies the next raw first span with the preceding bundle in the list. In particular B is the raw sixth span of ell, and B^+ is its raw seventh span. The latter is saturated and sits in the exact sequence

    0 -> B -> B^+ -> O(4) ->0,
    rank B^+=8, degree B^+=-24.                (18)

Saturation in (18) follows from the saturated standalone derivative image O(2), not from generic rank alone.

The coefficient span C11 of ell is a quotient representation of Sym10 W=A+V+D. All its raw polars, including B^+, lie in C11 O. Every proper quotient of this multiplicity-free representation has dimension at most eight. A dimension-eight quotient is also impossible: it would contain the rank-eight saturated B^+, hence equal B^+ as a bundle, contrary to degree minus twenty-four. Thus the coefficient map from Sym10 W is injective and

    C11 isomorphic to Sym10 W, dimension11.

Under this coefficient isomorphism, ell is the full degree-ten Veronese line. Its reconstructed polar flag proves the actual equality

    B=U_6^10 subset C11 O.                     (19)

This proves both the full constant span and all intermediate ranks and saturation claims; it does not extrapolate them from the first Gauss increment.

## 8. Full span separates the scalar constant space

Let C9 be the actual coefficient span of the projected L_-=O(-8) in H''. It is a quotient of Sym8 W=P+D, so dimension C9 is at most nine. By full span of E'',

    C11+C9=H'', dimension H''=20.

Since dimension C11=11, equality forces dimension C9=9 and C11 intersect C9=0. Thus the actual constant quotient decomposes as

    H''=C11 direct-sum C9,
    C9 isomorphic to Sym8 W,
    E''=U_6^10 direct-sum U_0^8.              (20)

The scalar coefficient map is an isomorphism onto its full Sym8 coefficient space, so its line inclusion is the standard degree-eight Veronese inclusion. Its polar images are saturated by the universal Euler sequence. This conclusion uses full span, not a presumed splitting of the projected scalar plane. The source direct sum was already an actual quotient splitting before the dimension argument.

## 9. The balanced high parameter and retained off-diagonal lifts

The coefficient map q:C10->H0(O(18)) is injective, since H0(F)=0. The source C10=A+V+P contains the unique A and V in Sym18 W=A+V+2P+D and one line in its two-dimensional P multiplicity space. Up to the nonzero constant scalings of the irreducible source summands, q is therefore described by a parameter

    p in P(Hom_G(P,Sym18 W))=P1.

No parameter is selected. Twisting (16) by one and using F(1)=(P+D)(-1) gives that the exact multiplication map

    C10 W -> Sym19 W

is an isomorphism. Hence p belongs to precisely the balanced open set Omega of PR876, Sections2-3, defined by the two nonzero linear channel conditions there. Conversely that published argument proves Omega is nonempty; our deduction is a necessary condition on the actual top quotient, not an existence claim about actual HM.

The top F has no raw derivative defect. Its raw first span in C10 is generated after twisting by one, because it is the first-polar image of the quadratic inclusion F. It has generic rank ten: a nonconstant hyperplane curve has nonzero derivative, and a zero derivative would make the negative F preserved. If Delta is the defect divisor in C10, generation after twist one and containment in a constant bundle give degree Delta at most ten. Equivariance and the minimum invariant divisor degree twelve force Delta=0. Thus the standalone derivative of F is onto O(16), as in the published balanced family.

Finally choose any equivariant constant splitting H=C10 direct-sum H''; semisimplicity permits this, but makes no claim that the original source splits across these constant spaces. The original inclusions of B_src and L_- then have the form

    b -> (u(b), i_6(b), 0),
    l -> (v(l), 0, i_0(l)),

where i_6 and i_0 are the standard inclusions in (20), and

    u in Hom_G((V+P)(-4),C10 O),
    v in Hom_G(O(-8),C10 O).

These are retained arbitrary regular off-diagonal bundle maps subject to whatever further actual-source conditions hold. They have not been set to zero, evaluated, or proved removable. Changing a lift by a map into F does not change the generated bundle, and changing the constant splitting changes u,v by corresponding constant-complement terms. The normal form asserts no classification of the resulting equivalence classes or of the extra profile constraints on them.

The case u=v=0 is exactly the architecture of PR876's abstract family, so the normal form is compatible with its nonemptiness. Deciding which lifted inclusions can be the fixed actual HM inclusion remains open. No whole-source or stable-label decrement follows from this theorem.
