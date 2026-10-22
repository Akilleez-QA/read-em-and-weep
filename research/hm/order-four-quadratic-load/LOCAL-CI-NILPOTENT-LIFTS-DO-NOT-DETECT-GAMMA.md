# Local CI(3,5) nilpotents lift through first-order A1 smoothing

## Checked result and restriction

The canonical vertex nilpotent admits a formal local first-order nilpotent lift through an arbitrary transverse A1 smoothing. Thus the local complete-intersection model, or nondeformability of a maximal Cohen--Macaulay spinor, cannot alone prove the global smoothing coefficient gamma nonzero. The lift below is local; no global gluing or flat spinor image is claimed.

## 1. Local model and square-ideal regularity

Work over the generic vertex field k, in B=k[[a,b]], with R=B_even=k[[X,Y,Z]]/(XZ-Y²). Let f,g be odd functions with coprime initial homogeneous forms f3 and g5 of degrees3 and5. These are the actual local CI orders established from the vertex Loewy dimensions and the free middle term.

The homogeneous square ideal (f3,g5)² has resolution

    0 -> k[a,b](-11) plus k[a,b](-13)
      -> k[a,b](-6) plus k[a,b](-8) plus k[a,b](-10)
      -> (f3,g5)² -> 0.

Indeed its generators are f3²,f3g5,g5² and its two syzygies are (g5,-f3,0), (0,g5,-f3). Coprimality makes this the Hilbert--Burch resolution. The quotient Hilbert series is

    (1-t6-t8-t10+t11+t13)/(1-t)².

Every coefficient in degrees at least12 vanishes. Since the initial ideal of (f,g)² contains (f3,g5)², successive cancellation of initial forms, followed by completeness, gives

    (a,b)^12 subset (f,g)².

This filtered containment does not assume f,g homogeneous. Ideals in the complete Noetherian ring are closed, so the convergent successive correction lies in the actual square ideal. For an even element, averaging the coefficient expressions under (a,b)->(-a,-b) makes all three coefficients even, because f²,fg,g² are even.

## 2. Correcting the determinant

The canonical nilpotent in a local free frame has the form

    N = [[-fg,f²],[-g²,fg]].

Choose tracefree ambient lifts of its three entries to k[[X,Y,Z]], preserving their positive-coordinate orders3,4,5. Their determinant vanishes modulo q0=XZ-Y², so

    det(N_tilde)=q0 H.

The determinant has positive-coordinate order at least8; hence H has order at least6, or cover order at least12. The containment above shows H belongs to (f²,fg,g²) in R.

On the first-order deformation q0+epsilon c=0, epsilon²=0, the uncorrected determinant is -epsilon c H. The linear determinant variation of a tracefree correction matrix ranges over precisely the ideal (f²,fg,g²): its coefficients pair with the three entries of N, with the harmless invertible factor2 on fg. Therefore there exists a tracefree correction K such that

    N_epsilon=N_tilde+epsilon K,
    det(N_epsilon)=0 on q0+epsilon c=0.

For a tracefree two-by-two matrix, Cayley--Hamilton gives N_epsilon²=0. This constructs a formal local nilpotent lift for every smoothing coefficient c.

## Limit

A nilpotent lift need not have a flat rank-one reflexive image or kernel across the infinitesimal smoothing. Nor does this calculation solve the global cocycle needed to glue the lift. The global gamma obstruction may remain nonzero even though this local nilpotency obstruction vanishes identically. This theorem excludes a purely local nilpotency argument; it does not settle gamma in either direction.
