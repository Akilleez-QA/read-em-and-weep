Publication context: this retained proof or audit may describe an intermediate bound or then-open branch. Read the unit overview for the current scope and later implications. Historical mathematical review is not a new formal verification.

# Exclusion of length-six isolated rank-two defects

## Theorem and scope

Let R be a regular local complex ring of dimension four at a fixed point of a finite group H. Let M be an H-equivariant reflexive R-module of rank two, free off the closed point, with equivariantly trivial determinant. Suppose H contains G=C5⋊C4 such that W=m/m² restricts to the irreducible four-dimensional G-representation V: its clock weights are the four distinct nontrivial C5 characters and C4 permutes their lines transitively. Then

    length_R Ext²_R(M,R) ≠ 6.

Only the order-twenty subgroup is needed. The full canonical stabilizer imposes further constraints but is unnecessary here. This theorem makes no existence or nonexistence assertion for local lengths seven or larger.

## 1. Audited necessary inequality

Put Q=Ext²_R(M,R). The isolated rank-two self-duality and free-cover argument in ../length-five-local-defect/PROOF.md, Section 1 (independently audited there), give

    β2(Q) − μ(D(Q)) ≤ 2 + β1(Q) − β0(Q),
    D(Q)=Ext⁴_R(Q,R).

Finite-length duality reverses a minimal free resolution over R, so μ(D(Q))=β4(Q). Since Q has rank zero, its resolution has alternating rank sum zero:

    β0−β1+β2−β3+β4=0.

Consequently the necessary inequality is equivalently

    β3(Q) ≤ 2β4(Q)+2.                         (1)

All these numbers ignore equivariant character twists. We will show that every equivariant length-six Q violates (1).

Completion preserves the invariants in question. Over the completion, averaging a section of m→W gives an equivariant regular-parameter space W inside m. Thus multiplication and its induced maps on radical layers are G-equivariant. In particular

    W ⊗ (m^jQ/m^(j+1)Q) → m^(j+1)Q/m^(j+2)Q

is surjective.

## 2. Exhaustive radical-filtration classification

The irreducibles of G are its four characters, all clock-trivial, and the unique four-dimensional representation V. This is proved directly by the orbit-of-clock-weights argument in ../length-five-local-defect/PROOF.md, Section 2. Therefore a length-six Q is either entirely clock-trivial, or, as a G-representation,

    Q ≅ V ⊕ U,       dim U=2, with U clock-trivial.

If Q is entirely clock-trivial, multiplication W⊗Q→Q is zero by clock weights. Then Q=k^6, with β3=24 and β4=6, violating (1).

More generally, every module with mQ=0, irrespective of its G-representation, has underlying R-module k^6 and the same contradictory Betti numbers. This also excludes the semisimple case containing V.

Assume henceforth Q contains V and mQ≠0. Write L_j=m^jQ/m^(j+1)Q. Since G is finite over C, each layer is semisimple, and exactly one layer L_s contains the single constituent V. Every other constituent of every layer is a character. A map W⊗U_1→U_2 between clock-trivial representations U_1,U_2 is zero. Thus two consecutive nonzero layers cannot both be clock-trivial. The layers before the terminal zero layer are nonzero by Nakayama. It follows that s is zero or one and there are at most three nonzero layers.

If three layers occur, the first and third each contain at least one character. The entire supply of character dimensions is two, so the dimensions and constituents are exactly

    (L0,L1,L2)=(character,V,character),        m³Q=0.    (2)

Otherwise m²Q=0. Put T=Q/mQ and S=mQ; multiplication induces a surjection W⊗T→S. There are exactly these possibilities:

(a) S contains V. Then T is clock-trivial. Since W⊗T is a sum of copies of V (tensoring V by a G-character leaves it isomorphic to V), S cannot contain a character. Hence (dim T,dim S)=(2,4).

(b) T contains V. Then S is clock-trivial of dimension r=1 or 2, and T consists of V and 2−r characters. Hence (dim T,dim S)=(5,1) or (4,2).

This exhausts nonzero square-zero actions, including possible residue-field direct summands. No claim about uniqueness of their multiplication pairings is needed.

## 3. Square-zero modules: Koszul rank bounds

For an arbitrary square-zero module with a vector-space splitting Q=T⊕S, parameters kill S and send T into S. In the Koszul complex of the four parameters with coefficients in Q, let

    d_i: T⊗Λ^iW → S⊗Λ^(i−1)W,       r_i=rank(d_i).

