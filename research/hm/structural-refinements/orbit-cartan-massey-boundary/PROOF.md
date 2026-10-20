> Scope: read CURRENT-SCOPE.md and DEPENDENCIES.json with this complete historical derivation. Historical open-case wording is qualified there.

# Boundary of the first and two-direction orbit-Cartan identities

## Result

For the actual PGL orbit, a smooth splitting of the Atiyah operators supplies derivations L_X and degree-one representatives a_X of its Kodaira–Spencer classes. The first Cartan identity gives only the already-known cyclic Massey relation. The antisymmetric two-direction commutator identity cancels all terms involving first derivatives of a third cocycle before taking cohomology. Its remainder is the Atiyah curvature identity itself. Thus these particular first-derivative and commutator manipulations give no extra equation on the four symmetric or four alternating eligible lower parameters, or the four eligible upper parameters.

This is a bounded exclusion of the displayed manipulations. It is not a proof that all information in an orbit family, higher compatibility, or the Atiyah algebroid gives no further constraint. Actual vanishing/nonvanishing remains undecided. Section 6 supplies a stronger representative reduction for both lower and upper operations: all End-valued pair primitives cancel modulo an explicit differential, leaving only a covariant-derivative term and scalar primitives.

## 1. Operators and twists

Work in the twist-graded Dolbeault DGA A of End(H), with d=bar-partial. Use the Lie algebra sl(V) to obtain the genuine linearized Lie action on every O(k). A smooth connection supplies C-linear, degree-zero derivations L_X on A, covering the holomorphic vector field X. Include the natural holomorphic O(k) action on each twist; then no twist-line curvature term enters [d,L_X]. For suitable degree-one End(H) cochains a_X,

    [d,L_X]=ad(a_X),     d a_X=0.                         (1)

The classes of a_X are the orbit Kodaira–Spencer classes, up to the common choice of sign convention. One can choose the determinant lift to be the holomorphic linearized lift on det(H)=O(-1). Then a_X is trace-free. The commutator defect on H is order zero:

    [L_X,L_Y]-L_[X,Y]=ad(R_XY),                          (2)

with R_XY a degree-zero trace-free End(H) cochain. On the bundle operators themselves, not merely modulo their central adjoint action, the graded Jacobi identity gives

    L_X a_Y-L_Y a_X-a_[X,Y]=d R_XY.                     (3)

The determinant normalization removes any scalar ambiguity in (3). Equivalently, derive (3) directly from [d,D_X]=a_X for the chosen first-order bundle operators D_X. These are smooth operators, not holomorphic lifts of all X to H. Holomorphic lifts would kill the nonzero Kodaira–Spencer map.

### Global twist construction and the single symbol

The twist action here is essential. Use the canonical holomorphic infinitesimal sl5 lift on O(k), not the horizontal derivative of an arbitrary Chern connection on O(k). In local holomorphic frames write the smooth bundle lift as D_X^H=X+Gamma_X and the holomorphic line lift as D_X^(k)=X+lambda_X,k. The coefficients lambda_X,k are holomorphic. On End(H)⊗O(k), the combined operator is

    L_X=Lie_X+ad(Gamma_X)+lambda_X,k.

There is exactly one base derivative. Intrinsically the tensor rule D(e⊗l)=D_H(e)⊗l+e⊗D_line(l) is balanced: applying it to (fe)⊗l or e⊗(fl) gives the same single X(f) term. The analogous rule for End(H) and its line twist is therefore globally well-defined. On (0,q)-forms Lie_X is the holomorphic vector-field action; it commutes with bar-partial. Thus

    [d,L_X]=ad(bar-partial Gamma_X)

without a twist scalar term. The line actions are compatible with tensor multiplication, so lambda_X,k+l=lambda_X,k+lambda_X,l and L_X is a derivation of the entire twist-graded algebra. A naive Chern horizontal line derivative would instead contribute its contracted (1,1) curvature; it must not be substituted here. Passing from PGL5 to its Lie algebra sl5 is harmless and provides the unique trace-free lift of every projective vector field.

## 2. First Cartan identity and cyclic zero

Let a=a_X and let b,c be closed degree-one inputs in any of the permitted twists. Suppose every pair product needed below is exact, and products with the closed primitive ambiguities vanish in the corresponding cohomology. This holds for the specified 001 and 011 patterns.

Choose d h_uv=u v. Equation (1) says

    d L_X b=ab+ba,    d L_X c=ac+ca.

Consequently

    z_b=L_X b-h_ab-h_ba,
    z_c=L_X c-h_ac-h_ca

