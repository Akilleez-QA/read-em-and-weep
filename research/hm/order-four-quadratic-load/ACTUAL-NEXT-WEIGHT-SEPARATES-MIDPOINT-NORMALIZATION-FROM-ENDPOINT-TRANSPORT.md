# Next-weight midpoint normalization and endpoint transport are different problems

## Results and scope

The solved weight-four affine R2 family does not solve weight eight. Three precise interfaces remain distinct:

1. The midpoint weight-four nilpotent mismatch Z4 has coefficient bundle `E4(-6)`. Its invariant cohomology class vanishes, and it admits a unique compatible partial normalization that also kills its degree-twelve scalar square coefficient. This leaves the nonzero Z0/chi8 unchanged.
2. The endpoint transition changes that calculation by an explicit first-order mismatch and a nonzero-allowed harmonic term depending on the **complete lowest eta**, not just its diagonal.
3. The weight-four connection correction K4 lies in E4. Its action on the weight-twelve tangent first error fits an exact coefficient sequence with quotient `V O(4)`. The actual full first-error section of that quotient has not been computed here.

All coefficient bundles below are the marked homogeneous/associated-graded bundles. Extraction from an arbitrary actual full lift requires the lower-weight terms and inhomogeneous transport to be retained. No global endpoint nilpotent or third-neighborhood midpoint is assumed.

## 1. Two different coefficient sequences

Let E4 be the weight-four coefficient bundle of `B_Q(4)` established in the preceding coefficient theorem. Then

`0 -> Wprime O(-1) -> E4 --tr(n·)--> Sym12(Wprime) O -> 0`.     (1)

K4 has this physical twist four. In contrast Z4 is a q² coefficient of N, whose physical twist is two. Thus Z4 has physical twist minus two, and its bundle is

`J4=E4(-6)`.

Consequently

`0 -> Wprime O(-7) -> J4 --tr(n·)--> Sym12(Wprime) O(-6) -> 0`. (2)

The entry degrees of both matrices are `(4,2;6,4)`. For J4 their coefficient lines are O(-4), O(4), O(-12); these are the lines of E4 shifted by minus six, not the lines of J_eta. The tangent preimage is in G(-4), with lower component degree one and line `O(-5/2-4-1/2)=O(-7)`.

In particular `H0(J4)=0`. Moreover

`H1(Wprime O(-7))^G=(Wprime tensor Sym5 W)^G=0`,

because Sym5 W is the irreducible six-space. Thus the map

`H1(J4)^G -> H1(Sym12(Wprime) O(-6))^G`                     (3)

is injective, indeed an isomorphism since the base is a line. The universal character identity

`Sym12(Wprime)=1+V+P4+D5`

shows that both spaces in (3) have dimension one. This dimension alone does not evaluate a Z4 class.

## 2. The actual MIDPOINT Z4 class and its simultaneous normalization

Use the actual oriented Serre frames normalized in `MIDPOINT-HESSIAN-SYMBOL-MATCHING-BY-FULL-FRAME-COVARIANCE.md` and the already checked affine-transport proof. In these frames the ordinary nilpotent is the weight-eight matrix of the marked homogeneous cubic/quintic pair. The remaining ordinary conic and Koszul stabilizer transitions start at chain weight eight and stabilize that pair. They cannot mix Z0 or Z2 into Z4. This is the normalized-frame comparison needed here; it is not a claim that every arbitrary regular frame preserves homogeneous degrees.

The genuine midpoint first-normal pair gives the exact local relation

`N_j-Ad(P_hat)N_i=q² Z_ij mod q³`.

All actual P1 terms and their harmonic products remain in Z. The trace-free square identity is exact:

`chi_j-chi_i=tr(n_j Z_ij)`.

Because n has weight eight in these frames and ordinary transition mixing starts at eight, its degree-twelve component is exactly

`delta chi12=tr(n8 Z4)`.                                   (4)

There is no omitted contribution from Z0 times a weight-twelve component of n: the normalized ordinary n has no such component. Higher first-normal T coefficients and every P1 correction are already included in the **complete local chi12**. They must not be discarded when constructing a representative.

