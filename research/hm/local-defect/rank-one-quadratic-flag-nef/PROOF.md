> Publication scope: preserved mathematical proof/audit. Historical statements that rank eight remains open are superseded only after the final assembly and all its prerequisites. No source-instance evaluation or formal verification is claimed here.

# The quadratic flag incidence is at most three-dimensional: the rank-one component exists

## Result

Assume the structural hypotheses and established results of ../rank-one-normal-obstruction/PROOF.md: dim V=5, dim J=20, the canonical trilinear operation f with outer reversal and cyclic zero, and two-plane injectivity. Then:

1. The projective incidence of nonzero zeros of the normal quadratic obstruction Q_u has dimension at most three.
2. Its image in P(V)=P^4 is a proper closed subset. For every line outside this subset, Q_u has no nonzero zero.
3. Consequently the rank-at-most-one determinantal cone D is an irreducible component of the full cubic zero scheme. Its generic multiplicity lies between five and sixteen, its generic maximal ideal has fifth power zero, and that scheme is nonreduced at every point of D.
4. The all-inputs-nonzero rank-one points lying in the closure of independent zero triples form a subset of dimension at most six, inside the seven-dimensional rank-one stratum.
5. Together with the established coordinate-component and independent-zero results, the full zero scheme has at least five irreducible components.

This settles the rank-one component alternative structurally. It does not determine the exact generic multiplicity or whether the exceptional quadratic incidence is empty. No actual matrix, operation value, rank, selected input, polynomial instance, residue, or jet is evaluated.

## 1. Exact global bundles

Let X=P(V), with tautological line L=O_X(-1), and put U=(V tensor O_X)/L. Write h=c1(L*). Structural repeated-input injectivity gives a vector-bundle injection

    A: L^2 tensor U -> J tensor O_X,
    u^2 tensor vbar -> f(u,u,v).

Its cokernel C is locally free of rank sixteen. The expression f(p,u,p), modulo the image of A, defines a global bundle map

    Q: L tensor Sym^2 U -> C.

Indeed replacing p by p+c u changes the expression by 2c f(u,u,p); the square term vanishes. Polarization gives the asserted map. This also establishes the exact base twist: Q takes values in C tensor L* when viewed as a quadratic map on U.

Let F=P_X(U), with the convention of lines, and let M=O_F(-1) be its tautological line. It is the flag variety Flag(1,2;V): its rank-two tautological subbundle P fits into

    0 -> L -> P -> M -> 0.

Pullbacks are implicit. The quadratic incidence B is the zero scheme of the section

    Q_F in H^0(F, C tensor L* tensor (M*)^2).

In particular B is projective. In what follows B is replaced by its reduced structure. Write t=c1(M*).

A direct top-Chern test for this rank-sixteen bundle on the seven-dimensional F would be vacuous. The useful extra information is the recovered three-plane on B.

## 2. The recovered three-plane is a global subbundle

Locally choose nonvanishing frames u of L and p of M, with p lifted to P. On B, the equation Q_F=0 says that f(p,u,p) lies in the image of A. The injectivity of A therefore determines a unique class qbar in V/L with

    f(u,u,q)=f(p,u,p).

Only the class of q modulo P will be needed. It is nonzero at every geometric point. Otherwise q belongs to span(u,p), and the equation contradicts the two-plane injectivity, exactly as in Section 3 of the imported normal-obstruction proof.

The transformation rule is important. If

    u'=a u,    p'=b p+c u,

