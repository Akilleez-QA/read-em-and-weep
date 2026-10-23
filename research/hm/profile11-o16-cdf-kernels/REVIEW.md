# Independent review: three necessary high-P kernels for the c-d-f source127 edge

## Verdict and exact reviewed versions

**PASS for the stated necessary-kernel reduction.** The proof establishes that the actual high-P kernel for the specified c-d-f source127 edge must have one of the three displayed forms. The basepoint-free premise is explicitly discharged by the pinned PR859 theorem. The proof does not establish realizability of a remaining form, exclude the entire source edge or its stable label, or change a global frontier count.

This review applies to these exact file contents:

- `PROOF.md` SHA256: `10030e0f7acc9ac4bb35efb29356c2a85132b88876983d58b8a359d2c660e07f`.
- `verify.py` SHA256: `baaddc25c21fe82c1e719108b56dce4345fca1e921648b9c55f071f383d40a0f`.
- `REPRODUCE.md` SHA256: `99d9778778bddfdc02df50532c19c30618b78f061dd9d34c9dfc308e4f15cf65`.

The reviewer read the proof and its pinned mathematical dependencies, inspected and ran the supplied verifier successfully, and independently recomputed the kernel characters and all relevant Hom dimensions using integer McKay-ring arithmetic rather than the verifier's quadratic-field character table. No selected actual source map, coefficient, point, derivative, instance matrix, or rank was evaluated. No external publication action was taken in this review.

## Source identity and dependency checks

All eight local source copies pass their manifest Git-blob hash checks. The original `pairs.json` entry127 contains the tuple `(0,0,1,1,0,1,0,0)`, has defect zero, and has `A=[[-8,"one"],[2,"one"],[16,"one"]]`. The original frontier record identifies it with `G3.11.cce6e3ba4eeb`, source_index127, original_defect0.

Applying the original decoder, rather than relying on the displayed rank/degree assertion, gives

    R_2=(c+g+h-1)V+(d+e+g+h)P+(f+g)D=P+D,
    E=(P+D) O(-2)+(V+P) O(-4)+O(-8).

Its rank is `4+5+3+4+1=17` and degree is `-18-28-8=-54`. The actual inclusion and strict-top sources supply saturation in the same constant bundle and `H0(E^-(2))=0`. The original zero-defect identification, also restated in pinned PR802, supplies the saturated actual quotient `A_q` in `(H O/E)(-2)`.

The added basepoint-free dependency is pinned at PR859 commit `6129e92a26572779003f3295227f688b77ed881c`, Git blob `79ec9cd555997cb9e3b8dc76f3b64fa3f836ad2e`. Its statement explicitly includes this exact source tuple. Its argument preserves the raw divisor-twelve external image as `O(4)`, obtains the exact kernel `V O(-4)`, proves the internal map zero, and only then shows that the rank-five raw span of degree minus two has zero saturation defect: a defect is at most two but any nonempty invariant defect divisor has degree at least twelve. The resulting quadratic-span contradiction is valid without a profile-(1,2) no-section hypothesis. Thus citing PR859 here does not silently replace an unsaturated external image by `O(16)` or assume the desired result.

The internal/external saturated-image lemma from PR796 is used with all its hypotheses verified in each excluded case. The first-polar generation principle from PR802 is used only after raw saturation has been established. No horizontal splitting of an abstract equivariant decomposition is assumed.

## Complete rank-three classification

The onto sequence has rank-three kernel of degree minus twenty-four. Injectivity on twist-two sections forces every splitting degree at most minus three. The only irreducible coefficient combinations of total rank three are a three-space, a two-space plus a scalar, and three scalars. Central parity makes the two-space degree odd and scalar degrees even; the only three-spaces are A and V. A scalar `O(-4)` contributes a forbidden invariant to the first cohomology budget.

These facts leave exactly the thirteen candidates displayed in the proof: two three-space cases, eight two-space/scalar cases with `(j,k)=(3,18),(5,14),(7,10),(9,6)`, and the three sorted scalar partitions `(6,6,12),(6,8,10),(8,8,8)`. The tiny degree partitions were independently checked; no omitted combination or cancellation is available.

