# Independent whole-proof review: source127 a-b-c-f exclusion

## Verdict and exact reviewed version

**PASS.** The frozen proof establishes a whole-source exclusion of the exact a-b-c-f source specified below, conditional only on the stated original actual interface and the authenticated source-specific low-D lemma. I find no missing internal derivative channel, saturation gap, unproved splitting of a nonconstant connection, or transfer of a conclusion from another source. In particular, the actual-target pullback in Section 4 is sufficient and necessary for the argument as written; merely checking the derivative on a kernel would not suffice.

This review applies to these exact bytes:

- `PROOF.md`, SHA256 `c602fc27d75db4f386d00e8a65ced14888fc5f463f516b76e1c54f9306a909cc`.
- `verify.py`, SHA256 `416c76ff2422524d26c1b5ca4b6938c0deb8e089a951155e229471add936af79`.

I read the complete proof, verifier, reproduction note, both original mathematical notes, public PR905 proof, and public PR913 proof. I read and parsed both complete catalog files and inspected their exact source127 and stable-label records; their unrelated support records and aggregate counts are not mathematical premises of this exclusion. All six input Git blob hashes match the manifest. I ran the frozen verifier successfully. In addition, I independently recomputed the small representation identities using the affine-E8 McKay adjacency recurrence, rather than the verifier's character-table implementation. The geometric and sheaf-theoretic checks below are independent of the verifier.

The reviewer did not change the proof or verifier. Before final review binding, the author corrected exactly one notation typo in Section4: the removed high derivative row is O(16), not O(12). Reversing precisely that textual correction reproduces the original SHA256 f9ff16f3bc4b2eeb15df72e6509baa7a22b298140a2e1520b5eabc3f13b7c321; the current corrected bytes have the PROOF.md hash above. I confirm the corrected value, the exact corrected bytes, and the unchanged verifier. This review does not publish anything, change catalogs, or assert a revised count.

## 1. Authenticated inputs and dependency boundary

The six inputs authenticate as follows:

| Input | Git blob | SHA256 of source bytes |
|---|---|---|
| ACTUAL.md | b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3 | a52685fc9e7c89abf26171a15989cedeaf3bd101a2edde790a24f9cfe0179256 |
| STRICT-TOP.md | d7506dae49b4be43230450c4132bd5db91f137ef | 53ff5daf7e656bb1ec2dcf5feebd2813e2dbfbd6489a3a65117960f492b4cc08 |
| pairs.json | fe0afa410d89340d3082dc814277f89fbb582c19 | 6002ad138a41d98c351130a29703722979f31b8da90d7c75a120f28bf89480eb |
| frontier.json | 8b5971092f9ef762584912609fd5e9301c4e271d | a6fc9ec680d1866782e0233c234c5d80d398e9fc77734b59e61040ffc92021ad |
| HIGH-D-KERNEL.md | 3448047b9f67b258955f0fe53c3368b6f7615d9e | a886ede0c620726e422df8b897cdfaaa35da6d3698fb2130fa4d90d517c5e72d |
| D-REDUCTION.md | ac36f048fc0987a1c78fbd9a61bc18077963ce20 | 0131265788f518421265bb94ffd8d3f78f2e60753ac3fc515c6810c9b69803de |

The four original inputs are pinned to commit `db51525015bb7c5e825833d550d08dedf6f6ea96`. PR905 is pinned to `2db172b32dc014c06521a3fcba20261db5bb00fa`; PR913 is pinned to `b84ea860de5ebe38cff3c54054e80dd4be5ac77c`. The manifest supplies immutable source URLs and paths.

The pair catalog's row127 has original defect zero, A degrees `[-8,2,16]`, B degrees `[-18,-4,6]`, and includes the tuple `(1,1,1,0,0,1,0,0)` among its compatible E types. The frontier record `G3.11.cce6e3ba4eeb` has profile11, source_index127, the same A and B, and original_defect0. The tuple gives

    E = D(-2) + Wp(-3) + T(-3) + V(-4) + O(-8).

Its rank is 5+2+6+3+1=17 and degree is -10-6-18-12-8=-54. The actual-presentation note supplies the negative splitting and H0(E(1))=0, hence H0(E)=0. Strict-top supplies H0(E^-(2))=0, with its actual constant-connection justification, not a dimension-only replacement.

For a hypothetical actual occurrence of this catalog source, the original defect-zero convention identifies the actual derivative image with

    I = O(-8) + O(2) + O(16) inside Q(-2),
    Q = H O/E,

and identifies its untwist with the saturated subbundle

    E^+/E = O(-6) + O(4) + L,  L=O(18),

