# Independent review: linear adjugate and embedded-node thickening

Status: PASS for the structural theorem and its projective scheme consequences, under the actual-module inputs stated below. Independently derived; not formally checked. This review uses no selected HM/source coefficients or matrix, numerical evaluation, numerical rank test, search, or large computation.

## 1. Inputs inspected and review scope

Work over P=C[x0,...,x4]. Let I=I_S be the actual prime surface ideal of height two, and J=I_Z the radical homogeneous ideal of the thirty projective nodes, of height four. Since Z is contained in S, I is contained in J.

The actual minimal resolution, not a proposed complex inferred from Hilbert data, is

0 -> P(-10) --c--> P(-7)^10 --L--> P(-6)^10 --f--> P -> A=P/I -> 0.

Here c is a column of cubics, L is linear, and f is a row of sextics generating I. The actual Ext identification is

Ext^3_P(A,P(-5)) = (P/J)(5)

up to graded P-module isomorphism. These inputs were checked in the local copies of the complete-primary-resolution proof (PR598, commit acbdc8ab66c42e3bb216304255a50a00128bd3bb) and conductor-canonical-module proof (PR596, commit c54a80181e0e63a9f6a7404c07c525db131e3590). The former proves A equals its complete section ring, allowing the latter's Ext calculation to be applied directly to A.

For the numerical local and Hilbert-polynomial conclusions, the inspected primary-conductor proof, pinned at commit 3c92fdc469f6870520e7a9d905b5ab9199a5bf37, supplies the completed ambient local model

Q=C[[u1,u2,v1,v2]],  I_Q=(u_i v_j : 1<=i,j<=2),  J_Q=m_Q,

at each node, and P_S(n)=(15/2)n(n-1)-25. Only this abstract node model is used; no source-specific coefficient choice is made.

## 2. Recovering the node ideal from the final differential

Dualize the actual free resolution into P(-5). Its last two free modules are P(2)^10 -> P(5), and the last map is the transpose of c. Consequently

Ext^3_P(A,P(-5)) = (P/(c_1,...,c_10))(5).

The annihilator of a shifted cyclic quotient P/K is K. Isomorphic P-modules have equal annihilators. Comparing with the input Ext identification proves, as ideals rather than merely after radical or sheafification,

(c_1,...,c_10)=J.

This does not require identifying a preferred generator of the Ext module or choosing a scalar-compatible duality isomorphism.

## 3. The adjugate identity

Let K be the fraction field of P. Localizing the exact resolution over K is exact. The map c has rank one and f has rank one, since their generated ideals are nonzero. Thus L has rank nine. In particular det L=0 and adj(L) is nonzero.

The right kernel of L over K is Kc, and the left kernel is Kf. Since L adj(L)=adj(L)L=0, every column of adj(L) is a rational multiple of c.

The entries of c are primitive in the UFD P: a common irreducible divisor would put J in a height-one prime, contradicting height J=4. For a rational scalar q with qc in P^10, writing q=a/b in lowest terms shows that b divides every entry of c, hence b is a unit. Therefore q lies in P. Applying this column by column gives

adj(L)=c h

for a polynomial row h. Since adj(L)L=0 and c is nonzero, hL=0. Thus h=qf over K. The entries of f are primitive by the same argument, now using height I=2, so q belongs to P. Every nonzero entry of adj(L) has degree nine, every c_i degree three, and every nonzero f_j degree six. Hence q is homogeneous of degree zero. The nonvanishing of adj(L) gives

adj(L)=lambda c f,  lambda in C*.

No vector of rational functions has silently been treated as a polynomial vector. The two primitivity steps are what remove this possible gap.

The signed 9-by-9 minors are exactly the entries of adj(L). Since lambda is a unit and c and f generate J and I, respectively,

I_9(L)=IJ

as homogeneous ideals in P.

## 4. Radical, colon, and support

Because I is prime and I is contained in J,

sqrt(IJ)=sqrt(I) intersect sqrt(J)=I intersect J=I.

