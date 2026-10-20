> Publication scope: Imports public literal existence from PR112. Distinct HH2 torsor dimension and based-gauge separation. Ambient, not module, moduli. Historical statements about unresolved mixed classes refer to the source stage; this packet does not supersede the separately stated conditional mixed-vanishing result in PR145.

# Relative moduli of invariant ambient algebroid lifts

## Result and scope

Let X be an abelian variety of dimension g over C, let iota=[-1], and fix an individually iota-stable affine cover with affine intersections. Consider regular, normalized, differential associative algebroid descent data, with h fixed by iota, classical reductions (ordinary multiplication, identity maps, units 1). Suppose a strictly invariant literal presentation is fixed modulo h^N, N>=3. Allow all three types of coefficients to vary at order N: local binary products, overlap maps, and triple units.

Then the invariant lifts modulo h^(N+1), modulo invariant gauge transformations literally equal to the identity modulo h^N, form a nonempty torsor under HH^2(X)^iota tensor (h^N). Its dimension is binom(2g,2). Every point of this torsor has an invariant coefficientwise formal continuation to all orders. For g=4 this dimension is 28, decomposing as 6+16+6 under HKR.

Moreover distinct points cannot become equivalent through invariant differential algebroid gauges that are only required to be literally identity modulo h^3. This assertion concerns gauges on the fixed base, fixed parameter and fixed cover, with the standard inner 2-morphisms. It does not concern arbitrary unmarked equivalences, base automorphisms, changes of parameter, or non-equivariant gauges. The latter require a separate equivariant-descent argument and are not settled by invariant cohomology alone.

This is a relative-moduli consequence of null's literal lifting theorem, rather than another proof of its substantive descent-coherence identities. It is about ambient algebroids, not modules, and performs no physical model evaluation.

## Sources checked

1. Public source comment:
https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6259748725
2. The fixed-product versus varying-product distinction in the supplied proof at the supplied third-order-automorphism-obstruction proof (fixed-product/varying-product premise).
3. Algebraic differential deformation and crossed-groupoid background: Amnon Yekutieli, *Twisted Deformation Quantization of Algebraic Varieties*, sections 1, 3, and 5:
https://arxiv.org/html/0905.0488

Application to PR16 uses the strict invariance and regularity verified in source 1, and its stated two-jet, pinned at:
https://github.com/Akilleez-QA/read-em-and-weep/blob/c8aec970fd65a105f39f4e8aeb8a17f0f0053f89/research/hm/second-order-algebroid.md
No fresh differentiation or evaluation of that presentation is used here.

## 1. Complex and signs

Write D^q=C_diff^(q+1)(O_X), q>=-1, including arity zero. Cochains of positive arity are normalized. The Hochschild differential is

(bf)(x_1,...,x_(m+1)) = x_1 f(x_2,...,x_(m+1)) + sum_(j=1)^m (-1)^j f(x_1,...,x_j x_(j+1),...,x_(m+1)) + (-1)^(m+1) f(x_1,...,x_m)x_(m+1).

For m=0, (ba)(x)=xa-ax. Let delta be the alternating Cech differential, so (delta t)_ij=t_j-t_i and (delta c)_ijk=c_jk-c_ik+c_ij. Put L=Tot Cech(D) with d=delta+(-1)^p b on Cech degree p. Restriction commutes with b, so d^2=0. In particular,

L^1: z=(u,v,a) in Cech^0 C^2 + Cech^1 C^1 + Cech^2 C^0,
dz=(bu, delta u-bv, delta v+ba, delta a).

L^0: w=(t,c) in Cech^0 C^1 + Cech^1 C^0,
dw=(bt, delta t-bc, delta c).

L^(-1): s in Cech^0 C^0,
ds=(bs,delta s).

These are classical differentials. They are the correct linearization at every one-step extension because I=(h^N) in C[h]/h^(N+1) satisfies hI=I^2=0: multiplication by any positive-order coefficient disappears.

## 2. Lifts are an affine space of cocycles

