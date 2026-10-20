# Publication scope

This is a preserved theorem manuscript, with the exact hypotheses and held identifications listed in unit 03 INPUTS.md. Abstract geometry and formal conditional implications are distinct from identification with the actual HM module or retained source. Historical words such as “new,” “remaining,” or “previously verified” describe the source manuscript, not a claim about the current research frontier.

# Nullcone normalization, conductor, and the fourth-power boundary domain

## Result

Work over C. Let N⊂Y=P⁴ be the reduced binary-quartic triple-root surface, already proved to be the complete intersection of degrees (2,3). Write

    ν:S=P¹×P¹ → N,  (l,m)↦l³m,
    Δ⊂S the diagonal,  j:C≅P¹→N,  l↦l⁴.

Then ν is the normalization. Its conductor is the reduced ideal I_{C/N} downstairs, while

    I_{C/N} O_S = O_S(-2Δ).

There is a canonical exact sequence of O_N-modules

    0 → O_N → ν_*O_S → j_*O_P¹(-2) → 0.             (1)

The quotient identification uses C≅Δ and O_P¹(-2)=I_Δ/I_Δ², rather than an unspecified degree calculation. For every vector bundle F on N, tensoring gives

    0 → F → ν_*ν*F → j_*(F|C ⊗ O_P¹(-2)) → 0.     (2)

The final map is an intrinsic first-normal-derivative map: it differentiates along the kernel of dν on Δ, using frames pulled back from N. It is surjective as a sheaf map, but need not be surjective on global sections.

In particular, for B=B₀ on Y and every integer t,

    H⁰(N,B(t)|N)
      = ker[D_t:H⁰(S,ν*B⊗O_S(3t,t))
                    → H⁰(P¹,(j*B)⊗O_P¹(4t-2))].   (3)

Here ν*B abbreviates pullback along S→N→Y, and j*B along C→N→Y. Thus the exact domain of the previously established fourth-power Koszul boundary is

    ker D₄ ⊂ H⁰(S,ν*B⊗O_S(12,4)),
    D₄ has target H⁰(P¹,j*B⊗O_P¹(14)).             (4)

This supplies an explicit descent condition; it does not evaluate that kernel, the boundary, its rank, or any actual obstruction source.

## 1. An exact local ring at every collision

Choose an affine root coordinate x on P¹ such that neither root is at infinity. This is possible near every point of S after a common projective change of coordinate. The corresponding quartic can be uniquely normalized to be monic:

    (x-a)³(x-b).

Put s=(3a+b)/4 and d=b-a, so a=s-d/4 and b=s+3d/4. For z=x-s, the polynomial identity is

    (z+d/4)³(z-3d/4)
      = z⁴ -(3/8)d²z² -(1/8)d³z -(3/256)d⁴.

The x³ coefficient recovers s. The centered x² and x coefficients recover nonzero scalar multiples of d² and d³. Conversely all four monic coefficients are in C[s,d²,d³]. Since N is the reduced image, its coordinate algebra on this chart is exactly

    A=C[s,d²,d³] ≅ C[s,u,v]/(v²-u³),
    R=C[s,d],  u=d², v=d³.                        (5)

This is an equality of coordinate algebras, not only of formal or generic local models. Indeed the parametrization of this affine chart is surjective on geometric points; the kernel of the coefficient map defines its reduced closed image, and that image is N in the monic chart.

R is finite over A, generated as an A-module by 1,d. The fraction fields agree, because d=v/u away from u=0. R is normal, so it is the normalization of A. These affine charts cover N, proving the global normalization claim.

If d≠0, A localized at u equals R localized at d; N is smooth there. At every quadruple root d=0, the transverse singularity is an ordinary cusp, with the free coordinate s along C. In particular there is no exceptional higher cusp at a special quadruple root. All such points admit the same exact product model. This differs from the several triple-diagonal components upstairs in (P¹)⁴: N itself is unibranch along C.

For precision, the reduced singular locus is C=(u,v). The Jacobian singular subscheme in the cusp chart has ideal (u²,v), since the equation is v²-u³. Its nonreduced structure is not the conductor ideal. The conductor is computed next.

## 2. The conductor on both sides

As a C[s]-module,

    R=A ⊕ C[s]d.

Here A comprises precisely the polynomials with zero coefficient of d¹. Every element of d²R is in A, and multiplication by any element of R keeps it in A. Hence d²R is contained in the conductor.

Conversely an element a∈A can be written a=a₀(s)+d²g(s,d). If a is in the conductor then ad∈A. Its d¹ coefficient is a₀(s), which must therefore vanish. Thus

    conductor = Ann_A(R/A) = d²R = (d²,d³)A=(u,v)A. (6)

In particular it is exactly the reduced ideal of C downstairs. Extending it to R gives (d²), the ideal of 2Δ. This proves both global conductor formulas. The normalization fiber over a quadruple-root point has ring C[d]/(d²), despite the one-point set-theoretic fiber; this also records the ramification scheme structure.

## 3. Canonical quotient and global gluing

Let J=I_Δ⊂O_S. Locally J=(d) and J²=(d²). The map from J into R/A has kernel A∩(d)=d²R, and is surjective because R=A+(d). Hence inclusion canonically induces

    ν_*(J/J²) ≅ ν_*O_S/O_N.                       (7)

