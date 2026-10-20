# Affine dimension consequences and the geometry over curves

## Hypotheses and notation

Work over C with dim V=5, an outer-symmetric cyclic-zero trilinear map f:V³→J, and injective maps A_a:V/Ca→J for every nonzero a. The conclusions below use the rectangular-incidence theorem in PROOF.md, now independently audited, and the elementary fixed-middle results in /research/hm/normalizer-rank-five/full-support-scroll-exclusion/PROOF.md and /research/hm/middle-surface/rank-six-surface-reduction/PROOF.md, Sections 6–7.

Let Z_ind be the locally closed affine locus of triples (l,u,n) with f(l,u,n)=0 and l,u,n linearly independent. Its projectivization is the corresponding open locus PZ_ind in P(V)³. Passage from PZ_ind to Z_ind is a principal (C*)³ bundle. Thus every irreducible locally closed component and its affine closure acquire exactly three dimensions, not one.

For a fixed middle line [u], set E=V/Cu. The residual map Q_u is the symmetric outer map to J/im A_u; its kernel K_u lies in Sym²E. Rank Q_u=5 means dim K_u=5. After a splitting E→V and a representative u are chosen, the induced correction v:K_u→E is characterized by A_u(v(ab))=f(a,u,b), with a,b lifted using that splitting. For a rank-two tensor ab, lift reconstruction is possible exactly when v(ab)∈span(a,b). The two ordered factor choices give exactly two ordered projective zero lifts. This finite reconstruction preserves dimension. All the following fixed-middle locus statements are set-theoretic, or equivalently statements about reduced varieties; no assertion about nilpotent scheme structure is made.

## 1. Exact type III fiber

Assume the ENTIRE residual kernel, not merely a subspace of it, is

    K=span{xz,yz,xy,xw+y²,yw}

for a basis x,y,z,w of E. Assume its cubic scroll

    S: q=(s x+t y)(a z+b(s y+t w))

is compatible on a dense open. Compatibility is closed on the rank-two locus, and K contains no nonzero square. Hence the whole scroll is compatible. The full rank-two locus is

    R₂(K)=S ∪ P,       P=P(y span{x,z,w}).

Both components are surfaces. Consequently the compatible locus, and therefore the entire projective independent-zero fiber at [u], has dimension EXACTLY TWO.

There is a sharper description. Dense scroll compatibility forces the five-parameter formulas

    v(xz)=λx+μz,                  v(yz)=λy+νz,
    v(xy)=αx+μy,
    v(xw+y²)=βx+(α+ν)y+μw,       v(yw)=βy+νw.

Put δ=α−ν. On the extra plane, write q=y(Ax+Bz+Cw). Modulo Cy, compatibility says that

    αA x+νB z+νC w

is proportional to Ax+Bz+Cw. This is equivalent to

    δAB=δAC=0.

If δ≠0, the compatible part of P is exactly the line P(y span{z,w}) together with the point [xy]. Both already lie on S, so the ENTIRE compatible locus is S. If δ=0, the whole extra plane is compatible and the ENTIRE compatible locus is S∪P. In either case the fiber dimension remains two. Here δ=0 is precisely the contraction condition v(q)=2q(d) for a covector d, in the notation and symmetric-product convention of the cited proof.

The ordered zero lifts over S have projection spans

    X=span{x−μu,y−νu},
    Y=span{z−λu,y−αu,w−βu}.

For δ≠0 these are complementary. For δ=0 they intersect in C(y−νu). In the latter case the compatible plane reconstructs the transverse rectangular zero

    f(C(y−νu), u, span{x−μu,z−λu,w−βu})=0.

Thus contraction-type middle points belong to the fixed finite exceptional middle set F of PROOF.md. This also follows directly from its rectangular boundary lemma. None of these claims presumes the correction vanishes.

## 2. Components generically carrying a compatible scroll

Let C be an irreducible component of PZ_ind, and B the projective closure of its middle image. Suppose on a dense open of B:

1. rank Q_u=5;
2. the full kernel K_u is of the explicit full-support parametrized family classified in /research/hm/normalizer-rank-five/full-support-scroll-exclusion/PROOF.md;
3. a cubic-scroll surface in that kernel is compatible on a dense open.

Conditions 2–3 force type III: types I and II admit no densely compatible scroll under repeated-input injection. Every such [u] belongs to the closed middle image of the rectangular incidence R from PROOF.md. Therefore B is contained in that image and

    dim B≤1.

Section 1 bounds every generic projective fiber of C by two. Hence

    dim C≤dim B+2≤3,
    dim(affine component over C)≤6.

