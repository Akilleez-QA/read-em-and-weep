# Explicit regular cover transport for the HM detector

## Scope and outcome

This note gives signed maps between the standard tensor-product Cech complex and the ordered Cech complex, an explicit comparison homotopy, and polynomial partitions adapted to the actual six-carrier/line cover. Together they give formulas for both the transported cocycle and the six-equation comparison primitive.

The construction uses a conservative common pole bound N=62 derived below from the complete source operations and the pinned primitive certificates. The polynomial partitions are given by exact finite formulas; no Bezout search is needed. No source residual, held polynomial payload, or obstruction pairing has been generated or evaluated here. This is a mathematical max/add bound, not an executed full-End graph replay or a practical cost certificate.

## 1. Pinned geometric input

The source is the normalized, transposed full-sign residual and its closed total lift `J=J0+J1+J2+J3` from [PR41 closure and characters](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-residual-attribution/closure-and-characters.md), §3. The four bidegrees are `(2,0),(3,-1),(4,-2),(5,-3)`.

The cover equations and six local contractions are pinned in [source identity](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-geometric-dependencies/source-identity.md), §§1–3, and [physical frames and poles](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-geometric-dependencies/frames-and-poles.md). Write

`prod_i (Y_i+X_i z) = sum_(j=0)^4 v_j z^j`,

`h_j = v_j^5-v0*v1*v2*v3*v4`, and `a=v0*v1*v3*v4`.

The six carrier opens are `D(h_j)` for j=0,...,4 and the auxiliary `D(a)`. Legal line opens are

`W_i0=D(Y_i)`, `W_i1=D(X_i*(X_i^2-Y_i^2))`.

Source vertices are `(b,m)` with carrier b in `(*,0,1,2,3,4)` and mask m in `{0,1}^4`, on `V_(b,m)=D(H_b) intersect prod_i W_i,m_i`, where `H_*=a` and `H_j=h_j`. Empty intersections are omitted. Use the source's fixed alternating extension, never re-evaluate its nonlinear residual after permuting vertices.

On `Y=(P1)^4`, the full-sign internal-degree-r End summand is `O(r-2,r-2,r-2,r-2)` in the original frame. The pinned conversion is `tau^(r-2)`. All formulas below act on these actual sheaf sections; local matrix entries must first be transported into this frame.

The total differential is always `D=delta+(-1)^q d_End` in Cech degree q. End degrees are -3,...,3. The finite tensor contraction is the one in [the pinned oracle](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-proof/finite-model/full-sign-boundary-oracle.js), especially lines 58–198.

## 2. Standard tensor and ordered complexes

Let `U_0=D(Y)` and `U_1=D(X)` in each factor, and `U_e=prod_i U_e_i` for `e in {0,1}^4`. Order these 16 vertices lexicographically with coordinate 1 first.

Let T be the tensor product of the four two-chart Cech resolutions. A tensor cell has, in each coordinate i, either one vertex `[0]` or `[1]` in degree zero, or the oriented edge `[0,1]` in degree one. Its total Cech degree q is the number of edge factors. The tensor differential has sign `(-1)^(q1+...+q_(i-1))` on the ith factor.

Let O be the alternating ordered Cech complex of the 16 product opens. All formulas on O are first defined on increasing tuples and then extended alternatingly. A repeated vertex gives zero. In particular, raw formulas below are not to be applied to an unsorted tuple without the alternating extension.

### 2.1 Alexander–Whitney cochain map A: T -> O

For an increasing tuple `(e0,...,eq)`, sum over `(q1,...,q4) in {0,1}^4` with sum q. Put `p_i=q1+...+q_(i-1)`. The ith factor index is

`I_i=[e_(p_i),i]` if qi=0, and `I_i=[e_(p_i),i,e_(p_i+1),i]` if qi=1.

