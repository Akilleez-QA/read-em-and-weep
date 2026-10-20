# Binary-quartic discriminant: exact conductor and pole-layer descent

Work over C. Let Y=P⁴ parametrize binary quartics, D⊂Y its reduced degree-six discriminant hypersurface, and

    ν:T=P¹×P²→D, (l,q)↦l²q.

Here l denotes a linear factor, and q(l)=0 means that q vanishes at the root of l (equivalently l divides q). Put

    R={l divides q},  S={disc(q)=0},
    N={quartics with a triple root}, W={squares of quadratics},
    C={fourth powers}.

The principal results are

    conductor on T = O_T(-2R-S) ⊂ O_T,                (1)
    conductor on D = I_(N∪W)/D,                       (2)

where N∪W has its reduced union structure. Formula (1) is equality of actual ideals, not just divisor classes. In particular there is no additional ideal factor over C. We give two independent global controls of this issue: finite duality and a determinantal presentation. The associated conductor square supplies an exact section and cohomology descent test for every polar layer. No actual obstruction value or rank is evaluated.

## 1. Normalization and geometry of the boundary

The map ν is proper and has finite fibers: a quartic has finitely many distinct double-root factors, and each such factor uniquely determines its residual quadratic up to scale. Hence ν is finite. Its image is exactly D. A general discriminant quartic has exactly one double root and two other distinct roots, so ν is generically one-to-one and birational in characteristic zero. T is smooth and normal; a finite birational morphism from a normal integral scheme is the normalization. This proves the assertion everywhere, including triple, two-double, and quadruple fibers.

The hyperplane pullback is ν*O_Y(1)=O_T(2,1). R is the incidence divisor with equation Res(l,q), of bidegree (2,1); it is isomorphic to P¹×P¹ through (l,m)↦(l,lm). S=P¹×(smooth conic) has class (0,2) and is likewise P¹×P¹, with coordinates (l,m)↦(l,m²). Both are smooth irreducible divisors. Their images are N and W. Away from C, S→W is the degree-two map exchanging (l,m) and (m,l); at C the involution fixes the diagonal.

The map ν is an isomorphism where the quartic has only one double root and all other roots are simple. This can be seen by locally separating the coprime root clusters: the degree-two cluster has discriminant zero and a unique smoothly varying double root. Thus every non-isomorphism lies over N∪W, and its upstairs support is R∪S.

For precise local models, separate coprime monic factors in an étale neighborhood. The differential of multiplication of monic coprime factors is an isomorphism: if δg·h+g·δh=0, coprimality and the degree bounds imply both variations are zero. Consequently root-cluster factorization supplies étale local coordinates, and discriminants multiply by a unit times the individual discriminants.

At a triple root and a distinct simple root, the discriminant is the cubic discriminant times a unit. Center the cubic; a cubic with a marked double root has centered roots a,a,-2a, hence coefficients -3a² and 2a³. Transversely, the completed normalization is therefore

    k[[t²,t³]] ⊂ k[[t]],                              (3)

with smooth stratum coordinates retained. Its conductor is t²k[[t]], and its normalization quotient is k, the reduced stratum module. In particular the conductor order along R is two.

At two distinct double roots, split the polynomial into two coprime quadratics. Their discriminants x,y are independent smooth parameters and D has equation xy=0 times a unit. Its completed transverse normalization is

    k[[x,y]]/(xy) ⊂ k[[x]] ⊕ k[[y]],                  (4)

with equal constant terms on the left. The conductor is (x)⊕(y), and the quotient is k by the difference of constant terms. Thus the conductor order on each normalization branch, and hence along the irreducible divisor S, is one. Completion and étale localization are faithfully flat, so these calculations establish the generic orders and reduced generic quotient assertions on D itself.

## 2. Finite duality proves the exact upstairs ideal

D is a hypersurface, hence Gorenstein, with ω_D=O_D(6-5)=O_D(1). Finite duality identifies

    ν_*ω_T = Hom_D(ν_*O_T,ω_D).                       (5)

