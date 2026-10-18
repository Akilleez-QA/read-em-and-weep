# ID0 source-relabeling and shared Laurent certificate

## Result and scope

For the exact frozen ID0, the single complete preterminal scalar can be reused under the injective owner-seed relabeling 30 -> 0. One certified denominator quotient suffices mathematically for all three terminal coefficients. The precise identity is

    D0 = Q[d+(-3,-3,-1,-1)]
       + 2 Q[d+(-2,-2,-2,-2)]
       + Q[d+(-1,-1,-3,-3)],

where the complete stripped rational is A/B, B=x^d C, and **A=C Q must be certified exactly**. Q here denotes the certified polynomial quotient, not the test polynomial x1*x2+x3*x4.

This document proves a conditional source-equivalence lemma and an unconditional algebraic extraction theorem. The accompanying checker pins the existing source, verifies a symbolic seed-only AST change, and tests invented polynomial controls. It does not implement an ID0 physical adapter, validate the entire transitive physical source afresh, admit its costs, or compute its value. All guards are untouched.

## 1. Source-equivalence under provenance relabeling

An owner is (seed, occurrence, carrier, legal_mask, standard_tag). Define phi on every owner in the old one-request domain by

    phi(30,o,c,m,t)=(0,o,c,m,t).

Apply phi recursively to tuples, faces, dictionary keys, and cache keys; do not mix old and new owners in the same candidate. This is an injection with inverse on its image. It preserves equality and inequality of full owners, occurrence distinctions, tuple positions, source_key=(-1 if c=5 else c,m,t), physical_key=(c,m), and common_key=(c,m,t).

Consequently:

1. The potential-owner generator has the same domain, iteration order, and cardinality for each supplied tag/occurrence; its single constructor seed argument is the only alteration. No actual owners need to be enumerated to prove this.
2. Stable sorting by source_key returns the same permutation and whole-tuple parity. Even if source_key values tie, input positions and stable-sort behavior are unchanged. The relabeling does not authorize deduplicating tied source keys: distinct full owners remain distinct. Do not replace full-owner equality by physical_key equality.
3. The physical model consumes carrier and legal_mask; outer weights additionally consume standard_tag. None of these fields changes. The fixed data, coordinates, moving derivatives, old connection and gerbe remain identical. Equality-keyed memoization is conjugated by phi, so equal and unequal calls retain exactly their equality pattern. No persistent cache from another run may be smuggled into this equivalence.
4. Inductively each source leaf is equal, every matrix/scalar operation preserves equality, and the same ordered residual and HPL faces produce equal blocks. The base is the full source: seven kinetic terms, three negative gerbe terms, tracefree baseline, both Fk and both E terms, and the raw scalar's four blocks and both endpoints. The inductive step is the same original-resolution inclusion, ordered Cech faces, homotopy degree, and signs (1,1,-1,1).
5. The selector X13[5][0]+X02[1][3]+X02[4][2] is unchanged. Outer weights stay attached to original owners, not sorted replacements. Every staircase orientation, assignment, and summand is retained. Thus the whole scalar total, and only then its mask15 coefficient, are equal under phi.

The induction is on the formal finite computation DAG; it does not run that DAG. Its denotation is conditional on the existing physical model, lift, domain, and comparison theorems. The frozen raw_engine supplies a concrete constructor, not an arbitrary callback. The AST checker verifies that replacing the sole FullOwner seed argument and restoring it recovers the exact original AST. The unaltered complete preterminal prefix and weighted_assignment have recorded AST digests. It also checks that physical-engine and weight code do not explicitly consume seed/occurrence; this syntactic check supports, but does not replace, the equality/cache induction above.

The old _actual_body final output80 is NOT reused. It is removed from the denotational specification after the same complete stripped rational has been assembled. No value of output80 is needed or computed.

## 2. Necessary geometric premises are unchanged

The scalar coefficient must be the complete original-frame representative of S_(L5,0)([R_raw]) in H4(Y,O(-4,-4,-4,-4)), with one full deck-product removal and the internal-degree -2 tau^-4 conversion. On the finite chart tau=1. Mask15 is the deck-character coefficient, not the S4 alternating projector. It remains necessary.

The frozen domain retains carrier/legal/standard bounds 54/29/5251, every owner and owned suffix divisor, whole-coefficient regular extension to each full standard target, and the homogeneous degree formula from the full-lift contract:

    degree_i = sum_over_retained_factors(54*d_carrier
               + 29*(1+2*legal_bit_i) + 5251) - s - 2,
    d_carrier=4 for star carrier5, otherwise5.

This is an index formula; its satisfaction alone is not a proof that the actual numerator clears the poles. The full-source homogeneity and regularity theorem remains required. J3 closure (including delta J3=0) is required although J2 supplies the scalar. No cutoff is lowered by changing requested exponents.

The corrected alternating theorem uses the common ambient normalization

    A^E_ij = -dG_ij G_ij^-1 = -L_ij^t,

without the superseded extra scalar shift. With fixed transported old connections it gives e_sign R_raw=delta P, P=-(Z_i+Z_j)L_ij/72 after evaluation on the ordered four vector fields. Together with the accepted raw/N14 global comparison, [R_raw]=[Rsharp] lies in the retained sector. This is global cohomological equality, not equality of finite numerical cochains. We neither evaluate P nor assume it lies within the existing numerical cutoff. Complete raw evaluation is sufficient for the retained pairing.

