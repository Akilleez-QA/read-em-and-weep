# Conditional endomorphism descent and its central extension

## Result and scope

Assuming the specified locally free twisted left module exists, its local endomorphism algebras glue to an honest global algebra B_h. In the specified row convention, its local algebra is Mat_r(A_i)^op, and B_h/h B_h is End_O(E), with ordinary composition. Equivalently C_h := B_h^op is locally Mat_r(A_i), and its reduction is End_O(E)^op. Noncentral triple units cancel exactly.

This proves the proposed necessary-condition step 1. It does not construct the assumed module, establish formal matrix-Weyl normal form, prove a Harish–Chandra torsor is transitive, identify a period, or establish any characteristic-class vanishing. Everything below is universal algebra; no model, coordinate, jet, physical-matrix, repository, or obstruction-value computation is involved.

Inputs: [RESULT.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/d1422e5f9137ae64ec207c496a0391712ce93263/research/hm/null-module-boundary-audits/quantization-criteria/RESULT.md), especially its addendum, and [RESULT.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/d1422e5f9137ae64ec207c496a0391712ce93263/research/hm/null-module-boundary-audits/module-lifting/RESULT.md) for the row convention.

## 1. Hypotheses

Let A_i be sheaves of unital associative k[[h]]-algebras on U_i, flat, h-adically complete and separated, with A_i/h A_i = O_(U_i). Assume k has characteristic zero. On overlaps let F_ij: A_j -> A_i be k[[h]]-algebra isomorphisms, reducing to identity. On triple overlaps assume units A_ijk in A_i satisfy

    F_ij F_jk = Ad(A_ijk) F_ik.

The usual unit, inverse, and pentagon coherence is assumed for the given algebroid. Only the displayed triple equation is needed for the triple calculation below.

Assume, conditionally, free local LEFT modules M_i = A_i^(1 x r), with left scalar action entrywise, and invertible semilinear maps

    phi_ij(v) = F_ij(v) star G_ij,
    F_ij(G_jk) star G_ij = (A_ijk I_r) star G_ik.

Here F acts entrywise and all products are the associative matrix/row products induced by the indicated local algebra. A scalar in a matrix product means a scalar diagonal matrix; it is not assumed central. Reduction gives row transitions g_jk g_ij = g_ik and the classical vector bundle E. Rank may vary between connected components but is positive on each component under discussion.

These hypotheses are an implication's antecedent, not an existence claim. Statements about completeness/flatness below can instead be made at each finite h-adic order and then passed to the inverse limit when the module is formal.

## 2. Endomorphisms and their multiplication

Every left A_i-linear endomorphism of M_i has the unique form

    R_H(v) = v star H,    H in Mat_r(A_i).

For ordinary function composition,

    R_H o R_K = R_(K star H).

Thus H -> R_H is an anti-isomorphism from the ordinary matrix algebra, or an isomorphism Mat_r(A_i)^op -> End_(A_i)(M_i). This opposite cannot be dropped even when the coefficient algebra has commutative special fiber: ordinary matrices need not commute.

Transport an endomorphism from frame j to frame i by conjugating the semilinear module map:

    beta_ij(T) = phi_ij o T o phi_ij^(-1).

This is an algebra isomorphism for composition. Its exact row-matrix expression is

    T_ij(H) = G_ij^(-1) star F_ij(H) star G_ij,
    beta_ij(R_H) = R_(T_ij(H)).

Indeed phi_ij R_H(v) = F_ij(v) star F_ij(H) star G_ij, whereas R_(T_ij(H)) phi_ij(v) = F_ij(v) star G_ij star T_ij(H). The displayed T is also an isomorphism for ordinary matrix multiplication, so the same overlaps glue either the endomorphism algebra or its opposite.

## 3. Exact triple cancellation, with noncentral A

Write A=A_ijk I_r and Q=F_ij(G_jk) star G_ij. Then Q=A star G_ik and

    T_ij T_jk(H)
      = Q^(-1) star (F_ij F_jk)(H) star Q
      = (A star G_ik)^(-1)
          star A star F_ik(H) star A^(-1)
          star (A star G_ik)
      = G_ik^(-1) star F_ik(H) star G_ik
      = T_ik(H).

Only adjacency, associativity, and inverses are used. Moving A through H or G would be invalid and is unnecessary.

Equivalently, phi_ij phi_jk = L_(A_ijk) phi_ik. An A_i-linear endomorphism commutes with L_(A_ijk), even though L_(A_ijk) itself need not be A_i-linear. Hence conjugating by the twisted triple composite acts exactly as conjugating by phi_ik. This is why the obstruction to gluing the module as an ordinary sheaf does not obstruct gluing its algebra of endomorphisms.

Define B_h by ordinary sheaf descent of End_(A_i)(M_i) along beta_ij. Explicitly its sections are local endomorphisms with beta_ij(T_j)=T_i on overlaps. Multiplication is local composition. The cocycle just proved makes this an honest sheaf of associative unital algebras, not merely an algebroid. Its opposite C_h is glued from Mat_r(A_i) with ordinary matrix multiplication along T_ij. Flatness, completeness and separatedness follow locally from those of A_i.

## 4. Classical reduction

Modulo h, the overlap is

    H -> g_ij^(-1) H g_ij.

This is precisely the row-frame transformation of an endomorphism of E. Together with the reversed row-matrix multiplication for composition, it gives canonically

    B_h / h B_h = End_O(E),
    C_h / h C_h = End_O(E)^op.

