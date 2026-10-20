> Publication scope: Nef eigenline argument improves independent-frame bound to seven and excludes both intermediate eight-dimensional alternatives. Historical statements about unresolved mixed classes refer to the source stage; this packet does not supersede the separately stated conditional mixed-vanishing result in PR145.

# A nef eigenline obstruction: independent zero frames have dimension at most seven

## Result

Under the structural hypotheses and proved conclusions of ../nilpotent-kernel-parameter-locus/PROOF.md, over C:

1. The closed reduced projective spectral-kernel incidence has dimension at most four.
2. The independent zero-frame locus has dimension at most seven.
3. The locus of three-planes with kernel dimension at least two has dimension at most four. In particular a five-dimensional kernel-pencil locus is impossible.

This excludes both previously remaining possible eight-dimensional independent branches: the five-dimensional spectral line-kernel base and the five-dimensional nilpotent-free pencil base. No actual operation matrix, product, rank instance, selected input, jet, or source-model value is evaluated. The proof uses only universal vector bundles, characteristic polynomials, properness, and nef intersection theory.

## 1. Imports and universal incidences

Let G=Gr(3,V), dim V=5, S its tautological bundle, D=det S, and E=sl(S) tensor D. The structural operation gives T:E -> J tensor O_G. On the projective bundle p:P_G(E)->G of lines, write R=O(-1) and

    M=R* tensor p*D.

The universal tensor gives a twisted traceless endomorphism

    A:p*S -> p*S tensor M.

Its invariants are sections

    q=tr(A^2) in H^0(M^2),   h=det(A) in H^0(M^3).

Define the closed reduced spectral incidence

    X={T(R)=0, h=0}_red,

and its closed reduced nilpotent subincidence

    N={T(R)=0, h=0, q=0}_red.

They are projective. The imported global nilpotent theorem proves dim N<=3. Rank-one exclusion and the characteristic polynomial show that every point of X minus N is regular semisimple with eigenvalues 0,lambda,-lambda, where lambda^2=q/2. The imported orientation/eigenline construction identifies the reduced independent zero-frame locus, over a finite etale double cover of X minus N, with a principal (G_m)^3-bundle. Thus its dimension is dim(X minus N)+3. This dimension statement makes no assertion that an unreduced frame scheme is a bundle over the reduced incidence X.

## 2. Universal lemma: a projective spectral family avoiding nilpotents has dimension at most two

Let Y be any integral projective subvariety of X such that q is nowhere zero on Y. Then

    dim Y<=2.

First q trivializes M^2 on Y. There is a finite etale double cover pi:Y'->Y whose points are square roots lambda in M of q/2. On this cover lambda is nowhere zero, hence trivializes pi*M. Take an integral irreducible component of this cover with its reduced structure, still denoted Y'. It is projective, finite and surjective over Y: finite etale covers of an integral scheme are reduced, and each irreducible component dominates the base. Alternatively one can subsequently normalize such a component without changing any of the following identities or conclusions.

The normalized endomorphism B=lambda^(-1)A on S'=pi*p*S satisfies

    B^3=B.

This is the traceless three-dimensional characteristic identity because h=0 and tr(B^2)=2. Its three distinct constant eigenvalues are -1,0,1. The polynomial idempotents

    e_0=1-B^2,    e_+=(B^2+B)/2,    e_-=(B^2-B)/2

give a direct sum of three line subbundles

    S'=L_0 direct-sum L_+ direct-sum L_-.

Their ranks are one on every geometric fiber. Each L_i is a subbundle of V tensor O_{Y'}, since S' is. Therefore L_i* is globally generated and nef. Put x_i=c1(L_i*).

The projection g:Y->G is finite. Indeed M restricted to any geometric p-fiber is O(1), an ample line bundle; M^2 is trivial on Y. A positive-dimensional projective fiber would thus have an ample torsion line bundle, impossible (restrict to a projective integral curve in that fiber). All geometric fibers are zero-dimensional. Since g is proper, it is finite. Consequently g'=g composed with pi:Y'->G is finite, and

    H=(g')*c1(O_G(1))=x_0+x_++x_-

is ample on Y'.

The tautological quotient Q'=(V tensor O_{Y'})/S' has rank two, so c_3(Q')=0. Because c(S') is the product of (1-x_i), this identity is

    h_3(x_0,x_+,x_-)=sum_{a+b+c=3} x_0^a x_+^b x_-^c=0.

Suppose d=dim Y'=dim Y>=3. Intersect the identity with H^(d-3)[Y'] and take degree. Every term has nonnegative degree, since all x_i and H are nef. Hence each degree is zero. The expansion of H^3 is a positive-integer linear combination of exactly those degree-three monomials. It follows that degree(H^d[Y'])=0, contradicting ampleness. This proves the lemma.

The argument is valid on singular integral Y': operational Chern classes and intersection degrees are defined there, and nef nonnegativity can equivalently be checked after pulling back to a projective resolution. The pullback of H then has the same strictly positive top degree.

## 3. The projective spectral incidence has dimension at most four

Let Y be an integral irreducible component of X. If q vanishes identically on Y, then Y lies in N and dim Y<=3.

Otherwise its zero locus on Y is either empty or an effective Cartier divisor. If nonempty, every irreducible component of its support has codimension one, hence dimension dim Y-1. This support lies in N. Since dim N<=3, we obtain

    dim Y-1<=3,

and therefore dim Y<=4.

If the zero locus is empty, Section 2 gives dim Y<=2. These cases exhaust all components. Consequently

    dim X<=4,
    dim X minus N<=4,
    dim Z_ind<=4+3=7.

This uses the actual closed spectral incidence, rather than a kernel bundle on a rank stratum, so rank jumps create no missing boundary. It also avoids applying the earlier full-Grassmannian kernel-line argument on a divisor.

## 4. The kernel-at-least-two locus has dimension at most four

Let D_2={W in G:dim ker T_W>=2}, a closed determinantal locus. For every W in D_2, the homogeneous cubic h_W on the positive-dimensional projective space P(ker T_W) has a zero over C: either it vanishes identically or its projective hypersurface is nonempty. Thus the proper image p(X) contains D_2.

Since dim p(X)<=dim X<=4, it follows that

    dim D_2<=4.

This is a structural exclusion of any five-dimensional kernel-pencil locus, including the previously unresolved nilpotent-free nonzero-determinant branch. It is compatible with the sharper imported bounds dim G_3<=3 and dim G_4<=2.

## 5. Scope and remaining possibilities

The proof gives an upper bound, not existence of a seven-dimensional independent component. It does not compute the number, multiplicities, or exact dimensions of independent components. Every four-dimensional projective spectral component necessarily has a nonempty three-dimensional nilpotent boundary, since the nilpotent-free projective alternative has dimension at most two. Thus any independent component attaining the new seven-dimensional bound forces the global nilpotent incidence to attain its own bound of three.
