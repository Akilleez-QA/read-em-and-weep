# The uniform cyclic Betti table and its relative Tor bundles

Work over C. Set S=Sym(T), dim T=5, W=H_0=W', P=P(W), and let L_w=S/Ann_S(w). Parameter twists O(d) are distinct from internal polynomial shifts S(-j). We determine free-module terms of the minimal resolutions, not explicit differentials.

## Exact dependencies

- [PR499, commit 1112189481554b0353c64178e3adc0dede2c3fbe](https://github.com/Akilleez-QA/read-em-and-weep/blob/1112189481554b0353c64178e3adc0dede2c3fbe/research/hm/middle-euler-ghost-exclusion/PROOF.md): H has pure resolution (2,10,20,20,10,2) in internal degrees (0,2,4,6,8,10).
- [PR513, commit df947c1ce092c0c59dcef187639147da8a7b2873](https://github.com/Akilleez-QA/read-em-and-weep/blob/df947c1ce092c0c59dcef187639147da8a7b2873/research/hm/column-level-resolution/PROOF.md): the column A has resolution S; 10S(-2); 15S(-3)+(5+u)S(-4); uS(-4)+26S(-5); 20S(-6); 5S(-7).
- [PR514, commit d915ed6a7f0c679343447106707692eb7bdee6f7](https://github.com/Akilleez-QA/read-em-and-weep/blob/d915ed6a7f0c679343447106707692eb7bdee6f7/research/hm/cyclic-submodule-duality/PROOF.md): 0 -> L_w -> H -> A_w -> 0, and Hilbert function L_w=(1,5,15,20,10,2).
- [PR528, commit bd9a26837bb79b2e21cf35d6586d3ba3d6ca83fa](https://github.com/Akilleez-QA/read-em-and-weep/blob/bd9a26837bb79b2e21cf35d6586d3ba3d6ca83fa/research/hm/middle-family-parity/PROOF.md): C=H O/M=A O(1), where M=image(S O(-1)->H O); A has pieces O, T O, E O(2); Tor3(A)_5 has ordinary splitting 24O(4)+W0 O(2).
- [PR533, commit c2f8fd17d88e93606bba8a642d2af19dcac82d04](https://github.com/Akilleez-QA/read-em-and-weep/blob/c2f8fd17d88e93606bba8a642d2af19dcac82d04/research/hm/cyclic-relative-comparison/PROOF.md): rho=u, Tor1(S/K)_4=V O(10), Tor2(S/K)_4=10O+(V W0)O(-4), and K_3=I_3 O + A_rep O(-4).

Representation conventions are those in these proofs: E=A_rep*, E Lambda4(T)=T(U'+W0), U'=Sym2(W), and det(T)=1. Ordinary bundle splitting statements below do not assert that the direct sum of the twenty-four nontrivial Heisenberg character lines has trivial normalizer action.

The public representation source is [Horrocks--Mumford (1973), Section 3.3 and appendix](https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf).

## 1. Exhausting the fiberwise long exact sequence

For every internal degree j the exact sequence gives

Tor_(i+1)(H)_j -> Tor_(i+1)(A)_j -> Tor_i(L)_j -> Tor_i(H)_j -> Tor_i(A)_j.

In degree two the map Tor1(H)_2 -> Tor1(A)_2 is an isomorphism: both neighboring L groups vanish, since L is cyclic in degree zero and K_2=0. Degree three gives Tor1(L)_3=Tor2(A)_3, of dimension fifteen.

The sole nontrivial overlapping strand is degree four:

0 -> C^u -> Tor2(L)_4 -> C^20 --rho--> C^(5+u) -> Tor1(L)_4 -> 0.

The established equality rho=u therefore makes these L dimensions twenty and five, respectively, at every parameter. In degree five, Tor2(L)_5=Tor3(A)_5 has dimension twenty-six; Tor3(L)_5=0.

In degree six the exact sequence is

0 -> Tor4(A)_6 -> Tor3(L)_6 -> Tor3(H)_6 -> 0,

so Tor3(L)_6 has dimension forty, not twenty. Degrees seven, eight and ten give respectively

Tor4(L)_7=Tor5(A)_7=C^5,
Tor4(L)_8=Tor4(H)_8=C^10,
Tor5(L)_10=Tor5(H)_10=C^2.

All remaining positive Tor groups vanish: every such position is flanked by zero H and A terms in the displayed long exact sequence. Thus the minimal free-module terms are exactly

F0 = S,
F1 = 15S(-3) + 5S(-4),
F2 = 20S(-4) + 26S(-5),
F3 = 40S(-6),
F4 = 5S(-7) + 10S(-8),
F5 = 2S(-10).

In particular the cyclic Betti table is constant on the whole parameter line. The exceptional column jumps are absorbed by the degree-four comparison, not inherited by L. This is a consequence of actual connecting maps and rho=u, not a choice among templates with the same Hilbert series.

## 2. Relative base change is valid for L

Let script L=S/K=M O(1). It is a vector bundle in every graded degree: it has pieces S_d O for 0<=d<=2 and H_d O(1) for 3<=d<=5, and zero thereafter. The latter claim follows from C_d=0 for d>=3. For each fixed internal degree, its Koszul complex is bounded and consists of vector bundles.

Section 1 proves constant dimensions of all fiber homology groups in every such complex. Starting at an end of the complex, the formula

rank(d_i)+rank(d_(i+1))=rank(K_i)-dim H_i

then proves constant ranks for all its differentials. Kernels, images and homology are consequently vector bundles, and homology commutes with restriction to every fiber. This argument deliberately does not assume that the degree-four column Tor sheaves satisfy base change: they do not have constant fiber ranks.

## 3. The full ordinary relative Tor table

Write H_i^Tor=Tor_i(H)_(2i), a constant coefficient space of dimensions 10,20,20,10,2 for i=1,...,5. The nonzero positive relative Tor bundles of script L are

Tor1(script L)_3 = I_3 O + A_rep O(-4),
Tor1(script L)_4 = V O(10),
Tor2(script L)_4 = 10O + (V W0) O(-4),
Tor2(script L)_5 = 24O(6) + W0 O(4),
Tor3(script L)_6 = H_3^Tor O(1) + T W O(5) + T W0 O(4),
Tor4(script L)_7 = E O(4),
Tor4(script L)_8 = H_4^Tor O(1),
Tor5(script L)_10 = H_5^Tor O(1).

The first three are the established annihilator and syzygy bundles of PR533. For degree five the connecting isomorphism gives Tor2(M)_5=Tor3(C)_5. Twisting PR528's column bundle twice yields the stated O(6) and O(4) summands.

For degree six, the column Koszul strand is

T O -> E Lambda4(T) O(2) -> 0.

The first map is fiberwise injective because the column has no degree-one socle. After removing T it is 1 O -> (U'+W0)O(2). Central parity kills the W0 component. The U' component is the nonzero quadratic Veronese column, unique up to scalar; equivalently it is the dual of binary quadratic evaluation. Its cokernel is W O(3). Indeed dualizing 0 -> W O(-1) -> U' O -> O(2) -> 0 and twisting by O(2) gives 0 -> O -> U' O(2) -> W O(3) -> 0. Hence

Tor4(A)_6=T[W O(3)+W0 O(2)].

The relative degree-six connecting sequence, then twisted by O(1), is

0 -> T[W O(5)+W0 O(4)] -> Tor3(script L)_6 -> H_3^Tor O(1) -> 0.

It splits as ordinary vector bundles since H1(O(4))=H1(O(3))=0. One can average a splitting over the finite group when retaining the full coefficient representations.

The column's degree-seven top Tor is A_2 Lambda5(T)=E O(2). Twisting twice gives Tor4(script L)_7=E O(4). In degrees eight and ten all column Tor terms vanish, so the comparison with H yields the two remaining constant spaces twisted by O(1).

## 4. Independent graded consistency checks and boundary

The alternating rank polynomial of the stated free-module terms is

1-15t^3+15t^4+26t^5-40t^6+5t^7+10t^8-2t^10,

which equals (1+5t+15t^2+20t^3+10t^4+2t^5)(1-t)^5. This checks, but does not prove, the derived Betti table.

The alternating degrees of the relative Tor bundles in internal degrees 3,4,5,6,7,8,10 are respectively

20, -90, 152, -110, 20, 10, -2.

Independently the graded pieces of script L have degree polynomial 20t^3+10t^4+2t^5. Multiplying this by (1-t)^5 gives exactly those coefficients. This checks the parameter twists, including the O(1) shift between M and script L and the degree-six extension.

The contribution is the complete constant cyclic Betti table and all its relative Tor splitting types, closing the cyclic resolution uncertainty. It leaves the compressed Gorenstein quotient's middle obstruction, the original fixed-pair residual, higher-order lifting and algebraicity undecided. No selected HM/source instance, numerical multiplication matrix, coefficient search or large computation is used. This is an authored structural derivation conditional on the pinned inputs, not a formal proof-assistant check.