Likewise Z4 is a genuine coefficient cocycle. An arbitrary lifted bundle transition can have a q² triple defect C of minimum regular adjoint weight minus two. Its action on n starts at weight six, strictly above four. Ordinary weight-eight mixing also cannot enter this coefficient. Thus no global third-neighborhood bundle is needed for this cocycle statement.

The actual pair is equivariant, so its class is invariant. Equation (4) makes its image under (3) a coboundary in the entire trace target, not merely zero modulo the square ideal. Injectivity therefore proves

`[Z4]=0`.

There is a unique compatible local cochain S4 with

`delta S4=-Z4`,                                             (5)

because H0(J4)=0. Its equivariance follows from uniqueness. Taking traces in (5) and using (4), the section `tr(nS4)+chi12` is globally defined in `Sym12(Wprime)O(-6)`. That bundle has H0=0. Hence

`tr(nS4)=-chi12`.                                          (6)

Adding the local term q²S4 therefore kills both the weight-four mismatch and the degree-twelve scalar square coefficient. This is only a **partial midpoint normalization**. It leaves the already proved nonzero weight-zero mismatch and scalar degree-eight residue untouched, so it does not construct a global N2 or a square-zero third-neighborhood lift.

### 2.1 The stronger matched midpoint gauge

The matching source supplies more than a lowest-degree comparison. Section 4 of `MIDPOINT-HESSIAN-SYMBOL-MATCHING-BY-FULL-FRAME-COVARIANCE.md` proves that every corrected local Hessian matrix differs from the actual midpoint nilpotent by a normal commutator, removable by an identity-mod-q local conjugation. Section 1 of `ACTUAL-MIDPOINT-ABSOLUTE-SECTION-FOR-THE-FOURTH-SQUARE-INPUT.md` then supplies its complete harmonic expression. Thus actual local midpoint frames may be chosen with **exact** first-normal matrix `L(n8)+qL(T4)`, not merely its lowest coefficient.

This does not make the actual transitions literally harmonic marked transitions. Their ordinary conic/stabilizer corrections start at weight eight. Write the extra first-normal transition as I+qQ after those ordinary transitions. Their action on T first differs from the homogeneous transport at weight twelve. Compatibility with the exact local T4 therefore forces the weight-minus-two, zero, and two components of Q to centralize n. A regular trace-free centralizer is a regular scalar multiple of n; none of these weights allows that. Hence Q begins at weight four (a scalar matrix part has no adjoint effect).

With the displayed local representatives (and no added local q² term), chi has only degree eight, and the weight-four coefficient of the q² mismatch vanishes. This assertion is only about Z4: an arbitrary q² transition repair C of minimum regular adjoint weight minus two contributes [C,n8] starting at weight six, so no absence of all intermediate mismatch weights is asserted. In particular

`chi12=0`, `Z4=0`, `S4=0`.

The ordinary higher transitions have not vanished: their second harmonic products, and the permitted Q4, can first contribute to Z8. Independently chosen q² transition repairs can already contribute to Z6, but cannot change Z4. Sections 1–2 provide the gauge-independent partial normalization if other regular first-normal frames are used. Z4 is therefore **not independent missing midpoint data**. None of this fixes the connection's allowed global K4 coefficient or the full first-error representative.

## 3. Why the endpoint does not inherit Section 2

Fix the comparison convention that the endpoint transition is `(I+q eta0)` times the midpoint transition. Here eta0 is the complete lowest actual normal cocycle, including its lower quadratic entry, with the retained actual scale relative to eta_ap. Keep the midpoint local N matrices; do not pretend they define a global endpoint N.

The q² weight-four coefficient of harmonic conjugation by I+q eta0 is

`Omega4(eta0)=[eta0,T4]+B1(eta0,n8)-B1(n8,eta0)`.            (7)

The quadratic eta0 terms have weight eight in the q² coefficient and are not part of (7), but remain relevant at later weight. Therefore the endpoint mismatch starts already at first order:

`D1,8=-[eta0,n8]`,

