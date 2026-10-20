> Historical prerequisite proof from 15 October 2026; recorded checks are not new runs. See the common PUBLICATION-SCOPE.md.

# Direct finite-duality bridge for the four scalar detectors

## Result

Work over a characteristic-zero field k (in particular Q). Put X=(P1)^4 and let σ:X→P4 be the binary-product map. This note supplies a direct canonical trace bridge, not a splitting of σ_*O_X or a source evaluation. It applies separately to each of the four completed scalar carrier cocycles Y_d established in ../hm-four-detector-carrier-transfer-20261015/THEOREM.md.

There are six carrier opens, indexed in the fixed order (*,0,1,2,3,4). With coordinates [Z0:...:Z4] on P4, the carrier equations are H_j=Z_j^5−Z0 Z1 Z2 Z3 Z4 and H_*=Z0 Z1 Z3 Z4. Write V_b=D_+(H_b) and U_b=σ^−1(V_b). They cover: if a coordinate is zero, some H_j is nonzero; if all are nonzero, H_* is nonzero. These are affine opens, and all intersections are affine. Hence their Čech complexes compute coherent cohomology, also upstairs because σ is finite.

Use [X_i:Y_i] on factor i and x_i=X_i/Y_i on the all-finite chart. Define

q=X3² X4² Y1² Y2² ∈ H0(X,O(2,2,2,2)),
Δ=∏_{i<j}(X_i Y_j−X_j Y_i).

For each increasing carrier five-tuple A set

T_d,A = Alt(q Y_d,A)/Δ,
Alt(F)=∑_{π∈S4} sgn(π) π(F).

The permutation acts on the four coordinate pairs in the entire expression, including q and the numerator of Y; it leaves the carrier labels fixed. There is NO division by 24. The formula means a homogeneous rational coefficient for a section of O_P4(−5), after invariant descent. The theorem is

D_d = Tr_P4([T_d]) = Tr_X([q Y_d]),

where D_d is exactly the existing harmonic coefficient at (−1,−1,−3,−3). The global quotient T_d is regular on its carrier intersection and δT_d=0. No new discriminant poles occur; the certified owned carrier denominator exponents need not increase.

## 1. Geometry, frames, and the sign of the Jacobian

Define σ by Z_k=∑_{|S|=k}∏_{i∈S}X_i∏_{i∉S}Y_i. Thus σ*O(1)=O(1,1,1,1); on Z0≠0 its coordinates are e1,e2,e3,e4. The map is finite flat of degree 24. One proof covers the target, after algebraic closure, by effective divisors avoiding a point of P1. On each such chart it is k[e1,...,e4]⊂k[x1,...,x4], the elementary-symmetric finite free extension with Artin basis x1^a x2^b x3^c, 0≤a≤3, 0≤b≤2, 0≤c≤1. Flatness descends. This is also the previously established finite-flatness input in historical imported premise hm-symmetric-pushforward-status-20261015/AUDIT.md (see PUBLICATION-SCOPE.md); no new splitting choice is used.

Let Ω_i=Y_i dX_i−X_i dY_i, Ω_X=Ω1∧Ω2∧Ω3∧Ω4, and
Ω_P=∑_{j=0}^4(−1)^j Z_j dZ0∧...∧omit(dZj)∧...∧dZ4.
These are the standard homogeneous canonical frames: their coefficient degrees are (−2)^4 and −5. On Y_i=1 and Z0=1 their ordinary forms are dx1∧...∧dx4 and de1∧...∧de4. Direct differentiation gives

det(∂e_i/∂x_j)=∏_{i<j}(x_i−x_j)=Δ_aff,
σ*Ω_P=Δ Ω_X.

For a proof of the constant and sign, the determinant is alternating of degree 6, so is cΔ_aff. Its x1³x2²x3 coefficient is +1 (or induct on the number of variables by taking the highest x1 power); the same is true of Δ_aff. Thus c=+1. The homogeneous identity follows on the dense all-finite chart and hence globally. It proves all chart transitions, including infinity charts, without treating dx as a permutation-invariant frame. Ω_X acquires sgn(π) under factor permutation.

