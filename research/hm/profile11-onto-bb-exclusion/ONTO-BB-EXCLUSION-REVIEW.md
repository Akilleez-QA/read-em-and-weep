# Exact-version review of the onto-bb source exclusion

## Verdict and scope

**PASS.** The argument in `ONTO-BB-SOURCE-EXCLUSION.md` proves the claimed exclusion for the exact version identified below. Both possible actual top constant spans are excluded. The proof uses the original connection throughout, and its intersection and derivative-kernel arguments are statements about actual sheaves, not only generic ranks or abstract splitting types.

Consequently:

- For `G3.11.863639aa192e`, the entire source `E=P O(-2)+2T O(-3)+O(-10)`, tuple `(0,2,0,0,0,0,0,1)`, is excluded, using the split-target onto conclusion of PR821.
- For `G3.11.73682b4c817f`, only this source's onto-top branch is excluded. Its separate degree-twelve torsion branch is not treated.
- Neither entire stable label is excluded, and no global SF-rank conclusion follows from this result alone.

The audit below independently checks the new derivation, including the complete five-type necessary support list. No correction is required for the reviewed version.

## Exact versions and mathematical inputs

Review date: 2026-10-23.

Reviewed proof:

    ONTO-BB-SOURCE-EXCLUSION.md
    SHA256 4fbecacfb401cad0b82f3e5990d56fc0da65af6b493596ea6a8cadce16d8ca98

The two alternatives and the split-target onto conclusion are taken from the following immutable public theorem:

    PR821, commit 0d7e1e7312a114ded8a2c49ed1a7ca2f4d7e4c7f
    ONTO-RANK-FOUR-TOP-SUBSYSTEMS.md
    SHA256 87244e453597105dffb298743c1725ac29b00c8b8dc1cafad37f55235c81ea34

