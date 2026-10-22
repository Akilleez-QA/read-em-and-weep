# Independent mathematical review

## Verdict

PASS for the complete Gamma-equivariant ambient middle-operator family in the natural marked Koszul model and its exact vertex-restriction kernel, with the scope stated in `PROOF.md`. This is a structural mathematical review with bounded exact character checks, not proof-assistant formalization or a verification of the coupled monad-source equations. The physical-marking bridge is restricted to induced adjoint classes on the cone; no equality of arbitrary global monad-gauge actions is certified.

## Exactness and presentation

The pinned [global presentation](https://github.com/Akilleez-QA/read-em-and-weep/blob/b7fd2c946b39301bdb226af362674e1b2e755097/research/hm/global-skew-middle-presentation/PROOF.md) was read directly. Its Koszul resolution of `E(1)` locally splits into its degree-zero cohomology and contractible complexes. In characteristic zero, taking its graded symmetric square therefore resolves `Sym^2 E(1)`. The degree-one generators contribute `Lambda^2 G1`, while the degree-zero and degree-two cross term is `G2 tensor G0`; these signs and summands agree with the proposed presentation.

After twisting by three, the leftmost sheaf term is `Sym^2 G2 O(-1)`. It has no cohomology on projective four-space, and all the other displayed line-bundle terms have vanishing higher cohomology. Thus its omission from the global-section sequence is justified. The four remaining terms are exactly `C3,C2,C1,C0` in the proof. This is an exact presentation, not merely an Euler-characteristic dimension calculation.

Taking the center-even summand and then `Hom_Gamma(P2,-)` is exact over C. The resulting dimensions are

    0 -> C^6 -> C^103 -> C^744 -> C^1850 -> F -> 0,
    dim F = 1203.

The relation image consequently has dimension 647.

## Actual source weight and physical parity

The pinned [canonical lift](https://github.com/Akilleez-QA/read-em-and-weep/blob/3333cce744b3bd8e4472969f599588fec3e20d52/research/hm/order-four-quadratic-load/ACTUAL-MULTIPLIED-NILPOTENT-HAS-A-CANONICAL-SQUARE-ZERO-LIFT.md) identifies `U=Wprime` and the natural linear cochain `Z_a=k e_a`. The pinned [fifth-neighborhood comparison](https://github.com/Akilleez-QA/read-em-and-weep/blob/2e20281e6eb850904093af3a6c737f3ee0ed28f2/research/hm/order-four-quadratic-load/ACTUAL-FOURTH-BOCKSTEIN-AS-A-FIFTH-NEIGHBORHOOD-ADJOINT-BOUNDARY.md) gives the divided primitive equation `d C_h=a h Z_a-q V_h`. These support degree `(2,1)`, rather than the parameter degree of the later multiplied ladder.

The [Serre-involution source](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/ACTUAL-LOWER-COHOMOLOGY-SERRE-INVOLUTION-SPLITTING.md) explicitly scales the negative block by `mu`, with `mu^2=-1`, and distinguishes its square, physical inversion, from the additional Serre involution. Its scalar-conjugation argument identifies these actions on induced adjoint classes on the cone. It does not identify every possible monad-gauge lift. It also identifies the positive quadratic quotient with `D5`.

The central element acts on `H=V+W` as `(+1,-1)`. Its additional scalar on `U` cancels in endomorphisms, and the twist-four linearization agrees with the natural coordinate involution `iota=diag(+I_V,-I_W)`. Both determinant characters retained in the presentation are trivial. Consequently the center-even source `P2=Sym^2 A tensor D` can map only to the center-even sector. The natural iota parity adds no independent restriction. This is not a certificate that every separately chosen physical gauge has the same action on raw middle cochains. The additional Serre-phi eigenspace condition is not imposed.

## Vertex restriction and its kernel

The pinned global presentation proves surjectivity of full vertex restriction using the restriction of Koszul generators and multiplication of binary forms. Its center-even block is `(U tensor V) tensor (U tensor V) tensor D`, of dimension 180. Exactness of the equivariant-family functor gives a surjective 90-dimensional family target and a 1113-dimensional kernel.

For `Q:C0 -> R_Z` and `C0^Z=ker Q`, every relation from `C1` lies in `C0^Z`, since it already maps to zero in `R`. Surjectivity onto the vertex target gives `dim Phi(C0^Z)=1850-90=1760`. Restricting the exact presentation therefore yields the claimed exact sequence with dimensions `6,103,744,1760,1113`. There is no unproved vertex cokernel hidden in these subtractions.

## Reproducible checks and limitations

`python verify.py` completed successfully after the explicit expected-value assertions were added. It checks all displayed multiplicity vectors and family dimensions, full character-table orthogonality, determinant characters, the source symmetric square, and zero source-family multiplicity in the opposite natural-iota sector. Additional exact checks confirmed `Sym^2 U=V`, `Sym^2 V=1+D`, and that every center-even irreducible has zero multiplicity in the natural-iota-negative global sector. Character arithmetic does not establish the separate physical-gauge comparison discussed above.

No actual HM coefficients, selected source values, geometric point evaluations, monad matrix ranks, or fourth Bockstein values were computed. The 1203-dimensional space is the complete ambient ansatz, not a solution space of the source-arrow equations. Likewise, the 1113 vertex-preserving directions are not proved to span the simultaneous ramification target. These distinctions are maintained in the proof.
