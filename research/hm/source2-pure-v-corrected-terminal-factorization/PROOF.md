# Corrected full-domain factorization and the unique separated zero graph

## Result

Retain the conditional actual source2 nonzero pure-V compatible-radical
hypotheses. Use Q3:M3→M5, j3, and the full operator Theta=Xh delta of
PR1096. Put H=ker Q3, J=ker j3, K=H∩J, V5=im Q3=3T. Let
I3=im j3 and L_Theta=Theta(H), so (F3)_T=I3⊕L_Theta.
There is a canonical isomorphism a:I3→L_Theta for which

    Theta=a j3+ell Q3          on ALL of M3.            (1)

The map ell:V5→I3 is the actual canonical terminal row of PR1094.
Its inclusion into M3 through I3 is understood in (1). The correction
a j3 is essential. This is NOT the invalid extension Theta=ell Q3
off J, nor an extension of h or Theta to a graded-module map.

Fix the genuine negative-module terminal separation

    V5=V0⊕NR5,      V0=(N0,5)_T≅2T,      NR5≅T.

Write ell0=ell|V0 and tau=ell|NR5, keeping these as actual maps. In the
nonzero-N0 mechanism the actual F5 is the graph of a unique map
 g:V0→NR5. Then

    R=0  iff  ell0+tau g=0.                            (2)

Because ell is onto, equation (2) forces tau≠0 and hence

    g=−tau^(-1)ell0.                                  (3)

Thus tau=0 forces R≠0 in the separated mechanism. If tau≠0, the zero
gate requires precisely the graph (3), and no other graph for this
fixed actual row. In contrast the existing residual-large criterion is
R=0 iff tau=0, since its F5 is the actual NR5. Neither tau, mechanism,
or incidence is selected here. These comparisons refer to the row and
subspaces belonging to the SAME retained actual object; they do not
identify tau values across distinct source instances.

There is also an actual conditional cross-block requirement. If tau=0,
then the N0 terminal projection of Q3(NR3) is detected surjectively by
ell0:

    ell0 e0 Q3(NR3)=I3.                                (4)

In particular Q3 cannot preserve the residual degree-three-to-five
block in that case. This is a consequence, not an assumption that Q
usually preserves or fails to preserve the horizontal decomposition.

## 1. Four exact inputs and scope

INPUTS.json pins complete proofs:

- PR1096 at36f7231633a84971dfd865eaf4803727f1edd73d proves the actual
  full operator, im Theta=(F3)_T, Theta(H)=L_Theta complementary to I3,
  ker(Theta|H)=ker(j3|H)=K, j3(H)=I3, and the quotient formula

      q Theta=d j3,    q:F3→F3/I3,    d:I3→F3/I3 injective. (5)

  It retains NR3⊂J and Theta(NR3)=I3, and all square-zero products
  between j3 and Theta. These are actual maps under its retained hypotheses.
- PR1094 at79b84d3b21cdbc76bb19d3a973e09981936dda32 constructs the onto
  ell:V5→I3 with Theta|J=ell Q3|J, proves Q3:J→V5 onto, and proves
  R=0 iff ell(F5)=0. Its scalar-kernel universal operator is not rerun
  or replaced with an instance test here.
- PR1072 atd03beb727c7e778026dcceb3555c899a0808e093 constructs the genuine
  terminal separation M5=N0,5⊕NR5 with N0,5=W′+2T and NR5=T.
  The inclusions and projectors commute with negative multiplication.
  It does NOT assert Q respects these projectors.
- PR1081 at411b644cdc12938c35b7fedac5bb92664bfc1a47 proves that in the
  nonzero-N0 mechanism the actual projection F5→V0 is an isomorphism.
  F5 has character2T and may be a graph into the residual T.

The residual-large incidence criterion quoted in the result is already
contained in PR1094; no new residual lift-channel restriction is claimed.
All inherited actual-source hypotheses remain. No relation between these
spaces and any separate opposite-pencil marked subspace is assumed.

## 2. A canonical correction on all of M3

For u∈H define

    a(j3u)=Theta(u).                                  (6)

This is well-defined because ker(j3|H)=K and Theta(K)=0. It is onto
L_Theta by definition; both induced maps from H/K are isomorphisms,
so a is a canonical equivariant isomorphism. No lift u of an element
of I3 is chosen as part of the map. Changing the lift by K does not
change its value.

Equations (5)-(6) imply q a=d: for any i=j3u, u∈H,
q a(i)=q Theta(u)=d j3u=d i. Therefore the full-domain operator

    D=Theta−a j3

has image in I3, since qD=0, and it annihilates H by (6). It factors
uniquely through the actual quotient Q3:M3→V5 to a map ell':V5→I3.
On J the correction term vanishes, so

    ell' Q3|J=Theta|J=ell Q3|J.

Because Q3:J→V5 is onto, ell'=ell. This proves (1) without selecting
any right inverse to Q3 and without asserting Theta=ell Q3 off J.
Indeed on H that incorrect formula would give Theta(H)=0, whereas
Theta(H)=L_Theta is nonzero.

