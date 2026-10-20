# A 5,192-index complete retained detector family

This refines, without replacing, PROOF.md and its twenty-value cubic basis. It uses only scalar commutativity, symmetric coefficient products, and character-forced vanishings. A surviving indexed detector is not asserted nonzero. No numerical pivot or minimal twelve-element selection is made.

## 1. First reduction by commutativity: 9,900 indices

Keep the twenty triples (u_t,v_t,w_t), their cubic basis values B_t, coordinate sections x_l, coefficient basis c_r, canonical lift j, and retained projector P of PROOF.md.

For upper values retain only r≤s. Their upper symbols depend on the symmetric product mu11(c_r,c_s), so these 66 products still span C2. This reduces the upper family to 20·5·66=6,600 indices. The full upstairs upper values for (r,s) and (s,r) need not agree: their difference has zero upper symbol and can lie in the lower retained subspace, which the lower family already spans.

For lower values retain only l≤h. Scalar linearity gives the exact downstairs equality

    m001(x_l u_t,x_h v_t,w_t)
      =x_l x_h B_t
      =m001(x_h u_t,x_l v_t,w_t).

Exact lower transfer identifies their retained upstairs values, not just their symbols: the difference lies in retained filtration zero, which is zero because that filtration is S4-trivial and P contains e_[22]. Thus the 15 unordered coordinate pairs suffice, giving 20·15·11=3,300 lower indices. The union of these two families has 9,900 indices and still spans Tret.

## 2. The ten J1 weights and their reversal signs

The literal output plane W has quadratic-diagonal characters beta² and beta³, as recorded by the diagonal lift and the explicit J2 quotient. Its alpha character is trivial. The historical Galois operation theta sends fifth-root characters to their squares and W to W′. Hence W′ has beta characters beta and beta⁴, i.e. offsets ±1. Passing between the usual and opposite actions negates these pairs and leaves their sets unchanged.

The lower-image proof gives J1=V⊗W′. In the current opposite-cochain convention V has the derivative weights (-i,-i²). Therefore J1 has exactly the ten distinct one-dimensional weights

    (c,4c²+epsilon),  c in F5, epsilon in {1,4}.

This assertion follows from the established module identification and literal diagonal characters; it is not inferred from the dimension ten alone.

For the stipulated reversal R:i↦4-i, a twist-minus-one weight has first coordinate c↦1-c, and its offset epsilon is unchanged. One can see this directly from V and from R's central action on W′, which commutes with its diagonal restriction. Equivalently, substitution into the quadratic-character transport gives this formula. There are two fixed lines, those with c=3; the other eight lines are exchanged in four pairs and contribute zero trace. The imported involution trace on J1 is -2. Thus both fixed lines have eigenvalue -1. Their positive projection is zero. No sign on an individual nonfixed line is needed.

Sources: [the lower weight image symmetry manuscript](../../foundation-p05b/LOWER-TRANSFER.md), Sections 1–2 and 4; [the filtered massey target manuscript](../../foundation-p04/FILTERED-TARGET.md), Section 4; [the derivative transgression relations manuscript](../../../derivative-transgression-relations/EXPLICIT-COEFFICIENT-QUOTIENT.md), Section 2; [the diagonal symmetry classification manuscript](../../foundation-p02/DIAGONAL.md), the literal diagonal lifts.

## 3. Upper pruning: 64 coordinate indices

Label each B_t by its unique weight

    wt(B_t)=(a,3a²+delta),  delta≠0.

For R_(i,d), these labels are a=2i-d and delta=d². For A_(m,d), they are a=2m and delta=3d². Thus every one of the twenty pairs (a,delta) occurs exactly once.

The coordinate x_l has weight (l,l²), so x_l B_t has first coordinate b=a+l and J2 offset

    eta=3a²+delta+l²-2(a+l)²
       =delta-(l-3a)².

If eta=0 the J2 character is absent and the multiplication is zero. If b=1 the target J2 line is reversal-negative by the explicit J2 quotient theorem. Its positive projection is therefore zero.

Keep precisely the upper coordinate indices satisfying

    delta-(l-3a)² != 0,     a+l != 1.

There are 80 indices after the first condition: for each a and each square delta, precisely two l are excluded, while nonsquare delta excludes none. This is 5·(3+3+5+5)=80.

The second condition discards 16 of these. For l=1-a the excluded offset would be delta-(1+a)². If a=4, all four nonzero deltas survive the first condition; for each of the other four a, exactly three survive. Hence 4+4·3=16, leaving 64.

Using all r≤s with these indices gives 64·66=4,224 upper indexed detectors. Removed values have zero upper retained symbol. Their possible lower components are irrelevant because the retained lower subspace remains spanned by the lower family.

## 4. Lower pruning: 88 unordered coordinate indices

For l≤h in the ordinary ordering 0,...,4, put

    c=a+l+h,
    epsilon=3a²+delta+l²+h²+c².

The twice-multiplied value x_l x_h B_t has weight (c,4c²+epsilon). By Section 2 it vanishes if epsilon is not 1 or 4, and its positive projection vanishes if c=3.

Keep precisely the lower coordinate indices satisfying

    epsilon in {1,4},     c != 3.

One may also test both intermediate multiplication conditions, but these are redundant. If, for example, delta=(l-3a)², set b=a+l. Then direct formal substitution gives

    epsilon=2(h+3b)²,

which lies in {0,2,3} and cannot pass the final-target test. The same argument applies with l,h interchanged.

Here is a purely symbolic count, independent of any cohomology value. For each prescribed c, translation of the index labels reduces the count to c=0 while preserving delta and epsilon. Regard {l,h} as an unordered pair, write s=l+h and z=l-h up to sign, and set a=-s. Then

    epsilon=delta+s²+3z².

The possibilities z²=0,1,4 parameterize the three difference types, and each s∈F5 gives exactly one unordered pair of a given difference type. For delta=1,2,3,4 the numbers with epsilon∈{1,4}, summed over the three difference types, are respectively

    4, 7, 7, 4.

More explicitly the counts for z²=0,1,4 are respectively (1,1,2), (2,4,1), (2,1,4), and (1,2,1). Thus each c contributes 22 eligible indices. All five c give 110. Removing c=3 leaves 4·22=88.

Using all eleven coefficient basis vectors gives 88·11=968 lower indexed detectors. Every removed lower detector is zero after P, since lower transfer is exact and the projected filtration-zero ambiguity vanishes. Therefore the remaining lower family still spans the entire four-dimensional lower subspace.

## 5. Final family and conclusion

The family consists of:

    P M(x_l u_t, j(c_r⊗v_t), j(c_s⊗w_t))

for r≤s and the two upper predicates of Section 3; and

    P M(x_l u_t, x_h v_t, j(c_r⊗w_t))

for l≤h and the two lower predicates of Section 4.

Its indexed size is

    4,224 + 968 = 5,192.

Its lower values span the canonical four-dimensional retained subspace. Its upper symbols span the eight-dimensional quotient. The union therefore spans all twelve retained dimensions, without a complement or a numerical pivot. Pairing against this finite family detects zero of a physical retained class by the imported perfect sign-valued Serre pairing. Nothing here evaluates those pairings or decides an actual physical class.

