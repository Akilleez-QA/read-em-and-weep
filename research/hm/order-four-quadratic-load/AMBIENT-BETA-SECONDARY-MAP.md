# Ambient restriction obstruction as a six-to-thirty secondary map

## Inputs and scope

Let F be normalized HM on P4, E=F(3). Let D lie in the hyperplane H=(ell=0), be an integral ACM sextic of genus three, with ideal resolution on H

0 -> 3 O_H(-4) -> 4 O_H(-3) -> I_{D,H} -> 0.

Assume the generic beta conclusions of BETA-SPLIT-IMAGE-BOUNDARY.md at d755d22d3bf460fe314dd846bda1e893d682b71c: restriction U=H0(E) -> H0(E_D) is injective, h0(E_D)=26, H1(E_D)=0. These remain conditional on the residual beta branch, not its existence or exclusion.

Use the standard primary HM cohomology: H1(F)=C5, H1(F(2))=C10, H1(F(3))=C2; H2(F(t)) vanishes except t=-2, where it is C2; H1(F(t)) is supported at t=0,1,2,3. Also H0(F(2))=0, H0(E)=C4. F(-1) is acyclic and F(-2) has only H2. These latter assertions also follow from the normalized monad 5O(-1) -> 2 Omega^2(2) -> 5O by twisting and Bott cohomology. Higher H3,H4 at the twists used here vanish by Serre duality F*=F(1), the H1 support statement and stability. No selected matrix ranks are inputs.

Public sources: primary support is stated and sourced in research/hm/actual-primary-image-extension/PROOF.md at d5d9bd997145b0ecf7d7bd659a19fb7845afb75f; the sextic resolution is INTEGRAL-SEXTIC-ACM-RESOLUTION.md at 7c7bf54af204daa4a00ddfec0b69e3c3dda94424. All commits are in Akilleez-QA/read-em-and-weep.

## 1. Explicit ambient resolution

Choose coordinates splitting H, and lift its cubic generators g=(g1,...,g4) and linear Hilbert--Burch matrix M (4 by 3) by the same polynomials in these four coordinates. Then gM=0 holds already in the P4 polynomial ring. The mapping cone with multiplication by ell gives the exact locally free resolution

0 -> 3O(-5) -> 7O(-4) -> 4O(-3) plus O(-1) -> I_D -> 0.

Writing the middle term as 3O(-4) plus 4O(-4), its maps are

v |-> (-ell v, Mv),
(a,b) |-> (Ma+ell b, -gb),
(c,d) |-> gc+ell d.

The two composites are zero by gM=0. Exactness follows either from the tensor product of the H-resolution with the regular hyperplane Koszul resolution, or the mapping-cone resolution of the quotient by the new variable ell. Tensoring by the locally free E remains exact:

0 -> A=3F(-2) -> P=7F(-1) -> Q=4F plus F(2) -> I_D tensor E -> 0.   (1)

Thus the actual ambient restriction problem has a fixed finite derived-cohomology presentation, not just a dimension difference.

## 2. Canonical secondary map and forced injectivity

Put K=coker(A -> P), equivalently the image of P -> Q. Acyclicity of P identifies H1(K) canonically with H2(A)=C6 and gives H0(K)=H2(K)=H3(K)=H4(K)=0. The second short exact sequence 0 -> K -> Q -> I_D E -> 0 therefore yields

0 -> H0(I_D E) -> C6 --tau_D--> C30 -> H1(I_D E) -> 0,   (2)

and H^i(I_D E)=0 for i>=2. Here C30 means 4H1(F) plus H1(F(2)); C6 means 3H2(F(-2)). The map tau_D is the composite H2(A) -> H1(K) -> H1(Q), where the first arrow is the inverse of the connecting isomorphism. It is an actual secondary cohomology map from the displayed resolution. It is not a selected numerical matrix evaluation. Basis changes or another presentation give equivalent complexes; the cohomology kernel and cokernel are intrinsic.

Because U -> H0(E_D) is injective, H0(I_D E)=0. Therefore tau_D has rank six, and

H1(I_D E)=coker(tau_D), dimension 24; H^i(I_D E)=0 for i not equal to 1.

This rank is forced abstractly by beta-spanning and exactness, not computed by the prohibited selected-coefficient experiment. In particular any proposed residual beta configuration whose ambient secondary map fails to be injective is impossible.

