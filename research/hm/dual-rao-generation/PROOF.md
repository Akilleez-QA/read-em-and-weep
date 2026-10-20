# The lower Rao graph scalar is nonzero

Work over C. Let C be the twenty-five disjoint HM evaluation-degeneracy lines in P(V), S=Sym(T), T=V*, dim V=5, and M_d=H^1(I_C(d)). Put P_e=M_(6-e)*, with multiplication dual to that of M. Thus P is a finite-length graded S-module. Let B=End_0(F) for the normalized HM bundle.

We prove actual surjectivity T tensor H^1(B) -> H^1(B(1)), determine the unique two-channel relation scalar to be nonzero, and prove that M modulo its six-dimensional degree-five socle is level of socle degree six and type five. These are structural statements about the full Rao module, not a selected source-instance evaluation.

## 1. Pinned inputs and the complete presentation

PR471 at a38c45f91c3f29134c6c8d0a2c51d5e8d1e002d9 proves the complete minimal resolution of I_C, whose last two terms are

F_3=6S(-10) direct-sum 5S(-11),
F_2=45S(-9) direct-sum S(-10).

Graded local duality identifies M^vee with Ext^4(S/I_C,S(-5)), which is the cokernel of the last dual differential. Shifting the grading to P therefore gives an exact minimal PRESENTATION

S(-1) direct-sum 45S(-2) -> S tensor V direct-sum S(-1) tensor R_6 -> P -> 0.  (1)

In particular ALL relations are generated in degrees one and two. We do not assume that the dualized complex is exact at preceding terms. Cokernel exactness alone gives (1).

PR471 identifies P_0=V and P_1=End_0(V) direct-sum R_6. Its actual multiplication calculation, recorded in PR472, makes the unique linear relation the identity in T tensor V=End(V), after compatible dual identifications. Write this Euler relation as epsilon=sum x_i tensor v_i. There is no relation involving R_6 in degree one; such a constant entry would violate minimality.

PR455 at 8cbbe482ee50c35d52ffcdf3efb837fa8cf96af4 proves

H^1(B(1))=V* tensor (J_5 direct-sum R_6).

The Eagon--Northcott complex, twisted to I_C(4), has left term B(-6), middle term Lambda^3 H^0(F(3)) tensor F(-3), and right free term Lambda^2 H^0(F(3)) tensor O(-1). The determinant character is trivial. The middle term has H^2=H^3=0 by primary HM cohomology and Serre duality. Splitting the complex into two short exact sequences gives

M_4=H^3(B(-6))=H^1(B(1))*=V tensor (J_5 direct-sum R_6).

These connecting maps are natural for multiplication. The corresponding degree-five dual injection H^1(B) -> P_1 is exactly its nontrivial Heisenberg-character summand End_0(V). Thus the image T H^1(B) in H^1(B(1)) is the quadratic image S_2 P_0 in P_2.

## 2. Conventions and the two degree-two channels

