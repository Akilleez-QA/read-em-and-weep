# Nonzero first-block projection: the length-51 actual negative module

**23 October 2026 · PR1081, read in full**

[Immutable proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/411b644cdc12938c35b7fedac5bb92664bfc1a47/research/hm/source2-pure-v-separated-terminal/PROOF.md), blob `3aa53fa809fa82cef18629cc040cf61fe4eb0a90`.

## Hypothesis and exact module

Retain actual source2 pure-V compatible-radical hypotheses and a genuine separated negative block N0. Assume the canonical P_h has nonzero projection to N0,2. For R=Sym W, the actual module F∞=R·im h has original degrees 2,3,4,5 of dimensions **9,14,16,12**, and is zero from degree six. Its length is **51**. Its terminal character is 2T, not the single marked residual T of the other surviving mechanism.

The actual projection F5→N0,5 is an isomorphism onto the full T-isotypical component of N0,5=W′+2T. This does **not** identify F5 with that separated subspace: it can be a graph into NR5=T, whose map remains unspecified.

## Actual quotient and universal certificate

The actual Koszul sequence and multiplication-compatible projectors give

N0,5 = (Sym³W ⊗ Sym⁸W)/im[W ⊗ Sym¹⁰W → Sym³W ⊗ Sym⁸W],

where the relation map is W times the same quadratic polarization used for N0,4. The relation image has rank 22. The pair of unnormalized transvectants of orders two and three gives a rank-14 map onto Sym⁷W⊕Sym⁵W, annihilating precisely those relations.

Restricting the full cubic descendant map to the pinned P8 inclusion gives rank twelve. A specified twelve-by-twelve minor has determinant −548077643046499094530321725505142784. The domain Sym³W⊗P=S+2T and target W′+2T have no common S, giving the matching upper bound. Naturality transports this universal certificate through the actual nonzero P_h projection. It is not an evaluated HM-instance rank.

## Socle, resolution and annihilator

The degree-four socle is exactly F4∩NC4=I4=P: the first-block projection is injective on all quadratic P_h descendants, whereas NC4 has zero such projection. Actual Koszul injectivity excludes a degree-three socle; the disjoint first images exclude degree two. All of F5=2T is terminal. Thus the full socle is I4 in degree four plus 2T in degree five.

With original cohomological grading, the minimal equivariant resolution is

    0 → P⊗R(-6) ⊕ 2T⊗R(-7)
      → S⊗R(-3) ⊕ V⊗R(-4) ⊕ (W′+S)⊗R(-5)
          ⊕ (V+P+D)⊗R(-6)
      → (P+D)⊗R(-2) → F∞ → 0.

The quartic relation P in R(-6) is compulsory even though it cancels numerically against the socle P in the Hilbert numerator. Equal-shift terms do not permit constant cancellation in a minimal resolution: that differential component is zero.

The exact annihilator is (W)⁴. Quartic products vanish by terminality, while the action of each irreducible SymᵈW for d=1,2,3 is nonzero and therefore faithful as a representation map. Homogeneity excludes hidden lower-degree annihilators.

## Current boundary

[PR1082](109-small-branch-exclusion.md) leaves this mechanism and the [residual-large length-45 mechanism](107-actual-residual-large-module.md), with neither selected or realized. These are negative-coordinate modules, not full Rao modules, Q-stable or positive-stable submodules. The terminal graph, positive action and actual gate coefficient are not determined. The written actual-map transport is essential; finite rational rank and representation checks do not replace it.
