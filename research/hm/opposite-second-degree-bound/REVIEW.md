# Independent final whole-package review

Verdict: PASS. No mathematical correction or publication blocker found.

This is an independent mathematical review and bounded exact-arithmetic replay, not formal proof-assistant certification.

## Reviewed final bytes

SHA256:

- PROOF.md: 97b4f4b099106b6f2663385e1f310aa87960f60c763bbd13dafdc757c68391db
- verify.py: 210e18f1f784cca81fd0e07155f93ff560357f1c80b946607ca8ebde265b9446
- INPUTS.json: ab5698d1442d22dca3182e9cb44d71fdaca94e8dbd6d2502b314b67777a87a68
- REPRODUCE.md: 90134c45ffe8f7506b2f4530eee69922ffddddb9c0fbb5f337c3fbe3cdc4e53a

The reviewer freshly fetched all four originals from GitHub at the exact manifest commits and paths. Their bytes equal the local verification copies, and their recomputed Git blob identities equal the manifest values. Their SHA256 values are:

- TWIST: baabea589839f5b8ceba93f9e458b794fb66690384540cbd7746f621a723fa19
- MONAD: 5b0dff3dd55c0d9ca9bb26c2b3cbadc3456e6a829ef96aa4e36b7c97639f283c
- PLANE: 03f7909a73ebe2cd2ff7c8639f3bea3384741058297156f51f38b2b6094354e6
- AMPLE: f48000f35baca29dc049cefb628c58902739b5e5a69d71e858817c33f94425f8

In particular AMPLE is the published PR994 original at commit48727e1f5fd5ab079c21b8b39af608f7d91fabab, not merely an unpublished local draft.

## Mathematical audit

1. Tensoring the exterior Euler complex by K gives the stated three-term resolution, with K tensor K in degree zero. The standard Bott vanishings reduce its H2 to the cokernel of H tensor H0(K(1)) to H0(K(2)). The homogeneous degree-three and degree-four Koszul strands canonically identify the multiplication map with the surjection H tensor Lambda3 H to H0(K(2)), whose kernel is Lambda4 H. This proves H2(K tensor K)=0 universally. The dimension arithmetic 50 minus 5 equals 45 is only a check, not the proof of surjectivity.
2. In the graded symmetric-square monad the five total-degree-two terms have precisely the stated cohomological degrees. The first four vanish, including the central term by the direct-summand argument. The terminal E1 term Lambda2 N has no outgoing differential; incoming differentials are retained. Since no other total-degree-two associated graded term survives, H2(B(-1)) is its natural equivariant quotient. There is no hidden central H2 term and no unjustified degeneration assumption.
3. The current right-target convention N=A+W' is authenticated separately from TWIST's old labels. Lambda2 N=1+A+T6 therefore gives at most one invariant in the actual quotient. No label identification from the old convention is silently assumed.
4. For M=p*B(-1) tensor O(4E), the successive j=2,3,4 layers are B_R(1), W tensor B_R(2), and A tensor B_R(3). The exact nonsplit extensions make H1(J) a quotient of A+V because the later two H1 groups vanish. Thus H1(J) has no invariants, even though neither the sheaf extensions nor their connecting maps are assumed split or zero.
5. The two-row p-Leray sequence then bounds H2(X,M) invariants by H2(B(-1)) invariants, retaining the possible H0(J) transgression. Curve-base pi-Leray supplies the required canonical H1 injection without requiring higher-direct-image vanishings. The actual C(-4) summand and equivariant Serre duality with omega_T=O(-2) give the claimed H0(C*(2)) invariant bound.
6. The final nine-row table agrees with the authenticated AMPLE list. O(2) contributes one invariant, W O(1) contributes one, and A O(2) contributes none. In particular row15 contains O(2) and its dimension is one. The exact dimension vector is 2,1,1,2,1,1,1,1,1, excluding precisely rows7 and12 and leaving rows9,10,14,15,17,18,20. The claims about row9 and the vertex scalar are explicitly inherited from AMPLE rather than newly evaluated.

7. The added Section6 is reviewed in full. Every surviving row gives exactly one invariant map to O(2). In the first four cases it is projection onto O(2), and in the final three it is the surjective Euler map on W O(1); all other atoms contribute no equivariant map. Thus the kernel is a canonical rank-four degree-twenty-four subbundle, and all seven listed kernels are correct. The quotient sequence is split in the projection cases and retains its nonsplit Euler component in the other cases.
8. The common lower bound one forces equality in the invariant Leray dimension chain and proves the actual H2(B(-1)) invariant dimension is one. The resulting invariant transgression vanishing is correct. The final paragraph also correctly notes the simpler source explanation: all three exceptional layers have invariant H0 zero, so H0(J)^G=0. Accordingly this is not presented as a new nontrivial scalar evaluation. The reviewer independently checked both vanishing character pairings.

## Bounded replay and scope

The reviewer inspected the entire standard-library verifier and ran both python verify.py and python -O verify.py. Both passed with identical output and the seven stated survivors. The checks use explicit runtime failures, not removable assertions. They cover fixed abstract character identities, universal dimension arithmetic, exact immutable bytes, a filter of nine already authenticated rows, and all seven quotient-kernel ranks and degrees. REPRODUCE.md correctly reconstructs all four omitted input originals using immutable git-show commands before running the checks.

No selected actual HM/source coefficient, parameter, point, jet, derivative, matrix or instance rank was evaluated. The proof does not determine which surviving type is actual, the rank of the top obstruction, or the row9 vertex scalar. Its geometric premises remain explicitly imported from the immutable inputs. All stated scope limits are accurate.
