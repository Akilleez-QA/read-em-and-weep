# Exact first negative trace twist and the twist-four value target

## Inputs

Let p:J_P -> S_w be the finite flat graph cover, with algebra A=O_S_w directsum T, and b:J_P -> S_x its graph blowup at the length-sixty regular zero scheme Z. The source and target modular projections are q_x,q_w. Keep their divisor classes separate. The global graph polarization gives

    p^*H_w=h=b^*(4I_x+5F)-E_Z.

The established source splitting is

    E_4=q_x*O(4I_x)=O(-5)^5 directsum O(-4)^15,
    E_1=q_w*O(I_w)=O(-2)^5.

For completeness the E_4 derivation is self-contained. Positive degree on every elliptic-fiber component gives R1q_x*O(4I_x)=0, rank twenty. Riemann–Roch gives degree minus85. The Heisenberg center acts nontrivially and the unique irreducible representation with that central character has dimension five, so every splitting multiplicity is divisible by five. If 4I+3F were effective, its intersection minus one with each torsion section would force their full sum 5I as a component. The residual class −I+3F has negative intersection with the nef modular fiber, impossible. Hence every summand has degree at most minus four. Writing four degrees a_j with sum minus17 therefore forces one minus5 and three minus4, each repeated five times. This proves the displayed E_4 splitting. Likewise E_1 has rank five, degree minus10, and Heisenberg multiplicity five, hence O(-2)^5. The primary normalization inputs are pinned by PR570 at e5e55594ef2b99cefb81c4c02b22cb45e1ff0025; the splitting is the explicit deduction above, also recorded in ELLIPTIC-PUSHFORWARD-SPLITTING.md.

## 1. An exact split negative twist

On the graph blowup, b_*O(E_Z)=O and its higher direct image vanishes, because the exceptional quotient is the relative O(-1). Therefore

    Rb_*O_J_P(-h)=O_S_x(-4I_x-5F).

Relative duality with omega_(S_x/P1)=O(5F) now gives

    R1 q_w*(A(-H_w))=E_4^* tensor O(-10)
                   =O(-5)^5 directsum O(-6)^15.

Its degree-zero direct image vanishes. The trace decomposition splits off

    R1 q_w*O(-H_w)=E_1^* tensor O(-7)=O(-5)^5.

The trace splitting is a genuine direct sum in the derived pushforward, not merely a short exact sequence. By uniqueness of the multiset of line-bundle summands on P1 (Krull–Schmidt/Birkhoff–Grothendieck), removing the five O(-5) summands forces the remaining fifteen summands to be O(-6). Thus it proves the new exact identity

    R1 q_w*(T(-H_w))=O(-6)^15,
    q_w*(T(-H_w))=0.

Equivalently, relative duality gives

    q_w*(T^dual(H_w))=O(1)^15.

This conclusion concerns the dual trace bundle in the positive twist. It does not replace T by T^dual across cusps.

## 2. Exact presentation of the twist-four value target

Let Y in |2H_w| be the target quadric-section curve. The actual twist-four value target on the modular line is

    V_4=q_Y*(T|Y tensor O_Y(12F-H_w)).

Both degree-zero direct images of T(-H_w) and T(-3H_w) vanish. This follows by viewing each as a trace summand of A(-dH_w): b_*O(dE_Z)=O, so q_w*A(-dH_w)=q_x*O(-4dI_x-5dF)=0. This avoids an unjustified negative-ample argument on nonreduced cusp fibers. The quadric restriction sequence consequently gives the exact sequence

    0 -> V_4 -> (R1 q_w*T(-3H_w))(12) -> O(6)^15 -> 0.

Since the end terms are bundles on P1, the sequence also proves that its middle term is locally free. The first middle bundle has rank45 and degree135; V_4 has rank30 and degree45. In particular the quotient is the explicitly split rank-fifteen bundle O(6)^15, not an unspecified bundle of the same degree.

The map is the actual multiplication/restriction map of the chosen quadric. Its source splitting has not been determined. This presentation alone neither computes the splitting of the rank25 degree-minus65 value-map kernel K4 nor proves that it has no global sections.

## 3. Euler check for all negative twists

For d>=1, b_*O(dE_Z)=O and the exceptional contribution to Euler characteristic is minus60 binom(d,2). Riemann–Roch on S_x then gives

    χ(O_J_P(-d h))=5+30d²+60d,
    χ(T(-dH_w))=15d(3d+7)/2.

For completeness the first direct images are locally free: choose a general finite-flat hyperplane section of S_w over the modular line, and apply its restriction sequence inductively, starting with the proved relative acyclicity of T. Each step expresses R1q_w*T(-(d+1)H_w) as an extension of R1q_w*T(-dH_w) by the finite pushforward of a vector bundle on that hyperplane section. The generic graph fibers have h-degree20 and genus one, so A(-dH_w) has first direct-image rank20d. Removing the rank5d structure-sheaf summand gives

    rank R1q_w*T(-dH_w)=15d,
    deg R1q_w*T(-dH_w)=−15d(3d+9)/2.

For d=1 this is rank15, degree minus90, agreeing with O(-6)^15. For d=3 it is rank45, degree minus405, giving degree135 after twisting by O(12), as used above.

No selected HM coefficients or rank evaluations are used. PR1 coordination was read through comments6316852300 and6317063542: the remaining actual gate is H0(K4)=0, and the independent primary Picard lane is not used here.
