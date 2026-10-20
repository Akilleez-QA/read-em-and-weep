# Independent mathematical review

Reviewed PROOF.md SHA256: `20f03ead5490e3fae66744bd84fdd4052a78d76a48a0ffe0a401790db0979193`.

Verdict: accepted, conditional on the explicitly pinned HM inputs. No mathematical correction is required. This is independent mathematical review, not formal verification or recertification of every antecedent proof.

## Checks

1. Riemann–Roch gives exactly the displayed polynomial from ch(B)=3−15h²+(75/4)h⁴. Its values at twists three and four are −100 and −85. The cited h¹ dimensions, together with the established H², H³ and H⁴ vanishings, therefore prove H⁰(B(3))=H⁰(B(4))=0. Positive-twist section vanishing is not inferred from stability.

2. For the sheaf Koszul complex tensored by B(t), the q=1 terms are ΛⁱT tensor K_(t+1−i), and the q=2 terms are ΛⁱT tensor H_(t+5−i). Their internal degrees are consequently t+1 and t+5. The differential has the stated bidegree (a,1−a).

3. Complementary exterior degrees sum to five, while the perfect compatible H pairing has complementary module degrees summing to five. Thus complementary Tor internal degrees sum to ten. Generation and the actual isomorphism T tensor H_0 → H_1 annihilate every internal-degree-one H Tor group, hence every internal-degree-nine group. Internal degree zero has only Tor_0(H)_0=H_0, so internal degree ten has only Tor_5(H)_10=H_0* tensor det T. Its identification with W′ follows from the stated normalizer determinant trivialization and the perfect pairing.

4. For B(4), the q=0 row vanishes in all twists −1 through four. PR476 covers the q=3 row throughout that range, and Serre duality reduces the q=4 row to strictly negative-twist section groups. The q=2 row is zero on E_2 by the preceding duality check. Every remaining q=1 term therefore has no higher incoming or outgoing differential and survives to the zero abutment. This proves Tor_i(K)_5=0 for every i.

5. For B(5), the only q=0 term is H⁰(B(5)) at (0,0), and the only q=2 term on E_2 is H_0* tensor det T at (−5,2). The latter has no incoming differential; its d_3 target (−2,0) is zero. Its d_2 target (−3,1) has no other incoming differential and has zero outgoing d_2 target (−1,0). Thus their d_2 is an isomorphism. The position (−2,1) has zero incoming d_2 source (−4,2), zero higher incoming sources, and no outgoing map after d_2. Its target (0,0) has zero alternate d_3 source (−3,2) and zero higher sources. This second d_2 is also an isomorphism. Every other q=1 term is isolated and must vanish. Both identifications arise from actual hypercohomology differentials.

6. The seven exact pinned dependencies support the claimed inputs. The six cited PROOF.md texts agree with their pinned published versions; PR167 explicitly proves H²(B(t))=0 for t≥2. PR456 identifies B(5)=Sym²(F(3)) and proves the natural section isomorphism Sym²H⁰(F(3)) → H⁰(B(5)), giving dimension ten.

## Boundary

The conclusions do not use either unresolved cubic or middle parameter. They do not determine the original fixed-pair quotients, remove PR477’s Tor correction, establish selected-source membership, or imply higher-order lifting or algebraicity. No selected HM/source-instance evaluation, numerical multiplication matrix or rank, coefficient search, generator/checker, or large computation was performed.
