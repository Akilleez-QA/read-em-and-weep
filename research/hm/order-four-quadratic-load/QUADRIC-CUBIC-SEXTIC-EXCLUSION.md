# The generic a=1, b=5 branch is excluded

## Scope and inputs

This extends the residual sextic method to the unique-quadric/five-cubic branch. The new steps are generic integrality of its complete intersection and the genus-four Plücker bound. Neither step assumes an integral cubic-base curve. No selected HM coefficients, minors, ranks, or experiments are used.

Work over C with the established actual HM evaluation U⊗O→E: dim U=4, det E=O(5), c2(E)=10, and its six minors generate I_C, with C the reduced union of 25 skew lines. For general H, Z=C∩H consists of 25 distinct points spanning H≅P3, with no three collinear. The projective normalizer acts transitively on the 25 labels, semilinearly over the generic hyperplane parameter; all canonical constructions below are equivariant. The Heisenberg group fixes U and is transitive on C. Use the established vanishings H0(I_C E)=0, H0(I_C(4))=0, and H0(E(-1))=0.

Assume a=h0(I_Z(2))=1 and b=h0(I_Z(3))=5 generically. The unique quadric Q is irreducible, as established for this branch. Multiplication by Q supplies a four-dimensional subspace Q·H0(O_H(1)) of I_Z(3). Its quotient has dimension one; choose a cubic G representing it. Thus D^ci=V(Q,G) is a canonical complete intersection, independent of changing G by Q times a linear form. Since Q is irreducible and G is not divisible by Q, this is a pure Cohen–Macaulay curve of degree six and arithmetic genus four. It contains Z scheme-theoretically.

The family is intrinsic and rational on a dense hyperplane open: the quadric kernel and cubic quotient have constant rank there. Passing to reduced supports and to a flat stratum is permitted in characteristic zero. Geometric components are considered over an algebraic closure of the generic parameter field.

## 1. Its reduced support is smooth at all marked points

Let R=(D^ci)_red. Its degree is at most six. Choose a linear combination q of the six actual quintics that contains no component of R. Such a q exists because their common base on H is exactly Z, so no curve is contained in all of them. Consequently the zero-dimensional Cartier cut q|R has length 5 deg R≤30 and contains all 25 marked points.

The singular locus of the reduced curve R is finite and canonical. The subset of the 25 labels lying in this singular locus is invariant under the semilinear normalizer action. Transitivity forces that subset to be empty or all labels.

At a singular point p of a reduced curve, a nonzerodivisor f in the maximal ideal cannot have colength one: colength one would give (f)=m_p, so the one-dimensional local ring would be regular. Thus, if all 25 marked points were singular, q|R would have length at least 50. This contradicts its length at most 30. Therefore every marked point is smooth on R, and in particular lies on exactly one geometric component.

## 2. A single integral component contains every marked point

The nonempty subsets of Z lying on the geometric components of R form a canonical partition of the 25 labels. Transitivity forces equally sized blocks, so the number r of components meeting Z divides 25. Since r≤deg R≤6, either r=1 or r=5.

If r=5, every such component contains five marked points. No component can be a line, since no three marked points are collinear. These five components would have total degree at least ten, impossible. Hence a unique integral component D0 contains all 25 points.

A general actual quintic meets D0 properly and gives 25≤5 deg D0, so deg D0 is five or six. D0 is canonical (the unique marked component), descends over the generic parameter, and spans H because it contains Z.

If deg D0=5, a proper quintic cut has length exactly 25 and is exactly the reduced divisor Z. Dividing the six restricted minors by such a quintic produces global regular functions on the integral projective curve D0, hence constants. The actual Plücker evaluation is constant on D0\Z. This is precisely the reusable degree-at-least-five constant-Plücker family forbidden by EXCLUDE-FIVE-CUBIC-ENDPOINT.md. That theorem explicitly has no quadric or genus hypothesis.

Thus deg D0=6. Since D^ci has total degree six, it has just this component with generic multiplicity one. Cohen–Macaulayness rules out embedded associated primes, and generic reducedness then implies reducedness. Therefore D^ci=D0 is integral. In particular it is the integral Gorenstein genus-four sextic D, and all of Z lies in its smooth locus. This proves generic integrality rather than imposing it.

