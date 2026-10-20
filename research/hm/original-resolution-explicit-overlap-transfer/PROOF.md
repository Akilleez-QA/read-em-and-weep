# Explicit first-face corrections for the original stage-two derivative

## Result and scope

Use the SAME genuine original-reference directional derivative as the accepted differentiated-homotopy theorem. Let S_i be its explicit contraction-preserving correction at owner i, and let the coefficientwise operator ℒ act by ad_(S_i) at the leading owner of every ambient cochain. Write C=δℒ−ℒδ. For the actual stage-two word J2=−HδHδj, with the input held fixed, the exact identity is

    J2′ = ℒJ2 + J2 a_S − H C Hδj − HδH Cj,
    a_S = π(j′−ℒj).                                      (A)

In fixed common original-resolution coordinates, C is only the explicit first-face insertion ad_(S_(t1)−S_(t0)); its later-face terms cancel. This is not a claim that the original ambient δ varies. It is the connection defect of δ for the new, owner-dependent corrected connection.

For a scalar selector Λ, the full selected derivative is

    (ΛJ2)′ = (Λ′+Λℒ)J2 + (ΛJ2)a_S
                         − ΛH C Hδj − ΛHδH Cj.             (B)

Neither ΛℒJ2 nor the two first-face insertions nor a_S is discarded. In particular, (B) is not a trace-zero, boundary, domain, or total-divergence theorem. It reorganizes the prescribed derivative exactly. The scalar selector is called Λ here to distinguish it from ℒ; the public comparison proofs use L for that selector.

Only supplied formal identities and inert source text are used. No actual source/model/owner evaluation, physical matrix arithmetic, source polynomial product, current remainder cancellation, execution occurs.

## 1. Inputs, fixed derivative, and degrees

The principal dependency is the accepted proof with SHA-256

    641e7224e2ab1d9e530119817659439bf09d688d179d7572ff01ae63f2a753e1,

vendored as dependencies/accepted-homotopy-PROOF.md with its independent acceptance review. Its §§2, 7 identify the original-reference derivative and explicitly construct S_i. The comparison inputs are the following public files at commit 4c0e965b4de72e43c39ba863f9aa8eea15571851 of Akilleez-QA/read-em-and-weep:

- research/hm/null-differentiated-contraction-transfer/PROOF.md and its dependencies/hpl.md and dependencies/endpoint.md;
- research/hm/null-inner-boundary-domain/PROOF.md and SYNTHESIS.md.

Their full immutable links, Git blobs, and vendored-byte hashes are in pins.json. All five public snapshots were fetched read-only at that exact commit; the two proof snapshots also match the bytes already authenticated there by the accepted dependency. Hashes bind text, not mathematical truth.

Let D be the original-resolution differential and d its graded End differential. To avoid confusing D with a Čech operator, write

    d(F)=DF−(−1)^r FD,          |F|=r.

The accepted ownerwise contraction has

    D²=0, Dh+hD=1−E, E²=E, DE=ED=0,
    h²=hE=Eh=0,
    E=A B, BA=1, DA=BD=0, hA=Bh=0.

On End coefficients, the actual maps are

    H_r(F)=hF+(−1)^r EFh,
    j(R)=A R^t B,               π(F)=(B F A)^t,
    dH+Hd=1−P,                 P=jπ,
    H²=Hj=πH=0,               πj=1, dj=πd=0.              (1.1)

P is zero off internal degree zero. There is exactly one transpose in j; these are the source-bound conventions of the public hpl dependency, not alternative row conventions.

The prime is an even directional coefficient derivative, in the frozen original-reference frame. It differentiates every factor, including D, h, E, A and B. In particular d′ need not vanish. In the same fixed common ambient coordinates δ′=0, dδ=δd, and Δ=πδj is the actual row differential, including first-face conjugation. A varying input Z contributes J2(Z′) in addition to the kernel derivative considered here.

The bidegrees (Čech, internal) are d:(0,+1), H:(0,−1), j,π,ℒ,a_S:(0,0), δ,Δ,C:(+1,0), and J2:(+2,−2). The even prime and degree-zero ℒ introduce no extra graded commutator sign. The actual word −HδHδj has the same minus sign for every input Čech degree n, even though the signed stage-one HPL words differ when n changes parity. In this proof J1=Hδj always denotes the unsigned intermediate word.

## 2. The explicit correction and the induced cohomology connection

