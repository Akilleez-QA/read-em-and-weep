# A universal one-parameter abstract family for the source127 c-d-f edge

## Result and boundary

There is a nonempty Zariski-open subset Omega of P1, obtained by removing at most two points, whose members define equivariant constant inclusions

    E=(P+D) O(-2)+(V+P) O(-4)+O(-8) subset H O,
    H=2A+2V+2P+2D,

with saturated Gauss quotients

    A_q=O(-8)+O(2)+O(16),
    B_q=O(-18)+O(-4)+O(6).                         (1)

Both initial Gauss ranks are three and both next generic Gauss ranks are two. Thus these abstract inclusions have the formal maximal profile-(1,1) and source tuple

    G3.11.cce6e3ba4eeb, source_index127,
    (0,0,1,1,0,1,0,0).

No point of Omega is selected. This proves existence of an abstract family satisfying the displayed constant-bundle, source, quotient, saturation, strict-top and profile conditions. It does not identify any member with the fixed actual HM inclusion, reconstruct or extend the full actual HM module, or assert that every abstract realization of this source belongs to the family. No source edge or stable label is excluded. The contribution is an explicit boundary for further exclusions: the listed structural conditions alone are consistent on this edge.

The family is constructed from a balanced degree-eighteen quotient and two universal osculating bundles. Nonemptiness follows from exact Euler sequences on covariant spaces, not from a chosen coefficient calculation, matrix, parameter, or point. The verifier uses only fixed abstract character identities and the original pinned source lists.

## 1. Immutable data and conventions

All original actual coefficient, source and quotient data are at commit

    db51525015bb7c5e825833d550d08dedf6f6ea96

of Akilleez-QA/read-em-and-weep, under

https://github.com/Akilleez-QA/read-em-and-weep/tree/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load

The exact files are ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md, NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md, one-one-endpoint-necessary-pairs.json and rank-three-quotient-frontier-144.json. The manifest records their immutable URLs and Git blob hashes. We use these only to identify the target formal data, not as evidence that the constructed family occurs in actual HM data.

The quadratic first-polar and derivative-image principles are recorded in PR802, commit e484640a6565c278321bf6557860262c1ac1b7df, Sections2 and5:

https://github.com/Akilleez-QA/read-em-and-weep/blob/e484640a6565c278321bf6557860262c1ac1b7df/research/hm/profile11-o16-constant-span-exclusion/PROOF.md

The dual second fundamental form and saturated-image conventions agree with PR796, commit d2b43060c83328dd5118aee6b9288fcfa0c873ac:

https://github.com/Akilleez-QA/read-em-and-weep/blob/d2b43060c83328dd5118aee6b9288fcfa0c873ac/research/hm/profile12-quadratic-block-exclusion/PROOF.md

Every needed geometric argument is also given below. Work over C with the binary icosahedral group G and its defining two-space W. Put A=Sym2 W, S=Sym3 W, D=Sym4 W and T=Sym5 W; Wp,V,P are the other irreducibles of dimensions2,3,4. All irreducibles are self-dual. Use invariant alternating forms on W and Wp and the equivariant identifications

    P=W Wp,    T=A Wp=V W.

Tensor products are written by juxtaposition. Every nonempty invariant effective divisor on P(W) has degree at least twelve. In particular there is no invariant scalar form of degree sixteen, as is also checked by its character below. The formal vector w denotes the homogeneous variable, never a chosen parameter-line point.

For an irreducible R write M_R(n)=Hom_G(R,Sym^n W). After self-duality this is the space of R-valued covariants of degree n. The fixed identities used in the construction are

    Sym16 W=V+P+2D,
    Sym17 W=Wp+S+2T,
    Sym18 W=A+V+2P+D,
    Sym19 W=W+Wp+S+2T,
    Sym10 W=A+V+D,
    Sym8 W=P+D,
    Sym7 W=Wp+T,
    Sym6 W=V+P.                                    (2)

## 2. The degree-eighteen quotient family

Set C0=A+V+P, of dimension ten. An injective coefficient map C0->Sym18 W contains the unique A and V constituents and one P copy in a two-dimensional multiplicity space. Up to independent nonzero constant scalings of A,V,P it is therefore specified by

    p in P(M_P(18))=P1.

Write q_p:C0 O->O(18) for its coefficient system. Its A and V components are nonzero by definition; p is a nonzero P covariant up to scalar. Initially q_p need not be onto. The multiplication map on sections is

    mu_p:C0 W -> Sym19 W.                           (3)

