# The remaining defect twelve has only the lower-normal orientation

## Statement and retained boundary

Retain the complete actual-geometric hypotheses and conclusions of PR1214, hence the original rank-four maximal ordered profile (1,1), its source and section gates, and precisely the full-positive coherent-image branch

    A_q=A(4)+O(-8),  A=Sym2 W,  im beta_K=A(2).

Let F=p(K^-) be the actual rank-ten degree-minus-sixty-four bundle in the genuine fifteen-dimensional constant ambient V18* O. Write I=im beta_F for its coherent derivative image, E for its saturation, and delta=length(E/I). The previously proved necessary possibilities are delta in {0,12}.

This proof establishes two new actual-map constraints:

1. The intrinsic derivative of the actual rank-eleven bundle J^- is coherently onto its normal line:

       beta_(J^-):J^- -> (J/J^-)(-2)=O(10)
       is everywhere surjective.                         (1)

2. If delta=12, then the coherent image has only the following orientation in the actual normal bundle:

       E=O(2)+O(10),
       I=O(2)(-D12)+O(10) subset E,
       E/I=O(2)|D12,                                     (2)

   where D12 is the unique reduced orbit of length twelve. In particular I is equivariantly isomorphic to O(-10)+O(10). The other possible abstract type O(2)+O(-2), which would put the defect in the O(10) normal direction, is impossible.

The displayed O(2) is the actual subline (J^-/F)(-2), while O(10) is the actual normal quotient (J/J^-)(-2). Thus (2) distinguishes the two geometric normal directions, not merely their unordered splitting degrees. At every point of D12 the elementary divisors have orders zero and one; outside D12 the image is full.

Neither delta=0 nor delta=12 is asserted to occur, and delta=12 is not excluded. The original defect remains t=0 and is distinct from delta. Both retained F18 types, both dual-extension alternatives, all other triplet coherent-image branches, and the whole-branch/profile and algebraicity questions remain open. No original degree-eighteen fourth-jet assertion is made. No actual coefficient, parameter, point, jet, tensor, matrix, instance rank, or relative normalization is selected or evaluated.

## 1. Complete immutable inputs and actual flag

INPUTS.json records three complete freshly fetched immutable inputs, including commits, paths, Git blobs, UTF8 lengths and SHA256 hashes:

* PR1214 at 4c70887589bbb6f9ffe818575005268d82d14cf0, research/hm/rankfour-profile11-triplet-twenty-exclusion/PROOF.md.
* PR1212 at ca235151d5d93bbead2beffa7640fbd0741aec43, research/hm/rankfour-profile11-triplet-defect-capacity/PROOF.md.
* PR1210 at b2d020a32a3ac5aaf5f264e33e2f930c16195c34, research/hm/rankfour-profile11-triplet-projected-ranktwo/PROOF.md.

All their transitive actual-geometric hypotheses remain assumptions. The proof of (1) below is made directly for the actual rank-eleven bundle and its own coherent backward flag. It does not transfer a rank-seventeen theorem to it.

Work over C on the physical binary-icosahedral line, with G=SL2(F5), fixed determinant convention, and the retained physical representation names. G has no nontrivial scalar characters. Its projective action is A5, with orbit sizes 12,20,30,60 and a unique orbit of size twelve. In particular an invariant effective divisor of degree less than twelve is empty, and one of degree twelve is exactly the reduced D12. The center-even irreducibles have dimensions 1,3,3,4,5. The only dimension-one representation is trivial. The small physical identities used below are

    Sym4 W=D,
    Sym6 W=V+P,
    (Sym4 W)^G=(Sym6 W)^G=0.                           (3)

The inputs supply the actual saturated flag in the same constant ambient

    F subset B:=J^- subset J subset V18* O,
    rank F=10, deg F=-64,
    rank B=11, deg B=-60,
    B/F=O(4), J/B=O(12),
    E=(J/F)(-2)=O(2)+O(10).                           (4)

