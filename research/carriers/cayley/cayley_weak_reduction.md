# Genuine Cayley mixed Atiyah tests: reductions

Work over C. Let X=(P1)^4, H=sum h_i, and g:X→Q=Q5 be the explicit seven-section map in `rank7_construction.md`. Let C be any normalized Cayley bundle on Q, S the normalized rank-four spinor bundle, and F=g*C. Thus c1(C)=−H, c2(C)=H², S*=S(1). No SO7-equivariance of a fixed C is assumed.

## 1. Monad and Bott groups

Ottaviani's original construction gives C as cohomology of

    O_Q(−1) → S → O_Q.

Equivalently, set K=ker(S→O). There are exact sequences

    0→O(−1)→K→C→0,
    0→K→S→O→0.

The choice of C is a nonisotropic spinor, a point of P7\Q6. A fixed C is G2-homogeneous. Source: G. Ottaviani, On Cayley bundles on the five-dimensional quadric, Boll. UMI 4-A (1990), 87–100, especially pp. 88, 93–94; https://people.dimai.unifi.it/ottaviani/pubblic/cayleybundle.pdf.

For G2/P1, with alpha1 short and fundamental weights omega1,omega2, End_0 C(t) has Levi-highest weight (t−3)omega1+2omega2. Add rho=(1,1), and use s1(a,b)=(−a,b+a), s2(a,b)=(a+3b,−b). Bott gives:

- End C: h0=1,h1=7; other groups zero.
- End C(−1): acyclic.
- End C(−2): h2=1 only.
- End C(−3): h3=1 only.
- End C(−4): acyclic.
- End C(−5): h4=7,h5=1.

The scalar summand is included in this list. The reflection calculations give the displayed groups.

Let alpha_C in H²(Q,End C(−2)) be the actual conormal–Atiyah obstruction for Q⊂P6. It is nonzero. Indeed, if zero, At(C) lifts to H¹(End C⊗Omega_P6|Q). Tensoring the ambient Euler sequence and using End C(−1) acyclic and H0 End C=C shows this lift must be scalar. Then At(C)=−(1/2)Id H by trace. This would give ch2(C)=H²/4 instead of −H²/2. Therefore alpha_C generates the one-dimensional group.

## 2. Every pair is a genuine partial Segre obstruction

Write A_i(F) for the factor-i component of the Atiyah class and u_i=c1 O_X(e_i), understood in H¹(O_X(−2e_i)). The six classes required by the product-elliptic weak test are

    Delta_ij=A_i(F) cup u_j − u_i cup A_j(F)
       in H²(X,End F(−2e_i−2e_j)).

Each is, up to the single global convention sign, the exact obstruction to extending F to the first neighborhood of the partial Segre embedding

    X ⊂ Z_ij=P3_(ij) × P1_k × P1_l.

This follows from the two-factor tensor-Euler conormal sequence, pulled over the other factors. It does not require any full four-factor conormal equivalence.

The seven defining sections extend to a morphism from a neighborhood of X in Z_ij to P6. With z00,z01,z10,z11 the P3 coordinates replacing factors 1,2, direct polynomial expansion gives

    q0(g_tilde)=−[34]² (z00 z11−z01 z10),
    [kl]=a_k b_l−b_k a_l.

By S4-invariance of q0, the analogous identity holds for every pair. Naturality of the conormal–Atiyah obstruction therefore proves the equality up to the fixed overall sign

    Delta_ij = ± [kl]² · g*alpha_C.

This statement uses only equivariance of the explicit quadratic equation, not equivariance of C. It is a reduction to actual cohomology multiplication maps, not just a Chern-character test.

The full Segre conormal has rank 11, with pair/triple/quadruple pieces. One must not infer full first-neighborhood extendability from six pairwise vanishing classes without a separate argument.

## 3. Exact resolution of g_*O_X

The quotient calculation in `image_geometry.md` establishes Y=X/V4, where Y is the normal cubic section (q0,k) of Q. Hence g_*O_X decomposes into invariant O_Y and three nontrivial character summands M_chi.

For the partition 12|34 set

    P=(a1a2,a1b2+b1a2,b1b2),
    R=(a3a4,a3b4+b3a4,b3b4).

The corresponding matrix is

    D_U = [[2A,B,U],[B,2(V+W),D],[U,D,2E]] = P R^t + R P^t.

Its determinant is −2k−2Uq0. The three components of P cross R are a basis of the appropriate degree-one nontrivial V4-character space and satisfy D_U(P cross R)=0. Thus there is a nonzero map coker(D_U)→M_chi. The cokernel is a rank-one Cohen–Macaulay O_Y-module, so the generically injective map has no torsion kernel. Both sheaves have identical Hilbert polynomial

    ((n+1)^4−(n+1)^2)/4.

