# Discriminant stratification of the hidden Type II first symbol

## Theorem and precise scope

Assume an actual source126 Type II occurrence and full compatibility of its
negative-pencil radical with the canonical invariant product Q. Suppose its
joint-annihilator footprint is one of the two P-surplus rows

    (r,epsilon,d)=(1,1,0) or (2,0,0)

of the pinned Type II joint-annihilator theorem. Here the d in the footprint
is an integer multiplicity and is NOT a scalar coefficient below.

Write U=Ann_J N2 and Z=Ann_J N4. The internal two-term map Q|U has kernel
A+D and cokernel D. The full internal first symbol of Q+tT_a is

    b_a:A+D→D,    b_a(k,h)=[T_a(k+h)] mod Q(U),
    a∈A=Sym²W, D=Sym⁴W.                                    (1)

After any fixed G-equivariant identifications of these three irreducible
copies with the binary-form models, there are scalars lambda,mu with
lambda≠0 such that

    b_a(k,h)=lambda·a k + mu·{a,h}_1,                       (2)
    {a,h}_1=(∂_x a)(∂_y h)-(∂_y a)(∂_x h).

For EVERY nonzero a, the exact ranks are:

| scalar alternative | quadratic a | rank b_a | kernel dimension | cokernel dimension |
|---|---|---:|---:|---:|
| mu=0 | arbitrary nonzero | 3 | 5 | 2 |
| mu≠0 | square, discriminant zero | 4 | 4 | 1 |
| mu≠0 | nonsquare, discriminant nonzero | 5 | 3 | 0 |

Thus if mu≠0, the non-surjective locus of the internal first symbol in
P(A) is EXACTLY the binary-quadratic discriminant conic. This is a
set-theoretic rank-locus statement, not a claim of scheme multiplicity.
At a=0 the symbol is zero regardless of the coefficients.

No value or vanishing choice for the ACTUAL scalar mu is established.
Neither alternative is asserted to occur. This theorem concerns an
INTERNAL first symbol whose cokernel maps to zero in the original
cokernel; it does not contradict original first-Bockstein vanishing,
determine an original higher obstruction, exclude a source, or decrement
the catalogue frontier.

## 1. Pinned interfaces and absence of extra representation channels

INPUTS.json records the exact immutable inputs and their hashes. The
Type II joint-annihilator theorem is PR961 at commit
cc3215b97a5c92a9253a9774d0f25ade0648b6e5, path
research/hm/source126-typeII-joint-annihilator/PROOF.md. It proves,
in the two stipulated rows:

- ker(Q|U) is the unique actual A+D of ker Q;
- coker(Q|U)=D and its map to the original cokernel P is zero;
- the internal bilinear symbol on A⊗A is nonzero;
- every T_a preserves U→Z, so (1) is well-defined and G-equivariant.

The source126 reconstruction theorem PR944, commit
84d7c9b3ee57c0a12c9e99816ec690cd8ea7ffbc, supplies the fixed identification
Sym⁶W=V+P (via H1(O(-8))). Here V,P,A,D are pairwise nonisomorphic
irreducibles of dimensions 3,4,3,5, respectively. All original hypotheses
of the input theorem remain in force; no abstract-symbol model is used
to replace an actual obstruction.

The Clebsch-Gordan decompositions restrict from SL2(W) to G as

    A⊗A = Sym⁴W + Sym²W + Sym⁰W = D+A+1,
    A⊗D = Sym⁶W + Sym⁴W + Sym²W = V+P+D+A.                  (3)

D appears once in each. Hence each of Hom_G(A⊗A,D) and Hom_G(A⊗D,D)
is one-dimensional. The first is spanned by ordinary multiplication
of binary quadratics. The second is spanned by the first transvectant:
it is equivariant under SL2 because the alternating derivative pairing
is preserved by determinant-one coordinate changes, and it is nonzero
(for example {x²,y⁴}_1=8xy³ as a universal polynomial identity).
This proves (2), and the imported nonvanishing of the A-part proves
lambda≠0. The scalars depend on the chosen equivariant identifications;
the dichotomy mu=0 versus mu≠0 and the stated ranks do not.

These arguments do not assume that the actual HM module or its
annihilator admits an SL2 action. The ACTUAL symbol is G-equivariant;
the two one-dimensional Hom spaces force it to equal (2). That
particular universal expression is SL2-equivariant, so its rank can
be analyzed using SL2 covariance in the binary-form models. This
logical direction is essential.

## 2. The multiplication-only alternative

If mu=0, the map on A is lambda times multiplication by a, and the map
on D is zero. For nonzero a, multiplication by a is injective in the
polynomial domain C[x,y]. Thus rank is dim A=3, and the kernel and
cokernel dimensions are 8-3=5 and 5-3=2. This does not use any selected
actual negative quadratic; it is a uniform polynomial-domain argument.

## 3. Square directions when mu is nonzero

A nonzero binary quadratic of discriminant zero is a scalar times the
square of a nonzero linear form. Under a determinant-one change of
variables and multiplication of a by a nonzero scalar, it reduces to
x². Scaling a scales the entire symbol and leaves its rank unchanged.

For a=x², the transvectant operator is 2x∂_y. On the quartic monomial
basis its image is

    span{x⁴,x³y,x²y²,xy³},                               (4)

of dimension four. The multiplication image x²A is
span{x⁴,x³y,x²y²}, contained in (4). Because mu≠0, the D-domain alone
already spans (4); because both input factors have image in (4),
the complete symbol has rank exactly four. Its kernel has dimension
four and its cokernel dimension one.

## 4. Nonsquare directions when mu is nonzero

Over C, a nonzero binary quadratic with nonzero discriminant factors
as a product of distinct linear forms. A determinant-one coordinate
change and a nonzero scalar reduce it to xy. Again only universal
binary-form covariance and scaling are used.

For a=xy, the operator is y∂_y-x∂_x. On x^(4-i)y^i its eigenvalue is
2i-4, which is zero only for i=2. Consequently its image is

    span{x⁴,x³y,xy³,y⁴}.                                (5)

The multiplication image xyA contains x²y², absent from (5). Since
lambda and mu are both nonzero and the two domain summands are
independent, their images sum to all of D. Thus the full symbol has
rank five, kernel dimension three and zero cokernel.

Every nonzero quadratic falls into exactly one of Sections 3 and 4.
Writing a=alpha x²+beta xy+gamma y², its discriminant is
beta²-4alpha gamma. This proves the precise conic locus in the theorem.

## 5. What the stratification does and does not resolve

The old internal A-part statement had rank three for every nonzero a.
The full symbol now has a sharp dichotomy: it stays rank three when
its D-part scalar vanishes, or becomes rank four on the discriminant
and rank five off it when that scalar does not vanish. This is more
than the general bound rank≤5, but does not select the actual branch.

The ambient original first Bockstein still vanishes. The input theorem
identifies the non-acyclic quotient kernel D which removes the internal
first obstruction when corrections outside U are permitted. Therefore
surjectivity of (1) is not surjectivity of the original map Q+tT_a and
is not a complete proof repair.

The verifier checks the universal multiplication and transvectant
matrices symbolically, both normal-form image ranks and containments,
the kernel/cokernel arithmetic, and bounded exact nonzero coefficients.
It authenticates the immutable inputs. These are synthetic universal
polynomial tests, not actual HM coefficient, derivative, parameter,
or instance-rank evaluations. The written proof establishes the result
for all nonzero complex directions; finite tests alone would not.
