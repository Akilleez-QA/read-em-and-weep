# A forced constant A excludes the source127 a-b-c-f edge

## Result and exact scope

The entire original source

    G3.11.cce6e3ba4eeb, source_index127,
    (1,1,1,0,0,1,0,0),
    E=D O(-2)+(Wp+T) O(-3)+V O(-4)+O(-8),
    A_q=O(-8)+O(2)+O(16),
    B_q=O(-18)+O(-4)+O(6), original defect zero

is impossible. This is a whole-source exclusion, not a whole-label exclusion or necessary-pair count. It does not concern the separate c-d-f abstract family.

The new step forces an actual constant A from the Euler character of the inverse image of the two positive Gauss summands. That A captures the saturated high quotient. An exact rank-two kernel calculation then gives a projected rank-fourteen bundle whose cohomology leaves three possibilities, all incompatible with this source's nonzero low D row or cubic block. A crucial equivariant extension calculation justifies separating it from the retained scalar O(-8).

No selected actual HM/source coefficients, parameters, points, derivatives, matrices, instance ranks, models, scans or large computation are used. All checks are fixed abstract characters and finite coefficient possibilities.

## 1. Immutable actual interface and the one source-specific input

The four original inputs are the actual-presentation note, strict-top theorem and two catalogs at commit db51525015bb7c5e825833d550d08dedf6f6ea96, under research/hm/order-four-quadratic-load in Akilleez-QA/read-em-and-weep. Their exact URLs and Git blob hashes are in audit-inputs/manifest.json. They give saturated full-span E in H O, with

    H=2A+2V+2P+2D, rank E=17, degree E=-54,
    H0(E)=0, H0(E^-(2))=0, Q=H O/E,
    E^+/E=O(-6)+O(4)+L, L=O(18) saturated in Q. (1)

The last equality uses the original defect-zero convention. Work over C with binary icosahedral G. Here W is its defining two-space; A=Sym2 W, S=Sym3 W, D=Sym4 W, T=Sym5 W; Wp,V,P are the other irreducibles of dimensions2,3,4. All are self-dual. There are no nontrivial line characters. Every nonempty invariant effective divisor has degree at least twelve.

The source-specific input is the public PR913 reduction at

    b84ea860de5ebe38cff3c54054e80dd4be5ac77c,
    research/hm/profile11-source127-abcf-reduction/PROOF.md,
    Git blob ac36f048fc0987a1c78fbd9a61bc18077963ce20.

https://github.com/Akilleez-QA/read-em-and-weep/blob/b84ea860de5ebe38cff3c54054e80dd4be5ac77c/research/hm/profile11-source127-abcf-reduction/PROOF.md

Its Sections2-4 prove that the low O(2) external derivative row of the canonical F=D O(-2) block is nonzero. We use precisely that conclusion, not its subsequent two-row kernel classification, and impose no assumption on the high row. Its high-only dependency is the public PR905 proof at 2db172b32dc014c06521a3fcba20261db5bb00fa, Git blob 3448047b9f67b258955f0fe53c3368b6f7615d9e. That proof is also included in the manifest to authenticate the full dependency chain.

This nonzero low-D input is essential. The same later residual bundle (V+P)(-4) need not be contradictory for another source whose original top D has zero low row; no conclusion is transferred to the genuine c-d-f abstract family.

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

In particular A captures the saturated high quotient, with no assumption about either high or low row of F used in this step.

## 3. The exact A kernel is W(-9), and the scalar summand survives

The onto sequence in (3) gives

    H0(N_A)=0,
    H1(N_A)=Sym18 W-A=V+2P+D.                 (4)

All its splitting degrees are negative. A rank-two equivariant splitting is either two scalar lines or a W/Wp coefficient at a single degree. Central parity and degree minus eighteen leave the scalar pairs

    O(-2)+O(-16), O(-4)+O(-14),
    O(-6)+O(-12), O(-8)+O(-10),               (5)

