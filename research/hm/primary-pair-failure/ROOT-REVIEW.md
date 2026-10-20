# Second mathematical review

Reviewed proof SHA-256: 698c6e50bcf72227c42eb33b016878ab449eef1aaceca0cd8636656169bde0fc.

Verdict: PASS relative to the pinned representation and cup-product inputs. Mathematical review, not formal verification.

The cubic multiplication target is Hom(A*,W)=A tensor W. In the stated normalizer decomposition it occurs once, with a nonisomorphic 25-dimensional complementary summand. Degree-zero generation makes multiplication nonzero, so equivariance and irreducibility give the stated surjective projection and its 25-dimensional kernel. The source and target dual conventions agree.

For each nonzero bad quadratic, PR449 gives a nonzero one-dimensional image l. The combined image fails to span the two-dimensional target precisely when cubic multiplication takes values in that same line. This is exactly the rank-thirty kernel bundle in the proof. The tautological subline has degree minus one, while the nilpotent embedding is quadratic in that line; these distinct twists are correctly separated. Projectivizing the subbundle gives a closed smooth irreducible image of dimension 34, hence codimension 14 in P14 times P34. Equality is asserted for reduced closed loci only; no scheme-theoretic determinantal multiplicity claim is made.

The rank-one 2-by-5 tensor cone has affine dimension six; adding the 25-dimensional kernel and projectivizing gives dimension thirty and codimension four. Rank-zero, rank-one and rank-two cubic fibers over the bad-quadratic locus are correctly distinguished. In particular rank-two cubic multiplication covers the target independently of u.

Injectivity of the natural target cup product gives a subspace of L0 intersect U of dimension exactly four times the combined primary rank. Every nonzero u has rank at least one, so the residual-to-full discrepancy is uniformly at most four. Equality is not implied: non-primary inputs may add further elements of L0 intersect U. The bounds 10+k and 6+k follow from the pinned residual bound under global coprimality, without asserting vanishing or evaluating a selected pair.

The new classification does not resolve residual interpolation, original-pair membership, retained source values, pure conditions, module lifting or quantization algebraicity.
