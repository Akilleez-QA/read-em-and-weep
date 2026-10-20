# The last syzygies from the HM line Rao module

Work over C. Let F be the normalized HM bundle on P(V)=P^4, B=End_0(F), and C the union of its twenty-five disjoint transverse evaluation-degeneracy lines. Put S=Sym(V*), I=I_C, and M_d=H^1(I_C(d)). Betti indices below refer to I, not S/I.

We prove that the parameters left open in PR470 are b=1 and a=0. In particular the last free module is S(-10)^6 direct-sum S(-11)^5, and there is exactly one degree-ten second syzygy. A rank-one argument in the dual complex then excludes all degree-nine first syzygies and determines the complete minimal Betti table.

## 1. Equivariant conventions and pinned premises

Use the normalizer N in SL(V), its Heisenberg subgroup H, and quotient G=SL_2(F_5). Write A=V_1 and A*=V_3 for the two five-dimensional Galois conjugates used in the normalized monad, W,W' for the two two-dimensional quotient representations, U=Sym^2W, T_4=W tensor W', and R_6 for the irreducible six-dimensional quotient representation. Determinants of W,W' and V are trivial. The four-dimensional section representation V_s=H^0(F(3)) is T_4 and D=det V_s is trivial.

The identities used below are Lambda^2 V=A tensor W, Lambda^2 A*=V tensor W', and T_4 tensor W=W' direct-sum R_6. The latter follows from W tensor W=1 direct-sum U and U tensor W'=R_6. They are the HM normalizer identities, not chosen matrix calculations.

Import the exact Eagon--Northcott complex

0 -> D tensor B(-5) -> Lambda^3 V_s tensor F(-2) -> Lambda^2 V_s tensor O -> I_C(5) -> 0.

Import h^0 I_C(5)=6 and the isomorphism Lambda^2 V_s -> H^0 I_C(5); h^1 I_C(6)=5; H^1 I_C(d)=0 for d>=7; and PR470's constrained minimal resolution. Import PR455's structural bound h^2 B<=2, proved there by a universal exterior-image estimate and Heisenberg symmetry. The precise pins appear below.

## 2. Exact untwisted endomorphism cohomology without evaluating a differential

Let Q be the universal rank-four quotient and K=Lambda^2 Q*=Omega^2(2). The normalized monad is A O(-1) -> W tensor K -> A* O. Twist its graded symmetric square by one to compute B. All its terms have no positive cohomology, as proved by Bott in PR455. For clarity the central Schur summands S_(2,2)Q*(1) and S_(2,1,1)Q*(1) have repeated shifted weights (5,5,4,1,0) and (5,5,3,2,0); Lambda^4 Q*(1)=O. The remaining terms O(-1), K, K(1), O(1) have the stated elementary cohomology.

Thus B is computed on global sections by the three-term N-complex in degrees zero, one and two:

U direct-sum End(A) -> W tensor A* tensor Lambda^3 V* -> Lambda^2 A* tensor V*.

Its dimensions are 28,100,50. Since det V is trivial, Lambda^3 V*=Lambda^2 V=A tensor W. The middle representation is End(A) tensor (1 direct-sum U), and the last is End(V) tensor W'. Taking H-invariants therefore gives

1 direct-sum U -> 1 direct-sum U -> W'.

The final arrow is zero by inequivalent irreducible G-types. Invariants are exact because H is finite in characteristic zero. Consequently H^2(B)^H=W'. The imported bound h^2 B<=2 now proves the exact N-isomorphism H^2(B)=W'.

Stability of F implies H^0(B)=0. Hence the first arrow in the invariant complex is injective and, since both spaces have dimension four, an isomorphism. Thus H^1(B)^H=0. The global complex has no higher terms, and its Euler characteristic is 28-100+50=-22. Therefore h^1(B)=24.

The center of H acts trivially on B. The quotient G acts transitively on the twenty-four nontrivial characters of H/Z(H). Since H^1(B) has dimension twenty-four and no invariant part, each of those characters occurs exactly once. This makes H^1(B) irreducible under N: a nonzero N-submodule contains an H-weight space and therefore the entire orbit. No deformation-obstruction map or smoothness statement is inferred from these cohomology groups.

## 3. The two top pieces of the Rao module

Let K_5 denote the image of Lambda^3 V_s tensor F(-2) in Lambda^2 V_s tensor O. The second short exact sequence of the Eagon--Northcott complex and the imported quintic isomorphism give H^1(K_5)=0 and M_5=H^2(K_5). The primary HM cohomology gives H^2(F(-2))=W and H^3(F(-2))=0. Equivariant Serre duality, B*=B and N contained in SL(V) give

