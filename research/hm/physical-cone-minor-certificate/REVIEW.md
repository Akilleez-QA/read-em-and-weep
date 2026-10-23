# Independent review of the fixed-minor global cone interface

2026-10-23. PASS for the stated conditional construction and its strict domain.
This review supports, but is not itself, the new constructive deduction.
No actual HM coefficient, parameter, matrix, rank, primitive or response was
selected or evaluated. No proof-assistant verification is claimed.

## Frozen reviewed bytes

- PROOF.md SHA256: ee1983bcf0ab2fbbbb252275a04bcc296bae284162b9375de0813a11280428a6
- verify_minor_certificate.py SHA256: 6c0c817ada6cc9fea75848a1e58cd9f1a482a5ca2136ad9ac11dd5043ffd8884
- README.md SHA256: 5dbd9571664b3431b91da7710d230c06af28cbaecc12aee10f27b764189fa1a1
- SOURCE-MANIFEST.json SHA256: 6cbd627c975fb8969747e1de3c902ac441e8e2a51a74fc713fb7f1523e73477a

I read the full proof and code, and the complete pinned PR908 and PR914 input
copies. Both input hashes match the immutable pins stated in the proof. This
review checks the deduction from those supplied exact inputs; it does not
reprove their complete geometric ancestry or authenticate an actual HM packet.

## Independent derivation

Let C=D[:,J] and R=D[I,:], with B=D[I,J] invertible and delta=det(B).
The rank residual is delta D=C adj(B) R. It writes all columns in the span
of C; the nonzero minor makes these r columns independent. Hence the rank
is exactly r, not merely at least r. With T=E_J B^{-1} P_I, this gives DTD=D.
Consequently DT is an idempotent with image exactly im(D), and I-DT has
kernel im(D). Its selected I rows vanish because B B^{-1}=1. The remaining
m-r rows have rank m-r, so the stated complete residual dimension is correct.
It is not the dimension of the closed-source cohomology obstruction.

The descent identity L=LTD is equivalent to L killing ker(D): the reverse
implication follows by applying L to x-TDx, which lies in ker(D). These are
split finite-dimensional vector spaces over k, so extending scalars to any
k-algebra of regular chart functions preserves the reasoning. No assertion
about a variable-rank differential over an arbitrary coefficient ring follows.

For an exact source s, Ts is a primitive and LTs is its unique extraction
value. This proves M3 and its agreement with PR908's factor. Another certified
pivot gives a primitive differing by ker(D), proving M5 only on im(D).
Outside that image the two extensions can disagree, as the explicit all-ones
2-by-2 example in the tests demonstrates. Thus no physical meaning is assigned
to a well-defined but off-image numerical extension value.

The empty pivot case is also sound: delta=1 and N=0 force D=L=0; membership
then requires s=0. A nonzero minor alone is insufficient in positive rank,
and the full nonpivot columns are correctly included in both certificates.

## Regularity and physical limits

The fixed global D has entries in k, not source parameters a or h. Its
certified delta is therefore an invertible scalar in every physical chart.
The formula preserves the whole polynomial source family and creates no
new exceptional source divisor. By contrast, D=[t] and s=1 over k[t] satisfy
the cleared membership identity but require primitive 1/t. The proof and
code explicitly restrict this alternative to localization, and do not infer
global membership or extend across t=0.

The optional finite-group average is valid: averaging a right inverse on
im(D) remains a right inverse by equivariance of D, and its difference from
T lands in ker(D). This does not make the separately supplied physical
extraction or contraction equivariant.

M6 is substitution into the existing PR908 formula after authentication
and matching. The proof correctly retains PR914's full-cover regularity,
tensor compatibility, marking/frame alignment, paired globality and mixed
scalar gluing as separate gates. Algebraic descent cannot authenticate a
physical row. The zero-row diagnostic makes that limitation explicit.
Neither actual matrix data nor the full ambient lower projection y has been
constructed. No source case, witness or original proof-repair obstruction
is removed by this interface alone.

## Independent test evidence

I reran the final verifier in normal and optimized Python modes. Each run
passed 144 checks and rejected all 17 negative controls. The final fixture
includes a genuinely homogeneous cubic family in a0,a1,a2, linear in h;
the degree assertion is explicitly checked rather than inferred from a
mixed-degree polynomial example. Runtime checks use explicit exceptions,
so optimized mode does not remove the certificate gates.

Separately, before reading the candidate implementation, I exhaustively
checked 5,832 synthetic rank-one pivot/row/source combinations: all nonzero
rank-one 2-by-2 matrices with entries in {-1,0,1}, all similarly bounded
rows and sources, and all nonzero scalar pivots. Every accepted source
reconstructed from its selected primitive, and all accepted pivots gave
the same response. An outside-image source for the all-ones matrix gave
different extended values with different row pivots, as required. These
finite synthetic checks corroborate the written algebra, not the HM geometry.

No remaining blocker was found in the frozen theorem or its scoped tests.