[Exact PR821 theorem](https://github.com/Akilleez-QA/read-em-and-weep/blob/0d7e1e7312a114ded8a2c49ed1a7ca2f4d7e4c7f/research/hm/profile11-onto-rank-four-top/ONTO-RANK-FOUR-TOP-SUBSYSTEMS.md).

The saturated internal/external derivative-image argument is Section 3 of:

    PR796, commit d2b43060c83328dd5118aee6b9288fcfa0c873ac
    research/hm/profile12-quadratic-block-exclusion/PROOF.md
    Audited copy SHA256 622763aac375db7e17bc7cab472f1afda0477b0f769371a3b3ef845cd5c9e3b1

[Exact PR796 proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/d2b43060c83328dd5118aee6b9288fcfa0c873ac/research/hm/profile12-quadratic-block-exclusion/PROOF.md).

PR821 pins the original actual-source data at commit `db51525015bb7c5e825833d550d08dedf6f6ea96`. The following audited input files have exactly the Git blob identities specified there:

    ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md
    b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3

    NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md
    d7506dae49b4be43230450c4132bd5db91f137ef

    ONE-ONE-ENDPOINT-DEGREE-WINDOWS-AND-159-NECESSARY-PAIRS.md
    dcacf0bcdef8377c1ed7654e5b82659ea409456e

    one-one-endpoint-necessary-pairs.json
    fe0afa410d89340d3082dc814277f89fbb582c19

    rank-three-quotient-frontier-144.json
    8b5971092f9ef762584912609fd5e9301c4e271d

[Pinned original inputs](https://github.com/Akilleez-QA/read-em-and-weep/tree/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load).

The frontier data record original determinant defect zero for both stated labels and the quoted targets. The new proof needs the resulting saturated inclusion `A_q -> (H O/E)(-2)`. It does not infer saturation from an arbitrary equal-rank injection. PR821 is used as the stated public dependency, including its own explicitly cited predecessors; this review does not claim an independent reproof of the entire historical dependency chain.

## 1. Exact transform and actual intersections

Let `F=P O(-2)`, let `p:F -> U` be onto, and put `M=F^+`. PR821 supplies

    K0=W O(-9),  M=(Wp+T) O(-1),
    im(kappa)=W O(-9),
    0 -> F -> I0=M intersect E -> W O(-7) -> 0.

The twist by two in the last quotient is correct: the internal derivative image lives in `(E/F)(-2)`, whereas the first-span quotient lives in `H O/F`.

Only the source `O(-10)` can map to the negative target `O(-10)`. Onto-ness of `E -> A_q` makes that scalar restriction an isomorphism. Hence the actual kernel of the negative projection is

    E'=P O(-2)+2T O(-3),  rank 16,  degree -44.

The restriction `E' -> U` is onto. Projection to `E'/F=2T O(-3)` gives the exact sequence

    0 -> W O(-9) -> K=E^- -> 2T O(-3) -> 0:

local lifting is possible precisely because `F -> U` is onto. This is an exact statement about the actual kernel, regardless of whether the extension splits. Twisting by nine, global sections lift through the right-hand term because `H1(W O)=0`. Thus `K(9)` is generated and every degree of `K` is at least -9.

Also `I0` lies in `E'`: its map to `E/E'=O(-10)` kills `F` and factors through `W O(-7)`, from which it vanishes by ordinary degree. Consequently `M intersect E'=I0` exactly.

The derivative of `K` lies in `E`. Its component in `(E/E')(-2)=O(-12)` is O-linear, since `K` lies in `E'`, and vanishes by the lower degree bound on `K`. The external derivative of `E'` is the saturated positive summand `U`, already attained by `F`.

The proof of PR796, Section 3 applies equally to a vector-bundle target `U`, not only to the line target used in that section's application: the raw derivative image has exact sequence `0 -> J -> I -> U -> 0`, and locally free internal and external quotients make the full ambient quotient locally free. Here `J=0`, so the raw image is already saturated and isomorphic to `U`. Therefore

    G=(E')^+,  G/E'=U(2),  rank G=18,  degree G=-30.

Finally, `M -> G/E'` is onto because `F -> U` is onto. Since `M` lies in `G`, this proves the sheaf equality `G=E'+M`, not merely equality after saturation or over the function field.

## 2. The nine-dimensional alternative

For the degree-eight alternative, PR821 gives `C O/M=O(8)`. Set `S0=E'+C O`. The equality just verified implies

    derivative(E') lies in (E'+M)(-2) subset S0(-2),

and the constant summand is preserved as well. Hence `S0` is connection-stable.

For completeness, the lattice step is valid at every point. Its generic span is connection-stable, so its saturated subbundle has constant Grassmannian map in characteristic zero and is a constant subbundle. A full-rank coherent subsheaf of that bundle is locally free on the smooth curve. If its determinant has local colength `m`, its determinant lattice has the form `t^m O` times a horizontal determinant frame. Connection stability would require `m t^(m-1) dt` to belong to `t^m O dt`. In characteristic zero this forces `m=0`. Thus `S0` is itself saturated and constant.

The quotient `S0/G` is generated by `C O/M`, so `rank S0<=19`. If its rank were 18, saturation of `G` in the ambient trivial bundle would make `G=S0`, contradicting `degree G=-30`. Hence `rank S0=19` and `S0/G` is a line bundle of degree 30. The induced surjection

    O(8)=C O/M -> S0/G

cannot exist: a surjective map of line bundles is an isomorphism. This argument retains all divisor information; it is not only a generic-rank comparison.

## 3. Cohomology and the complete support calculation

Both `E'(3)` and `M(3)` are generated, and their direct sum maps onto `G(3)`. Since `G` is saturated in a trivial bundle, all of its degrees are therefore in `{0,-1,-2,-3}`. Write

    G=c O+a O(-1)+b O(-2)+d O(-3).

The coefficient representations `c,b` are even and `a,d` are odd. The exact intersection sequence gives

    H1(I0)=P+W Sym^5 W=V+2P+D.

There are no sections of either outside term of `0 -> F -> I0 -> W O(-7) -> 0`; thus additivity here is exact, not an assumed vanishing of an intervening map. The sum sequence `0 -> I0 -> E' direct-sum M -> G -> 0` then injects `c=H0(G)` into this representation. Hence `c<=V+2P+D`.

The Euler-character identities check independently as follows:

    chi(E')=-P-2TW=-(2V+3P+2D),
    H0(U(2))=V+2P+D,
    chi(G)=-(V+P+D);

    chi(E'(1))=-2T,
    H0(U(3))=Wp+S+2T,
    chi(G(1))=Wp+S.

For the split target the positive-section calculations use `Sym^6 W=V+P`, `Sym^7 W=Wp+T`, `Sym^8 W=P+D`, and `Sym^9 W=S+T`. For the balanced target they use `W Sym^7 W` and `W Sym^8 W`, giving the same answers. No higher cohomology is present in either positive target twist.

It follows that

    b+dW=c+(V+P+D),
    a+cW-d=Wp+S.

The injection `M -> G` injects `Wp+T=H0(M(1))` into `H0(G(1))=a+cW=Wp+S+d`. Consequently `d` contains a `T`, and writing `d=T+u` gives

    b+uW=c,
    a=Wp+S+T+u-cW.

Here every displayed coefficient is genuine. The four odd irreducibles are `W,Wp,S,T`. The identities

    WW=1+A,  WpW=P,  SW=A+D,  TW=V+P+D

and the support bound on `c` force `u=m Wp+n T`. Since `c=b+uW`, the formula for `a` can be rewritten as

    a=Wp+S+T-bW-uA.

Using `Wp A=T` and `T A=Wp+S+2T`, the `T` multiplicity gives `m+2n<=1`. Thus `(m,n)` is exactly `(0,0)` or `(1,0)`.

Write `c=xV+yP+zD`, with `x,z<=1`, `y<=2`. Then

    cW=yWp+zS+(x+y+z)T.

When `u=0`, nonnegativity of `a` forces `x+y+z<=1`, giving exactly `c=0,V,P,D`. When `u=Wp`, the condition `c>=P` and the same bound force `c=P`. Substitution gives exactly the five types in the reviewed proof. Direct rank and degree checks give `(18,-30)` for each. This establishes completeness of the necessary overlist without a hidden search range or a realizability assumption.

## 4. Elimination of four types

The actual subbundle `T O(-1)` of `M` injects into `G`. In each of types ii-v, its map to the degree-minus-one block is zero by equivariance and Schur's lemma; its maps to the lower-degree blocks vanish by ordinary degree. It would therefore factor through the constant block, whose rank is respectively 3, 4, 5, or 4. None can receive an injective rank-six sheaf map. This excludes those four types, leaving

    G=L+T O(-3),  L=(Wp+S+T) O(-1).

The degree-minus-one top subbundle `L` is canonical, is saturated in the original constant bundle, and contains `M`. Choosing an equivariant splitting to check Hom groups does not impose a horizontal splitting.

## 5. Actual rank-ten kernel subbundle and coefficient-span contradiction

The projection `E' -> G/L=T O(-3)` is onto, since `G=E'+M` and `M` lies in `L`. The component from `P O(-2)` is zero by ordinary degree. The remaining map is a nonzero constant equivariant map `2T -> T`, so its kernel is one copy of `T`. Therefore the actual intersection is

    I=E' intersect L=P O(-2)+T O(-3),  rank I=10.

In particular, this is not a generic intersection estimate. The quotient map is onto everywhere, and its kernel is the stated bundle. The derivative of `I` lies in `G`, because `I` lies in `E'`. Its projection to `(G/L)(-2)=T O(-5)` is O-linear because `I` lies in `L`. Both relevant ordinary Hom spaces vanish:

    Hom(P O(-2),T O(-5))=0,
    Hom(T O(-3),T O(-5))=0.

Thus `I` is contained in the actual Gauss kernel of `L`. The proof needs only this rank-ten subbundle of the kernel, not equality with the entire kernel. It correctly concludes that the derivative rank of `L` is at most two.

For a pure-linear inclusion, local values and first derivatives span precisely its constant coefficients. This holds for an arbitrary linear inclusion, with no selected coefficient values: writing its local columns symbolically as `a_i+z b_i`, values together with derivatives span all `a_i,b_i`. Consequently `L^+=C_L O` for its actual coefficient span, and

    12 < dim C_L <=14.

The strict lower bound uses saturation: a saturated rank-twelve subbundle spanning only a twelve-dimensional constant space would equal that space's constant bundle, contradicting `degree L=-12`.

Since `M` lies in `L`, its actual constant span `C=V+P+D` lies in `C_L`. On the other hand, the coefficient map makes `C_L` a quotient representation of

    (Wp+S+T)W=A+V+2P+2D.

Complete reducibility implies that `C_L/C` is supported by `A+P+D`. Its nonzero irreducible constituents have dimensions 3, 4, and 5, so it cannot have dimension one or two. Thus `dim C_L` is either 12 or at least 15, contradicting the preceding bounds. This excludes the last alternative.

## Verification boundary

This is a structural mathematical audit of the frozen proof and its explicitly cited inputs. It is not proof-assistant certification or a fresh verification of every older theorem cited by PR821. The checks consist of exact sequences, saturation, universal connection arguments, complete bounded representation reasoning, input identities, and file hashes. No selected actual HM/source coefficients, points, derivatives, matrices, instance ranks, model experiments, scans, or large computation were used. No external content was modified. Any change to the proof's reviewed hash requires a new exact-version review.
