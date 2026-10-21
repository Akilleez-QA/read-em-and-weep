# A forced invariant component of the scalar-to-excess comparison

Work over the complex numbers, with S=Sym(T), T=V*, and the normalizer and finite Heisenberg group Γ of the pinned HM representation conventions. Put I=Ann_S(H), D=Fitt_0(H), and Z=I/D. Write W′ for the two-dimensional generator representation, U and U′ for the two three-dimensional even representations, Qspin for the odd four-dimensional representation, and T_4 for the distinct even four-dimensional representation.

The result concerns the degree-five comparison of free resolutions of I and Z, not the unresolved degree-six connecting map of PR503.

## 1. Free covers and the forced comparison

The pinned minimal covers are

F_0(I)=S(-3)⊗(A⊗W′) ⊕ S(-4)⊗(V⊗U),
F_0(Z)=S(-3)⊗(A⊗W′).

The quotient I→Z is the identity on the cubic generator space. Choose normalizer-equivariant minimal resolutions; this is possible by averaging over the finite normalizer. Its comparison in homological degree zero is uniquely the identity on cubic generators and zero on quartic generators. Indeed the only possible quartic lift would be a normalizer map

V⊗U → T⊗A⊗W′ = V⊗(W′⊕Qspin⊕T_4),

which vanishes by irreducibility and the absence of U. The quartic generators do map to zero in Z, since they lie in D_4.

The first minimal syzygy generators of I have degrees four and five:

F_1(I)=S(-4)⊗(V⊗W′) ⊕ S(-5)⊗B,

where B=Tor_1^S(I,S/m)_5 has dimension52. The pure excess resolution gives

F_1(Z)=S(-4)⊗V⊗(W′⊕Qspin),
F_2(Z)=S(-6)⊗Tor_2^S(Z,S/m)_6.

Consequently F_1(Z)→F_0(Z) has no kernel in degree five. Every chosen equivariant lift of B to degree-five syzygies of I therefore has a unique comparison lift

f_5:B→(F_1(Z))_5 = T⊗V⊗(W′⊕Qspin).

If f_5(b)=0, the associated syzygy of I has zero cubic-generator component: the comparison F_0(I)→F_0(Z) is identity on that component. Thus this syzygy uses only the quartic V⊗U generators. This implication does not assert that f_5 is globally injective.

## 2. The invariant source and target

The exact degree-five presentation strand of I gives in the representation ring

[B]=[S_2⊗A⊗W′]+[T⊗V⊗U]−[I_5]−[T⊗V⊗W′].

There are no degree-five second syzygies of I, by the scalar resolution. Taking Γ-invariants is exact. Using S_2=E⊗U′, E=A*, and the one-dimensional invariant parts of E⊗A and T⊗V, the four invariant terms are respectively

U′⊗W′=W′⊕Qspin,  U,  U,  W′.

Here I_5^Γ=U is the pinned invariant-quintic identification. Hence

B^Γ≅Qspin.

Similarly

((F_1(Z))_5)^Γ≅W′⊕Qspin.

This identifies the possible invariant comparison channel; it does not yet establish nonvanishing.

## 3. Euler multiplication excludes its kernel

The pinned quartic space V⊗U is the span of the first derivatives of I_5^Γ=U. Therefore multiplication induces an isomorphism

(T⊗V⊗U)^Γ≅U → I_5^Γ=U.

For clarity, surjectivity is not being inferred from equal dimensions: for each homogeneous quintic f in U, Euler's identity gives

sum_i t_i (∂f/∂t_i)=5f,

and every derivative belongs to V⊗U. Thus invariant multiplication is onto and, since both spaces have dimension three, injective.

Now let b∈B^Γ with f_5(b)=0. Choose the degree-five syzygy representative equivariantly; it is Γ-invariant. Section 1 makes it a quartic-only invariant syzygy, hence an element of the kernel of the preceding injective multiplication map. It is zero, so b=0. Consequently f_5 is injective on B^Γ. Normalizer equivariance and the inequivalence of W′ and Qspin then give

f_5|_(B^Γ):Qspin → Qspin

as an isomorphism onto the unique Qspin summand of the invariant target.

The conclusion is independent of the equivariant choice of minimal degree-five representatives: their possible differences lie in (T⊗V⊗W′)^Γ=W′, which admits no normalizer map from Qspin.

## 4. Contribution and boundary

This proves a nonzero comparison-map component that dimensions and the Betti tables alone did not determine. It supplies a fixed four-dimensional invariant contribution to the degree-five scalar-to-excess lift. The component has linear polynomial entries between free modules; it is not a nonzero induced degree-five Tor map, since those entries vanish after tensoring with S/m.

It does not prove that the connecting map Tor_3(S/I)_6→Tor_2(Z)_6 is nonzero on either of its undecided source summands T⊗W′ and T⊗Qspin. Contributions from the remaining forty-eight dimensions of B and their degree-six compositions still require control. In particular k remains in {15,25,35,45}; no value is selected here. No original fixed-pair/source evaluation, higher-order lifting, or algebraicity assertion is made.

## Exact dependencies and status

- PR489, scalar generators, invariant quintics and their derivatives: https://github.com/Akilleez-QA/read-em-and-weep/blob/5637cdd610fc2ec8ffbbbbfc7627b2d6c54f6873/research/hm/scalar-quartic-generators/PROOF.md
- PR498, the excess factor and its multiplication: https://github.com/Akilleez-QA/read-em-and-weep/blob/77018c2e6904a4ef9adfee5f2f48e49894b63fe9/research/hm/determinantal-excess-module/PROOF.md
- PR500, the exact scalar resolution: https://github.com/Akilleez-QA/read-em-and-weep/blob/86d7e1b5d3aee770ea3e7652c950b29bca1aba10/research/hm/scalar-last-ghost-exclusion/PROOF.md
- PR502, purity of C and therefore the shifted excess resolution: https://github.com/Akilleez-QA/read-em-and-weep/blob/f8c9b1fb8b03a5721e4eca97cac4137f7ba955d0/research/hm/excess-contraction-invertibility/PROOF.md
- PR503, the unresolved degree-six connecting map and exhaustive k-family: https://github.com/Akilleez-QA/read-em-and-weep/blob/c56c902d227f6205cf132897dd66cf2070f05b4a/research/hm/determinantal-resolution-constraints/PROOF.md

Authored structural derivation with independent and root mathematical reviews, conditional on these pinned inputs; not formally checked. No selected HM/source-instance evaluation, numerical matrix or rank calculation, coefficient search, checker, generator, or large computation was used.
