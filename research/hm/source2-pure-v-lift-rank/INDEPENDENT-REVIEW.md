# Independent review: the quadratic P-to-D lift pencil

## Verdict and boundary

PASS for the universal pencil classification, conditional on the exact retained representation identifications and source2 pure-V hypotheses in PR1025. The actual two lift coefficients remain unselected. This does not prove that either projective class occurs for an HM source, determine any actual higher symbol, or exclude a source.

The verification here is independently assembled exterior algebra and exact polynomial ideal arithmetic over Q(sqrt(5)), with all direction variables p,q,t and pencil variables alpha,beta indeterminate. It never selects actual HM coefficients, parameters, points, matrices, or instance ranks.

## Inputs and normalization

INPUTS.json retains immutable commit URLs, SHA256 digests, and Git blob hashes. Relevant direct inputs are PR1025 at 09f1377f83b027ca27eea0b3a9f40a1b92c6c466, PR1005 at 4a50853a6b6a4f18f1a7aac06a90e33e78e7787e, and the exact universal-symbol script at 6c724c3b74e2ae4d6992d8c7b99b41c0715d69c0. All retained bytes were checked against both hashes. All three direct inputs were freshly fetched through the GitHub connector at their exact commit references during this independent review. The returned UTF-8 contents matched the retained bytes exactly, and both SHA256 and Git-blob SHA1 values were recomputed and matched. The matching blobs are: universal-symbol script 0ff4a2fd717842d8df9cf3ce3e3d29fd189bcd6e; PR1005 ba88e70e50342eef9c92db9053789cb238802dee; PR1025 d036adcf5bc2bfc53e07cd752ff180c5993251f7. This authenticates those three dependencies, not a fresh replay of every transitive source theorem. The source script was inspected but not executed, since unrelated portions perform specializations unnecessary here.

Let A=Sym²W, D=Sym⁴W, S=Sym⁶W, V=ker(Pi), and P=S/V. In ascending y-degree monomial bases, Pi is exactly the pinned P6 matrix. Use the invariant apolar forms G_n with antidiagonal entries (-1)^i/binom(n,i). Set

E=G6^(-1) Pi^T (Pi G6^(-1) Pi^T)^(-1), GP=E^T G6 E.

Then Pi E=1 and E embeds P as V-perpendicular. In particular the apparent quotient endomorphism rho_P is the canonical orthogonal compression Pi rho_6 E, not an assertion that the full SL2 action preserves V. Only finite-group equivariance is claimed and needed.

For a=p x²+q xy+t y², let M_a:D→S multiply by a, L_a=Pi M_a, L_a*=G4^(-1)L_a^T GP, and rho_n(a)f=a_x f_y−a_y f_x. The two maps are R1=rho4(a)L_a* and R2=L_a*rho_P(a).

## Dimension and spanning

The finite-group equivariance of Pi, E, the apolar adjoints, multiplication, and the Hamiltonian action makes both R1,R2 equivariant homogeneous quadratic maps P→D. The A5 character computation gives

Hom_G(P,D tensor Sym²A) dimension 2,

since Sym²A=1+D and the class data are sizes (1,15,20,12,12), chi_D=(5,1,−1,0,0), chi_P=(4,0,1,−1,−1). The independent coefficient matrix of R1,R2, expanded in all six degree-two monomials in p,q,t, has rank two. Hence these maps form a basis of the full space. PR1025 identifies this space isomorphically with the quotient-third gate; no extra source-occurrence assertion is required or justified.

## Full homogeneous coefficient ideal and projective locus

The check takes the wedge of all four columns of alpha R1+beta R2. This computes all five maximal minors by iterative exterior multiplication, independently of the author's permutation determinant routine. Each minor is homogeneous degree eight in p,q,t and degree four in alpha,beta. All 115 nonzero direction coefficients generate the following exact ideal over Q(sqrt(5)):

I=(alpha^4−beta^4, alpha^3 beta+beta^4, alpha² beta²−beta^4, alpha beta³+beta^4)
 =(alpha+beta)(alpha,beta)^3.

The displayed Groebner basis was computed in the independent review. Dividing every coefficient by alpha+beta gives exactly (alpha,beta)^3. Consequently

I : (alpha,beta)^infinity = (alpha+beta).

This is a reduced point of the projective pencil, not just a set-theoretic gcd observation. Independently, the alpha=1 chart gives ideal (beta+1) and the beta=1 chart gives ideal (alpha+1). The divided residual coefficients give the unit ideal on both charts. Thus there is no additional root at infinity and no hidden projective nilpotent thickening.

