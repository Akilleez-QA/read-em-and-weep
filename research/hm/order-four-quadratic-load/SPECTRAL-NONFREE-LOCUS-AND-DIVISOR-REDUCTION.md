# The exact nonfree spectral locus and removal of scalar divisors

Let Q be a smooth complex quadric threefold and V=F|Q with detV=O_Q(-1), c2(V)=4H² and H0(V(2))=0. Let 0≠φ∈H0(End_0(V)(4)) be an actual remaining quadratic kernel section. The preceding no-rank-one lemma shows that its spectral cover Y is integral. All constructions here retain V itself, rather than replacing it with an arbitrary rank-two bundle or abstract module.

## 1. The nonfree locus is exactly the zero scheme of φ

Locally trivialize V and O_Q(4), and write

φ=[[a,b],[c,-a]],  f=a²+bc,
Y: λ²=f.

The spectral sheaf M has the presentation coker(λI−φ) over the total space of O_Q(4). Indeed polynomial division by the monic λI−φ identifies its underlying module over Q with V, with λ acting as φ. Its matrix factorization companion is λI+φ, whose composite is (λ²−f)I.

At a point of Y with φ nonzero on the residue field, λI−φ has rank one. It cannot have rank zero: that would imply φ=λI and trace φ=0, hence λ=0 and φ=0. A unit entry allows row and column elimination, leaving diag(1,λ²−f) up to units. Its cokernel is therefore free of rank one over O_Y.

At a point with φ=0, λ=0 as well. The presented module has two minimal generators there, so is not free of rank one. Scheme-theoretically its first Fitting ideal is

Fitt_1(M)=(λ-a,λ+a,b,c)=(λ,a,b,c).

Consequently the nonfree Fitting subscheme of M is canonically isomorphic to the zero scheme of φ on Q, via its embedding at λ=0. This statement includes nonreduced zero schemes, not merely their supports.

M is maximal Cohen–Macaulay and generically rank one. If Y is normal it is thus reflexive. Every zero of φ is then a non-Cartier locus of the rank-one divisor class represented by M. In particular a normal locally factorial spectral cover is impossible, because every rank-one reflexive sheaf on such a variety is invertible, whereas φ has a forced zero. More locally, Y cannot be locally factorial at any zero of φ.

If φ has a divisorial zero, Y is singular along a divisor: the local determinant has order at least two there and λ=0 is the ramification point. Since Y is a hypersurface and hence Cohen–Macaulay, this violates the regular-in-codimension-one requirement for normality. Thus normal Y forbids divisorial zeros, although the converse is not asserted.

## 2. Exhaustive scalar-divisor reduction

The common codimension-one zero orders of φ define a unique maximal effective divisor D. Smoothness and Pic(Q)=Z identify D with the divisor of a section s∈H0O_Q(d), d≥0. Divide to obtain

φ=sψ,  ψ∈H0(End_0(V)(k)),  k=4-d,

where ψ has no divisorial zero.

The vanishing H0(V(2))=0 implies that every saturated line subsheaf of V is O(a) with a≤-3. In particular V is slope-stable, because a<μ(V)=-1/2. Stability gives Hom(V,V(k))=0 for k<0 and Hom(V,V)=C·id for k=0. Its trace-free part at k=0 is zero in characteristic zero. Therefore k≥1, or

0≤d≤3,  k∈{1,2,3,4}.

This is all that the stated vanishing proves about the lower twist. In particular it does NOT prove H0(End_0(V)(1)), H0(End_0(V)(2)), or H0(End_0(V)(3)) vanish.

The no-rank-one proof applies equally to every k≤4: kernel O(a) and saturated image O(b+k), with a,b≤-3, would force a nonzero section of O(a+b+k+1), whose degree is at most k-5<0. Consequently every nonzero ψ here has irreducible quadratic characteristic polynomial over K(Q).

Let Y' be its integral spectral cover in Tot O_Q(k), with coordinate μ. Multiplication λ=sμ defines a finite birational map ν:Y'→Y. Finiteness follows either from the integral equation for μ, or because the target and source are both finite over Q and the source algebra is finite as an O_Q-module. It is an isomorphism away D. If d>0 it is a partial normalization; when Y' is normal it is the normalization. No assertion that Y' is normal is made.

The action of ψ on V gives its spectral sheaf M' on Y'. Since φ=sψ, the original module action is restriction along O_Y→ν_*O_Y'. Thus

M=ν_*M',  π'_*M'=V.

Scalar divisor removal preserves the exact underlying HM restriction and its spectral obstruction, not merely the characteristic polynomial.

## 3. Smaller primitive zero budgets

For E_k=End_0(V)(k), the Chern roots give

c3(E_k)=k(k²+15)H³,
∫_Q c3(E_k)=2k(k²+15).

For k=1,2,3,4 these degrees are32,76,144,248. They are positive, so every primitive ψ still vanishes somewhere. Its zero scheme has codimension at least two by construction. If finite, the three component equations form a regular sequence and its length is the indicated degree. If it contains curves, these numbers are not asserted to be lengths or numbers of points.

Thus an actual obstruction reduces to one of four positive twists, an integral spectral cover with a nonempty codimension-at-least-two nonfree locus, and its rank-one MCM sheaf pushing forward to exactly V. A normal surviving cover must fail local factoriality at that locus. These necessary conditions do not exclude the remaining primitive cases.

Inputs are the actual common-open restriction construction in QUADRIC-FIFTY-POINT-BOUNDARY.md and the Chern/no-rank-one calculations in SINGULAR-SPECTRAL-COVER-NECESSITY.md. No selected HM coefficients, matrices, rank samples, or external writes were used.
