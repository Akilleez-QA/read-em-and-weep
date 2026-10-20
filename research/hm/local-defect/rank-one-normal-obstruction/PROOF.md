> Publication scope: preserved mathematical proof/audit. Historical statements that rank eight remains open are superseded only after the final assembly and all its prerequisites. No source-instance evaluation or formal verification is claimed here.

# Full rank-one neighborhood: exact elimination and regular-nilpotent quadratic obstruction

## Theorem

Work over C with dim V=5 and dim J=20. Let f:V^3→J be the canonical trilinear operation. Import outer reversal, cyclic zero, and structural two-plane injectivity from the proofs listed below. Let Z=V(f) and let R be the rank-one locus with all three inputs nonzero. Then:

1. Locally along R, the full scheme Z is isomorphic to the zero scheme of sixteen explicitly described regular residual functions on a smooth eleven-dimensional space. The seven-dimensional smooth locus R is its zero section, with four remaining normal coordinates p. All sixteen residual functions vanish to order at least two along R. This is an exact scheme presentation, not a fixed-two-plane restriction.
2. At a normalized point (u,u,u), the degree-two normal obstruction is

       Q_u(p) = [f(p,u,p)] in J / f(u,u,V),   p in V/Cu.

   This is well defined, and the normal cone of R in Z is a closed subscheme of the zero scheme of Q in a rank-four bundle. Equality with that quadratic zero scheme is not asserted.
3. A nonzero normal direction [p] has Q_u(p)=0 if and only if it corresponds to a regular nilpotent kernel tensor on a three-plane W containing u, whose associated endomorphism has kernel Cu. More precisely, such a direction determines a unique W and a unique projective tensor [k]∈P(ker T_W) with that property; conversely every such pair gives a direction. Thus absence of these regular nilpotents is an explicit intrinsic sufficient condition for R to be the sole reduced support of Z in a neighborhood of the given point.
4. If R is an irreducible component of Z, its generic multiplicity in the full scheme is at least five. In particular the multiplicity-two result for the fixed-two-plane restriction cannot be the full generic multiplicity of a rank-one component.

No actual kernel, value, rank, matrix, product, polynomial instance, selected input, residue, or jet is evaluated. The statements hold structurally; no absence or existence of the regular nilpotents for the actual operation is claimed.

## Imports

- ../../cubic-loci/two-and-three-plane-zeros/two-plane-cubic-zero-scheme/PROOF.md: outer reversal, cyclic zero, injectivity of T_P:P⊗det P→J, and the classification excluding nonzero rank-two zero triples.
- ../../cubic-loci/repeated-input-slice/repeated-extension-slice/PROOF.md: the map V/Cu→J induced by v↦f(u,u,v) is a locally split rank-four injection for u≠0.
- ../../cubic-loci/global-kernel-incidence/general-three-plane-kernel/PROOF.md: E_W=ker(W⊗Λ²W→Λ³W), factorization through T_W, and E_W≅sl(W)⊗det W.
- ../../cubic-loci/cubic-component-multiplicities/coordinate-component-multiplicities/PROOF.md: ambient framework and dimension twenty of J. Its multiplicity theorem concerns coordinate components, not R.

## 1. Honest coordinates on the full ambient neighborhood

Choose a linear functional ℓ that is nonzero on the line at the point under consideration, and put H=ker ℓ. On the ambient open where ℓ(x),ℓ(y),ℓ(z) are all invertible, define

    u=y,  s=ℓ(x)/ℓ(y),  t=ℓ(z)/ℓ(y),
    p=x/s−u,  w=z/t−u+p.

Then p,w∈H and conversely

    (x,y,z)=(s(u+p),u,t(u−p+w)).

These are algebraic inverse coordinates, with u∈{ℓ≠0}, s,t∈G_m, p,w∈H. The factors s,t multiply f by the unit st and hence do not change its zero ideal. The locus R in this chart is exactly p=w=0. Its base coordinates (u,s,t) have dimension seven.

Put, as universal bundle expressions depending on u and p,

    A_u(w)=f(u,u,w),
    B_{u,p}(w)=f(p,u,w),
    F_u(p)=f(p,u,p).