are closed. Applying (1) to h_bc and using that L_X is an ordinary degree-zero derivation gives

    d L_X h_bc
      =L_X(bc)+a h_bc+h_bc a
      =(a h_bc+h_ab c)
       +(b h_ac+h_ba c)
       +(b h_ca+h_bc a)+z_b c+b z_c.

The last two terms are zero in cohomology by the assumed ordered cup vanishings. Hence

    m(a,b,c)+m(b,a,c)+m(b,c,a)=0.                      (4)

Outer reversal turns (4) into the existing cyclic identity. This is an independent orbit-Cartan source for that identity, not an additional constraint. In particular it does not imply that the middle placement vanishes.

## 3. Exact antisymmetric two-direction calculation

For any closed degree-one b in a permitted twist, (1) gives

    d(L_X L_Y b)
      =[L_X a_Y,b]+[a_Y,L_X b]+[a_X,L_Y b].            (5)

Here every bracket between degree-one terms is their anticommutator. Subtract the expression with X,Y exchanged. The two terms containing L_X b or L_Y b cancel identically, leaving

    d([L_X,L_Y]b)=[L_X a_Y-L_Y a_X,b].                (6)

Subtract d L_[X,Y] b and use (3):

    d(([L_X,L_Y]-L_[X,Y])b)=[dR_XY,b]
                               =d[R_XY,b].           (7)

Equation (2) identifies the two primitives in (7) already at cochain level. Thus this antisymmetric commutator calculation supplies no closed residual, and no new linear relation among triple Massey classes. The terms from which such a relation might have arisen cancel before passing to primitives or cohomology.

In particular, it is invalid to replace L_X a_Y by L_Y a_X modulo exact cochains while forgetting a_[X,Y]. Their difference has the class kappa([X,Y]); by the imported injective orbit Kodaira–Spencer map this is nonzero whenever [X,Y] is nonzero. Its products with the remaining degree-one input nevertheless vanish under the given ordered-product hypotheses. The Lie bracket contribution therefore does not select the alternating part of m001 by this argument.

The symmetric second-direction extension calculation is the usual polarized lifting obstruction; Section 2 already gives its cyclic combination. This note does not classify arbitrary identities obtained by differentiating chosen primitives further or by imposing higher coherent transport data.

## 4. Chern flatness and the scalar primitives

A Chern (1,0) connection has curvature of type (1,1), so on holomorphic (1,0) vector fields its commutator defect has R_XY=0 before any irrelevant central normalization. With the compatible action on (0,q)-forms, the same cancellation in (5)–(7) then reads

    L_X a_Y-L_Y a_X=a_[X,Y]

modulo central terms if working only on End. Flatness removes R; it does not remove a_[X,Y] and does not restore the canceled triple terms.

For trace-free closed b, trace-preserving L_X, and trace-free a_X, one may set

    q_Xb=(1/2)L_X b,    d q_Xb=(a_X b+b a_X)/2.

Rank two identifies the last expression with the trace-free part of a_X b. A full ordered primitive still requires a scalar degree-one t_Xb with

    d t_Xb=tr(a_X b)/2,
    h_Xb=q_Xb+t_Xb Id,    h_bX=q_Xb-t_Xb Id.

Scalar H2 vanishing provides t_Xb, while scalar H1 vanishing removes ambiguity among scalar primitives modulo boundaries. Neither vanishing implies t_Xb=0: its prescribed differential need not be zero. Thus the scalar contributions to the Massey expression cannot be dropped.

When both inputs are orbit directions, the formulas q_XY=(1/2)L_X a_Y and q_YX=(1/2)L_Y a_X are generally not equal. Their difference is (a_[X,Y]+dR_XY)/2. A symmetric adjugation-compatible choice is instead

    q_XY=q_YX=(L_X a_Y+L_Y a_X)/4.

Each of the one-sided choices differs from this by a closed cochain. Its products disappear in the relevant cohomology, by the established ordered cup vanishings, but the cochain difference itself cannot be set to zero.

It would also overstate this argument to say that the scalar primitives are the sole unresolved part. The trace-free expression still involves L_X b and L_X a_Y, and no proof here makes its separate class vanish. The unresolved information is the full ordered primitive expression, including both trace-free and scalar terms.

## 5. Explicit lower alternating reduction with scalar terms retained

