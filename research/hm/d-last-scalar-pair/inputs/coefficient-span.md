# Complete sextic-channel support and coefficient-span classification

## Scope and immutable inputs

Work over C with G=SL2(F5), defining doublet W and Sym6 W=V+P, where V and P are inequivalent irreducibles of dimensions three and four. Fix determinant self-duality and invariant apolarity. Write T=Sym5 W, of dimension six, and W' for the other doublet. Full immutable proofs PR1147, PR1150 and PR1148, and the public character source, are retained in inputs/ and authenticated in INPUTS.json. They establish the V and P evaluation kernels and the partial-system apolar method. This note adds the full-system row, exact active-support classification, equality of coefficient span rather than only containment, and the exceptional linear-multiplier strata. It claims no new actual HM profile exclusion.

## 1. All nonzero equivariant sextic subsystems

Semisimplicity and multiplicity one imply that every nonzero equivariant subspace U of Sym6 W is exactly V, P, or V+P. The exact evaluation kernels are respectively

    0 -> W' O(-3) -> V O -> O(6) -> 0,
    0 -> V O(-2) -> P O -> O(6) -> 0,
    0 -> T O(-1) -> (V+P) O -> O(6) -> 0.          (1)

The first two are the retained full proofs. For the third, the evaluation kernel at a parameter line l is the sextics divisible by l, using the fixed determinant identification. Multiplication l Sym5 W is fiberwise injective of dimension six and is exactly that kernel. This proves the third sequence equivariantly and globally.

For multiplication U tensor Sym^d W -> Sym^(d+6) W, the smallest degrees of surjectivity are 2,1,0, respectively. The V row has cokernels P at d=0 and W' at d=1, and kernel W' tensor Sym^(d-3) W for d>=3. The P row has cokernel V at d=0 and kernel V tensor Sym^(d-2) W for d>=2. The full row is onto for every d>=0, with kernel T tensor Sym^(d-1) W for d>=1. These formulas follow by twisting (1) and taking cohomology, not by character matching alone.

In particular the linear V image is T inside Sym7 W=W'+T; every other positive-degree row fills the whole target except this one.

For the polynomial ring A=Sym(W), the three generated ideals have minimal resolutions

    0 -> W' A(-9) -> V A(-6) -> A -> A/(V) -> 0,
    0 -> V A(-8) -> P A(-6) -> A -> A/(P) -> 0,
    0 -> T A(-7) -> (V+P) A(-6) -> A -> A/m^6 -> 0. (2)

The third ideal is m^6 because it contains all sextics. Its quotient Hilbert vector is (1,2,3,4,5,6), length21. The other two vectors are (1,2,3,4,5,6,4,2), length27, and (1,2,3,4,5,6,3), length24. Exactness in every degree follows from the kernel bundle in (1); the module identifications respect multiplication. The shifts are positive, so each resolution is minimal.

## 2. Actual apolar setup and active support

Let d>=1, n=d+6 and k=d-1. Let F be an equivariant saturated negative subbundle of a constant H O, and put S=(H O/F)* inside H* O. Assume H0(S)=0. Assume an actual equivariant saturated line C=O(-n) lies in S and its actual constant-connection osculating directions through order k lie generically in S. Finally assume an equivariant bundle decomposition

    F=F_high direct-sum U O(-d),                   (3)

where U is one of the three systems above and every degree of F_high is greater than -d. This splitting is not assumed horizontal. Negativity excludes d=0 and forces F_high=0 when d=1.

Let q:Sym^n W -> R subset H* be the coefficient map of C, onto its constant image. Initially it may be partial. Dualizing embeds R* into (Sym^n W)*. Compose this injection with the actual projection F -> R* O. The osculating assumption means this map annihilates the universal fibers l^7 Sym^(d-1) W. Their full apolar annihilator is l^d Sym6 W, so the map factors through Sym6 W O(-d). This uses the dual injection before assuming any completeness. Generic annihilation extends globally because it is vanishing of a bundle morphism.

All higher-degree blocks map to zero by degree. On U O(-d), the factor is an equivariant constant map a:U->V+P. For U=V or P it is scalar; for U=V+P it has two independent scalar channels. The map cannot be zero, since otherwise the nonzero constant R would lie in S. Define the active support J=im(a), a nonempty sum of the available V and P constituents, and put r=dim J. This is not necessarily U. In particular a nonzero endomorphism of V+P need not be invertible.

The actual image of F in (Sym^n W)* O has precisely fibers l^d J. Its kernel inside F is the bundle

    B=F_high direct-sum ker(a) O(-d).              (4)

The actual embedding of B in H O is saturated because it is a bundle summand of saturated F. Inactive same-degree constituents must be retained in this kernel; they cannot be omitted from the ambient-rank argument.

## 3. Exact coefficient span, including the exceptional stratum

For any subbundle F of H O, its constant coefficient span is the intersection of all constant subspaces containing its fibers. Its annihilator is exactly H0((H O/F)*). Thus H0(S)=0 means that F spans H. Constant projection H->R* sends this span onto R*. But the projected F has fibers l^d J. Therefore, inside (Sym^n W)*,

    R* = span_l(l^d J) = image[J tensor Sym^d W -> Sym^(d+6) W]. (5)

Here pure dth powers span Sym^d in characteristic zero. Equation (5) is an equality, not just the containment used to prove completeness above threshold.

It gives the complete coefficient-image classification:

- J=V, d=1: R*=T, of dimension6, and q has kernel W' in Sym7 W. The line's coefficient system is necessarily partial.
- J=V, d>=2: R*=Sym^n W, of dimension n+1.
- J=P, d>=1: R*=Sym^n W, of dimension n+1.
- J=V+P, d>=1: R*=Sym^n W, of dimension n+1.