of Q. Saturation and defect zero are essential inherited hypotheses; they are not inferred from the catalog merely recording a compatible abstract bundle. The displayed ambient character H=2A+2V+2P+2D is consistent with the setup, but no step of the new exclusion requires a special placement or evaluation of its coefficient copies.

The only newer source-specific conclusion used is PR913 Sections2-4: the actual low O(2) row on the canonical top block F=D(-2) is nonzero. Nothing in the new proof requires the high D row to be nonzero. PR913's later two-row classification and zero-high-row identification are not premises.

### Audit of the source-specific lemma, including its PR905 interface

PR905 Sections2-3 give a universal conditional statement about a nonzero high-only D(-2) row: it is basepoint-free and its kernel is

    K = O(-6) + Wp(-5) + O(-10).

The absence of D in Sym6 eliminates a degree12 common factor. The five independent degree18 coefficient sections bound a common divisor by14; the invariant-degree restrictions eliminate the other possibilities. The kernel calculation uses rank4, degree-26, H0(K(2))=0, H1(K(2))=A+V+2P, and chi(K(3))=-W-Wp-T. The six possible negative atoms listed there are exhaustive under rank, central parity and cohomology support. The negative T and W force O(-10) and O(-6); the remaining P forces Wp(-5), exhausting rank4. This part does not depend on PR905's second top D block or its whole-source conclusion.

Assuming the low row zero in the present source, strict-top forces a nonzero high row, so this conditional statement applies. PR913 correctly retains both internal channels from O(-10): one into T(-5), and one into the original scalar O(-10). The full image of this term is a saturated line whenever nonzero, including when both channels occur. The other nonzero possible internal image is the equal-degree Wp(-5) row. The complete image alternatives therefore give exactly a constant first span (A+P) O or A O+T_lin(-1), after the positive-degree possibilities are excluded.

The actual identity (E intersect M)/F=J(2) follows by taking the preimage of the internal derivative image; it is not merely an equality of characters. Thus the scalar O(-8) image is an actual line S0 in T_src(-3)+O(-8). A nonzero scalar component would make S0 a graph over the original scalar summand. Removing that graph leaves a bundle, or in the linear case an extension of bundles, all having zero Hom to the required negative O(-8) derivative row. This contradiction uses exactness of Hom for the extension, not an unproved splitting. Hence the scalar component vanishes.

The remaining T-only S0 is the complete quintic Euler inclusion O(-8) into T_src(-3), with quotient D(-2). In the constant-first-span branch the original Wp cubic block is trapped horizontally. In the linear branch the projected top D lies in T_lin(-1); its derivative kernel forces the latter's constant span to be V+P. The original Wp cubic's coefficient span is then exactly V, since Wp Sym3=V+D. Its external derivative is zero after high capture, and its internal derivative to the quotient has target degrees too low. Its saturated first span V O would lie in T_lin(-1), a contradiction. The original Wp block is indeed contained in the relevant first span: the displayed actual preimage identity contains the whole original Wp summand, not just an abstract isomorphic quotient.

This audits the precise source-specific low-D conclusion needed here. It neither imports PR905's other-source conclusion nor assumes that a generic source has the same low-D behavior.

## 2. Independent reconstruction of the forced constant A

Let Bplus denote the canonical positive slope subbundle O(4)+L of the actual E^+/E. Its inverse image Epos in H O is a subbundle: Q/Bplus is locally free because Bplus is saturated in E^+/E and E^+/E is saturated in Q. Consequently

    0 -> E -> Epos -> Bplus -> 0

is an actual exact sequence of bundles.

The equivariant Euler calculation is

    chi(E) = -2V-4P-3D,
    chi(Bplus) = D + (A+V+2P+D),
    chi(Epos) = A-V-2P-D.

Thus the A multiplicity in H0(Epos) is at least one. This is valid without any H1 vanishing: H1 is a genuine representation. Every section of Epos is an actual constant vector of H because Epos is included in H O.

The multiplicity is exactly one. The map H0(Epos)->H0(Bplus) is injective because H0(E)=0; the A multiplicity in H0(Bplus) is one, lying entirely in H0(L)=Sym18. More intrinsically, the map from the A-isotypical constant subbundle to Bplus/L=O(4) is zero because A is absent from Sym4=D. Hence its image lands in the actual canonical high line L, without selecting a horizontal splitting of Epos. This constructs one uniquely determined A-isotypical constant subspace, with a nonzero map

    A O -> L=O(18).

