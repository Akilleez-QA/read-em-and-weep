# The rank-four maximal cubic plateau is impossible

## 1. Result and precise scope

Retain the actual geometric hypotheses, fixed physical marking and original
parameter line of `ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md`,
pinned at `db51525015bb7c5e825833d550d08dedf6f6ea96` in `INPUTS.json`.
Then the actual second fundamental form cannot have generic rank four
with maximal consecutive rank-four plateau lengths `(k,l)=(3,3)`.

This excludes that one ordered rank-four stratum. It does not exclude
rank four in another profile, imply rank at least five, establish the
auxiliary square map's surjectivity, or repair the original proof.
The proof uses no actual selected coefficients, parameters, jets,
matrices, instance ranks, or local-model experiments. Its only finite
classification is a newly derived twenty-shape list of abstract rank-four
bundles in a forced slope window. It does not rerun any historical
28/37/159-record enumeration.

The new structural restriction is already useful independently: the
hypothetical six-block plateau would have zero determinant defects,
endpoint degrees `-30,-6`, and block degrees
`-16,-8,0,8,16,24`. Those conclusions use only ranks, total degree,
section persistence, and nonnegative determinant defects. In particular
no invariant-divisor gap is necessary.

## 2. Actual inputs and notation

Work over `C` with `G=SL2(F5)` on the physical `T=P(W*)`, with the
standard determinant-one linearization of `O(1)`. The actual saturated
inclusion is

    0 -> E -> H tensor O -> Q -> 0,
    dim H=30, rank E=17, degree E=-54,
    rank Q*=13, degree Q*=-54.

Both E and its annihilator Q* have no constant subbundle and span their
constant ambients. The named irreducibles use the fixed physical marking:

    1, W, A=Sym2 W, S4=Sym3 W, D=Sym4 W, T6=Sym5 W,
    P, W', V,
    dimensions 1,2,3,4,5,6,4,2,3.

The other even three-space is V, not A. Center-odd representations are
W,W',S4,T6. The center acts trivially on every actual plateau bundle;
a coefficient representation in a summand R O(e) has parity e. The
perfect group has no nontrivial one-dimensional representation. All
irreducibles are self-dual.

The imported ACTUAL cohomology identity is

    H1(E(1))=W'+3T6.                                     (1a)

Together with persistence this will force, by the small degree-deficit
argument below rather than any historical enumeration,

    E=U O(-3)+V O(-4),    U=W'+2T6.                       (1)

The cohomology identity comes from the original actual presentations,
not an arbitrary equivariant rank17 degree-54 bundle. Equivariant
Birkhoff splitting is used only for cohomology and ordinary slope bounds,
never to split an ambient connection.

Suppose the asserted rank-four `(3,3)` plateau exists. Write its actual
saturated stages

    F0 < F1 < ... < F6,    E=F3,
    rank Fi=5+4i,
    Li=Fi/F(i-1),    1<=i<=6.                              (2)

For every interior i, the sheaf derivative kernel is F(i-1), its
saturated forward transform is F(i+1), and the induced derivative

    Li -> L(i+1)(-2),    1<=i<=5,                          (3)

is regular and generically invertible. These are actual kernel and
saturation statements, not generic subspaces used without extension
across special parameters. The endpoint derivative ranks need not be
four; no such assumption will be used. Indeed the upper endpoint has
codimension one.

`EXCEPTIONAL-CUBIC-GAUSS-CORNER-EXCLUSION.md` is retained in full as an
explicit comparison source. Its rank-three pairing inequalities and
rank-three conclusion are NOT imported. Its five dual cubic splitting
types remain a necessary list when k=3, but the present proof does not
need them, and does not enumerate them again.

## 3. Persistence at all stages, including both endpoints

Every Fi with i<6 has no nonzero constant subbundle. Below E this follows
by inclusion; above E a constant subbundle propagates backwards through
the interior derivative kernels to E. Dually every Fi with i>0 spans H.
Thus the reversed annihilator sequence

    Di=F(6-i)^perp in H* tensor O,    0<=i<=6,

has the same interior derivative properties and its stages Di with i<6
contain no constant subbundle.

