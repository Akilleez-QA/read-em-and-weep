# Square-zero Koszul representatives for the determinantal quotient

Let S=C[x_1,...,x_5], D=Fitt_0(H), Q=S/D, and m=Q_{>0}. Use the Hilbert function and quartic initial degree proved in PR495/497, and the resolution family in PR503 refined by PR546. Write k for the resolution parameter, not the residue field.

## 1. A direct chain-level vanishing

The pinned Hilbert function of Q is (1,5,15,35,35,3); hence m^6=0. Its defining ideal has initial degree four. Consequently every positive Koszul homology group satisfies

Tor_i^S(Q,C)_j=0 for j<i+3, i>=1.

This follows either directly from the pinned resolution or from minimality: first syzygy generators have degree at least four, and each subsequent nonzero differential has entries in the homogeneous maximal ideal.

Let K=Q tensor exterior(C^5) be the Koszul differential graded algebra, with each exterior generator of homological and internal degree one. Choose a bihomogeneous C-basis h of H_{>0}(K), and homogeneous cycle representatives z_h. If h has bidegree (i,j), every coefficient of z_h has polynomial degree j-i>=3. Thus z_h belongs to m^3 K. For every pair h,h',

z_h z_h' belongs to m^6 K=0.

This is zero as a chain, not merely a boundary. Define a Massey-operation system by mu(h)=z_h and mu(h_1,...,h_n)=0 for n>=2. The defining differential equations hold: for length two their right side is a product z_h z_h'=0; for longer lengths every term contains an operation of length at least two and is zero. All values belong to mK. This is a simultaneous trivial Massey operation. Therefore Q is Golod. Independently, Herzog–Ahangari Maleki Theorem 2.1 applies directly with I=D and J=(x_1,...,x_5)^3: D is contained in J, J^2 is contained in D because Q_{>=6}=0, and the natural positive Tor maps from Q to S/J are zero because the chosen representative coefficients lie in J. This verifies the Golod conclusion without relying on a mere binary-homology-product test.

In particular, this proves more than the vanishing of the product on positive Koszul homology: a single homogeneous choice makes every pairwise representative product vanish identically, and all higher defining operations may be chosen zero.

## 2. The infinite residue-field resolution

The Golod equality gives

P_C^Q(t)=(1+t)^5 / (1-t(P_Q^S(t)-1)).

From the pinned S-resolution,

P_Q^S(t)=1+35t+(107+k)t^2+(160+k)t^3+110t^4+23t^5.

Hence

P_C^Q(t)=(1+t)^5 /
 [1-35t^2-(107+k)t^3-(160+k)t^4-110t^5-23t^6],

where k is in {15,25,35}. This determines the entire residue-field Betti sequence conditional on the remaining k choice. For example its first terms are

1, 5, 45, 292+k, 2275+6k.

The coefficient recurrence for n>=6 is

b_n=35 b_(n-2)+(107+k)b_(n-3)+(160+k)b_(n-4)+110 b_(n-5)+23 b_(n-6).

The Golod denominator is an equality, not just Serre's upper bound. It also shows that the unresolved comparison changes genuinely infinite homological data: b_3=292+k is respectively307,317,327. No particular value is selected.

## 3. General structural scope and limitations

The same direct argument works for any standard graded quotient A=S/J with initial degree d>=2 and A_{>=2d-2}=0: all positive Koszul classes have representative coefficients in m^(d-1), so their products are zero as chains. Here d=4 and Q_{>=6}=0 are exactly sufficient.

The result concerns the Koszul algebra Tor^S(Q,C) and the residue-field resolution over Q. It does not imply triviality of products in the different derived-intersection algebra Tor^P(A,B), nor does it assert geometric higher-order unobstructedness, source-instance rank, flatness, or algebraicity. It does not choose either remaining actual comparison channel in PR503. No selected source coefficients, matrices, ranks, or computation were used.

## Sources and dependencies

- PR495, Hilbert function: https://github.com/Akilleez-QA/read-em-and-weep/blob/b972aa22b72658b419e2c8948a56e0eec7f59e13/research/hm/fitting-thickening/PROOF.md
- PR503, resolution family: https://github.com/Akilleez-QA/read-em-and-weep/blob/c56c902d227f6205cf132897dd66cf2070f05b4a/research/hm/determinantal-resolution-constraints/PROOF.md
- PR546, surviving k values: https://github.com/Akilleez-QA/read-em-and-weep/pull/546 at e5f7b60a39ee01ae26a14e14dd39bd87af0ebfe3.
- Herzog and Ahangari Maleki, Koszul cycles and Golod rings, https://arxiv.org/pdf/1701.06738, introduction for the Golod equality and Theorem 2.1 for the square-zero ideal/Tor-map criterion. The chain argument above is given explicitly rather than inferred from vanishing binary products alone.

Authored proof candidate, conditional on pinned inputs; requires independent review. Not formally checked.