That nonzero irreducible coefficient map has three independent sections. A common divisor therefore has degree at most16. It is G-invariant; because G has no nontrivial characters, it corresponds to an invariant scalar form, not merely a potentially nontrivial semi-invariant. The minimum positive invariant-divisor degree is12. Central parity excludes odd degrees, and Sym14 and Sym16 have no invariant. A degree12 factor would leave an A covariant of degree6, impossible because Sym6=V+P. Thus the map is onto at every point.

It follows that N_A=E intersect A O is the actual rank2, degree-18 kernel. Moreover, A captures exactly the saturated high L. This step is global and does not use either D row.

## 3. The A kernel and coherent separation of the scalar summand

Since H0(N_A)=0, every ordinary splitting degree of N_A is negative. Equivariant splitting, central parity, absence of nontrivial line characters, and rank2/degree-18 leave exactly four scalar pairs and the two irreducible two-space options. Their H1 characters are:

| Kernel candidate | H1 character |
|---|---|
| O(-2)+O(-16) | 1+A+V+P+D |
| O(-4)+O(-14) | 1+2A+P+D |
| O(-6)+O(-12) | A+V+2D |
| O(-8)+O(-10) | V+2P+D |
| W(-9) | V+2P+D |
| Wp(-9) | 1+A+V+P+D |

The exact onto sequence requires H1(N_A)=Sym18-A=V+2P+D. Only O(-8)+O(-10) and W(-9) match. The scalar pair cannot inject into A O, since Hom_G(O(-8),A O)=0: Sym8=P+D contains no A. Therefore

    N_A = W(-9)

as an equivariant bundle. This uses the actual embedding, not only cohomology.

The original negative derivative row E->O(-8) is supplied solely by the original scalar L_-=O(-8): all other source degrees are greater than -8. Its scalar restriction is nonzero, and hence an isomorphism, because the actual full derivative image includes the negative row. For any section of N_A, differentiation stays in the actual constant A. Modulo E, that constant A has image solely in the high L. Thus the negative derivative row vanishes on N_A, forcing the component N_A->L_- to vanish.

Consequently N_A lies in the actual direct summand

    Ehat = D(-2)+Wp(-3)+T(-3)+V(-4).

After projection by the constant A,

    E' = E/N_A = E0 direct-sum L_-,
    E0 = Ehat/N_A,
    rank E0=14, degree E0=-28.

These are coherent quotient identifications. N_A is saturated in E as the kernel of projection to H/A; hence its quotient in Ehat is locally free. Also

    (H/A) O/E' = Q/L

is locally free, because L was saturated in Q. Therefore E' is saturated in the projected constant ambient bundle. Since E0 is a direct summand of E', E0 is saturated there as well.

Finally Ehat(4) is globally generated. Its quotient E0(4) is globally generated, while E0 embeds into a trivial bundle. Together these give every degree of E0 in [-4,0]. No degree estimate is inferred from rank and degree alone.

## 4. The complete actual derivative target of E0

This is the crucial interface, and I reconstruct it explicitly.

Set H'=H/A, Q0=H' O/E0, and Q'=H' O/E'. Constant projection by A makes the derivative of E' the projection of the original derivative. Its image is the actual saturated bundle

    I' = O(-8)+U inside Q'(-2),  U=O(2),

because the high summand L(-2) is exactly what was removed. The low U is itself saturated in Q'(-2): it is a direct summand of I', and the quotient by I' is locally free.

The negative component of the derivative on E0 is zero, inherited from Ehat. The original F has image in E0 and retains its nonzero low row. That row D(-2)->O(2) is the unique nonzero complete quartic evaluation and is everywhere onto. The scalar L_- has no low component, since Hom_G(O(-8),O(2)) is the invariant degree10 space, which is zero.

It is not valid to conclude immediately that the standalone derivative of E0 has image U: a derivative internal to E' toward L_- remains possible before the following calculation.

From the actual inclusion E0 subset E' there is an exact sequence

    0 -> L_- -> Q0 -> Q' -> 0.

Twisting by -2 gives kernel O(-10). Define Z to be the actual inverse image of U under this actual quotient map:

    Z = Q0(-2) fiber-product over Q'(-2) with U.

Thus, by pullback, not by selecting an abstract target type,

    0 -> O(-10) -> Z -> U=O(2) -> 0.

Furthermore Q0(-2)/Z is canonically Q'(-2)/U and is locally free. The standalone derivative beta0:E0->Q0(-2) lands in Z, because its projection to Q'(-2) is the derivative of E' restricted to E0, with only the low U row.

