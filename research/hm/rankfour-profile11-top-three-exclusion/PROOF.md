# Coherent-image cohomology excludes the actual top-degree-three boundary

## 1. Exact result and retained assumptions

Work over C on the original physical parameter line T=P(W*) with its fixed G=SL2(F5) marking. Retain the actual saturated plane-section inclusion

    0 -> E -> H O_T -> Q -> 0,       dim H=30,
    S=Q* subset H* O_T,

with the constant connection, and write

    K=ker beta_E,    A_q=E/K,
    L=ker beta_S,   B=S/L.

These are coherent derivative kernels and actual locally free quotients on the smooth curve, not arbitrarily chosen splitting summands. The actual source presentations and physical representation identifications are those of ACTUAL at db51525015bb7c5e825833d550d08dedf6f6ea96, retained in inputs/actual.md. In particular

    0 -> S -> M3* O(-1) -> M2* O -> 0,
    M2=A_std+2V+3P+4D,
    A_std=Sym2 W,   S4=Sym3 W,   D=Sym4 W.          (1)

All irreducibles displayed here are self-dual. The vector spaces A_std,V,P,D are pairwise inequivalent irreducibles of dimensions 3,3,4,5. We do not identify the other three-space V with A_std.

The theorem is that the actual Gauss quotient cannot be

    A_q=W O(3)+O(2)+O(-8).                         (2)

There is no restriction on the determinant defect in this exclusion. In particular it excludes both previously retained defects zero and twelve, and every other nonnegative defect, without replacing any coherent image by its saturation.

The immutable top-three theorem, PR1188 at 518b3f2686269f83e4f788fe4ed30d0e36dac37b, retained in inputs/top-three.md, proves that (2) is necessary when the actual generic derivative rank is four, the maximal ordered rank-four plateau is (1,1), and max ordinary degree(A_q)=3. Relative to that theorem's imported geometric/source hypotheses, the top-degree-three boundary is therefore impossible.

This does not close the full rank-four profile (1,1): quotients with higher top degree remain outside this result. It makes no new global rank bound, square-surjectivity, full-adjoint, smoothing, algebraicity or original-repair claim. It does not use the later positive-endpoint theorem, a rank17 rank-three theorem, a quotient connection, a horizontal splitting, a selected actual coefficient, parameter, point, jet, tensor, matrix or instance-rank computation.

Two full immutable inputs are retained in INPUTS.json, with full source URLs, commits, byte lengths, SHA256 and Git blob identities. They were freshly fetched from their immutable commits and authenticated against the retained copies. Those identities certify provenance, not the transitive actual geometric premises.

## 2. A torsion-tolerant section gate for an actual Gauss quotient

For any equivariant saturated subbundle E of a constant bundle on this smooth curve, let r be the generic rank of its actual derivative. This derivative has kernel K and gives a coherent sheaf injection

    A_q=E/K -> Q(-2).                                (3)

Indeed the quotient by the exact sheaf kernel identifies A_q with the coherent image. The image need not be saturated; no saturation is used. Global sections are left exact, hence

    H0(A_q) -> H0(Q(-2))                             (4)

is an equivariant injection. Equivariant Serre duality, with S=Q* and Omega_T=O(-2), identifies

    H0(Q(-2)) = H1(S)*.                              (5)

Consequently every irreducible multiplicity in H0(A_q) must be no larger than in H1(S)*. This is a coefficient-space injection, not a fiberwise inclusion of A_q into a constant bundle and not a horizontal decomposition. It remains valid at every ramified parameter because it uses the exact coherent kernel and image.

For completeness the following independent dual argument yields the equivalent cohomology surjection

    H1(S) ->> H1(A_q*(-2)).                         (6)

Here is the complete argument, including possible ramification.

The second fundamental forms of E and its annihilator S are negative transposes. For local sections e of E and s of S, differentiate the identity pairing(s,e)=0:

    pairing(d s,e)+pairing(s,d e)=0.

