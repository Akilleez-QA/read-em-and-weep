Publication context: this retained proof or audit may describe an intermediate bound or then-open branch. Read the unit overview for the current scope and later implications. Historical mathematical review is not a new formal verification.

# The length-ten wedge module is not a realizable canonical equivariant defect

## Result and scope

Let R be the completed regular local ring of dimension four at a canonical point, with the full stabilizer H described in length-two-local-defect/PROOF.md. Write W=m/m², choose equivariant linear parameters, and let

    P=W ⊕ Λ²W,     x·v=x∧v,     x·s=0,
    D(N)=Ext⁴_R(N,R).

For every one-dimensional H-representation χ, the finite module

    Qχ=D(P)⊗χ

cannot be Ext²_R(M,R) for an H-equivariant rank-two reflexive module M, free off the closed point, with equivariantly trivial determinant.

This excludes only the specified wedge module and all its character twists. It does not exclude all length-ten defects or change the established global lower bound 300. The wedge module remains a valid counterexample to the proposed blanket numerical claim β3(Q)−2β4(Q)≥3. The new obstruction concerns realizability as an Ext² defect, not existence of an equivariant finite module.

## 1. An equivariant equality-case condition

Let Q=Ext²_R(M,R), A=Ext¹_R(M,R), and b_i=β_i(Q). Rank-two equivariantly trivial determinant gives the equivariant self-duality M≅M*. The natural isolated local duality then gives

    A≅D(Q).

For completeness, this identity is obtained by dualizing a free resolution and dimension shifting in its kernels and images, as in rank-eight-isolated-singularity/PROOF.md §1. All maps are equivariant, so there is no additional character in this identity.

Choose an equivariant minimal free resolution

    0 → F2 → F1 → F0 → M → 0.

Such resolutions exist: take an H-equivariant section of the finite-dimensional generator quotient at each step by averaging. Put J=im(F1*→F2*), K=ker(F1*→F2*), and C=im(F0*→F1*). There are equivariant exact sequences

    0 → J → F2* → Q → 0,
    0 → K → F1* → J → 0,
    0 → C → K → A → 0.

Minimality gives rank F2=b0. The free cover F1*→J has b1 minimal columns and u additional columns for some u≥0. Nonequivariant column operations split off u zero columns, so

    rank F1=b1+u,
    rank F0=2+b1+u−b0,
    μ(K)=b2+u.

Only these numerical statements need the splitting; we do not presume that the extra summands have trivial H-linearization. Finite duality reverses Betti numbers, giving μ(A)=b4. Hence

    b2+u−b4 ≤ μ(C) ≤ 2+b1+u−b0.              (1)

The finite-length Euler identity is b0−b1+b2−b3+b4=0. If

    b3−2b4=2,

the two extremes in (1) coincide. In particular μ(C)=μ(K)−μ(A). The exact sequence on generator spaces

    C/mC → K/mK → A/mA → 0

then forces its first map to be injective: its image has dimension μ(K)−μ(A)=μ(C). The Tor sequence therefore forces a surjection

    Tor₁^R(K,k) → Tor₁^R(A,k).                (2)

The two earlier exact sequences, whose middle terms are free, give a natural equivariant dimension-shifting isomorphism

    Tor₁^R(K,k) ≅ Tor₃^R(Q,k).

This holds even if the presentation has extra free summands; no equivariant choice of their splitting is required. Also β1(A)=b3 by finite duality, so source and target of (2) have the same dimension. We obtain the necessary equivariant isomorphism

    Tor₃^R(Q,k) ≅ Tor₁^R(D(Q),k).             (3)

Equivalently, Tor₁(D(Q),k) must be self-dual as an H-representation, by the exact equivariant Betti reversal below.

## 2. Duality and line twists, with conventions fixed

For a finite-length equivariant module N, a minimal equivariant free resolution E• of length four has dual complex exact except in degree four, where its cokernel is D(N). Reading that dual complex in reverse gives a minimal resolution of D(N). Thus, as actual H-representations,

    Tor_i(D(N),k) ≅ Tor_(4−i)(N,k)*.           (4)

