# Prior mathematical audit

This audit concerns the source manuscript. It is not a formal verification or a review of later normalized publication bytes.

# Independent audit: diagonal–Hartogs K7 proof

## Result

**Passed.** I independently checked the argument in `PROOF.md`, including its direct treatments of both common-factor cases and the three-dimensional subspace lemma. No mathematical gap was found. Over C, the stated conclusion holds: for every seven-dimensional K ⊂ Sym²E with dim E = 4 and every square-avoiding linear v:K→E, the ordered distinct compatible-pair locus has dimension at most two.

The written proof is self-contained relative to standard intersection theory, finite normalization, Hartogs extension on a normal variety, and elementary Chern-class facts. It no longer depends on an earlier K6 theorem or a separate common-radical theorem.

## Checks of the extension lemma

1. **Meeting the diagonal.** For an effective integral threefold Z ⊂ P³×P³, all mixed degrees d_i = deg_Z(h1^i h2^(3−i)) are nonnegative. The positive degree of the ample class (h1+h2)^3 ensures at least one d_i is positive. Therefore deg([Z]·[Δ]) = Σ d_i > 0. If Z were disjoint from Δ this intersection product would vanish. Proper intersection is not needed for this implication: the refined intersection is supported on Z∩Δ.

2. **Normalization and codimension.** Normalization of an integral complex projective variety is finite and surjective. Hence a diagonal locus of dimension at most one has inverse image of dimension at most one in its three-dimensional normalization. The complement therefore removes a closed subset of codimension at least two. Non-normality of Z causes no problem.

3. **Correct bundles and regular coefficients.** With L1 and L2 the pullbacks of O(1,0) and O(0,1), respectively, the tautological vectors are sections of E⊗L1 and E⊗L2. Their product, and v applied to it, are sections twisted by L1⊗L2. Thus the coefficients in v(ab)=αa+βb belong to L2 and L1, respectively, exactly as stated. Off the diagonal the two tautological lines form a rank-two subbundle of the constant E-bundle. A section taking values in this subbundle has unique regular coordinates. This remains true after normalization, even if N is singular.

4. **Closure does not create an off-diagonal problem.** The condition ab∈K is closed. The wedge condition a∧b∧v(ab)=0 is also closed wherever ab∈K. On the off-diagonal locus it is equivalent to compatibility. Consequently dense generic compatibility gives compatibility throughout the off-diagonal part of Z.

5. **Hartogs and evaluation.** Sections of an invertible sheaf on a normal variety extend uniquely across codimension at least two, by local trivialization and the normal Hartogs property. The extended identity holds by density. At a point over the diagonal, both tautological vectors are multiples of the same nonzero e, and their product is a nonzero multiple of e². The identity therefore gives v(e²)∈Ce. Also e²∈K by the closed product condition. This is precisely the prohibited square-compatible point.

## Direct exceptional-case checks

### The P(A)×P(A) lemma

For dim A=3, the diagonal class is h1²+h1h2+h2². Multiplication by h1+h2 gives degree 2(deg_Z h1²h2+deg_Z h1h2²), which is positive on any threefold in P²×P² by ampleness; the pure cubes vanish. Thus the smaller ambient product supplies the required nonempty diagonal intersection.

If the normal component Q(a)=q(v(a²)) is nonzero, the compatible closure satisfies the closed equation q(v(ab))=0. Its diagonal intersection is consequently contained in the projective zero locus of a nonzero plane quadratic, of dimension at most one. The extension lemma applies even though all squares from A lie in K: only the actual diagonal intersection needs this dimension bound.

If Q is identically zero, polarization over C implies v(Sym²A)⊂A. The induced section of the universal quotient bundle Q_A⊗O(2) on P² has top Chern class c2= h²+2h²+4h²=7h². A nowhere-vanishing section would force this top Chern class to vanish. Hence a zero exists, giving an eigenline, with zero eigenvalue allowed. Square avoidance excludes it.

### A common linear factor with z∉L

The decomposition E=Cp⊕A and K=Cp²⊕Sym²A is correct. The cross-term equation xw+yu=0 yields precisely P(A)×P(A) together with the graph of [xp+u]↦[xp−u]. An integral threefold not contained in the first component must equal the entire graph. Dense compatibility then extends to all distinct graph pairs. For fixed u≠0 the displayed relation at p±tu holds for every t≠0, and its limit at zero places v(p²) in span(p,u). Intersecting these planes over u∈A gives Cp, a contradiction.

### A common linear factor with z∈L

The three polar equations written in the proof give exactly P(A)×P(A) and the two stars through r=ker L. In particular rE⊂K, so every expression used in the star argument is defined. An integral threefold in either star equals that star. Taking a=r+tu and then t→0 puts v(r²) in every span(r,u), hence in Cr. This contradicts square avoidance. The P(A)×P(A) lemma treats the remaining component.

## Exhaustion and dimension

A three-dimensional net of quadrics with a common polynomial factor must have a common linear factor; a common degree-two factor would leave a space of dimension at most one. Without a common factor its base locus in P³ has dimension at most one, since any surface component would be a common hypersurface factor. These alternatives exhaust all K7.

If the compatible locus had dimension greater than three, its closure admits an integral projective three-dimensional section meeting the dense compatible distinct-pair open subset. Applying the same argument to that section is legitimate. Thus excluding threefolds excludes every dimension greater than two.

## K8 coprime-pencil consequence

The same extension lemma also proves the bound for any eight-dimensional K whose two-dimensional annihilator pencil consists of quadrics with no common polynomial factor. The pencil base locus then has dimension at most one, so every hypothetical compatible threefold has diagonal intersection of dimension at most one. This consequence requires no new exceptional-case argument. It does **not**, by itself, settle the K8 pencils having a common linear factor; the K7 common-factor classification must not be silently reused for a two-dimensional L.

## Further K8 consequence: common factor belongs to the pencil's linear span

The K8 common-factor case W=zL with dim L=2 and z∈L is also excluded. Write W=span(z²,zx) with z,x independent, A=ker z, and R=ker z∩ker x. The polar equations give exactly

P(A)×P(A) ∪ P(R)×P(E) ∪ P(E)×P(R).

Indeed z(a)z(b)=0; when z(a)≠0 the other equation forces z(b)=x(b)=0, and the symmetric case is identical. When both z-values vanish the pair is in P(A)×P(A).

The first component is handled by the direct three-dimensional subspace lemma. For the remaining components I checked the universal finite partner-plane theorem in `../rank-three-compatible-fiber-structure/PROOF.md`, Sections 1–2. Its argument is valid independently of dim K: the closed projective parameter space of pairs ([a],U), dim U=3, satisfying aU⊂K and the universal compatibility identity avoids the ample incidence divisor a∈U. Avoidance follows by two independent limits to a². Thus this parameter space has finite reduced support. The fixed-factor matrix pencil has generic rank three when M_a=E, and exceptional kernels have projective dimension at most two; each surface component is a partner plane. If dim M_a≤3, a surface must simply fill the plane P(M_a). Consequently all fixed-factor fibers have dimension at most two, and outside finitely many first factors they have dimension at most one.

Over the projective line P(R), the nonexceptional fibers therefore contribute dimension at most 1+1=2, and the finitely many exceptional fibers contribute dimension at most two. The same holds with the factors reversed. Neither remaining incidence component can contain a compatible threefold.

Combining this with the coprime-pencil corollary, the only K8 annihilator pencils not settled by these arguments are common-factor pencils W=zL with dim L=2 and z∉L. This is a remaining case, not an assertion that a compatible threefold exists there.