The accepted construction, applied separately to each owner with the SAME initial reference derivative, is

    B0=1−E,    A0=[E′,E],    q=B0 D′ B0,
    U0=−h q,
    k=h′−[A0+U0,h],         C0=−Dk,
    S=A0+U0+C0.                                           (2.1)

Here B0,A0,U0,C0 are auxiliary underlying-resolution maps, not the physical A,B or the transfer primitive U below. The accepted proof establishes

    D′=[S,D],       h′=[S,h],       E′=[S,E].               (2.2)

Thus ∇^natural=∇^ref−S preserves D,h,E. On End maps its coefficient correction is ℒ=ad_S, and (2.2) gives

    d′=[ℒ,d],      H′=[ℒ,H],      P′=[ℒ,P].               (2.3)

These statements compare connections; they do not replace the original derivative in the question. The original H′ remains the generally nonzero commutator in (2.3).

### 2.1 Inclusion and projection, without assuming a fixed row frame

Set v=j′−ℒj. Differentiating dj=0 and using d′=ℒd−dℒ gives dv=0. Differentiating Hj=0 and using H′=ℒH−Hℒ gives Hv=0. Therefore the actual normalized contraction implies

    (1−jπ)v=(dH+Hd)v=0.

It follows, with no choice of horizontal cohomology basis, that

    j′=ℒj+j a_S,       a_S=π(j′−ℒj).                     (2.4)

This is an identity of operators on arbitrary row cochains. Define a=πj′, as in the public differentiated-transfer proof, and b=πℒj. Then

    a_S=a−b.                                               (2.5)

Differentiating P=jπ and using (2.3)–(2.4) yields

    j(a_Sπ+π′+πℒ)=0.

Since πj=1, multiplication by π on the left proves the exact companion identity

    π′=−a_Sπ−πℒ.                                          (2.6)

Consequently the row connection ∇_R=V+a_S and the ambient End connection ∇_E=V−ℒ make j and π parallel. It is not justified to set a_S=0 while retaining the original row coefficients.

### 2.2 Explicit row action and the single transpose

Let S act on the cohomology block of the underlying resolution. Differentiation of E A=A, together with E′=[S,E], gives

    A′−SA=A c_S,             c_S=B(A′−SA).

Likewise B E=B and BA=1 give B′+BS=−c_S B. For a fixed row matrix R,

    (j′−ℒj)(R)=A(c_S R^t−R^t c_S)B,
    a_S(R)=R c_S^t−c_S^t R.                               (2.7)

This is an explicit row-endomorphism connection. In the public notation c=BA′,

    c_S=c−BSA,
    a(R)=R c^t−c^t R,
    b(R)=R(BSA)^t−(BSA)^t R.

The transpose reverses the order; reversing the sign in (2.7) would be a different connection. None of these equations evaluates the actual matrices.

## 3. Exact first-face defect, with original ambient and row transports kept distinct

For an ambient Čech n-cochain F, define

    (ℒ_n F)_(t0...tn)=[S_(t0),F_(t0...tn)].

The owner is selected before face deletion, exactly as in the frozen Lift recurrence. In fixed common ambient coordinates,

    (δ_n F)_(t0...t_(n+1))
      = Σ_(k=0)^(n+1) (−1)^k F_(t0...hat(tk)...t_(n+1)),

where all terms are restricted to the same overlap. Let

    C_n=δ_nℒ_n−ℒ_(n+1)δ_n.

For every k>0 the deleted face still has leading owner t0, so its two commutator terms cancel exactly. The k=0 face has leading owner t1 and sign +1. Hence

    (C_n F)_(t0...t_(n+1))
      =[S_(t1)−S_(t0),F_(t1...t_(n+1))].                  (3.1)

All factors on the right are first restricted to the complete overlap. This is the precise sense in which C is an explicit first-face insertion. There are no unspecified higher-face pieces and no inserted row conjugation inside δ.

If one keeps nonidentity ambient bundle restriction maps ρ_01 instead of writing common coordinates, the invariant first-face formula is

    C(F)=ρ_01 ℒ_(t1)(F)−ℒ_(t0)(ρ_01 F)
        =[ρ_01(S_(t1))−S_(t0),ρ_01(F)].                   (3.2)

The last expression uses the admitted algebra-preserving bundle transport. It does not identify differently framed matrices without transport. The fixed-reference proof uses δ′=0; if the initial derivative genuinely has δ′≠0, (A) acquires the separate terms −Hδ′Hδj−HδHδ′j. In corrected-connection notation the combined restriction defect is δ′+C, not C alone.

