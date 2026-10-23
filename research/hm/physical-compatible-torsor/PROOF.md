# Compatible W choices have zero physical trace variation

2026-10-23. A bounded written deduction from actual cone geometry.
No actual HM source, coefficient, point, matrix, rank or calibration is
evaluated. This is not Lean certification. PR889 and PR894 are unchanged.

## Result and strict normal-order boundary

Fix the actual lower data of PR815/894: the canonical/compared correction
b, the preceding V division, Z, J3, the physical frames and harmonic
convention. Let (W0,E0) and (W1,E1) be TWO COMPATIBLE full global choices:

    dEj=S-q Wj,    S=a(V-bZ),    dWj=0,    j=0,1.

Their positive cohomology difference belongs to

    K=ker(q:H1(B(2))_+ -> H1(B(4))_+)=A+D5.

The actual boundary inverse identifies this difference with a unique
global cone adjoint k=gN in H0(B_Q(4))_+. Consequently:

1. The actual physical weight-four coefficient of k is ZERO. The induced
   variation map K->Sym^12(U) is defined and identically zero, including
   its D5 constituent, not merely its A constituent.
2. Every authenticated physical source row of PR815 has the same value
   on S-qW0 and S-qW1. All seven equivariant family-torsor directions
   of PR894 are invisible to that row and to rho16.
3. More intrinsically, the scalar norm n(J4) is unchanged ON ACTUAL 4Q.
   Thus PR815's full rho on Q is unchanged, not only its weight-sixteen
   coefficient. This makes NO claim about the ambient norm, a q^4 norm
   coefficient, a fifth-neighborhood norm error, or a fifth boundary.

There is also a precise source-row quotient: on certified full exact
sources D=dC^0_4, the row annihilates D intersect qC^1_2 and descends to
the cone restrictions of D. This does not define Lambda on arbitrary
ambient sources and does not remove PR894's 27-dimensional membership
gate. It uses an actual global-cone coefficient theorem, not generic
linear algebra or a presumed equivariant physical contraction.

## 1. Exact sources and physical meaning of the coefficient

SOURCE-MANIFEST.json records seven immutable source copies, with their
Git blob and SHA256 authentication.

- membership894 at c963b48d8bd28eaac1dc2db1116fc1c430ba18b4: the actual
  full global complex, preceding-division/canonical-correction premises,
  and compatible cohomology-family torsor Hom_G(R,K) of dimension seven,
  where R=Sym^3(A) tensor D5=3A+3V+3P4+4D5.
- q_exact at eeb1a11799ca38a60c37f6ba96f263ef8e20dd1c: ambient
  H0(B(2))=H0(B(4))=0 and the ACTUAL cone closure

      H0(B_Q(4))_+=N H0(O_Q(2))_+=N(A+D5).           (1)

- spinor at 4e16e69c776bd85506341b5bb785f0d8a396bd3e, Section 5:
  N is the actual invariant nilpotent, N^2=0, and multiplication by N
  injects scalar quadratic sections into actual cone adjoints. The later
  q_exact source, not this earlier note alone, proves equality in (1).
- next_weight at 3d21e93865152ec961ceaf32d48f845399158b69, Sections 1
  and 3.2: the fixed marked physical coefficient bundle fits

      0 -> U O_L(-1) -> E4 --tau--> Sym^12(U) O_L -> 0,

  and EVERY GLOBAL ACTUAL section of B_Q(4) has zero weight-four
  coefficient. The proof retains the actual ordinary transition gap,
  the absence of a regular weight-minus-four adjoint, and global conic
  regularity of tr(Nk). It is not a statement about an arbitrary
  homogeneous coefficient or a freely chosen local frame.
- pr815 at 0eaeca734b9e17142da2f1bdfd9a1721d0bb1d42: the actual
  physical projection P_i(X)=(p_i X i_i)_0, source row Lambda_i,
  full affine weight-sixteen formula, and definition of rho on 4Q.
- ladder at 8d8b5be4ce62c3055bb53be9e16d29cc63072f04: full cochain
  comparison at twists >=2, J4=aJ3-q^3 E, and J4|Q=a^3 h N.
- normalization866 at 25b1d2927294fffbc393e6ac2285f5a58cfd6c60:
  the separate mixed-contraction defect and thirteen-dimensional
  associated-graded affine normalization blind space.

Here U=Wprime is the positive binary representation, not the negative W;
A=Sym^2(W) and V=Sym^2(U) are distinct. The plus sign is the physical
HM-inversion sector authenticated in PR894, not the cone Serre involution.

