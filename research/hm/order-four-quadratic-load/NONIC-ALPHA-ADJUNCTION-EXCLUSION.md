# Canonical adjunction excludes an actual nonic alpha differential symbol

## New conclusion

Let D⊂P3 be the integral (3,3) complete-intersection carrier in the actual two-cubic HM branch, and let Z be its 25 reduced smooth marked points. Suppose an actual fixed-point differential tuple of a cubic generator is nonzero and of alpha type, with center p∈D outside Z. This is impossible.

The key additional input, not present for an arbitrary compatible tuple in H0(O_D(4)(−Z)), is that an actual tuple has the form x∧y with all four components of y global cubic sections on D. Complete-intersection adjunction identifies O_D(2) with ω_D. The absence of a single-pole canonical section then forces the alpha tuple to vanish.

The pinned compatible-defect theorem 277400cb97e3308a15c1f45e7e98a970c1e3a034 and universal-pencil Chern obstruction 442704f478661c35f6dbe001065f6db4aa9e356c have reduced every possible nonzero actual symbol to precisely this alpha alternative. Therefore the generic marked nonic branch is excluded. No statement about the b=0 or b=1 branches or full Q4 follows.

## 1. Inputs and fixed-fiber notation

The integral complete intersection D of two cubics has degree nine, arithmetic genus ten, and invertible dualizing sheaf

ω_D≅O_D(2).

Put H=O_D(1). In the actual b=2 branch, the two-dimensional cubic space through Z is exactly H0(I_D(3)). As D is ACM, restriction in degree three is surjective and the exact sequence yields

H0(O_D(3)(−Z))=0.                                  (1)

The alpha-center analysis in NONIC-COMPATIBLE-DEFECT-CONSTRAINTS.md supplies a canonical center p∈D outside Z for the nonzero actual symbol, after shrinking the hyperplane parameter space. It does not assert p is smooth; none is required here.

On the usual chart H_t: X4=Σ t_i X_i, let G(t,x) be a local algebraic cubic generator and fix a general parameter t. Set

y_i=(∂_(t_i)G)|D∈H0(O_D(3)).

Its actual fixed-point differential tuple is

P_ij=x_i y_j−x_j y_i∈H0(O_D(4)).                    (2)

Every P_ij vanishes on Z. Alpha type means that, at the generic point of D, the bivector P=x∧y is proportional to x∧p. Choose constant projective coordinates at this fixed parameter with p=[1:0:0:0]. Then

x_j y_k−x_k y_j=0  for 1≤j,k≤3.                   (3)

There is no assumption that the center is constant as the parameter varies. This coordinate choice and all subsequent arguments take place on a single general fiber.

## 2. A duality lemma, including singular points

For every closed point p of an integral projective Gorenstein curve D, the restriction map

H0(ω_D)=Hom(O_D,ω_D) → Hom(I_p,ω_D)

is an isomorphism.

Indeed apply Hom(−,ω_D) to 0→I_p→O_D→k_p→0. Since ω_D is torsion-free, Hom(k_p,ω_D)=0. The relevant part of the global Ext sequence is

0→H0(ω_D)→Hom(I_p,ω_D)→Ext^1(k_p,ω_D)→H1(ω_D).

Serre duality identifies the dual of the last arrow with the restriction of constants H0(O_D)→H0(k_p). Since D is integral and projective over C, both spaces are C and this restriction is an isomorphism. Thus the last arrow is an isomorphism, proving the claim.

Equivalently, a homomorphism from the point ideal to the canonical sheaf cannot acquire one extra global section by allowing a single point of poles. This exact duality argument applies at singular p as well; it does not replace I_p by an unjustified invertible O_D(−p).

## 3. The alpha relations produce a canonical-sheaf homomorphism

The three coordinates x1,x2,x3 generate I_p⊗H on D. Relations (3) say that their assigned values y1,y2,y3 are proportional to them at the generic point. Consequently sending x_j to y_j defines a sheaf homomorphism

