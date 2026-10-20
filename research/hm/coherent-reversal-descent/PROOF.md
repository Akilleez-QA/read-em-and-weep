# Coherent reversal descent and strict parity data

## 0. Statement and scope

Retain exactly the invariant marked differential continuation setting of PR436, PR438 and PR444. Thus X is the stipulated connected complex abelian variety, the affine acyclic cover is individually invariant under geometric inversion, P is a literal reversal-compatible presentation modulo h^M with M>=3, all higher product/map/unit coefficients may vary, and every gauge and chart 2-unit is identity modulo h^M. The literal lifting premise retained by PR416 is still a hypothesis. All coefficients are regular differential operators of finite order, without a uniform bound in the formal degree.

Let U_n be the unrestricted presentation 2-groupoid modulo h^n, with ordinary chart 2-units, and let R_n be its strict reversal-fixed 2-groupoid, with unitary chart 2-units. Use U and R for their coefficientwise formal versions. Write I for the exact covariant reversed-opposite involution of PR444. Its fixed data are precisely the parity objects, even/unitary gauges, and unitary 2-units.

Let U_n^{hI} and U^{hI} denote the normalized coherent fixed-point 2-groupoids defined explicitly in Section 1. The natural functors

    R_n -> U_n^{hI},       R -> U^{hI}

are biequivalences. In particular:

1. A marked unrestricted object admits coherent reversal data if and only if its object class is reversal-fixed, equivalently if and only if it admits a parity representative.
2. Coherent structures over any one such underlying object class form one equivalence class, not one literal structure. Every relative equivariant 1-automorphism is equivariantly 2-isomorphic to the identity.
3. Equivariant 2-automorphisms remain. Their formal group is

       exp(product_{r>=M, r odd} C h^r),

   with the corresponding truncated formula at finite order. Thus each nonempty formal connected component is not discrete or contractible; a smallest finite truncation may have zero pi_2.
4. Every specified marked equivalence between two underlying objects carrying coherent structures can be equipped with an equivariant comparison 2-cell. For that fixed equivalence, different admissible comparison cells are related by an equivariant 2-isomorphism. This is existence and uniqueness up to the stated 2-isomorphism, not literal uniqueness of a comparison cell.

The new step upgrades PR444's fixed-object-class criterion, which explicitly excluded coherent actions, to a coherent 2-groupoid comparison. It removes the possible square-coherence and equivariant-gauge ambiguities without erasing the surviving scalar 2-automorphisms. It concerns marked ambient presentations only, not a module lift, a prescribed-product theorem, unmarked equivalences, convergence, or algebraicity. The original degree-six HM quotient and six pure conditions are not evaluated.

## 1. Exact coherent-data conventions

Composition of 1-arrows is written from right to left. A coherent fixed object is a triple (x,u,a) where

    u:x -> I x,
    a:(I u) u => id_x

is an invertible 2-cell satisfying the order-two coherence

    I(a) * u = u * a.                                  (1)

Here * means the indicated whiskering; both sides are 2-cells from u(Iu)u to u. This is the nontrivial triple-product condition for a normalized C2 action. All unit-group identity constraints are literal identities.

A 1-arrow from (x,u,a) to (y,v,b) is a gauge f:x->y together with

    eta: v f => (I f) u

such that

    b * f = (f * a) o (I(eta) * u) o (I(v) * eta).       (2)

The source of either side is I(v)v f and the target is f. A 2-arrow c:(f,eta)=>(f',eta') is an ordinary chart 2-unit c:f=>f' satisfying

    eta' o (v * c) = (I(c) * u) o eta.                 (3)

These definitions use the exact 2-functor I proved in PR444, so applying I preserves arrow direction, vertical composition, horizontal composition and identities. Standard pasting of (2) defines composition of equivariant arrows. It uses no reversal of Cech indices.

A strict fixed object x gives (x,id_x,id). A strict fixed gauge f gives (f,id_f), and a strict fixed 2-cell gives (3). This defines the displayed functor from R.

For reference, the involution on actual data is

    mu^I(f,g)=tau(mu(tau(g),tau(f))),  F^I=tau F tau,
    A^I=tau(A^{-1}), E^I=tau E tau,
    B^I=tau(B^{-1}), C^I=tau(C^{-1}),

where tau(h)=-h. The unit map C -> tau(C^{-1}) is a homomorphism into the reversed-opposite unit group. Hence (1)--(3) are equations in the actual presentation 2-groupoid, not a merely cohomological model.

## 2. Relative automorphisms and scalar 2-units

