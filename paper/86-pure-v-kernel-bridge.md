# Kernel bundles and the ten singular modifications

**Craig Ward · 23 October 2026 · PR1049**

[Immutable full proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/6210a276622e15c6977b8070bc1fd12744fe2f07/research/hm/source2-pure-v-kernel-bridge/PROOF.md).

## Exact bridge for every nonzero member

Let B be the finite component scheme of a nonzero universal conditional pure-V gate, with length b. Normalize the surjections to their image ideals as

    F:P O→I_B(9),      H:D O→I_B(10),
    L:D O→P O(1),     H=F(1)L.

The [component-ideal transfer](84-pure-v-fourth-ideal-transfer.md) supplies equality of these image ideals everywhere, not just generically. K_F=ker F and K_H=ker H are bundles of ranks three and four: on a regular surface a finite-colength ideal has projective dimension one, so the kernel of its free presentation is locally free. This applies to all five classified schemes, including non-complete-intersection fat points.

The snake lemma gives the exact sequence

    0→O(-4)→K_H→K_F(1)→C_L→0,

where C_L=coker L has length ten, one at each reduced order-three axis. The map K_F(1)→C_L is onto at every axis for every nonzero coefficient direction, including the C₃ jet line. The finite sheaf retains its specified twist; equal lengths do not identify different equivariant twists.

## The intermediate sheaf is not a bundle

Define E=ker(K_F(1)→C_L). Then

    0→O(-4)→K_H→E→0,
    0→E→K_F(1)→C_L→0.

At an axis let R be the regular local ring, m=(u,v). Compatible invertible basis changes put the maps simultaneously in the forms

    L=diag(I3,(u,v)),
    F=(g1,g2,g3,0),       H=(g1,g2,g3,0,0).

Indeed, writing initially F=(g1,g2,g3,f4) and J=(g1,g2,g3), equality J+(f4)=J+m(f4) forces f4∈J by Nakayama. The changes removing f4 can be matched by source-column operations preserving the normal form of L.

With S=ker(R³→I_B) free of rank two, the kernel comparison is

    S⊕R² → S⊕R,       (s,a,b)↦(s,ua+vb).

It follows that E≅R²⊕m at every one of the ten axes. E is torsion-free of rank three but not locally free there; it is a bundle elsewhere. Its double dual is canonically K_F(1), and E**/E=C_L has length ten.

Locally the first sequence is the direct sum of the identity on S and the nontrivial Koszul extension 0→R→R²→m→0, with 1↦(-v,u). It cannot split, since that would make m a projective, hence free, summand. Therefore O(-4)→K_H is an injection of sheaves, **not a subbundle inclusion** at the ten axes. As a section of K_H(4), it has exactly those ten reduced zeros. No coefficient direction removes this local defect.

## Fiber images are not bundle ranks

The common ideal is m off the C₃ jet line and m² on it, requiring respectively two and three generators. Thus the images of K_F and K_H in the fibers of their original free source modules have dimensions respectively (2,3) off that line and (1,2) on it. The bundles themselves retain ranks three and four everywhere.

The map to C_L detects the one redundant F direction on the jet line. Off it, one further redundant direction remains in its kernel. Minimal syzygies have zero source-fiber image and map to zero in C_L. This describes the indicated inclusions, not injectivity of a singular target after specialization or extra specialized A-kernel classes.

## Chern data and scope

With h the plane hyperplane class, the exact classes are

| Sheaf | Rank | c1 | c2 |
|---|---:|---:|---:|
| K_F | 3 | −9h | (81−b)h² |
| K_H | 4 | −10h | (100−b)h² |
| K_F(1) | 3 | −6h | (66−b)h² |
| E | 3 | −6h | (76−b)h² |

The length-ten correction is essential; omitting it lowers the predicted c2(K_H) by ten. Chern classes of the non-locally-free E are its coherent-sheaf K-class Chern classes.

The completed [five-stratum theorem](82-pure-v-complete-nonic-classification.md) supplies b=54,49,46,46,34 at the four special ratios and their complement. It remains a classification of universal nonzero members, not selection of the actual member. The zero gate is outside this finite-scheme kernel theorem. The original-fourth interpretation concerns its surviving D summand through the determinant target, not quadratic-lift degeneracy or additional specialized A-kernel classes. Neither source occurrence nor actual coefficients are determined.

The written regular-local, snake-lemma, Nakayama and Koszul arguments establish the sheaf claims. Symbolic basis-change, twist, Chern and fiber bookkeeping checks support them without substituting numerical ranks for proofs.
