# Regular source-divisor normalization of the fifth norm class

## Scope and pinned inputs

Work over C on the actual integral quadric cone Q, with the fixed physical-even marking. Let

    Qsq = pi_*(I_Z^2(6)) subset O_Q(6),
    R6 = O_Q(6)/Qsq = pi_*O_(2Z)(6).

Here I_Z is the ideal of the regular section on the smooth weighted stack, and its square is the ordinary STACK square, never the square of the coarse Ext-annihilator. We retain nonzero sources a,h, the classified completion data, K=aJ4, and f=a^4h in H0(O_Q(10)). Thus K|Q=fN.

The inputs, not new results of this note, are:

1. [PR769 at 1599ab33ec5392433da49fcfbd0bddd5ba1482d3](https://github.com/Akilleez-QA/read-em-and-weep/blob/1599ab33ec5392433da49fcfbd0bddd5ba1482d3/research/hm/ideal-valued-fifth-norm/PROOF.md). For local fifth adjoint lifts K_i and a global scalar lift P of n(K), write

       K_j-K_i=q^4 c_ij,
       n(K_i)-P=q^4 w_i,
       w_j-w_i=f tau(c_ij),   tau=tr(N-).

   The w_i modulo f Qsq glue to chi_P in H0(C_f), where C_f=O_Q(16)/(f Qsq). Its class nu(K) modulo global O_Q(16) has connecting class tau_*(delta_5 K) in H1(Qsq).
2. [PR770 at b242300110c33627eb77ee5ab36cc81fffa359e4](https://github.com/Akilleez-QA/read-em-and-weep/blob/b242300110c33627eb77ee5ab36cc81fffa359e4/research/hm/faithful-fifth-norm/PROOF.md). The actual trace map induces an isomorphism H1(B_Q(4))_+ to H1(Qsq)_+. Hence the norm criterion is faithful, including after quotient by the actual second-symbol image V_a=im(beta2_a).
3. [The square-filtration theorem at 8d8b5be4ce62c3055bb53be9e16d29cc63072f04, sections 1--2](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/POSITIVE-SECOND-BOCKSTEIN-SQUARE-FILTRATION.md). It already identifies H1(Qsq)_+ with the vertex quotient H0(Q4(6))/H0(Sym8(W') tensor O_L(2)), and then with H1(P4 tensor O_L(-2)). Q4 here denotes the vertex relation bundle, not Qsq.

The new step is an explicit, regular representative-level passage from the degree-sixteen norm coset to this already-known degree-six vertex test. It removes the source divisor without restricting to its complement, and proves exactly how all choices disappear. No value of the actual norm class is computed.

## 1. A source-divisor lifting lemma

Let Y be a scheme, L and M invertible sheaves, A a subsheaf of L, and f a section of M which is a non-zero-divisor on O_Y. Put

    R=L/A,   C=(L tensor M)/(f A),   D=div(f).

Assume H1(Y,L)=0. Multiplication by f induces a canonical isomorphism

    H0(R)/im H0(L)  -->  H0(C)/im H0(L tensor M).       (1)

More explicitly, the inverse is computed by lifting the residue on the whole effective Cartier divisor D, subtracting that global lift, and then using multiplication by f onto its image.

Proof. The non-zero-divisor condition gives the exact sequences

    0 -> L --f--> L tensor M -> (L tensor M)|D -> 0,    (2)
    0 -> R --f--> C -> (L tensor M)|D -> 0.            (3)

The first arrow of (3) is injective even if R has f-torsion: locally, if f l belongs to f A in L tensor M, cancellation in the invertible ambient sheaf gives l in A. This assertion must not be confused with injectivity of multiplication by f from R to R tensor M, which is not required and may fail.

For chi in H0(C), let d be its image in H0((L tensor M)|D). By H1(L)=0 and (2), choose r in H0(L tensor M) restricting to d. Then chi-r lies in the kernel of the last map of (3), so there is a unique t in H0(R) with f t=chi-r. If another lift r' is chosen, (2) gives a unique s in H0(L) with r'-r=f s; the corresponding t' is t-s. Replacing chi by chi+u for global u in H0(L tensor M) permits the choice r+u and leaves t unchanged. Thus [t] is well-defined on the right side of (1).

Conversely multiplication by f sends ambient sections of L to ambient sections of L tensor M. It therefore defines (1); the construction above is its inverse. Equivalently, if f t is represented by a global r, then r|D=0, r=f s for global s, and injectivity in (3) gives t=s in H0(R). This proves injectivity as well as surjectivity. All constructions use regular sheaves on Y, including along D. No rational inverse of f occurs. QED.

This lemma does not assume that D is reduced, smooth, disjoint from the support of R, or transverse to that support.

## 2. Apply the lemma to the local norm errors

Use Y=Q, L=O_Q(6), M=O_Q(10), A=Qsq. Since Q is integral and f is nonzero, f is a non-zero-divisor. The hypersurface sequence

    0 -> O_P4(4) -> O_P4(6) -> O_Q(6) -> 0

and intermediate line-bundle cohomology on P4 give H1(O_Q(6))=0. Thus (1) applies, with D the full possibly nonreduced divisor of a^4h. It identifies the norm quotient canonically with

    H0(R6)/im H0(O_Q(6)).                            (4)

Here is the local extraction, including its sign. The restrictions w_i|D agree because their differences lie in f Qsq. They define d in H0(O_D(16)). Choose a global r in H0(O_Q(16)) lifting d. On each affine chart,

    w_i-r=f v_i,       v_i in O_Q(6),                (5)

where v_i exists by the image-kernel equality in (2) and is unique by injectivity. Formula (5) is a regular image equation, not meromorphic division. On overlaps, cancellation in the ambient invertible sheaf gives

    v_j-v_i=tau(c_ij).                              (6)

Therefore the images of v_i modulo Qsq glue to t in H0(R6). The positive-Cech connecting map for 0 -> Qsq -> O_Q(6) -> R6 -> 0 sends [t] to [tau(c_ij)], exactly the norm class, not its negative.

The invariances can also be checked directly. A change K_i -> K_i+q^4 D_i adds f tau(D_i) to w_i, hence adds tau(D_i) to v_i and leaves t unchanged. A scalar-lift change P -> P+q^4 u subtracts the global u from w_i; replacing r by r-u leaves v_i unchanged. Changing r alone changes t by a global sextic, as in the lemma. Thus the only ambiguity in t is precisely the one in (4).

The physical-even operations are legitimate: f is even, all sequences are equivariant for physical inversion, and averaging in characteristic zero permits even r and even local data on an invariant affine cover. This physical parity is not the local stack stabilizer character.

## 3. Explicit passage to the finite vertex test

We now apply, rather than reprove as a new result, the pinned square-filtration normalization. The physical-even section space H0(R6)_+ has a conic component and a filtered vertex component. At the vertex L=P(W), its positive graded pieces are

    gr0=O_L(6),
    gr2=Sym4(W') tensor O_L(4),
    gr4=Q4(6),

and F^6=0. The ambient positive sextics have polynomial pieces of cover degrees 0,4,8,12, respectively of dimensions 7,25,27,13.

Given t from (5), perform these exact operations:

- Remove its conic value using the unique cover-degree-twelve polynomial. The conic has H0(O_C(6))=H0(O_P1(12)), dimension 13. This polynomial vanishes on the vertex quotient because F^6=0.
- Remove the low vertex quotient modulo F^4 using the cover-degree-zero and cover-degree-four polynomial pieces. They vanish on the conic. Their actual filtered restriction induces the identity on gr0 and gr2, hence is an isomorphism onto the low quotient on global sections. Its dimensions are 7 and 25. This uses a filtered isomorphism, not an assumed homogeneous splitting of the vertex thickening.
- The remaining section s vanishes on the conic and belongs to F^4 on the vertex, canonically identified with H0(L,Q4(6)). Changing t by an ambient sextic changes s exactly by the image of the cover-degree-eight piece Sym8(W') tensor H0(O_L(2)).

In the second step, surjectivity on global sections also follows by the vanishing of H1 of the two low graded bundles. The top piece does not affect that quotient. The exact top relation sequence is

    0 -> P4 tensor O_L(-2)
      -> Sym8(W') tensor O_L(2)
      -> Q4(6) -> 0.                                (7)

Since H0(O_L(-2))=0 and H1(O_L(2))=0, its boundary gives

    H0(Q4(6))/H0(Sym8(W') tensor O_L(2))
        ~= H1(P4 tensor O_L(-2)).                    (8)

The dimensions are 31 modulo 27, leaving four. For the fixed marking this is the prior P4 target. No equality here is inferred merely by matching dimensions.

For an entirely sheaf-theoretic extraction of (8), take the two standard affine charts of L, lift s locally through the surjection in (7), subtract the two lifts on their intersection, and regard that difference in P4 tensor O_L(-2). Its Cech cohomology class is delta_6(s). Changing the local lifts changes this cocycle by a coboundary. Thus the extraction needs no global splitting of (7), no selected actual point, and no source-dependent matrix inverse.

Combining (5)--(8) yields the explicit map

    (w_i modulo f Qsq and global degree-sixteen scalars)
       -> [t] -> [s] -> eta(K)=delta_6(s) in P4.      (9)

Every choice was accounted for above. By (6) and the pinned natural square-filtration identification, eta(K) is exactly the image of tau_*(delta_5 K), with the same connecting convention.

## 4. What this resolves and what remains

Let T:H1(Qsq)_+ -> H1(P4 tensor O_L(-2)) denote the fixed isomorphism (8). Define the transported second-symbol subspace

    W_a=T(tau_*(V_a)).

Then PR770 and (9) give the exact finite criterion

    beta4_a(h)=0  iff  eta(K) belongs to W_a.         (10)

For a fixed fourth lift K before completion changes, K extends to 5Q if and only if eta(K)=0. For classified changes of completion, eta changes by W_a. These statements need no constant-rank assumption on beta2_a and remain valid on rank-drop directions.

The newly supplied dependency is the regular reduction of arbitrary norm errors, not just zero norm classes, to the old finite vertex model. Even when D contains or meets the support of the square thickening, the residue lift and cancellation take place in ambient invertible sheaves, so the extraction remains defined. In particular one must not replace this by evaluating w_i/f on the complement of D and assuming the result extends.

The actual local norm data needed to determine eta(K) have not been evaluated. This note does not decide its membership in W_a, infer beta4 from a nonzero q^3 norm coefficient, or prove algebraicity. The old P4 quotient and the faithfulness theorem are explicitly dependencies, not claimed as new. The proof is deductive exact-sequence and filtration reasoning; it is authored, not proof-assistant certified. No selected actual coefficient, point, derivative, matrix, rank, or source-instance computation, and no large computation, is used.
