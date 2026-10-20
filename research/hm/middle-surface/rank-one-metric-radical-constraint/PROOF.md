# Rank-one metric boundary: a radical Plücker identity and finite metric fibers

## New conclusions and scope

Work over C with one fixed outer-symmetric, cyclic-zero trilinear operation f on a five-dimensional V, and suppose all repeated-input maps A_u:V/Cu→J are injective. Use the resolved projective metric family of `/research/conductor-normalization/metric-discriminant-localization/PROOF.md`, including its proved regular supported correction through residual-rank drops. Let T be the normalization of any complete integral curve on that model whose metric has rank one at its general point. Then its metric has rank one everywhere. Write

    U ⊂ P ⊂ H ⊂ V⊗O_T,       ranks 1,3,4,
    E=H/U,   R=rad(h)⊂E,   P=preimage(R),   N=V/H.

Thus R has rank two and P has rank three. Put L_P=det(P*). There is an equality of line-bundle classes, not just of degrees,

    L_P^7 ≅ (U*)^9 ⊗ N^3.                              (1)

No preferred isomorphism is asserted. With a=deg U*, n=deg N, p=deg L_P,

    7p=9a+3n.                                           (2)

Consequently p is divisible by three, 3a+n is divisible by seven, and a nonconstant middle curve has p≥3. In particular a complete rank-one metric boundary curve cannot have constant lifted radical three-plane P if its middle or support hyperplane varies.

There is also a new fiberwise conclusion. When the support map extends to the normalized middle surface, the rank-one locus in every fiber of its projective metric graph is finite. An exceptional curve on the metric graph itself therefore cannot have generic metric rank one. This fiberwise statement is superseded by the stronger intrinsic extension in INTRINSIC_METRIC_EXTENSION.md: once H is regular, the entire metric graph is isomorphic to the base, in all metric ranks. Rank-one boundary curves mapping onto curves and exceptional curves introduced by resolving the complement graph remain unexcluded.

The proof uses the regular correction obtained from the actual fixed family identity, and repeated-input injectivity over every geometric point. It does not assume constant actual residual rank, evaluate any source operation, or replace the actual family by freely assigned corrections.

## 1. Actual-family correction and its splitting independence

We recall precisely the necessary family identity, including at rank drops. The repeated-input map is a bundle monomorphism

    A:((V⊗O)/U)⊗U² → J⊗O.

Its image is a subbundle because it has constant rank four. Local splittings of H→E define the middle numerator on Sym²E⊗U. On the dense original good locus this numerator on K_h=ker(h) takes values in im(A). The identity extends over the integral metric model: its composite to the locally free quotient by im(A) vanishes on a dense open. Applying local left inverses of A consequently gives a unique regular correction

    v_s:K_h → E⊗U.

Its values lie in E⊗U everywhere because this is a closed bundle condition which holds on the dense good locus. This is exactly the extension argument of Section 3 of the metric-discriminant localization proof. It allows the actual residual kernel to become larger than the rank-five subbundle K_h.

For a change of splitting by d:E→U, the correction changes by

    v_{s+d}(q)−v_s(q)=2q(d).                             (3)

On q=r² this change belongs to Cr⊗U. Repeated injectivity and the cyclic/outer identities imply, for every geometric fiber,

    h(r,r)=0, r≠0  ⇒  v_s(r²)∉Cr⊗U.                   (4)

Indeed a compatible square would make A_r(u) proportional to A_u(r) for independent lifts r,u. The standard repeated-input pencil argument says those two vectors are independent. All these statements concern the actual family, not independently chosen pointwise tensors.

## 2. A nowhere-zero section on the radical ruled surface

Because h is nowhere zero as a functional, rank≤1 means exactly rank one. Rank≤1 is closed, so a curve generically of rank one has rank one at all its points, including after normalization. Its radical R is therefore a rank-two subbundle of E.

Let

    π:S=P_T(R)→T

parameterize lines, and let L=O_S(−1)⊂π*R⊂π*E be its tautological line. Since R is the radical, L² lies inside π*K_h. Restrict v_s and project its output to π*E/L. This gives a local section of the rank-two bundle

    F=(π*E/L)⊗π*U⊗L^(−2).                              (5)

The local sections glue: by (3), a splitting change has output in L⊗π*U and is zero in the quotient. Thus this construction is global even if H does not split globally. It is nowhere zero by (4), applied to every line in every radical fiber. In particular O_S→F is a subbundle with line-bundle quotient. Hence

    c2(F)=0 in CH²(S).                                   (6)

This is the key additional geometric restriction. Merely testing a single radical direction would not yield (6); it uses the entire projective radical-line family simultaneously.

