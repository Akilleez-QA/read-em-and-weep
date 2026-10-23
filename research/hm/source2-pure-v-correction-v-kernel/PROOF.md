# The zero-fourth correction selects the exact common homotopy kernel on two V copies

## Result and scope

Retain the actual source2 nonzero pure-V compatible-radical hypotheses
and the RESIDUAL-LARGE mechanism: P_h⊂NR2 and π2(P_h)≠0 in N8,2.
Let E_V=(NR2)_V be the full actual V-isotypical space, of character2V,
and V_C the unique actual V⊂NC2. Define

    Gamma:E_V→Hom(A,I2),       Gamma(v)(a)=hT_a v,
    V_h=ker Gamma.                                      (1)

Then Gamma is nonzero on V_C and has image the unique V constituent
of Hom(A,I2). Its actual kernel V_h is one V, with

    E_V=V_C⊕V_h,       π2|V_h:V_h≅(N8,2)_V.             (2)

These are actual coefficient-space splittings selected by Gamma, not
a splitting of the entire residual negative module.

Assume additionally that the quadratic fourth lift R vanishes. Let
G:Z=im Q2→M2 be any equivariant right inverse, s:I4→P_h the canonical
inverse of Q2, and k:A⊗I4→M2 the actual first correction

    k(b⊗p)=G T_b s(p).

Let V_in be the unique V constituent of A⊗I4=V+P+D. Then

    k(V_in)=V_h,                                       (3)

and this restriction of k is independent of G. In particular the
correction has a forced NONZERO quotient projection onto (N8,2)_V;
it cannot be placed inside NC2 by choosing a different equivariant
Q-preimage.

For the genuine N0 projector e0, the same zero-fourth hypothesis gives

    V_h=ker(e0 Q2|E_V),
    Q2(V_h)=(NR4)_V,
    Gamma=chi (e0 Q2)|E_V,                              (4)

where chi:(N0,4)_V→Hom(A,I2)_V is the unique induced isomorphism.
No value of chi or of a repeated-copy coefficient is selected. Neither
R=0 nor the residual mechanism is asserted realized. This is an actual
alignment of kernels under R=0, not a proof of fourth or fifth
nonvanishing, and not a positive-coordinate comparison.

## 1. Seven immutable inputs

INPUTS.json retains complete proofs at exact commits:

- PR795: the genuine negative separation N=N0⊕NR and exact quotient
  0→NC→NR --π→N8→0, with actual commuting negative arrows. Its
  degree-two characters are N0,2=P+D, NR2=A+2V+2P+3D,
  NC2=V+P+2D, N8,2=A+D+V+P. In particular E_V contains both V copies
  of the full M2, and E_V∩NC2=V_C.
- PR1064: h(NR4)=I2=D, negative stability of NR, and in residual-large
  F4=ker h∩NR4=V+2P+D, with F4→N8,4 onto and kernel I4.
  Also NR4=V+2P+2D has a unique V.
- PR1059: in residual-large the actual quadratic descendant map
  A⊗P_h→N8,4 is an isomorphism, and F4/I4 is the actual free
  quadratic descendant quotient. No old endpoint-nine possibility
  is used in this packet.
- PR1069: ker Q2=A+I2, Q2:P_h→I4 is an isomorphism, T_b s⊂Z,
  and B(a,b)p=hT_a G T_b s(p), with diagonal R.
- PR1089: B is symmetric, so R=0 implies B(a,b)=0 for every a,b.
  It also retains Theta(z)=X_x hY_yz−X_y hY_xz on NR3.
- PR1106: T_Q=Q3(NC3)=Q3(W V_C)=W Q2(V_C) is one canonical T.
  In residual-large ell|T_Q is an isomorphism to I3. If tau=ell|NR5=0,
  the actual map e0 Q2|V_C is an isomorphism onto (N0,4)_V.
- PR1094: residual-large has R=0 iff tau=0. It proves the restricted
  factorization Theta|ker j3=ell Q3|ker j3, using the same actual
  terminal row ell and genuine residual terminal space NR5.

All actual-source hypotheses of these inputs remain. A=Sym2 W,
I2=D, I4=P, and A⊗V=P+D. No repeated V or D copies are identified
by character without an actual inclusion or map.

## 2. The actual common kernel is one V, transverse to the marked V

For v∈E_V⊂NR2, negative stability gives T_a v∈NR4, hence hT_a v∈I2.
Thus (1) is an actual equivariant map with the indicated domain and
codomain. The representation identity A⊗V=P+D implies

    dim Hom_G(V,Hom(A,I2))=dim Hom_G(A⊗V,D)=1.