Use the defects S,H,K,P and orientation from source 1:
F_ij F_jk=Ad(A_ijk)F_ik, and A_ijk A_ikl=F_ij(A_jkl)A_ijl.
The obstruction is O=(-S,H,K,-P). For additive coefficient changes z=(u,v,a) in I tensor L^1, source 1's exact first-order calculation gives

Delta S=-bu, Delta H=delta u-bv, Delta K=delta v+ba, Delta P=-delta a,
hence Delta O=dz.

The calculation works also for the difference of any two genuine lifts of the same literal preceding presentation. Thus their difference is an invariant degree-one cocycle. Conversely adding any invariant degree-one cocycle to a genuine lift gives another genuine lift. No nonlinear remainder survives I^2=0. Consequently, once one lift exists, literal invariant lifts form a torsor under Z^1(L^iota) tensor I.

For existence, source 1 proves dO=0 before the trial lift is repaired. Since H^2(L)^iota=HH^3(X)^iota=0, O has a primitive. Average the primitive, rather than averaging nonlinear descent data. Repairing with its negative gives an invariant literal lift. This use of source 1 retains the freedom to change higher local products; it does not freeze the all-order Moyal product.

## 3. Relative gauges give exactly boundaries

Here is an explicit convention producing the signs above. For chart automorphisms E_i and overlap units B_ij define transformed data by

mu'_i(x,y)=E_i^(-1)(mu_i(E_i x,E_i y)),
F'_ij=E_i^(-1) Ad(B_ij) F_ij E_j,
A'_ijk=E_i^(-1)(B_ij F_ij(B_jk) A_ijk B_ik^(-1)).

All products/inverses in this formula use the unprimed local algebras. These formulas preserve the descent equations by ordinary transport and inner conjugation. Put E_i=id+h^N t_i and B_ij=1+h^N c_ij, with t_i(1)=0. Classical commutativity and hI=I^2=0 give

mu'-mu=h^N bt,
F'-F=h^N(delta t-bc),
A'-A=h^N delta c.

The -bc sign follows from Ad(1+epsilon c)(x)=x+epsilon(cx-xc)=x-epsilon bc(x). In this particular commutative classical setting bc=0; keeping the term records the correct general total-complex sign.

Every normalized degree-zero cochain defines such a relative gauge, with inverse defined by the finite h-adic expansion. Thus the equivalence relation on literal lifts is exactly translation by B^1(L^iota) tensor I, and the quotient is the asserted H^1(L^iota) tensor I torsor. This is a torsor, not a preferred vector space: selecting one lift selects an origin.

## 4. Dimensions and parity

Differential HKR, affine Cech descent, and exactness of invariants over C give
H^j(L^iota)=HH^(j+1)(X)^iota,
HH^n(X)=direct_sum_(r+s=n) H^s(X,Lambda^r T_X).

Let V=H^0(X,T_X) and W=H^1(X,O_X), both of dimension g. The tangent bundle is trivial, H^s(O_X)=Lambda^s W, and inversion acts by -1 on both V and W. Hence
H^s(X,Lambda^r T_X)=Lambda^r V tensor Lambda^s W
has parity (-1)^(r+s). In particular HH^n is entirely even or odd according to n, and its dimension is sum_(r+s=n) binom(g,r)binom(g,s)=binom(2g,n).

For g=4:
- HH^2(X)^iota = Lambda^2 V + (V tensor W) + Lambda^2 W, dimension 6+16+6=28.
- HH^3(X)^iota=0, despite unrestricted HH^3 having dimension 56.
- HH^1(X)^iota=0, despite unrestricted HH^1 having dimension 8.
- HH^0(X)^iota=C.

The three HH^2 summands represent infinitesimal local-product bivectors, overlap deformation classes, and scalar gerbe classes. These are cohomological directions; they are not a claim that arbitrary representatives can be independently kept in only one Cech/Hochschild slot at every nonlinear order.

## 5. All branches continue

