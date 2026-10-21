# Reduced proof of uniform sextic interpolation and exact linear failure

We prove that the reduced failure locus of linear multiplication H¹B(4) -> H¹B(5) is exactly the union of the 25 dual planes of the HM component lines. The proof supplies a shorter dependency chain for the proper-section spanning input from PR474. It uses the primary monad and representations, transverse evaluation geometry, and PR538's actual image sequence. It does not use the complete Rao resolution, Betti numbers, the exact six-dimensional exceptional defect, quintic saturation dimension, or Cayley–Bacharach.

## 1. Direct negative-twist Bott calculation

Let V be the five-dimensional ambient Schrödinger representation, T=V*, A=V_1, W the monad two-space, and W' its conjugate. Put Q for the universal rank-four quotient and J=Lambda²Q*=Omega²(2). The normalized monad is A O(-1) -> W tensor J -> A* O, with cohomology F. Its graded symmetric square computes Sym²F=B(-1). In degrees -2,-1,0,1,2 the terms are

Lambda²A O(-2),
A tensor W tensor J(-1),
Sym²(W tensor J) directsum End(A) O(-1),
W tensor A* tensor J,
Lambda²A* O.

The negative line bundles and J(-1)=Omega²(1), J=Omega²(2) are acyclic. The central decomposition is

Sym²(W tensor J)=(Sym²W tensor Sym²J) directsum (Lambda²W tensor Lambda²J),
Sym²J=S_(2,2)Q* directsum Lambda⁴Q*,
Lambda²J=S_(2,1,1)Q*.

For S_(2,2)Q*, the shifted Bott weights are (4,5,4,1,0), with a repeated4, so the bundle is acyclic; Lambda⁴Q*=O(-1) is also acyclic. For S_(2,1,1)Q*, the weights (4,5,3,2,0) require exactly one transposition. Subtracting rho after sorting gives (1,1,1,1,0), so its only cohomology is H¹=Lambda⁴V*=V. Since Lambda²W is trivial, the sole central cohomology term is V in bidegree(0,1). The sole other E1 term is Lambda²A*=V tensor W' in bidegree(2,0).

The only possible nonzero higher differential is d2:V -> V tensor W'. The target is irreducible under the normalizer by the primary H-isotypic criterion; its dimension is10, whereas the source has dimension5. Thus this equivariant map is zero. There are no other possible differentials touching total degree1. Therefore

H¹B(-1)=V.

No matrix entries or numerical rank have been used.

## 2. The image sequence and absence of a scalar target

Use the actual EN sequence of PR538, with K_j=H¹B(j-1), M_d=H¹I_C(d), P_D,j=D tensor M_(6-j)* and D=det U, U=H⁰E. At j=0 the primary term and exception vanish, so

P_D,0=K_0=V.

The section representation U is a four-dimensional irreducible representation of SL₂(F5), H acts trivially, and its determinant is trivial because SL₂(F5) is perfect. Thus D is trivial, and M_6=V*.

At j=1, PR538 gives

0 -> H¹B(0) -> P_D,1 -> Q_exc ->0,
Q_exc subset U tensor H²F(-2).

The rightmost containing representation has no trivial normalizer constituent: U is irreducible of dimension4 and H²F(-2) is irreducible of dimension2; a trivial tensor constituent would give a nonzero homomorphism between these inequivalent irreducibles.

For completeness the left term also has no invariants. Twist the symmetric-square monad of Section1 by one to compute B(0). Bott gives no positive cohomology in any term; the central Schur weights (5,5,4,1,0) and (5,5,3,2,0) repeat, while Lambda⁴Q*(1)=O. The representation label in the middle is the same W, not W′: HM Section2 (printed pp67–68) defines W=Hom_H(A,Lambda²V), hence Lambda²V=A tensor W, and uses W in the monad. Since det V=1, H⁰Omega²(3)=Lambda³V*=Lambda²V=A tensor W. Thus the degree-one global sections are W tensor A* tensor (A tensor W)=End(A) tensor (W tensor W). Its H-invariants are W tensor W=1 directsum Sym²W. The conjugate W′ enters only the final term Lambda²A* tensor V*=End(V) tensor W′. Consequently the complex of H-invariant global sections in degrees0,1,2 is

1 directsum Sym²W -> 1 directsum Sym²W -> W'.

Simplicity of F gives H⁰B(0)=0. Therefore the first arrow is injective, hence an isomorphism between the two four-dimensional terms. The next arrow is zero by irreducible types. Consequently H¹B(0)^H=0, in particular H¹B(0)^N=0. Exactness of finite-group invariants now gives

(P_D,1)^N=0.

This step does not require h¹B(0)=24 or dim Q_exc=6.

## 3. The actual top Rao multiplication has only the scalar kernel

For all d the restriction sequence gives M_d=coker[S_d -> H⁰O_C(d)]. The section module is the direct sum of S/I_l over the25 lines. Hence M is generated in degree0; in particular S_1 M_5=M_6. Since M_6=V* is nonzero, the transpose contraction

c:T tensor P_D,0 -> P_D,1

is nonzero. Its source is V* tensor V=1 directsum Ad(V), with the24-dimensional adjoint part irreducible under the normalizer (the24 nontrivial Heisenberg characters form a transitive orbit). Its scalar summand maps to zero by Section2, and its adjoint summand maps injectively by irreducibility. Thus ker c is exactly the scalar identity line.

For a fixed nonzero ell in T, the restriction p -> c(ell tensor p) is injective: a nonzero decomposable tensor has rank1 as an endomorphism, whereas a nonzero scalar identity has rank5. Dualizing yields