For any i,d>=0 with i+d<6,

    H0(Fi(d))=0,    H0(Di(d))=0.                           (4)

Here is the universal proof, including i=0. A nonzero section saturates
to an actual line O(-e) in Fi with e<=d. This line is saturated in the
constant ambient because both successive quotients are locally free.
It has e>0, since Fi has no constant subbundle. A degree-e polynomial
vector representing any such line reaches its constant coefficient
span after at most e derivatives: the ordinary derivative-to-coefficient
change of generators is triangular with nonzero factorial diagonal.
No actual vector is chosen or evaluated. Its successive saturated
transforms lie in F(i+j), including the first transform from i=0;
that inclusion follows from the kernel construction at F1. Thus the
constant coefficient span lies in the interior F(i+e), contradiction.
The identical argument applies to Di. This is a sheaf-level argument
on the whole curve, not an assumed horizontal splitting.

Taking i=3,d=2 gives maxdeg E<=-3. Since rank E=17 and degree E=-54,
the ordinary deficit from seventeen copies of O(-3) is exactly3.
A block at degree-5 has center-odd coefficient of dimension at least2,
so would cost at least4, impossible. The only possibilities are

    E=R14 O(-3)+R3 O(-4), or E=R16 O(-3)+O(-6).

The second has S4=H1(O(-5)) as a constituent of H1(E(1)), contrary
to (1a). In the first case R3 is a genuine center-even representation
of dimension3, hence A, V, or 3 copies of1. The identity
R14+R3 W=W'+3T6 excludes A and 3 copies of1 by their W/S4
constituents, and VW=T6 forces R3=V and R14=W'+2T6. This proves (1)
without importing or rerunning the historical twenty-eight-type list.

Taking i=0,d=5 on both sides gives

    every degree of F0 <= -6,
    D0=F6^perp=O(-e), e>=6.

Set a=degree F0 and b=degree F6. Since rank F0=5 and D0 has rank one,

    a<=-30,    b=degree D0<=-6.                            (5)

## 4. The determinant equality forces exact graded twists

Put ci=degree Li. The nonzero determinants of (3) give

    c(i+1)=ci+8+delta_i,    delta_i>=0.                    (6)

The deltas are lengths of effective torsion cokernels. No claim that
they vanish at special parameters has yet been made. Directly summing
(6) and using degree F3=-54 gives

    a+b = -36 + delta1+2delta2+3delta3+2delta4+delta5.       (7)

For clarity, c1+c2+c3=3c1+24+2delta1+delta2 and
c1+...+c6=6c1+120+5delta1+4delta2+3delta3+2delta4+delta5;
substitution gives (7).

The left side is at most -36 by (5); the right side is at least -36.
Consequently

    a=-30, b=-6, all delta_i=0,
    (c1,...,c6)=(-16,-8,0,8,16,24).                       (8)

All maps (3) are now isomorphisms of equivariant bundles, since their
cokernels have length zero. Set

    B=L3=E/F2.

Then rank B=4, degree B=0, and Li=B(2i-6). In particular L1=B(-4).
This is an isomorphism of the associated graded bundles induced by the
derivative; it is NOT a splitting of the filtered bundle or connection.
The letter B is used to avoid confusing this quotient with the
three-dimensional irreducible representation A.

## 5. A forced slope window and cubic character

By (4), every degree of F1 is at most -5. Its rank is9 and its degree
is a+c1=-46. Its excess over nine copies of O(-5) is therefore exactly
one. Center parity and perfectness force

    F0=R5 O(-6),
    F1=R8 O(-5)+O(-6),                                   (9)

where R5 is center-even of dimension5, and R8 is center-odd of
dimension8. Their actual characters are not guessed or assumed.
The exact sequence

    0 -> F0(5) -> F1(5) -> B(1) -> 0

has acyclic left term R5 O(-1), and H1(F1(5))=0. Therefore

    H1(B(1))=0.                                         (10)

Each ordinary degree of B is at least -2. Since B has rank4 and total
degree0, each is also at most6. This finite window is derived, not a
computational cutoff.

Likewise F2 has rank13, degree a+c1+c2=-54, and by (4) every degree
is at most -4. Its excess over thirteen O(-4)'s is exactly two. The
only ordinary partitions of that excess, refined by central parity,
are

    F2=R11 O(-4)+X O(-5),    X=W or W';                   (11a)
    F2=R12 O(-4)+O(-6).                                  (11b)

