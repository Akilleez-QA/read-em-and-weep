# Independent mathematical review

Reviewed proof: `PROOF.md`, SHA256
`c39ee4b52bd2864b4f833cd666f3c4fc27c17ee1db79ac211149227d6335ac0a`.

Verdict: PASS for the stated results and limits. This is a mathematical text review, not formal proof verification.

## Checks

1. **Paired endpoint.** Tensoring the K4, K3, and K2 resolutions by B(-3), B(-4), and B(-5) gives dual syzygy targets (H¹B5,H¹B6), H¹B6, and H¹B5. The generator H² groups vanish in the stated range. PR450 removes only degree six; the surviving two incoming maps retain exactly vH¹B2+uH¹B3. Thus the whole order-five dual is two copies of Q5.

2. **Primary presentation.** At twist five, H²L5=0 and H²K5=0 give the asserted cokernel. Both the linear 35M1→15M2 block and the quadratic 35M1→4M3 block are necessary. The quotient defining P5 uses the proved surjection p3, but only the actual image of p2. Its primary target is therefore exactly the one in (4), not a replacement of all inputs by M/(u,v)M.

3. **Degree-two defect.** At twist two the exact sequences identify H²L2 with 2M1*, and H³L2=0. Their dimensions are consistent with H¹K2=ker(a2) and H²K2=coker(a2), for a2 between dimensions 20 and 70. The 15 scalar sections of O(2) inject into H¹K2 because H⁰E0(2)=0. Hence rank(a2)≤5 and 65≤dim C2≤70. No assumption about H⁰B2 or an evaluated rank is needed.

4. **Cubic contribution.** Changing a lift of c in C2 changes vb by v im(p2), zero in P5. The map delta_v is therefore well-defined. Its image is exactly the omitted cubic image, yielding C2→P5→Q5→0 and the dimension inequalities stated. Neither a nonzero domain nor a nonzero P5 establishes a nonzero Q5.

5. **Raw nonvanishing.** The Chern-character calculation gives χB5=-22. The section-resolution cohomology diagonals establish H³B5=H⁴B5=0; PR167 provides H²B5=0. Horrocks–Mumford printed pp.73–74 were checked: Lemma4.10 and its proof exclude wedge-zero independent pairs of global sections when H⁰(E(-1))=0, and the primary cohomology table gives four sections of E=F(3). The rank-normal-form argument over C(P4)[X,Y] then excludes every nonzero quadratic relation among these four sections. Thus h⁰B5≥10 and h¹B5≥32. This does not assert equality or survival after multiplication by u and v.

## Scope

The proof resolves a genuine missing dependency in the degree-five reduction and excludes a zero ambient target at that degree. It does not evaluate D5', delta_v, the fixed quotient Q5, or any selected source. It does not establish order-six optimality, an actual-source primitive, pure diagonal conditions, a module lift, or algebraicity. No selected HM map, matrix, rank computation, or computational tensor-cohomology table is used in these checks.