Consequently every nonzero channel is complete for d>=2. At d=1, P-active channels are complete, but V-only support is not. In the exceptional stratum it is incorrect even to leave a possible full eight-dimensional image: equation (5) rules that out.

## 4. Channel-aware codimension bounds

Let m=dim R, c=dim H-rank F, and b=rank B. The constant projection kernel N=ker(H->R*) has dimension dim H-m. Equation (4) gives a saturated negative inclusion B->N O. Rank yields b<=dim N. If b>0 equality is impossible: N O/B is torsion-free as a submodule of H O/B and hence locally free; equal ranks would force B=N O, contrary to negativity. Since rank F=b+r,

    c >= m-r, and c >= m-r+1 when B is nonzero.    (6)

These are necessary bounds, not a claim of optimality in every representation stratum. For d>=2 the rows are

    active V:      c>=n-2, improved to n-1 if B!=0;
    active P:      c>=n-3, improved to n-2 if B!=0;
    active V+P:    c>=n-6, improved to n-5 if B!=0.

For full source U=V+P, single active support automatically makes B nonzero even when F_high=0. This strict improvement is therefore compulsory, not optional. The extra inactive source is negative, so having degree exactly -d does not weaken the saturation argument.

## 5. Exact d=1 ambient and codimension classification

At d=1 there is no high block. Since F spans H, its coefficient map U tensor W -> H is onto. The relevant representations are

    V tensor W=T,
    P tensor W=W'+T,
    (V+P) tensor W=W'+2T.                          (7)

The following lists give all possible ambient representations and codimensions under the stated hypotheses, up to representation isomorphism, not canonical choices of the repeated T summands:

    source V, active V:           H=T,        c=3;
    source P, active P:           H=W'+T,     c=4;
    source V+P, active V:         H=2T or W'+2T, c=5 or7;
    source V+P, active P:         H=W'+2T,    c=7;
    source V+P, active V+P:       H=W'+T or W'+2T, c=1 or7. (8)

Proof of necessity. The first row follows from the nonzero quotient of irreducible T. In the second row, the active coefficient image already has dimension8 and is W'+T; (7) permits no larger ambient. For full source with V-only support, the inactive P O(-1) lies in N O. Its constant span is a quotient of P tensor W=W'+T and must have dimension at least four because its fiber rank is four. The only possible quotient dimensions are0,2,6,8, so that span has dimension at least six. Since R*=T, (7) forces H to contain two T summands, with the W' optional. For P-only support, the inactive V O(-1) has nonzero irreducible coefficient span T inside N. The quotient R*=W'+T then forces H=W'+2T. With both channels active, R*=W'+T and (7) allows only H=W'+T or W'+2T. These arguments use semisimplicity to identify representation subquotients, not assumed constant choices of source complements.

## 6. Universal models realize every d=1 row

All models here are abstract equivariant polynomial inclusions, never selected actual HM/source instances.

First, multiplication V O(-1)->T O is fiberwise injective: ordinary multiplication by l is injective and its coefficient image V tensor W is exactly T in Sym7. Multiplication P O(-1)->Sym7 O is also fiberwise injective and spans W'+T. These realize the first two rows. Their dual polynomial line is the projection of the complete degree-seven line to the corresponding dual coefficient space. It has no base divisor: a nonempty invariant divisor has degree at most seven, less than the minimum projective orbit size twelve. Thus it is saturated. Apolarity gives its containment in the annihilator, and order k=0 requires no further derivatives.

For the full source, the universal coefficient inclusion

    (V+P) O(-1) -> ((V+P) tensor W) O

is fiberwise multiplication by the tautological vector, hence saturated and spans H=W'+2T. Projection to the V coefficient factor, to the P coefficient factor, or full polynomial multiplication gives respectively active V, P, or both. The same apolar construction gives the required saturated C. This realizes all three fourteen-dimensional ambient alternatives in (8).

The eight-dimensional both-active model is full multiplication Sym6 W O(-1)->Sym7 W O. It is fiberwise injective and spans the ambient, and its complete degree-seven line lies in its apolar annihilator.

For the twelve-dimensional V-only model retain the full V coefficient factor T and only the T quotient of P tensor W. The resulting P O(-1)->T O is fiberwise injective. To prove this rather than infer it from dimensions, identify its unique equivariant coefficient map with directional contraction P subset Sym6 W -> Sym5 W=T. A directional derivative on binary sextics has one-dimensional kernel generated by a pure sixth power. No pure sixth power belongs to P: under the invariant apolar form, distinct V and P are orthogonal; a pure sixth power in P would make all sextics in V vanish at the corresponding line, contrary to the already-proved basepoint-freeness of V. Therefore the contraction restriction to P has rank four on every fiber. Its coefficient span is all T by irreducibility. Taking its direct sum with the V multiplication model yields H=2T, a saturated rank-seven inclusion spanning H. Projecting to the first T gives active V, and the same saturated partial degree-seven line as above lies in the annihilator. Thus c=5 is attained.

For center-even ambients the line hypothesis forces n even. Since n=7 at d=1, none of these exceptional rows can occur in a center-even actual ambient. They remain necessary to the general equivariant classification and are valid for the odd-center ambient models just constructed.

## Boundaries and reproduction

Equation (5), the active/inactive support distinction, the exact d=1 strata, and the full-system evaluation row are the new conclusions. This exhausts the three nonzero equivariant sextic subsystems and their scalar-channel supports; it does not exhaust actual Gauss profiles or supply osculating containment for any new HM configuration. The previous profile11 shape exclusion is not counted again. Run python verify.py and python -O verify.py; the exact representation, rank, Hilbert, source-authentication and formal apolar controls must agree with RESULT.json. Finite controls support the written all-degree proof and are not proof-assistant certification.
