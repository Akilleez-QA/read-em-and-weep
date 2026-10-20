# Prior mathematical audit

This audit concerns the source manuscript. It is not a formal verification or a review of later normalized publication bytes.

# Independent audit of the residual-rank-one model

Audit date: 2026-10-19. Reviewed `PROOF.md`, sections 1–6, independently from the stated hypotheses. Work is over C and all dimensions below concern reduced supports.

## Verdict

The universal compatible-fiber bound of three for a nine-dimensional hyperplane K in Sym²(C⁴), its sharp generic realization for a nondegenerate trace form, and the isolated-middle abstract cyclic-tensor quotient construction are valid. No mathematical gap was found in these claims. Their scope is abstract tensor algebra: they establish neither a source/equivariant realization nor a moving exceptional-middle family, and they do not establish sharpness of the global affine upper bound eight.

The opening statement originally had a wording issue, now corrected: dimension six is the **affine independent-zero locus**, not the unrestricted all-inputs-nonzero zero locus. All-collinear triples always vanish and form an affine seven-dimensional locus. The current opening statement explicitly restricts to independent zeros.

## Checks

1. **Diagonal extension.** For every nonzero hyperplane functional h, the projective square locus is a quadric support of dimension two, including degenerate and double-plane cases. If a compatible component has dimension at least four, general ample cuts give an integral projective fourfold Z. Its diagonal intersection has dimension at most two. A projective threefold slice S must meet the diagonal: the diagonal class in P³×P³ is the sum of all four degree-three mixed monomials; those mixed degrees on S are nonnegative, and at least one is positive by ampleness of O(1,1). Finite normalization preserves the bound on the inverse image of the diagonal. Away from that inverse image the two tautological lines are independent, so the compatible vector has unique regular coefficients, sections of the opposite tautological-dual line bundles. Normality extends these across codimension at least two, and the vector identity extends by density. Evaluation on the nonempty diagonal forces a forbidden square. This proves the claimed upper bound without a K8 theorem or genericity.

2. **Generic sharpness.** The square-violation incidence has dimension 2+33=35 in the 36-dimensional correction space; projectivity of its base makes its image closed. The distinct ordered trace-orthogonal pair variety is a nonempty open subset of a smooth irreducible P²-bundle over P³, hence has dimension five. Its factor-exchange quotient is the smooth rank-two tensor locus, with finite étale double cover. Compatibility gives two independently surjective linear conditions on v, producing a smooth irreducible incidence of dimension 39. Dominance is not inferred from dimension alone: choosing two embedded tangent directions independent modulo q and prescribing v(q)=0 makes the two q-direction derivatives onto the quotient E/im(q). The moving-subspace derivative contributes zero at this point. Thus the projection has surjective differential and is dominant. Generic fibers are nonempty of dimension three, and the relevant nonempty open intersects the square-avoidance open.

3. **Universal tensor space and graph.** The wedge-kernel W has dimension 50−10=40. Its rank-one tensors are exactly a⊗(a∧b), and their projectivization is the seven-dimensional flag variety. The universal middle space F_a has dimension 14, repeated-input image dimension four, and quotient Sym²(V/Ca). The graph L has dimension nine and avoids the rank-one variety. The displayed matrix correctly has rows −v(q) and 2M(q). Its second-factor support contains at least two independent vectors u∧w_i, by either rank(q)≥2 or square avoidance. Containment of both in a∧V forces a proportional to u; hence L∩F_a=0 for every other middle.

4. **Completion counts.** In W/L of dimension 31, Gr(11,31) has dimension 220. Planes containing one prescribed line form Gr(10,30), dimension 200. The projected rank-one locus gives bad dimension at most 7+200=207. The other-middle incidence gives at most 4+13+200=217. Taking its closure is legitimate and necessary because the middle parameter space omits u. The third bad condition, meeting the fixed five-space F_u/L, is a proper closed Schubert condition. Thus the three required good opens have nonempty intersection. No unjustified properness assumption enters the other-middle argument.

5. **Exact ranks and independent zeros.** The residual rank is dim p(F_a)−4=10−dim(Ktot∩F_a), hence equals one at u and ten elsewhere. Expanding outer lifts yields the stated equation A_u(v(ab)+βa+αb). For independent a,b modulo u, the two coefficients are unique exactly when v(ab) belongs to their span. Therefore the separately projectivized independent-zero locus has dimension three, its affine independent-zero locus dimension six, and its affine fiber with a nonzero middle vector fixed dimension five.

## Unrestricted nonzero zero locus (clarification)

The all-collinear triples have projective dimension four and affine dimension seven. There are no additional nonzero zero triples spanning exactly a two-plane: in that plane f0(x,y,z) is a rank-one tensor unless it is zero, and for three nonzero inputs it is zero only when all three lines coincide. The quotient preserves nonzero rank-one tensors. Consequently this model's unrestricted nonzero zero locus has dimension seven, the maximum of the independent stratum's six and the collinear stratum's seven. This does not affect any independent-zero claim.

## Integrated equality-case corollary

The corollary is sound, with the established global middle-support hypothesis and prior rank-stratum bounds retained explicitly. The residual-rank-zero exclusion in `../rank-one-boundary-support/PROOF.md`, Section 7, is valid: the twisted Euler sequence gives c3(T_P³(1))=15h³, so a correction on all Sym²E must have a compatible square. Rank zero therefore cannot occur.

Import the already established affine upper bound seven for components generically of residual rank at least two (including the completed K8 result in `../diagonal-hartogs-fiber-bound/UNSQUARED_PENCIL.md`), and hypothesis (H), which bounds the projective rank-drop middle support by two. Then any affine dimension-eight independent-zero component must generically have residual rank one. Removing its three nonzero input scales gives projective dimension five. Its projective middle image has dimension at most two and its generic projective fiber has dimension at most three by the present K9 theorem. The dimension formula forces equality in both: middle-image dimension two and generic projective fiber dimension three.

This is a necessary equality-case description, not an existence theorem. The isolated-middle model has middle-image dimension zero, projective fiber dimension three, and affine independent dimension six; it does not realize the equality case. The earlier global affine bound eight is already proved in `../nilpotent-kernel-parameter-locus/PROOF.md`, Sections 7–8; the new result refines its potential equality case rather than newly establishing that numerical bound.
