# Historical mathematical audit receipt

This is a preserved review of the source mathematical manuscript, not a fresh review of the publication bytes. Hashes quoted below identify the historical source versions. See [hm-apolar-reconstruction-PUBLICATION-CHECK.md](../hm-apolar-reconstruction-PUBLICATION-CHECK.md) for the final-publication review.

# Independent audit: minimal relations of the HM middle module

## Verdict

The revised PROOF.md is correct, conditional on its explicitly imported and separately audited generation, cohomology representations, and perfect degree-five duality. In particular:

- The quadratic relation space is exactly R₂=V₃⊗W′, of dimension ten.
- The degree-three relation multiplication has three initial irreducible blocks, of dimensions 5, 15, and 30.
- Its five- and thirty-dimensional blocks are necessarily nonzero by the independent structural arguments given below.
- Its kernel and cokernel are therefore each either zero or V₁⊗χ₃′. Their common dimension is 0 or 15.
- The displayed self-dual Betti shape is necessary. If the cubic obstruction vanishes, the parameters c and d vanish as well. Possible quartic relations and middle ghost terms are not excluded.

This audit does not settle the remaining fifteen-dimensional block or claim quadratic generation.

## 1. Inputs and primary representations

I read ../quintic-scalar-propagation/PROOF.md and AUDIT.md, ../quintic-pairing-representation/PROOF.md, and the final revised PROOF.md in this directory. I also opened the original Horrocks–Mumford paper and checked its relevant representation statements and appendix:

https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf

Lemma 2.4(ii), printed pp.68–69, directly identifies X⊗V₃ as V₁⊗(χ₃⊕W′). Thus no separate restriction formula for V on a chosen SL₂(F₅) complement is needed. Dualizing Lemma 3.3(v),(vi) gives precisely the stated Sym²X and Sym³X identities, since V₁*=V₃ and all relevant quotient characters are self-dual.

The four small quotient tensor identities in Section 1 check against the appendix. One can verify them using η+η′=−1 and ηη′=−1. In particular χ₃⊗W′ has values (6,−6,0,0,0,1,1,−1,−1), the χ₆ row. The product χ₅⊗W′ has values (10,−10,0,1,−1,0,0,0,0), the sum of Q and χ₆. The identity χ₃′⊗W′=W′⊕Q uses the spinorial Q, not the other four-dimensional representation.

The Heisenberg-isotypic evaluation equivalence ensures that the factors V₁⊗T and V₃⊗T are irreducible exactly when T is, and that distinct quotient irreducibles give distinct N-modules. This justifies the multiplicity-one and Schur-lemma arguments.

## 2. Relation spaces and the meaning of the cubic map

Generation makes both degree-two and degree-three polynomial maps onto the stated actual cohomology modules. Their semisimple kernels are consequently exactly the complements of V₃⊗Q and V₁⊗Q in the displayed source decompositions. This proves the specified R₂ and R₃ without identifying any multiplication coefficients.

The polynomial map m:X⊗R₂→R₃ has isomorphic source and target, each the multiplicity-free sum V₁⊗(1⊕χ₃′⊕χ₆). Every block is therefore either zero or an isomorphism. Its kernel and cokernel are isomorphic representations, although there is no preferred isomorphism between them from this argument.

There are no relations in degree one. Thus the kernel in degree three is precisely the minimal degree-three second syzygy space. The cokernel R₃/XR₂ is precisely the space of minimal cubic relations. Higher-degree generators do not alter either identification. This verifies the two asserted Tor interpretations.

## 3. Universal shadow bound

The monomial reduction is valid for subspaces of a free polynomial module: choose a multiplicative module term order, take a row-echelon basis in the fixed degree, and record its distinct leading monomials. Multiplication by any variable preserves the leading-term rule, so the monomial shadow is contained in the leading-monomial space of XT. Its dimension can only give a lower bound for dim XT; no equality is presumed.

