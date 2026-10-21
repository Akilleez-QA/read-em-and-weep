# Quadratic primary injection, a structural failure family, and the remaining bridge

## Scope and notation

Work over C with normalized HM bundle F, B=End_0(F), and primary module M_j=H^1(F(j)). Put A0=M_0=V_3, W=W', and U'=Sym^2(W)=sl(W). This A0 is the dual of the five-dimensional A used in PR449. Put G=H^0(F(3)), of dimension four, to avoid confusing the section representation with the three-dimensional representations U,U'.

No selected polynomial, HM multiplication matrix, coefficient, source, or numerical rank is evaluated. Current PR1 was read through the #543 announcement. The results concern the actual natural multiplication and its actual primary submodule from #538.

## 1. The exterior formula

The primary HM representation identities give

    S_2=A0 tensor U',  M_2=V tensor W,
    exterior^2 A0=V tensor W,  Sym^2 A0=V tensor U.

Here U and U' are the two three-dimensional quotient representations. These follow from HM Lemma 3.3(ii),(v) by the third Galois conjugation, while M_0 and M_2 are (4.4),(4.11). On quotient multiplicity spaces the binary central involution acts positively on U,U' and negatively on W. Therefore

    Hom_N(Sym^2 A0 tensor U', V tensor W)=0.

The exterior channel has dimension one: Hom(W tensor U',W) has dimension one, since End(W)=1 direct-sum U' and U' is irreducible. Its nonzero map is the ordinary sl(W)-action on W. Natural quadratic multiplication is nonzero because S_2 M_0=M_2 by degree-zero generation, HM (4.2). Consequently there is a nonzero scalar c such that

    (a tensor D) x = c (id_V tensor D)(a wedge x),

under the displayed exterior-power identification. This is a universal equivariant formula, not an identification with a chosen polynomial-coordinate system.

## 2. Generic primary injectivity without a rank sample

Fix x nonzero and put L_x=x wedge A0, a four-dimensional subspace of V tensor W. The image of universal evaluation

    e_x:S_2 -> M_2,  q -> qx

is Y_x=span{(id_V tensor D)L_x : D in sl(W)}. An invertible traceless D gives dim Y_x>=4. If dim Y_x=4, every invertible traceless D maps L_x onto Y_x. Fix H with eigenvalues 1,-1. Hence all H^{-1}D, initially for invertible traceless D and then for every traceless D by linearity/density, preserve L_x. Their algebra is End(W): it contains the identity and both off-diagonal elementary operators, whose products supply the diagonal projections. Thus L_x=E_x tensor W for a two-dimensional E_x in V.

The rank-four locus in P(A0) is closed. It is proper by a purely linear-algebraic argument. Otherwise every id_V tensor D would preserve every star x wedge A0. An endomorphism of exterior^2 A0 preserving all stars is scalar: intersections of distinct stars are the decomposable lines C(x wedge y), so these are all eigenlines; the decomposable sums x wedge (y+z) force the eigenvalues for intersecting pairs to agree, and a basis of exterior products connects all pairs. This contradicts a non-scalar id_V tensor D. Hence the rank-four locus has dimension at most3.

The projective incidence of ([x],[q]) with qx=0 has fibers of dimension10 over that locus, so this part has dimension at most13. Elsewhere rank(e_x)>=5, and its fibers have dimension at most9 over P(A0)=P4, again giving dimension at most13. The entire incidence therefore has dimension at most13. Its projection to P(S_2)=P14 is closed, being a projective projection, and proper. Outside that projection, q:M_0->M_2 is injective.

This argument is universal for the exterior-plus-sl(W) multiplication model: it needs neither a selected evaluation nor the geometric local-splitting lemma. It proves a nonempty primary-injective quadratic open, not full adjoint injection or residual surjectivity.

For completeness, HM geometry gives the stronger pointwise bound rank(e_x)>=5 for every x. HM Lemma 2.5 says that no nonzero full fiber t tensor W_original in exterior^2 V lies in y wedge V. Third Galois conjugation sends V to V_3=A0, V_1 to V, and W_original to W', giving the same no-fiber assertion for L_x. The above rank-four argument would give L_x=E_x tensor W and contradict that assertion. This stronger statement is not needed for the generic-injectivity conclusion.

## 3. A definite bad family for the full square adjoint map

Let Sigma=P(A0) times P(U') in P(S_2), the Segre variety of decomposable tensors. For every q=a tensor D in Sigma, the exterior formula gives qa=0. The actual primary injection G tensor M_0 -> H^1(B(2)) is multiplication-compatible. Thus

    dim ker(q:H^1(B(2))->H^1(B(4))) >=4.

Both adjoint groups have dimension85, by the independent dimension proof in #543. Their cokernel therefore also has dimension at least4. In particular Sigma is contained in the full quadratic failure locus.

If D is invertible, the exterior formula has primary kernel exactly C a, since x -> a wedge x has this kernel and id_V tensor D is invertible. Thus the primary quadratic rank is exactly4 and its direct adjoint-primary image has dimension16. This is distinct from PR449's quadratic cone for M_1->M_3: the latter is the smaller Segre-Veronese locus where D is nilpotent. For the decomposable tensors here with invertible D, M_1->M_3 is onto, while M_0->M_2 is not injective. No intersection with an unproved residual-good open is asserted.

For every cubic v, set K_j=H^1(B(j-1)), L_3=G tensor M_0, and

    D(q,v)=K_5/(vK_2+qL_3).

If k_v=dim ker(v:K_2->K_5), then dim K_2=55 and dim K_5=85 give

    dim D(q,v)>=85-(55-k_v)-16=14+k_v

for the invertible-D part of Sigma. The same bound >=14+k_v holds on all of Sigma, since the primary rank cannot exceed4 there. The exact quotient criterion from #543 still requires the particular induced N_3 -> D(q,v) to be onto; the numerical lower bound is only necessary.

## 4. Determinant and the exact unresolved square bridge

Let Delta(q) be the determinant of the universal 85-by-85 full adjoint quadratic map, defined up to a nonzero scalar. Either it is identically zero or it is homogeneous of degree85. At every nonzero point of the affine Segre cone, the matrix has corank at least4. The determinant expansion around that point therefore has no terms of order less than4. Equivalently Delta has pointwise local maximal-ideal order at least4 there; in particular it has symbolic order at least4 at the generic point of Sigma. No global ordinary fourth-power ideal membership is claimed.

To identify the remaining obstruction precisely, use the actual rows

    0 -> P_2 -> H^1(B(2)) -> N_2 ->0,
    0 -> P_4 -> H^1(B(4)) -> N_4 ->0,

with dimensions (20,85,65) and (40,85,45). On the proved primary-injective open, coker(q:P_2->P_4) has dimension20. If the residual map q:N_2->N_4 is onto, its kernel also has dimension20. The snake lemma then supplies a canonical lift boundary

    delta_q:ker(q:N_2->N_4) -> coker(q:P_2->P_4).

The full adjoint map is an isomorphism if and only if delta_q is an isomorphism, provided those two stated flank conditions hold. Conversely, full isomorphism forces primary injectivity, residual surjectivity, and this boundary isomorphism. This keeps the actual primary/residual extension; no splitting is chosen.

Thus the new generic primary injection removes one necessary premise, and Sigma gives a concrete unavoidable bad family and a stronger paired load bound. What remains unproved is residual surjectivity on a suitable quadratic open and nondegeneracy of the actual 20-dimensional lift boundary there. Dimensions, generation, and the degree-five coverage theorem alone prove neither. Ordinary Serre self-duality pairs H^1(B(t)) with H^3(B(-t-5)), not with H^1(B(6-t)); it does not turn this 85-dimensional map into an alternating form.

## Sources and dependency boundary

- Horrocks–Mumford, Topology 12 (1973), 63–81, Lemma 2.5 (printed p.69), Lemma 3.3(ii),(v) (p.70), equations (4.2),(4.4),(4.11) (pp.72–73), appendix (p.81): https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf
- PR449, head e4b6acdd27d8da8be4052c117ea2dca0f48f46ff: quadratic M_1->M_3 contraction and its smaller nilpotent cone. https://github.com/Akilleez-QA/read-em-and-weep/pull/449
- PR538: actual primary image extension, not an assumed split Rao model. https://github.com/Akilleez-QA/read-em-and-weep/pull/538
- PR543, head e16586f3058cb02a2aac958ed01282f50385dd2b: independent dimensions and paired quadratic-load quotient. https://github.com/Akilleez-QA/read-em-and-weep/pull/543

These are new deductions for the quadratic map into degree four, not a review or a claim about the original selected coefficients. Generic full quadratic isomorphism and generic/full Q4 vanishing remain unresolved here.
