# Birationality and the quartic inverse of the actual ten-cubic node/conductor map

Status: structural mathematical proof, with independent mathematical review in REVIEW.md. Not formally checked. Work over C. No selected HM/source coefficients, numerical matrix or point evaluations, numerical rank tests, searches, or large computations are used. The bilinear map and minors below are universal constructions from the actual differential, not evaluations of a chosen coefficient instance.

## 1. Pinned inputs, notation, and conclusions

Let P=C[x0,...,x4], let S⊂P4 be the actual integral primary surface of degree 15, and let Z⊂S be its thirty reduced transverse double points. Set I=I_S and J=I_Z. Write ν:X→S for its smooth finite normalization.

The exact inputs are:

1. PR599, commit f8154d28e5c56ca96dc4e41cdf3097aaeba3b1a4, Sections 1–3 and 6: the actual primary resolution is

   0→P(-10) --c--> P(-7)^10 --L--> P(-6)^10 --f--> P→P/I→0.

   The cubic column c=(c1,...,c10)^t generates J as a homogeneous ideal; Lc=0. The linear map L has rank 9 on P4\S, rank 8 on S\Z, and rank 6 on Z. In particular, for x∉S its kernel is the one-dimensional space spanned by c(x).

2. PR600, commit 90f29113ae2d3a53cd8816ad7d32c96634be5b4a, Sections 2–3: the ten entries of c form a basis of J_3, and their images on S are the actual conductor ideal J/I, not an unrelated ten-dimensional linear system.

3. PR601, commit a582a76063b21fb4773d85d16fb39a3b54dee3bc, Sections 3–6: for

   π:M=Bl_Z P4→P4,
   b:Y=Bl_W X→X,  W=ν^(-1)(Z),

   the smooth surface Y is the strict transform of S in M; W consists of sixty reduced points. Let H=π*O_P4(1), E=Σ_(z∈Z)E_z be the ambient exceptional divisor, and E_Y=Σ_(w∈W)E_w. Then

   D=3H−E,
   D|Y=3b*ν*O_S(1)−E_Y,
   (D|Y)^2=75.

   The conductor sections generate D|Y. Each E_z≅P3 has normal bundle O_P3(-1), and Y∩E_z is two disjoint reduced lines.

4. PR574, commit 3c92fdc469f6870520e7a9d905b5ab9199a5bf37, Sections 1 and 3: X is a smooth connected projective surface with p_g(X)=h^0(X,K_X)=4. Its polarization satisfies (ν*O_S(1))^2=15. This positive geometric genus will exclude a covering family of lines; no exact classification of the lines on S is needed.

Exact source links:

- https://github.com/Akilleez-QA/read-em-and-weep/blob/f8154d28e5c56ca96dc4e41cdf3097aaeba3b1a4/research/hm/linear-adjugate/PROOF.md
- https://github.com/Akilleez-QA/read-em-and-weep/blob/90f29113ae2d3a53cd8816ad7d32c96634be5b4a/research/hm/primary-syzygy-geometry/PROOF.md
- https://github.com/Akilleez-QA/read-em-and-weep/blob/a582a76063b21fb4773d85d16fb39a3b54dee3bc/research/hm/conductor-blowup/PROOF.md
- https://github.com/Akilleez-QA/read-em-and-weep/blob/3c92fdc469f6870520e7a9d905b5ab9199a5bf37/research/hm/primary-conductor/PROOF.md

The globally generated bundle D defines a morphism Φ:M→P9. Give its image V=Φ(M) the reduced structure, and likewise let T=Φ(Y). The principal conclusions are:

**Theorem.**

(a) Φ:M→V is birational, V is a nondegenerate integral fourfold, and deg(V)=51.

(b) Φ|Y:Y→T is birational, T is a nondegenerate integral surface, and deg(T)=75.

(c) Writing the actual bilinear identity as B(y)x=L(x)y produces a 10×5 matrix B whose entries are linear forms in y. Its generic rank on both V and T is exactly four. On the rank-four locus its kernel defines a morphism to P4, agreeing with the ambient rational inverse and restricting to the rational inverse T⇢S. This map is given on suitable charts by signed 4×4 minors, homogeneous quartics. The assertion is a quartic presentation, not that the minimal inverse degree is exactly four.

