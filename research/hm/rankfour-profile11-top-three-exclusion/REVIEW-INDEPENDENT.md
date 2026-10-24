# Independent whole-proof review: actual top-degree-three exclusion

## Verdict and reviewed artifact

PASS, conditional on the explicitly retained actual-geometric premises and the imported top-three necessity theorem. The whole written proof is valid, not merely its representation calculation. It excludes the actual quotient W O(3)+O(2)+O(-8) for every possible determinant defect. Together with the pinned top-three theorem, it excludes the entire maxdeg(A_q)=3 boundary of actual generic rank four and maximal ordered plateau (1,1). Higher top degrees and the complete profile remain open.

Reviewed file: PROOF.md.

Reviewed SHA256: ff1ee385836e7af3f28c3d94892939f6b3b25af5daa6ddf2d6d2ee472c1999a3.

I independently fetched both complete original inputs through the GitHub connector at the exact immutable commits, rather than relying only on a manifest or a previous worker's source claim. The returned bytes and Git blob identities agree with both retained inputs. The exact fetched text, URLs and blob identities are retained in INDEPENDENT-REMOTE-EVIDENCE.json. This establishes source provenance, not formal certification of the imported geometric results.

## 1. Exact objects and imported hypotheses

ACTUAL at db51525015bb7c5e825833d550d08dedf6f6ea96 identifies Q as D_lin(1), provides the exact locally free presentation

    0 -> Q* -> M3* O(-1) -> M2* O -> 0,
    M2=A_std+2V+3P+4D,

and uses the original physical binary-icosahedral marking. In particular A_std=Sym2 W and V are distinct three-dimensional irreducibles. It states self-duality and the center-even bundle convention. The actual ambient inclusion is the plane-section inclusion in a constant thirty-space, not the 54-dimensional coefficient presentation.

The independently fetched top-three proof at 518b3f2686269f83e4f788fe4ed30d0e36dac37b explicitly defines K as the actual derivative kernel and A_q=E/K on the same physical parameter line. Its T1 gives precisely the required quotient under the actual rank-four, maximal ordered (1,1), top-degree-three hypotheses and its stated transitive geometric/source premises. No abstract rank-four bundle is silently substituted for this actual derivative quotient.

The new exclusion itself needs only the actual ambient inclusion, its equivariance and the displayed Q* presentation. It does not depend on any choice among the three K shapes, positive-endpoint results, special defect classification, rank-three coverage, or a construction of the quotient. The additional rank/profile assumptions enter only when applying the pinned T1 to exclude the whole boundary.

## 2. Coherent-image injection is valid at ramification

The invariant constant connection gives an O_T-linear equivariant second fundamental form beta_E:E -> Q tensor Omega_T. Its exact sheaf kernel is K. The first isomorphism theorem identifies E/K with the coherent image, so there is an injective morphism of coherent sheaves

    A_q -> Q(-2).

Since Q(-2) is locally free on the smooth curve, its coherent image is torsion-free and hence locally free. Thus K is saturated in E and the quotient used here really is a vector bundle. None of this asserts that the image is saturated in Q(-2). The map may lose fiber rank at ramification; this does not invalidate sheaf injectivity. Taking global sections is left exact, independently of what happens on individual fibers. The claimed equivariant injection H0(A_q) -> H0(Q(-2)) is therefore justified without a zero-defect assumption.

No connection on the quotient A_q is introduced. Its splitting is used only to compute ordinary bundle cohomology; it is never declared horizontal.

## 3. Twist, duality and linearization audit

On T=P(W*) for G contained in SL(W), the canonical line has its standard equivariant identification Omega_T=O(-2), since det W is trivial. Equivariant Serre duality therefore gives

    H0(Q(-2)) = H1(Q*)*.

There is no determinant-character correction. The central signs also match: the central element acts by minus one on W and on O(3), and trivially on O(2) and O(-8). Every displayed A_q block is center-even, as are Q(-2) and M2. The alternate choice W versus W* causes no representation change because W is self-dual. An alternating rather than symmetric self-duality form does not insert a character or negate multiplicities. G is perfect, so a hidden nontrivial one-dimensional character twist cannot repair the mismatch.

