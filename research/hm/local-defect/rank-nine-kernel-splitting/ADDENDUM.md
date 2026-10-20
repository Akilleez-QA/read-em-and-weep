> Publication scope: preserved mathematical proof/audit. Historical statements that rank eight remains open are superseded only after the final assembly and all its prerequisites. No source-instance evaluation or formal verification is claimed here.

# Rank nine forces a codimension-two saturation defect of degree at least 21

Assume generic rank(Q)=9 and retain the notation of PROOF.md. Write G=im b, F for its saturation in J⊗O, T=F/G, and R=(J⊗O)/F. Then

    degree([T]₂) ≥ 21.

Here [T]₂ is the effective codimension-two cycle obtained by weighting each codimension-two component of supp T by the length of T at its generic point. In particular G≠F, and a codimension-two saturation defect is unavoidable. This does not determine the actual defect cycle.

## 1. Chern classes

The proven resolution is

    0 → O(-3)⊕O(-8) → O(-1)^15 → G → 0.

With h the hyperplane class, its Chern character through degree two is

    ch(G)=13−4h−29h²+… .

Thus c₁(G)=−4h and c₂(G)=37h². Since d=0, T is supported in codimension at least two. Put [T]₂=a h², with a≥0. The leading-term formula for the Chern character of a torsion sheaf gives ch₂(T)=[T]₂. Additivity in

    0 → G → F → T → 0

therefore yields

    c₁(F)=−4h,  c₂(F)=(37−a)h².

The quotient R is globally generated and torsion-free of rank seven, by the definition of saturation. From 0→F→O^20→R→0 we obtain

    c₁(R)=4h,  c₂(R)=(a−21)h².

These are Chern classes of coherent sheaves in the K-theory of the smooth ambient projective space; local freeness of G, F, or R everywhere is not assumed.

## 2. Positivity for a globally generated torsion-free sheaf

Let M be a globally generated torsion-free sheaf of rank s on a smooth projective variety X. Its second Chern class is represented by an effective codimension-two cycle.

Choose s−1 sufficiently general global sections. On the locally free locus of M, the incidence condition that their rank be at most s−2 has codimension two: the corresponding determinantal locus of s-by-(s−1) matrices has codimension two, and evaluation is surjective at every point. The incidence dimension estimate thus shows that general sections have no divisorial rank-drop locus. Since M is torsion-free, its non-locally-free locus also has codimension at least two. We obtain an injection

    0 → O^(s−1) → M → N → 0,

with N rank one and locally free at all codimension-one points. Generic injectivity implies sheaf injectivity because the source is torsion-free.

At a codimension-two point, the local ring is regular of dimension two. The source has depth two, and the torsion-free module M has depth at least one. The depth lemma therefore gives depth N≥1. Thus N has no torsion supported at the generic point of a codimension-two subvariety. Its local freeness at codimension-one points also excludes divisorial torsion. The torsion subsheaf of N is consequently supported in codimension at least three.

Remove that support and call the remaining open set X₀. On X₀, N is torsion-free of rank one; hence its double dual is a line bundle, necessarily det M. It follows that

    N|X₀ ≅ I_Z⊗det M

for a closed subscheme Z⊂X₀ of codimension at least two. The exact sequence gives

    c₂(M)|X₀ = c₂(N|X₀) = [Z]₂,

where [Z]₂ is the effective codimension-two fundamental cycle. The last equality follows also from ch(I_Z)=1−ch(O_Z): the leading component of ch(O_Z) is its effective codimension-two cycle.

Removing a codimension-at-least-three closed set does not change the Chow group in codimension two, by the localization sequence. Taking closures of the components of [Z]₂ therefore represents c₂(M) on X by an effective cycle. This argument does not require M to be reflexive or locally free in codimension two. When s=1, use the empty list of sections and the same rank-one argument.

## 3. Application

Apply this lemma with M=R on P⁴. Since

    c₂(R)=(a−21)h²,

effectivity implies a−21≥0. Hence a≥21. In particular T is nonzero and has a codimension-two component.

## 4. Scope

The conclusion is a new necessary condition for generic rank nine: the actual image cannot equal its saturation, and the codimension-two part of their discrepancy has degree at least 21. It does not exclude rank nine, identify the supporting surfaces, or calculate their individual multiplicities. No actual operation value, source matrix, rank instance, polynomial instance, input, jet, or residue has been evaluated.
