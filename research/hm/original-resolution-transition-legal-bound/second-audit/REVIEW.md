Editorial source note: filenames such as source-pins.json and inputs/ in the historical text refer to the original source edition. This mathematical edition records original and staged SHA256 values in SOURCE-BINDINGS.json; unavailable supporting source bindings remain explicit publication prerequisites, not asserted included files. Historical audit runs are not new checks.

# Independent second audit: actual transition legal-factor bound

## Verdict

**Accepted, with the scope stated in the producer proof. No mathematical blocker remains.** For the authenticated product-root model and the frozen row-transition formula, the conservative carrier/legal bound is **4/1 per actual endpoint occurrence** for the undifferentiated transition and its rank-two adjugate. For the genuine invariant derivation, the stated **5/2** and **6/3** derivative consequences follow. Separately, the literal resolution inclusion adds **4/1 at its selected owner**, coefficientwise for an arbitrary input in the specified physical cohomology frame.

This accepts the revised producer `PROOF.md` with SHA-256 `b4c3041e8f945df65518f37dd59f92e16d6cd8cc29fd9803d8576daf7c9b99c8`. An exact reviewed copy is included as `inputs/reviewed-PROOF.md`. The extra sentence in section 4 correctly clarifies that standard tags choose domains and trivializations; they do not insert a new scalar in the frozen transition leaf.

The argument does not evaluate a physical source, certify a numerical jet implementation, update a full-source ledger, lower an outer partition, identify a residual class. None of those conclusions is needed for the accepted local bound.

## 1. Inputs, source identity, and audit boundary

I read the producer proof and all six supplied inputs. The two earlier proofs and their independent reviews remain mathematical dependencies: this audit checks the new transition and inclusion argument against their exact accepted frame and carrier conclusions, rather than re-proving all earlier primitive identities. The six snapshots were also compared with their existing local predecessor packets. No fresh remote-fetch claim is made.

| Input | SHA-256 |
| --- | --- |
| `homogeneous-PROOF.md` | `b8d85b3adb79b69953a6ac1d13e69d9aa2e0b679653822af6bd6834cffedb18b` |
| `homogeneous-REVIEW.md` | `7eb64a97a1b86996c0d5aa7e6dee1aadaa3a08f240bc4688683cb132658628d9` |
| `product-root-PROOF.md` | `8dea4aa63017a52441b7e1e1f22b6886754a0030b1dfe9932e005b11d8ab5342` |
| `product-root-REVIEW.md` | `1b88fe1bdcf399fb6158984692925fcc84c3afd25a17cb60ddbe5148fa8f8bb0` |
| `raw_engine.py.txt` | `c9804022b362277d63217c7674c4d6d3dff5941ae4210c30f51f3b5cf3868da9` |
| `refined-tracefree-pole-domain.md` | `209d8c8a35edabadabd57d4608c4b49a508700cc00e983d50045b7a722de5ab2` |

`source-pins.json` records SHA-256, byte lengths, and Git blob hashes for the six inputs, exact reviewed proof, and inspected producer checker. The inherited product-root source manifest identifies the raw engine at immutable commit `e93cf712f9da4926a8450cc870ed45a7bfc379ab`, path `research/codex-swarm/detector-realization/raw_engine.py`, with Git blob `34a230aedc9e6d47148195752da54c30c576f53a`. The supplied bytes have that same blob. The refined-domain source is the pinned file at commit `491306fd2f7f8a04c29784afa48a6cb8a467f154`, with blob `b6e9933ffafcd7018b1b2876ad3685f22e3b5292`.

Only local file reads/writes, hashing, inert Python AST parsing, and small integer-exponent metadata checks were performed. No source or model module was imported. No physical object, primitive matrix, actual polynomial product, residual, coefficient detector, or jet was constructed or evaluated. 

## 2. Transpose order and homogeneous weights

The raw engine literally uses

    g_ij = D_j transpose(P_i I_j) D_i^-1,
    D_i = diag(nu_i, nu_i^-1).

