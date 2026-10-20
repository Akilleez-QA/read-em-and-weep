# An explicit fourth-order local associativity correction

## Scope and source

This is a universal calculation in a commutative differential algebra over a characteristic-zero field. All derivatives below act on formal independent functions or coefficient symbols. No physical source functions, matrices, inputs, detectors, or residuals are evaluated. This proves local associativity only, not fourth-order overlap descent, a module lift, or a central-period identification.

Source read on 2026-10-19: https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6260064519 . The surrounding PR1 coordination since 04:40 UTC was also read. The source supplies a product through order three of the form Moyal + h³ρ/2, where ρ=z_P π_P+z_Q π_Q and the two coefficients have disjoint pair dependence. The earlier fixed-product automorphism criterion in `antecedent third-order-automorphism-obstruction / PROOF.md` was read; no fixed-product Poisson-preservation or period claim is made here.

## 1. Setting and statement

Let R carry four commuting derivations D_1,...,D_4. Let π_P=D_1∧D_2, π_Q=D_3∧D_4, π=π_P+π_Q, with constant components π^{ij}. Write

ρ=z_P π_P+z_Q π_Q,
D_3 z_P=D_4 z_P=D_1 z_Q=D_2 z_Q=0.

Repeated indices below run from 1 to 4 and are summed. The notation ρ^{kl} denotes formal coefficients in this derivation basis; in particular no source matrix is being formed or evaluated. Let

M_n(f,g) = (1/(2^n n!)) π^{i_1j_1}...π^{i_nj_n}(D_{i_1}...D_{i_n}f)(D_{j_1}...D_{j_n}g)

be the ordinary constant-coefficient Moyal coefficients, with M_0(f,g)=fg. Put B(f,g)=ρ^{kl}(D_k f)(D_l g)/2. Define

N(f,g) = (1/4)π^{ij}ρ^{kl}(D_iD_k f)(D_jD_l g),

K(f,g) = (1/12)π^{ij}(D_jρ^{kl})[(D_iD_k f)(D_l g) − (D_k f)(D_iD_l g)],

Q=N+K.

**Theorem.** The normalized differential product

f ⋆ g = Σ_{n=0}^4 h^n M_n(f,g) + h³ B(f,g) + h⁴ Q(f,g)  modulo h⁵

is associative and has exactly the prescribed third-order truncation. Its coefficients require only regular coefficient symbols and their derivatives, with no integration, division by a function, or local coordinate primitive. Thus regular derivations and regular z_P,z_Q give a regular fourth-order local product.

Both N and K are symmetric in their two arguments. Symmetry of K follows either from its pair formula below or by interchanging k,l and using antisymmetry of ρ. Hence this correction also preserves the usual parity of the fourth coefficient.

## 2. Exact equation at order four

For a bilinear cochain Q use

(d_H Q)(f,g,k)=f Q(g,k)−Q(fg,k)+Q(f,gk)−Q(f,g)k.

Moyal is associative because all D_i commute. B is a biderivation, so its Hochschild differential vanishes, and hence it introduces no order-three defect. At order four the only new composition terms involve B with M_1. The associator (f⋆g)⋆k−f⋆(g⋆k) therefore has coefficient

R(f,g,k)−d_H Q(f,g,k),

where

R = M_1(B(f,g),k)+B(M_1(f,g),k)−M_1(f,B(g,k))−B(f,M_1(g,k)).

There is no term involving B with M_2 until order five, or B with itself until order six. It suffices to prove d_H(N+K)=R.

Separate R into terms R_0 in which no derivative hits a coefficient of ρ and terms R_1 where one does. Freezing the coefficients and expanding the constant Moyal product with π replaced by π+ε ρ shows

d_H N=R_0.

Indeed its coefficient linear in ε at second order is exactly (π^{ij}ρ^{kl}+ρ^{ij}π^{kl})D_iD_k f D_jD_l g/8=N; constant-coefficient associativity proves the identity. This freezing argument is legitimate for d_H N because the classical Hochschild differential never differentiates coefficients.

The derivative part is explicitly