## 3. Genus-four determinant image has at most three sections

On D, the actual minors generate I_Z. Their common Cartier divisor is exactly Z. The image J of U⊗O_D→E|D is locally free of rank two: off Z it equals E|D; at a marked point the DVR elementary divisors are 1,t because the determinant ideal is the reduced point ideal and evaluation has rank one. Hence

    det J = L = O_D(5)(-Z),    deg L=5.

The surjection U⊗O_D→J gives a kernel map f:D→Gr(2,U), and the six minors generate L without base points. Adjunction for the (2,3) complete intersection gives ω_D=O_D(1), with degree six. Riemann–Roch and duality yield

    h0(L)=2+h0(M),    M=ω_D⊗L^(-1),    deg M=1.

On an integral projective curve of arithmetic genus four, a degree-one line bundle M has h0(M)≤1. Here is a proof allowing singular D. If s is a nonzero section, its Cartier zero scheme has length one, so it is one smooth point p. A second independent section t cannot vanish at p: otherwise it too has zero divisor p and t/s is globally regular, forcing proportionality. Thus s,t form a basepoint-free pencil and define a finite degree-one morphism D→P1. A finite birational morphism onto the normal curve P1 is an isomorphism (the intermediate finite algebra lies in its function field and normality forces equality). This would make p_a(D)=0, contradiction.

Consequently 2≤h0(L)≤3. Let r be the dimension of the image of the six minors in H0(L). Basepoint freeness and positive degree give r≥2, and thus r=2 or 3.

For r=2, f(D) is a Grassmannian line and f has degree five. For r=3, f(D) spans a plane; 5=deg(f)·deg(f(D)) forces a finite birational map onto an integral plane quintic. The Plücker quadratic equation must vanish on the entire plane, since no nonzero plane quadratic contains an integral quintic. Thus this is an alpha or beta plane. In the plane case the finite birational quotient has length 6−4=2, not the length three of the genus-three branch. No argument below uses that discrepancy length.

This gives exactly the same alpha/line/beta trichotomy as before, with the genus-four bound proved separately.

## 4. Alpha and line remain impossible

For an alpha-plane-spanning image or a Grassmannian-line image, the intersection of all extended kernel planes is a unique line A_H⊂U. Equivalently H0(I_D E)=A_H. The resulting rational map from dual P4 to P(U)≅P3 has positive-dimensional fibers. A fixed nonzero s therefore vanishes on the distinct integral sextics in a positive-dimensional family.

Its section-zero scheme is pure lci degree ten: there is no divisor of zeros by H0(E(-1))=0. A fixed integral surface component S contains the moving sextics. A general family hyperplane meets S properly, giving deg S≥6. Its Heisenberg orbit has size 1,5,or25; total degree ten forces orbit size one. Thus S is invariant.

If no component line L_i of C were contained in S, each S∩L_i would be finite. The maps H↦H∩L_i would all be constant on the irreducible family. Since Z spans H, the hyperplanes would be constant, contradiction. Hence S contains one line, and transitivity gives C⊂S. Thus s∈H0(I_C E), contrary to its vanishing. This argument uses degree six, integrality, spanning, and the marked points, not genus three.

Accordingly the generic case must be beta, with its unique rationally varying three-space B_H⊂U.

## 5. Beta is excluded by the same genus-independent surface arguments

For completeness, the dependency transfer is precise. The fixed-beta surface X_B is defined by Λ²B and is pure locally CM of degree fifteen. A positive-dimensional fixed-B family of these integral sextics produces an invariant component S of degree at least six containing all C. Its degree is divisible by five, leaving degrees ten or fifteen. None of this uses the sextic genus (the old statement included genus three but its proof does not use it).

The degree-ten alternative leaves an invariant quintic surface or five planes. The normalization splitting lemma proves that every integral surface component T⊂X_B contains some line of C: otherwise E pulls to O⊕O(5) on its normalization by extending the complementary-section quotient across finitely many points, contradicting c2(E)·T=10 deg T. An invariant quintic then contains all C and has a quartic equation, contradicting H0(I_C(4))=0; five planes cannot contain 25 skew lines. Hence X_B is reduced integral of degree fifteen. This too is genus-independent.