The two primitive weights are genuinely row/column dependent: P row a has weight -a, and I column b has weight b. Thus the formal summands of T_(a,b) have weight b-a. Since v_A=tau_A v_ref,

    T_(a,b)(v_ref) = tau_A^(a-b) T_(a,b)(v_A).

The entry g_(b,a), including its transposed indices, has endpoint factor

    nu_j^(1-2b) nu_i^(2a-1) tau_A^(a-b).

In one coordinate tau=ell^-1. Therefore the four scalar factors, in the producer's order `(a,b)=(0,0),(1,1),(1,0),(0,1)`, are exactly

    e_j/e_i, e_i/e_j, e_i e_j/ell, ell/(e_i e_j).

In particular the infinity ell factor cannot be omitted or inverted. These are the actual sections e0=1 and e1=y/x, not formal square roots of the standard squared-line frames. The source AST contracts independently bind nu, Dframe, g, and the two physical inclusion/projection leaves to these expressions.

## 3. Scalar tables and polynomial extension

I independently checked all 32 entries in the two raw scalar tables and all 32 entries in the cleared tables. On the finite chart, h=x^2-1 and y^2=xh give

    e1=y/x, 1/e1=y/h, e1^2=h/x, 1/e1^2=x/h.

On the infinity chart, x=1/t, y=u/t^2, s=1-t^2, u^2=ts, and ell=1/t. Hence

    e1=u/t, 1/e1=u/s,
    e0^2/ell=t, e1^2/ell=s,
    e0 e1/ell=u, ell/(e0 e1)=1/u=u/(ts).

The last expression is decisive for allocation: multiplying by the actual bit-zero owner's t and the actual bit-one owner's s gives u. Omitting either charge leaves a denominator in the corresponding basis coefficient. Charging two copies of only one of those differently labelled factors would not establish this clearance.

The legal sections have their correct degrees. The finite representatives L0=1 and L1=xh become t and s after the degree-one and degree-three trivialization changes. In particular xh becomes s/t^3 as an unweighted rational function; its section representative on the infinity chart is s only after multiplication by t^3.

These checks establish polynomial coefficients in Q[x]+Q[x]y and Q[t]+Q[t]u, not merely regularity after localizing by the legal factors. Both quadratic coordinate rings are free modules of rank two over their base polynomial rings because their defining equations are monic in y or u. Tensoring four such rings gives the 16-element product basis. Reducing products of odd basis elements multiplies coefficients by xh or ts and creates no denominator. The product-chart conclusion therefore follows coordinatewise.

The integer metadata checker also verifies finite-to-infinity substitution independently: an exponent triple `(a,b,c)` for x^a h^b y^c transforms to `(-a-2b-2c,b,c)` for t,s,u, before reduction and the prescribed ell weight. This recovers all four infinity factors for every mask pair.

## 4. Carrier and occurrence ownership; standard tags

The accepted homogeneous primitive theorem supplies polynomial extensions of H_i^2 P_i and H_j^2 I_j, with each factor belonging to its own actual occurrence. Consequently each formal summand of T is cleared by H_i^2 H_j^2 on any common standard chart. Combining this with the scalar tables proves the stronger local statement with carrier power two at each separate endpoint. Padding to the retained conservative power four is legitimate because the additional local carrier representatives are polynomial.

This reasoning does not merge occurrences whose labels agree. The two endpoint slots remain two slots, and their two legal clearances remain in the ledger with multiplicity. If an arithmetic construction subsequently identifies a specific selected occurrence, its charges must be added there. An equality of standard tag, carrier label, or legal mask is not permission to borrow from or collapse an occurrence.

The standard-tag argument is valid because the carrier and legal clearing objects are global homogeneous sections. Represent them and their homogeneous primitive maps in one chosen chart A. The primitive weight transformation is exactly the tau factor already incorporated in section 2, and the legal transformations are exactly the degree-one/degree-three changes just checked. The cleared coefficient is polynomial on each A independently; there is no unaccounted standard-coordinate denominator to transfer to another owner.

One must still retain the full target intersection and original target-tag correspondence in any later outer comparison. The theorem does not authorize replacing that target by a smaller or differently tagged intersection. The producer explicitly retains this condition.

