# Deck-character Euler index: consistency and exact S4 degree-three target

## Result

The conditional physical identification F=N tensor f*E, with E represented by the specified four-term complex, gives full-deck-sign Euler characteristic 274 for End(F), and 273 for End_0(F). The total, across all sixteen deck characters, is 7200 for either End or End_0. There is no discrepancy with the previously reported full-sign H2 dimension 352: its published companion degrees are H3=79 and H4=1, and 352-79+1=274.

With the genuine factor-permutation action, the full-sign virtual S4 characters are

- End: (274,86,-26,-26,-4)
- End_0: (273,87,-27,-27,-3)

in conjugacy order identity, transposition, double transposition, 3-cycle, 4-cycle. Importing the published H2 representation and full-sign H1=0 recovers

    H3(End_0 F)_fullsign = 24 sign + 15(V tensor sign) + 5 U22.

Its dimension is 79 and character (79,-39,19,19,-9). This is also H3(End F)_fullsign. The inspected small-certificate source states the degree-three dimension and its D8 epsilon multiplicity 29; it does not explicitly print this full S4 decomposition. The decomposition follows independently from its displayed twist-one groups and from the Euler check here. This is an index consistency review, not a new rank computation or a new proof of 352.

## 1. Matched objects and evidence boundary

The [pinned global-Hom proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/4659e4425c6b5ab6b1899e6af93656ac03ff0862/research/hm/null-cm-global-hom/PROOF.md) identifies the physical complex as N tensor f*K with

    K^-1=5O(-1), K^0=15O, K^1=10O(1), K^2=2O(2).

Its conclusion that this is quasi-isomorphic to a rank-two bundle retains the imported exact A-identity receipt and stated global geometric identification. Those conditions are not removed here.

The older pinned ext-model.md defines C:y²=x³-x, X=C^4, q:X->Y=(P1)^4 as the x maps, rho:Y->P4 as the elementary symmetric quotient, f=rho q, and the physical object as f*H tensor N. Its section 1 specifies exactly the above degree/twist/rank complex and physical powers (-1,1,3,5). The newer Perfect-Complex-D8-F3.md defines L by those same four terms and pinned integer maps, P=f*L, and explicitly says its Ext dimensions are unchanged by a line twist. Thus the source objects and the intended degree conventions agree; the 352 does not arise from a different indicated degree or a differently twisted endomorphism bundle. We inspected the older source's coefficient-construction text but did not regenerate it or execute a coefficient comparison against the later JSON. Identification with the exact current frozen model remains the stated pin/geometric premise, rather than an unperformed new coefficient audit.

For Euler characteristics alone, the maps need not be evaluated: the index follows from the four terms of the perfect complex. For ordinary bundle H^j(End F) language, retain the local quasi-isomorphism/bundle premise. For the derived perfect-complex endomorphism object the same virtual-index computation is valid without bundle exactness.

## 2. Deck eigensheaves and the scalar correction

For one elliptic double cover pi:C->P1, pi_*O_C=O plus O(-2). The second summand is deck odd. Its finite-chart generator is y, and the infinity-chart regular generator is y/x²; this gives the degree -2 transition. Tensoring the four double-cover algebras gives

    q_*O_X = direct sum over S of O_Y(-2S).

The equivariant identification End(N tensor f*E)=f*End(E) is canonical: the line-factor linearization cancels between source and target. With the divisor-induced deck linearization of N, the squared-line identification N²=f*O(1) is deck even. No extra odd character is introduced by the physical N twist.

Internal Hom of the pulled-back four-term complex has terms

    A^p = O_Y(p,p,p,p)^(m_p),
    (m_-3,...,m_3)=(10,80,245,354,245,80,10).

For |S|=k its Euler characteristic is therefore

    chi_S = sum_p (-1)^p m_p (p-1)^k (p+1)^(4-k).

Here chi(P1,O(n))=n+1 for every integer n, including -1 and all negative n. The five weight values are (274,446,514,446,274), giving

    274+4*446+6*514+4*446+274=7200.

The scalar summand has one dimension in cohomological degree k for each character S, so its Euler characteristic is (-1)^k. Since rank two is invertible, trace splits End=O plus End_0. The tracefree weight values are (273,447,513,447,273). Their binomially weighted sum is again 7200, since chi(O_X)=0. In particular full-sign scalars contribute in degree four, not degree two or degree three.

## 3. Canonical characters and S4 signs

