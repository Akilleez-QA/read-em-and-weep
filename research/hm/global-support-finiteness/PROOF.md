# Global classification of the primary support-drop scheme

## Statement and scope

Work over C. In the pinned exterior-star model, let A and V have dimension five, W dimension two, and let phi: exterior^2 A -> V tensor W be any Heisenberg-equivariant isomorphism of the representation type used in PR553. The Heisenberg group acts trivially on W. Let

sigma: Q(-1) tensor W* -> V tensor O

on P(A) be contraction of phi(x wedge A), where Q is the tautological quotient. Its rank-at-most-four determinantal scheme D4 is exactly the thirty reduced Heisenberg eigenlines Omega constructed in PR553. In particular, there are no additional positive-dimensional components.

This is a universal symbolic proof for every intertwiner of this type. No coefficients of a selected actual HM/source instance, selected matrices, numerical ranks, or search are used. The scheme assertion concerns sigma, not the original primary evaluation determinantal scheme.

## Pinned dependencies

- Exterior primary-evaluation model: PR543, commit 7bf725bcd857a2deb975f9ecb80fca32e7833ae0, research/hm/order-four-quadratic-load/PRIMARY-INJECTION-AND-FAILURE.md.
- Support/evaluation classification: PR552, commit e037e0a3686ecaae2d4691435c54db338e2b1798, research/hm/primary-support-strata/PROOF.md. Set-theoretically D4 is the primary evaluation rank-at-most-eight locus. Full support gives evaluation rank nine or ten.
- Thirty distinct eigenlines, evaluation rank eight there, and reduced isolated support-drop points: PR553, commit 342e2e3754664477026e4fcc3bc6a135a1eab9cc, research/hm/heisenberg-support-points/PROOF.md and LOCAL-TRANSVERSALITY.md.
- Generic primary evaluation rank ten: PR547, commit 5a8efc999e9b886c51f18232a580407bac4bbe66.

The only representation input needed below is the universal normal form already derived in PR553. No numerical Porteous degree is used to infer finiteness.

## 1. Universal equations for the common annihilator

All indices are in F5. Choose compatible Schrödinger bases e_i of A and v_j of V. For every allowed intertwiner,

phi(e_i wedge e_j) = v_(i+j) tensor w_(j-i),

where w_0=0, w_(-d)=-w_d, and w_1,w_2 are independent. These two vectors remain arbitrary throughout.

Write x=sum_i x_i e_i and y_j=y(v_j) for a nonzero covector y in V*. The point [x] belongs to D4 exactly when such a [y] annihilates the V-support of phi(x wedge A). For every b this means

sum_i x_i y_(i+b) w_(b-i)=0.

Independence of w_1,w_2 turns these into ten binomials:

(E1_b) x_(b-1)y_(2b-1) = x_(b+1)y_(2b+1),
(E2_b) x_(b-2)y_(2b-2) = x_(b+2)y_(2b+2).

Thus it suffices to classify their projective solutions ([x],[y]) in P4 times P4.

## 2. No intermediate coordinate supports

Let S={i:x_i nonzero} and T={k:y_k nonzero}. Both are nonempty. A product cell (i,k) in a binomial is paired with

tau(i,k)=(2i+2k, i+3k).

Indeed, setting i=b-d and k=2b-d gives b=k-i and d=k-2i, and the opposite cell is (b+d,2b+d). The map tau is an involution, and its fixed cells are precisely k=2i. Every nonfixed cell belongs to one of the ten binomials. Therefore the rectangle S times T is tau-invariant: each paired product is zero if and only if the other is zero, and fixed cells need no equation.

Projecting tau(S times T)=S times T gives

2S+2T subset S, and S+3T subset T.

For each t in T, the inclusion 2S+2t subset S is an equality, since its two sides have equal finite cardinality. If T contains two distinct elements, their two translates imply that S is invariant under a nonzero translation of F5. Such a translation generates the additive group, so S=F5. Then S+3T subset T forces T=F5.