The equivariant extension class lies in

    Ext1_G(O(2),O(-10))
       = H1(O(-12))^G
       = (Sym10 W)^G = 0,

using characteristic zero and finite G to take exact invariants, and det W=1 for equivariant Serre duality. Here Sym10=A+V+D. The ordinary Ext1 space is not zero; it is its invariant part that vanishes. Therefore this particular equivariant extension splits. Its splitting is unique because Hom(O(2),O(-10))=H0(O(-12))=0. The resulting copy of U in Z is an actual globally defined subbundle.

Under that unique splitting, the O(-10) component of beta0 is a global regular sheaf map E0->O(-10). Every degree of E0 is at least -4, so this whole-source map is zero. This does not merely kill a restriction to some derivative kernel. The surviving component to U is onto because its composition with the original F is the complete quartic evaluation. Hence

    image(beta0) = U inside Z inside Q0(-2)

as an actual image sheaf.

For saturation, there is the exact sequence

    0 -> O(-10) -> Q0(-2)/image(beta0)
      -> Q'(-2)/U -> 0.

Both end terms are locally free, so the middle quotient is locally free. This proves that the standalone derivative image is exactly one saturated O(2), and verifies the full image/preimage identification claimed in Section4. There is no omitted negative internal channel.

## 5. Exact cohomology and exhaustive residual classification

The exact quotient by N_A gives the following independently computed characters:

    chi(Ehat) = -V-3P-3D,
    chi(N_A) = -V-2P-D,
    chi(E0) = -P-2D;

    chi(Ehat(1)) = -Wp-2T,
    chi(N_A(1)) = -Wp-2T,
    chi(E0(1)) = 0;

    chi(Ehat(2)) = D-V,
    chi(N_A(2)) = -D-P-V,
    chi(E0(2)) = P+2D.

Also H0(Ehat(1))=0, so the cohomology sequence gives an actual injection

    H0(E0(1)) -> H1(N_A(1)) = Wp+2T.

The degree bound allows the equivariant splitting

    E0 = C0 O+C1(-1)+C2(-2)+C3(-3)+C4(-4).

Here C0 is an actual constant subspace of H'. The H0 budget is C0 W+C1 contained in Wp+2T. The even coefficient products are

    1 W=W, A W=W+S, V W=T,
    P W=Wp+T, D W=S+T.

Thus C0 consists only of V and P, and C1 only of Wp and T.

The saturated top subbundle C0 O+C1(-1) has zero external derivative: C0 is constant, and the C1 rows to O(2) vanish because Wp and T are absent from Sym3=S. Its internal derivative into the quotient twisted by -2 also vanishes, since that quotient has degrees at most -4. A saturated subbundle preserved by the trivial connection has constant classifying map in characteristic zero and is a constant bundle. Its degree is therefore zero; this forces C1=0. This is a connection argument on the actual embedded subbundle, not a horizontal interpretation of an arbitrary splitting.

Quotienting by the actual constant C0 yields a saturated negative E1 in the corresponding constant ambient quotient. Because C0 is already contained in E0 and is constant, this projection leaves the external quotient and its actual O(2) derivative image unchanged.

The top coefficient map C2->H0(O(4))=D must be injective. If a nonzero coefficient kernel U existed, its direct summand U(-2) would have zero external derivative, and its internal derivative would land in degrees at most -4. It would be a forbidden preserved negative subbundle. Since D is irreducible, C2 is 0 or D.

Write C0=pV+qP. The budget gives q<=1 and p+q<=2, so exactly five possibilities:

    (p,q) = (0,0), (1,0), (2,0), (0,1), (1,1).

The equation chi(E0(1))=0 gives C3+C4 W=C0 W. Positivity forces C4=uV+vP, since any other even irreducible would introduce W or S. Combining this equation with chi(E0)=-P-2D, and using W^2=1+A, yields

    C2 = P+2D-C0 A+C4
       = (1-p-q+v)P+(2-p-q)D+(u-q)V.

Here V A=P+D and P A=V+P+D. Since C2 is 0 or D, the V and P coefficients force u=q and v=p+q-1. The zero constant budget makes v negative; the 2V budget makes C3=T-Wp, which is not genuine. Exactly three possibilities remain:

    C0=V:   E1=D(-2)+T(-3);
    C0=P:   E1=D(-2)+Wp(-3)+V(-4);
    C0=V+P: E1=(V+P)(-4).

Each also satisfies rank14 and degree-28 after C0 is restored. The enumeration is exhaustive under the actual H0 injection; no unlisted constant, linear, quadratic, cubic or quartic coefficient can survive.

## 6. Independent audit of the three actual contradictions

