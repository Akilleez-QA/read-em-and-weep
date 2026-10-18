# An exact finite owned-denominator model for the direct scalar dual solve

## New result

A full homogeneous numerator construction gives an exact finite scalar model in degrees 0,1,2. Unlike a Laurent cutoff, its exactness follows from a locally exact sheaf Koszul resolution with acyclic terms. For the pair character on (P1)^4, its degree-one cohomology vanishes. Consequently the necessary and sufficient kernel-annihilation check for the direct dual solve reduces to the explicit finite identity D0^t e=0. A bounded total-primitive construction below proves this identity formally for the authenticated detector, without evaluating its physical coefficient rows.

The construction uses actual vertex-owned denominators; no new apex, transferred owner, or second partition enters the scalar differential. The model is very large. Its existence is not a multiplication or storage certificate.

## 1. General finite-model lemma

Let X be a projective integral scheme over k, F a line bundle, and v range over a finite ordered set of cover vertices. Let d_v be a nonzero global section of a line bundle L_v. Assume:

(A) The principal opens U_v={d_v!=0} cover X.

(B) For every nonempty vertex subset I, the bundle F tensor product_(v in I) L_v is acyclic in positive sheaf-cohomology degrees.

Define the sheaf cochain complex

    C^q = direct sum_(|I|=q+1) F tensor product_(v in I) L_v.

For J=(j0<...<j_(q+1)), define

    (D a)_J = sum_l (-1)^l d_(j_l) a_(J minus j_l).

Augment it by F -> C^0, f -> (d_v f)_v. This augmented complex is exact: locally where d_w is a unit, multiplication by d is wedge multiplication by a nowhere-zero vector in direct sum_v L_v. Contraction by the local dual vector selecting d_w and dividing by d_w satisfies contraction*d + d*contraction = identity. This proves exactness as SHEAVES; no meromorphic extension to an absent owner is made.

The nonaugmented complex C^0->C^1->... is therefore a resolution of F in degree zero. Assumption (B) makes its global sections an acyclic resolution. Equivalently, its hypercohomology spectral sequence collapses to the global-section complex. Thus, for Vq=H0(X,C^q),

    H^q(V•,D) = H^q(X,F).

In particular H1(X,F)=0 implies ker D1=im D0. All Vq are finite-dimensional. Only V0,V1,V2 are required to compute this equality, although its proof uses the complete finite Koszul resolution.

For the I summand, send a global numerator P_I to the regular cochain P_I/product_(v in I)d_v on U_I. This is injective because X is integral and U_I is dense whenever nonempty. An empty intersection may instead be omitted together with its zero regular-cochain space; for the present irreducible variety all finite intersections of nonempty principal opens are nonempty. Dividing the displayed differential by the J denominator gives the actual alternating Cech restriction differential. Thus this is a finite SUBCOMPLEX of regular rational cochains, with no projection or numerical truncation.

## 2. Instantiation on the authenticated common refinement

Take X=(P1)^4, F=O(n), with n=(0,0,-2,-2) or its pair permutation. Use the actual common vertices v=(e,b,m) of the authenticated source-first cover. Write H_b for the homogeneous carrier equation and ell_(m,i) for the actual homogeneous legal defining section in coordinate i. Factors equal to 1 are harmless. Write Z_(e,i)=Y_i for e_i=0 and X_i for e_i=1.

Set

    d_v = H_b^14 product_i ell_(m,i) product_i Z_(e,i)^5250,
    L_v = O(div d_v).

The pinned homogeneous definitions in `hm-regular-cover-transport.md` section 1 are ell_(0,i)=Y_i and ell_(1,i)=X_i(X_i^2-Y_i^2). The carriers are H_*=a and H_j=h_j, where product_i(Y_i+X_i z)=sum_j v_j z^j, a=v0 v1 v3 v4 and h_j=v_j^5-v0 v1 v2 v3 v4. Thus every d_v is genuinely globally homogeneous. This is the same ownership interpretation used for global numerators in refined-tracefree-pole-domain.md section 6 and scalar-cover-and-domain-audit.md section 7.

The carrier opens cover: if a and every h_j vanished, the identities v_j^5=h_j+v2 a would force every v_j to vanish, impossible because product_i(Y_i+X_i z) is a nonzero polynomial at every point of X. The two legal sections cover each P1 because Y_i=0 forces X_i^3!=0. Combining with the standard charts proves the common cover assertion. A compiler must retain these actual homogeneous sections, rather than replace them with unhomogenized affine expressions.

The locus d_v!=0 is exactly the corresponding standard/carrier/legal common open, and these opens cover X. Every coordinate degree of L_v is at least 5250. Therefore for every nonempty I, every coordinate degree of F tensor product_(v in I)L_v is at least 5248. The usual homogeneous-monomial basis describes all its global sections, and positive cohomology vanishes by the P1 cohomology calculation and Kunneth. Assumptions (A),(B) hold.

