## 1. Sources and convention

`pins.json` binds inert, locally vendored excerpts of the frozen compiler, shared schema and raw engine; the full-lift face program; the corrected JC proof; its independent acceptance review; and the transition bridge. Upstream full-file hashes and exact selection descriptions record provenance; the portable hashes authenticate the excerpts. The checker never imports or executes these excerpts. The compiler SHA256 is `28e95b87adefaba0d4ec886a7ab272f252f376bbb1fc26e0a387bc05f896a386`; raw engine SHA256 is `c9804022b362277d63217c7674c4d6d3dff5941ae4210c30f51f3b5cf3868da9`. These are the same implementation bytes as the prior integrated denotation theorem. The accepted JC review concerns PR88 at `d18d9810f7333d9f94a895c4e26985520cc60057`; its corrected prism qualification does not change the HPL argument.

Let K have terms K0,K1,K2,K3 of dimensions 5,15,10,2 and differential d of degree +1. In a common original-resolution trivialization, d has blocks gamma, delta_K, ev. A block key `(u,v)` in the compiler means a map Ku → Kv, with rows dim Kv and columns dim Ku. Thus its internal degree is v−u, NOT u−v.

For each local owner i assume a contraction with inclusion A_i into K1, projection B_i from K1, and h_i of degree −1:

    d²=0, dA_i=0, B_i d=0, B_i A_i=1,
    E_i=A_i B_i, dh_i+h_i d=1−E_i.

The usual side conditions h²=hA=Bh=0 are compatible and supplied by the accepted contraction package; the displayed End homotopy identity itself needs the displayed relations, rather than all side conditions. Original-resolution restrictions must commute with d and compose functorially. “Fixed frame” means all summed terms have already been expressed in the same ambient trivialization on their overlap; it does not erase genuine bundle transport between different trivializations.

## 2. Projection compatibility derived, including first-face transport

For the normalized physical leaves in the frozen engine,

    A_i=I_ci D_i, B_i=D_i^-1 P_ci,
    D_i=diag(nu_i,nu_i^-1).

The quotient transition theorem gives T_ij=P_ci I_cj, T_ij T_jk=T_ik, T_ii=1. Therefore

    B_i A_j=G_ij=D_i^-1 T_ij D_j=g_ij^t,
    G_ij G_ji=1.

This holds even when the literal images of I_ci differ. No equality A_j=A_iG_ij is assumed: equality modulo exact vectors suffices for the transition theorem. Define

    j_i(R)=A_i R^t B_i,
    pi_i(F)=(B_i F A_i)^t.

Then pi_i j_i(R)=R. For a different leading owner j, associativity and the transpose reversal give

    pi_i j_j(R)
      =(G_ij R^t G_ji)^t
      =g_ji R g_ij
      =g_ij^-1 R g_ij.

Consequently on t=(i0,i1,i2,i3),

    pi_i0(delta j(R))(t)
      =g_i0i1^-1 R(i1,i2,i3) g_i0i1
       −R(i0,i2,i3)+R(i0,i1,i3)−R(i0,i1,i2)
      =(delta_row R)(t).

Only the first face changes leading owner. The other three project in their own i0 frame. This supplies precisely the compatibility used in JC §2. No extra row-End conjugation belongs inside `Lift.delta`: it already sums original-resolution maps; inserting row conjugation there would mix representations and double-count the change after projection.

If the full physical leaves have additional common scalar line factors A_i^phys=lambda_i A_i and B_i^phys=lambda_i^-1 B_i, j_i and E_i are unchanged. Their two cross contractions contribute lambda_j/lambda_i and its inverse, which cancel in pi_i j_j. This proves cancellation of that paired factor, not arbitrary omission of external source line-bundle transport. The same ambient-frame/line identification, correct source bundle restriction, and legal localization remain geometric premises. On a general trivialization the above identities are read after the specified ambient transports. Determinant one is not needed for this abstract inverse identity, although the frozen source's adjugate-based implementation needs it upstream to supply the intended g^-1 and R.

Thus local contractions ALONE do not imply closure of the first correction. They do imply the needed projection formula when combined with the actual quotient-transition/frame identification; complete raw source closure then gives pi_first delta J0=0. Neither five individually closed summands nor ordinary untwisted row closure may replace it.

## 3. End homotopy and exact block lowering

For internal degree r set

    d_End F=dF−(−1)^r Fd,
    H_i,r(F)=h_i F+(−1)^r E_i F h_i.

Expanding d_End H_i,r+H_i,r+1 d_End and using dE=Ed=0 gives

    (dh+hd)F+EF(hd+dh)=F−EFE.

The terms hFd cancel with their precise graded signs. EFE=j_i pi_i(F) in degree zero, while EFE=0 in all nonzero internal degrees because E has support only at K1. The checker verifies this identity by explicit formal-word reduction for r=−3,...,3, using only the declared relations.

The compiler's first H term sends `(u,v)` to `(u,v−1)` with H(v) on the left, provided v>0. The second sends `(u,1)` to `(u+1,1)` with `(A_i B_i) F H(u+1)` and sign (−1)^r, provided u<3. These are exactly the two allowed typed products; the `v==1` test is E's support condition, not a dropped term. The block supports are