The full deck-sign eigensheaf L_chi=O_Y(-2,-2,-2,-2) has the ordinary product linearization: y1 y2 y3 y4 is invariant under permuting factors. The canonical sheaf omega_Y has the same underlying line bundle but its natural action is the product linearization tensor S4 sign, because a transposition reverses the wedge of four one-forms. Consequently

    R^j Gamma(Y, g*End(E) tensor L_chi)
      = H^(4-j)(Y,g*End(E))^* tensor sign

under equivariant Serre duality and the canonical self-duality of End. Equivalently, omega_X is non-equivariantly trivial, but its chosen volume product(dx_i/y_i) has full deck character and S4 sign. Dropping either character is an equivariant error.

One can derive the virtual S4 index directly without using any cohomology ranks. For a permutation with c cycles and sign epsilon, in internal degrees -3<=p<=0 the line O(p-2) has only H1 on each factor, of dimension 1-p. The fourfold tensor permutation includes its Koszul sign epsilon. Its trace in H4 is therefore epsilon*(1-p)^c. At p=1 there is no cohomology; p=2 gives the trivial one-dimensional H0 tensor; p=3 gives H0 dimension two on every factor. Thus

    chi_End(g)=epsilon*sum_(p=-3)^0 (-1)^p m_p (1-p)^c +80-10*2^c.

This yields the character stated above. The scalar full-sign H4 carries sign, so the tracefree virtual character subtracts (1,-1,1,1,-1), not the trivial representation.

## 4. Reconciliation with the old 352 and stronger representation check

The small certificate explicitly gives full-sign Ext degrees (0,0,352,79,1). On P4 its four twist cohomologies in degrees 0..4 are

    t=0:  (1,24,2,0,0)
    t=-1: (0,5,10,0,0)
    t=-2: (0,0,20,0,0)
    t=-3: (0,0,20,0,0).

With W0=1, W1=3V+U22, W2=3(V tensor sign)+U22, W3=sign, projection formula gives trivial-deck H1=24*1+5W1. Serre duality therefore gives full-sign H3=24sign+15(V tensor sign)+5U22, as found by the index calculation.

The imported full-sign H2 is 20*1+60V+30U22+30(V tensor sign)+2sign, character (352,48,-8,-8,-12). Since H0=H1=0 and the scalar splitting removes H4, subtracting the tracefree index from this H2 character gives exactly the H3 character above. Its D8 epsilon multiplicity is 24+5=29, agreeing with the source's explicit degree-three epsilon result. If one does not admit the historical H1=0 calculation, the index alone gives only a constraint on the alternating sum; with tracefree H0=H4=0 it determines H1 direct sum H3, not H3 alone.

No vanishing of an actual obstruction or retained detector follows from these index equalities.

## Sources and performed checks

- [Global-Hom proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/4659e4425c6b5ab6b1899e6af93656ac03ff0862/research/hm/null-cm-global-hom/PROOF.md) and [root-line geometry](https://github.com/Akilleez-QA/read-em-and-weep/blob/4659e4425c6b5ab6b1899e6af93656ac03ff0862/research/hm/null-root-line-geometry/PROOF.md).
- https://github.com/Akilleez-QA/read-em-and-weep/blob/add03476d9055aa00e1e00778eea6332cf8e01cc/research/hm/ext-model.md ; fetched blob fad0e87f0e30ec916e18fd47feea584c7d8eaae6.
- https://github.com/Akilleez-QA/read-em-and-weep/blob/add03476d9055aa00e1e00778eea6332cf8e01cc/research/hm/verify-hm-ext.js ; only source lines 1-28 fetched/read, blob fa5231de92b61143e3406111d4af028284db6d55. No execution.
- https://github.com/Akilleez-QA/read-em-and-weep/blob/f968b53943ba2312f09fbc3e8f9d462e86bcaa34/research/hm/d8-small-certificates/p4/Perfect-Complex-D8-F3.md ; fetched blob 3a8c3633e83466b29ea2e5739c6b486f856b91b2.
- [Permutation-sector proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/4659e4425c6b5ab6b1899e6af93656ac03ff0862/research/hm/null-permutation-sector/PROOF.md) for the already established characteristic-zero S4 decomposition.

The original check used only integer Euler/character arithmetic. The previously published source documents are linked above rather than duplicated; integer-results.json preserves the reported character check. No physical source or jet values were evaluated.
