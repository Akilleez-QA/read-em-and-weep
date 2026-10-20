> Historical mathematical audit, preserved in full apart from nonmathematical process statements and source-link normalization. Original-source hashes identify the audited source text; publication-byte hashes are recorded separately. This is not a claim of a fresh or formal proof check.

# Independent audit: target-relative Atiyah detectors

## Verdict and scope

The cohomological vanishing argument in PROOF.md, including the stronger full-deck argument in section 3A, is valid. The two projective contraction maps are zero, and the target-relative first and second Atiyah-trace maps vanish on the entire full-deck sector of the stated product-cover geometry. The optional inversion calculation is also consistent with the stated imported cohomology and equivariance inputs; its bound of eight is strictly weaker than the actual zero theorem.

This audit checks abstract cup-product identities, natural coefficient contractions, Euler/Kunneth/Serre-duality arguments, and the displayed finite-character arithmetic. It accepts the established carrier, finite-cover eigensheaves, bundle splitting, classical HM cohomology rows, and equivariant KS79 theorem as inputs. It does not establish actual-source membership, authenticate raw source primitives, evaluate an obstruction, or identify a historical detector with the relative trace construction.

## 1. Bundle-valued symmetry and the rank-two identity

Put S=At_0(H) and t=tr At(H), so A=S+(t/2)Id. The required symmetry is a symmetry of cohomology classes, not an illicit commutation of arbitrary matrix-valued cocycles.

Before multiplying endomorphisms, the cup square S cup S changes sign under simultaneous interchange of its two End_0(H) tensor Omega^1 coefficient factors: both classes have cohomological degree one. After projecting the two Omega^1 factors to Omega^2, their interchange supplies another minus sign. Thus the resulting class with two still-unmultiplied End_0 factors is invariant under interchange of those factors. In characteristic zero it lies in the symmetric summand.

For every rank-two fiber and traceless u,v, one has

  uv+vu=tr(uv)Id.

Consequently the trace-free multiplication map vanishes on Sym^2 End_0(H), and tf(S^2)=0. Exchanging t and S in the cup-wedge product likewise produces two cancelling signs. The mixed terms therefore sum to tS, proving

  tf(A^2)=tS.

This is globally intrinsic and requires no global frame. Taking the scalar part gives the equivalent full Cayley-Hamilton identity

  A^2-tA+c_2(H)Id=0,
  2c_2(H)=t^2-tr(A^2),

with the common Atiyah normalization understood. A curvature representative gives the same identity because its scalar (1,1)-form entries have even total degree. These arguments justify the identity in cohomology; they do not imply a literal identity for arbitrary uncorrected Cech representatives.

## 2. Contraction and projective vanishing

