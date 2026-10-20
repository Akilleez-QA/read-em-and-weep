# Canonical odd lines have residual rank at least five

## Hypotheses and conclusion

Retain exactly the representation, equivariance, cyclic identity, and repeated-input-injectivity hypotheses of ../canonical-line-parity-exclusion/PROOF.md. Use its notation: Gamma = SL_2(F_5), V = W direct sum T, dim W = 2, dim T = 3, central involution z acts negatively on W and positively on T, and q is a nondegenerate invariant quadratic form on T. The canonical line is L = P(W).

**Theorem.** The odd parity block b_- has rank at least five everywhere on L. Therefore the full middle matrix b has rank at least nine, and the residual map Q has rank at least five, everywhere on every canonical odd line. In particular the twenty-five canonical lines are disjoint from Z_4.

This strengthens, rather than repeats, the earlier rank-at-least-four conclusion. It uses no decic closure or global determinantal geometry for the line assertion.

## 1. A useful dimension-two target lemma

Let B be any two-dimensional Gamma representation. Every equivariant map

    W tensor Sym^2 T -> B

factors through contraction with q, followed by a Gamma map W -> B.

Indeed Sym^2 T = 1 direct sum P_5, with P_5 irreducible of dimension five. Tensor-Hom adjunction gives

    Hom_Gamma(W tensor P_5, B) = Hom_Gamma(P_5, W* tensor B) = 0,

since the target of the last Hom has dimension four and finite-group representations over C are semisimple. No classification of two-dimensional binary-icosahedral representations is needed.

The same conclusion holds for any target which is a direct sum of two-dimensional representations, with one linear map h out of W into that sum.

## 2. Excluding odd-block rank four

The previous parity proof proves constant rank r for b_-, and supplies its image bundle I on P(W), with

    I = O(-1)^a direct sum O^b,  a+b=r.

It also supplies an intrinsic constant subbundle H tensor O contained in I, where H is isomorphic to W and dim H=2. Namely H is the image of the restriction of f to W^3, and b_u(Sym^2 W)=H for every nonzero u in W.

The vector space C=H^0(I) is a Gamma representation, contains H, and z acts on C by minus the identity. Since Gamma is perfect, its determinant character is trivial; hence b=dim C is even.

Suppose r<=4. The prior proof already excludes r<=3, so r=4. There are exactly two possibilities.

### Case a=0, b=4

All of I is constant, with image C in J_-. Choose an invariant complement B of H in C. Then dim B=2. Apply Section 1 separately to H and B. All the mixed values have the form

    f(t,u,t)=q(t)h(u),  t in T, u in W,

for one linear h:W->C.

### Case a=2, b=2

Here C=H, and the intrinsic quotient bundle I/(H tensor O) is isomorphic as an ordinary bundle to O(-1)^2. Choose a Gamma-invariant complement J' of H in J_-. Projecting to J' embeds this quotient bundle into J' tensor O as a subbundle.

Let U=O(-1) with its canonical Gamma linearization, and put

    B=H^0((I/(H tensor O)) tensor U*).

Evaluation identifies the quotient equivariantly with U tensor B, and dim B=2. The central involution acts negatively on both the quotient and U, so it acts trivially on B. Thus B is a two-dimensional representation of A_5. It is trivial, since A_5 has no nontrivial complex representation of dimension one or two.

The inclusion U tensor B -> J' tensor O corresponds to a Gamma map W tensor B -> J'. Consequently its total image is contained in the fixed representation H'=image(W tensor B), a quotient of W direct sum W. Semisimplicity shows that H' is a direct sum of at most two copies of W. Therefore all mixed values f(t,u,t) lie in H direct sum H', and Section 1 again gives

    f(t,u,t)=q(t)h(u).

### Common contradiction

Over C, choose a nonzero isotropic vector t for the nondegenerate quadratic form q on the three-dimensional T. For any nonzero u in W the displayed identity gives f(t,u,t)=0. Outer symmetry and cyclic zero give 2f(t,t,u)+f(t,u,t)=0. Repeated-input injectivity therefore forces u in Ct, contradicting W intersect T = 0.