## 3. The actual 22-dimensional section-lifting target

Restriction 0 -> I_D E -> E -> E_D -> 0 gives

0 -> U -> H0(E_D) --partial_D--> coker(tau_D) --rho_D--> H1(E) -> 0.   (3)

Consequently rho_D is surjective onto C2, and the obstruction space for on-curve sections is the 22-dimensional subspace ker(rho_D). A section lifts to a global section of E if and only if its boundary partial_D vanishes. The induced map

H0(E_D)/U -> ker(rho_D)

is an isomorphism. The vanishing of H1(E_D) does not say every section lifts: only the four-dimensional kernel U lifts out of the 26-dimensional section space.

There is an explicit primary-module formula for rho_D. The composite Q -> I_D E -> E in (1) is multiplication by the four defining cubics g_i on the four F summands and by ell on F(2). Hence define

Psi_D: H1(F)^4 plus H1(F(2)) -> H1(F(3)),
(a1,a2,a3,a4,b) |-> sum_i g_i a_i + ell b.

Then Psi_D tau_D=0, and rho_D is the map induced by Psi_D on coker(tau_D). Equation (3) proves Psi_D has rank two, independently of any selected evaluation. Thus the actual obstruction has the concrete cohomological presentation

H0(E_D)/U = ker(Psi_D) / image(tau_D),

as the middle cohomology of the complex C6 -> C30 -> C2, whose two arrow ranks are six and two. Its dimension is (30-2)-6=22. Cubic multiplication has exactly the required twist F -> F(3), and the last linear multiplication has twist F(2) -> F(3). This presentation records actual maps, not just their dimensions. Although a coordinate splitting of H supplies convenient g_i and M, the resulting middle cohomology is canonically the restriction quotient in (3).

The quotient description of E_D from the beta line gives, additionally,

H0(E_D)/U = H0(O_D(Z)) / image(U/B),

with image(U/B) a one-dimensional span of the distinguished section vanishing on Z (up to scalar). This section-lifting obstruction space is NOT identified with Ext1(O_D(Z),L)=H1(L(-Z)), even though the latter also has dimension 22. One concerns sections of a fixed ambient restriction; the other varies the on-curve extension class.

## 4. Hyperplane-only comparison and a distinct rank still unknown

On H, the restriction sequences and primary cohomology give

H1(F_H(-1))=H2(F(-2))=C2,
H1(F_H)=H1(F)=C5,

and every other cohomology group of either bundle is zero. Tensoring the original Hilbert--Burch sequence by E_H therefore gives a primary multiplication map

mu_D: 3H1(F_H(-1))=C6 -> 4H1(F_H)=C20

whose entries are multiplication by the linear entries of M, with exact sequence

0 -> H0(I_{D,H} E_H) -> C6 --mu_D--> C20 -> H1(I_{D,H} E_H) -> 0,

and H^i(I_{D,H} E_H)=0 for i>=2. If r=rank(mu_D), then the two nonzero possible dimensions are 6-r and 20-r. Unlike tau_D, injectivity of mu_D is NOT proved here: a section on H vanishing on D need not extend to P4. This distinction prevents silently replacing the ambient problem by a hyperplane section problem.

A useful constraint follows from 0 -> E(-1) -> I_D E -> i_*I_{D,H} E_H -> 0. Since H0(I_D E)=0 and H0(E(-1))=0, there is an exact sequence

0 -> ker(mu_D) -> H1(F(2))=C10 -> coker(tau_D)=C24 -> coker(mu_D) -> 0.

Thus the hyperplane extra sections are precisely the kernel of this actual C10-to-C24 map. This is a second, independent exactness check on all dimensions: (20-r) = 24-10+(6-r). No injectivity/surjectivity beyond the stated sequences has been assumed.

## New deduction and remaining limitation

This constructs an explicit ambient secondary-map presentation of the remaining section-lifting obstruction, proves its six-dimensional source injects, computes all ambient ideal-bundle cohomology, and isolates the different hyperplane-only rank question. It does not classify which 22-dimensional extension parameters arise from E, exclude beta, or establish full Q4. The missing information is the actual compatibility of the extension class with ambient restriction, not the already-surjective three-dimensional on-curve principal-parts boundary. No external write, selected HM coefficients, selected rank experiment, or consumed one-shot was used.