Thus Proj(P/IJ) has S as its reduction.

There is actually a valid one-step colon strengthening in this setting:

(IJ:J)=I.

Indeed I is contained in (IJ:J). Conversely (IJ:J) is contained in (I:J), and (I:J)=I because J is not contained in the prime I. Explicitly choose j in J minus I; if aJ is contained in I, then aj lies in I, so a lies in I. More generally the same argument with j^r proves

(IJ:J^r)=I for every r>=1, and (IJ:J^infinity)=I.

This argument is specific to primeness of I and J not being contained in I. It should not be presented as a general product-ideal cancellation law.

Away from V(J), J becomes the unit ideal, so IJ becomes I. On projective space, the two schemes are therefore identical away from the thirty nodes. Saturation with respect to J is not saturation with respect to the irrelevant ideal P_+; no equality (IJ)^sat=I is asserted. In fact the nontrivial embedded projective node structure precludes that equality.

## 5. Square-zero nilradical and embedded associated points

There is an exact sequence

0 -> I/IJ -> P/IJ -> P/I -> 0.

Since sqrt(IJ)=I, the kernel I/IJ is exactly the nilradical of P/IJ. It is annihilated by J. It is square-zero because I is contained in J, hence I^2 is contained in IJ. These statements remain true after sheafification.

At a projective node z, let Q=O_{P4,z}, m its maximal ideal, and I_z the local surface ideal. Since Z is reduced, J_z=m. The nilradical stalk is

N_z=I_z/m I_z.

It is nonzero by Nakayama, since I_z is a nonzero finitely generated ideal. Every element of m annihilates it. Thus a nonzero element of N_z has annihilator precisely m, which proves that z is an embedded associated point of the thickened surface. This conclusion does not depend on the numerical local model.

Moreover N_z is the entire socle of Q/(m I_z), not merely a subspace of that socle. The quotient by N_z is Q/I_z, a positive-dimensional local domain because S is integral. Such a domain has zero m-socle: choose any nonzero element of its maximal ideal and use the absence of zero divisors. The image of the socle of Q/(m I_z) in Q/I_z is consequently zero. Since N_z is already annihilated by m, equality follows.

Projectively the associated points consist of the generic point of S and the thirty nodes. Away from the nodes the local rings coincide with the reduced integral surface, and the exact sequence above introduces no other support. This is not a claim excluding possible extra irrelevant-origin behavior for the affine cone.

## 6. Exact local length and Hilbert polynomial

Completion is faithfully flat and preserves I_z/m I_z and its residue-field dimension. In the pinned model,

I_Q=(u1v1,u1v2,u2v1,u2v2).

These four quadrics generate. Their classes modulo m_Q I_Q are linearly independent, because m_Q I_Q has order at least three while the four distinct quadratic monomials are linearly independent in m_Q^2/m_Q^3. Thus

dim_C N_z=mu(I_z)=4.

Accordingly each node contributes a four-dimensional square-zero nilradical, equal to the full local socle. The sheaf N=tilde(I/IJ) is supported at the thirty reduced points and has length

length(N)=30*4=120.

A sheaf annihilated by I_Z on this reduced zero-dimensional scheme is (noncanonically) a direct sum of its residue-field vector spaces. Thus N is noncanonically isomorphic to a direct sum of four copies of k(z) at each node. No splitting of the ring extension is implied.

For D=Proj(P/I_9(L))=Proj(P/IJ), sheafification and Euler characteristic give

P_D(n)=P_S(n)+120=(15/2)n(n-1)+95.

This is a projective Hilbert-polynomial statement, valid regardless of any irrelevant-primary discrepancy of IJ. The graded module I/IJ is not claimed to have finite total C-dimension; it is the associated projective sheaf whose length is 120.

## 7. Independent verdict and boundary

All proposed core conclusions and the four-dimensional-node/length-120 strengthening are correct under the stated actual-module and local-geometric inputs. The one-step colon equality is also rigorously available by the elementary prime-ideal argument above.

