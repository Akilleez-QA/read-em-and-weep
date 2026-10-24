# The top-degree-three boundary has one source, one quotient, and three kernel shapes

## 1. Precise conditional statement

Use the actual saturated plane-section inclusion E in H O on the original physical binary-icosahedral parameter line P(W*), over C, with dim H=30. Assume generic derivative rank four and maximal ordered plateau (1,1). Put S=Q*, K=E^-, L=S^-, A_q=E/K, B=S/L. The ranks of E,S,K,L,A_q,B are 17,13,13,9,4,4 respectively, with deg E=deg S=-54. Write a=deg A_q, b=deg B and t=-8-a-b>=0. All maps are the actual second fundamental forms and their coherent images; no image saturation or zero-defect assumption is made.

Retain the same actual geometric and four-source premises as PR1185 at 236e0a3723c3d73ea7fb9e549376540a8e70508b, research/hm/rankfour-profile11-low-top/PROOF.md. That proof establishes maxdeg A_q>=3. Here we treat precisely the boundary

    max ordinary degree(A_q)=3.

Then necessarily the actual source is E_D and

    A_q = W O(3)+O(2)+O(-8).                            (T1)

The actual derivative kernel K has exactly one of these three necessary equivariant splitting shapes:

    K_T = S4 O(-3)+V O(-4)+T6 O(-5),
    K_W = S4 O(-3)+(V+P)O(-4)+W' O(-7),
    K_1 = S4 O(-3)+(V+D)O(-4)+O(-10).                   (T2)

These are necessary bundle identities, not occurrences, not actual-map constructions, and not a profile closure. We do not assert that the remaining determinant defect vanishes. No coarse rank-four label is removed and no new global rank bound follows.

Nine full immutable inputs are retained in INPUTS.json. The eight original actual, ambient, strict-top, source, double-channel, capacity, rank-strata and physical-character files are identical to the freshly authenticated copies in the preceding packet. The new low-top proof was fetched directly from its published immutable head and authenticated. Its actual-source dependencies remain explicit; a source byte hash is not a proof of its transitive geometry.

