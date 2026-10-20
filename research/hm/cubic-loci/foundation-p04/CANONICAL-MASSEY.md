# Canonical invariant ordered triple Massey operation

## Result and limits

Assume the ordered-product lemma in [the quadratic yoneda exclusion manuscript](../foundation-p01/ORDERED-PRODUCTS.md): K·K=0, where K=Ext¹(E,E)^G is the 79-dimensional invariant tangent space. There is a canonical trilinear map

    M: K⊗K⊗K → T=Ext²(E,E)^G.

It is the invariant ordered triple Massey operation, with sign convention

    M(a,b,c)=[α hβγ+hαβ γ],     d hαβ=αβ.

It is equivariant for S4 and the established inversion action ι. Rank two forces outer reversal symmetry, and the actual smooth family forces the polarized cubic relation:

    M(a,b,c)=M(c,b,a),
    M(a,b,c)+M(b,c,a)+M(c,a,b)=0.

These constraints leave a representation-theoretically eligible [22], ι-positive channel. They do not prove that the geometric operation, its projection to that channel, or its pairing with the retained obstruction is nonzero. Nor is there a completeness statement for these identities among all possible geometric constraints.

The construction MUST be performed in the invariant DGA, or equivalently with invariant representatives and primitives. Arbitrary primitives in the unrestricted DGA can change the class by a·Ext¹+Ext¹·c; K·K=0 alone does not kill this larger indeterminacy.

## 1. Invariant DGA and existence

Over C use A=(A^{0,*}(End E), ∂̄)^G. The finite group acts by DGA automorphisms. Averaging is exact, so H*(A)=Ext*(E,E)^G. In particular H¹(A)=K. The scalar subcomplex C=(A^{0,*}(O))^G has H¹(C)=H²(C)=0 because the quotient is Y=(P¹)^4.

Choose closed α,β,γ in A¹ representing a,b,c. Vanishing of their cohomological products supplies hαβ,hβγ in A¹ with d hαβ=αβ and d hβγ=βγ. The Leibniz rule gives

    d(α hβγ+hαβ γ)=−αβγ+αβγ=0.

Changing the primitives by closed u,v changes the class by a[v]+[u]c=0. Thus the class is independent of both primitives, even though the primitives themselves need not be canonical.

## 2. Representative independence, linearity, and model independence

It suffices to change one representative at a time. All cochains below lie in A, and x,y,z have degree zero.

* Replace α by α+dx, and hαβ by hαβ+xβ. The defining cocycle changes by d(x hβγ).
* Replace γ by γ+dz, and hβγ by hβγ−βz. The defining cocycle changes by −d(hαβ z).
* Replace β by β+dy, hαβ by hαβ−αy, and hβγ by hβγ+yγ. The defining cocycle is unchanged.

Each displayed new primitive has the required differential. Subsequent arbitrary primitive choices do not change the class by Section 1. If two invariant representatives differ by a boundary in the unrestricted complex, averaging a primitive makes the boundary primitive invariant. This proves independence in H¹(A), without requiring a canonical section of cocycles.

Choose a linear section s:K→Z¹(A). Since products of its values are boundaries, choose a linear right inverse of d:A¹→B²(A), with section direction B²(A)→A¹, on the span of these products. The resulting h(a,b) is bilinear; the displayed formula for M is then trilinear. Independence already proved removes dependence on both linear sections. This argument proves linearity rather than merely additivity modulo a varying indeterminacy.

A DGA morphism transports representatives, primitives, and the defining cocycle. Consequently this singleton Massey operation is natural under DGA quasi-isomorphisms. Multiplicative Čech–Dolbeault comparison, through the total Čech–Dolbeault DGA, identifies it with the algebraic derived-endomorphism operation. It is not a new choice of a minimal A∞ model; it is the choice-independent class determined by a vanishing-product domain.

## 3. Geometric equivariance

Any DGA automorphism preserving A sends a defining system for (a,b,c) to one for its transformed triple. Uniqueness gives

    g M(a,b,c)=M(ga,gb,gc).