The proof gives a structural linear-adjugate reconstruction and identifies exactly why its 9-minor scheme differs from S. It does not provide selected HM/source coefficients, an explicit source-specific matrix L, a prescribed-source lift, a full-adjoint theorem, or algebraicity. In particular it must not be used to assert that the 9-minor ideal itself is the prime ideal I, that its irrelevant saturation removes the embedded nodes, that the ring extension splits, or that the affine-cone nilradical is a finite-length module.

## 8. Additional independently verified step: complete local rank profile

The smaller-minor claims can also be proved without selecting an actual HM/source matrix. Only the universal transverse-two-plane ideal in the completed local ring is used.

Write x=u1, y=u2, s=v1, t=v2, Q=C[[x,y,s,t]], m=(x,y,s,t), and K=(x,y)(s,t). A minimal resolution of Q/K has final generator row (xs,xt,ys,yt), middle differential

D = [ t   0   y   0 ]
    [-s   0   0   y ]
    [ 0   t  -x   0 ]
    [ 0  -s   0  -x ],

and final column (y,-x,-t,s)^T. This is the tensor-Koszul resolution for the two disjoint parameter pairs; its Betti numbers are (1,4,4,1).

Here is a direct exactness check, independent of that name. A relation (a,b,c,d) on (xs,xt,ys,yt) gives

x(as+bt)+y(cs+dt)=0.

Coprimality of x and y gives as+bt=y e and cs+dt=-x e. The element y is a nonzerodivisor modulo (s,t), so e belongs to (s,t); write e=s alpha+t beta. Coprimality of s and t then gives

(a,b,c,d)=(t gamma+y alpha, -s gamma+y beta, t delta-x alpha, -s delta-x beta),

which is D(gamma,delta,alpha,beta)^T. Thus ker(f)=im(D). If D(gamma,delta,alpha,beta)^T=0, its first equation and coprimality of y,t give gamma=y eta and alpha=-t eta. The other equations give beta=s eta and delta=-x eta. Hence ker(D)=Q(y,-x,-t,s)^T, and this final map is injective. All entries lie in m, so the resolution is minimal.

At an actual node, f and c have no unit entries, whereas the residue-field rank of L is 10-4=6, from the minimal generator number of the surface ideal. Equivalently the first Tor group has dimension four. Cancelling those six unit middle summands transforms L over Q into diag(I_6,D), up to invertible changes of the two middle bases. The remaining minimal resolution is isomorphic to the displayed universal resolution by uniqueness of minimal free resolutions. There are no end cancellations because f and c vanish at the node.

Off S, IJ is the unit ideal, so the established identity I_9(L)=IJ and det L=0 give rank L=9. On S minus Z, the surface is smooth of codimension two, so its local ideal has two minimal generators. Tensoring the localized presentation P^10 --L--> P^10 -> I ->0 with the residue field gives rank L=10-2=8. At a node the same argument gives rank L=10-4=6. Thus the pointwise rank profile is exactly

- 9 off S;
- 8 on S minus Z;
- 6 on Z.

There are no rank-seven points. These are structural ranks deduced from local generator numbers, not numerical rank tests on selected coefficients.

## 9. The seven- and eight-minor sheaves

The entries of D generate m. All 2-by-2 minors lie in m^2. Conversely the following minors exhibit all ten monomial generators of m^2, up to signs. Row and column numbers refer only to the universal D above:

- t^2: rows (1,3), columns (1,2).
- s^2: rows (2,4), columns (1,2).
- st: rows (1,4), columns (1,2).
- x^2: rows (3,4), columns (3,4).
- y^2: rows (1,2), columns (3,4).
- xy: rows (1,4), columns (3,4).
- xs: rows (2,3), columns (1,3).
- xt: rows (1,3), columns (1,3).
- ys: rows (1,2), columns (1,3).
- yt: rows (1,2), columns (1,4).

