# Trace-free request wrappers equal the raw v5 first-current contractions

## Result and scope

For the eight E34 branch requests of PR84 at
`fc7563595b8fd0aeed1675d886b178d43c385bdf` (four each for seeds 12 and 30),
the explicit trace-free wrapper on `normalized_source_ast` is algebraically
the identity. Consequently its selector contraction, all fixed-mask outer
weights, and both quotient-and-frame normal-order coefficients equal the
raw v5 quantities, as rational expressions on each legal overlap. This
proves the currently unresolved *projection-equivalence* proposition. It
does not edit the compiler, change its flags, or discharge any other gate.

The lemma applies equally to every correctly bound first L/U current in
v5, for either E12 or E34. It does not assert that an arbitrary residual,
raw baseline M0, raw normalized second jet, or arbitrary rank-two matrix is
trace-free. It does not prove a detector/null identity, T12F12 realization,
regularized Laurent admissibility, historical-order equivalence, finite
coefficient support, or any product/storage resource bound.

## Source chain (read-only; existing determinant proof not rerun)

Exact URLs and Git blobs are in `source-pins.json`. The files in `sources/`
are immutable retrieved source evidence, not code executed by this package.

1. PR84 `bind_requests.py` at fc756359 fixes v5 commit
   ea2d1a1d2b5774984d0ad48bc15df5fa4d2e0f18 and requests
   `tf(R)=R-tr(R) I/2` on the raw normalized L/U AST. It explicitly leaves
   raw-projection equivalence false. Its seed12 owners are
   `(12,0,5,8,1),(12,1,1,9,9),(12,2,2,11,13),(12,3,4,15,15)`;
   seed30 owners are `(30,i,i,m_i,t_i)` with m=(0,1,3,7,15),
   t=(0,8,12,14,15). No owner, order, or mask is changed here.
2. v5 `physical_current_source_binding.py`, blob
   558516485e0df8b7375b6d34224b2045d51184d7, defines exactly the core,
   physical D frame, Q logarithmic derivatives, tangents, normalized L/U,
   and physical conjugation used below. Its general inverse is retained.
3. Pinned `first-order-source.md` at
   08b73637d4136f91606aad332c46cafd064417f8, blob
   5f4e56252cd9a8a6eb218aceb911c95a1c330ebc, sections 1 and 4, establishes
   det(P_a I_b)=1 for all 36 carrier pairs and the physical transition
   dictionary. `determinant-verification.json` from the same commit, blob
   d36f2f1f0f84e1aae4412ae346487d6663e1d6d4, records all 36 exact rational
   identities by integer-polynomial cross multiplication, not sampling.
   Its model hash is 635bb12d9986e0dcada161d4173c773c4f134b9225354a3bc74267840ca19926,
   exactly the v5 binding's model hash. `attribution-pins.json` also matches
   its source excerpt hash c4f65ff831092d0e56b3e33a0357f44182169fda45943ea780c8c551b4023f94.
   This package imports that already-recorded exact result; it performs no
   new physical polynomial multiplication, expansion, or evaluation.
4. v5 `resolution_selector_source_binding.py` defines K=(r l)^t and
   l Rbar^t r=tr(K Rbar), with matching first-tail owner frames.
   `compile_actual_scalar_differential_kernel.py` retains both Q terms,
   checks that matching owner, and keeps C outside the scalar derivative.
5. `outer-pinned-frames-and-poles.md`, section 2, proves equality of the
   homogeneous physical blocks before differentiation and exact chart
   transport. The result below concerns the prescribed global-finite
   expression and its restrictions; it never differentiates a frozen
   nu=1 or resets an infinity-chart connection.

## Reusable current lemma

Work over a characteristic-zero commutative differential ring localized
where the stated transitions are invertible. Put

    A=C_ab=(P_a I_b)^t, B=C_bc=(P_b I_c)^t,
    D_v=diag(nu_v,nu_v^-1), Q_v=(partial D_v)D_v^-1
       =diag(ell_v,-ell_v),
    T_ab=partial A+Q_b A-A Q_a,
    T_bc=partial B+Q_c B-B Q_b.

All these formulas retain true moving frames. An x-independent multiplier
in nu_v has no effect on Q_v and need not be chosen or set to one. By the
pinned determinant identities, det A=det B=1 as rational functions, not
merely at a point. Jacobi's formula and trace cyclicity give

    tr(A^-1 T_ab)
      = (partial det A)/det A + tr(Q_b)-tr(Q_a) = 0.

For the common-current U exactly as bound by v5,

    Lbar=A^-1 T_ab,
    Ubar=A^-1 B^-1 T_bc A,