PR438 Lemma 2.1 proves that every finite unrestricted relative 1-automorphism is 2-trivial. The same is true formally, with compatible trivializing units: choose the unit at the initial marking to be 1. Given a trivializing unit modulo h^n, lift it as ordinary invariant chart-unit data to order n+1. Applying it to the automorphism leaves one literally identity modulo h^n. The top-order argument of PR438 removes that remainder by a unit identity modulo h^n. Composition gives a trivializing unit at order n+1 restricting to the chosen one. Its coefficientwise limit is a valid formal unit. Every coefficient uses finitely many operations and has finite differential order. This is the ordinary-unit version of PR436 Section 6.1, not an inference from finite pi_1 alone.

Let C_i be a 2-automorphism of an identity gauge. Then

    Ad_i(C_i)=id,      C_i=F_ij(C_j),      C_i=1 modulo h^M.

Inductively, after the lower coefficients are common scalars, the next gluing equation says the next coefficient is a global regular function on X: all normalized positive-order coefficients of the unital maps vanish on constants. Connected properness gives H^0(X,O_X)=C. Thus every C_i is the same scalar formal unit. Conversely all such units are central and glue. The finite proof is identical with truncation.

Consequently unrestricted pi_2 is the multiplicative group of scalar units 1+h^M C[[h]], identified by logarithm with

    A = h^M C[[h]],
    A_n = h^M C[h]/(h^n)                             (finite case).

Transport by any marked gauge acts identically on these scalar groups, because its chart algebra maps are unital and C[[h]]-linear. On logarithms the involution acts as

    j(c(h)) = -c(-h).                                 (4)

Indeed I(C)=tau(C^{-1}). Thus j^2=1, the groups are uniquely 2-divisible, and

    A^j = product_{r>=M, r odd} C h^r.

In particular the involution on pi_2 is not merely tau. All subsequent computations may be made additively in A or A_n.

We also use the unitary-category results of PR436: finite and formal relative pi_1 in R vanish, and its pi_2 is precisely exp(A^j). The ordinary and unitary 2-unit conventions must not be interchanged in the comparison.

## 3. Strictifying coherent objects

A coherent object (x,u,a) has reversal-fixed underlying object class. PR444 therefore supplies a strict parity object p and a marked equivalence g:x->p. Transport (u,a) along g. The resulting 1-arrow is

    v=(I g) u g^{-1}:p -> I p=p,

with square cell transported by whiskering from a. The cancellation of g^{-1}g and I(g^{-1})I(g) gives a coherent square cell; applying the strict 2-functor I preserves (1). This is transport of an existing structure, not an assertion that an arbitrary gauge already commutes with reversal.

By Section 2, v is 2-isomorphic to id_p. Pasting such a trivialization and its I-image into the square cell replaces the coherent object by one of the form (p,id_p,a_0). Equivalently, this is transport across an isomorphism of its chosen u-arrow in the definitions (1)--(3); invertibility of the 2-cell ensures an equivariant equivalence. Equation (1) now reduces exactly to

    j(a_0)=a_0.                                      (5)

The element a_0 is a scalar 2-unit logarithm, not a chart-dependent cochain. For the identity underlying gauge between (p,id,a_0) and (p,id,a_1), a comparison cell with scalar logarithm d satisfies (2) precisely when

    a_1 = a_0 + d + j(d).                            (6)

Set d=-a_0/2. Equation (5) gives a_1=0. Hence (p,id,a_0) is equivariantly equivalent to the strict coherent object (p,id,id).

This proves essential surjectivity onto coherent objects. Conversely, if an unrestricted object's class is fixed, PR444 supplies p and g as above. Transporting the strict coherent structure of p back along g gives a coherent structure on x. In fact its comparison arrow can be chosen as (I g)^{-1}g and its square cell is the literal cancellation identity. Therefore existence is equivalent to the fixed-class condition; no additional coherence obstruction remains.

The calculation (6) is the explicit vanishing of A^j/(1+j)A. It uses the actual scalar group and division by two, not an assumption that every group-cohomology obstruction vanishes without checking its coefficient action.

## 4. Equivariant arrows and their 2-automorphisms

First take a strict coherent object p. An equivariant automorphism has underlying gauge f:p->p and comparison eta:f=>I f. Section 2 supplies a 2-isomorphism from f to id_p. Transport eta through it using (3). The normalized comparison is then a scalar logarithm d, and the coherence (2) is

    d+j(d)=0.                                        (7)

A scalar 2-cell with logarithm c from the normalized underlying identity to itself changes that comparison, by (3), to

    d' = d+j(c)-c.                                   (8)

Choosing c=d/2, equation (7) makes d'=0. Thus every equivariant relative automorphism is equivariantly 2-isomorphic to the identity. The construction is valid at each finite order and directly for formal scalar series; division by two preserves every h-adic filtration and the initial marking.

The 2-automorphisms of the equivariant identity satisfy (3) with both comparison cells trivial, so they are exactly c with j(c)=c. This gives precisely exp(A^j), not the zero group.