Let u represent a class in U1, and let a_X,a_Y represent the two U0 inputs. All are trace-free. For odd trace-free forms define B(x,y)=(xy+yx)/2, the trace-free part of xy. Choose the symmetric q_XY from Section 4 and scalar primitives

    d t_XY=tr(a_X a_Y)/2,     t_YX=-t_XY,
    d t_Xu=tr(a_X u)/2,       d t_Yu=tr(a_Y u)/2.

The scalar primitive equations have solutions by H2(O)=H2(O(-1))=0. Graded cyclicity gives tr(a_Y a_X)=-tr(a_X a_Y); applying one linear right inverse of d on scalar boundaries therefore makes t_XY bilinear and antisymmetric, including t_XX=0. Their differences are scalar exact cochains by H1(O)=H1(O(-1))=0. The full primitives h_XY=q_XY+t_XY Id and h_Yu=(L_Yu)/2+t_Yu Id have the correct ordered differentials.

Taking the trace-free part of the defining Massey cocycle yields the following representative of F(X,Y,u)=m001(a_X,a_Y,u):

    C_XY(u)= (1/2)B(a_X,L_Yu)
           + (1/4)B(L_Xa_Y+L_Ya_X,u)
           - t_Yu a_X + t_XY u.                       (8)

The minus sign comes from a_X t_Yu=-t_Yu a_X. Trace-free projection preserves the class because the scalar target H2(O(-1)) vanishes.

In particular the alternating two-orbit-slot class has representative

    C_alt(X,Y;u)
      = (1/4)(B(a_X,L_Yu)-B(a_Y,L_Xu))
        - (1/2)(t_Yu a_X-t_Xu a_Y)+t_XY u.            (9)

The orbit-orbit trace-free primitive cancels entirely in (9). For reference, the symmetric part has representative

    C_sym(X,Y;u)
      = (1/4)(B(a_X,L_Yu)+B(a_Y,L_Xu))
        + (1/4)B(L_Xa_Y+L_Ya_X,u)
        - (1/2)(t_Yu a_X+t_Xu a_Y).                  (10)

Each expression is a cocycle, because it is respectively the alternating or symmetric part of the trace-free Massey cocycle (8). Its cohomology class is independent of connection, representative, and scalar primitive choices by the established canonical Massey theorem. No stronger claim of cochain independence is made.

Equation (9) is the precise remaining alternating expression after the direct orbit reduction. It describes the four symmetry-eligible alternating lower components only; it does not claim that those are the only remaining actual components or exclude the four symmetric ones. It is a usable reduction, rather than an additional vanishing identity: both its derivative-of-u term and its scalar-primitive terms remain. The two-direction commutator calculation of Section 3 does not show that their sum is exact. Equation (10) remains the corresponding symmetric expression, constrained by the already-known cyclic relation to the middle ordering.

## 6. Stronger reduction: no End-valued pair primitives remain

The holomorphic twist construction above gives a stronger formula for either weight pattern. Let a=a_X be one orbit input and let b,c be the remaining closed odd trace-free inputs. Their twists may be (0,-1) for the lower operation or (-1,-1) for the upper operation. Choose a trace-free q_bc and scalar t_bc with

    d q_bc=B(b,c),       d t_bc=tr(bc)/2,

so h_bc=q_bc+t_bc Id. Choose h_ab=(L_Xb)/2+t_ab Id with d t_ab=tr(ab)/2. These scalar equations are solvable at twists 0,-1,-2, since H2(O(k))=0 there. Scalar H1 vanishing makes their choices unique modulo exact scalar cochains.

The trace-free defining Massey cocycle is

    M_tf=B(a,q_bc)+(1/2)B(L_Xb,c)-t_bc a+t_ab c.

Using that L_X is a trace-preserving derivation and [d,L_X]=ad(a) yields the exact identity

    d L_Xq_bc
      =B(L_Xb,c)+B(b,L_Xc)+2B(a,q_bc).

Consequently

    M_tf=C(X;b,c)+(1/2)d L_Xq_bc,
    C(X;b,c)=-(1/2)B(b,L_Xc)-t_bc a_X+t_ab c.          (11)

This is an exact cochain equality; no separate cohomology class is assigned to the individual B terms. Equation (11) proves that C is closed and represents the canonical Massey class. The resulting class is connection-independent by the canonical zero-indeterminacy theorem. The formula removes every End-valued pair primitive; it retains scalar primitives and the covariant derivative of c.

For upper weights it gives

    m011(a_X,b,c)=[-(1/2)B(b,L_Xc)-t_bc a_X+t_Xb c].   (12)

For lower weights it gives

    m001(a_X,a_Y,u)
      =[-(1/2)B(a_Y,L_Xu)-t_Yu a_X+t_XY u].           (13)

