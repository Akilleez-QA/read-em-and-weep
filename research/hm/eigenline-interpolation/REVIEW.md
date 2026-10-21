# Independent review: universal eigenline interpolation

Reviewed 2026-10-21. Verdict: **PASS, with the representation hypothesis stated below retained explicitly.** This is an independent mathematical audit, not formal proof-assistant verification. No evaluation matrices, numerical ranks, selected HM/source coefficient tests, or public writes were used. This review is independent of any degree-two conductor-generation argument.

## 1. Exact scope of the universal assertion

The opening hypothesis of PROOF.md is correct: work over C with a five-dimensional irreducible representation of the order-125 Heisenberg group having nontrivial central character. Equivalently, a five-dimensional module on which the center acts by a fixed nontrivial character is necessarily irreducible. Every such module has a Schrödinger basis, with the primitive fifth root chosen to match its central character. Changing basis transports both the configuration and restriction map, so surjectivity is basis-independent. Primitive-power changes and dualization relabel the displayed projective configuration; they do not identify inequivalent linear representations.

“Any five-dimensional Heisenberg module” without this qualification would be false. For example, the five-dimensional trivial module has no canonical collection of thirty distinct one-dimensional eigenspaces. The qualified theorem actually written in PROOF.md has no such defect. Summaries must preserve the qualification.

## 2. Symbolic interpolation checked independently

For sigma(e_i)=e_(i-1), the coefficient of e_i in sigma(v_(a,b)) is zeta^(a(i+1)^2+b(i+1)). Applying tau^(-2a) cancels its extra 2ai term, leaving eigenvalue zeta^(a+b). For fixed a, the five eigenvalues as b varies are distinct. The five directions (-2a,1), together with the tau direction, exhaust the six lines in F5². Coordinate vectors supply the remaining five eigenlines. All chirps have nonzero coordinates; equality of their normalized representatives forces equality of a,b, since a quadratic polynomial with zero values at all five residues has zero coefficients.

The PR554 substitution q=zeta^(2a), r_0=zeta^(a+b) gives the exponent (a+b)i+a i(i-1)=a i²+bi exactly. Thus the configuration consists of points in the stated representation, not inadvertently of dual hyperplanes.

The seven displayed S=0 triples have square sums respectively 0,2,3,1,4,1,4 modulo five. In particular, the first five alone already witness every possible Q. Simultaneous translation of the three indices gives (Q,S) -> (Q+2tS+3t²,S+3t), so starting with S=0 and choosing t=S'/3 supplies every (Q',S'). Repeated indices are valid monomials. The Fourier inversion formula follows from the two geometric-series identities over F5; its sign, normalization 1/25, and assignment of Q,S all agree. Hence cubics prescribe arbitrary values on the twenty-five normalized chirps.

The sums of all five indices and of their squares are both zero modulo five. Consequently the exponent of product_(j != i) x_j at v_(a,b) is -(ai²+bi)=4(ai²+bi), exactly the exponent of x_i^4. Thus each F_i vanishes on every chirp. At e_j the product term is zero, whereas x_i^4 is delta_(i,j). Multiplying the interpolating cubic by x_0 preserves all chirp values, and adding the stated linear combination of F_i independently corrects all five coordinate values. This proves the full quartic restriction surjectivity without a rank computation. Trivializing the thirty fibers by representatives is legitimate and does not change surjectivity. A hyperplane avoiding this finite set exists over C; its powers give the stated all-d>=4 extension.

## 3. Pinned source check and actual-node identification

The following four files were read directly through the read-only GitHub connector at the exact commits specified in PROOF.md. Their returned immutable URLs and file contents support the quoted inputs:

