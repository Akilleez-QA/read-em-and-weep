# Independent review: full constant two-direction cup exclusion

Status: ACCEPTED for the bounded statement and corollary in PROOF.md.

Reviewed proof SHA256:

    384f9fdb789308fc718ca076804906ca5c0d107def08426f36b125b6afdec25d

## Independent derivation

The reviewer read the accepted same-pair scalar-side proof in full, independently derived the full endpoint formulas, and checked all six integer-mask substitutions before reading this new proof. The independent derivation used the reciprocal ratio r1/r0; converting to the proof's t=r0/r1 gives precisely formula (2) and every entry of the six-witness table. A tiny symbolic calculation used only constant coefficient labels and integer mask differences. No actual source, model, primitive matrix, physical polynomial, point, jet, residual, detector, or source computation was performed.

The signs are correct: the ambient associator gives (1+lambda)F+(lambda-1)G, with delta_row N=-F-G. The scalar-slot order makes the E contribution to G negative in the general formula. The diagonal contamination on 0135 and 0236 is respectively G=E/t R and G=-Dt R. Their earlier off-diagonal endpoint isolation cannot be reused unchanged, and the new proof explicitly handles this.

## Checks

1. Every ordered cup, including a diagonal cup, is a scalar cocycle by edge additivity. The accepted associator calculation therefore extends without a new first-lift existence assumption. Its implication is conditional on any valid first lift, independent of that lift and of arbitrary scalar c, matrix W, and associative second star coefficient.
2. The normalized same-carrier currents and F,G are multiples of H=diag(1,-1). Thus the scalar K cannot cancel the displayed trace-free obstruction.
3. All six witnesses are strictly increasing legal masks. Adding mask 4 changes the union to {0,...,7} but does not change the common legal locus L=(U0 intersect U1)^3 times U0. The existing auxiliary carrier and L intersect nontrivially by the accepted carrier nonemptiness and integrality. No new owner/localization is introduced.
4. R is a nonzero rational section, whose restriction to the nonempty open remains nonzero. Cancellation does not require pointwise nonvanishing everywhere.
5. The factorwise elliptic involution gives t -> -t in the product function field and fixes complex constants. Since t is nonzero in characteristic zero, the pairwise constant linear independence of {1,t} and {1,t^-1} follows. Applying this field automorphism requires no invariance of the carrier: equalities on a nonempty open first extend to the function field. The proof needs only these pairwise independence statements.
6. The first four witnesses force A=B=0 and (lambda-1)D=(lambda-1)E=0. The additional witnesses 0146 and 0245 give (1+lambda)D=(1+lambda)E=0. Subtraction yields 2D=2E=0. This proves the stated necessity for every complex constant lambda. Independently, the four tuples 0135,0236,0146,0245 alone also suffice after pairwise coefficient separation, providing a redundant check.
7. The quadratic-repair signs are correct: delta(q_d^2)=-2q_d,ij q_d,jk and delta(q0 q1)=-(q0,ij q1,jk+q1,ij q0,jk). The repaired constants are (-2s,15/4-t0,-t0,-2u), and A-B=15/4 excludes allzero. U'=U0+e g is the correct first-lift correction and remains regular on legal edges.

## Quantifiers and boundary

The proof makes no sufficiency claim at b=0. Both the coefficients C_ab and lambda must be constants; this is not a result about variable coefficients, arbitrary scalar cochains or coboundaries, changed zeroth transitions, algebra-overlap automorphisms, non-scalar higher twists, general star-gerbes, mixed-class exactness, or algebraicity. The conclusion is a trace-free associativity compatibility obstruction, not a nonzero closed Cech class. Within that scope, no mathematical correction is required.