Let p_I,p_L be the projections in the ACTUAL canonical decomposition
(F3)_T=I3⊕L_Theta. Equation (1) says more explicitly

    p_I Theta=ell Q3,          p_L Theta=a j3.         (7)

Thus the two contributions are separated by genuine image projections.
It does not identify either contribution with negative multiplication
by a polynomial or turn either operator into a module endomorphism.

## 3. The actual separated graph and its zero-gate test

Restrict the genuine terminal separation to V5, the full T-isotypical
space. Its two pieces are V0 and NR5 as above. In the nonzero-N0
mechanism let e0:F5→V0 be the actual projector. PR1081 says e0 is an
isomorphism. Its inverse defines

    g=eR (e0|F5)^(-1):V0→NR5,
    F5={v+g(v):v∈V0}.                                (8)

No arbitrary complement is selected. On this graph the actual row ell
is exactly ell0+tau g. The PR1094 criterion R=0 iff ell(F5)=0 now
proves (2) in both directions.

If tau=0 and (2) holds, then ell0=0 as well, so ell=0 on
V5=V0⊕NR5, contradicting its proved surjectivity. Thus R=0 forces
tau≠0. Both NR5 and I3 are irreducible T; a nonzero equivariant tau
is an isomorphism, and rearranging (2) gives precisely (3). Conversely
when tau≠0, that graph equation makes ell vanish on F5, so it gives
R=0 by the same criterion. This identifies a unique possible zero
incidence for the fixed row, not an actual realization of that graph.

For the residual-large mechanism PR1094 gives F5=NR5, so its criterion
is exactly R=0 iff tau=0. This old implication is recorded only to
contrast the two distinct actual embeddings. It does not transfer a
coefficient value or a nonvanishing conclusion between mechanisms.

## 4. Forced cross-block detection if tau vanishes

The actual NR3 lies in J, so (1) restricts there to
Theta|NR3=ell Q3|NR3. If tau=0, decompose the target of Q3 by the genuine
projectors: ell Q3|NR3=ell0 e0 Q3|NR3. PR1096 proves Theta(NR3)=I3.
This gives (4) exactly. In particular e0 Q3|NR3 is nonzero, and its
T-isotypical image has multiplicity at least one. It is not permissible
under tau=0 to set this off-diagonal actual Q3 block to zero.

This deduction neither proves tau vanishes nor supplies a rank of the
whole off-diagonal block. It explicitly uses, rather than assumes away,
the possibility that multiplication by Q crosses the negative-module
separation.

## 5. Exact limit of the two-generator odd action alone

The following universal FORMAL MULTIPLICITY control distinguishes the
new actual-map conclusions from a false scalar selection. It is NOT an
actual source2 module and does not model all negative arrows, h, the
geometric presentation, or the actual terminal graph.

Let E have basis (u,i,l,v1,v2,v3), let V have basis (e1,e2,e3), and work
over C[z,t]. Put

    Q(va)=ea,    Q(u)=Q(i)=Q(l)=0,
    j(u)=i,      j(i)=j(l)=j(va)=0,
    ell=(1,z,t),
    Theta(u)=l,  Theta(v1)=i, Theta(v2)=z i, Theta(v3)=t i,
    Theta(i)=Theta(l)=0,       a(i)=l.                 (9)

Here H=ker Q has basis(u,i,l); K has basis(i,l), the two marked images
are Ci and Cl, and j,Theta on H are the regular two-generator
square-zero action from PR1096. All pairwise products of j and Theta
vanish on E; QTheta=0; the combined (Q,j) rank is four; Theta has rank
two for every specialization of the formal z,t because fixed unit
minors witness it. Also Theta=a j+ell Q identically.

Give V the formal split V0=span(e1,e2), V_R=span(e3). Its terminal
restriction is t, completely free in this abstract family. Thus the
listed two-generator operator identities, ranks and marked complement
alone do not force that restriction to vanish or be nonzero. This is a
non-implication certificate for those identities only, not proof that
all choices occur in the actual geometry.

For an arbitrary formal graph g=(g1,g2), the row on it is
(1+t g1,z+t g2). Its zero equations force t invertible, since
1=−t g1; on the open t≠0 they give uniquely g1=−1/t,g2=−z/t.
This exact symbolic control agrees with Section3 and makes no evaluation
of actual source coefficients or points. Additional geometric constraints
on tau or the actual graph are not resolved by this packet.

## Reproduction

Run python verify.py and python -O verify.py. The checker authenticates
all four immutable inputs, checks the quotient/factorization dimensions
and composition types, verifies every identity and fixed unit minor in
(9) over the formal polynomial ring, and checks the graph ideal and its
unique localized solution. The actual-map and embedding arguments in
Sections2–4 are supplied by the proof, not by the abstract control.
No actual HM coefficient, parameter, direction, point, jet, matrix or
instance rank is evaluated. No actual source or mechanism is realized.
