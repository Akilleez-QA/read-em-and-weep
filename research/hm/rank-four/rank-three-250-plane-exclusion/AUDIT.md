# Independent audit: residual rank at least four on the 250-point orbit

## Verdict

**PASS, conditional on the stated representation, orbit, repeated-input-injectivity, and rank-conversion inputs.** The argument in `PROOF.md` proves that the even block has rank at least five and the odd block has rank at least three on the ten-point plane orbit. Consequently it proves `rank b >= 8`, hence `rank Q >= 4`, on the full 250-point normalizer orbit. I found no gap in the new exclusion argument.

This is genuinely stronger than the preceding plane proof's bound `rank Q >= 3`. It neither classifies other isolated rank-three points nor proves their absence. No actual source-instance evaluation is claimed.

I read the present proof, `../rank-two-250-plane-exclusion/PROOF.md`, and `../canonical-line-parity-exclusion/PROOF.md`. The review below independently checks the new deductions and the immediately reused algebra and bundle arguments. It does not reestablish the upstream identification of the Schrödinger normalizer's 250-point orbit or its stabilizer.

## 1. Target multiplicities: valid

Let `L: T ⊕ P5 -> J+` be the equivariant map induced by the pure-T universal tensor. Its restriction to P5 is injective by the preceding proof's repeated-input argument; write `H=L(P5)` for that particular five-dimensional submodule.

A nonzero restriction of L to T is injective. Its image has zero intersection with H because T and P5 are inequivalent irreducibles. This statement concerns the two actual images, and does not assume that either irreducible has multiplicity one in the ambient target.

After the T restriction is excluded, the pure-T image at each nonzero u is a four-dimensional subspace of H. If total even rank is four at the orbit points, all mixed values at those points belong to this subspace. Passing to the genuine quotient `J+/H` is legitimate regardless of ambient multiplicities. For every fixed s in T', the resulting map from T is linear and vanishes at representatives spanning T. It is therefore zero everywhere. Thus the mixed map has image in this specific H, rather than merely in the P5-isotypic component. This is sufficient to apply the multiplicity-one statement in `T'⊗T=P4⊕P5`.

## 2. The metric excludes the pure T constituent: valid

Under the invariant metric identification, the universal metric-source value is

    2 sum_i e_i ⊗ C_u(e_i),  where C_u(x)=u×x.

As an endomorphism it is `2 C_u^transpose = -2 C_u`, up to the harmless choice of tensor-to-matrix convention. It is skew-symmetric and nonzero for every nonzero u. Its P5 projection is zero, and it belongs to the T constituent.

The pure-T source map already projects onto a four-dimensional subspace of H. If L(T) survives, the metric value is a nonzero additional image vector with zero H projection. Rank-nullity for the projection of the pure-source image to H then gives pure-source rank at least five. This avoids any unjustified assumption that the other four image vectors lie in H before the T constituent has been killed.

Accordingly, even rank four at just one orbit point forces the whole equivariant T restriction of L to vanish. The universal rank-four P5 assertion used here is valid also for isotropic u: the nilpotent action on `Sym^4(C^2)` has a one-dimensional kernel. Thus no exceptional nonzero u invalidates this step.

## 3. Nonvanishing of the mixed map: valid

If `g: Sym²W ⊗ T -> H` were zero, then `f(w,t,w)=0` for all w,t. Outer symmetry and cyclic zero give

    2 f(w,w,t) + f(w,t,w) = 0.

For nonzero w in W and nonzero t in T this contradicts repeated-input injectivity, since the direct sum decomposition ensures `t` is not a scalar multiple of `w`. Therefore g is nonzero. The decomposition `T'⊗T=P4⊕P5` then shows that the map to H is the unique P5 projection up to a nonzero scalar.

## 4. Cubic annihilator and tensor identification: valid

The endomorphism

    K(u)=u⊗u-(q(u)/3)Id

is symmetric and traceless. Both `C_u(u)=0` and the skew-symmetry of C_u imply `[C_u,K(u)]=0`. Cyclicity of trace gives

    tr([C_u,S] K(u)) = tr(S [K(u),C_u]) = 0.

Consequently every value in the pure-T image is orthogonal to K(u), including at isotropic u. Since g is linear in u and K is quadratic, `F_s(u)=tr(g(s,u)K(u))` is a homogeneous cubic. The mixed-image containment forces each such cubic to vanish on the ten-point orbit, and the no-cubic lemma makes it identically zero.

The trace-free condition removes the scalar term of K exactly:

    F_s(u)=tr(g(s,u)(u⊗u)).

