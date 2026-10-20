# Generic order-five vanishing by quintic factor incidence

Work over C on Y=P^4, with S_d=H^0(Y,O(d)). Let F be the normalized Horrocks–Mumford bundle, B=End_0(F), E=F(3), and C the union of the twenty-five evaluation-degeneracy lines. Write

    W=H^0(I_C(5)),
    Q_5(u,v)=H^1(B(5))/(uH^1(B(3))+vH^1(B(2))).

The pinned structural results give dim W=6, dim H^1(B(5))=32 and an eight-dimensional primary image L. We prove that Q_5(u,v)=0 on a nonempty Zariski-open set of pairs. More strongly, for every u in a specified nonempty open set of quadrics, the exceptional cubics have codimension at least 24 in P(S_3). This is an existence and dimension theorem, not a determination of the original selected pair.

## 1. Quadrics avoiding all quintic factors

Consider the projective incidence

    X={( [h],[u],[g] ) ∈ P(W)×P(S_2)×P(S_3): [h]=[ug]}.

Multiplication is a morphism on the product of projective spaces, since the polynomial ring is a domain. Thus X is closed and projective. For fixed nonzero h, there are only finitely many projective factorizations h=ug with deg u=2 and deg g=3: unique factorization gives finitely many allocations of its irreducible factors, and projective classes remove scalar choices. Hence the projection X→P(W) has finite fibers, so dim X≤dim P(W)=5.

The image D_2 of X in P(S_2)=P^14 is therefore closed of dimension at most five. If [u] lies outside D_2, no nonzero h∈W is divisible by u. Equivalently, restriction

    W→H^0(Q,O_Q(5)),  Q=V(u),                   (1)

is injective, by 0→O(3) --u→ O(5)→O_Q(5)→0.

Let O be the set of quadrics satisfying all four conditions:

- Q is smooth;
- [u] is outside D_2;
- multiplication u:H^1(F(1))→H^1(F(3)) is surjective;
- Q contains none of the twenty-five component lines of C.

This is a nonempty Zariski-open subset of P^14. Smoothness is a nonempty open condition. The second bad locus has dimension at most five. PR449 proves that the third bad locus has codimension nine. For each fixed line, containing that line imposes three independent linear conditions on S_2, so the fourth bad locus is a finite union of proper linear subspaces. Irreducibility of P^14 makes the intersection of these finitely many nonempty opens nonempty. This argument chooses no actual quadratic coefficients.

## 2. A finite-factor lemma on a smooth quadric

Fix [u]∈O and let Q=V(u), a smooth integral projective threefold. Put

    A_d=H^0(Q,O_Q(d)),  W_Q=res(W)⊂A_5.

Then dim W_Q=6, dim A_2=15−1=14 and dim A_3=35−5=30. The dimensions follow from the hypersurface restriction sequence and vanishing of intermediate cohomology of line bundles on P^4.

Define

    Y_u={( [h],[a],[b] ) ∈ P(W_Q)×P(A_2)×P(A_3): [h]=[ab]}.

This is again a closed projective incidence: nonzero sections on an integral variety have nonzero product. For fixed nonzero h, each factor b has an effective divisor div(b) which is an effective sub-divisor of div(h). A divisor has finitely many irreducible components with finite multiplicities, so there are only finitely many such sub-divisors. Two nonzero sections of O_Q(3) with the same divisor differ by a global invertible regular function: their ratio has neither poles nor zeros on the smooth variety, and projectivity and integrality make it a nonzero constant. Thus there are only finitely many projective b, and likewise finitely many projective factorizations h=ab. No unique factorization assertion about the homogeneous coordinate ring of Q is needed.

It follows that dim Y_u≤5. Its image D_3(u) in P(A_3)=P^29 is closed of dimension at most five. Therefore

    codim D_3(u)≥24.                            (2)

If [bar v] is outside D_3(u), there is no nonzero h∈W_Q divisible, as a section, by bar v. In polynomial terms this says

    W ∩ (u,v)_5 = 0.                            (3)

Indeed a relation h=uf+vg restricts to bar h=bar v·bar g, and (1) ensures bar h≠0 for nonzero h. Conversely every such factorization on Q lifts: S_2→A_2 and S_3→A_3 are surjective, and the kernel of S_5→A_5 is uS_3. The signs in the two-generator ideal are immaterial.

## 3. The exceptional cone in cubic space

The restriction S_3→A_3 is surjective with kernel uS_1, of dimension five. Let Z_u⊂P(S_3)=P^34 be the projectivized inverse image of the affine cone over D_3(u), including the projection center P(uS_1)=P^4. This is closed. If D_3(u) is nonempty, its affine cone has dimension at most six, so the inverse image has affine dimension at most eleven and projective dimension at most ten. If the incidence is empty, Z_u is just the center and the same upper bound holds. Thus

    dim Z_u≤10,  codim Z_u≥24.                  (4)