If T is a singleton, S+3T subset T forces S to be a singleton as well. Say S={a}, T={k}. Tau-invariance forces k=2a. Hence there are exactly five singleton projective pairs, and every other solution has all ten coordinates nonzero.

## 3. The full torus has exactly twenty-five solutions

For full-support solutions define cyclic ratios

r_i=x_(i+1)/x_i, and s_j=y_(j+1)/y_j.

Their products are one. Equation E2_b states that a four-step ratio product in each variable has product one. Since the omitted ratios are r_(b+2) and s_(2b+2), it is equivalent to

r_(b+2) s_(2b+2)=1.

Equivalently,

s_(2i+3)=r_i^(-1).

Equation E1_b gives r_(b-1)r_b s_(2b-1)s_(2b)=1. Substituting the preceding formula gives

r_(b-1)r_b = r_(b-2)r_(b+1).

Set t_i=r_i/r_(i-1). The last equation says t_(b+1)=t_(b-1). Since stepping by two traverses F5, all t_i equal a scalar q. Thus

r_i=r_0 q^i, q^5=1.

The product of the r_i is one, so r_0^5 q^10=1, hence r_0^5=1. There are at most twenty-five choices of the pair (r_0,q), and the ratios determine [x]. The displayed formula for s determines [y] uniquely.

For completeness, every choice r_0,q in the fifth roots of unity occurs. Normalize x_0=1 and put

x_i=r_0^i q^(i(i-1)/2), for i=0,1,2,3,4.

The conditions r_0^5=q^5=1 ensure cyclic consistency. Set s_(2i+3)=r_i^(-1); its product is one, so it integrates to a unique projective y. E2 holds by construction. Constant t_i=q gives the recurrence above, hence E1. This proves exactly twenty-five torus pairs.

## 4. Global scheme identification

The common-annihilator incidence has exactly thirty closed points: five singleton pairs and twenty-five full-torus pairs. Consequently its image D4 has at most thirty closed points and is zero-dimensional. PR553 already supplies thirty distinct closed points Omega in D4, so the support of D4 equals Omega. PR553's invertible normal-derivative argument says the local determinantal scheme at each such point is a reduced point. Thus D4 equals Omega scheme-theoretically.

This reasoning first establishes global finiteness by classifying all supports and all torus solutions; it does not infer finiteness from thirty isolated points or from a Chern number. Uniqueness of [y] at every classified solution also confirms support rank exactly four throughout D4.

## 5. Primary-only consequence: codimension six of bad quadratics

Let B in P(S2)=P14 be the primary-bad locus: [q] belongs to B when the primary map m_q:A->M2 has a nonzero kernel. Consider the projective incidence of ([x],[q]) with m_q(x)=0. The evaluation map at x has rank r, and its q-fiber is P^(14-r).

By the global result and PR552, evaluation rank eight occurs precisely at the thirty points Omega, while all other points have rank nine or ten. There are no rank-six or rank-seven points. The rank-nine stratum has dimension at most three because rank ten holds on a nonempty open set by PR547. Therefore the incidence dimensions over the three strata are bounded by

rank eight: 0+6=6;
rank nine: 3+5=8;
rank ten: 4+4=8.

It follows that dim B is at most eight, hence codim(B,P14) is at least six. In particular a general projective 5-plane misses B. Moreover, through any prescribed point p of P14 a general projective 5-plane meets B at most at p: project from p to P13, take the closure of the image of B minus {p}, of dimension at most eight, and choose a projective 4-plane avoiding it. Its cone with vertex p is the required projective 5-plane.

This is an existence statement and does not decide whether a prescribed selected quadratic is primary-good. It does not settle the full adjoint rank, a selected Q4/source instance, higher-order lifting, or algebraicity.

## Verification status

Authored structural proof. The binomial reduction, elementary support dichotomy, torus necessity and converse were independently checked by a separate mathematical reviewer before this file was prepared. No formal proof assistant verification is claimed. Exact-file review is still to be recorded separately.