Using the invariant nondegenerate pairings, currying g produces a nonzero equivariant map `a:T' -> P5⊗T`. Its domain is irreducible, so it is injective. Identifying a symmetric traceless endomorphism A with the quadratic polynomial `u -> q(u,Au)`, contraction in the displayed formula is precisely multiplication of the corresponding quadratic and linear factors. Hence the map `s -> F_s` is `m∘a`; there is no missing dual representation or different contraction here. Alternative polarization conventions would only introduce a common nonzero scalar.

## 5. Multiplication kernel and representation types: valid

The map `m:P5⊗T -> Sym³T` is equivariant and surjective. The proof's monomial argument checks all monomials: any cubic involving at least two variables is a multiple of an off-diagonal traceless quadratic, and

    xi³ = (xi²-xj²)xi + (xi xj)xj,  j≠i,

handles pure cubes. Both quadratics on the right lie in P5. This establishes surjectivity directly without assuming a decomposition of the kernel.

On the A5 classes of sizes `(1,15,20,12,12)`, the product character of P5⊗T is `(15,-1,0,0,0)`. The symmetric-cube character is `(10,-2,1,0,0)`, obtained from the symmetric-cube character formula. The proposed decompositions agree term by term with the recorded character table:

    P5⊗T = T ⊕ T' ⊕ P4 ⊕ P5,
    Sym³T = T ⊕ T' ⊕ P4.

Thus the kernel character is `(5,1,-1,0,0)`, exactly the irreducible P5 character. Complete reducibility over C gives `ker m ≅ P5`.

In particular `a(T')` cannot lie in `ker m`: a nonzero map between the inequivalent irreducibles T' and P5 is impossible. This proves `m∘a ≠ 0`, contradicting the cubic vanishing. The distinction between the two inequivalent three-dimensional representations is retained correctly throughout.

## 6. Odd rank at least three: valid independently of a total-rank upper bound

Repeated-input injectivity makes `w -> f(u,u,w)` injective on W for every nonzero u in T, giving odd rank at least two everywhere on P(T).

If odd rank were at most two at one orbit point, equivariance would impose this bound on all ten points. All three-minors of the linear odd block are cubics, so the no-cubic lemma makes them identically zero. The odd block would then have constant rank exactly two on P(T). Its image is a rank-two vector bundle I and a quotient of `O(-1)^6`.

The repeated-input map `O(-2)⊗W -> I` is a morphism of vector bundles and is an isomorphism on every fiber, hence an isomorphism of bundles. Therefore `I≅O(-2)^2`. But every morphism from `O(-1)` to `O(-2)` on P² is zero, since `H^0(O(-1))=0`. This contradicts the defining quotient map. No assumption on total rank is used in this argument.

## 7. Reused no-cubic input and final scope

The preceding plane proof's immediate no-cubic argument also checks out, given ten distinct spanning orbit points off the invariant conic. A nonconstant common divisor of an invariant linear system of cubics is a semi-invariant, hence invariant because A5 is perfect. The invariant-form dimensions in degrees one, two, three are respectively zero, one, zero, leaving only the invariant quadratic as a possible common divisor. Since it does not vanish on the orbit, this would force linear forms vanishing on a spanning orbit. With constant gcd, two cubics without common component would meet in at most nine points, contradicting the ten distinct orbit points.

Finally, the universal even lower bound is four. Excluding equality raises it to at least five. Complementary target parity spaces make block ranks add, and normalizer equivariance transports the result from the ten-point plane orbit to the full 250-point orbit. The conversion `rank b=4+rank Q` is an explicit upstream dependency. Subject to that dependency, the claimed disjointness from Z3 follows.

**Required repairs:** none. A useful optional clarification would be to state the projection/rank-nullity explanation in Section 2 explicitly, so readers do not mistake the four P5-projected directions for four already-pure H directions before the T constituent has been eliminated.

## 8. Independent audit of ADDENDUM.md

**PASS, with the additional explicit dependency on the Heisenberg-eigenpoint lower bound.** I read `ADDENDUM.md` and `../heisenberg-eigenpoint-rank-parity/PROOF.md`. The extension proves `rank Q >= 4` throughout every canonical positive reflection plane, under the same hypotheses and the additional eigenpoint input. No repair is required.

### Small off-conic orbits

For an A5 orbit of size at most nine, the line stabilizer has order greater than six. The elementary subgroup list leaves A4, D5, or A5. Irreducibility excludes A5. In the restriction to A4, the multiplicity of every one-dimensional character is zero: its value is one on the normal four-group, T has character 3 at the identity and -1 at each of the three involutions, and T has character zero on all eight order-three elements. Thus A4 stabilizes no line, including lines with nontrivial character.

For D5, an order-five generator has three distinct eigenlines. A normalizing involution exchanges the two nontrivial eigenlines, so only its eigenvalue-one axis is stable under D5. The six Sylow-five normalizers supply a single orbit of six axes. Different normalizers cannot yield the same axis, because a line stabilizer containing two of them would be larger than D5 and is excluded by the same subgroup analysis. Therefore this is precisely the only orbit of size at most nine.