For b in H^0(Lambda^2 T(-a)), define b# by beta(b#alpha)=b(alpha,beta). Then the sheaf identity

  b contracted with (alpha wedge beta)=beta(b#alpha)

shows that contraction of tS factors through the evaluation cup product of (b#)_*t in H^1(T(-a)) with S. Different standard contraction normalizations change only a fixed sign or factor. This factorization follows from morphisms of coefficient bundles and is therefore valid on sheaf cohomology; it does not assume that a cocycle representative of t is exact before applying b#.

The Euler sequence

  0 -> O(-a) -> O(1-a)^5 -> T(-a) -> 0

and the absence of intermediate line-bundle cohomology on P^4 give H^1(T(-a))=0. Thus the trace-free contraction vanishes. Its scalar component lies in H^2(O(-a)), also zero. The conclusion is valid for every integer a, including the stated a=1,2, and for every rank-two bundle on P^4.

## 3. Relative duality and the stronger full-deck route

The trace pairing gives self-duality of End E. The stated volume character converts full-deck Serre duality into deck-invariant cohomology, with an S4 sign twist and no simultaneous-inversion sign. The [22] representation is unchanged by the S4 sign twist. In the imported splitting of B=sigma_*O_Y, the two [22] generator summands occur at O(-1) and O(-2). Since multiplication by a class pulled back from P^4 is O_P^4-linear, its maps act componentwise in such a splitting. A splitting compatible with multiplication in B is unnecessary. This verifies the identification of the proposed [22] dual maps with the maps audited in section 2.

Section 3A proves more without any of this representation counting. By finite pushforward and the full-deck eigensheaf (q_*O_X)_full=L^(-2),

  H^3(X,f*Omega^1)_full
  = H^3(Y,sigma*Omega^1 tensor L^(-2)).

The pulled-back and twisted cotangent Euler sequence is exact:

  0 -> sigma*Omega^1 tensor L^(-2)
    -> (L^(-3))^5 -> L^(-2) -> 0.

Pullback preserves this sequence since it is locally split as a sequence of vector bundles. For Y=(P^1)^4, both L^(-3) and L^(-2) have cohomology only in degree four by Kunneth. The long exact sequence therefore makes the displayed H^3 zero. Hence tau_rel,1 vanishes on every full-deck class.

For full-deck z in H^2(End E), its trace is zero because H^2(O_X)_full=0: Kunneth gives characters supported on exactly two elliptic factors. Multiplying the full rank-two identity by z and taking trace consequently gives

  tau_rel,2(z)=f*c_1(H) cup tau_rel,1(z)
               -f*c_2(H) cup tr(z)=0.

All products retain the target-relative coefficient bundles. The formula does not replace f*Omega^1 by Omega_X^1. Thus the stronger vanishing holds on the entire full-deck sector, regardless of S4 type or inversion eigenvalue. The dimensions 352 and 176 merely describe the established sector and are not inputs to this vanishing argument.

## 4. Optional inversion-count audit

Under the stated lifts, R has eigenvalue multiplicities (3,2), trace 1, and determinant +1. The [22] generator at degree one has reversal character det(J)^2=+1. Finite duality B^vee=B(3) tensor sgn introduces no reversal character: the four P^1 determinant characters multiply to +1, and det R=+1. The degree-two [22] generator therefore also has reversal character +1. No hidden generator sign changes the counts below.

The symmetric-power traces in degrees 1,2,3,4 are 1,3,3,6, since their generating series is (1-t)^(-3)(1+t)^(-2). Also tr(Lambda^2 R)=(1^2-5)/2=-2. Exterior Euler then gives:

- H^0(Lambda^2 T(-1)): dimension 45, trace -3, positive dimension 21.
- H^0(Lambda^2 T(-2)): dimension 10, trace -2, positive dimension 4.

The imported Hom coefficient traces 18,1,-8,-2 and equality of negative-degree traces give the displayed equivariant Euler characteristics directly. For twist -1, only internal degrees 1,2,3 contribute, giving -1-8+6=-3. For twist -2, internal degrees 2,3,-3 contribute, giving -8+2+2=-4; the last term uses tr H^4(O(-5))=+1. These signs agree with the parity of the internal Hom degrees.

The equivariant KS79 identification gives [31] multiplicity trace -1. The degree-one [31] generator has trace -1, so its tensor product with H^1(End H(-1)) forces the latter trace to be +1. With the imported cohomology rows, this gives:

- H^2(End H(-1)): dimension 10, trace -2, positive dimension 4.
- H^2(End H(-2)): dimension 20, trace -4, positive dimension 8.

Thus the componentwise positive-image bound is min(21,4)+min(4,8)=8 in the 12-dimensional retained positive dual. This arithmetic is correct. It is not needed for, and does not weaken, the zero-map conclusion.

## 5. Evidence boundary

No flaw affecting the stated zero theorem was found. The essential qualification remains that the results concern genuine cohomology maps and classes. Their vanishing neither proves the obstruction is zero nor proves that an unrelated scalar, jet, or historical detector factors through one of these maps.