- PR553, commit 342e2e3754664477026e4fcc3bc6a135a1eab9cc, research/hm/heisenberg-support-points/PROOF.md, blob 67dd9cdda130404f0107e6e652d1c4ed0f03b0f6: thirty distinct canonical eigenlines and actual primary rank exactly eight at every one.
- PR554, commit eb16c0e38e5157dc2902273cea3939b3410057c7, research/hm/global-support-finiteness/PROOF.md, blob 4b6ffb14a663ee3c55c65fdaff368243399e668a: the five coordinate points and exactly twenty-five torus points in the quoted ratio convention.
- PR573, commit 6c2dbd48edea0577acf063a60e1edbbbe92ced5c, research/hm/global-primary-equality/PROOF.md, blob 2f8f8bc7085f541a905e33b496978f2a3ed6f5a3: global scheme equality D9(e)=S, the exact sigma/tau convention, and smoothness except at thirty transverse double points.
- PR578, commit d3f1135f7c3c1104ec431fcc44fdb5e2d80bb078, research/hm/primary-postulation/PROOF.md, blob ebd673b5912a1630224aa8e7ca14c0c0ad1e8ad6: cubic very ampleness, normalization branch-difference sequence, H¹(X,nH)=0 for n>=1, the specified divisor intersections and canonical class, and the central-character divisibility of the image dimensions.

This checks the dependency statements against their pinned files; it does not claim to reprove every upstream geometric theorem or its original literature dependencies.

Locally e is a map from a rank-12 bundle to a rank-10 bundle. Its rank-at-most-nine degeneracy ideal is generated by 10-by-10 minors. At a rank-eight point every 9-by-9 cofactor vanishes. The Leibniz derivative of every defining minor is therefore zero, including when the entries vary in a local bundle trivialization. The ideal is contained in the square of the ambient maximal ideal, so its Zariski tangent space is the full four-dimensional ambient tangent space. Scheme equality transfers this tangent statement to the two-dimensional S; every eigenline is singular. The independent statement that S has precisely thirty singular points then identifies its node support with the thirty already-distinct eigenlines. This is a valid inclusion-plus-cardinality argument, not identification by cardinality alone. The length-one quotient at every transverse node supplies the reduced-support property used subsequently.

## 4. Conductor multiplication and cohomological consequences

Very ampleness of the complete |3H| separates the two distinct normalization points over each node. A section vanishing at one but not the other has a nonzero branch difference regardless of fiber trivializations. Thus each coordinate difference functional is nonzero. The complement of the union of its thirty proper kernels is nonempty over C; a single s can be chosen with every difference coordinate nonzero.

The quotient nu_*O_X/O_S is O_S-linear. Hence rho_(3+d)((nu^*p)s)=(p|_Z)rho_3(s), with the twists as written. At each reduced node multiplication by the nonzero value of rho_3(s) is an isomorphism between its one-dimensional fibers. Ambient quartic interpolation consequently gives surjectivity of rho_7, and multiplication by a linear form avoiding Z propagates it to every n>=7. Cubic interpolation only gives a surjective projection onto twenty-five node summands in degree six, hence r_6>=25; no unproved independence for the other five summands is assumed. The cited primitive-character divisibility at n=6 then restricts r_6 to 25 or 30.

The normalization long exact sequence and H¹(X,nH)=0 identify H¹(S,O_S(n)) with coker(rho_n) for n>=1. Thus h¹(O_S(6))<=5 and H¹(O_S(n))=0 for n>=7 follow. The zero-dimensional quotient also gives H²(O_S(6))=H²(X,6H). Serre duality reduces its vanishing to H⁰(K_X-6H)=0. The fiber class F is nef, and (K_X-6H).F=-30, excluding an effective divisor in that class and proving the vanishing.

Therefore H¹(O_S(7))=H²(O_S(6))=0; higher cohomology vanishes by two-dimensional support. These are exactly the conditions for 8-regularity of O_S on P4. The asserted complete-section multiplication for n>=8 is a valid Castelnuovo-Mumford regularity consequence.

## 5. Limits and final verdict

No step identifies ambient polynomials with all complete sections on S. The proof establishes neither ambient projective normality, vanishing of H¹(I_S(n)), ideal-sheaf regularity, nor ideal generation. It also does not independently establish r_6=30. Any stronger combined corollary must cite its separate additional input.

The independently audited standalone results are quartic interpolation on all thirty eigenlines, cubic interpolation on the twenty-five chirps, r_n=30 for n>=7, r_6 in {25,30}, and 8-regularity of O_S, relative to the explicitly pinned geometry. No mathematical correction to PROOF.md is required. Preserve its nontrivial-central-character irreducibility hypothesis in every universal summary.
