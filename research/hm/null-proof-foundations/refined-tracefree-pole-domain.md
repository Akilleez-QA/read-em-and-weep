# Fresh pole domain and finite support for the refined trace-free source

## Result

The new trace-free representative Rsharp has a fresh, explicitly owned outer comparison domain. A sufficient outer partition uses carrier power54 and legal-line power29. Standard-chart boundary factors need not be cleared by that partition: they are already units on the target standard intersection, provided the SAME projection r from the common refinement to its standard tag is used.

The new scalar solver contributes finite standard-boundary pole order at most5250, or5251 after its complementary derivative. This leads to an explicit conservative Laurent support envelope for the transported source. These bounds do not reuse the original source's62/63 pole certificate, four-tail reduction, or781-feature count.

All calculations below are symbolic degree/order accounting and integer metadata arithmetic. No source polynomial, residual, partition, coefficient, sample, or jet was evaluated. No executable complexity certificate is claimed.

## 1. Objects and ownership

Use the source-first common refinement B with vertices v=(e,b,m): standard chart e, carrier b, legal mask m. The map r(v)=e is fixed throughout. At coordinate i the standard chart equation is Z_(e,i)=Y_i if e_i=0, and X_i if e_i=1. It is a unit on U_e.

The scalar solutions are the N14 transition-only solutions, and the closed trace-free representative is

    Rsharp = M0^0 + F_q k_p,ik + F_p k_q,ik
                       + E_p(T_q F_q)+E_q(T_p F_p).

M0 is the FULL gerbe-corrected normalized baseline at u_p=g k_p, u_q=g k_q. Definitions and proof of closedness are in `direct-scalar-free-pairing-reduction.md`.

A divisor charge belongs to an actual vertex occurrence. Carrier and legal factors may not be transferred to an absent owner. A standard equation can be charged to an output vertex with the same standard tag when an inserted scalar-prism vertex has that tag: it is the very same unit equation on that chart. This is a geometric unit argument, not a reassignment of a carrier divisor.

## 2. Scalar standard-branch Laurent support

The N14 scalar finite-demand proof gives:

- Cleared F numerator degree at most217 in each coordinate (210 in nonpair coordinates).
- A carrier quotient degree at most1677 in a finite local coordinate and481 in an infinity coordinate.
- Legal additions of degree0 in a finite coordinate, and at most2 in an infinity coordinate (pair quotients actually need at most1).
- A finite-frame reversal shift at most14*5+3=73 per source vertex in one coordinate.

The scalar input has three vertices. Its exact demand equation therefore bounds every coordinate exponent of Pi F by

    lower >= -3*(481+2)-3*73 = -1668,
    upper <= 217+3*1677 = 5248.

The independent maxima are deliberately combined conservatively; they need not occur on the same chart. S,h,A,K_cov preserve finite-frame exponents. Thus the standard branch R(K_cov Pi+A h S Pi)F has support inside

    [-1668,5248]^4.

A scalar pair-character coefficient has twist n_i=0 or-2. Converting its finite-frame monomial x_i^e to the infinity frame gives exponent n_i-e. Hence all coordinate boundary pole orders of this branch are at most5250.

Because it is a regular sheaf cochain on its standard edge intersection, a negative local coordinate power can occur only at a boundary excluded by one of that edge's actual standard chart labels. Where no owner exists, regularity forces the relevant Laurent coefficients to vanish. This is established regularity of the whole cochain; it is not a claim that every summand of an uncombined expression has the same cancellation.

## 3. Scalar prism branch and differentiation

For N14 a raw carrier weight is H_b^14 times its certified quotient. Its finite-coordinate degree is at most

    1677+14*5 = 1747.

Finite-chart legal weights have degree0. In an infinity coordinate the raw carrier-plus-legal degree is at most

    481+14*5+2 = 553.

Thus1747 is a valid uniform local degree bound for an entire raw rho weight. One must NOT add2 to1747: that legal addition occurs in the different infinity case, already bounded by553.

In H_rho F on an output edge (a0,a1), the first branch has one weight on standard tag e0; the second has two weights with tags e0,e1. Each is regular on its own U_e and has boundary poles of order at most1747 when expressed in another standard chart. Charge these respectively to a0 and a1. Inserted carrier/legal factors cancel by the existing N14 divisibility proof. The unchanged suffix retains carrier order14 and legal order1 per owner.

