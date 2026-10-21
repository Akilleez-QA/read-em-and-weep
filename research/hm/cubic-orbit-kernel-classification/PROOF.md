# Twelve distinct conductor kernels and the exact positive-section support

Work over C. Let V=V51, L0=O_V(1), and S=H0(V,L0), of dimension ten. Let U be the projective Heisenberg subgroup of order25 and Gamma the full polarized automorphism group. A node means one of the sixty reduced double values of the normalization. This is an authored structural proof conditional on the pinned inputs; it is not proof-assistant verification.

## Pinned dependencies

All paths and PRs refer to https://github.com/Akilleez-QA/read-em-and-weep.

- PR623, be95ac2c06a947ded324b8865a18abca577597da, research/hm/cubic-automorphisms/PROOF.md: Gamma is the actual complex-linear projective Heisenberg normalizer, with exact sequence 1 -> U -> Gamma -> SL2(F5) -> 1. It preserves L0 and acts transitively on the six eigenline pentads. Its universal eigenbasis description includes the index dilations e_i -> e_(a i), a in F5*.
- PR626, 8c25863b2c17de5c652fc2ced74163c0a6364a0a, research/hm/cubic-symmetry-deformation-strata/PROOF.md: U acts on the flags (i,j), i!=j, within each pentad by simultaneous translation of the two eigenline labels.
- PR637, a5fd5de0044a12bc7bb33f3431b1aa7eae7031b6, research/hm/cubic-equivariant-polarization-splitting/PROOF.md: pairing flags by (i,j) -> (2i-j,3i-2j) gives twelve U-orbits O_i of five nodes each, two in each pentad. The two orbits in a pentad are indexed by d=j-i in F5*/{+1,-1}. A lift J of central inversion -I in SL2(F5) preserves every one of these twelve node orbits, acting on eigenline labels as i -> a-i.
- PR639, 7ba345185284c42a385ebe4a3c225ded6d9164d2, research/hm/cubic-conductor-section-strata/PROOF.md: the actual evaluation maps E_i:S -> direct-sum_(y in O_i)(L0)_y are surjective of rank five. Their kernels K_i are irreducible five-dimensional subrepresentations of the order125 Heisenberg cover, with the same primitive central character. The two kernels belonging to any one pentad are complementary. On the conductor-gluing torus T12=(G_m)^12, the exact section equation over any C-algebra R is

      H0(V_R,L_lambda) = intersection_i ker((1-lambda_i)E_i).

  This torus has an open neighborhood T_amp of the identity on which the universal line bundle is relatively ample. Its parameters are genuine distinct marked polarization classes; its underlying scheme is constant V.

## 1. The actual transitive twelve-point action

Let X be the set of twelve U-orbits of nodes. Because U is normal in Gamma, Gamma acts on X, with U acting trivially. Thus the action factors through SL2(F5). The lift J of -I fixes every element of X by PR637. Consequently the action factors further through

    G = PSL2(F5), of order60.

For completeness, the transitivity on X is stronger than transitivity on the six pentads, and needs a separate check. Fix one pentad and choose a Heisenberg eigenbasis e_i, i in F5, with g e_i=zeta^i e_i and s e_i=e_(i+1). The index dilation D_a:e_i -> e_(a i) satisfies

    D_a g D_a^(-1)=g^(a^(-1)),
    D_a s D_a^(-1)=s^a.

It therefore normalizes the Heisenberg group and belongs projectively to Gamma. It preserves the chosen pentad and sends a flag (i,i+d) to (a i,a i+a d). Taking a=2 exchanges the two classes in F5*/{+1,-1}. Hence the pentad stabilizer is transitive on its two node orbits. Together with transitivity on the six pentads, this proves transitivity on all twelve elements of X.

These are universal basis and label identities, not evaluations of selected source coefficients or actual node coordinates. In particular they establish the action used below from the actual automorphism group, not from a proposed representation of the right dimension.

For x in X, let P=G_x. Transitivity gives |P|=60/12=5. The stabilizer B of the pentad containing x has order60/6=10, and P is contained in B. The orbit Bx is exactly the two elements of that pentad.

## 2. The only possible invariant blocks

We use the elementary finite-group fact that PSL2(F5) is simple. One can verify it without the exceptional identification with A5: its conjugacy classes have sizes 1,15,20,12,12. The nonidentity classes are respectively the involutions, elements of order3, and the two unipotent classes of order5. These sizes follow from projective centralizers of orders4,3,5,5 in SL2(F5)/{+I,-I}; the unipotent parameter has two square classes. No sum consisting of1 together with a proper nonempty selection of15,20,12,12 divides60, so no proper nontrivial normal subgroup exists.

Here is the required subgroup consequence, with all overgroup possibilities included. Suppose P <= Q <= G and |P|=5. By Lagrange, |Q| is one of

    5, 10, 15, 20, 30, 60.

