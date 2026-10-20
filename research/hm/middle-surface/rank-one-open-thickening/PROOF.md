# Actual square-zero structure on the rank-ten open

## Theorem

Work over C in the canonical cubic setup. Let M=V^3=A^15, X=V(f), and D the rank-one component, of dimension seven. Let R⊂D be the open locus with all three inputs nonzero. The repeated-input theorem gives linear normal rank four on R. Write Q for the quadratic normal map from the rank-ten symmetric square of the residual rank-four normal bundle to the rank-sixteen target quotient, and put

    U={d∈R : rank Q_d=10}.

The generic rank-ten theorem /research/hm/local-defect/rank-eight-global-exclusion/PROOF.md makes U nonempty and dense. Then:

1. There is an ambient open W with W∩D=U such that T=X∩W has reduced scheme U. Its nilradical N satisfies N²=0 and is a vector bundle of rank four on U.
2. Canonically, N is the cokernel of df*:J*⊗O_U→N*_(D/M)|_U. The image has rank four and the ambient conormal rank eight.
3. Zariski locally, T is the split square-zero thickening Spec_U(O_U⊕N). These local retractions are finite flat of degree five. A global retraction is not asserted; if one exists, it is finite flat of degree five and splits T globally.
4. No other irreducible component of X meets U. Thus intersections of other components with R are contained in the actual determinantal locus rank Q≤9, without an additional unexplained shrinking of U.
5. T is Cohen–Macaulay of type four, nowhere Gorenstein or a local complete intersection. At a closed point it has dimension seven and tangent dimension eleven. Its ambient ideal has fourteen minimal generators: four linear-normal equations and ten quadratic residual equations. Its component cycle is 5[U].

This upgrades a generic Artinian normal form to actual open scheme structure. 

## 1. Pointwise coherent Nakayama lemma

Let D⊂Y be a regular embedding in a noetherian scheme, with ideal P, and let J⊂P² be coherent. Suppose at d∈D the quadratic classes of J generate P²/P³. Then

    (P²)_d=J_d+(P³)_d.

The finite O_(Y,d)-module C=(P²/J)_d satisfies C=P_d C. Since P_d lies in the maximal ideal, Nakayama gives C=0. Thus J_d=(P²)_d, and coherence gives equality on a neighborhood of d in Y. If surjectivity is initially given on the residue-field fiber, first apply Nakayama over O_(D,d) to the cokernel of the map to P²/P³.

Conversely J_d=(P²)_d forces quadratic surjectivity. This is an exact criterion in the eliminated presentation. It uses neither completion nor an assumed flatness or prior isolation of a component.

## 2. Exact Zariski algebraic elimination supplies the hypotheses

Use /research/hm/local-defect/rank-one-normal-obstruction/PROOF.md, Sections 1–2. This precedes the formal even-coordinate presentation, and importantly gives an exact rational elimination valid at every point of R.

Choose ell nonzero on the common line, H=ker ell, and ambient coordinates

    (x,y,z)=(s(u+p),u,t(u-p+w)),

where ell(u),s,t are invertible and p,w∈H. The seven base coordinates are (u,s,t); D is p=w=0. Set

    A_u(w)=f(u,u,w), B_(u,p)(w)=f(p,u,w), F_u(p)=f(p,u,p).

The repeated-input injection makes A a locally split rank-four subbundle. Choose local target projections (L,pi) with LA=1 and pi A=0. The exact equation (A+B)w-F=0 has four equations

    (1+LB)w=LF.

The determinant of 1+LB equals one along p=0. Therefore on an ambient Zariski open containing the local zero section these equations give the actual algebraic graph

    w=(1+LB)^(-1)LF.

Its ambient space Y has dimension eleven. The remaining sixteen equations generate the ideal J with vector of generators

    G=pi B(1+LB)^(-1)LF-pi F.

For P=(p1,p2,p3,p4), one has J⊂P² and G mod P³=-pi F, precisely the quadratic normal equations. At d∈U these span all of Sym²(P/P²), of rank ten. Section 1 proves J=P² near d.

Thus locally in the fifteen-dimensional ambient space,

    I_X=I_Y + a lift of I_(D/Y)^2.

This is the correct squared-ideal statement. It is NOT I_X=I_(D/M)^2: the latter has eight surviving normal variables and omits the four independent linear normal equations. The four eliminated equations and the ten quadratic residual equations are essential.

## 3. Gluing and canonical nilradical

Take the union of the neighborhoods obtained at every d∈U, shrinking each neighborhood's intersection with D into U. This gives W as in the theorem. Locally the reduced scheme of X is exactly D, so T_red=U. The ideals I_D/I_X glue because they are ideals of the same open subscheme of X; they are its nilradical N. Locally N²=0 and hence globally N²=0.

The natural surjection of conormal bundles is

    I_D/I_D² → I_D/I_X=N.

It exists because I_D²⊂I_X locally, as follows from Section 2. Its kernel is precisely the linear-normal image of the defining equations f, namely im(df*). Thus

    0→im(df*)→N*_(D/M)|_U→N→0

