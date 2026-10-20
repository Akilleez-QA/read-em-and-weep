# Exact sextic saturation and its canonical new channel

Work over C on P^4. Let F be the normalized Horrocks–Mumford bundle, B=End_0(F), and C the transverse union of its twenty-five disjoint evaluation-degeneracy lines. The determinant of F is O(-1), so Sym^2 F=B(-1). This note derives h^1B(-1)=5, h^2B(-1)=10, h^0 I_C(6)=40, and h^1 I_C(6)=5.

## 1. Equivariant symmetric monad

Write Q for the universal rank-four quotient on P(V), K=Lambda^2 Q*=Omega^2(2). The normalized HM monad is

A O(-1) -> W tensor K -> C_0 O,

where A=V_1, C_0=V_3, dim A=dim C_0=5, dim W=2. The maps are N-equivariant: this is the explicit construction in HM (1973), section 2, equation (2.3), after twisting by -3. The letter C_0 denotes a representation and is distinct from the union C of lines.

The graded symmetric square is quasi-isomorphic to Sym^2F. Its terms in degrees -2,-1,0,1,2 are

Lambda^2A O(-2), A tensor W tensor K(-1),
Sym^2(W tensor K) direct-sum A tensor C_0 O(-1),
W tensor C_0 tensor K, Lambda^2 C_0 O.

Local splitting of the original monad into its cohomology and contractible complexes proves this assertion in characteristic zero. Taking its symmetric square is functorial, so all induced spectral-sequence differentials are N-equivariant.

## 2. Bott calculation

The bundles O(-2), K(-1)=Omega^2(1), O(-1), and K=Omega^2(2) are acyclic. For the central term,

Sym^2(W tensor K) = Sym^2W tensor Sym^2K direct-sum Lambda^2W tensor Lambda^2K,
Sym^2K = S_(2,2)Q* direct-sum Lambda^4Q*,
Lambda^2K = S_(2,1,1)Q*.

Lambda^4Q*=O(-1) is acyclic. With Bott convention (0,lambda_1,lambda_2,lambda_3,lambda_4)+(4,3,2,1,0), the weight for S_(2,2)Q* is (4,5,4,1,0). A repetition makes it acyclic. For S_(2,1,1)Q*, the shifted weight is (4,5,3,2,0). Sorting requires exactly one adjacent transposition and subtracting rho gives (1,1,1,1,0). Thus its only cohomology is H^1 of dimension five. Since Lambda^2W has dimension one, the central term has only H^1, also dimension five.

Consequently the first hypercohomology page has exactly two nonzero entries: E_1^(0,1) of dimension five and E_1^(2,0)=Lambda^2C_0 of dimension ten. The only possible differential is d_2:E_2^(0,1)->E_2^(2,0).

## 3. Symmetry forces the transgression to vanish

HM (1973), printed pp67–68, proves Lambda^2 V = V_1 tensor W, with W the irreducible two-dimensional representation of N/H, and states the irreducibility criterion (2.2). Hence Lambda^2V is irreducible as an N-module. All four V_i are the Galois conjugates of V under theta:zeta_5->zeta_5^2. Applying theta^3 preserves irreducibility and gives Lambda^2V_3 irreducible, of dimension ten. Therefore the N-equivariant image of d_2 in Lambda^2C_0 is either zero or the whole ten-dimensional irreducible representation. Its source has dimension five, so the image must be zero.

The spectral sequence degenerates. There is only one surviving graded piece in each of total degrees one and two, so

h^1 B(-1)=5, h^2 B(-1)=10,

and all other cohomology of B(-1) vanishes. This argument never evaluates a selected HM matrix or a cohomology differential. It excludes a nonzero differential by symmetry rather than assuming its rank.

## 4. Saturation and restriction deficiency

Import PR463's exact Eagon–Northcott cohomology sequence

0 -> S_1 tensor H^0 I_C(5) -> H^0 I_C(6) -> D tensor H^2B(-4) -> 0,

where dim H^0I_C(5)=6 by PR458 and D is a constant determinant line. B is self-dual, so Serre duality identifies H^2B(-4) with H^2B(-1)*. It follows that h^0I_C(6)=30+10=40. In particular the quotient by the thirty independent linear multiples of the six quintics has dimension exactly ten.

Because C consists of twenty-five disjoint lines, h^0O_C(6)=25*7=175 and H^1O_C(6)=0. Since h^0O_P4(6)=210 and H^1O_P4(6)=0, the restriction exact sequence gives

h^1 I_C(6)=175-(210-40)=5.

Thus the lines impose exactly 170 independent conditions on sextics, leaving a five-dimensional restriction deficiency. This is a new exact correction beyond the Hilbert lower bound of PR463, not a restatement of six generators of the ideal sheaf as six generators of its saturated graded ideal.

## 5. A canonical new sextic summand

The saturation quotient is not merely ten-dimensional. The spectral edge isomorphism identifies H^2B(-1) with Lambda^2C_0 as N-modules. Equivariant Serre duality then identifies the new sextic quotient with D tensor (Lambda^2C_0)*. The canonical bundle linearization has no determinant correction because N is a subgroup of SL(V). Thus this quotient is irreducible of dimension ten.

HM (1973), Theorem 3.5, identifies the six invariant quintics with the direct sum of the two irreducible three-dimensional quotient representations U and U'. Accordingly the product submodule is

S_1 tensor H^0I_C(5) = V* tensor U direct-sum V* tensor U'.

Both fifteen-dimensional summands are irreducible as N-modules by HM (2.2): V* remains irreducible on H, while U and U' are irreducible on N/H. Neither can be isomorphic to the ten-dimensional saturation quotient. Therefore Hom_N(D tensor (Lambda^2C_0)*, S_1 tensor H^0I_C(5))=0.

Maschke's theorem provides an N-equivariant section of the saturation quotient, and the difference between any two such sections is in this zero Hom space. The section is therefore unique. Consequently H^0I_C(6) has a canonical N-equivariant decomposition into the thirty-dimensional quintic-product space and a new irreducible ten-dimensional space of sextics. This specifies an intrinsic new channel, not a selected generator or numerical basis. It does not identify its intersection with a fixed complete-intersection ideal (u,v).

## Dependencies and scope

- HM (1973), pp67–68, construction (2.3), irreducibility (2.2), and the description of V_i as Galois conjugates: https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf
- PR463, commit 8ec3631dcd6937e6cc7491d0200c1c78b5d21434: https://github.com/Akilleez-QA/read-em-and-weep/blob/8ec3631dcd6937e6cc7491d0200c1c78b5d21434/research/hm/order-four-residue/PROOF.md
- PR458, commit b46c3b48a8b10a7d0656fde247f2c3f258d1fd23: https://github.com/Akilleez-QA/read-em-and-weep/blob/b46c3b48a8b10a7d0656fde247f2c3f258d1fd23/research/hm/pair-interpolation/PROOF.md

The exact twist-minus-one calculation uses the primary equivariant monad and general Bott and representation theory, not an imported computational cohomology table. The sextic conclusion imports the pinned Eagon–Northcott sequence and prior quintic saturation result. No assertion about the value of the original fixed-pair Q4 or P5^(2,1), source membership, pure conditions, higher-order lifting, or algebraicity follows merely from these dimensions. This is mathematical verification, not formal proof-assistant checking.