Here B is the actual backward kernel of J, so derivatives of B lie in J. Hence its intrinsic derivative factors regularly through the actual line subbundle

    phi:=beta_B:B -> (J/B)(-2)=O(10).                 (5)

The O(2) in (4) is the actual (B/F)(-2). Its possible component to O(10) would be an invariant degree-eight section and is zero. Conversely an equivariant map O(10)->O(2) vanishes by degree. The equivariant splitting in (4) therefore retains the actual subline and quotient and has no cross-term ambiguity. It is only a bundle splitting, never a horizontal one.

Every derivative below is taken only on an actual saturated subbundle of the original constant ambient. In particular naturality for F subset B subset J gives the commutative restriction identity

    phi|F = [F --beta_F--> I subset E -> O(10)],       (6)

where the last map is the quotient of E by its actual O(2) subline.

PR1212's complete-versus-actual third-jet comparison gives the actual injection

    B subset Sym14 W(-4),
    top B<=-4.                                        (7)

Thus every nonzero subbundle of B has negative top degree. PR1214 supplies delta in {0,12}. Since deg E=12, the case delta=12 has deg I=0.

## 2. A coherent rank-one capacity proves fullness of phi

The derivative (5) cannot be zero: a saturated horizontal subbundle of a constant bundle on the complex projective line has constant Grassmannian map, hence degree zero, whereas deg B=-60. Its coherent image is therefore a nonzero line subsheaf of O(10), of the form

    im phi=O(10)(-D),  e=deg D>=0.                    (8)

The divisor D is invariant because the map and its image are equivariant.

Starting with Q0=B, take each actual backward kernel Q_(i+1)=Qi^- until zero. The kernels are saturated subbundles of the same constant ambient. By (7), every nonzero Qi has negative top, so it cannot be horizontal. Thus every nonzero stage strictly decreases rank; no horizontal residual bundle survives.

Put Ri=Qi/Q_(i+1). As in the direct coherent-flag argument of PR1212, derivatives of Qi lie in Q_(i-1), and the exact intrinsic kernel gives an injection

    Ri -> R_(i-1)(-2),  i>=1.                        (9)

The first quotient R0 is the actual coherent line (8). Consequently every positive quotient rank equals one; there are exactly eleven such quotients before zero. Composing (9), without saturating any image, gives

    Ri -> O(10-e-2i),  0<=i<=10.

Summing their actual degrees yields

    -60=deg B=sum_i deg Ri
       <= sum_(i=0)^10 (10-e-2i)
        = -11e.                                      (10)

Hence 0<=e<=60/11<12. Invariance of D and the minimum orbit size force e=0. Therefore (5) is coherently onto O(10), proving (1). This is stronger than knowing its image saturation, and uses no chosen splitting or connection on a quotient.

For later bookkeeping write H=ker phi. It is an actual saturated rank-ten degree-minus-seventy subbundle:

    0 -> H -> B --phi--> O(10) -> 0,
    rank H=10, deg H=-70.                             (11)

No jet identification of H is needed or asserted here.

## 3. The two possible degree-zero coherent image types

Suppose delta=12, so I has rank two and degree zero. Write its ordinary splitting degrees as a>=b, with a+b=0.

If a=b=0, equivariance identifies I with R O for a two-dimensional multiplicity representation R. I is center-even, being a subsheaf of the center-even E, so R is center-even. The retained irreducible dimensions above force R=1+1. But every map from O to E vanishes equivariantly: its two components would be invariant sections of O(2) and O(10), both positive degrees below twelve. This contradicts the injection I->E. Thus a>0 and b=-a.

The highest-degree line in I is then canonical, hence equivariant. As G has no scalar characters it is the physical O(a). Its nonzero map into E has at least one nonzero component to O(2) or O(10). Any such component is an invariant section of degree 2-a or 10-a. Since a>0, a nonnegative one of these degrees is less than twelve. Its zero divisor must be empty, forcing that degree to be zero. Consequently

    a=2 or a=10.                                     (12)

