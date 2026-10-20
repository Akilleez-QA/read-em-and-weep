> Scope: read CURRENT-SCOPE.md and DEPENDENCIES.json with this complete historical derivation. Historical open-case wording is qualified there.

# Ten-point positive-plane interpolation does not force a degree-eight base curve

## Result

Let Omega be the unique 250-point orbit in the projective five-dimensional Schrodinger representation of G = F5^2 semidirect SL2(F5). The twenty-five positive reflection planes partition Omega into twenty-five disjoint ten-point sets, in the precise incidence sense that each point of Omega belongs to exactly one of these planes.

In each positive plane P, write X = Omega intersect P. Then:

1. No nonzero plane cubic vanishes on X.
2. The space of plane quartics vanishing on X has dimension five and generates the reduced ideal sheaf of X.
3. Products of these quartics generate the square ideal sheaf I_X^2 in degree eight. In particular, the plane degree-eight forms double at X have base scheme exactly the ten double points, with no base curve.

Thus degree eight and double vanishing at the ten points, considered solely on an individual positive plane, do not force a positive-dimensional base. This does not construct global degree-eight forms double at all 250 points, and it does not exclude the remaining rank-two orbit. Compatibility between planes and normal derivatives is not resolved here.

## 1. Incidence count

Use the stabilizer and representation results of [normalizer-250-simple-defect](https://github.com/Akilleez-QA/read-em-and-weep/blob/1d6db2e95f9f7fc207a350ebc805c2ce0ae873da/research/hm/normalizer-rank-five/normalizer-250-simple-defect/PROOF.md). Every point p of Omega has stabilizer conjugate to Dic3, of order twelve. This stabilizer has exactly one involution. Its unique stable line lies in the three-dimensional positive eigenspace of that involution.

Every involution of G projects to the unique involution c = -I of SL2(F5). It therefore has the form (v,c), with v in F5^2; conversely all twenty-five such elements are involutions. They are conjugate under F5^2. Their normalized determinant-one lifts have eigenspace dimensions three and two, giving the positive planes and negative lines.

If p belonged to the positive plane of another involution, that involution would also fix p, contradicting uniqueness of the involution in G_p. Hence each p belongs to exactly one positive plane. The twenty-five planes are distinct: if two coincided, every point of this plane would be fixed by the product of the two involutions, a nonidentity element of F5^2. Such an element has five distinct eigenlines in the Schrodinger representation, and cannot fix an entire plane pointwise.

Transitivity on the twenty-five planes makes their incidence counts equal. Their total is 250, so each has ten points. Fix the plane P(V_+) of c. Its complement SL2(F5) acts through A5 on P(V_+), and X is its orbit of size ten: the projective stabilizer has order six, the normalizer of a subgroup of order three. These ten points are precisely the fixed-axis lines of the ten order-three subgroups.

## 2. The invariant quadratic does not vanish at X

Write T = V_+, the irreducible three-dimensional A5 representation. It carries a nondegenerate invariant quadratic form q, and has no invariant linear forms. For an order-three element a, its eigenvalues on T are 1, omega, omega^2. Its fixed line ell is orthogonal, for q, to the other two eigenspaces. Nondegeneracy of q therefore implies q restricted to ell is nonzero. Since every point of X is such an axis, q is nonzero at every point of X.

The small character identities already used in [canonical-line-parity-exclusion](https://github.com/Akilleez-QA/read-em-and-weep/blob/c92b59ea3aa135921f34b1842e26060a4960f1ac/research/hm/rank-four/canonical-line-parity-exclusion/PROOF.md) give

    Sym^2(T*) = 1 + P5,
    Sym^3(T*) = T + T' + P4.

For the second identity one may apply the symmetric-cube character formula to the displayed A5 character table there; dimensions are 3 + 3 + 4 = 10. Consequently there is no invariant cubic, and the invariant quadratics are precisely the multiples of q.

## 3. No cubic passes through all ten points

Suppose U = H^0(P, I_X(3)) is nonzero. It is A5-stable. Let h be the greatest common divisor of all its forms, up to scalar. Its divisor is A5-invariant, so the line spanned by h is an A5-character. A5 is perfect, hence this character is trivial.

If deg h > 0, the preceding invariant calculation shows that h must be a scalar multiple of q: there are no invariant forms of degree one or three. Every F in U is then q times a linear form. Since q is nonzero everywhere on X, that linear form vanishes on X. But X spans T, because its span is a nonzero invariant subspace of the irreducible T. Thus F = 0, a contradiction.

If deg h = 0, there are two elements F,G in U without a common component. Indeed, fix nonzero F and choose G avoiding the finitely many proper subspaces consisting of forms divisible by each irreducible factor of F. Bezout gives at most nine common points, whereas F and G both vanish at the ten distinct points of X. This is again a contradiction.

Therefore U = 0.

## 4. Quartic interpolation and the full plane double-point ideal

The cubic evaluation map on ten points is an isomorphism: it is injective by Section 3 and both vector spaces have dimension ten. Choose cubic interpolation forms C_i such that C_i(p_j) is zero for j different from i and nonzero for j = i. These ten forms form a basis of all plane cubics.

For every line equation l vanishing at p_i, the quartic C_i l vanishes at all of X. Near p_i, C_i is a unit, and two independent line equations through p_i generate its maximal ideal. Thus these quartics generate I_X at each p_i.

For y outside X, some C_i(y) is nonzero, since the C_i span every cubic and the full cubic system has no base point. Choose a line through p_i avoiding y. Then C_i l is a quartic vanishing on X but nonzero at y. Hence these quartics generate I_X everywhere, not merely away from an unspecified residual finite set.

A line equation nonzero at all ten points, multiplied by all cubics, shows that quartic evaluation is surjective. Therefore

    dim H^0(P, I_X(4)) = 15 - 10 = 5.

Taking pairwise products of a basis of this five-dimensional space now generates I_X^2 at every stalk. At p_i the generated ideal is exactly m_{p_i}^2, and off X it is the unit ideal. Each product has degree eight. Since X is a disjoint reduced set of smooth points, I_X^2 is exactly its double-point ideal sheaf. The full degree-eight double-vanishing system contains these products and has precisely the same base ideal sheaf.

## Scope and evidence boundary

This is a rigorous limitation of the proposed plane-restriction route, not an exclusion of the global 250-point rank-two alternative.
