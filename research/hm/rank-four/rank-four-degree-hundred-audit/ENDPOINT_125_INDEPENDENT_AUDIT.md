# Independent audit of the degree125 endpoint exclusion

## Verdict: PASS

I independently checked ENDPOINT_125_EXCLUSION.md against the earlier rank-four component-degree theorem, the full-span disconnected-normalization divisibility lemma, and the representation conventions in ../rank-four-degree-three-four-exclusion/PROOF.md. The endpoint exclusion is valid under these stated dependencies. The resulting necessary condition is

    Γ4 is empty, or its reduced total degree equals100.

No additional assumption of embedded smoothness, linear normality, or irreducibility of the whole rank-four curve is needed.

## 1. Exhaustion of the endpoint configurations

All component degrees are at least5. A component orbit of size five under A has six distinct conjugate stabilizer axes and therefore at least30 components in its full N-orbit, costing at least150 degrees. A free A-orbit of size25 costs at least125. At total125, equality forces exactly25 quintic components and no other components. The full N-orbit cannot exceed this set; it already contains the whole free A-orbit, so its size is exactly25. Thus the component stabilizer K has order120, intersects A trivially, and surjects isomorphically onto G.

If there is no non-A-stable component, every component spans P4 and the previously audited total-degree divisibility lemma contradicts50|125. These cases exhaust the three possible A-orbit sizes1,5,25.

## 2. Complement conjugacy and span cases

Write K as the graph of c:G→A. The cocycle equations for zh=hz, with z=−I acting as−1 on A, give2c(h)=(1−h)c(z). Since2 is invertible in F5, setting a=c(z)/2 yields c(h)=a−ha. Conjugation by (−a,1) takes this graph to the standard complement. Thus it is legitimate to apply the honest G-representation V=T⊕W to the translated curve.

The inequivalent irreducible summands have dimensions3 and2. Multiplicity-freeness and semisimplicity exclude any further subrepresentation spans. A positive-degree integral curve cannot have zero-dimensional span. Span W gives a curve in a projective line; an integral closed one-dimensional subscheme with reduced support there is the line itself, of degree1, not5. Hence only T and V remain.

## 3. Full-span quintic check

For degree5 in P4, the Castelnuovo division is5−1=3·1+1, giving π(5,4)=1. This bounds the smooth normalization genus, including singular embedded curves. The G-action on normalization is faithful because the curve spans P4: a projective transformation fixing the curve pointwise has it contained in one eigenspace and is therefore scalar.

In genus0, the image of the nontrivial central involution forces the entire G-image into its centralizer in PGL2. That centralizer is G_m⋊C2, a solvable group. Since G is perfect and nontrivial, a faithful embedding is impossible. In genus1, the automorphism group modulo translations is cyclic; perfect G maps trivially to this quotient and hence into the abelian translations, again trivially. Both arguments are valid for the entire G, not merely its quotient A5.

## 4. Plane quintic character check

An integral plane quintic has a principal degree-five homogeneous equation. Its equation line is invariant under G, and perfection makes its character trivial. Thus the needed representation-theoretic obstruction is exactly the vanishing of (Sym5 T*)^G, not a stronger claim about all semi-invariants of a nonperfect group.

I checked all five character values independently:

- At identity: binom(7,2)=21.
- At order2: coefficient t5 of ((1−t)(1+t)^2)^−1 is1−2+3−4+5−6=−3.
- At order3: the eigenvalues1,ω,ω² give (1−t³)^−1, whose t5 coefficient is0.
- At either order5 class: the eigenvalues1,ζ^a,ζ^−a leave the complementary roots ζ^(2a),ζ^(−2a). The generating function is (1−ζ^(2a)t)(1−ζ^(−2a)t)/(1−t5), whose t5 coefficient is1.

Thus the character is (21,−3,0,1,1). Its A5 average is

    (21−45+12+12)/60=0.

The conclusion holds for either three-dimensional icosahedral representation and its dual. Therefore there is no invariant plane quintic, and the final span case is excluded.

## 5. Scope

The endpoint result and the earlier alternatives {100,125} combine to give exactly100 for a nonempty reduced rank-four curve. This does not establish existence, classify a degree100 configuration, or settle isolated points or scheme multiplicities. The audit used no actual source tensor, selected point, operation value, coefficient, matrix, rank instance, jet, or residue, and changed no external state.