The entire differential vanishes on S⊗Λ^iW. Hence, writing r_5=0,

    β_i(Q)=6 binom(4,i)−r_i−r_(i+1).

In particular

    β3=24−r3−r4,       β4=6−r4.

Thus (1) would require

    10+r4 ≤ r3.                                  (3)

For case (a), the source of d_3 has dimension 2·4=8. Therefore r3≤8, contradicting (3) because r4≥0.

For case (b), the clock-trivial part of T is annihilated by all parameters. On its V constituent, the common kernel of all parameter multiplication maps is a G-invariant subspace. The action on V is nonzero because W⊗T→S is surjective and S≠0, so irreducibility makes that common kernel zero. The kernel of d_4 is precisely the common parameter annihilator in T, tensored with the one-dimensional Λ⁴W: in a parameter basis the four coefficients of d_4 lie in the four independent basis vectors of Λ³W. Consequently r4=4. The target of d_3 has dimension r·6≤12, so r3≤12. Equation (3) would require r3≥14, a contradiction.

Every square-zero possibility is excluded.

## 4. Three layers: cyclic Gorenstein and too many relations

Consider (2). Its one-dimensional top makes Q cyclic by Nakayama. Thus Q≅A=R/I as an underlying R-module, with Hilbert function (1,4,1) and m³A=0. Its radical layers have G-representations character, V, character; the cyclic generator may be chosen in a character complement to mQ.

Multiplication gives a nonzero pairing

    W ⊗ L1 → L2.

It is nonzero since m²Q=L2≠0. Its common kernel in L1 is G-invariant and therefore zero by irreducibility. It follows that the socle of Q is exactly m²Q and has dimension one: a socle vector in mQ maps into that common kernel, hence is in m²Q; a socle vector outside mQ would generate Q and make mQ=0, a contradiction. Equivalently, the multiplication quadratic form on mA/m²A is nondegenerate.

For completeness the resulting finite duality is elementary. Choose a complex linear functional λ:A→C nonzero on its one-dimensional socle. The map

    A → Hom_C(A,C),     a ↦ (b ↦ λ(ab))

is injective: any nonzero principal ideal aA contains a nonzero socle element (multiply by the maximal ideal to the last nonzero stage), on which λ is nonzero. Equal dimensions make it an isomorphism. The finite R-dual D(A) is isomorphic as an underlying R-module to Hom_C(A,C), up to the irrelevant one-dimensional canonical factor. Thus D(A)≅A. Reversing a minimal free resolution yields

    β3(A)=β1(A),       β4(A)=β0(A)=1.             (4)

Finally I⊂m² since the embedding dimension of A is four. The surjection m²/m³→m²A has one-dimensional image, whereas dim m²/m³=10. Its kernel is (I+m³)/m³, of dimension nine. Since mI⊂m³, the natural map

    I/mI → (I+m³)/m³

is surjective. Therefore β1(A)=μ(I)≥9. Equations (4) contradict (1), which would require β3(A)≤4.

This excludes the final case and proves the theorem.

## 5. Conditional global consequence

Combine this theorem with the separately audited exclusions of local lengths one through five and the unique canonical orbit of size thirty below the orbit-size threshold 250. On the stipulated actual-rank-eight branch, the nonzero finite defect T=Ext²(B,O) now satisfies

    length(T) ≥ 210.

Indeed canonical support has local length at least seven and hence contributes at least 30·7=210; any noncanonical orbit contributes at least 250. If 0<length(T)<250, the only remaining necessary values are

    length(T) ∈ {210,240},

corresponding to canonical local lengths seven and eight. The same numerical restrictions transfer to the saturation defect by the previously audited finite duality. In notation length(T)=5q, this says q≥42 and 0<q<50 implies q∈{42,48}.

These are necessary restrictions only. They neither realize the remaining lengths nor exclude the rank-eight branch.

## Dependencies and evidence boundary

Read ../length-two-local-defect/PROOF.md and AUDIT.md, and ../length-five-local-defect/PROOF.md and AUDIT.md. Their local-duality, subgroup-representation, and global orbit-gap inputs are used as expressly identified above. Every new step is universal local algebra or abstract representation theory. No physical source/model matrices, operation, chosen input, actual rank instance, jets, or residue evaluation were used. No source-app, repository, upstream, installation, or large computation was performed.