`Z4,end=Z4,mid-Omega4(eta0)`                                (8)

for this ordered comparison. Reverse arrows reverse the corresponding transported Cech signs.

For a general first-order discrepancy D1, squaring the two local lifts adds

`tr(T D1)+tr B1(n,D1)+(1/2)tr(D1²)`

to the second-normal scalar comparison. Here T denotes the transported SOURCE first-normal coefficient, not the target coefficient; their weight-four pieces agree in the comparison being used. At degree twelve, the quadratic term is absent but the first two terms survive:

`delta chi12=tr(n8 Z4)+tr(T4 D1,8)+tr B1(n8,D1,8)`.          (9)

Thus the midpoint argument based on (4) cannot be copied to the endpoint. The universal identity

`tr(n8 Omega4)+tr(T4[eta0,n8])+tr B1(n8,[eta0,n8])=0`        (10)

checks the compatibility of (7)–(9), including both harmonic orders. Formula (7) identifies one forced, eta-controlled transition contribution. It does not identify every actual local adjoint/source correction or restore global endpoint nilpotent gluing.

The first-normal connection law similarly forces the eta-dependent affine change

`delta K4 = [eta0,A0]-H0Deta0-H0rho eta0`

`         =-(H0D+ad A0+H0rho)eta0`,                         (11)

when isolating this endpoint-versus-midpoint transition leg. The normal-line term follows from differentiating q eta0. Other already specified lower-data affine terms must be included in the full transition equation. H1(E4)=0 permits splittings of a genuine E4 cocycle, but the ambiguity is

`H0(E4)=Sym12(Wprime)`,

not zero. Eta alone therefore does not specify the actual K4 zero-cochain; its actual section action, trace/source normalization, and all prescribed affine corrections must also be supplied.

### 3.1 An admissible midpoint K4 coefficient choice, not the full operator

In the matched midpoint frames from Section 2.1, the same gap argument applies to the adjoint connection. Its leading cone coefficient A0 has weight four and its known first-normal coefficient K0 has weight zero. Ordinary conic/stabilizer corrections begin at eight. Their conjugation, their harmonic B1 terms with A0, and the term H1·D(stabilizer) all first affect the first-normal connection at weight eight. Likewise the permitted midpoint Q4 contributes `-[H0(D+rho)+ad A0]Q4` at weight eight. None forces weight four.

The already checked root/determinant correction has weight zero. A scalar first-normal frame Q0 could contribute a scalar weight-four connection term, but this is removed by the prescribed determinant connection and trace-free operation, not retained as an adjoint K4. Thus K4=0 is an admissible midpoint **vertex coefficient** choice through this weight.

This does not identify the prescribed full actual operator with that choice. An arbitrary coefficient in H0(E4) may be added at this associated-graded stage, but it is not a global actual operator ambiguity: the following conic comparison rules out any nonzero such coefficient coming from a global actual adjoint section. At the endpoint the eta-dependent affine term (11) must still be solved.

### 3.2 Global conic regularity removes all thirteen homogeneous adjoint ambiguities

Every global actual section K of B_Q(4) has zero marked weight-four coefficient.

Indeed its weight-four coefficient is a global section of E4. The homogeneous marked transition preserves weighted degree, and the ordinary conic/Koszul correction starts at eight. Mixing into four would therefore require a regular adjoint of weight minus four, which does not exist (the regular minimum is minus two). This is a coefficient statement for sections on Q, not a claim of a homogeneous subbundle for arbitrary higher coefficients.

The scalar tr(NK) is a global section of I_Z²(6). Since N is exactly the marked homogeneous n8 in the vertex Serre frames, its positive-cover degree-twelve component is precisely tr(n8 K4), a section of Sym12(Wprime) O_L. On the other hand, H0(O_Q(6)) is the degree-six quadric coordinate ring. Its pure-positive summand is the space of sextics on the positive rank-three quadratic cone, canonically Sym12(Wprime). Restriction of that summand to the fixed conic C is an isomorphism onto H0(C,O_C(12)); every term with a negative coordinate vanishes on C. There is no cancellation between a pure-positive term and the mixed terms upon restriction. Since tr(NK) lies in I_Z²(6), its restriction to C is zero, so its degree-twelve component is zero. Exactness of (1), together with H0(Wprime O_L(-1))=0, now gives K4=0.

