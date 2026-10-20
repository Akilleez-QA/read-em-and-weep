# The canonical nonfinite Cohen–Macaulay modification and its pushforward

## Statement

Work over k=C. Write B=R/Q for the universal primary closure of `../global-rank-one-primary-closure/PROOF.md`, C=R/P for its reduced rank-one cone, and m for the vertex ideal. To avoid the earlier use of B for an open set of directions, B here always denotes the affine algebra. Let I_1,I_2,I_3 be its three input-coordinate ideals and K=I_1 I_2 I_3.

Put T=P(V)=P^4, Ω=Ω_T, and

    S=Spec_T(O_T ⊕ Ω),    Ω²=0.

Specify three morphisms π_i:S→T by their pullbacks on local functions:

    π_1*(a)=a+da,    π_2*(a)=a,    π_3*(a)=a−da.

For L=O_T(−1), let L_i=π_i*L. Then:

1. The multiprojective scheme defined by Q in T³ is exactly S, with its indicated three projections, over ALL of T. Equivalently (π_2,π_1) identifies S with the first infinitesimal diagonal in T×T. This extends the projective description of the good component without asserting that the full original equation ideal J has the same projectivization at bad directions.
2. There is a canonical identification

       W=Bl_K(Spec B)=Tot_S(L_1⊕L_2⊕L_3).

   Its map f:W→Spec B is projective, birational in the scheme-theoretic sense, and nonfinite. W is everywhere Cohen–Macaulay of local type four, dimension seven. Its reduction is Tot_T(O_T(−1)^⊕3). The vertex fiber is S.
3. As a B-algebra, not just as a vector space,

       Γ(W,O_W)=B^h,
       f_*O_W=the sheaf associated to B^h,
       R¹f_*O_W=k(m),
       R^if_*O_W=0    for i≥2.

   Here B^h is the canonical finite S2/Hartogs hull constructed in `../primary-graded-geometry/VERTEX_DEPTH.md`; the equality takes place in the common total quotient algebra. The nonzero R¹ is concentrated in multidegree (0,0,0), and B acts on it through B/m=k.
4. The canonical Stein factorization is

       W → Spec B^h → Spec B.

   The first map is proper, birational, has geometrically connected fibers, and has direct image of its structure sheaf equal to O_(Spec B^h). Its higher direct images are again k at the vertex in degree one and zero above. The finite second map does not resolve the remaining depth-two vertex defect of B^h.
5. W has no global regular retraction to W_red. Its projective base S does have the specified middle-projection retraction. W is a nonreduced CM modification, not a smooth resolution.

All constructions and computations use formal universal parameters only. No actual operation, source, selected input, model matrix, rank evaluation, or physical transport is performed.

## 1. Projectivizing the universal kernel on all directions

The defining map is

    φ:R→k[u_1,…,u_5,r_1,r_2,r_3,p_1,…,p_5]/(p)²,
    x=r_1(u+p), y=r_2u, z=r_3(u−p),
    Q=ker φ.

The ideal Q is multihomogeneous for the three input degrees. Its radical P defines the projective diagonal. Consequently the multiprojective subscheme defined by Q is topologically the diagonal and is covered by the common-coordinate charts x_i y_i z_i≠0 in multiprojective notation.

On such a chart, radial absorption from Section 2 of the primary-closure proof gives the exact normalized expressions

    x=ρ_1(v+q), y=ρ_2v, z=ρ_3(v−q),
    v_i=1, q_i=0, (q)²=0.

Here the scalar coordinates ρ_j are invertible. The localized image algebra is exactly

    k[v_j (j≠i),q_j (j≠i),ρ_1^±1,ρ_2^±1,ρ_3^±1]/(q)².

