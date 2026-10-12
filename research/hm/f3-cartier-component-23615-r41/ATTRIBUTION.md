# Scope and next mathematical obligation

Write C_r(f)=sum_q [x^(3q+r)]f x^q over F3, with four coordinates and
r=(2,1,1,1), with code=sum(r[k]*3**k)=41. Dense traversal separately
uses the last coordinate fastest.
The supplied value is C_r(s23615). It is one internal component, not Q1 below.

The authenticated source-use review identifies one original use: the fourth
row of s25027 contains tag 15 times s23615. The direct module use is twisted
product 142904=(15,133174), with no ordinary outside-weight reference to source s23615.
Its global source demand includes all 81 residue channels. Completing channel 41
does not discharge that demand or justify substituting this section for the
full original source. A next assembly must pin all companion coefficients,
channels, original/module identifiers, support windows and shared uses.

## Remaining assignment 01234 recurrence

The first complemented numerator U is the normalized root scalar 2 times
s8^2 s9 s10^2 s11^2 s14^2 s15^2 s16 s21 s42167. Preserve that scalar.
The adjusted polynomial sections are:

- Q1=C_(2,1,1,1)(U).
- Q2=C_(2,2,1,0)(Q1 M2), M2=s8^2 s10^2 s11^2 s12^2 s14^2.
- Q3=C_(0,0,0,0)(Q2 M3),
  M3=s8^2 s9^2 s10 s11^2 s12^2 s13^2 s14 s15^2.

The external Laurent carries are respectively (-3,-3,-2,-2),
(-1,-1,-1,-1), (-1,-1,-1,-1). The final denominator is
E3=s8 s9 s10 s11 s12 s13 s14 s15. The assignment scalar is the
coefficient at (-1,-1,-1,-1) after multiplication by the exact Laurent
multiplier A D/E3 and the final carry monomial. Preserve A's scalar.

The target-preserving Q3 demand is total degree 46 inside
[19,22] x [10,23] x [0,17] x [0,4], enclosing 270 positions.
Q2 has bounds(16,0,0,0)..(27,28,28,12), total 37..79;
Q1 has bounds(22,0,0,0)..(57,58,57,36), total 84..173.
These are demand enclosures, not assertions of nonzero support.
For any product, every pair of input residues compatible modulo3 contributes,
with its coordinate carry. Outside cube-peeled weights retain their complete
original polynomials in the quotient variables.

## Larger pairing

Assignment01234 already combines the two signed J2 queries on simplex
(0,1,3,7,15), orientation+1. The J2 transfer minus and row-shuffle signs are
already incorporated; adding another J2 minus would double count a sign.
Of 94 assignments on that first J2 simplex, 29 remain possible after 14 syntactic
zeros and 51 support exclusions. The other 23 J2 simplices and fresh F3 J0/J1
contributions on 2/6 simplices also remain.

There is one pairing with nine signed queries: three J0 weights [1,-2,1],
four J1 weights [1,2,1,2], and two J2 weights [-1,1]. J3's direct tensor image
vanishes in degree 5, while J3 is retained for source closure and the comparison
homotopy. Old comparison components cannot be transferred individually.
Only a complete nonzero F3 pairing gives the corresponding rational
nonvanishing implication; this nonzero internal polynomial does not.

## Source identity anchors (not included source files)

Normalized formulas:8067c59cd141b44741156bd5ac5d0ac2d7055177b6aee43ea9a09f1b600176fc
Module graph:58203463187374dd0e1259712f6b0ead0c24983022b33f8740de579c3a2703a6
Recurrence:89a303696a3253ed4974ead7632aaedc3867f74b553875934e23e0e708c42799
Demand review:493b39a57b03616e1f837de923b6b7457401edc041ebb9d5e4de12fc57580c92
Nine-query source:513229cb2cfd152b8e2036d4c8e09fbcf9493721824fa33a61e5f0b351fbd045
F3 comparison:304e50f18127392ee8eca01abf349801e55eeae7e7586e8a65ca6c123acb155d
