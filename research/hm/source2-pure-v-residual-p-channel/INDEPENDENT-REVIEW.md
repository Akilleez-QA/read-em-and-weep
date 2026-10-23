# Independent residual endpoint-dichotomy review

Result: PASS. No mathematical blocker found.

Read the complete proof, checker and immutable typed source inputs,
particularly the actual A-channel maps in PR794, residual evaluation
sequence in PR795, generated submodule in PR1054 and separated-P theorem
in PR1058. Independently replayed 35 main checks in normal and optimized
modes: output is byte-identical and agrees with RESULT.json.

## Actual endpoint-contained branch

The A-channel first map is genuinely injective from Sym8 W into NC2,
so its unique P source maps isomorphically onto the unique P16 target.
The previous separated-block theorem makes the D component of the
quadratic descendants nonzero and onto the unique D in N0,4. The actual
fourth A-channel map is an isomorphism on that D. Commutation of the
fixed-pencil map with quadratic multiplication therefore forces the D
in NC4 to be generated from P_h. Together with I4=P, this gives all
NC4 and dimension nine. This does not identify the distinct first-degree
D images of the A and V channels. No character-only nonvanishing inference
is substituted for the typed actual-map argument.

The middle dimension fourteen is compatible with this branch and does
not contradict the degree-eighteen endpoint reconstruction. Modulo I4,
the quadratic map has image D and kernel V+P. The possible P graph into
I4 remains unselected. The condition F4 subset ker h gives the stated
h(NC4)=0 consequence without choosing a gate coefficient.

## Residual quotient and universal calculation

PR795 supplies the genuine exact sequence NC->NR->N8 with actual quotient
and connecting maps. Its constant section inclusion for N8,4 is the
complete polarization of Sym8 in A tensor Sym6. In N8,2=A tensor Sym4,
the unique P comes from the polarized Sym6 constituent. The coefficient
A factor is fixed by negative multiplication; only the polynomial Sym4
factor is multiplied by the negative quadratic. The checker implements
that distinction correctly.

The authenticated apolar embedding and group intertwiners identify the
unique P constituent. Complete polarization is injective, the two
transvectants kill its exact image and have the required full rank, and
the stated 12-by-12 determinant is nonzero. Thus the universal quotient
map is an isomorphism, rather than merely a map with matching characters.
Actual quotient naturality then proves injectivity modulo I4 for every
nonzero residual P projection. Combined with PR1054's surjection this
gives dimension sixteen and the negative free-module summand. The argument
never splits NR horizontally and does not claim a Q-stable decomposition.

In particular the radical map j4 kills NR in the published orientation;
it is NOT a row on the N8 quotient. No such incorrect use enters this
proof. The three projection alternatives exhaust P_h and give exactly
the necessary endpoints nine or sixteen. Neither endpoint is selected
or excluded. The former conditional rank-36 argument whose antecedent
was F4=I4 is unavailable, but that does not prove generic rank differs
from 36 by some other mechanism.

## Independent alternate certificate

The supplementary verify_independent_direct_sum.py constructs complete
polarization independently by extracting the degree-two X,Y part of
f(x+X,y+Y). It then multiplies the second polynomial factor, retains the
full 21-dimensional A tensor Sym6 ambient space, and forms the square
matrix of nine polarization columns followed by twelve descendants.
No transvectant quotient or its rank is used in this alternate test.

Both normal and optimized runs give exactly

    det[polarization | descendants]
       = -515610823884800000000000000000.

This nonzero determinant directly proves that the descendants form a
complement to the actual polarization image, hence proves the same
quotient injectivity independently of the main quotient formula. The
script's SHA256 is
338594251618bc7c6ad1dec9939ee46b7711094cc5da58df1e4fffd3861267c1.
It uses only universal representation data, not an actual source instance.

## Immutable provenance

Fresh direct GitHub reads during this task authenticated:

- PR790 blob 0641ffadf54324d5520aec89767658e938815223.
- PR792 blob 76bee93507d1a2d0840926d4e4e27edadfebb7d7.
- PR794 blob 3ad30b9aa1920408cc34778e78405f544b5adc8e.
- PR795 blob 9358ec81c552913fac20f3a92d7b9f7c58105656.
- PR1054 blob 64e6bf9f1bf46440700ebab7c90a18f9d8155fd8.
- PR1058 blob 3d42713aaaf4078e3a1b44d8eb3d9f545daa880c.

The universal-symbol source blob
0ff4a2fd717842d8df9cf3ce3e3d29fd189bcd6e was freshly authenticated earlier
in the same review session. All exact commits, paths and URLs are in
INPUTS.json; retained bytes match their hashes. The historical executable
was not run.

## Frozen main hashes

SHA256:

- PROOF.md: ebcd4b123652a7526a74459d0d5875858de7ac90480d38ee1928fd293a31cb18
- verify.py: a7dc3e2b254e98d9d452081246c64ae64669427d644fc4a839f569cb75672130
- INPUTS.json: ccf59053ed5521f8619bba046c70de13c6791d4396ed24c25b7ae99207280b92
- RESULT.json: a9574379f142baa3d5c9f964ba7d6cd41659340d706113488ef59013156fd0be

No actual coefficients, chosen directions, residual coupling values or
source-instance ranks were evaluated. No public files were changed.
