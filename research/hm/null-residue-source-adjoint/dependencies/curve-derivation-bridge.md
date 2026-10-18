# Curve-derivation implementation bridge

## Result and exact scope

The frozen `Element.V(i)` denotes the invariant derivation V_i on
A = Q(x_0,x_1,x_2,x_3)[y_0,y_1,y_2,y_3]/(y_i²−x_i³+x_i).
Its `jet((i_1,...,i_n))` denotes V_(i_n)...V_(i_1), including repeated axes. The four derivations commute as mathematical operators. No sign, coefficient, basis-mask or quotient-rule defect was found. This closes the source-level derivation sub-obligation previously imported by the moving-frame, raw-scalar and integrated ID0 bridges, subject to the execution/arithmetic premises below. It proves neither a physical value nor ID0=0.

Only inert source text and published proof artifacts were read. No production import, source AST execution, physical model/source/owner/jet evaluation or actual polynomial product occurred. The executable algebra below uses invented free differential symbols, not curve-polynomial data. All writes are local to this deliverable.

## 1. Byte and AST binding

The source is `retained-detector-zero-plan/sources/exact-curve-field/field.py`, SHA256
`4dade295de59741ceb54eb4574c58ffc82c8a1a17063fd1c081656a8b2069b01`.
The frozen source manifest associates it with commit `e93cf712f9da4926a8450cc870ed45a7bfc379ab`; that manifest is provenance, not independent remote verification here.

The published inert candidate is `inert-id0-production-patch/public/candidate-text/exact-curve-field/field.py.txt`, SHA256
`0efb8eff9bacacc9cddad9f29a598479c2c6925cf6472e2733ce4d37e841cc1c`.
All 53 original class methods other than methods named `laurent_coefficient` are AST-identical in that candidate, including V, jet, constructors, partials, multiplication, all Execution methods and inverse. Thus this is also a bridge to that published candidate's unchanged derivation core, without transferring a claim about its added certificate machinery.

`reference-methods.txt` is a reviewed snapshot of eight selected source methods, rendered with ast.unparse. It is an exact source contract, not an independently derived implementation or a second proof oracle. `check.py` compares complete method ASTs (including branches, loops, calls, arguments and returns), ignoring only location attributes; whole-file hashes bind all other definitions. The mathematical interpretation of these bodies is established in sections 2–5, rather than inferred from hash agreement. This report does not authenticate a current remote checkout or deploy a patch.

## 2. Representation, ordinary arithmetic, and rational partial

Put K=Q(x_0,...,x_3), C_i=x_i³−x_i and h_i=(3x_i²−1)/2. For mask m write b_m=product_(i: bit_i(m)=1) y_i. Successive reduction by the four monic polynomials gives a free K-module with basis b_0,...,b_15: adjoining each monic quadratic gives unique remainder of degree less than two in that variable. This needs no unproved numerical independence test and no assumption about a specialized point. In particular C_i is a nonzero polynomial and hence a unit of K; y_i is a unit in A since y_i(y_i/C_i)=1. The theorem only needs this algebra and its rational-x localization, not a separately assumed field structure of A.

A Poly record denotes sum_e q_e x^e. The constructor validates four nonnegative integer exponents, adds duplicate coefficients, deletes exactly zero totals and sorts the result. Its add concatenates terms for that constructor; scale multiplies each coefficient; multiplication adds exponent vectors and multiplies coefficients for every input pair. Thus these loops implement the respective polynomial operations, conditional on exact scalar arithmetic and ordinary Python iteration/storage semantics. No polynomial multiplication was performed in this review. The frozen `Poly.partial` checks the axis, iterates each (e,q), drops terms with e_i=0, and otherwise emits (e−unit_i, q e_i). This is the monomial derivative, including its coefficient and exponent; it never emits a negative exponent. Finite linearity gives the formal polynomial partial on all represented inputs.

A Rational record (N,D) denotes N/D in K; D is checked nonzero. Its constructor's three normalization branches preserve this denotation: zero numerator becomes 0/1; a nonzero constant denominator d rescales N by 1/d; otherwise a nonunit leading coefficient rescales N and D by the same nonzero number. A common polynomial factor need not be canceled for this representation to be valid. Cross-products in equality and ordinary addition/multiplication have their stated meanings by the preceding polynomial rules.