(d) The curves contracted by Φ are exactly the strict transforms of lines containing three distinct points of Z. There are only finitely many such lines. The curves contracted by Φ|Y are exactly those among them that are contained in S.

The proof of (b) is separate from that of (a). Birationality of an ambient map is not treated as automatically implying birationality on a special surface.

## 2. Ambient resolution, positivity, and degree product

Since c generates J, pulling back O_P4^10→J(3) and then taking its image gives a surjection

                    O_M^10→O_M(3H−E).

Thus D is globally generated. Equivalently M is the graph blowup of this actual cubic system. Over P4\Z, Φ is the map x↦[c1(x):...:c10(x)].

The standard point-blowup intersections are H^4=1, H|E_z=0, and

   E_z^4=∫_(E_z)c1(O_(E_z)(E_z))^3
        =∫_(P3)c1(O_P3(-1))^3=−1.

Different E_z are disjoint, and every mixed intersection involving both a positive power of H and E_z vanishes. Consequently

                           D^4=3^4−30=51.                 (1)

If the image had dimension less than four, four general pulled-back hyperplanes would have zero intersection. Equation (1) therefore proves dim V=4 and generic finiteness, before any inverse construction is used. The projection formula gives

                     deg(Φ)·deg(V)=51.                   (2)

The ten cubics are linearly independent, so V is nondegenerate in P9. Also I_3=0 from the actual primary resolution, whose first equations have degree six. Thus their restrictions to S remain linearly independent, and T is nondegenerate. Input 3 similarly gives dim T=2 and

                     deg(Φ|Y)·deg(T)=75.                  (3)

Only the exact ideal-generation statement justifies resolution by the point blowup; equality of cubic dimensions alone would not suffice.

## 3. The bilinear incidence and ambient birationality

Choose coordinate vector x=(x0,...,x4)^t and target vector y=(y1,...,y10)^t. Because L has linear entries in x, there is a unique matrix B(y), with ten rows and five columns and entries linear in y, such that

                         B(y)x=L(x)y.                      (4)

This merely reorders the two factors in the actual bilinear map. We do not choose or evaluate coefficients of L. The identity L(x)c(x)=0 becomes

                         B(c(x))x=0.                       (5)

For a target point y define the projective linear subspace

                         Λ_y=P(ker B(y))⊂P4.               (6)

If x∉S, rank L(x)=9 and ker L(x)=C·c(x). Hence

   x∈Λ_y\S  ⇔ L(x)y=0  ⇔ [c(x)]=y.                       (7)

In particular the fiber of the rational cubic map outside S is exactly the open subset Λ_y\S, not merely a subset satisfying necessary linear syzygies. Additional quadratic syzygies of J do not change (7): rank nine already identifies the entire kernel of the actual L(x).

Choose a general y∈V outside Φ(Y) and Φ(E). Such a choice is possible since these closed images have dimensions at most two and three. The fiber is nonempty and consists of points lying over P4\S. By generic finiteness it has dimension zero. If Λ_y had positive dimension, its nonempty open subset Λ_y\S in (7) would be positive-dimensional, a contradiction. Thus Λ_y is a single reduced projective point and rank B(y)=4.

There is also a rational inverse, so no inference from point-counting in a possibly inseparable setting is needed. On the rank-four locus the one-dimensional kernel of B varies algebraically and gives a morphism

                       q:V°→P4,  q(y)=Λ_y,                (8)

where V°={y∈V:rank B(y)=4}. The identity (5) shows q(Φ(x))=x for general x∈P4. Conversely (7) shows Φ(q(y))=y for general y∈V. Hence Φ is birational, and (2) gives

                            deg V=51.                     (9)

