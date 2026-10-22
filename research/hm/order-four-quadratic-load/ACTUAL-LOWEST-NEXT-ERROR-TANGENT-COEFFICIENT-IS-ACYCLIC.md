# The lowest next-error tangent coefficient is acyclic

## Exact result and limitation

For the actual marked vertex filtration, let E4 be the **associated-graded**, weighted-degree-four coefficient bundle of `B_Q(4)`. The lowest tangent-modulo-conjugation coefficient of `M(2)` is

`gr4 M(2)=Wprime O_L(-1)`.

Consequently both its H0 and H1 vanish, before taking invariants. More precisely, there is an exact coefficient sequence

`0 -> Wprime O_L(-1) -> E4 --tr(n·)--> Sym12(Wprime) O_L -> 0`.       (1)

Therefore the map on H0 in (1) is an isomorphism, and `H1(E4)=0`.

These are associated-graded statements. The full actual R2 has affine transition corrections involving known lower errors, the harmonic products, the conic transport, and the failed endpoint nilpotent lift. It need not be tangent and need not transform as a section of E4 before a compatible subtraction. Thus (1) is not a complete actual R2 comparison and does not imply the fourth value vanishes.

## 1. Tangent equation without deleting the trace constraint

The actual regular pair has leading odd cover degrees `deg f=3`, `deg g=5`. Write

`n=[[fg,-f²],[g²,-fg]]`.

A weight-four matrix `R=[[a,b],[c,-a]]` has entry degrees `(4,2;6,4)`. Its trace against n is

`tr(nR)=2fg a+g²b-f²c`.                         (2)

Assume only in this paragraph that (2) vanishes. Since f,g form a regular pair, reduction modulo f gives `f|b`. Degree two is less than degree three, so `b=0`. Now `2ga=fc`; coprimality gives

`a=f ell`, `c=2g ell`, `deg ell=1`.

Equivalently, with the fixed tangent map `tau(v)=sigma v^T J+v sigma^T J`,

`R=tau(0,ell)`,                                (3)

uniquely. The general tangent component degrees are `deg v1=weight-5` and `deg v2=weight-3`. At weight four these are minus one and one, so the first component is absent. Endomorphism diagonal weights are even; weight four is the lowest possible regular tangent weight.

A conjugator K with `[K,n]` of weight four would have weight minus four. Its entry degrees would be `(-4,-6;-2,-4)`, so no regular such adjoint exists. Thus no conjugation image changes (3) at this weight.

## 2. Physical line and complete marked transition

R2 has physical twist four. Since tau has twist two, its tangent preimage lies in `G(2)`, not G, G(-2), or G(4). The actual marked frame lines for G are `O(9/2),O(-5/2)`, and a positive cover-linear polynomial contributes `O(-1/2)`. Hence the lower coefficient line is

`O(-5/2+2-1/2)=O(-1)`.

Its representation factor is Wprime. The forbidden degree-minus-one first component would have coefficient line O(7), but there are no regular polynomials of that degree.

Here is the full coefficient transition, retaining the triangular term. Put `w=-1/z`, and write the marked sigma transition as

`sigma_x=P D sigma_y`,

`P=[[1,0],[p,1]]`, `D=diag(z³,z^-5)`.

For a tangent preimage in G(2) with component degrees minus one and one, the coefficient transition is

`v_x=P diag(z⁷,z^-1) v_y`.

Since `v1=0`, this becomes exactly

`ell_x=z^-1 ell_y(-1/z)`.

The triangular term does not create a hidden first component. Directly, the complete matrix transport is

`tau(sigma_x,v_x)=z²(PD) tau(sigma_y,v_y) (PD)^-1`.     (4)

Its diagonal, upper, and lower coefficient lines are respectively O(2), O(10), O(-6), as independently obtained from physical twist four and cover degrees four, two, six. Equation (4) incorporates the determinant factor of tau; it is not plain untwisted conjugation.

Thus the tangent coefficient really is `Wprime O(-1)`. Standard P1 cohomology gives `H0=H1=0` for this entire coefficient bundle.

