# The rank-four maximal adjacent plateau (2,3) is impossible

## 1. Result and precise scope

Retain the actual geometric hypotheses, fixed physical marking, and original
parameter line of `ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md`,
pinned at `db51525015bb7c5e825833d550d08dedf6f6ea96` in `INPUTS.json`.
Then the actual second fundamental form cannot have generic rank four with
ordered maximal consecutive rank-four plateau lengths `(k,l)=(2,3)`.

This excludes precisely this ordered rank-four stratum. It does not exclude
another rank-four profile, prove rank at least five, prove square-map
surjectivity, or repair the original proof. No actual coefficients,
parameters, jets, matrices, instance ranks, or local-model experiments are
used. No historical candidate enumeration is rerun. Indeed, no rank-four
quotient enumeration or quotient slope window is needed at all.

The obstruction is an exact equivariant Euler identity forced by two adjacent
unramified quotient blocks. Ordinary ranks and degrees satisfy that identity;
the physically distinct three-dimensional characters do not.

## 2. Actual inputs and the conditional geometric ledger

Work over C with the binary icosahedral group G on the physical parameter line
T=P(W*). Give O(1) its standard determinant-one linearization. The actual
saturated inclusion is

    0 -> E -> H tensor O -> Q -> 0,
    dim H=30, rank E=17, degree E=-54.

E contains no nonzero constant subbundle and spans H. The center acts
trivially on E and all its actual saturated Gauss stages. The imported
original supplies the actual equivariant presentation

    0 -> E -> M3 tensor O(-1) -> M4 tensor O -> 0,
    M3=3W'+3S4+6T6,   M4=2V+4P+3D,

and consequently the crucial exact identity

    chi_G(E(2)) = -V.                                      (1)

Here the fixed physical irreducibles are

    1, W, A=Sym2 W, S4=Sym3 W, D=Sym4 W, T6=Sym5 W,
    P, W', V,
    dimensions 1,2,3,4,5,6,4,2,3.

In particular A and V are distinct. The odd irreducibles are W,W',S4,T6;
the even ones are 1,A,D,P,V. The perfect group G has only the trivial
one-dimensional representation. We will use only

    W tensor W = 1+A,   W tensor W' = P,                   (2)

and chi_G(O(-2))=-1, chi_G(O(-3))=-W,
chi_G(O(-4))=-A. Equivariant Serre duality has no determinant-character
correction since det W=1. The checker independently verifies these
identities and (1) against exact conjugacy-class characters.

The geometric inputs retained from the original are actual local freeness
and saturation, the actual presentation and marking, the original
parameter line, and the universal differentiation/saturation facts for
its Gauss stages. These are assumptions of the conditional argument,
not facts proved by the arithmetic checker. Equivariant splitting on P1
is used only for bundle cohomology, never as a horizontal splitting of a
filtered bundle or ambient connection.

Suppose the forbidden plateau exists. Its saturated stages are

    F0 < F1 < F2 < F3 < F4 < F5,
    E=F2,    rank Fi=9+4i,
    Li=Fi/F(i-1),    1<=i<=5.                             (3)

At every interior stage, the actual derivative kernel is F(i-1), the
saturated forward transform is F(i+1), and the induced derivative

    Li -> L(i+1)(-2),    1<=i<=4,                         (4)

is regular and generically invertible. No assumption that either endpoint
has derivative rank four is used. The upper endpoint has codimension one.

## 3. Persistence includes both endpoints

Every Fi for i<5 contains no nonzero constant subbundle. Below E this follows
by inclusion; above E a constant subbundle lies in each derivative kernel
and propagates backwards to E. Every Fi for i>0 spans H: below E a proper
constant span would contain successive forward transforms and eventually E.
Thus the reversed annihilators Di=F(5-i)^perp have the same properties.

For i,d>=0 and i+d<5, universal section persistence gives

    H0(Fi(d))=0,   H0(Di(d))=0.                           (5)

For completeness the endpoint case is included in the argument. Saturate
a nonzero section into an actual line O(-e) in Fi, where 1<=e<=d. This
line remains saturated in the constant ambient because all successive
quotients are locally free. A degree-e polynomial vector reaches its
constant coefficient span after at most e derivatives: the derivative-to-
coefficient change of generators is triangular with nonzero factorial
diagonal. This is a universal proof, not selection or evaluation of an
actual vector. Its saturated j-th transforms lie in F(i+j). At i=0 the
first inclusion follows because F0 is the derivative kernel at F1, so
its derivative lies in F1 tensor Omega; the remaining inclusions follow
from the interior transforms. The resulting constant span lies in the
interior F(i+e), contradiction. Saturation extends the identities over
the entire parameter line. The same proof applies to Di.

In particular every degree of F0 is at most -5, and D0=F5^perp has rank
one and degree at most -5. Put a=degree F0 and b=degree F5=degree D0.
The determinant of each Fi is center-even. Every equivariant line bundle
on T is O(d) with the standard linearization up to a one-dimensional
character; G has no nontrivial such character. The central sign of this
line bundle is therefore (-1)^d, and every stage degree is even. Hence

    a<=-45 and a even, so a<=-46;
    b<=-5  and b even, so b<=-6.                          (6)

