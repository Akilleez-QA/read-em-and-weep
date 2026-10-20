Editorial scope: This is a mathematical source edition. Historical review and check statements describe the original artifact, not a fresh run. Supporting snapshots are dependencies, not additional new results. Later PR145 mixed-class vanishing supersedes historical unknown mixed-class status; it does not resolve the six pure diagonal conditions.

# Independent review: six-frame determinant normalization

## Verdict

Accepted, conditional on the common-complex and primitive-contraction premises stated in PROOF.md. Independent sparse support analysis gives the same answer for all six frames:

    lambda_i = det[gamma,I_i,H1_i W_i] / det[W_i,eta_i] = 1.

Consequently det(P_i I_j)=1 for every ordered pair. This is a new source-bound structural normalization proof, not an execution receipt for physical products and not a proof of the remaining primitive contraction premise A. It does not establish the global obstruction.

The independent derivation used a fixed coordinate lift and perfect-matching signs. It did not rely on equivariance of the full stored I arrays, on the producer's determinant claims, or on a historical 36-pair computation. The matching certificate directly covers each of the six charts.

## 1. Authenticated source and permitted checks

The reviewed model is `research/hm/null-operator-compiler/hm-pinned-model.json` at commit `48b4ae6d9ccf4a8f12ef54f7514f0ec8f4a1d4ba`:

- Immutable source: https://github.com/Akilleez-QA/read-em-and-weep/blob/48b4ae6d9ccf4a8f12ef54f7514f0ec8f4a1d4ba/research/hm/null-operator-compiler/hm-pinned-model.json
- Git blob: `fcd48a9a22d40d55ce7a08b8aefcb4eaa2fdf761`
- SHA256: `635bb12d9986e0dcada161d4173c773c4f134b9225354a3bc74267840ca19926`
- Exact byte count: 16,803

The source decoder excerpt, `hm-pinned-source-formulas.js`, has Git blob `3dfed53a28b53b3c912a097971d89fc547330a5f`; immutable links and all producer intake pins are in source-pins.json. Its literal denominator convention is I=stored I/di. Its v0 is exactly 1. The preliminary local snapshot had an extra newline; all final checks below use the exact, source-authenticated bytes listed above.

`check_matching_metadata.py` is a new independent metadata checker. It checks both immutable hashes, JSON dimensions, nonzero support, complete perfect matchings, permutation parity, signed coefficient parity, ordered inert factor-label lists, inclusion zero rows, selected inclusion entries, and row shuffles. The selected diagonal numerator checks compare existing exponent metadata; they do not construct or evaluate a product polynomial. The checker contains no polynomial, rational-function, determinant, physical matrix-product, source, owner, or jet evaluator. No repository was imported or executed. The existing model was read as inert JSON only.

Normal and `python -O` runs passed with byte-identical stdout and matching-certificate.json. Guards use explicit exceptions, so optimization cannot erase them. A one-byte trailing-space modification in a separate temporary copy was rejected with `Model SHA256 drift` in both modes. No source file or repository state was changed by this negative control.

## 2. Determinant line and fixed-lift reduction

Assume a common complex

    K0(5) --gamma--> K1(15) --delta--> K2(10) --ev--> K3(2)

whose only cohomology is rank two in degree one, with the contraction equations of PROOF.md. Let

    U_i=[gamma,I_i,H1_i W_i],  V_i=[W_i,eta_i],  T_ij=P_i I_j.

In these exact column orders, U_i^-1 U_j has diagonal blocks (Id5,T_ij,A_ij), while V_i^-1 V_j has diagonal blocks (A_ij,Id2). Here A_ij is the change of basis on ker(ev), or L_i W_j for the pinned split. It follows without an additional sign that

    det T_ij = (det U_j / det V_j)/(det U_i / det V_i).

For any basis W of ker(ev), any lift Z with delta Z=W, and any eta with ev eta=Id2, define on cycles

    beta(u,v)=det[gamma,u,v,Z]/det[W,eta].

Changing Z by cycles changes its columns by combinations of gamma,u,v; changing eta by ker(ev) does not change its determinant; changing W by a basis matrix multiplies numerator and denominator by the same determinant. Replacing u or v by an image of gamma gives zero. Thus beta is one well-defined nonzero alternating form on ker(delta)/im(gamma), normalized by the fixed ambient volume forms. It satisfies lambda_i=beta(I_i[:,0],I_i[:,1]).

In particular choose an ordered coordinate set S of size eight and set Z=E_S, W=delta E_S. Then

    lambda_i=det[gamma,I_i,E_S]/det[delta E_S,eta_i].

This removes every homotopy and every projection from the actual normalization calculation. Nonvanishing of the sparse minors below certifies that each chosen lift is valid.

## 3. Complete six-chart coordinate data