The separately read PR853 Source2TraceKernel.lean, at
a0834508e3a1772763f28ca88edd98e3d161319c, concerns fixed-pencil diagonal
coordinate trace maps. Its generic kernel statement is not reproved here.
The present deduction uses the actual boundary inverse, (1), and the
global cone coefficient vanishing just specified.

## 2. The variation is an actual global cone adjoint

Use the sign convention

    DeltaW=W1-W0,    DeltaE=E0-E1.

Then

    d DeltaE=q DeltaW,
    J4_1-J4_0=q^3 DeltaE.                           (2)

The restriction sequence for the ACTUAL adjoint bundle is

    0 -> B(2) --q--> B(4) -> B_Q(4) -> 0.

The ambient H0 vanishings give an isomorphism onto the kernel,

    delta_q:H0(B_Q(4)) -> ker(q:H1(B(2))->H1(B(4))). (3)

Because DeltaE is closed modulo q, its restriction induces a global cone
adjoint k. The boundary convention is [d(lift)/q], so (2) gives

    delta_q(k)=[DeltaW].                            (4)

Thus k is uniquely determined by the cohomology class of DeltaW, not by
the chosen cochain representative or primitive. On the positive sector,
(1) gives a unique quadratic g with k=gN. The uniqueness of g uses the
injectivity of multiplication by N, not division by its zero set.

For clarity, if DeltaW is changed by dY, one can change DeltaE by qY.
Its cone section is unchanged. With DeltaW fixed, two primitives differ
by a globally closed twist-four cochain; H0(B(4))=0 makes its induced
cone adjoint zero. Neither assertion says the primitive cochains themselves
are literally equal. The seven-dimensional count concerns cohomology
families, not all cochain representatives.

## 3. The physical coefficient variation is zero without a Schur guess

The actual coefficient theorem in input next_weight defines, in the fixed
marked physical frames, a global extraction on cone adjoints

    chi4:H0(B_Q(4)) -> H0(E4),       chi4(k)=k_[4].

It proves chi4=0. Consequently the rigorously defined variation map is

    nu=H0(tau) composed with chi4 composed with delta_q^-1:
       K -> H0(Sym^12(U) O_L)=Sym^12(U),
    nu=0.                                           (5)

This is stronger than the representation-only observation that A is
absent from Sym^12(U)=1+V+P4+D5 while D5 is present. That observation
would at most allow one D5 coupling after equivariance were proved; it
would not prove its nonzero value or even identify a physical map. Here
the actual map is defined by (3) and the authenticated coefficient
extraction, and the global geometric theorem kills BOTH summands.
No equivariance of a chosen local contraction is needed to infer zero.

Indeed, for any authenticated contraction of the actual monad, restriction
of P_i(DeltaE) to Q is the matrix of the intrinsic section k: DeltaE is
closed on Q. Therefore PR815's full-source identity gives

    Lambda_i(q DeltaW)
      =tr(n8_i [P_i(DeltaE)|Q]_[4])=0.              (6)

Both q DeltaW and S-qWj belong to im(d). Thus linearity on that domain,
with the actual signs retained, gives

    Lambda_i(S-qW1)=Lambda_i(S-qW0).                (7)

This statement is independent of the arbitrary off-cone representatives
but remains a statement about authenticated physical rows. It does not
furnish their numerical matrices or an arbitrary middle-block substitute.

For coherent equivariant families, composing (5) with R->K kills every
one of the seven directions in Hom_G(R,K): three A-type and four D5-type
scalar multiplicity slots. The actual vector space K itself has dimension
eight. Neither dimension is the thirteen-dimensional trace space.

## 4. No hidden lower-weight or affine correction enters rho16

The difference q^3 k on 4Q is supported in the top normal ideal, so it
does not change the q^0,q^1,q^2 normal data. The full actual weight-four
coefficient of k vanishes by chi4=0, hence its q^3 contribution has no
total-weight-sixteen part. This conclusion uses the global coefficient
theorem, not a truncated supported source calculation.

There is also a direct check in the pinned marked cone frames: N=n8,
and g in A+D5 has cover weights zero and four, respectively. Thus k has
weights eight and twelve and q^3 k first has weights twenty and twenty-four.
In particular it changes neither the complete weight-twelve leading
ladder nor the weight-sixteen layer. Higher harmonic terms in a lift of
k are multiplied by q^4 and do not enter a section on 4Q.

In PR815 notation the lower cochain aJ3 and the contraction are fixed,
so y_i is fixed. The lower coefficients s_i,r_i and leading layer L_i
are fixed as well; therefore their FULL affine term Q_i is unchanged.
Combining (7) with the actual formula

    rho16_i=Q_i+a^3 h tau_i(y_i)-a^3 h Lambda_i(S-qWj)