The summand is the tensor cochain entry with indices `(I_1,...,I_4)`, restricted to the intersection of all `U_ej`. An edge `[1,0]` contributes minus the `[0,1]` entry, and `[0,0]` or `[1,1]` contributes zero. Thus

`(Af)_(e0...eq) = sum_(q1+...+q4=q) f_(I1,...,I4)|_(U_e0...eq)`.

There is no additional sign outside these oriented factor edges. The cut positions, factor order 1,2,3,4, and tensor differential fix the convention. For q>4 the sum is empty.

The standard cut-and-boundary cancellation proves `delta A=A delta`: deleting a cut vertex cancels the adjacent cut contribution; the remaining face terms give the tensor factor boundaries with the displayed preceding-degree signs. This argument also allows projected factor edges to reverse orientation. Sheaf restrictions commute with the calculation.

### 2.2 Signed staircase map S: O -> T

For a tensor cell, let `I={i1<...<iq}` be its active edge coordinates and fix the inactive coordinate vertices. For each permutation sigma of I, form the staircase

`e^0_sigma,...,e^q_sigma`

which starts with every active coordinate zero and changes coordinate `sigma(k)` to one at step k. Every staircase tuple is increasing. Define

`(Sc)_cell = sum_(sigma in Sym(I)) sign(sigma) c_(e^0_sigma,...,e^q_sigma)`.

Every path intersection equals the tensor cell's open intersection, so no localization is enlarged. The boundary of the signed triangulation of a q-cube is exactly its tensor boundary; internal faces cancel in pairs. Hence `S delta=delta S`.

Moreover `SA=1` exactly. On a staircase, the Alexander–Whitney cuts contributing to the same tensor cell force the active coordinates to be changed in increasing factor order. Its sign is +1; every other staircase or degree allocation has a constant edge in some active factor and vanishes.

A two-coordinate sign control is

`(Sc)_[01]x[01] = c_(00,10,11) - c_(00,01,11)`.

## 3. An explicit rectangle-cone comparison homotopy

The following finite recurrence avoids an unspecified Eilenberg–Zilber homotopy.

Use the formal oriented simplicial chains on the 16 vertices. For an ordered simplex sigma, let `R(sigma)` be the coordinate rectangle consisting of all choices of coordinate values appearing in sigma. Let `b(sigma)` be its coordinatewise minimum vertex. Any intersection supporting sigma is contained in every product open indexed by `R(sigma)`.

Let G be the chain map dual to the cochain operator AS: first use the Alexander–Whitney cuts on chains, then the signed staircase chain map. G takes each simplex to a chain of vertices in its rectangle.

For a vertex b let `cone_b([v0,...,vk])=[b,v0,...,vk]`, with sorting signs and zero for repetitions. On augmented chains,

`boundary cone_b + cone_b boundary = 1`.

Define the chain homotopy k recursively by `k=0` in degrees -1 and 0, and for q>=1 by

`k(sigma) = cone_(b(sigma)) (sigma - G(sigma) - k(boundary sigma))`.

Inductively the quantity in parentheses is a cycle: the lower-degree identity `boundary k+k boundary=1-G` makes its boundary zero. Applying the cone identity gives

`boundary k+k boundary=1-G`.

Every term stays in `R(sigma)`: faces have smaller rectangles, and both G and the cone respect the containing rectangle. Dualizing with restrictions therefore defines a regular cochain map K of degree -1 satisfying

`delta K+K delta=1-AS`.

For example, on the diagonal edge `(00,11)` in two coordinates,

`k[00,11]=-[00,01,11]`,

consistent with G replacing it by `[00,01]+[01,11]`. This fixes the homotopy sign independently of notation.

A, S, and K preserve internal degree and commute with the sheaf map `d_End`. Their total-complex identities are consequently

`DA=AD`, `DS=SD`, and `DK+KD=1-AS`.

The last identity has no extra vertical term because K lowers q by one: the two vertical contributions have opposite totalization signs.