All indices are zero-based; each displayed list is in its actual order. Let F have five K1 coordinates, D two K1 coordinates, S their increasing complement, J the two evaluation-pivot K2 coordinates, and L its increasing complement.

| i | F | D | S | J | numerator row sign |
|---|---|---|---|---|---|
| 0 | 1,4,7,8,10 | 0,5 | 2,3,6,9,11,12,13,14 | 0,5 | + |
| 1 | 0,2,8,9,11 | 1,6 | 3,4,5,7,10,12,13,14 | 1,6 | - |
| 2 | 1,3,5,9,12 | 2,7 | 0,4,6,8,10,11,13,14 | 2,7 | + |
| 3 | 2,4,5,6,13 | 3,8 | 0,1,7,9,10,11,12,14 | 3,8 | - |
| 4 | 0,3,6,7,14 | 4,9 | 1,2,5,8,10,11,12,13 | 4,9 | + |
| 5 | 4,7,8,10,11 | 5,14 | 0,1,2,3,6,9,12,13 | 0,5 | + |

The numerator row sign is the sign of (F,D,S) as a permutation of all 15 ambient rows. Every denominator row permutation (L,J) is even. The source's L_i uses cyclic rather than increasing nonpivot order in each block of five. The same four-coordinate permutation occurs in both blocks, so its total sign is a square and equals +1. Thus the increasing-row minors in this review and the source's cyclic-row minors in PROOF.md have the same determinant.

Direct literal comparison gives I_i[F,:]=0 and

    I_c[D,:]=diag(1,v_c), c=0,...,4;
    I_5[D,:]=diag(1,-v4/v1^2).

The primary denominators are d_c=product_(r=0..4) v_r-v_c^5. The auxiliary denominator is -v1^2 v3 v4. For c>0, the second diagonal numerator has exactly the denominator's signed terms with exponent c increased by one; for c=0 it equals the denominator. The auxiliary second diagonal numerator is the single literal +v3 v4^2. These are source-interpretation statements, not evaluated products.

## 4. Full matching and sign tables

In each table, a permutation lists the chosen local column for each successive retained row. The sign includes BOTH permutation parity and the signs of the selected entries. The factors column is the ordered list of variable labels, not an evaluated product. v0 means the literal constant 1 in this actual model.

### gamma[F,:]

| i | permutation | sign | ordered factor labels |
|---|---|---|---|
| 0 | 3,2,1,4,0 | - | v2,v3,v4,v1,v0 |
| 0 | 4,1,3,2,0 | + | v0,v0,v0,v0,v0 |
| 1 | 2,0,4,3,1 | - | v1,v1,v1,v1,v1 |
| 1 | 3,4,2,0,1 | + | v4,v3,v0,v2,v1 |
| 2 | 3,1,4,0,2 | + | v2,v2,v2,v2,v2 |
| 2 | 4,0,1,3,2 | - | v0,v4,v3,v1,v2 |
| 3 | 0,1,4,2,3 | + | v1,v0,v2,v4,v3 |
| 3 | 4,2,1,0,3 | - | v3,v3,v3,v3,v3 |
| 4 | 2,1,0,3,4 | - | v1,v2,v3,v0,v4 |
| 4 | 3,0,2,1,4 | + | v4,v4,v4,v4,v4 |
| 5 | 2,3,4,0,1 | + | v3,v0,v1,v0,v1 |

There are no other perfect matchings. For the primaries the forced singleton leaves one four-cycle, hence precisely its two matchings. For the auxiliary the support successively forces all columns. By the determinant's defining signed-matching formula, this table proves

    det gamma[F_c,:]=(-1)^(c+1)d_c, c=0,...,4;
    det gamma[F_5,:]=v1^2 v3.

### delta[L,S]

| i | permutation | sign | ordered factor labels |
|---|---|---|---|
| 0 | 1,4,7,0,6,2,3,5 | + | v0,v0,v0,v0,v0,v0,v0,v0 |
| 0 | 1,6,5,0,7,2,3,4 | - | v0,v4,v1,v0,v2,v0,v0,v3 |
| 1 | 0,1,5,4,6,7,3,2 | + | v1,v1,v1,v1,v1,v1,v1,v1 |
| 1 | 0,1,7,6,5,4,3,2 | - | v1,v1,v0,v2,v4,v3,v1,v1 |
| 2 | 5,1,0,6,2,7,4,3 | + | v2,v2,v2,v2,v2,v2,v2,v2 |
| 2 | 7,1,0,4,2,6,5,3 | - | v3,v2,v2,v1,v2,v0,v4,v2 |
| 3 | 5,4,0,1,3,2,7,6 | - | v2,v4,v3,v3,v3,v3,v1,v0 |
| 3 | 7,6,0,1,3,2,4,5 | + | v3,v3,v3,v3,v3,v3,v3,v3 |
| 4 | 1,4,7,0,6,2,3,5 | + | v4,v4,v4,v4,v4,v4,v4,v4 |
| 4 | 1,6,5,0,7,2,3,4 | - | v4,v3,v0,v4,v1,v4,v4,v2 |
| 5 | 3,0,1,2,7,4,5,6 | - | v0,v3,v4,v0,v0,v0,v0,v0 |