There is no omitted determinant factor in (4): D is Ext⁴(-,R), not the unshifted vector-space dual. For example D(k)=k⊗(det W)*, already incorporating the canonical character. Likewise double duality gives D(D(N))≅N, and

    D(N⊗χ)≅D(N)⊗χ⁻¹.

One can also identify D(N) with the vector-space dual twisted by (det W)* in this formal setting; that convention must not be applied a second time to (4).

The established wedge calculation gives β0(P)=4 and β1(P)=10, so Qχ has b4=4, b3=10, and b3−2b4=2. Furthermore

    Tor₁(P,k)≅Sym²W.                         (5)

Indeed, the degree-one Koszul cycles in the top component W⊗W are exactly the kernel of wedge multiplication, Sym²W. The entire bottom component Λ²W⊗W is killed in homology because the top degree-two differential W⊗Λ²W→Λ²W⊗W is an isomorphism. That invertibility was proved in length-ten-local-defect/PROOF.md §2 by writing its flipped form as I−JA, with AJ=3I.

For Qχ, equations (4) and (5) give

    Tor₃(Qχ,k)≅(Sym²W)*⊗χ,
    D(Qχ)≅P⊗χ⁻¹,
    Tor₁(D(Qχ),k)≅Sym²W⊗χ⁻¹.

Consequently realizability would require

    (Sym²W)*⊗χ ≅ Sym²W⊗χ⁻¹.                 (6)

Equivariantly trivial determinant of M is used precisely for A≅D(Q); it is not being inferred from nonequivariant determinant triviality. No change to that hypothesis is needed in the theorem.

## 3. The full stabilizer defeats the necessary isomorphism

The full stabilizer has

    H=μ5 × (B⋊C4),       B=⟨Z,D⟩≅C5²,
    gZg⁻¹=Z³,           gDg⁻¹=D⁴.

Every character χ of H restricts trivially to B: evaluating either conjugation relation in a character gives χ(Z)=χ(Z)³ and χ(D)=χ(D)⁴, and these fifth roots must be one. This includes all central μ5 characters; no descent to the projective stabilizer has been assumed.

Choose the weight convention in which the four B-weights of W are

    (i,i²/2),       i∈F5×.

The other usual cotangent/pullback convention simultaneously negates all these weights and gives exactly the dual calculation below, with the same contradiction. We compute weights modulo five, where 1/2=3. In Sym²W:

- The four squares have weights (2i,i²). Writing a=2i gives (a,4a²), for each a≠0.
- The two opposite-index products have weights (0,1) and (0,4).
- The remaining four unordered products have weights (a,0), for each a≠0. Indeed their indices have ratio 2 or 3, so their squared indices sum to zero.

Thus the weight multiset is

    {(a,4a²):a≠0} ∪ {(a,0):a≠0} ∪ {(0,1),(0,4)}.

Dualizing negates both entries, giving instead

    {(a,a²):a≠0} ∪ {(a,0):a≠0} ∪ {(0,1),(0,4)}.

These multisets differ: for instance (1,4) occurs in the former and not the latter. Hence Sym²W and (Sym²W)* are not isomorphic even after restriction to B. Since χ|B is trivial, equation (6) is impossible for every H-character χ.

This proves the asserted family exclusion.

## 4. What has and has not changed

The equality case of the numerical generator bound has a representation-level necessary condition, which the natural wedge module violates at the full canonical stabilizer. The order-twenty subgroup alone forgets the second B-weight and does not exhibit this contradiction.

No universal strict numerical Betti bound has been restored: Qχ really is an equivariant finite module with β3−2β4=2. Other length-ten modules have not been classified or excluded. No rank instance or actual defect has been computed or realized.

Inputs: length-ten-local-defect/PROOF.md and AUDIT.md (wedge construction and Betti calculation); length-five-local-defect/PROOF.md §1 (generator bound); length-two-local-defect/PROOF.md §1 (full stabilizer); minimal-local-defect-character/PROOF.md §1 and rank-eight-isolated-singularity/PROOF.md §1 (natural equivariant local duality).

All calculations use universal representations and local algebra only. No physical source/model matrix, operation, chosen input, rank instance, jet, or residue was evaluated. 
