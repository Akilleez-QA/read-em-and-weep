# Independent review: complementary sextic system

Verdict: PASS within the stated universal scope. This is a whole written-proof review with independent exact controls, not proof-assistant verification or an additional actual-profile exclusion.

## Frozen bindings

- PROOF.md SHA256: `226ec41be2adb15161a42f243c4c2546ea0da1229f7a5134da1c92d1665c8f4a`.
- verify.py SHA256: `4edf0cc6ea2afdb01d4e2af6cc9d5a7c37235404bd744bcf8e7d6c6ce192e1d7`.
- RESULT.json SHA256: `b648e1f1e94baa70a18df97f364604a2f4c67622c721f52f606bceddcdb0b701`.

The complete proof, checker and reproduction instructions were read. All three full immutable public inputs were freshly fetched independently and match the retained sources byte for byte, by SHA256 and Git blob ID. AUTHENTICATED.json records their public URLs and bindings; originals/ contains those independently retrieved files.

## Mathematical verification

1. The four-dimensional P coefficient system is independent and basepoint-free. Its potential common-zero divisor has degree at most six, less than the minimum twelve-point projective orbit. The evaluation kernel is consequently a bundle of rank three and degree minus six with no sections. Its splitting degrees are at most minus one, so its twist by one has at most three sections.
2. The actual multiplier P tensor W to Sym7 W is equivariant with both sides Wprime plus T, multiplicity one. The Wprime component cannot vanish because the full polynomial multiplication is onto and V tensor W supplies no Wprime. The T component cannot vanish because that would place six sections in the kernel, contradicting the bound three. This proves an isomorphism of actual multiplication maps, not merely equal characters.
3. The resulting vanishing of the linear kernel forces all three evaluation-kernel degrees at most minus two. Their sum is minus six, so the kernel is ordinarily O(-2)^3. Equivariant global evaluation after twisting by two identifies its coefficient representation. Independent class-character identities give P tensor Sym2 minus Sym8 equal to V, proving the exact kernel V O(-2).
4. The twist-cohomology sequence gives every multiplier kernel and cokernel, including the degree-zero failure and degree-one isomorphism. The graded module identifications commute with multiplication and justify the full free resolution. Positive entry degrees prove minimality. The Hilbert vector (1,2,3,4,5,6,3), length24, follows; it is not being used as a substitute for exactness.
5. The apolar argument permits an initially partial coefficient quotient. Its dual injection pulls actual annihilation back to the full universal osculating bundle, whose full annihilator is Sym6 O(-d). All higher-degree source blocks vanish by ordinary Hom degree, leaving the unique scalar P channel. A zero scalar would produce a nonzero constant subspace of the dual quotient, forbidden by its H0 vanishing. Linear-and-higher saturation then forces the coefficient quotient to be full.
6. The high block lies in the constant projection kernel. Rank gives codimension at least n-3. Because that block is a summand of saturated F, it is saturated in the ambient and hence in the constant kernel. If it is nonzero, equal ranks would make it constant, contradicting its negative degrees; this proves the stricter n-2 bound. No arbitrary source summand is treated as horizontal.
7. At d=1 there can be no nonzero negative high block with degree greater than minus one. The proof correctly restricts the stronger sharp model to d at least two. The rank-four multiplication model and its direct sum with W O(-1) in Sym2 W are fiberwise injective, saturated, span their ambient spaces and have the required apolar osculation. Their codimensions attain the bounds. These are universal abstract models, not actual HM realizations. Center-even ambient space forces n even, and the even-n sharp models respect this.

## Exact evidence

The production checker reproduces 3,879 controls, including 2,100 formal monomial apolar identities, identically normally and under Python optimization. Both outputs equal the retained RESULT.json.

The portable independent_check.py in this directory constructs exact class-character values in Q(sqrt5) directly instead of using the production tensor recurrence. It checks the linear isomorphism characters, exact V coefficient kernel and all multiplier characters for degrees one through sixty. It additionally checks the finite splitting possibilities, Hilbert numerator and length, rank/strict-rank inequalities, the d=1 boundary, parity and 2,457 full formal apolar identities on an indeterminate affine coordinate. Its 16,841 controls reproduce identically normally and under optimization. These checks support the written unbounded proof; they do not certify its geometry by themselves.

Run the packet's `python verify.py` and `python -O verify.py`. From this independent-review directory run `python independent_check.py` and `python -O independent_check.py`; these two outputs must equal this directory's distinct RESULT.json. No nonstandard Python package is needed.

## Scope

Accepted are the universal complementary sextic syzygy theorem, sharp multiplier threshold, exact finite quotient and conditional sharp apolar codimension criterion. No actual source parameters, coefficients, selected points, tensors, jets, instance matrices or ranks were evaluated. No stopped experiment was rerun. This result does not identify an actual HM realization, add an actual-profile exclusion, close profile11 or global coverage, or repair the original theorem.