Consequently two global actual first-normal operators with the same symbol and scalar/determinant normalization cannot differ at K4 when their difference is a global B_Q(4) section. Conic regularity selects at most one member of the thirteen-dimensional homogeneous affine family. This proves uniqueness, not existence or the value of that member. In particular the locally admissible midpoint choice K4=0 must still be compared with the full prescribed operator; the endpoint eta-forced affine family is not thereby set to zero.

## 4. Exact K4 / weight-twelve tangent-first-error interface

A tangent R1 of diagonal cover degree twelve lies in the weight-twelve coefficient of G(4). Denote this marked coefficient bundle by E12. Its components have degrees seven and nine, with coefficient lines O(5), O(-3), so it retains the nonsplit sequence

`0 -> Sym9(Wprime) O(-3) -> E12 -> Sym7(Wprime) O(5) -> 0`.  (12)

There is a natural exact sequence

`0 -> E4 --K↦K sigma--> E12 -> V O(4) -> 0`.                (13)

Here is a direct proof, independent of a guessed duality identification. The wedge maps on E12 and E4 have common target `Sym12(Wprime)O`:

`sigma wedge(K sigma)=-tr(nK)`.

Both are onto: the degree-twelve quotient of the regular-pair ideal and of its square is zero. The first kernel is `sigma·Sym4(Wprime)O(2)`, and the second kernel is `tau(0,ell)`, with `ell` in Wprime O(-1). On these kernels,

`tau(0,ell) sigma=sigma·f ell`.

Their cokernel is therefore

`Sym4(Wprime)O(2) / f·Wprime O(-1) = V O(4)`,

by the established actual cubic coefficient sequence, the fourfold twist of `UNIVERSAL-CUBIC-EVEN-DEFECT-QUOTIENT-IS-TRIVIAL-V.md`, equation (1). Finally the map K↦K sigma has no kernel at weight four: a stabilizer multiple of n would require a negative-degree scalar. This proves (13), including its global coefficient lines.

The bundle ranks/degrees are `(18,10)=(15,-2)+(3,12)`. Since H1(E4)=0, every global section of V O(4) lifts to E12. In fact

`H0(E12)` has dimension 28, and `H1(E12)=0`.

This does not determine the actual section of V O(4). One must first establish a full, compatibly tangent first-error representative; its degree-eight residue does not specify its degree-twelve coefficient.

There is also an actual-filtering warning: a chain-weight-eight Koszul/conic stabilizer can mix a lower weight-four G(4) component into weight twelve. Thus literal extraction of E12 from a full actual G(4) lift requires that lower component to be tracked or its absence to be proved for the specified lift. Sequence (13) is not permission to replace an arbitrary full lift by its homogeneous coefficient.

## 5. What is still required at R2 weight eight

The midpoint normalization (5) and the forced eta terms (7),(11) are useful interfaces, not the complete next division. Potential surviving weight-eight terms include:

- `L2(Z4)` and harmonic transport `F_P(R1,12)`;
- `[K4,T4]`, `[K0,T8]`, and `B1(K4,n8)`;
- the action of a weight-zero first-normal transition on R1,8;
- allowed local weight-zero second-normal connection/symbol coefficients acting on n8;
- all lower-coefficient mixing under the exact actual conic/stabilizer transport.

The full source and lower-error subtractions must be retained, as must the difference between the midpoint pair and the endpoint adjoint problem. No assertion about all R2 or beta4 follows from the coefficient sequences or the partial midpoint normalization alone.

## 6. Full first-mismatch error law at the endpoint

For clarity work first in a common physical-q and tensor frame. Write a lifted transition as `P_hat=(I+qQ)L(P0) mod q²`. Set

`N_j-Ad(P_hat)N_i=qL(D1)+q²L(Z) mod q³`.