At source lines 321–325, `Rational.partial` returns
(N_i D − N D_i)/(D D).
The exact AST has a subtraction between the ordered numerator products, not addition, and the denominator is D times D. Since K is a field and D≠0, D²≠0. The result is independent of the chosen representative: the polynomial partial extends uniquely to the localization by differentiating D·D^−1=1, obtaining partial_i(D^−1)=−D_i/D². Applying Leibniz to N·D^−1 gives exactly the implemented expression. Consequently cancellation or normalization choices cannot change derivative denotation. The normalized zero case and constant denominators are included in this argument.

The coefficient partials commute. They commute on polynomial generators, and their commutator is a derivation that vanishes on these generators and hence also on inverses by the inverse rule. Therefore it vanishes throughout K.

## 3. Multiplication and the exact V lowering

For any two masks a,b the basis law is
b_a b_b = b_(a XOR b) product_(i: a_i=b_i=1) C_i.
For each axis the unreduced exponent is 0,1 or 2; its parity is precisely XOR and its quotient by two records exactly one C_i for overlap. This proves the rule for every pair, not merely generators.

At source lines 395–407, `Element.__mul__` loops over every input pair (a,c),(b,d), sets q=c*d, loops over all four axes and multiplies q by `rational(curve(i))` exactly when `a & b & (1 << i)` is nonzero, then yields `(a ^ b,q)`. Execution.curve returns x*x*x−x; Execution.y returns the unit singleton mask and coefficient one. Element's constructor merges duplicate masks additively and removes exactly zero coefficients. Therefore the actual multiplication used inside V implements the displayed basis law without extra signs or multiplicities.

Define a Q-derivation on the generators by
V_i(x_j)=delta_ij y_i, V_i(y_j)=delta_ij h_i.
On rational-x coefficients this is V_i(c)=y_i partial_i(c). To see that these prescriptions define a derivation on A, first extend to the polynomial algebra over K using that derivation K→A, then check the relations:
V_i(y_j²−C_j)=0 for j≠i,
V_i(y_i²−C_i)=2 y_i h_i − (3x_i²−1)y_i=0.
Thus the defining ideal is preserved. Inverses of rational-x denominators cause no obstruction because they are units. This establishes Leibniz and well-definedness on the quotient, rather than assuming either from the desired formula.

Now apply this derivation to c b_m. With e=bit_i(m), the exact basis result is
- e=0: V_i(c b_m) = partial_i(c) b_(m XOR 2^i).
- e=1: V_i(c b_m) = [C_i partial_i(c)+h_i c] b_(m XOR 2^i).

The actual source lines 434–435 first construct the singleton `(mask,c.partial(i))`, multiply it by `self.ex.y(i)` using the proved multiplication routine, and append its reduced terms. This contributes precisely partial_i(c) when e=0, and C_i partial_i(c) when e=1, at the toggled mask. Lines 436–440 then act only when the bit is present, construct `(x*x).scale(3)−constant(1)`, scale the entire difference by Fraction(1,2), and append `(mask XOR 2^i,c*rational(dy))`. This is +h_i c at that same toggled mask. It has no remaining C_i factor because the differentiated y_i has been removed, not multiplied by another y_i. Finally Element sums both contributions, so cancellations are retained. The loop over input terms gives the full linear result.

In particular V_i(x_i)=y_i and V_i(y_i)=h_i; the latter is not zero and not y_i h_i. Omitting the second branch would preserve neither the curve relation nor repeated derivatives. Both rational denominator differentiation and the moving-basis derivative occur in the inspected body.

## 4. Repeated derivatives, mixed commutation, and jets

Applying the two-state rule twice gives, for c in K,
- bit absent: V_i²(c b_m) = [C_i partial_i²(c)+h_i partial_i(c)] b_m.
- bit present: V_i²(c b_m) = [C_i partial_i²(c)+3h_i partial_i(c)+3x_i c] b_m.

For the second line, differentiate C_i partial_i(c)+h_i c after the first toggle: partial_i C_i=2h_i and partial_i h_i=3x_i; hence the coefficient of partial_i(c) is 2h_i+h_i. No factorial normalization is inserted. These formulas explicitly exhibit the extra repeated-axis terms that a rule y_i^n partial_i^n would miss. They hold for arbitrary rational c, including denominators, by section 2. Further repeated or mixed derivatives are correct by induction: after each successful application the representation still denotes an element of A, and section 3 applies again.

