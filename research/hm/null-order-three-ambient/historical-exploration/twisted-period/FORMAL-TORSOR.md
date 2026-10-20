# Closing the matrix-algebra formal-coordinate torsor premise

## Statement and scope

Let X be a smooth complex holomorphic symplectic manifold of dimension 2p. Let C_h be an honest flat, h-adically complete sheaf of k[[h]]-algebras locally isomorphic to Mat_r(A_i), where A_i is a unital differential deformation quantization of O_(U_i) with first commutator hπ. Require overlap maps to be h-adically continuous and coefficientwise differential operators over the identity of X. Then C_h has a canonical formal-algebra-frame Harish–Chandra torsor for

    (g,F) = (Der_cont,k[[h]](Mat_r(D_p)), Aut_origin,k[[h]](Mat_r(D_p))).

Its Cartan form is transitive. Here origin means the ideal reducing modulo h to matrices whose coefficients vanish at the formal origin, NOT a chosen augmentation of the matrix algebra to k. The reductive quotient is PGL_r×Sp_(2p); the kernel is pro-unipotent. Consequently Baranovsky's relative Gelfand–Fuks map and universal class apply.

For the source X=C^4 with C an elliptic curve, p=2. Conditional on the twisted module whose exact descent yields C_h, these hypotheses hold provided the ambient μ,F are differential DQ data as stipulated. Multiplication by a formal matrix using a differential star product is coefficientwise differential, so conjugation by G preserves this category. This statement concerns the holomorphic setting; it need not assume a global algebra deforming O_X or a globally glued module over such an algebra.

## Construction and proof

### 1. Formal fibers

On each U_i use the local matrix presentation. Complete at x in the ideal whose reduction is Mat_r(m_x). The resulting algebra is Mat_r(completed A_(i,x)). Formal Darboux/formal symplectic quantization uniqueness gives an h-linear continuous algebra isomorphism

    completed A_(i,x) ≅ D_p.

Thus every formal fiber of C_h is Mat_r(D_p). This uses the full symplectic hypothesis. It does not follow from the derivation-extension lemma alone.

For full support, no module-normal-form argument remains: locally the given module is free A_i^r by assumption. Its right-action algebra is already the displayed matrix algebra. The coisotropic constraints and module-generator corrections in the general formal-model theorem are unnecessary here.

### 2. Horizontal jet algebra

Take formal Taylor jets of the local coefficient sheaves and of their multiplication maps. The local star product induces an O_X-linear multiplication on the jet bundle: coefficients of each bidifferential operator are replaced by their Taylor jets and derivatives act in the formal fiber variables. The jet bundle carries the Grothendieck flat connection ∇^G. Since jet prolongation commutes with composition and multiplication of differential operators, ∇^G is a derivation of this multiplication.

Every coefficientwise differential overlap isomorphism T_ij prolongs to a horizontal algebra isomorphism J(T_ij). Exact T_ij T_jk=T_ik gives an exact cocycle on jets. Hence the local jet algebras and their Grothendieck connections glue to a global flat jet algebra J(C_h).

This is why algebraic gluing alone, with completely arbitrary nonlocal maps, would not have sufficed. In our differential setting the needed extra structure follows from the hypotheses.

### 3. Algebra-frame torsor and Cartan form

Define P_C over X as the functor of continuous h-linear formal-algebra isomorphisms

    σ: Mat_r(D_p) → J(C_h)_x

preserving the origin ideal and inducing a symplectic isomorphism on the center of the classical formal algebra. It is a torsor under F by precomposition. Formal Darboux gives its local nonemptiness; equivalently construct it levelwise in the formal topology as a proalgebraic frame functor. This construction does not require a global section of P_C.

Pull back ∇^G to P_C and use the universal σ to trivialize J(C_h). In that trivialization the connection is d+θ, with θ valued in continuous h-linear algebra derivations g. Flatness gives

    dθ + (1/2)[θ,θ] = 0.