Antisymmetrizing (13) reproduces equation (9). In deriving (13), the one-sided trace-free primitive (L_Xa_Y)/2 is legitimate even though it is not symmetric in X,Y. Its difference from the symmetric primitive used in (8) is closed, and its product with u vanishes in cohomology by the established ordered cups. Thus the two lower formulas agree as canonical classes.

This is a genuine representative reduction, not a vanishing theorem or an extra parameter equation. It does not say that the scalar terms alone carry the obstruction: the remaining B(b,L_Xc) term is essential and generally not separately closed. Nothing here evaluates either operation or removes any eligible symmetric or alternating component.

### A specified scalar homotopy, without evaluation

If a fully specified smooth scalar primitive is desired, choose Hermitian metrics and the Dolbeault Green operator G_k on O(k), k=0,-1,-2. Put

    t_pq=(1/2)bar-partial* G_k tr(pq).

The scalar two-form tr(pq) is closed; H2(O(k))=0 removes the harmonic term. Hodge decomposition and commutation of G_k with bar-partial then give d t_pq=tr(pq)/2. One common operator gives bilinearity and t_qp=-t_pq. H1(O(k))=0 ensures that changing this scalar homotopy changes t_pq by an exact scalar cochain.

The finite group N permits invariant metrics: average a Hermitian metric on V to obtain an invariant Fubini–Study metric, use its line-bundle metrics, and average a Hermitian metric on H. The scalar Green operators are then N-equivariant. This prescribes the scalar part of (11) naturally relative to chosen metric data; no Green operator, product, representative, or value is evaluated here.

The displayed homotopy is smooth Dolbeault data. Comparison identifies the resulting cohomology class with the algebraic singleton Massey operation. No regular algebraic Čech primitive, effective computation, or nonvanishing follows from this choice alone.

## 7. Two cautions about triviality and equivariance

Pullback by the automorphisms of P4 identifies the fiberwise twisted endomorphism DGAs along the orbit. Such identifications change the coordinate action: for the coordinate ring S, transport obeys T_g(fu)=(g^*f)T_g(u), with the corresponding pullback convention. It is therefore semilinear over the fixed S, rather than an S-linear trivialization respecting fixed coordinate multiplication. Constancy of the relative derived endomorphism algebra over the parameter base is a different statement and does not supply that missing fixed-S trivialization.

Nor do the L_X induce an sl5 action on the fixed-fiber cohomology by themselves: (1) says they are not chain maps. A nonzero orbit tangent measures precisely the failure of a holomorphic lift. The actual finite stabilizer N still acts on the fixed fiber and gives the audited representation restrictions. No PGL-equivariance constraint on a fixed-fiber Massey tensor has been proved by constructing the orbit family.

## 8. Audit and evidence boundary

The signs in Section 2 follow directly from |h|=1, so [a,h]=ah+ha. In Section 3 the two derivative-of-b anticommutators appear with opposite signs after exchanging X,Y, and cancel exactly; the remaining curvature term has |R|=0, so d[R,b]=[dR,b]. These checks use no cohomological dimension argument or guessed primitive.

The substantive result is limited: the explicit two-direction commutator route requested here reduces to an exact cochain identity and supplies no additional Massey equation. It does not settle the broader orbit/Atiyah route.   

Inputs: [lower-weight-image-symmetry](https://github.com/Akilleez-QA/read-em-and-weep/blob/292d59b1e28c33968537a5f13700e7c45dc9214f/research/hm/cubic-loci/foundation-p05b/LOWER-TRANSFER.md); [equivariant-massey-multiplicity](https://github.com/Akilleez-QA/read-em-and-weep/blob/1260bfd20b6680dc2ce66088c19ae6431b347ab0/research/hm/cubic-loci/foundation-p05/ELIGIBLE-MULTIPLICITY.md); [cech-transgression-primitives](https://github.com/Akilleez-QA/read-em-and-weep/blob/1260bfd20b6680dc2ce66088c19ae6431b347ab0/research/hm/cubic-loci/foundation-p05/CECH-PRIMITIVES.md); [canonical-massey-detector](https://github.com/Akilleez-QA/read-em-and-weep/blob/721fdc556714bb40f0a805f01fae51cf6d555fd5/research/hm/cubic-loci/foundation-p04/CANONICAL-MASSEY.md); family-extension-massey-constraint (historical comparison); structural-massey-formality-boundary (historical comparison); rank-two-primitive-identity-boundary (historical comparison).
