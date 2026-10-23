# Actual invariant-quadratic commutation excludes the nine-dimensional endpoint

## Theorem

Retain the actual source2 and nonzero pure-V Q-compatible radical
hypotheses of PR1059. Let h be its canonical homotopy and F the negative
submodule generated in degrees two through four by im h. Then the
nine-dimensional generated endpoint is impossible. Necessarily

    dim F4=16,    P_h is not contained in NC2.             (1)

This excludes only one conditional generated-endpoint branch, not
source2 itself. It does not decide between the nonzero-N0 and the
residual-large ways of obtaining endpoint16, or select an actual
projection, scalar, source coefficient or instance.

The new ingredient is the ACTUAL invariant quadratic in degree three,
commuting with actual negative multiplication into degree five. No
extension or commutation property of the homotopy h is assumed.

## 1. Immutable actual-map inputs and notation

INPUTS.json authenticates five complete public originals:

- PR1054 at8732cb65fe0e72da59e785f3f85ad197a7092e6c,
  research/hm/source2-pure-v-generated-homotopy/PROOF.md:
  F2=im h=I2 plus P_h, Q2(F2)=I4, F3=W F2, and the actual direct sum

      F3=I3 plus (W tensor P_h)=W'+2T.                    (2)

- PR1059 ataf2f163e4bcc593b6895ace840c139d2d4668cde,
  research/hm/source2-pure-v-residual-p-channel/PROOF.md:
  dim F4 belongs to{9,16}, with9 equivalent to P_h contained in NC2.
  In that branch F4=NC4. The actual endpoint submodule has

      NC2=Sym16 W=V+P+2D,
      NC3=Sym17 W=W'+S+2T,
      NC4=P+D,                                         (3)

  and both negative arrows are the inherited polynomial multiplication
  and multiplication followed by its endpoint quotient.
- PR1065 atfd75633464cd587856287cc7866520fb4105ef5b,
  research/hm/source2-pure-v-q-transversality/PROOF.md:
  Q2 is the actual invariant quadratic and

      ker(Q2|NC2)=I2,   I2 has character D.              (4)

  In particular it is injective on the unique actual V in NC2.
  No assertion Q2(NC2) contained in NR4 is made or used.
- PR1068 at05e8b33eb87e9f36aa30500145cc42bc0ea00df8,
  research/hm/pure-v-terminal-nonvanishing/PROOF.md:
  the embedded NC4 is exactly the FULL joint-negative kernel in M4,

      NC4=ker[M4 -> W tensor M5_-].                     (5)

  The proof identifies the actual E_C kernel inclusion and independently
  restricts the exact actual Koszul injection NC3->W tensor NC4. It is
  not an equality inferred from the P+D character.
- PR1072 atd03beb727c7e778026dcceb3555c899a0808e093,
  research/hm/terminal-pencil-quotient/PROOF.md:
  the actual degree-five negative space genuinely separates as

      M5_-=N0,5 plus NR5=(W'+2T) plus T=W'+3T.           (6)

  Its inclusions and projections come from the same evaluation kernel
  and actual cohomological multiplications. In particular M5_- has no S.

Here Q_d denotes multiplication by the SAME actual invariant quadratic
from cohomological degree d to degree d+2. It is not a separately chosen
map at each degree, a representation model map, or the homotopy h.
The central involution acts on Q trivially because Q is invariant.
Thus Q preserves central parity: Q2 maps the positive N2 to positive
N4=M4, and Q3 maps negative M3 to negative M5_-. The negative coordinates
W reverse parity. Actual polynomial multiplication is commutative,
so for every ell in the fixed W and every a in N2,

    Q3(ell a)=ell Q2(a).                              (7)

This is literal ring/module associativity. It is not a new extension
of a three-vertex pencil endomorphism, and imposes no extra condition
on h in degree five.

## 2. The small branch would annihilate the whole endpoint middle under Q

Suppose for contradiction that dim F4=9. Then PR1059 gives P_h contained
in NC2. Also I2 is already embedded in NC2. Therefore F2 is contained
in NC2 and the actual negative submodule property puts

    F3=W F2 contained in NC3.

This is an actual containment, not an identification of two spaces
having related characters. Equations(2) and(3), with semisimplicity of
G representations in characteristic zero, give the actual quotient
character

    NC3/F3 is isomorphic to S.                         (8)

Since Q2(F2)=I4 and I4 is contained in NC4, the full joint-kernel
identity(5) gives W Q2(F2)=W I4=0. By literal commutation(7),

    Q3(F3)=Q3(W F2)=W Q2(F2)=0.                       (9)

Consequently the actual restriction Q3|NC3 factors through the quotient
NC3/F3. This quotient is S, while its target M5_- has character W'+3T
and contains no S. Equivariance and Schur's lemma force

    Q3|NC3=0.                                        (10)

Neither a quotient of M5_- nor an arbitrary chosen terminal T is used:
the target in this Hom vanishing is the entire actual negative-parity
space in degree five.

## 3. The actual V gives a contradiction

Let V_C denote the unique irreducible V subspace of NC2 in(3).
Its negative multiples lie in NC3, because NC is an actual subpencil.
For every v in V_C and ell in W, equations(7) and(10) give

    ell Q2(v)=Q3(ell v)=0.

Thus Q2(V_C) lies in the FULL joint-negative kernel(5), namely NC4.
But(4) says Q2 is injective on V_C: its kernel inside NC2 is the actual
I2 of type D, which meets V_C trivially. Therefore Q2(V_C) is a
nonzero irreducible V contained in NC4=P+D. This is impossible by
semisimplicity, since Hom_G(V,P+D)=0.

The contradiction rules out the supposed endpoint9. The already proved
exhaustive alternatives in PR1059 then give(1).

## 4. Consequences and precise boundaries

The smaller conditional negative module and its conditional resolution
in PR1066 and the later actual-small-module corollary describe a branch
which cannot occur once these actual degree-five commutation constraints
are retained. Their conditional deductions are not used as a source
realization. No contradiction is claimed with the existence of the
endpoint subsystem NC itself: what fails is P_h being contained in NC2
under the simultaneous invariant-Q compatibility assumptions.

Endpoint16 remains necessary, not asserted realized. The proof does not
identify repeated D copies, assume Q preserves NR, split the residual
extension horizontally, extend h to a module map, or select a residual
coupling. It makes no new assertion that an original Bockstein vanishes
or that source2 has been excluded. The obstruction uses only the actual
V in NC2 and two exact joint-kernel/quotient statements.

## Reproduction and evidential scope

Run python verify.py and python -O verify.py. Both reproduce RESULT.json.
The bounded verifier authenticates all five originals, checks the exact
representation subtraction and Hom vanishings, parity bookkeeping,
Koszul determinant identity and contradiction dimensions. These finite
checks support, but do not replace, the actual-map proof of(7)–(10).
No actual source coefficient, point, parameter, derivative, jet, tensor
or instance rank is evaluated. No public files are changed by this packet.
