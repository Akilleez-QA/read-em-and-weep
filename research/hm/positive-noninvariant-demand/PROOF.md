# The non-invariant positive channel has a forced curried representation

## Result and interpretation

Work with the actual HM cohomology module and the previously proved canonical invariant-product theorem. No c-d-f occurrence or source classification is assumed. Write N₂=H¹(B(2))₊ and N₄=H¹(B(4))₊, the degree-three and degree-five positive pieces of the shifted module. The positive quadratic representation is Sym²V=1⊕D. Write q_+=q_inv+q_D for the invariant and non-invariant input components, extended by zero on the other summand. Then the image of the curried map

    C_D:V⊗N₂→V*⊗N₄

contains a G-subrepresentation isomorphic to

    1+2A+3V+3P+5D, dimension53.                 (1)

This is a universal lower bound on a curried representation, NOT the dimension of im(q_D)⊂N₄, and not an evaluated actual rank. In particular q_D is nonzero. Moreover q_D alone cannot admit a positive-linear factorization through the same actual middle K₄⁺ of dimension46, although q_+=q_inv+q_D does. Here positive-linear factorization means q_D(st⊗x)=b_s a_t(x) with both arrows passing through one and the same prescribed middle; it does not mean an ordinary linear factorization of D⊗N₂→N₄. Projection onto the non-invariant quadratic component need not preserve such a two-step factorization.

The proof uses the actual middle character and an already proved geometric invariant-product character. It supplies neither the actual q_D nor a source exclusion, and does not determine any c-d-f scalar/C² alternative.

## 1. Inputs and invariant normalization

The immediate inputs are:

- The canonical minimal-factor theorem and actual middle-character derivation in PR928, commit 1a8fb75aa886f9bb6c07e357759d37630cdd127d, research/hm/profile11-source127-cdf-positive-factorization/PROOF.md, Git blob 92e389cc07e7c2e61b64a04b17b91d0c1650c7dd. Its actual source conventions and original immutable inputs identify T₊=V and

      K₄⁺=1+4A+2V+3P+3D.

- The geometric theorem POSITIVE-INVARIANT-VERTEX-RANK-33-PROVED.md at commit eeb1a11799ca38a60c37f6ba96f263ef8e20dd1c, research/hm/order-four-quadratic-load/, blob019c1f31773476f0a4877d88632ce5d46fbd4b9f in Akilleez-QA/read-em-and-weep. It gives the canonical invariant positive product Q:N₂→N₄ with

      im Q≅2V+3P+3D.

  This is an imported universal geometric result, not a selected-instance calculation.

The invariant summand in Sym²V is one-dimensional. Choose a nonzero representative q₀ in that canonical line and normalize its equivariant projection ε:Sym²V→C by ε(q₀)=1. Set Q(x)=q_+(q₀⊗x), so

    q_inv(s⊗x)=ε(s)Q(x),    q_D=q_+-q_inv.

The definition of q_inv is independent of the reciprocal rescaling of q₀ and ε. It is the intrinsic isotypic projection, not a choice of actual coordinates or coefficients. Because V is irreducible and self-dual of odd dimension, ε is a nondegenerate invariant symmetric bilinear form on V. Thus its associated map ε♯:V→V* is an isomorphism.

## 2. A universal image-sum inequality

For equivariant linear maps f,g:X→Y, let h=f+g. Then

    im f⊆im h+im g.

The sum is a quotient of im h⊕im g. Semisimplicity implies, for every irreducible ρ,

    m_ρ(im f)≤m_ρ(im h)+m_ρ(im g).             (2)

This holds without a relation between the two image subspaces and without claiming their sum is direct. In particular if im h is a subrepresentation of a prescribed module P, then

    m_ρ(im g)≥m_ρ(im f)-m_ρ(P).                (3)

Positive differences in (3) give a genuine subrepresentation of im g. This is an existence of a subrepresentation, not a canonical embedded complement.

## 3. Apply the inequality to the two positive quadratic channels

Let C_+, C_inv, C_D be the curried maps V⊗N₂→V*⊗N₄. Currying is linear, so C_+=C_inv+C_D. Actual positive multiplication factors q_+ through K₄⁺. The minimal-factor theorem therefore says

    im C_+ embeds equivariantly in K₄⁺.       (4)

On the other hand, C_inv=ε♯⊗Q. Hence

    im C_inv≅V*⊗im Q
               ≅V⊗(2V+3P+3D)
               =2+6A+5V+6P+8D.              (5)

The last identity uses the fixed character identities

    V⊗V=1+V+D,
    V⊗P=A+P+D,
    V⊗D=A+V+P+D.

The representation in (5) has dimension99. Apply (3) using f=C_inv, g=C_D and h=C_+. Subtracting the upper bound in (4) gives

    (2+6A+5V+6P+8D)−(1+4A+2V+3P+3D)
       =1+2A+3V+3P+5D.

Every coefficient is positive, so (2) forces all the multiplicities in (1), proving the theorem.

For exact sign bookkeeping, C_inv=C_+−C_D; thus im C_inv⊆im C_++im C_D, which is the only inclusion used. There is no claim that either image is contained in the other or that their overlap is canonical.

Since dim im C_D≥53>46, the minimal-factor theorem also rules out a standalone factorization of q_D through K₄⁺. Since dim im C_inv=99>46, the invariant component alone cannot factor there either. Their actual sum does factor there. Thus the two components must combine in a way invisible to their separate factorization problems.

## 4. Contribution and limitations

The invariant-only aggregate extension is now rigorously impossible on the actual middle module, despite its innocuous aggregate appearance. This result is global for the actual HM module: its proof uses no c-d-f negative-pencil decomposition, idempotent alternative or selected source parameter. A substantial non-invariant channel is forced by the fixed cohomology characters and actual positive factorization, without recovering any coefficient.

The bound concerns an image in Hom(V,N₄), not the 37-dimensional target N₄. It is not a statement that a single non-invariant quadratic has image dimension53, nor that im(q_D) has that dimension. No actual instance matrix, point, parameter or rank is evaluated.

The theorem does not determine the relative positions of these curried images, the sharpness of53, the remaining aggregate algebra, marked mixed squares, the full module, or actual-HM membership. No source-dual pair, stable label or frontier count changes.
