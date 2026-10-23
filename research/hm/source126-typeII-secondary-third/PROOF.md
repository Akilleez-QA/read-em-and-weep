# A secondary naturality test is injective on the Type II cubic gate

## Result and limits

Retain the actual full-radical source126 Type II hypotheses of PR982 and PR980. Let

    E=coker[A O(-1) --a multiplication--> D O],
    r:D O(-3)→E

be the canonical internal third symbol, and let κ:O(-5)→D O(-1) be the kernel sheaf of the quotient first symbol h↦[a h] in Sym⁶W/V6. Write ρ(a)h={a,h}_1, and let ν be the secondary scalar on the canonical radical kernel line J0 supplied by PR980.

The linear restriction

    r ↦ r ρ(a) κ

is INJECTIVE on the canonical two-dimensional space of equivariant cubic maps satisfying rκ=0. The first composition is a bundle map O(-8)→E; the original κ restriction is O(-7)→E, with twists understood. The target invariant section space H0(E(8))^G has dimension two, so this restriction is an isomorphism onto that target.

Consequently the actual symbols satisfy the conditional alternative

    ν=0  OR  r=0.                                    (1)

If ν≠0, the original fourth Bockstein on its GENERIC surviving D kernel is zero by PR982. Neither ν nor r is selected here. In particular this is not an exclusion of Type II, full-J compatibility, any source pair, or the original proof problem. No claim is made about specialized extra kernel classes at exceptional directions or higher original symbols.

This is a symbolic representation computation on the entire parameter chart, combined with exact chain-map naturality. No selected HM coefficient, source instance, point, quadratic value, actual obstruction matrix or actual rank is evaluated.

## 1. Immutable inputs

INPUTS.json authenticates:

- PR982,25df67afcafd5f84c2c0cda7e6baee41fdbf8212, research/hm/source126-typeII-internal-third/PROOF.md. It constructs r globally, proves Hom_G(D O(-3),E) has dimension three, proves its κ-zero subspace has dimension two, and compares r with the original fourth symbol on the generic D kernel. Its internal-second-vanishing dependency remains in force.
- PR980,3dd68c99b9dfd85fe10cc327c2fa95c24bc185f5, research/hm/source126-typeII-secondary-homotopy/PROOF.md. Its unique equivariant homotopy supplies the genuine chain map K_a for the SAME Q+tL_a family, with induced k0,a=(0,νρ(a)) and k1,a=0.
- The exact universal projection script verify_positive_second_bockstein_symbols.py at6c724c3b74e2ae4d6992d8c7b99b41c0715d69c0, research/hm/order-four-quadratic-load/. Only its universal P6 projection of Sym⁶W onto P is used, not its unrelated higher computations or any selected actual data. The projection is verified against binary-icosahedral generators in that source; the present checker repeats those identities independently.

All original geometric hypotheses are retained. The coordinate model below identifies the unique representation subsystem V6=ker P6. It does not select a realization of the actual balanced source.

## 2. The correct higher-naturality domain

Work first on the dense open of P(A) where the quotient first symbol b_T,a:D→P has rank four. After cancelling the Q-contractible blocks in T, its residual formal differential is t times a matrix whose leading term b_T,a is surjective. Every vector in ker b_T,a can be extended to a formal kernel vector to any prescribed finite order: at each order the remaining target coefficient is cancelled by solving a new equation with the surjective leading map. In particular κ(a) admits the corrections needed through the third page.

For this fixed a, PR980 gives a chain map K_a:T→S for the entire Q+tL_a family. It is constant in t even though it is linear in a. Applying it to a sufficiently high-order quotient kernel lift gives an S kernel lift whose initial cohomology class is νρ(a)κ(a). Internal first vanishing on D and internal second vanishing, as retained in PR982, therefore imply

    ν r_a(ρ(a)κ(a))=0.                               (2)

This is higher naturality ONLY on the quotient first kernel. It is not a claim that all of D consists of higher quotient cycles. Nor does it assume K_a commutes with the family in another direction b.

Both sides of (2) are global polynomial bundle maps: κ has polynomial degree four, ρ degree one, and r degree three, so the total map is O(-8)→E. The equality on a dense open extends globally. If ν≠0, (2) gives rρκ=0; PR982 already gives rκ=0. It remains to prove that these simultaneous conditions force r=0.

## 3. Explicit universal cubic covariants

Use binary variables x,y, and set z=√5. In the monomial basis x⁶,x⁵y,…,y⁶, the authenticated universal quotient matrix is

    P6 = [ z    0    1    0   -z/3   0    5 ]
         [ 0   z/3   0   -1     0   -z    0 ]
         [ 0   -z    0   -1     0   z/3    0 ]
         [ 5    0   -z/3  0     1    0    z ].

An exact basis of its kernel consists of

    v0=−x⁶/15+(2z/5)x⁴y²+x²y⁴,
    v1=x⁵y−(2z/3)x³y³+xy⁵,
    v2=−(2z/5)x⁶−3x⁴y²+y⁶.

