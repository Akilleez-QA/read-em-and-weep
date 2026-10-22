# The rank-eight degree-zero square quotient is not trivial

Let

    0 -> (A tensor V*) O_T(-6) -> E4,+ -> J -> 0      (1)

be the actual constant-rank square-product sequence of INTERTWINING-PLANE-BOUNDARIES-AND-SQUARE-SUBBUNDLES.md. Thus J has rank eight and degree zero. Here W is the actual negative binary representation, A=Sym^2 W is the opposite three-dimensional representation to V, S4=Sym^3 W, and T6=Sym^5 W. Denote the other binary two-dimensional representation by W'.

## Theorem

The actual bundle J is not trivial. More precisely, as representations of the binary icosahedral group,

    H0(T,J(-1)) contains 2W directsum S4,
    H1(T,J(-1)) contains W' directsum T6.              (2)

In particular both dimensions are at least eight. If J splits as a sum of O_T(a_i), then

    sum_{a_i>0} a_i = sum_{a_i<0} (-a_i) >= 8.        (3)

Neither equality in these bounds nor a particular splitting is asserted.

## 1. Identifying the actual target cohomology

On X=Bl_R(P4), with exceptional divisor E_R, the tautological identity is

    pi*O_T(-1)=p*O_P4(-1) tensor O_X(E_R).

The standard exceptional-divisor sequence gives

    Rp_*O_X(E_R)=O_P4.

Indeed Rp_*O_X=O_P4, while O_E_R(E_R) restricts to O_P1(-1) on each exceptional fiber and has zero direct images in every degree. Therefore

    H1(X,p*B(4) tensor pi*O_T(-1)) = H1(P4,B(3)).     (4)

This identification is equivariant: O_T(-1) has its actual inversion-odd linearization. The uniform twist-four theorem proves (R1 pi_*p*B(4))_+=0, while the even section bundle is E4,+. Taking the odd part of Leray after the odd twist in (4) consequently gives

    H1(T,E4,+(-1)) = H1(P4,B(3))_-.                  (5)

There is no contribution from the other R1 eigensheaf to this parity. Also H0(E4,+(-1))=0 because E4,+ is a subbundle of 30 O_T.

The actual ambient cohomology character, not merely its virtual Euler character, is established in EXCEPTIONAL-HYPERPLANE-CHARACTERS-AND-REMAINING-SCALAR.md, Section 3:

    H1(P4,B(3))_- = 3W' + 3S4 + 6T6.                (6)

That source uses the proved concentration of the actual ambient twist-three adjoint cohomology in H1. The subsequent elimination of exceptional torsion does not alter (6).

## 2. The source character and forced kernel

Twisting (1) by O_T(-1) yields the exact cohomology sequence

    0 -> H0(J(-1))
      -> (A tensor V*) tensor H1(O_T(-7))
      -> H1(E4,+(-1))
      -> H1(J(-1)) -> 0.                             (7)

Equivariant Serre duality identifies H1(O_T(-7)) with Sym^5 W, since the binary group has determinant one; all representations here are self-dual. The universal binary-icosahedral tensor decomposition is

    A tensor V tensor T6 = 2W + 2W' + 4S4 + 5T6.    (8)

The two middle spaces in (7) both have dimension 54, but their characters differ. In characteristic zero representations are semisimple, and an equivariant map cannot mix inequivalent irreducible summands. The target (6) has no W, so the entire source 2W lies in its kernel. Its S4 multiplicity is three, while the source multiplicity is four, forcing another S4 in the kernel. Dually, the target exceeds the source by one W' and one T6. This proves (2).

More precisely there is a possibly zero representation R, built from the shared W', S4, and T6 channels, such that

    H0(J(-1)) = 2W + S4 + R,
    H1(J(-1)) = W' + T6 + R.                         (9)

No maximal-rank assumption is made in a shared isotypical channel.

## 3. The splitting consequence and the remaining interface

For a degree-zero bundle J=sum O_T(a_i),

    h0(J(-1))=sum max(a_i,0),
    h1(J(-1))=sum max(-a_i,0).

Thus (2) implies (3) and immediately excludes J=8 O_T. A hypothetical trivial root-cover or fixed-representation-bundle description is therefore incompatible with the actual cohomology characters.

There is nevertheless a geometric realization. Let ev:Y tensor O_X->p*F(2) be the actual two-section evaluation and set

    T_ev=coker[Sym^2 Y tensor O_X -> p*B(3)].

The determinant is nonzero on each hyperplane, so this map is injective. After twisting by p*O(1), its pushforward gives

    J = pi_*(T_ev(1)),
    R1 pi_*(T_ev(1)) = C_lin(1),

where the first sheaf has even parity and the second odd parity. The source direct image is exactly the complete square-multiple bundle

    (A tensor V*) O_T(-6) directsum A O_T(-5),

and has no higher direct images. On the rank-one locus of the determinant surface, the evaluation has local form diag(1,f); its symmetric-square cokernel is

    O/(f) directsum O/(f^2).

Consequently this cokernel cannot simply be replaced by a line sheaf on the reduced three-plane determinant surface. Its nonreduced structure and the loci where the original evaluation has rank zero remain relevant to any more explicit description of J.

The standalone companion verify_square_quotient_character_obstruction.py checks (8), the actual character difference used in (9), and the forced dimensions using exact universal binary-group characters over Q(sqrt(5)). It evaluates no actual HM coefficients or multiplication matrices.
