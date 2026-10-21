# Exact postulation of the thirty Heisenberg eigenlines

Status: independently mathematically reviewed (PASS); see REVIEW.md. Not formally checked. Work over C. No evaluation matrix, numerical rank test, selected HM/source coefficients, or large computation is used.

## 1. Inputs, hypothesis, and novelty

Let A be a five-dimensional irreducible Schrödinger representation of the order-125 Heisenberg group with nontrivial central character. Choose a primitive fifth root zeta matching that character and a Schrödinger basis e_i, with indices in F_5. Its thirty projective eigenlines form the reduced set

Omega = { [e_i] : i in F_5 } union { [v_(a,b)] : a,b in F_5 },
v_(a,b) = sum_i zeta^(a i^2+b i) e_i.

We use the [universal eigenline interpolation proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/865ab24e91333688d7ae76303d7d594aae8521f8/research/hm/eigenline-interpolation/PROOF.md), commit 865ab24e91333688d7ae76303d7d594aae8521f8, and its independent review. That proof establishes this coordinate identification, cubic interpolation on the twenty-five chirps, and quartic interpolation on all thirty points. We reproduce the necessary symbolic arguments below; no further geometric input is needed for exact postulation.

The new assertion is the exact Hilbert function, including the strict failure of cubic interpolation on the full thirty points:

h_Omega(d) = 1, 5, 15, 25, 30, 30, ... for d = 0, 1, 2, 3, 4, 5, ... .

Consequently the least interpolation degree is four; I_Omega is exactly 5-regular, not 4-regular. The Hilbert h-vector is (1,4,10,10,5).

## 2. Characters and degrees zero through two

Write x_i for the dual coordinates and use e_i and v_(a,b) as representatives, thus fixing fiber trivializations. A degree-d monomial with index multiset (i_1,...,i_d) restricts on the chirps to

chi_(Q,S)(a,b) = zeta^(aQ+bS),
Q = sum i_j^2, S = sum i_j in F_5.

The twenty-five characters are linearly independent: the sum of chi_(Q,S) times chi_(-Q',-S') over a,b is 25 if their indices match and zero otherwise. This follows from the product of the two fifth-root geometric series. Thus the image dimension of any collection of monomials on the chirps is exactly the number of distinct characters represented, without constructing an evaluation matrix.

Constants have image dimension one. Linear monomials have the five distinct pairs (i^2,i), so have image dimension five on the chirps and hence on Omega.

For quadratic monomials x_i x_j, the pair (Q,S) determines the unordered pair {i,j}: its product is ij=(S^2-Q)/2, and i,j are the roots with multiplicities of

t^2-S t+(S^2-Q)/2.

There are fifteen unordered pairs with repetition. They therefore give fifteen distinct characters; quadratic restriction on the chirps is injective. Adding five coordinate points cannot increase the image dimension beyond the fifteen-dimensional space of quadrics. This proves h_Omega(2)=15. In particular, each pure square has its own unique character and its coefficient, which is the value at e_i, is already determined by chirp values.

## 3. Cubic character coverage and unique pure-cube characters

For sum S=0 the triples

000, 014, 023, 113, 122, 244, 334

have square sums respectively

0, 2, 3, 1, 4, 1, 4.

Only coverage of the five square sums is needed here. Translating every index by t transforms (Q,S) into

(Q+2tS+3t^2, S+3t).

Since 3 is invertible in F_5, translates of the displayed triples supply every character (Q,S). Hence cubic restriction onto the chirps is surjective, with image dimension 25.

We must show that adding the coordinate points supplies no additional independent conditions. A pure cube x_i^3 has pair (3i^2,3i). Suppose an arbitrary cubic monomial has this same pair. Translate all its indices by -i. Its resulting indices u,v,w satisfy

u+v+w=0, u^2+v^2+w^2=0.

Eliminate w: u^2+uv+v^2=0. If v=0, this forces u=0. If v is nonzero, u/v would be a root of t^2+t+1, whose discriminant is -3=2 in F_5. Since 2 is not a square in F_5, no such root exists. Therefore u=v=w=0, and the original monomial is x_i^3. This proves pure-cube character uniqueness without needing completeness of the seven-triple list.

