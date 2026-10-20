# The exceptional C5 stabilizer does not improve the local 25 bound by itself

## Result and precise scope

At a point of the exceptional orbit M600, the following local information is compatible with an auxiliary (1,1,5,5) complete intersection of length exactly 25:

- the actual tangent representation of its order-five stabilizer;
- the actual character multiplicities of the source and target fibers;
- residue rank nine and generic rank fourteen;
- an equivariant kernel line with the character of the tautological square;
- the universal vanishing of the normalized derivative on that kernel line;
- an isolated, indeed reduced, rank-at-most-nine locus.

An explicit model is given below. Consequently no improvement of 25 can follow from these data alone, including congruences for stabilizer-equivariant local lengths. This is a countermodel for a local representation-theoretic inference, NOT a construction of the original globally linear cyclic operation. Additional cyclic identities involving the other five kernel directions remain a possible source of an improvement.

The same model distinguishes the auxiliary complete-intersection length 25 from determinantal stalk length 1. Confusing these lengths cannot justify a stronger orbit contribution.

## 1. The universal normalized derivative loses one column

Write b_u(xy)=f(x,u,y). Let p=[u] have rank b_u=9, K=ker b_u, C=coker b_u. The first derivative followed by projection to C gives the intrinsic map

    dbar b_p : T_p P(V) -> Hom(K,C),

with the usual tautological-line twists understood. Because f is cyclic-zero and outer-symmetric,

    b_u(u²)=0,
    (d b)_v(u²)=f(u,v,u)=-2f(u,u,v)=-2b_u(uv).

Thus dbar b_p(v)(u²)=0 for every tangent direction v. Since dim K=6 and dim C=11, the effective normalized derivative is an 11-by-5 matrix of linear forms, not an unrestricted 11-by-6 matrix.

This fact alone does not force its maximal minors to have a common zero on a general two-dimensional tangent slice. The model below demonstrates this explicitly, even equivariantly at M600.

## 2. Fiber characters at M600

Let H=C5 be the projective stabilizer. Its nonzero-cocycle generator has a monomial five-cycle lift on V. Choose its order-five scalar normalization and normalize the eigenvalue of the point line to one. Then V is the regular H-representation R5, the point line is its weight-zero line, and tangent coordinates transform with the four nonzero weights 1,2,3,4 modulo five.

The fiber of O(-1) tensor Sym²V has three copies of each H-character: Sym²R5=3R5. The point-line twist does not change these multiplicities.

The actual target J has four copies of each character. Here is a derivation using the standing identities Λ²V=A tensor W_h and J=A* tensor Sym³W_h from ../../rank-four/rank-four-canonical-conic-exclusion/POINTWISE_ADDENDUM.md. At every nonidentity power of the chosen generator, V has trace zero, so Λ²V also has trace zero. The two eigenvalues on W_h are fifth roots of unity, whose sum cannot vanish; hence A has trace zero at each such power. Since dim A=5, A is regular on H. Tensoring its dual with the four-dimensional Sym³W_h gives J=4R5 on H. Any scalar normalization shifts all character labels and leaves regular multiplicities unchanged.

Therefore the source and target character multiplicities used next match the actual fibers, rather than arbitrary substitute representations.

## 3. Explicit equivariant local model

Work in the regular local ring

    R=C[x1,x2,x3,x4]_(x1,x2,x3,x4).

The generator acts on points by xi -> ζ^i xi, i=1,2,3,4. Equivalently, the usual left action on coordinate functions has weights -i; all formulas below use the stated point-action covariance convention. Give R5 a basis e_j, j modulo five, with weight j. Let S_i(e_j)=e_(j+i). Thus S_i has conjugation weight i.

Take the effective kernel and cokernel fibers to be

    K'=R5,
    C=R5 direct sum R5 direct sum 1.

Define the 11-by-5 residual matrix

    D(x) = [ x1 S1 + x2 S2 ]
           [ x3 S3 + x4 S4 ]
           [       0       ].

