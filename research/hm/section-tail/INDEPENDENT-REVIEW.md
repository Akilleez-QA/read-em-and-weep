# Independent review of the exact adjoint section-tail proof

## Reviewed artifact and verdict

Reviewed PROOF.md, SHA256 9bbfd053d4ef81ab0659e76593a5f793875c1cad9fc091bad9a4a46fda8af886, in full.

The proof is correct conditional on its explicitly pinned cohomology, primary section-resolution, and evaluation-degeneracy inputs. The new conclusions follow without selected HM/source-instance evaluation. This is independent mathematical review, not formal proof-assistant checking.

## Checks

1. The compact symmetric multiplication complex is exact. In the transverse regular-sequence local form, the kernel at V tensor E consists of the displayed mixed relations and Koszul syzygies. The kernel at Lambda^2 V is the single final Koszul relation. Complementary minors transform globally as det(V) tensor det(E)^(-1), exactly the stated D tensor O(-5). Its cokernel is canonically i_*L^2, not the thicker symmetric-evaluation cokernel from a different complex.

2. For t=1,2 all asserted intermediate cohomology of A_t vanishes by the two-term line-bundle resolution. Both H^0(O(t-5)) and H^1(O(t-5)) vanish, giving the stated H^0(A_t). The isomorphism H^1(J_t)=V tensor H^1(E(t)) uses H^1(A_t)=H^2(A_t)=0 and is valid.

3. In degree seven, the skew denominator lies entirely inside V tensor (T V). Because the primary degree-one multiplication T tensor V embeds, the quotient of that subspace is exactly T tensor Sym^2 V and injects into G_7. Taking the quotient yields V tensor (H^0(E(1))/(T V)), dimension60, canonically. The assertion is about the actual multiplication map, not only dimensions.

4. In degree eight, H^1(E(2))=0 makes the defect-section map surjective. Surjectivity of T H^0(E(1)) onto H^0(E(2)), together with the natural commutative multiplication maps, identifies the kernel exactly as T G_7. Each of the25 disjoint lines contributes one section to L^2(2), so the quotient has dimension25. No equivariant character identification is assumed.

5. The full-section condition justifies vanishing of H_m^0 and H_m^1. H_m^2 is nonzero in degree6 and vanishes above6, so depth2 is exact. Auslander–Buchsbaum gives projective dimension3. The four end bounds6,1,-1,-9 imply regularity8, with equality attained by H_m^2. The weaker bound -1 for H_m^4 used in this proof suffices and is consistent with its stated H^3 input. Minimality gives the lower syzygy shift bounds, while regularity gives the upper bounds; hence no additional generator degrees occur.

6. For n>=7 the smallest sheaf twist in the coordinate Koszul complex is n-6>=1. All q>=2 rows vanish already on E_1. Thus the only possible higher differential is the stated d_2 between K and G rows. Zero abutment forces each paired differential to be an isomorphism and the unpaired edge terms to vanish. The homological shift by two is correct. In particular the transferred second-syzygy counts are exactly60 and25.

7. The sharpening is valid. Injectivity of T tensor G_6 into G_7 means the minimal free cover has no degree-seven kernel: its sixty degree-seven minimal generators are independent modulo T G_6, and the remaining fifty products are independent. There is also no lower-degree kernel. Hence the first syzygies begin in degree eight, and minimality propagates the lower bounds nine and ten to the next two homological degrees. The upper bounds remain nine, ten, eleven by regularity. Transferring these gives i+5<=n<=i+6 for i=3,4,5.

8. The exact first-syzygy count also passes: the primary resolution gives h^0(E(2))=4(15)+15(5)-35=100, with no subsequent free term in that degree. The compact symmetric complex then gives dim G_8=4(100)-6(15)+25=335. The minimal free cover has degree-eight dimension10(15)+60(5)+25=475. Its kernel has dimension140, and every element is a minimal first syzygy because the kernel vanishes in smaller degrees. Therefore dim Tor_1(G,C)_8=140 and the spectral comparison gives dim Tor_3(K,C)_8=140. These are structural consequences of exact sequences, not evaluations of selected multiplication ranks.

The proof keeps the lower-degree ambiguities, fixed-pair Tor correction, selected-source membership, higher-order lifting, and algebraicity unresolved. No numerical rank computation, selected coefficient search, or formal verification is claimed.
