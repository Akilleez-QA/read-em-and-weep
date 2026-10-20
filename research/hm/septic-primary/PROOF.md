# The primary septic channel is nonzero

Work over C. Retain the normalized Horrocks–Mumford bundle F, E=F(3), B=End_0(F), the twenty-five transverse evaluation-degeneracy lines C in P^4, and all N-representation conventions of PR467. Put S=C[x_0,...,x_4], S_d=H^0 O(d), I_d=H^0 I_C(d), and V_s=H^0E. In particular D=det V_s is trivial, A*=V_3, W,W' are the two inequivalent two-dimensional quotient representations, T_4=W tensor W', and Q_4 is the spin four-dimensional representation. The ordinary T_4 and spin Q_4 are distinct.

We prove that the remaining primary scalar alpha_T of PR467 is nonzero. Together with that paper's independently established alpha_Q nonvanishing, this proves that there are no minimal septic generators. We then determine the full degree-seven linear-syzygy representation canonically. No assertion about minimal octic generators or the entire minimal free resolution is made.

## 1. The next EN twist forbids cubic relations among the quintics

Let H=I_5, of dimension six. The wedge evaluation identifies H with Lambda^2 V_s. The degree-eight Eagon–Northcott sequence is

0 -> D tensor B(-2) -> Lambda^3 V_s tensor F(1) -> Lambda^2 V_s tensor O(3) -> I_C(8) -> 0.

Write K_8 for the image of the middle map. The first short exact sequence, H^0F(1)=0, and H^1B(-2)=0 imply H^0K_8=0. The first vanishing is the primary HM cohomology; the second is PR466's structural calculation. Therefore

S_3 tensor H -> I_8

is injective. In concrete terms, for any basis h_1,...,h_6 of H, an identity sum_a c_a h_a=0 with c_a in S_3 forces every c_a=0. This conclusion concerns relations among the six quintics, not the absence of all degree-eight syzygies.

We will also use the injectivity S_2 tensor H -> I_7 from PR466.

## 2. A polynomial Koszul lifting lemma

Let x=sum_i x_i e_i in S_1 tensor C^5, and let d be exterior multiplication by x on S tensor Lambda^bullet C^5. On polynomial exterior forms define

delta=sum_i (contraction by e_i*) composed with partial/partial x_i.

For a form of polynomial degree a and exterior degree p, direct application of the product rule and the exterior contraction identity gives

delta d + d delta = (5+a-p) times the identity.

Thus a d-closed form with 5+a-p nonzero is d-exact, with primitive delta(form)/(5+a-p). This is an explicit homogeneous contracting identity, so no coefficients of any HM map are required.

In particular, if quadratic polynomials r_ij=-r_ji satisfy

x_i r_jk - x_j r_ik + x_k r_ij=0,

then r_ij=x_i b_j-x_j b_i for linear polynomials b_i. Apply the identity with (a,p)=(2,2); the denominator is five. Likewise, if sextics q_i satisfy x_i q_j-x_j q_i=0, then q_i=x_i h for a quintic h: apply it with (a,p)=(6,1), whose denominator is ten.

## 3. Vanishing of the ordinary channel contradicts new sextics

PR467 canonically identifies the new sextic complement U_6 with S_1 tensor W'. Its multiplication source is

S_1 tensor U_6 = (S_1 tensor S_1) tensor W'.

Because Lambda^2 S_1=A* tensor W and W tensor W'=T_4, its exterior-factor summand

Lambda^2 S_1 tensor W'

is exactly the irreducible summand X_T of PR467, not either of the other source summands. The target is R_7=I_7/(S_2 H)=Y_T direct-sum Y_Q. Consequently, if alpha_T=0, multiplication sends all of Lambda^2 S_1 tensor W' into S_2 H.

Choose any nonzero w' in W', and an N-equivariant isomorphism S_1 tensor W' -> U_6. Let q_i be the image of x_i tensor w'. These are actual sextic polynomials in the canonical complement U_6, and are nonzero. Under the assumption alpha_T=0 there are unique quadratic polynomials r_ij^a such that

x_i q_j - x_j q_i = sum_a r_ij^a h_a.

Uniqueness follows from S_2 tensor H -> I_7 being injective; set r_ji^a=-r_ij^a. Taking the alternating combination with x_i,x_j,x_k gives

sum_a (x_i r_jk^a - x_j r_ik^a + x_k r_ij^a) h_a=0.

Every coefficient is cubic, so section 1's injectivity forces each parenthesized polynomial to vanish. Apply section 2 separately for every a to obtain linear polynomials b_i^a with r_ij^a=x_i b_j^a-x_j b_i^a. Define

