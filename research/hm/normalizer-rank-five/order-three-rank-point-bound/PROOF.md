# At most one order-three-stabilizer orbit in the finite rank-three locus

## Statement and inputs

Under the hypotheses of the established finite-rank-three and reflection-fixed-locus exclusions, the reduced locus Z3 contains at most one normalizer orbit of size 1000.

More precisely, for every order-three subgroup H of G=A⋊K, A=F5² and K=SL2(F5), each of its two projective fixed lines contains at most two points of Z3. If either contains any, each contains exactly two, all belonging to the same 1000-point orbit. This does not assert that such an orbit exists or exclude it.

Inputs:

- ../../rank-four/rank-three-250-plane-exclusion/ADDENDUM.md: Z3 is finite, avoids every canonical reflection plane and line, and each of its point stabilizers has order 1,3, or5. Its possible orbit sizes are 3000,1000,600.
- ../normalizer-500-point-orbits/PROOF.md, Sections1–3: for an order-three element a of the standard complement, its eigenvalue decomposition on V=T⊕W is 1,ω,ω² on T and ω,ω² on W. The normalizer of H=⟨a⟩ in K is Dic3 of order12, with central involution c and an element exchanging ω and ω². Its unique eigenvalue-one line is in the excluded 250-point orbit.
- ../../rank-four/canonical-line-rank-five-strengthening/PROOF.md: rank b≥9 at every point of P(W), the negative line of c.

We retain outer symmetry and the cyclic-zero identity for f:V³→J, global repeated-input injectivity, and b_u(xy)=f(x,u,y), with rank b=4+rank Q. Only universal tensors, small group facts, and determinantal orders are used.

## 1. A universal constant two-dimensional image on every projective line

Let U⊂V have dimension two. Choose a nonzero alternating form det on U. The universal outer-symmetric cyclic-zero trilinear tensor on U has the form

    f(x,u,y)=h(det(x,u)y+det(y,u)x),

for a linear map h:U→J (with the determinant twist absorbed by the choice of det). Equivalently the universal coefficient module is S_(2,1)U≅U⊗det U.

The map h is injective. If 0≠v∈ker h, choose w independent of v. Then

    f(v,v,w)=det(w,v)h(v)=0,

contrary to repeated-input injectivity. Put H_U=im h, a fixed two-dimensional subspace of J. For every nonzero u∈U and w independent of u, the values on uw and w² under b_u are respectively a nonzero multiple of h(u) and a nonzero multiple of h(w). Consequently

    b_u(Sym²U)=H_U  for every [u]∈P(U).

Project b to J/H_U. Since all values on Sym²U vanish in this quotient, it induces a linear matrix pencil

    B_U: O_P(U)(−1)⊗(Sym²V/Sym²U) → (J/H_U)⊗O_P(U).

At every point of P(U),

    rank B_U = rank b_u−2.

In particular Z3∩P(U) is precisely the locus rank B_U≤5.

## 2. A line meeting a canonical negative line has at most three Z3 points

Suppose P(U) contains a point p on a canonical negative line. The cited strengthening gives rank b_p≥9, hence rank B_U(p)≥7. Some seven-by-seven minor d of B_U is therefore a nonzero homogeneous polynomial of degree seven on P(U)≅P1.

At any point q of Z3∩P(U), rank B_U(q)≤5, so ord_q(d)≥2. To verify the order bound, work in the local discrete valuation ring at q and use invertible row and column operations to separate a maximal rank-r block, r≤5, from a remaining block all of whose entries vanish at q. Every seven-minor then belongs to the (7−r)th power of the maximal ideal, in particular its square. This is also the standard determinantal order inequality, independent of the chosen minor.

Thus

    2·|Z3,red∩P(U)| ≤ deg div(d)=7,

so that intersection has at most three distinct points. The statement requires only that one point of the line has rank b≥9, and has no group-action hypothesis of its own.

## 3. Order-three subgroup conjugacy and normalizers

Every order-three subgroup S of G injects into K, since A has order25. Its image is a Sylow-three subgroup H, and S is the graph of a cocycle f:H→A. Since3 is invertible in F5, the cocycle is a coboundary. Explicitly, with t=(1/3)Σ_(h∈H)f(h), the cocycle identity summed over h gives f(g)=t−gt. Conjugation by A therefore sends S to H. Sylow conjugacy in K shows that all order-three subgroups of G are conjugate.

For the chosen H≤K, its generator has no nonzero fixed vector on A: its order is3 and its minimal polynomial is x²+x+1 over F5, since an order-three matrix in SL2(F5) cannot have eigenvalue1 unless it is identity. Hence A^H=0. An element (v,k) normalizing H must have k∈N_K(H) and v fixed by H, so v=0. Consequently

    N_G(H)=N_K(H)=Dic3, of order12.

Its subgroup preserving an individual ω-eigenspace of V is C6=⟨a,c⟩, of order6: the other normalizer coset exchanges the ω- and ω²-eigenspaces.

## 4. Fixed lines and their incidence with 1000-point orbits

Write V_ω and V_ω² for the two-dimensional eigenspaces. Each is the sum of one line in T and one in W. Thus L_ω=P(V_ω) and L_ω²=P(V_ω²) each contains a point on the canonical negative line P(W). Section2 gives at most three Z3 points on each.

The central involution c acts on either line with eigenvalues +1 and−1. Its two fixed points are the T and W endpoints, both excluded from Z3. Therefore Z3∩L_ω is a free c-invariant set and has even cardinality. It follows that each intersection has at most two points.

For completeness, each 1000-point orbit contributes exactly two points to each fixed line. Take a point p on this orbit with stabilizer H, after conjugation. Its H-fixed orbit points correspond to cosets gH such that g^−1Hg⊂H, equivalently g∈N_G(H). Thus there are |N_G(H)|/|H|=4 such points, forming one normalizer orbit. The one-dimensional eigenvalue-one space cannot contain them because its point is excluded. The subgroup C6 preserving either eigenline has quotient C6/H of order2, which acts freely since the point stabilizer is exactly H. The remaining normalizer coset exchanges the two lines. Hence precisely two of the four points lie on each line.

Conversely every Z3 point fixed by H has stabilizer divisible by3. The allowed stabilizer orders 1,3,5 force its stabilizer to be exactly H. Thus all such points arise from 1000-point orbits as just counted.

If b denotes the number of 1000-point orbits in Z3, then

    |Z3∩L_ω|=|Z3∩L_ω²|=2b≤2,

which proves b≤1.

## Consequences and boundary

The existing cardinality expression sharpens to

    |Z3,red|=600a+1000b+3000c≤4000,  with b∈{0,1}.

The proof excludes two, three, or four simultaneous 1000-point orbits, not a single such orbit. It makes no assertion about local determinantal lengths, the existence of any remaining orbit, or the order-five and trivial-stabilizer cases.

No actual source operation, source input, source evaluation, external write, installation, or large computation was used. This local proof artifact is the only write.
