# Neither constant-span type can occur in the onto bb source

## Result and precise scope

For either original-zero-defect label

    G3.11.863639aa192e: A_q=O(-10)+U, U=O(4)+O(6),
    G3.11.73682b4c817f: A_q=O(-10)+U, U=W O(5),

the bb source

    E=P O(-2)+2T O(-3)+O(-10)

cannot have an onto top map F=P O(-2)->U. The source tuple is (0,2,0,0,0,0,0,1). In the split label the top map is necessarily onto by PR821, so its entire bb source is excluded. In the balanced label only the onto branch is excluded; the separate degree-twelve torsion branch is untouched. Neither whole stable label is excluded.

The two possible intrinsic top constant spans from PR821 are ruled out by different structural arguments. The nine-dimensional degree-eight span contradicts a horizontal-lattice quotient degree. The twelve-dimensional P-conic span contradicts the exact bounded splitting support of the full positive-endpoint transform and the derivative rank of its linear top block.

## Public inputs

PR821 at immutable commit 0d7e1e7312a114ded8a2c49ed1a7ca2f4d7e4c7f gives both constant-span alternatives and the split-label onto conclusion:

https://github.com/Akilleez-QA/read-em-and-weep/blob/0d7e1e7312a114ded8a2c49ed1a7ca2f4d7e4c7f/research/hm/profile11-onto-rank-four-top/ONTO-RANK-FOUR-TOP-SUBSYSTEMS.md

Its SHA256 is 87244e453597105dffb298743c1725ac29b00c8b8dc1cafad37f55235c81ea34. It pins the original data at db51525015bb7c5e825833d550d08dedf6f6ea96 and the original quotient's saturation. The internal/external derivative-image lemma is PR796, Section3:

https://github.com/Akilleez-QA/read-em-and-weep/blob/d2b43060c83328dd5118aee6b9288fcfa0c873ac/research/hm/profile12-quadratic-block-exclusion/PROOF.md

No unpublished continuation is a dependency. Work over C with the actual trivial connection on H O and the binary icosahedral representations W,Wp,A,V,P,S,D,T of those inputs. All representation equalities below concern abstract equivariant bundles, never a horizontal splitting of a connection.

## 1. The exact transform after removing the negative endpoint

Assume F->U is onto. Write M=F^+. The pinned theorem gives

    K0=ker(F->U)=W O(-9),
    im(kappa)=W O(-9),
    M=(Wp+T) O(-1), rank M=8, deg M=-8.          (1)

The internal image in (E/F)(-2) is saturated and lies in a T-multiplicity line, not in O(-12). Thus I0=M intersect E has the exact sequence

    0 -> F -> I0 -> W O(-7) -> 0.               (2)

Let E'=ker(E->A_q->O(-10)), K=E^-. Only the O(-10) source block maps to that negative quotient, and its restriction is an isomorphism. Therefore

    E'=P O(-2)+2T O(-3), rank E'=16, deg E'=-44,
    E'/K=U,
    0 -> W O(-9) -> K -> 2T O(-3) -> 0.         (3)

Also I0 is contained in E': the quotient W O(-7) in (2) has zero component to E/E'=O(-10) by degrees.

Twisting (3) by9 shows that K(9) is globally generated: both outside terms are generated and H1(W O)=0. Hence every degree of K is at least -9, so Hom(K,O(-12))=0. Derivatives of K lie in E, and their possible component outside E' is precisely a map to (E/E')(-2)=O(-12). It is zero.

The derivative of E' has external saturated image U, already supplied by F, and zero internal image from K. The internal/external image lemma makes its full raw image saturated and isomorphic to U. Consequently, with G=(E')^+,

    G/E'=U(2), rank G=18, deg G=-30,
    G=E'+M                                     (4)

as actual sheaves. Its intersection M intersect E' is exactly I0. The nonzero internal derivative of F is retained in (2); it does not produce an internal component for K outside E'.

## 2. Exclude the degree-eight constant-span alternative

Suppose the full actual constant span C of M is the nine-dimensional Sym^8 W. Then

    C O/M=O(8).                                 (5)

The coherent sum S0=E'+C O is preserved by the trivial connection, by (4) and constancy of C. Its horizontal saturation is a constant subbundle. A preserved full-rank coherent lattice in a constant bundle has no divisor defect in characteristic zero: on determinants it is locally t^m O, and preservation would require m t^(m-1) dt to lie in t^m O dt, forcing m=0. Applying this to S0 in its saturation shows that S0 itself is constant.

It contains the saturated rank-eighteen G, and (5) makes its rank at most nineteen. Rank eighteen would make G constant, contrary to degree -30. Thus S0 has rank nineteen, and S0/G is a line of degree30. But the sum identity and (4) give a surjection

    O(8)=C O/M -> S0/G.

A surjection between line bundles is an isomorphism, contradicting 8!=30. Thus only the P-conic constant span could remain.

## 3. Complete four-degree support of G

Now suppose C has dimension12 and representation V+P+D. Its actual subsystem is the standard P-tensored conic. Since G=E'+M, both E'(3) and M(3) are globally generated; hence G(3) is globally generated. As G is a subbundle of a constant bundle, all its degrees are among 0,-1,-2,-3. Write

    G=c O+a O(-1)+b O(-2)+d O(-3),              (6)

