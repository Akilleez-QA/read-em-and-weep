# Independent first-normal comparison review

Reviewed 2026-10-11 against the pinned first_jet.json SHA256 2be28aebeb2ff40754f17ca94f76b68eb40043f6492a1794bd91436bc27e1f10 from PR61 head6b69eefd57098d9a0c1d9f43ed993d36e1e54bcb. This review concerns the constructed plane completion, with explicit j→i vector action convention (Id−h A_eta)g0, where A_eta(v)={eta,v}. It does not identify an ancestor or a higher-order logarithm dictionary.

## Independently executed identities

Using only the displayed polynomials and the frozen JSON, I separately reconstructed the denominator-change matrix M with

    M (W⁶,g,F)^T = (X⁸,Y⁸,W⁶)^T.

Its determinant is CF(X²−Y²)(F²−S²). Projecting −z a det(M)/(X⁸Y⁸W⁶) to all-negative plane Laurent exponents gives exactly

    Δ = z³/(W² X Y⁴) − z³/(W² X⁴ Y)
        + z²/(W⁴ X Y²) − z²/(W⁴ X² Y).

I independently evaluated the finite frozen Hamiltonian cochains on E0 using Ω(B_j,E0)=(0,0,−F,−g). Their alternating Čech sums are multiples of the relation (−a,W⁶,−g,F). Projecting the corresponding relation coefficient gives Δ for the origin and zero for all four directions a,b,c,d. These identities were checked by exact symbolic expansion over Q, without importing the comparison implementation.

A separate scan of all76 nonzero exported section-correction terms verifies:

- BI plane degrees (−4,−1,−5,−5);
- finite secondary weights1+d_i and infinity weights1+d_i−6;
- nonnegative finite-base powers and nonpositive infinity-base powers;
- negative plane powers only on coordinates inverted by the named open.

Thus the exported corrections have the required twists, characters and regularity, not merely equality in a rational-function field.

## Signed section equation

Let g0 send q_j to q_i+w_ij and fix the descended E0. With local section v_i=E0+h(t0 q_i+s_i), and j→i deformation (Id−h A_eta,ij)g0, the section compatibility equation to first order is

    s_j−s_i = A_eta,ij(E0)−t0 w_ij

in G. This is exactly the equation used by the comparison checker. On the base overlap, q_infinity maps to z q_finite+k, while t0 has representatives1 and z. The equation becomes

    k + TB s_infinity − s_finite − A_eta,mixed(E0) = 0

in G. The signs and normal coefficient are therefore correct for the explicitly stated convention. Reversing the action sign while retaining all other displayed conventions would require a different equation; it is not a silent permissible substitution.

The pinned PR61 files explicitly fix the Hamiltonian bracket and BCH tensors, but do not explicitly identify a stored tensor eta with the signed j→i vector action exp(±h A_eta). Accordingly this review does not label the comparison convention a correction of a demonstrated source error. A full second- and higher-logarithm dictionary remains separate.

## Common-refinement transfer

I inspected check_refinement.py. Its maps send the standard-cover q generator to an old radical-patch q generator plus a vector of G, fix B pointwise, and preserve the relation. The noncentral shift a·(lambda_old×lambda_standard) has precisely the required pairing difference because both lambda covectors evaluate to1 on r_E. Its displayed central terms have denominators only in the named radical coordinate and the named standard coordinate. On the base overlap z is invertible.

Because the maps fix B and its quotient G, the frozen Sym²(G) cochains and their evaluations are transported without a new basis transformation on G. The script compares against the actual previous base isometry, not merely an abstract existence statement. The producer's initial primary run had736 checks. The frozen primary checker adds ten output base-regularity/character checks, for a reported746 checks; the refinement run has153 checks. I inspected that addition but did not rerun either full producer suite. This review separately executed the class and76-term audits above and inspected the remaining formulas and signed equations.

## Bounded conclusion

The fixed-middle connecting class is canceled at first order by the evaluated frozen middle cochain under the stated action convention. The explicit regular section corrections and common-refinement formulas give a concrete first-normal comparison for our constructed plane completion. This does not obstruct the coupled formal deformation, prove a global ancestor identification, establish the higher-order action dictionary, or construct a carrier or zero-defect member.