The ideal I_{C/N} annihilates the quotient, so it is an O_C-module. The restriction ν|Δ:Δ→C is an isomorphism. Since Δ has divisor class (1,1) on S,

    J/J²=O_S(-Δ)|Δ≅O_P¹(-2).

This proves (1), including its canonical quotient identification. It also distinguishes the conductor O_S(-2Δ) from the quotient conormal line O_Δ(-Δ).

One can describe the associated quotient map as follows. The map 2Δ→N factors through C, since I_C maps to J². It therefore supplies a retraction ρ:2Δ→C≅Δ. On 2Δ, subtract the pullback along ρ of a function's restriction to Δ; the remainder is in J/J². This realizes the quotient map in (7). The retraction is induced by ν, not chosen independently.

## 4. The derivative is coordinate and frame independent

In the coordinates of §1 the quotient map sends f(s,d) to

    (∂f/∂d)(s,0)·[d] ∈ J/J².

At d=0 the fixed-s vector ∂/∂d is

    K=(-∂/∂a+3∂/∂b)/4.

It satisfies K(s)=0 and K(d)=1. It spans ker(dν|Δ), and its projection to the normal bundle N_{Δ/S} is an isomorphism. Thus it is a distinguished transverse direction, not the derivative with a or b fixed.

For a change of affine root coordinate a'=h(a), b'=h(b), put s'=(3a'+b')/4 and d'=b'-a'. Modulo d²,

    s'=h(s),  d'=h'(s)d.

The potentially unwanted linear term in s' cancels because 3(-1/4)+3/4=0. Hence the first-order coefficient transforms as a conormal coefficient, exactly as in §3.

For a locally free F on N use a local frame of F and pull it back to S. Apply the scalar derivative to each coefficient. Any transition matrix between such frames has entries in A, so its derivative K along Δ is zero. The product rule therefore introduces no extra transition term. This proves intrinsic frame independence without selecting a connection on F or pretending that arbitrary frames on S have this property. Equivalently tensor (1) with F and apply the finite projection formula; its last map is precisely this derivative construction.

Taking global sections of (2) proves (3), since ν*O_Y(1)=O_S(3,1) and O_Y(1)|C=O_P¹(4). In a pulled-back frame, a section descends if and only if every coefficient has zero d¹ term. There is no additional higher-order condition: every power d^n for n≥2 already belongs to A.

The next terms of the exact sequence are retained:

    0 → H⁰(N,F) → H⁰(S,ν*F) → H⁰(C,F|C⊗O(-2))
      → H¹(N,F) → H¹(S,ν*F) → H¹(C,F|C⊗O(-2))
      → H²(N,F) → H²(S,ν*F) → 0.

Thus neither a direct-sum cohomology formula nor global surjectivity of the derivative map is being assumed.

## 5. Exact consequence for the fourth-power obstruction dependency

The independently established fourth-power calculation gives

    im[H²(Y,B(-4)I_N)→H²(Y,B(-4))] = (im δ_N)^⊥,

where δ_N is the two-step Koszul boundary

    H⁰(N,B(4)|N) → H²(Y,B(-1)).

It is constructed from

    0→B(-1)→B(2)⊕B(1)→B(4)I_N→0,
    0→B(4)I_N→B(4)→B(4)|N→0.

Let dsc:ker D₄→H⁰(N,B(4)|N) denote the inverse of the injective normalization pullback. Then the fully specified smooth-normalization version is

    δ̃_N := δ_N∘dsc : ker D₄ → H²(Y,B(-1)),
    fourth-power image = (im δ̃_N)^⊥.              (8)

The target is the previously proved ten-dimensional space. Therefore fourth-power membership forces universal first-ten vanishing precisely when δ̃_N is surjective. Formula (4) resolves the geometric section-descent dependency at the quadruple-root cusp, but does not establish this surjectivity. Applying δ_N to all normalized sections without first imposing D₄=0 would enlarge its domain incorrectly. Replacing D₄ by an arbitrary transverse derivative could also give a wrong descent test.

## 6. Consistency check and scope

For F=O_N(t), the Euler characteristic from (1) is

    χ(O_N(t)) = (3t+1)(t+1) - χ(O_P¹(4t-2))
               = (3t+1)(t+1) - (4t-1) = 3t²+2.

This agrees with a degree-six (2,3) complete-intersection surface with trivial dualizing sheaf. It is only a consistency check; the local ring proves the quotient and conductor independently of this numerical identity.

The proof uses universal local coordinate algebra and exact sequences only. No actual source, selected polynomial instance, rank instance, physical jet, obstruction pairing, or large computation was evaluated. 

## Dependencies and coordination

- ../fourth-ideal-pushforward/PROOF.md: N is the reduced (2,3) complete intersection, with the actual fourth-power sign inclusion.
- ../fourth-power-cohomology/PROOF.md: dual Koszul boundary and its exact relationship to the fourth-power cohomology image.
- ../finite-collision-detection/PROOF.md: finite-neighborhood context; its source and lifting hypotheses remain unaffected.
- AUDIT.md: fresh independent audit of this normalization and descent calculation.