The Leibniz terms disappear in the respective quotients, giving the globally defined transpose identity for beta_E and beta_S, with their common cotangent twist Omega_T=O(-2). In particular beta_S annihilates K under the dual pairing, so it factors through

    beta_S:S -> A_q*(-2) subset E*(-2).             (7)

It has generic rank r by the transpose identity. Since rank A_q=r, the coherent image has full generic rank in A_q*(-2). Its kernel is L by definition. Thus the induced map

    B=S/L -> A_q*(-2)

is an injection of vector bundles of equal rank, with a possibly nonzero torsion cokernel Z. This is a coherent-image injection; no zero-defect premise or saturation equality is being assumed.

There are therefore actual equivariant exact sequences

    0 -> L -> S -> B -> 0,
    0 -> B -> A_q*(-2) -> Z -> 0.                   (8)

Because T has dimension one, H2(L)=0. Because Z has finite support, H1(Z)=0. The two long cohomology sequences consequently give surjections

    H1(S) ->> H1(B) ->> H1(A_q*(-2)).               (9)

Their composite proves (6), for every torsion length and support. Both maps are G-equivariant; finite-dimensional complex G-representations are semisimple, so every irreducible multiplicity in the final target must be no larger than in H1(S).

## 3. Compute the source cohomology from the actual presentation

In (1), both H0(M3* O(-1)) and H1(M3* O(-1)) vanish. The boundary map is thus an equivariant isomorphism

    H1(S)=M2*=A_std+2V+3P+4D.                      (10)

In particular the multiplicity of A_std in H1(S) is exactly one. This equality is an actual cohomology consequence of the original S presentation. It is not inferred from a necessary splitting ledger or selected source.

## 4. The forced quotient demands two copies of A_std

For (2), self-duality of W gives

    A_q*(-2)=W O(-5)+O(-4)+O(6).

Equivariant Serre duality on T, with det W=1, gives

    H1(O(6))=0,
    H1(O(-4))=Sym2 W=A_std,
    H1(W O(-5))=W tensor Sym3 W=A_std+D.            (11)

The last identity is the universal Clebsch-Gordan formula

    W tensor Sym3 W = Sym2 W + Sym4 W.

Consequently

    H1(A_q*(-2))=2A_std+D.                         (12)

Its A_std multiplicity is two, whereas (10) has only one. Thus the equivariant surjection (6) is impossible, contradicting the actual quotient (2).

For an independent check of the same representation calculation, use the direct section injection (4)-(5):

    H0(A_q)=H0(W O(3))+H0(O(2))+H0(O(-8))
            =W tensor Sym3 W+Sym2 W+0
            =2A_std+D.

It cannot inject into M2. This verifies the twist and duality signs without computing a source instance or assuming a determinant defect vanishes.

## 5. Contribution and scope

The section/cohomology gate is an established actual-map constraint, rederived here in (3)-(9). It already appears as condition 4 of Section 5 in ONE-ONE-ENDPOINT-DEGREE-WINDOWS-AND-159-NECESSARY-PAIRS.md at the original commit db51525015bb7c5e825833d550d08dedf6f6ea96; that historical necessity ledger is not needed as a proof premise here. The new contribution is the direct all-defect application (10)-(12) to the forced rank-four top-degree-three quotient, excluding its entire boundary without the subsequent image or filtration refinements. A positive determinant defect cannot repair the deficit: it enlarges or modifies H1(B) but never prevents its surjection onto H1(A_q*(-2)). Therefore restricting the defect to zero or twelve is unnecessary for this exclusion.

Combined with the immutable top-three necessity theorem, the entire maxdeg(A_q)=3 boundary in the actual rank-four maximal ordered profile (1,1) is excluded, including all three previously retained K shapes. This is a conditional boundary exclusion, not a claim that every remaining rank-four quotient or the original global problem is resolved.

The proof is structural. Its only representation arithmetic is the fixed identity W tensor Sym3 W=Sym2 W+Sym4 W and the actual source character in (1). There is no search, enumeration, selected actual value or hidden flat quotient connection.