Consequently their quotient has zero Hilbert polynomial and is zero. This proves

    0→O_Q(−2)^3→O_Q(−1)^3→M_chi→0.

Use D_V,D_W for the other two characters. With the cubic resolution of O_Y, this gives the exact sequence

    0→O_Q(−3) ⊕ O_Q(−2)^9
      →O_Q ⊕ O_Q(−1)^9 →g_*O_X→0.

Tensoring by End C and its twists, the Bott table yields actual cohomology:

    h*(End F)=(1,16,1,0,0),
    h*(End F(−H))=(0,0,18,0,0),
    h*(End F(−2H))=(0,0,1,16,1).

The nonzero alpha_C restricts injectively to Y because H²,H³(End C(−5))=0; quotient averaging then shows g*alpha_C is nonzero. It spans the entire H²(End F(−2H)).

Thus each mixed test is a single map from a known one-dimensional space:

    C·g*alpha_C --[kl]^2--> H²(End F(−2e_i−2e_j)).

The nonzero source does not by itself prove a nonzero image.

## 4. Exact ACM resolution for the pair twist

Let L_12=O_X(−1,−1,0,0) and M_12=g_*L_12. All H¹,H²,H³(X,L_12(nH)) vanish by Kunneth. The sheaf is locally Cohen–Macaulay of codimension one on smooth Q, hence any free presentation has vector-bundle kernel. Its Hilbert function for n≥1 is n²(n+1)², while h0=0 for n≤0. Over denominator (1−t)^6 its numerator is

    4t+12t²−12t³−4t⁴.

As a sheaf on P6, M_12 is 3-regular: the only possibly relevant top group is H4(L_12(−H))=0. Therefore its section module is generated in degrees at most 3. Exact integer multiplication matrices built directly from the seven sections have full ranks modulo 32003:

- degree 1→2: size 36×28, rank 28;
- degree 2→3: size 144×252, rank 144.

Full modular rank proves the corresponding full characteristic-zero rank. Hence minimal generators are four in degree 1 and eight in degree 2, with none in degree 3. See `pair_module_generation.py` and `.txt`.

The kernel of O(−1)^4⊕O(−2)^8→M_12 is an ACM bundle on Q. The classification of ACM bundles on a smooth quadric as sums of line and spinor bundles, together with its Hilbert numerator 20t³+4t⁴, uniquely gives O(−3)^4⊕S(−2)^2. Therefore

    0→O_Q(−3)^4 ⊕ S(−2)^2
      →O_Q(−1)^4 ⊕ O_Q(−2)^8 →M_12→0.

The same holds for every pair by permutation symmetry of the seven-section subspace (this is independent of C). For the ACM classification, see Knorrer; a precise modern theorem statement is Theorem 2.1 in https://msp.org/ant/2015/9-4/ant-v9-n4-p08-s.pdf. Spinor conventions there are shifted by one relative to S here.

Tensoring by End C gives the precise remaining cohomology kernel

    H¹(X,End F(−e_i−e_j))
      = ker[H²(Q,End C⊗S(−2))^2 → C^8].

If H²(End C⊗S(−2))=0, then every individual Delta_ij is nonzero: vanishing Delta_ij would lift the relative Atiyah class through the partial Segre conormal sequence; its relative ambient Euler sequence and this H¹-vanishing would force the relative Atiyah class to equal phi(h_i+h_j) for a global phi in H0 End F=C. The trace fixes phi=−Id/2, contradicting the nonzero centered c2 on a pair fiber P1×P1.

## 5. The remaining scalar is nonzero: exact invariant CE calculation

The cohomology in question is completely acyclic:

    H*(Q,End C⊗S(−2))=0.

Here is a finite exact proof. The scalar summand S(−2) is acyclic by the spinor ACM property. Set A=End_0 C. From the Cayley filtration,

    A⊗C(−2) = Sym³ C(−1) ⊕ C(−2)

is acyclic. (Using End instead of A gives two copies of C(−2).) The C term is acyclic by Ottaviani's theorem; Sym³ C(−1) has shifted G2 weight (−6,4), reflecting to (6,−2) and then (0,2), hence singular. The two exact filtration sequences consequently show that the only possible cohomology of A⊗S(−2) is the kernel and cokernel of

    H²(A(−2))=C → H³(A(−3))=C.

Both are trivial G2-representations. Thus computing the G2-invariant cohomology suffices to decide all cohomology.

