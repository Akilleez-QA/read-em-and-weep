# Third negative trace twist: an exact cusp-jet presentation

This is a new symbolic presentation, not a selected-rank computation or a claim that the resulting elementary transform is balanced.

## 1. The graph center consists of the sixty reduced nodes

Use the established graph model b:J_P=Bl_Z(S_x), p:J_P->S_w finite flat of degree four, and q_w p=q_x b. The center is the regular zero scheme of the rank-two graph section and has length sixty. Both modular surfaces have twelve I5 fibers. ADHPR Proposition4.19(ii), printed page28, explicitly identifies the generic graph map E_(lambda:mu)(x) -> E_(lambda:mu)(w) as multiplication by two in the group law (the online PDF text lines2072–2092). After passage to the source and target modular normalizations this is an equality of maps of the generic elliptic curves. It extends on the smooth group loci of the semistable minimal models by the group law. A different origin or sign in the coordinate transport would replace it by [±2] followed by translation by a section, which leaves the argument below unchanged. The target here is S_w, not its singular degree-fifteen projective image; nonadjacent cusp components are disjoint in S_w.

At any cusp, label the five source components by Z/5. Their smooth group loci map dominantly to target components indexed by twice the source index (a simultaneous translation of the labels does not change this argument). Adjacent components j and j+1 therefore map to components 2j and 2j+2. These two target components do not meet in an I5 polygon. If the graph map extended at their source node, its image would belong to both closed target components: continuity on each source component forces this. This is impossible. Consequently every one of the sixty source nodes belongs to Z. Since Z has total length sixty, all these points have local length one and there are no others. Thus Z is reduced, exactly the cusp-node set.

This argument uses the multiplication-by-two graph identification and the semistable I5 models, not merely the numerical length of Z.

## 2. Exact first-jet elementary transform

Write G_3=R1 q_w*(A(-3H_w)), where A=O directsum T. The graph polarization and relative dualizing line are

 p^*H_w=b^*(4I_x+5F)-E_Z,   omega_(J_P/S_w)=O(E_Z).

Finite duality and the ordinary blowup pushforward give

 q_w*(A^dual(3H_w))
   =q_x* I_Z^2(12I_x+15F).

The higher direct image of this positive dual bundle vanishes: relative duality identifies it with the dual of q_w*A(-3H_w), which is zero by the graph blowup calculation. Relative duality has the sign

 q_w*(A^dual(3H_w))=G_3^dual(-5).

The length of O/I_Z^2 is 3 at each smooth surface point, hence 180 in total. Pushing its evaluation sequence gives the exact sequence

 0 -> G_3^dual(-5) -> E_12(15)
   -> directsum_(t a cusp) C_t^15 -> 0.                 (1)

Here E_n=q_x*O(nI_x). The displayed quotient really is killed by each reduced cusp parameter, not just a torsion sheaf of total length 180. At a node the semistable surface has local coordinates x,y with the modular parameter t=xy up to a unit. Thus t belongs to m^2 and annihilates O/m^2. Each of the five nodes in that fiber contributes three dimensions. The arrows in (1) are the actual value-and-first-derivative maps at these nodes.

## 3. Explicit split source

The twenty-five disjoint torsion sections have sum C=5I and O_C(nI) is the sum of twenty-five O_P1(-n). Positive fiber degree and duality give R1 q_*O(mI)=0 for m>0. Therefore, for n>5,

 0 -> E_(n-5) -> E_n -> O(-n)^25 -> 0.

For n=7 and n=12 these extensions split: their Ext1 groups are H1(E_(n-5)(n)) and vanish using the splittings below. The previously checked alternatives are

 E_2=O(-2)^5 directsum O(-4)^5, or E_2=O(-3)^10.

It follows, without choosing between these alternatives, that

 E_12=E_2 directsum O(-7)^25 directsum O(-12)^25,
 E_12(15)=E_2(15) directsum O(8)^25 directsum O(3)^25.   (2)

The splitting is not asserted to diagonalize the cusp-jet map. Its rank is sixty and its degree is395; (1) consequently has kernel degree215, agreeing with relative duality.

## 4. The exact remaining trace question

The trace splitting is genuine and yields

 G_3^dual(-5)=E_3(6) directsum B_3,
 B_3=(R1 q_w*T(-3H_w))^dual(-5).

Thus B_3 has rank45 and degree180. Its exact description is the trace-free direct summand of the first-jet kernel (1), with the explicitly split source (2). Equivalently, dualizing (1) gives an elementary enlargement

 0 -> E_12^dual(-20) -> G_3
   -> directsum_(t a cusp) C_t^15 -> 0,

where the last skyscraper identifications are noncanonical but their lengths and reduced support are canonical.

If Delta is the reduced divisor of the twelve cusp parameters, then multiplication by its equation gives the additional canonical sandwich

 E_12(3) -> G_3^dual(-5) -> E_12(15),

with injective arrows. This follows because the jet quotient is annihilated by Delta. It records the exact order of the cusp correction.

Determining the splitting of B_3 still requires the actual symbolic node-jet map, not just its dimensions, support, or surjectivity. In particular nothing here proves B_3=O(4)^45 or R1 q*T(-3H)=O(-9)^45. Nor does this presentation compute the separate K4 connecting map or prove H0(K4)=0.

## Inputs and source pins

The graph algebra, blowup model and relative dualizing calculation are recorded in GLOBAL-GRAPH-TRACE-BUNDLE.md, published at 83cfae3ee74dd32cdb476be617489131c115f7f3. The exact first negative trace twist is published at 41ab0df75f47e8979fdc06d9357c1c495dd0e1a4. The primary modular source/target graph and I5 geometry are ADHPR, https://arxiv.org/pdf/alg-geom/9606013, Remarks4.9–4.10, Lemmas4.14–4.15 and Proposition4.19. The E2 alternatives and Heisenberg splitting input are in ELLIPTIC-PUSHFORWARD-SPLITTING.md, with the primary normalization pinned by PR570 e5e55594ef2b99cefb81c4c02b22cb45e1ff0025.

## 5. Explicit geometric trace-pairing correction

The reduced-center proof also identifies every component of the previously abstract trace-pairing cokernel. For a source cusp node between components j and j+1, its exceptional curve E_j is P1 and has h-degree one. The map p is finite and preserves the modular parameter. Its image is therefore an integral target cusp component, and the degree formula for p^*H=h forces degree one onto that component. Thus p|E_j is an isomorphism. It meets the images of both adjacent strict source components, namely target components 2j and 2j+2. The unique target component meeting both in the I5 polygon is 2j+1. As j varies, these are all five target components, without repetition.

Since O_E(E)=O_P1(-1) for the blowup of a reduced point, the trace-pairing modification consequently has the explicit form

 0 -> T -> T^dual -> directsum_(D a target cusp component) i_D*O_D(-1) -> 0.

There are sixty summands. This is a sheaf on the smooth target modular surface, with the individual components retained separately; it is not a claim that the union is disjoint. Its twist by 3H has modular direct image C_t^15 at each cusp because H.D=1 and h0(P1,O(2))=3. This agrees with the first-jet quotient above. It does not on its own diagonalize the global elementary-transform map.

The exceptional curve occurs with multiplicity two in the modular fiber: locally t=xy pulls back to a function of order two along the exceptional divisor of the point blowup. Thus the degree-two map on the strict source component and the degree-one exceptional map with multiplicity two contribute total degree four over a general point of each target cusp component, consistently with finite flatness. The scheme-theoretic fiber must not be treated as a reduced ten-gon.