This assertion does NOT need a separate bound on the full middle rank-drop locus. If C is specifically dominated by the ordered scrolls, its generic fiber has dimension two, so the affine dimension is exactly dim B+5: five over a point and six over a curve. For an arbitrary C above these same middle points, the generic fiber can be smaller; “exactly two” refers to the full fixed-middle zero fiber, not automatically to every component of the total incidence.

If B is a curve, its general point avoids F. Thus its general correction has δ≠0 and its full compatible rank-two locus is just S. The extra compatible plane can occur only at finitely many middle points, even if it appears at the boundary. Nothing about residual kernels at other boundary points is required.

## 3. A stronger conditional bound for every kernel in the explicit family

Assume additionally that the closure of the relevant rank-drop middle locus has dimension at most two, as in the earlier global dimension arguments. Then every affine independent-zero component whose generic full residual kernel is one of the explicit types I, II, III has dimension at most six, even WITHOUT assuming a compatible scroll in advance.

For I and II the entire compatible locus has dimension at most one, by the full-kernel exclusions already proved. Adding a middle dimension at most two and the three scalings gives six.

For III, the whole rank-two locus has dimension two, so the projective fiber never has dimension greater than two. Whenever a compatible surface exists, its closure must be S or P, because those are the only irreducible surface components of R₂(K). A densely compatible S has middle image in pr(R), of dimension at most one. A densely compatible transverse plane P gives a rectangular zero of type (1,3), by the general correction calculation in /research/hm/middle-surface/rank-six-surface-reduction/PROOF.md, Section 7.3. Its middle belongs to the fixed finite polar-exceptional set F: its factor has a three-dimensional polar kernel. This plane argument applies to arbitrary corrections, not just corrections already compatible on S.

Consequently a two-dimensional middle image cannot have generic projective fiber dimension two. If the middle image has dimension two, the generic fiber has dimension at most one; if it has dimension at most one, the generic fiber has dimension at most two. In both cases the total projective dimension is at most three and the affine dimension at most six.

This strengthens the conclusion for this explicit kernel stratum only. It does not classify all rank-five kernels and does not establish a universal affine bound six outside the stated generic hypotheses. In particular no tracefree-ternary or other unclassified rank-five kernel is silently included.

## 4. Additional structure of the rectangular incidence over curves

Retain R and the finite exceptional middle set F from PROOF.md. For any [u] outside F, the projective fiber R_u is finite as a set. Indeed every point of that fiber is a complementary pair X⊕Y=V. On any reduced irreducible projective component of R_u, the projector onto X along Y is a regular matrix. All its entries are constant by projectivity, and its image and kernel determine X,Y uniquely. Thus each component is a point. No reducedness or unramifiedness of the original fiber scheme is asserted.

In particular R→P(V) is finite over the complement of F in its image: it is proper and quasi-finite there. Every irreducible component of R with nonconstant middle image is therefore a projective curve, finite over its middle curve away from F. Components supported over F are not addressed by this assertion and may have larger dimension.

Let T be the normalization of such a curve component. It is a smooth projective curve. Let X_T and Y_T be the pulled-back tautological subbundles of the trivial V-bundle, and put

    d_X=deg det(X_T*),       d_Y=deg det(Y_T*).

Both are nonnegative Plücker degrees. The determinant of the addition map

    X_T⊕Y_T → V⊗O_T

is generically nonzero and defines an effective divisor D with

    deg D=d_X+d_Y,
    support(D)⊂preimage(F).

Its zero set is exactly where the two subspaces cease to be complementary. Thus if either Grassmannian map varies, then d_X+d_Y>0 and the curve necessarily meets F. This gives a quantitative boundary restriction: the total determinant-degeneration multiplicity equals the sum of the two Plücker degrees. Multiplicities need not be one, even though the intersection of X and Y has dimension at most one at every point of R.

Conversely, if the curve avoids F, both Grassmannian maps are constant. More generally D=0 is equivalent to both maps being constant (their general values are complementary). Such a component is necessarily

    B × {(X₀,Y₀)}

for fixed complementary subspaces, and its normalization maps birationally onto B. The theorem does not exclude this constant-splitting possibility. It also does not prove that any such curve exists.

These statements apply to any curve component of R with nonconstant middle image, whether or not its general point comes from a scroll. For an algebraic family of compatible type III scrolls with nonconstant middle image, use the intrinsic spans from PROOF.md to obtain its rational map to R, then take the closure of the image. All degree assertions are on the normalization of that image curve; they do not require arbitrary parametrizing families to be finite over the middle image.

## Scope and provenance

Only universal trilinear geometry, finite factor reconstruction, explicit correction identities, projective fiber dimension, and tautological bundles on curves were used.   The independently audited rectangular-incidence dimension theorem is the stated dependency.
