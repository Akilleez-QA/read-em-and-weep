> Publication scope: Operational cubic Chern relation and Picard rank obstruction on nilpotent/spectral components; no actual occurrence asserted. Historical statements about unresolved mixed classes refer to the source stage; this packet does not supersede the separately stated conditional mixed-vanishing result in PR145.

# A cubic Chern identity and a Picard obstruction for extremal components

## Results

Under the hypotheses and proved conclusions of `../spectral-nef-boundary-bound/PROOF.md`, over C:

1. On the reduced global nilpotent incidence N, with the flag notation below,

       t(h^2 - 2ht + 3t^2) = 0

   as a rational operational Chow class.
2. On every integral three-dimensional closed subvariety Z of N, h and t are linearly independent in N^1(Z)_R. In particular rho(Z) >= 2.
3. If Y is an integral four-dimensional component of the projective spectral incidence X, the restrictions to every three-dimensional component Z of its nilpotent boundary of the two global classes r=c1(O_P(E)(1)) and H=p*c1(O_G(1)) are linearly independent. In particular rho(Y) >= 2. More strongly, the image of N^1(Y)_R -> N^1(Z)_R has dimension at least two.

These are constraints, not an improvement of dim N <= 3 or dim X <= 4. No example-specific operation, matrix, rank, selected input, jet, residue, or source-model computation is used. Only local proof files are written.

## 1. Bundles and the new cubic relation

On N, identified with the reduced quadratic flag incidence, the recovered rank-three subbundle W of V tensor O has a filtration with line quotients

       L, M, M^2 tensor L^(-1).

Put h=c1(L*) and t=c1(M*). The imported flag argument proves that h,t are nef and 2h+t is ample. It also proves det W=M^3, so the recovered-three-plane map g:N -> Gr(3,V) satisfies

       g*c1(O_Gr(3,V)(1))=3t.

The formal Chern roots of W are -h,-t,h-2t. Therefore those of W* are h,t,2t-h. Since Q=(V tensor O)/W has rank two, c3(Q)=0. Expanding c(Q)=c(W)^(-1) yields

       c1(Q)=3t,
       c2(Q)=h^2-2ht+7t^2,
       c3(Q)=5h^2t-10ht^2+15t^3.

Consequently the stated rational cubic relation holds. This uses the recovered W; it is distinct from the earlier degree-four projective-bundle relation. The relation is valid on a singular reduced base via operational Chern classes.

## 2. Numerical independence on a nilpotent threefold

Let Z be an integral projective threefold in N. First t cannot be numerically zero on Z. Indeed if t were numerically zero, the morphism g|Z would be constant: a nonconstant projective morphism has a curve mapping nontrivially to its image, on which the pullback of an ample bundle has positive degree. A fiber of g has dimension at most one. Indeed it is a closed projective subvariety of P(sl(W)) consisting entirely of regular nilpotents; the universal theorem in `../../cubic-loci/cubic-component-multiplicities/applications/isotropic-four-kernel-exclusion/PROOF.md` excludes every integral projective surface of regular nilpotents. Any projective variety of dimension at least two contains such a surface by hyperplane sections, so the theorem gives the claimed fiber bound directly, independently of the kernel-rank stratification. Thus g cannot contract Z to a point.

Suppose h,t are linearly dependent in N^1(Z)_R. Since t is nonzero, h=lambda t for a real lambda. Because both classes are nef and t has positive intersection with some curve, lambda>=0. The ample class 2h+t is then (2lambda+1)t, so t is ample as an R-numerical class and deg(t^3[Z])>0. Intersecting the cubic relation with [Z] gives

       0=(lambda^2-2lambda+3) deg(t^3[Z]).

But lambda^2-2lambda+3=(lambda-1)^2+2>0. This contradiction proves independence.

No assertion that 2t-h is nef is needed or made. In general the mixed sign in the cubic relation prevents replacing this argument by a sum-of-nef-monomials contradiction.

## 3. Consequence for four-dimensional spectral components

Write E=sl(S) tensor det S, R=O_P(E)(-1), and let p:P_G(E)->G. The global classes

       r=c1(R*),    H=p*c1(O_G(1))

restrict to N as

       r=h+2t,      H=3t.

Indeed the inverse flag construction has tensor line R=L tensor M^2 and determinant line det W=M^3.

For completeness, the flag class h itself also extends to X. The universal twisted endomorphism A:S -> S tensor (R* tensor det S) is nonzero at every projective point, has determinant zero, and cannot have rank one by the imported rank-one exclusion. It therefore has constant geometric rank two on the reduced scheme X. The usual invertible-minor argument on a reduced scheme gives a line subbundle L_X=ker A of S, hence of V tensor O_X. Thus h_X=c1(L_X*) is nef and restricts to h on N. The rational class t_X=H/3 also extends t. This gives an alternative direct way to see the restriction obstruction below.

Let Y be an integral component of X of dimension four. The existing spectral bound proves that q does not vanish identically on Y and that its zero divisor is nonempty. The section q is a nonzero section of a line bundle on the integral Y, so its nonempty zero scheme is an effective Cartier divisor. Every integral component Z of its reduced support has dimension three and lies in N. On such a Z,

       t=H/3,      h=r-2H/3.

By Section 2 these restrictions are independent. Hence the restrictions of r,H are independent, and the restriction map from N^1(Y)_R has image of dimension at least two. In particular r,H are independent on Y and rho(Y)>=2.

The conclusion remains valid when Y and Z are singular: numerical equivalence of Cartier divisors is tested on integral curves, and a numerically trivial divisor on Y restricts to a numerically trivial divisor on Z.

## 4. Intersection-number constraints and the remaining gap

For an integral threefold Z in N define

       a=deg(h^2t[Z]), b=deg(ht^2[Z]), c=deg(t^3[Z]).

Nefness gives a,b,c>=0, and the cubic identity gives

       a=2b-3c, so b>=3c/2.

In fact b>0. The image g(Z) has dimension at least two because its fibers have dimension at most one. Hence t has numerical dimension at least two, so deg(t^2(2h+t)[Z])=2b+c>0. If b=0, the preceding equality and nonnegativity imply a=c=0, contradiction.

If g(Z) has dimension three then c>0; if it has dimension two then c=0 and a=2b>0. These alternatives do not themselves give a contradiction. The Khovanskii-Teissier inequality b^2>=ac is compatible with a=2b-3c; its direction must not be reversed.

Thus excluding the remaining extremal components requires additional input beyond these numerical identities. The present proof rules out Picard-number-one extremal components, but does not show that all spectral components have Picard number one, nor that three-dimensional nilpotent components are impossible.
