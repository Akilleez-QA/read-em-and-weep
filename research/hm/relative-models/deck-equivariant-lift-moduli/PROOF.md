> Publication scope: Exact even/odd two-parameter torsor dimensions and diagonal restriction ranks; imports public two-parameter existence. Historical statements about unresolved mixed classes refer to the source stage; this packet does not supersede the separately stated conditional mixed-vanishing result in PR145.

# Exact two-parameter deck-equivariant ambient lift moduli

## Statement and scope

Let X=C^4, where C is the elliptic curve (not affine four-space), and G=(C2)^4 act by independent factor inversions. Put P={1,2}, Q={3,4}, R=P symmetric-difference Q={1,2,3,4}. Parameters s,t carry characters P,Q respectively. Let m=(s,t), A_N=C[s,t]/m^N and I_N=m^N/m^(N+1). Fix the literal G-equivariant ambient two-jet of null's comment, and work with regular normalized differential algebroids on the same G-stable affine cover, allowing higher products, overlap maps and triple units to vary.

For every N>=3 and every literal equivariant lift over A_N extending that two-jet, the classes of lifts over A_(N+1), modulo equivariant gauges literally identity over A_N, form a nonempty torsor T_N under

H_N=(HH^2(X) tensor I_N)^G.

The exact dimensions are:

- N=2m, m>=2: dim H_N=4(m+1).
- N=2m+1, m>=1: dim H_N=8(m+1).

Every class continues formally. Distinct points of T_N cannot be identified even by equivariant gauges merely identity over A_3, with the usual inner 2-isomorphisms. Relative equivariant 1-automorphisms have no nontrivial classes modulo inner 2-isomorphism. This is not uniqueness of objects or uniqueness of literal gauge formulas.

For the diagonal s=t=h, each T_N maps affinely to the 28-dimensional inversion-invariant one-parameter lift torsor of the fixed diagonal preceding jet. Its image has dimension 4 for N even and 8 for N odd; its fibers have dimensions 4m and 8m respectively. Thus the image has codimension 24 or 20. These assertions fix the whole preceding two-parameter jet, not just its diagonal.

## Sources and novelty

Public sources:
https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6259871686

Also read the independently audited one-parameter relative-moduli proof and audits in ambient-lifting-relative-moduli. The small-extension closure identity, existence theorem, and two-parameter starting jet are inputs from null's comment and its preceding literal lifting lemma:
https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6259748725

The new conclusions here are exact degree-by-degree two-parameter moduli, based-gauge rigidity, the precise meaning of full-sign forced coefficients, and the diagonal image and kernel. These do not evaluate the physical presentation, detector values, or module obstructions.

## 1. Linearized complex and representation

Use the shifted normalized differential Hochschild complex D^q=C_diff^(q+1)(O_X), q>=-1, including arity zero, and the Cech total complex L with differential d=delta+(-1)^p b. In total degrees 1,0,-1 respectively its cochains are

z=(u_i,v_ij,a_ijk), w=(t_i,c_ij), r=(r_i).

The degree-zero boundary is dw=(bt,delta t-bc,delta c). Its cohomology is H^j(L)=HH^(j+1)(X). Finite-group invariants are exact over C.

Write V=H^0(T_X)=direct_sum_i C v_i and W=H^1(O_X)=direct_sum_i C w_i. Both v_i,w_i have singleton character {i}. HKR gives

HH^k(X)=direct_sum_(r+q=k) Lambda^r V tensor Lambda^q W.

The weight-zero HH^2 space has basis v_i tensor w_i, i=1,...,4, so dimension 4. For each pair {i,j}, the weight-{i,j} space has basis

v_i wedge v_j, v_i tensor w_j, v_j tensor w_i, w_i wedge w_j,

so dimension 4. These exhaust HH^2: 4+6*4=28. In particular HH^2_R=0.

All HH^1 characters are singletons. All HH^3 characters have odd cardinality: the parity of the symmetric difference of three singleton weights is odd, even when repeated indices cancel. Every monomial in s,t has even-cardinality character, so for all N,

(HH^1 tensor I_N)^G=0, (HH^3 tensor I_N)^G=0.

## 2. One-step lifting and count

The kernel I_N is killed by m and squares to zero. Therefore all positive-order background coefficients disappear in the linearized differences between two lifts; the differential is the classical d, without an N-dependent twist. Null's closure identity puts the trial-lift obstruction in the degree-two cocycles of (L tensor I_N)^G. The vanishing of (HH^3 tensor I_N)^G provides an invariant primitive and hence existence. Differences of genuine lifts are the degree-one cocycles; gauges identity over A_N act by the degree-one boundaries. Thus the quotient is exactly the nonempty torsor asserted above.

The monomial s^a t^b, a+b=N, has character (a mod 2)P+(b mod 2)Q. As all characters are self-dual, an invariant coefficient must have this same character.

If N=2m, the even-even monomials are s^(2j)t^(2m-2j), j=0,...,m. Each carries weight zero and contributes four dimensions. The m odd-odd monomials s^(2j+1)t^(2m-2j-1), j=0,...,m-1, carry R and contribute zero. Hence dim H_(2m)=4(m+1).

If N=2m+1, there are m+1 odd-even monomials s^(2j+1)t^(2m-2j), all of character P, and m+1 even-odd monomials s^(2j)t^(2m-2j+1), all of character Q. Each contributes four dimensions. Hence dim H_(2m+1)=8(m+1).