This applies to geometric S4 and to the stipulated projective inversion lift: conjugation provides the coherent action on End E, scalar ambiguities cancel, and inversion preserves/normalizes the deck invariants. On K and T its square is the action of simultaneous deck inversion, hence is the identity. No extra permutation sign is inserted into this naturality formula. The order of the three arguments is a separate S3 bookkeeping symmetry, not the geometric S4 action.

## 4. Rank-two outer reversal identity

Define the rank-two adjugation τ(u)=tr(u)·I−u on End-valued forms. The matrix identity adj(AB)=adj(B)adj(A), together with exterior signs, implies for homogeneous forms

    τ(uv)=(-1)^{|u||v|}τ(v)τ(u),    τ²=id,    dτ=τd.

This is a graded anti-automorphism; τ is NOT claimed to be an ordinary DGA automorphism. Trace and scalar inclusion are global, so τ needs no chosen determinant trivialization and commutes with geometric symmetries.

Because H¹(C)=0, choose a linear trace-free section s:K→Z¹(A), so τα=−α. Start with bilinear primitives h⁰(a,b) and replace them by

    h(a,b)=(h⁰(a,b)−τ h⁰(b,a))/2.

Indeed τ(βα)=−αβ, hence d h(a,b)=αβ; also τ h(a,b)=−h(b,a). Applying τ to the defining cocycle gives

    τ(α h(b,c)+h(a,b)γ)=−h(c,b)α−γ h(b,a).

Therefore τ M(a,b,c)=−M(c,b,a). On H²(A), however, τ acts as −id because its difference from −id factors through H²(C)=0. Combining these two identities proves

    M(a,b,c)=M(c,b,a).

Equivalently, the symmetric part of h(a,b) is trace-free and the antisymmetric part is scalar. This is the precise chain-level normalization behind the odd-form Cayley–Hamilton argument. No claim that each primitive is trace-free is made.

## 5. Exactly what smoothness proves here

The actual algebraic family of holomorphic bundles on fixed X has a smooth 79-dimensional parameter space and tangent image K. A family merely of underlying smooth bundles would not suffice here. For each a in K, pull it back along a formal one-parameter curve with that tangent. In a fixed smooth trivialization the induced Dolbeault deformation satisfies the Maurer–Cartan equation and has expansion

    η(t)=tα+t²b+t³c+…,   dη+η²=0.

Its first three equations are dα=0, db=−α², dc=−(αb+bα). The representative α can be chosen invariant by the representative-independence statement. Equivalently, first change the smooth trivialization to arrange the chosen α. Then averaging b and c over G preserves these equations because α is invariant. Hence h(a,a)=−b is an allowed invariant primitive and

    M(a,a,a)=[−αb−bα]=[dc]=0.

This uses the third-order lift in the actual family, not merely vanishing of the quadratic obstruction. Polarization of the trilinear map gives

    Σ_{σ∈S3} M(aσ(1),aσ(2),aσ(3))=0.

Outer reversal identifies the six summands in three equal pairs, giving the cyclic relation stated above. The implication is not that each ordered Massey value vanishes. The deformation-theoretic cubic obstruction is the fully symmetric combination; it is different from an ordered triple operation.

The source quotient is

    Q=K^⊗3 / ⟨a⊗b⊗c−c⊗b⊗a,
                    a⊗b⊗c+b⊗c⊗a+c⊗a⊗b⟩.

As a functor of K in characteristic zero, Q is one copy of the Schur functor S_(2,1)K. More explicitly, quotienting by reversal first removes the alternating S3 representation and retains one line in each standard S3 representation; the cyclic relation removes the symmetric representation. This is an argument-permutation statement. It is not a statement that the geometric S4 representation is [21], nor does the source quotient have a residual canonical S3 action by every permutation.

## 6. A [22], inversion-positive channel survives these constraints

The established equivariant Kodaira–Spencer identification is

    K ≅ (W⊗C⁵)/C v,    W=(C²)^⊗4,

