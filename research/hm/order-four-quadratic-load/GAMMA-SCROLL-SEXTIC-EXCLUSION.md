# Smooth-modular Gamma fibers: exact dictionary and sextic exclusion

Status: checked deduction conditional only on the already established transversal evaluation normal form along C and the cited primary-source geometric statements. No HM coefficient specialization or numerical rank computation is used.

Primary source: Aure, Decker, Hulek, Popescu, Ranestad, *Syzygies of Abelian and Bielliptic Surfaces in P4*, arXiv:alg-geom/9606013v2, https://arxiv.org/pdf/alg-geom/9606013 .

Source inputs (paraphrased): Section 4 identifies the six invariant quintics with Λ²H⁰(E). Proposition 4.2 gives the elliptic-normal-quintic family E_p, with origin p on the HM line, smooth except at twelve modular parameters. Lemma 4.14 identifies the incidence surface I_p with a smooth elliptic quintic scroll Q_p, ruled over E_p. Lemma 4.15 constructs S_p by a basepoint-free bilinear map I_p→P4 and identifies it with the degree15 base locus of the net of invariant quintics singular along E_p. Proposition 4.16 identifies S_p birationally with Sym²E_p and says its singular locus is E_p, with multiplicity four. These are distinct from §9's reducible unions of five cubic surfaces in hyperplanes.

## 1. Exact parameter dictionary

Let p lie on the chosen HM component L and outside the twelve modular parameters. Put B_p=ker(U→E_p), dimension3. At p the full evaluation has rank1. Its transversal rank-drop hypothesis gives an isomorphism

N_{L/P4,p} → Hom(B_p,Q_p^ev),

where Q_p^ev is the one-dimensional evaluation cokernel (not the elliptic scroll Q_p).

Choose s0∈U with nonzero evaluation and a basis b1,b2,b3 of B_p. In a local frame the first-order evaluation has first row (1,*,*,*) and second row (0,a1,a2,a3), where a1,a2,a3 are independent conormal coordinates. The differentials of s0∧bi are independent; the differentials of bi∧bj vanish. Consequently the subspace of the six invariant quintics singular at p is exactly Λ²B_p, dimension3. This is invariant under changes of frame or basis.

The net W_p of invariant quintics singular along the smooth elliptic quintic E_p is three-dimensional by Lemma4.15 and its proof. Since p∈E_p, W_p⊂Λ²B_p. Equality follows from dimensions. Therefore the actual determinantal surface X_{B_p}, cut out by Λ²B_p, has the same underlying surface as S_p. Under the established pure-CM-degree15 assertion for X_B, it equals the reduced S_p scheme-theoretically: S_p is integral degree15, so X_B has generic multiplicity1 and CM forbids embedded associated components. (For the curve exclusion below, support equality already suffices.)

Thus this is an identification of the actual B-family, not an analogy between moduli spaces.

## 2. No integral sextic on S_p

Let I_p⊂E_p(x)×P4(z) be the incidence surface of Lemma4.14. Its second projection is an isomorphism to the smooth elliptic quintic scroll Q_p; denote the first projection by q:I_p→E_p. The map ν:I_p→S_p is given by bilinear forms without base points, so

ν*O_{S_p}(1)=pr_x*O_{E_p}(1)⊗pr_z*O_{Q_p}(1).

This line bundle is ample because it is the restriction of O(1,1) from the product of projective spaces. Hence ν is finite (a positive-dimensional proper fiber would contain a curve of degree zero for an ample bundle). Birationality also follows directly from degrees: on the quintic scroll, O_Q(1) has square5 and degree1 on a ruling; q*O_E(1) is numerically5 fibers. Thus (ν*H)^2=5+2·5=15. Since deg S_p=15, the finite map ν has degree1. As I_p is smooth, ν is the normalization. This avoids assuming that merely being birational to Sym²E proves birationality of this particular map.

Suppose D⊂S_p is an integral degree6 curve. It cannot equal the singular elliptic quintic E_p (degree5). Its strict transform T⊂I_p therefore maps birationally to D. Write

h=deg(O_{Q_p}(1)|T)>0,

d=deg(T→E_p) if nonconstant, and d=0 if constant.

Since E_p is an elliptic normal quintic, the polarization identity gives 6=h+5d.

If d≥2, the right side is at least11, impossible. If d=1, then h=1. But an integral degree1 curve in projective space is a line; thus T, viewed in Q_p, is P1 and cannot map nonconstantly to the elliptic curve E_p. If d=0, T is contained in a ruling fiber P1 of I_p≅Q_p. Being an integral curve it is the whole fiber. Its h-degree is1, again contrary to6=h+5d.

Therefore S_p contains no integral degree6 curve.

## 3. Consequence for the active beta problem

The active branch requires an integral sextic D_H⊂X_{B_H}. Hence B_H cannot equal κ(p) for any smooth modular parameter p∈L. Only the twelve cusp images in Γ remain unexcluded by this argument. Since κ:L→Γ is an isomorphism and the beta-parameter image is positive-dimensional, it cannot be contained in this finite set. In particular a curve-image branch cannot have image Γ. This does NOT eliminate curve images elsewhere in P(U*), nor two-dimensional images, nor claim a full repair.

No assertion is made here about the individual cusp fibers. The five-cubic-surface pencil of §9 cannot be equated with all of Γ; that would contradict the smooth-modular identification above.

## 4. Generic parameters avoid the entire rank-zero locus

The closure Y_beta of the image of the irreducible hyperplane parameter space is irreducible and has dimension one or two by the prior image-dimension argument. If its general point lay on Gamma, it would be contained in Gamma. It cannot have dimension two there, and in dimension one it would equal Gamma, contradicting Section 3. Hence a general active beta parameter lies outside Gamma. This conclusion does not require deciding the twelve individual cusp fibers: a positive-dimensional irreducible image cannot be confined to them.

Accordingly the off-Gamma hypotheses of BETA-QUOTIENT-DEFECT-UPPER-BOUND.md apply to the general member of either remaining image dimension. The upper bound e<=46 is now generic in the entire active beta branch (not a pointwise assertion at every cusp). The lower bound is23 for fixed-parameter families of dimension two and25 for dimension three. The quotient degree is100 at these general parameters. These implications are derived here; they are not claims made by the literature source.

Repository input pins: evaluation/kappa description 3edb50b13b8a5ce876f52a2085ecc8d16b3181c0; integral-degree15 reduction 3714d276821366f9b1230abb6cc60b81861bb878; image dimension one or two 3f780322a40b38d92d6f400f14b661b807e01030; quotient/defect upper bound d9f7c24471a1e2640152cb17bd092ed1f22c63f8. All are in Akilleez-QA/read-em-and-weep PR543.
