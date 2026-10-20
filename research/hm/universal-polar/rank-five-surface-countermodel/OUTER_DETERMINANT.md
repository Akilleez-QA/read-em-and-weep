# Optional strengthening: a nonzero outer determinant in the synthetic model

## Statement and scope

The quotient kernel in ./PROOF.md can also be chosen so that the
synthetic operation has a nonzero outer determinant section. Thus its
isolated rank-five middle point and two-dimensional independent-zero
fiber do not force that determinant to vanish identically.

This is an additional open condition within the same abstract quotient
construction. It makes no nonvanishing assertion for the actual source
operation, and evaluates no source input or matrix.

## 1. The universal outer image

Retain the notation of ./PROOF.md, and set

    H = Cu ⊕ E0,       dim H=4.

Choose an abstract complementary line Cr, so V=Cr⊕H. For the universal
operation f0 define

    O_r = span{ f0(p,q,r) : p,q∈V } ⊂ W.

We claim that

    dim O_r=20,
    O_r ∩ (H⊗Λ²H)=0.                                    (1)

For h,k∈H,

    f0(h,k,r) = h⊗(k∧r) + r⊗(k∧h).

Projection to the summand H⊗(H∧r) is the tensor isomorphism
h⊗k↦h⊗(k∧r). Hence the image of H⊗H has dimension 16. Its tensors
have exactly one r-factor in the direct-sum grading induced by
V=Cr⊕H.

The mixed-input values are

    f0(h,r,r) = r⊗(r∧h),
    f0(r,h,r) = −2r⊗(r∧h),
    f0(r,r,r) = 0.

They span r⊗(r∧H), of dimension 4. This summand has two r-factors,
so it is independent of the preceding 16-dimensional image. All outer
values are sums of these two parts, proving dim O_r=20. They have no
component of r-degree zero, whereas H⊗Λ²H is exactly such a component.
This proves the second assertion in (1).

The prescribed graph kernel L lies in H⊗Λ²H, by its formula
B0_u(q)−A0_u(v(q)) with q∈Sym²E0 and v(q)∈E0. Therefore

    O_r ∩ L=0.                                            (2)

## 2. One further nonempty open condition

The image O_bar of O_r in W_bar=W/L is 20-dimensional. In the
irreducible parameter space

    G=Gr(15,W_bar),       dim W_bar=35,

the condition

    M∩O_bar=0

is nonempty open: a 15-plane complementary to O_bar exists because
15+20=35. In inverse-image terms it says

    K_tot∩O_r=0.                                          (3)

Intersect this open with the three nonempty opens already imposed in
Section 5 of ./PROOF.md. The intersection remains nonempty, and all
its previous conclusions hold unchanged.

For the resulting quotient p:W→J, both O_r and J have dimension 20.
Equation (3) makes p|O_r an isomorphism. Consequently

    V⊗V → J,       p⊗q ↦ f(p,q,r)

has rank 20.

## 3. Interpretation as outer-determinant nonvanishing

Outer symmetry and cyclic zero impose the canonical relations

    r⊗h + 2h⊗r

in the kernel of the last map, including its nonzero multiple 3r⊗r
when h=r. These relations form a five-dimensional subspace of V⊗V,
so the map descends to the canonical 20-dimensional outer quotient
at [r]. The induced map to J is an isomorphism, because it has rank
20. Therefore its determinant is nonzero at [r].

Equivalently, for the global outer quotient bundle C on P(V) and its
map Phi:C→J⊗O described in
../outer-boundary-determinant/PROOF.md, the determinant section

    delta=det Phi

is not identically zero for this synthetic model. That section has
line bundle O(15), up to fixed determinant factors. No explicit
polynomial, source-operation matrix, or numerical rank witness is
needed: its nonvanishing follows from the abstract support grading
and the additional open complement condition.

The distinction remains important: this is an existence proof for a
chosen synthetic quotient, not evidence that the determinant of the
specified actual operation is nonzero.
