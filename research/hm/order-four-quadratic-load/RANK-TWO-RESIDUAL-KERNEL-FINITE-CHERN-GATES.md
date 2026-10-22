# Finite Chern gates for the rank-two residual alternative

## Statement and limits

Work over C on P=P(Sym^2 W), with G=SL2(F5). Assume the established seven possible splittings of C_lin and the actual residual morphism

    m: E4=W tensor S6* -> K8.

This note does not choose its generic rank. IF that rank is two, let N=ker(m) and I=im(m). Then N is a rank-two vector bundle, I is torsion-free rank two, and both are G-equivariant slope-semistable. Write

    c1(N)=-d, c2(N)=n.

Then

    6 <= d <= 28, d even,
    c1(I)=d-10,
    c2(I)=55+d^2-10d-n.                         (1)

There are stronger type-dependent bounds below. Every center-odd equivariant rank-two torsion-free sheaf on P2 has EVEN first Chern class. If c1=2a then c2 is congruent to a modulo 2. Each of N and I further satisfies the normalized Chern gate:

- c2-a^2 is a nonnegative EVEN integer.
- If it is nonzero, it is at least two.
- Equality 0 forces the sheaf to be R tensor O(a), where R is a two-dimensional representation with central character -1. In particular the sheaf is locally free, not a punctual modification of such a bundle.

These are necessary conditions only. We do not assert existence for any surviving Chern pair or any particular splitting type, and we do not infer rank four from a finite list.

## 1. Center parity forces rank-two semistability

The center acts trivially on P and on every G-linearized line bundle on P: the standard O(1) is center-even and G has no nontrivial characters. Every rank-one equivariant torsion-free sheaf therefore has center-even double dual, and is itself center-even.

A center-odd rank-two torsion-free sheaf cannot be unstable. Its unique maximal destabilizing rank-one saturated subsheaf would be G-equivariant by uniqueness of the Harder-Narasimhan filtration, and center-odd by inclusion. Its double dual contradicts the preceding paragraph. Thus every such rank-two sheaf is slope-semistable; if its first Chern class is odd it is stable, since equal rank-one slope would not be integral.

Both N and I inherit central character -1. The kernel N is locally free: on the smooth surface, the kernel of a map from a locally free sheaf onto a torsion-free sheaf has depth two at closed points, hence is reflexive, hence locally free. The actual image I, not an assumed saturated image, is used throughout (1).

## 2. Stability of the root bundles

On the ordered-root cover nu:P1 x P1 -> P2, natural evaluation gives

    0 -> O(-1,n-1) -> nu* S_n -> O(n,0) -> 0.    (2)

Evaluation is surjective even on the diagonal, since a section on a length-two scheme can be evaluated at its selected root. The kernel follows either from the universal root sequence or from det(nu*S_n)=O(n-1,n-1).

For n>=2 put t=ceil((n-1)/2). Twisting (2) by O(-t,-t) makes both end terms have a negative coordinate, so H0(S_n(-t))=0. A destabilizing rank-one subsheaf of S_n would extend across its finite singular set to a nonzero O(a)->S_n with a>=t, contradicting this vanishing. Thus S_n is stable, with slope (n-1)/2. Its dual is stable as well.

In particular E=S6* is stable with slope -5/2. A nonzero component of N -> W tensor E gives mu(N)<=-5/2. Equality would make N stable and isomorphic to E. The inclusion would then correspond to a line in W. Because N and the inclusion are equivariant, that line would be G-invariant, impossible for irreducible W. Hence c1(N)<-5, proving d>=6.

This excludes the equal-slope rank-two direct-summand alternative, not just odd generic ranks.

## 3. Type-dependent upper bounds on d

The seven previously established possibilities for F4=ker[C_lin->O(2)] and hence K8=nu_*eta*(F4(1)) are:

    F4                            K8                              d maximum
    P4 O(6)                       P4 tensor S7                    14
    W' O(5) + W' O(7)             W' tensor S6 + W' tensor S8      16
    V O(4) + O(12)                V tensor S5 + S13               22
    A O(2) + O(18)                A tensor S3 + S19               28
    O + V O(8)                    S1 + V tensor S9                16
    O + W' O(5) + O(14)           S1 + W' tensor S6 + S15         24
    O + W O(3) + O(18)            S1 + W tensor S4 + S19          28

Here S1=W tensor O is semistable of slope zero, and every other displayed S_n is stable by Section 2. Since I is semistable, any nonzero component of I->K8 bounds mu(I) by the largest displayed slope.

For rows 1, 2 and 5 the maximal-slope factor has respectively multiplicity P4, W', V, all with no invariant line. Equality of slopes would force I** to be isomorphic to that S_n: a nonzero equal-slope map to a stable rank-two target has full rank, and its double dual has constant nonzero determinant. All maps into the maximal factor would then be proportional in the S_n coordinate. Equivariance makes their multiplicity line invariant, impossible. Thus the slope inequality is strict in those rows. Inserting c1(I)=d-10 and the even-determinant constraint in Section 4 gives the bounds in the table.

