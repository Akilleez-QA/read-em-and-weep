# Unpolarized automorphisms of the cubic image

## Dependencies and scope

Work over C. Let Z be the thirty reduced Heisenberg centers in P4, let pi:M=Bl_Z(P4) -> P4, and write H=pi*O(1) and E=sum_z E_z. The complete cubic system D=3H-E induces the finite birational normalization nu:M -> V51 subset P9. We use:

- PR611, commit 12b28d33627cc0e8b283d142dc16439a51bb5e00, for the normalization and conductor description.
- PR623, commit be95ac2c06a947ded324b8865a18abca577597da, research/hm/cubic-automorphisms/PROOF.md, for Stab_PGL5(Z)=Gamma, |Gamma|=3000, its faithful induced cubic action on V51, and the torsion-free presentation Pic(M)=ZH direct-sum (direct-sum_z ZE_z).

Here Aut means complex algebraic automorphisms, without initially preserving any chosen line bundle. No selected source-instance coefficients, points, derivatives or matrices are evaluated.

## 1. Intrinsic recognition of exceptional divisors

Lemma. On the blowup of P4 at any finite reduced set of points, every smooth prime divisor F isomorphic to P3 is either an exceptional divisor, with normal bundle O_P3(-1), or the strict transform of a hyperplane avoiding all centers, with normal bundle O_P3(1).

Proof. Since H is globally generated, H|F=O_P3(a) for an integer a>=0. If a=0, the five pulled-back homogeneous coordinate sections restrict to constants on F. Consequently pi|F is constant. A fiber away from the centers is a point, whereas the fiber over a center z is precisely E_z. Dimension and irreducibility imply F=E_z.

Suppose a>0. Any positive-dimensional fiber of pi|F contains a projective curve C. On that curve the pullback H has degree zero, contradicting the ampleness of O_P3(a). Hence pi|F is proper and quasi-finite, and therefore finite onto its image.

For any center z, F is distinct from E_z. If F meets E_z, the restriction of the defining section of E_z to the smooth integral threefold F is a nonzero section with a nonempty zero set. That zero set is an effective Cartier divisor on F, of pure dimension two. It is contained in a fiber of pi|F, contradicting finiteness. Thus F is disjoint from every exceptional divisor.

The blowdown is an isomorphism M minus E -> P4 minus Z. Its restriction identifies F with its image Y. Properness makes Y closed also in P4. Thus Y is a smooth hypersurface in P4, disjoint from Z. Let d be its degree. Intersection with three hyperplanes gives d=(H|F)^3=a^3. Adjunction on the smooth degree-d hypersurface gives

    -4 = a(d-5) = a(a^3-5).

For a>=2 the right-hand side is positive; for a=1 it is -4. Thus a=d=1 and Y is a hyperplane. Its normal bundle is O_P3(1). Conversely a hyperplane avoiding Z has that strict transform and normal bundle. The exceptional normal bundle is O_P3(-1), by the blowup construction. This proves the lemma.

In particular the exceptional divisors are characterized without a polarization: they are exactly the embedded P3 prime divisors with normal bundle O_P3(-1).

## 2. Every automorphism of the normalization descends to P4

Any f in Aut(M) permutes the intrinsically characterized exceptional divisors, hence f*E=E. It also preserves the canonical class. The blowup formula is

    K_M=-5H+3E.

It follows that 5(f*H-H)=0. The above torsion-free Picard presentation implies f*H=H. The complete linear system |H| is exactly the blowdown to P4: pi_*O_M=O_P4 implies H0(M,H)=H0(P4,O(1)). Consequently f induces a projective linear automorphism a of P4 satisfying pi f=a pi. Its permutation of exceptional fibers implies a(Z)=Z.

Conversely every projective automorphism preserving Z lifts uniquely to its blowup. The two constructions are inverse, because equality away from the exceptional divisors extends on the integral separated variety M. Therefore

    Aut(M)=Stab_PGL5(Z)=Gamma,

as groups of complex automorphisms. In particular |Aut(M)|=3000.

## 3. Every automorphism of V51 is automatically polarized

Functoriality of normalization lifts any f in Aut(V51) uniquely to an automorphism f_tilde of M with nu f_tilde=f nu. This lifting map is injective: an automorphism acting trivially after normalization acts trivially on the dense normal open subset and hence everywhere.

By Section 2, f_tilde is the blowup lift of some a in Gamma. The action of a on the complete cubics through Z induces the polarized automorphism f_a of V51 established in PR623. Its normalization lift is precisely f_tilde, so injectivity gives f=f_a. Conversely every element of Gamma acts in this way.

Thus normalization lifting is an isomorphism

    Aut(V51) -> Aut(M),

and both groups are Gamma, of order 3000. Every abstract automorphism of V51 preserves O_V51(1) and is induced by a projective transformation of P9. In particular forgetting the polarization introduces no new automorphisms.

This last assertion is not deduced by asserting injectivity of Pic(V51)->Pic(M). Such injectivity need not hold for a nonnormal variety with conductor. It follows instead by equality with the known cubic-induced polarized automorphism.

## Contribution and boundaries

PR623 classified polarized automorphisms. The intrinsic exceptional-divisor lemma removes that hypothesis and proves that every automorphism of the normalization descends to the cubic image. The auxiliary classification of all P3 divisors is valid for any finite reduced point blowup of P4, independently of Heisenberg geometry.

These are statements about complex automorphism groups. They do not claim absolute rigidity: the 576-dimensional abstract deformation tangent of PR614 remains unchanged. They make no assertion about the automorphism group of T75 or the original full adjoint system, and use no new selected-instance evaluation or large computation.