or W(-9), Wp(-9). The first three pairs fail (4): respectively they introduce a trivial constituent, an A constituent, or the character A+V+2D. Wp(-9) also introduces a trivial constituent. Both W(-9) and the final scalar pair have H1 character V+2P+D, but the scalar pair cannot inject into A O: its O(-8) summand has no map there, because A is absent from Sym8 W=P+D. Thus the actual kernel is uniquely

    N_A=W O(-9).                              (6)

Write R=Wp O(-3), T_src O(-3) for the original T block, and L_-=O(-8) for the original scalar summand. The original negative external row is supplied only by L_-, and its restriction is a nonzero scalar isomorphism: every other source degree is greater than minus eight. Differentiating N_A stays in the constant A, whose image modulo E is only the high L. Thus its negative external derivative is zero. This forces the original L_- component of N_A->E to vanish.

Define E_hat=F+R+T_src(-3)+V(-4), so E=E_hat direct-sum L_-. We have proved that N_A lies in E_hat as a coherent subbundle. Projection by constant A therefore gives an actual direct splitting

    E'=E/N_A=E0 direct-sum L_-,
    E0=E_hat/N_A, rank E0=14, degree E0=-28.    (7)

The image E' is saturated in (H/A) O, because A captures the saturated L in Q. Its direct summand E0 is therefore saturated in the same ambient constant bundle. No direct splitting is being inferred merely from Euler characters.

## 4. The standalone derivative of E0 requires an extension calculation

Since E_hat(4) is globally generated and E0 is its quotient, E0(4) is globally generated. Since E0 embeds in a constant bundle, all its splitting degrees are at most zero. Therefore every degree of E0 lies in

    [-4,0].                                   (8)

The derivative of E' in the projected ambient space has complete image O(2)+O(-8), with high O(16) removed by constant A. The E0 component has zero external O(-8) row, while its O(2) row is onto, since it retains the nonzero low row of F. The scalar L_- has no O(2) row because invariant degree10 is absent.

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

## 6. Each remaining bundle contradicts the actual low row

If C0=V+P, the original F=D(-2) has no map to E1=(V+P)(-4), by degree. Its projection in E0 would lie entirely in the constant C0, so its derivative would be zero. But its low O(2) row remains nonzero under both constant projections. This is impossible.

If C0=P, the original R=Wp(-3) remains injected after projection by A: any component of R toward constant A is zero, since A Sym3 W=W+S+T. Choose an equivariant constant complement of A to see this as an actual injection, not a rank assertion. Its map to constant P in E0 is also zero, since Wp Sym3 W=V+D has no P. Therefore R remains injected in E1. There it has no component in D(-2), because D W=S+T has no Wp, and no component in V(-4) by degree. It is consequently the entire equal-degree Wp(-3) summand. Its external row toward O(2) is zero because Wp is absent from Sym5 W=T; its internal derivative toward D(-4)+V(-6) is zero by degree. This gives a preserved saturated negative R, impossible.

Finally let C0=V, so E1=D(-2)+T(-3). The original F projects only to the D(-2) summand and maps nontrivially there because its low row survives. Its map is an isomorphism onto that summand. The nonzero row D(-2)->O(2) is complete quartic evaluation, with kernel S(-3).

The Hom space T(-3)->D(-2) is one-dimensional. Its nonzero universal Euler map has nonzero composite with D(-2)->O(2): otherwise it would factor through S(-3), but Hom_G(T,S)=0. Thus composition identifies this Hom space with the one-dimensional space T(-3)->O(2). There is therefore a unique equivariant triangular bundle change that removes the low row of the T(-3) summand. This is a structural row elimination; no coefficient or parameter value is selected or evaluated.

The resulting actual graph subbundle T(-3) has zero external derivative and no internal derivative toward the complementary D(-4), by degree. It is saturated and negative, so again cannot be preserved by the trivial connection. This excludes the final case of (14).

## Conclusion and boundary

All three possibilities (14) are impossible. Therefore the whole displayed a-b-c-f source is excluded, without assuming its high D row nonzero. The nonzero low-D input from PR913 is used exactly in the first and third cases of Section6; it cannot be omitted or extrapolated to other sources. This proof makes no whole-label or necessary-pair count claim and leaves the separate c-d-f abstract family untouched.