Formal trilinearity and outer reversal give the exact identity

    f(u+p,u,u−p+w)=(A_u+B_{u,p})w−F_u(p).

Indeed the constant term vanishes, and the two terms f(p,u,u) and −f(u,u,p) cancel. No input specialization or operation value is computed here.

The bundle map A:H→J over {ℓ≠0} is a locally split injection by the imported repeated-input theorem. Shrink on that base and choose a left inverse L:J→H and a complementary rank-sixteen projection π:J→C, so (L,π) identifies J with H⊕C, LA=I and πA=0.

Define D=I+LB. Its determinant equals one along p=0, so it is invertible on an open containing the entire local zero section. The H component of f=0 is precisely

    Dw=LF,

and therefore w=D^(-1)LF. Substitution gives the exact remaining equation

    G(u,p)=πB D^(-1)LF−πF=0.

Thus elimination is an actual isomorphism of schemes on this open, with inverse given by the displayed w. It commutes with base change, since every inverse used is the inverse of an explicitly invertible bundle map. The independent variables are (u,s,t,p), of total dimension eleven.

After multiplying by the unit det D, an equivalent equation is

    πB adj(D)LF − (det D)πF=0.

Its sixteen components have degree at most six in the four p coordinates. This degree bound is optional; the rational expression is already regular on the indicated open. It provides a finite exact presentation rather than an infinite formal series.

## 2. Quadratic normal obstruction and normal cone

B is homogeneous of degree one in p and F of degree two. Therefore

    w=LF + terms of p-order at least three,
    G=−πF + πBLF + terms of p-order at least four.

These identities are identities of universal power series in a formal neighborhood, not evaluations of jets at selected inputs. In particular the residual ideal is contained in (p)^2, and its degree-two terms are precisely the components of −πF.

The quotient class Q_u(p) does not depend on a representative of p modulo Cu: replacing p by p+cu changes F by

    c f(u,u,p)+c f(p,u,u)=2c A_u(p),

with the c² term zero. Thus the quadratic expression has an intrinsic value in J/im A_u. Choices of complement and target splitting merely give its local expression πF.

Let I_R denote the zero-section ideal in O_Z. Its associated graded algebra is a quotient of Sym(H*) over the base. Since the initial forms of the residual generators include the components of Q, the normal cone Spec(gr_(I_R) O_Z) is a closed subscheme of V(Q). Higher combinations of equations may impose further initial equations, so no equality is inferred from this argument. In particular every actual normal direction of a degeneration out of R satisfies Q=0; the converse can fail through higher obstructions.

## 3. Regular nilpotents are exactly nonzero quadratic-obstruction zeros

Fix u≠0 abstractly and use H as above. If p≠0 and Q_u(p)=0, injectivity of A_u gives a unique q∈H satisfying

    f(u,u,q)=f(p,u,p).

The vector q cannot belong to span(u,p). Otherwise q∈Cp because q,p∈H, and the equation would identify f(p,u,p)=−2f(p,p,u) with a multiple of f(u,u,p). The two-plane injection T_span(u,p) says these two vectors are independent. This is a contradiction. Thus W=span(u,p,q) has dimension three.

The tensor

    k=2p⊗(u∧p)−u⊗(u∧q) ∈ E_W

lies in ker T_W, because its image is f(p,u,p)−f(u,u,q). Let ω=u∧p∧q. Under E_W≅sl(W)⊗det W, write k=N⊗ω. Direct universal contraction gives

    N(u)=0,  N(p)=u,  N(q)=2p.

Consequently N³=0, N²≠0, rank N=2, and ker N=Cu: this is a regular nilpotent endomorphism. These rank statements concern the displayed universal normal form, not the rank of any actual operation map. Rescaling p by a nonzero scalar c rescales q by c² and k by c², so W and [k] depend only on [p]∈P(V/Cu).

Conversely let W contain u and let [k]∈P(ker T_W) correspond to a regular nilpotent endomorphism with kernel Cu. Its image is a plane containing Cu. Choose p∈H representing a nonzero vector of this image modulo Cu, and q_0∈W∩H completing u,p to a basis. A traceless nilpotent endomorphism with that kernel and image has the form

    N(u)=0,  N(p)=αu,  N(q_0)=βu+γp,