Our representation notation is A_std=Sym2 W, S4=Sym3 W, D=Sym4 W, T6=Sym5 W. The other three-space is V, the even four-space P, and the other doublet W'. All are self-dual. The actual sources are

    E_D=D O(-2)+(W'+T6)O(-3)+V O(-4)+O(-8),
    E_P=P O(-2)+(W'+T6)O(-3)+V O(-4)+W' O(-5),
    E_V=V O(-2)+(W'+T6)O(-3)+2V O(-4),
    E_Z=(W'+2T6)O(-3)+V O(-4).

The double-channel theorem gives W'+2T6 inside H0(A_q(3)). It also gives H0(K(3)) equal to 0 or S4 in source D, 0 or W' in source P, and zero in V or Z. Strict top gives maxdeg K<=-3. The preceding capacity proof gives, with u=maxdeg A_q and v=mindeg A_q,

    a+13u>=16,   a+9v<=-8-t,   v<=-1.                  (1)

Only these already-proved consequences are imported from that proof; no historical quotient enumeration is used.

## 2. Four possible quotients from actual low-slope maps

Since the top ordinary degree is three, its coefficient representation is center-odd. An irreducible dimension-four top block would fill the whole quotient, contradicting v<0. Thus the positive block is R O(3), with R=W or W', and the remaining bundle C has rank two.

If C is a doublet R' O(e), e is odd and negative. The possibility e=-1 has a=4 and v=-1, violating a+9v<=-8-t. Hence e<=-3. Since A_q is a quotient of E and E(8) is generated, e>=-8; thus e is -7,-5 or -3.

The complete small source-Hom calculation in this range has the following nonzero entries; all unlisted Hom spaces vanish:

    Hom_G(E_X,W' O(-3))=C for X=D,P,V,Z;
    Hom_G(E_P,W' O(-5))=C;
    Hom_G(E_D,W O(-7))=C.

The last map is supported solely on the source O(-8), so has rank at most one and cannot be the surjective projection onto a rank-two quotient block. The first Hom comes solely from the displayed W' O(-3), and the second solely from the displayed W' O(-5). Thus C can only be W' O(-3), or W' O(-5) with source P.

If C is the sum of two scalar blocks, at least one has negative even degree. The source Hom test from the preceding proof leaves only O(-8), forcing source D. The other scalar cannot have degree -6,-4,-2 or 0: every Hom from every actual source to these scalar bundles is zero. Nor can it be a second O(-8), since only one source line can supply the two-dimensional quotient. Therefore the second scalar is O(2).

The cubic identities

    H0(W O(6))=W'+2T6,
    H0(W' O(6))=W+W'+S4+T6

show that only R=W can occur with a negative doublet: W' O(-3) contributes W' but no T6, and W' O(-5) has no cubic sections. With the scalar complement O(2)+O(-8), the O(2) contributes one T6 and both positive doublets pass this preliminary condition.

Consequently exactly four written quotient shapes remain at this step:

    Q_a = W O(3)+W' O(-3),                all source labels initially;
    Q_b = W O(3)+W' O(-5),                source P only;
    Q_c = W' O(3)+O(2)+O(-8),             source D only;
    Q_d = W O(3)+O(2)+O(-8),              source D only. (2)

This is a symbolic rank/parity/source-map derivation. The fixed Hom products have symmetric degree at most eight; no global bundle-candidate search is used.

## 3. Two actual derivative coefficient constraints

First, strict top applied to K gives top K^-<=-4. Its actual derivative lands in A_q(-2). Hence

    H0(K(3)) embeds in H0(A_q(1)).                      (3)

This is coefficient-space injectivity, not a fiberwise rank assertion.

Second, choose an equivariant Birkhoff splitting

    K = R3 O(-3)+R4 O(-4)+N,

where every N degree is at most -5. The restriction of the ACTUAL derivative to the displayed R4 block gives an injective coefficient map

    R4 -> H0(A_q(2)).                                  (4)

To prove this without declaring any splitting horizontal, suppose a nonzero coefficient vector is killed. Its line O(-4) is a saturated direct summand of K, hence saturated in the original constant ambient. The quotient of K by that line has top degree at most -3. The line's actual second fundamental form, because beta_K kills it, lands in this quotient twisted by -2. Every target degree is at most -5, so Hom(O(-4),(K/O(-4))(-2))=0. The line is horizontal and therefore constant in characteristic zero, contradicting its degree -4. This proves (4), including coefficient combinations among repeated irreducibles.

Equivariant semisimplicity now lets us compare every R4 multiplicity with the corresponding H0(A_q(2)) multiplicity. Formula (4) also applies when R3=0; no saturation of the image in A_q(-2) is needed.

## 4. A small cohomology table, not a splitting search

The four actual sources have the same Euler characters

    chi_G(E(3))=W'+2T6,
    chi_G(E(4))=3V+3P+2D.

Subtracting the quotient characters gives this complete table:

    quotient   chi_G(K(3))   chi_G(K(4))          H0(A_q(2))
    Q_a        -W'          2V+D                 D+V+P
    Q_b        W'           [not needed]         D+V+P
    Q_c        -W           D+V+P-1              A_std+2D+P
    Q_d        S4-T6        A_std+D+V            2D+V+P.     (5)

For N as in Section 3, Serre duality and self-duality give

    H1(N(3)) = sum_(R O(-j) in N) R tensor Sym^(j-5) W,
    R4 = chi_G(K(4))-R3 tensor W+H1(N(4)).               (6)

All terms in the first formula are genuine. In every case below its total dimension is at most six. Therefore an irreducible block has (j-4)dim R<=6 and 5<=j<=10. The entire relevant universal block table is:

    block             H1(block(3))       H1(block(4))
    W O(-5)           W                   0
    W' O(-5)          W'                  0
    S4 O(-5)          S4                  0
    T6 O(-5)          T6                  0
    O(-6)             W                   1
    A_std O(-6)       W+S4                A_std
    V O(-6)           T6                  V
    W O(-7)           W+S4                1+A_std
    W' O(-7)          T6                  P
    O(-8)             S4                  A_std
    O(-10)            T6                  D.            (7)

Every other block with the proved dimension bound and correct central parity either exceeds the available dimension or contributes a forbidden constituent. The requested characters below are W', W, S4+W', S4+W, or T6. Their exact decompositions into (7) are immediate from the multiplicity-one W', W and S4 columns, or irreducibility of T6. This is a fixed universal representation table with a proved six-dimensional bound, not an empirical cutoff or a global enumeration of K or A_q.

## 5. Exclude the negative-doublet quotients

For Q_b, source P and (5) force H0(K(3))=W' and H1(K(3))=0. But H0(Q_b(1))=S4+T6, which lacks W'. This contradicts the actual injection (3). Thus Q_b is excluded.

For Q_a, H0(Q_a(1))=S4+T6 also excludes the possible P-source W' cubic kernel. The remaining alternatives for R3=H0(K(3)) are 0 or S4, the latter only in source D.

If R3=0, (5) gives H1(N(3))=W'. Table (7) forces N=W' O(-5), with H1(N(4))=0. Formula (6) gives R4=2V+D. Its two V copies cannot inject into H0(Q_a(2))=D+V+P. This contradicts (4).

If R3=S4, then H1(N(3))=S4+W'. There are just two possibilities in (7):

    N=S4 O(-5)+W' O(-5),    or N=O(-8)+W' O(-5).

Since S4 tensor W=A_std+D, formula (6) gives respectively R4=2V-A_std or R4=2V. The former is not genuine. The latter again has two V copies against one in the target of (4). Thus Q_a is excluded for every source.

## 6. Exclude the positive W' scalar quotient

For Q_c the source is D, so R3 is 0 or S4.

If R3=0, (5) gives H1(N(3))=W. Table (7) leaves W O(-5) or O(-6). Their H1 at twist four is respectively 0 or 1. Formula (6) gives R4=D+V+P-1 in the first case, not genuine, or R4=D+V+P in the second. The latter contains V, whereas H0(Q_c(2))=A_std+2D+P has no V. Thus (4) excludes it.

If R3=S4, then H1(N(3))=S4+W. The six possibilities in (7) and their H1(N(4)) are

    S4 O(-5)+W O(-5)       -> 0,
    S4 O(-5)+O(-6)         -> 1,
    O(-8)+W O(-5)          -> A_std,
    O(-8)+O(-6)            -> A_std+1,
    A_std O(-6)            -> A_std,
    W O(-7)               -> A_std+1.

Here (6) says R4=V+P-A_std-1+H1(N(4)). Only the fourth and sixth rows make it genuine; both force R4=V+P. This again contains V, absent from the target of (4). Thus Q_c is excluded.

## 7. The remaining quotient forces precisely three kernel shapes

Only Q_d remains, proving (T1). Its source is D. By (5), the positive S4 Euler constituent forces R3=S4, and then H1(N(3))=T6.

Irreducibility of T6 and table (7) leave exactly four possibilities:

    N=T6 O(-5),  V O(-6),  W' O(-7),  O(-10).

Using chi_G(K(4))=A_std+D+V and R3 tensor W=A_std+D, formula (6) gives respectively

    R4=V,  2V,  V+P,  V+D.

The second option has two V copies, whereas H0(Q_d(2))=2D+V+P has only one. It violates (4). The other three give exactly (T2). Their ranks are13 and degrees are-54, as required by a=0. Passing the displayed necessities does not establish actual realization of any of them.

## 8. Contribution and verification boundary

The preceding proof excluded the whole sublocus maxdeg A_q<=2. This separate theorem determines the next top-degree boundary without searching a global quotient domain: the actual source and quotient are forced, then small genuine cohomology and an actual near-top derivative obstruction reduce the kernel to three explicit shapes.

The unresolved tasks are to determine whether any of these three actual image/filtration configurations exists and to treat higher top quotient degrees. The full rank-four (1,1) profile remains open, as do the independently owned other rank-four profiles. No new coarse-bin exclusion, generic rank bound, square surjectivity, full-adjoint invertibility, smoothing, algebraicity or original repair is claimed.

No actual source coefficients, points, parameters, jets, tensors, instance matrices/ranks or scans are used. Universal character products, bounded scalar/doublet Hom tests and the dimension-six table are the only computations. The actual geometric and source premises are imported explicitly; neither byte authentication nor character arithmetic is proof-assistant certification of them.
