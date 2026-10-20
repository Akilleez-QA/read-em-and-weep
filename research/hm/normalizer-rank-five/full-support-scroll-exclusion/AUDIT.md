# Independent audit: full-support factor-parametrized cubic scrolls

## Verdict

Accepted, including the added whole-kernel exclusion for type I in Section 5.2. The classification and all conclusions are valid over C within the explicitly stated family. No computation of actual source instances, numerical ranks, or code experiments was used in this audit.

The proof does not classify arbitrary five-dimensional symmetric kernels, nor all cubic scrolls in the symmetric rank-two locus. Its squarefree type III is an abstract kernel/correction example, not a claimed occurrence in the intended source operation or a constructed global trilinear quotient.

## 1. Parametrization and normal forms

The five independent coefficient tensors identify the map with

    [as:at:bs²:bst:bt²].

These are the complete tautological sections of the projective bundle of lines in O(-1) ⊕ O(-2). The base and fiber can be recovered regularly on its standard charts. Thus the map really embeds the smooth degree-three scroll in P4; it has no contracted ruling, vanishing projective-bundle point, or projection singularity. The fiber weights are correctly distinguished from coordinates on P1 × P1.

The support is span{x,y,z,p,r}. For z in A=span{x,y}, full support forces p and r to be independent modulo A and gives I. For z outside A, the map span{s,t} → E/(A+Cz) has rank one. Aligning its kernel with [1:0], and subtracting z-components by the allowed change in fiber coordinate a, gives p in A and r outside A+Cz. Five-dimensionality forces p nonzero. Its two possibilities, p parallel to x and p not parallel to x, give II and III. The displayed shear in the second case is correct: its new y coefficient is p/beta, and rescaling m makes this the new p. The three cases are distinct because the unique square of I lies on the intrinsic degree-one directrix, that of II does not, and III has no square.

This verifies exhaustiveness and distinctness for the claimed parametrized family only.

## 2. Every square-boundary support plane

For I the square has local parameters (t,b) and support

    span{x+t y, -t y+b z+bt w}.

The independent leading coefficients of y,z prevent cancellation; bt is of strictly higher order along every nonconstant arc through the origin. The complete graph fiber is therefore

    { span{x,-c y+d z} : [c:d] in P1 }.

Every member is attained by a straight arc, including the two endpoint ratios. Equivalently these are the exceptional directions in the blow-up of (t,b). The intersection of the planes is Cx.

For II the support is span{x+t y,t(w-y)+a z}. Its complete graph fiber is

    { span{x,c(w-y)+d z} : [c:d] in P1 },

again with intersection Cx. The sign w-y is correct. There are no other approaches omitted by these charts because the parametrization is an embedding and the square is a unique point in each scroll.

Compatibility on a dense open extends to all of the rank-two open by closedness in the tautological support bundle. The separate closed incidence v(q) in P on the graph closure then forces v(x²) into every limiting plane. This correctly avoids assuming that rank-two compatibility automatically extends into the smaller rank-one support.

## 3. Entire rank-at-most-two loci

The factorization argument is exhaustive: over C every nonzero symmetric tensor of rank at most two is LM, and the missing z²,w²,zw coefficients force one factor into span{x,y}. Applying the remaining coefficient identities gives exactly the following reduced sets:

    I:   scroll ∪ P(x span{x,y,z}),
    II:  scroll ∪ P(x span{x,y+w,z}),
    III: scroll ∪ P(y span{x,z,w}).

For I the identities are t M_y=0 and s M_w=t M_z; for II they are t M_y=0 and s M_y+t M_x=s M_w; for III they are s M_x=0 and s M_w=t M_y. Splitting respectively on t=0 or s=0 gives precisely the scroll and plane stated, with both inclusions checked. This also excludes additional higher-dimensional components or an unaccounted surface. No scheme-theoretic reducedness is inferred.

Both I and II have exactly the square x². Their plane components force v(x²) in Cx by two independent support limits, just as their scroll components do. A square-avoiding correction thus has compatible rank-two locus of dimension at most one in each entire kernel. In particular the requested explicit kernel <x²,xy+xw,yw,xz,yz> is fully excluded, not only its cubic component.

III has no square anywhere in K: vanishing x²,z²,w² coefficients would force a putative square to be proportional to y², but its y² coefficient is tied to xw. The correction v=0 is therefore square-avoiding and compatible with all its rank-two tensors.

## 4. Exact compatible corrections for III

The directrix first forces v(xz)=lambda x+mu z and v(yz)=lambda y+nu z. For each base direction l=sx+ty, the two classes z and m=sy+tw are independent modulo l. Compatibility on the whole ruling says that its induced linear map preserves every line of their two-dimensional span, hence is scalar. Consequently

    s²v(xy)+st v(xw+y²)+t²v(yw)
      = (mu s+nu t)(sy+tw)+(alpha s+beta t)(sx+ty).

Comparing coefficients gives exactly the five-parameter formula in Section 6.1, without a missing endpoint condition. The displayed expression for v(q) proves sufficiency on every ruling. The five parameters are independent.

With the specified symmetric-product normalization, contraction q → 2q(d) corresponds exactly to alpha=nu and d(z)=lambda, d(x)=mu, d(y)=nu, d(w)=beta. Thus the contraction subspace has dimension four. On the extra plane, quotienting by y gives eigenvalues alpha,nu,nu on x,z,w, so full-plane compatibility is equivalent to alpha=nu. The claimed extra compatible-scroll direction is genuine.

## 5. Scope of the trilinear consequence

The use of square avoidance is legitimate under global repeated-input injection. For independent u,e, proportionality of A_u(e) and A_e(u) would, by outer symmetry and the cyclic relation, give a nonzero repeated-input kernel at a suitable line u+t e. Thus a compatible square is forbidden. The finite ordered-factor reconstruction preserves the dimension bound for independent-zero fibers at a fixed middle point.

The accepted result supplies whole-kernel exclusions for I and II and an explicit surviving squarefree geometry III. It does not resolve global occurrence, higher-order integrability, positive-dimensional middle families, or the intended source's remaining rank-five problem.