Take the parabolic with Levi SL2 times Gm and negative nilradical n with basis x,y,z,u,v, brackets

    [x,y]=z, [x,z]=u, [y,z]=v,

and all other brackets zero. Their central weights are (−1,−1,−2,−3,−3), and their SL2 weights are (1,−1,0,1,−1). This is the negative part of the standard (2,3,5) grading of g2.

The spinor fiber has a basis s0,a,b,c, with central weights (0,−1,−1,−2) and SL2 weights (0,1,−1,0). Its nilradical action can be normalized to

    x s0=a, y s0=b, x b=c, y a=−c, z s0=2c,

with all unlisted actions zero. The upper coefficient is nonzero because the quotient S→O has no global lift of 1: H0(S)=0. The symplectic O(−1)-valued pairing on S forces the lower coefficient to be nonzero as well; rescaling the basis gives the displayed formulas. The z coefficient then follows from [x,y]=z. This also verifies the full nilradical representation directly.

The fiber of A is the SL2 adjoint representation, central weight zero and trivial nilradical action. Write its standard Sym² basis as A0,B0,D0, of SL2 weights 2,0,−2. Twisting by O(−2) subtracts 4 from the central weight.

The G2-invariant part of homogeneous-bundle cohomology is computed by the Levi-invariant Chevalley–Eilenberg complex (V⊗Lambda* n*)^L. This follows from derived induction/Frobenius reciprocity and exactness of invariants for reductive G2 and L in characteristic zero. There are exactly two invariant cochains in degree 2, exactly two in degree 3, and none in any other degree.

Suppress stars on the dual forms x,y,z,u,v. In degree 2 one can take

    w1=A0 s0 xu+B0 s0(xv+yu)+D0 s0 yv,
    w2=−A0 b zu+B0 a zu−B0 b zv+D0 a zv.

In degree 3 take

    v1=−A0 b xyu+B0 a xyu−B0 b xyv+D0 a xyv,
    v2=A0 c xzu+B0 c(xzv+yzu)+D0 c yzv.

Using the module action above and d(z*)=−x*y*, d(u*)=−x*z*, d(v*)=−y*z* gives

    d(w1)=v1−2v2,
    d(w2)=−v1−v2.

Thus the differential matrix is

    [[1,−1],[−2,−1]], determinant −3.

It is invertible in characteristic zero. The invariant cohomology vanishes, and since all possible cohomology was already known to be trivial G2-representations, the entire cohomology vanishes. This computes the previously undetermined connecting scalar, rather than assuming that a spectral-sequence differential is nonzero. The calculation has been independently checked from the displayed cochain bases.

## 6. Completed individual-pair obstruction and weak-test failure

Combining section 5 with the pair resolution proves actual cohomology concentration

    h*(X,End F(−e_i−e_j))=(0,0,12,0,0)

for every pair i<j. In particular H¹ vanishes.

Suppose Delta_ij were zero. The partial Segre conormal sequence would lift the relative Atiyah class A_i(F)+A_j(F) to H¹(End F⊗Omega_P3|pair). The relative ambient Euler sequence

    0→End F⊗Omega_P3|pair
      →End F(−e_i−e_j)^4→End F→0

and H¹(End F(−e_i−e_j))=0 force this class to be phi(h_i+h_j), with phi in H0 End F=C. Tracing determines phi=−Id/2. On a pair fiber P1×P1 this would imply

    ch2(F|fiber)=1/4 (h_i+h_j)²=1/2 h_i h_j.

But the actual pullback Chern classes give

    ch2(F|fiber)=−1/2 (h_i+h_j)²=−h_i h_j.

This contradiction proves

    Delta_ij ≠ 0 for all six pairs i<j.

Equivalently all six maps [kl]² from the one-dimensional source in section 3 are nonzero on g*alpha_C. The proof applies to every Cayley bundle C over this explicit carrier g. It needs neither stability of F nor a square root of O_X(H).

Under the product-elliptic double-cover reduction, these six classes lie in distinct deck-character eigenspaces, so their six evaluations are linearly independent. With the four diagonal polarized directions and the six compensated-Poisson directions already known to vanish in the weak-test setup, the HH² evaluation has kernel dimension 10, not the required 16. This last numerical conclusion uses precisely that previously established HH²/weak-test normalization; the six nonvanishing End-valued classes above are independent of that bookkeeping.

This excludes the entire Cayley parameter family for this explicit map g. It does not exclude every rank-seven Segre carrier. By upper semicontinuity, the same pairwise failure persists wherever the six H¹ vanishings and simplicity persist in a flat family.
