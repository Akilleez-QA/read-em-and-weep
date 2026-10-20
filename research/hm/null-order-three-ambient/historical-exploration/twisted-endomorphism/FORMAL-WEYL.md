# Continuous derivations of the completed matrix Weyl algebra

## Precise result

Let k be a field of characteristic zero and let D be the weighted formal Weyl algebra on q_1,...,q_n,p_1,...,p_n,h, with

    [p_i,q_j] = h delta_ij,   [q_i,q_j]=[p_i,p_j]=0,   h central.

Complete the polynomial Weyl algebra for the descending weighted-degree filtration, assigning deg(q_i)=deg(p_i)=1 and deg(h)=2. In normal ordering q^alpha p^beta h^c, c>=0, D is the vector space of all formal series in these monomials. Multiplication is the continuous Weyl multiplication. Put C=Mat_r(D), with its entrywise weighted topology and ordinary matrix multiplication.

Write Der_cont,k[[h]](C) for k[[h]]-linear continuous derivations C->C. Continuity is for this weighted formal topology, not an unspecified operator topology, and no preservation of the augmentation ideal or of each filtration level is imposed. Then there is an exact sequence of Lie algebras

    0 -> h^(-1) k[[h]] I_r
      -> L := h^(-1)D I_r + Mat_r(D)
      --ad--> Der_cont,k[[h]](C)
      -> 0.

The bracket on L is the ordinary commutator in Mat_r(D[h^(-1)]), and ad(x)(y)=[x,y]. The sum defining L is not direct. Elements have at most the displayed scalar simple pole. Equip this lattice with its induced shifted weighted topology; the assertion of exactness is algebraic, and every displayed adjoint action is continuous.

This proves the required local derivation statement for this precise formal Weyl model. It does not prove that a given quantization is isomorphic to this model, nor construct a Harish–Chandra torsor or a period comparison.

## 1. Completion and the scalar commutator identities

Finite weight truncations have finitely many monomials. Weyl multiplication respects total weight, so multiplication of formal series is defined in each truncation and hence in the inverse limit. The normal-symbol description identifies the underlying vector space with k[[q,p,h]], with the weighted topology equivalent to its ordinary formal topology. This is a description of the vector space and topology, not a claim that multiplication is commutative.

The exact identities

    [f,q_i] = h partial_(p_i) f,
    [f,p_i] = -h partial_(q_i) f

hold first on polynomials and then on the completion by continuity. All h-adic divisions used below are justified by h-torsion-freeness. The scalar algebra satisfies [D,D] subset hD, although C does not satisfy [C,C] subset hC when r>1.

Every x=h^(-1)f I_r+S in L acts integrally on C: the scalar commutator is divisible by h, and S is integral. Moreover this adjoint action is continuous. For example, subtracting the q,p-independent part of f changes no adjoint action; the remaining f has weighted order at least one, and h^(-1)ad(f) lowers weighted order by at most one. Matrix ad(S) does not lower weight. The bracket closure of L follows from

    [h^(-1)f I,h^(-1)g I]=h^(-2)[f,g] I in h^(-1)D I,
    [h^(-1)f I,S]=h^(-1)[f I,S] in Mat_r(D).

## 2. Matrix units remove the matrix part

Let delta be a continuous k[[h]]-linear derivation of C, and let e_ij be the constant matrix units. Define

    S = sum_i delta(e_i1) e_1i in C.

Then [S,e_kl]=delta(e_kl). Indeed,

    S e_kl = delta(e_k1)e_1l,

while differentiation of e_kl e_i1=delta_li e_k1, followed by right multiplication by e_1i and summation, gives

    delta(e_kl) + e_kl S = delta(e_k1)e_1l.

Consequently delta'=delta-ad(S) kills all e_ij. Since aI commutes with every matrix unit, delta'(aI) also commutes with all matrix units. Their centralizer in Mat_r(D) is precisely the scalar diagonal copy D I (whose coefficients need not be central in D). Hence

    delta'(aI)=d(a) I

for a unique continuous k[[h]]-linear derivation d of D. Using a e_ij=(aI)e_ij shows that delta' acts entrywise by d. Thus it remains to prove d=h^(-1)ad(f).

This argument does not assume all derivations of an arbitrary coefficient algebra are inner. The next step is specific to the formal Weyl algebra and its topology.

## 3. Formal Poincare lemma supplies the scalar Hamiltonian

Set

    a_i=d(q_i),   b_i=d(p_i).

Apply d to the defining commutators. The exact identities in Section 1 and d(h)=0 yield

    partial_(p_j) a_i = partial_(p_i) a_j,
    partial_(q_j) b_i = partial_(q_i) b_j,
    partial_(p_j) b_i + partial_(q_i) a_j = 0.

