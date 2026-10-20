# Preserved mathematical audit

This review concerns the source manuscript and its stated assumptions. It is preserved as mathematical history, not a new independent certification of all publication edits or of unpublished input theorems. Source and publication hashes are recorded in SOURCE-HASHES.json. A split manuscript’s module or polar application remains conditional in its destination unit.

# Independent audit of the normalization-module resolution

## Verdict and scope

The proof in `PROOF.md` is correct as written. The minimal resolution, strict unit comparison, finite one-row model, duality identification, and sixteen-dimensional boundary criterion all follow without evaluating a selected HM/source matrix or claiming a new numerical rank. The available negative-twist HM cohomology is sufficient for the asserted sixteen-dimensional group; no unproved positive-twist vanishing is used.

The audit independently checked the algebra, representation identities, derived comparison, and finite dimension arithmetic. In particular, it did not infer a restriction-map rank from a Hilbert series or from a list of cohomology dimensions.

## 1. Saturation, Cohen–Macaulayness, and every Betti degree

Put L=O_S(3,1). The finite morphism f supplies a coherent sheaf f_*O_S on P4, and M is its full graded section module. The extension to all integer degrees agrees with the stated nonnegative definition because H0(S,L^t)=0 when t<0. Consequently the section-module local-cohomology sequence gives both H0_m(M)=0 and H1_m(M)=0, not merely the latter in large degree.

For every integer t, Künneth gives

    H1(S,O(3t,t))
      = H1(P1,O(3t))⊗H0(P1,O(t))
        ⊕ H0(P1,O(3t))⊗H1(P1,O(t)) = 0.

For nonnegative t both H1 factors vanish; for negative t both H0 factors vanish. Thus H2_m(M)=0. The support is the affine cone over the surface N and has dimension three. The module is therefore Cohen–Macaulay of depth three over the regular five-variable ring R, with projective dimension two.

The remaining local cohomology has degree-t piece H2(S,O(3t,t)). It is nonzero exactly when t≤−2, with dimension (−3t−1)(−t−1). Hence its highest nonzero degree is −2 and reg M=1.

The section count gives

    Hilb(M,z)=(1+5z)/(1−z)^3
             =(1+3z−9z²+5z³)/(1−z)^5.

The dimension-eight degree-one space contains the five-dimensional ambient V4 injectively. Nondegeneracy can also be checked geometrically because the diagonal image includes the rational normal quartic. The degree-zero generator plus a complementary V2 in degree one therefore generate, by regularity. They have no relation in degree one. This proves the lower shifts 2 for F1 and 3 for F2; regularity proves the matching upper shifts. The Hilbert numerator then forces 9 and 5. This establishes

    0→5R(-3)→9R(-2)→R⊕3R(-1)→M→0

without an unsupported cancellation assumption. The adjacent terms have strictly different generator degrees, so no homogeneous degree-zero cancellation is available in this minimal resolution.

## 2. Equivariant coefficients and the unit

The claimed SL2 coefficient spaces check:

    F0=R⊕V2R(-1),
    F1=(V4⊕V2⊕V0)R(-2),
    F2=V4R(-3).

In degree two, subtracting M2=V8⊕V6⊕V4 from

    Sym²V4⊕V2⊗V4
      =(V8⊕V4⊕V0)⊕(V6⊕V4⊕V2)

leaves V4⊕V2⊕V0. Surjectivity here follows from the already established generation. In degree three, the identity

    Sym³V4=V12⊕V8⊕V6⊕V4⊕V0,
    M3=V12⊕V10⊕V8⊕V6

and the stated exact character subtraction leave V4. Semisimplicity over C justifies these representation identifications.

The degree-zero generator is literally the section 1, so O→R• is its strict inclusion in the O summand. This does not make O→f_*O_S injective. Its kernel is I_N. The proof explicitly preserves this distinction.

## 3. Strict finite H4 model and arithmetic

The prior complex E0 represents B(-4) by vector bundles; the resolution R• represents f_*O_S by vector bundles. Their total tensor product therefore computes B(-4)⊗f_*O_S, with no unwanted derived Tor because B(-4) is locally free. The strict unit inclusion induces E0→Tot(E0⊗R•).

For k between −3 and 3, the twists of E0^k are k−4. Tensoring by the summands of R• adds 0, −1, −2, or −3. Every resulting twist is negative. A negative line bundle on P4 has only possible H4, so the relevant hypercohomology spectral sequences have a single nonzero row. In particular their degeneration and the compatibility of the induced restriction map are genuine consequences of a single-row model, with no cross-row comparison or hidden transfer map.