There is also a direct check avoiding Serre duality for the target. Dualize the locally free Q* presentation and twist by -2:

    0 -> M2 O(-2) -> M3 O(-1) -> Q(-2) -> 0.

The O(-1) terms are acyclic. Since H1(O(-2)) is the trivial representation, the cohomology sequence gives H0(Q(-2))=M2. This agrees exactly with the proof's duality route. In the original presentation H1(Q*)=M2*, and self-duality identifies its character with M2; neither equality presumes an unproved cohomology vanishing.

## 4. The arbitrary-torsion dual proof is also sound

Differentiating the zero pairing between E and S=Q* gives the negative-transpose identity between their actual second fundamental forms. Consequently beta_S annihilates K and factors through A_q*(-2) inside E*(-2). The transpose has the same generic rank r as beta_E, while rank A_q=r. Its exact kernel remains L=ker beta_S. The induced map

    B=S/L -> A_q*(-2)

is thus injective with full generic rank and finite-support torsion cokernel Z. No claim of saturation or equality is made.

The two exact sequences 0 -> L -> S -> B -> 0 and 0 -> B -> A_q*(-2) -> Z -> 0 imply

    H1(S) ->> H1(B) ->> H1(A_q*(-2)).

The first surjection uses H2(L)=0 on a curve; the second uses H1(Z)=0 for a finite-support torsion sheaf. Both facts hold for every torsion length and support. In rank four, deg Z=-8-deg A_q-deg B is exactly the usual determinant defect, but the proof does not need its value or orbit support. Positive defect cannot remove this final quotient of H1(S).

The overall minus sign in the transpose identity does not affect its kernel, rank, coherent image, or any of the resulting cohomology surjections. All arrows remain equivariant.

## 5. Decisive representation deficit

The forced quotient has

    H0(A_q) = W tensor Sym3 W + Sym2 W = 2A_std + D.

Its O(-8) block has no sections. The universal identity W tensor Sym3 W=Sym4 W+Sym2 W gives the first A_std, and the O(2) block supplies the second. The actual target M2 has only one A_std. Finite complex G-representations are semisimple, so an equivariant injection with these multiplicities is impossible, despite the unobstructed ordinary dimension comparison 11 <= 41.

For the dual route, A_q*(-2)=W O(-5)+O(-4)+O(6), whose H1 is likewise 2A_std+D. Therefore the claimed surjection from H1(S)=M2* is independently impossible by the same deficit. This verifies both twist signs and the direction of the required inequality.

## 6. Independent verification and limits

verify_independent.py imports no author checker, character module, or result data. It uses exact arithmetic in Q(sqrt(5)), the nine class traces and sizes, and closed symmetric-power character polynomials. It independently checks the nine irreducible characters and their orthogonality, the physical distinction A_std versus V, the Clebsch-Gordan identity, both cohomology routes, parity, quotient rank and degree, actual M2 multiplicities, source bytes and immutable pins, and the exact reviewed proof hash. No global bundle enumeration or actual coefficient, point, jet, matrix or instance-rank calculation occurs.

Both ordinary Python and optimized Python pass 348 explicit checks and return identical JSON. Optimization cannot disable the checks. The result is in INDEPENDENT-RESULT.json. These checks accompany the mathematical review above; they do not pretend to mechanically certify sheaf exactness or the transitive actual HM premises.

The final proof correctly attributes the section gate as established rather than new. I also independently fetched ONE-ONE-ENDPOINT-DEGREE-WINDOWS-AND-159-NECESSARY-PAIRS.md at db51525015bb7c5e825833d550d08dedf6f6ea96 and confirmed that Section 5, condition 4 already states H0(A)<=M2. Its returned Git blob is dcacf0bcdef8377c1ed7654e5b82659ea409456e. The historical rank-three enumeration is not imported as a proof premise or coverage theorem; the current argument rederives the rank-independent gate and applies it to the newly forced rank-four quotient. The contribution is this complete all-defect boundary exclusion, not discovery of the general gate.

No mathematical correction was needed. The final provenance clarification was read and incorporated before binding this review to its final proof hash. No public write was performed. Neither the entire rank-four profile nor a new global rank bound is claimed.
