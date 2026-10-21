# Low-degree parameter syzygies of the column Koszul map

Work over the established algebraically closed characteristic-zero field. Set S=Sym(T), dim(T)=5, P=P(W*), and let A be the column algebra family. Its graded pieces are A_0=O, A_1=T tensor O, A_2=E tensor O(2), and A_d=0 for d>=3.

## Pinned dependencies

- PR512, commit 26811b53c198879d0c55a2fb9ba75187bee38d9c, research/hm/column-family-intersections/PROOF.md: the actual family algebra, binary evaluation, and intersection of any three quadratic relation spaces equal to zero.
- PR521, commit 7f69d421d66038d2c55d20b1997aa818c98d29bd, research/hm/column-jump-orbits/PROOF.md: the reduced degree-four Koszul map phi:9O -> 10O(2), generic rank r=9-u_0/5, 5<=r<=9; its image J, saturation I, and jump divisor either empty or the reduced twelve-point orbit. In the latter case deg J<=2r-12; always deg J<=2r.
- PR494, commit 72ab9a7524aef8c9d1c1fd989f8b0e83826dc916, research/hm/higher-symmetric-powers/PROOF.md: actual binary multiplication gives (Sym^p_S H)_2=E tensor Sym^(p+2)W, for p>=1, with degree-zero and degree-one terms Sym^pW and T tensor Sym^pW.
- PR499, commit 1112189481554b0353c64178e3adc0dede2c3fbe, research/hm/middle-euler-ghost-exclusion/PROOF.md: the pure resolution of H, in particular Tor_3^S(H,k)_4=0.
- PR490, commit 1c5ad353bb5f1808150f64cde3c29b92c6e13d91, research/hm/dual-tensor-bridge/VERIFICATION.md: Sym^2_S H=R^vee(-5), compatibly with S multiplication.
- PR500, commit 86d7e1b5d3aee770ea3e7652c950b29bca1aba10, research/hm/scalar-last-ghost-exclusion/PROOF.md: the complete resolution of R.

All paths refer to https://github.com/Akilleez-QA/read-em-and-weep/blob/COMMIT/PATH with the displayed exact commit. These are conditional dependencies, not fresh certifications of their proofs.

## The vanishing statement

Let K=ker(phi), a vector bundle of rank 9-r. Then

H^0(P,K)=H^0(P,K(1))=H^0(P,K(2))=0.

Consequently each line-bundle summand of K has degree at most -3.

### Constant sections

Before taking the five-dimensional Heisenberg multiplicity factor, the source of phi is

C=(T tensor Lambda^3 T)/im(Lambda^4 T),

and the family map is the ordinary polynomial Koszul differential followed by S_2 -> (A_lambda)_2. If a constant class is killed for every lambda, its polynomial differential belongs to the intersection of the spaces (J_lambda)_2 tensor Lambda^2 T. The intersection is zero by PR512. Exactness of the polynomial Koszul complex shows that the original representative was a Lambda^4 T boundary. Thus no nonzero constant class survives.

### Sections of parameter degree one and two

The evaluation W tensor O -> O(1) induces an S-linear map

H tensor O -> A(1).

Indeed, an S-linear map from S tensor W to A(1) annihilates the original quadratic presentation precisely because contraction by the tautological covector gives the defining column relations. Multiplication in A therefore induces

Sym^p_S H tensor O -> A(p).

For p=1,2, the induced maps on global sections in S-degrees zero, one, and two are isomorphisms compatible with S multiplication. In degrees zero and one they are the ordinary binary evaluation identifications. In degree two they are the map

E tensor Sym^(p+2)W -> H^0(P,E tensor O(p+2)),

which is binary evaluation, hence an isomorphism. The identification is the actual quotient multiplication of PR494, not a comparison of equal dimensions.

The part of the internal-degree-four Koszul complex computing Tor_3 uses only S-degrees zero, one, and two:

Lambda^4 T tensor M_0 -> Lambda^3 T tensor M_1 -> Lambda^2 T tensor M_2.

Twisting the family complex by O(p) and taking global sections therefore identifies this three-term complex with the one for M=Sym^p_S H. Quotienting the first, constant-rank boundary map commutes with global sections: its source and target are constant bundles twisted by O(p), with H^1(O(p))=0 for p>=0. Thus, restoring the five-dimensional irreducible factor D,

