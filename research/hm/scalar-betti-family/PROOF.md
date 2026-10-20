# The scalar-annihilator Betti family and canonical relation sequence

Work over C with S=Sym(T), dim T=5, H_j=H²(End_0(F)(j−5)), I=Ann_S(H), R=S/I, and N_j=R_(5−j)*. This proof uses the complete H resolution in PR483, the scalar ideal generators in PR489, and the global identification N=Sym²_S H in PR491. All representations below retain the normalizer action; its determinant factors here are trivial. The existing parameters are r∈{0,15} and s∈{0,1} from PR483; they are not selected here.

Put P=S⊗W, with W=W′ two-dimensional, L=ker(P→H), and B=ker(Sym²P→N). Right exactness of symmetric powers identifies B with the image of L⊗W in Sym²P. Embed L⊗W in P⊗_S P. The kernel of symmetrization of P⊗P is the antisymmetric line S⊗detW. For a basis e₁,e₂, its element a(e₁⊗e₂−e₂⊗e₁) lies in L⊗W precisely when ae₁ and ae₂ lie in L, equivalently a annihilates H. Consequently the actual exact sequence is

0 → I⊗detW → L⊗W → B → 0.

In particular this is not an identification of I with the relation module L. The inclusion can be taken as the displayed antisymmetric tensor; changing the convention by a nonzero scalar changes none of the conclusions.

Since L is generated in degrees two and optionally three, B is generated in those degrees. Thus N has three generators in degree zero, twenty quadratic relations, and q cubic relations, with no further relation degrees. In degree three, I/mI=A⊗W′ and (L/mL)⊗W is zero when r=0, or A⊗(W′⊕Qspin) when r=15. Exactness on minimal generators and irreducibility of A⊗W′ imply

r=0 ⇒ q=0;
r=15 ⇒ q∈{20,30}.

The cubic relation module is, more precisely, A⊗Qspin if q=20 and A⊗(W′⊕Qspin) if q=30. In particular N is quadratically presented if and only if H is quadratically presented. The intermediate value ten is excluded: the source can remove only the W′ constituent, not Qspin.

For clarity, write Tor_i(M)_d for Tor_i^S(M,C)_d. From the presentation sequences, Tor_i(L)=Tor_(i+1)(H) and Tor_i(B)=Tor_(i+1)(N) for i≥1. At degree four the long exact sequence yields

0 → Tor_3(N)_4 → Tor_1(I)_4 → Tor_2(H)_4⊗W → Tor_2(N)_4 → (I/mI)_4 → 0.

The zero on the left follows from Tor_3(H)_4=0. The zero on the right follows from (L/mL)_4=0. The middle source is V⊗W′, dimension ten, by PR489; the next term is V⊗(2W′⊕Qspin), dimension forty, by PR483. Therefore the source map is either injective or zero. Put v=dim Tor_3(N)_4. Then v∈{0,10}, and dim Tor_2(N)_4=45+v. Graded duality identifies v=β_(2,6)(R) and 45+v=β_(3,6)(R). Semisimplicity further gives Tor_2(N)_4=V⊗(U⊕W′⊕Qspin), with one additional V⊗W′ precisely when v=10.

At degree five, Tor_2(N)_5 is a quotient of Tor_2(H)_5⊗W=sW′, since I has no minimal generator in degree five. Thus u=dim Tor_2(N)_5 belongs to {0,2}, with u≤2s. Duality makes this β_(3,5)(R). The other side of the same long exact sequence independently injects Tor_2(I)_5=Tor_3(R)_5 into Tor_3(H)_5⊗W=sW′, consistently with the same bound. No assertion about a particular scalar map or its rank is required.

Here are all support exclusions, so no unlisted Betti entries are being suppressed. Since R has no defining relations below degree three, minimality implies β_(i,d)(R)=0 for d<i+2, for 1≤i≤5. Since N has no defining relations below degree two, minimality gives β_(j,e)(N)=0 for e<j+1 for j≥1. Reversed duality β_(i,d)(R)=β_(5−i,10−d)(N) therefore bounds d≤i+4 for 1≤i≤4. Hence F₂(R) only has degrees four through six and F₃(R) only degrees five through seven. The complete N presentation further restricts F₄(R) to degrees seven and eight, with dimensions q and twenty. Levelness gives F₅(R)=3S(−10).

Multiplying (1+5t+15t²+25t³+15t⁴+3t⁵) by (1−t)⁵ gives

1−10t³−5t⁴+52t⁵−45t⁶−10t⁷+20t⁸−3t¹⁰.

Coefficient comparison, using these proved support bounds, gives exactly

F₀=S,
F₁=10S(−3)⊕15S(−4),
F₂=10S(−4)⊕(52+u)S(−5)⊕vS(−6),
F₃=uS(−5)⊕(45+v)S(−6)⊕(10+q)S(−7),
F₄=qS(−7)⊕20S(−8),
F₅=3S(−10).

This is a necessary complete Betti family, not a claim that all listed parameter combinations are realized or independent. It does not determine the differentials or select r,s,q,u,v. Equal-degree summands in adjacent terms of a minimal resolution are not cancellable units.

For the degree-five injection above, the preceding group is Tor_3(B)_5=Tor_4(N)_5, dual to Tor_1(R)_5. It vanishes because PR489 excludes quintic ideal generators. Thus the injection does not assume an omitted term is zero without justification.

Pinned dependencies:
- PR483, the H resolution and representation inputs: https://github.com/Akilleez-QA/read-em-and-weep/blob/e2ec3f19519b314ca119fb0f60ad9f41ed12af90/research/hm/dual-betti-family/PROOF.md
- PR489, complete scalar ideal generators and cubic linear syzygies: https://github.com/Akilleez-QA/read-em-and-weep/blob/5637cdd610fc2ec8ffbbbbfc7627b2d6c54f6873/research/hm/scalar-quartic-generators/PROOF.md
- PR491, global symmetric-square identification: https://github.com/Akilleez-QA/read-em-and-weep/blob/e9ed26058f69f3b96bdcdf920cb638e9dd68def8/research/hm/endomorphism-rigidity/INDEPENDENT-DERIVATION.md

This is an authored structural proof conditional on the cited inputs, not formal proof-assistant verification. No selected actual HM/source-instance evaluation, numerical matrices or rank computation, coefficient search, or large computation was performed. Original fixed-pair/source questions, higher-order lifting and algebraicity remain separate.
