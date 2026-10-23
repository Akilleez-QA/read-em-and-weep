# The nine-branch graph is nonzero; its truncation is artificial

**Craig Ward · 23 October 2026 · PR1066**

[Immutable full proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/638efef0469b7230f04560d0a02f3cf4d4116c0c/research/hm/source2-pure-v-small-relations/PROOF.md).

## Later actual-negative promotion through PR1073

[PR1073](103-actual-terminal-negative-module.md) uses the later actual joint-negative kernel theorem to prove that R·im h itself terminates in degree four in endpoint nine. Thus the resolution below, shifted by two, now describes that actual negative submodule. PR1066 alone proved only the explicitly artificial truncation recorded here. Neither theorem identifies this submodule with the full Rao module or supplies positive-coordinate stability.

## A former zero alternative is excluded

Assume the unselected nine-dimensional generated-endpoint branch. Then F2=I2⊕P_h, F3=I3⊕(W⊗P_h), F4=NC4=P+D. The quadratic descendants of P_h have a **nonzero P component in I4**. The former optional-zero P graph is therefore no longer an alternative in this branch. The negative-module extension 0→I→F→F/I→0 is nonsplit, even without requiring equivariance.

The scalar of the graph remains unknown. This refines a branch condition, not a choice between endpoint nine and sixteen or a source-pair exclusion.

## Balancedness forces nonvanishing

Inside the actual polynomial model NC=(Sym¹⁶W,Sym¹⁷W,Sym¹⁸W/H_t), P_h is the unique P16. Let U be the W′ constituent of its first descendants. Polynomial multiplication embeds W⊗U=P into Sym¹⁸W; call its image P_desc. It is exactly the P part of the quadratic descendants.

The next polynomial multiplication of P_desc has image Sym²W⊗U=T, of dimension six, and kernel W′. Balancedness of the actual endpoint says H_t⊗W→Sym¹⁹W is an isomorphism. Thus P_desc cannot equal the P-isotypical endpoint subspace P_t⊂H_t, since its W′ multiplication kernel would violate that isomorphism. Its quotient image in NC4 is therefore the nonzero unique P, namely I4.

Any equivariant splitting of F over F/I would have to lift the P generators to P_h, since Hom(P,I2)=0. Their nonzero quadratic P descendants contradict a splitting. A nonequivariant splitting would average to an equivariant one, so it is excluded too. This argument neither evaluates P_t nor chooses a graph coefficient.

## Minimal actual relations through quadratic degree

Grade F2 as degree zero. The only linear relations are the four literal Koszul relations on I2=Sym⁴W, forming S=Sym³W. Their linear multiples are independent, with representation W⊗S=A+D.

After dividing out those multiples, the degree-two presentation is

    (V_I+P_I)⊕(V_h+P_h^(2)+D_h).

The first V is killed by the image-system quotient, the second V is killed because NC4 has no V, and D_h maps isomorphically onto the endpoint D. Both P factors map isomorphically onto I4. Thus the minimal new quadratic relation space is

    2V⊕graph(P),

with both graph projections nonzero. The repeated V and P labels denote these specified source summands, not arbitrary equal-character subspaces.

## Explicit artificial truncation only

Define a different, artificially truncated R=Sym W module by M0=F2, M1=F3, M2=F4 and M_n=0 for n≥3. Its socle is exactly M2. The degree-zero joint annihilator is zero; in degree one the W′ part multiplies nontrivially, while the D projection separates the two T copies and the remaining T_I still multiplies to I4. Thus no lower socle remains.

The exact minimal equivariant resolution is

    0→(P+D)⊗R(-4)
      →S⊗R(-1)⊕(2V+P)⊗R(-2)⊕S⊗R(-3)
      →(P+D)⊗R→M→0.

The two-variable Koszul socle calculation puts Tor2 solely in degree four, and the representation-valued Hilbert numerator fixes the first syzygies. Its dimension numerator is 9−4t−10t²−4t³+9t⁴.

This resolution is **not a resolution of the full actual Rao module**. The artificial cubic relations do not assert vanishing in actual degree five, and no terminal-descendant conclusion follows.

## Q-preserving normalization retains an unknown ratio

Fix reference intertwiners and write λ≠0 for the P descendant coefficient and q≠0 for Q|P_h. Equivariant generator changes scale I2 by b and P_h by a; the first arrows determine their action on the generated middle space. Comparing two presentations gives

    bλ=aλ′,       bq=aq′,
    λ/q=λ′/q′.

If the literal Q normalization is fixed, q′=q forces a=b and λ′=λ. Changing reference intertwiners renames coordinates but does not eliminate the actual graph while preserving the specified arrows and Q. Nonvanishing is proved; no universal or actual numerical scalar is supplied.

The written balancedness, relation and socle arguments are supported by exact universal polynomial checks. Endpoint nine versus sixteen, actual source occurrence, the gate coefficients and the four necessary source-dual pairs remain unselected.