With m_k=(10,80,245,353,245,80,10), each summand contributes

    m_k · a · binom(−k+3−s,4)

when its R• summand is aO(s) and k−4+s≤−5, and contributes zero otherwise. Independent arithmetic gives, at total internal degrees −5,…,0,

    dim Z = 6300, 34300, 69275, 63550, 25930, 3664.

All other terms vanish. Their alternating sum is

    −6300+34300−69275+63550−25930+3664=9.

The total cohomological degree is internal degree plus four. Hence both the ambient and normalized H2 groups occur in internal degree −2, as stated. The unit comparison is the coordinate inclusion of C into Z and commutes with the H4-induced differentials. This supplies the claimed finite kernel test without choosing Čech contractions.

For the smaller strict quotient Q, the sheaf cohomology is correctly retained:

    H^-1(Q)=B(-4)I_N,
    H0(Q)=B|C⊗O_P1(-18).

Indeed it is the cone of the unit map, and the normalization quotient is O_C(-2), while O_Y(-4)|C=O_P1(-16). It is not a resolution of only that quotient sheaf.

As a supplementary consequence, the triangle gives

    ker rS=im[H1(Q)→H2(B(-4))].

The corresponding chain map Q→B(-4)[1] is the quadratic component 9B(-6)→B(-4), with the compatible connecting sign. This does not mean that the image can always be computed from that component on ordinary H2 alone: H1(Q) can also retain secondary information arising from the H3 row. The dual criterion in the proof safely retains the needed information.

## 4. Ext-duality and the precise Gysin map

Cohen–Macaulayness in codimension two implies that the sheaf Ext of f_*O_S into ω_Y is concentrated in degree two. Proper duality, using finite normalization followed by the codimension-two inclusion, identifies this Ext² with f_*ω_S. Dualizing the minimal resolution into O(-5) thus gives exactly

    0→O(-5)⊕3O(-4)→9O(-3)→5O(-2)→f_*ω_S→0.

Tensoring with B(4) uses B≅B∨ and yields E, L, P as written. Since f*O(4)=O(12,4) and ω_S=O(-2,-2), the final bundle upstairs is f*B⊗O(10,2).

The transpose of the strict unit inclusion is projection to the first summand of E=B(-1)⊕3B. The Yoneda two-extension associated to the displayed dual resolution is the composite of its two connecting homomorphisms. Consequently the map

    H0(S,H)→H2(E)→H2(B(-1))

is precisely the Serre-dual transpose of normalized restriction, with the common compatible connecting-sign convention. It is not merely an abstract map between spaces of the correct dimensions.

The dimension computation is also correct:

    h0(B)=h3(B)=h4(B)=0,
    h1(B)=24,
    χ(B)=3−25=−22,
    h2(B)=2.

The vanishing of h3(B) follows from h1(B(-5))=0, and that of h4(B) from h0(B(-5))=0. Thus h2(E)=10+3·2=16. The value h3(B(-4))=5 must not be confused with h3(B)=0; the final proof makes no such confusion.

## 5. Exact lifting criterion and retained dependencies

For K=im(L→P), exactness of 0→E→L→K→0 identifies the image of H1(K)→H2(E) with

    V=ker[H2(E)→H2(L)].

The kernel of this connecting map is im H1(L). Therefore mapping any lift of v∈V into H1(P) is independent of the lift after quotienting by im[H1(L)→H1(P)]. This proves that σ:V→J is well defined.

Exactness of 0→K→P→f_*H→0 then gives

    im Δ=ker σ,
    im δS=pr₁(ker σ).

For the reverse containment in the first equality, σ(v)=0 means that an H1(L) image can be subtracted from the chosen lift so its H1(P) image becomes zero. It therefore comes from H0(S,H). No H1 or H2 group has been silently discarded.

The rank formula, the injectivity and zero-map criteria, the stated sufficient criterion, and the more general criterion

    pr₁(V)=H2(B(-1)),
    σ(V)=σ(V∩ker pr₁)

all follow by finite-dimensional linear algebra. The last condition is exactly the ability to cancel the σ value using auxiliary directions without changing the ambient ten-component.

The proof properly stops short of asserting that any of these map-level conditions holds for the actual HM bundle. Its sixteen-dimensional intermediate space is a genuine compression of the possible detector directions, not an evaluated detector rank. The separate conductor/cusp map β remains necessary on ker rS when normalized restriction is not known to be injective.