For F, each O(-2) factor has H0=0 and H1 of dimension 1; each O(0) factor has H0 of dimension 1 and H1=0. Hence the only nonzero cohomology of F is H2 of dimension 1. In particular the constructed finite model has

    H0(V•)=0, H1(V•)=0, H2(V•)=k.

This correctly retains degree-two freedom; it does not accidentally contract the entire scalar complex.

All subsets use distinct COMMON vertices. Distinct vertices with equal carrier, standard, or mask labels remain distinct. Their equal divisor factors contribute their full multiplicities to the product denominator. There is no transfer of one occurrence's charge to another.

## 3. Explicit bases and matrices

For a tuple I let m_I=n+sum_(v in I)deg(d_v). A basis of its numerator space consists of

    product_i X_i^(a_i) Y_i^(m_(I,i)-a_i), 0<=a_i<=m_(I,i).

Attach the tuple I and its complete denominator-owner list to every basis vector. Dq is a signed multiplication matrix for the known section d_v on the relevant monomial spaces. A coefficient of d_v shifts a monomial exponent and contributes its exact scalar coefficient. Multiplication lands in the full target multidegree space, so no cutoff discards terms. D1 D0=0 follows by pairwise cancellation of the two orders of multiplication, including signs.

If physical geometry is represented symbolically, these are symbolic exact coefficient matrices. Their geometry and detector rows are not numerically evaluated in this note. Bases can be represented by bounded exponent predicates instead of materializing their columns.

## 4. Inclusion and detector domain

The authenticated scalar solution has per-actual-edge-owner carrier<=14, legal<=1, standard-boundary<=5250. Therefore multiplying any demanded s_I by product_(v in I)d_v clears every pole. Normality of X extends the resulting rational section globally, placing it in the full numerator space V1. Its actual coboundary lies in V2 by the exact differential construction.

The full V1 is larger than the source solver's Laurent support box. No claim that all its monomials satisfy that smaller box is made. Instead its coefficients have precisely the denominator bound by construction. Complementary physical differentiation gives carrier<=15, legal<=2 and standard-boundary<=5251. Multiplying by the actual current, of carrier<=9 and legal<=5, puts E(V1) in carrier<=24, legal<=7, standard-boundary<=5251. These are below the authenticated residual's 32/18/5251 bounds. The same calculation applies to A(V0).

The homogeneous numerator argument, rather than the solver box, supplies finite coefficient rows on this enlarged domain. For an E-input lift, inclusion and s successive End homotopies give carrier<=28+6s, legal<=9+3s, s=0,1,2,3. In particular they fit outer54/legal29, and there are at most 6 owners. Using the existing conservative outer54/29/5251 clearing rather than these sharper orders gives exactly the global homogeneous envelope in refined-tracefree-pole-domain.md section 6, including [-45684,73705]^4 after outer transport. Thus enlargement to full numerator spaces does not require assuming the smaller scalar Laurent box.

This establishes that the authenticated formula for e=E^*Phi has finite exactly regularized rows on V1. The following additional chain argument, not the envelope alone, proves the required boundary annihilation.

### 4.1 Bounded total primitive and exact kernel annihilation

Let A=A_p(f), f in V0, and R=delta A. If the detector includes trace-free projection, apply it to A as well; this linear projection commutes with delta and does not change the bounds. Form the authenticated closed lift J=J0+J1+J2+J3 of R. Its bidegrees are (2+s,-s), and d_End J_s=(-1)^(s+1) delta J_(s-1) for s>=1. The pinned End complex has degrees -3,...,3, cohomology only in degree0, and the stated local homotopy contracts its augmentation-zero part.

Construct K_s in bidegree (1+s,-s) by

    K0=jA,
    T_s=J_s-delta K_s,
    K_(s+1)=(-1)^s H_(-s)(T_s), s=0,1,2.

At s=0, T0 has zero augmentation, since J0=j(delta A) and augmentation commutes with delta. It is internally closed. Thus d_End K1=T0. Inductively T_s is internally closed: d_End J_s=(-1)^(s+1)delta J_(s-1), while the preceding recursion gives d_End delta K_s=(-1)^(s-1)delta J_(s-1), the same sign. At negative internal degrees, exactness and the contraction identity give

    d_End K_(s+1)=(-1)^s T_s.

The corresponding total differential contribution is (-1)^(s+2)d_End K_(s+1)=T_s. Finally T3 is internally closed in the bottom degree -3. Its internal cohomology vanishes and there is no degree -4, so T3=0. Therefore

    D(K0+K1+K2+K3)=J.

