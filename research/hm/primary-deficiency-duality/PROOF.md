# The actual primary deficiency module is the shifted dual of the node ring

Status: independently mathematically reviewed (PASS); see REVIEW.md. Not formally checked. Work over C. No selected actual HM/source coefficients, evaluation matrices, numerical rank test, large computation, or public write is used.

## 1. Inputs and exact statement

Let P=C[x0,...,x4], let S be the actual primary surface, let nu:X->S be its finite normalization, and set H=nu*O_S(1). Write Z for the reduced set of thirty double points (not the Heisenberg center), T=nu_*O_X/O_S, T_n=H0(T(n)), and M_n=im[H0(X,nH)->T_n]. The quotient T has one-dimensional reduced fibers at these nodes. Put

R=P/I_Z,    E=direct-sum_(n in Z) H1(S,O_S(n)).

Here E has its actual P-module structure from multiplication of cohomology classes by ambient polynomials. For a locally finite graded vector space V use (V^vee)_n=Hom_C(V_(-n),C), and V(a)_n=V_(n+a).

Pinned inputs are:

- PR590, eb236dac3af8adcbc7f2f660b55e9d07904858c6, research/hm/degree-five-invariants/PROOF.md: actual N-equivariance of the normalization sequence, its O_S-linear multiplication, and identification of the node support with the thirty Heisenberg eigenlines. The normalizer N acts transitively on these thirty nodes: H5 is transitive on each five-node direction orbit and N/H5 is transitive on the six directions.
- PR591, 64a12e00718ec4cb09f17473237e879b08b28e16, research/hm/normalizer-residue-signs/PROOF.md: dim M_5=29 and the cokernel T_5/M_5 is the trivial N-representation of dimension one.
- PR589, a1c77f791158cc0976df80220c958a50c2217ee3, research/hm/eigenline-postulation/PROOF.md: the exact node-ring Hilbert function is (1,5,15,25,30,30,...) in degrees zero upward. In particular R_d=H0(Z,O_Z(d)) for d>=4, as a restriction image; no identification between fibers of different twists is needed.
- PR592, 1a2822304e0e76d985f8a083fb36548127b881a1, research/hm/normalization-resolution/PROOF.md, Sections 6–7: H1(X,nH)=0 for all integers n and H0(X,nH)=0 for n<0. The latter also follows directly from the actual graded normalization resolution.
- Commit 80f302ddd7e0dd19f1c54b725f56e5f81bb47c69, research/hm/lower-conductor-ranks/PROOF.md, with its independent review: dim M_n=(0,0,5,15,25,29,30,30,...) for n=0,1,... .

Theorem. There is an N-equivariant graded P-module isomorphism, natural up to one nonzero scalar,

E = R^vee(-5),                 equivalently E_n = Hom_C(R_(5-n),C).       (1)

This is an identification of multiplication maps, not only of Hilbert functions. Its construction uses the actual degree-five residue quotient. In particular Ann_P(E)=I_Z, and the P_+-socle of E is one-dimensional and concentrated in degree five. The module is not finite-length: dim E_n=30 for every n<=1.

## 2. A nowhere-degenerate residue functional

Choose a nonzero quotient identification T_5/M_5->C, and compose with T_5->T_5/M_5 to obtain lambda:T_5->C. It is N-invariant because the quotient representation is trivial. It annihilates M_5 and is unique up to one scalar.

For each node z let lambda_z denote its restriction to the one-dimensional summand T(5)_z of T_5. These restrictions are all nonzero. Indeed the vanishing set of these restrictions is N-stable by invariance; transitivity would force either all or none to vanish. They cannot all vanish since lambda is nonzero. This argument does not choose branch orientations or independently normalize thirty coordinates.

For every integer n the product of the node fibers yields a perfect pairing

T_n x H0(Z,O_Z(5-n)) -> C,       (t,a) |-> lambda(a t).                 (2)

At each node it is multiplication between one-dimensional fibers, followed by the nonzero functional lambda_z; the sum over nodes is therefore nondegenerate. This is meaningful for negative twists too, since O_Z(d) is invertible on the reduced zero-dimensional scheme for every integer d.

## 3. Descending the pairing to actual cohomology

Since H1(X,nH)=0 for every integer n, the normalization long exact sequence gives, naturally and compatibly with multiplication,

E_n = T_n/M_n.                                                       (3)

For n<=5 let d=5-n>=0 and regard R_d as the image of ambient restriction in H0(Z,O_Z(d)). Define

Phi_n:T_n -> Hom_C(R_d,C),       Phi_n(t)(p|Z)=lambda(p t).             (4)

This is independent of the representative p because polynomials vanishing on Z act as zero on the reduced-fiber sheaf T. The restriction of the perfect pairing (2) to the subspace R_d gives a surjection Phi_n: a linear functional on R_d extends to the finite-dimensional space H0(Z,O_Z(d)), which is paired perfectly with T_n.

For p in P_d and t=rho_n(s) in M_n, O_S-linearity gives p t=rho_5((nu*p)s) in M_5. Thus lambda(p t)=0, proving M_n is contained in ker Phi_n. Equation (4) therefore descends to a surjection

barPhi_n:E_n -> Hom_C(R_(5-n),C).                                    (5)

It remains to prove this is an isomorphism; surjectivity alone is not enough. For n=0,...,5 the respective dimensions of E_n are

30,30,25,15,5,1,

