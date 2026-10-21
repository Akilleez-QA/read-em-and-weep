# Relative cubic syzygies and the twelve-point base-change defect

Use the notation and theorem of PROOF.md, in particular the nonzero residual morphism s:O(−12)→O with reduced zero divisor Ω.

The kernel sheaf of φ is

ker φ = T4⊗O(−3) ⊕ O(−4).

To see this, a local section (q,w,t) in the kernel has Aq=0, so q is a section of ker A=O(−12). Reducing Bq+Cw=0 modulo im C gives sq=0. Since s is a nonzero morphism between line bundles on the integral curve P¹, it is injective as a sheaf, so q=0. Now w belongs to ker C=O(−4), while the T4 component is arbitrary. This is a kernel-sheaf assertion, not a claim of constant fiber rank for φ.

Let K be the actual kernel sheaf of cubic linear multiplication

T⊗J_3→J_4.

The constant map T⊗I_3→T I_3 has kernel of dimension ten, namely the cubic linear syzygies of I established in PR489. Quotienting source and target by these constant pieces gives the exact sequence

0→10O→K→V⊗ker φ→0.

Surjectivity on the right is a sheaf assertion: a local lift of a kernel section has product in T I_3, which can be canceled by a local section of T⊗I_3 since the latter maps onto T I_3. Thus the sequence is exact. Since Ext¹(O(−3),O)=H¹(O(3))=0 and Ext¹(O(−4),O)=H¹(O(4))=0, it splits as an ordinary bundle sequence. Hence

K ≅ 10O ⊕ 20O(−3) ⊕ 5O(−4).

In particular K has rank35 and degree−80. It is a subbundle of the source in the sense that the image sheaf is locally free, but it does not commute with taking the full multiplication kernel at the twelve exceptional fibers.

More precisely, the cokernel of T⊗J_3→J_4 is the original quartic-generator torsion sheaf, of length60, with local model five copies of O/(t) at each point of Ω. Tensoring the exact presentation with the residue field gives an exact sequence

0→K⊗k(p)→ker[T⊗J_3,p→J_4,p]→Tor₁(coker,k(p))→0.

The last vector space vanishes off Ω and has dimension five on Ω. Therefore the actual cubic linear-syzygy counts are35 off Ω and40 on Ω, agreeing with β₂,₄(G_w)=35+a(w). This identifies both the full relative kernel bundle and the exact reason its fibers miss five exceptional syzygies.

These deductions are structural consequences of PROOF.md and the pinned PR489 cubic-syzygy input. They involve no selected-instance evaluation and do not determine the middle Betti parameter b.