The standard D matrix has eigenvalues `1,ζ,ζ^4` on the positive three-space, with unique eigenvalue-one line `Ce0`. Its determinant on W is one, so this assertion is compatible with the normalized action used in the main proof. Thus these axes are translates of a canonical Heisenberg eigenpoint. The cited eigenpoint theorem supplies the required lower bound four. Its relevant proof additionally checks out: disjoint B-character supports force the correction from a residual kernel vector into the repeated-input image to vanish; repeated-input injectivity then prevents the square-character module from lying in the residual kernel, forcing a quotient of dimension at least four.

### All other orbits off the conic

Such an orbit has more than nine points and spans T. The gcd/Bezout proof of the no-cubic lemma requires exactly these facts and that q is nonzero at the orbit points; it does not require the orbit to have exactly ten points. Therefore both the odd-block contradiction and the even-block mixed-cubic contradiction apply without change. The resulting rank bound is valid on every nonexceptional off-conic orbit.

### Orbits on the conic

The conic action is faithful. Indeed, its kernel acts projectively as scalars on the spanning plane; the nontrivial irreducible A5 representation is faithful, and A5 has trivial center, so no nonidentity element can act this way. A finite stabilizer of a point of P1 is cyclic. The possible cyclic subgroup orders in A5 are 1,2,3,5, so a conic orbit has at least twelve distinct points.

A cubic restricted from the plane has degree six on the conic. Hence vanishing on such an orbit forces the restriction to be zero. For the odd block, vanishing of all three-minors on the conic gives constant rank two there; the repeated-input image is `O_P1(-4)^2`, whereas the linear block makes it a quotient of `O_P1(-2)^6`. The Hom vanishing is correct and yields the asserted contradiction.

For the even block, the metric and rank-four commutator arguments remain valid at isotropic points. The orbit spans T, so quotienting by H again forces the full mixed coefficient image into H. The main proof shows that the cubic coefficient map from T' is nonzero, hence has irreducible image isomorphic to T'. Vanishing of all its restrictions to the conic places that image in the degree-three part of the conic ideal, exactly `q·T`, isomorphic to T. These two irreducibles are inequivalent, so this containment is impossible. This is the correct substitute for asserting, incorrectly, that no plane cubic could vanish on a conic orbit.

### Conclusion and scope

The six-axis orbit, the other off-conic orbits, and the conic cover the plane. The addendum therefore establishes the bound on all positive reflection planes. Together with the negative-reflection-line theorem, it excludes every projective fixed point of a canonical reflection from Z3. It does not alone exclude other points of Z3 or determine their stabilizers. The addendum's phrase “pending independent audit” may now be updated to reference this section.

## 9. Audit of the added finite-support consequences (ADDENDUM.md, Section 5)

**PASS, conditional on the additionally stated finiteness and Heisenberg-action inputs.** The necessary orbit sizes are 600, 1000, and 3000, and the reduced support cardinality is at most 4000. These restrictions do not prove that a nonempty support exists.

Outside the canonical thirty eigenpoints, freeness of A implies that a point stabilizer S intersects A trivially, so projection embeds S into `K=SL2(F5)`. Every involution of `N=A⋊K` projects to the unique involution of K: a nontrivial element of A cannot have order two. The projected involution acts by -1 on A, and conjugation by an element b of A changes the translation part by `2b`. Because multiplication by two is invertible on A, all involutions are A-conjugate to the canonical reflection. The audited positive-plane and negative-line exclusions thus imply that a Z3 stabilizer has no involution, and Cauchy's theorem gives odd order.

An odd-order subgroup of K has order 1, 3, 5, or 15, and embeds in A5 after quotienting by the central involution. A group of order 15 in A5 would have a unique Sylow-five subgroup, hence lie in its order-ten normalizer, a contradiction. Therefore `|S|` is 1, 3, or 5. Dividing 3000 by these numbers yields exactly the listed possible orbit sizes. No unjustified conjugacy claim for order-five lifts is needed.

The degree bound is also valid. The rank relation identifies Z3 set-theoretically with the rank-at-most-seven locus of the linear matrix b, whose defining eight-minors are homogeneous of degree eight. If their projective base locus is finite, four suitably general linear combinations form a zero-dimensional complete intersection in P4 containing it. At each stage one avoids the finitely many positive-dimensional irreducible components of the preceding intersection; none can be contained in the finite base locus. The resulting complete intersection has length `8^4=4096`, which bounds the number of distinct points of Z3. Every allowed orbit size is divisible by 200, so that cardinality is a multiple of 200 and at most 4000.

This argument bounds reduced support cardinality; it should not be read as an independently established exact length or reducedness statement for the original determinantal scheme.
