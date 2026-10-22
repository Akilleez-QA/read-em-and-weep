# Gamma theta restriction forces nonpositive K4 splitting

## Scope and inputs read

This note concerns the actual general-quadric full-adjoint problem, not the primary Picard scheme. No symmetry of the chosen general quadric q is assumed.

Inputs read before the deduction:

- BEILINSON-AMBIENT-RESTRICTION-ISOMORPHISM.md: for M=M4 and f:Xhat->P3, the actual complex Rf_*M has a locally free model

      K tensor O directsum [P tensor Omega^1(1) -> R tensor O],

  in degrees0,1, with K=H0(Xhat,M), R=H1(Xhat,M), dim P=5. The constant K-summand is the canonical evaluation of global sections. Restriction identifies K with H0(S,M|S), where S=f^{-1}(Gamma).
- GENERIC-BETA-ABELIAN-INTERPOLATION.md: the actual map Theta:det(U) tensor R_Rao* -> P tensor U is 20->20 and has kernel K. Its sheaf counterpart theta has source rank20 and target P tensor O(1). This R_Rao has dimension20 and is not the R=H1(Xhat,M) in the Beilinson model.
- KAPPA-RATIONAL-SEXTIC.md: the actual restriction Omega^1(1)|Gamma is O_P1(-2)^3, from the evaluation kernel on each HM line. This is stronger than merely knowing Gamma has degree six.
- ACTUAL-GAMMA-CONDUCTOR-BUNDLE-GATE.md: the normalization direct image G4 is a rank55 vector bundle, and its positive higher direct image vanishes at every parameter, including cusps and modified fibers.
- CONDUCTOR-VALUE-DERIVATIVE-FILTRATION.md: the actual conductor target has exact sequence 0->P4->E4->V4->0, where P4 is rank10, degree -35, and H0(P4)=0.
- TWIST-FOUR-VALUE-MAP-GENERIC-SURJECTIVITY.md, Section8: the actual map G4->V4 is everywhere onto on the established common open. Its kernel K4 has rank25 and degree -65.
- ACTUAL-GAMMA-BALANCED-NORMAL-BUNDLE.md: the actual normal bundle is O(11)^2. In particular the already proved infinitesimal-neighborhood section restriction isomorphisms apply without splitting the full formal neighborhood.

All identifications below use these actual maps. They do not replace K4 by the generally different sheaf g_*M, where g:S->Gamma.

## 1. A quadratic complementary complex on Gamma

The ambient Euler characteristic is zero. This follows directly from the Beilinson model: its derived rank is k+15-r, while flat-fiber Riemann–Roch gives rank Rf_*M=15. Thus r=k, where k=dim K and r=dim R. Equivalently, the actual 20->20 boundary has equal kernel and cokernel dimensions.

Restrict the locally free Beilinson model to Gamma. Derived base change gives the exact model

    Rg_*(M|S) = K tensor O_Gamma
      directsum [O_P1(-2)^15 --a--> O_P1^k].             (1)

The map a is actual and depends on q. Its entries are binary quadratics after bases are chosen; no equivariance of a under A5 is asserted. The O(-2) splitting comes from Gamma's actual evaluation geometry, not a generic balancedness assumption.

In particular

    g_*(M|S)=K tensor O directsum ker(a),
    R1g_*(M|S)=coker(a).                               (2)

The constant summand is the natural evaluation map. The kernel of a is locally free, as a torsion-free subsheaf on the smooth parameter curve. Every splitting summand of ker(a) has degree at most -2, since it embeds in O(-2)^15.

For every beta in Gamma, derived base change to that point makes K a direct summand of H0(S_beta,M|S_beta). Thus the k actual ambient sections are linearly independent on every entire fiber, including singular and cusp fibers. This is stronger than saying an individual section has a nonzero value at each of fifty marked points. It does not assert that values at a single point of a fiber are linearly independent.

## 2. Global conductor comparison, including cusps

