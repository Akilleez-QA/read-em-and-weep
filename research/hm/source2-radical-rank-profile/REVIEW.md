# Independent review of the degree-six V-channel image pencil

## Verdict and reviewed version

**Verdict: the stated theorem follows from the cited structural inputs.**
No mathematical defect was found in the reviewed argument. In particular,
the proof establishes the entire fixed-variable image pencil, not only its
three characters or a generic fiber-rank statement.

Reviewed file: `PROOF.md`, titled *The degree-six image pencil of the
source2 V-channel radical*.

Reviewed SHA-256:

```text
0d4eb3e4e9e98dd9ea8202399590f9741c06771411d5ce40e69a139c461b3798
```

Review date: 2026-10-22 (UTC).

This is an independent deductive review of the written structural proof.
It is **not proof-assistant certification**, a calculation with the actual
source2 tensors, or a proof that an actual HM source exists. Its
actual-source conclusion retains exactly the conditional status stated in
the proof. The underlying published source hypotheses are inputs, not
assertions newly established by this review.

## Exact public dependencies inspected

The following files in `Akilleez-QA/read-em-and-weep` were retrieved and
read at the exact immutable commits cited by the proof. The audit checked
the specific statements used, rather than substituting a current branch
version or an abstractly chosen model.

1. [PR754: abstract balanced degree-eighteen systems](https://github.com/Akilleez-QA/read-em-and-weep/blob/044add76ebb14043a0edf73171517c90b9ef0c13/research/hm/order-four-quadratic-load/ABSTRACT-DEGREE-EIGHTEEN-BALANCED-SYSTEMS.md),
   commit `044add76ebb14043a0edf73171517c90b9ef0c13`.
   Sections 3–5 give `V18=f12 V6`, identify `f12 P6` as the unique
   b-zero endpoint, and identify the balanced locus as the complement of
   the two exceptional parameters.
2. [PR786: endpoint Wronskian](https://github.com/Akilleez-QA/read-em-and-weep/blob/575c0720268af5bb4b305e29284f65614ba9f9ca/research/hm/source2-endpoint-wronskian/PROOF.md),
   commit `575c0720268af5bb4b305e29284f65614ba9f9ca`.
   Section 1 supplies the projective orbit sizes, uniqueness of the
   reduced twelve-point orbit, and perfectness of the binary group.
   The stronger endpoint Wronskian classification is not needed here.
3. [PR789: residual coupling normal form](https://github.com/Akilleez-QA/read-em-and-weep/blob/2d1642ad40ae1111b84b50eeaca0426bfbfbb314/research/hm/source2-residual-coupling-normal-form/PROOF.md),
   commit `2d1642ad40ae1111b84b50eeaca0426bfbfbb314`.
   Its graph description preserves the genuine endpoint quotient for
   every coupling. Section 6 supplies the actual annihilator exact
   sequence, independently of a constant splitting of the residual.
4. [PR790: first constant block](https://github.com/Akilleez-QA/read-em-and-weep/blob/af0e03d26da5e47d18ae732291aca46f4d448dc5/research/hm/source2-first-constant-block/PROOF.md),
   commit `af0e03d26da5e47d18ae732291aca46f4d448dc5`.
   This gives the genuine constant separation of the degree-ten block.
   Section 6 identifies the natural cohomological reconstruction with
   the original fixed pencils, using one common variable convention.
5. [PR791: exact source2 endomorphism algebra](https://github.com/Akilleez-QA/read-em-and-weep/blob/2cd033a4a5ba549d07330427cd779364cb83c0fb/research/hm/source2-pencil-endomorphism-algebra/PROOF.md),
   commit `2cd033a4a5ba549d07330427cd779364cb83c0fb`.
   Sections 4–7 identify the one-dimensional V channel in the
   square-zero radical and justify its contravariant transfer to the
   fixed-pencil endomorphisms. The retrieved proof's SHA-256 was checked
   to equal the cited value:

   ```text
   8b0a5b22fd5221b7532befaee121dcf42edf0bbbc249141b8e029c957c527290
   ```

The direct dependencies support the exact normal-form data stated in
Section 1 of the reviewed proof. In particular, the residual quotient is
not replaced by a chosen lift, and the actual-source transfer is stronger
than a comparison of representation characters.

## 1. Division by the orbit form is valid globally

For a nonzero V-channel map, full constant span of the endpoint ensures
that its restriction to `C=O(-18)` is nonzero. The identity
`V18=f12 V6` gives its factorization through `O(-6)` as a map into the
constant degree-ten block.

The proof then correctly verifies the essential extra assertion: the
divided map lands in `U=U_8^10`, including over `D12`. The quotient
`Z=(V0 O)/U=W O(9)` is locally free. The composite of the divided map
with `Z` is killed by multiplication by `f12`; a nonzero local equation
cannot annihilate a section of a locally free sheaf on the integral
curve. Thus that composite is zero everywhere. Merely knowing containment
away from `D12` would not have justified division in a nonsaturated
target, but the torsion-free quotient supplies precisely what is needed.

The resulting nonzero invariant map

```text
q_V: U* = Sym^8 W O(2) -> O(6)
```

has, on sections after twisting by `-2`, a nonzero equivariant map
`Sym^8 W=P+D -> Sym^4 W=D`. Multiplicity one makes it a nonzero scalar
multiple of the D projection and hence surjective. Its twist-`-1`
section map is that projection tensored with `W`, followed by ordinary
multiplication into `Sym^5 W`; it is also surjective. These statements
use the full spaces of universal sections and require no instance test.

The constant projection `p` and `q_V` form the genuine evaluation-sequence
morphism (13). Its map `g:E0 -> E_V` is therefore an actual sheaf map,
not a putative map inferred from matching characters.

## 2. The degree-six syzygy bundle is identified correctly

The orbit-size bound proves that `V6` is basepoint-free. Its evaluation
kernel has rank two, degree `-6`, and no global sections. If its ordinary
splitting were unbalanced, its unique maximal-degree line subbundle would
have underlying bundle `O(-1)` or `O(-2)`. This subbundle is intrinsic,
so it is G-stable. Perfectness removes the possible character twist in
its linearization. An equivariant inclusion into `V6 O` would then imply
a V constituent in `Sym^1 W` or `Sym^2 W`, which is impossible.

Consequently the kernel is ordinarily `O(-3)^2`. Taking
`K=H^0(E_V(3))` gives its equivariant coefficient representation. The
inclusion into `V6 O` places the two-dimensional `K` inside

```text
V tensor Sym^3 W = W' + S + T.
```

This identity follows from the displayed Clebsch recurrence and products;
it has exactly one two-dimensional summand and no trivial summand.
Semisimplicity therefore forces `K=W'`. Hence

```text
E_V = W' O(-3),
H^1(E_V) = W' tensor W = P.
```

The evaluation exact sequence additionally identifies this last space
naturally with `Sym^6 W/V6`. Thus the identification needed for the second
pencil is a quotient-of-sections identification, not only an abstract
representation isomorphism.

## 3. Generic first jets and the determinant divisor are sufficient

Apolar duality identifies `E0` with the complete first osculating bundle
`U_1^10=W O(-9)`. Restricting the constant projection `p` to this bundle
is dual to the first-jet map of the unique degree-ten V subsystem, with
the same symplectic point convention. No point or derivative value is
selected in making this identification.

That subsystem has no base divisor because its degree is less than the
smallest projective orbit size. Its independent sections define a
nonconstant morphism. In characteristic zero a nonconstant function-field
ratio has nonzero differential, so its value and first derivative have
generic rank two. This supplies the nonvanishing of `det g`; no
everywhere-jet-spanning assertion is being assumed.

The determinant is an invariant section of `O(12)`. Perfectness makes
the coefficient determinant characters trivial. Every nonzero invariant
effective divisor of degree twelve must be the unique reduced orbit
`D12`. It follows that `g` is an injective sheaf map with cokernel of
length one at each of these twelve points:

```text
0 -> E0 -> E_V -> T12 -> 0.
```

A simple determinant zero also gives fiber rank one at each point of
`D12`, and rank two elsewhere. Most importantly, `H^1(T12)=0` gives
surjectivity of `H^1(E0) -> H^1(E_V)`. The proof correctly derives the
degree-four image from this cohomological surjectivity, not from
pointwise rank or representation multiplicities alone.

## 4. The endpoint injection uses the correct balanced-locus condition

The inclusion `j:V6 -> H_t` is constant: it sends a coefficient vector
to its degree-eighteen form `f12 v`. The associated line-bundle map is
multiplication by `f12`, which is injective as a sheaf map but is not a
subbundle inclusion along its zero divisor. The snake-lemma sequence in
Section 5 correctly keeps that divisor term:

```text
0 -> E_C/E_V -> (A18+P_t) O -> O(18)|D12 -> 0.
```

This proves that `E_C/E_V` is locally free, hence that `E_V` is saturated
in `E_C`. Its space of global sections is the restriction kernel of
`A18+P_t` on `D12`. Divisibility by `f12` cannot occur on the A summand,
because `Sym^6 W=V+P` contains no A. It occurs on a P summand only at
`P_t=f12 P6`, the b-zero endpoint excluded from the balanced locus by
PR754. Equivariance and the inequivalence of A and P rule out cancellation
between their images. Thus `H^0(E_C/E_V)=0` for every balanced endpoint,
which proves injectivity of

```text
H^1(E_V) -> H^1(E_C).
```

This is the required actual-map argument. Neither the abstract splitting
of `E_C` nor the occurrence of a P constituent would have sufficed by
itself. The proof makes no inappropriate extension across the excluded
b-zero endpoint.

## 5. Arbitrary residual coupling does not destroy the injection

For every allowed coupling the genuine endpoint projection and
intersection give

```text
0 -> E_C -> E_R -> T O(-3) -> 0.
```

Since the last term has no global sections, `H^1(E_C) -> H^1(E_R)` is
injective. Dually the actual quotient `R -> C` gives the subbundle
inclusion `C* -> R*`, which remains injective on sections after twists
`-2` and `-1`. Therefore the morphism from the degree-six evaluation
sequence into the residual sequence is injective in all three
reconstructed spaces.

No part of this argument assumes that a chosen bundle splitting is
horizontal, sets the residual graph parameter to zero, or identifies a
nonzero coupling with the split witness. It treats every graph parameter,
and therefore both constant-gauge coupling classes.

## 6. The full pencil factorization establishes the image

Dualizing the V-channel constant endomorphism gives a map supported from
the dual degree-ten block into the dual residual block. Its constant,
quotient, and kernel maps are exactly the composites displayed in
Sections 2, 5, and 6. Natural cohomology consequently factors its pencil
endomorphism through the degree-six evaluation system.

The first factor is surjective on the three reconstructed spaces by the
two section calculations and the determinant-cokernel argument. The
second factor is injective by the endpoint and residual arguments above.
Hence its image is exactly

```text
Sym^4 W -> Sym^5 W -> Sym^6 W/V6,
s |-> l s,          s |-> [l s],
```

with image characters `(D,T,P)` and ranks `(5,6,4)`. Naturality ensures
commutation for each of the same linear forms `l`; there is no independent
reparameterization of either pencil. The square-zero assertion follows
from the constant map's support and the contravariant transfer, which
preserves square-zero even though it reverses composition.

Multiplication by a nonzero linear form is injective on `Sym^4 W`.
Moreover `l Sym^5 W` is the hyperplane of degree-six forms vanishing at
the zero of `l`. Basepoint-freeness of `V6` gives
`l Sym^5 W+V6=Sym^6 W`, proving that the second pencil is surjective for
every nonzero `l`, not only generically. The natural constant
reconstruction has constant space `V6`, as asserted.

## 7. Sheaf images, saturation, and cohomological images

The distinction made at the end of the proof is necessary and correct.
More explicitly, three different objects must not be conflated:

- The literal kernel-side image is `g(E0)` inside the embedded `E_V`.
  Its quotient in `E_V` is `T12`, so it is not saturated. Since `E_V`
  is saturated in both `E_C` and `E_R`, the saturation of this literal
  image in `E_R` is `E_V`.
- The exact degree-six evaluation sequence has kernel `E_V`, constant
  space `V6`, and quotient `O(6)`. It is this exact system that mediates
  the image-pencil factorization. The sequence obtained by taking the
  literal sheaf image at every term of the original morphism need not
  be exact at its middle term; here its discrepancy is precisely `T12`.
- The cohomological image is the embedded `H^1(E_V)=P`, because
  `H^1(g)` is surjective and the subsequent `H^1` maps are injective.
  It is not determined by the fiberwise rank drop of `g`.

There is a related quotient-side distinction. The quotient image is
`f12 O(6)` inside `C*=O(18)` and then inside `R*`. It is isomorphic as a
sheaf to `O(6)`, but is not saturated in `C*`; its saturation is `C*`,
and the discrepancy has length twelve. Thus one must not replace the
quotient image by its ambient saturation and still call the resulting
object the degree-six image system. The relevant exact degree-six
evaluation system is obtained using the quotient image with its natural
`O(6)` identification and the saturated evaluation kernel `E_V`.

These distinctions reconcile the degeneration along `D12` with the exact
rank profile of the three finite-dimensional pencil spaces.

## Scope of the approval

The proof supplies a uniform necessary constraint over the whole stated
balanced normal-form family and both residual coupling classes. Changing
a nonzero generator of `f12` or of the one-dimensional V channel only
rescales identifications; it does not change the image subspaces or
their fixed-variable pencil isomorphism type.

The audit used structural representation identities, exact sequences,
saturation, characteristic-zero generic separability, and natural
cohomology. File hashing was an integrity check only. No actual-source
coefficient, parameter, point, derivative value, matrix, rank, selected
model, scan, or large computation was used. No actual HM endomorphism
algebra was measured, and no realization or source exclusion follows
from this approval.
