# Finite iterated section envelopes exclude eleven more quotient labels

## Result

Starting from the37-label maximal-profile frontier published in PR722 at acae327c07c3a71f0832c07ebae61c6cd2bef7f2, a finite set of iterated section tests excludes eleven labels: nine in profile(1,1), none in profile(1,2), and two in profile(2,1). The new frontier is **26**, with profile counts **20/4/2**. All original182 stable IDs are preserved. No profile is closed.

## The necessary inequality

Let F be a saturated subbundle of a constant bundle, with top degree at most -d<0. Suppose a locally free J injects into the ambient quotient by F and its actual derivative factors through J(-2). Set F0=F, Fj=F(j-1)^-, and Qj=F(j-1)/Fj. The strict-slope theorem gives top Fj<=-d-j. The actual derivatives give sheaf injections

    Q1 -> J(-2),  Qj -> Q(j-1)(-2) -> J(-2j).

For any integer r>=d put m=r-d+1. Then top(Fm(r))<=-1, so H0(Fm(r))=0. The exact sequences for Fj and Qj give, by telescoping and finite-group semisimplicity,

    H0(F(r)) <= sum_(j=1)^m H0(Qj(r))
              <= sum_(j=1)^m H0(J(r-2j))

as an irreducible-multiplicity inequality. Therefore

    D(F,J,d,r)=sum_(j=1)^(r-d+1) H0(J(r-2j))-chi_G(F(r))    (1)

must be genuine: it is the previous nonnegative difference plus H1(F(r)). No ranks of later derivatives are prescribed, and zero stages are permitted. This proof uses the actual constant connection at every step. A fuller statement is in `NEGATIVE-GAUSS-FLAGS-HAVE-ITERATED-SECTION-ENVELOPES.md`; the argument above is sufficient independently of that separate note.

## Actual orientations and source characters

Apply (1) in two orientations already justified by the primal and dual degree-envelope applications:

    primal: F=K=E^-, J=A=E/K, d=3,
            chi K(r)=chi E(r)-chi A(r);
    dual:   F=L=(Q*)^-, J=B=Q*/L, d=2,
            chi L(r)=chi Q*(r)-chi B(r).

The actual subbundle E has top<=-2, so K has top<=-3. The source presentation Q*->M3* O(-1) gives top Q*<=-1, hence top L<=-2; no H0(Q*(1)) hypothesis is needed. A and B inject naturally into the appropriate ambient quotient by K or L, and the derivatives factor through them with exactly the actual Gauss kernels.

The actual presentations give

    chi E(r)=M3 chi O(r-1)-M4 chi O(r),
    chi Q*(r)=M3* chi O(r-1)-M2* chi O(r),

where M3=3Wp+3S+6T, M4=2V+4P+3D, and M2=A_std+2V+3P+4D. All irreducibles here are self-dual. On P1, chi O(t)=Sym^t W for t>=0, zero for t=-1, and -Sym^(-t-2) W for t<=-2. Thus (1) is computable without any splitting choice for K or L.

## Explicit finite witnesses

The checker tests primal twists3 through11 and dual twists2 through11. Each row below gives one negative multiplicity in (1), enough to exclude that label; A denotes primal, B dual, and1 the trivial representation.

| Stable ID | Side | Twist | Negative constituent |
|---|---:|---:|---:|
| G3.11.2e0d1359392c | B | 6 | 1: -1 |
| G3.11.8db06186550e | B | 6 | 1: -1 |
| G3.11.dde2c08e25a5 | A | 8 | 1: -1 |
| G3.11.32f5d3efc97b | B | 11 | Wp: -1 |
| G3.11.966331d6ffc3 | B | 11 | Wp: -1 |
| G3.11.1aa4528c491e | A | 4 | V: -1 |
| G3.11.1310166d970e | A | 10 | 1: -1 |
| G3.11.a9f1c3893e1e | B | 7 | W: -1 |
| G3.11.4797404c6d0b | B | 6 | 1: -1 |
| G3.21.3bc00aa2165a | B | 11 | Wp: -1 |
| G3.21.8de61cbbef4b | B | 11 | Wp: -1 |

The certificate stores full target, Euler and difference characters, plus the first obstruction in each orientation when both exist. The surviving26 labels satisfy this selected finite test set; no assertion is made that it exhausts all twists or all necessary conditions.

## Reproduction and scope

Run `python3 verify_all_profile_iterated_section_envelope.py` to generate `all-profile-iterated-section-envelope.json`. The standalone cached verifier uses exact Q(sqrt(5)) character arithmetic and standard Python only. It pins the published baseline144, public722 certificate, actual source/plateau note and strict-slope theorem. It imports no other verifier, output, unpublished audit or witness data. The certificate partitions the original182 stable IDs into145 previous exclusions, eleven new exclusions and26 remaining labels.

These are bounded abstract character tests. No selected actual coefficients, points, matrices, actual-instance rank evaluations, scans, spikes or consumed experiments enter. There is no realization, smoothing, complete-proof or SF claim.