H^2 B(-5)=H^2(B)*=W', and H^3 B(-5)=H^1(B)*.

The first short exact sequence now yields

0 -> W' -> Lambda^3 V_s tensor W -> M_5 -> H^1(B)* -> 0.

Here Lambda^3 V_s=T_4 and T_4 tensor W=W' direct-sum R_6. The injection from W' fills that unique summand. Thus M_5 is the direct sum of its H-invariant part R_6 and a twenty-four-dimensional N-irreducible nontrivial-character part. The splitting into invariant and nontrivial H-characters is canonical. Its dimension is thirty, consistently with 25(6)-(126-6)=30.

Similarly, twisting Eagon--Northcott by one, the primary vanishings H^2(F(-1))=H^3(F(-1))=0 give M_6=D tensor H^3 B(-4)=H^1 B(-1)*. We record the equivariant refinement of PR464's five-dimensional calculation: its surviving H^1 central summand is Lambda^2 W tensor H^1(S_(2,1,1)Q*). Bott gives dominant weight (1,1,1,1,0), hence Lambda^4 V*=V, since det V=1. The only possible transgression vanishes as proved in PR464. Therefore H^1 B(-1)=V and

M_6=V*.

These are canonical N-module identifications; dimension five alone would not suffice for the next step.

## 4. Actual multiplication and the Rao socle

For d>=0, the disjoint-line description identifies the graded section module with

L=direct-sum over the twenty-five lines l of S/I_l.

Indeed restriction on each line identifies (S/I_l)_d with H^0(O_l(d)), compatibly with multiplication. For d<0 both section spaces vanish. The restriction sequence on P^4 identifies the entire Rao module M with coker(S -> L), because H^1(O_P4(d))=0 for every d. Each S/I_l is generated in degree zero, so its quotient M is generated in degree zero. In particular S_1 M_5=M_6, which is nonzero.

Consider the adjoint of actual multiplication:

mu: M_5 -> S_1* tensor M_6 = V tensor V* = End(V).

The H-invariant part of the target is the trivial one-dimensional G-representation. There is no G-map R_6 -> 1, so mu kills the invariant R_6 in M_5. The remaining target is the sum of the twenty-four nontrivial H-characters, once each, hence N-irreducible by the same orbit argument as above. Since multiplication is surjective onto M_6, its adjoint is nonzero. It follows that mu maps the nontrivial twenty-four-dimensional summand of M_5 isomorphically onto the corresponding target summand. Thus

Soc(M)_5=R_6, of dimension six.

All of M_6 is socle, since M_7=0. Hence dim Soc(M)_6=5. This argument establishes the actual multiplication kernel through equivariance and generation; it does not replace a selected multiplication by an arbitrary map of matching dimensions.

## 5. Local duality determines b

Put R=S/I. Saturation identifies H^1_m(R)=M. Graded local duality over the five-variable polynomial ring gives

Ext^4_S(R,S(-5))=M^vee,

where (M^vee)_e=Hom_C(M_{-e},C). PR470 proves pd(I)=3, hence pd(R)=4. If G is the minimal resolution of R, its last dual differential has cokernel Ext^4. Its image lies in m Hom(G_4,S(-5)) by minimality. Therefore minimal generators of Ext^4 are precisely those of Hom(G_4,S(-5)). Dualizing M identifies their degree 5-j multiplicity with dim Soc(M)_(j-5). Since G_4 is the third syzygy module of I,

beta_(3,j)(I)=dim Soc(M)_(j-5).

In particular beta_(3,10)=6 and beta_(3,11)=5. Comparing with PR470's beta_(3,10)=5+b proves b=1, and its Hilbert-numerator relation gives beta_(2,10)=1.

The remaining minimal resolution consequently has free modules

F_0=S(-5)^6 direct-sum S(-6)^10,
F_1=S(-7)^10 direct-sum S(-8)^40 direct-sum S(-9)^a,
F_2=S(-9)^(45+a) direct-sum S(-10),
F_3=S(-10)^6 direct-sum S(-11)^5,

with only a>=0 still undetermined. Equal shifts in adjacent modules are not canceled: minimal differentials between them have zero constant blocks. This proves a nonzero degree-ten second-syzygy term rather than guessing that all possible overlapping shifts disappear.

