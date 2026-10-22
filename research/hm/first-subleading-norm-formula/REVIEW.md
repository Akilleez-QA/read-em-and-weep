# Independent review: first-subleading fifth-norm formula

## Verdict

**PASS. No blocking mathematical finding.**

Reviewed file: `PROOF.md`.

Final reviewed SHA-256:

`b23dfbf6aaa8a923bbe9873c5a5aad89b26d61bc408080d812bbc563822c3a9f`

The initial frozen version had SHA-256
`98a7532aa80f651225141054c0aed9215c93c397f1e8681bde381a8254bd4255`.
The author subsequently added immutable dependency links, made the standard
negative-chart scalar trivializations explicit, and replaced the ambiguous
two-argument `tau` notation by `tr`. Reversing exactly those editorial changes
in memory reproduces the initial SHA-256. No other proof change occurred.
The reviewer did not edit the proof.

The result is a deductive formula for a global quotient class, conditional on
the stated pinned geometric inputs. It does not evaluate the actual class.
The audit checked the new integration and the exact interfaces below; it is
not a proof-assistant certification or an independent reproof of the entire
earlier HM development.

## Pinned sources checked

The following files were fetched at their exact cited commits, rather than
read only at a moving branch or inferred from PR titles. Returned Git blob
SHAs are recorded for reproducibility. The repository is
`Akilleez-QA/read-em-and-weep`.

| Input | Commit | File below `research/hm/` | Returned blob SHA |
|---|---|---|---|
| PR713 | `5b3943980ecaef78ee7f56fbc015d40955fb24f0` | `leading-vertex-obstruction/PROOF.md` | `fe33455d86f6094f9b5d31350869a4eba066302f` |
| PR692 | `858f96ba1539afb1293f31239b8761af08e46f60` | `vertex-scalar-filtration/PROOF.md` | `bc9a9a2aa1b4d7343de5c4168d93bb8017e155bb` |
| PR774 | `eec909bef4a7e6998737773d5eadd0ad562e79d9` | `matrix-jet-filtration/PROOF.md` | `79b6df5441d7d9bf7038f9de5a7e1756f9ca784d` |
| PR773 | `53209eb6d4e45883ce0f31dd6d9b1c191bd6c4a3` | `fifth-norm-finite-jet/PROOF.md` | `a56dba203fe27dda0aebcec5a3b21dd89ba70f32` |
| PR769 | `1599ab33ec5392433da49fcfbd0bddd5ba1482d3` | `ideal-valued-fifth-norm/PROOF.md` | `a421d2dfbc2aafba50684620ef5d13ac6b561a83` |
| PR770 | `b242300110c33627eb77ee5ab36cc81fffa359e4` | `faithful-fifth-norm/PROOF.md` | `dd0489148189fdc8dfd8d9c18dd8f2d8ea32761f` |
| PR772 | `9cfcea876a88cfdaf774e3b02e7cd05739dbfcc4` | `source-divisor-normalization/PROOF.md` | `5164d88071e2055eab02cdf578e5346170bbc203` |
| PR685 | `449a8df60662bd7a1d93e318ea4f7e6dab28e5ad` | `third-lift-uniqueness/PROOF.md` | `15757d06b0047aaa42c63608618a810786604ac6` |

The following underlying interfaces were also fetched at
`8d8b5be4ce62c3055bb53be9e16d29cc63072f04`, all below
`research/hm/order-four-quadratic-load/`:

- `ACTUAL-CORRECTED-THIRD-NEIGHBORHOOD-LIFT-IS-SQUARE-ZERO.md`, blob
  `66ad91bc7026203d340a7988f679caa1b98b02ce`.
- `UNIVERSAL-SECOND-NORMAL-HARMONIC-PRODUCT-AND-OPERATOR-DEFECT.md`, blob
  `acab5fcac801d0843306d4afb74228191a00b2a4`.
- `NEGATIVE-VERTEX-EVALUATION-SCALAR.md`, blob
  `4d2737b94c19b84816382984db9ecb91af66ef0e`.
- `NO-PRESERVING-POSITIVE-CONE-EXCESS.md`, blob
  `2f90c2c3d816220c0ab3142c2eeb5c2d3c49b74c`.
- `VERTEX-QUINTIC-RELATION-EXTENSION-AND-SQUARE-P4.md`, blob
  `0800677ef4177a96226f490e28d9a2ea948b7678`.
