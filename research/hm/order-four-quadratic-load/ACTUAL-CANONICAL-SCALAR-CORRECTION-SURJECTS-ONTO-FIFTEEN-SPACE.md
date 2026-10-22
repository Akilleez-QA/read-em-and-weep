# The actual canonical scalar correction surjects onto the fifteen-space

## Result

Let Q:D5 O_L->V O_L(2) be the ACTUAL quartic quotient, with kernel Wprime O_L(-3). The canonical global scalar correction in the third-operator calculation is

    Q(u(a,h))=k a Lie_(D_a)(Qh).

It factors through S=a^2 in Sym^4 W=D5. As a bilinear map in the positive quartic h and the negative quartic S, it is surjective:

    D5_positive tensor D5_negative -> H0(D5 O_L(2)).   (1)

The target has dimension15 and character A+V+P4+D5. Every target channel is nonzero; the kernel has character 1+P4+D5 and dimension10. This is a geometric proof for the actual correction map, without evaluating actual coefficients or matrix ranks.

This determines a further actual factor in the normal cochain. It does not prove the resulting full third-Bockstein composite nonzero: the cochain also contains the actual quintic-extension terms and the final second-symbol quotient.

## 1. Intrinsic quartic Gaussian form

Use the first negative transvectant (S,q)_1=S_s q_t-S_t q_s. For deg S=4, deg q=2, and S=a^2,

    (1/2)(S,q)_1=a D_a(q).

Equivalently on z=t/s this equals 2S q_z-S_z q. The actual scalar formula therefore is

    Q(u(S,h))=(k/2)(S,Qh)_1.                       (2)

The actual map H0(D5 O2)->H0(V O4) induced by Q is an isomorphism. It remains to prove surjectivity of the Gaussian map on the right of (2).

## 2. The second fundamental map of the actual quotient

Write K=ker Q=Wprime O(-3). Since D5 O has its trivial connection, the second fundamental map of K is intrinsically

    B:K -> (D5 O/K) tensor Omega_L^1 = V O.

In a local affine frame it is, up to an overall sign, Q_z restricted to K. Its definition is independent of local line connections because Q annihilates K.

The map B is nonzero. If it vanished, the classifying map L->Gr(2,D5) for the kernel subbundle would have zero derivative in characteristic zero and hence would be constant. Then K would be a trivial degree-zero subbundle, contradicting deg K=-6.

Its generic rank cannot be one. Otherwise its saturated image in V O would be an equivariant line O(-d), with d>=0. A nonzero map Wprime O(-3)->O(-d) requires

    Hom_G(Wprime,Sym^(3-d) W) nonzero,

with 0<=d<=3. But Sym^j W for j=0,1,2,3 is respectively 1,W,A,S4, none containing Wprime. The equivariant line has the standard linearization: the binary icosahedral group has no nontrivial character. Thus B has generic rank two.

Any rank-drop point is a common zero of its maximal minors, which are components of a section of V O(6). At least one minor is a nonzero degree-six form. The rank-drop scheme is invariant, while every orbit on the faithful icosahedral projective line has at least twelve points. Therefore there are no rank-drop points. Consequently

    0 -> Wprime O(-3) --B--> V O -> O(6) -> 0,       (3)

and its dual has kernel O(-6). This argument is a uniform geometric rank proof, not a matrix evaluation.

## 3. The apolar adjoint has zero kernel

Put the invariant symmetric forms on V and on the negative quartic representation Sym^4 W. Their tensor product identifies the dual of H0(V O4) with another copy of that space.

For a fixed negative quadratic q, the first-transvectant operator S->(S,q)_1 is an sl2 action on quartics and is skew-adjoint for the invariant apolar form. Thus an element z in H0(V O4) annihilates the Gaussian image if and only if, for every h,

    sum_v (z_v,(Qh)_v)_1=0.

In an affine frame, expanding degrees4 and2 gives exactly

    Q^t z_z-2(Q_z)^t z=0.                           (4)

Multiply (4) by the transpose of the kernel inclusion K->D5 O. The first term vanishes, and the second says

    B^t z=0.

Dualizing (3) and twisting by4 identifies this kernel with O(-2). Hence z belongs to H0(O(-2))=0. The apolar adjoint is injective, proving Gaussian surjectivity, and then (2) proves (1).

This proof retains the actual complete cubic quotient Q. It does not argue that arbitrary nonzero maps must compose nontrivially.

## 4. Channel bookkeeping and scope

The source character is

    D5 tensor D5=1+A+V+2P4+2D5,

whereas the target is

    D5 tensor A=A+V+P4+D5.

Surjectivity therefore gives kernel 1+P4+D5. In particular both the antisymmetric A and V source channels contribute, while the repeated P4 and D5 source combinations require their actual normalization and are not assigned a guessed ratio.

The canonical scalar is thus no longer only known to exist uniquely: its full fifteen-dimensional image is proved. This does not cancel or evaluate the f-linear local extension correction in the canonical vector cochain R.

## Dependencies and verification

Use POSITIVE-SERRE-RESIDUE-AND-CANONICAL-CONE-OPERATOR-CORRECTION.md for the actual quotient and inverse; ACTUAL-POSITIVE-ATIYAH-MULTIPLICATION-SURJECTS-ONTO-NINE-SPACE.md for the actual residue formula; and ACTUAL-CONE-DIAGONAL-IS-CANONICAL-RESIDUE-INVERSE.md for (2) with its fixed determinant convention.

The companion verifier checks the universal Hamiltonian/transvectant and apolar-adjoint identities, representation arithmetic, and degree calculations. The geometric rank proof in Section2 is symbolic and uniform; no actual HM coefficients or actual-instance rank calculation is used.
