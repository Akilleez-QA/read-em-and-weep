# Two graded modular divisions eliminate the actual second jet

## Hypotheses and contribution

Work over k=C(L) in the fixed harmonic frame of PR713 (commit 5b3943980ecaef78ee7f56fbc015d40955fb24f0), PR716 (2a602d811b904def02bd56518fb0549e2911ff3e), and PR724 (2061379fe77ec4c82b5f05c7a11d3b7454b97a04). Write f=f3, g=g5, n=u[[fg,-f²],[g²,-fg]], with (f,g) regular and u nonzero. Distinguish the scalar source A=a²h of degree four from f. Thus P=A n and M=A T+s n+B1(A,n), where s is a scalar in k. The first-normal matrix N=n+qT is square-zero modulo q² in the harmonic coefficient algebra. Let R have weight four and satisfy the leading q² square equation. C(P,M,R) is the eight-term cubic scalar of PR713.

The construction below eliminates R by two graded modular divisions. It supplies an exact criterion for the immutable quotient from P,M alone. It does not decide the actual base class or claim its vanishing.

Immutable dependencies:

- PR713: https://github.com/Akilleez-QA/read-em-and-weep/blob/5b3943980ecaef78ee7f56fbc015d40955fb24f0/research/hm/leading-vertex-obstruction/PROOF.md
- PR716: https://github.com/Akilleez-QA/read-em-and-weep/blob/2a602d811b904def02bd56518fb0549e2911ff3e/research/hm/firstnormal-trace-variation/PROOF.md
- PR724: https://github.com/Akilleez-QA/read-em-and-weep/blob/2061379fe77ec4c82b5f05c7a11d3b7454b97a04/research/hm/canonical-trace-isomorphism/PROOF.md

## 1. A canonical representative up to a linear splitting

Define the degree-sixteen scalar

 E=sc(M²+B1(P,M)+B1(M,P)+B2(P,P)).

The q² equation is A tr(nR)=-E. Since a regular R exists in the hypotheses, E is divisible by A. Put e=-E/(Au), a homogeneous degree-twelve polynomial. This division is justified by the equation, not by calling h a unit.

For R=[[x,y],[z,-x]], the equation becomes

 2fgx+g²y-f²z=e.                                      (1)

Here x,y,z have degrees four, two, six. Multiplication by g² gives an isomorphism

 S2 -> (S/(f))12.

Indeed it is injective because f divides g²y only if f divides y, impossible for nonzero y of degree two. Both spaces have dimension three, so it is an isomorphism. Define y* to be the unique solution of

 [g² y*]=[e] in (S/(f))12.                            (2)

Set w=(e-g²y*)/f in S9. Multiplication by 2g gives an isomorphism

 (S/(f))4 -> (S/(f))9,

by the same regularity and dimension argument. Thus there is a unique class [x*] satisfying

 [2g x*]=[w] in (S/(f))9.                            (3)

Choose any k-linear splitting of S4 -> (S/(f))4 and use it to represent x*. Define

 z*=(2g x*-w)/f,     R*=[[x*,y*],[z*,-x*]].            (4)

Every division here has been proved exact. In particular R* is regular of the required weight and solves (1). No coefficient, root, derivative, or rank of the actual pair is evaluated. This is a construction using inverse linear isomorphisms, not a numerical algorithm executed on the actual data.

Changing the splitting changes x* by f l for l in S1 and changes z* by 2g l, so changes R* by 2l [[f/2,0],[g,-f/2]]. Conversely every solution R has y=y*, and the same argument shows R-R* has precisely this form. Thus R* together with all these kernel translations exhausts the affine solution space. Varying a linear splitting need not itself produce every translation, for example when [x*]=0; no such assertion is needed.

By PR716 and PR724, C(P,M,R*) is divisible by h if one actual base numerator is; its change under any other splitting lies in a²h f S5. Hence

 K(P,M)=[C(P,M,R*)/(a h)] in (S/(f))8                (5)

is independent of the splitting and equals the immutable quotient π(r0). Formula (5), with (2)-(4), is an exact actual-R-free test. It makes no claim that K(P,M) vanishes. In particular local cancellation exists exactly when K(P,M)=0; when it does exist, PR724 gives the unique cancelling direction. The actual global R remains fixed under the previously classified completion changes.


## Remaining dependency
The value of (5) for the actual input remains unevaluated. This construction does not imply its vanishing.
