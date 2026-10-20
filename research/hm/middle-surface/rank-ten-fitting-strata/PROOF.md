# Rank-ten singularity sheaf and quadratic-fiber strata

Assume the hypotheses and conditional generic-rank-ten conclusion of `/research/hm/normalizer-rank-five/quintic-normalizer-exclusion/COROLLARY.md`. Thus on X=P^4 there is an exact sequence

    0 -> G -> O^20 -> R -> 0,

where G is locally free of rank fourteen and R is torsion-free of rank six. The normal quadratic map Q has ranks ten and sixteen. Let Z be its rank-drop locus, with its maximal-minor scheme structure. Put S=Ext^1_X(R,O_X).

## 1. Exact singularity invariant

Dualizing gives

    0 -> R* -> O^20 -> G* -> S -> 0,
    Ext^i_X(R,O_X)=0 for i>=2.

The support of S is exactly the non-locally-free locus of R, and exactly Z set-theoretically. In fact

    Fitt_0(S)=I_Z.

To check the equality of ideals, locally split off the rank-four subbundle A that lies in the image of G -> O^20. Its inverse image in G is a subbundle: the map from that inverse image to A is an isomorphism, and the quotient G/A is locally free. The resulting remaining injection is the rank-ten-to-sixteen presentation Q. The transpose of Q presents S, so its maximal minors generate Fitt_0(S). Equivalently, direct block elimination identifies these with the rank-fourteen minors of G -> O^20.

For a geometric point u let delta(u)=10-rank(Q_u). Right exactness of tensoring the presentation of S gives

    dim_C(S tensor k(u)) = delta(u).

The higher rank-drop schemes satisfy

    {rank Q <= 10-j} = V(Fitt_(j-1)(S)),   1<=j<=10,

where each equality uses the usual determinantal scheme structures.

At a nonfree point p of ambient codimension c, the local projective dimension of R_p is exactly one: it is at most one from the bundle presentation and cannot be zero. Auslander-Buchsbaum over the regular local ring O_(X,p) therefore gives

    depth(R_p)=c-1.

Thus codimension-two nonfree points are precisely the obstruction to reflexivity: R is reflexive if and only if Z has codimension at least three. The already proved torsion-freeness allows codimension-two singularities and does not eliminate them.

At the generic point of a codimension-two component, R** is free. If T=R**/R there, then

    S_p = Ext^2(T_p,O_(X,p)).

Local duality on the regular local surface shows that S_p and T_p have equal finite lengths. Hence the codimension-two cycle of S records exactly the failure of R to equal its reflexive hull.

## 2. Fiber dimension forces substantially deeper rank drop

Let B_u be the reduced projective base locus of the quadratic system at u. Under the second Veronese embedding it lies in P(ker Q_u), a projective space of dimension delta(u)-1.

If B_u contains an integral k-dimensional subvariety Y, the span of its Veronese image has dimension at least binom(k+2,2)-1. Here is an elementary proof. Choose k+1 linear forms on the projective span of Y that give a finite dominant linear projection Y -> P^k (a linear Noether normalization of its homogeneous coordinate ring). The polynomial algebra on these forms injects into that ring; its degree-two piece has dimension binom(k+2,2). Consequently h_Y(2)>=binom(k+2,2), which is exactly the required lower bound for the Veronese span.

It follows that

    delta(u) >= binom(k+2,2).

In particular:

- A positive-dimensional base locus requires rank(Q_u)<=7.
- A base locus containing a surface requires rank(Q_u)<=4.
- A three-dimensional base locus would require Q_u=0 (and is independently excluded by the existing flag geometry).

These implications hold without any generic-rank assumption; rank ten is used only for the global exceptional-set bound and the singularity-sheaf interpretation above.

At rank nine, B_u has at most one geometric point. At rank eight, it has at most two geometric points. Indeed three distinct points of a quadratic Veronese variety cannot be collinear: if their original points are linearly independent their squares are linearly independent; if they are collinear, their squares lie on a smooth plane conic and remain linearly independent. Thus a projective line meets the Veronese variety in at most two geometric points.

Consequently, over the open rank-at-least-eight locus the projective quadratic incidence is finite over its image. Any contracted positive-dimensional eigenline-boundary fiber described in `../spectral-eigenline-contraction/PROOF.md` lies over rank at most seven; any two-dimensional such fiber lies over rank at most four.

## Limits

The results identify the exceptional locus through a coherent Ext sheaf and separate its higher-dimensional fibers by strictly deeper Fitting strata. They do not prove codimension at least three for Z, do not exclude a two-dimensional exceptional image, and do not promote R to a vector bundle.