Every v outside Z_u has nonzero restriction to Q, so u does not divide v. Since smooth u is irreducible, gcd(u,v)=1. Formula (3) holds for these cubics.

## 4. The full order-five quotient vanishes

PR458 supplies the following two structural facts for coprime u,v:

1. The residual quotient R=H^1(B(5))/(L+uH^1(B(3))+vH^1(B(2))) has dual, up to a common one-dimensional determinant factor, the simultaneous interpolation space W(u,v).
2. The map W(u,v)→W∩(u,v)_5 has kernel of dimension k, the number of component lines contained in both u and v.

Our choice of u contains no component line, so k=0 for every v. Hence (3) implies W(u,v)=0 and R=0. This uses only injectivity of the tuple-to-quintic map; it does not require C∩V(u,v) to be empty.

The primary obstruction also vanishes. PR449's surjectivity uM_1=M_3, where M_j=H^1(F(j)), implies uM_1+vM_0=M_3. By the natural cup maps and PR458, this implies L⊂uH^1(B(3))+vH^1(B(2)). The exact primary/residual quotient sequence therefore gives

    Q_5(u,v)=0   for [u]∈O and [v]∉Z_u.         (5)

In particular, for every quadric in the nonempty open O, the full order-five exceptional cubic locus is contained in a closed subset of codimension at least 24. We do not claim equality between the exceptional locus and Z_u: an element of W∩(u,v)_5 need not be a residual obstruction without additional hypotheses.

Multiplication gives an algebraic family of maps from H^1(B(3))⊕H^1(B(2)) to H^1(B(5)) on affine parameter charts, with entries linear in u and v. Surjectivity is an open condition, independent of rescaling either form. Equation (5) supplies nonemptiness. Thus full Q_5 vanishing holds on a nonempty Zariski-open, hence dense, subset of P(S_2)×P(S_3). No numerical matrix is formed or evaluated in this openness argument.

## 5. Additional geometric consequence

One may additionally arrange C∩V(u,v)=empty. For [u]∈O, the intersection C∩Q is finite of scheme length fifty, since each line is cut by a nonzero quadratic. Cubics nonvanishing at every point of its finite support form a nonempty open subset of P(S_3): evaluation at any one point is a nonzero linear functional. This open intersects the nonempty complement of Z_u. The resulting pair simultaneously has primary coverage, no intersection on C and zero quintic intersection. In this subfamily PR458's stronger residual/quintic isomorphism applies, although it was unnecessary for (5).

Where the full geometric hypotheses of PR451 realize a coefficient pair, its paired order-five obstruction coefficient dual is Q_5(u,v)⊕Q_5(u,v). Such a realization therefore has vanishing order-five coefficient whenever its pair belongs to the open set above. Genericity here is proved only in the full independent coefficient space S_2×S_3. No restricted source-compatible parameter family has been shown to meet that open set. This is not a proof of order-four vanishing or optimality.

## Pinned dependencies and limits

- PR458, b46c3b48a8b10a7d0656fde247f2c3f258d1fd23: six-dimensional quintic space, simultaneous interpolation, exact common-line kernel and primary separation:
https://github.com/Akilleez-QA/read-em-and-weep/blob/b46c3b48a8b10a7d0656fde247f2c3f258d1fd23/research/hm/pair-interpolation/PROOF.md
- PR449, e4b6acdd27d8da8be4052c117ea2dca0f48f46ff: proper codimension-nine primary bad-quadratic locus:
https://github.com/Akilleez-QA/read-em-and-weep/blob/e4b6acdd27d8da8be4052c117ea2dca0f48f46ff/research/hm/quadratic-failure-cone/PROOF.md
- PR451, ed8841c18f103e71b84c0e9376e20a2a4ed2ef9c: paired order-five coefficient quotient:
https://github.com/Akilleez-QA/read-em-and-weep/blob/ed8841c18f103e71b84c0e9376e20a2a4ed2ef9c/research/hm/order-five-cubic-defect/PROOF.md

The new work is the factor-incidence exclusion, codimension bound, and full generic order-five vanishing. The original selected pair has not been proved to lie in O or outside Z_u, and no genericity statement for a restricted actual-source family is inferred. Its Q_5 remains unresolved. Actual-source membership, six pure conditions, higher-order module lifting and algebraicity remain separate. No selected HM/source-instance evaluation, coefficient search, numerical rank, generator/checker or large computation is used. This is a mathematical proof for review, not formal machine verification.