## 4. The common cover and why fixed line masks are insufficient

Use common-refinement vertices `(e,b,m)` on

`B_(e,b,m)=U_e intersect V_(b,m)`.

Let `r(e,b,m)=e` and `s(e,b,m)=(b,m)`. The r-fiber covers every U_e. Fixing only `m=e` would not do so: on an infinity chart `X_i!=0`, the legal mask-one open omits `Y_i/X_i=+1,-1`; those points require the mask-zero open.

Choose the common-vertex ordering once, and use alternating pullbacks along r and s. Transport all coefficients into the same original End frames. Set `u=s*J`.

## 5. Explicit fixed polynomial partitions; no Bezout search

This section constructs partitions for any positive integer N. Section 6.1 derives the conservative choice N=62 for the complete declared source. The formulas remain parameterized so that a sharper separately certified bound can later be substituted without changing the argument.

### 5.1 A unit identity on every standard product chart

On U_e put `x_i=X_i/Y_i` for finite coordinates and `t_i=Y_i/X_i` for infinity coordinates. Let s be the number of infinity coordinates and use the local homogeneous trivialization

`F(z)=prod_(finite i)(1+x_i z) prod_(infinity i)(t_i+z)=sum_(j=0)^4 v_j z^j`.

Here and below the homogeneous symbols denote their expressions in this chart. Let `H_k(x_A)` be the complete homogeneous symmetric polynomial of degree k in the finite coordinates, with H0=1. Formal division at z=0 gives the **finite** coefficient identity

`1 = [z^s](F(z)/prod_(finite i)(1+x_i z))`

`  = sum_(j=0)^s (-1)^(s-j) H_(s-j)(x_A) v_j`.

The reason the first coefficient is 1 is that `prod_(infinity i)(t_i+z)` is monic of degree s. No infinite series needs to be computed. Put `g_j=(-1)^(s-j) H_(s-j)(x_A) v_j`; then `sum g_j=1`.

### 5.2 Raising a unit partition to prescribed powers

Given L0>=1, put `d=s+1` and `L=d*(L0-1)+1`. Expand the formal multinomial `(sum_(j=0)^s g_j)^L=1`. Every multi-index n with sum L has at least one n_j>=L0. Assign it to the smallest such j, and define

`E_j = sum_(n assigned to j) multinomial(L;n) prod_i g_i^(n_i)`.

Then `sum E_j=1`, and every E_j is divisible by `v_j^L0`. This is a complete exact formula for the polynomial; its expansion is unnecessary for the proof. Set `B_j=E_j/v_j^L0`, which is polynomial by construction.

### 5.3 Two-carrier identity and its powered form

For every j,

`v_j^5 = h_j + v2*a`.

Set `M=2N-1` and define the polynomial numerators

`C_j = sum_(k=N)^M binom(M,k) h_j^k (v2*a)^(M-k)`,

`D_j = sum_(k=0)^(N-1) binom(M,k) h_j^k (v2*a)^(M-k)`.

They satisfy `C_j+D_j=v_j^(5M)`, with `h_j^N | C_j` and `a^N | D_j`.

Apply §5.2 with `L0=5M`, and define carrier weights on U_e by

`R_j=B_j C_j` for 0<=j<=s, `R_j=0` for j>s,

`R_*=sum_(j=0)^s B_j D_j`.

All are regular polynomials on U_e, their sum is 1, and they are divisible by `h_j^N` and `a^N` respectively. This clears the apparent `v_j^(5M)` denominators in the intermediate two-carrier partition without inverting v_j on U_e.

### 5.4 Legal-line weights

For a finite coordinate choose `L_i0=1`, `L_i1=0`; its whole standard chart is already W_i0.

For an infinity coordinate t=Y/X, use `t^2+(1-t^2)=1`. With the same N and M=2N-1, set