so

    tr(Ubar)=tr(B^-1 T_bc)
      = (partial det B)/det B + tr(Q_c)-tr(Q_b)=0.

The A-conjugation in U is essential for its full matrix meaning, but leaves
its trace unchanged. The physical currents are D_a Lbar D_a^-1 and
D_a Ubar D_a^-1, so they too have trace zero. Conversely, conjugating them
back once gives the exact normalized matrices; physical and normalized
entries are not identified. Scalar stripping of invariant y factors
preserves zero trace. These facts hold for every legal mask, carrier pair
including auxiliary carrier 5, and retained standard-chart restriction.

The minimal general hypothesis is partial(det C)=0 and equal endpoint
traces tr Q; determinant one and traceless Q supply it for this source.
A frozen determinant-one value alone is not sufficient.

## Selector and weight lemma

For arbitrary 2x2 matrices K,R,

    tr(K R)-tr(K tf(R)) = tr(K) tr(R)/2.                  (1)

This is the exact missing term. Do not replace (1) by an assumption that
K is traceless: the selector construction K=(r l)^t is rank at most one,
and rank one does not imply trace zero.

The source contracts l Rbar^t r. Its transpose convention is important:
tr((r l)^t Rbar)=l Rbar^t r, by direct entry expansion. The physical adapter
uses Iphys=I D_a, Pphys=D_a^-1 P and Rphys=D_a Rbar D_a^-1;
D_a is diagonal, so Iphys Rphys^t Pphys=I Rbar^t P. The frames therefore
cancel exactly once, preserving the same K and both Q terms. As tr Rbar=0
for Lbar and Ubar, equation (1) vanishes branch by branch for any selector.

For every scalar f in the same ring, tf(f R)=f tf(R); therefore projection
before or after multiplying scalar factors gives precisely the same matrix.
Multiplying by the exact signed coefficient and the product of *all*
fixed-mask outer weights preserves equality. No prefix legal-weight merger,
replacement of a weight by 1, new repeated factor, or division by a weight
is used. This remains an identity at zeros of the weights.

For each scalar numerator P and owned edge denominator D, v5 normal-orders

    C (alpha partial_d + beta)(conversion P/D).

C comprises the signed coefficient, every outer weight, and the selector
contraction. Equality of projected/raw C implies equality of both normal
coefficients A0 and A1, because D, conversion, alpha and beta are unchanged.
No derivative is moved across C. If a later authorized manipulation
differentiates a proved equality, the entire product rule (including weight,
selector, physical-frame, and current derivatives) must be retained; this
lemma is not a license to omit any such terms.

For either seed, write its tail (i,j,k). The E34 branches are:

- edge (j,k), derivative 2, current L_3, sign +1/2;
- edge (j,k), derivative 3, current L_2, sign -1/2;
- edge (i,j), derivative 3, current U_2, sign +1/2;
- edge (i,j), derivative 2, current U_3, sign -1/2.

Indices here are zero-based. The seed coefficient is 2 for seed12 and 1
for seed30. Each individual current has zero trace, so no cancellation
between these branches or between seeds is needed. The edge numerator may
remain arbitrary as in v5; identifying it with T12F12 is a separate issue.

## Baseline versus E boundary

The E operator here is a scalar derivative times a first current, summed
with signs, so its resulting matrix also has zero trace. By contrast,
M0 before projection can have a central component. Products of traceless
currents need not be traceless: diag(1,-1)^2=I. Raw normalized second jets
also need not be traceless even for determinant-one transitions; for
A(t)=diag(exp(t),exp(-t)), A^-1 A''=I. The complete baseline explicitly
projects out central terms, including the central gerbe contribution.
Equation (1) applies to that baseline, but the present proof does not
annihilate its right-hand side.

For example K=diag(1,0), R=I gives tr(K R)=1 and tr(K tf(R))=0.
Thus there is no universal raw-baseline/projected-baseline equivalence.
Whether a particular baseline selector or sum kills its trace requires a
separate source-backed identity. This counterexample only blocks an
universal inference; it is not a physical-source obstruction calculation.

## Controls and release status

`test_tracefree_equivalence.py` uses only abstract rational 2x2 matrices,
formal low-degree jets, and authentication of stored source bytes. It tests
physical moving frames, transported U, arbitrary nontraceless selectors,
weights, the exact missing term, and negative controls for general jets,
baselines and raw second jets. It never imports the physical polynomial
model, compiler, or determinant checker.

Mathematical projection equivalence is established with the pinned
external determinant result as an explicit dependency. All existing
execution, Laurent, T12F12, pole, detector and historical-order gates
remain unchanged and outside this certificate.
