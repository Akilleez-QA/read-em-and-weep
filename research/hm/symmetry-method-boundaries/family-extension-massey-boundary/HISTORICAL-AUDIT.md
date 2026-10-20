Historical independent audit of the source edition. The displayed SHA-256 binds the original complete proof. Publication changes are source-link normalization, explicit reuse labels and current-scope clarification; the current normalized bytes require their own review.

# Independent audit: family extension and mixed Massey constraints

## Audited final version and dependency correction

This audit independently checks the final proof at `PROOF.md`, SHA-256

    bce253daf1776bcdaca339f97d899e45809675da3c2b58da0159053b6deaed4d

The final proof's two-parameter expansion in Section 6 was checked directly: after substituting its stated primitives, the coefficient is exactly A+B+C+D−E−F, and its reversal formulas reduce this to 2(A+B+C). Its three trace-transposition formulas and its converse implication by perfect H³χ–K duality are correct. No mathematical correction to that final proof is required by this audit.

The updated dependency statement in its Section 1 is also respected here. The invariant Ext row is supplied independently by [the independently proved invariant row](https://github.com/Akilleez-QA/read-em-and-weep/blob/2b03992b32d2f5cf0509b6f4840adf08369f54b7/research/hm/cubic-loci/foundation-p01/INVARIANT-COHOMOLOGY.md), which was read for this audit. The older relative theorem labels that dimension input D; its historical numerical source is not being reintroduced. The independently identified presentation, published classical cohomology result, family, and relative local-freeness/base-change arguments remain inherited inputs rather than new certifications in this formal audit.

As in the underlying canonical-detector proof, Dolbeault calculations are made over the complex numbers; their claimed characteristic-zero scope uses the stipulated algebraic comparison and scalar-extension/descent statements. No Dolbeault complex over an arbitrary unrelated characteristic-zero field is intended.

## Verdict

The proposed shortcut is correct, with the following necessary qualifications.

1. Every central class in full-sign degree two extends **locally** along the stipulated coefficient family because its relative degree-two cohomology is a vector bundle with base change. This is existence of a section through the class, not a canonical, flat, or horizontal extension.
2. The vanishing of all ordered invariant products implies that every full-sign degree-two class annihilates the invariant degree-one space on both sides. Perfect degree-three/full-sign versus degree-one/invariant duality is essential here.
3. The mixed Massey operations are single-valued only when representatives and primitives have the prescribed deck characters. Their indeterminacies vanish because of the preceding annihilation result for **all** full-sign degree-two classes.
4. The two proposed adjugation signs and the proposed second-order relation are correct.
5. All three terms in that second-order relation transpose with a positive sign to the three specified invariant triple Massey terms. The resulting relation is exactly the already established cyclic relation after outer reversal. This argument supplies no additional vanishing of the canonical triple detector.

This audit uses only formal DGA reasoning and the premises in the three specified documents. It evaluates no source, model, matrix rank, polynomial instance, point, jet, residual, or detector.

## 1. Setup and the scalar trace issue

Let A be the deck-graded Dolbeault endomorphism DGA, let 1 denote the trivial deck character, and let χ be the full-sign character. Write

    K = H¹(A)₁,
    T = H²(A)₁,
    V = H²(A)χ,
    L = H⁴(O_X)χ.

The imported inputs are K·K=0 and perfect trace/Serre pairings

    H³(A)χ × K → L,
    V × T → L.

The target L is one-dimensional. Choosing the stipulated volume form identifies it with the ground field, but this choice is unnecessary for any sign calculation below.

One must distinguish endomorphism cohomology from scalar cohomology:

    H³(A)χ has dimension 79,
    H³(O_X)χ = 0.

The second equality does not assert that the first space vanishes. For X=C⁴, Künneth identifies scalar degree-j cohomology with the sum of the deck characters supported on j-element subsets of the four factors. The full-sign character occurs only in degree four. Consequently

    H²(O_X)χ = H³(O_X)χ = 0,
    H¹(O_X)₁ = H²(O_X)₁ = 0.

Trace and scalar inclusion commute with the differential and with deck projectors. Thus classes in K and V have closed trace-free representatives in their own character sectors. For rank two, adjugation is

    τ(u) = tr(u)·I − u.

It therefore induces −id on K, T, V, and H³(A)χ. The last assertion uses specifically the scalar vanishing H³(O_X)χ=0.

## 2. All mixed ordinary products vanish

Take R∈V and a,b∈K. Associativity gives

    ⟨Ra,b⟩ = [tr(Rab)] = 0,

because ab=0 in cohomology. Since the pairing H³(A)χ×K is perfect, Ra=0.

For the other order, graded trace cyclicity gives

    [tr(aRb)] = (−1)^(1·(2+1)) [tr(Rba)]
              = −[tr(Rba)] = 0.

The same perfect pairing yields aR=0. Hence

    V·K = K·V = 0.

This conclusion holds for every class of V. It does not rely on R being the particular actual residual, and it does not require choosing an extension of R first.

## 3. Canonical mixed operations and their indeterminacy

For homogeneous closed cochains x,y,z of degrees p,q,r, respectively, use

    m(x,y,z) = [x h_yz + (−1)^(p+1) h_xy z],
    d h_xy = xy,
    d h_yz = yz.

The defining expression is closed by the Leibniz rule. Choose every primitive in the product character sector. Such primitives exist whenever the corresponding product class vanishes: apply the appropriate deck projector to any primitive.

For R∈V and a,b∈K the formulas become

    m(R,a,b) = [R h_ab − h_Ra b],
    m(a,R,b) = [a h_Rb + h_aR b],
    m(a,b,R) = [a h_bR + h_ab R].

All take values in H³(A)χ. Their possible primitive indeterminacies are, respectively,

    R·K + V·b,
    a·V + V·b,
    a·V + K·R.

Each is zero by Section 2. In particular, it would be insufficient merely to cite H¹(A)χ=0: the potentially varying mixed primitives have degree two, and it is V·K=K·V=0 that removes their ambiguity.

For completeness, the general representative-change checks are as follows. All cochains and corrections remain character-homogeneous.

* Replacing x by x+dξ and h_xy by h_xy+ξy changes the defining cocycle by d(ξh_yz).
* Replacing z by z+dζ and h_yz by h_yz+(−1)^q yζ changes it by (−1)^q d(h_xyζ).
* Replacing y by y+dυ, h_xy by h_xy+(−1)^p xυ, and h_yz by h_yz+υz leaves it unchanged.

Together with zero primitive indeterminacy, these identities prove representative independence. Linear choices of closed representatives and primitives make trilinearity explicit, and independence then removes the choices. Thus these are canonical trilinear mixed operations on the indicated cohomology spaces.

Allowing arbitrary primitives in the unrestricted endomorphism DGA would introduce other character sectors and their larger product indeterminacies. The restricted construction is indispensable.

## 4. Adjugation: the two reversal signs

For homogeneous forms,

    τ(uv) = (−1)^(|u||v|) τ(v)τ(u),
    dτ = τd.

Use trace-free representatives x,y,z. Primitives can be normalized by

    h_xy = (h⁰_xy + (−1)^(pq) τ(h⁰_yx))/2.

This preserves d h_xy=xy and gives

    τ(h_xy) = (−1)^(pq) h_yx.

Applying τ to the defining expression and using τx=−x, τy=−y, τz=−z gives the general formula

    τ m(x,y,z)
      = (−1)^(pq+pr+qr+p+r) m(z,y,x).

For degree patterns (2,1,1) and (1,1,2), the displayed exponent is even. Since τ=−id on the output H³(A)χ,

    m(a,b,R) = −m(R,b,a).

For degree pattern (1,2,1), the exponent is odd, so

    m(a,R,b) = m(b,R,a).

These are the proposed signs. There is no additional sign coming from the deck character: all multiplication and cyclicity signs above depend on cohomological degrees.

The primitive normalization is convenient for proving reversal, but is unnecessary in the subsequent extension calculation. Canonical independence allows one to use the family-supplied primitive there.

## 5. What relative local freeness actually permits

Using the presentation/family and relative base-change arguments of the relative-obstruction-locus proof, with its dimension premise D now supplied by the independent structural proof described above, the family has a locally free bundle V_B of full-sign degree-two cohomology, with arbitrary base change. For any central R∈V, a local trivialization of V_B gives a section through R. Pulling it back along a formal curve in the smooth coefficient base produces a cohomology class extending R to every Artinian order, in particular through order t².

This uses only the vector-bundle conclusion; it does not use the additional actual-source premise S. It concerns an arbitrary section through R, not a claim that the particular actual residual section is constant or has any specified derivative.

On an affine Artinian parameter base, the relative proof identifies such a section with a cohomology class of the pulled-back endomorphism complex. In a local G-equivariant smooth trivialization of the family, the complex can be written as the fixed underlying graded DGA with deformed differential

    d_η = d + [η, −],
    dη + η² = 0.

An equivariant trivialization is available locally: transport using a G-invariant smooth connection, obtained by averaging. A lifted cohomology representative may initially reduce to a different cocycle representing R; extending its degree-one correction and subtracting the corresponding deformed coboundary makes its central representative the chosen R itself. Thus the formal cocycle expansions used below are justified by relative lifting, rather than being an extra assumption about a canonical connection on cohomology.

No global extension on all of B, no uniqueness, no horizontal structure, and no vanishing of the extended class is asserted.

## 6. Second-order extension equation, including the closed correction

Fix a∈K and a formal family curve with tangent a. Use expansions with ordinary power-series coefficients, not divided powers:

    η(t) = t a + t²β + O(t³),
    R(t) = R + tρ + t²σ + O(t³).

Here the letters a and R also denote chosen closed cochain representatives. The Maurer–Cartan and cocycle equations give

    dβ = −a²,
    dρ = Ra − aR,
    dσ + aρ − ρa + βR − Rβ = 0.

Choose h_aa=−β. Choose any homogeneous h_Ra and h_aR with the prescribed differentials. Then

    ρ = h_Ra − h_aR + s,
    ds = 0,

for a full-sign degree-two cocycle s. It is not legitimate simply to omit this closed correction at the chain level. Its contribution to the cohomology of the last equation is [as−sa]=0 by Section 2, so it can be omitted after passing to cohomology.

Substituting gives

    0 = [aρ − ρa + βR − Rβ]
      = m(R,a,a) + m(a,R,a) − m(a,a,R).

Outer reversal turns the last term into +m(R,a,a). Hence

    2m(R,a,a) + m(a,R,a) = 0.

Polarizing in a and b gives

    2m(R,a,b) + 2m(R,b,a)
      + m(a,R,b) + m(b,R,a) = 0.

Using middle-position reversal symmetry and dividing by two yields exactly

    m(R,a,b) + m(R,b,a) + m(a,R,b) = 0.

This conclusion is independent of the choice of the family curve, the section extending R, all its derivatives, and all primitive choices. Their contributions have disappeared using canonical operations and the mixed product vanishing.

## 7. Trace transposition: three positive signs

Let c∈K. Write the pairings as cohomology classes of matrix traces in L. The invariant operation is

    M(a,b,c) = [a h_bc + h_ab c].

The first transposition follows from

    d tr(h_Ra h_bc)
      = tr(Ra h_bc + h_Ra bc).

Therefore

    ⟨m(R,a,b),c⟩
      = [tr(Rh_ab c − h_Ra bc)]
      = [tr(Rh_ab c + Ra h_bc)]
      = ⟨R,M(a,b,c)⟩.

Exchanging a and b gives

    ⟨m(R,b,a),c⟩ = ⟨R,M(b,a,c)⟩.

For the middle-position operation, first use graded cyclicity:

    tr(a h_Rb c) = −tr(h_Rb ca).

Then use the exact trace differentials

    d tr(h_Rb h_ca) = tr(Rb h_ca + h_Rb ca),
    d tr(h_aR h_bc) = tr(aR h_bc + h_aR bc).

The first converts the term −tr(h_Rb ca) into tr(Rb h_ca). The second converts tr(h_aR bc) into −tr(aR h_bc), which in turn equals tr(Rh_bc a) by graded cyclicity. Consequently

    ⟨m(a,R,b),c⟩
      = [tr(Rb h_ca + Rh_bc a)]
      = ⟨R,M(b,c,a)⟩.

Thus every transposition sign proposed in the question is positive. As an independent consistency check, the remaining placement obeys

    ⟨m(a,b,R),c⟩ = −⟨R,M(c,a,b)⟩,

in agreement with mixed reversal and invariant outer reversal.

## 8. Exact relation to the existing cyclic identity

Pairing the second-order mixed relation with c gives

    ⟨R, M(a,b,c) + M(b,a,c) + M(b,c,a)⟩ = 0.

Outer reversal identifies M(b,a,c)=M(c,a,b). Hence this is

    ⟨R, M(a,b,c) + M(b,c,a) + M(c,a,b)⟩ = 0,

which is precisely the already established cyclic-zero relation.

The equivalence is exact at this level:

* Existing cyclic-zero and the trace-transposition formulas imply the mixed second-order relation, because H³(A)χ×K is perfect.
* The mixed second-order relation for every R∈V implies cyclic-zero, because V×T is perfect.

Accordingly, this family-extension argument gives a second derivation of the same trilinear relation. It does not force individual ordered Massey values to vanish, does not annihilate their permitted [22] channel, and does not prove the actual residual is zero or detected. It also does not establish that no other geometric or higher-order constraints exist; only this specific second-order shortcut has been fully accounted for.

## Immutable public inputs

The proof's DEPENDENCIES.json binds the current public editions of the canonical Massey, invariant ordered-product, coefficient-family, invariant cohomology and relative obstruction-bundle theorems. Only the latter's geometric P,D vector-bundle conclusion is used, not its actual-source premise S. This audit is a formal cochain and sign review, not an actual source or detector calculation.
