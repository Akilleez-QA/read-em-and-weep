# The pinned common-complex syzygy by a path involution

## Result and evidence boundary

The literal pinned matrices satisfy

    delta gamma = 0.

This is proved independently of primitive A, the stored chart primitives, the historical exact-computation receipt, and any assertion of exactness. The proof identifies a universal cyclic incidence pattern and pairs every two-edge path with one of opposite sign and reversed scalar-label order. There are 60 paths and 30 pairs. Commutativity kills each pair.

The argument works over every commutative ring with arbitrary v0,...,v4. It therefore proves both the finite pinned identity, where v0=1, and its degree-one homogeneous lift, where the constant linear tokens become v0. It persists under specialization and localization. All six carriers share these same gamma and delta fields.

No actual polynomial matrix multiplication, polynomial expansion, source evaluation, numerical specialization, source jet, production import, or historical-checker execution was performed. The executable certificate only compares literal singleton records, zero entries, indices, sign parity, and ordered pairs of variable labels. It never combines two source labels into a polynomial or exponent tuple. The source-specific theorem is the cyclic proof plus this exact input identification, not a claim that metadata alone proves arbitrary matrix identities.

The result removes one of the four remaining families in the independent retraction reduction. It does not prove delta I=0 or the complementary inverse. Full A remains unproved here.

## 1. Source pin and conventions

Pinned source:

https://github.com/Akilleez-QA/read-em-and-weep/blob/31f5b074f7c212f9bb6498ed2920e0c93cc781a9/research/hm/null-operator-compiler/hm-pinned-model.json

- Git blob: fcd48a9a22d40d55ce7a08b8aefcb4eaa2fdf761
- SHA256: 635bb12d9986e0dcada161d4173c773c4f134b9225354a3bc74267840ca19926
- Length: 16,803 bytes

This immutable model was read again at current PR79 head 31f5b074f7c212f9bb6498ed2920e0c93cc781a9 on 2026-10-18. The returned Git blob agrees with the blob computed from the bundled bytes; those bytes also match the prior determinant/retraction source pin. PR1's current coordination discussion and the current PR79 description were read before this work. The regularity and rational-residue work remains separate.

Indices in a five-coordinate block are elements of Z/5Z. Ambient rows of gamma are ordered A0,...,A4,B0,...,B4,C0,...,C4; outputs of delta are Y0,...,Y4,Z0,...,Z4. Domain coordinates are x0,...,x4. Letter C for this third ambient block is unrelated to the previously named identity ev delta=0.

Every nonzero gamma/delta entry is exactly one record with coefficient +1 or -1 and one of the five exponent tokens

    0,0,0,0 -> v0=1,
    1,0,0,0 -> v1,
    0,1,0,0 -> v2,
    0,0,1,0 -> v3,
    0,0,0,1 -> v4.

The homogeneous interpretation replaces only the first token's scalar 1 by v0. It is the degree-one lift of these linear maps. No rational chart denominator or chart-dependent entry is used for the syzygy proof.

## 2. The complete universal cyclic pattern

For arbitrary x, gamma has the coordinate description

    A_i =  v_(i+1) x_(i+2) + v_(i-1) x_(i-2),
    B_i = -v_(i-2) x_(i+1) - v_(i+2) x_(i-1),
    C_i =  v_i x_i.                                      (1)

The ten coordinates of delta on an arbitrary (A,B,C) are

    Y_i =  v_(i-1) A_(i+2) - v_(i+1) A_(i-2)
         + v_(i+2) C_(i+1) - v_(i-2) C_(i-1),

    Z_i =  v_(i+2) B_(i+1) - v_(i-2) B_(i-1)
         + v_(i-1) C_(i+2) - v_(i+1) C_(i-2).             (2)

The checker compares all 75 gamma cells and all 150 delta cells against (1)-(2), including every zero cell. There are exactly 25 and 40 nonzero edges, respectively. Thus (1)-(2) identify the entire maps, not merely a sampled cyclic representative or a selected minor.

## 3. The sign-reversing path involution

A path starts at one domain coordinate x_j, passes through a middle coordinate A_k, B_k, or C_k, and ends at Y_i or Z_i. Its sign is the parity of the two edge signs. Its ordered labels are written in output-edge, input-edge order. Keep these as two labels, without multiplying them.

For each fixed i, the following table gives every pair. A row names the common input, the two middle coordinates, the path signs, and their ordered variable-label indices. Every index is modulo five.

| Output | Input | First middle | First sign/labels | Second middle | Second sign/labels |
|---|---|---|---|---|---|
| Y_i | x_i | A_(i+2) | + (i-1,i+1) | A_(i-2) | - (i+1,i-1) |
| Y_i | x_(i-1) | A_(i+2) | + (i-1,i-2) | C_(i-1) | - (i-2,i-1) |
| Y_i | x_(i+1) | A_(i-2) | - (i+1,i+2) | C_(i+1) | + (i+2,i+1) |
| Z_i | x_i | B_(i+1) | - (i+2,i-2) | B_(i-1) | + (i-2,i+2) |
| Z_i | x_(i+2) | B_(i+1) | - (i+2,i-1) | C_(i+2) | + (i-1,i+2) |
| Z_i | x_(i-2) | B_(i-1) | + (i-2,i+1) | C_(i-2) | - (i+1,i-2) |

