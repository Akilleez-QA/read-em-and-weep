# The cubic canonical relation alternative is rigid

Work over C, with S=Sym(T), H and I=Ann_S(H), R=S/I, and N_j=R_(5-j)* as in PR492. Write W=W′=H_0, P=S⊗W, L=ker(P→H), and B=ker(Sym²P→N). The determinant of W is trivial. All maps are the actual graded module maps, with the normalizer action retained.

PR492 proves the exact sequence

0 → I⊗det W → L⊗W → B → 0,

where the first map takes a to a e₁⊗e₂−a e₂⊗e₁ for any basis e₁,e₂ of W. Let G=(L/mL)_3, with m=S_+. The cubic part on minimal generators is

I_3⊗det W → G⊗W → Tor_1^S(N,C)_3 → 0.

Here C in Tor coefficients denotes the ground field.

We prove that if the common cubic ghost r is fifteen, the first map is nonzero and hence injective. Thus the optional q=30 alternative in PR492 cannot occur:

r=0 implies q=0;
r=15 implies q=20.

## Coefficient extraction and the missing constituent

By PR483 and PR479, L_2=A*⊗W′ and

T⊗L_2=A⊗(R_6⊕1⊕U′).

Since H has no linear relations, the kernel of T⊗L_2→L_3 is precisely Tor_2^S(H,C)_3. If r=15, this kernel is A⊗U′. Semisimplicity therefore identifies

(mL)_3=T L_2=A⊗(R_6⊕1).

The scalar annihilator satisfies I_3=A⊗W′ by PR489, hence

I_3⊗W=A⊗(1⊕U′).

Scalar multiplication gives an injective map I_3⊗W→L_3: it is the restriction of S_3⊗W=P_3 to a subspace, and it lands in L_3 because I annihilates H.

Suppose that I_3⊗det W→G⊗W is zero. In the displayed basis, for every a∈I_3 this means

[a e₁]⊗e₂−[a e₂]⊗e₁=0 in G⊗W.

Extracting the e₁ and e₂ coefficients gives [a e₁]=[a e₂]=0. Thus the injective map I_3⊗W→L_3 factors through (mL)_3. This is impossible: its source contains the irreducible A⊗U′ summand, and its target A⊗(R_6⊕1) contains no such summand. Therefore the map on minimal generators is nonzero. Its source I_3 is irreducible, so it is injective.

For r=15, G⊗W=A⊗U′⊗W′=A⊗(W′⊕Qspin). Removing the injected A⊗W′ leaves exactly A⊗Qspin, of dimension twenty. When r=0, G=0 and no cubic relation of N is possible, as already proved in PR492.

This argument does not assume that an equivariant map is nonzero merely because the representations match. Its nonvanishing follows from coefficient extraction and the impossibility of an equivariant injection into a space missing the required constituent.

## The next cubic syzygy step

The same exact sequence at internal degree three gives

0 → Tor_2(H,C)_3⊗W → Tor_2(N,C)_3 → I_3⊗det W → G⊗W.

The initial zero uses Tor_1(I,C)_3=0, since I has no generators below degree three and a minimal syzygy increases degree. If r=15 the last arrow is now injective. Hence the first arrow is an isomorphism onto Tor_2(N,C)_3, yielding

Tor_2(N,C)_3=A⊗(W′⊕Qspin), dimension thirty.

If r=0, the first term and G vanish, so Tor_2(N,C)_3=I_3=A⊗W′, dimension ten. Duality consequently fixes the formerly 10+q dimensional degree-seven third syzygies of R to dimensions ten and thirty, respectively. The degree-seven fourth syzygies have dimensions zero and twenty, respectively. In particular these two Betti entries introduce no parameter independent of r.

## Linear syzygies force v=0 when r=15

Assume r=15. Put M=L⊗W and choose a graded minimal free cover E→M. Its generators have degrees two and three. Write Z=ker(E→M). Lift I→M to the minimal free cover of I and then to E. On degree-three generators I_3, the constant component into the cubic generator block E^(3)=S(-3)⊗(G⊗W) is precisely the injective map α:I_3⊗det W→G⊗W proved above.

Since I has no generators below degree three, every element z of Tor_1(I,C)_4 is a linear relation among I_3. It is represented by a nonzero element of T⊗I_3, with no constant coefficient on a minimal quartic generator. Applying the lifted map gives a syzygy z′∈Z_4. Its projection to the cubic generator block is (id_T⊗α)(z), which is nonzero.

If the induced map Tor_1(I,C)_4→Tor_1(M,C)_4 killed z, then z′ would belong to (mZ)_4. Here Z has no elements below degree three, so (mZ)_4=T Z_3. Every degree-three syzygy in Z_3 has zero projection to E^(3): a nonzero constant projection would be a dependence of the cubic minimal generators modulo mM. Consequently T Z_3 also has zero cubic-block projection, contradicting the preceding nonzero projection. Therefore

Tor_1(I,C)_4 → Tor_1(M,C)_4=Tor_2(H,C)_4⊗W

is injective. This is exactly the map defining v in PR492. Hence r=15 forces v=0.

This is a minimal-generator argument, not an evaluation of any chosen syzygy matrix. It is independent of the choices of graded lifts, because changing a lift changes its syzygy only by the corresponding boundary and does not alter the constant cubic-generator component.

## Refined scalar-algebra Betti alternatives

Substitute q=20 and v=0 when r=15 into PR492. The full scalar-algebra free modules then read

F₀=S,
F₁=10S(-3)⊕15S(-4),
F₂=10S(-4)⊕(52+u)S(-5),
F₃=uS(-5)⊕45S(-6)⊕30S(-7),
F₄=20S(-7)⊕20S(-8),
F₅=3S(-10).

If r=0, the PR492 family instead has q=0, with v∈{0,10} still unresolved. In both cases u∈{0,2} and u≤2s remain as before. Thus any occurrence of v=10 forces r=0. No independence or realizability of the remaining combinations is claimed.

## Pinned inputs and limits

- PR492 at 720d25905320ffcbcd5433c6f61a92b2634afef8: https://github.com/Akilleez-QA/read-em-and-weep/blob/720d25905320ffcbcd5433c6f61a92b2634afef8/research/hm/scalar-betti-family/PROOF.md
- PR483 at e2ec3f19519b314ca119fb0f60ad9f41ed12af90: https://github.com/Akilleez-QA/read-em-and-weep/blob/e2ec3f19519b314ca119fb0f60ad9f41ed12af90/research/hm/dual-betti-family/PROOF.md
- PR479 at b57cf851bb244706acfe6c6485d4dfa54ceb6519, section 4: https://github.com/Akilleez-QA/read-em-and-weep/blob/b57cf851bb244706acfe6c6485d4dfa54ceb6519/research/hm/quadratic-shadow-exclusion/PROOF.md
- PR489 at 5637cdd610fc2ec8ffbbbbfc7627b2d6c54f6873: https://github.com/Akilleez-QA/read-em-and-weep/blob/5637cdd610fc2ec8ffbbbbfc7627b2d6c54f6873/research/hm/scalar-quartic-generators/PROOF.md

This is authored structural mathematics conditional on those inputs, not formal proof-assistant verification. It excludes q=30 and proves r=15 implies v=0; it does not select r, s or u, or settle v when r=0. It evaluates no selected HM/source instance, polynomial coefficient, multiplication matrix or numerical rank, and uses no large computation. Original fixed-pair/source questions, higher-order lifting and algebraicity remain separate and unresolved.
