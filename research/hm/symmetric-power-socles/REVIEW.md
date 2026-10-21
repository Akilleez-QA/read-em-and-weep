# Independent review: exact socles of higher symmetric powers

Reviewed proof SHA256: 45323e1af06e12e9b07aa0cd77484b5f4b4c788f43e05befaed996b74f93b9cd.

Verdict: the claims follow from the pinned PR494 multiplication model and support statements. No gap was found in the common-radical argument or in the representation-theoretic exclusions. This is a mathematical review conditional on those inputs, not a formal proof-assistant check.

## 1. Universal evaluation really detects degree-one socle

Write z=sum_i v_i tensor f_i in T tensor Sym^p(W). The degree-two model says that t z maps to sum_i beta(t v_i) f_i in E tensor Sym^(p+2)(W), where beta:Sym²(T)→E tensor Sym²(W) is the fixed equivariant identification. Therefore evaluation at any nonzero covector lambda gives sum_i (id_E tensor ev_lambda)(beta(t v_i)) f_i(lambda), exactly B_lambda(t, v_lambda). The evaluation degrees are two plus p; there is no omitted derivative or polarization factor.

The map ev_lambda:Sym²(W)→C is nonzero for every nonzero lambda. Its tensor product with E is onto E, and beta is an isomorphism. Thus B_lambda is nonzero because the products t v span Sym²(T). The subgroup Gamma fixes W, so evaluation preserves Gamma-equivariance. The common radical of B_lambda in the second T factor is Gamma-invariant. Since T is Gamma-irreducible, the radical is zero or T; nonzeroness excludes T. This uses a common radical, not a claim that every individual scalar multiplication is injective.

If all t kill z, every v_lambda is zero. In characteristic zero, a homogeneous binary polynomial vanishing on every nonzero covector is zero; applying this to each coefficient in any basis of T proves z=0. This is an abstract polynomial identity valid for the entire family. It neither selects an HM instance nor evaluates its coefficients. Degree zero is also socle-free, since multiplication identifies T tensor M_0 with M_1.

## 2. Independent character checks

The Horrocks–Mumford Appendix supplies the two-dimensional character W′ and the irreducible characters J_5, R_6, U, T_4. Since det(W′)=1, its symmetric-power characters obey f_0=1, f_1=t and f_(n+1)=t f_n−f_(n−1). Consequently

f_4=t^4−3t²+1,
f_5=t^5−4t³+3t,
f_6=t^6−5t^4+6t²−1.

At the identity and central involution these give dimensions/parities (5,5), (6,−6), and (7,7). On the other classes the W′ traces are 0, −1, 1 and the two roots eta, eta′ of t²+t−1, together with their negatives. Substitution in the three displayed polynomials reproduces the Appendix rows J_5, R_6 and U+T_4 respectively. In particular f_6(eta′)=eta′=−eta−1, agreeing with the U character −eta plus the T_4 character −1. This checks the unprimed U in Sym⁶(W′), not U′. The four-dimensional T_4 is the even representation, not the odd spin representation.

The identity V tensor A = E tensor (U+W′) is the dual of the pinned T tensor A* = A tensor (U+W′). The quotient representations U and W′ are self-dual; this also follows from their real-valued characters in the Appendix. For each nontrivial Heisenberg factor, irreducibility and distinctness after tensoring with the quotient labels follow from HM (2.2): the Gamma multiplicity-space functor is an equivalence on this isotypic component. Thus one cannot identify E tensor T_4 with a target summand merely from a similar dimension.

## 3. Exact degree-two kernels

For p=3, M_2=E tensor R_6 is irreducible. The map delta:M_2→Hom(T,M_3) is nonzero because degree-zero generation and M_3≠0 imply T M_2=M_3. Its kernel is invariant and hence zero.

For p=4, the source is E tensor (U+T_4) and the target is E tensor (U+W′). Semisimplicity and inequivalent irreducibles force the entire T_4 summand into the kernel. The U restriction must be nonzero, since otherwise the total map vanishes, contradicting T M_2=M_3≠0. The U restriction is injective by irreducibility. The kernel is therefore exactly E tensor T_4, of dimension twenty. Nonzero action is proved from generation here; it is not inferred merely from a shared representation label.

All final-degree components are automatically in the socle. Together with the degree-zero and degree-one exclusions and PR494 support cutoffs, this proves the entire claimed socles: dimension ten in degree three for M_3; dimensions twenty in degree two and five in degree three for M_4; dimension 5(p+3) in degree two for p≥5.

## 4. Grading and terminal Betti modules

The last Koszul term in internal degree j is Lambda^5(T) tensor M_(j−5), whose differential vanishes precisely on the socle. Hence a socle element of polynomial degree d contributes a minimal fifth syzygy in internal degree d+5. This gives 10S(−8), 20S(−7)+5S(−8), and 5(p+3)S(−7), respectively. The determinant character is trivial for the HM normalizer in SL(V); even without that equivariant simplification the displayed nonequivariant ranks and shifts remain correct. Reversing the graded dual at the respective top degree gives the claimed generator degrees and multiplicities.

## 5. Penultimate upper corners

The added section 5 is also verified. For a nonzero finite-length module, regularity equals the greatest supported degree d. At internal degree d+4, all homological terms with i≤3 vanish by the regularity bound j−i≤d. Hence the Hilbert-numerator coefficient is exactly beta_(4,d+4)−beta_(5,d+4). For p≥5, the degree-six coefficient is −5(p+1)+25(p+3)=20p+70, with beta_(5,6)=0. For p=3, the degree-seven coefficient is −30+50=20, with beta_(5,7)=0. For p=4, the degree-seven coefficient is −35+25=−10, with beta_(5,7)=20, giving beta_(4,7)=10. No uncomputed lower syzygy can contaminate these coefficients. These establish only the claimed upper-corner entries, not the full resolution.

## Sources and boundaries

- PR494, commit 72ab9a7524aef8c9d1c1fd989f8b0e83826dc916: https://github.com/Akilleez-QA/read-em-and-weep/blob/72ab9a7524aef8c9d1c1fd989f8b0e83826dc916/research/hm/higher-symmetric-powers/PROOF.md
- PR478, commit 142b0b52f4ad0ddea526ae044774e4f1dd599aef: https://github.com/Akilleez-QA/read-em-and-weep/blob/142b0b52f4ad0ddea526ae044774e4f1dd599aef/research/hm/cubic-ghost-exclusion/PROOF.md
- Horrocks–Mumford, (2.2), Lemma 3.3 and Appendix: https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf

No selected actual HM/source-instance evaluation, numerical matrices or rank computations, coefficient searches, or large computations were used. These module-symmetric-power statements do not settle the original fixed-pair/source values, higher-order deformation lifting, or algebraicity.