The second algebra is also canonically End_O(E^vee), but changing to that description must track dualization and must not silently replace E by E^vee in a characteristic-class formula. These are local sheaf quotient identifications; they do not assert surjectivity of reduction on global sections.

## 5. Center: exactly what algebraic descent proves

For any unital algebra A and positive finite r,

    Z(Mat_r(A)) = Z(A) I_r.

The same center is obtained for the opposite algebra. Since a central scalar diagonal matrix commutes with G_ij,

    T_ij(z I_r) = F_ij(z) I_r,    z in Z(A_j).

On centers the original inner triple twist acts trivially, so the F_ij restrict to honest center descent. Therefore Z(B_h)=Z(C_h) is exactly the sheaf obtained by gluing the local Z(A_i). The module matrices G do not enter its overlap formula.

There is always a canonical central copy of k[[h]] I. It is NOT generally correct to assert Z(B_h)=O_X[[h]], nor does taking centers commute with reduction: Z(B_h/h B_h)=O_X, whereas the quantum center can be much smaller.

With the additional usual symplectic hypotheses one obtains the customary center: if the first commutator of A_i is a nondegenerate Poisson bracket and local functions with zero differential are locally constant, then Z(A_i) is the locally constant sheaf k[[h]] (over the applicable field of constants). Proof: the leading coefficient of a central element is Poisson central, hence locally constant; subtract that scalar lift, divide by h, and repeat. Torsion-freeness and completeness justify induction and its limit. This extra conclusion uses the Poisson/local-constants hypotheses, not just twisted descent. Degenerate Poisson structures, different constants, or truncated algebras require separate treatment.

## 6. Canonical inner central extension and scalar normalization

For any algebra sheaf C, there is the universal exact Lie-algebra sequence

    0 -> Z(C) -> C_Lie --ad--> InnDer(C) -> 0,
    ad(x)(y) = xy-yx,

where InnDer is defined as the image sheaf; this does NOT assert all derivations are inner. It applies globally to C_h and, separately, B_h. This alone provides no de Rham period comparison.

There is also a useful h-rescaled extension, canonical in this setting. Work first in C_h. Inside C_h[h^(-1)] set

    L_C = { h^(-1) x : x in C_h and x mod h is central in C_h/h C_h }.

Locally,

    L_C = h^(-1) A_i I_r + Mat_r(A_i).

The sum is not a direct sum. This equality follows because the center of the reduced matrix algebra is O I_r. Since [A_i,A_i] is contained in h A_i, direct calculation gives

    [h^(-1)a I, h^(-1)b I] = h^(-2)[a,b] I in h^(-1) A_i I,
    [h^(-1)a I, H] = h^(-1)[a I,H] in Mat_r(A_i).

Thus L_C is a Lie subalgebra under the unrescaled commutator in C_h[h^(-1)], and its adjoint action preserves C_h. The overlaps preserve L_C intrinsically; explicitly,

    h^(-1)G^(-1) F(a I) G
      = h^(-1)F(a) I + h^(-1)G^(-1)[F(a) I,G],

and the second term is integral. Consequently there is a globally defined exact central extension

    0 -> h^(-1) Z(C_h) -> L_C --ad--> D_C -> 0,

where D_C is, by definition, the image sheaf in Der_(k[[h]])(C_h). The kernel formula follows because h x commutes with C_h whenever x does, and torsion-freeness permits division by h. Under the additional symplectic-center hypotheses of Section 5, the kernel is h^(-1) k[[h]] locally constantly.

One must NOT replace L_C by all h^(-1)Mat_r(A_i): for r>1, matrix commutators need not be divisible by h, so that larger lattice does not in general act by derivations preserving C_h. Nor does this argument prove D_C=Der(C_h). Such a surjectivity statement requires further local structure and possible topological/continuity hypotheses.

For B_h the intrinsic construction is identical, but when represented by the same row matrices its Lie bracket is the NEGATIVE matrix commutator. Accordingly its adjoint action is represented by -ad_C. The identity underlying linear space carries a Lie anti-isomorphism between the two versions; multiplication by -1 gives a Lie isomorphism L_B -> L_C and sends a central scalar z I to -z I. Therefore choosing an opposite convention can reverse the identification of the central kernel. A period-sign convention cannot be declared independent of this choice.

The scalar normalization actually fixed by this construction is the unit embedding

    a -> a I_r,   and   h^(-1)a -> h^(-1)a I_r.

There is no factor of r in that embedding. On the classical matrix algebra, normalized trace (1/r) tr sends a I_r to a and supplies the scalar projection; unnormalized trace sends it to r a. This explains exactly where rank factors can enter a separately defined trace convention. Over noncommutative A_i, ordinary matrix trace is not generally a map to the center and is not generally cyclic as an A_i-valued map. It cannot by itself supply a global splitting of the quantum central extension or a quantum scalar projection. Trace modulo coefficient commutators is a different, weaker statement.

## 7. What is still needed for the proposed characteristic-class route

The honest global endomorphism algebra and the above intrinsic central extension exist conditionally and with exact signs. To invoke a matrix-Weyl characteristic-class theorem one must still establish its required local normal form and derivation/torsor hypotheses, match the theorem's central-kernel convention to B_h versus C_h, and identify the resulting global characteristic class from the original (mu,F,A) and the assumed module. None of these follows merely from cancellation of triple units.

In particular this calculation does not identify the algebroid's gerbe coefficient with a period, does not determine an exp(-c) versus exp(c) convention, and does not prove characteristic-class detection of any trace-free module obstruction. The original module-existence question remains open; the present result is a legitimate conditional step in a necessary-condition argument.