Combining with section2, the scalar solution s has:

    carrier <=14,
    legal <=1,
    additional standard-boundary <=5250 per actual edge vertex.

A complementary invariant derivative can increase an existing carrier or coordinate-boundary order by at most1. For legal orders one may conservatively allow an increase by1 as well, although the complementary coordinate does not differentiate the pair's existing legal factors. Therefore use

    V(s): carrier <=15, legal <=2, standard-boundary <=5251.

This includes derivatives of partition weights. No derivative has been commuted through rho or discarded. Crucially, first perform the certified inserted-vertex cancellation in each weighted term, using the explicit polynomial quotient formula, and then differentiate that exact regularized expression. The raw Leibniz pieces (V rho)F and rho V(F) can separately display an extra inserted-carrier denominator; N14 does not independently clear those pieces. Their sum is the derivative of the already canceled polynomial quotient. This sequencing prevents a false extra pole or a false claim of separate cancellation. In the pair-complementary coordinate, the stripped derivative is the verified map O->O(-2); its infinity frame change is included, rather than treated as a new arbitrary pole.

## 4. Fresh Rsharp order ledger

Use the already authenticated primitive bounds as INPUT facts: I,P,H entries have carrier order<=2; g and its determinant-one inverse have carrier<=4; their physical legal cost is<=2. One derivative raises the corresponding existing order by at most1. These primitive facts do not import an old full-source bound.

### Carrier orders

- k=-mu(g^(-1),g)/2 has carrier<=5+5=10.
- u0=g k has carrier<=4+10=14.
- The largest baseline term is normalized u0*u0, of order<=4+14+14=32.
- Normalized mu(u0,g) or mu(g,u0) is <=4+15+5=24.
- Normalized mixed mu2(g,g) is <=4+6+6=16.
- The gerbe baseline terms are smaller; the actual normalized expression includes -b_p k_q-b_q k_p-b_p b_q I.
- F k has carrier<=14+10=24.
- L_d=g_ij^(-1)V_d(g_ij) has carrier<=9.
- The transported current U_d has the EXACT alternative expression

      U_d=g_ik^(-1)V_d(g_ik)-g_ij^(-1)V_d(g_ij).

  This follows by differentiating g_ik=g_jk g_ij. Both terms use actual triple vertices. Thus U also has carrier<=9, rather than the unsimplified apparent17.
- E(TF) has carrier<=15+9=24.

Consequently Rsharp has carrier<=32 per owner. The trace-free projection is linear and adds no poles.

### Legal orders

Use the coarse physical-frame cost ledger, not a numerator cancellation assumption:

- g,g^(-1) <=2, their first derivatives<=3, second derivatives<=4;
- k<=6, u0<=8;
- normalized u0*u0<=18, normalized mu(u0,g)<=14, normalized mu2(g,g)<=10;
- F k<=1+6=7;
- L,U<=5, so E(TF)<=2+5=7.

Thus legal order<=18 suffices for Rsharp. This intentionally ignores sharper complementary-coordinate cancellations.

The extra standard-boundary order stays<=5251: only the scalar-derived branches introduce those factors. All remaining maps in this ledger are geometric sheaf operations whose primitive poles are already charged to actual carrier/legal divisors in homogeneous physical frames.

## 5. Resolution lift and the fresh outer domain

Apply the pinned linear local resolution inclusion and successive End homotopies to Rsharp^t on B. These constructions apply to any closed normalized End cochain; they do not require the old three-carrier-local residual formula.

The inclusion I(-)P adds carrier<=4 and legal<=2. Each undifferentiated End homotopy H(-)+(-1)^r(IP)(-)H adds carrier<=6 and legal<=3. Cech differences and the regular End differential introduce no new divisor owners. There are no further scalar derivatives in this lift.

For J_s of Cech degree2+s and internal degree-s, s=0,1,2,3, sufficient bounds are:

    J0: carrier36, legal20;
    J1: carrier42, legal23;
    J2: carrier48, legal26;
    J3: carrier54, legal29.

Retain the standard-boundary5251 bound at each actual common vertex. Newly inserted resolution-prefix vertices may be given the same conservative allowance even when no such factor occurs.

