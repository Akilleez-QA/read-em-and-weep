# A canonical degree-three syzygy detects the alternating transfer

## Theorem and scope

Retain the actual source2 nonzero pure-V compatible-radical hypotheses.
Use only the fixed negative two-space W. Write Q2:M2→M4 and Q3:M3→M5
for multiplication by the SAME actual invariant quadratic. Let j2,j3,j4
be the actual fixed-negative-pencil radical and h:M4→M2 its canonical
endpoint homotopy. Put F2=im h, F3=W F2, and

    K3=ker Q3 ∩ ker j3 ⊂ M3.

Then F3⊂K3. There is a canonical equivariant map

    Hbar: W⊗I4 → K3/F3,                               (1)

independent of the equivariant right inverse used below, and a canonical
pairing

    Psi:W⊗(K3/F3)→I2,     Psi(n,[v])=hY_n v.           (2)

Normalize the bilinear transfer of PR1069 by

    Alt B(a,b)=(B(a,b)−B(b,a))/2=κ L_[a,b]*,
    [a,b]=a_xb_y−a_yb_x.

Then the exact mixed-direction identity is

    Psi(n,Hbar(r,p))=4κ L_(nr)*p                       (3)

for all n,r∈W and p∈I4. No assumption that the diagonal R vanishes is
needed. The two symmetric transfer channels cancel from this identity.

Consequently, if κ≠0, the T=Sym5 W constituent of W⊗I4=W'+T maps
injectively into K3/F3. Since F3 has character W'+2T, the ACTUAL
T-multiplicity map of the combined map

    (Q3,j3):M3→M5⊕I3,       I3=im j3=T,

has domain dimension6, target dimension4, and rank at most3. Equivalently
its fourth exterior power is zero. This is a conditional structural rank
constraint, not an evaluated rank of actual coefficients.

In particular, in endpoint sixteen, a nonzero purely alternating transfer
(R=0 but B≠0) requires this combined multiplicity rank drop. If that map
were separately proved to have rank4, then κ=0; if also R=0, then B=0.
Neither rank nor coefficient is selected here, and the zero full-transfer
case is not excluded. No endpoint or source realization is asserted.

## 1. Exact inputs and notation

INPUTS.json authenticates five immutable public proofs:

- PR1048: hT_a h=0, actual radical intertwining at all three degrees,
  and the restriction to the fixed W; no mixed commutation is supplied.
- PR1054: actual F2=I2⊕P_h and F3=I3⊕X_W P_h, with
  F3=W'+2T, I3=T and dimensions9,14. Only its first-stage statements
  are used, not its old endpoint list or conditional smallest endpoint.
- PR1068: NC4 is the FULL joint-negative kernel in M4, so W I4=0;
  the actual spaces are M3=3W'+3S+6T and M5=W'+3T. Its inherited
  multiplication is the actual negative-coordinate action.
- PR1069: Q2:P_h→I4 is an isomorphism, s its inverse, and
  Π_a=hT_aG_Q, B(a,b)=Π_aT_bs, with exact target I2 and diagonal R.
  Equivariant right inverses differ by a map into I2⊂ker Q2.
- PR1071: fixed Hamiltonian bracket and invariant bilinear-adjoint
  normalization; L_[a,b]* is a nonzero generator of the unique alternating
  channel. Its special endpoint-nine coefficient statement is NOT needed.

Set X_l:M2→M3 and Y_l:M3→M4 to be negative linear multiplication.
Thus Y_mX_l=T_lm. Write Z=im Q2. The right inverse G_Q:Z→M2 is always
G-equivariant. The source of s is the actual I4, not an arbitrary P copy.
All claims retain the original actual-source hypotheses of the inputs.

No extension of h to other degrees is used. Q3 is actual polynomial
multiplication, so ordinary module associativity gives

    Q3 X_l v = l Q2 v.                                (4)

The multiplication on the right lands in M5. It is not a claim that Q
preserves NC, NR, F, or any horizontal splitting.

## 2. The common degree-three kernel and the lifted relation

Since Q2 F2=I4 and W I4=0 by PR1068, (4) gives Q3F3=0. Also
j3 X_l=X_l j2 and j2h=0 give j3F3=0. Hence F3⊂K3.

For b∈A define the actual correction without a sign change

    k_b=G_QT_b s:I4→M2,       Q2 k_b=T_b s.            (5)

It is defined since T_b im h⊂ker h⊂Z. Equation hQ2=j2 yields

    j2 k_b=hT_bs=0.

For l,m,r∈W define

    H(l,m;r)=X_l k_(mr)−X_m k_(lr):I4→M3.            (6)