The row first face is different: the accepted quotient-transition theorem gives

    π_i j_j(R)=g_ij^−1 R g_ij,

so Δ has that first-face transport. Differentiating Δ_n=π_(n+1)δ_n j_n and using (2.4), (2.6) proves

    Δ_n′=Δ_n a_(S,n)−a_(S,n+1)Δ_n
                           +π_(n+1) C_n j_n.              (3.3)

Thus Δ′ need not vanish when ambient δ′=0. In row covariant notation,

    dotΔ_n=Δ_n′+a_(S,n+1)Δ_n−Δ_n a_(S,n)
           =π_(n+1)C_n j_n.

On an individual first face (3.3) reads

    (g_ij^−1 (−) g_ij)′
       = transport_ij a_(S,j)−a_(S,i) transport_ij
                          +π_i ad_(S_j−S_i)j_j.           (3.4)

Equation (3.4) is an operator identity with a fixed row input. It retains the two endpoints of the row transport, including the single-transpose convention from §2. For nontrivial ambient transport, use (3.2) in its final term. No equality A_j=A_i g_ij^t, which is not an admitted source identity, has been assumed.

## 4. Stage-two identity and the selected scalar row

Differentiate the literal word J2=−HδHδj with δ′=0:

    J2′=−H′δHδj−HδH′δj−HδHδj′.

Substitute H′=ℒH−Hℒ and j′=ℒj+j a_S without moving H past δ:

    J2′=−ℒHδHδj+HℒδHδj−HδℒHδj
                     +HδHℒδj−HδHδℒj−HδHδj a_S.

The first and final terms are ℒJ2 and J2a_S. Pairing the remaining four terms gives

    HℒδHδj−HδℒHδj=−H C Hδj,
    HδHℒδj−HδHδℒj=−HδH Cj.

This proves (A), with BOTH minus signs. The derivative is even, and ℒ has internal degree zero, so no extra sign arises from the negative internal degrees of the two H factors.

For input Čech degree n, the fully indexed formula is

    J2_n=−H_(n+2,−1) δ_(n+1) H_(n+1,0) δ_n j_n,

    J2_n′=ℒ_(n+2)J2_n+J2_n a_(S,n)
      −H_(n+2,−1) C_(n+1) H_(n+1,0) δ_n j_n
      −H_(n+2,−1) δ_(n+1) H_(n+1,0) C_n j_n.            (4.1)

The second index on H is its internal INPUT degree. C preserves that degree and raises the Čech degree by one. All four displayed terms have bidegree (+2,−2). Formula (4.1) is valid for nonclosed row inputs; it does not assume ΔZ=0 and does not add a separate Δ′ term to the derivative of a word that contains δ, not Δ.

Apply the actual selector Λ and differentiate it separately to obtain (B). If Z also varies, add (ΛJ2)(Z′). If there are partition weights, test factors, deck projections, or subsequent operators, their own admitted derivative laws must also be applied. None is made constant by (B).

An algebraic trace annihilates some commutators only under a specified trace representation. The map Λ here is the actual degree-minus-two selector, not an assumed trace on an ungraded matrix algebra. There is no premise Λℒ=0. Neither d-closedness nor Λd=0 supplies it.

## 5. Exact comparison with the public a/E transfer formula

To avoid overloading the accepted generator S, call the public auxiliary word σ=HH′. Its original-reference quantities are

    t=Hj′,
    U=σδj−Hδt,
    W=−σδJ1+HδU,
    E_var=−H d′J2+HδH d′J1+HδHδH d′j,
    a=πj′,                 J1=Hδj.

The public theorem states, degree by degree,

    J2_n′=dW_n−δU_n−U_(n+1)Δ_n+J2_n a_n+E_(var,n).     (5.1)

Our a_S is a−b with b=πℒj. Comparing the two independently established expressions for the SAME J2′ gives exactly

    dW−δU−UΔ+E_var
      =ℒJ2−J2 b−H C Hδj−HδH Cj.                         (5.2)

Thus E_var alone is NOT being identified with the two overlap insertions. The boundary, nonclosed-input term, and the b correction participate in the change of decomposition. Equation (5.2), rather than dropping any of those terms, is the precise comparison.

The normalized identities also give a useful explicit check on the public primitive:

    U=HℒHδj−HδHℒj.                                      (5.3)

