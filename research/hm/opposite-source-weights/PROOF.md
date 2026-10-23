# Signed torsion weights and the vertex-extension absorption law

Status: authored structural proof independently mathematically reviewed in REVIEW.md; not formally checked. Work over C. No selected actual HM/source points, coefficients, parameters, matrices, derivatives or instance ranks are evaluated.

## 1. Exact inputs

All repository paths refer to Akilleez-QA/read-em-and-weep; INPUTS.json supplies exact immutable identities.

- PR934 at 8c9847612b5f575b987cec9c62b72b099d745e44, research/hm/reduced-opposite-pencil/PROOF.md: the actual 26-to-31 presentation 0->E O(-1)->H O->C->0, with H=1+3A+V+2P+2D, the source identity [E]=[U]-[S]-[H14] in representation K-theory, U=H1(B(2))_-, S=Sym3 W and H14=W'+2T6; and the actual extension 0->O(10)->D_vert->C->0.
- PR936 at 60fd2b9951dd151dfbdff5b09316d05495cca53d, research/hm/opposite-torsion-trichotomy/PROOF.md: the torsion length budget and canonical complete-evaluation splitting; in the maximal case length(Z)=24 the three global characters and six possible degree-two quotient bundles F=C/Z. The middle character forces semisimple length-two stalks.
- PR928 at 1a8fb75aa886f9bb6c07e357759d37630cdd127d, research/hm/profile11-source127-cdf-positive-factorization/PROOF.md, Section 3 only: the actual normalized HM monad and fixed nine-class lambda-ring Euler formula. Its source-specific factorization results are not used. Its imported actual cohomology and section-resolution inputs remain in force.

We retain G=SL2(F5), W, W', A=Sym2 W, V=Sym2 W', P, S=Sym3 W, D=Sym4 W and T6=Sym5 W. Let Omega be the unique orbit of length twelve. No point of Omega is selected for evaluation: statements about a stalk below are uniform equivariant statements for an arbitrary abstract stabilizer.

## 2. The actual source character

The actual E is

    E = 2W + W' + 2S + 2T6.                         (1)

Here is a derivation, not an inference from its dimension. As B(2)=Sym2(F_HM)(3), use PR928's notation Hcoord=V+W, L2=Lambda2(Hcoord), N=A+W', S_n=Sym^n(Hcoord), and

    c_-1=-N, c_0=W'L2-N, c_1=-W'Hcoord, c_2=W'.

The Euler character is

    chi_G(B(2)) = (1/2) sum_(i,j=-1)^2 c_i c_j S_(i+j+3)
                   + (1/2) sum_(i=-1)^2 psi2(c_i) S_(2i+3).       (2)

All twists are between one and seven, so only ordinary symmetric-power characters occur. H0(B(2))=H2(B(2))=0 are among PR934's geometric inputs. To check the remaining vanishings, the tensor section resolution of End(F_HM)(2) has terms E0=15F_HM(-1)+4F_HM and E1=35F_HM(-2), followed by terms in higher homological degrees. For H3 the controlling groups are H3(E0), dual to H1F_HM(-3), H1F_HM(-4), and H4(E1), dual to H0F_HM(-2). These vanish by the primary cohomology inputs used in PR928. For H4 only H4(E0) occurs, dual to H0F_HM(-3), H0F_HM(-4), also zero. Higher diagonal terms exceed dimension four. Trace splitting gives these vanishings for B. Thus H1(B(2))=-chi_G(B(2)).

The fixed abstract nine-class arithmetic of (2) gives

    H1(B(2)) = A+2V+3P+4D + 2W+2W'+3S+4T6.

Its negative part is U=2W+2W'+3S+4T6. Subtract S and H14=W'+2T6 to prove (1). The accompanying verifier checks all class values, not an actual monad differential.

## 3. Stabilizer conventions and the source of an evaluation pencil

Let K=C10 be the binary stabilizer. Define lambda to be its character on the fiber of O(1), and put zeta=lambda^2. Then

    W|K=lambda+lambda^-1,
    A|K=1+zeta+zeta^-1,
    cotangent character tau=lambda^-2=zeta^-1,
    O(10)|K=1.                                      (3)