is exact. The image is a subbundle of rank four by constant linear rank, giving the canonical rank-four residual conormal description. It is independent of coordinates and target splittings.

If a distinct irreducible component C of X met U, its nonempty open portion C∩W would lie in D. Its closure would force C⊂D, contradicting maximality as a distinct component. This proves component separation pointwise on the whole rank-ten locus.

The complement in R is defined by the maximal minors of Q. Under the bundle identifications of /research/hm/middle-surface/rank-ten-fitting-strata/PROOF.md it is the inverse image under R→P(V), taking the common line, of V(Fitt_0(S)), where S is that paper's sheaf Ext¹ of the rank-six quotient. No new codimension bound is claimed.

The boundary D\R contains triples with a zero input, not only the vertex. The unconditional intersection statement here is C∩R⊂{rank Q≤9}. An extension to boundary points requires the hypotheses of Section 6 there; those hypotheses are not silently assumed.

## 4. Local splitting and the global obstruction

The exact coordinates provide a genuine retraction to (u,s,t). After shrinking and trivializing the residual normal bundle,

    O_T ≅ O_U[p1,p2,p3,p4]/(p1,p2,p3,p4)^2.

This is Zariski algebraic, not merely formal or etale. Shrinking an ambient neighborhood away from a closed subset disjoint from the zero section does not change its square-zero infinitesimal neighborhood.

Globally the exact sequence of C-algebra sheaves

    0→N→O_T→O_U→0

does not itself give an O_U-algebra structure on O_T. A retraction is a section of this quotient. Once chosen, it gives O_T=O_U⊕N with square-zero multiplication on N. This proves finite flatness of degree five for that retraction, but does not manufacture a global retraction.

Since U is smooth, local splittings differ by C-derivations O_U→N, or sections of T_U⊗N. Their differences give the obstruction class in H¹(U,T_U⊗N). Its vanishing is equivalent to a global splitting; when it vanishes, splittings form a torsor under H⁰(U,T_U⊗N). In particular a splitting exists on every affine open, but is not canonical. We neither evaluate the class nor assert that it is nonzero.

## 5. Local ring and cycle consequences

Let A be a regular local ring on U and B=A[p1,p2,p3,p4]/(p)². As an A-module B is free of rank five. A regular system of parameters of A remains B-regular, and B has the same dimension as A, so B is Cohen–Macaulay. Modulo these parameters the Artinian quotient is k⊕k⁴ with square-zero maximal ideal; its socle has dimension four. Thus the Cohen–Macaulay type is four and B is not Gorenstein.

The residual ideal has ten minimal quadratic generators p_i p_j, i≤j, and height four, hence is not a complete intersection. The full ambient ideal has four further independent linear-normal generators, hence fourteen minimal generators and height eight. At a closed point the linear equations cut tangent dimension fifteen down to eleven. At the generic point the length is five, so the component cycle is 5[U].

## 6. Abstract extension criterion and topology distinctions

More generally, let D⊂X⊂M with D and M smooth. Suppose on an open of D that the first normal derivatives of the equations of X have constant rank a, and their residual quadratic normal equations span the full symmetric square of the remaining conormal bundle. Choose a defining equations with independent conormal classes. Their zero scheme Y is smooth of codimension a near D. In Y the remaining ideal J lies in I_(D/Y)², since its first conormal classes vanish along D. Section 1 gives

    J=I_(D/Y)²

Zariski locally. The reduction is therefore D, with square-zero nilradical the residual conormal bundle; other components cannot meet there.

This equality does not in general identify the ambient pair (Y,D) Zariski locally with a normal bundle. Etale or formal tubular coordinates must not be called Zariski ambient coordinates. Nevertheless the abstract square-zero thickening splits Zariski locally: on an affine smooth open of D, formal smoothness lifts its coordinate algebra across the square-zero quotient. In the canonical all-nonzero chart Section 2 already supplies explicit algebraic elimination and a base retraction.

## Novelty and scope check

The prior even-normal-form packet determines the generic algebra; the global-exclusion packet fixes its length. The full-neighborhood packet gives exact elimination and only a normal-cone inclusion. The new step is coherent Nakayama on the whole rank-ten open, with actual scheme equality, canonical nilradical, component separation, splitting distinction and local algebra consequences. 

Nothing here computes a source value, proves global splitting, trivializes N globally, classifies the exceptional locus or settles higher module/connection quantization. 

## 7. Exact characterization of the good locus

Within R, U is exactly the locus at which the germ of X is a square-zero thickening of D. The forward direction is proved above. Conversely, suppose at d∈R that the reduced germ of X is D and that its nilradical has square zero. In the exact eliminated presentation this nilradical is P/J, so its square zero gives P²⊂J. The universal inclusion J⊂P² then forces equality, and hence all ten quadratic normal monomials lie in the span of the quadratic equations. Thus rank Q_d=10. This converse requires the stated reduced-support hypothesis; it says nothing analogous about the nilradical of a germ whose reduction has extra components.
