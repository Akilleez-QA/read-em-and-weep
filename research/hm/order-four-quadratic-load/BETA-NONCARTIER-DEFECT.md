# A quantitative non-Cartier defect for moving beta sextics

## Statement

Let D be a general member of an r-dimensional family of distinct integral residual beta sextics on a fixed X=X_B. Work on a neighborhood of D where B has rank one; activity at Z and the beta description away from Z guarantee such a neighborhood. Then X is a Gorenstein lci surface there, ω_X|D≅O_D(Z), and deg ω_X|D=25. D is integral Cohen–Macaulay with p_a(D)=3, but need not be Gorenstein or smooth.

There is a canonical exact sequence of coherent sheaves on D

0 → ω_D⊗(ω_X|D)^−1 → N_{D/X} → F_D → 0,

where N_{D/X}=Hom_X(I_D,O_D) is rank-one torsion-free, and F_D has finite length and is supported on the non-Cartier locus of D in X. This locus is away from Z. Write e(D)=length F_D. Then

deg N_{D/X}=e(D)−21.

A moving family forces the following bounds:

- r≥1 implies e(D)≥21;
- r≥2 implies e(D)≥23;
- r≥3 implies e(D)≥25;
- r≥4 implies e(D)≥27.

In particular, after the beta-image dimension drop to at most two, a general surviving fixed-B fiber has dimension at least two and requires e(D)≥23.

## 1. Why the generic Cartier hypothesis is available

The sextic-containing integral component S of X has degree ten or fifteen and multiplicity one, by BETA-DEGENERACY-SURFACE.md. Thus X is reduced and smooth on a dense open of S. The singular locus meets S in a proper closed set, with only finitely many curve components. A positive-dimensional family of distinct integral curves on S cannot have its general member contained in that fixed locus. Hence the generic point of a general D is a smooth point of X.

Accordingly I=I_{D/X} is invertible except at finitely many points: away from D it equals O_X; at the generic point of D, X is regular. This assertion requires neither normality nor irreducibility of all of X. We use only the multiplicity-one component containing the moving curves and the locally Cohen–Macaulay property.

## 2. End(I)=O_X and the canonical injection

Locally I contains a nonzerodivisor: D has codimension one and contains no component of the pure Cohen–Macaulay surface. An endomorphism of I is therefore multiplication by an element of the total quotient ring. Indeed for a regular element t∈I and any a∈I, tφ(a)=aφ(t), so the multiplier is φ(t)/t.

Because I is invertible off a finite set, that multiplier is regular off this finite set. The S2 extension property for the Cohen–Macaulay surface extends it across that codimension-two set. Consequently End_X(I)=O_X. One can equivalently apply the local-cohomology depth≥2 exact sequence O_X→j_*O_{X\finite} to obtain this equality. The argument does not assume that X is normal.

Apply sheaf Hom_X(I,−) to 0→I→O_X→O_D→0. Its initial exact segment is

0→End_X(I)→I*→Hom_X(I,O_D)→Ext¹_X(I,I).

On the other hand, apply Hom_X(−,O_X) to the same short exact sequence. Hom_X(O_D,O_X)=0, since I contains a nonzerodivisor, and hence

I*/O_X ≅ Ext¹_X(O_D,O_X)
          ≅ ω_D⊗(ω_X|D)^−1.

The last identification is codimension-one duality for a Cohen–Macaulay curve in a Gorenstein surface. It does not require ω_D to be invertible. Combining the two sequences and End(I)=O_X gives the claimed injection into N_{D/X}.

At every Cartier point the injection is the standard isomorphism ω_D⊗ω_X^−1≅O_D(D)=N_{D/X}. Thus its cokernel F_D is supported on the finite non-Cartier locus. Both source and target have rank one. N_{D/X} is torsion-free as an O_D-module, since locally it embeds in a finite direct sum of copies of the domain O_D by evaluating a homomorphism on generators of I.

At active p∈Z, the fourth section cuts the smooth curve C as a Cartier divisor in X, which forces X to be regular at p. Therefore D is Cartier there. In particular F_D is supported away from Z.

## 3. Degree and deformation dimension

For a rank-one torsion-free sheaf M on D, define deg M=χ(M)−χ(O_D). Duality gives deg ω_D=2p_a(D)−2=4. Twisting by the inverse of ω_X|D subtracts 25, giving degree −21. Additivity in the finite-length exact sequence proves deg N=e(D)−21.

The tangent space of the Hilbert scheme of X at D is H0(N). An r-dimensional family of distinct D has r-dimensional image in that Hilbert scheme, so h0(N)≥r at a general member. A nonzero section O_D→N is injective, with finite-length cokernel, and already implies deg N≥0, hence e(D)≥21.

## 4. Genus-three improvement without Gorensteinness

Set a=h0(N) and b=h1(N). Serre duality identifies b with dim Hom_D(N,ω_D). If b>0, the multiplication/evaluation pairing

H0(N)⊗Hom_D(N,ω_D)→H0(ω_D)

has no zero divisors: a nonzero section and a nonzero homomorphism are both nonzero at the generic point of the integral curve. The elementary Hopf dimension lemma therefore gives a+b−1≤h0(ω_D)=3. To recall its proof, the projectivized kernel of a bilinear map with no zero divisors misses the Segre variety P^{a−1}×P^{b−1}; the projective dimension inequality forces the image dimension to be at least a+b−1.

Riemann–Roch says a−b=deg N−2. If b>0, combining these statements gives deg N≥2a−2. If b=0, Riemann–Roch instead gives deg N=a+2. Therefore a≥2 forces deg N≥2; a≥3 forces deg N≥4. If a≥4, b>0 is impossible because a+b≤4, so deg N≥6. Adding 21 proves the stated thresholds 23,25,27.

## Boundary

The defect is explicitly length coker[Ext¹_X(O_D,O_X)→Hom_X(I_D,O_D)]. It is not asserted equal to a familiar singularity invariant, nor bounded above here. Its support is contained in the non-Cartier locus; no assertion that every non-Cartier point contributes positively is needed. The result gives a necessary obstruction budget for exceptional singular surfaces, not their exclusion. No coefficient evaluation, matrix-rank computation, scan, or prohibited experiment is used.