No saturation correction is omitted: only the torsion-free I and its double dual are used for this slope argument; (1) uses the actual I.

## 4. Hilbert-polynomial parity and the normalized second-Chern gate

First, every finite-dimensional representation of G with central character -1 has even dimension. One can see this without the character table by restricting to a quaternion subgroup Q8: its generators i,j satisfy i^2=j^2=-1 and ij=-ji. The operator i is diagonalizable with eigenvalues +sqrt(-1),-sqrt(-1), and j interchanges its two eigenspaces. Their dimensions are equal.

Let H be ANY center-odd equivariant rank-two coherent sheaf on P2. Each cohomology group H^i(P2,H(t)) is a center-odd representation, because the center acts trivially on the base and on O(t). All their dimensions, and hence chi(H(t)), are even. For torsion-free H with Chern classes c1,c2, Riemann-Roch gives

    chi(H(t)) = t^2+(c1+3)t+2+(c1^2+3c1)/2-c2,
    chi(H(t+1))-chi(H(t)) = 2t+c1+4.

Therefore c1 is even. Write c1=2a. Evaluating at t=0 then gives

    c2 == a (mod 2).                              (3a)

This argument does not require semistability. In particular no odd-determinant hypothetical kernel or image is possible.

Now twist the torsion-free H to c1=0; this preserves its central character and semistability from Section 1. Its normalized c2 is c2-a^2, which is even by (3a). Serre duality and semistability give H2(H)=Hom(H,O(-3))*=0.

If H0(H)=0, Riemann-Roch gives chi(H)=2-c2(H), hence c2(H)>=2.

If instead H0(H) is nonzero, the image of the equivariant evaluation H0(H) tensor O -> H cannot have generic rank one: its rank-one double dual would be an equivariant center-odd line bundle. Thus two sections are generically independent. Their wedge is a nonzero constant section of det(H)=O. They trivialize H** everywhere; the factorization O^2 -> H -> H**=O^2 has invertible determinant and hence is an isomorphism. Therefore H=R tensor O for the two-dimensional center-odd representation R=H0(H), and c2(H)=0.

Twisting back proves the normalized gate, including exclusion of all odd normalized defects and exclusion of punctual singularities in the zero case. This proof does not invoke Bogomolov.

## 5. Source vanishing strengthens the small determinant cases

The defining Steiner sequence 0 -> Sym^4 W O(-1) -> Sym^6 W O -> S6 -> 0 gives H0(S6(-1))=0, since H1(O(-2))=0 on P2. Since S6*=S6(-5), this is H0(E(4))=0. Consequently H0(N(4))=0.

For d<14, semistability gives H2(N(4))=Hom(N,O(-7))*=0. Riemann-Roch now implies

    n >= (d^2-11d+60)/2,       6<=d<=12, d even.           (3)

In particular the lower kernel c2 bounds at d=6,8 improve to 15,18, respectively, rather than 9,16. For d>=14 this particular H2 vanishing is not asserted. Also a split kernel with even d has nonzero H0(N(4)) whenever d<=8, so the zero-normalized-defect case is excluded there independently.

## 6. Chern accounting and reproducibility

The source has c1(E4)=-10,c2(E4)=55. Applying c(E4)=c(N)c(I) gives (1). Apply Section 4 to c1=-d and c1=d-10. Consequently d is even, n is congruent to d/2 modulo 2, and n lies in the finite interval

    d^2/4 <= n <= 55+d^2-10d-(d-10)^2/4,

Also impose (3) when 6<=d<=12, d even. The image parity automatically agrees: c2(I) is congruent to (d-10)/2 modulo 2 because the Chern sum 55+d^2-10d is odd. Zero normalized defect has the rigid splitting consequence above.

The companion verify_rank_two_chern_gates.py computes only this universal integer accounting and the displayed slope bounds. It contains no actual HM coefficients, selected fibers, matrices, or rank computation. Its surviving pairs are not geometric existence claims.

## Dependencies

- RESIDUAL-SMOOTHING-NONVANISHING-AND-EVEN-RANK.md supplies the actual residual map and rank-two-or-four alternative. This note is conditional on rank two and does not need its nonvanishing proof.
- NONZERO-INVARIANT-SMOOTHING-CHANNEL-BY-FLAG-FILTRATION.md supplies the unique surjective C_lin->O(2), residual source and K8.
- COKERNEL-SPLITTING-NINE-CANDIDATES-AND-LOW-QUOTIENT.md and the unique-channel result supply the seven remaining types.
- All root-cover, semistability, Riemann-Roch and Chern deductions needed here are proved above. Mathematical proof, not a Lean certificate.