`L_i0=sum_(k=N)^M binom(M,k) (t^2)^k (1-t^2)^(M-k)`,

`L_i1=sum_(k=0)^(N-1) binom(M,k) (t^2)^k (1-t^2)^(M-k)`.

Their sum is 1; `t^N` divides L_i0 (in fact t^(2N) does), and `(1-t^2)^N` divides L_i1. These are the respective complement equations for W_i0 and W_i1 inside the infinity chart.

Finally define, once on each U_e,

`rho_(e,b,m)=R_b prod_i L_i,m_i`.

These regular polynomials sum to 1 over b,m. They have the required carrier and legal-line divisibilities. The same weights are then restricted to every target intersection; they are not recomputed on faces or separately for individual source components.

The formulas are valid over the coefficient ring whenever the geometric source is defined. They involve integer binomial coefficients and no division by factorials. This does not by itself certify a characteristic-three bundle or comparison of its obstruction with the characteristic-zero one.

## 6. The one common pole-domain requirement

Fix one N before using the weights. It must dominate the per-inserted-vertex carrier and legal-line poles of **all** components J0,J1,J2,J3, their restrictions and Cech/End differentials, and the cochain entries used in the prism below, in the actual transported frames.

A sufficient precise domain is the subcomplex of common-cover cochains whose coefficient on each tuple becomes regular on the corresponding standard target intersection after multiplication, for each vertex occurrence, by the Nth powers of its carrier equation and the legal complement equations that are not already units. Distinct carrier owners or repeated factors are not silently identified. Addition, restrictions, and the Cech differential preserve this bound; `d_End` is a regular sheaf map and introduces no new carrier or legal denominator. This gives one linear chain map on a D-stable domain.

The weighted prism clears each newly inserted vertex using the corresponding rho and leaves the original vertex denominators in the allowed domain. Thus the same N suffices for the prism when the bound is formulated per vertex occurrence as above. Arbitrary cancellation is not needed.

The existing [451-entry seed table](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-geometric-dependencies/data/divisor-seeds.json), the derivative rule in [frames and poles §1](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-geometric-dependencies/frames-and-poles.md), and the [unexpanded source formulas](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-geometric-dependencies/data/source-formulas.js) give the following coarse bound. The completed scalar's smaller allocation is not reused as a bound for all J components.

### 6.1 Conservative full-source bound N=62

For a fixed owned carrier divisor, addition takes the maximum pole order and multiplication adds orders. One ordinary local derivative raises an existing order by at most one; it introduces no absent carrier divisor. Apply this entrywise, ignoring all cancellations and allowing repeated carrier owners.

The pinned [seed certificate](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-geometric-dependencies/certificates/divisor-seeds.json) has primary factor maxima (1,1) and auxiliary maxima (2,2,1,1). Thus every I,P,H0,H1 entry has order at most 2 in every owned factor. Primary factors are `(v_j,F_j)`, where `h_j=v_j F_j`; auxiliary factors are `(v0,v1,v3,v4)`. The six pivots in the pinned model are `(0,1,2,3,4,0)`, so W and eta invert only a factor of their own carrier. Bound their orders by 2 as well. The resolution arrows and L have order zero.

The exact source gives the following carrier-order ledger:

- `U0=(gamma,I,H1 W)`: at most 4; `Q0=(H0;P;L delta_K)`: at most 2. U1 and Q1 obey the same upper bounds.
- `B=-(partial U)Q-old_connection`: at most `(4+1)+2=7`; the connection has no carrier poles.
- `g` and `g^-1`: at most 4. The latter is the two-by-two adjugate because the pinned source proves determinant one for all 36 carrier pairs, so no new determinant denominator is inserted.
- `K=mu1(g^-1,g)`: at most `5+5=10`.
- The scalar first-lift term is a sum of B_i B_j, qB, and qq terms, hence at most 14. Therefore `u=g(s I-K/2)` has order at most 18.
- In the mixed residual, `u*u` has order at most 36; `mu1(u,g)` and `mu1(g,u)` at most `19+5=24`; the mixed `mu2(g,g)` at most `6+6=12`; the gerbe terms at most 18. Thus the complete full-sign R has order at most 36.
- Left normalization by `g^-1` gives C2 at most 40; `J0=I C2^t P` gives at most 44.
- Each undifferentiated End homotopy `h(F)=HF+(-1)^r(IP)FH` adds at most `2+2+2=6`. Cech differences introduce no carrier poles. Hence J0,J1,J2,J3 have respective bounds `44,50,56,62`.

