# Two-plane cubic classification and its universal zero scheme

## Result and scope

Work over C. Let V=U1 (dimension five), J=J3, and f:V^3→J be the canonical trilinear operation. Import outer reversal f(x,y,z)=f(z,y,x), cyclic zero, and structural nonvanishing f(x,x,y)≠0 for independent x,y. Then:

1. For every two-plane P⊂V there is a unique injective linear map T_P:P⊗det(P)→J such that

   f(x,y,z)=T_P(x⊗(y∧z)−z⊗(x∧y)) for x,y,z∈P.

2. A triple of span dimension at most two has f=0 exactly when its span has dimension at most one or at least one input is zero. In particular every coplanar triple of nonzero inputs spanning a two-plane obstructs the graded-framed filtered rank-eight completion.
3. On Gr(2,V), the maps T_P form a locally split rank-two bundle injection. Thus on the tautological incidence space of triples in a chosen two-plane, the full cubic zero scheme, including its nilpotents, is cut out by the two components of the displayed universal tensor. This statement survives arbitrary base change.
4. On the exact-rank-two triple stratum in V^3, the cubic zero scheme is reduced and smooth, and is the disjoint union of three loci: one labeled input is zero and the other two are independent. Each has dimension ten, codimension two in the rank-two stratum.
5. On a fixed two-plane, the zero scheme in P^3≅A^6 is a codimension-two complete intersection of two cubics, of degree nine. Its reduced support has four irreducible components: the rank-at-most-one determinantal variety and the three coordinate four-planes. It has generic multiplicity two on the determinantal component and one on each coordinate plane, with no embedded associated primes.

The last assertion is about the fixed-plane scheme (and locally the tautological incidence family). It does not determine multiplicities in the full zero scheme in V^3. No assertion about rank-three triples is made.

## Imports and evidence boundary

Read: [the cubic structural nonvanishing manuscript](../../cubic-structural-nonvanishing/cubic-structural-nonvanishing/PROOF.md); [the cubic massey module reduction manuscript](../../canonical-cubic-extension/cubic-massey-module-reduction/PROOF.md); [the cubic filtered extension obstruction manuscript](../../canonical-cubic-extension/cubic-filtered-extension-obstruction/PROOF.md); [the repeated extension slice manuscript](../../repeated-input-slice/repeated-extension-slice/PROOF.md); [the repeated slice blowup manuscript](../../repeated-input-slice/repeated-slice-blowup/PROOF.md). Only their structural nonvanishing, formal symmetries, trilinearity and filtered-extension representability are imported. The preceding repeated-slice results do not already classify arbitrary ordered triples in a two-plane.

All calculations below concern universal tensors and their formal coordinate rings. They are not evaluations of HM/source/model matrices, products, numerical ranks, selected input values, points, jets, residues or Massey values. There are no external writes or local Codex tasks.

## 1. Universal normal form and injectivity

Choose an abstract basis u,v of P, put ω=u∧v, and denote A=f(u,u,v), B=f(v,v,u). The identities give

   f(u,v,u)=−2A,  f(v,u,u)=A,
   f(v,u,v)=−2B,  f(u,v,v)=B,
   f(u,u,u)=f(v,v,v)=0.

These identities describe all eight basis tensors by formal trilinearity. Define T_P(u⊗ω)=A and T_P(v⊗ω)=−B. Direct expansion of the universal tensor

   τ(x,y,z)=x⊗(y∧z)−z⊗(x∧y)

has exactly these six mixed coefficients and the two zero diagonal coefficients, proving f|P^3=T_Pτ. The tensors τ(u,u,v)=u⊗ω and τ(v,v,u)=−v⊗ω span P⊗det(P), so T_P is unique and the construction is independent of the chosen basis.

For formal x=a u+b v and y=c u+d v, one has

   f(x,x,y)=(ad−bc)(a A−b B).

If A,B were dependent, there would be (a,b)≠(0,0) with a A−b B=0. Choose y independent of that nonzero x. The displayed identity contradicts imported structural nonvanishing. Thus A,B are independent and T_P is injective. This is an abstract consequence of the theorem, not an evaluation of an actual cubic value or rank.

## 2. Classification over fields

If the three inputs span at most a line, trilinearity and f(t,t,t)=0 imply f=0. If any input is zero, trilinearity also gives f=0.

Conversely suppose x,y,z span P and all are nonzero. If x,z are independent, τ=0 would force y∧z=x∧y=0 by independence of x,z. This forces y=0, a contradiction. If x,z are dependent, write z=cx with c≠0. Then

   τ=−2c x⊗(x∧y),

which is nonzero because x,y are independent and the characteristic is zero. Injectivity of T_P proves the claim. All arguments and imported nonvanishing persist after field extension.

## 3. Tautological bundle factorization and arbitrary bases

Let G=Gr(2,V), let S be its rank-two tautological subbundle, and set E=S⊗det(S). Local frames give the maps of Section 1 with regular coefficients; uniqueness makes them agree on overlaps. Thus there is a global bundle map

   T:E→J⊗O_G.

It is injective on every closed complex fiber. The locus of failure of a rank-two source to inject is a closed degeneracy locus; if nonempty it would contain a closed complex point, contradicting Section 1. Hence T is locally split injective, with locally free cokernel. This derives a subbundle property from the structural theorem without an actual input rank calculation.

