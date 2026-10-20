# The realized module has an explicit minimal-resolution shape

This next step uses the separately proved graded Betti theorem for P_lambda in length-sixteen-dual-presentation/PROOF.md, in addition to the symplectic construction. No actual source or global-kernel instance is used.

Work first over S=C[x1,x2,x3,x4] with P generated in degree zero. Its minimal resolution has terms

    F0=S^4,
    F1=S(-1)^10,
    F2=S(-2)^4 + S(-3)^6 + S(-5)^2,
    F3=S(-4)^4 + S(-6)^4,
    F4=S(-7)^2.

Let K=ker(F1 -> F0) and let M=K / im b for b=J L^t, with the grading b:S(-2)^4 -> F1. The four columns of b are linearly independent as degree-two syzygies: b is injective over S, so in particular there is no constant relation among its columns. The degree-two minimal syzygy space has dimension four by the displayed Betti theorem. Thus these columns are a basis of its complete degree-two part.

Consequently choose the decomposition F2=B+C with B=S(-2)^4 mapping to K exactly by b, and C=S(-3)^6+S(-5)^2. The map B -> K is injective. Projecting F3 -> B+C to C therefore yields an exact sequence

    0 -> F4 -> F3 -> C -> M -> 0.

Indeed an element of F3 mapping into B has image zero in K, and the injection B -> K forces that image in B to be zero. Such an element lies in ker(F3 -> F2)=im F4. The cokernel after projection is precisely K/b(B). There is therefore no hidden Tor correction in removing B.

All remaining differential entries have positive degree whenever nonzero. A degree-four generator in F3 cannot map to the degree-five generators of C; all other degree differences are positive. Likewise both differences from degree seven in F4 to degrees four and six in F3 are positive. The resulting resolution is minimal:

    0 -> S(-7)^2
      -> S(-4)^4 + S(-6)^4
      -> S(-3)^6 + S(-5)^2
      -> M -> 0.

In particular the realized local module has Betti numbers (8,8,2), projective dimension two and depth two. It needs eight local generators; the symplectic monad is not incorrectly being identified with a free resolution of length one.

For the centered projective cone F of GLOBAL-CONE.md, sheafify M(1) after adjoining y. Its locally free resolution is

    0 -> O(-6)^2
      -> O(-3)^4 + O(-5)^4
      -> O(-2)^6 + O(-4)^2
      -> F -> 0.

This independently checks the singular K-class, without inserting the length correction by hand:

    ch(F)=6e^(-2H)+2e^(-4H)-4e^(-3H)-4e^(-5H)+2e^(-6H)
         =2-4H^2+(47/3)H^4.

It gives c2=4 and c4=-86 exactly as the monad-plus-length calculation. Thus the construction and the independent dual-presentation Betti computation agree at the level of the full resolved K-class.
