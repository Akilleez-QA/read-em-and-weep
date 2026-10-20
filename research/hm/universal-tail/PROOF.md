# Universal Rao contraction and the saturated HM syzygy tail

Work over C. Let S=Sym(V*), dim V=5, and let I be the saturated ideal of the twenty-five disjoint HM evaluation-degeneracy lines C in P(V). Put M_d=H^1(I_C(d)). All Betti indices and free modules F_i below refer to I, not S/I.

## 1. Pinned input and actual contraction

Import PR471 at a38c45f91c3f29134c6c8d0a2c51d5e8d1e002d9. It proves the minimal resolution

0 -> F_3 -> F_2 -> F_1 -> F_0 -> I -> 0,
F_0=6S(-5) direct-sum 10S(-6),
F_1=10S(-7) direct-sum 40S(-8),
F_2=45S(-9) direct-sum S(-10),
F_3=6S(-10) direct-sum 5S(-11).

It also identifies M_5=R_6 direct-sum E_24 and M_6=V*, where R_6 is the invariant six-dimensional socle and the adjoint of actual multiplication identifies E_24 isomorphically with End_0(V) inside V tensor V*. This follows there from Heisenberg-character symmetry and degree-zero generation of the Rao module, not from evaluating a chosen matrix. Use this actual adjoint as the identification. Then multiplication by ell in S_1=V* is exactly

M_5 -> M_6, (r,A) |-> ell composed with A.

In particular it kills R_6. This identity determines all degree-five-to-six multiplications simultaneously, up to the imported equivariant identification of M_6 with V*.

## 2. Uniform multiplication for every nonzero linear form

Let L be any r-dimensional subspace of V*. The joint multiplication map is

M_5 -> Hom(L,V*), (r_0,A) |-> [ell |-> ell composed with A].

If r<5, this map is surjective. Choose a basis of V* whose first r elements span L. An arbitrary prescribed image fixes the first r rows of A. At least one unused diagonal entry remains; choose it to make tr(A)=0. Hence the rank is 5r and the common annihilator in M_5 has dimension 30-5r. This includes r=0.

If r=5, the image is exactly the trace-free endomorphisms, of dimension twenty-four, and the common annihilator is exactly R_6, of dimension six. In particular every nonzero ell gives a surjection M_5 -> M_6 of rank five and kernel dimension twenty-five. This is uniform in ell; it is stronger than surjectivity of the aggregate map S_1 tensor M_5 -> M_6. It does not assert a Lefschetz property in any other degree.

## 3. Every proper hyperplane section has sextic interpolation

Let H=(ell=0) contain no component line of C. Since C is reduced and its components are disjoint, ell is a nonzerodivisor on O_C. Thus D=C intersection H consists of twenty-five distinct reduced points, and restriction gives the exact sequence

0 -> I_C(5) --ell--> I_C(6) -> I_(D,H)(6) -> 0.

Its cohomology, section 2's surjectivity and H^2(I_C(5))=H^1(O_C(5))=0 give H^1(I_(D,H)(6))=0. Therefore the twenty-five points impose independent sextic conditions in H=P^3, and

h^0(I_(D,H)(6))=binom(9,3)-25=59.

The other regularity conditions H^2(I_(D,H)(5))=0 and H^3(I_(D,H)(4))=0 follow from the point restriction sequence and elementary cohomology on P^3. Consequently reg(I_(D,H))<=7. Neither exact regularity seven nor interpolation in smaller degree is asserted.

## 4. The tail row is the full coordinate row

Choose an N-equivariant minimal resolution, which exists by taking equivariant generator complements in each degree over the characteristic-zero field. In its last differential, minimality gives a block form

d_3 = [ L  Q ; 0  ell_row ],

where L maps 6S(-10) to 45S(-9), Q maps 5S(-11) to 45S(-9), and ell_row maps 5S(-11) to S(-10). The entries of L and ell_row are linear and those of Q are quadratic. The zero block is forced by minimality, not by a special basis calculation.

PR471 proves that ell_row is nonzero: in the dual complex, degree -5 has last free-space dimension thirty-one and Ext^4 dimension thirty, so the unique preceding degree -5 generator has nonzero image. The coefficient span of ell_row is an N-stable subspace of S_1. Indeed the source multiplicity space and the one-dimensional target multiplicity space are N-modules, so the coefficient map has invariant image, even if the target has a character twist. Since S_1=V* is irreducible under N, this nonzero span is all S_1. Its five entries are therefore a basis. After a constant basis change in the five source generators, write

ell_row=(x_0,x_1,x_2,x_3,x_4).

This normal form is universal up to basis choice. It does not compute L, Q or any selected HM coefficient.

## 5. A length-one saturation defect and an explicit Koszul tail

Write d_2=[A b], with A the restriction to 45S(-9), and put Z_2=im(d_2)=ker(d_1) inside F_1 and J=im(A). Exactness of the minimal resolution gives

Z_2/J = F_2 / (45S(-9)+im(d_3)) = S(-10)/(x_0,...,x_4)S(-10) = k(-10).

Thus all positive-degree multiples of the exceptional degree-ten second syzygy lie in J, while that syzygy itself does not. The sequence 0 -> J -> Z_2 -> k(-10) -> 0 is nonsplit: Z_2 is a submodule of the free module F_1 and is torsion-free, so it has no submodule isomorphic to k.

Here saturation is taken inside F_1: J^sat={z in F_1 : m^n z is contained in J for some n}. The quotient F_1/Z_2=im(d_1) is torsion-free, so Z_2 is saturated in F_1. The finite-length quotient above therefore proves J^sat=Z_2. This is a graded-module saturation defect, not an obstruction class for the original source problem.

Finally d_3 is injective. It identifies ker(A) with the inverse image of 45S(-9) under d_3, namely

6S(-10) direct-sum ker[5S(-11) --(x_0,...,x_4)--> S(-10)].

The second summand is the shifted second syzygy module of the residue field. Its usual Koszul resolution gives the minimal free resolution of J:

0 -> S(-15) -> 5S(-14) -> 10S(-13)
  -> 10S(-12) direct-sum 6S(-10) -> 45S(-9) -> J -> 0.

All maps are minimal: the Koszul differentials have linear entries, the six-generator component maps by L with linear entries, and the ten degree-twelve generators map through Q times a linear Koszul relation, with cubic entries. The resulting projective dimension of J is four and its depth is one, whereas Z_2 has projective dimension one and depth four. The discrepancy is exactly the length-one nonsplit saturation defect, not a failure of exactness of the HM resolution.

## Dependencies and boundaries

- PR471, a38c45f91c3f29134c6c8d0a2c51d5e8d1e002d9: complete resolution, actual Rao adjoint, top socle and nonzero tail map. https://github.com/Akilleez-QA/read-em-and-weep/blob/a38c45f91c3f29134c6c8d0a2c51d5e8d1e002d9/research/hm/rao-socle/PROOF.md
- The characteristic-zero HM normalizer and transverse line geometry are pinned through PR471 to the primary paper: https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf

This is an authored structural derivation requiring mathematical review, not proof-assistant verification. It uses no selected HM/source-instance evaluation, numerical matrix/rank, coefficient search, generator/checker or large computation. The original fixed-pair intersections, actual-source membership, pure conditions, higher-order lifting and algebraicity remain unresolved. No explicit coefficient matrices for L, Q or the preceding differentials are supplied.
