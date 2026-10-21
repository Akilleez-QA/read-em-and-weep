# Intrinsic support strata and a forced primary corank-two point

Work over C. This note concerns only the primary evaluation e_x:S2 -> M2, not the full adjoint quadratic multiplication.

## 1. Universal support classification

Let dim(V)=5, dim(W)=2, and let L be a four-plane in V tensor W containing no nonzero full fiber v tensor W. Define its intrinsic V-support

    U(L)=span{(id_V tensor lambda)(ell): ell in L, lambda in W*},
    r=dim U(L),   Y=sl(W)L.

Then r belongs to {3,4,5}, and the following are the only possibilities:

    r=3: dim Y=6;
    r=4: dim Y is 7 or 8;
    r=5: dim Y is 9 or 10.

These are necessary alternatives; no realization assertion is made for every alternative.

Proof. Choose a basis of W and write A=pr1(L), B=pr2(L), C=A intersection B, with dimensions a,b,c. Put d=dim(L intersection (C direct-sum C)). Then U(L)=A+B, r=a+b-c. The dimension identity proved in PR550 gives

    dim Y=a+b+4-d.

Since Y is contained in U(L) tensor W, its deficit delta=2r-dim Y is nonnegative. Let p=a-c, q=b-c and t=4-d. The image of L in (A/C) direct-sum (B/C) has dimension t and projects surjectively to both factors. Thus t>=max(p,q), and

    delta=p+q-t<=min(p,q).

Suppose delta>=2. Then p,q>=2 and r=p+q+c<=5 forces c<=1. If c=0, then d=0 and delta=r-4<=1, contradiction. If c=1, the constraints force p=q=2 and r=5. Now delta=p+q-(4-d)=d>=2, while d<=dim(C direct-sum C)=2. Hence d=2 and C tensor W is contained in L, contradicting the no-full-fiber hypothesis. Consequently delta<=1.

Also r>=2 because L is four-dimensional and L is contained in U(L) tensor W. Equality r=2 would force L=U(L) tensor W, again prohibited. PR550 supplies dim Y>=6. Together these facts give exactly the asserted alternatives.

In particular,

    dim Y<=8 iff r<=4;
    dim Y=6 iff r=3.

## 2. The intrinsic support bundle map

Use the pinned actual exterior model

    A0=M0, dim A0=5, exterior^2 A0=V tensor W,
    M2=V tensor W, S2=A0 tensor sl(W),
    (a tensor D)x=c(id_V tensor D)(a wedge x), c nonzero.

Let X=P(A0) parametrize lines, and let Q be the rank-four tautological quotient:

    0 -> O_X(-1) -> A0 tensor O_X -> Q -> 0.

The universal star is the subbundle O_X(-1) tensor Q of exterior^2 A0 tensor O_X. Contracting its W-factor defines

    sigma:E=Q(-1) tensor W* -> V tensor O_X.

Its source has rank eight and target rank five. The image of the fiber map at [x] is U(Lx), where Lx=x wedge A0. This assertion is about the image of the fiber map, and does not interchange taking fibers with forming an image sheaf.

Equivalently sigma is induced by a linear bundle map

    sigma_tilde:A0 tensor W* tensor O_X(-1) -> V tensor O_X,

whose formula sends a tensor lambda tensor x to the W-contraction of x wedge a. Its kernel contains W* tensor O_X(-2), and the exact sequence

    0 -> W* tensor O_X(-2) -> A0 tensor W* tensor O_X(-1)
      -> E -> 0

shows that sigma_tilde and sigma have equal rank at every point. Thus support rank at most k is intrinsically cut out by the (k+1)-minors of a 5-by-10 matrix of linear forms, without selecting or evaluating any entries.

The actual no-full-fiber theorem applies to every Lx. Section 1 therefore proves the equalities of closed sets

    {rank(e_x)<=8}=D4(sigma),
    {rank(e_x)<=6}=D3(sigma).

They also imply equality of the corresponding radical ideal sheaves. Equality of determinantal schemes, multiplicities, or scheme structures is not asserted. PR547's generic rank(e_x)=10 implies generic rank(sigma)=5.