Both cases are impossible. Hence r>=5.

## 3. Rank and global consequences

The even block has rank at least four by the prior parity proof. Their target eigenspaces are complementary, so rank b_u>=9 and rank Q_u>=5 on L. Normalizer equivariance propagates this to all twenty-five lines.

Under the global decic-closure hypotheses that give dim Z_5<=1, let Gamma_4 be the reduced curve part of Z_4. The degree-ten minors of b have generic order at least two along each component of Gamma_4. The same regular-local parameter-ideal multiplicity argument used in ../rank-three-curve-constraints/PROOF.md gives

    8 deg Gamma_4 <= 1000,  hence deg Gamma_4 <=125.

The component-orbit classification in Sections 2--5 of that file, together with canonical identification in ../rank-three-line-rank-constancy/PROOF.md Section 7, applies to ANY normalizer-invariant reduced curve of degree at most37: if nonzero it must be the canonical twenty-five-line orbit. The new theorem excludes that possibility for Gamma_4. Since Heisenberg invariance makes its degree divisible by five, we obtain the new gap

    Gamma_4 = 0, or 40 <= deg Gamma_4 <=125, with 5 dividing deg Gamma_4.

This is not a classification or exclusion of all rank-four curves. It excludes the smallest possible invariant curve configuration and all canonical-line rank-four fibers. It does not yet lower the universal rank-four compatible-fiber bound of two.

## Boundary

Only abstract representation and vector-bundle arguments are used. No actual source-instance evaluation is claimed. The local proof artifact is the sole change. The proof imports the audited earlier parity and invariant-curve classification results, and its independent audit is recorded in AUDIT.md.

## 4. Additional rigidity at the remaining rank-five threshold

If the residual rank on a canonical line is exactly five, its parity ranks must be (even,odd)=(4,5). There are useful necessary image-bundle forms:

    I_+ = P_4 tensor O,
    I_- = (H tensor O) extended by (O(-1) tensor B),

where H is isomorphic to W and B is one of the two irreducible three-dimensional A_5 representations. The extension splits as an ordinary bundle, but no equivariant splitting is claimed or needed.

Here are the details. For an even rank-four image write I_+=O(-1)^a direct sum O^b. In the kernel sequence from O(-1) tensor (W tensor T), irreducibility of the six-dimensional W tensor T implies H^0(K(1))=0. The rank-two kernel has degree -6+a and both splitting degrees at most -2, so a<=2 and b>=2. The constant image C_+=H^0(I_+) is a subrepresentation of the coefficient image of the even block. That coefficient space is W tensor W tensor T = T direct sum P_4 direct sum P_5. Thus b=2 is impossible, b=3 forces C_+=T, and b=4 forces C_+=P_4. In the b=3 case a=1, the quotient by the constant image is O(-1) with a linearization whose central involution acts positively, since the target is J_+. Twisting by the canonical O(1) would give a one-dimensional Gamma representation with z acting negatively, impossible for perfect Gamma. Hence b=4,a=0.

For odd rank five, the constant dimension b is even and at least two, hence b=2 or4. If b=4, quotienting by the constant image gives O(-1), with its canonical linearization, so its span in a complementary fixed target is a copy of W. The constant image itself splits equivariantly as H plus a two-dimensional representation. Section 1 then again forces f(t,u,t)=q(t)h(u), impossible. Thus b=2,a=3. The negative quotient is O(-1) tensor B for an A_5 representation B of dimension three. If B were trivial, its total span in a complementary target would be a sum of copies of W, producing the same contradiction. Semisimplicity and the absence of nontrivial representations of A_5 of dimensions one or two leave precisely its two irreducible three-dimensional representations.

These are necessary representation-bundle configurations, not existence statements. They isolate the first remaining canonical-line case without evaluating the source operation.