Indeed ρ_1=x_i, ρ_2=y_i, ρ_3=z_i, v=y/ρ_2 and q=x/ρ_1−v recover all these generators. Conversely these normalized parameters satisfy precisely the universal kernel: localization loses no identities because the denominators are regular, and the redundant radial variable can be absorbed into the ρ_j. This is the exact kernel argument, not an appeal to a rank calculation or a leading-order normal form.

Taking degree zero for the independent three scalar gradings gives

    k[v_j,q_j:j≠i]/(q)².

For another common-coordinate chart, put a=ℓ_j(v), b=ℓ_j(q). The exact changes of normalized representatives are

    v'=v/a,
    q'=q/a−bv/a².

They are the differential changes of projective coordinates. Thus the nilpotent coordinate functions glue as Ω_T, with no nilpotent shift in v. The three direction maps are v+q, v, v−q, hence their pullbacks on functions are a+da, a, a−da. This proves the assertion globally over T. In particular the first two direction maps identify this with the usual first infinitesimal diagonal: on reduction the identification is the identity, and on its conormal it is the identity Ω_T→Ω_T.

This proof uses the universal Q, whose primaryness was established independently of behavior at a special direction. It does not extend any rank-ten assertion about J beyond its proved open set.

## 2. The intrinsic blowup and local Cohen–Macaulayness

The ambient product blowup of V³ has the canonical presentation

    Tot_(T³)(L_1⊕L_2⊕L_3),

as proved by its Rees charts in `../full-boundary-product-blowup/PROOF.md`. In a chart it has independent scalar coordinates ρ_j and normalized direction coordinates. A multihomogeneous equation F∈Q of degree α becomes ρ^α times its direction dehomogenization. After inverting ρ_1ρ_2ρ_3, these scalar factors are units. The contracted ideal is exactly the extension of the direction ideal: multiplication by ρ_1ρ_2ρ_3 is regular in any polynomial ring over the direction quotient, even when that quotient is nonreduced. Thus saturation of the total-transform ideal gives precisely the projective scheme from Section 1, times the three scalar coordinates.

The image-definition of the Rees algebra identifies this saturation with the intrinsic blowup chart; it is not ordinary closed base change of the ambient blowup. The charts therefore glue to Tot_S(L_1⊕L_2⊕L_3). This also supplies a closed embedding in the projective ambient blowup and proves projectivity over Spec B.

Locally on T all three line bundles trivialize, and the resulting ring is

    A[q_1,q_2,q_3,q_4]/(q)²,

where A is the smooth coordinate algebra of an open of affine seven-space. At any point, a regular system of parameters of the localized regular ring A is a regular sequence on the displayed free A-module. Its Artinian reduction has square-zero maximal ideal of dimension four and socle of dimension four. Hence W is CM, of local type four everywhere, with dimension seven. In particular it is nowhere reduced or smooth.

Over the dense locus of at least two nonzero columns, the normalized q coordinates are recoverable and the map is an isomorphism. This proves birationality with the nilpotent structure retained. At the vertex, each normalized scalar ρ_j is itself an input coordinate, so setting all input coordinates to zero sets precisely ρ_1=ρ_2=ρ_3=0. The fiber is S, of dimension four. Thus f is not finite.

## 3. The coefficient extensions and their cohomology

Let p:W→S be the vector-bundle projection and π=π_2:S→T the finite split projection. Both are affine. For α=(a,b,c)≥0 and d=a+b+c, put

    M_α=π_*(L_1^(−a)⊗L_2^(−b)⊗L_3^(−c)).

Then, as an O_T-algebra,

    (πp)_*O_W=⊕_(α≥0) M_α,

with multiplication induced by tensor product of the indicated invertible O_S-modules. Restriction to the reduction gives an O_T-module exact sequence

    0→Ω(d)→M_α→O_T(d)→0.                 (1)

These extensions must not silently be replaced by split modules. If c(L)∈H¹(T,Ω) is represented by dlog of the transition functions of L, the extension class of (1) is

    (c−a)c(L).