whereas dim R_(5-n) are exactly the same list by the node postulation input. Thus ker Phi_n=M_n in this range. For n<0, H0(X,nH)=0 gives M_n=0, while d=5-n>=6 and restriction R_d->H0(Z,O_Z(d)) is an isomorphism of thirty-dimensional spaces. The perfect pairing (2) then makes Phi_n an isomorphism. For n>=6, M_n=T_n and E_n=0, while R_(5-n)=0 by the nonnegative grading. Set barPhi_n=0 between these zero spaces.

This handles n=0 explicitly: M_0=0 and the pairing is against the full thirty-dimensional R_5, not against constants. There is no missing degree-zero extension in (3).

## 4. Multiplication compatibility and equivariance

The P-action on R^vee(-5) is contraction: for x in P_1, f in Hom_C(R_(5-n),C), and p in R_(4-n), set

(x f)(p)=f(x p).

For n<=4, t representing e in E_n, and p in R_(4-n), associativity of multiplication on T gives

barPhi_(n+1)(x e)(p)=lambda(p x t)=lambda((x p)t)
                         =(x barPhi_n(e))(p).                       (6)

For n=5 both target degree-six spaces vanish; for n>=6 all relevant E spaces vanish. Hence (6) holds in every degree. Since P is generated by P_1 and constants, the maps assemble into the graded P-module isomorphism (1).

All multiplication and restriction maps are N-equivariant, and lambda is invariant. More explicitly, for g in N,

Phi_n(g t)(p)=lambda(p g t)=lambda(g((g^(-1)p)t))
                              =Phi_n(t)(g^(-1)p).

This is exactly the contragredient action on Hom_C(R_(5-n),C). Thus (1) is an isomorphism of N-equivariant graded P-modules. No character or determinant twist has been silently suppressed. The only choice was scaling lambda, so the construction is canonical up to one scalar.

## 5. Module-theoretic consequences

First Ann_P(E)=I_Z. Inclusion I_Z subset Ann_P(E) follows from (1), or directly from its action on T. Conversely, if a homogeneous p of degree k has nonzero image in R_k, choose f in R_k^* with f(p) nonzero. It corresponds to e in E_(5-k), and (p e) in E_5 is nonzero since its value on 1 in R_0 is f(p). Thus p cannot annihilate E. The annihilator of a graded module is homogeneous, so this proves equality for arbitrary polynomials too. Consequently the full node scheme is recovered from the actual primary deficiency module, not just its length or Hilbert function.

Second, Soc_(P_+)(E)=E_5=C. Indeed at degree n<5 put d=5-n>0. A functional f on R_d killed by all linear forms vanishes on P_1 R_(d-1)=R_d, since R is standard graded, so f=0. At degree five all positive-degree multiplications vanish, and higher E degrees are zero. The degree-five socle is trivial under N by the residue construction.

Third, dualizing degreewise gives E^vee=R(5). Thus the dual of the entire actual deficiency module is cyclic, generated in degree -5, with its complete homogeneous relation ideal exactly I_Z. This gives a genuine inverse-system description without asserting that E itself is cyclic or finitely generated. Its nonzero negative tail precludes finite length and finite generation over the positively graded ring P.

A useful multiplication consequence is available without new geometric input. Let ell be any ambient linear form nonzero at all nodes. It is a nonzerodivisor on R, hence multiplication ell:E_n->E_(n+1) is surjective for every n by (1). Its kernel has dimensions

5,10,10,4,1 in degrees n=1,2,3,4,5,

and zero in every other degree. This follows by dualizing the injective maps ell:R_(4-n)->R_(5-n), or from the first differences (1,4,10,10,5) of the node Hilbert function with reversed degrees. In particular ell is an isomorphism on E_n->E_(n+1) for every n<=0. These are actual multiplication-rank conclusions, stronger than the dimensions of E alone.

## 6. The actual homogeneous-ring deficiency Ext module

Let A=P/I_S be the saturated homogeneous coordinate ring of the primary surface, and let m=P_+. The standard graded sheaf/local-cohomology comparison gives

H2_m(A)_n = H1(S,O_S(n))

naturally in every integer n and compatibly with polynomial multiplication. This comparison in cohomological degree two does not require projective normality or surjectivity of ambient restriction on H0. Hence H2_m(A)=E as graded P-modules. Graded local duality over the five-variable polynomial ring, with its canonical module P(-5), now gives

Ext3_P(A,P(-5)) = (H2_m(A))^vee = E^vee = R(5).                      (7)

These are actual graded modules, not only associated sheaves or equal Hilbert series. In particular this deficiency Ext module is cyclic with generator in degree -5 and relation ideal I_Z. Equation (7) is asserted as a graded P-module isomorphism; no extra equivariant canonical-module convention is needed for this assertion. If one uses the ambient determinant-one normalizer linearization and its induced trivial determinant line, it also has the compatible N-equivariant form.

## 7. Verification boundary and contribution

The proof uses a perfect pairing on the actual thirty node fibers, annihilation by actual normalization products, and the separately proved ranks to identify its kernel. It does not infer a P-module structure merely from matching Hilbert functions. It also checks the degree-zero term, all negative twists, the degree-five boundary, the grading-shift sign, and the full N-action.

This resolves the missing multiplication-structure dependency for the primary H1 module, supplies its exact annihilator and socle, and identifies the actual homogeneous-ring deficiency Ext module. It neither determines the primary surface ideal I_S nor proves ambient restriction isomorphisms. In particular it does not claim the primary surface is arithmetically Cohen–Macaulay. The full-adjoint K4 connecting-map problem, prescribed-source membership, higher lifting, and algebraicity remain separate and unresolved here.