## 3. Chern calculation, with projectivization signs fixed

Write e=c1(E), r=c1(R), u=c1(U) on T and ξ=c1(L*). Classes from T are pulled back without additional notation. The line convention for P(R) gives

    ξ²+π*r·ξ=0,       π*push(ξ)=1.

The quotient G=π*E/L has

    c1(G)=e+ξ,        c2(G)=eξ+ξ².

Twisting G by the line bundle with first Chern class u+2ξ yields

    c2(F)
      = c2(G)+(u+2ξ)c1(G)+(u+2ξ)²
      = (3e+5u)ξ+7ξ².

Products of two base-divisor classes vanish because T is a curve. Push (6) down to T, obtaining

    3c1(E)+5c1(U)−7c1(R)=0 in CH¹(T)=Pic(T).             (7)

Now det E=N^(−1)⊗U^(−1), and det R=det P⊗U^(−1). Substituting in (7) gives

    7c1(det P*)+9c1(U)−3c1(N)=0,

which is exactly (1). Taking degrees gives (2). There is also an integral Picard-group strengthening. Put Q=(U*)³⊗N and T₀=Q⊗L_P^(−2). Since L_P^7≅Q³, one obtains

    L_P≅T₀³,       (U*)³⊗N≅T₀^7.

Thus these are actual cube and seventh-power classes, not merely degree congruences.

Both N and det P* are pullbacks of hyperplane/Plücker bundles; U* is the middle hyperplane bundle. They have nonnegative degree on every complete curve. Thus p=0 forces a=n=0. Also 7p=3(3a+n) implies 3 divides p and 7 divides 3a+n. If the middle map is nonconstant, a>0, so p>0 and hence p≥3. A degree-zero Plücker pullback has constant Grassmannian map, and conversely. This proves the claimed constant-radical exclusion.

## 4. Finite rank-one locus in each projective metric fiber

Assume the support hyperplane map extends to the normalized middle surface X, as in the localization proof. Let G_h be the reduced projective metric graph over X. On G_h the bundles U,H,E and the nowhere-zero projective metric are defined. The regular supported correction and (4) hold there as well: the proof in Section 1 needs integrality and locally free bundles, not smoothness.

Fix x∈X. The closed rank-one locus in the projective fiber (G_h)_x is projective. If it had positive dimension, it would contain a complete integral curve; normalize that curve to T. The middle U and support H are constant along T, so a=n=0. Formula (2) gives p=0; therefore its lifted radical plane P is constant.

For a fixed E, a rank-one symmetric form up to scale is uniquely determined by its radical hyperplane R: it is the square of a covector annihilating R. Hence the projective metric is constant on T. But G_h is a closed subvariety of the relative projective metric bundle, so a curve with both its base point and its projective metric constant cannot be a curve. This is a contradiction. The rank-one fiber locus is therefore zero-dimensional and, being projective of finite type, finite.

In particular, if a curve of G_h contracts to a point of X and its generic metric rank were one, rank≤1 closedness and the nowhere-zero metric would make it a curve in the forbidden rank-one fiber locus. Curves on a subsequent resolution that map to a point of G_h are not excluded: for them the metric and radical can both be constant, consistently with a=n=p=0.

## 5. A degree constraint for the metric and determinant lines

Let M be the metric value line on T and m=deg M. At rank one the induced pairing on E/R is nondegenerate, so

    (E/R)²≅M.

Here h is a pairing E⊗E→M, so this is the value-line convention. Accordingly

    m=2(deg E−deg R)=2(p−n).

Combining this with (2) gives

    7m=18a−8n.

For the determinant line D=(det E*)²⊗M³,

    7 deg(D|T)=40a−10n.                                 (8)

Thus a rank-one boundary curve carries more information than its DVR multiplicity: its radical Plücker and metric degrees must obey (1) and (8). No sign for deg(D|T) is inferred merely from effectivity of the ambient discriminant, since T can itself be a component of that divisor.

## Remaining frontier

This result is a necessary structure theorem, not a complete exclusion of the affine-dimension-seven ternary-support family. It rules out constant-radical rank-one boundary curves with varying middle/support, and rules out entire rank-one metric-graph curves above a fixed normalized middle. The remaining boundary may include rank-two curves, rank-one curves with the compelled nonconstant radical map and degree identity, and additional exceptional curves on complement resolutions. The stronger companion theorem INTRINSIC_METRIC_EXTENSION.md eliminates every exceptional metric-graph fiber once H extends, so there is no remaining rank-two metric-graph exceptional case. A natural next step is to compare (1) with the actual second fundamental forms of U⊂P⊂H along a rank-one boundary curve, or to bound the complement-covector base ideal at those points.