- `POSITIVE-SECOND-BOCKSTEIN-SQUARE-FILTRATION.md`, blob
  `7fe07b9b6971e089abf74b4526fe8adb07d242be`.

## Mathematical checks

### 1. The generic bound is transferred through a regular adapted frame

PR692 and the actual third-neighborhood theorem use the full actual regular
pair, with initial section components of degrees three and five, not a
meromorphic normal form. PR713 supplies the three coefficient bounds
`12,8,4` and eliminates the possible weight-minus-two fourth coefficient.
Multiplication by the negative quadratic `a` has transverse weight zero.
Consequently `K=aJ4` has generic total weighted order at least twelve.

The cubic-first line is the one identified by PR774. Its identification is
consistent with the actual splitting
`E|L=O_L(5)_- direct-sum O_L(-2)_+`: quotient generators and section
components are interchanged by the rank-two Koszul description. A regular
change between cubic-first/quintic-second section frames cannot have a
nonzero constant lower-left entry, since that would create a cubic term in
the second component. No homogeneity of the full pair is required.

Thus the generic comparison has nonnegative weighted order, as does its
inverse. Here coefficients may lie in `C(L)`, but the transverse change is
regular. This is not a meromorphic diagonalization with transverse poles.
An ambient lift of the regular comparison retains its restriction on `L`,
so the same adapted condition applies on the finite `q`-thickenings.

PR774 then supplies the genuine sheaf filtration and locally free graded
coefficient modules along every point of `L`. Each forbidden lower
coefficient vanishes generically and hence vanishes globally. This use of
saturation is legitimate for the ambient matrix filtration. It neither
divides by a source at its zero nor saturates the later source-multiplied
relation image.

### 2. Only weights twelve and sixteen can reach the surviving scalar block

In an ordered physical eigenframe, diagonal physical-even entries have
cover degrees `0 mod 4`; off-diagonal entries have degrees `2 mod 4`.
With the specified shifts, every physical-even matrix weight is a multiple
of four and every regular such matrix has nonnegative weight. A fifth-layer
change `q^4 D` therefore starts at total weight sixteen.

It follows that local fifth lifts have only weights twelve, sixteen, and
at least twenty. The harmonic coefficients of the weight-twelve block stop
at `q^3`; a `q^4` coefficient would have weight minus four. The weight-sixteen
block can have its regular weight-zero `q^4` coefficient `B_4`. Killing this
coefficient is an allowed local correction, not a global or gauge-canonical
normalization.

At scalar total weight twenty-eight, the only product is `12+16`.
The leading self-product has total weight twenty-four, hence cover degree
eight after extracting `q^4`. Every product involving a matrix block of
weight at least twenty has total weight at least thirty-two, hence cover
degree at least sixteen after that extraction. PR773 removes those scalar
ranges in the global norm quotient. Its conclusion is not being inferred
from a generic calculation or from homogeneous square-ideal generators.

### 3. The harmonic pairing has fourteen terms and no extra factor two

The fixed homogeneous harmonic decomposition determines the operators
`H_r`; its coefficient of `q^r` lowers cover degree by `4r`. Entrywise
degrees are used before matrix multiplication. Opposite off-diagonal
shifts cancel in the trace. Scalar commutativity and exchange of the trace
indices give `tr H_r(A,B)=tr H_r(B,A)` even when the relevant entry degrees
differ.

For `n(X)=tr(X^2)/2`, polarization gives

`n(K)_[28]=tr(K_[12] K_[16])`.

The two ordered cross-products cancel the factor one-half exactly once.
There is no further factor two. Extracting `q^4` requires
`r=4-i-j`, with `0<=i<=3`, `0<=j<=4`, and `i+j<=4`.
The row counts are `5,4,3,2`, totaling fourteen. For every pair the trace
coefficient has degree

`(12-4i)+(16-4j)-4(4-i-j)=12`.

The sole term containing `B_4` is `(i,j)=(0,4)`. Setting `B_4=0` leaves
thirteen formal terms. The proof correctly does not claim that all these
terms are nonzero or linearly independent for actual data.

### 4. The scalar reference is retained in the literal local equality

The exact sequence

`0 -> O_Q(16) -> O_(5Q)(24) -> O_(4Q)(24) -> 0`

and `H1(O_Q(16))=0` supply a global scalar reference `P`, independently of
whether the adjoint extends globally. Therefore
`n(K_i)-P=q^4 w_i` and the literal degree-twelve equation is
`(w_i)_12=F_i-p_12`, not merely `F_i`.