Orders15,20,30 would give a nontrivial coset action G -> S_m of degree m=4,3,2 respectively. Its kernel is normal. Simplicity makes a nontrivial action injective, impossible because |S_m|<60. Thus these orders do not occur.

The number n_5 of Sylow5-subgroups divides12 and is1 modulo5, so it is1 or6. Simplicity excludes1; hence n_5=6 and |N_G(P)|=10. Every order10 subgroup containing P normalizes P, since P has index two in it. Thus N_G(P) is the unique order10 overgroup of P. In particular B=N_G(P), using Section1.

Now let C be a block for the transitive action G on X, containing x, and let Q be its setwise stabilizer. Then P <= Q and C=Qx. Indeed an element fixing x makes its translate of C meet C and so preserves C. Conversely, for c in C, transitivity supplies g with gx=c; then gC meets C and the block property forces gC=C. Consequently |C|=[Q:P]. The overgroup classification proves that a block containing x is exactly one of:

- the singleton {x};
- the two-element pentad fiber Bx;
- all twelve elements of X.

In particular there is no other two-element block and no block of size three, four, or six.

## 3. Kernel equality is such a block system

A polarized automorphism gamma supplies a linear isomorphism on S after choosing an isomorphism gamma*L0 with L0. Changing this choice only multiplies the isomorphism by a nonzero scalar, because H0(V,O_V)=C. Thus it acts unambiguously on subspaces of S. A section vanishes on O_i if and only if its transported section vanishes on gamma(O_i), giving

    gamma(K_i)=K_(gamma i),

with a consistent pushforward convention for the projective action. No coherent Gamma-linearization of L0 is being assumed. In particular no representation on a Heisenberg multiplicity space is required.

The equivalence relation i~j if K_i=K_j is therefore Gamma-invariant, and hence G-invariant on X. Each equivalence class is a block: group elements carry classes to classes, which are either equal or disjoint. Section2 classifies these blocks.

A two-element block would be the two node orbits of a pentad. Their kernels are complementary by PR639, so they cannot be equal. The full twelve-element block also contains such a complementary pair and is impossible. Every equality class is therefore a singleton:

    K_i != K_j for every i!=j.

By the pinned irreducibility, K_i intersection K_j is zero whenever i!=j. Since both have dimension five in S of dimension ten, every pair of distinct orbit kernels is complementary, not merely the six original pentad pairs. Equivalently, every combined evaluation map E_i direct-sum E_j is an isomorphism for i!=j.

## 4. Exactly twelve axes of positive sections

At a field-valued point lambda of T12, define A(lambda)={i:lambda_i!=1}. The section equation and Section3 give the complete classification:

    h0(V,L_lambda)=10  if |A(lambda)|=0;
    h0(V,L_lambda)=5   if |A(lambda)|=1;
    h0(V,L_lambda)=0   if |A(lambda)|>=2.

Thus the reduced positive-section support is exactly the union of the twelve coordinate subtori

    T_i = {lambda_j=1 for all j!=i},   each isomorphic to G_m.

They meet only at the identity. The support has exactly twelve irreducible components, pure dimension one and codimension eleven in T12. The same assertions hold after restriction to T_amp: each axis meets this open neighborhood in a nonempty irreducible open subset containing the identity. The h0=5 locus is their union with the identity removed; the h0=10 locus is just the identity.

This determines the reduced support, not an unspecified determinantal or Fitting scheme structure. It sharpens the bound of dimension at most six from PR639 to exact dimension one, and replaces the unspecified equality partition there by twelve singletons.

## 5. Finite-order consequence for any two distinct orbits

The stronger complementarity also removes the same-pentad restriction from the finite-order formulas. Let i!=j, R_n=C[t]/(t^(n+1)), k,l>=1, and vary only

    lambda_i=1+t^k,    lambda_j=1+t^l.

Write W_i and W_j for the five-dimensional evaluation targets. Use the now-proved isomorphism S -> W_i direct-sum W_j. The exact section module is

    (W_i tensor Ann_Rn(t^k)) direct-sum
    (W_j tensor Ann_Rn(t^l)).

Its C-dimension is 5 min(k,n+1)+5 min(l,n+1). The image of reduction to the ten-dimensional central section space has dimension ten if n<min(k,l), five if min(k,l)<=n<max(k,l), and zero if n>=max(k,l). In the intermediate range the image is precisely the kernel of the orbit whose ratio changes first. Over C[[t]] the section module is zero. Hence any two different orbit directions, regardless of their pentads, eventually destroy all nonzero central sections; unequal orders make the intermediate five-section stage explicit.

## Scope

The proof uses actual automorphisms, universal finite-group structure, and the pinned conductor evaluations. It performs no selected actual HM/source evaluation and no large computation. It concerns degree-one sections in the constant-underlying-scheme, U-fixed polarization family of V51. It makes no claim about a full Gamma-linearization, the full nonreduced section-jump scheme, the surface T75, higher adjoint Bocksteins, or Weil-class algebraicity.
