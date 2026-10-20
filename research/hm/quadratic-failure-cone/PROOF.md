# The quadratic failure cone from Horrocks–Mumford symmetry

## Statement and scope

Work over C. Let F be the normalized Horrocks–Mumford bundle on P^4, let S=H^0_*(O), and let M=H^1_*(F). For a quadratic q write T_q:M_1 -> M_3 for multiplication. The dimensions of these spaces are ten and two. Throughout, rank means the rank of this multiplication map, not the rank of q as a quadratic form.

There exist representation-theoretic identifications with a five-dimensional vector space A and a two-dimensional vector space W such that

    S_2 = A^vee tensor sl(W),
    M_1 = A tensor W,       M_3 = W,

and quadratic multiplication is contraction followed by the indicated trace-zero endomorphism, up to one nonzero scalar. The identifications are not binary-quartic coefficient coordinates, and no such coordinate identification is asserted here.

Consequently:

1. T_q is nonzero for every nonzero q. In particular its rank is one or two, never zero.
2. The nonzero quadratics with rank T_q=1 correspond exactly to tensors a tensor n, with a nonzero in A^vee and n a nonzero rank-one nilpotent in sl(W). Their reduced projective locus is P^4 times P^1 in P(S_2)=P^14, with embedding line bundle O(1,2). Its dimension is five and codimension nine. We make no assertion here about possible embedded scheme structure of the maximal-minor ideal at the affine vertex.
3. For every nonzero lambda in M_3^vee, the map C_lambda:S_2 -> M_1^vee, q |-> lambda composed with T_q, has rank exactly ten.
4. For the original nonzero quadratic u_0 and arbitrary cubic v_0, the primary quotient M_3/(u_0 M_1+v_0 M_0) has dimension at most one. PR440 therefore gives the unconditional fixed-endpoint bound dim Q_0 <=15. The whole paired order-six coefficient cohomology, whose dual is Q_0 direct sum Q_0, has dimension at most thirty.

This excludes the rank-zero branch left open in PR448, and replaces its codimension-at-least-two estimate by the exact reduced failure cone for HM. It does not determine whether u_0 belongs to that cone. In particular it does not prove Q_0=0 or Q_0 nonzero, evaluate a selected multiplication map, or identify an actual source class.

## 1. Exact primary inputs and normalization

The primary reference is G. Horrocks and D. Mumford, *A rank 2 vector bundle on P^4 with 15,000 symmetries*, Topology 12 (1973), 63–81:

https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf

Use E for the bundle denoted by F in that paper. It has c_1(E)=5, while our F=E(-3) has c_1(F)=-1. Therefore

    M_j=H^1(E(j-3)).                                  (1)

Let V be the paper's five-dimensional representation, H its Heisenberg subgroup and N its normalizer. The paper's V_i are the Galois conjugates of V=V_0; in particular V_1^vee=V_3. Write W' for its two-dimensional N/H representation of character chi_2', and U' for the three-dimensional representation of character chi_3'. In the remainder of this proof A=V_1 and W=W'.

The following precise locations supply the inputs:

- Section 1, printed pp.64–65: H is normal in N, N/H=SL_2(F_5), and each V_i is irreducible on H; duality is V_i^vee=V_(i+2).
- Observation (2.2), printed p.67: an isotypic H-module is the tensor product of a chosen extending irreducible H-module with its N/H multiplicity space; irreducibility is equivalent to that of the multiplicity space.
- Lemma 2.4, printed p.68, defines U=Sym^2(W_original), with W' its Galois conjugate. The appendix, printed p.81, labels U', W' by chi_3', chi_2'. Thus U'=Sym^2(W').
- Lemma 3.3(v), printed p.70, gives Sym^2(V)=V_1 tensor U'. Dualizing yields S_2=Sym^2(V^vee)=V_3 tensor (U')^vee.
- Equation (4.6), printed p.73, gives H^1(E(-2))=V_1 tensor W'; equation (4.12), printed p.74, gives H^1(E)=W'. Combining with (1) yields M_1=A tensor W and M_3=W.

