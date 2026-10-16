# Exact scalar dual closedness and a direct dual-fill contract

Reading-order qualification: this contract precedes `owned-denominator-finite-domain-certificate.md` and its independent audit. Those later notes supply the full finite-domain exactness and bounded-primitive comparison at proof level. They do not supply instantiated physical coefficient rows, a practical pivot/factored inverse, or a physical direct-fill residual.

## Result and scope

The scalar adjoint e_q=E_p^*Phi annihilates scalar boundaries whose induced End-valued primitives A_p(f) are admitted by the authenticated regular comparison. This follows from an explicit chain identity, not merely scalar H1 vanishing. Extension of this closedness statement to every scalar cocycle requires a compatible primitive-domain hypothesis; the existing finite pole bounds do not alone supply it. A direct finite dual construction is an exact row-space solve for the scalar Cech differential, which can avoid introducing a second partition in its FORMULA. However, the existing detector/domain artifacts do not supply the finite coefficient-space splitting or row-space certificate needed to instantiate that construction. A fixed-apex shortcut is not justified by the present ownership bounds.

This note therefore supplies (i) exact chain identities; (ii) a precise alternative dual algorithm and its verification equation; and (iii) the missing finite-domain/kernel data. It does not claim a cheaper executable circuit or evaluate source coefficients.

## 1. Cochain conventions

Let ell_d be the End-valued current 1-cochain on the common cover, represented on edge ij by g_ij^(-1)D_d g_ij. Its twisted Cech differential vanishes:

    delta ell_d=0,

because on a triple the current of g_ik=g_jk g_ij is the sum of the ij current and the transported jk current. Cup products use row-End transport to the first endpoint. Scalar derivatives commute with scalar restriction and delta, with their physical character/frame conversions retained.

For scalar cochains t of degree n, define

    A_p(t)=1/2(ell_b cup D_a t + D_a t cup ell_b
                    -ell_a cup D_b t - D_b t cup ell_a).

For a scalar 1-cochain s, the original E operator is

    E_p(s)=1/2(ell_b cup D_a s - D_a s cup ell_b
                    -ell_a cup D_b s + D_b s cup ell_a).

These formulas reproduce exactly the four current/derivative terms in the transition-only reduction. They do not commute a derivative past a partition weight.

## 2. Exact chain identities

The Cech cup Leibniz rule gives, for every scalar 0-cochain f,

    E_p(delta f)=-delta A_p(f).                         (1)

Indeed delta(ell_b cup D_a f)=-ell_b cup D_a delta f, while delta(D_a f cup ell_b)=D_a delta f cup ell_b. The a,b-swapped terms supply the other two signs.

For every scalar 1-cochain s,

    delta E_p(s)=-A_p(delta s).                         (2)

Here A_p is evaluated on a scalar 2-cochain: the signs remain plus between the two cup orders. These identities use the actual current cocycle and physical scalar derivations; no choice of scalar solver appears.

Let Phi be the authenticated refined detector. Its cohomological interpretation annihilates regular End-valued Cech boundaries on the admitted comparison domain. For every scalar f for which A_p(f) and its boundary participate in that authenticated comparison, (1) therefore implies

    <E_p^*Phi,delta f>=0,
    delta_0^* e_q=0 on this gauge domain,
    e_q=E_p^*Phi.                                      (3)

This is a domain-qualified statement. A fixed outer partition and coefficient envelope do not authenticate Phi on arbitrary regular primitives with unbounded poles. For a proposed scalar domain C0->C1->C2, require Phi on E_p(C1) and boundary annihilation for every A_p(f), f in C0. If a finite truncated domain is used, check these requirements there; do not assume that a full-regular-complex primitive remains within its cutoff.

## 3. Exact factorization and its nonuniqueness

For the pair-q scalar character O(0,0,-2,-2), with coordinates permuted as necessary, H1=0. Thus on the full regular Cech complex,

    ker(delta_1)=im(delta_0).

However, this full-complex equality does not by itself show that the primitives f lie in the admitted gauge domain of (3). Fix a scalar domain C1 on which e_q is defined and impose the following additional compatibility condition: every s in ker(delta_1|C1) has a regular scalar primitive f with delta_0 f=s for which A_p(f) and its boundary are admitted by the authenticated comparison. As a weaker sufficient alternative for the filling argument, one may directly certify that e_q vanishes on ker(delta_1|C1). A compatible extension of Phi annihilating all regular boundaries would also suffice, but has not been supplied by the bounded artifacts.

UNDER THIS CONDITION, e_q annihilates ker(delta_1|C1). It therefore defines a WELL-DEFINED functional on the image of delta_1|C1:

    eta_q(delta_1 s)=e_q(s).                            (4)

This is independent of the choice of s within C1. In particular eta_q(F_q)=Phi(E_p(s_q)) if s_q is represented in C1. The same conditional statement holds with p,q exchanged. No unconditional extension to the entire regular complex is asserted.

An extension of eta_q from im(delta_1|C1) to a containing scalar degree-2 space need not be unique. Two fillings differ by a functional annihilating im(delta_1|C1). On the full regular complex this includes dual degree-two cohomological freedom: pair-q H2 is nonzero, even though H1 vanishes. A finite model need not retain that full H2, so its freedom must instead be read from its actual annihilator. Thus closedness does not specify the coefficient rows of a preferred filling or force a cancellation of the existing inner weights.

