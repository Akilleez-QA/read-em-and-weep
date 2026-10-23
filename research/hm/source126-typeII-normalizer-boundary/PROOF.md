# The known HM normalizer supplies no extra symmetry of the fixed octic gate

## Exact result and boundary

Let N5 be the authenticated Heisenberg normalizer acting on the actual Horrocks–Mumford bundle, and let Nbar be its image in PGL5. Let G≅SL2(F5) be the existing binary icosahedral complement, with the fixed positive plane and negative line L. Let Q0 be the invariant rank-three quadric used by the fixed source126 pencil, and let A be its negative quadratic parameter space.

Then the exact projective stabilizers satisfy

       Stab_Nbar(L)=Stab_Nbar([Q0])=G.                 (1)

Consequently the stabilizer in Nbar of the pair consisting of [Q0] and the fixed negative pencil is also G. The canonical octic line is G-fixed, so the known actual Heisenberg normalizer supplies NO additional nontrivial character capable of forcing its scalar to vanish.

This is an exact obstruction to this particular symmetry route, not a proof that every actual HM automorphism lies in Nbar. The actual full projective HM stabilizer is known to be finite, but the retained inputs do not classify it. An additional same-bundle, same-pencil automorphism outside Nbar would require a new authenticated theorem and its actual endpoint action. No actual HM coefficient, parameter or instance rank is evaluated here.

## 1. Authenticated actual geometry, not universal substitute symmetries

INPUTS.json pins six public repository inputs. Five are at db51525015bb7c5e825833d550d08dedf6f6ea96, under research/hm/order-four-quadratic-load/:

- ACTUAL-THETA-KERNEL-INTERPOLATION.md §1: actual HM action of H5 and N5; projective H5/center has order25.
- INVERSION-EVEN-QUADRICS-ARE-ADJOINT-BAD.md §7: the25 Heisenberg translates of the negative line are distinct actual HM lines, with distinct conjugate inversions and even-quadric subsystems.
- INVARIANT-CONE-DEGREE-SEVEN-DEFECT-IS-VERTEX-SUPPORTED.md §1: ambient representation V⊕W, of dimensions3 and2; the invariant Q0 has rank3 and vertex L=P(W).
- NORMAL-QUADRATIC-NONZERO-BY-SERRE-RESIDUE-DOUBLE-COVER.md §§4–6: the order-four block scaling preserves the cone restriction but does NOT preserve the ambient HM bundle isomorphism class.
- EXACT-AMBIENT-ADJOINT-DEFORMATIONS.md §1: finiteness of the full projective HM stabilizer, explicitly without identifying it with Nbar.

The sixth input is PR995 at f9435fa37c78e86391fd1a773a039dd646a05e53, research/hm/source126-typeII-internal-octic-gate/PROOF.md, for the canonical invariant octic line and the exact unresolved scalar boundary.

The embedded-complement premise is also checked directly in the primary source: Aure–Decker–Hulek–Popescu–Ranestad, Syzygies of Abelian and Bielliptic Surfaces in P4, arXiv:alg-geom/9606013v2, §1, printed pp4–6 (PDF pages3–5), https://arxiv.org/pdf/alg-geom/9606013v2 . It presents H5 of order125 with scalar center μ5 and the actual embedding N5=H5⋊SL2(F5) in SL5, of order15000, and identifies inversion eigenspaces and the induced icosahedral actions. Thus the complement is an actual subgroup, not merely an abstract quotient. Only this finite-group/action structure is imported from that source.

A targeted search of source126 and generic-beta Markdown inputs found the separate ingredients above, but no previous exact equality(1) or full-normalizer exclusion for the octic character route. The older nonisomorphism of the order-four scaling is retained, not claimed as new.

## 2. Exact stabilizer of the chosen negative line

The scalar subgroup in N5 is μ5, so |Nbar|=15000/5=3000. The embedded complement G has order120 and injects into PGL5: its nontrivial central involution acts as +1 on V and -1 on W, hence is not a scalar; its intersection with μ5 is trivial.

Every g∈G preserves L, so G⊂Stab_Nbar(L). The Heisenberg translates of L are25 distinct lines by the pinned actual geometry. Therefore the Nbar orbit of L has at least25 members. Orbit–stabilizer and the inclusion of G give

       |Nbar·L|=3000/|Stab_Nbar(L)|≤3000/120=25.