This is an actual regular primitive construction. No extra End homotopy beyond K3 is required. The maximum bounds at stage s are carrier28+6s, legal9+3s and standard-boundary5251: both J_s and delta K_s satisfy the same stage bound, subtraction takes their maximum rather than adding pole orders, and H adds6/3. For s<=3 these are at most46/18/5251, strictly within the fixed outer54/29 comparison. The tuple has at most5 vertices for K; no owner is introduced without retaining it and its outer weight. Fixed standard tags make their coordinate divisors units under the same projection r.

Consequently the exact outer comparison sends J to a total boundary, since it is defined and commutes with D on this bounded primitive K. The full authenticated tensor dual cocycle annihilates total boundaries; its evaluation on J agrees with the three terminal rows because J has no internal-degree-positive components. The restricted three-row formula is not asserted to annihilate arbitrary total boundaries outside that subspace. Hence Phi(delta A)=0 for every f in V0. The previously checked chain identity E(delta f)=-delta A_p(f) now proves

    D0^t e=0 on the entire constructed V0,
    e annihilates ker D1=im D0.

This is a formal identity proof on the full finite domain; it does not evaluate any detector coefficient or physical source polynomial.

## 5. Concrete sufficient certificate for the direct solve

The finite-domain certificate and subsequent implementation obligations are now explicit:

1. A section/owner table for d_v and its multidegree, certifying the existing cover and factorization.
2. The full monomial-space predicates above, and exact signed multiplication maps D0,D1. Their symbolic relation D1 D0=0 and the theorem above certify ker D1=im D0.
3. Exactly regularized rows e_j=Phi(E(b_j)) for the V1 basis, retaining all physical frame, prefix-owner and partition data.
4. The formal identity D0^t e=0 proved in section 4.1, with no projected or dropped rows; a concrete compiler may also check its exact matrix residual.
5. A pivot selection and exact residual D1^t eta=e, as in direct-dual-scalar-fill-contract.md section 4.

Item 4 is NECESSARY AND SUFFICIENT for kernel annihilation in this model, because ker D1=im D0. Section 4.1 proves it by a comparison-compatible chain homotopy for every A(V0) element. It can alternatively be checked directly by exact symbolic identities. Neither proof is replaced by H1 alone. Conversely, one nonzero entry of D0^t e is a precise obstruction to any direct filling on this chosen domain.

After item 4, exact rational row reduction yields eta. D0 is injective here because H0(F)=0, so its columns are already a basis of ker D1; no separate nullspace computation is required. Dimensions and a structural rank check are

    rank D0=dim V0,
    rank D1=dim V1-dim V0.

This is a concrete sufficient finite-domain certificate and construction, but not an evaluated physical row-space solve. It eliminates the missing finite-H1 and primitive-domain assumptions at proof level; it does not materialize or price the coefficient matrices.

## 6. Checked small example and truncation obstruction

The accompanying test uses X=P1xP1, F=O(-2,-2), and four standard product charts with sections d_(a,b)=Z_a^2 W_b^2. All numerator terms are acyclic. Exact rational matrices have

    dimensions (4,54,100,49), ranks (4,50,49),
    cohomology dimensions (0,0,1,0).

The test checks D1D0=D2D1=0, degree-one exactness, retained H2, and dual kernel annihilation for e=D1^t eta.

A minimal modification demonstrates the truncation danger: delete just ONE basis vector from V0 while leaving V1,V2 intact. The modified domain still satisfies D1D0'=0 but H1 has dimension1. Let z be the omitted D0 column, and e=z using the standard coordinate pairing. The four D0 columns have disjoint monomial supports, so

    (D0')^t e=0, D1 z=0, e(z)=3.

Thus all retained gauge tests pass, yet no eta solves D1^t eta=e. This is an explicit one-column obstruction on a sheaf with H1=0. It illustrates precisely why clipping even an apparently harmless numerator degree/vertex coefficient invalidates an exactness argument.

Files: test_owned_denominator_complex.py and owned-denominator-test-results.json. The test uses only abstract small rational matrices and no physical source polynomials.

## Status

New checked lemma: the full owned-denominator numerator complex is finite, regular and H1-exact under the stated homogeneous cover assumptions, which match the authenticated ownership construction. New explicit truncation counterexample passes exact tests. The bounded primitive comparison also proves the detector compatibility identity at formula level. Still missing: instantiated coefficient matrices/rows, pivot or factored inverse, exact direct-fill residual for the chosen implementation, and a product/byte schedule. No physical source evaluation was performed.

## Dependency scope

Companion references are identified by basename. A referenced file not supplied with this collection is an external prerequisite, not an embedded proof or a verified relative link. The reading order and unresolved conditions are listed in `proof-notes-index.md`. Reported test results describe the source audit; this proof copy does not by itself constitute a new test run.