This bounds all matrix entries, all source masks, and auxiliary as well as primary carriers. It does not use sparse scalar rows, disjoint prefix/tail owners, or a vanishing assumption. A carrier factor absent from the source tuple remains absent: every inverse comes from a primitive at a vertex of that tuple. Clearing with h_j^62 or a^62 therefore respects factor ownership. Each occurrence of a primitive is charged to its vertex occurrence; identifying two equal polynomial factors does not transfer that charge to an absent carrier.

Legal-line poles have a smaller conservative ledger. Work directly in each local homogeneous physical frame, not by multiplying an affine bound by an unsupported Laurent factor. On a finite coordinate the nontrivial squared ratio is `(x^2-1)/x`; on an infinity coordinate t it is `t` for mask zero and `1-t^2` for mask one. These are the exact transported ratios in frames-and-poles §2. Their logarithmic derivatives and the transported old connections have order at most one on their respective legal complements. On the finite chart q/y is `(m_j-m_i)/x`, so a nonzero term has a mask-one vertex. On the infinity chart q/z is the corresponding signed `(m_j-m_i)/t`, so a nonzero term has a mask-zero vertex. Thus every legal pole is assigned to an actual vertex with the appropriate mask.

Assign cost at most one to each nu or nu inverse, and also to each nu squared or inverse squared, on the relevant base divisor. This is conservative even before the invariant product descends. The physical U and Q column weights have legal cost at most one; one stripped local derivative raises that cost by at most one. Accordingly B has cost at most 3; g and its adjugate at most 2; K and the scalar first-lift term at most 6; u at most 8; R at most 16; normalized C2 at most 18; included J0 at most 20. A physical H has at most one squared-ratio factor, and IP at most two single-ratio factors, so each End homotopy adds at most 3. This gives legal bounds `20,23,26,29` for J0,...,J3.

The local infinity calculation matters: the source's general internal-degree covariance is `c_S=tau^(r-2)c_affine`, including r=-3. The local homogeneous primitive matrices, squared ratios t and 1-t^2, and invariant vector field `-z partial_t` already implement this covariance before taking pole orders. An extra t^-5 bound must not be appended afterward: it could falsely create a pole at a mask-one vertex where t=0 is allowed. No same-coordinate second derivative is needed in the mixed full-sign formula, so no omitted second derivative of a coordinate change enters this argument.

Taking N=62 dominates both ledgers. The same per-vertex bound applies to restrictions and the D-stable domain of §6, and the prism clears inserted vertices without taking further derivatives. This is a source-reading/max-add proof; no full residual coefficients, pole-graph expansion, or independent executable replay were produced here. A computational implementation should audit the ledger against the pinned operation graph before numerical use. The high-powered partitions are checkable expressions, not an efficiency claim or permission to expand them.

## 7. Weighted projection and its regular prism

For a common-cover cochain c define

`(Pi_rho c)_(e0...eq) = sum_(alpha0,...,alphaq) (prod_i rho_(ei,alphai)) c_((e0,alpha0),...,(eq,alphaq))`,

where alpha=(b,m), and every term is extended regularly onto the standard target intersection by the pole-domain certificate. Fixed vertex weights and `sum_alpha rho_(e,alpha)=1` give

`Pi_rho delta=delta Pi_rho`, `Pi_rho r*=1`.