The two exact budgets are independently confirmed:

    H1(K(2))=A+V+P+D,
    chi_G(K(3))=-(W+S+T).

Every row of the table agrees. Exactly five candidates satisfy both budgets:

    A O(-8);
    W O(-7)+O(-10);
    W O(-9)+O(-6);
    Wp O(-3)+O(-18);
    O(-6)+O(-8)+O(-10).

The independent ring calculation used the standard McKay products `W*1=W`, `W*W=1+A`, `W*A=W+S`, `W*S=A+D`, `W*D=S+T`, `W*T=D+V+P`, `W*V=T`, `W*P=T+Wp`, and `W*Wp=P`, together with `Sym(n+1)=W*Sym(n)-Sym(n-1)`. This is a distinct arithmetic implementation, not a second invocation of the supplied character code.

## Audit of the W O(-9)+O(-6) exclusion

Use target columns `D O(-4), V O(-6), P O(-6), O(-10)`. The complete equivariant Hom-dimension matrix, with source rows `W O(-9), O(-6)`, is

    1 0 0 0
    0 0 0 0.

The unique nonzero map in the first column is indeed the composite

    W O(-9) -> O(-8) -> Sym4 W O(-4).

The first map is the twisted Euler quotient and has kernel `O(-10)`; it is onto everywhere. The second is the fourth-power tautological inclusion, which is nonzero on every line in W and has locally free quotient. Their composite is nonzero, so multiplicity one identifies every nonzero equivariant map with it up to scalar. Its image is exactly the saturated `O(-8)`, not a torsion modification or merely a generic line.

Consequently the internal image is either zero or that line. The external `O(16)` is saturated by the already established dependencies. The actual-image lemma therefore gives saturated first spans with degrees ten or four. Both contradict being a subbundle of a constant bundle. The entire stated kernel form, not merely one scalar choice, is excluded.

## Audit of the three-scalar exclusion

For source rows `O(-6), O(-8), O(-10)` and the same target columns, the complete Hom-dimension matrix is

    0 0 0 0
    1 0 0 0
    0 0 0 1.

Thus every scalar choice is accounted for. A nonzero D component is the saturated fourth-power tautological line; a nonzero lower scalar component is an isomorphism. The images lie in distinct target direct summands, so the two-component image is saturated as well. The four possible images are exactly `0`, `O(-8)`, `O(-10)`, and their direct sum.

The zero and single-row choices give first-span degrees ten, four, and two, respectively, and are impossible. With both rows present the actual exact sequences give rank seven and degree minus four. First polars then force splitting only in degrees zero and minus one. Equivariant Euler characteristics yield

    C=chi_G(M)=-P+Sym18 W-Sym4 W-Sym6 W=A,
    C W+L=chi_G(M(1))=Sym19 W-Sym3 W-Sym5 W=W+Wp+T.

Since `A W=W+S`, the linear coefficient would be `L=Wp+T-S`, whose S multiplicity is minus one. This cannot be a genuine representation. The rank and degree alone would not suffice for this last alternative; the proof correctly supplies the additional character obstruction and retains both internal rows until that point.

## Remaining interfaces and evidence boundary

The remaining forms have nonzero possible internal channels, confirmed independently and by the supplied verifier:

- `A O(-8)` has the D channel.
- `W O(-7)+O(-10)` has the W-to-D and lower scalar channels.
- `Wp O(-3)+O(-18)` has the scalar-to-D and scalar-to-P channels.

They are not eliminated merely because the other two kernel forms fail. The proof appropriately leaves their actual-connection compatibility and complementary endpoint constraints open.

`python3 verify.py` passes against all eight pinned inputs. Its assertions check the stated abstract characters, Hom multiplicities, rank/degree arithmetic, original catalog identifiers, and input hashes. Classification exhaustiveness and the actual saturation, universal-map, and first-polar arguments remain written mathematical proofs, audited above. This review is not proof-assistant certification and gives no whole-edge or whole-label exclusion.
