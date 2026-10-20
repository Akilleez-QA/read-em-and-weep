> Historical mathematical review of the source manuscript. This is not a new independent review or a formal verification certificate. Original source-byte hashes refer to the archived manuscript; public-byte hashes are in SOURCE-BINDINGS.json.

# Independent audit of the higher-twist exclusions

## Verdict

The claims in `PROOF.md` are mathematically sound under its stated HM input, H⁰(F(u))=0 for u<3, and the stated Chern classes. No substantive correction was needed, and this audit did not modify `PROOF.md`. In particular, the broad Picard-group assertion is supported by the cited primary source, including singular and nonnormal integral covers. It does not promote the spectral module to a line bundle.

## 1. Generic rank-one exclusion

For a saturated rank-one subsheaf K of a vector bundle on the smooth base, the quotient is torsion-free. At local rings of dimension at least two, the depth lemma gives depth(K)≥2. At dimension one, torsion-freeness gives depth at least one. Thus K is reflexive; on P⁴ it is a line bundle. This applies both to the kernel of a generic-rank-one map and to its saturated image.

The inclusions O(a)⊂F and O(b)⊂F(k) give a≤−3 and b≤k−3. The rank-one torsion-free quotient F/O(a) has double dual O(−1−a), so it is I_Z(−1−a) for a codimension-at-least-two subscheme. The nonzero induced map to O(b) belongs to H⁰(O(a+b+1)): the identity Hom(I_Z,O)=O follows by extending across codimension two. Since a+b+1≤k−5, there is no such map for k≤4.

For trace-free φ, the zero determinant case and the nonzero square determinant case reduce to this exclusion. In the latter case φ−s·id is nonzero and generically rank one: its determinant is zero, and its trace is −2s. The rational-square-to-polynomial-square argument is valid over C. Hence the double-cover algebra is a domain, not merely generically reduced.

## 2. Chern and singular-scheme arguments

The root calculation gives c₂(End₀F)=15H² and c₃(End₀F(k))=(k³+15k)H³. The values 38, 72, 124 are correct. A nowhere-vanishing section would give a locally free rank-two quotient, contradicting this nonzero third Chern class.

The zero ideal has three local generators. Krull's height theorem bounds the height of every minimal prime over it by three, so each irreducible component of its support has dimension at least one. Nonemptiness alone would not suffice for this conclusion; the three-generator bound supplies the missing dimension statement.

Locally q=a²+bc belongs to I_Z² and each derivative of q belongs to I_Z. Consequently the Jacobian ideal (q,∂q) is contained in I_Z, which is the correct ideal direction for the closed-scheme inclusion Z⊂Sing(V(q)). Trivializing the twisting line bundle differently preserves this conclusion. This remains true for a nonreduced branch divisor.

The degree interpretation of c₃ is correctly conditional on expected codimension three. In that case the three generators form a regular sequence in the regular base, and the zero-section formula gives the fundamental cycle. No unconditional degree of the singular locus is inferred.

## 3. Spectral module and exact nonfree locus

The finite-flat rank-two algebra acts on F by the Cayley–Hamilton identity. At the generic point it is a quadratic field extension, so the two-dimensional base-field module F has rank one over that field.

A base regular system of parameters is a regular sequence on F because F is locally free on the base. At each closed point of X the same parameters form a system of parameters and remain module-regular after localization. Thus M is MCM; this property localizes to nonclosed points. This does not use normality.

A nonzero trace-free two-by-two matrix in characteristic zero is nonscalar and has a cyclic vector. Lifting such a vector makes v,φv a local basis and identifies the spectral module with its algebra. This works at nonzero nilpotent branch matrices as well as away from the branch.

At φ(y)=0, the unique spectral point has residual module of dimension two, whereas a free rank-one module has residual dimension one. This proves nonfreeness. The argument identifies the asserted loci first at closed points; equality as underlying closed subsets follows because the nonfree locus of a finitely presented rank-one module is closed and X is a finite-type C-scheme. Alternatively the same cyclic-vector argument works over the infinite residue fields of all base points. The statement is set-theoretic, and no equality of a chosen nonfree scheme structure with the lifted zero scheme is claimed.

## 4. Normality and factoriality

The construction does not prove normality, and the text properly says so. For example, a square factor in q can yield a nonnormal integral double cover. On a normal X, a rank-one MCM module is reflexive (torsion-free and S₂). Its torsion-freeness can also be seen directly: a nonzero element of the quadratic algebra has nonzero norm in the base domain, so algebra torsion would imply base torsion in the base-free F.

A rank-one reflexive module over a factorial normal local ring is free. Therefore each point of the identified nonfree locus is genuinely non-locally-factorial when X is normal. Neither normality alone nor MCM alone suffices for freeness. The proof avoids both invalid implications.

## 5. Primary-source Picard check

Source: Grothendieck et al., SGA 2, Exposé XII, Corollaries 3.5–3.7, revised printed pages 120–121 (PDF pages 128–129):

https://www.cmls.polytechnique.fr/perso/laszlo/sga2/sga2-smf.pdf#page=128

I inspected the rendered typeset pages, not only extracted text. In particular, Corollary 3.7 has dimension ≥3, not >3. Its complete-intersection hypothesis does not include smoothness or reducedness. Corollary 3.5 supplies the setup for 3.6: a projective scheme, an ample invertible sheaf, and a regular section. Very ampleness is not required.

For applying these results here, take the ample sheaf L=π*O(k) and its regular section z. Then D=(z) is Cartier, D≅V(q) scheme-theoretically, and X has depth four at closed points. The conormal powers on D are O_D(−nk); the hypersurface sequence gives their H¹ and H² vanishing for every positive n. Finally the closed points outside D are regular of dimension four, hence parafactorial. These checks meet the bijectivity case of XII 3.6. The three-dimensional hypersurface D meets XII 3.7, even if it is reducible or nonreduced. Restriction carries π*O(1) to O_D(1), yielding Pic(X)=Z[π*O(1)].

Thus the proposed broad Picard proof is valid, but it classifies invertible sheaves only. The actual spectral M is noninvertible along the forced positive-dimensional zero locus, so there is no contradiction with that Picard calculation.

## 6. Scope and stopping point

The splitting/Chern obstruction is also correct: a spectral line bundle π*O(m) would force c₁=2m−k=−1 and c₂=m(m−k)=4, while substitution gives c₂=(1−k²)/4. Restrictions to linear Pⁿ with n≥2 retain the required Chern-class comparison whenever the stated line-module hypothesis holds there.

No conclusion that H⁰(End₀F(k)) vanishes for k=2,3,4 follows. The remaining singular/nonfree possibilities are real logical residual cases.
