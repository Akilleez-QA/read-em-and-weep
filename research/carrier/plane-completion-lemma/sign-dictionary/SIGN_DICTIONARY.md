# Hamiltonian-to-vector dictionary and the BCH correction signs

Date: 2026-10-11. This is a separate universal sign calculation. The frozen first-normal comparison package and earlier plane-completion artifacts are unchanged.

## Conclusion

With the pinned Poisson convention, the map Aη(x)={η,x} is a Lie homomorphism from quadratic Hamiltonians to symplectic vector endomorphisms. The vector-logarithm dictionary ρ(η)=−Aη used by the positive-pairing first-normal construction is an **anti-homomorphism**. Therefore multiplying j→i vector transitions corresponds to tensor BCH in reversed order.

Nevertheless the resulting second-logarithm **correction equations** have the positive right-hand sides displayed in the pinned source. The bracket sign in an opposite BCH product and the sign after moving a linear correction to the other side of a cocycle equation must not be conflated. There is no demonstrated sign contradiction.

## 1. Conventions and exact general identity

Work over a commutative Q-algebra (in particular a characteristic-zero field or our rational parameter ring), in a local frame in which Ω is the alternating-form matrix. For a quadratic polynomial η write

    η(x)=½ xᵀ Hη x,    Hη=Hessian(η)=Hηᵀ.

This includes the pinned factor-of-two convention on a diagonal tensor coefficient. Define

    {η,θ}=(grad η)ᵀ Ω(grad θ),
    Aη=Hη Ω.

On a linear generator v, the coefficient vector of {η,v} is Aη v. For the usual endomorphism commutator [A,B]=AB−BA, direct differentiation gives

    H{η,θ}=Hη Ω Hθ − Hθ Ω Hη,
    A{η,θ}=[Aη,Aθ].

Also AηᵀΩ+ΩAη=0. These identities hold even when Ω is degenerate; for our full rank-four completion Ω is nondegenerate, so the quadratic-to-symplectic-endomorphism identification is faithful after the actual relation quotient.

For ρ(η)=−Aη,

    [ρ(η),ρ(θ)] = −ρ({η,θ}).

Thus ρ is anti-homomorphic under these explicitly stated brackets. Merely multiplying a Lie homomorphism by −1 does not preserve its homomorphism property.

The dictionary respects the bundle/value-line transport. If a frame change T satisfies Tᵀ Ωi T=ell Ωj, the tensor transport is H↦ell⁻¹ T H Tᵀ and

    A_i(transport η)=T A_j(η) T⁻¹.

Consequently the identities are global statements for the appropriately line-valued Hamiltonians; they do not assume a trivial value line or discard the triangular TB entry.

## 2. Exact opposite-BCH identity

For formal positive-order Hamiltonians η and θ, exponentials and logarithms exist in the normal-adic completion. The elementary identity

    exp(−Aη) exp(−Aθ) = [exp(Aθ) exp(Aη)]⁻¹

and the Lie-homomorphism property of A imply

    exp(ρ(η)) exp(ρ(θ))
       = exp(ρ(BCH(θ,η))).

Equivalently,

    BCH(ρ(η),ρ(θ)) = ρ(BCH(θ,η)).

The tensor order is reversed. Through bracket length two the tensor expression on the right is η+θ−½{η,θ}+higher terms. This is an exact formal identity, not a finite test extended by extrapolation. It does not assert that any particular unavailable higher coefficient has been constructed.

## 3. Plane triangle: why the correction right-hand side is positive

Normalize all terms to the first frame; include the baseline transition transport in θ when it is nontrivial. Write the j→i vector transition as

    g̃ij=exp(−h Aηij − h² Aκij + O(h³)) gij.

The baseline transitions satisfy gij gjk=gik. The order-one relation is δη=ηij+Tij ηjk−ηik=0. The opposite-BCH formula yields

    κik=κij+Tij κjk−½{ηij,Tij ηjk},

or, with the correction on the left,

    δκ=+½{ηij,Tij ηjk}.

One can see the same sign without invoking a BCH theorem: the vector logarithm of the triangle defect at order two is

    −A(δκ)+½ A{ηij,Tij ηjk}.

Setting it to zero gives the positive correction equation. On the source's plane cover the displayed homogeneous B frame makes the relevant plane transports implicit, giving exactly its finite and infinity expressions +½{e01,e12}.

## 4. Mixed base/plane square

Let H_i denote an infinity-to-finite base transition, with first tensor logarithm h_i, and let ηF,ij and ηI,ij be the plane cochains. The square is

    g̃F,ij H̃_j = H̃_i g̃I,ij.

Move every Hamiltonian to the finite i frame using the baseline transitions. Denote the transported infinity cochain by TηI,ij and the transported h_j simply by h_j. The order-one relation is

    TηI,ij−ηF,ij−(h_j−h_i)=0.

At order two write the analogous cochains as κF,κI,κH. Applying opposite BCH to the two sides and rearranging gives

    TκI,ij−κF,ij−δκH,ij
      = ½({h_i,TηI,ij}−{ηF,ij,h_j}).

This is the pinned mixed correction right-hand side, with both terms and signs unchanged. No appeal to a guessed coordinate-versus-vector convention is necessary: the result follows from the explicitly declared vector convention and composition direction.

## 5. Exact source comparison and remaining boundary

Pinned source:
https://github.com/Akilleez-QA/read-em-and-weep/blob/6b69eefd57098d9a0c1d9f43ed993d36e1e54bcb/research/carrier/formal-five-parameter-chart/audit_original_cover/check_original_cover.py#L183-L205

The source's `coeff_bch` uses

- line189: finite +½{e01,e12};
- line190: infinity +½{e01,e12};
- lines191–194: mixed +½({h_i,T eI,ij}−{eF,ij,h_j}).

Those are exactly the correction right-hand sides derived in §§3–4. The source's positive bracket terms are therefore compatible with the negative vector action required by the positive-pairing first-normal comparison.

The general anti-BCH identity tells how to translate future logarithms once their meaning is specified. It does not by itself verify a particular higher-normal-order section correction, relation primitive, higher transition coefficient, ancestor restriction, algebraic carrier or defect. Before making such a claim, the actual coefficient must be transported using this dictionary and its equation checked at the stated order.

## 6. Verification

`check_sign_dictionary.py` checks the Hessian identity, Lie and anti-Lie identities, symplectic infinitesimal identity, and the plane/mixed correction equations on independent symbolic 4×4 matrices over Q. It uses exact polynomial expansion with exception-based checks. `SIGN_DICTIONARY_CHECKS.json` records the result.

The universal BCH statement is proved by the exponential inverse identity in §2; the finite symbolic checks are supporting checks, not its proof. Independent review separately derived both correction equations and confirmed the distinction between opposite BCH composition and the positive correction right-hand side.