Retain the full first-normal operator data

`Hhat=L(H0)+qL(H1)`, `Ahat=L(A0)+qL(K1)`,

`Lambdahat=L(Lambda0)+qL(Lambda1)`.

Define

`Lr(W)=H0DW+[A0,W]+(r H0rho-Lambda0)W`,

and

```
C1(W) = H1(D+rho)W + [K1,W] - Lambda1 W
        + B1(H0,(D+rho)W)
        + B1(A0,W)-B1(W,A0)-B1(Lambda0,W).
```

For arbitrary P0 set Q0=P0^-1 and I1=-Q0 B1(P0,Q0). The inverse of L(P0) is L(Q0)+qL(I1) modulo q², so the general transport term in (14) is

`F_P0(R)=B1(P0,R)Q0+B1(P0R,Q0)+P0 R I1`.

For the marked homogeneous triangular/root P0 the harmonic inverse is exact, I1=0, and this reduces to the two-term formula used previously. Full ordinary stabilizers start at weight eight; their inverse repairs and their additional first-error transport terms start above the retained weight eight because R1 starts at eight. Thus the two-term formula suffices at that retained weight, but is not asserted globally for arbitrary full ordinary P0.

All D actions here retain their physical coefficient-line connections. If only first-normal operator compatibility has been supplied, denote its remaining q² transport defect by `h2 D+ad a2-lambda2`. Its contribution on n is `Op2(n)=h2 Dn+[a2,n]-lambda2 n`. This is not presumed zero. Exact q-adic expansion gives

```
R1,j = Ad(P0)R1,i + L1(D1),
R2,j = Ad(P0)R2,i + F_P0(R1,i)
        + [Q,Ad(P0)R1,i] + L2(Z) + C1(D1) + Op2(n).
```                                                       (14)

The normal first-error transport commutator `[Q,Ad(P0)R1]` is essential at the next weight. It could be ignored in the prior weight-four theorem by degree, but for Q0=eta0 and R1,8 it has weight eight. No vanishing of that term is inferred from a residue calculation.

For the matched midpoint-versus-endpoint comparison, `D1,8=-[eta0,n8]` and `Z4=-Omega4(eta0)`. Therefore the forced eta-dependent contribution at weight eight includes exactly

`[eta0,R1,8] - L2(Omega4(eta0)) - C1([eta0,n8])`,            (15)

where C1 uses the weight-zero pieces H1, K0, Lambda1. This retains the derivative of q, both ordered harmonic commutators, and the complete scalar term. The separate `F_P0(R1,12)` contribution still requires the actual full first-error coefficient. The operator defect Op2 also survives unless separately controlled: its weight-zero a2 component can contribute `[a2_0,n8]` at weight eight. Formula (15) isolates the nilpotent/first-normal-transition contribution, not this additional operator defect. Any specialized choice such as the prescribed harmonic scalar with Lambda1=0 must be applied explicitly, not built silently into (14).

Independently, an actual K4 changes the local q² error by

`[K4,T4]+B1(K4,n8)-B1(n8,K4)`

at weight eight, while its first-error action is `[K4,n8]` at weight twelve. Hence (14)–(15) do not eliminate the E12 reconstruction problem in Section 4. They isolate a forced transition leg rather than compute the entire next error.

On overlaps `q_j=u_ij q_i`, the coefficient of normal order r acquires `u_ij^-r` in addition to its ordinary tensor transition, and `rho_j=rho_i+Dlog u_ij`. The r*rho terms in Lr and the `(D+rho)` terms in C1 are necessary for this covariance. No claim is made that choosing a local equation kills the derivative of the fixed global normal section.

## Verification

Run `python verify_next_weight_midpoint_endpoint_interfaces.py`.

It checks exact binary-group characters, coefficient twists/ranks/degrees, the wedge/trace diagram and its sign, all relevant mixing bounds, and (7),(10) for unrestricted abstract homogeneous coefficients, retaining the entire lower eta entry. No actual source parameter is assigned, and no actual-instance matrix or rank is evaluated. All preceding frozen files are unchanged.