## 6. A rank-one exclusion resolves the final parameter

Continue with the minimal resolution G of R and its dual complex C^i=Hom_S(G_i,S(-5)). The preceding calculation gives

C^1=S^6 direct-sum S(1)^10,
C^2=S(2)^10 direct-sum S(3)^40 direct-sum S(4)^a,
C^3=S(4)^(45+a) direct-sum S(5),
C^4=S(5)^6 direct-sum S(6)^5.

The outgoing differential restricted to the rank-one summand S(5) of C^3 is nonzero. One way to see this directly is degree -5: C^4 has dimension 6+5*5=31 there, while Ext^4=M^vee has dimension dim M_5=30. Therefore the one-dimensional C^3_{-5} has nonzero image. As S is a domain and C^4 is free, this restriction S(5) -> C^4 is injective.

A degree -4 basis generator of S(4)^a in C^2 can map into C^3 only through the S(5) summand with linear coefficients: a map into S(4) would have constant coefficients, forbidden by minimality. The composite with C^3 -> C^4 is zero. Injectivity on S(5) therefore forces the image of each such generator to vanish.

On the other hand Ext^2_S(R,S(-5))=0. This follows either from grade(R)=3 over the polynomial ring or from local duality and H^3_m(R)=0 because dim R=2. There is no degree -4 component in C^1. Thus exactness at C^2 in degree -4 forces its kernel to be zero, contradicting any nonzero S(4)^a generator. Hence a=0.

The minimal resolution of I has the complete free-module profile

0 -> S(-10)^6 direct-sum S(-11)^5
  -> S(-9)^45 direct-sum S(-10)
  -> S(-7)^10 direct-sum S(-8)^40
  -> S(-5)^6 direct-sum S(-6)^10
  -> I -> 0.

The arrows here denote the existing minimal differentials; this determines all graded Betti numbers, not explicit coefficient matrices. The simultaneous degree-ten terms are genuine and do not cancel in the minimal resolution. The proof resolves the two numerical dependencies in PR470 without evaluating a syzygy differential.

## Pinned dependencies and scope

- HM (1973), equivariant monad, normalizer identities, primary cohomology and transverse line geometry: https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf
- PR455, 8cbbe482ee50c35d52ffcdf3efb837fa8cf96af4, the structural bound h^2 B<=2 and acyclic twist-one symmetric monad: https://github.com/Akilleez-QA/read-em-and-weep/blob/8cbbe482ee50c35d52ffcdf3efb837fa8cf96af4/research/hm/twist-one-structural-vanishing/PROOF.md
- PR458, b46c3b48a8b10a7d0656fde247f2c3f258d1fd23, quintic saturation: https://github.com/Akilleez-QA/read-em-and-weep/blob/b46c3b48a8b10a7d0656fde247f2c3f258d1fd23/research/hm/pair-interpolation/PROOF.md
- PR463, 8ec3631dcd6937e6cc7491d0200c1c78b5d21434, Eagon--Northcott complex: https://github.com/Akilleez-QA/read-em-and-weep/blob/8ec3631dcd6937e6cc7491d0200c1c78b5d21434/research/hm/order-four-residue/PROOF.md
- PR464, a091db646c2ad9ba73d0893f4d92ff54891aaf0c, twist-minus-one cohomology: https://github.com/Akilleez-QA/read-em-and-weep/blob/a091db646c2ad9ba73d0893f4d92ff54891aaf0c/research/hm/exact-sextic-saturation/PROOF.md
- PR466, b378990352d5f9bba3aaed27a0b6e0ff4683e15c, regularity and high-degree Rao vanishing: https://github.com/Akilleez-QA/read-em-and-weep/blob/b378990352d5f9bba3aaed27a0b6e0ff4683e15c/research/hm/exact-septic-saturation/PROOF.md
- PR470, ad0498d7f88141c9e5b5ef8fa9cb2c2e5dc98183, constrained minimal resolution: https://github.com/Akilleez-QA/read-em-and-weep/blob/ad0498d7f88141c9e5b5ef8fa9cb2c2e5dc98183/research/hm/minimal-linear-syzygies/PROOF.md

This is an authored structural proof requiring mathematical review, not formal proof-assistant checking. It uses no selected actual HM/source-instance evaluation, numerical matrix/rank, coefficient search, generator/checker or large computation. Explicit coefficient differentials, original fixed-pair intersections, actual-source membership, pure conditions, higher-order lifting and algebraicity are not settled.
