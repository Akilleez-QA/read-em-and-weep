# Independent audit of the ternary metric boundary construction

## Scope and status

This is a formal geometric audit, using the canonical-complement construction in `/research/hm/middle-surface/rank-five-middle-families/PROOF.md`.  The independent derivation below was completed before reading the new boundary proof. The completed `PROOF.md` was subsequently read in full and passes this audit without substantive correction.

The proposed formulas are correct with the bundle and divisor hypotheses made explicit below. Smoothness of the determinant divisor is unnecessary. Reducedness matters only if one describes its multiplicity as one along its reduced support.

## 1. Assumptions and trace convention

Work over C. Let U be a line subbundle of a rank-four bundle H, let E=H/U have rank three, and let H be a subbundle of a rank-five bundle V. Put N=V/H. Let the ternary form be a nowhere-zero, possibly line-valued symmetric form on E. Assume its determinant is not identically zero, defines an effective Cartier divisor D, and the form has rank two at every point of D.

On local trivializations choose a lift s:E -> H, a nonzero frame u of U, and a representative h of the conformal form. Let K=ker(h:Sym^2 E -> O), and suppose the regular correction v:K -> E has the transformation laws of the canonical-complement construction. Assume square avoidance at every point of D: if 0 != r spans rad(h), then v(r^2) is not in Cr.

Choose any regular extension W:Sym^2 E -> E of v. Such extensions exist locally because the nonzero functional h is surjective locally and K is a subbundle. Define tr(W) by contracting the output with one symmetric input: in a local frame it has components W^i_{ij}. This is a tensor contraction, independent of frames.

## 2. Extension and conformal invariance

Off D define

    tau = tr(W) - (1/3) h(W(h^{-1}), -).

An alternative extension is W+a h for a local section a of E. Its trace increases by h(a,-), while its value on h^{-1} increases by 3a. Thus tau is extension independent. Replacing h by c h for an invertible function c leaves tau unchanged. Every contraction in the formula is tensorial, so arbitrary frame changes also preserve it.

For the shear correction sigma(d)(q)=2q(d), one has tr(sigma(d))=4d and sigma(d)(h^{-1})=2h^{-1}d. Hence tau(sigma(d))=(10/3)d. This recovers exactly the normalization in the earlier proof. The intrinsic covector is therefore the earlier trace-pairing covector; equivalently one can compute in a local h-orthonormal frame, where the orthogonal projection from all symmetric tensors to K subtracts h^{-1}tr/3.

## 3. Pole and residue

Write delta=det(h) in the chosen frame. Then

    tau = tr(W) - h(W(adj(h)), -)/(3 delta).

At a point of D, adj(h) is a nonzero rank-one tensor proportional to r^2, where r spans the radical. Moreover h(adj(h))=3 delta, so adj(h) belongs to K at that point. Consequently

    rho = h(v(adj(h)), -)

is well-defined there, independent of W, and nonzero by square avoidance: its vanishing would imply v(adj(h)) lies in rad(h). The graph correction -(3/10)tau therefore has polar numerator +rho/10. The statement “residue” here means the numerator relative to the local determinant equation; intrinsically it is a line-twisted residue, not a scalar covector independent of the chosen equation.

For x=alpha u+s(e), define the regular functional

    phi(x) = delta alpha + (3/10) delta tr(W)(e)
             - (1/10) h(W(adj(h)),e).

On D this is -rho(e)/10, so phi is surjective locally. Its kernel C is a rank-three subbundle. Off D it is exactly the canonical normalized complement. On D its fiber is

    C_b = U_b + s(ker(rho_b)).

This sum, equivalently the inverse image of ker(rho_b) in H_b, is independent of s. No diagonal normal form or path choice is involved. The kernel construction proves uniqueness of the extension from a dense complement of D on an integral base.

## 4. Intrinsic target and elementary transform

The rational functional lambda(x)=alpha+(3/10)tau(e), multiplied by u, is an intrinsic rational map H -> U. Under s'=s+d u, the coordinate alpha changes by -d(e), while tau changes by +(10/3)d. Under u'=t u, lambda changes by t^{-1}; thus lambda u is unchanged. Scaling h or changing its frame does not affect lambda.

Its simple pole as a rational map is bounded by D. Therefore it is intrinsically a regular surjection H -> U(D). The local formula for this map is phi above, interpreted using the local generator u/delta of U(D). Its restriction to U is the canonical inclusion U -> U(D), since phi(u)=delta. In particular

    0 -> C -> H -> U(D) -> 0,
    H/C = U(D).

