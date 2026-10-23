# Forced quotient splitting for source127 c-d-f

## Claim and precise dependency

Work over C with binary icosahedral G and the linearizations of PR920. Assume the actual source127 c-d-f hypotheses and conclusions of [PR920, Sections6–9](https://github.com/Akilleez-QA/read-em-and-weep/blob/1528ff8ea56b21e03f7501a962bdaa6728a75904/research/hm/profile11-source127-cdf-normal-form/PROOF.md), Git blob718b5245560a84568492874bab8d8c34730e8319. In particular, E is saturated in H O, C10 is an actual constant subspace, F=E intersect C10 O, C10 O/F=O(18) is saturated in Q=H O/E, and projection by C10 identifies E/F with U_6^10 direct-sum U_0^8 in the actual direct constant sum Sym10 W direct-sum Sym8 W. All off-diagonal lifts retained in PR920 are allowed. Then

    Q* = O(-18) direct-sum S O(-7) direct-sum Wp O(-1) direct-sum T O(-1)

as a G-equivariant vector bundle. This is an additional necessary quotient-type condition, not a classification of inclusions or an actual realization theorem.

## Universal quotient, including its orientation

Let ell be the tautological line in a determinant-one two-space W and let U_k^n have fiber ell^(n-k) Sym^k W inside Sym^n W. Under the invariant perfect apolar pairing on Sym^n W, its annihilator is ell^(k+1) Sym^(n-k-1) W. Indeed choose ell=Cx and a complementary y: the subspace has monomials x^(n-j)y^j, 0<=j<=k; apolar pairing pairs index j only with n-j, so its annihilator consists of monomials with x exponent at least k+1. This argument is independent of the complementary vector and hence identifies the whole equivariant subbundle. It gives an exact sequence

    0 -> U_k^n -> Sym^n W O -> Sym^(n-k-1) W O(k+1) -> 0.

Fiber ranks are constant everywhere, so the sequence is a sequence of bundles, not a generic-rank calculation. We used self-duality of symmetric powers of a determinant-one two-space. For (n,k)=(10,6) the quotient is S O(7); for (8,0) it is Sym7 W O(1).

## Exact extension and its splitting

The quotient map Q -> H O/(E+C10 O) has kernel C10 O/F=O(18). The projected inclusion in PR920 shows its target is

    R = S O(7) direct-sum Sym7 W O(1).

The target and kernel are locally free by the saturated normal form. Thus the sequence is

    0 -> O(18) -> Q -> R -> 0.

Its ordinary extension group is

    Ext1(R,O(18)) = H1(S O(11)) direct-sum H1(Sym7 W O(17)) = 0,

because H1(O(d))=0 for d>=-1 on P1. The direction matters: Ext1(O(18),R) generally is not zero. Hence a bundle splitting exists. Averaging any splitting over the finite group G in characteristic zero preserves the right-inverse equation, so a G-equivariant splitting exists too. No canonical choice is asserted. Dualizing and using the self-dual irreducibles and Sym7 W=Wp+T gives the claimed Q*.

Checks: rank(Q)=1+4+8=13; degree(Q)=18+28+8=54. Also h0(Q(-1))=18+4*7+8=54 and h0(Q(-2))=17+4*6=41. These are consequences, not replacements for the extension proof.

## Exact catalogue consequence

The original source is index127, defect0, endpoints A=[O(-8),O(2),O(16)], B=[O(-18),O(-4),O(6)], tuple(0,0,1,1,0,1,0,0). Its bundle is (P+D)(-2)+(V+P)(-4)+O(-8). In the explicitly pinned campaign E catalogue its unique ID is14. In the independently pinned original unrestricted dual catalogue the unique ID of the above Q* multiset is148; the campaign Q catalogue agrees entry-for-entry with that catalogue.

At the pinned through917 checkpoint the source127 c-d-f row has32 distinct pairs, all with E ID14, including(14,148). Exactly31 alternatives are incompatible with this necessary quotient theorem. The executable fragment targets only stable label G3.11.cce6e3ba4eeb and its exact tuple and endpoint data. It retains(14,148), leaves other labels untouched, and does not remove any stable label. It returns a fragment rather than overwriting the campaign ledger, so independent source2 propagation can be composed separately.

## Limits

An abstract equivariant splitting of Q is not a constant splitting of H, a horizontal splitting for the induced derivative, or removal of source lifts u,v. None is needed or claimed. In particular this argument does not duplicate PR920's separate lift-removal work. The remaining pair may be unrealizable; no example of actual HM is supplied. No actual coefficients, points, derivatives, matrices or instance ranks are evaluated. The finite checker certifies arithmetic, source identity and catalogue accounting, not the full geometric proof in a proof assistant.
