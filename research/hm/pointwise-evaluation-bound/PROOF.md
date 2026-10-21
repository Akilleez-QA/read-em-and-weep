# Pointwise primary evaluation rank at least six

Work over C. All statements below concern the primary multiplication M0 -> M2, not the full adjoint quadratic multiplication.

## 1. Universal four-plane lemma

Let W have dimension two, V be any finite-dimensional vector space, and L be a four-dimensional subspace of V tensor W. Write

    Y = span{(id_V tensor D)L : D in sl(W)}.

Then either L=E tensor W for a two-dimensional subspace E of V and dim(Y)=4, or dim(Y)>=6. In particular dim(Y)=5 is impossible. Consequently, if L contains no nonzero full fiber v tensor W, then dim(Y)>=6.

Proof. Choose a basis of W and identify V tensor W with V direct-sum V. Put A=pr1(L), B=pr2(L), C=A intersection B, s=dim(A)+dim(B), and d=dim(L intersection (C direct-sum C)). For the standard traceless operators E12, E21, H=diag(1,-1),

    E12 L = B direct-sum 0,
    E21 L = 0 direct-sum A.

Their sum has dimension s. The map L -> (V direct-sum V)/(B direct-sum A), sending (a,b) to the class of (a,-b), has kernel exactly L intersection (C direct-sum C). Thus

    dim(Y) = s + 4 - d.                                      (1)

Since L is contained in A direct-sum B, s>=4. If s>=6, the two off-diagonal images already give dim(Y)>=6. If s=5 and dim(Y)<=5, (1) forces d=4. Then L is contained in C direct-sum C, so its projection images A and B both equal C. This contradicts the odd value s=5. Finally, if s=4, L=A direct-sum B and d=2dim(C), whence dim(Y)=8-2dim(C). A value at most five forces dim(C)>=2; since dim(A)+dim(B)=4, this implies A=B=C of dimension two and L=C tensor W. Conversely such an L has Y=L. This proves the dichotomy.

The bound six is sharp under the no-full-fiber hypothesis in the universal setting. Inside E direct-sum E with E=span(e1,e2,e3), take

    L=span{(e1,0), (e2,e1), (e3,e2), (0,e3)}.

Its two projection images equal E, so (1) gives dim(Y)=6. If (v,0) belongs to L, then v is a multiple of e1; if (0,v) belongs to L, then v is a multiple of e3. Thus no nonzero v has both properties. This is an abstract sharpness example, not an evaluation or realization of an HM star.

## 2. Actual primary consequence

Use the actual exterior multiplication model established in PR543:

    A0=M0, dim(A0)=5, M2=V tensor W, dim(V)=5, dim(W)=2,
    S2=A0 tensor sl(W), exterior^2 A0=V tensor W,
    (a tensor D)x = c (id_V tensor D)(a wedge x), c != 0.

For every nonzero x, the star Lx=x wedge A0 has dimension four. The Galois-conjugated HM Lemma 2.5 says it contains no nonzero full fiber v tensor W. Therefore the universal lemma proves

    rank(e_x)>=6 for every [x] in P(A0),
    e_x:S2 -> M2, q |-> qx.                                  (2)

This improves the established pointwise bound five without evaluating a selected coefficient, matrix, source instance, or numerical rank.

## 3. Primary-bad codimension at least four

Let B be the closed locus of [q] in P(S2)=P14 for which q:M0 -> M2 is not injective. Two separately pinned inputs are used:

- The invariant-gcd argument of PR543 proves dim{x:rank(e_x)<=6}<=2.
- PR547 proves generic rank(e_x)=10. Hence the rank-at-most-nine locus is proper in P(A0)=P4 and has dimension at most three.

Consider Z={([x],[q]): qx=0} inside P4 times P14. Over the evaluation-rank-r stratum its fiber is P(ker e_x), of dimension 14-r. By (2), only ranks six through ten occur. The rank-six stratum contributes dimension at most 2+8=10. Each rank-seven, eight, or nine stratum has base dimension at most three, hence contributes at most 3+7=10. The rank-ten stratum contributes at most 4+4=8. Thus dim(Z)<=10. Its projective image is exactly B, so

    dim(B)<=10, codim(B,P14)>=4.                              (3)

A general projective three-space in P14 therefore avoids B, since 3+10<14. Equivalently, a general four-dimensional vector subspace of S2 consists entirely of primary-injective nonzero quadratics.

Fix any nonzero q0, without deciding whether p=[q0] is in B. Project B minus {p} from p to P13; the closure of its image has dimension at most ten. A general P2 in P13 misses this closure, since 2+10<13. The corresponding P3 through p meets B only possibly at p. Thus every prescribed quadratic lies in a projective three-space all of whose other parameters are primary-injective. This is not a decision about the prescribed quadratic itself.

## Dependencies and verification boundary

1. Exterior model and no-full-fiber input: PR543, commit 7bf725bcd857a2deb975f9ecb80fca32e7833ae0, research/hm/order-four-quadratic-load/PRIMARY-INJECTION-AND-FAILURE.md:
https://github.com/Akilleez-QA/read-em-and-weep/blob/7bf725bcd857a2deb975f9ecb80fca32e7833ae0/research/hm/order-four-quadratic-load/PRIMARY-INJECTION-AND-FAILURE.md
2. Rank-at-most-six locus dimension bound: PR543, commit 8d24a12c4af9c922db2052a360c96a053dcba5b8, Sections 1–2 of PRIMARY-BAD-CODIMENSION-THREE.md:
https://github.com/Akilleez-QA/read-em-and-weep/blob/8d24a12c4af9c922db2052a360c96a053dcba5b8/research/hm/order-four-quadratic-load/PRIMARY-BAD-CODIMENSION-THREE.md
3. Generic rank ten: PR547, commit 5a8efc999e9b886c51f18232a580407bac4bbe66:
https://github.com/Akilleez-QA/read-em-and-weep/blob/5a8efc999e9b886c51f18232a580407bac4bbe66/research/hm/primary-evaluation-generic-surjectivity/PROOF.md
4. Primary source: Horrocks–Mumford (1973), Lemma 2.5, printed page 69:
https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf

The new deductions are the universal rank-five exclusion, actual pointwise rank-six bound, codimension-four bound, and uniform/punctured three-spaces. The proof is mathematical, not proof-assistant checked. Independent review should explicitly verify (1), the pinned no-full-fiber input, and the incidence dimensions. No expected-codimension assertion about evaluation degeneracy is needed. Full adjoint quadratic invertibility, residual surjectivity, the actual twenty-dimensional lift boundary, Q4, original selected-pair membership, higher-order lifting and algebraicity remain unresolved.