Indeed substitution of H′=ℒH−Hℒ and j′=ℒj+j a_S into U leaves (5.3); the extra terms have H² or Hj and vanish by (1.1). This does not say that U=0.

For the general-gauge formula in the public boundary proof §5, choose

    Γ_E=−ℒ,          Γ_R=a_S,          Γ_scalar=0.

Then dotd=dotH=dotj=dotπ=0, a_cov=0, and

    dotδ=C,          dotΛ=Λ′+Λℒ.

The covariant U and W are zero, while the covariant differential-variation family is zero. The full restriction family remains exactly

    E_(restr,cov)=−H C Hδj−HδH Cj.

Since dot(ΛJ2)=(ΛJ2)′−(ΛJ2)a_S, the public general-gauge identity becomes (B) verbatim. This independently checks every sign and the row-connection placement.

It also checks the primitive change. The public formula is

    U_cov−U=HΓ_EHδj−HδHΓ_Ej.

With Γ_E=−ℒ, its right side is −U by (5.3), so U_cov=0. A changed primitive being zero in this corrected connection does not establish zero of the original U or of its original selected boundary family.

The public SYNTHESIS uses T_n=ΛJ2_n and M_n=Π_(n+2)T_n, differentiating the partition separately. Our formula can be inserted only as an equality for that same T_n′. It does not erase Π′T, move ℒ across Π or Λ without a proof, change the established full comparison, or separately assign a domain to its new summands. In particular the public conditional boundary-domain result is not a theorem that the right-hand side of (B) has zero pairing.

## 6. Ownership, reference poles, and deliberately limited bound

The accepted generator has carrier/legal bound 5/0 for the original-reference derivative, with one explicit standard-coordinate factor t_r in the differentiated infinity coordinate. In a regular standard frame the actual reference derivative of H is

    K_ref,A=K_regular,A+(V log τ_A)H_A,

and V log τ_A=−u_r/t_r when r is an infinity coordinate. The standard factor is not removed by writing H′=[ℒ,H]. The old-connection bound 5/1 belongs to a DIFFERENT initial derivative and is not substituted here.

Each S_i in (3.1) retains its own full owner occurrence, its carrier charge, and its reference standard allowance. The difference S_j−S_i is a sum of two owned terms, not a new owner whose denominator can be identified with either endpoint. Equal masks or coincident physical divisors do not merge these occurrences. All H owners selected before subsequent face deletion remain attached as well. The construction of a_S retains the physical inclusion/projection factors and their owners; no final numerical bound for that composite is asserted.

There is also a valid functional cancellation in the precise special case identified by the accepted proof §7.5: if two occurrences have the identical carrier contraction as a rational map and use the SAME initial derivative, their explicit constructions give S_i=S_j. The corresponding first-face insertion C then vanishes as a rational operator. This equality does not identify the two clearance occurrences or supply a cancellation for unrelated owners. Equal masks alone or coincidence of a physical divisor alone is insufficient. Even when every applicable first-face difference vanishes, the selector correction and induced row connection in (B) remain unless independently eliminated.

The new conclusion is an exact rational/cochain reorganization plus the inherited factor-level bound on its explicit generators. It does not claim a sharper bound for J2′ by expanding products, a new full-sign character, a regular scalar domain for the separately displayed summands, a valid use of any existing standard bound. Those require their own complete frame, character, ownership, and comparison arguments. No domain claim is made here.

## 7. Tiny formal controls and stopping point

check_formal.py uses only finite dictionaries of invented operator words, degree pairs, tuple deletion, string transposition, and byte hashes. It never imports a source module, forms a source/model polynomial, or evaluates a matrix. It checks the six-term free-word expansion of (A), its selected version (B), degree consistency, first-face cancellation for input degrees zero through four, the row compatibility expansion (3.3), the transpose sign in (2.7), and the normalized primitive formula (5.3).

Active negative controls reject omission of either overlap insertion, either insertion's wrong sign, omission of a_S, omission of either selector derivative/connection term, the opposite first-face sign, freezing the row differential without its connection/overlap terms, the wrong transpose order, and declaring U zero by confusing it with U_cov. Checks are run in normal and optimized Python without relying on assert. These checks detect the listed formal mistakes; the mathematical proofs and the admitted source denotations above establish the theorem.

The resulting contribution is deliberately complementary: the accepted explicit S_i now yields fully specified stage-two overlap and selector corrections in the original prescribed derivative. It does not duplicate or finish the public remainder cancellation problem, prove a total divergence, or obtain a numerical retained value.
