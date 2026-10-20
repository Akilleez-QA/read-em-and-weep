> Publication scope: preserved mathematical proof/audit. Historical statements that rank eight remains open are superseded only after the final assembly and all its prerequisites. No source-instance evaluation or formal verification is claimed here.

# Rank-eight normalized kernel: singularity sheaves and higher Chern constraints

## Result

Retain the proved conditional rank-eight branch from `../rank-eight-kernel-chern/PROOF.md` and `../rank-eight-flat-kernel-exclusion/PROOF.md`, with stability proved in the latter directory's `STABILITY.md`. On X=P^4 over C, its normalized kernel B is rank two, reflexive and slope-stable, with

    det B=O,  c2(B)=5h^2,

and carries the established H5-linearization with trivial central action. It is not locally free. Define the sheaf Ext objects

    S=Ext^1_X(B,O_X),    T=Ext^2_X(B,O_X).

Here S and T are new notation local to this document, not the earlier saturation defect. Write c3(B)=c3 h^3 and c4(B)=c4 h^4. Then:

1. B is self-dual by its reflexive alternating determinant pairing. It has local projective dimension at most two. S has support of dimension at most one, T has finite support, and all higher sheaf Ext objects vanish.
2. The singular locus of B is precisely Supp(S) union Supp(T). In fact Supp(T) is contained in Supp(S).
3. There are natural biduality consequences

       T ≅ Ext^4_X(S,O_X),
       0 → Ext^4_X(T,O_X) → S → Ext^3_X(S,O_X) → 0.

   The kernel in the second line is exactly the largest zero-dimensional subsheaf S_0 of S. Consequently length(S_0)=length(T). The quotient C=S/S_0 is pure one-dimensional (or zero), is Cohen–Macaulay on its support, and satisfies C ≅ Ext^3_X(C,O_X).
4. If ell=length(T), then

       ch(S)=c3 h^3 + ell h^4,
       ch(C)=c3 h^3,
       chi(S(m))=c3(m+5/2)+ell.

   In particular c3 is a nonnegative even integer. Equivariance strengthens the arithmetic to

       c3=10n,  n≥0;      ell=5q,  q≥0;
       c4 ≡ 15(n−1) (mod 30).

   Equivalently c4=15(n−1)+30k for an integer k. There is no sign bound on k proved here.
5. The singularity sheaf has the particularly restricted Hilbert polynomial

       chi(S(m))=10nm+25n+5q.

   Non-local-freeness implies n+q>0. If n=0, the singular locus is finite, S=S_0, and q≥5. If q=0, B has local projective dimension at most one everywhere, its nonempty singular locus has pure dimension one, and n≥1. More generally q is either zero or at least five, by the N-invariant finite-support argument below.

These are conditional necessary constraints. They neither realize nor exclude rank eight, and they do not change the established rank alternative {8,10}.

## 1. Reflexive self-duality and support bounds

Let U be the locally free locus of B. On U, exterior multiplication gives an alternating perfect pairing

    B|_U × B|_U → det(B)|_U=O_U.

Both B and its sheaf dual are reflexive, and X\U has codimension at least three. The induced isomorphism on U extends uniquely to an isomorphism B≅B*. This is a sheaf-dual statement, not the false assertion that B is isomorphic to its entire derived dual. No choice of an equivariantly trivial determinant is needed for this nonequivariant isomorphism.

At a point x of codimension d, the regular local ring O_{X,x} has dimension d. Reflexivity gives depth B_x≥min(2,d). Auslander–Buchsbaum therefore yields

    pd(B_x)≤max(d−2,0).

Thus pd≤2 globally; pd≤1 at codimension-three points; B is free in codimension at most two. This proves the support and vanishing statements for the higher Ext sheaves. For a finite module over a regular local ring, a nonzero top term of its minimal free resolution has nonzero top Ext into the ring. Hence vanishing of all positive Ext detects freeness in this situation. This identifies the singular locus with Supp(S) union Supp(T).

