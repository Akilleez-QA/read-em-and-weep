# Simultaneous elliptic CM: source-bound obstruction to the obvious lift

## Result

The strongest result is the independently verified rank-250 certificate in CONSTANT-GAMMA-ADDENDUM.md: all 375 constant coefficient equations force M=N=0 in M gamma(v)=gamma(Sv) N. This excludes every constant gamma intertwiner, including non-diagonal ones. The two earlier arguments below remain useful separate checks.

Follow-on strengthening: CONSTANT-GAMMA-ADDENDUM.md now excludes ALL constant intertwiners of gamma, not just diagonal ones, using the separately authorized fixed coefficient linear system. Statements below that leave non-diagonal gamma lifts open describe the initial six-entry argument only. Coordinate-dependent and abstract bundle lifts remain outside both results.

The order-four curve automorphism exists over Q(i), but it supplies no authenticated extra symmetry of the pinned complete source/detector pairing. The original analysis supplied two exact obstructions before a detector-character argument can start:

1. Six entries of the homogeneous differential gamma exclude every constant diagonal intertwiner for the induced coordinate action.
2. A genuine pole in one stored primitive inclusion excludes even arbitrary constant invertible row/column changes combined with any permutation of the six stored carriers as an intertwiner of the literal primitive family.

These are bounded nonexistence statements. They do NOT prove that the underlying bundle has no CM lift by a coordinate-dependent gauge or after cover refinement. They do not prove the complete scalar has no accidental covariance. No such alternative lift/covariance is established here. All 30 remaining detector tests remain unknown; the already known full-S4-sign two-dimensional boundary is unchanged. No source evaluation or external post was made.

## Pins and prior-work distinction

The model is the literal file hm-pinned-model.json at commit 10810ee877fdaf291399198ad60d7dd0c316a42d, SHA256 635bb12d9986e0dcada161d4173c773c4f134b9225354a3bc74267840ca19926. Original source: https://github.com/Akilleez-QA/read-em-and-weep/blob/10810ee877fdaf291399198ad60d7dd0c316a42d/research/hm/null-operator-compiler/hm-pinned-model.json .

The primitive decoder and transitions are raw_engine.py at e93cf712f9da4926a8450cc870ed45a7bfc379ab, SHA256 c9804022b362277d63217c7674c4d6d3dff5941ae4210c30f51f3b5cf3868da9, saved at raw_engine.py. Its _build_body computes v0=1, vj=e_j(x1,...,x4); polynomial/matrix decode the stored records, primitive uses I/di and P/dp; g uses D_b(P_a I_b)^t D_a^-1.

The homogeneous convention is the inert historical verify_homogeneous_identities.py.txt, SHA256 ad6fdb925262b9661bd51c0f65fe1a48d8f4ab1927bbf14b23786a4f0e1503bf, in sources. Its hom(p,1) homogenizes gamma, delta, ev; primitive weights are I columns (0,1), P rows (0,-1), H0/H1 weight -1. It was read, never imported or executed. The primitive-contraction-bridge PROOF and pins identify the same files.

Reviewed prior reductions: permutation-sector-reduction/PROOF.md and ORDERED_NERVE.md, post-spike-symmetry notes, fixed-source-incidence-public/RESULT.md, scalar-frame-bridge-public/{frame,scalar}/PROOF.md, and the old public-math-foundations/null-proof-foundations notes. Their S4/D8 action permutes elliptic factors and therefore FIXES elementary symmetric coordinates. CM instead changes those coordinates. Deck signs fix all x and v. Thus neither prior reduction establishes this lift. This packet analyzes frozen source pins; it does not authenticate a current remote head.

## 1. What genuinely transforms on the curve

Write sigma(x_a)=-x_a, sigma(y_a)=i y_a. It preserves y_a^2=x_a^3-x_a, has order four, and its square is the simultaneous deck involution. It commutes with every separate deck involution and with factor permutations. On elementary coordinates sigma(v_j)=(-1)^j v_j, including fixed v0. Elementary coordinates are algebraically independent, so the polynomial mismatches below survive pullback to the product of curves.

For invariant derivations V_a(x_a)=y_a, V_a(y_a)=(3x_a^2-1)/2, the exact law is sigma V_a sigma^-1=-i V_a. Equivalently sigma(V_a f)=-i V_a(sigma f). The differential dx_a/y_a has character i. Each polarization bivector V_a wedge V_b has character -1, and their complementary product has character +1. The full product y1 y2 y3 y4 has character i^4=1. Consequently this is not an automatic sign-reversing symmetry of a second-order complementary-pair test.

For a fixed legal-mask label m, nu_m=product(y_a/x_a)^m_a transforms by (-i)^|m|, hence D_m=diag(nu_m,nu_m^-1) has a known constant diagonal multiplier. Both q_ab,d and the old connection coefficient m_d y_d/[x_d(x_d^2-1)] have character -i. These true laws do not determine the primitive I/P transforms.

## 2. Exact homogeneous gamma obstruction

All indices below are zero-based. The six literal entries are

 gamma[0,2]=v1, gamma[0,3]=v4,
 gamma[9,3]=-v1, gamma[9,0]=-v2,
 gamma[6,0]=-v3, gamma[6,2]=-v4.

Consider the more general coordinate scaling v_j -> lambda^j v_j and a putative constant diagonal relation gamma(lambda^j v_j)=B gamma(v) A^-1, with nonzero diagonal entries b_r,a_c. Each nonzero entry of degree j forces b_r/a_c=lambda^j. Dividing each row's two equations and multiplying around the six-edge cycle gives

 1=lambda^(1-4+1-2+3-4)=lambda^-5.