Use the HM normalizer N in SL(V), Heisenberg subgroup H, quotient SL_2(F_5), and five-dimensional conjugates A=V_1, A*=V_3, with V*=V_2. Write W,W' for the two-dimensional quotient representations, U'=Sym^2(W'), J_5 for the five-dimensional quotient representation, and R_6 for the six-dimensional one. The relevant quotient representations are self-dual. The tensor identities are

Sym^2 T=A* tensor U',
V tensor A*=V* tensor (U' direct-sum W),
U' tensor U'=1 direct-sum U' direct-sum J_5,
W tensor U'=R_6.

Consequently

S_2 tensor V=V* tensor (1 direct-sum U' direct-sum J_5 direct-sum R_6).

The products T epsilon form the V* tensor 1 summand: multiplication by the nonzero vector epsilon in a free S-module is injective, and this is the unique copy of that irreducible. After dividing by these Euler products, the free degree-two source of (1) is

V* tensor (U' direct-sum J_5 direct-sum R_6) direct-sum V* tensor R_6.  (2)

The first three summands are quadratic in the V-generators; the last is linear in the R_6-generators. The target is P_2=V* tensor (J_5 direct-sum R_6). The displayed tensor representations are inequivalent irreducibles except for the indicated two R_6 copies, by the HM Heisenberg-normalizer correspondence.

## 3. The actual linear-R_6 map is an isomorphism

The disjoint-line description gives M=coker[S -> direct-sum_l S/I_l], so M is generated in degree zero. In particular T M_4=M_5. Project its actual multiplication to the H-invariant summand R_6 in M_5. Since (T tensor V)^H is the one-dimensional identity summand, the J_5 source cannot map to R_6. On the other source V tensor R_6, the map must be a scalar multiple of evaluation T tensor V -> C, tensored with identity on R_6. Generation makes this scalar nonzero.

Normalize it to evaluation. For EVERY nonzero ell in T, the composite

M_4=V tensor (J_5 direct-sum R_6) --ell--> M_5 -> R_6

is zero on V tensor J_5 and is ell tensor identity on V tensor R_6. In particular it is surjective, without any proper-hyperplane hypothesis.

Dually, the linear-R_6 source in (2) maps isomorphically onto the R_6 target channel. The quadratic J_5 channel must also map isomorphically: it is the only source of that target. Normalize both maps. The U' channel is forced to be a relation. The remaining map is one scalar alpha from the quadratic R_6 channel to the target R_6. Thus the forty-five-dimensional quadratic relation space, modulo Euler products, is

V* tensor U' direct-sum {(q,-alpha q): q in V* tensor R_6}.  (3)

This derives the graph from actual multiplication and exactness, not merely matching characters.

## 4. Finite length excludes alpha=0

Suppose alpha=0. Then (3) lies entirely in the quadratic V-generator summand. Euler products also lie there. Hence every degree-two relation of (1), not only its class modulo Euler products, has zero component in S(-1) tensor R_6. The degree-one relation has the same property.

But (1) is the COMPLETE presentation: there are no higher-degree minimal relations that could subsequently involve those six generators. Its cokernel would therefore contain the free direct summand S(-1) tensor R_6. This contradicts finite length of P. Therefore alpha is nonzero. Rescaling the relative generator normalization makes alpha=1; zero versus nonzero does not depend on that choice.

Both target channels are now attained by S_2 tensor V. Therefore

S_2 P_0=P_2,
T H^1(B)=H^1(B(1)).

The second equality is the actual cohomological multiplication identified in section 1. No conclusion that multiplication by each individual linear form is surjective follows.

## 5. The resulting level quotient and detection at the top degree

Let N_0=S P_0 be the submodule of P generated by its degree-zero part. Quotienting (1) by the V-generators, the graph relations with alpha nonzero impose precisely T tensor R_6 on the remaining generators. Hence

P/N_0=R_6 tensor k(-1).  (4)

Thus (N_0)_e=P_e for all e>=2, and (N_0)_1=End_0(V). Since N_0 is generated in degree zero, the dual module with grading reversed about six has socle only in degree six, of dimension five. Dualizing (4) identifies this module as

M / Soc(M)_5 = M / R_6,

where R_6 is placed in degree five. It is also generated in degree zero, being a quotient of M. Thus this quotient is level, with socle degree six and type five. This refers to a finite-length module, not an assertion that it is the coordinate ring of a level scheme.

For every 0<=d<=4, generation of N_0 and (N_0)_(6-d)=P_(6-d) imply that the joint multiplication map

M_d -> Hom_C(S_(6-d),M_6)

is injective. In particular no nonzero M_4 class is killed by every quadratic, and no nonzero M_4 class has all its linear multiples contained in the R_6 socle. This is an aggregate detection theorem, not injectivity for one chosen quadratic. It continues the scalar exclusion through the full finite-length module rather than stopping at a degree-two character calculation.

## Dependencies, review and scope

- PR471: https://github.com/Akilleez-QA/read-em-and-weep/blob/a38c45f91c3f29134c6c8d0a2c51d5e8d1e002d9/research/hm/rao-socle/PROOF.md
- PR472: https://github.com/Akilleez-QA/read-em-and-weep/blob/306cd02e623881f3caeddaf17a286c33d3bec63f/research/hm/universal-tail/PROOF.md
- PR455: https://github.com/Akilleez-QA/read-em-and-weep/blob/8cbbe482ee50c35d52ffcdf3efb837fa8cf96af4/research/hm/twist-one-structural-vanishing/PROOF.md
- PR463, Eagon--Northcott: https://github.com/Akilleez-QA/read-em-and-weep/blob/8ec3631dcd6937e6cc7491d0200c1c78b5d21434/research/hm/order-four-residue/PROOF.md
- Horrocks--Mumford (1973), monad, primary cohomology and normalizer representation identities: https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf

Stacked after PR474 at 366f1acc08e23d6111fe310ae149c9636ebebb0e; its plane-incidence conclusion is not needed for the scalar exclusion. This is an authored structural proof subject to independent mathematical review, not formal proof-assistant verification. No selected actual HM/source evaluation, numerical matrix or rank computation, coefficient search, generator/checker or large computation is used. Exact ranks for individual lower multiplications, the original fixed-pair/source membership, higher-order lifting and algebraicity remain unresolved.
