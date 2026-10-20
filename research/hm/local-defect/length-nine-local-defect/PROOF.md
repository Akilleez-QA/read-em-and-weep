Publication context: this retained proof or audit may describe an intermediate bound or then-open branch. Read the unit overview for the current scope and later implications. Historical mathematical review is not a new formal verification.

# Exclusion of a canonical local defect of length nine

## Theorem and scope

Let R be a regular local complex ring of dimension four, with residue field C and a finite group action containing G=C5⋊C4. Suppose its cotangent representation W is the irreducible four-dimensional representation V, with all four nonzero clock weights, transitively permuted by C4. Every G-equivariant finite R-module Q of length nine satisfies

    β3(Q) − 2β4(Q) ≥ 3.                                      (A)

Consequently Q cannot equal Ext²_R(M,R) for an equivariant reflexive rank-two module M, free away from the closed point, with equivariantly trivial determinant. The already audited isolated self-duality/generator argument requires

    β3(Q) − 2β4(Q) ≤ 2.                                      (B)

Only abstract representations and universal local algebra are used. No actual physical source/model matrix, operation, selected input, rank instance, jet, or residue is evaluated.

## 1. Setup and exhaustive radical shapes

Complete faithfully flatly, which preserves lengths and Betti numbers. Averaging a linear section gives equivariant parameters x_i, indexed by i∈F5×, of clock weight i. The irreducibles of G are four one-dimensional clock-trivial characters and V. Thus a length-nine module has representation type: nine character dimensions; V plus five character dimensions; or 2V plus one character.

Every nonzero radical layer L_j=m^jQ/m^(j+1)Q is a semisimple G-representation. Multiplication W⊗L_j→L_(j+1) is surjective. In particular two consecutive character-only layers are impossible. If Q has only character constituents, the parameters kill Q outright.

With a single V, there are at most three nonzero layers. In the three-layer case the unique V must be in the middle, and there are exactly the shapes

    (a,4,b), a+b=5, a,b>0,                                  (1)

where the end layers are clock-trivial. Indeed, the middle cannot contain characters, because W times the character-only top has no character quotient. All other such modules are square-zero.

With two copies of V and one character, there are at most three nonzero layers: there are only three irreducible constituents in total, counted with multiplicity. The three-layer possibilities are exactly

    (1,4,4), (4,1,4), (4,4,1).                             (2)

This is a fresh radical-layer enumeration at length nine, without importing a length-eight classification.

## 2. All square-zero modules

Suppose m²Q=0, including the semisimple case. Choose an invariant vector-space decomposition Q=T⊕S, S=mQ. Let r_i be the rank of the Koszul differential T⊗Λ^iW→S⊗Λ^(i−1)W. The differential vanishes on S. Therefore

    β3=36−r3−r4, β4=9−r4,
    β3−2β4=18−r3+r4.                                       (3)

The common parameter kernel K⊂T is precisely ker δ4 up to its one-dimensional wedge factor. Thus r4=dim(T/K), and δ3 factors through (T/K)⊗Λ³W, giving r3≤4r4.

If dim T≤5, then r3−r4≤3r4≤15 and (A) follows.

Suppose dim T>5 and S≠0. In the one-V representation case, S must consist of characters, since otherwise T would have dimension at most five. The character constituents of T are killed by every parameter. Its V constituent maps nontrivially, and its common parameter kernel is zero by irreducibility. Hence the active quotient T/K is V and r4=4.

In the two-V case, dim T>5 forces T=2V and S a single character (other placements cannot leave a nonzero S). The common kernel of the action is the kernel of the nonzero equivariant map

    T → Hom_C(W,S) ≅ V.

This map is surjective by irreducibility of its target, so again T/K≅V and r4=4.

In either case the active quotient is a V mapping into clock-trivial S. For a weight vector v_i of this quotient, only x_(−i) acts nontrivially. The four independent tensors

    v_i ⊗ wedge of the three x_j with j≠−i

lie in the kernel of its degree-three Koszul map. Therefore r3≤12. Equation (3) gives β3−2β4≥10. Finally, if S=0, (3) gives 18. This proves (A) for every square-zero case.

## 3. Single-V three-layer modules

For (1), invariant complements give Q=T⊕V⊕S with dim T=a, dim S=b, mQ=V⊕S and m²Q=S. Clock weights rule out all higher correction terms and give exactly

    x_i t=a_i(t)v_i,  x_(−i)v_i=b_i∈S,
    x_jv_i=0 for j≠−i,  WS=0.                             (4)

All a_i and b_i are nonzero. The a_i are nonzero because WT generates the middle V; the common kernel of W on the middle V is G-invariant and proper, so is zero, which proves b_i≠0. The b_i span S.

Commutativity gives nonzero rank-one tensor identities

    a_i⊗b_i=a_(−i)⊗b_(−i).                                (5)

The factors belonging to an opposite pair are proportional. There are two opposite pairs, so

    b≤2, r:=dim span{a_i}≤2.

The common kernel K of the a_i is G-invariant and killed by every parameter. An invariant complement T' gives an actual equivariant R-module splitting

    Q=K⊕N, dim K=a−r, N=T'⊕V⊕S.                           (6)

The socle of N is exactly S: its T' components are separated by the a_i, and the middle V has no common parameter kernel. Each residue-field summand contributes 2 to β3−2β4.