## 2. Identification with canonical finite trace

Finite duality identifies σ_*ω_X with Hom_O(σ_*O_X,ω_P4); the adjunction counit is evaluation at 1. On the generic étale locus the canonical identification sends a form F dx1∧...∧dx4 to the functional

b ↦ Tr_{k(X)/k(P4)}(b F/Δ_aff) de1∧...∧de4.

Consequently its counit is

Tr_σ(F dx1∧...∧dx4)
 = (∑_π π(F/Δ_aff)) de1∧...∧de4
 = Alt(F)/Δ_aff · de1∧...∧de4.

This is the ordinary field trace, the sum over 24 sheets. It is not a Reynolds average. Since canonical finite trace exists across ramification, the generic identity determines it everywhere: regular sheaves on the integral target inject into their generic fibers. The next section independently proves regularity of this particular quotient, so extension is not assumed on the strength of a formal pole cancellation.

References for the finite adjoint and its evaluation-at-1 counit: Stacks Project, https://stacks.math.columbia.edu/tag/0AWZ, especially Remark 48.11.5, and https://stacks.math.columbia.edu/tag/0AWG. The explicit Jacobian computation and alternating quotient here are additional arguments, not asserted to be supplied by those references.

## 3. Global ramification divisibility and invariant descent

On a carrier intersection choose the existing symmetric homogeneous clearing denominator

B_A=∏_{b∈A} σ*H_b^{n_b},

with the certified ownership exponents n_b (24 is an admitted common envelope). Let m=∑ n_b deg(H_b). Since qY_d,A is canonical, it has homogeneous coefficient N_A/B_A with N_A a polynomial of multidegree (m−2,m−2,m−2,m−2). This follows from regularity on U_A and the homogeneous localization description; if the actual pole certificate chooses smaller exponents, use those instead. A negative numerator degree forces that section to be zero.

B_A is symmetric. Thus Alt(qY_d,A)=Alt(N_A)/B_A. The polynomial Alt(N_A) vanishes whenever factors i and j represent the same point of P1: in local representatives with equal pairs the transposition fixes the variables and negates the alternant. Equivalently, reducing modulo the prime bracket X_iY_j−X_jY_i gives zero. One may check this on the dense portion Y_iY_j≠0 of that irreducible divisor; polynomial vanishing extends over its boundary. Each bracket therefore divides Alt(N_A) in the polynomial Cox ring. The six brackets are distinct irreducible, pairwise nonassociated elements of a UFD, so their product Δ divides Alt(N_A). This also covers multiple-collision intersections and infinity points; no separate assumption of disjoint branch divisors is needed.

Let M_A=Alt(N_A)/Δ. It is a polynomial, symmetric under S4, and has equal multidegree m−5 in each pair. Symmetric equal-multidegree polynomials of degree r≥0 descend to H0(P4,O(r)): geometrically P4=Sym4(P1), and algebraically the symmetric Segre section ring is the polynomial ring in Z0,...,Z4. To see surjectivity without a chosen generator splitting, dehomogenize to a symmetric polynomial in four x variables, each of degree at most r. For completeness, the usual lexicographic elimination proof preserves this degree bound: a sorted leading exponent a1≥a2≥a3≥a4 is removed by e1^(a1−a2)e2^(a2−a3)e3^(a3−a4)e4^a4, with total factor count a1≤r. Every monomial of that product still has each variable degree at most a1. Induction therefore writes the polynomial in elementary monomials having total elementary-factor count at most r; homogenize by Z0 to degree r. Injectivity holds on the dense Z0 chart. If r<0 then M_A=0.

It follows that T_d,A=M_A(Z)/∏H_b^{n_b} has degree −5 on P4 and is regular on V_A. In particular dividing by Δ adds no poles and no carrier powers. This argument retains the owned denominator factors; it makes no claim that forming Alt, exact division, or converting to Z coordinates is computationally free.

The canonical-frame identity in §1 and generic trace identity in §2 show that these locally regular quotients agree on all overlaps. This establishes global gluing, not merely affine symmetry.