One way to justify the sheaf statement without an unstated vanishing assumption is to apply finite duality to the normalized dualizing complexes ω_D[3] and ω_T[3]. Since T is smooth and both schemes have dimension three, comparison in degree -3 gives (5); the other degrees also give the corresponding positive Ext vanishing. This is the finite right-adjoint identity in [Stacks, §48.19](https://stacks.math.columbia.edu/tag/0AU3), items (4) and (6).

For a local finite birational inclusion A⊂B in the common fraction field K, each A-linear map φ:B→A becomes a K-linear endomorphism of K, hence multiplication by c=φ(1). Its condition is exactly cB⊂A. Thus evaluation at 1 identifies

    Hom_A(B,A) = {c∈A:cB⊂A} = I,                     (6)

the conductor, as a B-module and as an actual ideal inside B. The duality trace is this evaluation map after tensoring with ω_D; no ordinary algebra trace or division by a degree is being used.

Equations (5)-(6) identify the conductor B-module upstairs with

    ω_T⊗ν*ω_D^(-1)=O_T(-2,-3)⊗O_T(-2,-1)
                         =O_T(-4,-4).                (7)

Crucially (6) gives an injection of this invertible sheaf into O_T. Therefore the conductor is an effective Cartier ideal, not merely a rank-one module with that numerical class. Its support lies in R∪S. The two generic local calculations show its divisor is exactly 2R+S, proving (1). On a smooth integral scheme an invertible ideal is determined by its Cartier divisor, so no codimension-two correction can remain at R∩S. Equality of classes alone would not prove this.

For an explicit chart valid also at every quadruple root, choose the root coordinate so all roots are finite and normalize the quartic to be monic. Write

    f(x)=(x-a)²[(x-a)²+u(x-a)+v].

Then B=C[a,u,v] is the normalization chart, R=(v), S=(u²-4v), and the quadruple curve is (u,v). Thus the full conductor ideal is

    I B=(v²(u²-4v)).                                 (8)

The scheme intersection R∩S is (v,u²), so the divisors are tangent along C. Formula (8) includes this nonreduced intersection; replacing the support by a transverse crossing would be incorrect.

## 3. Downstairs conductor: a reduced determinantal union

Let M=ν_*O_T, now regarded as a sheaf on Y by the closed inclusion of D. For every integer t, Künneth gives

    H¹(T,O(2t,t))=H²(T,O(2t,t))=0.

Indeed the possible H¹ term requires simultaneously t≤-1 on P¹ and t≥0 on P²; the possible H² term requires simultaneously t≥0 on P¹ and t≤-3 on P². All other intermediate terms vanish. The full section module of M is therefore Cohen–Macaulay of dimension four over the five-variable homogeneous coordinate ring. Equivalently its sheaf resolution has length one. This uses the full section module, which is saturated and has no degree-zero or degree-one local-cohomology defect.

M is 1-regular: the remaining condition H³(M(-2))=0 holds since H²(P²,O(-2))=0; H⁴ is zero by support dimension. The degree-t section dimension for t≥0 is

    h⁰(M(t))=(2t+1) binom(t+2,2),
    Hilb(M)=(1+5z)/(1-z)^4=(1+4z-5z²)/(1-z)^5.

There is one degree-zero generator, the unit; degree one has dimension nine and the ambient coordinate multiples of the unit span a five-dimensional subspace. Thus there are four further minimal degree-one generators. Regularity and minimality force all first syzygies to have degree two, and the Hilbert numerator gives five of them. Consequently

    0→O_Y(-2)^5 --Bmat→ O_Y⊕O_Y(-1)^4→M→0.           (9)

The unit summand maps with image O_D; its kernel is O_Y(-6), generated by the quartic discriminant. Delete the row of Bmat landing in O_Y. If A_mat is the resulting 4×5 matrix of linear forms, then

    O_Y(-2)^5 --A_mat→O_Y(-1)^4→Q→0,
    Q=M/O_D.                                         (10)

More precisely, the kernel of A_mat is O_Y(-6): under Bmat it maps isomorphically onto the kernel of the unit O_Y→M. Thus

    0→O_Y(-6)→O_Y(-2)^5→O_Y(-1)^4→Q→0.              (10a)

Let J=Fitt₀(Q), generated by the five maximal minors of A_mat. The support of Q is exactly N∪W, by (3)-(4) and the isomorphism statement outside it. Both components have codimension two in Y, so J has height two. Hilbert–Burch therefore supplies

    0→O_Y(-5)^4→O_Y(-4)^5→J→0.                       (11)

The corresponding homogeneous quotient is Cohen–Macaulay of codimension two, with no embedded associated primes. At the generic point of N or W the local quotient Q is exactly the residue field of that stratum by (3)-(4). Its zeroth Fitting ideal is therefore the reduced prime ideal there. A noetherian ring with no embedded associated primes which is reduced at each minimal prime is reduced: any nonzero nilpotent submodule would have an associated prime, necessarily minimal, contradicting that localization. Hence J is the reduced ideal of N∪W everywhere, including C.

For every finitely presented module, Fitt₀(Q)⊂Ann(Q), and both have the same radical. Since J is already radical,

    J ⊂ Ann_Y(Q) ⊂ rad Ann_Y(Q)=J.

Thus Ann_Y(Q)=I_(N∪W)/Y. Restricting to D gives (2), and extension to T gives (1) again. This distinguishes the reduced downstairs union from the doubled cusp divisor upstairs and from any Jacobian singular subscheme.

As a consistency check, (11) gives degree ten. N has degree six: its birational parametrization P¹×P¹→N, (l,m)↦l³m, pulls a hyperplane back to (3,1), whose self-intersection is six. This also agrees with the previously established (2,3) complete-intersection description. W has degree four: the square map P²→P⁴ is a closed embedding with hyperplane pullback O_P²(2). Injectivity follows from equality of squares up to scalar; its differential is injective because q·δq being proportional to q² forces δq proportional to q. Properness then gives the embedding (or use the corresponding projection of the Veronese surface). Degree ten agrees with the reduced union. This degree count is not being used instead of the unmixed/generic-reduced proof.

### Equivariant generators and their exact pullback

Write V_n=Symⁿ(C²), with the usual harmless dual convention. The degree-one normalization sections are V₂⊗V₂=V₄⊕V₂⊕V₀. The V₄ summand comes from Y, so the four extra generators are V₂⊕V₀. Equivariant complete reducibility permits these choices in (9). In degree two,

    H⁰(T,O(4,2)) = V₄⊗Sym²(V₂)
                   = V₈⊕V₆⊕2V₄⊕V₂⊕V₀.

Comparing with Sym²(V₄)⊕[V₄⊗(V₂⊕V₀)] shows that the five quadratic relations form V₄. Therefore (9) can be chosen equivariantly as

    V₄⊗O(-2) → O⊕(V₂⊕V₀)⊗O(-1).

The five maximal minors likewise form V₄ (all determinant characters of SL₂ here are trivial). Their pullbacks, of bidegree (8,4), are divisible by the actual conductor equation Res(l,q)²disc(q), of bidegree (4,4), and the quotients are sections of O_T(4,0). This defines a nonzero equivariant map V₄→H⁰(T,O(4,0))=V₄, hence an isomorphism up to scalar. Nonzero follows because no nonzero quartic generator can vanish on the degree-six irreducible hypersurface D. After compatible bases, the five pullbacks are thus a common nonzero scalar times

    Res(l,q)²disc(q) · (l₀⁴,l₀³l₁,l₀²l₁²,l₀l₁³,l₁⁴).

The last five factors have no common projective zero. This verifies exact generation of the extended conductor ideal even at quadruple roots; it is not merely a comparison of divisorial valuations or numerical classes. No selected quartic or matrix rank is evaluated.

## 4. Exact conductor-square section descent

Write I for the conductor on D, Z=V_D(I)=N∪W with its reduced structure, E=V_T(I O_T)=2R+S, and π:E→Z the induced finite map. Locally A⊂B and I is a common ideal in both rings. The elementary identity

    A = B ×_(B/I) (A/I)                              (12)

holds: a b∈B whose residue is in A/I differs from an element of A by an element of I⊂A. Thus there is a canonical exact sequence

    0→O_D→ν_*O_T⊕O_Z→ν_*O_E→0,                      (13)

where the final map is restriction minus pullback. It is surjective as a sheaf map because B→B/I is surjective. In particular

    Q ≅ ν_*O_E / O_Z.                               (14)

All maps include the scheme structures, in particular the tangency at C. For any vector bundle F on D, tensoring is exact and projection formula gives

    0→F→ν_*ν*F --dsc_F→ F⊗Q→0.                      (15)

A regular normalized section s descends precisely when its restriction to E lies in the image of sections on Z, locally as in (12), or equivalently dsc_F(s)=0. This criterion is global without imposing an unjustified surjectivity on global sections.

The monic chart makes (12) a fully specified algebra test. Expanding f above gives coefficients

    c1=u-4a,
    c2=v-3au+6a²,
    c3=-2av+3a²u-4a³,
    c4=a²v-a³u+a⁴.

The discriminant chart ring is A=C[c1,c2,c3,c4]⊂B=C[a,u,v]. With h=v²(u²-4v), the residue algebra A/I is exactly the image of that displayed subalgebra in B/(h). Thus f∈B descends iff its residue modulo h is in the subalgebra generated by those four displayed residues. This is an exact chart description covering quadruple roots, not a test on a selected polynomial instance.

Away from C, (15) reduces to familiar conditions. At R\S it is the first-normal-derivative condition in the cusp model (3): the coefficient of t¹ must vanish. The derivative is taken along the kernel of dν, with stratum coordinates fixed, not along an arbitrary transverse vector. At S\R it is equality of the two branch restrictions, equivalently invariance under (l,m)↔(m,l). For bundle sections, apply these conditions in frames pulled back from F; those transition functions already descend.

For example, in the monic chart the kernel direction on R is spanned by

    K=∂a+4∂u+3u∂v,  at v=0.

It annihilates the differentials of all c_i along R. For u≠0 it is transverse to R; at u=0 it becomes tangent to R. This degeneration cautions against extending a freely chosen transverse derivative test to the quadruple locus. The exact condition there is (12)-(15). We do not replace the scheme-theoretic conductor-square condition by an unproved assertion that separate generic derivative and value tests suffice.

## Publication boundary

The polar-layer application is published separately as POLAR-LAYER-APPLICATION.md in the conductor section-lifting unit. The proof above is pure binary-quartic geometry and requires no actual HM-module identification.
