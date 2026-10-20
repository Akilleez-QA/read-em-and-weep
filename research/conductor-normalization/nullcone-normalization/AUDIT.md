# Preserved mathematical audit

This review concerns the source manuscript and its stated assumptions. It is preserved as mathematical history, not a new independent certification of all publication edits or of unpublished input theorems. Source and publication hashes are recorded in SOURCE-HASHES.json. A split manuscript’s module or polar application remains conditional in its destination unit.

# Independent audit: normalization, conductor, and first-order descent

## Verdict and scope

Work over a field of characteristic zero, as in the cohomological context over C. Let N be the reduced binary-quartic triple-root surface, let S=P1×P1, and let

    ν:S→N,  (l,m)↦l³m.

Write Δ⊂S for the diagonal, C⊂N for the quadruple-root curve, and j:C→N for its inclusion. The map ν|Δ identifies Δ with C≅P1. The following assertions are correct:

    ν is the normalization;
    conductor on N = I_C;
    conductor on S = I_Δ² = O_S(-2Δ);
    ν_*O_S / O_N ≅ j_*O_P1(-2).

The last isomorphism is canonical after the natural identification C≅Δ: inclusion of I_Δ into O_S identifies the quotient with I_Δ/I_Δ². The intrinsic first-order descent operator uses the retraction r:2Δ→C induced by ν. Its local derivative direction is (-∂a+3∂b)/4, not a derivative holding a fixed.

For every locally free F on N there is an exact sequence

    0 → F → ν_*ν*F → j_*(F|C ⊗ O_P1(-2)) → 0.

In particular,

    H0(N,F) = ker[H0(S,ν*F) → H0(C,F|C ⊗ O_P1(-2))].

No surjectivity on global sections is asserted. For F=B0(4)|N the source and target of the displayed operator are exactly

    H0(S,ν*B0 ⊗ O_S(12,4))
    and H0(P1,B0|C ⊗ O_P1(14)).

This audit uses only universal symbolic geometry. It evaluates no specific source, polynomial instance, obstruction, jet, or matrix rank.

## 1. Affine model and normalization

Choose an affine root coordinate in which both roots are finite and write the quartic as a monic polynomial

    (x-a)³(x-b).

Set

    s=(3a+b)/4,  d=b-a,
    a=s-d/4,    b=s+3d/4,    z=x-s.

Then direct expansion gives

    (z+d/4)³(z-3d/4)
       = z⁴ -(3/8)d²z² -(1/8)d³z -(3/256)d⁴.

The coefficient of x³ recovers s. The coefficients of x² and x recover d² and d³, respectively, once s is known. Every coefficient is a polynomial in s,d²,d³. Thus the affine coordinate inclusion is precisely

    A=k[s,d²,d³] ⊂ R=k[s,d],

or, equivalently, A=k[s,u,v]/(v²-u³) with u=d² and v=d³. Here d is integral over A, and d=v/u away from d=0. Therefore Spec R→Spec A is finite and birational, and R is normal. These root-coordinate charts cover N: one can choose a point at infinity outside the finite root set of any nonzero quartic. Consequently ν:S→N is the normalization, and it is an isomorphism away from Δ and C.

## 2. The conductor and the quotient

An element of A is a polynomial in d with no degree-one term. For f∈R, the condition fR⊂A is equivalent to divisibility by d²:

- f∈A is necessary;
- writing f=f0(s)+d²g(s,d), the further condition fd∈A forces f0=0;
- d²R⊂A, so this condition is sufficient.

Thus the common conductor is d²R=(d²,d³)A. On Spec A the ideal (d²,d³) is exactly the reduced ideal of the quadruple-root curve; on Spec R it is (d²). Globally this proves

    Ann_ON(ν_*O_S/O_N)=I_C,
    I_C O_S=I_Δ²=O_S(-2Δ).

There is a particularly direct canonical identification of the quotient. Locally,

    A+dR=R,    A∩dR=d²R.

Therefore inclusion dR⊂R induces

    dR/d²R ≅ R/A.

These maps are induced by the global inclusion I_Δ⊂O_S and hence glue without choosing a splitting or a coordinate. They identify

    ν_*O_S/O_N ≅ j_*(I_Δ/I_Δ²).

Since O_S(Δ)=O_S(1,1),

    I_Δ/I_Δ²=O_Δ(-Δ)=O_P1(-2).

The quotient is supported on the reduced C and is annihilated by I_C. In particular, it is not the full structure sheaf of the doubled diagonal.

## 3. The canonical first-order retraction and its gluing

Let 2Δ be defined by I_Δ². The equality I_C O_S=I_Δ² implies that ν|2Δ factors through C:

    r:2Δ→C,    ν|2Δ=j∘r.

The restriction of r to Δ is the identity under C≅Δ. In the above affine coordinates,

    O(2Δ)=k[s,d]/(d²),    r* sends h(s) to h(s).

Equivalently, the local conductor square is the fiber-product identity

    A = R ×_{R/(d²)} k[s].

Thus the functions descending to N are exactly those whose restriction to 2Δ is pulled back from C by r.

The weighted coordinate s defines this retraction only to first order. For an overlap root coordinate a'=g(a), b'=g(b), put s'=(3a'+b')/4 and d'=b'-a'. Modulo d²,

    s'=g(s),    d'=g'(s)d.