with a,b invertible, then trilinearity and outer reversal give

    f(p',u',p')=a b^2 f(p,u,p)+2a b c f(u,u,p).

Consequently

    q' = (b^2/a) q +(2bc/a) p modulo L,

and hence q' modulo P equals (b^2/a) q modulo P. This is precisely the transition rule for M^2 tensor L^(-1). Thus there is a canonical bundle map

    M^2 tensor L^(-1) -> (V tensor O_B)/P

which is nowhere zero in geometric fibers. It is therefore a line subbundle: locally one entry is a unit and provides a splitting. Let W be its inverse image in V tensor O_B. Then W is a rank-three subbundle, and

    0 -> P -> W -> M^2 tensor L^(-1) -> 0.

This construction defines a morphism g:B -> Gr(3,V). In particular

    det W = (L tensor M) tensor (M^2 tensor L^(-1)) = M^3.

No choice of local lift survives in the construction. Working on the reduction suffices; alternatively the same formulas give the bundle on the original zero scheme.

## 3. Two nef classes and one ample class

The class h is nef on B because it is pulled back from the hyperplane bundle of P(V). The determinant identity gives

    (M*)^3 = g* O_Gr(3,V)(1).

Thus t is nef on B as well. This is the key property: t need not be nef on the full flag variety F.

The other projection F -> Gr(2,V) pulls back its Plucker bundle to det(P*)=L* tensor M*, of class h+t. The standard closed incidence embedding

    F -> P(V) x Gr(2,V)

therefore shows that the line bundle of class

    a = h+(h+t)=2h+t

is ample on F, and hence ample on B.

## 4. The projective-bundle relation excludes dimension four

From the tautological sequence on P(V),

    c(U)=1+h+h^2+h^3+h^4.

For the line convention P(U), the projective-bundle relation is

    t^4+h t^3+h^2 t^2+h^3 t+h^4=0.

This relation pulls back to B as an identity of operational Chern classes, so it can be intersected with cycles on singular components as well.

Suppose an integral component Y of B has dimension d>=4. Intersect the displayed identity with a^(d-4)[Y] and take degree. Every summand

    degree(h^i t^(4-i) a^(d-4)[Y]),  0<=i<=4,

is nonnegative, because h and t are nef and a is ample. This positivity may also be checked on a projective resolution of Y. Their sum is zero, so each summand is zero. Expanding (2h+t)^4 as a positive linear combination of the same five monomials now yields

    degree(a^d[Y])=0,

contradicting ampleness. Hence every component of B has dimension at most three.

Notice that the proof uses the degree-four projective-bundle relation, rather than a degree-sixteen top Chern class. The recovery of W turns all five terms in that relation into nonnegative intersection numbers.

## 5. The actual rank-one component and its boundary

The projective map pi:B -> P(V) has closed image E of dimension at most three. Thus E is proper. For each [u] outside E, the quadratic obstruction has no nonzero zero. Section 4 of ../rank-one-normal-obstruction/PROOF.md then says that the cubic zero scheme has only the rank-one locus as reduced support in a neighborhood of every all-nonzero rank-one triple on that line.

It follows that D is an irreducible component. The generic local calculation in Sections 5 and 6 of that proof supplies generic length at least five and nonreducedness at every point of D. The closure argument for the latter uses the coherent nilradical: its support contains the generic point of D and hence all of D.

Any all-nonzero rank-one point in the closure of independent zero triples must lie above E: outside E it has an open neighborhood whose reduced support is rank one. Over E, all such rank-one triples lie in the product of three punctured tautological line bundles. Its dimension is dim E+3<=6, proving the asserted boundary bound. This is an upper bound; quadratic zeros need not be integrable, and no equality is claimed.

## Limits

The proof proves generic emptiness, not total emptiness, of the quadratic base locus. It neither computes the exceptional set E nor its degree, determines a higher-order normal equation, nor calculates the exact generic length of D. It uses only the previously established two-plane injectivity and symmetries, universal bundle construction, and nef intersection positivity.

## 6. A bounded generic thickness: length five through sixteen

Let K=C(D) and let A be the local ring of the cubic zero scheme at the generic point of D, with maximal ideal m. By Section 5, A is Artinian. The exact local presentation in the imported normal-obstruction proof gives four generators for m and residual equations in m^2. Their degree-two initial forms are the components of Q over K. The projective zero locus of those quadrics is empty even after extending K algebraically: the generic line lies outside the closed image E, and emptiness persists under base change.

Thus the homogeneous ideal I_Q generated by these quadrics in S=K[p1,p2,p3,p4] is m_S-primary. Since K is infinite, four K-linear combinations q1,...,q4 of the quadratic generators can be chosen to be a homogeneous system of parameters. For example, successively avoid the finitely many relevant homogeneous associated primes at each stage; I_Q is contained in none other than the irrelevant maximal ideal. As S is Cohen–Macaulay, these four quadrics form a regular sequence. The complete intersection has Hilbert series

    Hilb(S/(q1,q2,q3,q4);z)=(1+z)^4.

There is a graded surjection

    S/(q1,q2,q3,q4) -> gr_m(A),

because every q_i belongs to the initial ideal of the residual equations. Consequently the Hilbert-function bounds are

    dim_K(m^j/m^(j+1)) <= (1,4,6,4,1)_j  for 0<=j<=4,
    m^5/m^6=0.

Nakayama gives m^5=0. The first two graded dimensions are exactly one and four, since there are no linear residual equations. Therefore

    5 <= length(A) <= 16.

This is a generic local bound only; it does not assert that all sixteen degrees occur, that the actual quadratic ideal is a complete intersection, or that the local rings at special points of D have this length.

## 7. At least five irreducible components

The established results in ../../cubic-loci/cubic-component-multiplicities/applications/four-kernel-empty-incidence/PROOF.md give three distinct ten-dimensional coordinate-zero components and at least one component meeting the independent open. None of these equals D: D has dimension seven, and contains no independent triple. The independent-zero component is distinct from all three coordinate-zero components as well. Therefore the full cubic zero scheme has at least five irreducible components. The exact total remains unknown.
