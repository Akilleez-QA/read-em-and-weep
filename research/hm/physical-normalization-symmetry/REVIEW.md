# Independent final-byte mathematical review

Date: 2026-10-23. Verdict: PASS, conditional universal theorem as stated.
No mathematical correction is required in the reviewed proof or checker.
This is an independent written review, not Lean certification or authentication
of an actual physical response packet.

## Reviewed bytes and source authentication

The exact reviewed files have SHA-256 hashes:

- `PROOF.md`: `cf85d577d57f3b08369045b99599738498f0caf1fc0e45009a6d2bf227c95b22`
- `verify_symmetry_calibration.py`: `1da0bb9fec2aff05d8b30a43fd7bc257ddfa6ee6c109699916fff83f252c5f8e`
- `SOURCE-MANIFEST.json`: `09d9c776843bd07f7b9ffda5d77d423287aa330bae31a887153ee2c2184fb2f8`

Independently recomputed the byte count, SHA-256, and Git blob SHA-1 of each
of the six `inputs/*.md` files, using the Git `blob <length>\0` prefix. All
six agree exactly with the manifest. The manifest pins immutable repository
commits and paths; this review uses those exact copied source bytes, rather
than an unpinned current branch or unprovided upstream reference.

## Independent checks of the specialized mathematical advance

1. **The positive representation is not interchangeable with the negative
   one.** The multiplied-lift input identifies `U=Wprime`, while the
   next-weight input gives `Sym^12 U=1+V+P4+D5`. With `A=Sym^2 W` and
   `V=Sym^2 U`, replacing U by W swaps the two inequivalent three-spaces
   and is not allowed. Central parity is +1 on all thirteen trace
   coefficients, so it cannot itself reduce that space.

2. **The family hypothesis is genuinely additional.** An equivariant map
   satisfies `eta(ga,gh)=g eta(a,h)`, not invariance of its value at fixed
   non-invariant inputs. The pinned PR815/866 packet hypotheses authenticate
   contractions, frame alignment, differential response, and twisting, but
   do not by themselves authenticate coherent equivariance of the selected
   comparison packet across all sources. The proof explicitly preserves
   that missing certificate. It also correctly refrains from importing the
   stronger global-conic extension hypothesis of the next-weight theorem
   for a merely glued trace scalar.

3. **The corrected source has the claimed bidegree.** The multiplied-lift
   input supplies an a-linear equivariant representative of `Z_a`. The
   correction input identifies `b=L_can(a,h)` as polynomial of bidegree
   `(1,1)`. The first ladder input `a h Z_a` is `(2,1)`, and a coherent
   linear solution of the global cochain equation preserves this degree.
   Thus `a V_h` and `a b Z_a` are both `(3,1)`; the correction is not a
   removable lower-degree term. The simultaneous linear equation for
   `(E_h,W_h)` preserves `(3,1)` wherever the ladder supplies existence.
   Averaging a linear splitting is valid for these finite-dimensional
   equivariant linear equations in characteristic zero. This establishes
   existence of compatible family choices, not equivariance of arbitrary
   preselected physical contractions. The final proof correctly requires
   membership of the entire homogeneous source module in the relevant
   image and does not promote pointwise existence on a restricted source
   locus to a full polynomial family. It also expressly requires comparison
   before identifying an arbitrary Schur-gauge correction with L_can.
   The full `-q W_h` source remains
   present in the certified differential argument.

4. **Ten family parameters, twelve universal output directions, and
   thirteen unconstrained trace directions are different counts.**
   Independently taking characters gives
   `Sym^3 A=A+V+P4` and
   `Sym^3 A tensor D5=3A+3V+3P4+4D5`.
   The latter character is `(50,-2,-1,0,0)`, while T has character
   `(13,1,1,phibar,phi)`. Their inner product is
   `(650-30-20)/60=10`, and the domain has no trivial constituent.
   Hence every family has zero invariant output. All three nontrivial
   target irreducibles occur in the domain, and pure symmetric cubes span
   `Sym^3 A`, so the universal output span is exactly `V+P4+D5` of dimension
   twelve. This is not a claim that actual contractions realize that span.

5. **The axis kernel is exactly four-dimensional, with the twist retained.**
   No conic contains the six axes, so quadratic evaluation is an isomorphism;
   multiplication by an auxiliary linear form nonzero at all six points
   proves cubic evaluation surjective. The cubic vanishing module therefore
   has dimension four. In the dihedral normalizer, an involution swaps the
   nontrivial C5 eigenspaces of A and has determinant +1, hence acts by -1
   on its fixed C5 axis. The `O(3)` fiber consequently carries the sign
   character. The induced value character is `(6,-2,0,1,1)=A+V`, leaving
   exactly P4 as the vanishing module. Exactness of invariants and
   self-duality give kernel `Hom_G(P4 tensor D5,T)` of dimension four.
   The full stabilizer-compatible target has dimension six. Dropping this
   line character would give the wrong involution trace.