where α and γ are nonzero. In the determinant trivialization ω_0=u∧p∧q_0, its tensor is

    k=γp⊗(u∧p)+u⊗(βu∧p−αu∧q_0),

up to a nonzero common scalar. Rescaling the tensor by 2/γ and putting

    q=(2α/γ)q_0−(2β/γ)p

expresses its projective class as 2p⊗(u∧p)−u⊗(u∧q). Its image under T_W is zero, hence A_u(q)=F_u(p), proving Q_u(p)=0. Uniqueness of q follows from injectivity of A_u; the recovered direction is image(N)/Cu. These constructions are inverse on geometric points. No claim concerning an unproved incidence-scheme identification is needed.

This gives the promised intrinsic description of the projective quadratic zero locus. It detects candidate directions; it does not assert their integrability to actual independent zero triples.

## 4. Empty quadratic projectivization isolates the rank-one support

Suppose Q at the chosen base point has no nonzero zero over C. The relative projective zero scheme V(Q)⊂P(H) over the base is projective, so its image is closed. Removing that image gives a base neighborhood on which every projective fiber is empty. The homogeneous ideal of Q therefore contains a sufficiently high power of the positive-degree ideal locally on this base.

Equivalently, the normal cone in Section 2 has set-theoretic support only the zero section. To see the consequence directly with the exact equations, pass to the local ring at the chosen rank-one point and let m=(p) be the ideal of R after elimination. The quadratic-initial ideal contains some power of m, so for some n the residual equations imply

    m^n ⊂ m^(n+1)

in O_Z locally. Nakayama applied to the finitely generated module m^n gives m^n=0. Thus m is nilpotent locally: Z has exactly R as its reduced support in an open neighborhood of the point. In particular R is an irreducible component there. This does not prove the no-nilpotent hypothesis for any actual u.

## 5. Full-component multiplicity cannot be two

Assume R is an irreducible component of Z, meaning the closure of R is an irreducible component and we work at its generic point. Its local ring is then zero-dimensional and Noetherian, hence Artinian. In the exact presentation its residue field is K=C(R), its maximal ideal is generated by the four coordinates p, and all residual equations lie in (p)^2. Therefore

    dim_K m/m²=4.

The length satisfies

    length(O_(Z,η_R)) ≥ length(O_(Z,η_R)/m²)=1+4=5.

This remains true if other components meet a proper closed subset of R; they do not change the generic local ring. If instead R is contained in a larger irreducible component, a generic-component multiplicity for R is not defined, and this statement does not assign one.

The fixed-two-plane calculation has only one surviving normal coordinate, hence its length-two result is compatible with this theorem. Pullback to that incidence slice does not preserve the generic local length of a full ambient component.

## Boundary of the result

The exact local Schur-complement presentation and nilpotent quadratic criterion are unconditional. The actual quadratic base locus, higher initial equations, existence of independent degenerations, componenthood of R, and the exact generic length remain undetermined. The theorem introduces a finite four-variable local obstruction problem and a lower bound of five whenever the rank-one locus is a component; it does not substitute a numerical or polynomial-instance computation for the prohibited evaluations.

## 6. A global structural dichotomy

Let D be the closure of R, namely the irreducible rank-at-most-one determinantal cone. Exactly one of the following component alternatives holds:

- D is an irreducible component of Z. Its generic multiplicity is at least five. Moreover the full scheme Z is nonreduced at every point of D: its coherent nilradical is nonzero at the generic point of D by the length calculation, and the support of a coherent module is closed, hence contains that generic point's entire closure D.
- D is contained properly in an irreducible component C of Z. This component is the closure of its independent-zero locus. Consequently every point of D is in the closure of independent zero triples.

For the second assertion, C has dimension greater than dim D=7. Its all-inputs-nonzero open is nonempty because it contains R. On that open the imported classification allows only rank one and rank three. The open cannot be contained in D: otherwise its closure C would be contained in D. Therefore C has a nonempty rank-three open, which is dense because C is irreducible. This proves the assertion.

The alternatives classify componenthood, not exclusivity of individual boundary points: in the first alternative a proper closed subset of D may also meet independent-zero components. Neither branch is asserted to occur for the actual canonical operation without further information.
