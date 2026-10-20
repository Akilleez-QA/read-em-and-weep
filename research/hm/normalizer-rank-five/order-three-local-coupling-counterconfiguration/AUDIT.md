# Independent audit of the local counterconfiguration

## Verdict

**Verified, within its stated local scope.** The Dic_3 action, restricted representation types, extensions of both coefficient maps, reconstruction identities, cancellation, surjective extension, and optional binary-image injectivity are consistent. No coefficient of the actual geometric operation and no selected rank instance was evaluated in this audit.

Checked against `PROOF.md` in this directory and `../order-three-parity-pencil-rigidity/NEXT-STEP.md`, `PROOF.md`, and `TARGET-STRENGTHENING.md`.

## 1. Group and restricted types

Work over C. The presentation has normal forms a^r j^s, with 0<=r<3 and 0<=s<4. Its displayed action on W_v gives twelve distinct matrices, so the presented group has order twelve and is Dic_3. The displayed actions on both inputs satisfy j a j^{-1}=a^{-1}, with j^2=+1 on T and -1 on W_v. Also det T=det W_v=1.

Let chi_+ and chi_- be the one-dimensional odd representations with a=1 and j=+i,-i. Let Q be the displayed two-dimensional representation W_v. **Q is the unique odd two-dimensional irreducible with nontrivial a-action.** Indeed j exchanges the omega- and omega^2-eigenspaces of a. For any nonzero vector v of weight one, span(v,jv) is stable, with j(jv)=-v. An irreducible containing v must equal this plane. The two odd one-dimensional characters still exist; the uniqueness claim does not exclude them.

The actual restricted types are

    W_v|D = Q,
    S_4|D = chi_+ + chi_- + Q,
    R_6|D = chi_+ + chi_- + 2Q.

The S_4 formula follows directly from Sym^3 W_v: its weight-zero plane is spanned by w_1^3,w_2^3, on which j has eigenvalues +i,-i. The R_6 formula follows from T tensor W_v; its two-dimensional weight-zero plane likewise has eigenvalues +i,-i.

Consequently

    E|D = 2chi_+ + 2chi_- + 4Q,
    F|D = chi_+ + chi_- + 2Q.

The two selected planes span(e_1,e_4) and span(e_2,e_3) each have type chi_+ + chi_-. Assigning the four remaining Q copies in proportions 1,1,2 therefore gives exactly the claimed W_loc,S_loc,R_loc restricted types. This checks the extension of the weight-zero splitting, rather than merely its dimensions.

## 2. Source multiplicities and coefficient maps

The odd Schur source decomposes by multidegree as

    (S_(2,1)(T+W_v))_- = S_(2,1)W_v + E + F.

Since S_(2,1)W_v=W_v tensor det W_v=W_v, the binary-icosahedral identities in the input note give 2W_v+S_4+2R_6, of total dimension twenty. Its restriction is 3chi_+ + 3chi_- + 7Q, consistently with the displayed local modules. These multiplicities do not fix embeddings or relative intertwiners.

For k, the basis actions are jz_1=z_2 and jz_2=-z_1. Directly,

    j(e_3+2e_2)=e_2-2e_3,
    j(e_2-2e_3)=-(e_3+2e_2).

Thus its prescribed weight-zero map is D-equivariant. Its matrix in the ordered target basis (e_2,e_3) is [[2,1],[1,-2]], with determinant -5. The complementary source and target sectors are each 2Q, so a D-isomorphism on them exists independently. There is no missing extension condition. The identity g has nonzero scalars on every selected local summand.

## 3. Reconstruction and strengthening checks

For arbitrary symmetric g and alternating k, outer reversal and the three cyclic values

    -g/2+k/2,  g,  -g/2-k/2

give a well-defined trilinear operation with the required identities. They recover the definitions of g and k. Distinct multidegree summands of the Schur module can be assigned independently.

The pure-T extension is valid:

    S_(2,1)T = (T tensor Lambda^2 T)/Lambda^3 T
             = (T tensor T)/1 = T + P_5 = J_+.

These are representation isomorphisms, using the invariant metric and det T=1. Together with g onto J_-, it gives surjectivity onto the full twenty-dimensional restricted target.

For the optional binary-image extension, w_1^2 tensor t_1 and w_2^2 tensor t_2 have weight zero and are interchanged by j. The assignment p,jp is therefore equivariant for every p in (J_+)_0. A D-stable complement exists by characteristic-zero semisimplicity. The two generators of S_(2,1)U map to h=-e_1/2 and -p/2; these are nonzero in opposite c-parities. Hence this binary map is injective, its image has dimension two, and its odd image is exactly C h. Surjectivity and the odd coefficients are unchanged.

## 4. Cancellation and boundary

The constructed formal coefficients are h=-e_1/2 and C_tilde=D_tilde=e_2. Therefore h is nonzero, their common quotient class modulo C h is nonzero, and the required exterior product vanishes.

The illustrative parity block with alpha=beta=1 has determinant proportional to s^2-t^2. Its rank is two generically and at the endpoints, and one at t=+s,-s. As now explicitly stated in the proof, these positive coefficients are not claimed to be those induced by the constructed cubic extension.

The conclusion is only that the listed **local** representation data, nonvanishing coefficient maps, target surjectivity, and even the optional fixed-line binary injectivity do not force the exterior product to be nonzero. The construction does not test the actual full-complement embeddings, full-N coupling, kernel constraints, or global repeated-input injectivity. It neither disproves the original geometric claim nor excludes or produces any rank-three support. The unresolved reduction in NEXT-STEP.md remains unresolved.