The first formula verifies gluing of r, and the second verifies the conormal transition function. For example, if g(t)=1/t, then d'=-s^(-2)d modulo d², which is the transition of O_P1(-2). One must not regard the weighted average as a globally defined map S→P1; the first-order map r is what is canonical.

The retraction splits the square-zero thickening as an O_C-algebra:

    r_*O_2Δ ≅ O_C ⊕ O_P1(-2),

with square zero on the second summand. The quotient map O_S→ν_*O_S/O_N is, locally on N, restriction to 2Δ followed by projection onto this second summand. Intrinsically this projection is

    f ↦ f|2Δ - r*(f|Δ).

## 4. Derivative direction and vector-bundle descent

Along Δ, use tangent vectors (u,v) on the two factors. Differentiating l³m shows that

    ker(dν)|Δ = {(u,v):3u+v=0}.

The tangent direction of Δ is {(u,u)}, and the two lines are transverse in characteristic zero. The retraction has tangent map

    dr(u,v)=(3u+v)/4.

In the coordinates (s,d), the vector field normal to Δ selected by this kernel is

    D=∂d|s = (-∂a+3∂b)/4,
    Dd=1,    Ds=0.

For a scalar function f the quotient operator is

    J(f)=(Df)|Δ · [d] ∈ I_Δ/I_Δ².

The product, rather than its coefficient in an arbitrary chart, is invariant: under the preceding coordinate change [d'] = g'(s)[d] and the derivative coefficient transforms inversely. A derivative holding a fixed would be incorrect: the descending function s=(3a+b)/4 has ∂b(s)=1/4 but Ds=0.

Now let F be locally free on N, and put E=ν*F. Because E|2Δ=r*(F|C), the scalar projection gives an intrinsic map

    J_F:ν_*E→j_*(F|C⊗O_P1(-2)).

In a local frame e_i of F pulled back from N,

    J_F(Σ f_i e_i)=Σ (Df_i)|Δ · e_i|C ⊗ [d].

This formula is independent of the chosen downstairs frame. Its transition matrices have entries in A, so their D-derivatives vanish on Δ. No connection or arbitrary splitting of E is required. If one uses unrelated frames on S, one cannot omit their corresponding first-order changes.

Tensoring the scalar normalization sequence by F, using local freeness and the finite-morphism projection formula, proves

    0→F→ν_*E --J_F→j_*(F|C⊗O_P1(-2))→0.

Thus a section of E descends if and only if J_F vanishes, equivalently if its restriction to 2Δ equals the r-pullback of its restriction to Δ. The derivative operator is O_N-linear; it is not O_S-linear on arbitrary coefficients. Taking H0 gives the kernel statement in the verdict, but surjectivity of the sheaf map does not imply surjectivity on H0. The next term is H1(N,F).

## 5. The requested twist and the cohomological boundary

The defining map has bidegree (3,1), so

    ν*O_N(1)=O_S(3,1).

Its restriction to Δ gives O_C(1)=O_P1(4). Consequently, for F=B0(4)|N,

    E=ν*B0⊗O_S(12,4),
    F|C⊗O_P1(-2)=B0|C⊗O_P1(16-2)
                       =B0|C⊗O_P1(14).

Accordingly the domain of the Koszul boundary from the supplied context is exactly

    H0(N,B0(4)|N)
      ≅ ker[J_F:H0(S,ν*B0⊗O_S(12,4))
                    → H0(P1,B0|C⊗O_P1(14))].

The context file identifies the separate map

    δ_N:H0(N,B0(4)|N)→H2(P4,B0(-1)).

The normalization calculation makes its domain explicit. It proves neither a rank statement for J_F nor one for δ_N; in particular it does not canonically extend δ_N to all sections on the normalization. No conclusion about fourth-power vanishing follows solely from the conductor calculation.

Boundary context read: fourth-power-cohomology/PROOF.md.

## 6. Cross-check of the completed PROOF.md

The completed neighboring PROOF.md was independently read after the preceding audit was written. No mathematical correction was found. The specifically requested checks are:

- Exact affine chart: the monic coefficient chart excludes a root at infinity, so its entire normalization preimage is the affine (a,b)-chart. Its reduced coefficient-image ring is exactly A, not merely a completion or a generic local approximation. Finiteness of R over A also confirms the image is closed.
- Doubled normalization fiber: for the point of C with parameter s0, the maximal ideal (s-s0,u,v) extends to (s-s0,d²) in R. Hence the fiber is Spec C[d]/(d²). A one-point topological fiber need not be a reduced scheme fiber.
- Singular scheme versus conductor: the intrinsic Jacobian ideal of A=C[s,u,v]/(v²-u³) is (u²,v). The conductor is (u,v). The first defines a nonreduced thickening of C, while the latter defines C itself. Both assertions in the proof are correct.
- Equation (8): normalization pullback identifies H0(N,B(4)|N) with ker D4. Its inverse on that kernel is well-defined, so δ̃_N=δ_N∘dsc has exactly the same image as δ_N. The annihilator statement and the surjectivity criterion therefore follow from the supplied boundary context without enlarging the domain or imposing an unproved rank claim.
- Cohomology and Euler characteristic: the retained long exact sequence stops after H2(S,ν*F) because C has dimension one. The identity χ(O_N(t))=(3t+1)(t+1)-(4t-1)=3t²+2 is correct for all integer t.

The only interpretive care needed is already present in the proof: the transverse kernel is an intrinsic line subbundle, while K is its chartwise generator; and the retraction is defined on 2Δ, not on all of S.
