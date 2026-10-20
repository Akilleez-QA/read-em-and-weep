# Preserved mathematical audit

This review concerns the source manuscript and its stated assumptions. It is preserved as mathematical history, not a new independent certification of all publication edits or of unpublished input theorems. Source and publication hashes are recorded in SOURCE-HASHES.json. A split manuscript’s module or polar application remains conditional in its destination unit.

# Independent audit: finite collision-neighborhood detection

## Verdict and premises

The finite-detection theorem and its associated-graded refinements are mathematically valid under the imported regular coefficient-transport hypotheses. The audit uses the actual ordinary ideal sheaf and its audited global regular-sequence structure, including quadruple collisions. It does not independently establish the transport hypotheses or evaluate an actual source.

Files reviewed:

- `PROOF.md` and `DOWNSTAIRS-DETECTORS.md` in this directory, including their final revisions.
- `prerequisite full-target-collision-criterion, document PROOF.md (see the unit INPUTS.md)`.
- `../fourth-ideal-pushforward/PROOF.md`.
- `../sixth-ideal-pushforward/ALL-POWERS.md`.
- The relevant coefficient decomposition and subgroup-character statements in `prerequisite weighted-trace-filtration-audit, document TRACE-CORRECTED-SQUARE.md (see the unit INPUTS.md)` and `WEIGHTED-SELECTION.md`.

The inherited injectivity of the constant inclusions is required at all three twists r=0,1,2. Injectivity of a cohomology inclusion at twist zero alone would not imply the other two. The paired-space conclusion uses the exhaustive three-coordinate decomposition of that paired space, not an assertion that it is the whole upstairs H-sign sector.

## 1. Restriction injectivity is justified by exactness

The long exact sequence for

    0 → I^12E → E → E/I^12E → 0

identifies the restriction kernel with the image of H²(I^12E). Characteristic-zero projection allows the same statement in the H-sign sector. A preimage class has a regular closed ideal-valued representative on the quotient-adapted affine Čech cover; finite pushforward preserves affine acyclicity. Applying the common-order theorem to this representative kills the constant and both retained coordinates. The class is therefore zero if it belongs to the transported paired space.

This proves precisely the zero intersection of that paired space with the image of ideal-valued cohomology. It does not prove vanishing of H²(I^12E)_χ, zero of its unrestricted image, or injectivity on all of H²(E)_χ. Nor does it prove surjectivity: the full-sector restriction cokernel is the indicated kernel in H³.

The primitive-modulo-I^12 formulation is equivalent to the theorem. It requires a character-normalized representative if its quotient primitive is required to have that character. For an arbitrary representative with only its cohomology class in the paired sector, first apply the H-character projector, or permit an unrestricted quotient primitive. Averaging preserves the represented class but need not preserve equality with the original cochain modulo I^12.

An affine quotient primitive lifts cochainwise to E. Its residual is a closed ideal-valued cochain representing the original class. The theorem supplies an unrestricted primitive of that residual through vanishing of its class; it supplies no preferred formula and does not imply that the residual primitive lies in I^12E.

## 2. Primitive-lifting obstructions and signs

For the layer extension

    0 → L_k → Q_(k+1) → Q_k → 0,

fix a primitive b_k and set r_k=c_(k+1)−δb̃_k. Its class in H²(L_k) is independent of the chosen lift b̃_k. It vanishes exactly when that specific b_k extends. With the residual convention in the proof, if δa_k=r_k, the corrected primitive is

    b_(k+1)=b̃_k+a_k.

One adds the layer primitive to the lifted primitive.

Changing b_k by a closed one-cochain changes the obstruction by minus the connecting homomorphism H¹(Q_k)→H²(L_k). The obstruction to existence of some next-stage primitive is therefore the well-defined coset in its cokernel. Requiring an arbitrary frozen representative of that coset to be zero would be too strong.

A later change can force revisions of earlier compatible choices by restriction; the argument only claims existence of a successful finite chain. A successful final primitive supplies such a chain automatically. No direct-sum splitting of the filtration or convergence of a formal infinite procedure is used.

The final additional exact sequence is valid: L_k is supported on the projective surface D, so H³(L_k)=0. Hence H²(Q_(k+1))_χ→H²(Q_k)_χ is surjective and its kernel is canonically coker ∂_k. Together with H²(Q_1)_χ=0, the eleven cokernels are genuine successive kernels of the finite-neighborhood filtration. This does not imply surjectivity from H²(E), whose ideal kernel sheaf has four-dimensional support.

## 3. Componentwise H-character calculation

The conormal description gives

    L_k=E|D⊗Sym^k(U)⊗A^(-k)|D.

The subgroup H acts transitively on the four triple-diagonal components. The stabilizer of a component in H is a transposition subgroup C2. It acts pointwise trivially on that component and trivially on the descended bundles E and A. Since χ is negative on that transposition, every χ section of L_0 restricts to zero on every component. Reducedness of D and local freeness of L_0 make restriction into the component normalization injective. Hence (q_*L_0)_χ=0 globally, including the quadruple locus.