Thus lambda^5=1 is necessary. For lambda=-1 it fails in characteristic zero, including Q(i). Original coefficient signs cancel in these ratios; allowing a common extra scalar multiplier on the differential also cancels. This proves no constant diagonal lift of even gamma, so no diagonal lift of the entire homogeneous complex. It does not exclude non-diagonal lifts. The fifth-root condition is only necessary, not asserted sufficient.

## 3. A non-diagonal constant-carrier obstruction from a genuine pole

In the finite chart v0=1, carrier 1 has

 d1=v1 v2 v3 v4-v1^5,
 I_1[5,1]=-(v1^3+v1 v2^2 v3)/d1
          =-(v1^2+v2^2 v3)/(v2 v3 v4-v1^4).

These are directly read literal records, not computed source values. After CM the latter expression is

 sigma(I_1[5,1])=(v1^2-v2^2 v3)/(v2 v3 v4+v1^4).

Let Fplus=v2 v3 v4+v1^4. It is irreducible in Q(i)[v1,v2,v3,v4]: it is primitive and degree one in v4 over Q(i)[v1,v2,v3], with relatively prime leading and constant coefficients. The nonzero numerator is independent of v4, so is not divisible by Fplus. This entry therefore has a genuine pole along Fplus=0. This argument uses formal divisibility only, without values or products of source matrices.

The six stored di denominators are

 v1 v2 v3 v4-1;
 v1 v2 v3 v4-v1^5;
 v1 v2 v3 v4-v2^5;
 v1 v2 v3 v4-v3^5;
 v1 v2 v3 v4-v4^5;
 -v1^2 v3 v4.

None is divisible by Fplus. One can check this in the fraction field Q(i)(v1,v2,v3) by substituting the formal root v4=-v1^4/(v2 v3): each resulting expression is a nonzero rational function; for the denominator containing v4^5 the two resulting monomials remain distinct. Equivalently use polynomial remainder/divisibility. The homogeneous counterpart of d1 is v0 v1 v2 v3 v4-v1^5 and changes its second sign; v0-padding cannot repair the mismatch because v0 is fixed.

Every entry of any original I_c is regular at the generic point of Fplus=0. Multiplication on either side by constant matrices, and any permutation of the six carriers, preserves this regularity. But sigma(I_1) has the genuine pole just exhibited. Therefore no equalities sigma(I_c)=A_c I_pi(c) B_c with constant invertible A_c,B_c can hold for all c. This includes non-diagonal matrices and basis permutations. It is an obstruction to this literal primitive-family covariance, not an intrinsic pole of the underlying bundle: a coordinate-dependent gauge can introduce/remove frame poles, and a refined cover can add the transformed carrier. Those would require new proofs.

## 4. Downstream obligations that cannot be skipped

Bundle/complex: the curve automorphism alone does not supply maps intertwining gamma, delta, ev or a lift on their cohomology bundle. Section 2 rules out the simple diagonal recipe; section 3 rules out constant carrier-relabelled primitive covariance. A general bundle non-isomorphism theorem is not claimed.

Transitions: g_ab=D_b(P_a I_b)^t D_a^-1. The known CM factors of D do not repair the missing I/P intertwiner. One cannot assign a transition character solely by counting y factors.

Raw scalar: if an actually proved constant intertwiner made all directional B blocks transform by -i times conjugation, the exact raw-scalar formula would transform by (-i)^2=-1: the wedge terms, q times endpoint traces, and -15 qa qb/8 all have two directional factors. This is a conditional covariance calculation only. The moving-frame construction differentiates U=(gamma,I,H1W); the missing primitive intertwiner prevents applying it to the actual source.

HPL/selector: I_phys=I D and P_phys=D^-1 P enter insertion j; the homotopies use the same primitive data and face-leading owners. The literal selector is X13[5,0]+X02[1,3]+X02[4,2]. Even an abstract bundle lift would still need its HPL comparison and transformed selector/test established. Neither a commuting deck projector nor the two- and four-derivative character counts does that.

Polarization/test: both pair bivectors change sign, so their product does not. A complete pairing action needs covariance of the coefficient bundle, residual, test/selector, and trace/extraction on the actual covers. No new character projector or detector annihilation is justified. Formal extension to Q(i) does not supply these missing maps.

## Controls

check.py reads the pinned JSON as inert records, checks six gamma monomials, the exact pole-witness numerator, the six di/dp/dh lists, and integer degree/character arithmetic. It never imports production modules, constructs/evaluates actual matrices, or computes physical source values. Normal and optimized runs pass; both retain explicit error checks. The proof of the genuine-pole obstruction is the elementary divisibility argument above, not a claim that a literal hash or degree checker certifies all bundle geometry.

## 5. Retained polynomial-weight parities (additional bounded check)

Using weight-metadata.json, all displayed monomials in each request have one total-degree parity. Q=x1x2+x3x4 is even. IDs 0–19, with Q^2 weight, are all even. Among IDs 20–29, odd weights occur precisely at IDs 21,24,26,28 (v1 Q or v3 Q); the other six are even. Thus the 30 polynomial weights split 26 even / 4 odd. The two removed weights v0^2 and v1 v4 have even and odd parity respectively, illustrating that CM weight parity is not the previous S4-sign criterion.

This is only a weight classification. The accompanying coefficient maps L_(i,b) need not be fixed or eigenmaps under any as-yet-unproved bundle action. Hence these parities do not classify full detector characters, distinguish vanishing actual tests, or give a 26+4 cohomological reduction. The independent check uses only the published integer dual_monomial metadata, without coefficient/source evaluation.

For clarity, the derivative law in section 1 is equivalently V_a sigma=i sigma V_a. Four physical derivatives have scalar factor i^4=1 in that orientation, or (-i)^4=1 in the opposite orientation. Neither identity proves source covariance.