Indeed the first, middle and third lifted line transitions are respectively g(1+dlog g), g and g(1−dlog g); raising to powers −a,−b,−c gives the displayed class. For α=0 the algebra splitting of π does give M_0=O_T⊕Ω.

The Euler sequence

    0→Ω(d)→O_T(d−1)^5→O_T(d)→0

and elementary cohomology of projective-space line bundles show, for d≥0:

- H^i(O_T(d))=0 for all i>0;
- H¹(Ω)=k, H⁰(Ω)=0, and H^i(Ω)=0 for i≠1;
- Ω(1) is acyclic;
- for d≥2, Ω(d) has only H⁰, the kernel K_d of Sym^(d−1)V*⊗V*→Sym^d V*.

In particular H¹(Ω(d))=0 for every d>0. Applying (1) gives

    H¹(T,M_0)=k,
    H^i(T,M_α)=0 for every i>0 and α≠0,
    H^i(T,M_0)=0 for i≥2.

The one possible connecting map at d=0 is zero because 1 has a global lift; equivalently M_0 is split. For every α the map H⁰(M_α)→H⁰(O(d)) is surjective, with kernel K_d (K_0=K_1=0).

Since T has a finite affine cover with affine intersections, its Čech complex computes quasicoherent cohomology and commutes with direct sums. Therefore

    H¹(W,O_W)=k in multidegree zero,
    H^i(W,O_W)=0 for i≥2.                 (2)

Multiplication by any positive-degree function shifts the unique H¹ component into a zero group. Constants act in the usual way. Consequently (2), as a B-module, is precisely the residue field at the vertex. For a proper morphism to the affine Noetherian base Spec B, quasicoherent higher direct images are the sheaves associated to these cohomology modules. This proves the asserted higher-direct-image formulas.

## 4. Global sections equal the Hartogs hull as an algebra

The reduced total space has section algebra

    Γ(W_red,O)=⊕_(α≥0) H⁰(T,O(d))=C,

with its usual three-input Segre multiplication. The preceding degree-by-degree surjectivity gives

    0→N_W→Γ(W,O_W)→C→0,
    (N_W)_α=H⁰(T,Ω(d))=K_d,
    N_W²=0.                              (3)

These identifications respect the reduced C-action: multiplication on the nilmodule is ordinary multiplication of u-polynomials and input monomials. Thus

    N_W=⊕_(α≥0) r^α K_d=N^h,

where N^h is the unrestricted-input nilmodule of the cited Hartogs-hull construction. Its ordinary degree-d part is K_d⊗Sym^d(k³).

To compare the algebras rather than only their dimensions, restrict to the dense all-inputs-nonzero locus, where W and Spec B agree. This restriction is injective on regular functions: in the local presentations above multiplication by the product of the scalars is regular. It identifies Γ(W,O_W) with a subalgebra of the common total quotient algebra of B. The map B→Γ(W,O_W) is the original map induced by f, and its composite with (3) is the usual surjection B→C. Given any section, subtract a B-lift of its reduced image; the difference belongs to N_W=N^h. Therefore, inside that common algebra,

    Γ(W,O_W)=B+N^h=B^h.                   (4)

This proves equality with its full multiplication and its specified B-algebra structure. Finiteness and the intrinsic S2/Hartogs characterization follow as in VERTEX_DEPTH.md; alternatively (4) is finite because N^h is generated as a C-module by its degree-two part. The hull is CM away from the vertex but has depth two at that vertex, so (4) is not a finite CM repair.

### An explicit multiplication formula

For completeness, let w_α=a−c and λ_α=w_α/d when d>0. A convenient graded vector-space lift of a homogeneous polynomial f(u) of degree d is

    σ_α(f)=r^α(f+λ_α df),

where df means the p-linear polynomial Σ_i(∂_i f)p_i. These lifts belong already to B: contraction of the first-order part of any B-lift is w_α f; subtracting λ_α df leaves an element of K_d, which is present in every mixed-support degree. For a pure-support degree the substitution in its single input gives this formula directly.