For a cubic P, the coefficient of chi_(3i^2,3i) in its chirp restriction is consequently exactly the coefficient of x_i^3, hence P(e_i). If P vanishes at all chirps, character independence forces every pure-cube coefficient to vanish, so P vanishes at every coordinate point too. Thus the kernels of cubic restriction to the chirps and to Omega coincide, proving

h_Omega(3)=25 and dim H^0(I_Omega(3))=35-25=10.

In particular the five-dimensional cubic deficit on Omega is real, not just a limitation of an interpolation formula.

## 4. Explicit five equations for the cubic image

Write a prospective value vector as (f(a,b),c_i), indexed by chirps and coordinate points. Fourier inversion and pure-cube uniqueness give the exact necessary and sufficient equations

c_i = (1/25) sum_(a,b in F_5) f(a,b) zeta^(-3a i^2-3b i), for every i in F_5.       (1)

Necessity was just proved. For sufficiency, cubic chirp surjectivity supplies P with the prescribed f; its coordinate values must be the right sides of (1), so they equal the prescribed c_i. The five equations are independent since their respective coefficients of the five distinct c_i are one and the others zero. Thus they describe the entire annihilator of the cubic restriction image, not merely five relations satisfied by it. The formulas depend on the chosen representatives, but the resulting image and codimension are intrinsic.

## 5. Quartics, eventual stabilization, and regularity

For completeness, define F_i=x_i^4-product_(j != i) x_j. Since the sums of all indices and their squares vanish in F_5, both terms have the same character on the chirps, and F_i vanishes there. At the coordinate points F_i(e_j)=delta_(i,j).

Given chirp values, choose an interpolating cubic C. Since x_0 is one on every normalized chirp, x_0 C preserves those values. Adding suitable multiples of F_i then adjusts the five coordinate values independently. Hence quartic restriction is surjective. A linear form ell avoiding all thirty points exists over C. Multiplication by ell and division of prescribed target values by its nonzero fiber values propagate surjectivity to every degree d>=4. This proves the stated exact Hilbert function.

The first differences are (1,4,10,10,5,0,...), so the Hilbert series of the homogeneous coordinate ring R is

Hilb_R(t) = (1+4t+10t^2+10t^3+5t^4)/(1-t).

This is indeed its Artinian-reduction h-vector: ell is a nonzerodivisor on R, since R embeds in the product of the homogeneous coordinate rings of the reduced points, and ell is nonzero on each point. The Hilbert series of R/ell R is therefore the numerator.

Apply 0 -> I_Omega(k) -> O_P4(k) -> O_Omega(k) -> 0. All higher cohomology of O_Omega(k) vanishes. Since H^1(O_P4(k))=0, H^1(I_Omega(k)) is the cokernel of restriction, and

h^1(I_Omega(3))=30-25=5,
H^1(I_Omega(k))=0 for k>=4.

For 5-regularity the remaining groups are H^2(I_Omega(3)), H^3(I_Omega(2)), and H^4(I_Omega(1)). Each agrees with the corresponding cohomology of O_P4 at that twist by the same sequence and is zero. Thus I_Omega is 5-regular. It is not 4-regular because H^1(I_Omega(3)) is nonzero. By Castelnuovo-Mumford regularity propagation it cannot be m-regular for any m<4 either; its exact sheaf regularity is five.

Regularity implies generation of the saturated homogeneous ideal in degrees at most five (and the usual multiplication surjectivity from degree five onward). This statement does not assert the presence of minimal quintic generators or determine the minimal free resolution. It concerns I_Omega only, not the ideal of any surface containing Omega.

## 6. Precise contribution and limitation for the primary conductor

