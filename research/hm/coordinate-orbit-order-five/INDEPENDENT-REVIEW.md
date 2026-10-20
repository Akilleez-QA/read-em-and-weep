# Independent mathematical review

Verdict: PASS.

Reviewed artifact: `PROOF.md`, SHA256 `ed36858dc2b7d5bf24df12a167739867d5333febb821d2fa590ae59cfd797e6c`.

## Checks

1. **Frame separation.** Evaluations at closed points span the dual of any finite-dimensional space of projective-space sections, with evaluations understood as maps to the corresponding one-dimensional fibers. Independent evaluation is a nonempty open condition on ordered tuples. The frame-extendible locus is likewise nonempty open for r at most n+2. Irreducibility ensures these opens meet. Transitivity on ordered frames then gives a translate whose r evaluations separate W. Every section vanishing scheme-theoretically on the translated N vanishes at these support points. The same moving-point evaluation condition is open on PGL. Thus no assumption that N is reduced or projectively normal is used.

2. **Binary-quartic geometry.** A diagonal SL2 torus scales a highest-weight fourth power through all nonzero scalars over C; positive-degree invariant homogeneity forces I and J to vanish there. Equivariance gives the entire rational normal quartic. Degree-four interpolation makes every five distinct points independent, so any six distinct points are an ordered projective frame. Coprimality follows from nondegeneracy of I and absence of invariant linear forms, with the nonzero cubic J retained as a hypothesis from the cited invariant identification.

3. **Simultaneous coordinate orbit.** The convention u_g=(g inverse)*u0, v_g=(g inverse)*v0 gives V(u_g,v_g)=gN0, not its inverse translate. The degree-five polynomial ideal piece is contained in H0(I_(gN0)(5)); the proof only uses this containment and does not need saturation equality. PGL acts on forms up to nonzero scalar, which leaves the zero schemes, ideal pieces, multiplication images and quotient Q5 unchanged.

4. **Intersection of opens.** Nondegenerate quadrics form one projective PGL orbit. The primary-good open of PR449 meets the smooth-quadric locus by irreducibility. Each fixed line imposes a proper closed containment condition on smooth quadrics; a finite union does not exhaust that orbit. Pullback gives nonempty open subsets of PGL, whose intersection with the separation open remains nonempty because PGL is irreducible. No assertion that a generic independent cubic remains generic in a restricted family is made or needed.

5. **Residual and primary closure.** The dependency statement used from PR458 is its injective quintic map when there are no common-contained component lines, not its stronger surjective identification requiring avoidance of every common point. The no-contained-quadratic-line condition makes k=0, and separation makes the target quintic intersection zero. Its exact sequence 0 -> L/(L intersect U) -> Q5 -> R -> 0 then kills Q5 using uM1=M3. The endpoint conclusion uses PR451's two-copy identification, not an inference from primary generation alone. The relevant dependency arguments were checked against the available PR458, PR449, PR443 and PR451 proof texts; their previously established inputs remain explicit dependencies rather than newly reproved theorems here.

6. **One-parameter family.** For an existential lift G of a good g, H(t)=Id+t(G-Id) is invertible at both 0 and 1. Its determinant principal open T is irreducible and contains both points. The regular map to PGL has a nonempty inverse image of the good open because it contains 1; its complement is a proper closed subset of an open affine line, hence finite. H(t) also supplies an actual GL lift, so the transported coefficients can be chosen regularly on T. The conclusion concerns generic parameters, without implying the identity parameter is good or bounding its torsion length.

## Limits

The proof establishes existence and a nonempty open good locus inside the simultaneous coordinate family, with F fixed. It does not evaluate the original selected pair or a selected actual source instance. It neither asserts GL-equivariance of F nor upgrades coefficient-family algebraicity to quantization or module algebraicity. No computations, searches, multiplication matrices, or formal proof assistant were used in this review. This is independent mathematical review, not formal verification.
