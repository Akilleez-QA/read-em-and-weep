# Independent mathematical review

Reviewed `PROOF.md`, SHA256 `c6c676ea6e1f0b6375c40ce3f400a851a3013fd7f88c3a1d343e3d4413fad6c9`.

Verdict: the constant cyclic Betti table and the displayed ordinary relative Tor splitting types follow from the pinned inputs. No mathematical correction is required. This is independent mathematical review, conditional on those inputs, not formal proof-assistant verification.

## Exact inputs checked

The proof files were read at the exact repository commits for PR499 (`1112189481554b0353c64178e3adc0dede2c3fbe`), PR513 (`df947c1ce092c0c59dcef187639147da8a7b2873`), PR514 (`d915ed6a7f0c679343447106707692eb7bdee6f7`), PR528 (`bd9a26837bb79b2e21cf35d6586d3ba3d6ca83fa`), and PR533 (`c2f8fd17d88e93606bba8a642d2af19dcac82d04`). In particular PR533 supplies the actual comparison rank rho=u, not a rank inferred from Hilbert series.

## Exhaustion of the long exact sequence

At internal degree zero the exact sequence on generators is 0 -> C -> C^2 -> C -> 0. At degree two, K_2=0 and Tor0(L)_2=0 force the two ten-dimensional quadratic Tor1 spaces to map isomorphically. Internal degree three contributes exactly Tor1(L)_3 of dimension15.

At degree four, Tor3(A)_4 injects into Tor2(L)_4 because Tor3(H)_4=0. The remaining comparison has rank u; hence dim Tor2(L)_4=u+(20-u)=20 and dim Tor1(L)_4=5+u-u=5. This remains valid at the exceptional parameters, without any semicontinuity assumption on column Tor sheaves.

Degree five contributes exactly Tor2(L)_5 of dimension26. Degree six contributes the extension of two twenty-dimensional spaces, giving Tor3(L)_6 of dimension40. Degrees seven, eight and ten contribute respectively Tor4(L)_7=5, Tor4(L)_8=10 and Tor5(L)_10=2. All other positive homological positions have zero adjacent H and A terms. Thus there are no omitted cancellations or surviving shifts.

## Base change and the degree-six bundle

Each internal Koszul strand of script L is a bounded complex of vector bundles. Starting with its bottom differential of rank zero, the identity h_i=n_i-r_i-r_(i+1) recursively determines every differential rank from the constant fiber homology dimensions. Constant rank implies locally split images and kernels, so homology bundles commute with fibers. This does not import the invalid degree-four column base-change assertion.

For the column degree-six strand the source is A_1 Lambda5(T)=T O and the target is A_2 Lambda4(T)=T(U'+W0)O(2). Levelness excludes a degree-one socle and therefore gives a subbundle injection. After removing T, central parity kills the W0 component. Since U'=Sym2(W) is irreducible, the remaining equivariant map O -> U'O(2) is unique up to scalar; injectivity makes its scalar nonzero. It is the binary quadratic Veronese column.

The quadratic evaluation sequence has kernel W O(-1): its two linear syzygies generate everywhere. Dualizing and twisting by O(2) gives 0 -> O -> U'O(2) -> W O(3) -> 0. Therefore Tor4(A)_6=T[W O(3)+W0 O(2)]. The two successive twists, from A to C and from M to script L, give the claimed O(5) and O(4) terms. The remaining extension by H_3^Tor O(1) splits because the relevant Ext1 groups are H1(O(4)) and H1(O(3)), both zero. Averaging a splitting preserves equivariance when the actual coefficient representations are retained.

The degree-five terms similarly acquire two twists from PR528; the top column Tor gives E O(4) in Tor4(script L)_7. The ordinary multiplicity notation does not identify the twenty-four character summands with a trivial normalizer representation. The displayed rank polynomial and the alternating parameter degrees agree with the Koszul Euler characteristics.

No selected HM/source-instance evaluation, numerical rank calculation, coefficient search, or large computation was used. This result determines free-module terms and ordinary relative Tor bundles, not resolution differentials, the Gorenstein middle obstruction, the fixed-pair residual, higher-order lifting, or algebraicity.