This proves the stronger cochain assertion that every character-normalized regular source already belongs to IE. The level-zero primitive test is automatic and b_1=0 is permitted.

A reflection in the standard S3 representation U has eigenvalues +1 and −1. In Sym^k U the negative eigenspace has dimension floor((k+1)/2), counting odd powers of the negative eigenvector. After choosing a component, restriction embeds the H-sign layer into the finite pushforward of its coefficient bundle tensored with this eigenspace. This is a global upper container and gives the generic multiplicity. It does not identify the original sheaf with that container at component intersections; quadruple-locus gluing remains relevant.

## 4. Exact full-sign layers and weighted supports

Exact finite pushforward and sign projection, together with the audited equality of actual ideal subsheaves, give

    (q_*L_k)_sign=0                         for k=0,1,2,
    (q_*L_k)_sign=⊕_(2a+3b=k−3) B0(−k−2)|N  for k≥3.

The k=4 sum is empty. The formula is global: it follows from K_n/K_(n+1), rather than replacing q_*O_D by a trivial representation bundle. Tensoring by A^r gives exactly the coefficient twist written in the proof.

Multiplication by weights of orders r=0,1,2 sends source degree k to target degree k+r. Thus the only possible leading degrees are respectively 3+2a+3b, 2+2a+3b, and 1+2a+3b. The three displayed lists through degree eleven are correct. These are possible leading target layers, not proven nonzero maps, independent coordinates, or permission to discard higher extension terms.

## 5. Downstairs quotient detector diagram

The quotient coefficient map is, more precisely,

    (q_*Q_12)_χ → B0(r−5)/B0(r−5)K_(9+r).

It is well defined because the weight of order r sends I^12E into I^(12+r)EA^r and sign projection preserves those ideals. On paired classes it agrees with restriction of the corresponding global duality coordinate, using the inherited transport comparison. The vanishing of H² of each kernel coefficient makes these global coordinate restrictions injective. The additional H³ term still governs failure of surjectivity.

## 6. Common thickening and dual surface formulation

The supplementary statements in `DOWNSTAIRS-DETECTORS.md` were independently checked. Write u=t₂, v=t₃ and let T=V(K_11). The divisibility-minimal generators and adjacent syzygy degrees are

    K_11=(u^6,u^4v,u^3v^2,uv^3,v^4),
    generator degrees: 12,11,12,11,12,
    syzygy degrees: 15,14,15,14.

The audited regular-sequence flat-base-change argument implies T is Cohen–Macaulay of pure codimension two. Equivalently, its length-two locally free resolution and codimension give this conclusion locally. Dualizing that resolution into ω_Y=O_Y(−5) gives the exact sequence

    0 → O_Y(−5)
      → O_Y(7)^3 ⊕ O_Y(6)^2
      → O_Y(10)^2 ⊕ O_Y(9)^2
      → ω_T → 0.

The complete-intersection hypothesis is on the two parameters u,v, not on the five-generator thickening ideal K_11. The thickening need not be a local complete intersection for the displayed dualizing sheaf and Cohen–Macaulay duality to apply.

The prior ideal-cohomology bounds make both restriction maps

    H²(Y,B0(−4)) → H²(T,B0(−4)|T),
    H²(Y,B0(−3)) → H²(T,B0(−3)|T)

injective. Surface Cohen–Macaulay Serre duality, ordinary Serre duality on Y=P⁴, and B0 self-duality turn their transposes into the surjections

    H⁰(T,B0(4)|T⊗ω_T) → H²(Y,B0(−1)),
    H⁰(T,B0(3)|T⊗ω_T) → H²(Y,B0(−2)).

All signs, twists, and directions of these maps check. These are existence/surjectivity results, not an evaluated pairing or a computed source rank. The same common thickening also detects the constant coordinate by the corresponding r=0 bound; its dual map is H⁰(T,B0(5)|T⊗ω_T)→H²(Y,B0).

The transverse length and degree assertions are also correct. For K_11 the monomials of weight below eleven number 6+4+3+1=14, so degree(T)=14·6=84. For K_10 the number is 5+4+2+1=12 and the degree is 72. These count scheme multiplicities along the surface, not finitely many sample points. The K_10 generator list is divisibility-minimal as stated.

The supplement correctly distinguishes common global-coordinate restriction to T from the natural chain maps out of Q_12. For r<2, the latter only yield coefficient order K_(9+r), which does not imply the stronger K_11 order. Thus there is no asserted direct common-T chain map out of Q_12. The stated compatibility after further restriction is the correct one.

## Audit corrections and scope

The draft review requested three textual clarifications: require a χ-normalized c in the χ-primitive equivalence; add, rather than subtract, the layer primitive under the displayed residual convention; and make q_* and restriction of coordinates explicit in the downstairs quotient diagram. All three are incorporated in the final reviewed proof. Its explicit e_H normalization note also handles initially unprojected representatives. No mathematical defect remains in the reviewed statements, subject to their stated inherited hypotheses.

The audit performs only sheaf algebra, representation algebra, and exact-sequence reasoning. It makes no source evaluation, selected polynomial-instance calculation, matrix-rank computation, physical-jet computation, or external write.
