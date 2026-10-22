# Universal first-normal harmonic product and diagonal operator residue

## Scope

This computes the actual ambient algebra's first-normal multiplication, and an exact local expression for the operator defect once the actual normal bundle and nilpotent lift are supplied. It does not replace that actual lift by the Hessian candidate, nor calculate the global third Bockstein. No actual HM coefficients are selected.

## 1. Canonical ambient multiplication

Put q=xz-y² and restrict to the cone by (x,y,z)=(u²,uv,v²). Let L(p) be the unique harmonic lift of a binary form p of even degree 2m, with harmonicity defined by

    Δ=∂x∂z-(1/4)∂y².

Uniqueness follows from the harmonic decomposition of degree-m ternary forms into q-powers times harmonics. It is also immediate from Δ(qH_k)=(k+3/2)H_k for a harmonic degree-k polynomial. For even forms p,r of degrees 2m,2n, define the unnormalized second transvectant

    (p,r)_2=p_uu r_vv-2 p_uv r_uv+p_vv r_uu,
    B(p,r)=(p,r)_2/[2(2m-1)(2n-1)(2m+2n-1)].

Then the universal identity is

    L(p)L(r)=L(pr)+q L(B(p,r)) mod q².                 (1)

The formula includes constants: their second transvectant is zero. To prove (1), apply Δ and restrict to q=0. The restriction of Δ(L(p)L(r)) is an equivariant bilinear map to degree 2m+2n-4 binary forms. The corresponding Clebsch-Gordan summand occurs once, so it is proportional to (p,r)_2. Testing the universal highest/lowest monomials p=u^(2m), r=v^(2n) gives proportionality 1/[4(2m-1)(2n-1)]. Dividing by m+n-1/2, the factor from Δ(qH_(m+n-2)), gives (1). This tests an abstract representation identity, not any source instance. The cases m=0 or n=0 are direct.

Thus B is the actual symmetric first-order multiplication correction in the canonical harmonic splitting, not an arbitrary local deformation of the cone. Associativity of ambient multiplication supplies its weighted Hochschild cocycle identity. A cone-only product calculation omitting B need not give the ambient operator obstruction.

## 2. A local diagonal formula retaining the actual normal data

Work in a homogeneous local frame near the vertex, where the regular section is (f,g) with binary degrees3,5. Write

    n=[[fg,-f²],[g²,-fg]],
    N_tilde=L(n)+q L(t) mod q²,
    t=[[t11,t12],[t21,-t11]].

Here t MUST be the actual correction in the chosen actual midpoint frame. For the degree8 component of the final diagonal error, only the components of t of degrees4,2,6 in entries11,12,21 respectively contribute. The actual correction is not assumed homogeneous under a full block-torus action on the midpoint bundle. Interpret the displayed formulas componentwise if other degrees occur. The canonical harmonic splitting differs from an Euler-gradient lift; one must transform t when changing splittings.

Let D preserve this harmonic splitting and satisfy Dq=ρq. This includes a base derivation plus vertical Euler action, which is the local form of the negative-block vector fields. Write H for the degree4 local coefficient of the actual symbol k a²h D_a. In this paragraph the negative-coordinate factors are base coefficients. Let A be the q-order-zero (cone) part of the local operator's matrix connection, and let Λ absorb the scalar nilpotent eigenvalue and the chosen physical-line connection. Its cone preservation identity is

    H Dn+[A,n]-Λ n=0.                                (2)

Use actual local lifts with connection L(A)+q L(K) and scalar L(Λ)+q L(Λ1). In the harmonic splitting the normal error is

    R=B(H,Dn)+[A,n]_B-B(Λ,n)
       +H Dt+(Hρ-Λ)t+[A,t]+[K,n]-Λ1 n.              (3)

The notation [A,n]_B denotes matrix multiplication with B instead of ordinary scalar multiplication, in the two commutator terms. Formula (3) is just expansion of

    (L(H)D+ad_(L(A)+qL(K))-(L(Λ)+qL(Λ1))) N_tilde

to order q, using (1) and (2). All scalar physical-frame actions must be included in Λ before using it. In particular, Dq=ρq is not set to zero merely because the GLOBAL twisted symbol annihilates q0: a local trivialization of the normal equation may contribute ρ.

## 3. The canonical-module coordinate is the diagonal error

The regular-pair commutator computation gives tangent generators

    S1=[[f,0],[2g,-f]], S2=[[g,-2f],[0,-g]],

and the canonical-module presentation sends S1 to f and S2 to g in I/(f²,g²). Therefore the class of R=u S1+v S2 is represented simply by R11=u f+v g modulo (f²,g²). Taking entry11 of (3) gives

    r_local = B(H,D(fg))+B(A12,g²)+B(A21,f²)-B(Λ,fg)
              +H D(t11)+(Hρ-Λ)t11+A12 t21-A21 t12
              -Λ1 fg                    mod (f²,g²). (4)

The omitted term [K,n]11=K12 g²+K21 f² vanishes in this quotient. Thus the arbitrary local operator-lift correction K has disappeared explicitly, not by a claim that all tangent errors are commutators. The actual nilpotent correction t has NOT disappeared. Nor can the scalar term Λ1 fg be discarded locally: it belongs to the intrinsic O_Z submodule of M. Only a globally compatible change of scalar lift is killed after the global connecting map, as proved in ACTUAL-THIRD-VALUE-AS-MIDPOINT-DUALIZING-OPERATOR-DEFECT.md.

With A and the corrected cone operator chosen in their homogeneous degree4 component, projecting (4) to binary degree8 uses precisely the t components just specified and the degree0 part of Λ1. This isolates the local homogeneous piece relevant to the positive P4 obstruction; it does not assert that an arbitrary actual normal frame has no other degrees. It retains both ambient algebra terms B and actual bundle terms t. Compatible expressions glue intrinsically in M(4)=omega_(2Z)(5), not through a naive global identification with I/(f²,g²).

## Remaining mathematical action

To evaluate the absolute third gate one must identify the actual t and actual corrected connection A on overlapping frames, substitute in (4), and take the global boundary modulo H0(G(4)) and then the actual second-symbol image. The earlier Hessian formula alone does not complete that comparison. Formula (4) states explicitly which missing normal data enter the value and which arbitrary choices do not.

## Reproduction

Run verify_harmonic_first_normal_product.py. It checks all 256 pairs of monomial bases with 0≤m,n≤3, including harmonicity and restriction of each lift, together with disappearance of the diagonal gauge correction. The all-degree proof is Section1. The verifier performs universal polynomial identities only, with no selected HM coefficients, source-instance matrix or rank evaluation.