The source and target both equal W+Wp+S+2T. In their multiplicity spaces, (3) has the blocks

    W: a_W;  S: a_S;  Wp: p_Wp(p);
    T: [v_T, p_T(p)].                              (4)

Here a_W,a_S,v_T come from the fixed nonzero A and V covariants. We prove the required maps are nonzero or surjective instead of inferring this from multiplicities.

Contraction Sym2 W->W with the alternating covector associated with w gives the exact equivariant Euler sequence

    0 -> O(16) -> A O(18) -> W O(19) ->0.           (5)

Taking invariant sections is exact, since H1(O(16))=0 and G is finite in characteristic zero. Its left invariant space is zero by (2). Both other invariant spaces have dimension one. Hence a_W is nonzero. The A-to-S channel multiplies a quadratic by w and is fiberwise injective for every nonzero formal vector, so it sends a nonzero A covariant to a nonzero S covariant. Thus a_S is nonzero.

The identification V W=T similarly implies v_T is nonzero. For the P-to-Wp channel, tensoring Euler by Wp gives

    0 -> Wp O(17) -> P O(18) -> Wp O(19) ->0.       (6)

Taking invariant sections proves p_Wp:M_P(18)->M_Wp(19) is onto, with one-dimensional kernel: the three multiplicities are1,2,1 and the left H1 vanishes. The P-to-T channel instead multiplies the W factor in P=W Wp by w into A Wp=T. It is fiberwise injective, hence injective on covariants. Its source and target multiplicity spaces both have dimension two by (2), so

    p_T:M_P(18)->M_T(19)

is an isomorphism.

Consequently (3) is an isomorphism exactly when

    p_Wp(p) != 0,
    det(v_T,p_T(p)) != 0.                           (7)

These are nonzero linear forms on the two-dimensional space M_P(18). Their projective zero sets are points, possibly the same point. Their complement Omega in P1 is therefore nonempty, open and one-dimensional. This is a universal avoidance argument; no representative p is selected or evaluated.

## 3. Balanced kernel and unramified derivative

For p in Omega, q_p is onto everywhere. Otherwise every degree-nineteen section in the image of mu_p would vanish at a common point, contradicting the complete basepoint-free degree-nineteen system and the surjectivity of mu_p. Put F_p=ker q_p. Twisting its exact sequence by one and using (3) gives

    H0(F_p(1))=H1(F_p(1))=0.

A split line bundle on P1 is acyclic exactly in degree minus one. Hence F_p(1) is pure O(-1), and its equivariant Euler character identifies

    0 -> F_p=(P+D) O(-2) -> C0 O -> O(18) ->0.      (8)

Indeed Sym18 W-C0=P+D. The coefficient map C0->Sym18 W is injective, so its quotient curve is nonconstant and spans the dual ten-space. Its hyperplane kernel has generic Gauss rank one and saturated first span C0 O.

There is also no raw derivative defect. Let B be the raw sheaf generated by F_p and its first derivatives, and let Delta be its effective divisor of defect inside C0 O. Thus

    0 -> F_p -> B -> O(18-Delta) ->0,
    rank B=10,    deg B=-deg Delta.                 (9)

For a quadratic inclusion the raw first-polar image is the image of

    (P+D) W O(-1) -> C0 O.

It is exactly B: the value and derivative of a quadratic span its first polar, including the value by Euler's identity. Hence B(1) is generated. Also B is a torsion-free subsheaf of a constant bundle, so every splitting degree of B is at most zero. All its degrees are consequently zero or minus one, and

    0 <= deg Delta <= 10.

The construction is equivariant, so Delta is invariant. The minimum invariant divisor degree twelve forces Delta=0. Thus B=C0 O, with actual derivative surjection

    F_p -> O(16),                                  (10)

not merely a generically onto map followed by a torsion correction. This uses no actual HM specialization.

## 4. Two universal residual blocks

For 0<=k<n let U_k^n be the standard osculating subbundle in Sym^n W O: at the formal line l it is l^(n-k) Sym^k W. There are universal exact sequences

    U_k^n=Sym^k W O(k-n),
    0 -> U_k^n -> Sym^n W O
      -> Sym^(n-k-1) W O(k+1) ->0.                 (11)

The quotient in (11) follows from the Euler filtration of the symmetric power; its kernel consists exactly of the multiples of l^(n-k). Differentiating these multiples gives all multiples of l^(n-k-1) of the next degree. The coefficient n-k is nonzero in characteristic zero. Consequently, for k<n,

    (U_k^n)^+=U_(k+1)^n,
    U_(k+1)^n/U_k^n=O(2k-n+2),
    A_q(U_k^n)=O(2k-n),                            (12)