Exchange the two paths in each row. This is a fixed-point-free involution, since their middle coordinates differ. The paired paths have the same input and output, opposite signs, and reversed labels.

Completeness follows directly from the row degrees. Each output has two edges entering A/B coordinates with two predecessors apiece and two edges entering C coordinates with one predecessor apiece. Hence each output has exactly six paths, exactly the six paths covered by its three table rows. There are no paths to its other two domain inputs. The table therefore covers all 10 outputs and all 60 paths, with 30 occupied output/input slots and 20 empty slots.

For any two elements a,b of a commutative ring, the two opposite signed actions with reversed labels cancel because ab=ba. Apply this elementary fact to every table row. Every coordinate of delta(gamma(x)) is zero for arbitrary x. Thus delta gamma=0.

No division was used. The result holds before any localization, with arbitrary v0. Its finite specialization v0=1 proves the exact pinned identity. This is not an inference from A or from the historical contraction list; it independently establishes the common-complex equation that such a contraction theorem would otherwise have supplied conditionally.

## 4. Static source-binding certificate

`check_incidence.py` verifies the fixed model digest and Git blob, decodes only the five singleton linear tokens, compares every gamma/delta cell with (1)-(2), and verifies the displayed involution on the literal incidence graph. For each pair it checks:

1. Both paths exist and have the specified equal endpoints.
2. The middle coordinates differ and neither path was already paired.
3. The two ordered label pairs are reverses.
4. Their sign parities differ.
5. Every incidence path occurs exactly once.

The script neither sums path contributions nor creates product labels. The sign operation is Boolean parity; the only operations on variable labels are indexing, equality and reversal. The printed PASS is a static binding result, not a physical evaluation receipt.

Fourteen negative controls reject changed signs, variable labels, missing/extra edges, a nonunit coefficient, a duplicate record, a nonlinear token, a malformed row, a missing/repeated pair, a wrong endpoint, and independent path-checker sign/label defects. These are inert token/path mutations. The checks use explicit exceptions and remain active under Python optimization.

## 5. Exact reduction of the remaining A obligation

This section combines the new syzygy with the independently established retraction/support facts; it is not needed for Sections 1-4. The prior proof and review are bundled as `inputs/retraction-proof.md` and `inputs/retraction-review.md`. Their independently proved identities are

    H0 gamma=Id5, H0 I=0, H0 H1=0,
    PI=Id2, P E_S=0, P H1=0,

with the literal support decomposition (F,D,S) of dimensions (5,2,8). In that order gamma_F and I_D are invertible, I_F=0, H1_F=H1_D=0. Therefore

    N=[gamma | I | E_S]

is invertible by lower block triangularity. This uses no A identity and does not presume that the middle block row of N^-1 equals P.

Retain the independent pivot splitting

    LW=Id8, WL+eta ev=Id10,

and the already structural B and C identities H1 eta=0 and ev delta=0. Thus H1=H1WL and delta=WLdelta. Define

    T=E_S^t H1 W,    M=Ldelta E_S,
    R=gamma H0+IP+H1delta-Id15.

The exact abstract conjugated defect, now using delta gamma=0, is

    N^-1 R N =
        [ 0          0            0       ]
        [ Pgamma     0            0       ]
        [ 0          T Ldelta I   TM-Id8  ].              (3)

For clarity, its columns follow without identifying P with an inverse coordinate row: Rgamma=I(Pgamma); RI=E_S T(Ldelta I); RE_S=E_S(TM-Id8). These use only the stated retraction/support facts and the new common syzygy. In particular the lower-left 8x5 block is now proved zero independently of A.

It follows that A is equivalent to the three remaining families

    Pgamma=0        (2x5),
    Ldelta I=0      (8x2),
    TM=Id8          (8x8).                               (4)

For the reverse implication, substitute (4) into (3). For the forward implication, (3) first gives TM=Id8. Since T and M are square over a commutative ring, the determinant/adjugate theorem makes T invertible, so T Ldelta I=0 implies Ldelta I=0. This step needs no separately computed determinant formula for M. Structural C makes Ldelta I=0 equivalent to delta I=0.

This leaves 90 displayed scalar positions per carrier rather than 130 in the earlier split-basis presentation, removing 40 positions per carrier. They are counts of displayed obligations, not algebraic-independence or minimal-generator claims. If a separate proof establishes Pgamma=0, the remaining target becomes exactly the two families Ldelta I=0 and TM=Id8, totaling 80 displayed positions per carrier. This artifact does not claim that separate quotient proof or either remaining family.

At completion, the separate source-bound quotient proof and its independent review were available in `primitive-projection-20261018.zip`. Their mathematical notes are included as `inputs/projection-proof.md` and `inputs/projection-review.md`. They establish Pgamma=0 for the same six carriers without A. Importing that separately reviewed result gives the stated two-family, 80-position target immediately; the new proof here remains only the common syzygy and its exact consequence.

## 6. Scope and reproduction

Run `python check_incidence.py` and `python -O check_incidence.py` from this directory, or give its absolute script path from another directory. Use `--certificate path.json` to write the explicit 30-pair metadata certificate. `--model` can relocate the input but does not relax either immutable pin.

The new proved identity is delta gamma=0 for the pinned common maps, before localization. With the previously proved ev delta=0, these particular maps are a complex. Exactness, the chart inclusion equation delta I=0, the complementary inverse, full primitive A, source-frame/regularity premises, retained-test values, and the global obstruction remain distinct obligations.