By (4)-(5), Q3 applied to (6) is multiplication by
lmr−mlr on s, hence zero. Applying j3 is also zero because j2k_b=0.
Therefore H takes values in K3. It is alternating in l,m. Fix the
volume normalization epsilon(l,m)=l_xm_y−l_ym_x, so (6) factors as

    H(l,m;r)=epsilon(l,m) H_r.

This is a representation-theoretic factorization through Lambda2 W,
not evaluation at a chosen actual direction.

If G_Q is replaced by another EQUIVARIANT right inverse, its difference
has image in I2 by PR1069. Thus k_b changes by an I2-valued map, and
H changes by a map into W I2=I3⊂F3. The quotient class Hbar_r is
therefore canonical, proving (1). H_r itself need not be independent
of the chosen right inverse as a map into M3.

## 3. The canonical pairing and exact transfer comparison

For v∈K3, actual radical intertwining gives

    Q2 hY_n v=j4Y_n v=Y_n j3v=0.

The element hY_n v lies in im h, whose intersection with ker Q2 is I2.
Thus hY_n maps K3 into I2. It kills F3 because on its generators

    hY_n X_l h = hT_(nl)h=0.

This proves the well-defined pairing (2). Directly applying it to (6)
and using (5) gives the literal identity

    hY_n H(l,m;r)
      =hT_(nl)G_QT_(mr)s−hT_(nm)G_QT_(lr)s
      =B(nl,mr)−B(nm,lr).                             (7)

All targets here are the actual I2. No exchange of directions through
h, G_Q or Π is made.

## 4. Why the symmetric channels cancel and the coefficient is four

Let B_sym be the symmetric part of B. Ordinary multiplication has the
exact representation sequence

    0→1→Sym2(Sym2 W)→Sym4 W→0.

Because Hom_G(I4,I2)=Hom_G(P,D)=0, the restriction of B_sym to the
left trivial factor tensored with I4 is zero. Thus B_sym factors through
the product of its two quadratics. Since (nl)(mr)=(nm)(lr), it follows
that

    B_sym(nl,mr)−B_sym(nm,lr)=0.                       (8)

This argument applies to BOTH symmetric channels, not only a selected
basis vector. It uses the actual equivariance of B and the exact trivial
kernel, not the false claim that every symmetric function depends only
on the product of its arguments.

The remaining alternating part is κL_[a,b]* in the stated normalization.
The Poisson derivation rule in two variables gives the exact identity

    [nl,mr]−[nm,lr]=4 epsilon(l,m) nr.                 (9)

The checker expands (9) with all eight linear-form coefficients formal.
Combining (7)-(9), and using linearity of L* in the quadratic, yields

    hY_n H(l,m;r)=4κ epsilon(l,m)L_(nr)*.

Factoring out the determinant tensor gives (3). The number4 depends on
the explicitly fixed bracket and Alt=(B−B^op)/2 convention; no actual
source coefficient is normalized to a numerical value.

## 5. The actual T obstruction and its precise limit

Since W⊗I4=W'+T, decompose the source of Hbar into its two irreducible
constituents. The pairing with its W' constituent is always zero:
W⊗W'=P and Hom_G(P,I2)=0. If κ≠0, the right side of (3) is a nonzero
family, since products nr span A and L* is nonzero. Therefore Hbar is
nonzero on its T constituent. Irreducibility makes that restriction
injective into K3/F3.

Complete reducibility then shows that K3 contains at least three copies
of T: the two specified actual copies in F3 plus the detected quotient
copy. The kernel of (Q3,j3) is K3. Its T-isotypical multiplicity spaces
have sizes6 in M3,3 in M5, and1 in I3. Hence the induced combined
multiplicity map C6→C3⊕C has rank at most6−3=3, proving the asserted
fourth-exterior-power constraint. The multiplicity spaces and map are
actual; choosing bases to state a rank does not evaluate their entries.

This is a new syzygy constraint, not a classification of terminal
submodules. It does not prove the combined map has rank4, that κ≠0,
or that Hbar is nonzero when κ=0. The missing premise for excluding a
nonzero purely alternating remainder is control of this actual quotient
K3/F3 or of its pairing (2). Even rank4 would only force κ=0; when R=0
it would force B=0, which this theorem does not itself exclude.

## Reproduction

Run python verify.py and python -O verify.py. The bounded certificate
authenticates all five inputs, checks exact composition types, the full
formal symmetric-product relation and Poisson identity, and finite-group
representation multiplicities. It verifies the exterior-power dimension
implication with an abstract universal kernel normal form, not actual HM
matrices. The actual kernel inclusions, section independence and inherited
multiplication arguments are supplied in the written proof.

No actual coefficient, parameter, direction, jet or source-instance rank
is evaluated. The theorem applies under the retained conditional pure-V
hypotheses without assuming h is graded, Q preserves a horizontal block,
or mixed same-direction homotopies commute with arbitrary arrows.