For i≠j, the commutator [V_i,V_j] is a derivation. It is zero on every x_k because the only possible resulting y has the other axis, and zero on every y_k because h_k depends only on x_k. It is then zero on rational-x inverses and all sums/products of generators, hence on A. Alternatively the two-state rules commute: each axis toggles a distinct bit, C_i and h_i have zero j-partial, and the coefficient partials commute. This proves mixed commutation for all masks and rational coefficients, not just basis constants.

`Element.jet`, lines 444–451, sets result=self and for each supplied axis replaces result by result.V(i), then returns result. Induction on a finite valid axis sequence proves its denotation V_(i_n)...V_(i_1). The empty sequence returns self; repetitions are neither deduplicated nor discarded. Mathematical mixed derivatives may be reordered, but execution counters, budget exhaustion, intermediate representation sizes and object identity need not be equal under that reorder. The theorem concerns successful denotations, not operational equivalence of all runs.

## 5. Executable controls and their strength

Run `python check.py` and `python -O check.py` in this directory. Both yield the same 915-check PASS output. Controls use explicit `require`/raise checks, never Python assert, so -O removes none of the checks. These comprise two input hashes; eight complete AST contracts; 53 common-core AST comparisons to the published candidate; twenty mutation-presence/rejection checks; 512 exhaustive mask-pair parity/overlap checks; 64 repeated-axis and 256 mixed-axis formal-symbol checks.

Ten semantic source mutations are rejected: XOR→OR, intersection→union, wrong curve-derivative sign, missing half, omitted basis toggle, quotient plus sign, unsquared denominator, wrong exponent multiplier, jet reset, and jet reversal. This verifies that the contracts are sensitive to those edits, not that every possible defect is detected.

The invented algebra uses a single formal rational-coefficient symbol c with multi-index derivative labels and free commutative tokens C_i,h_i,h'_i,..., under partial_i C_i=2h_i and partial_i h_i=h'_i. It checks V_i² and pairwise commutation for every mask/axis using symbol-word collection. It constructs no x polynomials, curve-field objects or production jets and never compiles or executes any source AST. Its transition rule is an independent test model of the rule proved from the source above; AST comparison alone does not semantically interpret that model. General correctness, arbitrary-order induction, Leibniz and quotient well-definedness are the mathematical proof above, not inferred from finite checks.

## 6. Remaining premises and explicit exclusions

This bridge reduces the earlier undifferentiated “exact derivation semantics” premise to the following narrow execution/arithmetic premises:

1. Standard Python integer, tuple, bitwise, loop, dictionary and Fraction operations have their usual exact meanings; Fraction normalization and zero/equality tests are correct. This is a source-level proof, not verification of CPython or its standard library.
2. The immutable classes and helper definitions are those pinned here, with no monkey-patching, forged instances, hostile custom iterators, bypassed constructors or mutated Execution internals. Inputs are well-formed objects from one live Execution, and axis sequences are finite valid integers 0..3. Ordinary arithmetic definitions and constructor representation invariants reviewed in section 2 apply.
3. Each operation under discussion returns successfully within the aggregate meter limits. Checks/ticks/observe affect counters or raise; they do not alter exact returned coefficients. Exhaustion is a refusal, not a mathematical result. No resource/admission adequacy for physical ID0 is asserted.
4. Rational-x denominators must be nonzero formal polynomials. All such denominators are units in K. A pointwise/geometric specialization or a smaller legal chart separately requires the appropriate denominator nonvanishing/regular-extension theorem; formal differentiation does not prove that theorem.

General Element inversion remains deliberately unsupported for multi-term y expansions. This does not affect V/jet, which use rational-x operations and multiplication only. Correctness of polynomial long division, Laurent certification/extraction, terminal arithmetic, matrices, source/model identities, owner domains, transport/HPL, global comparison and complete physical evaluation is not proved by this bridge. The published 42 arithmetic controls are separate evidence and are not promoted here to a universal theorem. Existing bridge premises about shape, inverses and geometric inputs remain in force.

The conditional substitution and moving-frame arguments may now cite this source-bound derivation result instead of merely postulating that Element.V respects the curve relation and repeated/mixed differentiation. This does not discharge their separate primitive A identity receipt, whole residual/global comparison or geometric localization obligations.