Changing frames gives the usual adjoint transformation rule, and on vertical tangent vectors θ is the Maurer–Cartan form (choose the conventional right-action sign consistently). Thus (P_C,θ) is a Harish–Chandra torsor. Horizontality of J(T_ij) means that the Cartan forms just constructed on the different local matrix presentations agree under their intrinsic frame identifications.

### 4. Transitivity, including the matrix directions

Let f=Lie(F). Reduction modulo h gives a derivation of Mat_r(k[[z_1,...,z_(2p)]])). Its induced derivation on the scalar center is a symplectic formal vector field. Evaluation at z=0 gives a linear map

    g → k^(2p).

Its kernel is f: preserving the origin ideal is precisely vanishing of this center-vector-field value; the inner matrix derivations automatically preserve the two-sided origin ideal. Constant Hamiltonian translations show that this map is onto. Therefore

    g/f ≅ k^(2p).

The frame torsor tangent sequence is

    0 → vertical TP_C → TP_C → π*TX → 0.

The Cartan form is an isomorphism on the vertical term onto f. On quotients its map π*TX→(g/f)⊗O_(P_C) is the ordinary formal-coordinate soldering map, up to the harmless consistent choice of sign: changing the base point differentiates the constant term in Taylor expansion. The classical coordinate frame makes this an isomorphism. The two exact sequences therefore imply θ:TP_C→g⊗O_(P_C) is an isomorphism. This proves transitivity.

Matrix/Azumaya directions add vertical PGL_r and higher inner directions, not extra base directions. Thus the classical fiber being a matrix algebra is not an obstruction to transitivity.

### 5. Reductive quotient needed for relative GF

On the residual matrix algebra at the origin an automorphism acts through PGL_r. On the tangent space of the classical center it acts through Sp_(2p). Constant conjugations and linear symplectic changes split these maps. Automorphisms trivial on both residual data have a pronilpotent formal-order filtration; its finite stages are unipotent in characteristic zero. Accordingly F has Levi factor PGL_r×Sp_(2p) and pro-unipotent kernel, exactly the reductive Lie subalgebra used for the universal matrix-Weyl class.

It follows that the relative GF construction is available, and

    [GF_(P_C)(τ)]_j = 0 for j>2p.

For p=2 this yields the degree-six and degree-eight necessary vanishings WITHOUT any remaining independent torsor premise, under the differential/symplectic/completeness assumptions of this statement. It still does not identify this class with any expression using the source b.

## Source pins and distinction from a transcription

Baranovsky, https://ems.press/content/serial-article-files/42628 :

* §4.1 Lemma 4.1, printed pp. 52–54: formal models; the scalar formal-Darboux/uniqueness part on pp. 52–53 is the input used in step 1.
* §4.2, printed p.55: the isomorphisms of endomorphism formal fibers form P_E; this is stated separately from the pair torsor. In the full-support case its null foliation is zero.
* §3.2, printed pp.43–46: definition of HC torsor, transitivity/foliation, and relative GF via reductive/pro-unipotent structure.
* §3.3 equation (6) and Lemma 3.5: local derivation extension and universal vanishing.

The proof above is an adaptation by intrinsic differential-jet descent. It explains why no global algebra/module PAIR is needed for the frame torsor once C_h is honest and differential. It is not a claim that the paper states an arbitrary-gerbe theorem verbatim.

For the local continuous derivation extension, the companion direct proof is [FORMAL-WEYL.md](../twisted-endomorphism/FORMAL-WEYL.md). For exact C_h gluing and its opposite convention, see [RESULT.md](../twisted-endomorphism/RESULT.md).

## Remaining boundary

This closes formal geometry, not the period comparison. The scalar central-curvature class of the original algebroid and its relation to the symbol E must still be identified in compatible conventions. The construction is conditional on the existence of the twisted module and does not produce one. No finite jet or retained-coordinate value has been evaluated.
