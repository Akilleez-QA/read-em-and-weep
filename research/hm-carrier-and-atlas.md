# Explicit Horrocks–Mumford carrier and six-chart atlas

Status: checked construction and algebraic atlas. This is not an all-order deformation theorem or a repair of the withdrawn eightfold proof.

## Construction

Let H be the normalized Horrocks–Mumford bundle on P⁴, with rank 2, c₁(H)=−h, c₂(H)=4h² and monad 5O(−1) → 2Ω²(2) → 5O.
Primary source: Horrocks–Mumford, “A rank 2 vector bundle on P⁴ with 15000 symmetries”:
https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf

Take C: y²=x³−x, X=C⁴, Θ the sum of the four origin divisors, and N=O_X(Θ). The finite map f:X→P⁴ is X→(P¹)⁴→Sym⁴P¹=P⁴. On the finite x-chart its coordinates are v_k=e_k(x₁,x₂,x₃,x₄), k=0,…,4. Its degree is 16·24=384 and f*O(1)=N².

Set E=f*H⊗N. Then det E=O, c₂(E)=15θ² and
ch(E)=2−15θ²+(225/12)θ⁴=exp(i√15θ)+exp(−i√15θ).
This carrier concerns Q(√−15), not every imaginary quadratic field.

## Explicit monad matrices

Let V have ordered basis e₀,…,e₄, with indices modulo 5. Define
w⁺_a=e_{a+2}∧e_{a+3},  w⁻_a=e_{a+1}∧e_{a+4}.
With Q=V/O(−1), the middle term is (Λ²Q⊗O(−1))². The five columns of α are the projections of (w⁺_a,w⁻_a). The alternating pairing is u⁺∧v⁻−u⁻∧v⁺, and β=αᵗJ.

On v₀≠0 put a=v₁/v₀, b=v₂/v₀, c=v₃/v₀, d=v₄/v₀. Use Q basis (e₁,e₂,e₃,e₄) and wedge order (12,13,14,23,24,34) in each half. The rows of α are:
```
0  0  0  b  1
0  0  0  c  0
0  0  a  d  0
1  0  0  0  0
0  0  b  0  0
0  1  c  0  0
0  a  0  0  0
0  0 -1  0 -a
1  0  0  0  0
0 -c  0  0 -b
0 -d  0 -1  0
0  0  0  0  d
```
Here J=[[0,S],[−S,0]], with S symmetric and nonzero entries
S₀₅=S₅₀=1, S₁₄=S₄₁=−1, S₂₃=S₃₂=1.
Direct polynomial multiplication gives βα=0.

## Cover and frames

All matrix index lists below are zero-based.

For j=0,…,4 let
U_j={v_j≠0, v_j⁴−∏_{k≠j}v_k≠0}.
On chart j use the cyclic Q basis (e_{j+1},…,e_{j+4}), not numerical ascending order. Every inclusion and transition matrix must use this same order.

On U₀ use β-column indices I=(3,6,4,1,11), complement Jc=(0,2,5,7,8,9,10). Write A=α_{Jc}; choose its row indices P=(0,2,3,4,6), with complement U=(1,5). With D=1−abcd,
det β_I=−D,  det A_P=D.
The other four charts use cyclically transported data.

The sixth set is U_*={v₀v₁v₃v₄≠0}. In the v₀-chart use
I=(0,1,2,3,4), Jc=(5,6,7,8,9,10,11),
P=(0,1,2,3,5), U=(4,6).
Then det β_I=cd and det A_P=−a²c.

These six sets cover P⁴. If any coordinate vanishes, every chosen nonzero coordinate supplies a U_j. If none vanishes, the point is in U_*.

For either pivot choice define K by
K_{Jc}=I₇,  K_I=−β_I^{-1}β_{Jc}.
Define R(z)=z_U−A_U A_P^{-1}z_P and S=K e_U.
Then α=KA, RA=0, and R e_U=I₂. Thus S is a frame of ker β/im α; its coordinate map is R pr_{Jc}.

On overlaps let T^Q_ij be the quotient-basis change from chart j to chart i, with the cyclic orders above. Choose a further cover trivializing N, with local frames n_j=ν_ij n_i. The E transition is
G_ij=R_i pr_{Jc,i} [ν_ij(v_i/v_j) diag(Λ²T^Q_ij,Λ²T^Q_ij)] S_j.
This is an explicit rational formula after the line bundle is trivialized. The two inverse-x charts on C trivialize N², but should not be assumed to trivialize N itself.

## Verification scope

Exact sparse integer-polynomial calculations, including independent reconstructions, checked βα=0 and the four pivot determinants. The cover and frame identities follow from the displayed algebra. These establish an atlas, not its quantization.

The separate finite-RHom calculation uses the four-term model
5N⁻¹ → 15N → 10N³ → 2N⁵
in degrees −1,0,1,2. Endomorphisms involve only even powers of N, so the inverse-x chart model for N² suffices there.

An ordinary rational Čech representative of the compensating gerbe is not central under a Moyal product. A valid quantization calculation must include its algebroid descent corrections or use an equivalent central analytic model.
