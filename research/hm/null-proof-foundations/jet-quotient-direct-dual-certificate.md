# A tensor-jet quotient with an explicit dual contraction

## Result

There is a genuinely finite, matrix-free-in-the-full-domain dual certificate conditional on an exact detector-factorization identity. Replace each full homogeneous numerator space by a common finite tensor polynomial quotient. Multiplication by every owned denominator descends exactly. The cover supplies a unit ideal in that quotient, hence an explicit Koszul contraction. If the degree-zero quotient map is surjective, the already proved full boundary-annihilation identity forces closedness in the quotient. This gives a dual filling by finite quotient multiplication, without the full row-space pivot matrix.

The unresolved condition is substantial: the actual detector covector must factor through the selected quotient. Regularity, pole bounds, and full H1 exactness do not imply that condition. This note does not assert that the authenticated detector factors through small jets, nor that its physical pairing has been evaluated.

## 1. Exact tensor quotient

Use the full owned-denominator spaces Vq and multidegrees m_I from owned-denominator-finite-domain-certificate.md. Choose one product affine coordinate chart of (P1)^4, with coordinates z_i and its fixed homogeneous frames. Dehomogenization identifies the I summand with polynomials of coordinate degrees at most m_(I,i). This is injective for the global section space, even though this one chart need not cover X.

Fix monic polynomials g_i(z_i) of positive degrees r_i, and set

    A = k[z_1,...,z_4]/(g_1,...,g_4),
    R = dim A = product_i r_i.

For each actual tuple I use a separate copy of A. Define Wq as the direct sum of these copies over |I|=q+1. The map Qq:Vq -> Wq dehomogenizes each numerator and reduces it modulo the g_i. Let dbar_v be the dehomogenization of the actual section d_v reduced in A. Define

    (Dbar_q a)_J = sum_l (-1)^l dbar_(j_l) a_(J minus j_l).

Then, exactly and on the entire full numerator domain,

    Q_(q+1) Dq = Dbar_q Qq.

This is a ring-homomorphism identity, not a clipped multiplication. It retains all distinct vertex labels and uses the correct homogeneous frame for every multiplication. The discarded numerator subspaces form a differential-stable kernel.

A simple explicit surjectivity certificate is

    r_i - 1 <= min_v m_({v},i), for every coordinate i.       (S)

Each vertex numerator space then contains every tensor remainder monomial, so Q0 is onto. The higher Qq are onto as well for the positive denominator degrees here. Using the actual minimum denominator coordinate degree 5307, condition (S) permits r_i <= 5308 on the two zero-character coordinates and <= 5306 on the two character -2 coordinates. These are upper admissible orders, not a claim that such large quotients are affordable.

## 2. Constructive unit-ideal contraction

The principal opens of the d_v cover X. Consequently their dehomogenizations have no common zero on the chosen affine chart. Their images generate the unit ideal in every finite quotient A. Equivalently there exist a_v in A with

    sum_v a_v dbar_v = 1.                                  (U)

This can be independently certified by a remainder calculation in the tensor quotient. For an implementation it must be supplied as actual finite elements or arithmetic circuits, not an unexplained inverse symbol.

Let h_q:Wq -> W_(q-1) be contraction by the A-linear covector with entries a_v. In ordered-tuple notation, each term removes v from a source tuple with its deletion sign and multiplies by a_v. The exterior-algebra identity gives

    h_2 Dbar_1 + Dbar_0 h_1 = identity on W1.               (H)

The augmented quotient Koszul complex is contractible. This does not imply the original global-section complex is contractible: quotienting loses its H2, and its augmentation now has A in degree -1. In particular the quotient need not preserve the original H0. Only its chain-map and surjectivity properties are used.

### A particularly explicit jet choice

Take g_i=(z_i-p_i)^(r_i) at a point p in the chosen affine chart, and write t_i=z_i-p_i. By the cover choose an actual vertex w with c=d_w(p) nonzero. Set u=dbar_w-c. In A, u^N=0 for

    N=1+sum_i(r_i-1).

Thus (U) is certified by a_v=0 for v!=w and

    a_w = c^(-1) sum_(j=0)^(N-1) (-u/c)^j.

The identity a_w dbar_w=1 follows by the finite geometric-series identity; no limiting series is involved. Coordinate tensor arithmetic computes this in R remainder slots. This is a formal construction; evaluating a physical denominator at p is not authorized by this note.

## 3. The detector factorization obligation

Supply an exact covector ebar on W1 satisfying

    e = Q1^t ebar on ALL of V1.                            (F)

The full-domain certificate already proves e D0=0. From (F), intertwining, and surjectivity of Q0,

    ebar Dbar_0 Q0 = e D0 = 0,
    therefore ebar Dbar_0 = 0.                             (C)

