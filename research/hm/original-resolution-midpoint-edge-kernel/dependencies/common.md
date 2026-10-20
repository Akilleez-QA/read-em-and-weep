Editorial scope: This is a mathematical source edition. Historical review and check statements describe the original artifact, not a fresh run. Supporting snapshots are dependencies, not additional new results. Later PR145 mixed-class vanishing supersedes historical unknown mixed-class status; it does not resolve the six pure diagonal conditions.

Supporting dependency only: this complete source text is not a fresh result of this packet.

# Common original-resolution split connection and the exact second-stage derivative

## Checked result and boundary

The proposed connection is valid, conditional on the already declared primitive contraction/complex identities, common original-resolution identification, legal localization, and coefficient-derivation denotation. This is a formal source-specific refinement, not verification of actual primitive values or a vanishing theorem. Only supplied source text and formal algebra were used; no model, owner, source, jet, matrix-polynomial product, experiment was performed.

The supplied request context identifies PR1 comment 6249956567 and PR79 head 4c0e965b4de72e43c39ba863f9aa8eea15571851; this independent local audit does not freshly attest remote state. The static source is the frozen raw_engine.py in raw-first-order-transgression-public/inputs; the mathematical premises are scalar-frame-bridge-public/frame/PROOF.md, raw-first-order-transgression-public/PROOF.md (especially section 8), differentiated-contraction-transfer-public (including its HPL dependency), and inner-boundary-domain-public. These are conditional source/denotation premises; their presence does not establish fresh actual-model identities.

Write D for the common original-resolution differential, whose successive blocks are gamma, delta_K, ev; distinguish gamma from the scalar old-connection coefficient alpha. The complex degrees are −1,0,1,2, with line weights k=−1,1,3,5. Set rho=V(nu)/nu and beta=alpha−rho.

## 1. Exact common frames and constant split blocks

The source's local weighted frames are Id5, U0 S0, U1 S1, Id2, with U0=(gamma,I,H1W), U1=(W,eta), and weights exactly as in the frame bridge. Transport into the common original-resolution frame by multiplying the whole weight-k term by nu^k. The result is

    F_-1 = nu^-1 Id5,
    F_0  = (gamma nu^-1, I diag(nu,nu^-1), H1 W nu^3),
    F_1  = (W nu^3, eta nu^5),
    F_2  = nu^5 Id2.

Let Q0=(H0;P;L delta_K) and Q1=(L;ev). These supply the inverses with reciprocal column weights, under the imported identities. Thus the first pair has exponent −1 at both ends, the middle pair exponent 3, and the final pair exponent 5. Directly:

* gamma sends F_-1 to the first five columns of F_0;
* delta_K kills gamma and I and sends H1 W nu^3 to W nu^3;
* ev kills W and sends eta nu^5 to nu^5 Id2.

These are constant identity-pair differential blocks. The cohomology summand has columns A=I diag(nu,nu^-1), with B=diag(nu^-1,nu)P. The reverse identity-pair homotopy, transformed back to common coordinates, is precisely h=(H0,H1,eta): the scalar powers cancel on each pair, and H1WL=H1 follows from WL=1−eta ev and H1eta=0. Hence this is the SAME contraction used by the original-resolution HPL, not just a connection parallelizing the differently scaled local differential.

## 2. Literal raw blocks determine the common connection

Define Gamma_k=−V(F_k)F_k^-1. From F_k=nu^k F_local,k,

    Gamma_k = raw_moving_k − k rho Id
            = B_raw,k + k beta Id.

The source's scalar alpha and the curve logarithmic derivative give

    alpha=m y/[x(x²−1)],
    rho=m y(x²+1)/[2x(x²−1)],
    beta=−m y/(2x).

These identities refer to the same direction and legal-mask bit. At other representation charts they require the actual transported connection, not resetting coefficients to zero.

In particular Gamma_-1=rho Id5 and Gamma_2=−5rho Id2. The middle coefficients, without evaluating any matrix entries, are

    Gamma_0=−(V U0)Q0
       +rho[gamma H0 + I diag(−1,1)P −3 H1 delta_K],
    Gamma_1=−(V U1)Q1 −3rho WL −5rho eta ev.

Every derivative inside VU0 and VU1 remains, including V(H1W) and Veta. The diagonal cohomology weights cannot be replaced by a common scalar.

The common OLD connection is k beta Id; thus Gamma=B_raw+old_common, exactly as required. For owners i,j in one common ambient reference,

    Gamma_j,k−Gamma_i,k = B_raw,j,k−B_raw,i,k −(k/2)q_ij,
    q_ij=(m_j−m_i)y/x.

No conclusion that this overlap vanishes is made.

## 3. Induced End connection and parallelism

For an internal-degree-r map F:K^u→K^v define

    G(F)=Gamma_v F−F Gamma_u,     v−u=r.

G is degree zero, so every displayed operator commutator below is ordinary, with no additional Koszul sign. Since D and h have constant split matrices, and A,B are constant inclusion/projection matrices in the induced local cohomology frame,

    D′+[Gamma,D]=0,  h′+[Gamma,h]=0,
    A′+Gamma A=0,   B′−B Gamma=0.