This is equivariant because D(gx)=g_C D(x) g_K'^{-1}. Its entries span the full maximal ideal m=(x1,x2,x3,x4): the permutation supports of S1 and S2 are disjoint, as are those of S3 and S4.

Let A9 have weight multiplicities one in weight zero and two in each nonzero weight. Set

    E=A9 direct sum K' direct sum 1,
    F=A9 direct sum C,

and define B:E tensor R -> F tensor R by the identity on A9, D on K', and zero on the last trivial summand. Then

    dim E=15,  E=3R5;
    dim F=20,  F=4R5.

At the origin B has rank nine. Its kernel is K' plus the distinguished trivial line, and its cokernel is C. It has rank fourteen generically, and the distinguished line is an exact kernel line everywhere.

Moreover I10(B)=I1(D)=m. Thus its rank-at-most-nine determinantal scheme is precisely the reduced origin, of local length one.

## 4. Actual minor choices attain length 25

Because the identity block has size nine, every entry of D is a ten-minor of B up to sign. In particular choose

    f=x2,  g=x4.

Likewise the determinants of either five-row square block of D are fourteen-minors of B. Choose

    h=det(x1 S1+x2 S2),
    k=det(x3 S3+x4 S4).

Modulo (f,g), these become x1^5 and x3^5 respectively: each S_i is a five-cycle permutation matrix and has determinant one. Hence

    R/(f,g,h,k) = C[x1,x3]_(x1,x3)/(x1^5,x3^5),
    length R/(f,g,h,k)=25.

All four equations are members of exactly the required local minor ideals. Their orders are (1,1,5,5), they form a parameter regular sequence, and the lowest-order residual matrix has full column rank at every nonzero point of the slice x2=x4=0. The model therefore attains, rather than merely approaches, the lower bound underlying the support estimate 784.

The parameter ideal here is itself H-stable: f and g are eigenvectors and h,k are invariant, since every monomial in their determinant expansion has weight zero modulo five. Thus even imposing local equivariance on the auxiliary parameter ideal does not force its length above 25 at M600. No equivariant choice of the global complete intersection is asserted.

## 5. Moving kernel and the unresolved extra hypothesis

The exact constant kernel line in this model is locally equivalent to the moving tautological-square line. Write V=Cu direct sum T. The invertible linear change P(x) of V sending u to u+x and fixing T induces an invertible change Sym²P(x) of Sym²V. It satisfies P(gx)=gP(x)g^(-1), varies equivariantly with x, and sends u² to (u+x)². Here the normalized point-line fiber is trivial, and the source identification E≅Sym²V is chosen equivariantly with its distinguished line identified with Cu². A corresponding change of source frame makes the model annihilate that moving square line. Since the change is invertible and equals the identity at the origin, all determinantal ideals and the normalized derivative on K are unchanged up to their natural identifications.

This modification need not preserve linearity of all matrix entries in the original fixed source frame. More importantly, we have not shown that its other entries arise from an outer-symmetric cyclic-zero trilinear map. The model must not be cited as an example satisfying the full operation hypotheses, repeated-input injectivity, or global normalizer equivariance.

Possible remaining routes include additional cyclic-operation constraints on the induced map

    T_p P(V) tensor (K/Cu²) -> C,

higher-order cyclic identities, fixed-frame global linearity, repeated-input injectivity, or full-normalizer/global constraints. These are not represented by this countermodel. A stronger multiplicity bound need not arise from a first-derivative restriction: higher-order conditions can also change intersection multiplicities. Stabilizer weights, tangent weights, the forced square kernel, and isolated determinantal support alone are insufficient. The model gives a concrete test object for any claimed purely local-character proof: such a proof must either admit this length-25 model or identify the extra hypothesis it violates.

## Evidence boundary

Only symbolic finite representation and local matrix calculations were used. No actual source coefficient, operation value, chosen rank instance, jet, or residue of the user's operation was evaluated. The local artifact is the sole write. This result does not improve the surviving support alternatives; it rigorously closes off one proposed way of removing the 600-point alternative without additional hypotheses.