## 3. A corank-two primary evaluation must exist

Write h=c1(O_X(1)); the integral Chow ring of X is Z[h]/(h^5). The exact sequence above gives

    c(E)=(1-h)^10/(1-2h)^2.

Its degree-four coefficient is

    c4(E)=(210-480+540-320+80)h^4=30h^4, which is nonzero.

If sigma were everywhere surjective, its kernel K would be a vector bundle of rank three. The exact sequence 0 -> K -> E -> 5O_X -> 0 would give c(K)=c(E). But c4(K)=0 for a rank-three bundle, contradicting c4(E)=30h^4. Hence D4(sigma) is nonempty. By Section 2,

    there exists [x] in P(A0) with rank(e_x)<=8.

Equivalently, the actual primary evaluation has corank at least two somewhere. No point, coefficient, actual source instance, or numerical rank is selected or evaluated. Combining PR550, the possible ranks at such a point are six, seven, or eight; this argument does not distinguish them.

## 4. No divisorial support-drop component

The exterior model is N-equivariant. Hence the span of the maximal minors of sigma_tilde is an N-stable space of quintics, and it is nonzero by generic support rank five. The pinned invariant-gcd input states that N is perfect and has no positive-degree invariant on A0 of degree at most seven. Any nonconstant homogeneous gcd of these quintics would span a one-dimensional N-character, hence would be an invariant of degree at most five. This is impossible. Thus the maximal minors have constant gcd and their common zero set has no divisor component.

Consequently the nonempty rank-at-most-eight evaluation locus has dimension at most two in P4. This improves the available control of ranks seven and eight, not merely the rank-six locus. It does not assert expected codimension four.

For reference only, if D4(sigma) has the expected codimension four, the Thom-Porteous formula applied to the dual map 5O_X -> E* gives its zero-cycle class c4(E*)=30h^4. In that conditional case the determinantal scheme has length thirty. Expected codimension, reducedness, and any orbit description remain unproved; length thirty is not an unconditional conclusion.

## Dependencies and scope

- PR550 dimension identity and universal lower bound, commit edd49e0e6b15ae1bb41e51e5cd9f46f418e05f6f:
https://github.com/Akilleez-QA/read-em-and-weep/blob/edd49e0e6b15ae1bb41e51e5cd9f46f418e05f6f/research/hm/pointwise-evaluation-bound/PROOF.md
- Actual exterior model and no-full-fiber theorem, PR543 commit 7bf725bcd857a2deb975f9ecb80fca32e7833ae0:
https://github.com/Akilleez-QA/read-em-and-weep/blob/7bf725bcd857a2deb975f9ecb80fca32e7833ae0/research/hm/order-four-quadratic-load/PRIMARY-INJECTION-AND-FAILURE.md
- Generic evaluation rank ten, PR547 commit 5a8efc999e9b886c51f18232a580407bac4bbe66:
https://github.com/Akilleez-QA/read-em-and-weep/blob/5a8efc999e9b886c51f18232a580407bac4bbe66/research/hm/primary-evaluation-generic-surjectivity/PROOF.md
- Perfectness and absence of invariants of degrees one through seven, PR543 commit 8d24a12c4af9c922db2052a360c96a053dcba5b8, Section 2:
https://github.com/Akilleez-QA/read-em-and-weep/blob/8d24a12c4af9c922db2052a360c96a053dcba5b8/research/hm/order-four-quadratic-load/PRIMARY-BAD-CODIMENSION-THREE.md
- Primary representation source: Horrocks-Mumford (1973), Lemma 2.5 and Theorem 3.5:
https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf

The new conclusions are the universal support/rank classification, intrinsic smaller-minor presentation of actual rank-at-most-eight and rank-six strata, forced nonemptiness of the actual rank-at-most-eight locus, and exclusion of its divisorial components. The Chern obstruction uses no expected-codimension assumption. The full adjoint map, Q4, a selected quadratic or source pair, higher-order lifting, and algebraicity are not resolved. This is a mathematical derivation, not a proof-assistant verification.
