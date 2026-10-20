# A residual-rank-one middle surface must be an integral invariant quintic

## Assumptions and conclusion

Assume the conditional generic-rank-ten setup and full normalizer equivariance of /research/hm/normalizer-rank-five/quintic-normalizer-exclusion/COROLLARY.md. In particular X=P4, G is a rank-fourteen vector bundle, and

    0 -> G -> O^20 -> R -> 0,
    0 -> O(-3) -> O(-1)^15 -> G -> 0,

with R torsion-free of rank six. The rank-four repeated-input subbundle splits off locally, leaving the normal quadratic map Q of sizes 16 by 10. Import the established bound delta<=70 for the total codimension-two cycle of S=Ext^1(R,O), from /research/hm/middle-surface/rank-ten-fitting-strata/ADDENDUM.md. The symmetry is the stipulated N=H5 semidirect SL2(F5), with H5/Z(H5)=F5^2 and its standard conjugation action.

Let Y be the reduced union of the surface components of {rank Q<=1}, and assume Y is nonempty. Then:

1. Every component has singularity-cycle multiplicity at least twelve.
2. Y is an integral N-stable surface of degree five.
3. Its multiplicity m in [S]_2 is one of 12,13,14, so its contribution to delta is 60,65,70 respectively.
4. If m=12, the generic defect T=(R**/R)_eta, after completion of the regular local surface ring A=O_(X,eta), has the abstract module form

       T = (A/m_A^2)^3 direct-sum k^3.

5. Writing the Hilbert polynomial of O_Y as

       5 binom(t,2) + (6-g)t + chi(O_Y),

   its sectional arithmetic genus satisfies g=1 modulo 5 and chi(O_Y)=0 modulo 5.

These conclusions constrain the only middle-surface candidate for affine dimension eight identified in /research/hm/universal-polar/rank-one-residual-fiber-model/GLOBAL_FRONTIER.md. They do not assert existence or exclude an arbitrary singular integral quintic surface.

## 1. Local multiplicity bound, with the rank-six budget retained

Fix the generic point eta of a surface component on which Q has residual rank r. Put j=10-r and A=O_(X,eta), a regular local ring of dimension two. Here the codimension-two support has finite length after localization. Let T=(R**/R)_eta. Reflexivity implies R**_eta is free of rank six, so T is a quotient of A^6 and mu(T)<=6.

The established local duality in /research/hm/middle-surface/rank-ten-fitting-strata/PROOF.md gives

    S_eta = Ext^2_A(T,A),
    length(S_eta)=length(T)=lambda.

The presentation of S as the transpose of Q gives mu(S_eta)=j. Matlis duality interchanges minimal-generator dimension with socle dimension, hence dim_k Soc(T)=j. This can equivalently be seen from a minimal free resolution over A and its dual. No geometric-point algebraic closedness is needed.

After completion choose a coefficient field k and regular parameters x,y. Write mu=mu(T). Each multiplication map x,y:T->T kills Soc(T), so each has k-rank at most lambda-j. Since m_A T=xT+yT,

    lambda-mu = dim_k(m_A T)
               <= dim_k(xT)+dim_k(yT)
               <= 2(lambda-j).

Consequently

    lambda >= 2j-mu >= 2j-6.

Also lambda>=j. Thus the general local bound is

    lambda >= max(j,2j-6).

At residual rank one, j=9 and lambda>=12. At residual rank zero the even stronger lambda>=14 holds, although that stratum is independently excluded in the established repeated-input setting. For the present Y it suffices that j>=9, so every generic multiplicity is at least twelve, even without importing the rank-zero exclusion.

The coefficient of the component in [S]_2 is precisely lambda, by the definition of the associated codimension-two cycle and the cited local-duality equality. It follows that

    12 degree(Y) <= delta <=70,

hence degree(Y)<=5.

## 2. Equivariance forces degree five and irreducibility

The locus rank Q<=1 is N-stable, and taking its reduced union of two-dimensional irreducible components is functorial under N. Thus Y is N-stable and O_Y is H5-equivariant. The proper-support Hilbert congruence proved in /research/hm/local-defect/heisenberg-defect-hilbert-congruence/PROOF.md implies that degree(Y) is divisible by five. Therefore degree(Y)=5.

For any H5-orbit of irreducible components of Y, its reduced union is H5-stable. Its degree is likewise a positive multiple of five. Thus there is exactly one H5-orbit of components. The center acts trivially on P4, so orbit size is 1,5, or25. Degree five leaves only size one, or size five with each component a plane.

Suppose there were five planes. The projective group A0=H5/Z(H5)=F5^2 acts transitively on their set. Its permutation image is a transitive abelian group of order five, so the kernel is a one-dimensional F5-subspace L of A0. Because the entire five-plane set is N-stable, this kernel is preserved by conjugation by N. Hence L would be invariant under the standard SL2(F5) action on F5^2. No such line exists: SL2(F5) is transitive on its six projective lines. This is a contradiction.

Therefore Y is integral of degree five. Since its weighted contribution is 5m, the local lower bound and global upper bound give 12<=m<=14. In the established source setup residual rank zero is impossible, so its generic rank is precisely one. Alternatively, if residual rank zero were allowed, the conclusions through degree and irreducibility still hold, but m=14 would not distinguish ranks zero and one.

## 3. Equality normal form at multiplicity twelve

Assume generic residual rank one and lambda=12. The inequalities in Section 1 force mu(T)=6 and equality throughout. Therefore xT and yT both have dimension three and meet trivially. Each multiplication has a nine-dimensional kernel, equal to Soc(T). Commutativity gives

    y(xT)=x(yT) subset xT intersect yT=0.

Thus xT lies in ker(y)=Soc(T), and similarly yT lies in Soc(T). Hence m_A^2 T=0.

Let U=T/m_A T, dimension six. Multiplications induce surjections X:U->xT and Y:U->yT. Their common kernel is Soc(T)/m_A T, dimension three. Since each individual kernel also has dimension three, these kernels coincide. Choose a complement U0 of dimension three. Both X and Y restrict to isomorphisms from U0 onto their respective images. Each basis vector of U0, together with its x- and y-images, generates a copy of A/m_A^2. Their images are independent, yielding three such summands. The remaining three-dimensional common kernel contributes k^3. This proves the displayed abstract local normal form. Choices of coefficient field and bases make this description noncanonical; no equivariant splitting is claimed.

## 4. Hilbert constraints

For an integral degree-five surface the polynomial is

    P_Y(t)=(5/2)t^2+(7/2-g)t+chi(O_Y)
          =5 binom(t,2)+(6-g)t+chi(O_Y),

where g is the arithmetic genus of a general hyperplane section. The H5 proper-support theorem states that every integral-binomial coefficient is divisible by five. Therefore 6-g and chi(O_Y) are divisible by five, proving the claimed congruences. This does not identify g, impose smoothness or normality, or transfer chi to the normalization.

## Scope and checks

The advance beyond the existing total defect interval is the use of rank(R)=6 to strengthen local corank nine to multiplicity at least twelve, followed by equivariance to isolate an integral quintic. The no-quintic-divisor theorem is not misapplied to this codimension-two surface.