Take the Wronskian of v0(x,1),v1(x,1),v2(x,1), with derivative orders0,1,2 as rows, and homogenize to degree12. The result is

    f=−2x¹²−(44z/5)x¹⁰y²+66x⁸y⁴+(88z/5)x⁶y⁶
      +66x⁴y⁸−(44z/5)x²y¹⁰−2y¹².                   (3)

Its degree is exactly twelve, not a guessed homogenization degree. The Wronskian is a section of O(6)^3⊗K³=O(12). The G-linearization on its determinant factor is trivial because det V6 is a character and the binary icosahedral group is perfect. Thus f is G-invariant. This also follows by direct generator checks in the verifier. No invariant form of the actual HM geometry has been selected.

Let τ_n(F,H)=Σ_i(-1)^i binom(n,i) F_(x^(n−i)y^i) H_(x^i y^(n−i)) denote the unnormalized binary transvectant, and let (d)_n=d!/(d−n)!. Put Δ(a)=q²−4pt for a=px²+qxy+ty². Define three degree-three-in-a quartic-valued operators on h∈D:

    R1(a,h)=Δ(a) τ1(a,h),
    R2(a,h)=τ9(f,a³h)/((12)_9(10)_9),
    R3(a,h)=τ8(f,τ1(a³,h))/((12)_8(8)_8).             (4)

Each output has binary degree four. Transvectants are SL2-equivariant and f is G-invariant, so each R_i induces a G-equivariant map D O(-3)→E after quotient by aA. The coefficient certificate in Section4 proves their quotient classes are linearly independent. Since the whole equivariant Hom space has dimension three by PR982, they form a basis. Thus no unidentified cubic channel is omitted.

## 4. Exact coefficient certificate for injectivity

Work on the affine chart p≠0, normalized as

    a=x²+qxy+ty²,

where q,t remain algebraically independent throughout. This is a chart of the full parameter space, not substitution of a chosen quadratic direction. Let T(a) be the4×5 matrix whose i-th column is P6 applied to a x^(4−i)y^i. Define its polynomial kernel vector by signed maximal minors,

    κ_i(a)=(-1)^i det T(a) with column i removed.

Then Tκ=0 identically. This represents the line-sheaf kernel used in PR982, up to a nonzero constant: both have degree-four coordinates and the rank-drop locus has codimension two, so the minors have no common divisor. This normalization is convenient for the certificate; nonzero scaling of κ would not affect injectivity.

To reduce a binary quartic modulo aA, set y=1 and divide by the MONIC polynomial x²+qx+t. Its remainder is degree at most one in x. It is zero exactly when the homogeneous quartic is in a·Sym²W. The computation retains every coefficient in q,t over Q(√5); it does not evaluate q or t.

For each R_i form the remainders of R_i(a,κ(a)) and R_i(a,ρ(a)κ(a)). Their coefficient matrices C0 and C1 have respectively53 and75 possibly nonzero monomial rows and three columns, using lexicographically sorted triples(degree_x,degree_q,degree_t). Exact arithmetic gives

    rank C0=1,   rank C1=2,   rank [C0;C1]=3.          (5)

The checker supplies a compact full-rank witness: rows0,53,55 of the stacked matrix are

    [ 1280√5/9       1024/81       20480/63 ]
    [ 0             −256/9         5120/3  ]
    [−20480√5/9      7936/45      152576/63 ].

Their determinant is

    −268435456000√5/2187 ≠0.                         (6)

These rows consist of one κ-restriction coefficient and two ρκ-restriction coefficients. Thus if a cubic map R=c1R1+c2R2+c3R3 has BOTH restrictions zero, (6) forces c1=c2=c3=0. In particular the ρκ restriction is injective on the two-dimensional kernel of the κ restriction. This conclusion is not inferred from the source and target dimensions. The displayed exact nonzero minor certifies it.

For completeness, the target dimension is two: from0→A O(7)→D O(8)→E(8)→0 and H1(O(7))=0, take G-invariants to obtain the difference of invariant multiplicities in D⊗Sym⁸A and A⊗Sym⁷A. The exact character calculation in the checker gives two. Hence injectivity on the two-dimensional kernel is also surjectivity onto H0(E(8))^G.

## 5. Actual consequence and precise unresolved alternative

Apply Section4 to the actual global r. It already satisfies rκ=0 by PR982. If ν≠0, Section2 gives rρκ=0, so r=0. Conversely, if the original fourth symbol is nonzero on the generic D kernel, PR982 gives r≠0, and therefore ν must be zero. These are the equivalent forms of (1).

The argument does not prove ν≠0, and does not prove r≠0. It isolates an additional compatibility condition between two actual scalar/tensor gates. A nonzero radical endpoint row does not establish nonzero secondary cohomology. The original generic fourth alternative and full repair are still unresolved.

## Verification scope

verify.py authenticates all inputs, repeats universal generator/projection identities, constructs f, κ and the three covariants, performs polynomial remainder reduction on the whole symbolic chart, and verifies (5)-(6) over the exact quadratic number field. It also checks the invariant target multiplicity and the bundle degrees. It uses only universal binary-icosahedral representation data. No actual HM-instance evaluation, numerical sampling or unbounded search appears. The proof's actual-chain and higher-naturality comparisons are mathematical arguments, not inferred from the test count or proof-assistant certification.