Therefore Gamma is a row from the two-dimensional V multiplicity space
to one V multiplicity. Its image is either zero or that unique V.
We prove nonzero restriction to the specific marked V_C.

Suppose hT_a v=0 for every a∈A and v∈V_C. For any l∈W,

    Theta(X_l v)=X_x hT_(yl)v−X_y hT_(xl)v=0.          (5)

But W V_C⊂NC3⊂ker j3, so the actual restricted factorization gives
Theta(W V_C)=ell Q3(W V_C)=ell(T_Q)=I3 by PR1106 in residual-large.
This contradicts (5). Hence Gamma|V_C is nonzero and therefore an
isomorphism onto Hom(A,I2)_V. The full row Gamma has rank one in
multiplicity and kernel exactly one V. Its kernel meets V_C trivially,
proving the first part of (2).

The actual quotient π2 on E_V has kernel precisely V_C and image the
unique V in N8,2. Its restriction to the disjoint complementary V_h
is therefore an isomorphism, proving the second part of (2). This gives
a selected coefficient-space section on that V alone. It does not
supply a negative-horizontal section N8→NR or set a coefficient relative
to an arbitrary vector-space complement.

## 3. The corrected V channel is forced when R vanishes

For b⊗p∈A⊗I4, k is defined because T_b s(p)∈Z. It satisfies

    Q2 k(b⊗p)=T_b s(p).                               (6)

Consider the restriction to the unique V_in. The right side of (6) is
nonzero on V_in: after the actual quotient π4, PR1059 identifies the
whole map A⊗P_h→N8,4 with an isomorphism. Thus the V constituent has
nonzero image. It is the unique V of F4 and is contained in NR4.
Consequently k|V_in is nonzero and injective. Its image lies in E_V,
because the full degree-two V-isotypical part is E_V.

Under R=0, symmetry of B from PR1089 gives B=0. Its exact formula now
gives hT_a k(b⊗p)=0 for every a,b,p, so k(V_in)⊂V_h. Both are V and
the first is nonzero, proving (3).

If G is changed equivariantly, the difference of k|V_in has image in
ker Q2=A+I2=A+D. Hom_G(V,A+D)=0, so the difference is zero. The V
correction itself is therefore canonical, not merely its Q image. This
argument does not permit changes by an arbitrary nonequivariant section.
Combining (2) and (3) gives its forced nonzero N8 quotient projection.

## 4. Equality with the actual cross-block kernel

Still assume R=0 in residual-large. PR1094 gives tau=0, so PR1106
makes e0 Q2|V_C an isomorphism onto the unique (N0,4)_V. Hence
 e0 Q2|E_V is a nonzero multiplicity row with one-V kernel.
Equation (6) maps k(V_in)=V_h into F4⊂NR4, where e0 vanishes. Thus
V_h lies in that kernel; their equal dimension proves the first part
of (4). Its Q2 image is the nonzero V descendant already identified
in Section3, namely the unique (NR4)_V. The map on V_h is an
isomorphism because ker Q2 has no V.

The two actual surjections Gamma and e0 Q2|E_V have the same kernel.
They therefore induce a unique isomorphism chi between their images,
with Gamma=chi e0 Q2 on E_V. Both images are the specified unique V
constituents, proving the remaining assertion in (4). This factorization
is an actual-map equality without choosing a scalar normalization for
chi or a preferred basis of either multiplicity space.

Relative to the ACTUAL splitting E_V=V_C⊕V_h and the genuine target
V split (N0,4)_V⊕(NR4)_V, Q2 on E_V consequently has triangular
multiplicity form with nonzero diagonal and zero upper-right entry.
The lower-left entry is not determined. Matching characters alone would
not establish that zero entry or the equality of kernels; they follow
from the actual correction and R=0.

## Verification and limits

Run python verify.py and python -O verify.py. The checker authenticates
all seven inputs, verifies the full character identities and Hom
multiplicities, checks the correction types, and verifies the universal
row-kernel/triangular identities with indeterminate coefficients. Those
formal controls are not matrices of an actual HM source. The actual
nonzero marked channel and kernel alignment are proved above.

No actual coefficient, point, parameter, jet, matrix or instance rank
is evaluated. The remaining R=0 hypothesis is not decided; repeated-copy
cancellation is retained and expressed by the selected kernel V_h.
The result does not compute the new fifth class, identify V_C with any
marked positive/opposite block, or assume Q preserves NR.