Therefore the formal one-form in the COMMUTATIVE normal-symbol vector space

    alpha = sum_i (-b_i dq_i + a_i dp_i)

is closed relative to k[[h]]. The use of commutative symbols here is legitimate because the preceding commutator identities involve the ordinary formal partial derivatives exactly, not merely modulo h.

The formal Poincare lemma over k[[h]] gives a formal series f with df=alpha, unique modulo k[[h]]. One explicit choice is the radial primitive

    f(q,p,h)= integral_0^1 sum_i
       (-q_i b_i(tq,tp,h) + p_i a_i(tq,tp,h)) dt.

The integral means division by the positive integer m+1 on each homogeneous q,p-degree-m coefficient. Characteristic zero makes these denominators invertible, and the formula is valid in the weighted completion. It chooses f(0,0,h)=0. Thus

    partial_(p_i) f=a_i,   partial_(q_i) f=-b_i,
    h^(-1)[f,q_i]=d(q_i),   h^(-1)[f,p_i]=d(p_i).

Both d and h^(-1)ad(f) kill k[[h]], are continuous, and agree on all Weyl generators. They therefore agree on the dense polynomial Weyl algebra and hence on D. Returning to matrices,

    delta = ad(S+h^(-1)f I_r).

This proves surjectivity with no unmentioned h-inverting derivations or noncontinuous derivations.

## 4. Kernel and scalar normalization

An element in the kernel commutes with all matrix units, so it is scalar diagonal. Multiplying it by h gives an element of D commuting with every p_i and q_i. The identities of Section 1 imply that every q,p partial derivative of that element is zero. In characteristic zero its only coefficients are in k[[h]]. Conversely those scalars commute with everything. Thus

    ker(ad|L)=h^(-1)k[[h]] I_r.

The central inclusion is lambda -> lambda I_r, with no factor of r. Normalized classical matrix trace would recover lambda; unnormalized trace would recover r lambda. Neither trace is needed for the proof.

## 5. Filtration qualifications and opposite convention

The Lie algebra here contains translations, for example h^(-1)ad(p_i)=partial_(q_i). These are continuous but lower weighted order by one. Hence the theorem must not be silently read as a statement that every derivation preserves each filtration level or fixes the formal origin. In fact the proof shows that every continuous k[[h]]-linear derivation has filtration shift at least -1.

If the intended Lie algebra consists only of filtration-preserving continuous derivations, restrict the surjection to the inverse image of that subalgebra. Concretely, modulo the central kernel, this restricts the chosen scalar primitive f to weighted order at least two; the matrix term S is already nonnegative-weight. More generally, any additional grading, origin-fixing, or symmetry constraint must be imposed explicitly on the image and its preimage. An h-Euler derivation with delta(h) nonzero is excluded by k[[h]]-linearity and is not covered by this extension.

For the earlier row-module construction, C_h=B_h^op has the ordinary local algebra C used here. For B_h itself the local algebra is C^op, with bracket represented by the negative matrix commutator; the same underlying lattice surjects by the corresponding opposite adjoint action. Multiplication by -1 identifies the two Lie extensions but negates the central scalar generator. Any comparison to a paper's central-extension class must retain this convention.

## 6. Boundary of this result

Combined with RESULT.md, the proof shows: IF the existing local quantizations admit continuous h-linear identifications with this completed Weyl model, THEN their matrix endomorphism models have the displayed derivation extension, and the intrinsic lattice from RESULT.md is the correct one. Formal Weyl identifications, their compatibility with any specified filtration, the global formal-coordinate torsor and its transitivity remain separate inputs. No gerbe coefficient, period sign, or global characteristic class has been identified here.

## 7. Comparison with the cited extension

The parallel primary-source review by `compare_twisted_trace_period` reports that Baranovsky, *Chern classes of quantizable coisotropic bundles*, Section 3.3, equation (6), uses E=gl_e(D_p), completed Heisenberg relations [y_j,x_i]=delta_ij h, continuous k[[h]]-linear derivations, and exactly

    0 -> h^(-1)k[[h]] -> (h^(-1)D_p + E) -> Der(E) -> 0.

Its scalar D_p is embedded diagonally, and its weighted grading has deg(h)=2 and deg(x_i)=deg(y_j)=1. Thus the present convention matches that extension with x=q, y=p and E=C, not with unmodified composition multiplication in B=C^op. The proof above derives this exactness directly rather than relying on the paper's cited Morita-invariance argument. The cited source is https://ems.press/content/serial-article-files/42628 . This comparison does not supply the missing global formal-coordinate torsor or central-class identification.