R_1(f,g,k) = (1/4)π^{ij}(D_iρ^{ab})(D_a f)(D_b g)(D_j k)
              −(1/4)π^{ij}(D_jρ^{ab})(D_i f)(D_a g)(D_b k).

The disjoint-pair hypothesis makes R_1 and K sums of two independent two-derivation identities. Cross-pair terms vanish here; they do NOT vanish in N.

## 3. Direct proof of d_H K=R_1

Work in one abstract pair. For independent derivative-symbol vectors u,v,w write

[u,v]=u_1v_2−u_2v_1,
a=(D_1 z,D_2 z),
ℓ(u)=[u,a].

Symbols mean universal jets: u^I v^J records (D^I f)(D^J g), not a choice or evaluation of actual functions. Leibniz substitution gives the Hochschild differential of a bilinear symbol q as

q(v,w)−q(u+v,w)+q(u,v+w)−q(u,v).

For K the symbol is

q_K(u,v)=[u,v](ℓ(u)−ℓ(v))/12.

For R_1 the symbol is

r_1(u,v,w)=−([u,v]ℓ(w)+[v,w]ℓ(u))/4.

The elementary two-dimensional identity

[u,v]ℓ(w)+[v,w]ℓ(u)=[u,w]ℓ(v)

follows by expanding six scalar monomials (equivalently the alternating three-vector identity in dimension two). Expanding the Hochschild substitution for q_K gives

d_H q_K=−(2[u,w]ℓ(v)+[v,w]ℓ(u)+[u,v]ℓ(w))/12
        =−[u,w]ℓ(v)/4
        =r_1.

This proves the required cochain equality, pair by pair. Together with section 2 it proves the theorem. In particular this proof does not appeal to a formality theorem or infer associativity merely from Poisson compatibility.

## 4. Why naive varying-coefficient Moyal fails

Define the **frozen-coefficient Moyal prescription** for π_h=π+h²ρ by inserting its coefficients into the ordinary Moyal coefficient formula, while taking all displayed derivatives only on f and g. Its expansion through h⁴ is precisely

Σ_{n=0}^4 h^n M_n + h³B + h⁴N.

It omits K. Its order-four associator is therefore R_1. In one pair its universal symbol is

−[u,w]ℓ(v)/4.

For example, the coefficient of u_1v_1w_2 is −D_2z/4, and the coefficient of u_1v_2w_2 is D_1z/4. These are independent formal jet coefficients. Thus the frozen prescription is not a universal associative formula for variable z; in the free differential-jet setting its fourth-order defect vanishes only when both own-pair derivatives of each z vanish. Degenerate concrete algebras can have relations among derivations/jets, so no converse on such algebras is asserted.

The bivector π_h is nevertheless formally Poisson: each own-pair summand is Poisson in two derivation directions, and cross Schouten brackets vanish by disjoint dependence. Formal Poisson compatibility therefore does not validate the frozen Moyal prescription. The explicitly displayed K supplies the missing correction.

This distinguishes the frozen prescription from alternative meanings of an exponential involving variable-coefficient operators, where repeated operators can differentiate coefficients. No assertion about an unspecified alternative ordering is intended.

## 5. Mixed terms and limits

Writing P,Q for the frozen pair bidifferential contractions, the second-derivative correction N has coefficients

N = (1/4)[z_P P²+(z_P+z_Q)P Q+z_Q Q²].

Thus even disjoint pair dependence does not allow one to discard the mixed fourth-order contribution. In the two-parameter product with first coefficient (sP+tQ)/2 and cubic addition (s³z_P P+t³z_Q Q)/2, the same calculation gives the degree-four correction

(1/4)[s⁴z_P P²+(s³t z_P+st³ z_Q)P Q+t⁴z_Q Q²]
  + s⁴K_P+t⁴K_Q.

There are no mixed derivative-of-coefficient K terms. This statement is about total parameter degree four only.

The theorem gives a concrete local fourth coefficient preserving the new third coefficient. It leaves the order-four overlap operator, inner-gluing element, and pentagon correction to separate equations. It neither proves those prescribed local coefficients globally glue, nor identifies an algebroid period, nor lifts a module, nor determines any retained obstruction value.
