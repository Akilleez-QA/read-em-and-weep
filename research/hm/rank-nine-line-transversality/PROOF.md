# Reduced actual beta points and first-order geometry along the twenty-five lines

Status: authored structural proof; independent mathematical review is recorded separately. Not formally checked. Over C. No selected actual HM/source coefficient, matrix or rank evaluation is used. All calculations below are universal deformation or representation calculations.

## 1. Pinned setting

Use PR562, commit 86b643fe2adecbd321d1c8f98be84fe2082bcd10: exactly twenty-five rank-two projective tensors k in P(V* tensor W*) give zero-wedge nets N_k=phi*(sl(W)^T k). Each is a beta net Lambda^2 B, with B of dimension three. Its radical R is two-dimensional; the lines P(R) are disjoint and evaluation has rank nine everywhere on them. The associated graph conic C_k in P(V*) x P(W*) is a torsion section of the smooth BHM surface Z=S(5), with self-intersection -5.

Use PR561, commit 7ebf187d7e45d43763bbf07436460f3c951aa8bd, for the universal beta chart. The full-normalizer interface is PR543 at 7bf725bcd857a2deb975f9ecb80fca32e7833ae0, PRIMARY-INJECTION-AND-FAILURE.md Section 1.

Let T be the rank-two open subset of P(V* tensor W*), dimension nine. Let f:T -> Gr(3,Lambda^2 A*) be k -> N_k. Let W0 be the closed subscheme of T defined by ALL ENTRIES of Sym^2 N_k -> Lambda^4 A*. These are the zero-wedge equations, not the two-by-two minors that impose wedge rank at most one.

## 2. The actual zero-wedge scheme is reduced of length twenty-five

For any first-order point k_epsilon of W0 over C[epsilon]/(epsilon^2), the hyperplane sl(W)^T k_epsilon in L_epsilon tensor W* has a nondegenerate annihilating pairing. Here L_epsilon is the rank-two image of k_epsilon; it is a direct summand after restriction to the rank-two open. Its rank-one locus is a flat graph conic C_epsilon, with each projection a projective isomorphism onto P(W*) and P(L_epsilon), respectively.

Every form in N_(k_epsilon) has square zero because all wedge entries vanish. Thus the graph conic is a subscheme of the decomposability incidence Z, not merely a set of points of Z: the Grassmannian of decomposable two-forms is defined scheme-theoretically by the Plucker wedge equations. Therefore C_epsilon is an embedded first-order deformation of C_k inside the smooth surface Z.

The normal bundle of the smooth rational section is O_(P1)(C_k^2)=O_(P1)(-5). Consequently H^0(C_k,N_(C_k/Z))=0, so its embedded first-order deformation is constant. The graph recovers k functorially: its first projection recovers L; its Segre linear span recovers the hyperplane H in L tensor W*; the inverse/adjugate of its nondegenerate annihilator recovers [k]. All these operations are morphisms on the indicated open sets and are valid over dual numbers. Hence constant C_epsilon implies constant k_epsilon.

Thus T_k W0=0 at every one of the twenty-five geometric points. Their local maximal ideals satisfy m/m^2=0, and Nakayama gives m=0. Since PR562 already gives exactly these twenty-five geometric points, W0 is the disjoint union of twenty-five reduced C-points, of scheme length twenty-five.

This says nothing yet about the scheme defined by wedge rank-one MINORS. Those equations have zero first derivatives at every zero-wedge point.

## 3. Injective actual normal derivative to the beta stratum

Write A*=B direct-sum C, dimensions three and two, with N=Lambda^2 B. In the Grassmannian chart use beta basis omega_1=b_2 wedge b_3, omega_2=b_3 wedge b_1, omega_3=b_1 wedge b_2 and write

eta_i = omega_i + sum_(l,j) M_l(i,j) b_j wedge c_l + z_i c_1 wedge c_2.

At the origin, linearizing eta_i wedge eta_j=0 imposes M_l+M_l^t=0 and z=0. Indeed omega_i wedge b_j=delta_ij vol_B, so the coefficient of vol_B wedge c_l is M_l(j,i)+M_l(i,j); the self-wedges also force every z_i=0. Hence the zero-wedge tangent space is exactly the six-dimensional skew-matrix space, the tangent to the beta stratum Gr(3,A*).

Section 2 therefore says that df followed by the quotient by this six-dimensional tangent space is injective. Equivalently the actual nine-dimensional tangent space meets the beta tangent space trivially in the ambient Grassmannian tangent space. This is an injectivity statement, not surjectivity onto the fifteen-dimensional beta normal space.

For the complement I=SL2(F5) fixing k, k is invariant and N is its irreducible even three-dimensional representation. Under phi*, the invariant line k is Lambda^2 C: the even exterior-square part is N direct-sum Lambda^2 C and N has no invariants. Thus T_k T decomposes as N direct-sum (B tensor C), with dimensions three even and six odd. The beta normal space decomposes as the symmetric mixed part Sym^2 B tensor C (dimension twelve, odd) plus the z-space Hom(N,Lambda^2 C) (dimension three, even). Here determinants are trivial because I is perfect, and the identifications use the invariant volume on B.

The even derivative N -> z is an isomorphism: parity forbids any other normal component, and Section 2 makes it injective. The odd derivative B tensor C -> Sym^2 B tensor C is injective.

Consequently the exact pulled-back universal radical incidence near (k,[r]) can first eliminate the three even variables formally or étale locally by z=0, since the relevant Jacobian is invertible. For the conclusions here only tangent-linear elimination is needed. Its remaining linearized equations are H(v)r=0, for v in the odd six-dimensional tangent and [r] in P(R)=P(C*). This deduction concerns the actual pullback, not a transfer of generic universal transversality.