proves rho16_1=rho16_0. The first-normal qZ transport was not omitted:
its contribution to the affine law depends on the same unchanged leading
layer and the same fixed ambient transitions.

If V,b,J3, frames or contractions are changed as well, these fixed-data
arguments no longer apply automatically. In particular the mixed-row
normalization defect of PR866 is not removed by changing W.

## 5. The whole rho on Q is constant, but only through normal order three

Let n(J)=tr(J^2)/2. On 4Q, q^4=0, so the ideal (q^3) is square-zero.
Using (2), trace cyclicity and q central gives EXACTLY on 4Q

    n(J4_1)-n(J4_0)
      =q^3 tr((J4_0|Q) k)
      =q^3 a^3 h g tr(N^2)=0.                       (8)

The quadratic difference term has factor q^6 and vanishes on 4Q. Every
off-cone term of DeltaE or J4_0 in the cross pairing has factor at least
q^4 and vanishes there as well. This accounts for all relevant normal
coefficients, not only an order estimate.

PR815 defines n(J4)=q^3 rho on 4Q, where rho is a scalar section on Q
of physical twist fourteen. The Cartier ideal identification
(q^3)/(q^4)=O_Q(-6) is injective as its ideal inclusion on 4Q. Hence
(8) proves equality of rho on Q, with all cover degrees retained.
No inversion of q or cancellation at a point where q=0 occurs.

At the NEXT normal order the same argument stops. If formal lifts are
written J=J0+qJ1+... and DeltaE=k+qD1+..., then the q^4 cross coefficient
contains tr(J0 D1+J1 k). Neither N^2=0 nor k=gN forces this expression
to vanish. The individual J4 need not even extend to a closed section
on 5Q. Thus (8) says nothing about an ambient norm, fifth-order norm
coefficient or the fourth Bockstein's fifth-boundary value.

## 6. Exact cone-source quotient, with domain ordering retained

Let D=dC^0_4 be the certified full ambient exact-source space. If
T=dE belongs to D intersect qC^1_2, write T=qW. Then dW=0: q dW=0
and multiplication by q is injective on the locally free full monad
cochain terms. Thus E|Q induces a GLOBAL ACTUAL section of B_Q(4).
The next_weight theorem applies even without its being positive and
gives [P_i(E)|Q]_[4]=0. Consequently

    Lambda_i(D intersect qC^1_2)=0.                 (9)

If res_Q is restriction of global degree-one cochains, its kernel is
qC^1_2 by left exactness of global sections of the Cartier restriction
sequence. Therefore there is a UNIQUE row on the indicated quotient,

    barLambda_i:res_Q(D) -> local trace coefficients,
    Lambda_i=barLambda_i composed with res_Q on D,
    res_Q(D)=D/(D intersect qC^1_2).                (10)

This is a local physical row on a certified source-image domain, not an
assertion that its values or chosen contractions are globally invariant.
The same descent holds for the full local weight-four matrix extraction.
Equation (9) is the geometric input; the quotient factorization is its
elementary consequence, not the main new result.

For compatible sources, res_Q(S-qW)=res_Q(S) lies in res_Q(D). Thus the
source-response term can be written barLambda_i(res_Q(S)), independent
of the compatible W choice. Writing Lambda_i(S) is still generally
illegal, because S need not belong to D. Nor does (10) certify that a
particular supplied W satisfies S-qW in D. PR894's full 27-slot test
must precede using the corresponding ambient source formula.

## 7. Why this does not erase the thirteen normalization directions

PR866's thirteen-dimensional blind space is

    H0(E4) = H0(Sym^12(U) O_L),   dimension thirteen.

These are global sections of an associated-graded coefficient bundle.
They need NOT lift to global actual cone adjoints. In fact the pinned
next_weight theorem proves that the actual map

    H0(B_Q(4)) -> H0(E4)

has zero image. The compatible W difference has a genuine lift through
that map by (3)-(4), so it is killed. A hybrid contraction error eta of
PR866, even if its coefficient sections glue, is not thereby represented
by a closed global cone adjoint; its comparison expression applies to
nonclosed source data. There is no basis for applying chi4=0 to it.

Thus compatible W choices cannot be used to tune rho16 or to absorb a
nonzero normalization mismatch. A correct source-row value is unique
along this torsor, but the actual row and lower projection still have
to be constructed and normalized compatibly. No calibration, primitive
or original proof repair is supplied by this invariance theorem.
