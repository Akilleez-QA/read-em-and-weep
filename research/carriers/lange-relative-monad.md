# Every original Lange bundle has the required relative symplectic monad

## Statement

Let V be a bundle from Lange's abelian-surface construction in P=P1×P3, and put F=V(-1,-2). Write p:P→P1. Then F is the cohomology of a global symplectic monad

A=O_P(1,-2) → B → C=O_P(-1,2),

where B has a maximal isotropic subbundle U=O_P(-2,1)^2 and fits

0→U→B→W=O_P(2,-1)^2→0.

After identifying Lange's reduced ribbon with the graph of a ruling of a smooth quadric, local symplectic frames over the two base charts give maps α=(a,h), β=(-h^T,a^T), up to consistent signs and ordering, with

a=(t x0−s x2, t x1−s x3).

The restriction of h to the ruling line is a basepoint-free pair of binary cubics. Its coefficients are independent of the base parameter in the induced frames. Thus every original Lange bundle satisfies the relative-monad hypothesis of the mixed-nonvanishing proof; no classification of arbitrary same-Chern bundles is being assumed.

## 1. Cohomology from the actual Lange ribbon

Lange's construction gives

0→O_P(-3,0)→F→I_Y(3,0)→0,

where Y is a ribbon on Z≅P1_base×P1_ruling. The map Z→P3 is the Segre embedding of a smooth quadric, and its nilpotent ideal is O_Z(-2,2). In these coordinates

O_P(a,b)|Z=O_Z(a+b,b),
0→O_Z(-2,2)→O_Y→O_Z→0.

These are the actual statements of Lange's sections4–5, including the exclusion of the quadric-cone case.

For b=-1,-2, all relative cohomology of O_P(3,b) and O_P(-3,b) vanishes. Hence the ribbon exact sequences identify

R¹p_*F(0,b)=p_*O_Y(3,b),
p_*F(0,b)=0.

For b=-2, the structure sequence is an extension of O_Z(1,-2) by O_Z(-1,0), giving R¹p_*F(0,-2)=O_P1(-1). For b=-1 it is an extension of O_Z(2,-1) by O_Z(0,1), giving R¹p_*F(0,-1)=O_P1^2.

## 2. The fiber Rao module is cyclic

On every fiber P3, the normalized bundle has an exact sequence

0→O_P3→F_t→I_Yt→0.

The ribbon Y_t on the line Z_t has nilpotent ideal O_Zt(2). In coordinates on the line, its Ferrand map is given by cubics f,g without a common zero. Since line bundles on P3 have no intermediate cohomology,

H¹(P3,F_t(k))=coker[H0(O_P3(k))→H0(O_Yt(k))].

For k<-2 both groups on the right vanish. For k≥-2, the reduced-line sections are all restrictions of ambient sections when they occur. The remaining cokernel is

C[v0,v1]_(k+2) / (f,g)·C[v0,v1]_(k−1).

Thus H¹_*(F_t) is the cyclic graded module C[v0,v1]/(f,g), with its generator in twist -2. The normal linear forms act by zero.

## 3. A global universal extension kills H¹ on every fiber

Set C=O_P(-1,2), A=C*. Leray gives

Ext¹(C,F)=H¹(P,F(1,-2))=H0(P1,O_P1)=C.

Choose a nonzero class ε and form

0→F→K0→C→0.

Its restriction to every P3 fiber is the nonzero cyclic generator above. Consequently the connecting map

H0(O_P3(k+2))→H¹(F_t(k))

is surjective for every k. Therefore H¹(K0_t(k))=0 for all t and k.

## 4. Explicit global symplectic lift

The determinant trivialization gives F an alternating form J. The extension cocycle ε takes values in F⊗A. On local frames A⊕F⊕C, equip this direct sum with the alternating form

Ω = [[0,0,1],[0,J,0],[-1,0,0]].

For a local column e in F⊗A and h in A², the unipotent block matrix

N(e,h) = [[1,e^T J,h],[0,I,e],[0,0,1]]

preserves Ω. Direct multiplication gives

N(e,h)N(e′,h′)=N(e+e′,h+h′+e^T J e′).

Compose these with the diagonal transition matrices for A,F,C. The extension cocycle condition for e leaves only the central A²-valued two-cocycle e_ij^T J e_jk. Its cohomology class is zero because

H²(P,A²)=H²(P,O_P(2,-4))=0.

