# The exact duality barrier to complementary c-d-f preservation

## Result

Trace/Serre duality and the negative-pencil dual presentations do NOT by themselves turn the one-sided condition Q(X_B)⊂Y_B into complementary preservation Q(X_F)⊂Y_F⊕Y_L. The actual adjoint lives in a different cohomological window. The dual implication is precisely an annihilator inclusion, with reversed arrows.

There is a universal character-faithful family satisfying the exact endpoint characters, kernel A+D, cokernel P, one-sided B preservation, scalar commutant inside the full represented c-d-f negative-pencil algebra, and perfect graded pairings with the transpose action, yet with NONZERO complementary off-diagonal block. This disproves a linear/graded-duality-only implication. It is not an actual HM realization, and does not impose all actual multiplication, Bockstein or bundle relations.

A new geometric identification beyond duality would still be needed to close this route. No actual HM coefficients, parameters or instance ranks are evaluated.

## 1. Authenticated actual interfaces and prior-search boundary

PR924 (c6c25eaf0e5a67c27eee7c3ba4f000df55997692, blob83f5aee293995257459229e6b323522224ce8f3d) supplies the covariant simultaneous pencil and block algebra. PR935 (a7707ba3e25592023eb69cc15686aa4ee1fdcb7c, blob187fe2a8c1499e11afdb5002091aa3c144e1b4a3) supplies scalar Q-commutant under actual occurrence. PR939 supplies the quotient type. PR1001 (a7aa990e7705dd9dbf3d0fd34e437fa735c9e0f1, blobeebebae694f59e786aaebc64c3838d732b2a3832) supplies the exact consequences of one-sided preservation.

The actual two bundle presentations are independently authenticated from ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md at db51525015bb7c5e825833d550d08dedf6f6ea96, blob b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3. Exact originals and hashes are in INPUTS.json.

Prior c-d-f proofs PR924,929,935,939 and the two preserved-B packets were checked for this route. PR924 explicitly warns against an unmarked self-dual replacement of N2 by H¹(Q*). The new contribution here is the exact trace/Serre window, complementary-annihilator criterion and character-faithful scalar-commutant counterfamily below, not a new statement of scalar rigidity.

Write B_ad=End₀(F_HM), distinguishing it from the c-d-f B block. The actual endpoint spaces are

    X=H¹(P⁴,B_ad(2))_+, Y=H¹(P⁴,B_ad(4))_+,
    X_F=V+P+2D, X_B=A+V+2P+2D,
    Y_F=P+D, Y_B=V+2P+2D, Y_L=V+P.

They have dimensions dim X=41, dim Y=37, dim X_B=24, dim Y_B=21.

## 2. Actual trace/Serre adjunction has different degrees

For a rank-two bundle in characteristic zero, tr(UV) is a nondegenerate pairing on its tracefree endomorphisms. This can be checked universally on sl₂: with h=diag(1,-1), e=E12,f=E21 its Gram matrix has entries tr(h²)=2, tr(ef)=tr(fe)=1 and all other entries zero, determinant -2. The construction is conjugation-invariant and globalizes to B_ad≅B_ad*.

Since ω_P⁴=O(-5), Serre duality pairs

    H¹(B_ad(d)) × H³(B_ad(-d-5)) → C.

All linearizations are retained; G has no nontrivial character. On the indicated parity eigenspaces the pairing is perfect with the matching dual eigenspaces. Therefore the transpose of multiplication by q0 is exactly

    Q∨:H³(B_ad(-9))_+ → H³(B_ad(-7))_+,

and

    <Qx,z> = <x,q0 z>.

The arrow has dimensions37→41. It is NOT another arrow X→Y, and trace duality does not identify these two H³ spaces with X and Y in their original order. The dimensions already prohibit an identification Y*≅X or X*≅Y. A direct trace cup of x∈H¹(B_ad(2)) and y∈H¹(B_ad(4)) lands in H²(O(6))=0, so it supplies no perfect endpoint pairing.

Self-duality of every irreducible G-module gives abstract identifications X≅X*, Y≅Y*, not X≅Y*. It neither marks their repeated multiplicity spaces nor reverses the unequal cohomological/twist degrees. A transpose must not be silently renamed Q.

## 3. The negative-pencil duality also changes the marked objects

The actual P¹ presentations are

    0→E→M3 O(-1)→M4 O→0,
    0→Q_bundle*→M3* O(-1)→M2* O→0.

The covariant reconstruction gives X=H⁰(Q_bundle(-2)), Y=H¹(E). Serre duality on P¹ gives instead

    X*=H¹(Q_bundle*), Y*=H⁰(E*(-2)).

Dualizing 0→E→H O→Q_bundle→0 exchanges the source E with Q_bundle*. Their ranks are17 and13, respectively, so they cannot be the same embedded subbundle. On the B constant block, E_B=Sym⁶W O(-4) has rank7, while Q_bundle,B=Sym³W O(7) has rank4. The corresponding endpoint dimensions24 and21 are exchanged under duality, not identified. None of these constructions turns the chosen constant splitting into an orthogonal splitting for a pairing with Q self-adjoint.