Now define a full V2 covector by the factored expression

    eta = Q2^t h_2^t ebar.

The exact residual certificate is the short operator calculation

    eta D1 = ebar h_2 Q2 D1
           = ebar h_2 Dbar_1 Q1
           = ebar (identity-Dbar_0 h_1) Q1
           = ebar Q1 = e.

Thus (S), (U), and (F), together with the established full eD0=0 identity, are a sufficient explicit compressed dual certificate. No full D1 rank computation is needed. If (S) fails, it can be replaced by a directly verified (C); full closedness alone no longer implies it. If (F) fails, no conclusion about the requested detector follows, regardless of the quotient contraction.

### A checkable coefficient form of (F)

For the jet quotient at p, let c_(I,alpha) denote ebar on the jet monomial t^alpha, with 0<=alpha_i<r_i. On the dehomogenized numerator monomial z^a the exact required identity is

    e_I(z^a) = sum_(alpha<=a, alpha_i<r_i)
                 c_(I,alpha) product_i binom(a_i,alpha_i) p_i^(a_i-alpha_i)

for every exponent a in that tuple's complete numerator box. This is a finite identity and may be proved symbolically by the detector's adjoint expression or exact generating-function/recurrence identities. Checking a few samples is not a certificate. At p=0 it says specifically that the detector row vanishes outside the low rectangular exponent stencil. For a different chart, use that chart's homogeneous basis and corresponding reversed exponents where necessary.

High Laurent coefficient demands after multiplication by outer weights may depend on high numerator coefficients. Nothing in the existing pole bounds proves their absence. An exact adjoint-multiplier support calculation could prove (F), but it has not been supplied. Taking jet orders large enough to inject every full numerator space removes this obstruction but may destroy (S), and gives no numerator-dimension savings; direct verification of (C) would still be necessary. Multiple points or general tensor g_i are possible, but require their own exact factorization identity.

## 4. Ownership, storage, and limits

The inverse in (U) is used only in the finite numerator quotient. It is never interpreted as a regular cochain primitive with a new apex denominator. The resulting eta is an ordinary linear functional on the actual triple numerator spaces via Q2. Therefore the construction does not transfer an absent owner's poles, alter d_v, or assert that rational division by d_w is legal on an edge. No new comparison partition is introduced.

The construction avoids all full numerator matrices. It does not automatically avoid the enormous number of cover tuples: W1 still has choose(1536,2) R scalar slots if stored densely. A single-point apex contraction uses only triples containing w. In fact eta on a triple not containing w is zero; on an ordered triple J containing w it applies ebar_(J minus w) after multiplication by a_w, with the deletion sign. Edges containing w make no direct contribution to this formula; their residual is supplied by (C). This is an explicit support reduction, but even choose(1535,2) R slots are not a budget certificate. A sparse/factored representation of ebar and a live-storage/product schedule remain mandatory.

More fundamentally this is not a universal compressed solution. In an exact example below, only 12 dimensions of the full 134-dimensional closed covector space factor through the chosen quotient while remaining closed. Full H1 exactness alone cannot force the missing 122 dimensions into the selected jets.

## 5. Exact abstract check

The test uses X=P1 x P1, F=O(-2,-2), four denominators d_(a,b)=Z_a^3 W_b^3, and the jet algebra k[t,u]/(t^2,u^2) at (z,w)=(1,1). The actual vertex w=(1,1) has denominator (1+t)^3(1+u)^3 and inverse

    1-3t-3u+9tu modulo (t^2,u^2).

Full dimensions in degrees 0,1,2 are (16,150,256); quotient dimensions are (16,24,16). The test verifies exact intertwining, Q0 surjectivity, (H), and the lifted full residual D1^t eta=e for a nonzero abstract closed quotient row. It also verifies full ranks (16,134) and quotient ranks (12,12). Thus the factorable closed rows form a 12-dimensional space, whereas all full closed rows form a 134-dimensional space.

Files: test_jet_quotient_dual_certificate.py and jet-quotient-dual-test-results.json. They operate only on abstract small rational matrices. No physical source polynomials, samples, or detector rows were evaluated.

## Status and remaining unknowns

New: a constructive tensor-quotient certificate, explicit finite jet inverse, exact lifted residual proof, a precise detector-row factorization test, and an abstract verified compression with a strict limitation on its reach.

Unknown: a useful quotient for the actual detector; its exact factorization (F); economical a_v/ebar circuits; all actual operation and peak-byte counts. No physical evaluation was performed.

## Dependency scope

Companion references are identified by basename. A referenced file not supplied with this collection is an external prerequisite, not an embedded proof or a verified relative link. The reading order and unresolved conditions are listed in `proof-notes-index.md`. Reported test results describe the source audit; this proof copy does not by itself constitute a new test run.