## 5. Adjugate and derivative qualifications

For a two-by-two matrix, taking the adjugate only exchanges two diagonal entries and negates the off-diagonal entries. It therefore preserves this exact endpoint list and the same 4/1 bound without invoking determinant one. The accepted determinant normalization is needed only for the separate statement that this adjugate equals the genuine inverse.

The actual vector field has polynomial coordinates on both curve charts:

    V(x)=y, V(y)=(3x^2-1)/2,
    V(t)=-u, V(u)=(3t^2-1)/2.

These formulas preserve the relations y^2=x^3-x and u^2=t-t^3. In particular V(u) is essential; replacing the infinity field by just -u times the t derivative on arbitrary functions would be wrong.

Write a cleared coefficient as a regular numerator divided by the product of its owned local carrier/legal representatives. Applying the genuine derivation and the quotient rule raises each participating section exponent by at most one. The numerator remains regular because V preserves the local ring. Iterating proves 5/2 after one derivative and 6/3 after the stated second derivative. No claim that t is a uniformizer is needed; it has order two at O, and these are named-factor powers rather than order-one valuations.

This differentiates the actual rational expression, including the frame factors and homogeneous coefficient changes. It is not a certificate for stripped derivatives, fixed pointwise frame normalization, or a numerical jet implementation. The producer's limitation is both necessary and sufficient.

## 6. Separate resolution inclusion

For the term containing I column a and P row b in

    I D_m R^t D_m^-1 P,

the two diagonal factors contribute nu_m^(2(b-a)). The primitive product has weight a-b, so conversion from v_ref to v_A contributes tau_A^(b-a). The combined multiplier is

    (nu_m^2 tau_A)^(b-a) = (e_m^2/ell_A)^(b-a).

Only the exponents -1,0,1 occur. Their one-coordinate ratios are `(1,h/x)` on the finite chart and `(t,s)` on the infinity chart, in legal-bit order. One additional legal section at the selected owner clears each ratio and its reciprocal exactly as displayed in the producer's inclusion table. The two primitive carrier bounds add to four at that same owner.

The conclusion is coefficientwise in R. It does not require R to be closed, trace-free, or a curvature expression. It does require its coefficients to be in the physical cohomology frame specified in the formula. Existing poles of R are retained, and the extra 4/1 is added to the selected occurrence after alignment; it is not permission to count the same selected owner's previous clearance a second time. No End-homotopy improvement is proved here.

## 7. Checkers and acceptance scope

I inspected the entire producer `check_frame_metadata.py`, SHA-256 `f532951d116b5da5618eea69da9bad6df53b4beec854b41c3855b29bc000e783`. It uses inert ASTs and integer exponents only. Its normal and optimized runs agree exactly and reproduce the producer's supplied normal output. The independently generated receipts are `producer-normal.json` and `producer-optimized.json`.

The separate `check_independent_metadata.py` was written before reading the producer checker. It verifies the reviewed-byte pins, five raw source contracts, 32 raw table entries, 32 cleared entries, 18 one-coordinate chart/section covariance identities, all 4,096 ordered-mask-pair/common-chart combinations, and all 256 inclusion mask/chart combinations. Its eight negative controls detect omission of ell, omission of either mixed endpoint charge, a legal-zero allowance, collapsing repeated occurrence factors, reversed I/P weight compensation, omission of the degree-three legal section frame change, and replacement of the actual root by a square root of ell. Normal and `-O` output agree in `normal.json` and `optimized.json`.

These controls are checks of the bound's explicit premises and bookkeeping; they are not claims that the actual matrix entries attain the upper bound or that cancellations could never improve it further. The mathematical arguments above establish the bound. The checks authenticate the selected source and detect the specific convention errors.

**Accepted closure:** the undifferentiated actual transition legal allowance drops from two to one per endpoint occurrence, with carrier four retained; the separate inclusion's extra legal allowance drops from two to one at its selected owner. Further full-source, lift, partition, derivative-engine, residual, and obstruction conclusions still require their own explicit arguments and checks.