where S4 permutes the four C² factors and acts trivially on C⁵, inversion acts by J^⊗4⊗R, J interchanges the two basis vectors, R reverses five coordinates, and v is invariant and inversion-positive. The classical tensor decomposition gives

    W = Sym⁴(C²)⊗[4]
      ⊕ (Sym²(C²)⊗det)⊗[31]
      ⊕ det²⊗[22].

On det², J acts as +1; R has positive eigenspace of dimension 3. Thus K contains three copies of geometric [22] with inversion +. It also contains positive trivial vectors: on Sym⁴(C²), J has positive/negative dimensions 3/2, and R has 3/2, so the positive trivial multiplicity before removing Cv is 3·3+2·2=13, and afterwards is 12.

The existing invariant H² target has [22], inversion-positive multiplicity 12, by the independently established inversion eigenspace theorem and equivariant Serre duality. It is therefore nonzero.

To see directly that the two proved argument identities permit such a target, select a positive trivial line Ct in K, a positive copy U≅[22] in K, equivariant projections ℓ:K→C and P:K→U with ℓ(t)=1, and an equivariant nonzero φ:U→T_[22],+. Semisimplicity supplies these choices. The abstract tensor map

    F(a,b,c)=ℓ(a)ℓ(b)φ(Pc)+ℓ(b)ℓ(c)φ(Pa)
             −2ℓ(a)ℓ(c)φ(Pb)

is S4- and inversion-equivariant, obeys reversal and cyclic-zero, and satisfies F(t,t,u)=φ(u). Thus Hom_{S4×⟨ι⟩}(Q,T_[22],+) is nonzero. This is a formal representation-theoretic witness, not an evaluation of M or of any geometric source/model.

Accordingly

    D₃ = e_[22] · (1+ι)/2 · M

is a well-defined canonical candidate higher detector. Pairing its values with the full-deck [22], inversion-positive obstruction sector uses the established trace/Serre pairing. The pairing has value character sgn under S4. On D8, the physical retained class has character ε=sgn|D8; its dual detector therefore has the TRIVIAL D8 character, not ε. Since [22]|D8=1⊕ε, the canonical detector for that retained sector is e_D8,triv D₃. The target of D₃ is the full 24-dimensional [22], inversion-positive isotypic space; the target after e_D8,triv is 12-dimensional and pairs with the physical retained ε line tensored with its 12-dimensional positive multiplicity space. Here e_D8,triv=(1/8)Σ_{g∈D8}g. None of this proves a nonzero detector value, separation of that 12-dimensional retained space, or nonvanishing of the geometric map D₃.

The formal witness proves only that the rank-two reversal identity and the smooth-family polarized cubic identity do not themselves force the map to vanish. A theorem that all rank-two DGAs with these additional geometric hypotheses have nonzero M, or that no further rank-two/geometric identities exist, is neither needed nor asserted.

## 7. Algebraic scope and evidence boundary

Over the stipulated rational field of definition, use an algebraic derived-endomorphism DGA (for example an invariant Čech model). Since K·K=0, the same defining-system argument constructs the canonical operation there. Its formation commutes with scalar extension: one may transport a chosen linear section and primitives, and the resulting class is independent of them. Comparison over C proves the reversal and smoothness identities for this algebraic map. Faithful flatness descends vanishing identities; inversion is included after adjoining its stipulated field of definition, Q(i). The claims concern these stipulated base-changed data, not arbitrary unrelated characteristic-zero forms.

Static inputs read: the ordered-product addendum; the translation bundle deformations manuscript (MIXED-YONEDA-PRIMITIVE.md) (background on primitives, not a claimed primitive for all 79 directions); [the projective target directions manuscript](../foundation-p01/INVARIANT-COHOMOLOGY.md); and [the inversion eigenspaces manuscript](../foundation-p03/INVERSION-EIGENSPACES.md). No source/model/rank/polynomial-instance/point/jet/residual evaluation or execution, large computation, external write, or local Codex was used. Formal power-series coefficient equations above express the already-existing smooth family; no instance of it was evaluated.