Suppose the primary normalization nu:X->S and branch-difference quotient T satisfy the pinned geometric inputs of the interpolation proof: T has one-dimensional reduced fibers at these exact thirty nodes. Suppose also there is a section s in H^0(X,2H) such that q=rho_2(s) is nonzero at every node. This quadratic-section input is separate from the universal eigenline theorem. It is supplied for the actual primary surface by the [quadratic conductor-generation proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/7547a6a0d84d29478a0bad2d30bda271c37c269e/research/hm/quadratic-conductor-generation/PROOF.md), commit 7547a6a0d84d29478a0bad2d30bda271c37c269e, Sections 2–3: im(rho_2) projects nontrivially onto each node fiber. Each coordinate kernel is then a proper linear subspace of H^0(X,2H), and their finite union cannot exhaust that space over C. Choosing s outside this union gives the required nowhere-zero q. This does not follow merely from the Hilbert function.

O_S-linearity of the conductor map gives

rho_5((nu^*P)s) = (P|_Omega) q for every ambient cubic P.

Since q has no zero fiber, coordinatewise multiplication by q is invertible. Therefore the conductor-image subspace obtained by multiplying this single fixed quadratic section by all ambient cubics and then applying rho_5 has dimension exactly 25, not 30. This is a dimension statement about branch differences, not about the space of product sections on X. If q_(a,b) and q_i denote its nonzero fiber coordinates in compatible trivializations, this product subspace consists exactly of value vectors g obeying

g_i/q_i = (1/25) sum_(a,b) (g_(a,b)/q_(a,b)) zeta^(-3a i^2-3b i), for every i.       (2)

This gives a rigorous exclusion: one fixed nowhere-zero quadratic difference times ambient cubics cannot by itself prove r_5=30. Equation (2) also identifies the precise five residual obstructions to that particular construction, so additional quadratic sections or other degree-five normalization sections can be tested symbolically against these five functionals rather than a full thirty-coordinate problem.

The full rho_5 image may be larger. This one-section calculation does not determine its exact dimension; no exact value of r_5 follows from this exclusion. Other primary-geometry constraints must still be respected. Nor may (2) be imposed on arbitrary degree-five normalization sections without proving that they lie in the indicated product subspace.

More generally, for any fixed nowhere-zero degree-m branch-difference section, the conductor-image dimensions obtained by ambient multipliers of degrees 0,1,2,3,4,... are exactly 1,5,15,25,30,... . Thus quartic multiplication is the sharp uniform threshold for this one-section interpolation construction.

## 7. Actual-primary rank range and sharp stabilization degree

The preceding construction gives r_5>=25 for the actual primary surface. Independently, [PR578's primary postulation proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/d3f1135f7c3c1104ec431fcc44fdb5e2d80bb078/research/hm/primary-postulation/PROOF.md), commit d3f1135f7c3c1104ec431fcc44fdb5e2d80bb078, Section 3, records h^1(O_S(5))>=1. Its normalization cohomology identity gives r_5<=29. Consequently

25 <= r_5 <= 29 and 1 <= h^1(O_S(5)) <= 5.

For clarity, these upper bounds use the cited primary geometry, not the universal point-configuration theorem. No exact r_5 is asserted.

PR578's strict-growth lemma gives r_6>r_5 because r_5<30. Hence r_6>=26. Its nontrivial-central-character divisibility gives 5 | r_6, so r_6=30. Multiplication by a linear form avoiding the node support propagates this equality to every n>=6. Thus, with the separate pinned quadratic conductor input, degree six is the exact first degree of full conductor surjectivity: degree five is not full, and no earlier degree could be full since such fullness would propagate to degree five. This agrees with the separate quadratic conductor-generation proof, while identifying the exact failure at degree five and the five-dimensional barrier for a single quadratic section.

The same pins give exact regularity of O_S as a sheaf on P^4, distinct from the point ideal I_Omega. The quadratic conductor-generation proof gives 7-regularity. Since H^1(O_S(5))>=1, the first required vanishing for 6-regularity fails. Regularity propagation excludes every smaller regularity index too. Therefore O_S has exact regularity seven. No corresponding assertion about the surface ideal sheaf I_S follows.
