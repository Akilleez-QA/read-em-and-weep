# Two irreducible channels for septic multiplication

Work over C with the normalized Horrocks–Mumford bundle F, B=End_0(F), E=F(3), and its union C of twenty-five transverse evaluation-degeneracy lines. Let S_d=H^0 O(d). This note identifies the exact N-representations in the multiplication map left open by PR466. It first reduces the number g_7 of minimal septic ideal generators to two scalar tests, then proves the quotient-channel scalar nonzero by a universal Euler-complex comparison. Consequently g_7 belongs to {0,20}. The remaining primary-channel scalar is not determined.

## 1. Conventions, duality, and determinant lines

Use HM1973's normalizer N in SL(V), Heisenberg subgroup H, and quotient G=N/H=SL_2(F_5). Write theta for the Galois operation zeta_5 -> zeta_5^2, V_i=theta^i V with indices modulo four, A=V_1 and A*=V_3. HM section 1 identifies V_i*=V_(i+2). In particular S_1=V*=V_2.

Use W and W' for the quotient representations with characters chi_2 and chi_2'; U=Sym^2W and U'=Sym^2W' have characters chi_3 and chi_3'. Let T_4 have character chi_4 and Q_4 have character chi_4# (the latter is the spin four-dimensional representation). HM's Appendix shows that all these characters are real, hence the representations are self-dual; theta exchanges W,W' and U,U', while theta^2 fixes each. T_4 and Q_4 are inequivalent: the central involution of G acts as +1 and -1 respectively.

HM section 4, printed pp73–74, proves that V_s=H^0E is H-trivial with quotient character chi_4. Its determinant D=det V_s is trivial: it is a one-dimensional representation of the perfect group G. Thus Lambda^3 V_s=V_s* tensor D is T_4. Serre duality has no ambient determinant correction because N is contained in SL(V). The determinant linearizations in the EN sequences below are consequently the ones displayed, with D trivial.

The following identities are in HM section 2 and Lemma 3.3, or follow by multiplying the characters in its Appendix:

Lambda^2 V=A tensor W, Sym^2 V=A tensor U',
W tensor W'=T_4,
W tensor U=W direct-sum Q_4,
W' tensor U'=W' direct-sum Q_4.

For example the last two are the usual degree-two symmetric-product decomposition plus the irreducible Sym^3W, respectively Sym^3W'; the Appendix gives character chi_4# for both symmetric cubes. These labels are needed: the two distinct four-dimensional representations cannot be interchanged merely on dimensional grounds.

## 2. The canonical sextic source

PR464 identifies the unique N-equivariant new sextic complement U_6 with D tensor (Lambda^2 V_3)*. Applying theta^3 to Lambda^2V=A tensor W gives

Lambda^2V_3=V tensor W', hence U_6=V* tensor W'.

Moreover theta^2 fixes U' and W. Applying theta^2 to the symmetric/exterior decomposition of V tensor V gives