ell:M_5 -> M_6 onto for EVERY nonzero ell.

This proof does not import the top multiplication conclusion of PR471/472; it reconstructs it through a shorter dependency chain.

## 4. Uniform sextic interpolation for proper sections

If H=(ell=0) contains no component line, D=C intersect H consists of25 distinct reduced points. The ideal restriction sequence

0 -> I_C(5) --ell--> I_C(6) -> I_(D,H)(6) ->0

is exact, since ell is a nonzerodivisor on O_C. Its cohomology has final term H²I_C(5)=H¹O_C(5)=0. Therefore H¹I_(D,H)(6)=coker[ell:M_5->M_6]=0 by Section3. Equivalently h_D(6)=25.

## 5. A short nonplanarity proof without residual duality

Suppose D were contained in a plane Pi inside H. No component of C is contained in Pi, and C intersect Pi is exactly the same reduced set D. The six evaluation minors generate I_C(5) as a SHEAF by the transverse EN presentation. Restrict their sheaf surjection to Pi and take the image in O_Pi(5). Its image is I_D,Pi(5), even though tensoring may have a Tor kernel. Thus the resulting linear system of plane quintics has scheme-theoretic base locus exactly D, with no fixed curve.

Choose two members f,g with no common curve: after choosing nonzero f, exclude the finitely many proper subspaces of members divisible by its irreducible factors. Their plane complete intersection Z contains D. The Koszul resolution gives h_Z(6)=28-2*3=22. But D subset Z implies h_D(6)<=h_Z(6), while Section4 gives h_D(6)=25 (evaluation on H equals evaluation on Pi because D lies in Pi). Contradiction. Therefore every proper hyperplane section spans its H.

Only the preliminary complete-intersection bound22 was needed. The sharper19 bound, Cayley–Bacharach identity, and lower Rao multiplication ranks are unnecessary here.

## 6. Exact full linear failure classification

PR532's actual residue identification for j=4,5 makes the dual residual linear map [lambda] -> [lambda ell|C]. For proper H, Section5 shows that any compatible global linear form vanishing on D is a multiple of ell, so this map is injective. If H contains a component, a constant tuple supported on it gives a nonzero kernel class. Hence residual surjectivity holds exactly for proper H.

PR450 Section2 proves the natural contraction S_1 tensor H¹F(3)* -> H¹F(2)* is an isomorphism. Restricting to each nonzero ell makes the primary linear map H¹F(2)->H¹F(3) onto. Naturality of cups makes P_4->P_5 onto, and the primary/residual exact sequences identify full and residual cokernels. Consequently

ell:H¹B(4)->H¹B(5) onto iff H contains no component of C.

The reduced failure locus is the union of25 distinct P²'s in P(S_1)=P⁴, parametrizing hyperplanes containing each component. No determinantal multiplicities are asserted.

## Dependency boundary

The primary inputs still required are the normalized monad, its standard irreducible normalizer identities and simplicity, the two-dimensional primary H²F(-2), the four-dimensional section representation, and transverse evaluation geometry. They are not replaced by a numerical table. PR538's actual image sequence is used at its original pin d5d9bd997145b0ecf7d7bd659a19fb7845afb75f; the later exact-defect refinement is unnecessary. PR450's contraction is used independently of its endpoint-resolution proof. Bott calculations are displayed above. The generic quadratic-alone theorem in LOWER-DEGREE.md does not depend on this closure.

No selected HM/source-instance evaluation, multiplication matrix, numerical rank experiment, original fixed-pair membership, or higher lifting conclusion is involved.

## Verified sources

- Original actual EN/image extension, not its later numerical refinement: https://github.com/Akilleez-QA/read-em-and-weep/blob/d5d9bd997145b0ecf7d7bd659a19fb7845afb75f/research/hm/actual-primary-image-extension/PROOF.md
- Actual residue model: https://github.com/Akilleez-QA/read-em-and-weep/blob/5f08a072fa8d3bdf12007a6aab2f374c85c5e503/research/hm/residue-restriction-ambiguity/PROOF.md
- Primary contraction, PR450 at54d1eafe617e042edc452cb66edb8e4f7c78d2bf, Section2: https://github.com/Akilleez-QA/read-em-and-weep/pull/450
- Horrocks–Mumford primary monad, group representations, and primary cohomology: https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf

## Target-dimension independence check

The proof never substitutes a dimension for M_5, P_D,1, H¹B(0), or Q_exc. Their necessary property is absence of a trivial normalizer constituent, proved by the invariant complex and the embedding of Q_exc into a4-by2 tensor representation. Nonzero top multiplication is forced by degree-zero generation and M_6=V*, not by target-dimension subtraction. The irreducible24-dimensional source summand is injective into P_D,1 regardless of its dimension. The later full linear conclusion uses only surjectivity of the primary and residual maps, not dimensions of H¹B(4) or H¹B(5). The number25 appears geometrically as the number of components, and22 is the Hilbert function of a plane(5,5) complete intersection. These are not hidden selected-rank premises.

The proper-section nonplanarity argument is the preliminary bound of PR474 Section 2 at 366f1acc08e23d6111fe310ae149c9636ebebb0e, rederived here after independently closing its interpolation premise. Neither that geometric assertion nor the uniform top-Rao map is claimed new. The new conclusion is the exact failure classification for the full adjoint linear map, together with its reduced geometric locus. This is mathematical verification, not proof-assistant certification.
