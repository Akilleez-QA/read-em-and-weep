# Prior mathematical audit

This audit concerns the source manuscript. It is not a formal verification or a review of later normalized publication bytes.

# Audit of the optional outer-determinant strengthening

## Verdict

`OUTER_DETERMINANT.md` is correct as stated. Its additional Grassmannian
open condition is compatible with all the conditions in the frozen
`PROOF.md`, and it proves that the synthetic quotient can have a
nonzero outer determinant section. No revision is required.

## Support grading and dimension

With V=Cr⊕H, the map from H⊗H given by

    h⊗k ↦ f0(h,k,r)
         = h⊗(k∧r)+r⊗(k∧h)

is injective because its projection to H⊗(H∧r) is an isomorphism.
Its image therefore has dimension 16 and r-degree one. The mixed
values are exactly

    f0(h,r,r)=r⊗(r∧h),
    f0(r,h,r)=−2r⊗(r∧h),

and span a four-dimensional subspace of r-degree two. All outer
values are sums of these two parts. Thus dim O_r=20, and O_r has
zero intersection with the degree-zero summand H⊗Λ²H.

Every tensor in the prescribed five-dimensional graph L belongs to
H⊗Λ²H, because u, E0, and all correction values v(q) belong to H.
Consequently O_r∩L=0. This conclusion does not require a new property
of the already selected correction v.

## Simultaneous generic quotient

The image of O_r in W/L is 20-dimensional. The set of 15-planes
complementary to that image is a nonempty open subset of Gr(15,35).
Its intersection with the three established nonempty opens is
nonempty by irreducibility. The inverse-image kernel therefore
satisfies K_tot∩O_r=0 while retaining all residual-rank and
independent-zero conclusions of the main proof.

Since dim O_r=dim J=20, the restriction of the quotient map to O_r
is an isomorphism. The resulting bilinear outer map V⊗V→J at r has
rank 20.

## Canonical quotient and determinant

The displayed relation has the correct coefficient order:

    f(r,h,r)+2f(h,r,r)=0.

The tensors r⊗h+2h⊗r form a five-dimensional subspace. Indeed, writing
h=ar+w with w∈H gives

    3a r⊗r+r⊗w+2w⊗r,

whose components force a=w=0 if it vanishes. The bilinear outer map
therefore factors through its canonical 20-dimensional quotient and
has full rank there. The induced determinant is nonzero at [r].

The cited global bundle sequence is consistent with this fiber:

    0 → O(−2)⊗V → O(−1)⊗V⊗V → C → 0.

It gives c1(C)=−25h+10h=−15h, so det Phi is a section of O(15),
up to the fixed determinant factors of V and J. Full rank at [r]
proves this section is not identically zero.

This is an existence statement for the synthetic quotient only. The
argument makes no assertion about the actual source determinant and
does not evaluate that operation. No compactification or K3 assertion
is involved. Only this local review artifact was written.