Thus I_1(D)=m and I_2(D)=m^2. For diag(I_6,D), the seven-minor ideal is I_1(D), and the eight-minor ideal is I_2(D): larger minors of D add nothing because determinantal ideals are nested. Invertible basis changes preserve determinantal ideals. Therefore, at every node after completion,

I_7(L)=m,  I_8(L)=m^2.

Faithful flatness of local completion descends these equalities to the actual ambient local stalks. Away from Z, rank L is at least eight, so both ideals are the unit ideal. Consequently on projective space,

widetilde(I_7(L)) = I_Z as an ideal sheaf,
widetilde(I_8(L)) = I_Z^2 as an ideal sheaf.

The second identity is a square of ideal sheaves; it should not silently be replaced by equality of the raw homogeneous ideals I_8(L) and J^2.

## 10. Correct homogeneous saturation statements

Let q_z be the homogeneous prime ideal of a projective node z, and let saturation here mean saturation with respect to P_+ (not the J-saturation in Section 4). Since J is already saturated, equality of ideal sheaves gives

(I_7(L))^sat = J.

For the second identity, each q_z is generated by four independent linear forms, and q_z^2 is q_z-primary and saturated. The saturated ideal of the double-point sheaf I_Z^2 is therefore

intersection over z in Z of q_z^2 = J^(2),

where J^(2) denotes the second symbolic power, equivalently the intersection of the contracted squares after localizing at the minimal primes of J. Hence

(I_8(L))^sat = (J^2)^sat = J^(2).

This establishes precisely the claimed seven- and eight-minor saturation formulas. It does not assert I_7(L)=J or I_8(L)=J^2 before saturation, and it does not alter the distinct conclusion I_9(L)=IJ with its genuine projective embedded-node structure.

## 11. Extended verdict

PASS also for the seven/eight-minor ideal-sheaf identities, the corresponding homogeneous saturated ideals, and the exact rank profile 9/8/6. The calculation in Sections 8-9 is a universal local-coordinate normal form at every transverse double-plane node, not an actual-source matrix selection or evaluation.

## 12. Audit of the completed companion proof

The complete companion PROOF.md was read after its author finished Sections 1-7. Final verdict: PASS, with no mathematical corrections required. The audit covers the actual-file arguments for Ext annihilators, the rational-multiplier exclusion, the one-step colon, the full local socle, projective length and Hilbert polynomial, all rank strata, the six middle cancellations, lower-minor ideals, symbolic-square saturation, and I_6(L)^sat=P.

Two potentially delicate points are resolved explicitly:

1. There are exactly six middle contractible pairs. The original completed free ranks are (1,10,10,1); the minimal ranks are (1,4,4,1). A cancellation touching either end would lower an end rank below its minimal value one, so none can occur there. All six cancellations are between the middle terms.
2. The universal four-generator local complex is exact, not merely a complex with the right ranks. Section 8 above supplies a direct formal-power-series syzygy argument in addition to the companion proof's tensor-Koszul explanation.

The companion proof's assertion that the graded nilradical has dimension one, rather than finite length, is also valid: it is annihilated by J and has a nonzero stalk at each node-line prime, so its support has dimension exactly one. This does not change the length-120 statement for its associated projective sheaf.

## 13. Reciprocal-colon strengthening

PASS also for (IJ:I)=J. The inclusion J subset (IJ:I) is immediate. Conversely, if hI subset JI and h is outside a node-line prime q_z, localization at q_z makes h a unit and J_q=q_zP_q. Hence I_q=q_zI_q, contradicting Nakayama because I_q is a nonzero finite module over the local domain P_q. Thus h lies in every q_z, whose intersection is the radical ideal J. This proves the reverse inclusion.

Consequently L alone gives the reconstruction recipe I=sqrt(I_9(L)) and J=(I_9(L):I), after which (I_9(L):J)=I as before. The column c is used to prove the determinantal identity but need not be separately supplied to execute this abstract ideal-theoretic recipe.