D tensor H^0(P,K(p)) = Tor_3^S(Sym^p_S H,k)_4,  p=1,2.

For p=1 the right side vanishes by PR499. For p=2, dualizing the PR500 resolution of R gives the resolution of R^vee(-5)=Sym^2 H. Its homological-degree-three term is

52S(-5) + 10S(-6),

so its Tor_3 in internal degree four is zero. This proves both remaining vanishings. By splitting on P1, H^0(K(2))=0 forces every summand O(-d) to have d>=3.

## New numerical exclusions

The exact sequence 0 -> K -> 9O -> J -> 0 gives

deg J = -deg K >= 3(9-r).

The saturation I is a subbundle of 10O(2), so deg I<=2r. Since I/J has nonnegative length, deg J<=2r always. Therefore

3(9-r)<=2r,

which gives r>=6. The generic value u_0=20 is excluded. A point with u=20 is also excluded: by PR521 that could only be uniform u=20 or a jump from u_0=15.

If jumps occur, PR521 gives the sharper upper bound deg J<=2r-12. Combining the inequalities yields

3(9-r)<=2r-12,

so r>=8. Hence the only remaining jump alternatives are generic u_0=0 with u=5 on the twelve-point orbit, or generic u_0=5 with u=10 on that orbit. All other points take the generic value.

In particular u(lambda)<=15 uniformly, and any member attaining fifteen belongs to the constant-u=15 alternative. No particular remaining alternative is asserted to occur.

## Excluding the remaining positive-generic jump

The r=8 jump alternative can also be excluded using the actual normalizer action. We use the representation conventions of PR453, commit 56516a96a7eacfde0c8e272ca38db415cc7f294b, research/hm/cubic-invariant-target/PROOF.md, and the Horrocks--Mumford representation identities cited there (1973, Section 3.3). Write V=T*, W=W', U=Sym^2 W0, and R6=U' tensor W0. The relevant identities are

Lambda^3 T = A tensor W0,
T tensor A = V tensor (U' + W0),
W0 tensor W0 = 1 + U,
U' tensor W0 = R6,
Lambda^4 T = V.

Consequently the source C before taking Heisenberg multiplicities is

C = V tensor (U + R6).

The boundary V is exactly the unique trivial multiplicity summand in V tensor (1+U+R6), so passing to C removes that summand. These are identities of actual normalizer representations, not arbitrary equivariant structures imposed on ordinary splitting factors.

Taking Hom_Gamma(V,-) gives the genuine action of G=SL(2,F5) on the multiplicity source U+R6 and on its kernel bundle K. It is a genuine quotient action because Gamma acts trivially on this Hom space and V itself is an actual normalizer representation. If r=8 and jumps occur, K is a line bundle O(-d). The degree bounds already proved give 3<=d<=4.

Every G-linearization of O(-d) differs from its standard one by a character of G: the ratio of two linearizations is an invertible global function on P1 for each group element, hence a character. Since SL(2,F5) is perfect, it has no nontrivial characters. Thus an equivariant inclusion of K into (U+R6) tensor O would give a nonzero invariant element of

(U+R6) tensor H^0(O(d)) = (U+R6) tensor Sym^d(W).

But Sym^3(W')=Qspin is an irreducible representation of dimension four, and Sym^4(W')=J5 is an irreducible representation of dimension five. Neither contains the dual of U or R6, which have dimensions three and six. Complete reducibility therefore makes the invariant space zero for d=3,4. This contradiction excludes r=8 jumps.

The final classification is consequently:

- u is constant with value in {0,5,10,15}; or
- u is generically zero and is exactly five on the unique reduced twelve-point orbit, and zero elsewhere.

This is a necessary classification, not an existence claim for the alternatives. The new vanishing of parameter-linear and parameter-quadratic kernel sections and the normalizer obstruction are separate steps: the former gives the uniform bound, and the latter removes the last positive-generic jump.

## What this does not establish

This proof does not determine the generic rank or decide whether jumps occur. It does not prove all surviving constant alternatives possible. It performs no selected HM/source-instance evaluation, multiplication-rank calculation, coefficient search, or large computation. It proves a structural restriction on a parameter-family kernel. Original fixed-pair residual, higher-order lifting, and algebraicity remain unresolved. Status: authored proof requiring independent mathematical review; not formally proof-assistant checked.