## 2. Biduality supplies the zero-dimensional correction

Because X is smooth, every coherent sheaf is perfect locally. Derived biduality gives

    RHom(RHom(B,O_X),O_X) ≅ B.

The standard cohomology-to-hyper-Ext spectral sequence is

    E2^{p,q}=Ext^p_X(H^{-q}(RHom(B,O_X)),O_X)
              ⇒ H^{p+q}(B),

with d_r of bidegree (r,1−r). These are sheaf Ext and sheaf cohomology of complexes, not global Ext groups.

The only potentially nonzero E2 terms are:

    (0,0): B**,   (1,0): Ext^1(B*,O),   (2,0): Ext^2(B*,O),
    (3,−1): Ext^3(S,O),   (4,−1): Ext^4(S,O),
    (4,−2): Ext^4(T,O).

Here codimension-three support gives Ext^p(S,O)=0 for p<3, and finite support gives Ext^p(T,O)=0 for p<4. Use B*≅B to identify the first row with B,S,T.

The term (2,0) has exactly one possible nonzero incoming or outgoing differential, namely

    d2: T → Ext^4(S,O).

Both its kernel and cokernel must vanish: they would otherwise survive in total degrees two or three, whereas the abutment has only degree zero. Thus this map is an isomorphism.

Next d2: S→Ext^3(S,O) must be surjective, since a cokernel survives in total degree two. Its kernel is the E3 term at (1,0). The only remaining differential affecting that kernel and (4,−2) is d3, which must be an isomorphism for the same convergence reason. This proves the asserted short exact sequence. In particular Supp(T)⊆Supp(S).

For completeness, a sheaf supported in dimension at most one has a unique maximal zero-dimensional subsheaf S_0, and C=S/S_0 is pure of dimension one or zero. At each closed point of its support, purity implies depth at least one, hence it is Cohen–Macaulay of dimension one. Regular-local duality then gives Ext^4(C,O)=0, while Ext^3(C,O) is pure one-dimensional and is its canonical module, up to the ambient dualizing-line twist. It also gives Ext^3(S,O)=Ext^3(C,O), and Ext^4(S,O)=Ext^4(S_0,O). For a zero-dimensional sheaf M, Ext^4(M,O) preserves length and is zero only when M=0. Therefore the kernel in the biduality sequence has length length(S_0); since it is zero-dimensional and the quotient is pure, it equals S_0. The quotient isomorphism is C≅Ext^3(C,O).

## 3. Chern character identities

In K_0(X), derived duality is represented by

    [RHom(B,O)]=[B*]−[S]+[T]=[B]−[S]+[T].

For a locally free resolution, dualization changes ch_j by (−1)^j. This identity applies to the derived dual; applying it directly to the sheaf dual would incorrectly discard the singularity corrections. With c1=0,c2=5, the character is

    ch(B)=2−5h^2+(c3/2)h^3+(25/12−c4/6)h^4.

Comparison in degree three gives

    ch3(S)=c3 h^3.

This is the effective top-dimensional cycle of S, counted with generic lengths, so c3≥0. Degree four gives

    ch4(S)=ch4(T)=ell h^4.

The zero-dimensional correction S_0 has length ell, so ch(C)=c3 h^3. Riemann–Roch and td1(P^4)=(5/2)h now give

    chi(C(m))=c3 m+(5/2)c3,
    chi(S(m))=c3 m+(5/2)c3+ell.

Since chi(C) is an integer, c3 is even. This argument does not presume that S itself is pure or that T vanishes.

## 4. Equivariant divisibility and the fourth Chern congruence

S and T inherit H5-equivariant structures from B and O. The proper-support Hilbert-congruence theorem proved in `../heisenberg-defect-hilbert-congruence/PROOF.md` applies without any purity or central-weight hypothesis. It implies

    5 | degree[S]_3=c3,     5 | length(T)=ell.

Together with evenness this proves c3=10n and ell=5q for nonnegative integers n,q.

To control c4, use the full-support central character of B. Define

    D(m)=chi(B(m))−2chi(O(m)).

