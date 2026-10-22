# Independent mathematical review

## Result

The interpolation theorem and its universal Bezout construction pass independent mathematical review. The supplied verifier was rerun successfully with exit status zero. This is a mathematical review plus bounded symbolic verification, not a proof-assistant formalization.

The review takes the cited geometric hypotheses and complementary-middle transport identity as inputs. It verifies the deductions from those inputs, rather than independently reconstructing the underlying bicubic or transport identity.

## Checks

- In either positive affine chart, Euler's identity identifies the derivative ideal with `(f,f_x)`. For a smooth curve this is the ramification scheme of the negative projection. Its finite support makes the two defining sections a regular sequence, giving the stated Koszul resolution.
- After twisting by `(4,n)`, the relevant middle H1 and left H2 vanish for every integer n >= 2. Restriction is therefore surjective. Its kernel dimension is `5n-7`. The argument covers all such n; the finite range in the verifier is a check of the formulas, not the proof of the infinite assertion.
- The difference between the full kernel and ordinary polynomial derivative multiples is exactly H1(O(0,n-6)). Its dimensions are three, two, and one at n = 2, 3, and 4, and zero thereafter. At n >= 6, the initial H0 term correctly accounts for the Koszul relation.
- At fixed positive degree four, degrees zero and one have domain dimensions five and ten, so neither can interpolate arbitrary values on a length-twelve scheme. Degree two is minimal.
- The Bezout coefficients have bidegree `(4,2)` and vanish scheme-theoretically on the derivative-zero scheme. Cancellation of the determinant factor is valid on either negative affine chart because it is monic, up to a unit, in a primed affine variable. Finiteness of the common-zero scheme implies that the two binary cubics are generically coprime along the positive factor. The nonzero Bezout determinant then proves coefficient independence.
- The verifier successfully checks the determinant/resultant identity with eight free coefficients, the cohomological dimension formulas, and the indicated A5 character identity. No actual bicubic coefficients or ramification points enter those checks.
- Under the stated determinant-one linearizations and invariant equation, the kernel identification is equivariant. Serre duality and SL2 self-duality identify K_2 with the negative quadratic representation. The representation quotient is the fiber-weighted space H0(R,O_R(4,2)), not automatically the ordinary permutation module on the twelve points.
- The fixed-source physical expression has degree `(4,6)` under the stated degree conventions, while its coefficient before source evaluation has degree `(4,4)`. The proof correctly distinguishes both from the minimal scalar interpolation degree `(4,2)`.

## Scope and qualifications

Reducedness permits ordinary pointwise interpolation; the cohomological proof itself works for the corresponding finite complete-intersection scheme. Injectivity of the projections is not used in the interpolation proof.

The result removes the obstruction to extending scalar values in the specified line-bundle fibers. It does not establish that an interpolant lies in the admissible middle-operator symbol image, nor that independently extended values give a compatible source-linear map. Those limitations are explicit in the proof. The distinct kernel spaces K_4 and K_6 are separate affine freedoms, not a quotient of one by the other.

## Additional review: complete generator recipe

The added constructive recipe in Section 4 also passes review. Multiplication by any negative form of degree n-2 gives a morphism from the n=2 twisted Koszul sequence to the n sequence. Naturality of the connecting homomorphism therefore identifies the images of the multiplied Bezout generators with the cup-product map H1(O(-4)) tensor H0(O(n-2)) to H1(O(n-6)).

For n=2,3,4, the dual map is q ↦ (p ↦ pq), where q has degree 4-n and p has degree n-2. This map is injective because the homogeneous polynomial ring has no zero divisors. Thus the cup-product map is surjective. The ordinary derivative multiples already span the kernel of the connecting map, so together these two explicitly stated finite spanning families generate K_n. For n >= 5, the connecting target vanishes and derivative multiples alone suffice. The recipe claims a spanning set, not independence or a minimal basis, and introduces no assertion about admissible operator symbols.