The calculation (7)--(8) is the explicit vanishing of ker(1+j)/im(j-1). It also shows that any two allowed comparison cells on a fixed underlying gauge are related by a 2-isomorphism once they exist: their ratio, transported to a scalar 2-automorphism, is anti-fixed, and half of its logarithm gives the correction. Scalar identification is independent of a chosen 2-isomorphism because gauge transport on scalars is trivial.

For completeness, consider a specified underlying gauge f between two coherent objects. Section 3 replaces each endpoint equivariantly by a strict coherent parity object p or q. Their underlying classes are equal in U. PR438's injectivity on object classes provides a parity gauge k:p->q, which is an equivariant arrow with trivial comparison. Compose it with the endpoint equivalences to obtain some equivariant arrow with the same original endpoints. Its underlying gauge and f differ by a relative unrestricted automorphism; Section 2 supplies a 2-isomorphism between them. Transport the equivariant comparison across that 2-isomorphism by (3). This equips the specified f with coherent comparison data, proving assertion 4 without assuming that f is literally parity.

## 5. Local equivalence and the biequivalence

For two parity objects p,q, the ordinary hom-groupoid in R is empty exactly when no parity equivalence exists. If the coherent hom-groupoid between their strict images is nonempty, its underlying gauge makes p,q U-equivalent; PR438 then gives a parity gauge. Thus the two hom-groupoids are empty in precisely the same cases.

If nonempty, the R hom-groupoid is connected, since two parity gauges differ by a relative parity automorphism and PR436 makes it 2-trivial. Its 2-automorphism group at any gauge is exp(A^j), by scalar transport. The coherent hom-groupoid is likewise connected by Section 4 and has the same 2-automorphism group. The natural functor sends each scalar unit to exactly that same scalar unit. It is consequently an equivalence of these hom-groupoids: every object in the target is isomorphic to the image of one parity gauge, and the map on each isomorphism torsor is bijective because it is bijective on its automorphism group.

Combining local equivalence with the essential surjectivity of Section 3 proves the claimed biequivalences. At finite order replace A by A_n throughout. At the formal level the compatible-unit construction of Section 2 and coefficientwise scalar corrections prove the assertions directly; no interchange of homotopy fixed points and inverse limits is assumed.

## 6. Contribution and boundaries

PR444 identifies the reversal-fixed locus of marked object classes but leaves coherent involutive 2-actions open. The present proof settles that specific enhancement: strict parity data model all normalized coherent reversal objects and arrows up to biequivalence. Coherence contributes no extra object-class or 1-automorphism ambiguity, while the odd scalar pi_2 survives exactly.

The result is not a claim that an arbitrary reversal equivalence is literally square-one, that a chosen structure is unique as written, or that its equivariant automorphism 2-groupoid is contractible. It does not apply to initial-marking changes, arbitrary geometric automorphisms, non-invariant gauges, characteristic two, or coefficient groups lacking unique division by two. It retains the same literal ambient-lifting premise as PR444.

The fixed HM endpoint Q, selected source classes, six pure conditions, first-star and higher-star module lifting, periods, analytic convergence and algebraicity remain separate and unresolved by this argument. No source instance, multiplication matrix, detector, rank sample, generator or checker is evaluated. The proof is structural mathematics, not formal machine verification.

## Exact public dependencies

- PR444, commit `49ea1a16791fabbbfd6f8642854405446e98b2bd`, Sections 2 and 5--6: exact covariant involution on presentations/gauges/2-units, strict fixed-data identification, and finite/formal fixed-class normal form.
  https://github.com/Akilleez-QA/read-em-and-weep/blob/49ea1a16791fabbbfd6f8642854405446e98b2bd/research/hm/reversal-fixed-normal-form/PROOF.md
- PR438, commit `971c16a67b1e7d12fce0a8e2d2165ca4839911de`, Lemma 2.1 and Theorems 3.2,4.2: full finite unrestricted relative automorphism triviality and finite/formal forgetful injectivity.
  https://github.com/Akilleez-QA/read-em-and-weep/blob/971c16a67b1e7d12fce0a8e2d2165ca4839911de/research/hm/formal-forgetful-comparison/PROOF.md
- PR436, commit `502c978a17cd7037d740d4d08d373c1cb8bd5829`, Sections 3 and 6: parity relative automorphism triviality, compatible formal corrections and scalar pi_2.
  https://github.com/Akilleez-QA/read-em-and-weep/blob/502c978a17cd7037d740d4d08d373c1cb8bd5829/research/hm/formal-parity-tower/PROOF.md
- The retained literal lifting premise is PR416 at `c71356722bc7bd1a426d26ea0ca6d050f4c3ed81` and its pinned input:
  https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6259748725

Current PR1 and PR440--445 were inspected on 2026-10-20. This is a bounded comparison with the exact cited results, not an exhaustive repository or literature novelty claim.