### C0=V+P

The original F=D(-2) has no map to E1=(V+P)(-4), by degree. Its image in E0 therefore lies in the actual constant C0, so its external derivative in E0 is zero. On the other hand, constant projection by A preserves its nonzero original low row, and projection by constants already inside E0 does not alter that row. Contradiction. This is a source-specific contradiction, not a formal objection to the bundle (V+P)(-4) in every setting.

### C0=P

The original R=Wp(-3) has no map to constant A, since A Sym3=W+S+T has no Wp. Choosing an equivariant constant complement of A in H therefore shows that constant projection by A retains R as an actual injection. Similarly R has no map to constant P, because Wp Sym3=V+D has no P. It remains injected after the second constant projection.

In E1=D(-2)+Wp(-3)+V(-4), its components to D(-2) and V(-4) vanish: the former because D W=S+T has no Wp, the latter by degree. Therefore its nonzero equal-degree Wp component is an isomorphism, and its image is the whole saturated Wp(-3) summand. Its external derivative to O(2) is zero because Sym5=T has no Wp. Its internal derivative to D(-4)+V(-6) vanishes by degree. Thus this actual saturated negative subbundle is preserved by the trivial connection, a contradiction.

This argument does not silently replace injectivity with a generic-rank assertion, and does not require a conclusion about the original high D row.

### C0=V

The original F maps only to D(-2) inside E1=D(-2)+T(-3), since its component to T(-3) vanishes by degree. Its D component is nonzero because the low row survives, and is consequently an equivariant scalar isomorphism. The derivative row on this actual D(-2) summand is nonzero complete quartic evaluation, with kernel S(-3).

The space Hom_G(T(-3),D(-2)) is one-dimensional, since T occurs once in D W=S+T. Composition with the D derivative gives a nonzero map to Hom_G(T(-3),O(2)): a zero composite would factor through S(-3), but Hom_G(T,S)=0. The latter Hom space is also one-dimensional, since Sym5=T. Composition is therefore an isomorphism of these one-dimensional spaces.

For the actual existing T derivative row there is a unique triangular correction into the D summand cancelling it. The resulting graph is an actual saturated T(-3) complement to D(-2), not a selected value of a source coefficient and not a change to the ambient connection. Its external derivative is zero. Its internal derivative to the complementary D(-4) is a regular sheaf map and vanishes by degree. Hence that negative graph subbundle would be preserved, again impossible.

All three residual possibilities are therefore excluded.

## 7. Computational independence, permitted scope, and conclusion

The independent small representation calculation used the McKay products

    W*1=W; W*W=1+A; W*A=W+S; W*S=A+D;
    W*D=S+T; W*T=D+P+V; W*P=T+Wp;
    W*Wp=P; W*V=T,

and Sym(n+1)=W Sym(n)-Sym(n-1). It reproduced Sym6=V+P, Sym8=P+D, Sym10=A+V+D, Sym14=A+V+P+D, Sym16=2D+P+V, Sym18=A+V+2P+D, the full six-candidate kernel table, and the needed products A Sym3 and Wp Sym3. The frozen verifier separately passed all its authenticated-input, Euler, candidate, budget and Hom checks. Neither computation substitutes for the actual-image, quotient, connection and saturation reasoning above.

The whole-source conclusion is valid for precisely

    G3.11.cce6e3ba4eeb, source_index127,
    tuple (1,1,1,0,0,1,0,0), original defect0,
    E=D(-2)+(Wp+T)(-3)+V(-4)+O(-8),
    A_q=O(-8)+O(2)+O(16),
    B_q=O(-18)+O(-4)+O(6).

The proof covers both possibilities for the original high D row. The low-D lemma is also used to establish onto low image in the standalone E0 construction, and in the first and third final contradictions. It cannot be dropped from the interface. In particular, an unrelated source with zero low-D row is not excluded by the final (V+P)(-4) argument; there is no accidental exclusion of the separate c-d-f family.

No conclusion is drawn about all sources under the stable label, total necessary-pair counts, global rank-three impossibility, or realization of another abstract family. No selected actual HM/source coefficients, parameters, points, derivatives, matrices, instance ranks, models, scans, or large computation were used. All computations were fixed abstract characters and the six/five/three finite structural alternatives. The actual maps in the proof are forced equivariant maps, kernels, images, preimages or constant projections, not evaluated instances.

**Final verdict: PASS for the exact frozen proof and verifier hashes above.** The new forced-A construction and the actual-target invariant-extension calculation close the a-b-c-f whole-source exclusion without an unproved internal-channel vanishing.