The quotient is O(-a); the extension splits equivariantly, because H1(O(2a))=0 and the finite group is linearly reductive. Thus the two abstract types are exactly

    I=O(2)+O(-2),   or   I=O(10)+O(-10).              (13)

There is an actual containment in each case, not just a splitting label. For a=2, the top O(2) maps isomorphically to the O(2) of E and has zero O(10) component by invariant degree eight. For a=10, the top O(10) maps isomorphically to the O(10) of E and has no lower component by ordinary degree. In either case I contains the corresponding full actual normal summand.

Taking the quotient by that contained summand, the remaining line inclusion has degree difference twelve. Its invariant zero divisor is exactly D12. Hence the two possible embedded orientations before the next argument are

    I=O(2)+O(10)(-D12),   or
    I=O(2)(-D12)+O(10).                              (14)

These equalities are equalities of coherent subsheaves in the actual split E: a subsheaf containing the entire first summand is the preimage of its image in the quotient line. No horizontal meaning is assigned to either direct sum.

## 4. A torsion restriction obstruction excludes the first orientation

Assume the first possibility in (14). By the actual restriction identity (6),

    phi(F)=O(10)(-D12) subset O(10).                  (15)

Reduce the everywhere surjective phi from Section 2 modulo the ideal of D12. The resulting map B->O(10)|D12 kills F by (15). It therefore factors through the actual quotient B/F=O(4):

    B -> O(4) --psi--> O(10)|D12.                   (16)

We show that every equivariant psi is zero. Since O(4) is locally free,

    Hom_G(O(4),O(10)|D12)=H0(O(6)|D12)^G.            (17)

The invariant divisor D12 gives the equivariant exact sequence

    0 -> O(-6) -> O(6) -> O(6)|D12 -> 0.             (18)

Its first term is O(6)(-D12)=O(-6) with the physical linearization: any possible linearization difference is a scalar character, and G has none. Because taking invariants for a finite group over C is exact, the cohomology sequence of (18) places H0(O(6)|D12)^G between

    H0(O(6))^G=(Sym6 W)^G=0

and, by equivariant Serre duality in the fixed determinant convention,

    H1(O(-6))^G=(Sym4 W)^G=0.

Thus (17) vanishes. The map (16) is zero, whereas reduction of the surjective phi must still be onto the nonzero torsion sheaf O(10)|D12. This contradiction excludes the first orientation.

Only the second possibility in (14) survives. It is precisely (2), including the cyclic torsion and the simple local elementary divisors. This obstruction uses both the actual adjacent quotient B/F and coherent fullness of phi. It would not follow merely from identifying image saturations or splitting degrees.

## 5. The actual common-kernel incidence in the surviving case

Still conditionally on delta=12, equation (2) and (6) show that phi|F is coherently onto O(10). With H from (11), define the actual intersection G9=F intersect H. The quotient map F->B/H is onto, so

    F+H=B,
    0 -> G9 -> F -> O(10) -> 0,
    0 -> G9 -> H -> O(4) -> 0.                      (19)

In particular G9 is saturated in the constant ambient, has rank nine and degree -74. Since F^- is the exact kernel of F->I and the kernel of I->O(10) is the actual O(2)(-D12)=O(-10), there is also an exact sequence

    0 -> F^- -> G9 -> O(-10) -> 0,
    rank F^-=8, deg F^-=-64.                         (20)

These are common-kernel and quotient statements for the actual maps, not assertions about horizontal complements. They record the remaining incidence problem without identifying G9 with an intrinsic jet bundle.

## 6. Contribution and stopping point

The new unconditional step is coherent fullness of the actual derivative of J^-, proved by its own rank-one backward flag. The new conditional exclusion then uses a torsion-valued equivariant Hom obstruction along the fixed twelve-point orbit. It selects which of the two distinct normal directions can carry the remaining local defect.

The necessary alternatives are therefore delta=0 with I=E, or delta=12 with the exact embedded image (2) and common-kernel incidence (19)-(20). Neither alternative is asserted to occur or to be impossible. No original higher-jet separation, algebraicity, whole branch or profile exclusion is inferred.
