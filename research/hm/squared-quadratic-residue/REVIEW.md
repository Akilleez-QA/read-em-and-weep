# Independent scoped mathematical review

Reviewed edition: PROOF.md SHA256

    d26e27c3d54a96352742424728c0f7fa4d365e954f923afd70964670b632cf99

Conclusion: the new deductions in Sections 1–4 are valid relative to the pinned geometric and cohomological inputs. This is an independent mathematical review, not formal machine verification or an evaluation of any selected HM pair.

## Imported premises and scope

The review takes as inputs PR457 at 961694c4f3c805f0d58508811a42da4030dce7a6 (canonical residue duality, ordinary restriction transpose, and cubic naturality), PR463 at 8ec3631dcd6937e6cc7491d0200c1c78b5d21434 (degree-one residue model with zero primary image, injective degree-four restriction, the actual order-four direct sum and Q_4 bound), PR462 at a10049b8f7c57f30476c6f9c5554685583ea8c1b (injective eight-dimensional primary cup image), and PR458 at b46c3b48a8b10a7d0656fde247f2c3f258d1fd23 (Q_5 supported-line bound). The underlying HM geometry and those earlier proofs are not independently re-proved here. Their exact use is consistent with the statements quoted in this proof.

## Checks

1. Projecting aH^1B(1)+vH^1B(2) to A/L factors the second summand through its primary quotient. Duality therefore imposes both quartic and cubic restriction conditions on the same constant tuple. No primary source is improperly discarded from degree one, since that primary space is zero. The usual quotient sequence gives (2), and naturality embeds a space of dimension 4r_v in L intersect U. This proves the inequality (3), not an unwarranted equality when r_v<2.

2. Since gcd(u,v)=1, gcd(a,v)=1 for a=u^2. If vf=ag with deg f=4 and deg g=3, polynomial unique factorization forces f=ca,g=cv. This proves both the representation ambiguity for a septic and the kernel description of Phi. Restriction injectivity excludes a vanishing on all twenty-five lines, so supported tuples on the k common-contained lines are independent modulo diagonal constants. The kernel has exactly dimension k, not k-1.

3. For a septic in T, the pair of restrictions belongs to every local syzygy space K_l. A different global representation adds c(a_l,v_l), precisely the subspace divided out in E_l. Thus epsilon is intrinsic without choices of gcd representatives. Epsilon vanishes exactly when each restriction pair is a scalar multiple of (a_l,v_l). On a common-contained line this says that both restrictions are zero, which is also exactly the interpolation condition; the scalar remains free. Hence im Phi=ker epsilon in all cases. Nothing implies epsilon is onto E, and the proof correctly makes no such assertion.

4. If a_l and v_l are both nonzero, divide by their homogeneous gcd h_l. Coprimality of the reduced pair forces p=a'_l b and q=v'_l b. Degrees force b to have degree d_l=deg h_l, with no additional sections. The old scalar-pair subspace corresponds to C h_l, giving dimension (d_l+1)-1=d_l. If a_l=0 only, p=0 and q is arbitrary cubic, giving dimension 4-1=3. If v_l=0 only, q=0 and p is arbitrary quartic, giving dimension 5-1=4. If both are zero, there is no relation and no subspace to divide out, giving dimension 5+4=9. These checks also show that repeated common roots must be counted with their full gcd multiplicities.

5. Exactness gives dim R=k+dim ker epsilon, and elementary rank-nullity yields (8). Under avoidance every local gcd has degree zero and there are no common-contained lines, recovering the full septic-intersection isomorphism. Merely setting k=0 does not remove the local mismatch spaces. If r_v=2, (2) identifies P with R, justifying the conditional criterion (11).

6. For the actual descended pair only, the imported direct-sum decomposition lets one add the independently justified lower bounds k,2k,k. Thus the full order-four coefficient has dimension at least 4k. This does not evaluate k for the original pair, prove any actual source class nonzero, or establish lifting or algebraicity.

The saturated degree-seven target is correctly retained throughout. No quintic or sextic dimension is substituted for it. No selected HM/source evaluation, numerical rank calculation, parameter search, generator/checker, or large computation was used in this review.
