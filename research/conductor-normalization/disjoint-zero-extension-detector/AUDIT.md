# Preserved mathematical audit

This review concerns the source manuscript and its stated assumptions. It is preserved as mathematical history, not a new independent certification of all publication edits or of unpublished input theorems. Source and publication hashes are recorded in SOURCE-HASHES.json. A split manuscript’s module or polar application remains conditional in its destination unit.

# Independent audit: disjoint-zero-scheme residue detector

## Verdict

**Pass.** The revised `PROOF.md` establishes the exact residue-moment criterion, persistence, the Hilbert-function exclusion, and the uniform nonsplitting bound at `6C`, conditional on its explicitly imported actual-bundle vanishing. The first nonsplitting order is correctly confined to `[3,6]` when `a=0` and `[4,6]` when `a=1`. No actual extension moment, Horrocks–Mumford entry, or selected source-map rank has been evaluated.

The two wording corrections found during review have been incorporated: the direct twist defining `e` is `a+2`, and divisor adjunction is normalized by the fixed equation `q^n`. There is no remaining mathematical correction required.

## 1. Extension and local-duality functional

Twisting the displayed Serre sequence by `a+2` gives

    0 → O(b) → E(a+2) → I_Z → 0,   b=2a+2.

The vanishing of `H¹(O(b))` and `H²(O(b))` identifies its class with `Ext²(O_Z,O(b))`. Surface Serre duality identifies this latter space with `H⁰(O_Z(−b−3))*`.

The nondegeneracy assertion is valid, including for nonreduced `Z`. Locally write the lci ideal as `(u,v)` in a regular local surface ring. The basic Koszul extension has free middle module, and its extension classes are parametrized by the Artin quotient. The middle module is locally free precisely when the multiplying local extension parameter is a unit. Thus the functional supplied by the actual locally free extension generates the dualizing module of each Artin local component and is a Frobenius functional. In particular it is nonzero. The final `6C` argument requires only this last, weaker conclusion.

## 2. Naturality, twists, and normalization

Set `d=2n`, `k=−b−3`, and `t=d+k`. Disjointness of `Z` and `D_n` gives the exact sequence

    0 → I_Z(k) --q^n→ I_Z(t) → O_Dn(t) → 0.

The dual of the restriction of the extension class is its connecting map into `H¹(I_Z(k))`, using surface Serre duality followed by Cartier-divisor duality. One can see this either from the two-term resolution of `O_Dn(b)` or by the Yoneda boundary for `0→I_Z(−d)→I_Z→O_Dn→0` and the Cartier Gysin identification.

There is no missing space of sections: `H⁰(O(k))=H¹(O(k))=0`, so every section of `O_Dn(t)` comes from a unique plane form. The same vanishings identify `H⁰(O_Z(k))` with `H¹(I_Z(k))`.

The stated Čech calculation is correct. If `f_i` lifts `(p/q^n)|Z`, then `p−q^n f_i` lifts `p|D_n` to `I_Z(t)`, and its difference on an overlap, divided by `q^n`, is `f_i−f_j`. Hence, for boundary convention `f_j−f_i`,

    δ_D(p|D_n) = −δ_Z((p/q^n)|Z).

Consequently the displayed minus sign in the pairing formula is valid with the proof's stated choice of divisor-duality identification and its definition `λ_e(s)=⟨e,δ_Z(s)⟩`. A different global sign convention for Ext boundaries or adjunction can change that common sign, but not the criterion or transition. The exact equation `q^n` must be retained when identifying the dualizing sheaf with `O_Dn(2n−3)`; the revised proof now states this. Its Cartier resolution introduces no factor of `n`.

Thus the necessary-and-sufficient criterion, not merely one direction, is proved.

## 3. Layers and first possible order

Serre duality on the Cartier scheme `D_n` gives

    H¹(O_Dn(b))* = H⁰(O_Dn(2n−b−3)) = H⁰(P²,O(2n−b−3)).

The first nonzero possible degree is `1` at `n=a+3`; all groups at earlier positive orders vanish. Thus automatic splitting through `2C` or `3C`, respectively, is correct.

For `D_m⊂D_{m+1}`, every section of `O_Dm(b)` lifts from the plane because `H¹(O(b−2m))=0`. Therefore the layer connecting map `δ_m` really is zero. The exact sequence in the proof follows, and its kernel dimension is

    h¹(C,O_C(b−2m)) = max(4m−2b−1,0),

because a plane twist `r` restricts to degree `2r` on the conic. The quotient of polynomial spaces in the dual description has the same dimension. The identity `M_{n+1}(qp)=M_n(p)` gives persistence without any additional hypothesis.

## 4. Hilbert-function inequality

The inequality

    h_Z(r)+h_Z(t_n−r) ≤ length(Z)

under the assumption `ξ_n=0` is valid for every indicated `0≤r≤t_n`. A linear form avoiding the finite support simultaneously trivializes all twists. The factor arising from `q^(−n)` is a unit, so the resulting bilinear pairing remains perfect. Products of the two evaluation images are evaluations of degree-`t_n` forms, hence their pairing is zero. Orthogonal subspaces in a perfect pairing have dimension sum at most the full dimension. This argument does not require reduced points and does not silently assume an unknown Hilbert function.

## 5. Imported vanishing and the bound `6C`

The cited source `prerequisite global-conic-splitting-exclusion, document PROOF.md (see the unit INPUTS.md)`, §2, does state `H¹(E(u))=0` for `u≥8`. Its dimension-two resolution argument is valid given the imported locally free resolution: only `H¹` of the rightmost term and `H²` of the next term are needed. This audit does not rederive the original HM resolution.

In the present Serre sequence, put `u=k+2+a`. Then

    H¹(E(u)) → H¹(I_Z(k)) → H²(O(k+2a+2)).

For `k≥6−a`, both outer groups vanish. Evaluation is therefore surjective in every such degree. At `n=6`, the required degrees are `7` for `a=0` and `5` for `a=1`. Both meet the respective thresholds `6` and `5`. A nonzero functional cannot vanish on a surjective evaluation image. Hence `ξ_6≠0` in both branches, and persistence proves the assertion for every `n≥6`.

## 6. From the actual extension to every decomposition

On `C`, the positive summand is the unique maximal embedded line. Across the order-`m` thickening, the difference space for two embedded lifts of that line is

    H⁰(C,Hom(O_C(a),O_C(−2−a))⊗O_C(−2m))
      = H⁰(C,O_C(−b−2m)) = 0.

The actual global inclusion supplies a lift at every order. Induction therefore proves uniqueness at every order, allowing the abstract line bundles themselves to deform. Any hypothetical direct-sum decomposition on `D_n` has a summand restricting to the maximal line on `C`; uniqueness forces this summand to be the actual lifted line. Such a decomposition would split the actual extension. Thus the moment obstruction excludes all decompositions, as claimed.

## Scope

Only local proof artifacts were read or written. The obsolete complete-intersection alternative is unnecessary for the stronger `6C` conclusion and is not used here.