For the explicit universal presentation, choose four rows of B that are independent at a generic point. Their 4×5 matrix has kernel vector whose five coordinates are its signed maximal minors. These are homogeneous quartics in y. All choices agree wherever both vectors are nonzero, since they give the same one-dimensional kernel. No claim is made that a prescribed row choice works before this generic-rank proof.

All 5×5 minors of B vanish on V: they vanish on the dense image of P4\Z by (5). Also the closed incidence relation B(y)x=0 holds on the whole graph M, by density and continuity. Consequently on Φ^(-1)(V°),

                            q∘Φ=π.                        (10)

The inverse in (8) maps to P4, not directly to the blowup M. Its rational lift to M is the actual inverse of the birational morphism Φ.

## 4. The finite-trisecant lemma

The following controls exactly why the ambient incidence argument needs an extra step on S.

**Lemma.** If Λ_y has positive dimension and meets P4\S, then Λ_y is a line containing exactly three distinct points of Z. In particular all such Λ_y belong to a fixed finite set of lines.

**Proof.** The complement Λ_y\S is a nonempty dense open subset of the irreducible linear space Λ_y. By (7), the restrictions of the cubics are proportional to y on that open subset. Choose an index j with y_j≠0 and put h=c_j|_(Λ_y)/y_j. Then h is a nonzero homogeneous cubic on Λ_y, and polynomial identity on the dense open subset gives

                           c_i|_(Λ_y)=y_i h                (11)

for every i, identically on Λ_y. Nonzeroness follows because the cubics do not vanish at points outside S.

Since J is generated by the c_i, the image ideal J·O_(Λ_y) is the principal ideal sheaf (h). It defines exactly the scheme-theoretic intersection Z×_(P4)Λ_y. This intersection is a closed subscheme of the reduced finite scheme Z, hence is itself a reduced union of points. Equivalently, at a contained node the ambient maximal ideal maps to the maximal ideal of Λ_y. We use the image ideal, not an assertion that the tensor product J⊗O_(Λ_y) injects into O_(Λ_y).

A nonzero cubic hypersurface in a positive-dimensional projective space is nonempty and has pure dimension dim Λ_y−1. Since its zero scheme is finite and reduced, necessarily dim Λ_y=1. On this projective line h has three simple zeros, so Λ_y contains exactly three distinct nodes. A line through two distinct points is unique; therefore only finitely many lines can contain three points of Z. ∎

For clarity, no line can contain four nodes: every c_i would restrict to a cubic with at least four distinct roots, hence vanish identically on that line, contradicting that their common base scheme is the finite scheme Z. Thus the trisecant conclusion does not hide a higher-multiplicity or a four-point case. We do not need to decide whether any such trisecants actually exist.

## 5. Positive geometric genus excludes a covering family of lines

**Lemma.** S contains only finitely many projective lines.

**Proof.** The Fano scheme of lines on S is projective of finite type. Suppose its reduced scheme had a positive-dimensional component. It would contain an integral projective curve parametrizing distinct lines. After normalizing this curve, the universal family is a smooth projective P1-bundle U→C.

Its image in S is closed and contains infinitely many distinct lines. It cannot be a curve: a one-dimensional closed subset of a Noetherian scheme has only finitely many irreducible components, and each contained projective line is such a component. Therefore U→S is dominant. Both schemes have dimension two, so it is generically finite. Since U is normal, this dominant morphism factors through the finite normalization X→S. The resulting generically finite morphism U→X is separable in characteristic zero.

Pullback of differential forms consequently gives an injection

                         H^0(X,K_X)→H^0(U,K_U).            (12)

But H^0(U,K_U)=0: restricting the canonical bundle to every P1 fiber gives O_P1(-2), so a global two-form restricts to zero as a section on every fiber and hence vanishes. This contradicts h^0(X,K_X)=4. Thus the reduced Fano scheme is zero-dimensional, and projectivity implies it has only finitely many closed points. Its possible nilpotent scheme structure does not create additional lines. ∎

This proof uses only the pinned positive geometric genus. It does not import an exact count of the actual lines, a description of Heisenberg eigenvectors, or a selected incidence calculation.

## 6. Surface birationality and degree 75

