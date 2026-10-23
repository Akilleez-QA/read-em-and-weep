# The split bf source is excluded by the exact split-descent interface

## Statement

For the original-zero-defect profile-(1,1) label

    G3.11.863639aa192e, source_index=69,
    A_q=O(-10)+O(4)+O(6), B_q=O(-8)+O(-6)+O(8),

the source tuple (0,1,0,0,0,1,0,1), with actual bundle

    E=(P+D) O(-2)+T O(-3)+O(-8)+O(-10),

is impossible. Its rank is 9+6+1+1=17 and degree is -18-18-8-10=-54. This is a whole-source exclusion, not an entire-label or global-frontier assertion.

## Dependencies and exact versions

The original actual-bundle and source-list inputs are pinned at commit db51525015bb7c5e825833d550d08dedf6f6ea96 in [research/hm/order-four-quadratic-load](https://github.com/Akilleez-QA/read-em-and-weep/tree/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load).

The rank-two top branch is excluded by the combination of:

- [PR814's polar proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/1f94be65b3a470a1b594e61d56df7f6057c9d907/research/hm/profile11-low-positive/PROOF.md), commit 1f94be65b3a470a1b594e61d56df7f6057c9d907, SHA256 f0bd13d85ae8a890dbec84e5f15b7ec8605b04f474d5c7d80faeb3aa08f4defc;
- [PR830's split nonzero-channel exclusion](https://github.com/Akilleez-QA/read-em-and-weep/blob/620d5598ccc19e5e1c458a4cddb0d3a0709d83c3/research/hm/profile11-split-bf-rank-two-exclusion/SPLIT-BF-RANK-TWO-NONZERO-CHANNEL.md), commit 620d5598ccc19e5e1c458a4cddb0d3a0709d83c3, SHA256 d762e23c6b402bf8bfd62160e310ecacf601a910d47f6a3e278cd8a3806657f6.

For rank one, the two companion theorems used here are exactly:

- SPLIT-BF-BACKWARD-INTERFACE.md, SHA256 b5924ec48fe1dd7583b37d75d47b8ef1ec3f0b3a589744349ebf924c08de4a61;
- SPLIT-BACKWARD-DESCENT.md, SHA256 ee1096f2368fee248792c35feeb3c689a134b8e1a84934c9699575fbe920ee1a.

These companions must accompany this corollary in the same publication or be pinned immutably. The first establishes a forced subsystem only; the second is a source-free obstruction conditional on an actual split-connection interface. This corollary verifies their composition.

## Complete branch partition

Set F=(P+D) O(-2) and K_i=E^{(-i)} for the successive actual Gauss kernels in the fixed constant ambient bundle H O. The strict-top theorem injects the nonzero space H0(E(2))=P+D into the top quotient sections. Hence the top image is not rank zero.

If it has rank two, the nine independent sections generate an image I with I(2) globally generated and

    9 <= h0(I(2))=16-delta,

where delta is its determinant defect in O(4)+O(6). Thus delta<=7. An invariant nonzero effective divisor has degree at least twelve, so delta=0. The top map is onto. PR814 excludes the zero internal derivative channel; PR830 excludes every nonzero internal channel. This exhausts rank two without assuming one selected internal component is nonzero.

If the top image has rank one, the interface theorem proves that it is the complete O(6) direct summand, and proves the exact raw backward quotient

    K_1/K_2=O(2)+O(4).

In particular this quotient is saturated and has no hidden divisor correction. Its same theorem gives

    rank K_2=12, deg K_2=-60, maxdeg K_2<=-4,
    chi_G(K_2(4))=V-A,
    chi_G(K_2(5))=-W+Wp+2T.

The next actual derivative factors through

    (K_1/K_2)(-2)=O(0)+O(2).

This factorization has the exact geometric meaning required by the universal theorem. The inclusion K_1/K_2 -> H O/K_2 is a subbundle because its quotient H O/K_1 is locally free: K_1 is an actual saturated Gauss kernel. After twisting by -2, the displayed split target is therefore an actual subbundle of (H O/K_2)(-2). Its induced map from K_2 has precisely the actual derivative kernel and raw image.

All subsequent kernels are actual saturated negative subbundles of the same constant bundle, and the usual Gauss factorization through the preceding actual quotient holds. The original profile-(1,1) endpoint bounds these backward derivative ranks by two; the ranks are nonincreasing. Thus every hypothesis of SPLIT-BACKWARD-DESCENT.md is satisfied, with the same K_2 and the same actual connection. That theorem gives a contradiction. No balanced target, horizontal splitting of E, or replacement of a raw image by its saturation is used in this transfer.

Rank zero, rank one, and rank two are now all excluded. The stated split bf source is therefore impossible.

## Scope

This corollary combines structural theorems and verifies their geometric interface. It does not independently exclude any other source or assert a whole-label count. It uses no selected HM/source coefficients, parameters, points, evaluated derivatives, matrices, instance ranks, selected-model experiments, scans, or unapproved large computation.