## 3. Exact Laurent criterion and why one division suffices

Let K=Q, R=K[x1,x2,x3,x4], and S=R[x1^-1,...,x4^-1]. For A,B in R with B nonzero, set

    d_i=min{alpha_i : coefficient B_alpha is nonzero},
    C=x^-d B.

Then C is a nonzero polynomial and no xi divides C. A constant term in C is NOT necessary: x1+x2 is allowed. The following are equivalent:

    (i) A/B is a Laurent polynomial in S;
    (ii) C divides A in R;
    (iii) exact single-divisor polynomial division A=CQ+Remainder
          returns Remainder=0.

Proof of (i)->(ii): A/C=x^d A/B is Laurent, so some coordinate monomial x^n satisfies x^n A=C H in R. R is a UFD and C has no coordinate-variable prime factor, hence gcd(C,x^n)=1 and C divides A. The reverse direction is A/B=x^-d Q. For a fixed admissible monomial order, ordinary polynomial division by the single divisor C returns zero remainder exactly when A is in (C): the leading monomial of any nonzero multiple C H is divisible by LM(C), whereas all remainder monomials are not. The quotient Q is unique because R is an integral domain. Zero numerator gives Q=0; zero denominator is invalid.

For every integer exponent e, the Laurent coefficient is therefore Q[e+d], interpreted as zero if the exponent has any negative coordinate or is absent. The certificate (d,C,Q,A=CQ) is independent of e. One full zero-remainder validation can be shared among all three ID0 lookups. Multiplying numerator and denominator by extra common polynomial or monomial factors changes the certificate representation but not the Laurent polynomial or extracted values.

This is not Taylor-series division, iterated expansion, selected-degree truncation, or a test of only the three targets. For 1/(1+x1), all three negative target coefficients might appear absent under a chosen formal expansion, but the rational is not Laurent and must be rejected. Division cannot be skipped even when every shifted target is negative. Likewise local terms 1/C and (C-1)/C can each be non-Laurent while their complete sum is1; rejection or extraction of individual summands is not a substitute for the whole sum.

## 4. Pairing, degrees, and normalization

Write the test section as f=(x1*x2+x3*x4)^2. Its monomials are (2,2,0,0), (1,1,1,1), (0,0,2,2) with coefficients1,2,1. Each variable degree is at most2, so f is the finite-chart expression of a section O(2,2,2,2). Against F=O(-4,-4,-4,-4), the Serre trace is the coefficient of x^(-1,-1,-1,-1) in f times the transported scalar. Therefore its three requested exponents are exactly those above, corresponding to frozen indices8,40,72 under sum_i(2-m_i)3^(3-i). No factorial, denominator, new tau factor, or additional sign appears.

The harmonic scalar range is [-3,-1]^4. For a Laurent representative of the correct global scalar class, projection to these exponents gives its H4 coordinates; terms outside that range are Cech coboundaries in the product two-chart model. This conclusion uses the already authenticated transport/completeness theorem. An arbitrary Laurent rational with a matching triple of coefficients is not thereby authenticated as the physical scalar.

## 5. Preconditions of a future shared-certificate API

Mathematical sharing is valid when all lookups refer to exactly the same immutable complete stripped rational in the same variables and frame. Operationally a future certified object must bind its input identity and Execution, hold the immutable quotient and denominator shift, validate exact division fully before any lookup, validate each four-integer exponent, reject foreign receiving contexts, and check that the shared Execution is live at certificate creation and at every read/weighted operation. A failed/poisoned execution must not leak an already cached result as success.

The weighted terminal must use the SAME Execution: a+2b+c through metered q/mul/add (with the final result retained and charged). Quotient/remainder construction, retained certificate, scans, outputs, coefficient/exponent heights, and native scratch/lifetimes all require new metering and representation bounds. An operation-saving denotational proof is not a cap-fit proof. In particular, under finite budgets a batched implementation may succeed where the old repeated-division version fails; we claim equality of successful mathematical values, not identical failure traces or counters.

No shared-certificate API exists in the frozen field.py. This proof therefore resolves the mathematical sharing question but does not authorize dropping two charged divisions from an existing admission record. A new source-bound adapter, authenticated transitive closure, operational controls and independent cost/admission review remain missing.

## 6. Reproducible controls and remaining blocker

Run check_certificate.py with --source-root pointing to the pinned repository root (or its research/codex-swarm directory), normally and with python -O. See README.md for commands. It imports only the standard library and parses source as data. It verifies all23 manifest source files by SHA256 and Git blob hash before AST processing, pins the corrected alternating premise, and checks the exact retained ID0 record. Its invented sparse-polynomial implementation exercises full three-term values, weight2, a nonconstant residual with zero constant term, representation independence, zero numerator, zero-denominator rejection, non-Laurent rejection, complete-sum cancellation, and nontrivial weighted cancellation. It performs195 tiny invented polynomial coefficient products, bounded by10000, with no production arithmetic imported.

The proof is universal; finite invented controls catch transcription errors but do not establish physical provenance or geometric regularity. No physical owner/model/source/jet was constructed or evaluated. No Omega attempt was made, no guard changed, no external file written.

The exact remaining blocker to a physical D0 value is not an unresolved denominator-sharing identity. It is the absent source-bound ID0 implementation plus unchanged source/domain implementation authentication and resource admission/release. The proof does not settle D0. D0=0 alone remains undecided; one authenticated nonzero D0 would prove nonvanishing.
