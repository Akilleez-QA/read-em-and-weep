# Independent audit: order-three rank-point bound

## Verdict

**PASS, conditional on the explicitly imported finite-locus, reflection-plane exclusion, and representation hypotheses.** The proof correctly establishes that the reduced finite locus Z3 has at most one G-orbit of size 1000. No gap was found. It does not establish existence or exclusion of the one remaining possible orbit.

I checked PROOF.md in full, the relevant parts of the canonical-line rank-five strengthening and its parity predecessor, the reflection-plane ADDENDUM (especially the stabilizer and cardinality conclusions), and Sections 1–3 of the 500-point-orbit proof. The earlier global finiteness and plane-exclusion theorems remain imported conditional inputs; this is not a fresh audit of their entire recursive dependency tree.

## 1. Universal two-dimensional image

The displayed binary formula is indeed outer symmetric and satisfies cyclic zero. In dimension two the corresponding universal Schur module has dimension two, so it parametrizes every such tensor, with the determinant twist accounted for by the chosen alternating form. Its normalization is immaterial.

If h(v)=0 with v nonzero, then for w independent of v the formula gives f(v,v,w)=det(w,v)h(v)=0. Repeated-input injectivity contradicts this. For fixed nonzero u, the values of b_u on uw and w² are det(w,u)h(u) and 2det(w,u)h(w). Over C both coefficients are nonzero. Thus the image of Sym²U is exactly the same fixed two-space H_U at every point, including the endpoints of the line.

Projection to J/H_U therefore annihilates the fixed domain subspace Sym²U along the entire pencil, not merely pointwise after an unspecified choice. The resulting matrix has linear homogeneous entries and has rank exactly rank b_u minus two. Consequently the Z3 threshold becomes rank at most five, as required.

## 2. Degree and multiplicity

The canonical endpoint has rank b at least nine, giving rank B_U at least seven. Hence a seven-minor nonzero at that endpoint exists, and is a nonzero section of O(7). At a point with rank at most five, every seven-minor vanishes to order at least two. This follows either by the stated local block reduction and invariance of determinantal ideals under invertible operations, or directly by multilinearity of the determinant after separating its residue-field rank block.

The divisor of a nonzero degree-seven binary form has total multiplicity seven. Distinct Z3 points each contribute at least two, so there are at most three. This argument needs neither transversality nor reducedness of the determinantal scheme: the count is explicitly on its reduced support. Nor can an identically vanishing chosen minor invalidate it, since the endpoint certifies the choice is nonzero.

The imported canonical-line strengthening supplies precisely the needed pointwise rank-nine bound. Its argument uses the constant-rank parity image bundles, their constant two-dimensional binary image, perfectness of SL2(F5), and the small-target contraction lemma. The latter holds for any two-dimensional target, and its isotropic-vector contradiction is valid. The statement used here does not depend on that file's later curve-degree or rank-five rigidity consequences.

## 3. Group calculations

Every subgroup of order three projects injectively to K. Averaging its cocycle is legitimate because three is invertible in F5; the displayed average gives f(g)=t−gt, and an A-conjugation removes it. Sylow conjugacy in K therefore gives one G-conjugacy class of order-three subgroups.

An order-three element of SL2(F5) has characteristic polynomial x²+x+1 and no fixed vector on A. For an element (v,k) to normalize the standard H, k must normalize H and the translation term forces v to be H-fixed. Thus N_G(H)=N_K(H), of order twelve. Its order-six subgroup centralizing H preserves each nontrivial eigenspace, while the other coset interchanges them.

The imported spectra give two two-dimensional nontrivial eigenspaces and one one-dimensional trivial eigenspace. Each projective nontrivial eigenspace is a line with one T endpoint and one W endpoint. The involution c acts nontrivially on that line with exactly these two fixed points. Both endpoints are excluded from Z3, so c acts freely on the intersection. Combining even cardinality with the bound three gives cardinality at most two on each line.

## 4. Orbit incidence and conclusion

For a point orbit with stabilizer H, its H-fixed points correspond exactly to N_G(H)/H, hence number four. There are no further fixed cosets: inclusion of one order-three subgroup in another forces equality. The isolated eigenvalue-one point is excluded. The line-preserving subgroup C6 acts modulo H freely with order two, and the other normalizer coset exchanges the two lines. Therefore every size-1000 orbit contributes precisely two points to each line.

Conversely, any Z3 point fixed by H has a stabilizer containing H. The imported stabilizer list 1, 3, 5 forces that stabilizer to be H itself. There are consequently no contributions from other orbit sizes and no overcounting between distinct G-orbits. If b is the number of size-1000 orbits, each line contains exactly 2b such points, so 2b≤2 and b≤1.

The consequence |Z3,red|=600a+1000b+3000c≤4000 with b in {0,1} is a correct sharpening of the imported cardinality formula, without any additional assertion about local lengths or existence.

## Evidence boundary

Only local proof files were read and this local audit was written. No actual source operation, selected source input, source evaluation, external write, installation, or large computation was performed.