I_p⊗H → O_D(3).

To check all sheaf relations, not just the pairwise ones, choose a common rational proportionality factor at the generic point. Any relation among the x_j then gives zero generically among the y_j; its image is a section of torsion-free O_D(3), so it vanishes everywhere. The map is therefore well-defined even at singular p.

After tensoring by H^-1, this is a homomorphism

I_p→O_D(2)=ω_D.

By Section 2 it extends to O_D→ω_D. Thus there is a global q∈H0(O_D(2)) such that

y_j=x_j q  for j=1,2,3.                            (4)

No projective normality or polynomial lift of q is needed for this step, though the ACM hypothesis would also provide such a lift.

## 4. The remaining cubic section vanishes on Z

Set

s=y_0−x_0 q∈H0(O_D(3)).

Equations (2) and (4) give P_0j=−x_j s for j=1,2,3. At each marked point z∈Z, the tuple P vanishes. Since p is outside Z, at least one of x1,x2,x3 is nonzero at z. It follows that s vanishes at z. The marked scheme is reduced, so s vanishes on Z scheme-theoretically.

By (1), s=0. Combining this with (4), all four y_i equal x_i q. Hence x∧y=0 and every P_ij is zero, contrary to the assumed nonzero alpha symbol.

This is the contradiction.

## 5. Why this closes the actual alpha case but not arbitrary compatible sections

The earlier alpha-center analysis permits abstract compatible tuples in H0(M), M=4H−Z, arising from Hom(I_p,3H−Z). Such a tuple need not lift to four global cubic sections y_i with P=x∧y. The present argument uses precisely that extra property of an actual parameter derivative.

It also does not infer that the kernel cubic lifts to an ambient cubic. No integrability of a moving kernel basis and no ambient hypersurface descent are needed: canonical adjunction and the actual polynomial-derivative representation already force each alpha symbol to vanish on the carrier.

For clarity, the complete implication uses both pinned inputs as follows. The universal-pencil Chern theorem at 442704f478661c35f6dbe001065f6db4aa9e356c proves h0(M)≤4: multiplication of four independent linear sections with a partner of dimension at least three would require at least eight products, but the adjoint target has only seven sections. Its constant-rank pencil bundle on P2 gives the contradiction, and is valid for singular D. The compatible-defect theorem at 277400cb97e3308a15c1f45e7e98a970c1e3a034 then excludes nonzero spans one, two, and four; any nonzero symbol is alpha span three, with its uniquely determined center generically outside Z. Thus Section 4 forces both cubic symbols to vanish.

Finally the complete-intersection ideal is generated by the two cubics. Vanishing of their fixed-point differential quartics on D means those quartics belong to I_D(4), hence the fixed-ambient-point derivations preserve the universal curve ideal. The degree-four multiplication image has constant rank eight: the two cubics have no linear syzygy. Local bundle splittings make this preservation an algebraic family statement. The five-dimensional integral incidence has three independent fixed-point tangent directions, so its ambient image has dimension at most two, and at least two because point/hyperplane incidence fibers have dimension at most three. Its closure equals the full incidence of the resulting integral surface S. Thus a general hyperplane section of S is D and deg S=9. The entire construction is intrinsic and Heisenberg-equivariant, so S is invariant. The central-character Hilbert-polynomial argument forces invariant integral surface degrees to be divisible by five, contradicting nine.

This excludes the nonic branch without silently importing an incomplete four-span bound as a five/six-span theorem.

## Provenance and boundary

Read NONIC-COMPATIBLE-DEFECT-CONSTRAINTS.md, NONIC-FIVE-SIX-SECTION-EXCLUSION.md, and the existing two-cubic carrier classification before completing this proof. The new ingredient is the canonical-extension obstruction for an actual x∧y differential tuple. The center may be singular, and its absence from Z is explicitly used. No actual source coefficients, selected ranks, parameter scans, local-model spike, consumed experiment, or external writes were used.
