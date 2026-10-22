# Generic primary top multiplication is surjective

## New conditional-to-actual deduction

For the normalized Horrocks--Mumford bundle F on P4, set A_j=H1(F(j)). Using the standard normalized monad and dim A3=2, multiplication by a general linear form is surjective:

ell: A2 -> A3, of rank two.

This is a symbolic module argument, not a selected evaluation. It has a consequence for the residual beta sextic: E_H=F_H(3) satisfies h0(E_H)=12 and H1(E_H)=0 for general H. The residual hyperplane Hilbert--Burch map mu:C6->C20 is not proved injective by this result.

## 1. Primary generation from the normalized monad

Use the normalized monad

5 O(-1) -> 2 Omega^2(2) -> 5 O,

whose middle cohomology is F. If K is the kernel of the right-hand map, then

0 -> K(t) -> 2 Omega^2(t+2) -> 5 O(t) -> 0,
0 -> 5 O(t-1) -> K(t) -> F(t) -> 0.

For every t>=0, H1(O(t-1))=H2(O(t-1))=0, and H1(Omega^2(t+2))=0. Consequently

A_t = coker[H0(2 Omega^2(t+2)) -> C5 tensor S_t].

These identifications commute with multiplication by homogeneous polynomials, since they come from the fixed monad maps. Thus A in nonnegative degrees is a quotient of the free graded module C5 tensor S; in particular A2=S1 A1 and A3=S1 A2.

The differential-form vanishing can be checked directly from the exterior Euler sequence: its global sections are the degree-(t+2) Koszul complex, exact in the relevant middle position. For t>=0 no higher cohomology of the participating line bundles interferes. This avoids assuming the claimed generation solely from a Hilbert table.

## 2. Elementary two-dimensional-target lemma

Let M be a graded module over Sym(V) over an infinite field. Suppose M_{d-1}=V M_{d-2}, M_d=V M_{d-1}, and dim M_d=2. Then some, hence a general, x in V acts surjectively M_{d-1}->M_d.

Proof. If every multiplication map m_x had rank at most one, their linear span would be a vector space of rank-at-most-one matrices. Such a space either has a fixed image line, or all its elements share one covector on the domain:

m_x(a)=f(x) lambda(a).

For completeness, choose one nonzero map u tensor lambda. Any other rank-one map v tensor eta must have v proportional to u or eta proportional to lambda, since otherwise their sum has rank two. If a map with image different from u exists, comparison with both maps forces every covector proportional to lambda. If no such map exists, all images coincide.

A fixed image line contradicts M_d=V M_{d-1} and dim M_d=2. In the shared-covector case f:V->M_d must be onto, again by generation. Choose x,y with independent f(x),f(y). For a in M_{d-2}, commutativity gives

f(x) lambda(y a) = f(y) lambda(x a),

so lambda(x a)=lambda(y a)=0. For any z, compare z with x: f(x)lambda(z a)=f(z)lambda(x a)=0. Thus lambda(z a)=0 for every z,a. Because M_{d-1}=V M_{d-2}, lambda=0, contradicting the existence of a nonzero multiplication map. Therefore some m_x has rank two. Rank two is an open condition, so it holds for general x. QED.

Apply this with d=3 and M=A. The monad proves the required generation, and the standard primary cohomology gives dim A3=2. Hence generic rank(ell:A2->A3)=2.

## 3. New ambient consequences in the residual beta branch

From 0->F(2)->F(3)->E_H->0, together with h0(F(2))=0, h0(F(3))=4, dim A2=10 and generic surjectivity to A3=C2, one obtains

0 -> C4 -> H0(E_H) -> ker(ell:A2->A3)=C8 -> 0,
H1(E_H)=0,

so h0(E_H)=12.

Let D be the residual integral ACM sextic on this general H and assume the already-proved beta values h0(E_D)=26, H1(E_D)=0 and injectivity H0(E)->H0(E_D). If k=dim ker(mu_D), for the Hilbert--Burch map mu_D:C6->C20, restriction on H gives

0 -> C^k -> C12 -> C26 -> C^(14+k) -> 0.

Hence the hyperplane-restriction image has dimension 12-k (equivalently 6+rank(mu_D)), while its cokernel has dimension 14+k (equivalently 20-rank(mu_D)). This is compatible with, and sharper than leaving the primary linear rank unknown in, the ambient secondary-map presentation.

There is also an intrinsic exact comparison on the 22-dimensional global restriction quotient W=H0(E_D)/H0(E):

0 -> H0(I_{D,H} E_H) -> ker(ell:A2->A3) -> W -> H1(I_{D,H} E_H) -> 0.  (*)

To obtain (*), quotient the inclusion H0(E)->H0(E_H) by H0(E), then use the two restriction sequences. The kernel of H0(E_H)->H0(E_D) injects into H0(E_H)/H0(E), because H0(E)->H0(E_D) is injective. The latter quotient is precisely ker ell. Thus the portion of W supplied by sections extending to H has dimension 8-k; the remaining hyperplane obstruction has dimension 14+k.

This does not determine k, prove any extension class ambient-realizable, exclude beta, or solve Q4. It is a new generic primary-surjectivity deduction and a finer exact filtration of the already-known 22-dimensional section obstruction. It does not concern the other 22-dimensional space Ext1(O_D(Z),L).