Choose an A²-valued one-cochain h cancelling this defect. The resulting matrices define a rank-four symplectic bundle B, with an isotropic copy of A, quotient K0, and a surjection B→C. The cohomology of A→B→C is the original F. This constructs the symplectic monad directly; it does not rely on an unproved self-duality classification. Also H¹(P,A²)=0, although uniqueness of the lift is not needed.

## 5. Determine the middle term along the fibers

The exact sequence 0→A→B→K0→0 and vanishing of intermediate cohomology for line bundles on P3 give H¹(B_t(k))=0 for all k. Since B_t is symplectic, Serre duality gives H²(B_t(k))=0 for all k. Horrocks' splitting criterion applies.

The monad gives

ch(B_t)=ch(F_t)+exp(-2v)+exp(2v)=4+2v².

Thus B_t is a sum of four line bundles whose splitting integers have sum0 and sum of squares4. The only possibility is

B_t=O_P3(-1)^2⊕O_P3(1)^2.

## 6. Determine the global positive part and linear equations

The relative evaluation map defines a rank-two subbundle

U=p* p_*B(0,-1)⊗O_P(0,1) ⊂ B.

More explicitly, set K1=ker(B→C). The exact sequence 0→A(0,-1)→K1(0,-1)→F(0,-1)→0 has relatively acyclic first term A(0,-1)=O(1,-3). Hence R¹p_*K1(0,-1)=R¹p_*F(0,-1), and the boundary from 0→K1(0,-1)→B(0,-1)→C(0,-1)→0 is precisely multiplication by the original universal-extension class ε. These sequences give

0→p_*B(0,-1)→O_P1(-1)^4→O_P1^2→0.

The last arrow is multiplication from the degree -2 generator to the degree -1 part of the Rao module. In the smooth-quadric ruling coordinates it is ordinary restriction of ambient linear forms to the ruling line, twisted by O(-1). It is the standard Segre evaluation sequence, whose kernel is O_P1(-2)^2. Therefore

U=O_P(-2,1)^2.

The restriction of the alternating form to U vanishes: Hom(Λ²U,O_P)=H0(O_P(4,-2))=0. Since U has half the rank, B/U≅U*=O_P(2,-1)^2.

The restriction β|U:U→C is given by the two generators of the kernel of the displayed Segre evaluation. Consequently, after choosing homogeneous coordinates, its linear forms are a1=t x0−s x2 and a2=t x1−s x3. Symplectic duality determines the corresponding component of α.

## 7. The cubic pair required by the obstruction proof

Over an affine base chart, Ext¹(W,U)=0 because the only potentially contributing P3 group is H¹(O_P3(2))=0. Thus B splits locally as U⊕W; the splitting can be chosen symplectic. The remaining entries h of α are cubic in the P3 variables. Modulo (a1,a2), their changes of splitting vanish. Hence their restrictions glue to sections of

Hom(A,U)|Z=O_P(-3,3)|Z^2=O_Z(0,3)^2.

They are therefore binary cubics with coefficients constant along the base. Since α is a subbundle injection, these cubics have no common zero on any ruling line. This is exactly the hypothesis needed for the injective-Jacobian argument in the mixed-nonvanishing proof.

## Sources and checks

Lange, A Vector Bundle of Rank2 on P1×P3: https://arxiv.org/pdf/alg-geom/9506021, especially sections4–5.

Horrocks' splitting criterion is stated as Theorem1.2 in the primary research paper Yau–Ye, Several Splitting Criteria for Vector Bundles and Reflexive Sheaves: https://msp.org/pjm/2013/266-2/pjm-v266-n2-p10-p.pdf.

The two Heisenberg identities were independently checked algebraically, including exact symbolic 4×4 matrix verification. All seven steps of this lemma were also independently audited, including the identification of the relative boundary with Rao multiplication and the intrinsic nature of h restricted to Z. No unresolved monad-identification or classification assumption remains in this lemma.

## Mixed-class consequence

Applying [mixed-nonvanishing.md](mixed-nonvanishing.md) and [mixed-reduction.md](mixed-reduction.md), every original Lange bundle has nonzero Δ(F). Its symmetric degree-96 elliptic-product pullback therefore has three independent mixed polarized obstructions, HH² evaluation rank15, and kernel dimension13 rather than the character-annihilator dimension16. This excludes this symmetric pullback construction as a weak-kernel-equality carrier. It does not exclude all squareclass-two carriers or other pullback constructions.