If b=1, then a=4. Finite-length duality D=Ext⁴_R(−,R) makes D(N) cyclic of length 5+r, annihilated by m³ with m² action nonzero. The dual has a single V and clock-trivial other constituents, up to a one-dimensional twist. Cyclicity and the preceding layer argument force Hilbert function (1,4,r). Thus D(N)=R/I with I⊂m² and at least 10−r minimal quadratic relations. Betti reversal gives β3(N)≥10−r, β4(N)=1, and

    β3(Q)−2β4(Q) ≥ 10−r−2+2(4−r)=16−3r≥10.

If b=2, then a=3. If r=1, N is cyclic of Hilbert function (1,4,2) and socle dimension two. It is a graded quotient: m³⊂I⊂m² makes I determined by its quadratic relation subspace together with all cubics. Its Hilbert numerator is

    (1+4t+2t²)(1−t)^4=1−8t²+12t³−3t⁴−4t⁵+2t⁶.

There are no minimal ideal generators in degrees four or five, so those coefficients force β_(3,4)≥3 and β_(3,5)≥4. Hence β3(N)−2β4(N)≥7−4=3. Equation (6) contributes two residue-field summands, giving a bound of seven for Q.

If b=2 and r=2, representatives of the forms for the two opposite pairs are independent, as are the corresponding bottom vectors. Choose a dual top basis and the corresponding bottom basis. Equation (4) then splits N, as an underlying R-module, into the two cyclic length-four modules

    R/(x_2,x_3,x_1²,x_4²) and R/(x_1,x_4,x_2²,x_3²).

For clarity, each top basis vector is killed by the unused parameters, its two used parameter squares are zero, and their mixed product is nonzero by (5). This gives a surjection from the displayed quotient onto its four-dimensional summand; equality of lengths makes it an isomorphism. Each ideal is a regular sequence, so each summand has Betti sequence (1,4,6,4,1), contributing two to β3−2β4. The one residue-field summand in (6) contributes two more, giving six. All single-V three-layer cases satisfy (A).

## 4. The new two-V shapes

### 4.1 Shape (4,1,4) is impossible

Work in the associated graded module. Let its successive layers be U≅V, L a character, and S≅V. The surjection W⊗U→L is a nonzero equivariant pairing. Its adjoint U→W*⊗L is an isomorphism, so choose a weight vector u_(−j) such that x_j u_(−j) is a nonzero element of L. The map W⊗L→S is an isomorphism, so every x_i acts nontrivially on this element of L. Choose i≠j. Weight considerations give x_i u_(−j)=0 in L. Therefore

    x_i(x_j u_(−j))≠0, but x_j(x_i u_(−j))=0,

contradicting commutativity in the associated graded module. Higher-order corrections in Q cannot repair a failure of this induced multiplication.

### 4.2 Shape (1,4,4)

This module is cyclic. Write Q=R/I. Its Hilbert function is (1,4,4), hence m³⊂I⊂m² and it is a graded quotient by quadratic relations and all cubics. The common parameter kernel on its middle V is zero, because it is an invariant proper subspace and the middle generates the nonzero bottom. No element with nonzero degree-zero component is in the socle. Its socle is therefore precisely its four-dimensional degree-two layer, so β4(Q)=4.

The Hilbert numerator is

    (1+4t+4t²)(1−t)^4
      =1−6t²+4t³+9t⁴−12t⁵+4t⁶.

For a minimal graded free resolution this equals Σ_(i,j)(−1)^i β_(i,j)t^j. There are no degree-five minimal ideal generators since m³⊂I. Its degree-five coefficient therefore yields

    −12=β_(2,5)−β_(3,5)+β_(4,5),

and in particular β3(Q)≥12. Thus β3−2β4≥12−8=4.

### 4.3 Shape (4,4,1)

Its socle is exactly its bottom character. To see this without a gradedness assumption, multiplication from the top V to the middle V has common kernel a G-invariant proper subspace, hence zero. A socle vector cannot have a nonzero top component. The same argument applies to the middle V mapping to the bottom character. Thus β4(Q)=1.

The finite dual D(Q) is cyclic of length nine, and has representation type 2V plus one character, up to the one-dimensional duality twist. Its top is a character. It cannot have square-zero radical of dimension eight: the radical of a cyclic square-zero module is generated by the four parameters and has dimension at most four. The exhaustive shapes in Section 1 therefore force its Hilbert function to be (1,4,4).

Consequently D(Q)=R/I has at least 10−4=6 minimal quadratic relations. Betti reversal gives β3(Q)=β1(D(Q))≥6, and hence β3−2β4≥6−2=4. This proves (A) in the last case.

## 5. Consequence and exact boundary

Sections 1–4 prove (A) for every equivariant length-nine finite module. The defect inequality (B), imported from length-five-local-defect/PROOF.md Section 1, excludes length nine for the isolated self-dual rank-two reflexive defect.

Combined with the previously audited local exclusions through eight, the canonical thirty-point orbit contributes at least 30·10=300 to a nonzero defect. The separately audited unique 250-point orbit contributes at least 500, and all other support orbits have at least 300 points. Hence, in the stipulated actual-rank-eight branch,

    length(T)=length(D) ≥300, equivalently q≥60 if length(T)=5q.

In particular the formerly sole possible positive total below 300, namely 270, is excluded. This proves no realization at 300, no upper bound, and no exclusion of the actual-rank-eight branch itself.

## Dependencies

The imported universal defect inequality and finite-duality facts are in length-five-local-defect/PROOF.md. The representation setup and local linearization are independently recalled above, consistent with length-two-local-defect/PROOF.md. The earlier exclusions and global orbit/local-one facts are summarized in rank-eight-defect-270/COROLLARY.md. The length-eight proof was consulted for context, but the radical enumeration and all two-V three-layer arguments here are new and explicit. No upstream/source application was modified; no installation or large computation was performed.
