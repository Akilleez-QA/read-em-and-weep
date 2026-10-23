# A canonical saturated primary summand of the actual negative kernel bundle

Work over C with the actual HM module and the fixed physical G=SL2(F5) action. Let W be the negative coordinate two-space, P the positive four-space, W' the other negative doublet, and T6=Sym5 W. All bundles are on the original negative parameter line T=P(W*), with the same fixed determinant convention for every pencil. The actual kernel bundle E has rank17 and degree−54.

## 1. Exact inputs and new construction

Two full immutable originals suffice:

- PR1122 at 65c13bb9a3748a19eb8466f748bd29a5a849ecb5, research/hm/primary-terminal-source2-exclusion/PROOF.md. Its Section2 is independent of the later source2 hypothesis: the actual primary coefficient inclusions are

      A4=P tensor (1+A) subset M4=H1(B(4))_+,
      A5=P tensor W subset M5=H1(B(5))_-,

  where A=Sym2 W, and actual negative multiplication gives the everywhere exact subpencil

      0 -> A5 O(-2) -> A4 O(-1) -> A5 O -> 0.       (1)

  Both coefficient inclusions are injective. Their characters are A4=V+2P+D and A5=W'+T6, dimensions16 and8. This uses the actual primary module injection, physical parity and global levelness, not the source2 first-block splitting. No source2 assumption is imported here.
- PR1056 at 875e86e2eec36a050e9a626735199681762e43ec, research/hm/restriction-socle-kernel/PROOF.md. It supplies the actual original pencil 0->E->M3 O(-1)->M4 O->0, H0(E(1))=0, actual M4=H1(E), M5=H1(E(1)), and the parameter-multiplication identification with its fixed determinant rotation. The characters are M4=2V+4P+3D and M5=W'+3T6. These facts are independent of its conditional source-pair table.

The new theorem constructs a CANONICAL saturated equivariant subbundle

    E_prim subset E,        E_prim ≅ A5 O(-3),       (2)

from the actual primary coefficient inclusions, and the canonical quotient

    E_bar=E/E_prim,       rank E_bar=9, deg E_bar=−30.

The quotient has the actual everywhere exact terminal pencil

    0 -> E_bar(1) -> (M4/A4) O(-1)
      -> (M5/A5) O -> 0,                           (3)

with source character V+2P+2D (dimension21) and target character2T6 (dimension12). Moreover

    0 -> E_prim -> E -> E_bar -> 0                  (4)

splits as equivariant vector bundles. Its equivariant splittings form a nonempty affine space under a two-dimensional vector space. Thus the subbundle and quotient are canonical, but (4) does not specify a distinguished complement. Neither the splitting nor any complement is asserted horizontal for the original ambient Gauss inclusion, compatible with positive-coordinate/Q multiplication, or a splitting of the full graded adjoint primary extension.

## 2. Recover the same actual ambient terminal pencil

For any bundle F with H0(F)=H0(F(1))=0, the diagonal resolution produces naturally

    0 -> F(1) -> H1(F) O(-1) -> H1(F(1)) O -> 0.

Use F=E. For the original pencil u m_x+v m_y, PR1056 identifies multiplication by u on cohomology with m_y and multiplication by v with−m_x. The diagonal equation gives v H1(mult_u)−u H1(mult_v), equal to v m_y+u m_x. Thus the ambient terminal pencil is

    0 -> E(1) -> M4 O(-1) -> M5 O -> 0,             (5)

in precisely the same actual negative parameters as (1). No independent parameter rotation or arbitrary isomorphism of pencils is used. Both (1) and (5) are exact at every parameter, not only generically.

## 3. Both coefficient injections force saturation

The actual primary inclusions and module-linearity give a commutative diagram from (1) to (5). Their right and middle vertical maps are constant-bundle injections. The induced kernel map A5 O(-2)->E(1) is therefore injective. Define E_prim to be its image after twisting by−1. This is the actual image selected by the primary submodule; no representation complement has been chosen.

