# Independent audit: finite-dual presentation and Betti table

Verdict: PASS. Reviewed the complete proof at SHA256 `3a8666fbb9f83153ebbd3334292c74b85ee4ab0ac1c13ae2b5c014df84a5478a` directly against the original candidate's multiplication normal forms. No correction remains.

## Independently checked new conclusions

- The socle is exactly the terminal degree-three pair. Every lower homogeneous B-weight line has a nonzero parameter product; the indicated degree-one orbit and opposite pair are nonisomorphic irreducibles. Thus no lower socle is concealed by a nonhomogeneous linear combination. The action g²=−ε and central character ω² on the terminal pair agree with the original normalization.
- The four proposed linear dual annihilators follow by transposing x_iF_j=δ_ijG_j. The top of the normalized finite dual is the dual of the socle, so the two generators suffice. The canonical determinant-line factor is retained uniformly; it changes equivariant characters but not these module relations or their dimensions.
- All eight cubic values were checked separately on t1,t2,t3,t4. In particular the four paired value pairs are (−ε/λ,1), (−ε,−ε/λ), (1,1/λ), and (1/λ,−ε), giving precisely the displayed signs and coefficients.
- After the linear annihilators the module is the direct sum of two polynomial planes. The four cubic relations project isomorphically to both complete cubic monomial bases. Parameter multiplication therefore kills all quartics in both planes; the quotient has exact Hilbert function (2,4,6,4). The surjection onto the finite dual has equal length and is an isomorphism. The linear and cubic relations are minimal and complete.
- Graded duality complements degrees to seven, retaining the canonical character. Hence the dual presentation determines F3(P)=S(−4)^4⊕S(−6)^4 and F4(P)=S(−7)^2. Direct expansion of the Hilbert numerator gives the stated polynomial. With F0 and F1 already fixed by the original exact presentation, it forces F2(P)=S(−2)^4⊕S(−3)^6⊕S(−5)^2. Total Betti numbers are (4,10,12,8,2), reversed for the finite dual.
- The conditional rank counts for a reflexive rank-two realization follow from the finite dual's two generators and eight first relations: rank F2=2, rank F1=8+u and rank F0=8+u. The proof does not identify the required realization or its Tor map.

The independent calculation is also recorded in `INDEPENDENT-DERIVATION.md`. This is a symbolic mathematical review, not a compiler or formal-verification result. It uses no actual HM source, selected operation or matrix instance. The new result supplies concrete local presentation and resolution data; it does not establish geometric realization, higher-order cancellation or algebraicity.