On W=Tot_G(S⊕S⊕S), τ is a section of the pulled-back E and the pullback of f is Tτ. A local left inverse to T shows equality of the component ideals (f)=(τ). Since the left inverse remains a left inverse after every base change, this ideal equality and the zero-functor identification hold over arbitrary, including nonreduced, bases.

For an affine complex test scheme with a specified plane subbundle P_T⊂V⊗O_T, existence of the represented graded-framed filtered completion for three sections is therefore equivalent to τ=0 as a section, not merely to fiberwise support conditions. When it exists, the imported theorem gives uniqueness up to unique graded-framed isomorphism and an actual algebraic universal bundle by pullback.

## 4. The exact-rank-two stratum

Let W°⊂W be the open locus where the three universal sections span S. It identifies with the exact-rank-two determinantal stratum R_2⊂V^3: a spanning triple has a unique image plane subbundle, and this construction works functorially on the open charts where a two-by-two minor is invertible. These are scheme isomorphisms, not just bijections of complex points.

Cover W° by the opens where one of the three pairs is a frame. When x,z form a frame, write y=a x+b z. Then

   τ=(a x−b z)⊗(x∧z),

so its ideal is exactly (a,b); its zero scheme is y=0. When x,y form a frame, write z=a x+b y. Then

   τ=(−2a x−b y)⊗(x∧y),

and the zero scheme is z=0. When y,z form a frame, write x=a y+b z. Then

   τ=(a y+2b z)⊗(y∧z),

and the zero scheme is x=0. The coefficients 2 are invertible over C. These three zero loci are disjoint on W°, as two zero inputs cannot span a plane. They exhaust the zero scheme with its reduced structure.

Each is the independent-pair open subset of V^2, hence smooth of dimension ten. Equivalently each is a frame bundle of S over the six-dimensional G, of relative dimension four. The ambient R_2 has dimension twelve. The local two-equation descriptions are regular embeddings and survive arbitrary base change; no reducedness assertion is intended after base change to a nonreduced base.

Consequently the full filtered-extension moduli scheme restricted to R_2 has precisely this description. In particular there is no completion for any rank-two triple with all inputs nonzero. The restriction says nothing about full-moduli transverse infinitesimal directions leaving R_2.

## 5. The fixed-plane complete intersection

Fix P. Let R=Sym((P⊕P⊕P)^*) be its six-variable polynomial ring and I the two-component ideal of τ. By the field classification, the reduced zero set is the union of

   D={rank(x,y,z)≤1}, X={x=0}, Y={y=0}, Z={z=0}.

The generic 2-by-3 determinantal variety D is irreducible of dimension four: it is the affine cone over the Segre embedding P^1×P^2. Its standard minor ideal is prime, as follows also from the universal rank-one parametrization and its monomial relations. Each coordinate locus is an irreducible affine four-plane. None is contained in another: equivalently the independent-pair open of each coordinate locus is nonempty, and the rank-one cone has a nonempty open with all three columns nonzero. These observations concern universal open schemes rather than selected numerical inputs.

Thus I has height two. Since it is generated by two homogeneous cubics in the regular polynomial ring R, these form a regular sequence. The quotient is a four-dimensional complete intersection and is Cohen–Macaulay and unmixed. In particular it has exactly the four displayed minimal primes and no embedded associated primes. Its Hilbert series is

   (1−t^3)^2/(1−t)^6,

so its degree is nine. This does not assert that I is radical or give a primary decomposition.

## 6. Generic double structure on the rank-one component

The coordinate components have generic multiplicity one by the spanning-open ideal descriptions of Section 4. To determine the rank-one component without source/model evaluation, use a universal affine chart on which the first coordinate of x is invertible. Choose the complementary vector e=(0,1), so x,e form a regular frame on this chart, and write uniquely

   y=a x+b e,  z=c x+d e.

Here x_1,x_2,a,b,c,d are algebraic chart coordinates with x_1 inverted. A purely formal tensor expansion gives

   τ=((ad−2bc)x−bd e)⊗(x∧e).

Therefore the ideal is (ad−2bc,bd). Further localize at a and c. This open meets the generic point of D, and contains none of the three coordinate components. Eliminating d yields precisely

   (ad−2bc,bd)=(d−2bc/a,b^2)

in this localized coordinate ring; equality uses that a,c and 2 are units. Its quotient is the polynomial/Laurent coordinate ring in x_1,x_2,a,c, together with b subject to b^2=0. At the generic point of the reduced rank-one component this is K[b]/(b^2), so its length is exactly two.

For a consistency check, D has degree three: the degree of the Segre P^1×P^2 is the coefficient ∫(h_1+h_2)^3=3. Thus the degree cycle is 2[D]+[X]+[Y]+[Z], with degree 2·3+1+1+1=9, agreeing with the complete-intersection Hilbert series.

This proves a genuine generic nonreduced structure on the fixed-plane rank-one component. It supplies neither an entire primary decomposition nor a complete description at component intersections. The same local description holds in tautological frames over G. It must not be transported automatically to the full cubic zero scheme in V^3: over a nonzero rank-one triple the incidence map remembers an additional plane containing its line (a P^3 worth when dim V=5), whereas only the exact-rank-two locus has a unique span plane.

## Audit status

Two independent auditors confirmed Sections 1–4 and the fixed-plane refinement in Sections 5–6. The sole scope clarification was to state the filtered-bundle functor interpretation for affine complex test schemes, matching the imported theorem exactly. Universal ideal equality and arbitrary-base-change statements are unchanged. See AUDIT.md.
