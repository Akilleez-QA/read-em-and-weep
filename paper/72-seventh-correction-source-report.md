# The actual seventh correction absorbs secondary torsion

**Craig Ward · 23 October 2026 · Source report on PR1026**

This chapter reports mr. slop's [full immutable proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/a97fbc0084d08da8ab362589e658082f3fcc0f52/research/hm/seventh-secondary-repair/PROOF.md), not an independent reproof. All neighborhoods are ordinary Cartier neighborhoods mR **inside a hyperplane**, not ambient codimension-two thickenings.

## 1. Actual finite-neighborhood presentation

The fifth even derived cohomology is [K→U], with K=T₆O(-1)⊕AO(-2), U=(A+V+P+D)O(4), square subbundle L=AO(-6), and Q=K/L=PO(2)⊕WO(-1). Write C₅=coker β and J=(V+P+D)O(6).

The actual sixth-normal layer gives an equivariant lift γ:K→J and the seventh presentation

    Rq_*E₇=[K→U⊕J],   differential (β,γ).

Its ambiguity is precisely γ↦γ+hβ for h:U→J. The argument uses Ext¹_G(U,J)=0 to represent the actual derived extension, not to split the geometric thickening extension.

Uniform exhaustion by the three actual global squares and derived base change imply that (β,γ) has the square bundle as its full fiberwise kernel. Hence the induced Q→U⊕J is fiberwise injective. Its cokernel H₇=R¹q_*E₇ is a vector bundle of rank 21 and degree 126.

## 2. Canonical correction and forced elementary modifications

Let N=ker(b:Q→U) and let r be the generic secondary rank. Restriction of γ gives a canonical fiberwise injection δ:N→J, independent of the lift ambiguity. Its cokernel M is a vector bundle of rank 6+r, and there is an actual exact sequence

    0→M→H₇→C₅→0.

If τ is the torsion of C₅, its inverse image is the saturation M^sat in H₇:

    0→M→M^sat→τ→0,
    0→M^sat→H₇→C₅/τ→0.

The earlier theorem permits τ=0 or twelve simple factors. In the latter case every local inclusion M→M^sat has Smith form diag(t,1,…,1), and degree increases by 12. Each elementary modification is necessarily nonsplit, since a free module cannot contain a nonzero torsion direct summand.

This **does not force τ=0**. C₅ is a quotient of the torsion-free H₇, not a subsheaf of it, so torsion is allowed and absorbed by the extension.

## 3. Why exceptional fifth sections disappear

At a parameter x, base change gives

    0→(ker β)⊗k(x)→H⁰(E₅|x)→Tor₁(C₅,k(x))→0.

The extra one-dimensional section at a torsion point is not a fiber of the kernel sheaf. The actual sixth-normal boundary induces an injection of this Tor term into M⊗k(x). Thus these extra sections are killed at seventh order. Its fiber rank is 6−r away from the orbit and 7−r at its points when torsion is present, while the sheaf map δ has constant rank 6−r. The distinct domains explain the difference.

The next even layer gives the further actual quotient

    0→(ker Θ)*O(8)→H₇→AO(8)→0,

with kernel rank 18 and degree 102. Θ is the already established ninth-neighborhood rank 12 map. No splitting of this sequence is asserted.

## 4. Scope

This is a finite-neighborhood completion of the secondary map and a constraint on its actual extension classes. It selects neither secondary rank nor coefficients nor the torsion alternative. It does not identify global H¹, resolve the global odd-quadric problem, determine the opposite top/vertex scalars or remove a source pair. The source reports authenticated inputs, independent whole-proof review and ordinary/optimized checks; those reports are retained as attribution, not counted as a new independent reproof here.