The ambient lifting claim has the correct twist: the kernel of
`O_P4(24) -> O_(5Q)(24)` is `O_P4(14)`, since `q^5` has ordinary degree ten.
Its `H1` vanishes. A global polynomial lift of `P` thus exists, and its
fixed harmonic `q^4` coefficient is a global twist-sixteen scalar.
The cover-degree-twelve block is in `Sym12 U tensor O_L(10)`.
A different ambient lift differs by `q^5` times a polynomial and cannot
change the harmonic `q^4` coefficient. Hence `p_12` is ambient-removable,
with no appeal to arbitrary local scalar choices.

The final version explicitly fixes standard negative-coordinate
trivializations. Their overlap units depend only on `L`, so scalar
trivializations do not mix transverse weight blocks. This clarification
matters: arbitrary transverse-dependent scalar units could mix those
blocks, although the full intrinsic norm-error class would still exist.

### 5. Fifth-layer changes land in the actual relation image

Modulo `q^5`, the exact norm change under `K_i -> K_i+q^4D` is
`q^4 tr((K|Q)D)`; the quadratic correction has order `q^8`.
Since `K|Q=fN`, the norm-error change is `f tr(ND)`.
Its degree-twelve part is precisely `f tr(n8 D_0)`.

The formula produces this through its sole `B_4` term:
`A_0=f n8` and `H_0` is ordinary cone multiplication.
The image is the actual degree-eight leading stack-square relation,
multiplied by the whole source `f=a^4h`. This does not justify dropping
any of the other first-subleading coefficients `B_j`, `j<4`.

### 6. The weight-four gauge contribution cancels before extraction

For a physical adapted transition, the leading weight-zero matrix `T_0`
is invertible: its diagonal entries are units on the base and its possible
lower entry has cover degree two. Factoring it leaves a weight-four first
correction `X_4`, with all remaining transition contributions of weight
at least eight. At weight sixteen the only new term is the commutator
with the weight-twelve block, up to the convention-dependent sign.

The trace change is
`tr(K_[12] [K_[12],X_4])=0` by cyclicity. Leading conjugation by `T_0`
also preserves trace. These are ambient algebra identities, not identities
obtained after replacing harmonic multiplication by ordinary binary
multiplication. Their `q^4` harmonic coefficients therefore vanish as
claimed. Individual harmonic coefficients need not be invariant.

### 7. The global source image and exact second-symbol quotient are retained

PR773 identifies the surviving relation sheaf as the image of
`P4 O_L(-2) -> Sym8 U tensor O_L(2)` followed by multiplication by
`a^4h`, landing in `Sym12 U tensor O_L(10)`. The proof keeps that image
unsaturated. A nonzero `a` is a non-zero-divisor on the integral base, but
is not a unit at its zeros; generic division would lose information in
the quotient. The text correctly separates this issue from the earlier
ambient matrix saturation.

The local representatives glue modulo this sheaf image and ambient
polynomial sections by the exact PR769 overlap formula. PR770 identifies
the resulting class faithfully with the raw fifth adjoint boundary.
PR772's full-divisor construction gives the same class: subtract a global
lift of the norm residue on the whole divisor `div(a^4h)`, including its
multiplicities, and solve a regular image equation in ambient invertible
sheaves. No restriction to the divisor complement or inversion on the
square quotient is used. Subsequent conic and lower-vertex normalization
is the pinned natural identification with the `P4` boundary.

Finally, PR685 checks the exact variation for all classified completions
with `a,h,b,U_a` fixed, with source ranging over the full `A+D` space.
The raw fifth-boundary variation is exactly the second-symbol image;
changes of the even fourth lift itself have zero fifth boundary.
Transport through the PR770 and PR772 isomorphisms gives precisely
`T(tau_*(im beta2_a))`. Thus the final quotient is the actual transported
image, not an assumed zero subspace, an arbitrarily selected complement,
or a constant-rank inverse. The two pencil sign conventions have the
same image and do not change this quotient conclusion.

## Scope maintained

The proof supplies a finite bilinear formula for representatives and the
already faithful quotient criterion. It does not determine an actual
coefficient, prove nonvanishing or vanishing, decide membership in the
second-symbol image, or infer further lifting or algebraicity. The review
used symbolic degree and exact-sequence reasoning, source reads, and file
hash checks only. No selected actual HM/source coefficients, points,
matrices, ranks, or derivatives were evaluated; no large computation was performed.
