# Current independent mathematical review

Independent mathematical review, 20 October 2026. This is a check of the written derivation and the stated immediate prerequisites, not a formal verification certificate. Earlier audits are treated as historical evidence, not as a substitute for this review.

Reviewed PROOF.md SHA256: 5850b9a99d9e68d287b27dc611232fefd2ced59443da264bbf7063016356d906

Reviewed Git blob SHA1: 74a73edcd859b13dddf72dc738d7bf9c6d5c283d

## Verdict and scope

PASS for the plane ideal-sheaf theorem under the stipulated orbit and representation inputs. The genuinely additional conclusion is quartic generation and the exact degree-eight double-point base ideal, not a new global rank exclusion.

## Checks

- The unique involution in each Dic3 stabilizer gives exactly one positive-plane incidence. Distinct positive planes cannot coincide because their involution product is a nontrivial translation with only five projective eigenpoints. Transitivity therefore gives ten points per plane.
- The invariant quadratic is nonzero on every order-three axis: its pairing with the other eigenspaces vanishes, so an isotropic fixed axis would be in its radical. The symmetric-cube character is (10,-2,1,0,0), equal to T+T'+P4. Consequently an invariant cubic gcd cannot occur; a positive-degree gcd can only be the quadratic, which cannot vanish at these ten points. In the coprime case, two cubics would violate Bezout's bound nine.
- Cubic evaluation is thus an isomorphism. At a point p_i, products of its cubic interpolation unit with two independent lines through p_i generate the maximal ideal. Away from the ten points, an interpolation cubic nonzero at the point times a suitable line supplies a nonvanishing quartic. This proves global generation of I_X(4), not merely generation off a possible finite residual set.
- Quartic evaluation is surjective, so h0(I_X(4))=5. Pairwise products generate I_X^2 stalkwise. As the full degree-eight double-vanishing system contains those products and all its sections already lie in I_X^2(8), its base ideal is exactly I_X^2.

No assertion about spanning all sections by the products, saturation of the homogeneous ordinary square, ambient plane compatibility, normal derivatives, or global operation values follows. PR212 supplies the orbit/stabilizer input; PR230 supplies the character facts and separate stronger actual rank conclusions.