V* tensor V*=A* tensor (W direct-sum U').

It follows, using section 1's tensor identities, that the fifty-dimensional source has the multiplicity-free decomposition

S_1 tensor U_6 = A* tensor (W' direct-sum Q_4 direct-sum T_4).

Call its three isotypic summands X_10, X_Q, X_T, of dimensions 10,20,20. These summands are intrinsic, not choices of polynomial bases. Each is irreducible as an N-module by HM criterion (2.2), because A* is irreducible on H and the displayed quotient factor is irreducible. They are pairwise inequivalent, again by that criterion.

## 3. The exact septic target, including its labels

PR466 computes H^2B(-2) as the cokernel of the injective N-map

A tensor W -> Sym^2W tensor T',

where its universal cup lemma identifies T' with H^0 Omega^2(3)=Lambda^3V*. Since det V is trivial, Lambda^3V*=Lambda^2V=A tensor W. Consequently the target of this injection is

A tensor (U tensor W)=A tensor (W direct-sum Q_4).

The irreducible source A tensor W has multiplicity one here. Therefore the cokernel is exactly A tensor Q_4, not just an unspecified twenty-dimensional module. Equivariant Serre duality now gives

H^2B(-3)=A* tensor Q_4.

Let K_7 be the image in the EN sequence

0 -> D tensor B(-3) -> Lambda^3V_s tensor F -> Lambda^2V_s O(2) -> I_C(7) -> 0.

PR466 gives the exact sequence

0 -> Lambda^3V_s tensor H^1F -> H^1K_7 -> D tensor H^2B(-3) -> 0.

The primary monad cohomology H^1F=V_3=A* is HM's degree-zero normalized cohomology. With section 1's determinant calculation this becomes

0 -> A* tensor T_4 -> H^1K_7 -> A* tensor Q_4 -> 0.

Maschke's theorem splits this sequence. Since Hom_N(A* tensor Q_4,A* tensor T_4)=0, the equivariant splitting is unique. Thus both target summands are canonical. The first is the actual EN submodule Y_T; the second is the unique complement Y_Q mapping isomorphically onto the EN quotient.

PR466 identifies the forty-dimensional target of new-sextic multiplication with

R_7=H^0I_C(7)/(S_2 H^0I_C(5))=H^1K_7=Y_T direct-sum Y_Q.

## 4. Two scalars and a rigorous exclusion

Polynomial multiplication and every quotient above are N-equivariant. Therefore

m:S_1 tensor U_6 -> R_7

vanishes on X_10. It maps X_Q only to Y_Q and X_T only to Y_T. After choosing any nonzero intertwiner for each of these two pairs, its two restrictions are multiplication by scalars alpha_Q and alpha_T. Their numerical values depend on the normalization of these intertwiners, but their vanishing does not.

Schur's lemma implies that each restriction is either zero or an isomorphism. Hence

rank m=20 times the number of nonzero scalars,
g_7=dim coker m=20 times the number of zero scalars,

and in particular g_7 belongs to {0,20,40}. All other integer values between zero and forty are excluded structurally. More precisely,

ker m = X_10 direct-sum (X_Q if alpha_Q=0) direct-sum (X_T if alpha_T=0),
coker m = (Y_Q if alpha_Q=0) direct-sum (Y_T if alpha_T=0).

Thus there is an unavoidable canonical ten-dimensional kernel, not just a lower bound on its dimension. If g_7=20, the remaining generator space is one of two distinguishable irreducible twenty-dimensional representations.

## 5. Intrinsic tests and full linear syzygies

The quotient-channel test can be stated without choosing sextic representatives. The EN sequence at degree six identifies R_6=H^0I_C(6)/(S_1H^0I_C(5)) with D tensor H^2B(-4), and U_6 maps isomorphically onto R_6. Naturality of the cohomology connecting maps under multiplication by a linear form gives

pi_Q composed with m = D tensor [S_1 tensor H^2B(-4) -> H^2B(-3)],

under these identifications. Here pi_Q is the EN quotient, not a selected matrix projection. Accordingly alpha_Q is nonzero exactly when this cohomological multiplication is nonzero. By Serre duality this is equivalent to nonvanishing of its adjoint

H^2B(-2) -> S_1* tensor H^2B(-1).

The other scalar is the restriction X_T -> Y_T of m; its image lies in the primary EN submodule. It is a separate test. Neither scalar follows merely from the nonzero symmetric-monad differential used in PR466: that differential computes a cohomology group, whereas the present multiplication crosses the relevant hypercohomology filtrations. The next section proves alpha_Q nonzero by a different, explicit chain-map comparison.

For completeness let L_7 be the kernel of full multiplication S_1 tensor H^0I_C(6) -> H^0I_C(7). The canonical sextic splitting and the injectivity S_2 tensor H^0I_C(5) -> H^0I_C(7) give

0 -> Lambda^2S_1 tensor H^0I_C(5) -> L_7 -> ker m -> 0.

Indeed the old-product multiplication has kernel Lambda^2S_1 tensor H^0I_C(5) and surjects onto the quadratic quintic products; every element of ker m can therefore be cancelled by an old-product preimage. This sequence splits as N-modules by Maschke, without claiming a unique splitting. Thus the remaining uncertainty in the entire degree-seven linear-syzygy representation is exactly the same two vanishing tests. Its dimension is 70+g_7.

## 6. A universal Euler comparison forces the quotient channel

Put K=Lambda^2Q*=Omega^2(2) and L=Lambda^2V*. The exterior Euler sequence is

0 -> K -> L tensor O -> Q*(1) -> 0.

For a subbundle K of a trivial bundle L tensor O with quotient R=Q*(1), its degree-two Koszul complex

U^bullet=[Sym^2K -> K tensor L -> Lambda^2L tensor O]

in degrees 0,1,2 has only one cohomology sheaf, Lambda^2R=K(2), in degree two. This follows after locally splitting the short exact sequence; the mixed and pure K terms are contractible and the surviving term is Lambda^2R. Thus its hypercohomology in degree two after twisting by t is naturally H^0K(t+2).

At twist zero, both Sym^2K and K are acyclic, as proved by the Bott calculation in PR464. Consequently the canonical edge identifies Lambda^2L with H^0K(2). The latter is the irreducible 45-dimensional GL(V)-module of sections of Omega^2(4). Multiplication

S_1 tensor H^0K(1) -> H^0K(2)

is nonzero: a nonzero section of K(1) multiplied by a nonzero linear form cannot vanish, since K is locally free on integral projective space. It is GL(V)-equivariant with irreducible target, hence surjective. Here H^0K(1)=Lambda^3V* has dimension ten. Equivalently multiplication from hypercohomology degree two of U^bullet(-1) onto that of U^bullet is surjective. This argument is entirely universal, independent of the HM map.

Let q:W tensor K -> C_0 tensor O be the last arrow of the normalized HM monad, where C_0=V_3. Fix any w in W, and write q_w for its restriction K -> C_0 tensor O. There is a unique linear map c_w:L -> C_0 extending q_w. Indeed dual exterior Euler gives

0 -> Q(-1) -> L* tensor O -> K* -> 0,

and Q(-1) is acyclic by the ordinary Euler sequence. Therefore L* -> H^0K* is an isomorphism. This proves the extension assertion without choosing or evaluating any HM coefficients.

Let J^bullet be PR464's full symmetric-square monad, whose cohomology is B(-1). There is a chain map U^bullet -> J^bullet with maps in degrees 0,1,2 respectively

k_1 k_2 -> (w tensor k_1)(w tensor k_2),
k tensor l -> (w tensor k) tensor c_w(l),
l_1 wedge l_2 -> c_w(l_1) wedge c_w(l_2).

The degree-zero map lands in Sym^2(W tensor K), with zero component in the additional A tensor C_0 O(-1) summand. The maps in negative degrees are zero. The chain identities follow directly from q_w=c_w restricted to K and the symmetric-square differential: on degree zero it is the sum of the two products, and on degree one it is their alternating exterior product. The negative-degree terms of the target cause no additional identity for this map from U^bullet.

PR464's vanishing transgression proves that the canonical edge

Lambda^2C_0 -> hypercohomology^2(J^bullet)=H^2B(-1)

is an isomorphism. By naturality, the induced degree-two hypercohomology map at twist zero is therefore Lambda^2c_w under the two canonical edge isomorphisms.

Suppose multiplication S_1 tensor H^2B(-2) -> H^2B(-1) were zero. The chain map, also after twisting by -1, makes the multiplication square commute. The universal top multiplication is surjective, so the induced hypercohomology map at twist zero must vanish. Consequently Lambda^2c_w=0 for every w, and rank(c_w) is at most one for every w.

Take a basis w_1,w_2 of the two-dimensional space W. Then q(W tensor K) is contained in the constant subspace im(c_w1)+im(c_w2) of C_0, of dimension at most two. This contradicts the monad's sheaf-surjectivity onto C_0 tensor O of rank five. Hence the actual multiplication is nonzero. No selected instance, matrix, or numerical rank is evaluated: rank at most one is the universal consequence of a zero exterior square, used in a contradiction.

By Serre duality and section 5, alpha_Q is nonzero. Thus m maps X_Q isomorphically onto Y_Q, and only the primary scalar alpha_T remains:

g_7 is either 0 or 20;
ker m is X_10 if alpha_T is nonzero, and X_10 direct-sum X_T otherwise;
coker m is zero if alpha_T is nonzero, and Y_T=A* tensor T_4 otherwise.

In particular g_7=40 is excluded, as is a surviving spin-channel generator module. The universal comparison advances beyond the representation reduction without conflating its secondary multiplication with PR466's first differential.

## Sources, dependencies, and boundary

- Horrocks–Mumford (1973), section 1, criterion (2.2), construction (2.3), Lemma 3.3, section 4 and Appendix: https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf
- PR464, a091db646c2ad9ba73d0893f4d92ff54891aaf0c, exact sextic saturation and canonical complement: https://github.com/Akilleez-QA/read-em-and-weep/blob/a091db646c2ad9ba73d0893f4d92ff54891aaf0c/research/hm/exact-sextic-saturation/PROOF.md
- PR466, b378990352d5f9bba3aaed27a0b6e0ff4683e15c, universal cup, exact septic saturation and EN target: https://github.com/Akilleez-QA/read-em-and-weep/blob/b378990352d5f9bba3aaed27a0b6e0ff4683e15c/research/hm/exact-septic-saturation/PROOF.md

The new contribution is the exact multiplicity-free representation decomposition and the structural nonvanishing of its quotient channel. The remaining dependency is a structural proof of the primary scalar alpha_T's nonvanishing or vanishing. No selected actual HM/source-instance matrix, coefficient evaluation, numerical rank, generator/checker, parameter search or large computation is used. No exact value of g_7, original fixed-pair intersection, actual-source membership, pure conditions, higher-order lifting or algebraicity is inferred. This is mathematical proof text, not formal proof-assistant verification.
