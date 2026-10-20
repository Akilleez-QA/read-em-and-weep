# The eigenline contraction is birational and its nef class is big

## Statement

Use the reduced eigenvalue cover Y' of an integral nonnilpotent component Y of the spectral incidence X, and the extended eigenlines of ../spectral-eigenline-boundary-extension/PROOF.md. All assertions below apply separately to each integral component T of Y'. Let D be the Cartier divisor of lambda on T. The component T is given its reduced structure. Then:

1. The ordered-eigenline morphism

       F:T -> P(V) x P(V) x P(V)

   is birational onto its image, and is an isomorphism onto its image away from D and the small diagonal. In particular B=3r-2H is nef and big on every nonnilpotent component Y.
2. Every positive-dimensional fiber of F is contained in D. On D, F is the diagonal of the kernel-line map to P(V). The positive-dimensional fibers have dimension at most two.
3. An integral curve C in T has B.C=0 precisely when it lies in D and its kernel line is constant. Every curve not contained in D has B.C>0.
4. On a four-dimensional T the full K-theory correction yields the additional identity

       h4(x_-,x_0,x_+) = 60mx^3-105m^2x^2+90m^3x-31m^4,

   where x=x_0, m=c1(M). The resulting mixed degrees are explicitly controlled by the nilpotent divisor as recorded below.

These are universal constraints, not an exclusion of four-dimensional components. No actual operation, source matrix, selected input, rank instance, jet or residue is evaluated.

## 1. Reconstruction from an independent eigenline triple

Each L_i is a line subbundle of the constant V-bundle. Thus its dual is the pullback of O_P(V)(1) under its eigenline morphism, and the three morphisms define F. Off D the three lines are independent. Conversely an ordered independent triple of lines determines its span W and the projective endomorphism of W with eigenvalues -1,0,+1 on the respective lines. This construction is algebraic on the open locus of independent triples: W is the image subbundle of the direct sum of the three tautological lines, and the endomorphism is the conjugate of the constant diagonal endomorphism under this direct-sum isomorphism. Its projective class determines the point of P(sl(S) tensor det S).

The ordered labels also determine the point of the eigenvalue cover. Intrinsically on the reconstructed tensor line R, the + eigenvalue defines the nonzero homomorphism R -> det W, which is exactly lambda in R* tensor det W. This avoids choosing a numerical normalization or a determinant trivialization. The resulting map is the inverse of F on the independent-triple locus, by the eigenvalue decomposition. Therefore F restricts to an isomorphism there onto its image, and is birational onto its full image.

Multiplication by lambda remains a nonzerodivisor after passage to any reduced irreducible component T: every component dominates Y, and lambda is nonzero at its generic point. Thus D is Cartier on T. The independent locus is dense, so dim F(T)=dim T.

By the determinant identity, B=x_-+x_0+x_+ is the pullback of O(1,1,1). This is nef, and its top degree is the positive degree of F(T) for the Segre polarization, since F is generically degree one. It is therefore big. Nefness and positive top self-intersection descend through a finite dominant component T -> Y, proving the assertion on Y as well.

## 2. Contracted curves and the boundary fibers

At every point of D, all three eigenlines equal ker A; outside D they are independent. Hence F^{-1}(small diagonal)=D set-theoretically, and all positive-dimensional fibers are boundary fibers. The curve criterion follows because O(1,1,1) is ample on the product: its pullback has degree zero on an integral curve exactly when that curve is contracted.

For the fiber bound, use the identification of the reduced nilpotent incidence N with the quadratic flag incidence in https://github.com/Akilleez-QA/read-em-and-weep/blob/f67e4d962d7078b12b94718cac385c6f4438ba13/research/hm/relative-models/nilpotent-kernel-parameter-locus/PROOF.md. Its nef classes h,t satisfy that 2h+t is ample and

       t(h^2-2ht+3t^2)=0

in rational operational Chow, by https://github.com/Akilleez-QA/read-em-and-weep/blob/5c5c24194a0ea87378e80ed7e95a785128ee054d/research/hm/relative-models/nilpotent-extremal-picard-obstruction/PROOF.md. On a fiber of the kernel-line map h is trivial. If that fiber contained an integral threefold Z, then t is ample on Z and the identity would give 3 degree(t^3[Z])=0, impossible. Thus the kernel-line fibers have dimension at most two. The reduced boundary of the finite eigenvalue cover maps finitely to N, so its kernel-line fibers satisfy the same bound.

Consequently B need not be ample: the exact possible obstruction consists of positive-dimensional boundary loci with constant kernel line. The result proves bigness without assuming their absence.

## 3. Degree-four Chern correction

The K-theory formula in ../spectral-boundary-k-theory/PROOF.md gives

       c_z(Q)=(1-xz)/[(1-x_-z)(1-x_+z)(1+(m-x)z)(1+(2m-x)z)].

Whenever a term contains m, the relations m(x_i-x)=0 allow replacement of each x_i by x. The degree-four coefficient then has m-free term h4(x_-,x_0,x_+) and correction

       -60mx^3+105m^2x^2-90m^3x+31m^4.

Since rank Q=2, this coefficient is zero, proving the identity. Here h4 is the complete homogeneous symmetric polynomial of degree four.

On a fourfold T write intersections on the Cartier boundary cycle [D], including all its scheme-theoretic multiplicities. Restrict x=h and m=h-t. Put

       d=degree(h^3[D]), a=degree(h^2t[D]),
       b=degree(ht^2[D]), c=degree(t^3[D]).

These are nonnegative, and a=2b-3c. The degree-three and degree-four quotient identities give

       degree(h3(x_-,x_0,x_+) x_i[T])
           = 10d+5a+15b = 10d+25b-15c,  for each i;

       degree(h4(x_-,x_0,x_+)[T])
           = 14d+18a-3b+31c = 14d+33b-23c.

The first expression is strictly positive. Indeed B is nef and big, while B^3 is termwise bounded above by 6h3 in the nef monomial expansion. Hence degree(h3 B)>0. The three h3 x_i degrees are equal, so each is positive. In particular the Cartier boundary is nonempty for a fourfold, with nonzero positive mixed numerical contribution.

The boundary cycle is legitimate even when D is nonreduced: its reduced components map finitely to nilpotent components and the displayed identities restrict to each such component. Its positive cycle multiplicities are retained in all four numbers.

## 4. Remaining gap

The contraction can collapse boundary fibers of dimension one or two. Bigness therefore does not promote B to ampleness. The boundary mixed-degree identities remain compatible with the known nef inequalities and do not force dim T<=3. No stronger dimension bound is claimed.