Accordingly a positive-degree element of B^h may be written (f,k)_α with k∈K_d. For β of positive total degree e and an element (h,l)_β, their product is

    (fh, h k+f l+C_(α,β)(f,h))_(α+β),

where

    C_(α,β)(f,h)
      = (λ_α−λ_β)/(d+e) · (e h df−d f dh) ∈ K_(d+e).

Euler contraction of the parenthesis is zero. Constants multiply in the ordinary way, and products of two nilpotent terms are zero. This follows directly by multiplying the σ-expressions in the universal square-zero parameter algebra, so associativity is automatic. It also makes explicit why the chosen graded vector-space splitting is not an algebra splitting.

## 5. Stein factorization

The relative affine spectrum of f_*O_W is Spec B^h by (4). Proper Stein factorization consequently gives

    f: W --h--> Spec B^h --ν--> Spec B,

with ν finite, h proper, h_*O_W=O_(Spec B^h), and geometrically connected fibers. Both maps are birational and are isomorphisms over the locus with at least two nonzero columns. The topological map ν is bijective: both algebras have reduction C and differ only in their nilpotent modules. The fiber of h above the vertex is again S, since its defining maximal ideal includes the original scalar coordinates, and the added positive-degree nilpotent sections vanish on their common zero locus.

Because ν is affine, its direct image on quasicoherent sheaves is exact. The higher direct images of h can also be computed directly from the affine base Spec B^h using (2); the B^h-action on H¹ is again the residue-field action. Thus

    R¹h_*O_W=k(vertex),    R^ih_*O_W=0 for i≥2.

The surviving one-dimensional group is consistent with H²_m(B^h)=k and depth(B^h_m)=2. It is not evidence of a further finite CM intermediate algebra: the finite birational S2 hull is already forced by Hartogs extension.

## 6. No global retraction, and the precise scope of the modification

Restrict to the open in W on which all three scalar coordinates are nonzero. Its reduction identifies with

    U=(V\{0})×G_m²,
    (u,s,t)↦(su,u,tu).

Use local normalized transverse representatives p_i with λ_i(p_i)=0 and λ_i(u)=1. The exact scalar transitions are

    S_j=S_i(1+a_ij), T_j=T_i(1−a_ij),
    a_ij=(λ_j−λ_i)(p_i).

As in `../rank-one-global-splitting/PROOF.md`, the algebra-extension class of this open thickening is

    κ=e·(s∂_s−t∂_t),

where e is the connecting class of 1 for

    0→N→V*⊗O_U --evaluation at u--> O_U→0.

Here Γ(U,O_U)=k[u_1,…,u_5,s^±1,t^±1], by extension across the missing codimension-five locus. If e vanished there would be global polynomials/Laurent polynomials f_i with Σ f_i u_i=1, impossible after setting u=0 in this polynomial identity. Thus e≠0. Applying the global one-form dlog s to κ gives e, so κ≠0 and this open thickening has no retraction to its reduction, even allowing arbitrary changes of the lifted u,s,t coordinates.

Any retraction W→W_red would restrict to a retraction on this open, since a retraction is the identity on the underlying topological space and therefore preserves the inverse image of every reduction-open subset. This contradiction proves the claim. It also excludes an algebra section C→B^h of the reduced-quotient map B^h→C: such a splitting would restrict on U, where Spec B^h agrees with the original open thickening, to the same forbidden retraction.

Thus the projective splitting S→T does not split its total space: the opposite infinitesimal deformations of L_1 and L_3 obstruct that conclusion. The construction solves the finite-CM no-go by allowing a proper NONFINITE modification, retaining generic multiplicity five and local CM type four. Its positive-dimensional exceptional fiber and its nonzero R¹ are essential parts of the answer. No reduced smooth-resolution or rational-singularity claim is made.