Use an outer carrier partition at N=54 and a legal partition at N=29. Their independent sums are1, so their product is a valid fixed partition. Its carrier divisibility clears54; its legal divisibility clears29.

For every outer projection term, the sampled common tuple is

    ((e0,alpha0),...,(eq,alphaq))

over the target standard tuple (e0,...,eq). Hence each Z_(e_l,i) is ALREADY A UNIT on the target intersection. No outer weight is required to clear its5251 power. The same fact applies to inserted vertices in the outer prism: their standard tags are the designated target rows. Source-first sorting changes signs, not this ownership set.

This is a regular comparison on the stated domain and is stable under restrictions, Cech differential and End differential. An unrelated projection that forgets or replaces standard tags would require a new proof and cannot use this argument.

## 6. Explicit outer finite-degree consequences

For the carrier54 partition,

    M=107, threshold=535, L_s=(s+1)*534+1.

Its local carrier quotients obey the same exact syntactic cancellation formulas as the scalar N14 construction. The resulting degree bounds, indexed here by the NUMBER OF INFINITY COORDINATES t, are:

    t=0: degree266;
    t=1: finite1335, infinity853;
    t=2: finite3472, infinity1387;
    t=3: finite6677, infinity1921;
    t=4: degree266.

For the legal29 partition, M_line=57 and local weights have infinity degree at most114. Dividing by the owned legal factor to power29 gives degree<=85 for mask0 (divide t^29) and<=56 for mask1 (divide (1-t^2)^29). Finite legal quotients are constant or zero. Therefore each row's combined outer quotient has finite degree<=6677 and infinity degree<=2006.

For J_s, put m=s+3, r=-s. Clear its conservative carrier54/legal29 poles and multiply by the standard equations Z_(e_l,i)^5251 for each of its m vertex occurrences. This yields a homogeneous numerator P with coordinate degree

    deg_i P = 54 sum_l d_(b_l)
              +29 sum_l deg ell_(m_l,i)
              +5251m +(r-2)
          <= (270+87+5251)m-s-2
           = 5608m-s-2.

This uses the full-sign internal-degree-r eigensheaf O(r-2)^4. Clearing a pole-free factor unnecessarily only enlarges the envelope; it does not assert that the corresponding denominator occurs.

After multiplication by the outer weights, carrier/legal divisions cancel syntactically. In each row's own chart its standard equation is1. Finite-frame reversal records it in the exponent shift instead. Precisely,

    p_i + sum_(finite rows) a_(l,i)
        - sum_(infinity rows) a_(l,i) - m_i = kappa_i,

where

    m_i=sum_(infinity rows l)
          [54 d_(b_l)+29 deg ell_(m_l,i)+5251].

All variables have explicit finite boxes. In particular m<=6 yields

    deg_i P<=33643,      m_i<=33648,

and a safe uniform transported Laurent envelope is

    [-45684,73705]^4.

The lower endpoint is -6*2006-33648. The upper endpoint is33643+6*6677. S eliminates the Cech-degree-five J3 output, so actual detector requests can use smaller componentwise bounds, but the displayed common envelope also covers the domain needed for the complete chain-map argument.

These rectangles are not occupied supports, required storage, lower bounds, or permission to materialize them. The finite exponent predicates can be retained symbolically.

## 7. What this closes and what remains

Closed at formula level:

- A fresh regular outer comparison domain for the refined trace-free representative.
- Actual carrier/legal/standard ownership, including scalar-prism suffixes and derivatives of weights.
- A finite global numerator envelope and exact outer Laurent demand equation.

Still required:

- Instantiate the actual finite detector on this new comparison and compose its demands with the transposed scalar grammar.
- Apply new sparse support identities only after proving them for this refined source; none of the old four-tail/781 assumptions was reused here.
- Supply the complete static product ledger and peak-byte schedule before evaluation. Larger finite bounds are not an executable resource pass.

The obstruction value remains unknown.

## Dependency scope

Companion references are identified by basename. A referenced file not supplied with this collection or its support-certificate companion is an external prerequisite, not an embedded proof or a verified relative link. The reading order and unresolved conditions are listed in `proof-notes-index.md`. Reported test results describe the source audit; this proof copy does not by itself constitute a new test run.