Again these are all matchings. Each primary has four forced coordinate columns followed by a four-cycle. The auxiliary has one matching. Commutativity of the symbolic factors identifies the primary terms as +v_c^8 and -v_c^3 product_r v_r. Therefore, as a handwritten determinant identity,

    det delta[L_c,S_c]=-v_c^3 d_c, c=0,...,4;
    det delta[L_5,S_5]=-v3 v4.

Both raw ordered lists and exact expected lists are checked in the companion script. No symbolic multiplication engine is used to obtain these conclusions.

## 5. Cancellation and legal denominators

After the numerator row permutation (F,D,S), the fixed-lift matrix is block lower triangular with diagonal gamma_F, I_D, Id8. After the denominator row permutation (L,J), its diagonal blocks are delta[L,S] and ev[:,J]^-1, since eta=E_J ev[:,J]^-1.

For primary c, numerator and denominator therefore both equal -v_c d_c. For the auxiliary they both equal -v3 v4. Their ratios are exactly 1. All signs in this cancellation are accounted for by the preceding tables.

These inverses are valid in the actual carrier localizations, not merely on an unspecified generic open. For c>0,

    d_c=v_c (product_(r!=c) v_r-v_c^4),

so inverting d_c makes v_c a unit as well. For c=0, v0=1. Thus det gamma_F=±d_c, the pivot v_c, and det delta[L,S]=-v_c^3 d_c are units on the primary legal open. On the auxiliary open, inverting -v1^2 v3 v4 makes v1,v3,v4 units, so its gamma and delta minor inverses and selected I denominators are also legal. This is an algebraic statement about these carrier localizations; it does not independently prove the geometric owner/cover regularity requirements of the wider project.

More generally, an arbitrary fixed pivot gives a rational identity only where its minors are nonzero. If such a proof is used instead, extension to a larger overlap needs the existing regularity of the transition entries and an integral domain (or the appropriate componentwise dense-open argument). A rationally established identity alone must not be advertised as regularity of an arbitrary pivot formula. The chart-specific pivots above avoid that extra denominator issue for this normalization.

## 6. Further explicit quotient reduction

Define the two-row quotient map

    Q_i=E_D^t-gamma_D gamma_F^-1 E_F^t.

For cycles z, Q_i gamma=0 and Q_i is an isomorphism from the cohomology quotient to the two-dimensional coordinate quotient. Consequently

    P_i z=(Q_i I_i)^-1 Q_i z, for z in ker(delta),
    P_i I_j=(Q_i I_i)^-1 Q_i I_j.

The same signed pivot calculation identifies the single intrinsic form beta explicitly:

    beta(u,v)=v_c^-1 det[Q_cu,Q_cv], c=0,...,4;
    beta(u,v)=-(v1^2/v4) det[Q_5u,Q_5v].

The sparse selected inclusion diagonals immediately evaluate these expressions to 1. This realizes the missing volume as one fixed cohomology two-form, with six legal coordinate descriptions, independent of H0,H1,P.

The formula for P_i is ONLY asserted on cycles. Tiny invented countercontrol: take K1=Q^3, K2=Q, delta=(0,0,1), I=(e1,e2), H=e1+e3, P with rows (1,0,-1),(0,1,0), and Q with rows (1,0,0),(0,1,0). Then IP+H delta=Id3, PI=Id2, delta H=1, PH=0, and QI=Id2. Yet P e3=(-1,0), whereas Qe3=(0,0). Thus the identity P=(QI)^-1 Q is false on the whole ambient space even in an exact contraction; its restriction to ker(delta) is the correct statement.

## 7. Scope of the accepted consequence

The reviewed PROOF.md's determinant-line, fixed-lift, primary, auxiliary, and pivot-volume steps agree with this independent derivation. In particular the source's cyclic L order introduces no hidden sign, the auxiliary chart is evaluated only in the actual v0=1 convention, and no equality of full inclusion images is assumed.

The reciprocal root-line factors and transpose in the source transition preserve determinant. Therefore the normalization supports the source's adjugate-as-inverse interpretation once its separately stated contraction and common-frame identification premises apply. It does not prove primitive A, run a source product, admit physical execution, prove a source jet identity, or settle the global obstruction. Those remaining obligations retain exactly their prior scope.