with every displayed image saturated. These are universal exact maps, not ranks obtained by evaluating a chosen point.

Take R=U_6^10=(V+P) O(-4) in Sym10 W O and L=U_0^8=O(-8) in Sym8 W O. Their saturated derivative quotients from (12) are O(2) and O(-8), respectively. They span the full constant eleven- and nine-spaces. Now define

    E_p=F_p direct-sum R direct-sum L,
    H=C0 direct-sum Sym10 W direct-sum Sym8 W.       (13)

Each inclusion is saturated and spans its indicated constant space. Equations (2) and (8) show that (13) has exactly the source and H representation in the result. Its rank is9+7+1=17 and degree is-18-28-8=-54. Its quotient is

    Q_p=O(18)+S O(7)+(Wp+T) O(1).                  (14)

Thus rank Q_p=13, degree Q_p=54, H0(Q_p*)=0, and Q_p(-1) is globally generated.

The connection respects the actual constant direct sum (13), so (10) and (12) give the raw saturated Gauss quotient A_q in (1). The dual second fundamental form is the negative transpose. A locally split constant-rank image dualizes to a locally split image of the same rank; hence it too has no derivative defect, and its quotient is

    B_q=A_q*(-2)=O(-18)+O(-4)+O(6).

For completeness the quadratic strict-top condition also holds. If H0(F_p^-(2)) were nonzero, its constant coefficient kernel would give a nonzero subspace U of P+D such that U O(-2) differentiates inside F_p. Its internal derivative into (F_p/U O(-2))(-2), a sum of O(-4)'s, is zero by degree. Thus U O(-2) would be horizontal in C0 O, impossible for a negative bundle. The other summands of E_p have degree at most minus four, so

    H0(E_p^-(2))=0.

The quotient (14) also has precisely the actual fixed coefficient characters

    H1(E_p)=2V+4P+3D,
    H1(Q_p*)=A+2V+3P+4D,
    H1(E_p(-1))=H1(Q_p*(-1))=3Wp+3S+6T.                         (15)

These matching characters are useful formal compatibility checks, not an identification of either pencil with the fixed HM maps.

## 5. Both maximal plateaux have length one

The first forward span in (13) is

    E_p^+=C0 O+U_7^10+U_1^8,

of rank10+8+2=20. Its next forward span is

    E_p^(++)=C0 O+U_8^10+U_2^8,

of rank10+9+3=22. Thus the original generic Gauss rank is three and the next is two.

For the opposite direction, duality reduces the calculation to Q_p* in its dual constant sum. Its three summands are the quotient curve line O(-18) in C0* O, U_3^10=S O(-7), and U_7^8=(Wp+T) O(-1). Their first rank gains are1,1,1. The first one has rank gain one because it is a nonconstant line curve; its raw image is saturated by the transpose argument above. The next gains are1,1,0. For the standard blocks this is (12). For the curve line, its value, first derivative and second derivative are generically independent: otherwise every three coefficient sections would have identically zero Wronskian, forcing its ten-dimensional coefficient system to have dimension at most two in characteristic zero. Equivalently, a nondegenerate characteristic-zero curve with at least three independent coordinate functions has a generic second osculating plane. This statement concerns generic osculation universally, without evaluation at a chosen point.

Therefore the two successive ranks in the dual direction are again three and two. In the original maximal-plateau convention this is exactly profile-(1,1). Higher osculating divisors are immaterial to these generic rank statements and are not claimed absent.

## 6. Parameter meaning and the remaining actual problem

Within the constructed family, different p in Omega give inequivalent constant inclusions over the fixed identity map of P(W). The canonical degree-minus-two block of E_p is F_p, and its actual first span is C0 O. Any equivariant constant equivalence therefore restricts to an equivalence of (8). Such an equivalence preserves the coefficient subspace C0->H0(O(18)), up to the scalar automorphism of the line quotient. Its A and V copies are fixed and its P copy is exactly p. Conversely the same p gives the same quotient system up to the allowed constant changes of basis, and the two standard residual blocks are fixed.

This is a one-parameter family of abstract solutions to the stated structural conditions, not a classification of all abstract c-d-f inclusions. In particular it does not show that arbitrary couplings between the three blocks can be removed. Neither a selected parameter nor an actual HM source instance has been constructed or tested. An exclusion of this source, if true for the fixed actual HM object, must use additional actual-module constraints not implied by the conditions verified here.