Quotienting by U yields

    0 -> C -> E -> U(D)|D -> 0.

The first arrow is a sheaf injection, not an injection on boundary fibers: on D it has a one-dimensional fiber kernel. Indeed C meets U in zero as sheaves because delta is a non-zero-divisor, though C_b contains U_b for b in D. This distinction is necessary for interpreting the elementary transform correctly.

Since H is a subbundle of V, there is also an exact sequence of vector bundles

    0 -> U(D) -> V/C -> N -> 0.

## 5. Scheme-theoretic zero and Chern class

Twisting the last sequence by U* gives

    0 -> O(D) -> (V/C) tensor U* -> N tensor U* -> 0.

The section induced by U -> V/C factors through the canonical section of O(D). Because O(D) is a subbundle, its zero ideal is exactly the ideal of D, including any multiplicities. Thus it vanishes scheme-theoretically on D and nowhere else. If D is reduced, it has order one at each generic divisor point. Smoothness of D is not required for this conclusion.

Writing h_mid=c1(U*) to distinguish the middle hyperplane class from the ternary form, the Whitney formula gives

    c2((V/C) tensor U*) = [D](c1(N)+h_mid).

For a smooth base, the localized excess contribution along the Cartier divisor is c1((N tensor U*)|D) cap [D], pushed forward to the base. The normal line O(D)|D identifies with the first line subbundle of the restriction, so no extra D^2 term survives. This remains valid for a singular Cartier divisor using its normal line and Cartier Gysin formalism. On a surface this is a zero-cycle class, not the length of the divisorial zero scheme.

## 6. Necessary qualifications

- The extension requires constant ranks giving bundles U, H, E and N, regular correction v, a Cartier determinant equation, corank exactly one on D, and nonvanishing rho there.
- Rank-one points of h, vanishing rho, or rank/support jumps are outside this proof. Clearing denominators alone does not guarantee a primitive or surjective functional there.
- The algebraic construction itself also works for a nonreduced Cartier determinant divisor with corank one and nonzero rho, but the zero scheme then has its determinant multiplicity. “Exactly once” requires reducedness.
- No construction here asserts that such data arise from an actual source operation or that the remaining global boundary configurations exist.

## 7. Cross-check of the completed proof

The completed proof agrees with Sections 1–6 above. Its residue rho includes the factor 1/10 and the chosen determinant unit, whereas the local covector called rho in Section 3 of this audit omits those invertible factors. Both have the same intrinsic kernel and give the same limiting plane. Its canonical quotient is obtained by the regular functional t times the U-coordinate minus alpha; this fixes the sign so that the restriction to U is the canonical inclusion U -> U(D).

Its additional discriminant class also checks: if a=c1(U*), n=c1(N), and m=c1(M), then c1(E)=a-n, hence

    [D]=3m-2c1(E)=3m+2n-2a.

The general residual excess formula in its Section 5 is valid. On a smooth integral surface, after dividing a generically nonzero section of a rank-two bundle F by its maximal effective divisorial factor A, the residual zero scheme Z has dimension zero or is empty. At its points the two components form a regular sequence, so c2(F(-A))=[Z]. The rank-two twisting identity gives

    c2(F)=[Z]+A(c1(F)-A).

There is no implicit positivity assumption on the separate divisorial terms. The proof correctly limits its numerical positivity claim to the total class and limits the pure-simple-divisor identity to the hypotheses under which the global short exact sequence exists.

Verdict: the formal boundary theorem, normal-form independence, elementary transform, scheme-theoretic vanishing, and both excess formulas are certified under the stated hypotheses. Smoothness of the discriminant divisor is not an additional requirement.

## 8. Final multiplicity extension and frozen proof

The added Section 3A has been read and independently checked. For det(h)=f epsilon with f a non-zero-divisor, alpha=f lambda is regular and nonzero on every geometric boundary fiber by the rank-two radical-square argument. Thus alpha has a unit component locally. The generators with f replacing t give a subbundle, the quotient U(D), and exact zero ideal (f). Surjectivity of the residue map holds on the full nonreduced Cartier scheme by the same unit-component criterion, not merely on its reduction. At a DVR component of determinant multiplicity m, primitivity of alpha proves exact pole and section vanishing orders m. Equations (8)–(11) consequently retain their validity with the full divisor multiplicities. No assertion extends to higher-corank points.

Final verdict: Section 3A passes; the proof is approved for freeze.

Audited PROOF.md SHA-256:

    cd0be4013b9994ca30c7dfb8a07f20880718ffdb9e20f8eefa7527346e2135b4
