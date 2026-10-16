# V01 independent review of finite-field selection proof

Status: theorem route accepted conditionally; producer extraction/basis/cycle certificate pending inspection. This review concerns constant P4 linear algebra only, not source-polynomial arithmetic or obstruction values.

Let integer matrices B:Z^b->Z^n and C:Z^n->Z^c satisfy CB=0. Let selected integer columns Q have m columns and CQ=0 EXACTLY over Z. Assume an authenticated rational boundary upper bound rank_Q(B)<=r, and rank_Fp([B Q])=r+m for a proved prime p. Then rank_Q([B Q])>=r+m, because a nonzero modular minor is a nonzero integer determinant. Since adjoining m columns raises rank by at most m, rank_Q([B Q])<=rank_Q(B)+m<=r+m. Equalities follow: rank_Q(B)=r and the m selected classes are independent modulo im_Q(B). If dim_Q kerC/imB<=m is independently authenticated, these classes form a basis. The matching modular boundary rank r is useful corroboration; by itself it is NOT a rational upper bound.

Apply (n,r,m)=(400,240,10) and(1200,848,2). Exact selected-cycle checks and independently authenticated cohomology upper dimensions10/2 are load-bearing. Modular cycle checks alone do not imply rational cycles. A rank certificate must include actual pivot/minor/reduction evidence or a bounded independent regeneration; hashes alone do not prove rank.

Countercontrol: B=(p,0)^t, c=(1,0)^t. Modp rankB=0 and rank[B c]=1, but rationally c is a boundary. A guessed rankB_Q<=0 would invalidate the claimed class. Similarly Cc can be nonzero divisible byp while the modular cycle test passes. Do not infer rational upper bounds/cycles from a single prime.

## Source premises to bind

P4 saved certificate at f968b53943ba2312f09fbc3e8f9d462e86bcaa34, path research/hm/d8-small-certificates/p4/certificate.json blob304d031083bb2a19fb9bc012cfd338bbe0129980, reports B ranks240/848, outgoing150/350, dimensions400/1200. The paired producer check_hm_p4_all_twists.js blob7adc1d6a733636204b1dd613870c168717be6277 implements exact integral unit-pivot elimination plus BigInt tail and rejects nonunit rank; saved unit ranks equal full ranks, with zero tail bits. This is a pinned pre-existing premise, not an independent replay in this review. New modular code must reconstruct the SAME bases/matrices or provide an explicit permutation/sign isomorphism before borrowing its Q upper bounds.

Pinned basis(r,t) uses tuples(u,v,targetrow,sourcecolumn,m0,...,m4), v=u+r; homogeneous monomials of degree r+t, recursively increasing m0, then m1, etc. Hom differential is d f-(-1)^r f d. Reversing Hom source/target or changing a polynomial basis without matching both maps invalidates borrowed ranks. Verify block dimensions/nonzero counts AND canonical row/column tuple hashes; counts alone are insufficient.

Supertrace identification: free K_j has B[b,i]=1, j=15b+i, A[5b+k,a]=gamma[i,a,k]. Then str(XK_j)=sum gamma X02-X13=-L_(i,b)(X), with complex degrees0,1,2,3. Use c=-K for requested L labels. Multiplication shifts polynomial exponent only, preserving Hom tuple and sign. The Q and Q^2 labels belong to the D8 free-module splitting, not a coefficient reduction modulo101. Final result is characteristic-zero completeness conditional on the established Serre/invariant/source bridges, never an F101 obstruction value.

## Extraction/resource review requirements

Before execution inspect exact selected source ranges, source SHA/blob assertion and disabled monolithic-main boundary. Only constant arrows/basis/ordinary matrices and bounded ten-column d5 zigzag are allowed; no80,384-dimensional oracle, HM residual/masks/physical source modules. Bound all sparse pivots/candidates/update counts and serialized receipt. Enforce60s/512MiB externally, with cap-hit=inconclusive and no partial success. New producer files still pending; this note is not their execution approval or output acceptance.