## 4. Čech chain map and Serre trace

Multiplication by the global q is a sheaf map O_X(−4,−4,−4,−4)→ω_X. It commutes with restriction and hence with the ordinary ordered Čech differential. Canonical trace is likewise a sheaf map σ_*ω_X→ω_P4. Because U_A=σ^−1(V_A), it acts entrywise on the same ordered carrier tuple. Therefore

δT_d=Tr_σ(q δY_d)=0,

and boundaries map to boundaries. No permutation of carrier indices and no extra sorting sign occurs in this operation. Coordinate permutations in Alt must not be mistaken for permutations of Čech vertices.

For p:P4→Spec k, the counit for the composite pσ is the composite of the counits for σ and p. This follows directly from composition of adjunctions: evaluate a finite-duality Hom functional at 1, then apply the structure-morphism counit. On top cohomology it gives

Tr_X = Tr_P4 ∘ H4(Tr_σ).

Here ω_X[4] and ω_P4[4] are the compatible dualizing complexes. This is precisely the Serre-trace compatibility needed; no choice of the 1+11+11+1 splitting or its dual basis enters it.

## 5. Orientation and the exact selected coefficient

Fix the standard tensor Čech convention on X: each factor cover is (Y_i≠0, X_i≠0), its differential is restriction on the second open minus restriction on the first, and the factor order is 1,2,3,4. The normalized generator of H1(P1,ω_P1) is dx_i/x_i with trace +1. Tensoring these four traces gives

Tr_X([f dx1∧...∧dx4])=[x1^−1 x2^−1 x3^−1 x4^−1]f

in the harmonic tensor Čech quotient. The potential Koszul sign from interchanging the four degree-one Čech factors with the four one-form factors is (−1)^(4·3/2)=+1. Reordering factor coordinates by π introduces sgn(π) in both the top tensor Čech orientation and the wedge frame, consistently. The existing signed-staircase comparison is exactly the tensor orientation used in the four-detector theorem; this note does not replace it with an unsigned staircase.

In the finite line-bundle frame q=x3²x4². Thus for every class y∈H4(X,O(−4,−4,−4,−4)),

Tr_X(qy)=[x1^−1 x2^−1 x3^−3 x4^−3]y.

This is an identity of cohomological linear functionals. It does not prescribe a Laurent expansion of each rational carrier entry separately. A representative must first be interpreted through a valid Čech comparison or, equivalently, through the finite trace class constructed here.

On P4, the ordered coordinate cover (Z0≠0,...,Z4≠0) has normalized class Ω_P/(Z0 Z1 Z2 Z3 Z4) of trace +1. This fixes the target convention. The local generic formula uses the same orientation de1∧...∧de4. There is no sign or multiplicity left undetermined.

## 6. Small universal normalization controls

The companion check.py uses only manufactured polynomials and verifies:

- the elementary Jacobian is +Δ_aff;
- Alt(x1³x2²x3)/Δ_aff=1;
- Alt(Δ_aff)/Δ_aff=24;
- several alternants are polynomial multiples of Δ_aff with symmetric quotient;
- the all-infinity projective coordinate transition has determinant +e4^−5;
- all 24 tensor/wedge permutation signs cancel and all 81 harmonic monomials pair with q exactly at the requested target.

The first two trace examples distinguish canonical trace from the incorrect average and determine its affine sign. The harmonic tests control the tensor pairing, not production carrier values. The proofs above, rather than these finite tests, establish the general gluing and Serre-trace identity.

## 7. Remaining computational boundary

This closes the direct mathematical bridge from six completed scalar carrier sections to the exact current detector on P4. It does NOT evaluate any Y_d, give their coefficients, prove a detector nonzero, establish completeness of four detectors, or authorize a production run. An implementation still needs the exact six-section source provider, an exact alternating-division/invariant-descent action, and a P4 top-cohomology trace procedure with acquisition, arithmetic, bit-width, coefficient support, and peak-live-memory accounting. Replacing 24 source-coordinate substitutions with a symbolic functional is not by itself a resource saving.