where c,b are center-even representations and a,d are center-odd. The coefficient c=H0(G) is an actual constant subspace.

Equation (2) gives

    H1(I0)=P+W Sym^5 W=V+2P+D.

Indeed F and W O(-7) have no sections, and the long cohomology sequence is exact in H1. Since H0(E')=H0(M)=0, the sequence

    0 -> I0 -> E'+M (external direct sum) -> G -> 0

injects H0(G) into H1(I0). Therefore

    c <= V+2P+D                                (7)

as a subcharacter.

Taking Euler characteristics in (4), first at twist0 and then at twist1, gives

    chi_G(G)=-(V+P+D),
    chi_G(G(1))=Wp+S.

For example chi_G(E')=-(2V+3P+2D), while H0(U(2))=V+2P+D in both targets; also chi_G(E'(1))=-2T and H0(U(3))=Wp+S+2T. Combining with (6) yields

    b+d W=c+(V+P+D),
    a+c W-d=Wp+S.                              (8)

The embedded M=(Wp+T) O(-1) makes H0(G(1)) contain Wp+T. In (8), H0(G(1))=a+c W=Wp+S+d, so d must contain at least one T. Write d=T+u, with u a genuine odd representation. Since T W=V+P+D, equations (8) become

    b+u W=c,
    a=Wp+S+T+u-c W.                            (9)

These equations and (7) give a complete small support calculation, as follows. Because u W is supported by V+2P+D, the identities

    W W=1+A, W S=A+D, W Wp=P, W T=V+P+D

leave only u=m Wp+n T. Since c W contains u W^2=u+u A, the second equation in (9) forces

    u A <= Wp+S+T.

But Wp A=T and T A=Wp+S+2T. Thus n=0 and m<=1.

If u=0, the condition c W<=Wp+S+T and (7), together with

    V W=T, P W=Wp+T, D W=S+T,

gives exactly c=0,V,P,D. If u=Wp, then c contains P and c W<=2Wp+S+T, forcing c=P. Thus exactly five necessary types remain:

    i:   (Wp+S+T) O(-1)+T O(-3);
    ii:  V O+(Wp+S) O(-1)+V O(-2)+T O(-3);
    iii: P O+S O(-1)+P O(-2)+T O(-3);
    iv:  D O+Wp O(-1)+D O(-2)+T O(-3);
    v:   P O+(Wp+S) O(-1)+(Wp+T) O(-3).          (10)

Each has rank18 and degree-30. This is a complete necessary overlist for (6)-(8), not a realizability assertion or a numerical instance scan.

## 4. Four types cannot contain the actual linear first span

Consider the T O(-1) subbundle of M. In types ii-v, it has zero map to the degree-minus-one block by Schur's lemma, since those blocks contain no T. It has zero map to all degree-minus-two and degree-minus-three blocks by ordinary degrees. Its injection into G would therefore factor through the constant block c O.

The ranks of those constant blocks are respectively3,4,5,4, all strictly less than rank T=6. An injective sheaf map of rank six cannot factor through any of them. Thus types ii-v are impossible, leaving

    G=L+T O(-3),  L=(Wp+S+T) O(-1).             (11)

Here L is the canonical degree-minus-one top subbundle of G, and M is contained in L.

## 5. The remaining linear top has too small a possible constant span

Project (11) to G/L=T O(-3). The map E'->G/L is onto because G=E'+M and M is contained in L. Its F=P O(-2) component vanishes by degrees, and its map from 2T O(-3) is a nonzero constant map on the T multiplicity space. Hence its actual kernel is

    I=E' intersect L=P O(-2)+T O(-3),
    rank I=10.                                  (12)

Derivatives of I lie in G because I is contained in E'. Their possible component outside L is an O-linear map

    I -> (G/L)(-2)=T O(-5).

It vanishes by ordinary degrees using (12). Thus the derivative of I actually lies in L, and I is contained in the Gauss kernel of L. Therefore the derivative rank of L is at most12-10=2.

For a saturated pure-linear bundle, its first span is its full constant coefficient span: values and first derivatives span the coefficients. Let C_L be that constant span. The preceding actual kernel gives

    dim C_L<=14.                                (13)

Since L is a saturated negative rank-twelve subbundle, dim C_L is strictly greater than12. Otherwise L would equal a rank-twelve constant bundle. Also M is contained in L, so C_L contains its actual twelve-dimensional constant span C=V+P+D.

But C_L is a quotient of the coefficient representation

    (Wp+S+T) W=A+V+2P+2D.

After accounting for its subrepresentation C=V+P+D, any nonzero quotient C_L/C is supported by A+P+D. Every nonzero such representation has dimension at least3. Complete reducibility therefore implies either dim C_L=12 or dim C_L>=15. Both alternatives contradict the strict lower bound13 and upper bound14 from (13).

This excludes the remaining P-conic alternative, completing the onto-bb exclusion.

## Boundary and contribution

For the split label this excludes the entire bb source because PR821 rules out the nonsurjective rank-two and rank-one top cases. For the balanced label the degree-twelve torsion branch remains open. All arguments are universal exact-sequence, actual-connection and bounded abstract representation arguments. No selected HM/source coefficients, parameters, points, derivative values, matrices, instance ranks, model experiments, scans, or unapproved large computation are used.
