# Independent mathematical review

Proof reviewed: SHA-256 ec7569ebe8eb46dfe1ab152b32c818bc2c9f98c9975b72fcd964cae882ce5b7f.

Verdict: PASS, conditional on the explicitly cited geometric and cohomological predecessors. This is mathematical text review, not formal verification.

## Checked deductions

1. Twisting the fixed-cubic locally free resolution by minus two gives the stated exact cohomology sequence. The three image sequences use only the cited H2 and H3 vanishings of E(-2), H2B(3)=0, vanishing intermediate line-bundle cohomology, and H0 of ell squared twisted by minus two. The resulting dimensions are 40,100,75,15. The first map is the natural cup product.
2. The common determinant-line identification from duality is retained. It identifies the quadratic residue dual with the restriction cokernel, compatible with the cubic and degree-five identifications. Multiplication therefore gives one simultaneous tuple condition, rather than two unrelated choices of constants.
3. The exact sequence separating L/(L intersect U) from the residual quotient is the ordinary quotient-space exact sequence. Primary module coverage is sufficient for L contained in U by naturality; the proof correctly does not assert necessity or coverage for the selected pair.
4. For coprime global forms, vf=ug forces (f,g)=c(u,v). The kernel of the quintic map is therefore precisely the tuple classes supported on common contained lines. At least one line is not common contained, by injectivity of quadratic restriction, so the kernel dimension really is k.
5. When C avoids V(u,v), the two restrictions are coprime on each line. Divisibility and degree equality supply a common constant on each component. This proves surjectivity onto the quintic intersection. Merely having no common contained component is correctly distinguished from this stronger hypothesis.
6. The Eagon–Northcott terms and determinant twist in (13) are correct. In the transverse local normal form, exactness is equivalently Koszul exactness after removing split summands. Its image sequence gives H1(K) injecting into D tensor H2B(-5). The quotient of global quintics by the six minors is H1(K), since H1 of the trivial bundle vanishes. Trace-free endomorphisms are self-dual, hence Serre duality identifies the dimension with h2B(0), bounded by two in PR455.
7. The saturation argument does not confuse sheaf generation with global generation in degree five. Horrocks–Mumford Theorem 3.5 gives all invariant quintics dimension six, and the argument on printed page 73 identifies the exterior square of the invariant section space with that invariant quintic space; the following argument proves all sections invariant. These source statements identify the actual minors with the whole invariant subspace in the ordinary polynomial linearization. Thus any additional quotient has no invariant part, while a nontrivial Heisenberg character would bring an entire orbit of size 24. Its dimension at most two excludes it. The conclusion h0(I_C(5))=6 follows.
8. The lower and upper bounds follow by dimensions of the exact sequences, retaining the primary contribution of at most eight. No claimed bound is promoted to vanishing of the original Q5.

## Evidence boundary

The reviewed deductions use the pinned transverse geometry, primary cohomology, fixed-cubic duality construction, PR455's structural bound, and the primary HM invariant-section facts. The relevant primary text and the cited structural proof were inspected. No selected HM/source-instance evaluation, matrix rank calculation, parameter search, generator/checker, or large computation was performed. No original-pair emptiness, primary coverage, or quintic-intersection assertion is established here.
