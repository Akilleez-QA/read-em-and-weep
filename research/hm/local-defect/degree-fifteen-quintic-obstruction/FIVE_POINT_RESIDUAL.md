> Publication scope: preserved mathematical proof/audit. Historical statements that rank eight remains open are superseded only after the final assembly and all its prerequisites. No source-instance evaluation or formal verification is claimed here.

# The surviving degree-fifteen quotient has a length-five intrinsic bad locus

This addendum builds on PROOF.md Sections 1--3. Its geometric claims do not require any further symmetry assumption.

Let M=R be the still-possible degree-fifteen side. Let T be the maximal zero-dimensional subsheaf of O_Z. Since it is an ideal, O_Y=O_Z/T defines a closed subscheme Y of Z. The quotient has no zero-dimensional subsheaf: otherwise its inverse image would contradict maximality. A general hyperplane avoids supp(T), so its section on Y is still C=CI(3,5). The lifting proof applies to Y, hence Y has a cubic equation f; a quintic q coprime to f is supplied by I_Z(5) or by lifting the complete-intersection generator. Degree equality inside CI(f,q) gives Y=CI(3,5). We have

    0 -> I_Z -> I_Y -> T -> 0,
    h0(I_Y(3))=1, h0(I_Y(4))=5, h0(I_Y(5))=16,
    h0(I_Z(3))=h0(I_Z(4))=0, h0(I_Z(5))=11.

Let W be defined by the saturated colon ideal sheaf I_Z:f. This is a finite scheme because I_Z=I_Y away from supp(T), and I_Y:f is the unit ideal. Multiplication by f gives an injection O_W(-3)->T. The Hilbert function H_W of W satisfies H_W(1)=5: its kernel on linear forms is I_Z(4), which is zero. The image of f*S_2 in H0(T(5)) has dimension H_W(2), at most five, since the entire image of H0(I_Y(5)) has dimension 16-11=5. Multiplication by a linear form avoiding W is injective on its saturated coordinate ring, so H_W(2)>=H_W(1)=5. Thus H_W(2)=5. The finite-scheme Hilbert function strictly grows until it reaches the scheme's length. Therefore length(W)=5, and W spans P4.

Moreover the image of f*S_2 in H0(T(5)) is the entire five-dimensional image of H0(I_Y(5)). Subtracting a quadratic multiple of f from a quintic generator q of I_Y therefore gives a quintic q' in I_Z. It remains coprime to f. Since I_Y=(f,q'), every local section of I_Z can be written f*a+q'*b, and then a belongs to I_Z:f=I_W. Thus

    I_Z=(f I_W,q').

Also q' belongs to I_W. Since f and q' are coprime, (f) intersect (q')=(fq'). The preceding presentation gives

    T=I_Y/I_Z = O_W(-3).

In particular length(T)=5, including arbitrary embedded or nonreduced structure.

Finally supp(T) is intrinsic to R, independent of the chosen general nine sections. At every closed point p of Z, the source O_p^9 is free of depth four. The long exact local-cohomology sequence for 0->O_p^9->R_p->(I_Z)_p->0 identifies H^1_m(R_p) with H^1_m((I_Z)_p). The structure sequence identifies the latter with H^0_m((O_Z)_p). Since R is torsion-free, H^0_m(R_p)=0; therefore this is nonzero exactly when depth(R_p)=1. Away from Z, the section sequence has free quotient O(5), so R is free there. Consequently

    supp(T) = { closed points p : depth(R_p)=1 }.

It follows that this is a nonempty invariant finite point set with at most five geometric points under every symmetry preserving R.

## Full group-theoretic exclusion of rank six

The standing full-symmetry hypothesis is verified in ../../full-hm-image-symmetry/PROOF.md, Section 1: N=H5 semidirect SL2(F5), with Hbar=H5/Z(H5)=F5² and its natural SL2(F5) conjugation action. R is N-equivariant, so its intrinsic depth-one point set S is N-invariant. We have proved 1<=|S|<=5.

The permutation action Hbar->Sym(S) has a kernel invariant under SL2(F5), hence either zero or all of F5². (The natural two-dimensional module has no invariant one-dimensional subspace: SL2 acts transitively on its nonzero vectors.) A trivial kernel would embed a group of order25 into Sym(S), whose order divides 5!=120, impossible by Lagrange's theorem. Thus Hbar fixes every point of S. But the standard H5 action on P4 has no common fixed point: if standard generators sigma,tau preserved a common vector line, their scalar restrictions there would commute, whereas their commutator is the central primitive fifth root zeta times the identity. This contradiction shows S cannot exist.

Therefore the remaining pair (10,15) is impossible. Together with PROOF.md excluding (15,10) and the previous quintic bounds excluding (5,20),(20,5), this excludes the established rank-six branch entirely.

The proof uses only the already established abstract group and sheaf equivariance. It evaluates no operation, matrix, chosen input, rank instance, polynomial instance, jet, or residue. All new writes are the local proof deliverables.