It remains to prove its quotient locally free. An injection of bundles alone would not prove this. Because both coefficient vertical maps are subbundle inclusions, their cokernels are the constant bundles (M4/A4) O(-1) and (M5/A5) O. The induced arrow between these cokernels is onto: every local section of M5 lifts locally through the surjection (5), and passage to the quotients preserves this surjectivity. The snake lemma gives

    0 -> E(1)/(A5 O(-2)) -> (M4/A4) O(-1)
      -> (M5/A5) O -> 0.

The kernel of an onto vector-bundle map is locally free. Hence E_prim is saturated in E and the quotient is E_bar(1), proving (2)–(3) as actual bundles and arrows.

Character subtraction is now legitimate because it follows the actual coefficient injections:

    [M4/A4]=V+2P+2D,       [M5/A5]=2T6.

Rank and degree in (3) are9 and−21, so E_bar itself has rank9 and degree−30. They also equal17−8 and−54−(−24).

## 4. The quotient vanishings and actual cohomology identifications

Sequence (3) embeds E_bar(1) in21O(-1), so H0(E_bar(1))=0. In particular all ordinary Birkhoff degrees of E_bar are at most−2. This bound follows from the ACTUAL quotient pencil, not merely from E's slopes: quotients of negative bundles need not retain the same slope bound.

Taking cohomology in (3) gives a natural isomorphism

    H1(E_bar(1)) ≅ M5/A5 = 2T6.                    (6)

Twisting (3) by−1 and using the acyclicity of O(-1) gives, in the same fixed determinant convention,

    H1(E_bar) ≅ M4/A4.                             (7)

The corresponding primary identifications H1(E_prim)=A4 and H1(E_prim(1))=A5 come from the same operations on (1). Naturality makes the induced maps on cohomology exactly the original actual coefficient inclusions and quotients. Thus (3) is not a new model chosen only to have matching dimensions or characters.

## 5. Splitting exists, and its equivariant ambiguity is exactly two

Set R=A5=W'+T6, so E_prim=R O(-3). Then

    Ext1(E_bar,E_prim)
      = R tensor H1(E_bar* O(-3)).                 (8)

Serre duality on the parameter line, with its fixed determinant trivialization, identifies H1(E_bar* O(-3))* with H0(E_bar(1)). The latter is zero by Section4. Hence (8)=0, so (4) splits as ordinary vector bundles. Averaging any section of E->E_bar over the finite group G yields an equivariant section without changing its right-inverse property.

The differences between equivariant sections are precisely

    Hom_G(E_bar,E_prim)
      = (R tensor H0(E_bar* O(-3)))^G
      = Hom_G(H1(E_bar(1)), R),                    (9)

where the last identification is again Serre duality and is compatible with the fixed G linearizations. By (6), the right-hand side is Hom_G(2T6,W'+T6), which has dimension2 by irreducibility, nonisomorphism and Schur's lemma. Therefore the set of equivariant sections is a nonempty affine space of dimension2, not a vector space with a preferred zero.

This proves nonuniqueness of the complement even after imposing equivariance. It does not deny that additional unrelated structure might distinguish one; it proves that the exact sequence and equivariance alone do not specify a unique section.

## 6. Contribution and limits

The primary terminal image now supplies an actual canonical rank-eight degree−24 subbundle, not only a bound on the degree−3 slope multiplicity. The canonical residual quotient and its21→12 negative terminal pencil are determined simultaneously, and the precise two-dimensional equivariant complement ambiguity is computed without selecting an actual coefficient.

The proof never identifies this canonical primary summand with a named source2 or Gauss block by character. It neither selects an ordinary complement nor claims its preservation by the original ambient Gauss connection, positive multiplication, or invariant Q. In particular it does not split the full graded adjoint-primary extension, whose nonsplitting is a different statement. No rank-three coverage theorem, source occurrence, original obstruction value, full-adjoint invertibility, or algebraicity conclusion is inferred.

All computations are structural sheaf/cohomology and fixed representation arguments. No selected actual HM/source coefficient, tensor, matrix, point, parameter, derivative, jet, actual-instance rank or scan is evaluated.
