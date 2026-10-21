# Independent review of the scalar degree-six ghost exclusion

## Verdict and scope

The argument in PROOF.md is valid conditional on its pinned representation and presentation inputs, particularly r=0 from PR497 and the actual relation sequence from PR492. It proves v=0 without assuming s=0. This is an independent mathematical review, not a formal proof-assistant verification. No selected HM/source instance, numerical matrix rank, coefficient search, or large computation was used.

## 1. Normalizations and identification of the actual map

Put W=W′ and E=A*. Choose the isomorphism L₂≅E⊗W so that its inclusion into S₂⊗W is id_E⊗r, where r(x)=x²⊗y−xy⊗x and r(y)=xy⊗y−y²⊗x. Multiplicity one permits this normalization because the actual inclusion is nonzero. Identify I₃ with the actual A⊗W summand in S₃, and choose any nonzero embedding F:A⊗W→T⊗E.

The U summand in T⊗E=A⊗(U⊕W) cannot contribute to a map from A⊗W into T⊗E⊗W⊗W: U and U⊗U′=T₄⊕J₅ have no W constituent. Hence the full cubic lift lies in F(A⊗W)⊗W⊗W, not merely its projection to that summand.

Actual polynomial multiplication on F(A⊗W)⊗Sym²W is κ times the stated lower contraction. Its potential Qspin component has zero target because S₃=A⊗(J₅⊕W). If κ were zero, the nonzero subspace F(A⊗W)⊗W in T⊗L₂ would map to zero in S₃⊗W. This contradicts the injectivity obtained from r=0. Thus κ is nonzero. Rescaling F or the chosen identifications only rescales κ and the final nonzero factor; it cannot alter the relative eigenvalues of K.

## 2. Independent binary calculation

Composing the contraction with r gives K(xx)=−xx, K(yy)=−yy, K(xy)=xy−2yx, and K(yx)=yx−2xy. Therefore K=id−2 swap, with eigenvalues −1 and 3 on the symmetric and alternating subspaces. Its inverse is −(id+2 swap)/3.

With ε=xy−yx and ordered threefold tensors, the cubic lift has

κf(x)=−xxy+(1/3)xyx+(2/3)yxx,
κf(y)=yyx−(1/3)yxy−(2/3)xyy.

The antisymmetrizer on the last two factors sends these to −(2/3)x⊗ε and −(2/3)y⊗ε respectively. Thus the complete alternating projection is exactly −2/(3κ) times F⊗ε. This checks the two basis vectors and establishes the claimed universal identity with its nonzero constant.

## 3. Minimal Tor step

Let Q=S(−2)⊗L₂⊗W be the minimal free cover of L⊗W and J its kernel. Because L₂ is the quadratic relation space and r=0 excludes cubic syzygies, J has no elements in degrees at most three. Consequently J₄→(J/mJ)₄ is an isomorphism.

A degree-four minimal syzygy of I among its cubic generators is the actual inclusion G:V⊗W→T⊗I₃. Quartic minimal generators of I cannot enter such a relation with nonzero constant coefficients, by their minimality. Its image under T⊗f, followed by polynomial multiplication, lies in J₄ and represents the functorially induced map Tor₁(I)₄→Tor₁(L⊗W)₄. This is exactly τ from PR492, with Tor₁(L⊗W)=Tor₂(H)⊗W. Hence τ=0 would force the actual lifted polynomial relation to vanish, not just its class modulo possible boundaries.

Projection to Λ²W commutes with polynomial multiplication in the two T variables. The verified nonzero factor therefore yields sym∘(id_T⊗F)∘G=0 if τ=0.

## 4. Exterior obstruction and conclusion

The map (id_T⊗F)∘G is injective because both constituent vector-space maps are injective. The kernel of T⊗T→Sym²T is Λ²T. Thus a zero symmetric composite would embed V⊗W into Λ²T⊗E.

The stated representation identities give

Λ²T⊗E=(E⊗E)⊗W0=V⊗((U⊗W0)⊕(W⊗W0))=V⊗(W0⊕Qspin⊕T₄).

None of these quotient representations is W. Equivariance and semisimplicity therefore prohibit such an embedding. This proves τ≠0. Since its source V⊗W is irreducible, τ is injective, so v=0. By PR492 duality this gives β₂,₆(R)=0 and β₃,₆(R)=45.

The result removes precisely the scalar degree-six ghost conditional on r=0. It does not establish s=0 or u=0 by itself, determine actual differentials, evaluate a selected source instance, or settle higher-order lifting or algebraicity.

## 5. Complete-table corollary

I also checked the final PROOF.md corollary by direct substitution into the exhaustive PR492 family. With r=q=0 from PR497/492, s=u=0 from PR499, and v=0 proved here, its free modules are exactly

F₀=S;
F₁=10S(−3)⊕15S(−4);
F₂=10S(−4)⊕52S(−5);
F₃=45S(−6)⊕10S(−7);
F₄=20S(−8);
F₅=3S(−10).

Their alternating Hilbert numerator is 1−10t³−5t⁴+52t⁵−45t⁶−10t⁷+20t⁸−3t¹⁰, agreeing with PR492. The completeness claim uses PR492's proved support bounds, not the numerator alone. This corollary is conditional additionally on PR499 at commit 1112189481554b0353c64178e3adc0dede2c3fbe; that input is not needed for the v=0 proof itself.
