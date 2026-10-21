# Exact eigenclass cohomology on the modular double-cover model

## Scope and setup

This is an unconditional calculation on the compact ruled model, using the general smooth finite double cover established in MODULAR-QUADRIC-DOUBLE-COVER.md. Application to the actual resolved beta-Gamma incidence is conditional on a separate identification; no such identification is inferred from numerical agreement.

Let f:S=S(5)→P1, with I²=−5, I·F=5, F²=0, K_S=3F and χ(O_S)=5. Let V be the checked global rank-two z-ruling bundle, with

c1(V)=I+3F, c2(V)=10, V*=K⊂O_S^5,
f_*V=O_P1^5, R¹f_*V=0.

Put P=P_S(V), ξ=O_P(1), h=ξ+I. Let W∈|2h| be the smooth integral member induced by a general ambient quadric, with π:W→S finite flat of degree two, as established in MODULAR-QUADRIC-DOUBLE-COVER.md. The corrected five w-sections globally generate V(I); their quadratic products generate Sym²(V(I)), a rank-three bundle on a surface, and a general induced quadratic section is nowhere zero. No single induced quadric is evaluated here.

Set B=10I+12F and define

L3=π*B−2h|W,       L4=π*B−h|W.

These are the proposed primitive-three/four eigenclass line bundles, not assertions that their sections realize actual twisted endomorphisms.

## 1. Double-cover invariants

The projective-bundle sequence for W gives

π_*O_W=O_S⊕O_S(−3I−3F),    R^iπ_*O_W=0 for i>0.

Write M=3I+3F. Adjunction yields K_W=π*(K_S+M)=π*(3I+6F). Consequently

χ(O_W)=55,      K_W²=270.

If W is smooth, its topological Euler number is390. Using the already checked h1(O_S)=0 and H1(O_S(3H))=0 with H=I+2F gives q(W)=0 and p_g(W)=54. The vanishing follows also by dualizing the second summand of π_*O_W; K_S+M=3H.

With h³=30 and p_*h²=3I+3F, intersection in P gives

L3²=200,     K_W·L3=300,     χ(L3)=5,
L4²=740,     K_W·L4=480,     χ(L4)=185.

For clarity, B²=700, B·(3I+3F)=180, B·(3I+6F)=330 and (3I+3F)·(3I+6F)=90. These yield the displayed numbers directly from W=2h.

## 2. Exact pushforwards retain the ruling quadratic

The restriction sequence

0→O_P(B−3h)→O_P(B−h)→L4→0

and relative duality give

E4:=π_*L4 = V*⊗O_S(6I+9F) = V⊗O_S(5I+6F).

There are no higher direct images, since π is finite.

For L3 the corresponding sequence has terms B−4h and B−2h. It gives the exact vector-bundle sequence

0→E3:=π_*L3→Sym²(V*)⊗O_S(5I+9F)
  --contraction by the actual ruling quadratic--> O_S(7I+9F)→0.

Surjectivity follows precisely because the ruling quadratic is nowhere zero on S, equivalently W→S is finite. This is an actual q-dependent kernel, not a split or dimension-only replacement.

Its determinant is

det E3=O_S(5I+9F).

Using rank two, E3*=E3⊗(det E3)^(-1), so the same exact sequence supplies a useful injection

E3* ⊂ Sym²(V*).

## 3. A uniform modular-fiber vanishing

For every modular fiber E, smooth or an I5 polygon, H0(O_E)=C and ω_E=O_E. Since K=V* is an equivariant subbundle of the trivial five-dimensional Schrödinger bundle,

H0(E,Sym²K|E) ⊂ Sym²(C5)

is an H5-invariant subspace of constant vectors. The central character of Sym²(C5) is nontrivial, so every irreducible constituent has dimension five. But evaluation at any point injects this constant section space into the rank-three fiber Sym²K. Its dimension is therefore at most three. It must be zero.

No equivariance of the chosen quadric is needed: the larger bundle Sym²K is equivariant, and E3* embeds into it whether or not E3 is equivariant.

The displayed injection therefore gives H0(E,E3*|E)=0. Duality on the Gorenstein genus-one fiber gives H1(E,E3|E)=0. Its degree is25, so h0(E,E3|E)=25 on every fiber.

Likewise E4*=K⊗O_S(−5I−6F) embeds into O_S(−5I−6F)^5. On a smooth fiber this line bundle has degree−25. On an I5 fiber it has negative degree on every component, since I has degree one on each component. It has no section on either type of fiber. Thus H1(E,E4|E)=0 and h0(E,E4|E)=55 on every fiber.

## 4. Explicit splitting constraints and unavoidable sections

Cohomology and base change give

R¹f_*E3=R¹f_*E4=0,
rank(f_*E3)=25,       degree(f_*E3)=−20,
rank(f_*E4)=55,       degree(f_*E4)=130.

The degrees follow from χ(E3)=5 and χ(E4)=185, since χ of a rank-r bundle on P1 equals r+degree. Thus for their Birkhoff–Grothendieck splittings

f_*E3=⊕_(j=1)^25 O(a_j),     sum a_j=−20,
f_*E4=⊕_(j=1)^55 O(b_j),     sum b_j=130.

In particular

H2(W,L3)=H2(W,L4)=0,
h0(W,L3)=5+h1(W,L3)≥5,
h0(W,L4)=185+h1(W,L4)≥185.

These are exact lower bounds, not dimension predictions based on an unverified balanced splitting. No claim that the a_j are only0 and−1, or that either H1 vanishes, is made.

## 5. Fifty double-point corrections still cannot force twist-four vanishing

For any fifty distinct points p_1,...,p_50 on the smooth surface W, the disjoint union of their first infinitesimal neighborhoods has length3·50=150. The restriction exact sequence therefore gives

h0(W,L4⊗I_(p_1,...,p_50)^2) ≥ h0(W,L4)−150 ≥35.

No independence of these jet conditions is assumed; failure of independence only increases the lower bound. Equivalently, if b:W'→W is the blowup of these points with exceptional curves E_j,

h0(W',b*L4−2 sum E_j)≥35.

This is an abstract theorem for arbitrary fifty distinct points on this W. It is not an assertion that the actual resolved incidence has this blowup description or that its exceptional corrections have multiplicity two.

## Consequence

On this model, mere existence of an effective divisor in either proposed eigenclass cannot obstruct primitive twist three or four: the line bundles always have at least five and185 sections respectively. Even adding fifty arbitrary double-point conditions leaves at least35 twist-four sections. Any exclusion must impose additional compatibility with the actual endomorphism, spectral involution, or ambient evaluation construction. The actual-model identification and such compatibility remain separate gates.

No selected HM coefficients, ranks, or instance experiments are used.