The probability argument has the correct normalization. The probabilities (a_i+1)/(n+d) sum to one for every degree-d exponent vector a. A fixed degree-(d+1) vector b is reached with total probability

    (Σ_i b_i)/(N_d(n+d)) = (d+1)/(N_d(n+d)) = 1/N_(d+1).

Hence the output really is uniform. Membership of a in a selected set implies membership of b in its shadow. Applying this separately to the monomial sets in each free-module component and adding proves the exact normalized inequality used in the proof.

For n=5, d=2, and dim R₂=10, this gives dim XR₂≥24. Thus the fifty-dimensional source has kernel of dimension at most 26. Its thirty-dimensional irreducible block cannot lie in that kernel, proving its scalar is nonzero. This is a universal growth argument, not a selected rank evaluation.

## 4. Independent exclusion of the five-dimensional kernel

Ordinary polynomial multiplication X⊗Sym²X⊗U→Sym³X⊗U is surjective. Choose any N-equivariant splitting of the quadratic quotient; semisimplicity permits it. The second source summand X⊗L₂ is V₁⊗((χ₃⊕W′)⊗Q).

The trivial quotient representation occurs in neither χ₃⊗Q nor W′⊗Q: by self-duality this would require an isomorphism between irreducibles of different dimensions. Therefore X⊗L₂ contains no V₁. The full target has exactly one V₁. Surjectivity forces that target to be reached from the unique V₁ in X⊗R₂. The corresponding scalar is nonzero, independently of which equivariant splitting was chosen.

The target V₁ lies in R₃, since the quotient L₃ is the inequivalent irreducible V₁⊗Q. Consequently this is indeed nonvanishing of the V₁ block of m, not merely of an unrelated polynomial map. Together with Section 3 it leaves only V₁⊗χ₃′ as a possible kernel and cokernel. The cubic image dimensions are exactly restricted to 35 or 50.

## 5. Betti duality, numerator, and minimality consequences

The perfect degree-five pairing is S-linear after graded dualization, so D(L)≅L(5). Graded local duality in five variables gives Ext⁵(L,S(−5))≅D(L), or Ext⁵(L,S)≅L(10). Dualizing the minimal free resolution therefore yields β_(i,j)=β_(5−i,10−j). The determinant character is trivial under the stated N⊂SL₅ convention.

The two degree-zero generators and two degree-five socle elements give the two endpoint terms. Starting with quadratic first relations, minimality gives j≥i+1 for the four interior homological degrees; duality gives j≤i+4. Direct expansion of the Hilbert polynomial times (1−t)⁵ gives

    2−10t²+20t⁴−20t⁶+10t⁸−2t¹⁰.

Within those degree bounds and duality, coefficient comparison gives exactly the displayed five-parameter shape. The cubic calculation restricts a to 0 or 15. Nontrivial central character forces b and d to be multiples of five, as stated. The proof correctly refrains from presenting these necessary conditions as a realization theorem or exhaustive representation classification.

If a=0, a degree-four minimal generator of F₃ has no lower-degree target in F₂, so its differential is zero. Exactness would put that generator in the image of F₄, which is contained in the homogeneous maximal ideal times F₃ by minimality; this is impossible. Therefore d=0. The same argument for degree-five minimal generators of F₄ then gives c=0. It does not eliminate b or e. In particular the Hilbert numerator alone cannot justify deleting equal-degree middle ghost terms.

## Scope

Only static proof reading, primary-source representation reading, finite character identities, a universal monomial-growth argument, and formal homological algebra were used. No actual HM, cofactor, source, multiplication, or obstruction matrix was selected or evaluated. No polynomial instance, point, jet, or matrix-rank test was performed. The remaining cubic scalar and higher minimal relations stay explicitly unresolved.

## Reviewed proof fingerprint

SHA256 of the exact reviewed PROOF.md: f5d36dcffdf7c03875855a93ef93a6b855943aa5135237a76cda788cb4ebb3cd
