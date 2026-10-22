# Actual square quotient splitting and nonzero boundary on both summands

## Result

The actual cover-degree-eight square algebra quotient satisfies

    Q4(6) = W O_L(7) plus V O_L(4).                 (1)

For the actual square-ideal boundary

    delta: H0(Q4(6)) -> H1(P4 O_L(-2))=P4,

the restriction to EACH summand in (1) is nonzero, hence onto P4. In particular its V O(4) restriction is the unique P4 projection from V tensor D5, up to a NONZERO scalar. This does not determine the actual operator residue in Q4(6), and the two contributions can still cancel.

Dependencies are the actual degree-eight wedge diagram and the double-cubic/finite-duality splitting. No actual coefficient or actual-instance map evaluation is used.

## 1. Divide by the scalar nilpotent class

ACTUAL-DEGREE-EIGHT-DEFECT-AS-DOUBLE-CUBIC-PUSHFORWARD.md proves

    M8=A O_L(6) plus V O_L(4).

ACTUAL-DEGREE-EIGHT-NORMAL-OPERATOR-QUOTIENT.md proves the actual wedge sequence

    0 -> O_L(4) --class(N)--> M8 -> Q4(6) -> 0.     (2)

The V component of its injection is zero because

    Hom_G(O_L(4),V O_L(4))=V^G=0.

Its A component is nonzero by injectivity. Its equivariant Hom space is one-dimensional, since A=Sym^2 W and H0(O_L(2))=A. Therefore it is the dual complete-quadratic evaluation inclusion, up to a nonzero scalar. The dual evaluation sequence twisted by6 is

    0 -> O_L(4) -> A O_L(6) -> W O_L(7) -> 0.

This proves (1). Its ordinary section dimensions are16 and15, totaling31. No choice of an actual homogeneous G(4) subbundle is needed.

## 2. A perfect-pairing test for the boundary

For constant vector spaces U,T and d>=0, an extension

    0 -> T O_L(-2) -> E -> U O_L(d) -> 0

has class in Hom(U,T) tensor H1(O_L(-d-2)). Its global connecting map is exactly the cup pairing

    U tensor H0(O_L(d)) -> T tensor H1(O_L(-2)).

Serre duality makes H1(O_L(-d-2)) paired perfectly with H0(O_L(d)). Thus this connecting map vanishes identically if and only if the extension class vanishes. This assertion holds for the full map, not only for invariant vectors, and also applies to equivariant extensions.

## 3. Apply to the actual polynomial presentation

The actual square ideal gives

    0 -> P4 O_L(-2) -> Sym^8(Wprime) O_L(2)
      -> Q4(6) -> 0.                              (3)

Pull back (3) along either direct-summand inclusion U O_L(d)->Q4(6), with (U,d)=(W,7) or (V,4). If the corresponding restriction of delta vanished, Section2 would split that pullback extension. Its splitting would give a nonzero bundle map

    U O_L(d) -> Sym^8(Wprime) O_L(2)

lifting the direct-summand inclusion. But this Hom space is zero because H0(O_L(2-d))=0 for both d=7 and d=4. This contradiction proves both restrictions are nonzero. Equivariance and irreducibility of P4 then give surjectivity of each restriction.

The V O(4) section character is

    V tensor D5 = A plus V plus P4 plus D5.

It contains exactly one P4, proving the asserted unique nonzero projection. The W O(7) section character is V plus 2P4 plus D5; it contains two possible P4 channels, and this argument does not select their ratio.

## 4. What remains

The actual third value is the boundary of the particular corrected midpoint operator residue, then reduced by the actual second-symbol image. Equations(1)-(3) make that remaining boundary an explicit pair of nonzero maps on known split bundles. They do not show that the particular residue has a nonzero image, nor exclude cancellation between its two components.