The local cohomology connection is zero IN ITS OWN owner frame. It is not a global parallel trivialization across owners. For the actual End maps d,H,j,pi this gives

    d′=−[G,d],  H′=−[G,H],  j′=−Gj,  pi′=pi G.

Here j(R)=A R^t B and H_r(F)=hF+(−1)^r ABFh exactly as in the frozen HPL. In particular ordinary a=pi j′=−pi G j is generally nonzero, despite covariant a being zero. Row restrictions still vary; with fixed common ambient delta,

    Delta′=pi G delta j−pi delta G j=−pi[delta,G]j.

This explicitly prevents confusing local cohomology flatness with Delta′=0.

## 4. Exact overlap formula and second-stage derivative

For fixed common ambient restrictions set C=[delta,G]=delta G−G delta. On a cochain with output leading owner i0, all faces except the first retain that owner and cancel in this commutator. Thus

    (C X)_(i0...ip+1)
      =(G_i1−G_i0) X_(i1...ip+1),

with actual ambient restrictions/transport understood before subtraction. In a different ambient frame, the difference is transported G_i1 minus G_i0, and derivative-of-restriction terms must also be included. The first-face sign is positive. At the resolution block level the difference acts by (Gamma_i1,v−Gamma_i0,v)X−X(Gamma_i1,u−Gamma_i0,u).

Put J1=H delta j (the unsigned stage-one word) and J2=−H delta J1. Product differentiation gives

    J1′=−GJ1−HCj,
    J2′=−GJ2+HCJ1+H delta HCj.                 (A)

To check signs directly, substitute H′=−GH+HG and j′=−Gj; all adjacent G terms telescope except the exterior −GJ2 and the two delta/G commutators. This identity holds on nonclosed inputs and for every input Cech degree where the typed words exist. No Delta-closedness is used, and H is never moved past delta.

If ambient delta′ is nonzero, define C_eff=C−delta′. Equation (A) holds with C_eff in place of C, equivalently with the additional literal terms

    −H delta′ J1 −H delta H delta′ j.

## 5. Selector, inputs, and exact source blocks remain

For arbitrary selector L,

    (LJ2)′=(L′−LG)J2+LHCJ1+LH delta HCj.      (B)

For a varying input Z also add LJ2 Z′. Thus the selector connection LG is explicitly retained. It is not killed by Ld=0. At internal degree r, the raw-block expression is

    G(F)=B_raw,v F−F B_raw,u+2r beta F.

For J2, r=−2, so G(J2)=ad_(B_raw)(J2)−4beta J2. Hence even the scalar-by-weight part contributes to (B); ordinary coefficient trace cyclicity alone cannot remove a typed selector on maps between different complex terms.

With scalar output connection Gamma_S and row connection Gamma_R, the fully induced formula is obtained by adding Gamma_S LJ2−LJ2 Gamma_R to the left derivative and the matching terms to the selector/input Hom derivatives. The specialized proof above fixes Gamma_R=0 in the actual local cohomology frame and Gamma_S=0 in the chosen scalar reference; it makes no claim that either choice glues globally.

## 6. Relationship to the earlier boundary decomposition

The earlier ordinary primitive becomes explicit in the same raw blocks:

    t=−HGj, S=−HGH,
    U=−HGJ1+H delta HGj,
    a=−pi Gj.

Its covariant counterpart is zero because dot H=dot j=0. The prior ordinary U is NOT zero. Its existing regular-domain theorem still applies, with its original premises.

Let T=LJ2, Pi the ordinary partition comparison, and Pi′=delta Qdot+Qdot delta. Assuming fixed L and ambient restrictions, define

    R_conn=−LGJ2+LHCJ1+LH delta HCj.

Then the exact alternative to the earlier synthesis is

    (Pi T)′=delta(Qdot T)+(Qdot T)Delta+Pi R_conn.

This retains the outer boundary and its nonclosed-input defect. If instead retaining the earlier K=Qdot T−Pi LU, the connection/differential package must satisfy

    T a+LE = R_conn+delta(LU)+(LU)Delta.

Consequently one must not replace only Ta+LE by R_conn while leaving the earlier K unchanged: that would double-count the removal of the inner boundary and omit its nonclosed term. Either representation is exact, with all degrees interpreted as in the supplied synthesis.

## Untouched obligations

This reduces the inner derivative to explicit raw connection blocks, their first-face overlap, and the selector connection. It does not establish cancellation with the ten-term baseline or either Fk branch. Derivatives of p, current/source inputs, outer weights (unless processed through their existing partition identity), moving ambient restrictions, and moving selectors remain. Raw scalar leaves can remain in every displayed J word. The existing scalar-free current–F substitution applies only to the specified Delta Z subfamilies. No new global pole bound for separately expanded Gamma/overlap pieces is certified; equality preserves the complete expression, not arbitrary termwise regularity. No retained-test value, divergence certificate, or zero-obstruction conclusion follows.
