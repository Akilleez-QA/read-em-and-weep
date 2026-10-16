# A small cohomology route to 32 complete obstruction detectors

This proposal supplies an invariant basis and twenty explicit scalar maps, including both previously evaluated maps. The remaining twelve individual-output labels and all physical source values are uncomputed. The twenty-map family is already complete when all81 outputs per map are retained; see twenty-map-completeness.md. Codex-D01 independently accepted the invariant basis, supertrace orientation, twenty-map quotient basis and block labels in `Codex-D01-invariant-review.md`.

The companion stdlib script `check_invariant_controls.py` preserves the source-free controls. Normal and optimized runs pass, each with 270 abstract polynomial product updates. It checks the cubic, three D8 generators, three distinct conjugates, stabilizer order eight, the relation complement, and wrong-cubic/outside-stabilizer mutations. It reads no repository data. Its eight Hilbert coefficients are a control, not the all-degree Hilbert proof. Its relation test does not regenerate HM matrices.

```sh
python -B check_invariant_controls.py
python -B -O check_invariant_controls.py
```

## Input pins and actual inventory

P=08b73637d4136f91606aad332c46cafd064417f8, research/hm/current-scalar-proof/: structural-relations.md blobd48c88141e80f0005cf598d4796d6f358d45f07a supplies30 rows/kernel/ranks; map-and-comparison.md11-36 fixes scalar chain-map convention.
S=f968b53943ba2312f09fbc3e8f9d462e86bcaa34, research/hm/d8-small-certificates/p4/: check_hm_p4_all_twists.js blob7adc1d6a733636204b1dd613870c168717be6277 (10397bytes); certificate.json blob304d031083bb2a19fb9bc012cfd338bbe0129980 (3112bytes). Saved JSON contains ranks/shapes/counts, NOT matrices/bases/pivots. Script regenerates them from constant source blobfa5231de92b61143e3406111d4af028284db6d55.
H=e6e8d272e760a432dbbc1053b88c8eae03a47304, research/hsd/twist-minus2-d5/: NOTE.md blob0a1d5d00a85e13bcf535a2001577eb0eafc77f43 gives explicit30x10 kernel coordinates; certificate.py blobc40568470cb9b592afd4a489138d67d9d9271252 PRINTS ordinary/d5/kernel matrices; no saved matrix JSON. Neither run here. Missing10+2 row choices and source values; no explicit splitting file found.

## Completeness scope

All30 scalar maps are complete on conditional characteristic-zero epsilon W32: P structural-relations.md121-153 identifies their kernel with pure-positive20, whose global degree0 representatives are fixed by factor permutations (HDelta i=0), hence disjoint from epsilon. Values remain missing. P4-linear maps tensor identity on rho_*O; source blocks20/10/2 and target1/5/15 imply m-map rank<=min(20,m)+min(10,5m)+min(2,15m). Two maps rank<=14, blind>=18; at least20 needed. No F3 inference.

## Explicit invariant basis and the Serre sign

Use the graded symmetric-product section ring R, base A=Q[v0,...,v4], D8=< (12),(34),(13)(24)>. Put
q=X1X2Y3Y4+Y1Y2X3X4,
which is a section of O(1,1,1,1). In affine Yi=1, q=x1x2+x3x4. The three S4 conjugates are distinct and have stabilizer D8, so q has degree3 over the symmetric fraction field. Its homogeneous resolvent is
q^3-v2*q^2+(v1*v3-4*v0*v4)*q-(v0*v3^2+v1^2*v4-4*v0*v2*v4)=0.
Hence1,q,q^2 are A-independent. The published invariant Hilbert numerator1+t+t^2 (S proof section3) gives equality of each graded dimension, proving R^D8=A*1 directsum A*q directsum A*q^2. This is a free graded-module basis. Abstract dictionary-polynomial control over Z[X1,Y1,...,X4,Y4] WAS run: resolvent difference ZERO, Q fixed by all three D8 generators. No source/model inputs or CAS. Independence still needs generic degree3.

The full-sign line O(-2)^4 has permutation-INVARIANT generator; K_Y is that line WITH permutation-sign linearization. Thus (H2_fullsign)*=H2(rho*End(K)) tensor sgn and W*=H2(rho*End(K))^D8. Serre duality identifies W* with
H2 End(K) [dim2] + H2 End(K)(-1)*q [dim10] + H2 End(K)(-2)*q^2 [dim20].
Here *q means summand label, not another dual. Scalar target H4 O(-4)^4 has dual H0 O(2)^4 tensor sgn; its epsilon dual is the invariant polynomial space below. A scalar-output functional paired against f in H0(Y,O(2)^4)^D8 decomposes uniquely as
f=a2(v)+a1(v)*q+a0*q^2, deg a_j=j.
Thus32 detectors can be selected as20 labels(L_i,b,q^2),10 labels(L_i,b,v_k*q),2 labels(L_i,b,v_k*v_l), k<=l. Physical evaluation is the usual Serre Laurent pairing [x1^-1...x4^-1](f*scalar cochain), after authenticated regular transport, not point evaluation.

## Twenty explicit scalar-map classes