The cotangent identity fixes the orientation: the quotient evaluation W->O(1)|K has character lambda and its kernel has character lambda^-1. The tangent representation is Hom(kernel,quotient)=lambda^2; its dual is tau. This does not treat an arbitrary faithful C5 character as the cotangent character.

For a torsion sheaf M supported on Omega, let E_M=H0(K_M(1)), where K_M is its complete-evaluation kernel. Twisting the evaluation sequence and taking global sections gives

    [E_M]=W[H0(M)]-[H0(M(1))].                      (4)

This remains valid for nonreduced torsion because it uses exactness and its actual composition-factor filtration. If one local composition factor is zeta^r, its contribution to (4) is

    W Ind_K^G(lambda^(2r)) - Ind_K^G(lambda^(2r+1))
      = Ind_K^G(lambda^(2r-1)).                     (5)

The tensor-induction identity proves (5). The three odd inductions are

    J1=Ind(lambda)=Ind(lambda^-1)=W+S+T6,
    J3=Ind(lambda^3)=Ind(lambda^-3)=W'+S+T6,
    J5=Ind(lambda^5)=2T6.

These follow directly from the abstract restrictions W:{±1}, W':{±3}, S:{±1,±3}, T6:{±1,±3,5,5}. Consequently the exponents r=0,1,-1,2,-2 contribute respectively J1,J1,J3,J3,J5.

For each of PR936's degree-two quotient bundles, E_F is W when F has an O(2) summand or a W O(1) summand, and is W' when F=W' O(1)+A O. Indeed the evaluation kernel of O(2) is W O(-1); that of L O(1) is L O(-1), and constant summands have zero evaluation kernel. PR936's functorial evaluation splitting forces E=E_Z+E_F.

## 4. Signed local factors: all six bundles remain, but their pairing is forced

Assume length Z=24. The only possible unordered local composition-factor exponents relative to (3), with their quotient bundles, are:

    Type I:    {0,-1}, F=O(2)+P O;
    Type II:   {0,1},  F=W' O(1)+A O;
    Type III:  {1,-1}, F=O(2)+(1+V)O or W O(1)+V O;
    Type IV:   {1,2},  F=O(2)+(1+A)O or W O(1)+A O.    (6)

To prove exhaustiveness, PR936 supplies the possible absolute-weight pairs 0/±1, ±1/±1, and ±1/±2. If E_F=W, (1) requires E_Z=J1+J3; if E_F=W', it requires E_Z=2J1. Substituting (5) gives exactly (6). In the first row 0/1 would require source W', while 0/-1 requires W. In the second character pattern only opposite signs give J1+J3. In the last, only 1/2 does so; every other sign choice introduces either too many W' or too many T6 or too few W. This is a local-character restriction invisible in H0(C) alone.

No six-bundle exclusion follows from the two coefficient characters alone. In fact each bundle in (6) has an abstract G-equivariant model with exactly the prescribed E and H: induce from K the semisimple two-dimensional local module with the listed factors, regarded as a sheaf on the reduced orbit; form its direct sum with the listed F and take complete evaluation. PR936 computes H, and (5) computes E. Thus all six survive these source/target-character tests. This construction claims neither actual HM occurrence nor compatibility with the rest of its marked multiplication system.

The local module is either semisimple k+k or cyclic R/(x^2). In the cyclic case its top character r and next character r-1 are determined by tau=zeta^-1. Therefore Types I, II, IV have cyclic top characters respectively 0,1,2. Type III cannot be cyclic, as already shown in PR936.

## 5. Equivariant vertex-extension absorption table

The additional actual extension now obeys the following sharper laws, still without selecting its extension class:

    Type I, either local module: tors(D_vert) has length 24;
        indeed 0->O(10)->D_vert->C->0 splits G-equivariantly.
    Type II, either local module: tors(D_vert) has length 24 or 12.
    Type III, necessarily semisimple: tors(D_vert) has length 24 or 12.
    Type IV, semisimple: tors(D_vert) has length 24 or 12.
    Type IV, cyclic: tors(D_vert) has length 24 or 0, never 12.     (7)

More precisely, the invariant extension-class space Ext1_G(C,O(10)) has dimension zero in Type I and dimension one in every other row. In each one-dimensional row the zero class retains length 24, while every nonzero class has the other length specified in (7). This statement concerns the actual extension's possible values, not a claim that its class is nonzero.

