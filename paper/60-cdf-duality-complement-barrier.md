# Why duality alone does not supply complementary preservation

**Craig Ward · 23 October 2026 · Update through PR1008**

[PR1008](https://github.com/Akilleez-QA/read-em-and-weep/blob/18a22f8d8fecf4c321a247c44fe1f0f411115957/research/hm/cdf-duality-complement-barrier/PROOF.md) rules out a proposed inference, not a source: trace/Serre duality, the necessary endpoint characters, one-sided B preservation and a scalar compatible algebra do not by themselves force preservation of the complementary c-d-f block. A further actual-geometric identification would be needed. Neither one-sided preservation nor its failure is established, and the four-pair/three-label frontier is unchanged.

## 1. The actual transpose occupies another cohomological window

Write B_ad=End₀(F_HM), to distinguish the adjoint bundle from the c-d-f B block. The trace pairing is nondegenerate and gives B_ad≅B_ad*. Serre duality on P⁴ pairs H¹(B_ad(d)) with H³(B_ad(-d-5)). Consequently the transpose of the original quadratic map is

    Q∨: H³(B_ad(-9))₊ → H³(B_ad(-7))₊,

of dimensions 37→41, not another map in the original 41→37 window. The direct trace cup of its original endpoints lands in H²(O(6))=0. Self-duality of irreducible representations does not identify unequal endpoint spaces or mark repeated multiplicity spaces.

The actual P¹ negative-pencil presentations likewise exchange different bundles under duality: their ranks are 17 and 13, while the B-block bundle ranks are seven and four. Under one-sided preservation, the marked B source after removing the kernel has dimension16 and the marked B target dimension21. These particular marks cannot be aligned by a perfect cross-pairing. This does not deny other duality statements involving the surrounding spaces.

## 2. The correct implication uses annihilators

For any linear map, Q(U)⊂Z is equivalent to Q∨(Z⊥)⊂U⊥. Thus the one-sided condition gives

    Q∨((Y_F⊕Y_L)*) ⊂ X_F*.

Complementary preservation would instead require Q∨(Y_B*)⊂X_B*. The two inclusions concern different domain subspaces. Taking a transpose does not turn the first into the second, and no orthogonal splitting is supplied by the actual dual presentations.

## 3. A bounded counterfamily excludes the linear shortcut

Over the Laurent ring C[t,t⁻¹,u,u⁻¹], the proof constructs a character-faithful equivariant family with kernel A+D, cokernel P, one-sided B preservation, restricted image V+2P+D, and restricted cokernel D. Its complementary off-diagonal D block is t times the identity and is nonzero. Nevertheless its compatible algebra inside the full represented negative-pencil endpoint algebra is exactly the scalars: the V and D equations equate the three vertex scalars, and the P equation kills the radical arrow.

Perfect evaluation pairings with formal dual groups and the transpose action realize the same graded adjunction and twist bookkeeping. All these specified linear data therefore coexist with failure of complementary preservation.

This is **not an actual HM realization or a full multiplication model**. In particular the family does not enforce the fixed negative quadratic tensors, the original Bocksteins or every bundle relation. It shows insufficiency of the stated duality/character/commutant data, not failure of every possible argument using additional actual geometry.

## 4. Consequence for the current route

The [conditional c-d-f cubic reduction](59-cdf-preserved-b-cubic.md) retains exactly its one-sided hypothesis and raw three-dimensional gate. A shortcut through automatic complementary preservation is unavailable from these inputs. Establishing or excluding actual one-sided preservation, or finding a genuinely additional geometric relation, remains necessary.

The full proof has independent review and 46 checks in normal and optimized Python, covering exact input authentication, dual degrees, the formal kernel/cokernel identities and commutant equations. No actual coefficients or instance ranks are evaluated. These are supporting exact checks, not a complete proof-assistant verification or a source exclusion.