The previously authenticated T_q^*e_q reproduces e_q(T_q F_q) on the authenticated source inputs. Calling it a filling on a larger scalar model requires the same kernel/domain compatibility; its source-level pairing identity alone does not prove D1^t T_q^*e_q=e_q on arbitrary V1. Equation (4) does not prove it is the only filling or that every filling requires its weights.

## 4. Concrete finite direct-fill algorithm

A weight-free-in-the-formula alternative is available once a certified finite scalar cochain model is supplied. Let V0,V1,V2 be finite rational vector spaces of regular cochains with specified bases, restriction/frame maps, and the actual owned denominators. Require:

1. The demanded scalar 1-cochains are represented in V1 and their F images in V2.
2. delta_0 and delta_1 are represented by explicit matrices D0,D1.
3. D1 D0=0, ker D1=im D0 on the represented domain, AND every A_p(f), f in V0, is admitted by the boundary comparison proving (3). Alternatively, directly certify that e_q vanishes on every vector of ker D1; that weaker condition suffices without finite H1 exactness.
4. Each coefficient request constituting e_q has a certified linear row in the V1 basis, after exact regularization.

Choose column combinations b_1,...,b_r in V1 whose classes form a basis of V1/ker D1. Let B be their column matrix. Then D1 B has full column rank r. Choose r row indices I giving an invertible minor

    C=(D1 B)_I.

Define a V2 covector eta supported on I by

    eta_I=C^(-t) B^t e_q,       eta_(outside I)=0.       (5)

Here e_q is written as a column of its covector coefficients. Then

    D1^t eta=e_q.                                      (6)

To verify (6), both sides agree on the b_j by C^t eta_I=B^t e_q; both vanish on ker D1. This is a complete exact direct dual-fill construction, with no scalar primitive as an intermediate and no new partition explicitly inserted into (5).

A useful implementation need not materialize dense matrices. It may supply pivot selectors and a factored inverse/triangular solve, together with the exact residual certificate (6). The certificate, regularity of its coefficient rows, and a complete product/byte schedule are mandatory before evaluation. A formal inverse symbol C^(-t) is not an executable cost certificate.

## 5. Precisely what the existing artifacts do and do not supply

`authenticated-refined-detector-composition.md` supplies e_q as an explicit finite adjoint expression with outer carrier54/legal29 weights, physical current factors, derivative adjoints, and retained prefix owners. `refined-tracefree-pole-domain.md` supplies finite envelopes and ownership bounds for the admitted source and comparison.

They do NOT currently supply the V1/V2 bases, D1 quotient pivot structure, or C inverse in section4. They also do not supply a primitive-domain comparison extending (3) to all cocycles of an arbitrary proposed scalar model. A finite Laurent envelope for transported cochains is not automatically an exact finite Cech subcomplex: restriction/frame conversion and denominator alignment must preserve the proposed representation, and artificial kernel vectors at the truncation boundary must be excluded or killed by e_q. The known standard tensor homotopy gives a splitting after comparison, but transporting it back is exactly where the existing prism/projection data enter.

Thus (5) is a bounded alternative construction CONTRACT, not an already instantiated replacement of T_q^*e_q. Its possible advantage is that it solves only for the particular finite covector e_q rather than for all F inputs. Its possible disadvantage is a large or dense coefficient solve. Neither outcome can be inferred from H1=0.

## 6. Why a fixed-apex dual cone is not yet legal

Over the common function field, one can contract the Cech simplex with a fixed apex v and write a formal primitive using F(v,i,j). This adds no partition algebraically. But a regular cochain F(v,i,j) is initially defined only on the triple intersection including v. Treating it as a regular edge cochain on (i,j) may introduce the apex's carrier/legal poles, whose owner is absent from that edge.

The authenticated outer weights clear the owners present in each detector tuple. They do not automatically clear a new, globally chosen apex in every term. Nor may its denominator charge be transferred to an equal carrier label on a different owner. The coefficient functional may then leave its certified Laurent domain. Extending Phi to arbitrary meromorphic boundaries is not licensed by its regular cohomological interpretation.

To use an apex shortcut, one must exhibit either an existing owner that serves consistently across the required coupled terms, with all retained weights, or an explicit extra regularization/cancellation certificate. No such identity is supplied merely by (1)-(3).

## 7. Safe next mathematical target

The minimal new object is a finite dual filling eta with the exact certificate

    delta_1^* eta = E_p^*Phi

on the authenticated demanded domain. One may seek it by a sparse row-space solve as in (5), by proving that a subset of Phi's existing weighted owners supplies a legal dual cone, or by an additional Atiyah/cup-product identity. The chain identities above prove compatibility only for scalar boundaries whose A_p primitives are admitted by the regular comparison. The primitive-domain condition in section3, or a direct finite kernel-annihilation certificate, remains necessary; the identities do not supply the missing regular-domain splitting.

No physical source polynomial or coefficient was evaluated.

## Dependency scope

Companion references are identified by basename. A referenced file not supplied with this collection is an external prerequisite, not an embedded proof or a verified relative link. The reading order and unresolved conditions are listed in `proof-notes-index.md`. Reported test results describe the source audit; this proof copy does not by itself constitute a new test run.
