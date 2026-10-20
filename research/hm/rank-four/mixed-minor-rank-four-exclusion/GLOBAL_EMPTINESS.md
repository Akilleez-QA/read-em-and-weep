# Mixed minors and the point-orbit gap exclude all residual ranks at most four

## Theorem and precise additional input

Retain all hypotheses of PROOF.md in this directory, which proves dim Z4≤0. Also retain the standing image-dimension hypothesis that the span of the trilinear operation's values has dimension at least twenty. Then

    Z4=∅,
    rank Q_u≥5 at every u∈P4.

The additional image-dimension hypothesis is used only through ../heisenberg-eigenpoint-rank-six/PROOF.md and its independent audit. It holds in the standing problem because the target J3 is an irreducible twenty-dimensional normalizer representation, and repeated-input injectivity makes the equivariant operation nonzero; its linear image is therefore all J3. It must not be omitted for arbitrary operations satisfying weaker hypotheses.

Other imported input: ../normalizer-refined-point-gap/PROOF.md proves that the canonical thirty Heisenberg eigenpoints form one orbit E, and every other normalizer point orbit has at least250 points. The rank-six theorem gives rank Q∈{6,8,10} on E. All these are universal structural results, not selected evaluations.

## 1. Four nested minor systems give a zero-dimensional complete intersection

Let Lk be the span of the degree-k minors of the established linear matrix b. Thus

    Bs(L9)=Z4,   Bs(L10)=Z5,   Bs(L14)=Z9,
    dim Z4≤0,   dim Z5≤1,     dim Z9≤2.

Choose a nonzero f∈L9 avoiding every positive-dimensional irreducible component of Z5 and Z9. Since Bs(L9) is finite, each forbidden condition is a proper linear subspace, and finitely many can be avoided simultaneously. Hence

    dim(V(f)∩Z5)≤0,
    dim(V(f)∩Z9)≤1.

Choose g∈L10 satisfying both of the following finite lists of avoidance conditions:

1. It does not vanish identically on any irreducible component of the hypersurface V(f).
2. It does not vanish identically on any curve component of V(f)∩Z9.

For (1), a hypersurface component has dimension three and cannot lie in Bs(L10)=Z5. For (2), any such curve contained in Z5 would lie in V(f)∩Z5, which is finite. Thus no forbidden component lies in the base support, and g exists. These choices give a regular sequence f,g and a pure complete-intersection surface Y=V(f,g), satisfying

    dim(Y∩Z9)≤0.

Choose h∈L14 avoiding every surface component of Y. This is possible since Bs(L14)=Z9 meets Y only in finitely many points. The Cohen–Macaulay and unmixed properties of Y show that h is a nonzerodivisor. Thus V(f,g,h) is a pure curve.

Finally choose k∈L14 avoiding each component of that curve. None lies in Z9 because the curve is contained in Y and Y∩Z9 is finite. Again Cohen–Macaulayness makes k a nonzerodivisor. Consequently

    W=V(f,g,h,k)

is a zero-dimensional complete intersection of degrees(9,10,14,14), with total length

    length W=9·10·14·14=17640.

Every point of Z4 belongs to W, since all four systems vanish on Z4.

## 2. Multiplicity at every point of Z4

At p∈Z4, the local ring R=O_(P4,p) is regular of dimension four. The matrix b has residue rank at most8. The same block elimination as in PROOF.md gives the orders

    f∈m,   g∈m²,   h,k∈m⁶.

The ideal q=(f,g,h,k)R is an m-primary parameter ideal because W is zero-dimensional. Set

    q'=(f⁶,g³,h,k)R.

All generators of q' belong to m⁶, and they form a parameter regular sequence. The regular-sequence Hilbert–Samuel formula and the containment (q')^n⊂m^(6n) yield

    length(R/q') binom(n+3,4) ≥ binom(6n+3,4).

Comparing leading terms gives length(R/q')≥6⁴=1296. Powers in a parameter regular sequence multiply colengths: the elementary nonzerodivisor filtration used in PROOF.md applies successively after permuting the regular sequence. Therefore

    length(R/q')=6·3 length(R/q)=18 length(R/q),
    length(R/q)≥1296/18=72.

This is valid for every point, including points of residual rank less than four. Such lower ranks only increase the available order bounds.

## 3. The support bound and orbit contradiction

The total length of W bounds the sum of its local lengths at the subset Z4,red. Thus

    72 |Z4,red|≤17640,
    |Z4,red|≤245.

Equivariance makes this finite support N-invariant. Every orbit outside E has at least250 points, so any nonempty support of size at most245 would have to equal E. But rank Q≥6 on E, so E∩Z4=∅. Therefore Z4 is empty.

In particular every residual rank is at least five. This excludes all smaller ranks, including isolated low-rank points, and does not require any pointwise evaluation of b or Q.

## Scope

The length bound is for the auxiliary complete intersection W, not an asserted scheme length formula for a determinantal rank locus. The support argument proves the rank-at-most-four scheme empty as well: a nonzero coherent closed subscheme of projective space has nonempty support. No claim of constant rank five, or absence of ranks five through nine, follows.

The essential hypotheses remain generic rank ten and the associated dim Z9≤2 bound, decic closure dim Z5≤1, the earlier audited degree100 dichotomy used to obtain finite Z4, equivariance, and the twenty-dimensional image input excluding E. All are explicitly imported. No source tensor, coefficient, chosen input, operation value, rank instance, jet, or residue was evaluated.