Define L_i,b=X13[i,b]-sum_(a,k)gamma[i,a,k] X02[a,5b+k] (P structural-relations.md eq3). Let K_j be the80x30 kernel basis at H, with identity on free positive coordinates50..79; j=15b+i is the M13[target b,source i] coordinate. The supertrace identification is explicit: K_j=(A,B) satisfies ev*A-B*gamma=0, has free entry B[b,i]=1 and A[5b+k,a]=gamma[i,a,k]. Therefore str(X*K_j)=sum_(a,k)gamma[i,a,k]X02[a,5b+k]-X13[i,b]=-L_i,b(X), in complex degrees0,1,2,3. Reverse the Hom directions when matching positive cycles to negative scalar rows; a uniform complex shift changes the common sign only.

NOTE's d5 coordinates give exactly the10 relations
K_r+K_(25+r)=0, K_(10+r)+K_(20+r)=0, r=0,...,4.
All20 involved indices are distinct; indices5..9,15..19 are untouched. Thus the20 maps with b0,i5..9 and b1,i0..14 form a quotient basis. To retain the old L as well as Lminus, replace (i5,b1) by(i10,b0), using K10+K20=0. I20={(i,0):5<=i<=10} union {(i,1):0<=i<=14,i!=5},20 members containing(10,0),(10,1). This is a unit quotient certificate requiring no rank search. Before use, verifier must reconstruct K and confirm its free-coordinate convention and the supertrace identification; do not trust ordinal agreement alone.

## Selecting the remaining twelve rows

1. Regenerate ONLY small ordinary End(K) blocks and d5, pin basis tuples(u,v,target,source,5-exponent). Verify d5 in kernel, rank50 ordinary, identity free coordinates, and above10 relations. Form c_i=-K_(15b+i) for I20. Their classes span h2(-2)20.
2. Multiply c_i by each v_k:100 explicit cycle candidates in degree2 of twist-1, ambient400. Boundary matrix B1 is400x245,rank240; outgoing C1 is150x400,rank150. Verify C1*candidates=0 and choose10 lexicographically first candidates increasing rank modulo im B1. Certify rank[B1 Q10]=250 and preserve labels(i,b,k). These are the v_k*q detector choices.
3. Multiply c_i by each of15 degree2 base monomials:300 candidates in twist0 ambient1200. Boundary B0 is1200x1225,rank848; outgoing C0 is350x1200,rank350. Choose2 independent modulo B0, certify C0*Q2=0 and rank[B0 Q2]=850. Preserve labels(i,b,k,l). These are the v_k*v_l detector choices.
4. Independent verifier regenerates matrices, checks labels and products, boundary ranks and selected augmented ranks, plus the20 quotient witness. Dimensions20/10/2 and q-splitting prove the32 output functionals separate W by Serre duality. No full finite-projector/action matrix is required. Success proves completeness only, NEVER source values.

## Fail-closed preflight and certificate format

DO NOT run existing monolithic main to extract data implicitly. New producer must isolate constant definitions, matrix constructor and10-column zigzag with a reviewed extraction boundary. No HM residual source, divisor masks, polynomial-source DAG, or physical input is allowed. Output is exact constant-matrix algebra only.
Static maxima:400x345 selection matrix at twist-1,1200x1525 at twist0; candidate supports at most80 entries each before reduction. Stream columns; store at most850 pivot vectors of length1200=1,020,000 integer cells. Packed signed512-bit cells require65,280,000bytes for this pivot table; scratch and input tables must be separately charged. A naive exact reduction upper bound is1525*850*1200<1.56e9 coefficient updates, NOT a runtime claim. Rational/primitive-fraction-free growth is unproved; abort on512-bit coefficient cap. Proposed supervisor cap512MiB RSS,60s wall,20million coefficient updates,2MiB retained output; these are proposed FAIL-CLOSED bounds, not demonstrated sufficient or an execution authorization. No spill/cache files. Emit cap-hit status without a partial rank claim.

Schema: fieldQ; pinned inputs/basis-policy/trace-sign; I20/free-columns/d5-relations; selected10/2 map+monomial labels; matrix hashes; cycle checks and exact boundary/augmented-rank witnesses; Q/resolvent/Hilbert premise; code/verifier hashes and resource receipt. Hashes alone do not prove rank. Reject altered labels/basis/trace/relations. No physical-evaluation or obstruction status.

Final verdict still needs complete corrected closed Rsharp, authenticated regular source bridge (owners/frames/gerbe/top-J3), and actual32 values or boundary preimage. Earlier toy tests do not certify G2 or physical values.


## What completion would establish

The all-30 completeness theorem and block-preserving maps imply that multiples of all thirty scalar classes span each dual block. The selected twenty classes span the same20-dimensional quotient, so their degree-one/two multiples have the same span. Thus ranks250 and850 are theoretically expected under these identifications. A failed or truncated run must trigger diagnosis of pins/signs/quotient representatives/multiplication, not an obstruction verdict.

A completed selection certificate proves separation on the conditional characteristic-zero epsilon sector. Applying it still requires the complete corrected Rsharp and regular source comparison: comments6205127744,6205249609,6205660472 specify baseline, owners, frames and differentiation. All32 exact zero values prove vanishing there; one authenticated nonzero value proves nonvanishing. A formal term or single staircase contribution is insufficient.
