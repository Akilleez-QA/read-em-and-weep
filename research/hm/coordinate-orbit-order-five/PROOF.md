# Order-five vanishing on the binary-quartic coordinate orbit

Work over C. The HM bundle F and its coefficient-space coordinates remain fixed throughout. Only the binary-quartic root map and its coefficient pair are translated. This is a structural existence theorem on a restricted algebraic family, not an evaluation of the original source instance.

## Dependencies and notation

- [PR139](https://github.com/Akilleez-QA/read-em-and-weep/pull/139), commit `c5fb4a0bcc3c8e35093fcfcff9a73a79a45a18e5`, identifies the universal pair as u0=12I and v0=6J, the degree-two and degree-three binary-quartic invariants.
- [PR441](https://github.com/Akilleez-QA/read-em-and-weep/pull/441), commit `6d81d9500f42ae31bef6d3150cf3ba513c28502b`, and [PR443](https://github.com/Akilleez-QA/read-em-and-weep/pull/443), commit `bc5a8ba31104bc66b180984a1fdfc7f17ceb1eef`, fix the transport convention q_g=g composed with q0 and (u_g,v_g)=((g inverse)*u0,(g inverse)*v0). The bundle F is not transported.
- [PR449](https://github.com/Akilleez-QA/read-em-and-weep/pull/449), commit `e4b6acdd27d8da8be4052c117ea2dca0f48f46ff`, gives a nonempty open of quadrics with uM1=M3.
- [PR458](https://github.com/Akilleez-QA/read-em-and-weep/pull/458), commit `b46c3b48a8b10a7d0656fde247f2c3f258d1fd23`, identifies the residual dual and injects it into W intersect (u,v)_5 when u,v are coprime and no component line of C lies in both zero loci. Here C is the union of the 25 HM jumping lines and W=H0(I_C(5)) has dimension six.
- [PR459](https://github.com/Akilleez-QA/read-em-and-weep/pull/459), commit `0d4dcd49536c229ce0a602c6c3d37cf821ce85a5`, proves the requisite nonempty quadratic open and full independent-coefficient genericity. It does not prove compatibility with the coordinate orbit; that is the new conclusion here.
- [PR451](https://github.com/Akilleez-QA/read-em-and-weep/pull/451), commit `ed8841c18f103e71b84c0e9376e20a2a4ed2ef9c`, identifies the paired order-five dual cohomology with two copies of Q5 for the transported root geometry.

Write S=C[x0,...,x4], B=End_0(F), and

    Q5(u,v)=H1(B(5))/(u H1(B(3))+v H1(B(2))).

## 1. A projective-frame separation lemma

Let W be any r-dimensional subspace of H0(P^n,O(d)), with r at most n+2. Let N be a closed subscheme of P^n whose support contains r points extendible to a projective frame. Then a nonempty Zariski-open subset of PGL(n+1) satisfies

    W intersect H0(I_{gN}(d)) = 0.

Proof. Evaluations at closed points span W*: a section annihilated by every evaluation is zero. Thus some ordered r-tuple has independent evaluations. Independence is open in (P^n)^r. The locus of r-tuples extendible to a projective frame is also nonempty open. These two opens meet because (P^n)^r is irreducible. Fix r frame points on N and such a target tuple. Extend both to frames and use transitivity of PGL(n+1) on ordered frames. The resulting g sends the source points to points whose evaluations on W are independent. A section vanishing on gN therefore vanishes at all these points and is zero. Finally, independence of these same r moving-point evaluations is a nonempty open condition on g. This proves the assertion without assuming N reduced or identifying its ideal generators. QED.

## 2. The universal binary-quartic pair has a frame in its zero locus

Set N0=V(u0,v0) in P(Sym^4 C^2). The rational normal quartic R of pure fourth powers is contained in N0. Indeed, I and J are homogeneous SL2-invariant polynomials of positive degree. A diagonal torus scales a highest-weight pure fourth power by arbitrary nonzero scalars. Invariance and positive homogeneity force both invariants to vanish there. SL2 transitivity on P^1 gives the assertion on all of R.

Any six distinct points of R form a projective frame in P^4: any five are linearly independent by degree-four interpolation on P^1. This is a universal geometric statement, with no chosen HM coefficient evaluation.

The pair u0,v0 is coprime. The invariant quadratic I is nondegenerate, as established in PR441, hence irreducible. If J=I times a linear form, invariance and cancellation in the polynomial domain would make that linear form SL2-invariant. The irreducible nontrivial representation Sym^4 C^2 has no invariant linear forms. Since J is a nonzero invariant, this is impossible. Coprimality is preserved by every coordinate change.

## 3. Coordinate-orbit compatibility

Apply Section 1 with n=4, d=5, r=6 and W=H0(I_C(5)). Section 2 supplies the source frame. Thus a nonempty open U_sep in PGL5 satisfies

    W intersect H0(I_{gN0}(5)) = 0.

In particular W intersect (u_g,v_g)_5=0; only containment of the degree-five ideal piece in the scheme ideal is needed.

A second nonempty open U_pr consists of g for which u_g M1=M3. Indeed, u0 is nondegenerate, its projective orbit is the entire smooth-quadric locus, and the primary-good open from PR449 meets that locus. A third nonempty open U_lines consists of g for which u_g contains none of the 25 component lines of C. For each fixed line, containment is a proper closed condition on smooth quadrics, so finitely many such conditions cannot exhaust the smooth-quadric locus.

PGL5 is irreducible. Consequently U=U_sep intersect U_pr intersect U_lines is nonempty open. For every g in U, coprimality holds by Section 2, no component line lies in both zero loci, and PR458 injects the residual dual into the zero space W intersect (u_g,v_g)_5. Thus the residual quotient vanishes. Primary coverage u_g M1=M3 kills the remaining primary quotient by the exact sequence of PR458. Therefore

    Q5(u_g,v_g)=0  for every g in U.

This proves generic order-five vanishing on the actual simultaneous coordinate orbit of the binary-quartic pair. It is strictly more restrictive than choosing u and v independently. By the transport and endpoint identifications in PR441/PR451, the paired order-five ideal-power cohomology also vanishes for these translated root maps with F fixed.

## 4. An algebraic one-parameter family through the original geometry

The good locus can be approached in an algebraic family passing through the original root map, without evaluating its special fiber. Choose g in U and a matrix lift G in GL5. Put H(t)=Id+t(G-Id) and let T be the principal open subset of A^1 where det H(t) is nonzero. Both 0 and 1 belong to T. The projective classes h(t) define a regular map T to PGL5, with h(0)=identity and h(1)=g.

The inverse image of U is a nonempty open subset of T, hence its complement in T is finite. Therefore the family q_t=h(t) composed with q0, with u_t=(h(t) inverse)*u0 and v_t=(h(t) inverse)*v0, has Q5(u_t,v_t)=0 outside finitely many parameters. This is an existential algebraic family, not a coefficient search or a selected matrix computation. It gives no conclusion about t=0 and no bound on a possible special-fiber torsion length.

## Scope and verification

The new conclusions are coordinate-orbit compatibility and an algebraic family through the original geometry with generic order-five vanishing. They do not prove vanishing for the original fixed pair (u0,v0), actual retained mixed source values, lower-order obstruction vanishing, or existence/algebraicity of a quantization or module. Arbitrary projective transformations do not preserve F, and no such preservation is used.

This proof is structural: projective-frame transitivity, evaluation separation, invariant-theoretic coprimality, and intersection of nonempty opens. No selected actual HM/source instance was evaluated, and no numerical ranks, matrices, generators, checkers, coefficient searches or large computation were used. The argument is authored mathematics, not a formally machine-checked theorem.