This parity sharpening is essential. No invariant-divisor gap is used.

## 4. Endpoint equality removes all four determinant defects

Let ci=degree Li. The determinants of the actual maps (4) give

    c(i+1)=ci+8+delta_i,   delta_i>=0,   1<=i<=4.          (7)

Each delta is the length of an effective torsion cokernel; possible zeros
at special parameters have not been discarded. Using degree E=-54 and
summing (7) gives the exact identity

    -270 = 3a+2b-120-(3delta1+6delta2+4delta3+2delta4),

or equivalently

    3a+2b = -150+3delta1+6delta2+4delta3+2delta4.           (8)

Indeed degree E=a+2c1+8+delta1, while
b=a+5c1+80+4delta1+3delta2+2delta3+delta4.

By (6) the left side of (8) is at most -150 and the right side is at
least -150. Thus

    a=-46, b=-6, all four delta_i=0,
    (c1,c2,c3,c4,c5)=(-8,0,8,16,24),
    (degree F0,...,degree F5)=(-46,-54,-54,-46,-30,-6).    (9)

The maps (4) are isomorphisms because their cokernels have length zero.
Set B=L2=E/F1. The only graded identification needed below is

    L1=B(-2).                                           (10)

It is an induced isomorphism of associated graded bundles, not a splitting
of the filtered bundle or its connection.

## 5. The complete low-stage splitting possibilities

By (5), every degree of F0 is at most -5. Rank9 and degree -46 leave
exactly one unit of deficit from nine copies of O(-5). Central parity
and the absence of nontrivial one-dimensional characters imply

    F0=R8 tensor O(-5) + O(-6),                          (11)

where R8 is some genuine odd representation of dimension8. Therefore

    chi_G(F0(4))=-1.                                    (12)

Every degree of F1 is at most -4 by (5). Rank13 and degree -54 leave
exactly two units of deficit from thirteen copies of O(-4). The only
ordinary deficit partitions are 1+1 and 2. Central parity refines these
to precisely the following three tail types:

    F1=R11 tensor O(-4)+W tensor O(-5);                  (13a)
    F1=R11 tensor O(-4)+W' tensor O(-5);                 (13b)
    F1=R12 tensor O(-4)+O(-6).                           (13c)

The R11 or R12 is a genuine even representation of the indicated dimension,
but its character need not be determined. In (13a)-(13b), the combined
coefficient of degree -5 has dimension2 and odd parity, so is W or W'.
In (13c), the one-dimensional even coefficient is trivial. These are all
possibilities, not a cutoff or a list imported from a historical enumeration.

## 6. A two-sequence Euler identity contradicts all three tails

The two actual exact sequences, with (10), are

    0 -> F0 -> F1 -> B(-2) -> 0,
    0 -> F1 -> E  -> B     -> 0.

Twist the first by4 and the second by2. Equivariant Euler additivity gives

    chi_G(F1(4))-chi_G(F0(4)) = chi_G(B(2))
                                    = chi_G(E(2))-chi_G(F1(2)).

Hence (1) and (12) force

    chi_G(F1(4))+chi_G(F1(2)) = -1-V.                   (14)

There is no assumption of a surjection on global sections: Euler
additivity accounts for all H1 terms exactly.

For a doublet tail F1=R11 O(-4)+X O(-5), where X=W or W',

    chi_G(F1(4))=R11,
    chi_G(F1(2))=-R11-X tensor W.

Thus (14) requires X tensor W=1+V. If X=W, (2) instead gives 1+A,
contradicting A!=V. If X=W', (2) gives the irreducible P rather than
1+V. Both doublet tails are impossible.

For the line tail F1=R12 O(-4)+O(-6),

    chi_G(F1(4))=R12-1,
    chi_G(F1(2))=-R12-A.

Their sum is -1-A, again contradicting (14). This eliminates the last
tail and proves the stated ordered (2,3) exclusion.

More explicitly the three residuals, left side minus right side of (14),
are V-A, 1+V-P, and V-A. Each has ordinary dimension zero, but none is
the zero character. The contradiction requires exact equality, not merely
positivity or an ordinary numerical estimate.

## 7. Reproduction and limits

Run `python3 verify.py` and `python3 -O verify.py` from any directory.
Both outputs must match `RESULT.json` byte for byte. The program authenticates
the retained original, checks the actual Euler input and physical character
marking by exact arithmetic in Q(sqrt5), derives the endpoint identity
symbolically rather than sampling, verifies the small deficit partitions,
and reproduces all three nonzero dimension-zero residuals by McKay and
independent conjugacy-class arithmetic. Contract mutations are rejected.

The source hash authenticates bytes, not the validity of all transitive
geometric prerequisites. The proof is Sections2-6 conditional on the ledger
in Section2. No actual HM instance is evaluated. The previous (3,3) exclusion
is not used as an input; in particular its stronger quotient slope lower
bound is not imported into this shorter plateau.