This is an integer-valued polynomial of degree at most two, because the ranks and first Chern classes cancel. For m not divisible by five, both B(m) and O(m) have nontrivial scalar central character; every cohomology dimension is divisible by five by the elementary H5 representation lemma. Hence D(m) vanishes modulo five on the four nonzero residue classes. Multiplying the integer-valued degree-two polynomial by 2 gives an integral polynomial. Since 2 is invertible modulo five, the four-root argument proves 5|D(m) for every integer m, including m=0. In particular

    chi(B) ≡ 2 (mod 5).

Using td2(P^4)=(35/12)h^2 and chi(O)=1 gives

    chi(B)=−21/2+(5/4)c3−c4/6
          =(−63+75n−c4)/6.

Its integrality forces

    c4 ≡ 3(n−1) (mod 6).

Reducing 6chi(B)=−63+75n−c4 modulo five and using chi(B)≡2 gives 5|c4. Combining these congruences yields exactly

    c4 ≡ 15(n−1) (mod 30).

This also verifies the proposed residue without assuming divisibility of coherent-sheaf Chern classes from equivariance alone.

## 5. Nonemptiness and limitations

If n=q=0, the effective one-dimensional cycle of S vanishes and length(T)=0. Then S is zero-dimensional, and its length equals length(S_0)=length(T)=0. Thus S=T=0, so B is locally free, contradicting the proved obstruction. Hence n+q>0.

If n=0 then S has finite support. Its support, which equals the singular locus, is nonempty, and q≥1. This case is not excluded: a finite singular locus is not ruled out just by rank-two self-duality.

If q=0 then T=0, which forces pd≤1 by the local Ext criterion. The biduality sequence says S≅Ext^3(S,O), so S is pure one-dimensional or zero. It is nonzero by non-local-freeness, giving n≥1 and a pure one-dimensional singular support.

No equality such as c4=length(T), no positivity of c4, and no general vanishing of T follows from the arguments given. In particular the even-degree comparison in derived duality eliminates ch4(B); it constrains ch4(S), not c4(B). Keeping these distinctions is essential.

## 6. Normalizer symmetry strengthens the finite-length bound

The established normalizer action induces the standard SL2(F5) action on Hbar=H5/Z(H5)≅F5^2. Every nonempty finite N-invariant subset Z⊂P(V) contains at least 25 distinct points. Here is a universal orbit proof.

An Hbar-orbit on P(V) has size 1, 5, or 25. Size one is impossible: a projective point fixed by Hbar would determine an H5-invariant line in V, hence a one-dimensional representation of H5. Every commutator acts trivially on such a representation, whereas the central commutator generator acts by the nontrivial scalar zeta on V.

If Z contains an orbit of size 25, the assertion follows. Otherwise every orbit has size five, and its stabilizer in Hbar is a one-dimensional subspace. SL2(F5) is transitive on the six one-dimensional subspaces of F5^2. N-invariance therefore forces all six stabilizers to occur in Z. An Hbar-orbit has a single stabilizer because Hbar is abelian, so at least six distinct five-point orbits occur. In this alternative |Z|≥30.

Apply this to Supp(T) when T≠0. Its support is N-invariant because sheaf Ext inherits equivariance. Every support point contributes positive integral length, so

    T≠0 ⇒ length(T)≥25 ⇒ q≥5.

The same assertion holds for S_0. In particular n=0 forces q≥5, and the finite singular support has at least 25 distinct points. This is a lower bound only; this proof does not assert that a 25-point N-orbit exists or is impossible.

## Evidence boundary

The input consists solely of the proved local proof artifacts listed above. The new arguments are universal regular-local homological algebra, reflexive extension, the sheaf biduality spectral sequence, Chern characters, Riemann–Roch, and the already proved Heisenberg representation congruence. An exploratory literature search was not used as a proof input. No actual source, operation, matrix, selected input, rank instance, jet, residue, or large computation was evaluated. Only this local mathematical proof artifact was written.
