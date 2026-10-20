# First-order bracket obstruction to a negative mixed return

## Result and scope

Over a field of characteristic different from two, an identity-reduction return from the opposite of a two-axis square-zero algebra deformation, preserving the two axes, must negate each nonzero first-order commutator bracket. Consequently, if its coefficient maps are scalar signs and both pure brackets are nonzero, both signs must be negative. Its action on the product coefficient is then positive. A one-axis-negative return of this kind is impossible already on the first-order boundary.

This is a necessary-condition theorem, not construction of any return. It strengthens “a one-factor reversal has not been constructed” for this precisely marked class of candidates. It applies to local algebra equivalences and, with the explicit local-freeness hypothesis below, to line bimodule returns. It does not assert an unrestricted theorem for derived or arbitrary Morita equivalences.

## 1. Intrinsic bracket of a square-zero extension

Let A be a commutative k-algebra and L an A-module. Let A~ be a square-zero associative extension with kernel L, with left and right multiplication on L inducing the same A-module structure. For a,b in A choose arbitrary lifts a~,b~. Define

    beta(a,b) = [a~,b~] in L.

The definition is independent of lifts: replacing a~ by a~+l changes the commutator by lb−bl=0; products of two kernel elements vanish. Associativity gives the Leibniz identity for beta in each entry. No splitting, differential-operator assumption, or point evaluation is used.

If Phi:A~_1 -> A~_2 induces identity on A and lambda:L_1 -> L_2 on the kernels, then

    beta_2(a,b) = lambda(beta_1(a,b)).               (1)

This follows by applying Phi to a commutator. More generally, if the reduction is a base automorphism alpha, the necessary identity is

    beta_2(alpha(a),alpha(b)) = lambda(beta_1(a,b)). (2)

Thus an anti-Poisson base automorphism is expressly outside the identity-reduction exclusion.

For a split expression a*b=ab+B(a,b), beta=B−B^op. An identity-reduction gauge can alter B only by a Hochschild coboundary, whose antisymmetric part on a commutative algebra with symmetric coefficients is zero. Equation (1) is the coordinate-free version of that fact.

## 2. Two axes and the opposite return

Let an algebra deformation have marked pure coefficient lines L_z,L_h and a nonzero mixed piece J identified with L_z tensor_A L_h. The bounded parameter model is k[s,t]/(s²,t²), where st survives, not k[s,t]/(s,t)². The pure restrictions are obtained by killing the other axis. Coefficient-line transitions are retained in the sheaf version. Restricting to either pure axis produces extensions of the form above with brackets beta_z,beta_h. Assume both are nonzero. This means nonzero as sheaf maps; no values are selected.

The opposite algebra has pure brackets −beta_z and −beta_h. Suppose there is a return from that opposite algebra to the original algebra which:

- induces identity on the classical commutative algebra;
- preserves each pure axis;
- acts on L_z and L_h by scalar signs epsilon_z and epsilon_h;
- respects the specified coefficient product L_z tensor L_h -> J.

Restricting the return to each axis and applying (1) yields

    beta_z = −epsilon_z beta_z,
    beta_h = −epsilon_h beta_h.

Since 2 is invertible and both brackets are nonzero, epsilon_z=epsilon_h=−1. Multiplicativity of the coefficient marking then forces the action on J to be epsilon_z epsilon_h=+1. Higher mixed additions to parameter images do not change this: (−s+a st)(−t+b st)=st in the bounded ring. There is no independently adjustable sign on J when the fixed product identification is respected.

Similarly an identity-reduction automorphism of the original algebra, rather than a return from its opposite, must have epsilon_z=epsilon_h=+1. Therefore neither type of return gives a negative action on J under these hypotheses.

The proof uses only the pure restrictions. No mixed multiplication, module correction, ambient associator, or determinant data can repair a violation of this necessary condition: a full candidate would restrict to the forbidden pure candidate.

## 3. Limited extension to line bimodules

The same local test applies to an invertible (A~_2,A~_1)-bimodule P which is locally free of rank one as a right A~_1-module and whose classical reduction is a line with the usual identical left/right A-actions. Choose a local right generator e. Left multiplication defines a unital algebra map

    A~_2 -> End_(right A~_1)(P) = A~_1.

Invertibility makes this the relevant local algebra identification; the classical map is identity because ae=ea modulo the deformation ideal. Its induced kernel maps must satisfy (1), in the appropriate direction; scalar signs are their own inverses, so the conclusion in §2 is unchanged.

For a proposed determinant bimodule this proves the exclusion only if the bimodule really has these local rank-one and marked-action properties. It does not infer them merely from the classical determinant line. A more general derived equivalence requires its own Hochschild-class naturality argument; none is asserted here.

## 4. Application to the named corrected ambient

The corrected plane factor has local product

    (f,eta)*(g,theta)=(fg, f theta+g eta + (df wedge dg)/2).

Its intrinsic commutator is df wedge dg. The universal wedge of differentials on a smooth surface is nonzero: Omega^2 has rank one and is generated locally by wedges of a basis of Omega^1. This proves the needed nonzero sheaf-map premise without choosing a source coefficient, source point, matrix, or detector.

Both factors of the specified external-product ambient have this property on every nonempty smooth local chart. In the general theorem, local impossibility is asserted only on opens where both restricted brackets remain nonzero. Hence an identity-reduction, axis-preserving opposite return with scalar coefficient signs necessarily has positive mixed character. This positive coefficient character alone cannot supply the missing negative sign in the tracefree dual-defect operator. To conclude that the total returned operator remains +Id, one must additionally fix the classical module return so that its residual action on End0 is identity (for example, identity or scalar after the stated alternating identification), and exclude any independent band identification. A return with an extra nontrivial classical module automorphism is not covered by that conclusion.

A map which negates the coefficient line can identify a plus extension with its minus/opposite extension. It is not an automorphism of the marked plus extension. Simultaneous reversal can pass the local bracket test for an opposite return, but this test does not construct global overlap/associator compatibility, the required determinant bimodule, or the boundary-module return.

## 5. Remaining routes and stopping boundary

The theorem does not rule out returns covering nontrivial base automorphisms satisfying (2), axis exchange, non-scalar coefficient actions, partially opposite external products, or broader equivalences with separately established deformation-class functoriality. A candidate in one of those classes must also specify its actual action on the retained obstruction band and return the prescribed boundary, rather than merely identify the classical bundle.

No actual obstruction value or existence conclusion follows. The advance is the local impossibility of the naive negative-character return with identity classical reduction, not a vanishing or nonvanishing theorem for the mixed class.

Source for the corrected product: https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6270678828 . Source for the proposed symmetry issue: https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6272324961 . The proof is intrinsic formal algebra and uses no source evaluation.