## 3. Exact trace sequence and its proper consequence

The scalar `tr(nR2)` has physical twist six and cover degree twelve. Its coefficient line is O(6-12/2)=O, giving the target in (1).

For the actual cubic/quintic regular pair, the square-ideal Hilbert series is

`(1-t⁶-t⁸-t¹⁰+t¹¹+t¹³)/(1-t)²`.

It ends at degree eleven. Hence every degree-twelve polynomial lies in `(f,g)²`, and the map (2) is onto in this degree. This holds locally in the base for the actual flat regular-pair family, not just over a generic coefficient field. Its kernel is precisely (3), proving (1). No actual-instance matrix or rank test is used.

The long exact sequence, using the acyclicity of O(-1) and O, proves

`H0(E4) = Sym12(Wprime)`, `H1(E4)=0`.

Accordingly, **if** a degree-twelve scalar trace datum is a genuinely compatible global section in this associated-graded sequence, it has a unique global weight-four matrix lift. There is no independent global tangent choice. Likewise, a genuine Cech cocycle valued in the tangent coefficient can be removed, uniquely up to its nonexistent global sections.

These statements do not say that an arbitrary local quartic term vanishes. In particular, the nonzero local old-K quartic computed in `ACTUAL-LOWEST-NORMAL-CONNECTION-HAS-AN-EXPLICIT-NEXT-ERROR-TERM.md` is neither the complete R2 nor by itself a global tangent class. One must first assemble the full scalar trace and its compatible affine lift. Even after that, inhomogeneous lower-error terms in actual R2 transport require comparison; (1) alone does not dispose of them.

## 4. Retain the full differentiated-square constraint

Use the fixed actual midpoint first-normal nilpotent, with harmonic expansion

`Ncorr=L(n)+q L(T)`, `Ncorr²=q² L(chi) I mod q³`.

Let `Dq=rho q`, and retain the entire symbol `Hhat`, connection `Ahat`, and scalar `Lambdahat`. Put

`Ehat=Hhat D Ncorr+[Ahat,Ncorr]-Lambdahat Ncorr`

`=q L(R1)+q² L(R2) mod q³`.

There is no N2 hypothesis. The exact differentiated-square identity gives

`tr(nR2)+tr(TR1)+tr B1(n,R1)
 = H0 Dchi+2(H0 rho-Lambda0)chi`.                (5)

Both ordered B1 products occur before taking scalar half-trace. Thus the necessary trace datum for R2 is the **entire** right side minus both lower-error contributions on the left. The source chi is the nonzero actual scalar residue already proved in `ACTUAL-HARMONIC-NILPOTENT-HAS-A-NONZERO-SECOND-NORMAL-RESIDUE.md`; it cannot be removed by pretending a square-zero second-normal nilpotent exists. R1 has not been set to zero in (5).

At the leading weights, each scalar term in (5) has cover degree twelve: `8+4`, `4+8`, or `8+8-4`. Its square-ideal quotient is automatically zero in that degree, but its actual polynomial value is needed for the affine lift in (1). Vanishing of that quotient does not make R2 tangent.

## 5. The next weight remains open

The actual endpoint transition has a `q eta` term with eta of weight zero. Its effect on the first-normal connection can begin at weight four, and its failed nilpotent gluing changes T at weight eight. Consequently next-error expressions can receive weight-eight terms such as

`[K4,T4]`, `[K0,delta T8]`, and `B1(K4,n8)`.

Their weights are respectively `4+4`, `0+8`, and `4+8-4`. The exact finite conic transport and higher stabilizers must likewise remain in the complete calculation. The vanishing of the weight-four tangent coefficient does not exclude these terms or identify the full R2 with a homogeneous one. No higher endpoint class or fourth value is asserted.

## Verification

Run `python verify_lowest_next_error_tangent_acyclicity.py`.

It checks the universal tangent and trace formulas, the full diagonal-plus-triangular determinant transport, the physical coefficient lines, the forbidden conjugator degrees, the exact Hilbert/cohomology arithmetic, and the retained error weights. All four frozen nilpotence files and other prior sources remain unchanged.
