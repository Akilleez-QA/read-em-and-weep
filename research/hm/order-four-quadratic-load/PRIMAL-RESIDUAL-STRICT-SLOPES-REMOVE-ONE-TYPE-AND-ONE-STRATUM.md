# Primal residual strict slopes remove one type and one stratum

## Result and scope

On the six necessary residual quotient spaces of PR737 (commit7f041f462f2598165c834c1412ead9b16a8eb0d5), the actual Gauss strict-slope bounds have two further consequences:

1. Type Z6 is impossible for all three primal equality labels.
2. In type Z3, the scalar alpha on D O(-2) -> O(2) must be nonzero. The ordinary-surjection stratum alpha=0, a*beta!=0 is therefore impossible for the actual Gauss configuration.

Exactly five formal E splitting types remain. None of the three quotient labels is excluded: each still has five nonempty necessary residual parameter spaces. No connection on a quotient is introduced.

## 1. The residual kernel's two section bounds

Retain the proved saturated subbundles

    C=(P+D) O(-2) subset E,
    C7=(Wp+T) O(-3) subset K=E^-,

and set Z=E/C and N=K/C7. The ordinary quotient sequence established in PR737 is

    0 -> N -> Z -> R=O(2)+O(-8) -> 0.

The actual strict-slope theorem gives top K<=-3. As C7 is concentrated in degree-3, it embeds in K's top splitting block and its coefficient subrepresentation splits. Therefore K=C7 direct sum N equivariantly as bundles. This is not an assertion that the original ambient derivative descends to N.

First, top K<=-3 gives

    H0(N(2))=0.                                      (1)

Second, the actual derivative of K factors through A(-2), with kernel K^-. Strict slope gives top K^-<=-4, so its twist-three global sections vanish. Hence

    H0(K(3)) injects into H0(A(1)).

Here A=O(6)+O(2)+O(-8), so H0(A(1))=Sym7 W+Sym3 W=Wp+T+S. The direct summand C7 contributes exactly Wp+T to H0(K(3)). Semisimplicity consequently gives

    H0(N(3)) is a subrepresentation of S.             (2)

These are ordinary section consequences of the original derivative on K, not derivatives assigned to N.

## 2. The two cuts

For Z6=Wp O(-3)+V O(-4)+Wp O(-5)+O(-8), every equivariant map to R annihilates the Wp O(-3) summand: its possible upper Hom multiplicity is that of Wp in Sym5 W=T, namely zero, and its lower degree is negative. Thus N contains Wp O(-3), and H0(N(3)) contains Wp. This contradicts (2), because Wp and S are distinct irreducibles. Type Z6 is impossible.

For Z3=D O(-2)+O(-8)+W O(-9), setting alpha=0 annihilates D O(-2) in both rows of Z3 -> R. Thus N contains D O(-2), contradicting (1). This does not silently identify N with an arbitrary complement inside E; the argument uses the kernel N of the established residual quotient and the independently proved splitting K=C7 direct sum N.

Accordingly the actual necessary Z3 conditions simplify to

    alpha!=0 and (a,b)!=(0,0),

with beta unrestricted. The removed stratum had been a perfectly valid ordinary equivariant quotient in PR737; only the new actual strict-slope input excludes it.

## 3. Exact surviving twist-two and twist-three characters

For each surviving residual quotient, N's global sections are the kernel of H0(Z(r)) -> H0(R(r)). At r=2,3 the lower target contributes no sections.

In types Z1 and Z3 the relevant source is D at twist2 and W tensor D=S+T at twist3. With alpha!=0 the map is the standard full degree-four evaluation multiplied by constants or linear forms. It is an isomorphism D -> Sym4 W at twist2 and the surjective multiplication W tensor Sym4 W -> Sym5 W at twist3. Its twist-three kernel is S.

In types Z2 and Z4 the source has no twist-two sections and is T at twist3. The required alpha!=0 identifies it with the entire Sym5 W target, so the twist-three kernel is zero. In Z5 the source has no sections at either twist.

Thus for Z1 through Z5 respectively,

    H0(N(2)) = 0,0,0,0,0;
    H0(N(3)) = S,0,S,0,0.

Every remaining parameter choice from PR737, after alpha!=0 for Z3, passes (1)-(2). No stronger compatibility or realization follows from these two tests alone.

## Reproduction

Run verify_primal_residual_strict_slope_cuts.py. It pins PR737's note and certificate, the PR733 equality certificate, and the strict-slope theorem. It checks the target characters by an independent integer McKay recurrence, the killed Hom channels for the two cuts, the five surviving type IDs and exact section-kernel characters, and nonemptiness of all surviving necessary support loci. It records zero quotient-label exclusions. The geometric argument above supplies the actual Gauss input and justifies the bundle splitting; no actual-instance evaluation is used.