## 4. Representation types, checked without a selected evaluation

The precise types are B=U', C=W, with Sym^2 W=U and U not isomorphic to U'. Here W is the faithful two-dimensional complement representation distinct from the actual multiplicity representation W' in phi. The following argument fixes the labels intrinsically.

The invariant rank-two tensor k embeds W' into V*. Since the central involution acts oddly on W' and the odd eigenspace of V has dimension two, it identifies V_odd with W'. The eigenspace dimension also follows from Lambda^2 A=V tensor W': its even part has dimension four, so dim V_odd=2. The actual full-normalizer identity Sym^2 A=V tensor U then gives, on odd parts,

B tensor C = W' tensor U = 6,

where the last equality is the irreducible six-dimensional character in the HM appendix. Independently Lambda^2 B=N=sl(W')=U'. Since determinant B is trivial and the even three-dimensional representations are self-dual, B=U'. If C were W', the character product U' tensor W'=W' plus an odd four-dimensional irreducible would contradict irreducibility of B tensor C. Thus C is the other faithful two-dimensional representation W and Sym^2 C=U. The group is perfect, so its determinants and one-dimensional characters are trivial. This verifies the needed type mismatch without a selected source evaluation.

For either faithful two-dimensional representation C of the binary icosahedral group, Sym^4 C is the unique five-dimensional representation and Sym^5 C is the irreducible six-dimensional representation. Sym^2 B=1 direct-sum 5, and

Hom_I(6,C)=0, dim Hom_I(6,5 tensor C)=1.

These identities follow directly from the character table in the appendix of Horrocks-Mumford (1973); they do not use the actual source matrix. The five-times-two tensor product consists of the six-dimensional representation plus a four-dimensional irreducible. The canonical SL2 contraction Sym^5 C tensor C* -> Sym^4 C is nonzero, and therefore realizes the unique channel.

## 5. Exact rank-two normal derivative everywhere

By the representation types checked in Section 4, Section 3 forces H(v) to have zero component in 1 tensor C and nonzero component in 5 tensor C. By multiplicity one it is a nonzero scalar multiple of the canonical contraction channel, after invariant identifications. For every nonzero r in C*,

v -> H(v)r : Sym^5 C -> Sym^4 C

is surjective, of rank five. This is the universal directional derivative on binary quintics: in coordinates with r evaluating one variable, its kernel is the fifth power of the other variable. It is not a selected actual evaluation. Over P(C*) its kernel is the line subbundle O(-5) of 6 O.

The exact beta radical incidence has equations z=0 and H r=0 after its skew-coordinate shear. At H=0 the projective radical direction contributes one unconstrained tangent dimension. The three even variables are killed by dz, and the six odd variables have a one-dimensional kernel by the preceding paragraph. Hence the actual incidence tangent space at every point over k has dimension two.

Near every point of the rank-nine line, the projective annihilator incidence is scheme-isomorphic to the maximal-minor rank-drop scheme in P(A): a unit nine-by-nine minor solves the normalized annihilator coordinates uniquely, leaving precisely the residual maximal-minor equations. Therefore the actual primary evaluation rank-drop scheme has tangent dimension two at every point of each of the twenty-five lines.

Equivalently, its intrinsic first-normal derivative along such a line has rank exactly two, not three, everywhere. In particular the rank-drop scheme is NOT cut transversely as a reduced smooth line by its three residual entries. This does not determine whether it is a thickened curve, a singular curve, or lies on a surface component; no normality conclusion follows.

## 6. Transverse tangent line bundle

The kernel in the odd k-variation is O(-5). Forgetting k is the scheme isomorphism just proved, so the rank-one quotient of the rank-drop tangent bundle along L by T_L is also O_L(-5). Thus the intrinsic normal-derivative kernel fits

0 -> O_L(-5) -> N_(L/P4)=3 O_L(1) -> Image(delta) -> 0.

This is a global line-subbundle assertion, not only a count at general points. In particular Image(delta) has rank two and degree eight. If K is the rank-three kernel of the Euler-quotient evaluation E=3Q(-1) -> 10 O along L, then deg K=-9 and the cokernel of delta:N_(L/P4)->K* is a line bundle of degree one, hence O_L(1).

Define T_[D,L] as the constant-rank kernel of the linearized defining equations along L, equivalently Hom_(O_L)(Omega_D tensor O_L,O_L). Then 0 -> T_L=O_L(2) -> T_[D,L] -> O_L(-5) -> 0. Its extension class belongs to H^1(O_L(7))=0, so T_[D,L] splits as O_L(2) direct-sum O_L(-5). This notation deliberately does not mean the ordinary restriction of the tangent sheaf Hom_(O_D)(Omega_D,O_D), which need not commute with restriction. No smoothness is inferred.

These are first-order statements. Higher normal jets and the dimension/reducedness of the full rank-nine degeneracy scheme remain unresolved.

## Sources and boundaries

BHM, Shioda's Modular Surface S(5) and the Horrocks-Mumford Bundle, Sections 3.4, 4.2, 4.3 Lemma 9, 4.5 Proposition 9:
https://mathweb.tifr.res.in/Documents/Publications/Studies/Vector-Bundles-On-Algebraic-Varieties.pdf

Horrocks-Mumford, A Rank 2 Vector Bundle on P4 with 15,000 Symmetries (1973), Lemma 3.3 and appendix character table:
https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf

All assertions use the pinned PR562 and PR561 interfaces and the full-normalizer decompositions stated in Section 4. The representation-type derivation was independently checked before the continuation was asserted. No theorem about the original fixed coefficients, Q4, residual Rao transversality, higher lifting, or algebraicity is claimed.