Proof: work equivariantly over the completed DVR R at an abstract orbit point. A finite-order action can be linearized on its local parameter by averaging, so choose a formal uniformizer x with character tau. This is a universal local algebra argument, not a coordinate evaluation. The target line has trivial stabilizer character by (3); averaging a lift of its fiber generator gives an invariant local generator, so it is equivariantly the trivial R-module.

For a simple module k with character zeta^r, the resolution R tensor zeta^(r-1) -> R tensor zeta^r, with map multiplication by x, gives

    Ext1_R(k_r,R) has character zeta^(1-r).       (8)

For a cyclic length-two module with top character zeta^r, the analogous x^2 resolution gives

    Ext1_R((R/(x^2))_r,R)
       = (R/(x^2)) tensor zeta^(2-r).            (9)

Its constant and x terms have characters zeta^(2-r), zeta^(1-r). Therefore semisimple Type I has no invariant term; cyclic Type I has weights 2,1 and likewise none. Every other semisimple row has exactly one r=1 factor, hence a one-dimensional invariant Ext space. Cyclic Type II has weights 1,0, so its invariant class is a scalar multiple of x. Cyclic Type IV has weights 0,-1, so its invariant class is a scalar multiple of a unit.

For clarity about lengths, an extension of R/(x^2) by R with class a modulo x^2 has a presentation with relation x^2 y=a e. If a=0 its torsion length is two; if a is a nonzero multiple of x its torsion length is one; if a is a unit it is zero. This follows directly from Smith normal form, or the gcd of x^2 and a. For k+k, a nonzero class absorbs exactly one simple factor, leaving length one, whereas the zero class leaves length two. This proves all local assertions in (7).

To pass to the global invariant Ext space, first use a G-equivariant splitting C=Z+F from PR936. All degrees of F are at most two, so Ext1(F,O(10))=H1(F* tensor O(10))=0. For Z the sheaf Hom(Z,O(10)) vanishes, and its sheaf Ext1 has finite support. Thus global Ext1(Z,O(10)) is the direct sum of its twelve local Ext spaces. G-invariants identify this direct sum with the stabilizer-invariant Ext space at one abstract point. Characteristic zero makes taking finite-group invariants exact, so these are precisely equivariant extension classes. This proves the stated global dimensions and the equivariant splitting in Type I. A nonzero invariant class is nonzero at every point of the orbit, so summing the local torsion lengths proves (7).

## 6. The torsion-free vertex quotient and a local-freeness criterion

Still in the maximal-torsion case, let a be the absorbed local length, so a=0,1,2 and length(tors(D_vert))=24-12a. Then there exists a G-equivariant bundle/sheaf decomposition

    D_vert = F + O(10+12a) + tors(D_vert).           (10)

The summands' isomorphism types are asserted, not canonical complementary subspaces. In particular D_vert is locally free if and only if Type IV is cyclic and the actual invariant extension class is nonzero. In that event

    D_vert = F + O(34),

with F one of the two Type IV bundles in (6).

Indeed split C=F+Z equivariantly. The Ext1(F,O(10)) vanishing in Section 5 splits the extension over F, leaving D_vert=F+M with 0->O(10)->M->Z->0. Write T_M=tors(M). Its quotient is a rank-one bundle L, and the induced inclusion O(10)->L has torsion quotient of length 12a, supported uniformly on Omega. Thus L=O(10+12a). There is no extra G-character on this line because G is perfect. Finally 0->T_M->M->L->0 splits equivariantly since Ext1(L,T_M)=0 and averaging is available. This proves (10). The list (7) makes a=2 possible exactly in the stated cyclic Type IV case with nonzero class, proving the criterion.

## 7. Contribution and boundary

The original six quotient-bundle types are not further excluded by source and target characters: the abstract models above prove that limitation sharply. Nevertheless the actual source character fixes the signed stabilizer factors and forces a new vertex-extension table. In particular Type I cannot lose any torsion through O(10), while cyclic Type IV must lose either all of it or none of it. The earlier unrestricted alternatives 12 or 24, or bounds by tors(C), do not supply these distinctions.

No torsion length, quotient type, local cyclicity or actual extension scalar is selected. No actual source exclusion, catalogue/frontier change, selected-instance evaluation, mixed-map solution or algebraicity claim follows. This is structural mathematics, not formal proof-assistant verification.
