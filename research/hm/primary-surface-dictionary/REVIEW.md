# Independent mathematical review: primary degree-fifteen dictionary

Reviewed proof SHA256: a8047299b273c7319310b70f51bbee14823b861bce005b3f8e7493e75c7b2d55.

Verdict: PASS, conditional only on the explicitly pinned established inputs PR562, PR566 and PR567. This is independent mathematical review, not formal proof checking. No selected HM/source instance was evaluated; the checks below are universal identities and source comparisons.

## 1. Traceless action and cyclic kernels

For D=[[a,b],[c,-a]] acting on W and k=p epsilon1+q epsilon2, the dual action has coefficients (a p+c q,b p-a q). Applying phi* therefore spans F1(q), F2(p), F1(p)-F2(q). With PR562's F1=f+ and F2=-f-, the three annihilator contractions are exactly those in equation (1). This argument does not require p,q independent and consequently does not discard rank-one tensors.

The plus contraction coefficient at e_a* is u_(a-3)x_(a-1)-u_(a-2)x_(a+1). Its recurrence is u_(i+1)/u_i=x_(i+2)/x_(i+4), satisfied by r_i=x_i x_(i+1)x_(i+4). The minus coefficient is u_(a-4)x_(a-3)-u_(a-1)x_(a+3), giving step-three recurrence, satisfied by s_i=x_i x_(i+2)x_(i+3). On the coordinate torus all recurrence coefficients are units. Each cyclic recurrence has one free variable and no further consistency condition. Hence Q=a r and P=b s are the entire kernels, not just constructed kernel vectors.

Pullback by Delta_x multiplies e_j* wedge e_k* by x_j x_k. Therefore f+(s)=Delta_x* f+(x), f-(r)=Delta_x* f-(x) hold term by term. The natural contraction identity i_x Delta_x* omega=Delta_x* i_(Delta_x x) omega gives the required x-squared contraction, without an inverse or transpose error. The remaining equation is b v+ +a v-=0 after removing the common invertible diagonal factor and common minus sign. Thus existence of nonzero k is equivalent to the wedge-zero equation, including points where both cubics vanish.

The spaces are correctly distinguished: the BHM bivector coordinate space is identified with the covector space only for copying polynomial formulas. No equivariant A=V* identification is being asserted.

## 2. Source verification

Checked the primary BHM chapter in the TIFR volume, not a secondary numerical characterization:

- Printed page37, Section2.2: f+ and f- use offsets (2,3) and (1,4), h0 has square coordinates, and v± are the negative contractions displayed in the proof.
- Printed page41, Proposition2: v+ wedge v-=0 is equivalent to h+ wedge h0 wedge h-=0 and to existence of a decomposable pencil member.
- Printed pages63–64, Proposition9 and its proof: the image under |I+2F| is the irreducible S15, has degree (I+2F)^2=15, and is injective except for the stated pairs among60 singular-fiber vertices. Properness plus finite point fibers makes the map finite; it is birational. Since S(5) is smooth, this identifies it as the normalization.
- Printed page64, Proposition10 and its preceding paragraph: S15 is smooth except for30 points with two smooth transverse branches. Here the source's word 'immersion' concerns maximal differential rank; the reviewed proof does not require interpreting the noninjective normalization map as a scheme immersion.
- Printed page65, Proposition11: the ten wedge coefficients schematically define S15.

Source: https://mathweb.tifr.res.in/Documents/Publications/Studies/Vector-Bundles-On-Algebraic-Varieties.pdf

## 3. Closure, scheme precision and degree

PR567 supplies an integral invariant surface S. Its nonzero linear span is an invariant subspace of the irreducible Schrödinger representation, hence the whole ambient space. Irreducibility then ensures its coordinate-torus intersection is nonempty and dense. The established torus inclusion S intersect U subset T closes to S subset T. Both are integral surfaces, so equality follows, including equality as integral reduced closed subschemes. Therefore degree S=15.

The optional torus scheme equality is also valid: each rank-four cyclic system has four unit pivots, yielding an I8 block. The remaining five-by-two block is the indicated diagonal multiple of (v+,v-). In the original15-by10 presentation there are additionally two zero rows, one from each cyclic contraction system. Elementary operations over the Laurent ring preserve the maximal-minor ideal, which becomes the two-by-two-minor ideal of that residual block. This is not a boundary scheme assertion.

## 4. Torsion-section corollary

PR566 makes S smooth along each distinguished L with normal bundle O(-5). Normalization is an isomorphism over this smooth locus, so its strict transform has self-intersection -5 and adjunction gives K.L=3. BHM page58 has K=3F, and Proposition9 has H=I+2F; consequently F.L=1 and I.L=-1. BHM Lemma9, page59, states 5I equals the sum of the25 torsion sections in Pic(S(5)). If L differed from every one of them, nonnegative intersections of distinct irreducible curves on the smooth normalization would contradict 5I.L=-5. Distinctness and the cardinality25 identify the entire configuration. Hence C=5I and 5H-C=10F as divisor classes on the normalization.

No section-descent, ambient restriction surjectivity, global equality D=S, or original generic-section conclusion follows merely from these arguments. The proof correctly preserves these limitations.