For a fixed projective pair [alpha:beta], generic direction rank is below four exactly when all direction coefficients of all maximal minors vanish. This is precisely the projective scheme above. Every other nonzero member therefore has generic rank four. This does not assert rank four at every direction.

## Structural factorization of the exceptional member

Let Vmat be any basis matrix of ker Pi and GV=Vmat^T G6 Vmat. Define

J_a=G4^(-1) M_a^T G6 Vmat,
H_a=GV^(-1) Vmat^T G6 rho6(a) E.

Then R1−R2=J_a H_a, exactly as polynomial matrices. Conceptually, rho6(a)M_a=M_a rho4(a), because rho(a)a=0. Taking apolar adjoints, for which rho is skew-adjoint, gives rho4 M_a*=M_a* rho6. Insert 1=E Pi+pr_V to obtain the displayed factorization. The omitted V6 is three-dimensional, so exceptional rank is at most three everywhere.

An independent symbolic computation produced a nonzero 3×3 minor of the first three rows and columns of R1−R2. Its p^6 coefficient is −81/3200, which is nonzero; this is a formal coefficient test, not evaluation at a direction. Thus its generic rank is exactly three.

## Exact exceptional rank-drop scheme

The independent check computed all maximal minors of J and all 2×2 minors of H. On each of the three affine charts p=1, q=1, t=1, their respective ideals have Groebner basis [1]. Hence J is everywhere injective and H has rank at least two everywhere. These are whole symbolic charts, not selected direction evaluations.

The alternating cofactor vector of H equals exactly

−243 sqrt(5)/2560 · cP(a),  where cP(a)=Pi(a³).

Thus the 3×3-minor ideal of H is exactly the component ideal of cP, up to a nonzero scalar. Since J is a subbundle injection, locally it has a left inverse; determinantal ideals of JH and H therefore coincide locally. It follows that the exceptional rank-drop scheme is exactly the cubic base scheme, not merely the same support.

PR1005 §2 proves that this unique nonzero cubic P-covariant has exactly six reduced basepoints, the C5 axes. Its proof identifies dcP with the unique nonzero original quadratic A-to-P channel, imports its rank drop at the six axes, and uses Euler's identity and rank-two projective derivatives to establish reducedness. We use only this universal base-scheme result, not the source126 occurrence of any symbol.

Therefore R1−R2 has rank three away from those six points and rank exactly two at them; it never has rank one or zero at a nonzero direction. Its generic kernel is the cubic line spanned by cP. At a basepoint cP vanishes and the fiber kernel becomes two-dimensional; the generic cubic-kernel wording must not be extended there.

## Reproducibility and limits

The independent reviewer executed a separate full-homogeneous exterior-column-product calculation for all five maximal minors, computed the full coefficient ideal and both projective coefficient charts, checked all three direction charts for J and the two-minors of H, and checked the exact H-cofactor identity. A separate exact four-generator calculation verified the quotient, apolar form and orthogonal-section equivariance. Every check passed. These independent calculations are described here as executed cross-checks, not as additional bundled executables.

The bundled primary reproduction command is `python verify.py`, run from this packet's directory; `python -O verify.py` also retains the production check machinery. The primary verifier and model implement the normalized identities and full coefficient-span certificate described in PROOF.md. Their output is retained in RESULT.json. The mathematical review does not rely on a numerical sample or on the primary script alone.

The numerical constants and exceptional equation alpha+beta=0 depend on this displayed basis normalization. The intrinsic conclusion is a unique nonzero projective rank-defective lift, with the above factorization and six-point exceptional fiber degeneration. Nothing here evaluates the actual source's coefficient pair or decides its conditional higher-obstruction branch.

## Final author-text signoff

Reviewed the completed author PROOF.md, SHA256 7afb4f1c03d2077e158aaa5be9570cfc9d28f1f8b631d610b2fcca07c135e446. PASS without requested correction. The additional kernel-sheaf statement is sound: the kernel is reflexive by the depth lemma on the smooth surface, hence a line bundle; the cubic cofactor section has no divisorial common zero, so O(-5) identifies with that kernel. Its zero fiber vector at six points does not contradict the sheaf identification, since specialized kernels need not commute with base change. The explicit compressed action and its square formula are consistent with the model. An additional independent exact calculation confirmed the pinned quotient, apolar form and orthogonal inclusion on all four stated binary-icosahedral generators.
