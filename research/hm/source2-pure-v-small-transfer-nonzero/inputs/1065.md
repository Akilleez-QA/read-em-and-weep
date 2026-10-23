# A twelve-dimensional actual Q image transverse to the residual endpoint

## Theorem and scope

Retain the actual source2 compatible pure-V hypotheses and canonical
homotopy h. Write Q:N2->N4 for the invariant quadratic, I2=im j2,
I4=im j4, P_h for the canonical P in im h, and NC for the actual endpoint
submodule in the residual exact sequence. Define the actual subspace

    U_Q = Q(NC2) subset N4.

In every remaining branch,

    ker(Q|NC2)=I2,
    U_Q is isomorphic to NC2/I2 = V+P+D,
    dim U_Q=12,                 U_Q subset ker h.          (1)

Its intersection with the radical endpoint detects the generated endpoint:

    U_Q intersect I4 = I4  if dim F4=9,
    U_Q intersect I4 = 0   if dim F4=16.                   (2)

Now assume specifically the residual-large branch: for a genuine first-
block separation N=N0 plus NR, the actual N0 projection of P_h is zero
but its projection to N8 in NR/NC is nonzero. Then the stronger statement is

    U_Q intersect NC4 = 0.                                (3)

Consequently Q induces an injective actual map NC2/I2 -> N4/NC4, and
NC4 plus U_Q is a direct sum of dimension21 and character V+2P+2D.
This direct sum is NOT identified with NR4, despite having that character.
In particular no assertion Q(NC2) subset NR4 is made. Equation (3) is not
asserted for the other endpoint16 branch with nonzero N0 projection.

All maps are inherited actual maps; no coefficient, projector value or
branch is selected. Neither endpoint is excluded or asserted realized.

## 1. Exact dependencies and nonduplication

INPUTS.json pins the following published originals:

- PR1019, 3fb2475ffb275c5789acbaa8f9f84ed272713785: hQ=j2, Qh=j4,
  ker Q=A plus I2, im h=I2 plus P_h, Q|P_h:P_h->I4 an isomorphism.
- PR795, 3f811311d76914a555c7e7d0c5b887b41805aa6c: the genuine residual
  sequence NC->NR->N8, NC2=V+P+2D, NC4=P+D, and radical maps killing NR.
- PR1059, af2f163e4bcc593b6895ace840c139d2d4668cde: the generated endpoint
  has dimension9 precisely when P_h subset NC2, and dimension16 otherwise.
- PR1061, 90f33f808c2962cdd4c41d11ac32a10c30b0d353: ker h subset im Q,
  and the actual canonical complement im Q=ker h plus D_can.

For (3) only, PR1064 at bfc239e1c8624a0346394e1454b0bea3c976d40d
supplies the additional conclusion

    ker h intersect NC4 = I4                              (R)

under the stated residual-large hypothesis. Its complete proof is retained
as the fifth immutable input. Equations (1)-(2) use only the first four
inputs. The residual theorem derives (R)
from F4=ker h intersect NR4 and F4 intersect NC4=I4. Those results are
inputs here, not rederived or counted as new claims.

The new object is the invariant-quadratic image Q(NC2), not the negative
quadratic descendant image of P_h. Q is not assumed to preserve NR or NC.
The unique A in ker Q is absent from NC2 by its actual representation
character. I2 is the embedded pure-V radical image already inside NC2;
no other D copy is identified with it.

## 2. The full preimage of I4 under the actual Q

Since Q(P_h)=I4 and Q|P_h is an isomorphism, for any x with Qx in I4
there is a unique p in P_h with Qp=Qx. Then x-p belongs to ker Q.
Conversely ker Q plus P_h clearly maps into I4. Therefore as actual
subspaces of N2,

    Q^(-1)(I4)=ker Q plus P_h=A plus I2 plus P_h.          (4)

The displayed sum is direct: ker Q has character A+D, whereas P_h is P.
It also equals ker Q plus im h, since im h=I2 plus P_h. This is a preimage
identity, not an assertion that Q has a chosen inverse on all of N4.

All subspaces are equivariant. In characteristic zero they split into
isotypical components. Since NC2 contains no A, intersecting (4) with NC2
removes its A component. Its D component is exactly I2, already contained
in NC2. Its P component is P_h intersect NC2. Irreducibility of P_h makes
that intersection either all P_h or zero. Thus

    NC2 intersect Q^(-1)(I4)
       = I2 plus P_h  if P_h subset NC2,
       = I2           otherwise.                        (5)

In particular a possible graph of P_h in a larger P-isotypical space
cannot be canceled by an A or D component: the isotypical projections
preserve NC2 and separate these inequivalent types. Merely knowing that
a representative P vector is not in NC2 would not suffice; (5) uses the
whole irreducible actual P_h and equivariance.

## 3. Image rank and exact I4 intersection in every branch

The same isotypical argument gives

    NC2 intersect ker Q=I2.

The first isomorphism theorem yields U_Q=NC2/I2 as a representation, with
character V+P+D and dimension17-5=12. Because j2 kills NR2 and NC2 subset
NR2, hQ|NC2=j2|NC2=0. This proves U_Q subset ker h and all of (1).
It also gives U_Q intersect D_can=0 by the marked complement of PR1061.

For any linear map and subspace of its target,

    Q(NC2) intersect I4 = Q(NC2 intersect Q^(-1)(I4)).      (6)

Apply Q to (5). Its I2 summand dies; its P_h summand, when present, maps
isomorphically onto I4. This proves (2), using the equivalence between
P_h subset NC2 and endpoint9 from PR1059. In particular there is no
partial nonzero intersection with I4. For endpoint16 the induced map
NC2/I2 -> N4/I4 is injective; for endpoint9 it instead has a kernel P
and image dimension8. These quotient dimensions follow from (6), not from
a hypothetical residual splitting.

## 4. Stronger residual-large transversality

In the residual-large branch invoke exactly (R). If y belongs to U_Q and
NC4, then (1) gives h y=0. Hence (R) forces y in I4. The endpoint is16,
so (2) gives U_Q intersect I4=0; therefore y=0. This proves (3).

Equivalently the composite NC2 --Q--> N4 -> N4/NC4 has kernel exactly
I2. Its resulting injection on NC2/I2 has dimension12. Adding the actual
NC4 of dimension9 gives the direct sum claimed in the theorem. Since
both maps are equivariant, its character is

    (P+D)+(V+P+D)=V+2P+2D.

This matches the character of NR4 but does not identify the subspaces.
In particular, using the numerical match to deduce Q preserves the
residual system would be invalid. The statement is transversality in the
actual N4, not an endomorphism of the residual quotient.

## 5. Reproduction and limits

verify.py authenticates the immutable inputs, checks the character and
intersection dimensions, and verifies the formal preimage, quotient-kernel
and implication identities in abstract block coordinates. These coordinates
encode proved linear-algebra lemmas with symbolic maps, not actual HM
coefficients or selected points. The actual applicability of the lemmas
uses the pinned written proofs and (R), not synthetic rank tests.

The new conclusions constrain the position of an actual Q image. They do
not decide a branch, force any original Bockstein to vanish, select a
residual coupling, extend h to a graded-module map, or exclude a source.