Both inequalities are equalities. Thus |Stab_Nbar(L)|=120 and the inclusion of G is equality. This proof does not assume in advance that the Heisenberg orbit is the whole normalizer orbit.

There is an equivalent group certificate. Modulo scalar center, write Nbar=F5²⋊SL2(F5), with multiplication(v,g)(w,h)=(v+gw,gh). Inversion is i=(0,-I), and

       (v,g)i(v,g)^(-1)=(2v,-I).                      (2)

As multiplication by2 is injective on F5², the25 translates give25 distinct involutions, and the centralizer of i is exactly the zero-translation complement. This explains why importing a Heisenberg translation as a same-inversion symmetry is invalid. The geometric proof above additionally identifies the relevant actual fixed line, without confusing group conjugacy with an unproved bundle statement.

## 3. Stabilizing Q0 adds no element

A projective automorphism preserving a quadric hypersurface preserves its singular locus. The singular locus of the rank-three Q0 is exactly L. Hence

       Stab_Nbar([Q0]) ⊂ Stab_Nbar(L)=G.

Conversely Q0 is G-invariant in the fixed actual normalization. Thus G is contained in the left side and equality follows. Requiring the equation Q0 itself to be fixed rather than its projective class can only reduce a stabilizer; it cannot add a symmetry outside G. In the given G-linearization the invariant equation is already fixed.

The fixed negative quadratic pencil is a G-subrepresentation A=Sym²W, and Q0 is its invariant base member. Therefore all of G preserves the pair, while every normalizer element preserving the pair already preserves [Q0]. Its pair stabilizer is exactly G as claimed.

This conclusion does not assume that the entire Heisenberg normalizer preserves the chosen inversion plane or Q0. It proves precisely that it does not: all remaining projective normalizer elements leave the Q0 stabilizer.

## 4. Consequence for the octic line and the tempting block scaling

PR995 constructs the canonical octic generator as a G-equivariant bundle map D O(-8)→E. Consequently its line in the Hom representation is pointwise G-fixed. No element of the group in(1) acts on that line by a new nontrivial character. Rechoosing scalar linearizations of a projectively identical action is not an additional geometric automorphism and cannot create a new naturality constraint on the same fixed symbol.

A separate tempting candidate is block scaling φμ, equal to the identity on V and multiplication by μ on W, with μ²=-1. The retained actual theorem proves that it changes the nonzero ambient monad ratio r to μ^(-2)r=-r. Scalar source gauges preserve r. The proof upgrades this to nonisomorphism even after forgetting G-equivariance, using simplicity and the perfectness of G. Thus φμ preserves a cone bundle restriction but exchanges TWO DISTINCT actual ambient bundles/formal extensions. It is not an automorphism of the same actual HM pencil. Its sign cannot be inserted into same-object naturality.

Moreover its parameter action on A is multiplication by -1, whose degree-eight contribution alone is (-1)^8=+1. Even before the ambient-bundle obstruction, a negative sign on the octic line would need an authenticated endpoint/marking action; it does not follow from the even plane degree. No such endpoint action is asserted here.

## 5. What would be needed to reopen this route

The full projective stabilizer Aut_proj(F) is finite by the pinned adjoint-deformation theorem. Finiteness does NOT imply Aut_proj(F)=Nbar, nor that its Q0 stabilizer equals G. This packet intentionally makes neither claim.

A new exclusion via an outside symmetry must supply all of:

1. an actual ambient bundle isomorphism s*F≅F;
2. preservation of the same Q0 and negative pencil, not only another cone restriction or translated inversion;
3. compatible action on the actual cohomology identifications defining the internal symbol;
4. a nontrivial action on the canonical octic line after these endpoint and parameter actions are combined.

Known Nbar candidates cannot satisfy item4 by(1); order-four block scaling fails item1. No actual scalar is evaluated or forced to vanish, no source or pair is removed, and no ninth or higher internal gate is computed.

## Reproduction

verify.py authenticates the six repository inputs and checks the entire finite group calculation over F5: SL2 order120 and perfectness, the affine semidirect product order3000, the25-element inversion conjugacy orbit, its120-element centralizer, and the exact origin stabilizer. It also checks the orbit–stabilizer bounds, universal rank-three singular-locus equation, and the symbolic block-scaling ratio/parity identities. The actual HM action and25-line geometry are imported authenticated theorems, not substituted numerical examples. These checks supplement the proof and do not evaluate any actual HM data.