q'_i=q_i-sum_a b_i^a h_a.

Then x_i q'_j-x_j q'_i=0 for every pair. Section 2 yields q'_i=x_i h for a quintic polynomial h.

Each q'_i belongs to I_6. Hence x_i h vanishes on C for every i. On the projective affine chart where x_i is invertible this implies h vanishes on C; these charts cover C. Thus h belongs to the saturated ideal section space I_5=H. It follows that every q_i lies in S_1 H. But every q_i also lies in U_6, and PR464's direct decomposition I_6=(S_1 H) direct-sum U_6 has zero intersection. This contradicts q_i being nonzero.

Therefore alpha_T is nonzero. The argument uses polynomial identities in S and saturation only at the last step; it does not divide inside S/I_C or assume that multiplication there is injective.

## 4. Exact septic generators and the canonical syzygy splitting

PR467 proves alpha_Q nonzero and gives the multiplicity-free source and target

S_1 tensor U_6 = A* tensor (W' direct-sum Q_4 direct-sum T_4),
R_7 = A* tensor (Q_4 direct-sum T_4).

The primary nonvanishing just proved makes the T_4 restriction an isomorphism by Schur's lemma. Both target channels are therefore reached, and

S_1 I_6=I_7,
g_7=0,
ker(S_1 tensor U_6 -> R_7)=A* tensor W'.

For the full degree-seven linear syzygies L_7=ker(S_1 tensor I_6 -> I_7), PR467 supplies the exact sequence

0 -> Lambda^2 S_1 tensor H -> L_7 -> A* tensor W' -> 0.

Here H=U direct-sum U', where U=Sym^2W and U'=Sym^2W'. The HM character table gives W tensor U=W direct-sum Q_4 and W tensor U'=R_6, with R_6 the irreducible six-dimensional quotient representation. Thus

Lambda^2 S_1 tensor H = A* tensor (W direct-sum Q_4 direct-sum R_6).

These three irreducibles are inequivalent to A* tensor W'. Maschke's theorem gives an N-equivariant splitting of the sequence, and the vanishing of Hom_N(A* tensor W',Lambda^2S_1 tensor H) makes that splitting unique. Consequently

L_7 = A* tensor (W direct-sum W' direct-sum Q_4 direct-sum R_6)

canonically as the sum of its four distinct isotypic components. Its dimension is 5(2+2+4+6)=70. The canonical assertion is about the submodules and splitting, not a chosen normalization of an intertwiner or polynomial basis.

## Dependencies, sources, and limits

- PR464 at a091db646c2ad9ba73d0893f4d92ff54891aaf0c: canonical sextic complement and its directness. https://github.com/Akilleez-QA/read-em-and-weep/blob/a091db646c2ad9ba73d0893f4d92ff54891aaf0c/research/hm/exact-sextic-saturation/PROOF.md
- PR466 at b378990352d5f9bba3aaed27a0b6e0ff4683e15c: H^1B(-2)=0, EN setup, and injectivity of quadratic quintic products. https://github.com/Akilleez-QA/read-em-and-weep/blob/b378990352d5f9bba3aaed27a0b6e0ff4683e15c/research/hm/exact-septic-saturation/PROOF.md
- PR467 at 8bdc576a17726fa348efec82a7644f83074f34e1: the source and target decomposition, alpha_Q nonvanishing, and the syzygy exact sequence. https://github.com/Akilleez-QA/read-em-and-weep/blob/8bdc576a17726fa348efec82a7644f83074f34e1/research/hm/septic-multiplication/PROOF.md
- PR167 at 063da90fc4543304e87e701cdefcc08225412f17: primary vanishing H^0F(1)=0. https://github.com/Akilleez-QA/read-em-and-weep/blob/063da90fc4543304e87e701cdefcc08225412f17/research/conductor-normalization/sharper-hm-regularity/SHARPEST-BOUND.md
- Horrocks–Mumford (1973), sections 2–4 and Appendix, for representation conventions, the quintics and character products. https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf

This proof resolves the actual natural primary multiplication, rather than guessing a scalar from dimensions. It contains no selected HM/source-instance evaluation, numerical rank or matrix calculation, coefficient search, generator/checker, or large computation. It makes no conclusion about fixed-source incidence or membership, first-order conditions, higher-order lifting, or algebraicity. The result is mathematical proof text, not formal proof-assistant verification. Minimal octic generators and the remaining free-resolution maps are still open.
