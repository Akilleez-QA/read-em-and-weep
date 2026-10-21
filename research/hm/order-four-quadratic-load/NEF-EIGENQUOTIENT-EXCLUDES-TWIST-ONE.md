# Nef eigenquotient positivity excludes twist one entirely

## Hypotheses

Let Q⊂P4 be a smooth quadric meeting the 25 transverse HM evaluation-degeneracy lines C transversely. Put V=F|Q and E=V(3). The actual four-dimensional space U=H0(F(3)) evaluates with rank two away from Z=C∩Q and rank one at each of its fifty points. The Chern classes are c1(E)=5H and c2(E)=10H², with ∫_Q H³=2.

No selected coefficients, ranks, or numerical evaluations are used. The rank statement is the established global evaluation geometry, restricted transversely.

## 1. A nef line bundle with finite base locus

Use the quotient convention X=P_Q(E), with projection π and tautological quotient π*E→O_X(1). Write L=c1(O_X(1)), and also H for π*H.

The U subsystem of H0(X,O_X(1)) has no base point over Q\Z, because evaluation there spans E. Over z∈Z, its image in E_z is one-dimensional. Exactly one quotient E_z→one-dimensional space annihilates that image. Therefore the base locus of this subsystem has finite underlying support, one point over each z.

It follows that L is nef. For any integral projective curve Γ⊂X, the curve is not contained in this finite base support. A section in U nonzero at some point of Γ restricts to a nonzero section of O_X(1)|Γ. Pulling to the normalization shows deg(L|Γ)≥0. This argument does not assert global generation, and does not require the base scheme itself to be reduced.

## 2. The actual eigenquotient divisor

Let 0≠ψ:V→V(k) be trace-free. Twisting gives ψ:E→E(k). The universal quotient sequence on X has line kernel

0→K→π*E→O_X(1)→0,
K=π*det(E)⊗O_X(-1).

Compose K→π*E with π*ψ and then the quotient π*E(k)→O_X(1)⊗π*O_Q(k). This is a global section of

Hom(K,O_X(1)⊗π*O_Q(k))=O_X(2)⊗π*O_Q(k-5).

It is not the zero section. If it vanished identically, every one-dimensional kernel of a quotient of E at the generic point would be ψ-invariant, forcing ψ to be scalar over K(Q). Trace zero in characteristic zero then forces ψ=0, contradiction.

Its zero scheme is thus an effective Cartier divisor T_ψ on the smooth integral fourfold X, of class

[T_ψ]=2L+(k-5)H.

The divisor is nonempty: on each generic fiber P1, the equation has degree two. Its points parametrize quotient lines whose kernels are invariant under ψ, explaining the eigenquotient terminology. No assertion of smoothness, reducedness, or irreducibility is required for the positivity argument.

## 3. The decisive intersection

The projective-bundle relation is

L²-5HL+10H²=0.

Consequently

π_*(L³)=c1(E)²-c2(E)=15H²,
π_*(L⁴)=c1(E)³-2c1(E)c2(E)=25H³.

It follows that

∫_X L³[T_ψ]
=∫_Q (50+15(k-5))H³
=30k-50.

A nef line bundle has nonnegative top self-intersection on every effective divisor: restrict to each integral divisor component and use nef intersection positivity, or take the limit of ample classes L+εA. Therefore 30k-50≥0. Since k is integral,

k≥2.

In particular H0(Q,End_0(V)(1))=0. This excludes the entire twist-one spectral branch, including its rank-two and rank-three pencil alternatives, without a classification of singular covers or rank-one MCM sheaves.

## 4. Consequences and limits

After dividing the maximal scalar divisor from a nonzero original twist-four kernel section φ, its primitive twist must now be k∈{2,3,4}. The scalar divisor has degree at most two, improving the previous bound of three. The conditional finite primitive-zero lengths are76,144,248 respectively.

For k=2,3,4 the nef eigenquotient intersections are10,40,70, which are nonnegative. This proof does not exclude those twists or establish nondegeneracy of the original twenty-dimensional boundary. The fifty-point boundary and prior spectral reductions remain applicable.

Inputs: actual transverse evaluation geometry and exterior-symmetric resolution in PR538 at d5d9bd997145b0ecf7d7bd659a19fb7845afb75f; common quadratic open at14f4154ce6657e791a5e0fcdd9fdb67f9014712f. The proof uses only this geometry, the quotient projective-bundle formula, and nef intersection positivity.
