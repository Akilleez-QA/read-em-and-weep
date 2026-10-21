# The actual twenty-dimensional lift boundary as fifty-point quadric interpolation

Work over C. Let F be normalized HM, E=F(3), B=End_0(F), U=H0(E), D=det U. Let C be the 25 transverse evaluation-degeneracy lines and ell the evaluation cokernel, with ell|L=O_L(-1). All maps below are the actual evaluation maps; no selected coefficients or ranks are used.

Take q in the intersection of the nonempty primary-injective and residual-surjective quadratic opens, and the smooth-quadric/transverse-to-C open. These opens intersect in the irreducible space of quadrics. Put Q=(q=0), Z=C∩Q, so Z consists of fifty reduced points. The construction also works for a proper nonreduced intersection, but that generality is unnecessary here.

## 1. A canonical fifty-to-fifty map

The actual exterior-symmetric resolution from PR538, restricted to Q and twisted by -1, is

0 → D O_Q(-6) → Λ²U O_Q(-1) → U F_Q(2) → B_Q(4) → T → 0,

where T=ell²(-1)|Z has length fifty. Restriction is exact: multiplication by q is injective on ell² on C, so Tor_1(ell²,O_Q)=0. All the other terms of the original resolution are locally free.

Let R1 and R0 be the images in U F_Q(2) and B_Q(4), respectively. A smooth quadric threefold is ACM, with canonical bundle O_Q(-3). Hence H1 R1=H0 R1=0 and

H2 R1 = D H3 O_Q(-6), dimension h0 O_Q(3)=35-5=30.

The restriction sequence 0→F→F(2)→F_Q(2)→0 and primary injectivity give

H0 F_Q(2)=0,
H1 F_Q(2)=coker[q:H1 F→H1 F(2)], dimension five,
H2 F_Q(2)=H3 F_Q(2)=0.

Here the higher vanishings use the standard primary support and Serre duality, not an adjoint Hilbert table. The two image sequences now give H0 R0=H2 R0=0 and the canonical exact sequence

0 → U H1 F_Q(2) → H1 R0 → D H3 O_Q(-6) → 0.             (1)

Its dimensions are 20,50,30. Finally the boundary of 0→R0→B_Q(4)→T→0 gives

0 → H0 B_Q(4) → H0 T --b_q→ H1 R0 → H1 B_Q(4) → 0.    (2)

Thus the actual adjoint obstruction is a square fifty-point interpolation boundary, not an unspecified map between abstract twenty-spaces.

## 2. The thirty-dimensional quotient is cubic evaluation

Let p_q be the composite of b_q with the last map in (1). Up to the single compatible constant determinant line, its dual is exactly

H0 O_Q(3) → H0 O_Z(3).                               (3)

Here is the global dualizing identification, including its constant line. On C let M be the image line of U O_C→E_C and K its rank-three kernel, with cokernel ell. Then det K=D M^(-1). Transverse determinantal geometry gives N_{C/P4}=K*⊗ell. Consequently

 det N_{C/P4}=D^(-1) M ell³=D^(-1) det(E) ell²=D^(-1) O_C(5) ell².

Transversality identifies N_{Z/Q}=N_{C/P4}|Z. Adjunction on the smooth quadric, whose canonical bundle is O_Q(-3), therefore gives

 ω_Z=D^(-1) O_Z(2) ell²|Z,
 T*⊗ω_Z=D^(-1) O_Z(3).

Meanwhile dualizing the leftmost D O_Q(-6) term against ω_Q gives D^(-1) O_Q(3). Thus the dual of p_q is precisely the globally compatible map D^(-1) H0 O_Q(3)→D^(-1) H0 O_Z(3). The local evaluation normal form cancels units and leaves the Koszul resolution of the three transverse parameters, identifying this map with restriction under these adjunction identifications. No independent point weights or componentwise trivializations are inserted. This also identifies H0(T)* with D^(-1) H0 O_Z(3), as required by zero-dimensional Serre duality.

In particular p_q is onto precisely when H0 I_{Z,Q}(3)=0. This is equivalent to residual surjectivity: restricting C to Q gives

0 → I_C(1) --q→ I_C(3) → I_{Z,Q}(3) → 0,

and H0 I_C(1)=H0 I_C(3)=0, so H0 I_{Z,Q}(3)=ker[q:M1→M3], where Md=H1 I_C(d). The actual residual map N2→N4 is the dual of this multiplication. Therefore p_q is onto on the specified open and K_q=ker p_q has dimension twenty. Intrinsically K_q is the determinant-twisted dual of coker(3), or of H1 I_{Z,Q}(3).

## 3. The remaining twenty-boundary is an elementary-modification lift

For z in K_q, b_q(z) lands in the left term U H1 F_Q(2) of (1). Define

beta_q: K_q → U H1 F_Q(2)

by this factorization. Combining (1) and (2) gives

0 → H0 B_Q(4) → K_q --beta_q→ U H1 F_Q(2) → H1 B_Q(4) → 0.  (4)

In particular beta_q is an isomorphism if and only if B_Q(4) has no global sections. This is a concrete sheaf-theoretic criterion: none of the fifty point-supported values satisfying the thirty cubic dual constraints can lift to a trace-free twisted endomorphism of F_Q.

The original full multiplication has kernel H0 B_Q(4). Indeed H0 B(2)=H0 B(4)=0, directly from the same exterior-symmetric image sequences on P4: the relevant primary section spaces H0F and H0F(2), intermediate line-bundle groups, and H0ell²(-3), H0ell²(-1) all vanish. Thus restriction gives H0 B_Q(4)=ker[q:H1B(2)→H1B(4)]. Its target and source both have dimension85. Consequently

rank(beta_q)=20-corank(q:H1B(2)→H1B(4)).

Naturality identifies beta_q, up to the induced identifications of its source and target, with the snake-lemma boundary of the actual primary/residual extension. The target equality is immediate from F restriction and the cup map. The source equality is cubic restriction duality above. Thus this construction does not silently split that extension.

## Scope

This supplies an actual geometric realization and exact rank criterion for the remaining twenty-dimensional boundary, using fifty transverse points on a smooth quadric and their cubic interpolation cokernel. It does not establish its nondegeneracy. The missing input is the absence of global sections of B_Q(4), equivalently the nonexistence of a nonzero fifty-point compatible lift in (4). Cubic restriction injectivity alone does not imply that absence.

Sources: actual exterior-symmetric resolution and extension at https://github.com/Akilleez-QA/read-em-and-weep/pull/538 ; primary injection at https://github.com/Akilleez-QA/read-em-and-weep/blob/af3cf8bf93c4274e7651ad3d85e310825febaeee/research/hm/order-four-quadratic-load/PRIMARY-INJECTION-AND-FAILURE.md ; standard primary support and duality cited there and in PR538. Current PR1 coordination was read before this derivation. No external writes or selected HM evaluations were performed.

Pinned inputs: actual extension/resolution at d5d9bd997145b0ecf7d7bd659a19fb7845afb75f in PR538; nonempty common primary-injective/residual-surjective open at 14f4154ce6657e791a5e0fcdd9fdb67f9014712f in PR543.