6. **The square kernel is exactly three-dimensional.** A C5-fixed square
   has twelve distinct translates on the discriminant conic: its finite
   A5 point stabilizer is cyclic, contains C5, and cannot be larger because
   A5 has no larger cyclic subgroup. The final proof states this argument
   explicitly. Vanishing
   for the entire D5 source propagates to every translate by equivariance.
   Each scalar component restricts to a binary sextic, so twelve distinct
   zeros force zero restriction. The polynomial is divisible by the
   invariant discriminant delta. Its residual family is a-linear and
   h-linear, giving kernel `delta Hom_G(A tensor D5,T)` of dimension three.
   Thus the image dimension is seven, not the raw C5-compatible target
   dimension thirteen. The latter is independent of the square's `O(3)`
   character because D5 restricts to the regular C5 representation.

7. **The injectivity really holds for any axis-square pair.** After square
   vanishing, write `eta=delta ell`. Delta is nonzero at every semisimple
   axis, so axis vanishing forces `ell` to vanish there and on its whole
   six-point orbit. Those lines span A by irreducibility. An a-linear
   family vanishing on them is zero. This does not require the square to
   be attached to the chosen axis, and does not require a jet test.
   Both evaluations concern the entire h-family; a single chosen h is
   insufficient for this proof. The combined image has dimension ten,
   not the sum thirteen of the two separate image dimensions.

8. **The varying multiplier is genuinely retained.** PR866 supplies
   `error(a,h;x)=-a(x)^3 h eta(a,h)`. Thus the error has source degrees
   `(6,2)` and positive binary degree sixteen. For a source-linear map L,
   the coefficient of `H_j^2` in `h L(h)` is `m_j L(m_j)`; multiplication
   by every nonzero binary monomial is injective. This proves that
   `J(L)(h)=h L(h)` has an explicit formal coefficient left inverse,
   without selecting or evaluating an actual source. After prior globality,
   eta is constant along the base line. For an arbitrary axis-square pair,
   the complement of their finite quadratic zero loci is nonempty.
   At any base point in that open set, the full quadratic-in-h norm-error
   observations recover the two entire h-linear evaluations. This proves
   the stated conditional calibration, but supplies neither a selected
   physical calibration point nor the independent reference `rho_AA`.

## Checker inspection and independent replays

Inspected the full checker. It uses only the Python standard library,
exact rational arithmetic in Q(phi), universal finite-group characters,
and formal coefficient labels. The binary recurrence is applied to the
correct positive and negative two-dimensional characters. The symmetric
cube power maps on A5 classes are correct. The coefficient-loop diagnostic
really tests the diagonal left inverse on all 65 formal coefficients of
`Hom(D5,Sym^12 U)`; it is not an actual source matrix or rank calculation.
Its checks raise explicit exceptions, so optimized Python does not disable
them. Five negative controls distinguish the wrong positive representation,
family versus output counts, invariant vector versus equivariant family,
the missing odd line twist, and an incorrectly h-linear norm observation.

Independently replayed, from the package directory:

- `python verify_symmetry_calibration.py`
- `python -O verify_symmetry_calibration.py`

Both exited successfully and reported:

`PASS: 122 exact character/degree/coefficient checks; 5 negative controls`

The checker does not itself prove orbit geometry, source-ladder existence,
actual family equivariance, global gluing, or reference authentication. Those
are correctly separated into the written proof and its explicit hypotheses.
No actual HM coefficient, source value, point, matrix, calibration, or rank
was evaluated during this review. No installs, heavy computations, repository
publication, or changes to the frozen source files were performed.

## Final-byte clarification check

Reread the complete final proof after its four clarifications: the canonical
correction versus an arbitrary Schur gauge; full homogeneous-source image
membership; the determinant derivation of the axis sign; and the cyclic
stabilizer proof of the twelve-point square orbit. All four are correct and
sharpen, rather than enlarge, the conditional theorem. The final proof hash
above supersedes the earlier draft. The checker and manifest are unchanged.

## Final assessment

The new deduction is substantive and specialized: a certified cubic/linear
equivariant normalization-error family has no invariant output, exactly ten
universal family channels, and an injective full-source two-orbit calibration
whose varying physical multiplier cannot hide a nonzero family. The result
does not claim actual equivariance or realized image dimensions, compute the
physical response rows, establish rho16 or beta4, or repair the original
geometric theorem. The present exact bytes support this restricted conclusion.
