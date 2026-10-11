# Independent review of the plane-completion lemma

Reviewed 2026-10-11, against the fixed model at `6b69eefd57098d9a0c1d9f43ed993d36e1e54bcb`, `research/carrier/formal-five-parameter-chart/formal-chart.md`.

## Verdict

The displayed presymplectic rank-three bundle G has an algebraic rank-four L-valued symplectic completion, unique up to unique isometry fixing G and its canonical P–D pairing. The precisely stated rank-five presentation retaining the given B, A and quotient D is impossible. These assertions are compatible: quotienting the locally presented radical can permit descent even though the rank-five presentation does not descend.

This does not identify an omitted ancestor or a prescribed first-normal jet, construct an algebraic carrier family, or establish any defect or zero-defect statement.

## Local signs and algebra

Use r=(r1,r2,r3) and Omega=[[0,r3,-r2],[-r3,0,r1],[r2,-r1,0]], with the relation (-a,r). For psi_i=a e_i*/r_i, a local form on B plus D with cross pairing P–D equal to 1 and E–D equal to psi_i has radical exactly A. Pairing against P first forces the D coordinate of a radical vector to vanish; rank two of Omega then forces its E part to be a multiple of r, and pairing against D determines its P part.

For maps from chart j to chart i fixing G, the D lift changes by t_ij with Omega t_ij=psi_j-psi_i. The cyclic choices

- t12=a e3/(r1 r2)
- t23=a e1/(r2 r3)
- t31=a e2/(r3 r1)

give t12+t23+t31=a r/(r1 r2 r3)=a²P/(r1 r2 r3) in G. Adding P-valued corrections whose sum is minus that scalar cancels the exact cocycle. Because all maps fix G, composing them adds those G-valued shifts; there are no uncomputed higher commutator terms.

Finite r=(W6,-g,F): a²=gC+z³W6+TF², T=-3S+2F. The manuscript's corrections TF/(W6 g), z³/(gF), C/(W6 F) have the stated cyclic signs and sum to minus the residual.

Infinity r=(S³,-uS+W²,F): a²=S³+TF². Corrections -TF/(r1r2), -1/(r2r3), 0 again sum to minus the residual.

An independent symbolic rational calculation verified all six pairing equations, both vector sums, both central cancellations and the finite polynomial identity: eleven exact checks, all zero. This used a separately written calculation rather than running the producing artifact's code.

All corrections have plane degree -4, as required for M=P²L^-1=O(2,-4). The opens where r_i is invertible cover: on the finite base, simultaneous vanishing forces W=XY=X²+Y²=0; on the infinity base, S=F=0 forces W=0. Both are impossible in P2, including after field extension.

## Global descent and uniqueness

For two completions of the same G, locally split their projections to D. The difference of their G–D pairing functionals vanishes on P and is therefore represented by Omega_G(-,t) for a local t modulo P, because G/P is symplectic. Thus an isometry fixing G exists locally. The remaining automorphisms are exactly D-to-P translations, namely sections of M=Hom(D,P). No D–D constraint remains: D has rank one and the forms are alternating.

Consequently the sheaf of such isometries is an M-torsor. On Gm×P2, both H0(M) and H1(M) vanish. The separately constructed finite/infinity base-chart completions therefore have a unique algebraic gluing isometry. The two-open base cover has no additional triple compatibility to establish beyond choosing inverses. The same H0/H1 vanishing on Y gives uniqueness fixing G.

The alternate H2 argument also checks: H2(Y,O(2,-4))=H0(P1,O2) tensor H2(P2,O(-4)), of dimension 9. Restriction to an affine base chart is injective. Its central obstruction is already zero there.

The cohomology vanishing used here follows from the projective-space formula over an arbitrary coefficient ring: https://stacks.math.columbia.edu/tag/01XT. The specific torsor and cocycle are derived above, rather than inferred only from a generic gerbe citation.

## Exact boundary of the rank-five obstruction

If Q contains this B, with quotient D=LP^-1, then Ext1(D,B)=H1(BPL^-1). The four filtration lines are O(2,-4), O(-1,-1), O(3,-5), O(2,-5); each has H1=0, so the actual extensions also have H1=0. Hence Q splits as B plus D.

An alternating form extending the given form on B and the canonical P–D pairing then determines a global psi:E to P. Its restriction to E0 vanishes since H0(O(3,-3))=0. It factors through E/E0; the E1 component vanishes since H0(O(-1,1))=0, while the E2 component is any linear form in X,Y,W. Thus psi(r)=linear(X,Y,W)·XY, which cannot equal X³+Y³. This proves nonexistence only for the exact retained-B/A/pairing presentation contract.

## Equivariance and local normal lifting

If compatible torus linearizations on G, P, L and the pairing are fixed, the algebraic completion admits a unique compatible linearization. Over T×Y, the two pullback completions differ by a torsor under the pulled-back M; H0 and H1 still vanish after the affine torus base change. The unique isometry satisfies the action cocycle by uniqueness on T²×Y. This conditional statement does not independently identify the intended source's linearizations or frame.

Locally splitting V to D also gives a correctly typed normal lift v_tilde=E0+q(t0 h), since t0 h is a section of D=O(1,1), with positive pairing beta(v_tilde)=t0 h. Its global descent and identification with the prescribed frozen first jet remain separate obligations.