Choose a general point x∈S\Z avoiding both the finite set of lines contained in S from Section 5 and the finite set of node-trisecant lines from Section 4. This is possible because S is an integral surface and a finite union of curves is a proper closed subset. Put y=[c(x)]∈T.

By (5), x∈Λ_y. If Λ_y had positive dimension, there would be two possibilities:

- If Λ_y is not contained in S, Section 4 makes it one of the forbidden node-trisecant lines through x.
- If Λ_y is contained in S, it contains a projective line through x, contrary to the choice of x.

Both are impossible. Thus Λ_y={x} and rank B(y)=4. The rank-four locus therefore meets the dense image of S, and is dense open in the integral surface T. The inverse q of Section 3 restricts there to q(y)=x∈S, giving the rational inverse of the cubic map S⇢T. Since Y→S is birational, Φ|Y is birational as well. Equation (3) now yields

                             deg T=75.                    (13)

The same signed quartic-minor formulas give the inverse T⇢S on suitable nonempty open subsets. Their rational lift recovers Y. The crucial surface argument is the finite-trisecant/non-uniruledness argument; ambient birationality alone was not used to cancel the degree in (3).

## 7. Next consequence: all contracted curves are node trisecants

The point-blowup system satisfies

                            D|E_z=O_P3(1).                 (14)

Therefore Φ maps each E_z by a complete linear embedding into P9: the restricted sections generate O_P3(1), so their linear span is all its four-dimensional section space. In particular no curve inside an exceptional divisor is contracted.

Let C⊂M be an integral curve contracted to y. Its image Γ=π(C) is a curve, since a curve mapped to a point by π would lie in some E_z and contradict (14). By the incidence identity on M, Γ⊂Λ_y.

If Λ_y is not contained in S, it meets P4\S, and Section 4 says Λ_y is a node-trisecant line. Hence Γ=Λ_y. If Λ_y is contained in S, it has dimension at most one: a linear subspace of dimension at least two contained in the integral surface S would be a plane equal to S, contrary to deg S=15. Thus here too Γ=Λ_y is a line.

In the second case the actual constancy of Φ on C, not merely the linear relation L(x)y=0 on S, implies that c|Γ is a scalar cubic times y on Γ\Z. Repeating the principal-ideal argument of (11) proves that Γ contains exactly three distinct nodes. Since π is an isomorphism off Z and C dominates Γ, C is the strict transform of Γ.

Conversely, let ℓ be a line containing three distinct nodes. There are no further nodes on ℓ. Its strict transform is isomorphic to ℓ, since blowing up the reduced point ideal on a smooth curve blows up an invertible ideal. The restriction of the ambient exceptional divisor has degree three, one at each node. Hence

                         D·ℓ_tilde=3−3=0.                 (15)

A globally generated line bundle of degree zero on P1 is trivial; its associated map is constant. Thus ℓ_tilde is contracted. This proves (d), including finiteness.

Because Y is the closed strict transform of S, it contains ℓ_tilde exactly when S contains ℓ. Consequently Φ|Y contracts precisely the node-trisecant lines contained in S. This characterizes the possible contraction locus without asserting its existence or absence. In particular the next finiteness question is reduced to the exact incidence condition: does any line on S contain three nodes? Normality of either image and separation of any remaining finite fibers are separate questions.

## 8. Contribution and limits

The exact linear primary syzygy now supplies a rational inverse for the actual ten-cubic map. Its ambient degree is one and its fourfold image has degree 51. The conductor restriction is also degree one and has degree-75 image, by a separate geometric argument that rules out a generic rank-drop locus without any matrix evaluation. The quartic inverse presentation and the characterization of contracted curves are further exact consequences.

The proof does not claim the images are normal, that either morphism is an embedding, that all finite special fibers are singletons, that trisecants exist or are absent, or that the inverse's minimal degree is exactly four. It does not settle the distinct primitive-four/full-adjoint gate, prescribed-source membership, higher lifting, or algebraicity of the original deformation problem. These conclusions concern the actual primary/node/conductor system and its own resolved cubic map only.
