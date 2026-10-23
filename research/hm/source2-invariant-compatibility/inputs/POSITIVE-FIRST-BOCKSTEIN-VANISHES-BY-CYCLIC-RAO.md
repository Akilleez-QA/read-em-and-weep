# The positive first Bockstein vanishes after the invariant-cone closure

## Result

Assume the now-established invariant-cone closure

    H0(B_Q0(4))_+ = N H0(O_Q0(2))_+ = N(A+D5).

Then the entire positive first Bockstein for q0+t a, a a negative quadratic, is zero. In particular the scalar gamma of the earlier conditional first-order gate is zero, rather than nonzero. This does not decide generic positive maximal rank: higher Bocksteins remain possible.

## 1. The lower kernel is the invariant nilpotent alone

Every positive section s of B_Q0(2), multiplied by any nonzero positive linear form squared, belongs to the displayed twist-four centralizer. Hence [s,N]=0, since multiplication by a nonzero polynomial cannot kill a section of a torsion-free sheaf on the integral cone. The established centralizer description, using the absence of divisorial zeros of N, then gives s=cN. Therefore

    H0(B_Q0(2))_+ = C N.

As ambient H0(B(2))=0, the restriction connecting map embeds this space into H1(B)_+. Set xi=delta_q0(N). The exact restriction sequence identifies

    ker[q0:H1(B)_+ -> H1(B(2))_+] = C xi.

## 2. A canonical first-order correction to N

The actual cohomology characters are

    H1(B)_+ = 1+A+V+D5,
    H1(B(2))_+ = A+2V+3P4+4D5.

Since the only kernel of q0 is its invariant line, q0 is injective on the unique source A and maps it isomorphically onto the unique target A. Negative quadratic multiplication sends A tensor xi into this target A. It is nonzero, indeed injective, by the established degree-two cyclic Rao injection (ambient H0(B(4))=0 and multiplication by N on the integral cone).

Consequently there is a unique equivariant map zeta:A -> H1(B)_A such that, for every negative quadratic a,

    a xi = q0 zeta_a.

Uniqueness here is in the A-isotypical summand. One could otherwise add a scalar multiple of xi for a fixed a, but equivariance excludes that ambiguity. No coefficient or rank evaluation is used.

## 3. Associativity kills every positive first obstruction

For h in H0(O_Q0(2))_+=A+D5, the corresponding actual kernel vector of q0:H1(B(2))_+ -> H1(B(4))_+ is h xi. Its first Bockstein is the class of a h xi modulo q0 H1(B(2))_+. Multiplication in the actual cohomology module is associative, so

    a h xi = h(a xi) = q0(h zeta_a).

Thus every first Bockstein is zero, including the D5-to-P4 component gamma. This is stronger than showing the first and second linear legs have nonzero vectors: those two vectors must pair to zero in this particular cyclic configuration.

## 4. A canonical second-order gate

For fixed a, the vector

    k_h(t) = h xi - t h zeta_a

solves the actual pencil equation through order one:

    (q0+t a) k_h(t) = -t^2 a h zeta_a.

The first nontrivial possible higher obstruction is therefore the actual class

    beta2_a(h xi) = -[a h zeta_a]
       in H1(B(4))_+ / q0 H1(B(2))_+ = P4.

Because beta1 is identically zero, changing a first-order correction by an element of the original kernel changes this class by zero. Thus this is the canonical second Bockstein, not a choice-dependent rank surrogate. It depends quadratically on a and linearly on h. Its vanishing or nonvanishing is not established here.

The invariant-cone rank33 result stands. The implication rank33 and gamma nonzero -> generic surjectivity remains formally correct but its gamma-nonzero premise cannot occur in the actual situation. Generic surjectivity must instead be proved at a higher order or by another geometric argument.

## Inputs and evidence

The invariant-cone closure combines NO-PRESERVING-POSITIVE-CONE-EXCESS.md with POSITIVE-CONE-MOVING-LINE-OBSTRUCTION-VANISHES.md. The spinor centralizer and N are in INVARIANT-CONE-SPINOR-FILTRATION-AND-NILPOTENT.md. The actual H1(B) character retains H2(B)=W; no assertion of concentration at twist zero is used. The unique A calculation and the multiplication identities above are the proof; the verifier checks their universal representation dimensions and formal pencil expansion only.
