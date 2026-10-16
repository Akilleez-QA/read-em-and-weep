# QH01: bounded inner N14 quotient coefficient program

`quotient.py` supplies the missing generic first-hit composition coefficient algorithm. It imports the same exact demand-convolution Ring, Budget and FullOwner interfaces as INS01. Actual N14 chart formulas compile as metadata only. Every actual coefficient and finite-stream entry point raises PhysicalAdmissionMissing before even testing support. This artifact supplies no physical source value, execution admission, homogeneous-frame identification or obstruction result.

`source-pins.json` authenticates both consumed texts at commit10810ee877fdaf291399198ad60d7dd0c316a42d: `null-operator-compiler/outer_partition_source_binding.py` (blobf5a33e325e1eee6b801c94613093d1cd4686ca54) and `null-source-integration/combined-pole/PROOF.md` (blob9d7a5a400b48d9b8b46008fbd9fb3d79be601920). The former's parameterized PartitionChart formula is specialized to carrier_power14, legal_power1; it is not the outer54/legal29 program. ActualCatalog authenticates these Git contents at construction. No public module or historical physical evaluator is executed.

For standard bits e_i (high bit3-i), s=sum(e_i), and parameter N, put M=2N-1, T=5M and L=(s+1)(T-1)+1. Local v_j is the coefficient of z^j in product_(finite)(1+x_i z) product_(infinity)(t_i+z). Local h_j=v_j^5-product(v_0,...,v_4), a=v_0v_1v_3v_4. Complete homogeneous H_k uses only finite variables, including H0=1 and H_k>0=0 for an empty finite alphabet. Define c_i=(-1)^(s-i)H_(s-i).

The first-hit node for j sums over n_0+...+n_s=L with n_j>=T, n_i<T for i<j, and all n_i>=0. Its summand is multinomial(L;n) product_i c_i^n_i v_i^(n_i-T*[i=j]). All powers are nonnegative. The recursive enumeration visits every constrained composition exactly once; no coefficient or support cutoff removes an admissible term. Chained binomials compute the multinomial over integers. Prior slots are bounded by T-1, the chosen slot starts at T, later slots are unrestricted up to the remaining sum. No first-hit compositions are expanded during metadata compilation.

Primary quotient j<=s is B_j times

    sum_(k=N..M) binom(M,k) h_j^(k-N) (v2*a)^(M-k).

Primary j>s is zero. Auxiliary quotient is sum_(j=0..s) B_j times

    sum_(k=0..N-1) binom(M,k) h_j^k v2^(M-k) a^(M-k-N).

The endpoint ranges are inclusive as displayed. For N14, M27/T135 and L=134(s+1)+1. The whole catalog data are local chart polynomials, not finite-frame I/P entries.

For pair p, Qhat multiplies the carrier quotient by pair Qline and complementary raw legal weights. Finite Qline/raw weight=(1,0). Infinity Qline=(t,1); complementary raw weights=(t^2,1-t^2). The common finite-frame exponent shift at infinity coordinate i is -N*d_owner-deg(ell_owner,i)*[i in p], where d=5 for primary and4 for auxiliary, and deg(ell)=1 or3 from the low-bit mask. Local exponent alpha maps to shift-alpha at infinity and alpha at finite coordinates. There is no additional pair or section twist. Input owner seed, occurrence, carrier, legal mask and standard tag are retained exactly; no owner sorting or merging occurs in Qhat.

`QuotientProgram(owner, ActualCatalog(), N=14, pair=p)` compiles this metadata and supplies a conservative finite `support_box()`. Actual coefficients remain unavailable. This is syntactic formula binding, not geometric authentication of a physical source. `ArtificialCatalog(v,h,a,complete)` instead supplies explicit artificial base polynomials; its executable parameter range is N1 or N2. It need not satisfy physical generator identities: it tests the universal polynomial algorithm. Inputs are at most32 terms each, coordinate exponents0..2 and rational numerator/denominator bit lengths<=16. No actual catalog is accepted in this synthetic path.

`program.coefficient(global_exponent)` evaluates an exact requested Qhat coefficient. `program.factor_terms(owner,pair)` implements the INS/STD finite quotient stream interface for this one full owner. It traverses the entire conservative support box only when volume<=4096 and returns its nonzero coefficients. A larger enclosure raises; it never truncates or treats UNKNOWN as zero. A multi-owner adapter may cache programs by complete owner and pair, retaining one aggregate budget; this artifact does not enumerate actual owner fibers.

Degree enclosures may overestimate cancellations. The first-hit enclosure L*max_i(deg(c_i)+deg(v_i)) is sound because dropping the chosen v_j threshold subtraction only enlarges a bound. Other operations propagate exact nonnegative-power enclosures, followed by the signed affine chart reversal. Coefficient products convolve only the finite exponent range compatible with both operand enclosures. No infinite Laurent truncation is used.

The shared budget caps metadata nodes40000, aggregate coefficient queries100000, convolution splits200000 and cached demands100000. Each FiniteRing additionally caps cumulative composition/sum-index visits20000 and coefficient bit lengths4096. Caps abort with an exception; they do not yield a partial coefficient. The complete synthetic stream has a separate volume cap4096. These are conservative development guards, not a physical cost certificate or hard memory supervisor.

Replay from the repository root:

    python -m unittest discover -s research/codex-swarm/inner-quotient -p test_quotient.py -v
    python -O -m unittest discover -s research/codex-swarm/inner-quotient -p test_quotient.py

Seven artificial controls pass: independent first-hit binomial sums and disjointness, Cbar/Dbar endpoint counts, polynomial convolution against binomial coefficients, frame reversal with both pair/complement mask cases, zero finite masks and unavailable primary carriers, authentic actual N14 metadata refusal, and aggregate cap failures. No actual polynomial coefficients are evaluated. Reserved independent reviewer files are `test_independent.py` and `review-independent.md`.