In HKR types (local product, mixed, gerbe), the degree-2m dimensions are (0,4(m+1),0), and the degree-(2m+1) dimensions are (2(m+1),4(m+1),2(m+1)). These are cohomological types, not a claim that nonlinear representatives can keep each direction confined to one descent slot.

## 3. Full-sign coefficients are forced only modulo relative gauge

At an odd-odd monomial of a fixed one-step problem, the inhomogeneous correction equation is d z_R=-O_R. A solution exists because HH^3_R=0. The difference of any two solutions is closed, and HH^2_R=0 makes it a boundary. Therefore this coefficient has exactly one relative gauge class once all preceding coefficients are fixed.

This does NOT say z_R=0. The obstruction O_R may be a nonzero exact cochain, in which case z_R cannot be zero. Even if O_R=0, nonzero exact z_R can occur and is removable by a relative gauge. In particular the prescribed degree-two mixed terms in null's two-jet are not asserted to vanish. The correct conclusion is absence of independent new full-sign HH^2 parameters, not literal disappearance of odd-odd coefficient operators or units. Changing earlier coefficients can change later O_R and its required corrections nonlinearly.

## 4. Formal continuation and stronger based-gauge separation

Repeat the small-extension argument after any selected literal lift. The obstruction vanishing does not constrain that selection. Keeping all preceding coefficients literally gives an inverse-limit differential algebroid over C[[s,t]]. Each coefficient is regular and of finite differential order; no uniform bound, analytic convergence, or numerical evaluation is claimed.

Suppose two lifts over A_(N+1) agree over A_N, and an equivariant gauge between them is only required to be identity over A_3. Its reduction over A_N is an automorphism of the common preceding object. Assume inductively its first possible nonzero homogeneous term is in degree k, with 3<=k<N. The endpoint agreement implies its leading term w_k is a degree-zero cocycle in (L tensor I_k)^G. Since (HH^1 tensor I_k)^G=0, w_k=d r_k for an invariant degree-minus-one cochain. Target-chart units 1+r_k give a genuine inner 2-isomorphism of the gauge, with the appropriate inverse killing w_k. Their products and inverses exist in the full truncated target algebra. Endpoints remain unchanged; only higher gauge terms can be altered.

Inducting through k=N-1 makes the gauge identity over A_N. Its degree-N action is then a boundary, so it cannot merge distinct points of T_N. The same argument at the first differing relative class separates formal continuations. It also proves that relative equivariant 1-automorphism classes vanish modulo inner 2-isomorphism.

This only covers the fixed base, parameters, cover and strict G-action, with gauges literally identity over A_3. It excludes changes of parameter, base automorphisms, gauges preserving the two-jet merely as an unmarked object, and non-equivariant gauges.

For precision about residual 2-symmetry, HH^0=C has weight zero. The relative degree-2m 2-automorphism space has dimension m+1; the odd-degree space is zero. Full formal based 2-automorphisms are the invariant scalar units

1 + (m^3 C[[s,t]])^G = 1 + ((s^2,t^2)^2 C[[s^2,t^2]]).

Their centrality is exact for normalized parameter-linear products. There is therefore no assertion of unique 2-isomorphisms.

## 5. Diagonal restriction and its sharp deficiency

Let iota be simultaneous inversion of all four factors. Both P and Q restrict trivially to <iota>, so s,t and h are iota-fixed and s=t=h is an equivariant base map for this subgroup. It need not be a full-G-equivariant diagonal map.

Fix the entire preceding two-parameter object over A_N and its literal diagonal object over C[h]/h^N. Diagonal restriction sends lifts and relative gauges to one-parameter lifts and relative gauges. Thus it gives an affine map of torsors whose linear part is

E_N: (HH^2 tensor I_N)^G -> HH^2(X)^iota tensor C h^N,
E_N(sum_(a+b=N) alpha_ab s^a t^b)=(sum alpha_ab)h^N.

For N=2m, only the m+1 weight-zero cohomological terms exist. E_N is the summation map (HH^2_0)^(m+1) -> HH^2_0, surjective of rank 4, with kernel dimension 4m. Its affine image is a translate of HH^2_0 inside the 28-dimensional target, hence codimension 24.

For N=2m+1, E_N is the separate summation on m+1 copies each of HH^2_P and HH^2_Q. It is surjective onto HH^2_P direct_sum HH^2_Q, rank 8, with kernel dimension 8m. Its image has codimension 20 in the 28-dimensional target.

The affine translate depends on the common preceding jet and on a reference lift. The fixed parts of the diagonal coefficient can include characters outside the indicated translation space; only DIFFERENCES of diagonal lift classes are confined to that space. Nonzero kernel directions are genuinely inequivalent full-deck two-parameter relative lifts that become equivalent after diagonal restriction.

Consequently an arbitrary inversion-invariant one-parameter next lift cannot generally be promoted to a full-deck two-parameter next lift of this fixed preceding two-parameter jet. The claim does not exclude promotion after changing earlier off-diagonal jets whose diagonal happens to remain fixed. Such hidden preceding changes can alter the affine image through nonlinear lower-order contributions.

## 6. Boundary of the result

The module extension criterion and its characteristic-map cokernel are separate. This proof neither supplies a module lift nor annihilates any retained obstruction. The full-sign cohomological rigidity here concerns new AMBIENT coefficients only, with preceding jets fixed. All conclusions use varying higher local products, as in the ambient lifting lemma; none assert an all-order extension with local Moyal products frozen.
