# Independent monad check of first-normal nonuniqueness

Put H=V+W, N=A+W-prime, and K=Omega^2_P4(2). The actual normalized monad is N O(-1) -> W-prime K -> N O. Its graded symmetric square is quasi-isomorphic to Sym^2 F=B(-1). No actual differential is evaluated below.

## 1. Ambient twist minus one

The symmetric-square complex has terms, in degrees -2 through 2,

Lambda^2 N O(-2), N W-prime K(-1),
Sym^2(W-prime K) plus N^2 O(-1), N W-prime K, Lambda^2 N O.

All terms are acyclic except the central term and final term. With Q the universal rank-four quotient, K=Lambda^2 Q*, and

Sym^2 K=S_(2,2)Q* plus Lambda^4 Q*,
Lambda^2 K=S_(2,1,1)Q*.

Bott gives Sym^2 K acyclic and H1(Lambda^2 K)=Lambda^4 H=H*, with no other cohomology. Thus the central cohomology is H in degree one, since Lambda^2 W-prime is trivial. The only possible higher differential is H -> Lambda^2 N. But

H=V+W, Lambda^2 N=1+A+T6,

so equivariance forces that differential to vanish. Consequently

H1(B(-1))=V+W, H2(B(-1))=1+A+T6,
H0(B(-1))=H3(B(-1))=H4(B(-1))=0.

Serre duality is equivariant with no determinant character, since G is perfect and det H is trivial. Since B*=B, it yields

H1(B(-4))=0, H2(B(-4))=1+A+T6.

## 2. Ambient twist minus two retains an actual scalar

Twist the symmetric-square complex by -1. The only nonzero term cohomology is:

- In complex degree -1: H2(N W-prime Omega^2)=N W-prime.
- In complex degree 0: H2(Sym^2(W-prime K)(-1))=V Lambda^3 H.

Indeed Bott gives H2(Sym^2 K(-1))=Lambda^3 H and Lambda^2 K(-1) acyclic. All line-bundle terms have degrees -3,-2,-1 and are acyclic; the remaining Omega^2(1) term is acyclic. Therefore the complete cohomology is the actual two-term map

d:N W-prime -> V Lambda^3 H,
H1(B(-2))=ker d, H2(B(-2))=coker d,

with all other groups zero. The two invariant spaces each have dimension one:

N W-prime=1+V+T6,
Lambda^3 H=1+V+T6,
dim(V Lambda^3 H)^G=1.

Hence for some k in {0,1},

dim H1(B(-2))^G=dim H2(B(-2))^G=k.

No nonvanishing of d on invariants is asserted. The virtual character is W+V+S4+D5+T6, but this is not silently identified with H2 alone.

## 3. Exact invariant extension constraint

Apply the restriction sequence B(-4) --q0--> B(-2) -> B_Q0(-2), and take G-invariants (an exact operation in characteristic zero). The relevant segment is

0 -> C^k -> H1(B_Q0(-2))^G -> C --mu--> C^k.

Thus

dim H1(B_Q0(-2))^G=k+1-rank(mu),
1 <= dim H1(B_Q0(-2))^G <= 2.

It is one if k=0, or if k=1 and mu is nonzero; it is two precisely if both the invariant monad map d and the induced invariant q0 map mu vanish. These are actual remaining scalar conditions, not selected ranks.

The trace summand does not alter this first-normal extension space: H1(O_Q0(-2))=0 by the hypersurface sequence. Therefore first-order equivariant extensions of the fixed cone bundle, when nonempty, have a nonzero deformation space. The ambient bundle supplies existence. Cone data alone do not give uniqueness; the assertion concerns a fixed restriction identification, as usual for the square-zero deformation torsor.

This independently confirms the separate stack-square argument's bound, without using its square-thickening filtration. It does not identify gamma or force any first-normal extension parameter to a chosen value.

Evidence: the symmetric-square monad is the structural construction in PR455 at 8cbbe482ee50c35d52ffcdf3efb837fa8cf96af4, research/hm/twist-one-structural-vanishing/PROOF.md, Section 2. The normalized G-coefficients and exact character operations are in verify_negative_vertex_scalar.py. The companion verifier performs only universal representation arithmetic.
