# Full normalizer symmetry forces the pure-T three-dimensional channel

## Result

Under the standing honest normalizer action and target identification, the coefficient alpha of the pure-T map S_(2,1)T → T ⊂ J+ is nonzero. Therefore the quaternion orbit O375 cannot have residual rank five: its residual rank is at least six, by the audited quaternion coupling constraint.

This is a universal representation-tensor proof. It does not evaluate the actual operation, a source-model coefficient, or a selected rank instance. Its coordinates are solely those of the universal Schrödinger and Schur representations.

## 1. Standing inputs and the universal Schur model

Write N=H5⋊K, K=SL2(F5), V=T⊕W, dim(T,W)=(3,2). Its central complement involution R has eigenspaces T and W. Use the Schrödinger basis e_i, i in F5, and operators

    X e_i=e_(i+1), Z e_i=zeta^i e_i, R e_i=e_(-i).

The normalized complement contains D e_i=zeta^(i²)e_i. These are the conventions already checked in canonical-line-parity-exclusion/PROOF.md, Sections 1–2. The actual target J is an irreducible N-module of dimension twenty, with R-eigenspace dimensions (8,12), and J+ = T⊕P5. The canonical operation is a nonzero N-map from the forty-dimensional universal Schur module to J, hence is surjective. Nonzero follows, for example, from repeated-input injectivity.

Use

    U=ker[V⊗Λ²V → Λ³V],
    F(a,b,c)=a⊗(b∧c)+c⊗(b∧a).

This F has outer symmetry and cyclic sum zero, and its values span U. Thus f=q∘F for an N-equivariant surjection q:U→J. Its kernel has dimension twenty.

## 2. A central reflection class sum with an elementary action

There are twenty-five Heisenberg conjugates

    R_ab=X^a Z^b R Z^(-b) X^(-a),  a,b in F5.

The set is invariant under N: the center of H5 does not affect conjugation, K normalizes H5, and R is central in K. Consequently C=Σ_(a,b) R_ab is central in the group algebra action. On V,

    R_ab e_i=zeta^(-2b(i-a)) e_(2a-i).

On V⊗Λ²V, summing first over b gives the exact universal identity

    C(e_i⊗(e_j∧e_k))
      =5 e_(2a-i)⊗(e_(2a-j)∧e_(2a-k)),
      a=(i+j+k)/3 in F5.

Indeed the b-sum is zero unless i+j+k=3a, when it equals five. Let L be the displayed index transformation, so C=5L on this tensor space. The transformed triple has the same index sum as the original, and a second application restores all three indices. Thus L²=1. The operator preserves U, either by naturality of exterior multiplication or because C is a group-algebra operator.

The trace of R on U is zero. One direct computation uses

    tr(R|V)=1,
    tr(R|Λ²V)=(1²−5)/2=−2,
    tr(R|Λ³V)=−2,

where the last identity follows by taking the coefficient of t³ in (1+t)³(1−t)². Therefore tr(R|U)=1·(−2)−(−2)=0. Every conjugate has the same trace, so tr(C|U)=0. Since C²=25I, its +5 and −5 eigenspaces both have dimension twenty.

On irreducible J, the central C is scalar by Schur's lemma. Its trace is twenty-five times tr(R|J)=25(8−12)=−100. Hence C|J=−5I. Equivariance now makes the +5 eigenspace of C on U a subspace of ker(q). Their dimensions are both twenty, so

    ker(q)=U_(C=+5),
    q(t)=0 if and only if L(t)=t.                 (2.1)

This identifies the actual kernel by representation theory alone; it computes no coefficient of q.

## 3. The pure-T copy of T is not in this kernel

Put s1=e1+e4 and s2=e2+e3. Then T has basis e0,s1,s2, with D-eigenvalues 1,zeta,zeta^4. Let Q in Sym²T be the inverse tensor of a nondegenerate K-invariant symmetric metric on T. D-invariance forces

    Q=A e0⊗e0+B(s1⊗s2+s2⊗s1),  A B ≠ 0.

The nonvanishing of both A and B is precisely nondegeneracy in this basis. Existence and nondegeneracy of the invariant metric follow from the irreducible orthogonal A5 representation T, as already proved in canonical-line-parity-exclusion/PROOF.md.

Contracting Q in the outer slots of F gives a K-equivariant map

    i:T→S_(2,1)T⊂U,
    i(v)=Σ_(r,s) Q_rs F(t_r,v,t_s).

At v=e0 its universal tensor is

    t=i(e0)=2B[s1⊗(e0∧s2)+s2⊗(e0∧s1)].          (3.1)

It is nonzero, so i embeds the irreducible T. Since S_(2,1)T=T⊕P5, its image is exactly the pure-T T-summand.

The coefficient of e0⊗(e1∧e2) in t is zero, because every outer factor in (3.1) lies in span(s1,s2). Its coefficient in L(t) is −2B, which is nonzero. To verify this without a matrix calculation, L is an involutive permutation of tensor coordinates up to wedge orientation. Compute the index preimage directly: the target indices (0,1,2) have sum 3 and a=1. Reflection sends them to (2,1,0), hence the preimage is e2⊗(e1∧e0). In t, the coefficient of e2⊗(e0∧e1) is 2B; reversing that wedge gives the asserted −2B. Equivalently, L sends e2⊗(e0∧e1) to −e0⊗(e1∧e2).

Therefore L(t)≠t, and (2.1) gives q(t)≠0. Since q is K-equivariant, the image of i(T) is a nonzero copy of T in J+. The only such summand is the designated T. Hence alpha≠0.

## 4. Quaternion consequence and next step

The audited quaternion-rank-five-coupling-constraint proof establishes that alpha≠0 gives even-block rank at least six at every quaternion axis, and odd-block rank at least four. Thus total middle rank is at least ten there, and residual rank is at least six after the standing subtraction of four. This excludes residual rank five throughout O375.

The immediate next step is independent audit of the central class-sum normalization and the pure-T tensor embedding, then incorporating this exclusion into the existing orbit/rank reduction. No actual source-value computation is required.

## Evidence boundary and dependencies

Read-only local proof review and universal finite-group/tensor algebra only. No actual source-instance evaluation is claimed.

Dependencies: cubic-massey-module-reduction/PROOF.md (the unique eligible cubic channel and J irreducibility); full-hm-image-symmetry/PROOF.md (normalizer target identification, with duality as in the cubic proof); canonical-line-parity-exclusion/PROOF.md (honest K splitting, D normalization, metric, and J+ identification supplied by the standing problem); quaternion-rank-five-coupling-constraint/PROOF.md and AUDIT.md (rank consequence). The standing J parity dimensions are used explicitly rather than inferred merely from total dimension.