The page images, including the primes in these formulas, were inspected. The publicly downloaded PDF has SHA256 db786d5ee732e0b70d122a39823d22088c60930492a83582b2b1028de7d1e482.

The two-dimensional representation W has determinant one: its determinant is a character of the perfect group SL_2(F_5), hence trivial. Thus an invariant nondegenerate alternating form identifies W with W^vee and identifies Sym^2(W) with sl(W). This also identifies (U')^vee with U'. These are representation isomorphisms, not preferred bases. We obtain

    S_2 = A^vee tensor sl(W),
    Hom(M_1,M_3) = A^vee tensor End(W)
                  = (A^vee tensor C) direct sum
                    (A^vee tensor sl(W)).            (2)

By (2.2), the two summands on the right are irreducible N-modules: their H-multiplicity representations are the trivial representation and U', respectively. They are distinct, of dimensions five and fifteen. This uses the full normalizer N; H alone would leave multiplicities and would not prove the assertion.

For a central-character check, V_1 has central weight two and its dual has weight three modulo five. S_1=V^vee has weight four, so S_2 has weight three. M_3=W has trivial H-action. Hence the source and target of the multiplication map below have the same central weight, as (2) requires. No determinant twist has been suppressed.

## 2. The unique equivariant multiplication embedding

Multiplication in the cohomology module is natural under the N-linearized bundle action. Therefore the map

    Phi:S_2 -> Hom(M_1,M_3),       q |-> T_q           (3)

is N-equivariant. It is nonzero. Indeed M is generated in degree zero, as recorded by the exact linear presentation in PR167, and M_3 is nonzero. Therefore S_2 M_1=M_3: each degree-three monomial times a degree-zero generator is a quadratic times a degree-one element. The zero map (3) would contradict this equality. Alternatively, the final exact row of (4.2) in the primary paper, printed p.72, presents H^1(E(n)) as a quotient of H^0(O(n+3)) tensor V_3, compatibly with multiplication. After the shift (1), this makes M a graded quotient of S tensor V_3 and proves the required generation directly.

By (2), Schur's lemma forces (3) to be a nonzero scalar multiple of the inclusion of the fifteen-dimensional summand A^vee tensor sl(W). In particular it is injective. After choosing its harmless scalar in the identification, multiplication is exactly

    T_(sum_i a_i tensor B_i)(x tensor w)
       = sum_i a_i(x) B_i(w),                         (4)

where a_i are linear forms on A and B_i are trace-zero endomorphisms of W.

Formula (4) is a universal representation-theoretic identification. It is not a constructed matrix for u_0, v_0, or any selected source instance. It does not identify the image of a binary-quartic coordinate monomial in A^vee tensor sl(W).

## 3. Classification of the failure cone

For q in A^vee tensor sl(W), let b_q:A -> sl(W) be its associated linear map, and write K_q for its image. Equation (4) says

    im(T_q)=sum_(B in K_q) im(B).                     (5)

If q is nonzero, some B is nonzero, so (5) is nonzero. This proves the rank-zero exclusion.

Suppose the rank is one, and let L=im(T_q), a line in W. Every B in K_q has image contained in L. A trace-zero endomorphism with image in L must annihilate L: choose a basis with first vector spanning L; its matrix has second row zero, and trace zero makes its upper-left entry zero. Consequently

    K_q is contained in Hom(W/L,L),                  (6)

viewed as a one-dimensional subspace of sl(W). Conversely every nonzero map in this subspace has image and kernel equal to L, is nilpotent, and has rank one. Thus q has the form a tensor n_L with a nonzero and n_L a nonzero member of that line. Conversely every such tensor gives rank one by (4).

The nonzero nilpotents in sl(W) projectivize to a smooth conic. For example a trace-zero matrix with entries (z,x;y,-z) has determinant -z^2-xy; its determinant-zero locus is the smooth projective conic z^2+xy=0. Alternatively the parametrization is L |-> Hom(W/L,L). Under W≅W^vee from its alternating form this is the degree-two Veronese map P(W) -> P(sl(W)). Tensoring with a in A^vee gives the Segre-Veronese embedding

    P(A^vee) times P(W) -> P(A^vee tensor sl(W)),
    with line bundle O(1,2).                         (7)

Its image is precisely the reduced projectivized bad locus. It has dimension 4+1=5 inside dimension14, hence codimension9. Its affine cone has dimension6 inside S_2 of dimension15. This does not presume reducedness of an unrelated presentation of its defining ideal.

For the catalecticant assertion, fix lambda≠0 in W^vee. The linear map

    sl(W) -> W^vee,       B |-> lambda B

is surjective. In a basis with lambda=(1,0), its values on the displayed trace-zero matrix are the arbitrary row (z,x). Tensoring with A^vee gives a surjection onto A^vee tensor W^vee=M_1^vee. Thus rank C_lambda=10. In particular its kernel is five-dimensional, agreeing with the fibers of the rank-one incidence described above.

## 4. The original fixed endpoint

Retain the original binary-quartic invariant u_0 and cubic v_0, and B=End_0(F). No transformation of either coefficient or bundle is made. The invariant u_0 is a nonzero quadratic. Injectivity of Phi gives rank T_(u_0)>=1, so

    dim M_3/(u_0 M_1+v_0 M_0)
       <= dim M_3/u_0 M_1 <=1.                       (8)

PR440 supplies the exact presentation, with its incoming map retained,

    35 bar M_2 -> 15 bar M_3 -> Q_0 ->0,
    bar M=M/(u_0,v_0)M.

Together with (8), this proves dim Q_0<=15. Under PR439's identification of the whole paired order-six coefficient dual with Q_0 direct sum Q_0, its dimension is at most30.

If u_0 lies outside (7), then T_(u_0) is surjective and Q_0=0. If it lies on (7), then the cubic image and the retained incoming map still matter; nonzero primary cokernel does not imply Q_0 nonzero. Neither membership nor either remaining map is evaluated here.

The conclusion is invariant under conjugating the HM symmetry representation, so it does not require aligning the chosen binary-quartic coordinates with the paper's basis. What cannot be inferred from characters alone is the particular tensor representing u_0. In particular no arbitrary PGL-invariance of F, or equality between a translated family and the fixed problem, is used.

## Dependencies, novelty boundary, and verification status

- Primary HM1973 source and exact printed locations are in Section1. Its representation calculations are used as published mathematical results.
- PR167 at 063da90fc4543304e87e701cdefcc08225412f17 supplies generation in degree zero and the normalized module conventions:
  https://github.com/Akilleez-QA/read-em-and-weep/blob/063da90fc4543304e87e701cdefcc08225412f17/research/conductor-normalization/sharper-hm-regularity/PROOF.md
- PR440 at 829e03411d04511f6cf04860bf18db4a70b12448 supplies the fixed endpoint presentation:
  https://github.com/Akilleez-QA/read-em-and-weep/blob/829e03411d04511f6cf04860bf18db4a70b12448/research/hm/degree-six-structural-reduction/PROOF.md
- PR439 at bf6ce91fd73fbc96cb8ede65448dfedbc0328c7b supplies the paired coefficient identification:
  https://github.com/Akilleez-QA/read-em-and-weep/blob/bf6ce91fd73fbc96cb8ede65448dfedbc0328c7b/research/hm/paired-collision-endpoint/PROOF.md
- Comparison: PR448 at 57cd7c7ab2ce60ada8732e62dba836f149d07023 proves codimension>=2 for the more general class of finite-length linearly presented modules with two-dimensional degree-three part. It leaves the rank-zero case at a given quadratic open. The present argument uses HM's stronger full-normalizer representations, not only those general hypotheses:
  https://github.com/Akilleez-QA/read-em-and-weep/blob/57cd7c7ab2ce60ada8732e62dba836f149d07023/research/hm/linear-presentation-transversality/PROOF.md

Current PR1 and these relevant public proofs were read on 2026-10-20. This is a bounded comparison, not an exhaustive novelty claim. No selected actual HM/source-instance multiplication matrix, rank sample, source evaluation, generator, checker, or large computation was performed. The fixed Q_0 value, actual source membership, six pure conditions, module lifting and quantization algebraicity remain unresolved. Mathematical text review is distinct from formal verification.
