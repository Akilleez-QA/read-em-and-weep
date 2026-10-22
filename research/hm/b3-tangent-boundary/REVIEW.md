# Independent review: the weight-four tangent boundary extension

## Verdict and frozen artifact

**PASS**, within the reference and retained-weight scope stated in the proof.
No mathematical defect requiring a change was found.

Reviewed artifact: `PROOF.md`.

Final SHA256:

`1a59403c4ebf4cb3e2c15826546006de6a5ed9c099eb05a8d06de1eba740017a`.

The initially supplied artifact had SHA256
`07b745d057f0bab00b06ca9f29ddf284d311ed316d66a464be49979732f4b562`.
The only changes made during this review were the requested immutable links
for its numbered inputs and replacement of an irrelevant final scope phrase
with the mathematical no-large-computation statement. Its mathematical
argument was not changed. This is an independent authored review, not
proof-assistant verification.

The reviewed conclusion is that the particular reference connecting map
`mu(D)=-[M1(D)]` is an isomorphism, proved through an actual morphism of
extensions. It is not a claim that arbitrary nonzero pure `B3` shifts are
realized in the classified actual completion family.

## 1. Pinned source verification

The following exact-commit sources were read through the repository
connector, rather than relying only on local filenames or publication
summaries:

- [PR778](https://github.com/Akilleez-QA/read-em-and-weep/blob/e527b939f9a8f5cf8967f32048a23a9d830d77c9/research/hm/normal-transition-channel/PROOF.md): exact multiplicative ambient `T0`, equation-line convention, marked weight-zero coefficient, and its nonsplit transport.
- [PR780](https://github.com/Akilleez-QA/read-em-and-weep/blob/c82c3a3b6b513e80a5af21f06ecc52170cb0a056/research/hm/transition-boundary-formula/PROOF.md): faithful leading extraction, `J0(4)`, the trace/square-relation identification, and the ordered `-M1` formula.
- [PR781](https://github.com/Akilleez-QA/read-em-and-weep/blob/b1b970d232f1e400a8b1c58caafa9080fdfc92da/research/hm/completion-separated-boundary/PROOF.md): all-point lower weight bound, classified completion differences, and the genuine source-free reference section on `2Q`.
- [PR718](https://github.com/Akilleez-QA/read-em-and-weep/blob/2411fcd92acd738d0d8af7bebc79ee9191b276ef/research/hm/trace-obstruction-target-reduction/PROOF.md): divisibility of the trace numerator by the cubic and the reduced quintic quotient.
- [PR724](https://github.com/Akilleez-QA/read-em-and-weep/blob/2061379fe77ec4c82b5f05c7a11d3b7454b97a04/research/hm/canonical-trace-isomorphism/PROOF.md): the universal normalized quotient isomorphism.
- [The old tangent coefficient](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/ACTUAL-LOWEST-NEXT-ERROR-TANGENT-COEFFICIENT-IS-ACYCLIC.md): the full triangular tangent transport and its physical twist-four kernel.
- [The old quintic/square relation](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/VERTEX-QUINTIC-RELATION-EXTENSION-AND-SQUARE-P4.md): all-fiber regularity, complete quadratic evaluation, the nonsplit quintic-generator extension, and the ordinary stack-square relation.
- [The full homogeneous normal-matrix warning](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/FULL-HOMOGENEOUS-NORMAL-MATRIX-STILL-LOSES-THE-POLYNOMIAL-NINE-SPACE.md): the distinction between coefficient sections and actual global tangent sections.

The fetched PR778, PR780, PR781 and full homogeneous normal-matrix texts
were also compared with their local copies and agreed exactly. The review
uses the theorems at those pins as dependencies; it does not pretend to
reprove every earlier actual-family geometric input.

## 2. The reference extension is the correct sheaf extension

At matrix weight four and physical twist six, the regular trace kernel is
the twist-by-two of the old twist-four kernel, hence `T=U O_L(1)`.
Locally `D=ell[[f,0],[2g,-f]]`. The vanishing upper entry follows from
regularity of `(f,g)` and its degree being below the cubic degree; the
remaining equation forces precisely the displayed form. The cited old
tangent calculation includes the lower-triangular frame contribution, so
this is a bundle identity, not a choice of globally independent `f,g`.

The exact homogeneous transition `T0` really lifts multiplicatively to the
ambient reference: its only transverse entry is linear, and multiplication
of two lower-triangular transitions never multiplies their two lower
entries. This is the key existence input for an honest coefficient bundle.
It would fail for a general harmonic lift of an arbitrary transition.

Restriction of its homogeneous weight-four part to the tangent kernel
has locally arbitrary harmonic lifts `H(D)`. Its kernel is exactly `qX0`.
Division by the invariant normal equation removes matrix weight four and
physical twist two, giving `J0(4)`, not `J0(8)` or an untwisted `J0`.
No `q^2` term survives at this total matrix weight, since its coefficient
would have negative regular matrix weight. Thus

    0 -> J0(4) --q--> E_mu -> T -> 0

is exact, locally free, and has the asserted local expression
`H(D)+qX0`. The harmonic splitting is only local and is not incorrectly
assumed to be compatible with transport.

With target-minus-transport Čech signs, the transported harmonic lift has
the first-order correction `M1(D_j)`, whereas the target harmonic lift has
no such local term. Their divided difference is therefore `-M1(D_j)`.
For a tangent input the upper entry is zero, so its lower-entry transport
has at most the first harmonic correction; no higher harmonic term is
missing. Multiplication by `q^3` gives exactly the retained reference
fifth-boundary contribution from a `B3` change. This checks the particular
boundary map, not just its possible representation type.

## 3. The reference nilpotent is genuine and has the required square

PR781 constructs

    m=H(n8)+qH(T4)

as a genuine source-free section of the `T0` reference on `2Q`.
Its proof uses the exact chart sections `N_r=U_(r^2)/r^2`, dividing only
by the invertible chart generator. The differences between these charts,
and between actual and reference transport, start in total weight twelve.
Consequently their weight-eight pieces agree on reference `2Q`. This does
not require a global actual first-normal nilpotent.

Each `N_r` is square-zero on `2Q`, and its lowest total weight is eight.
The total-weight-sixteen part of its square is therefore precisely `m^2`.
No cross-term with a higher piece can enter that weight. This establishes
the nilpotence hypothesis needed for the PR718/724 first-normal trace
calculation on every regular chart. It also avoids dividing by the fixed
source `a` at its zero divisor. Equivalently, if one uses `U_a`, the
result follows by torsion-free cancellation of the source factor, but the
chart-generator construction already supplies the direct regular argument.

## 4. The intrinsic trace map, twists, and square relation

The trace pairing is invariant under simultaneous reference conjugation.
For `d` in `E_mu`, `tr(m d)` restricts to `tr(n8 D)=0` on `Q`. On `2Q`,
the kernel of restriction is the principal normal ideal. Its division by
the local equation is well defined as a section with the normal-line
twist, independent of representatives modulo `q^2`. Hence

    Lambda(d)=(tr(m d)/q)|Q

is a genuine gluing scalar morphism. It is not an arbitrarily selected
local first-normal trace coefficient.

The scalar physical twist is `2+6-2=6`; its binary cover degree is
`8+4-4=8`. Its coefficient bundle is therefore `Sym8 U O_L(2)`.
For `d=H(D)+qX0`, the expansion is exactly

    Psi(D)+tr(n8 X0).

There is no extra factor two here: the trace of one ordered harmonic
product equals the scalar half-trace of the two symmetrized products
because the scalar harmonic product is commutative and trace is cyclic.
The doubling issue is solely the change of tangent-input convention,
addressed below.

The cubic relation is a nowhere-zero line subbundle
`O_L(-2) -> Sym3 U O_L(1)`. Thus multiplication by its local cubic is an
intrinsic injection

    Sym5 U O_L(-1) -> Sym8 U O_L(2).

The local cubic has coefficient twist three, which accounts for both
line twists in this display. Its image `F` is a subbundle, not a
globally chosen polynomial quintic. The degree-eight ordinary stack-square
relation is `R=f^2 Sym2 U+kfg=fK5`, with
`R=P4 O_L(-2)`. The old complete quadratic evaluation, twisted by minus
one, supplies the exact sequence

    0 -> R -> F -> U O_L(1) -> 0.

In particular the nonsplit transformation of the quintic generator is
retained. Replacing `K5` by independent cubic multiples and a global
quintic-generator line would give the wrong sequence.

PR718 gives `Psi(D)` in `fS5`, and the kernel trace lies in `R`.
Thus `Lambda` lands in `F`. Its restriction to `J0(4)` is the genuine
bundle isomorphism from PR780:

    [[x,0],[z2,-x]] -> u(2fgx-f^2 z2).

Regularity makes it injective on every fiber and identifies its image
with exactly `R`; the local unit `u` is nowhere zero. Neither its
coefficient twist nor a potentially nonsplit lower-entry transition has
been discarded.

## 5. Quotient isomorphism and the all-point issue

The quotient of `F` by `R` is locally

    fS5/(f^2S2+kfg) = (S/(f,g))5,

and the map induced by `Lambda` is division by `f` of the reduced first
normal trace. PR724 uses

    D_old=ell[[f/2,0],[g,-f/2]].

For this convention its formula is `(u/30)i`, where `i` is the regular-pair
socle-duality isomorphism. The current convention is `D=2D_old`, so the
quotient map is `(u/15)i`. This factor is nonzero in characteristic zero.
The proof correctly declines to choose a global numerical scalar between
independently normalized copies of `P4`.

PR724 opens over `C(L)`, so one must check more than the word "generic."
Its actual argument supplies polynomial identities with only fixed
nonzero rational-number denominators, a canonical polynomial nilpotent
lift for arbitrary cubic/quintic forms, and independence of the reduced
map from the chosen nilpotent lift. The remaining duality statement is
the complete-intersection socle pairing for any regular pair of degrees
three and five. The same argument therefore works over each characteristic
zero residue field. It neither requires a square-free cubic nor selects
an actual point or coefficient.

The old relation theorem supplies uniform regularity along all of `L`;
the local normalization unit remains a unit. On every fiber the induced
quotient map is consequently invertible. Since `Lambda` and the quotient
bundles are already defined regularly, a morphism with invertible fibers
is an isomorphism of bundles. This is not extension of an unexamined
generic inverse across a zero divisor.

Both outer arrows in the diagram of extensions are now isomorphisms,
so the middle arrow is an isomorphism as well. Under the old equivariant
identification `Sym5 U=U tensor Sym2 W`, this proves

    E_mu = U tensor Sym2 W O_L(-1).

Both its `H0` and `H1` vanish. The long exact sequence then makes
`H0(U O_L(1)) -> H1(P4 O_L(-2))` an isomorphism. In particular the
extension is nonsplit: a splitting would give nonzero global sections
of its middle term from its positive-degree quotient. No Ext-dimension
or invariant-line count has been used to infer the nonzero extension.

## 6. Equivariance and physical parity

The canonical source-free coefficient in PR781 is independent of the
negative chart generator. The actual marking, homogeneous reference,
trace, equation division, cubic relation, and quotient maps are natural
under `Gamma`. This supplies the equivariance of the morphism and its
connecting map without requiring each chosen frame to be equivariant.

`U` and `W` are the center-odd binary representations. Thus
`H0(U O_L(1))=U tensor W=P4` is center-even, as is the target at its
specified marking. The odd linear cover parameter is paired with the
odd Serre factor to produce an allowed even weight-four matrix. There
is no confusion with the separate Serre involution, no replacement of
the physical quotient by an odd-multiplication-stable submodule, and no
exchange of the inequivalent positive and negative three-dimensional
representations. The stack-square, rather than a coarse annihilator
square, is the relation used throughout.

## 7. Retained norm constraint and actual-source exclusion

For the retained total-weight-sixteen reference change `q^3H(D)`, the
lower piece `K12` is unchanged. Thus its total-weight-twenty-four square
is unchanged. At weight twenty-eight on `4Q`, the only new term is

    q^3{A0,D}=q^3 a^4h tr(n8 D) Id,

which vanishes. Positive normal powers already present in `K12` give
`q^4`-divisible terms, and the square of the correction is divisible by
`q^6`. These are precisely the retained conditions claimed.

The proof expressly does not infer full actual gluing: higher actual
non-`q` transitions may introduce higher-total-weight defects in the
same truncated normal neighborhood. Nor does it infer preservation of
the full actual norm from the leading trace equation. For a legitimate
actual correction `q^3D_full`, polarization of the half-trace norm gives

    n(K+q^3D_full)-n(K)=q^3a^4h tr(ND_full)

on `4Q`. The last-layer injection and torsion-free cancellation of the
fixed nonzero scalar sources give the full trace condition on `Q`.
Local solutions of that condition do not by themselves give global ones.

PR781's complete classified variation has

    Delta B2=-a^2 s_A n8,   Delta B3=-a s_A U1.

Holding `B2` fixed forces `s_A=0` by regular torsion-free cancellation,
not by declaring the source invertible at its zeros. Therefore it forces
`Delta B3=0`. The `D5` and independent fourth-lift directions start too
high in total weight to restore a nonzero pure `B3` shift. The newly
detected nonzero reference directions are not classified freedoms.

The supplementary source-divisor test is correctly limited to a pure
`q^3` change over a fixed third lift. There `K=aJ4` forces `D4=aE4`.
After cancelling the nonzero source in the tangent equation, `E4` is a
global section of the old twist-four kernel `U O_L(-1)`, whose `H0`
vanishes. This is an independent necessary obstruction for that fixed
lower-lift situation, not a replacement for the broader classification.

## 8. Novelty and limitations

The old tangent kernel, old nonsplit quintic and square relation, and
PR724's first-normal trace isomorphism are prior inputs. PR724 already
excludes a nonzero local tangent direction with a first-normal
trace-orthogonal lift. None of these statements alone identifies the
specific reference `-M1` connecting map.

The new comparison is the intrinsic scalar morphism built from the
genuine PR781 reference section, identifying the whole reference lifting
extension with the old quadratic evaluation extension. This is a
substantive map-level bridge. It is not republishing the old twist-four
acyclicity, a dimension count, or the unrelated normal-variation trace
null-homotopy. The normal-matrix warning about the gap between coefficient
and actual global sections is respected explicitly.

This was a targeted comparison with the pinned sources above, not a
claim of exhaustive repository-wide novelty. The theorem evaluates no
actual `beta4`, does not alter its exact classified second-symbol
quotient, and produces no new actual source-ladder freedom. No actual
coefficients, selected points, actual derivatives, matrices, ranks,
source instances, model scans, or large computations were used in this
review.
