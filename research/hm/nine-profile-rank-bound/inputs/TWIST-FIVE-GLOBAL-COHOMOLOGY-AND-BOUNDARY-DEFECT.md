# Actual global twist-five cohomology and the plane-boundary section defect

Let G be the binary icosahedral group, W its negative two-space, A=Sym²W, V the other three-space, P the genuine four-space, D=Sym⁴W, and T6=Sym⁵W. Put B=End_0 F for the actual normalized HM bundle.

## Exact ambient cohomology

The actual exterior-symmetric evaluation resolution at
https://github.com/Akilleez-QA/read-em-and-weep/blob/d5d9bd997145b0ecf7d7bd659a19fb7845afb75f/research/hm/actual-primary-image-extension/PROOF.md
identifies H0(B(5)) with Sym²U, U=H0(F(3))=P. Its quotient on the evaluation-degeneracy lines is O_line(-2), which has no sections; the preceding exterior image has H1=0. Thus this is an actual multiplication identification, not an Euler-characteristic guess. Consequently

    H0(B(5)) = 1 + P + D.

The established higher adjoint vanishings give H2(B(5))=H3(B(5))=H4(B(5))=0. Alternatively, for the last two groups, tensor the actual primary section resolution by F*(5): the only controlling terms are positive-twist H3/H4 of F, which vanish. H2 is the previously proved all-t>=2 vanishing.

Using the actual equivariant monad K-class [B(5)]=[F]^2[O(6)]-[O(5)] then gives

    H1(B(5)) = 1 + A + V + D + W' + 3 T6.

Its even and odd dimensions are 12 and 20, respectively. The accompanying exact character verifier checks the Euler decomposition; the geometric support and H0 identification above are essential to extracting H1.

## A three-channel global-section defect

Write G5=ker[H0(B_R(5)) O_T -> C_lin(2)]. The actual plane boundary is surjective as a bundle map. The exact section-bundle sequence is

    0 -> A O_T(-4) -> E5,+ -> G5 -> 0,

where E5,+ is the even part of pi_*p*B(5) for the universal hyperplane. Uniform twist-five hyperplane higher vanishing implies that Leray identifies H1(E5,+) with H1(B(5))_+. Also H0(E5,+)=H0(B(5)), all even. Taking cohomology therefore yields

    0 -> 1+P+D -> H0(G5)
      -> 1+A+D --alpha--> 1+A+V+D
      -> H1(G5) -> 0.

Every common irreducible in alpha occurs once. Thus there is an unspecified representation R, a direct sum of a subset of {1,A,D}, such that

    H0(G5) = 1+P+D+R,
    H1(G5) = V+R.

These are representation isomorphisms, not canonical splittings. No value of any of the three actual alpha channels is asserted.

Since C_lin is globally generated of rank five and degree26, C_lin(2) has H1=0 and h0=41. The global sections of the surjective plane-boundary bundle map consequently have rank

    rank[H0(B_R(5)) -> H0(C_lin(2))] = 38-dim R,

and cokernel V+R. In particular this global-section map is NEVER surjective, despite the boundary being surjective on every parameter fiber. Its unavoidable cokernel contains the genuine V three-space.

This does not contradict nonzero invariant smoothing or residual nonvanishing: those concern specific moving inputs and fiber maps, not surjectivity on all global sections. The exact global defect must be retained in any attempt to reconstruct the boundary from section dimensions.

## Reproducibility and scope

Run verify_twist_five_global_cohomology.py beside verify_negative_vertex_scalar.py. Only universal representation-ring operations are performed. The actual cohomology support, exterior-symmetric resolution, and relative boundary sequences are retained as explicit proved inputs. No selected HM coefficients, actual matrices, numerical ranks or experiments are evaluated.