For an increasing common-cover tuple `a0,...,a_(q-1)`, with r(ai)=ei, define

`(H_rho c)_(a0...a_(q-1))`

`= sum_(k=0)^(q-1) (-1)^k sum_(beta0,...,betak) (prod_(i=0)^k rho_(ei,betai)) c_(b0,...,bk,ak,...,a_(q-1))`,

where `bi=(ei,betai)`. Extend the resulting cochain alternatingly. On degree zero put H_rho=0. As in the [pinned ordered prism proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-proof/residue-theorem.md), consecutive pivot terms cancel, sums at deleted inserted vertices use sum rho=1, and the endpoints give

`delta H_rho+H_rho delta=1-r*Pi_rho`.

Repeated target vertices remain in the sum; only identical alternating source vertices vanish. The new partition is adapted to the full End-valued pole domain, rather than importing the scalar merger.

The weights commute with `d_End`, and H_rho lowers Cech degree by one, so

`D Pi_rho=Pi_rho D`, `D H_rho+H_rho D=1-r*Pi_rho`.

## 8. Closed formulas for z and the six-equation primitive

Use the fixed N-domain and partition above. Set

`u=s*J`, `c=Pi_rho u`, `z=S c`,

`W= -H_rho u - r*K c`.

All maps and signs have been specified. Because Du=0, the chain identities give

`Dz=0`,

`u-r*c = D H_rho u`,

`c-Az = D Kc`.

Adding the last two identities gives exactly

`r*Az-u = DW`.

Thus the comparison in the previous note is instantiated by the map `r*A`, rather than an unspecified restriction from tensor cochains. No new linear system for W is required.

In internal degrees this is the same six-equation ladder:

`r*Az0 = d W0`,

`r*Az1 = delta W0-d W1`,

`r*Az2-J0 = delta W1+d W2`,

`r*Az3-J1 = delta W2-d W3`,

`r*Az4-J2 = delta W3+d W4`,

`-J3 = delta W4`.

Restrictions from the source cover to the common cover are suppressed here. The final identity follows because S has no degree-five target and A is zero above degree four; the top source component has been removed by the displayed homotopy, not discarded.

All these cover maps preserve internal degree. Since J has no internal-degree-positive component, the constructed tensor representative has `z0=z1=0`. Thus this particular source evaluation requires only `lambda_2(z2)+lambda_3(z3)+lambda_4(z4)`. The explicit lambda1 unit control in the earlier note remains a control on the general dual map, not a term that must be evaluated for this representative.

## 9. A bounded certificate and the actual evaluation target

A replayable, coefficient-free comparison artifact can contain:

1. The cover equations and fixed source/target ordering; the original-frame dictionary.
2. The cut map A, staircase map S, and rectangle-cone recurrence k, with the two-coordinate sign controls above and exact symbolic chain proofs.
3. The uniform source-bound ledger N=62 for the full J-domain, or a sharper independently certified replacement, checked against the pinned primitive/source formulas without recovering held residual coefficients.
4. The explicit partition formulas at that N, checked by the coefficient identity, multinomial partition, binomial partition, and divisibility proofs; no expanded partition polynomial is required.
5. The displayed z/W formulas and six identities as consequences of the verified chain operations.

Once these checks are supplied, the source-to-finite comparison is the concrete composition

`P_actual = p(1+Delta H)^(-1) S Pi_rho s* J`.

Here J on the right denotes the chain inclusion applied to the actual full-sign residual, while H is the pinned tensor Cech contraction. The actual detector is

`ell(P_actual(C2_full^t)) = Lambda(S Pi_rho s*J(C2_full^t))`.

Its finite Laurent support can then be used to request only the required transported coefficients. The partition/formula proof does not evaluate those coefficients or show that their construction fits the held polynomial budget. No numerical value, deformation conclusion, or new computational release follows from this note.