The R11 or R12 is a genuine center-even representation of the named
dimension. In particular

    H1(F2(3)) is W or W',
    H1(F2(4)) is 0 or 1.                                 (12)

For (11b), the first equality is H1(O(-3))=W; the second is
H1(O(-2))=1. There are no suppressed negative-tail corrections.

Using (1), H0(E(3))=U and H1(E(3))=0. Also H0(F2(3))=0. The exact
sequence 0->F2(3)->E(3)->B(3)->0 therefore forces

    H0(B(3)) = U+X,    X in {W,W'},                       (13)

as representations, because complex representations of the finite
group are semisimple. No surjectivity of sections is presumed before
the actual long exact sequence is used.

## 6. The new finite rank-four quotient list has one survivor

Write B as a sum of irreducible blocks R O(e). Rank4 excludes coefficient
irreducibles of dimension greater than4. Equations (10), degree0 and
central parity require

    -2<=e<=6,    parity(R)=e mod2,
    sum dim(R)=4,    sum e dim(R)=0.                     (14)

This is a complete finite necessary search space for this hypothetical
actual B, not a realization theorem. It contains exactly twenty
unordered multisets. `CANDIDATES.json` lists every one and its cubic
character. The recursion in verify.py enumerates all block multisets;
an independent ordinary-degree/representation assignment checks the
same list. Both use only (14), not historical source records.

For every multiset compute

    H0(B(3)) = sum R tensor Sym^(e+3) W.                 (15)

The fixed-marking McKay graph is the chain

    1--W--A--S4--D--T6--P--W', with the extra edge T6--V.

Symmetric powers satisfy the exact recurrence
R Sym^(n+1) W = W(R Sym^n W) - R Sym^(n-1) W.
The checker additionally verifies this graph and every character used
against nine exact conjugacy-class characters in Q(sqrt5), with
orthogonality weights summing to120.

Among the twenty shapes, condition (13) leaves exactly

    B = O(-2)+W' O(-1)+O(4).                             (16)

Its cubic character is W+W'+2T6=U+W. There is no survivor for U+W'.
This is an abstract quotient-shape restriction, not a chosen map.

## 7. Exact degree-four cohomology eliminates the survivor

From (1) and (16), ordinary cohomology gives

    chi_G(E(4)) = U W+V,
    chi_G(B(4)) = Sym2 W+W' Sym3 W+Sym8 W.

Both bundles have vanishing H1 at this twist. Exact Euler additivity
for 0->F2(4)->E(4)->B(4)->0 yields

    chi_G(F2(4)) = 2V+2P-A.                              (17)

The dimensions check: 6+8-3=11=13+(-54+4*13). But (12) says
H1(F2(4)) is either0 or the trivial representation1. Thus

    H0(F2(4)) = 2V+2P-A,
    or          2V+2P+1-A.                              (18)

Both have coefficient -1 at the physical three-space A. Neither is
a genuine representation. This contradiction eliminates (16), and
hence the entire hypothetical actual rank-four maximal `(3,3)` plateau.

The contradiction is equivariant, not an ordinary dimension count.
In particular adding the possible one-dimensional negative-tail H1
term does not repair the forbidden A multiplicity.

## 8. Reproduction and limits

Run `python3 verify.py` and `python3 -O verify.py` from any directory.
Both must match `RESULT.json` byte for byte. The program authenticates
the retained originals, checks the actual characters and numerical
inputs, derives endpoint equality and all degree rows, independently
enumerates the new twenty-shape space twice, verifies exact characters
by two methods, reproduces (17)-(18), and exercises fail-closed
mutations of the prerequisite/character/slope data.

The source hashes authenticate bytes, not the truth of all transitive
geometric prerequisites. The conditional geometric proof is Sections
2-7, not an assertion that the arithmetic program proves saturation,
actual presentations or the universal persistence lemma. No actual HM
coefficient system is evaluated. The five original dual cubic types
are not mistaken for rank-four images, and the old rank-three cubic
pairing inequality is never used at rank four.