The normalization sequence and the vanishing R1(g nu)_*N4=0 give

    0 -> g_*(M|S) -> G4 -> E4 -> R1g_*(M|S) -> 0.

Combine it with 0->P4->E4->V4->0 and with the everywhere-surjective G4->V4. The snake lemma yields an exact sequence on all Gamma:

    0 -> g_*(M|S) -> K4 --d_der--> P4
      -> R1g_*(M|S) -> 0.                              (3)

The arrow d_der is the actual derivative discrepancy remaining after value matching. It need not vanish fiberwise. Only its map on global sections vanishes, because H0(P4)=0.

Let J_der=im(d_der). It is a coherent subsheaf of the vector bundle P4, hence torsion-free and therefore locally free on Gamma=P1. Consequently K4/g_*(M|S)=J_der is locally free. This proves that g_*(M|S)->K4 is a subbundle inclusion at every parameter, including the cusps. No fiberwise identification of K4 with g_*M, no assertion that normalization commutes without correction, and no saturation of J_der inside P4 is used.

Together with (2), the canonical evaluation map

    K tensor O_Gamma -> K4

is a subbundle inclusion. Moreover H0(K4)=K, since (3) and H0(P4)=0 identify all global sections with those of g_*M.

## 3. New restriction on the actual K4 splitting

Write the Birkhoff–Grothendieck splitting of K4 as a sum of line bundles. If a summand O(b) had b>0, its b+1-dimensional space of sections would evaluate into a one-dimensional fiber. The evaluation map from all global sections would then have a nonzero fiber kernel. Section2 rules this out.

Therefore every splitting degree of K4 is nonpositive. The zero-degree summands contribute one section each, and the negative summands contribute none. Precisely,

    K4 = O^k directsum (directsum_{j=1}^{25-k} O(-a_j)),
    a_j>=1,  sum_j a_j=65,  0<=k<=20.                  (4)

Here k is exactly the actual full-adjoint corank dim ker Theta, not a freely chosen dimension. This improves the earlier upper bound five/six for individual splitting degrees to the sharp uniform upper bound zero. In particular H0(K4(-1))=0 unconditionally on the common open.

The remaining proof-repair gate is now exactly the absence of zero summands in K4. Negative total degree did not previously imply this, and (4) still does not prove k=0.

## 4. A bound on parameter torsion in the higher direct image

Let rho be the generic rank of the actual quadratic map a in (1), and let T_tor be the torsion subsheaf of coker(a). Then

    rank R1g_*(M|S)=k-rho,
    length T_tor <= 2 rho <= 30.                       (5)

Here is a bundle proof of the length bound. Let F=ker(a), I=im(a), and let Ibar be the saturation of I in O^k. The quotient Ibar/I is exactly T_tor. The kernel F is a subbundle of O(-2)^15: its quotient I is torsion-free, hence locally free. Its rank is15-rho and every summand has degree at most -2, so

    deg I = -30-deg F >= -2 rho.

Since Ibar is a subbundle of O^k, deg Ibar<=0. Therefore

    length T_tor=deg Ibar-deg I <=2 rho.

No particular minor or coefficient was evaluated. If a is generically onto, R1g_*(M|S) is finite and its total scheme-theoretic length is at most2k (necessarily k<=15). If it is not generically onto, the higher direct image has a nonzero vector-bundle part on all Gamma; the same bound still controls its additional torsion. Neither alternative is chosen here.

When a global comparison with the actual theta presentation is fixed, this gives the corresponding restriction on its cokernel along Gamma. The formula (5) is already unconditional for the actual geometric higher direct image; it does not infer that an arbitrary sheaf extension of theta across Gamma is the correct one.

## Boundary

The new assertions are the nonpositive K4 splitting, fiberwise independence of all actual global sections on every Gamma fiber, and the quadratic-model torsion bound. They do not show that K4 has no trivial summands, that the actual 45-dimensional and400-dimensional images in485 dimensions meet trivially, or that theta is onto along Gamma. The chosen quadric breaks normalizer symmetry, and no orbit-invariance argument is applied to its degeneracy scheme.
