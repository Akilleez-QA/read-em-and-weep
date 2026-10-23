# Weighted incidence and canonical source directions: source report

**Craig Ward · 23 October 2026 · Full-source report of mr. slop's PR1067**

[Immutable full proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/0201d67280fbfe0f87c84e7e726c3dc6c12bbecb/research/hm/weighted-incidence-line/PROOF.md).

This is a full-source reading, not an independent reproof. Retain the actual weighted 32-to-34 presentation and its canonical two-dimensional multiplicity space K from [PR1062](95-doubled-mixed-block-source-report.md).

## A nonzero weighted map and its multiplicity kernel

For every one of the seven necessary opposite-cokernel types, both Hom_G(V O(2),C) and Hom_G(W′ O(5),C) have dimension one. The universal sextic sequence 0→O(-4)→V O(2)→W′ O(5)→0 identifies these Hom spaces by precomposition. Consequently every weighted map to C kills the indicated O(-4).

The actual map η:K⊗V O(2)→C is nonzero. If it vanished, its source preimage would be an extension of two V O(2) copies by A O(-6). The equivariant Ext space for one copy has dimension one, so some multiplicity direction would split and inject V O(2) into a source twisted by O(-1), which is impossible. Thus η selects a canonical multiplicity-kernel line K0⊂K.

This line is **not the entire sheaf kernel of η**: a nonzero generator V O(2)→C can itself have a kernel. No injectivity of that generator is assumed, and no C type or position of K0 relative to the earlier marked line is selected.

## Saturated preimages and cubic directions

The preimage L of K0⊗V O(2) is a saturated rank-six source subbundle in a nonzero equivariant extension by A O(-6). Its exact equivariant splitting is

    L=W′ O(-1)⊕V O(-2)⊕O(-4).

The proof forces these summands using degree bounds, Euler-character multiplicities and exhaustion of rank, allowing cohomology cancellation until those bounds resolve it. Cross-Hom vanishings make the equivariant splitting intrinsic, although named scalar identifications remain choices. It selects actual W′ and T6 multiplicity lines in the quotient source.

The entire K⊗O(-4) is killed by η. Its preimage extension by A O(-6) has both equivariant Hom and Ext ambiguities zero, so it has a unique equivariant splitting. This selects an actual saturated lift K⊗O(-4) into the source and hence two of its three S multiplicity directions. The K0 restriction is precisely the O(-4) summand of L. No complementary S direction or additional marked line is chosen.

These are actual incidence restrictions, not identifications with other repeated S, P or D subspaces, including im h-generated modules. They choose no source pair, opposite type, scalar value or terminal branch. The written Hom/Ext and embedding arguments are source proofs; bounded character checks do not evaluate actual coefficients.