A further sharp dimensional obstruction appears under actual one-sided preservation: PR1001 forces ker Q=A+D⊂X_B and Y_B⊂im Q. Thus Q(X_B) has dimension16 although Y_B has dimension21. Even after discarding total kernel and cokernel to obtain the isomorphism X/ker Q→im Q, the marked B source has dimension16 and marked B target dimension21. A perfect blockwise cross-pairing aligning these two marks is impossible; the missing five-dimensional D is exactly the connecting interface from PR1001.

## 4. What one-sided preservation actually says on the transpose

For any map Q:X→Y and subspaces U⊂X,Z⊂Y, perfect dual pairings give the equivalence

    Q(U)⊂Z  iff  Q∨(Z⊥)⊂U⊥.

Indeed <Qx,z>=<x,Q∨z> for x∈U,z∈Z⊥. This is the exact consequence, with no need to choose complements.

In our marked splitting, U=X_B, Z=Y_B. Thus the automatic statement is

    Q∨((Y_F⊕Y_L)*)⊂X_F*.

By contrast the desired complementary preservation is equivalent to the ADDITIONAL condition

    Q∨(Y_B*)⊂X_B*.

These are different domain subspaces of Y*, not the same condition written twice. To conclude the latter from the former requires a further adjoint identification or block-pairing theorem that transports the two marks in exactly the needed way. Neither ambient trace duality nor the P¹ dual presentations supply it.

## 5. A universal counterfamily with the full endpoint characters

Work over R=C[t,t⁻¹,u,u⁻¹]. These are free synthetic formal units, not actual source coefficients. Every entry below means that scalar times the identity of an indicated irreducible. Retain all source and target blocks named in Section1. Define Q on each isotypic multiplicity space as follows.

A: the unique A in X_B maps to zero.

V: source order (X_F,V; X_B,V), target order (Y_B,V; Y_L,V):

    Q_V = [[0,1],[1,0]].

P: source order (X_F,P; X_B,P1; X_B,P2), target order (Y_F,P; Y_B,P1; Y_B,P2; Y_L,P):

    Q_P = [[1,0,0],[0,1,0],[0,0,1],[u,0,0]].

D: source order (X_F,D1; X_F,D2; X_B,D1; X_B,D2), target order (Y_F,D; Y_B,D1; Y_B,D2):

    Q_D = [[0,1,0,0],[0,0,1,0],[t,0,0,0]].

This is a G-equivariant family by construction. It preserves X_B→Y_B. Its complementary off-diagonal block contains t·id_D:X_F,D1→Y_B,D2 and is nonzero over R. Elementary identities, without specializing t,u, show:

    ker Q=A+(X_B,D2),
    im Q=2V+3P+3D, coker Q=P,
    ker Q_B=A+D, im Q_B=V+2P+D, coker Q_B=D,
    Y_B⊂im Q.

For example the P cokernel is represented by the functional (-u,0,0,1) on its four target copies, and the D part is onto with right-inverse entries involving only t⁻¹. This verifies the actual necessary characters without claiming an actual HM map.

The full represented c-d-f algebra has scalars (a,b,d) on F,B,L and radical w:Y_L,P→Y_F,P, with source scalars a,b. In this counterfamily the V commutator requires d=a, the D off-diagonal entry requires t(b-a)=0, and the P commutator requires uw=0. Since t,u are units, a=b=d,w=0. Conversely these common scalars commute. Thus its Q-compatible subalgebra is precisely R·1 over R, and K·1 over the fraction field K=C(t,u). The model is not evading the previously proved scalar-commutant condition.

Now adjoin formal dual groups X*=H³_-7 and Y*=H³_-9 with their evaluation pairings, and equip them with Q∨=Qᵗ. For arbitrary formal x,z the identity <Qx,z>=<x,Qᵗz> holds entrywise. Give opposite-order pairings the degree1/degree3 graded sign if desired. The perfect graded duality, actual twist bookkeeping and adjunction all coexist with the nonzero complementary block. For any further maps one can adjoin their duals in the same fashion; this observation asserts no additional actual multiplication relations.

The counterfamily intentionally does NOT identify itself with the fixed actual negative multiplication tensors, enforce the known original Bocksteins, or realize the c-d-f bundle. It proves only that the stated trace/Serre adjunction plus characters, one-sided preservation and scalar commutant are insufficient for complementary preservation. Additional actual geometry could still rule out the one-sided branch.

## Verification boundary

verify.py authenticates the input bytes, checks the actual dual degrees and rank mismatches, verifies the universal trace Gram matrix, checks every counterfamily kernel/cokernel relation and the scalar-commutant equations over the formal ring, and verifies transpose annihilator inclusion while explicitly retaining the opposite nonzero block. No actual matrix is evaluated and no parameter is selected. This supplies a reproducible negative result for the proposed shortcut, not a source exclusion or complete repair.