Start with any point of the one-step torsor and an invariant literal representative. The same invariant obstruction-vanishing argument applies at the next order, without imposing a special choice on this representative. Iterate inductively. Each transition retains all preceding coefficients literally. Their coefficientwise inverse limit therefore gives a formal differential algebroid over C[[h]], with the specified initial two-jet.

Coefficients are algebraically regular differential operators on the prescribed intersections, individually of finite differential order. No uniform bound in h is asserted. Formality here means h-adic existence; it asserts neither analytic convergence, evaluation at a nonzero numerical h, algebraization over a finite-type parameter base, nor a canonical formula for the higher coefficients.

## 6. Larger invariant gauges fixing the two-jet do not merge distinct branches

Suppose two lifts modulo h^(N+1) agree literally modulo h^N. Let an invariant gauge between them be identity modulo h^3, not necessarily modulo h^N. Its reduction modulo h^N is an automorphism of their common preceding presentation.

We can make this gauge identity modulo h^N by 2-isomorphisms. Inductively suppose it is already identity modulo h^k, with 3<=k<N. Its leading degree-k coefficients w=(t,c) obey dw=0, since its endpoints agree through degree k. The reason is precisely the linearization in section 3; all lower gauge coefficients have been removed, so only the classical differential remains at leading order.

As H^0(L^iota)=HH^1(X)^iota=0, there is invariant s in L^(-1) with w=ds. Inner 2-morphisms are collections of chart units 1+h^k s_i. Their leading change of a gauge is ds (or -ds for the inverse), as follows from chart conjugation and the ratio of the two chart units on each overlap. Use the inverse 2-morphism to kill w. The higher coefficients may change, but neither endpoint changes. These units can be taken directly in the target lifted algebras, so the adjustment is defined at the whole truncated order, not merely modulo h^(k+1).

Continue for k=3,...,N-1. The resulting gauge is identity modulo h^N and still connects the same endpoints. Section 3 now says that their order-N difference is a boundary. Therefore different points of the relative HH^2 torsor cannot be identified by this broader invariant based gauge group.

Consequently any two formal continuations whose first inequivalent relative coefficient differs are inequivalent under invariant gauges identity modulo h^3: any hypothetical formal gauge would truncate to the forbidden finite-order gauge. This proves genuine nonuniqueness, not merely nonuniqueness of literal formulas.

The word “invariant” matters in this proof. Dropping it replaces the zero group HH^1(X)^iota by HH^1(X), which is nonzero. We make no assertion either that non-equivariant gauges do identify these classes or that they cannot: the above argument alone does not decide it. Likewise, a gauge that preserves the two-jet as an object but is not itself identity modulo h^3 is outside the based-gauge statement; it can have an additional stabilizer action.

## 7. Automorphisms are not uniqueness of objects

At one small-extension step, automorphisms of a fixed lift that are identity below that step are degree-zero cocycles; their classes modulo inner 2-isomorphism are H^0(L^iota) tensor I=0. This says they are 2-isomorphic to the identity. It does not say there is only one lift, only one literal gauge, or only one 2-isomorphism.

Degree-minus-one cocycles give relative 2-automorphisms of the identity, namely H^(-1)(L^iota) tensor I=HH^0(X)^iota tensor I=C tensor I. Concretely these are global scalar units 1+h^N lambda. For full formal based gauges, scalar units 1+h^3 C[[h]] remain as 2-automorphisms. Their centrality is exact in every normalized C[[h]]-linear deformation.

Thus the appropriate picture is many lift classes, no nontrivial relative invariant 1-automorphism classes, and a surviving scalar 2-automorphism group. Removing arity zero would erase essential gerbe directions and 2-morphism information.

## Audit boundary

This argument makes no assertion about the HM module obstruction, any of the thirty retained detector values, or whether the prescribed T_ij preserve the original Poisson tensor. The fixed-product obstruction in the supplied third-order proof remains valid. The 28-dimensional torsor relies on admitting varying higher local products and scalar triple units, precisely as in null's ambient existence theorem.