Outside Γ=κ(C), X_B is smooth near C, its lines are Cartier with self-intersection −1, and ω_X=O_X(C). On a smooth resolution unchanged near C, write H for the pulled-back hyperplane class and C for the sum of lifted lines. Then H²=15, H·C=25, C²=−25. A general moving strict transform D~ has H·D~=6, D~·C=25, and n=D~²≥0, since it belongs to a positive-dimensional algebraic family of distinct integral curves. Hodge index for H+C and D~+C gives

    31² ≥ 40(n+25),    or    40n ≤ −39,

impossible. This uses no genus formula for D.

The beta image cannot be constant: otherwise general hyperplane sections of the fixed integral degree-fifteen X_B would contain the integral sextics, contrary to Bertini. If its image is not contained in Γ, its general image point outside Γ gives exactly the forbidden fixed-surface family. Therefore its positive-dimensional irreducible image is dense in Γ.

At a general point κ(p) of Γ, the established exact ADHPR dictionary identifies X_{κ(p)} with the degree-fifteen elliptic-scroll image. Its normalization is a smooth elliptic quintic scroll Q→E_p with pulled-back hyperplane bundle O_Q(1)⊗q*O_Ep(1). An integral sextic, distinct from its singular elliptic quintic, would have strict transform T birational to it and satisfy 6=h+5d, with h=deg O_Q(1)|T>0 and d its degree over E_p (or zero for a vertical curve). If d≥2 this is impossible; if d=1 then h=1, so T is a line and cannot dominate an elliptic curve; if d=0 then T is a ruling fiber and has h=1, not six. Thus there is no integral sextic. The finitely many modular cusp parameters cannot contain the positive-dimensional beta image.

This excludes beta and hence excludes the generic a=1,b=5 branch. The surviving cases become a=0,b≤3 and a=1,b=4. No conclusion about full Q4 or those remaining cases is claimed.

## Pinned dependencies and checks

All repository paths below are in Akilleez-QA/read-em-and-weep, research/hm/order-four-quadratic-load/ unless specified otherwise.

- EXCLUDE-FIVE-CUBIC-ENDPOINT.md, c159a09d691605f3254d4d01eca07e042647e6d0: genus/quadric-independent constant-Plücker family exclusion; read via GitHub.
- FOUR-CUBIC-SEXTIC-BASE.md, fd58cd7d25b213841fce0c34e5207bc84e62c42f: canonical singular-label/component-partition argument; read via GitHub. Its no-quadric degree-bound step is NOT used here.
- SEXTIC-PLUCKER-FLAGS.md, a82e9aeaad55a4e58a0fea12581bab1dcf42e4b0: actual image-bundle and Grassmannian flag interpretation; read via GitHub. Its genus-three Riemann–Roch step is replaced by Section 3.
- research/hm/sextic-alpha-exclusion/ALPHA-EXCLUSION.md, 212f18bb3afb52171068d1aaf8a0dbfbf9954d2b: no-common-section and moving alpha/line exclusion; read through pinned GitHub commit.
- BETA-DEGENERACY-SURFACE.md, 26240e70230aef0de1f1b8714a06bd644adeec69: checked directly via GitHub that proof uses no sextic genus.
- BETA-RESIDUAL-SURFACE-EXCLUSION.md, 3714d276821366f9b1230abb6cc60b81861bb878: residual-component exclusion.
- BETA-HODGE-SEXTIC-EXCLUSION.md, 57839111ecf315c833651671c4cb633818994637: genus-independent moving-sextic Hodge contradiction.
- GAMMA-SCROLL-SEXTIC-EXCLUSION.md, 38c517ed358c08d776b59ab5def5856106dcdeb5: exact parameter dictionary and genus-independent integral-sextic exclusion. Primary source: https://arxiv.org/pdf/alg-geom/9606013, §§4.14–4.16.

Current PR1 coordination was read through comment 6312850973. This is a mathematical deduction with explicit dependencies, not a formal proof-assistant verification or an independent review. No external write was made.
