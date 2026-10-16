**D01 review: accept. \(I_{20}\) is a complete minimal family of constant maps, retaining all 81 cohomological outputs per map.** This strengthens my earlier review; it does not supply 32 selected independent output rows or decide \(R^\sharp\).

Work over \(\mathbf Q\). Write \(P=08b73637d4136f91606aad332c46cafd064417f8\), \(H=e6e8d272e760a432dbbc1053b88c8eae03a47304\), and \(C=\operatorname{End}(K)\).

**Derived identification and signs.** Since \(K\) is perfect, the supertrace pairing identifies \(C^\vee\simeq C\). Hence
\[
\operatorname{Hom}_{D(\mathbf P^4)}(C,\mathcal O(-2)[2])
=\mathbb H^2(C^\vee(-2))
\simeq\mathbb H^2(C(-2)).
\]
The target has its sole term in degree \(-2\), agreeing with \(P\): `research/hm/current-scalar-proof/map-and-comparison.md`, §1.

With the free-coordinate convention in \(H\): `research/hsd/twist-minus2-d5/certificate.py`, \(j=15b+i\), the positive cycle \(K_j=(A,B)\) has \(B_{b,i}=1\) and
\[
A_{5b'+k,a}=\delta_{b'b}\gamma[i,a,k].
\]
Consequently
\[
\operatorname{str}(XK_j)
=\sum_{a,k}\gamma[i,a,k]X_{02}[a,5b+k]-X_{13}[i,b]
=-L_{i,b}(X).
\]
Thus the global duality identification really sends \(L_{i,b}\) to \(-[K_j]\).

**The decisive implication.** At twist \(-2\), line-bundle cohomology leaves only the \(H^4\) row at internal degree \(-3\), and the \(H^0\) row at degrees \(2,3\). Therefore the published \(d_5\) images are actual hypercohomology boundaries. The ten coordinates in \(H\): `research/hsd/twist-minus2-d5/NOTE.md` imply relations of derived morphisms:
\[
L_{r,0}+L_{10+r,1}=0,\qquad
L_{10+r,0}+L_{5+r,1}=0
\quad(0\le r<5).
\]
These are neither pointwise identities nor asserted global homotopies in the original bundle complex.

The disjoint pairs eliminate precisely the ten omitted labels from
\[
I_{20}=\{(i,0):5\le i\le10\}
\cup\{(i,1):0\le i\le14,\ i\ne5\}.
\]
Thus these twenty maps span all thirty as derived morphisms.

**Pullback and all 81 outputs.** For the finite flat symmetric map \(\rho:Y=(\mathbf P^1)^4\to\mathbf P^4\), pullback and tensoring by the full-sign line \(T=\mathcal O_Y(-2,-2,-2,-2)\) preserve these relations. Their target is
\[
\rho^*\mathcal O(-2)\otimes T[2]
=\mathcal O_Y(-4,-4,-4,-4)[2],
\]
exactly the pinned scalar target. Therefore every relation holds in its entire 81-dimensional \(H^4\), with the pinned Laurent coordinates. The twenty-map operator has **the same kernel on the entire full-sign \(H^2\)** as all thirty.

By the accepted all-thirty lemma from \(P\): `structural-relations.md`, §4, and the geometric permutation argument underlying comments **6130352358/6130391535**, that kernel intersects the actual characteristic-zero epsilon sector trivially.

**Minimality.** On its 20-dimensional first block, each constant map contributes at most one scalar dimension. Hence fewer than twenty cannot separate the sector; \(I_{20}\) attains the bound.

**Failure control/dependency:** completeness uses the accepted rational all-thirty and geometric-action premises. No characteristic-three conclusion follows. Authenticating and evaluating complete corrected \(R^\sharp\), including comment **6205127744**’s derivative terms, remains unresolved. No arithmetic tests ran.

Reviewer: **V07/root**. Next: review this upgrade, then authenticate the twenty full scalar images.