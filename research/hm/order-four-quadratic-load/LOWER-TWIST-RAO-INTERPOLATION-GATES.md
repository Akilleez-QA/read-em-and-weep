# Exact lower-twist Rao interpolation gates

Let Q be smooth and transverse to C, V=F|Q, Z=C∩Q, B=End_0(F), U=H0F(3), D=det U, and M_d=H1I_C(d). Keep M distinct from the primary module A_j=H1F(j).

For k=2 or3, restrict the actual exterior-symmetric resolution to Q and twist by k-5:

0→D O_Q(k-10)→Λ²U O_Q(k-5)→U V(k-2)→B_Q(k)→T_k→0,
T_k=ell²(k-5)|Z.

Let R1,R0 be the successive images. Quadric ACM vanishing gives H0R1=H1R1=0 and H2R1=D H3O_Q(k-10). The primary restriction sequences give H0V(k-2)=0, H2V(k-2)=H3V(k-2)=0. Thus H0R0=H2R0=0 and

0→U H1V(k-2)→H1R0→D H3O_Q(k-10)→0.

The fifty-point boundary b_k:H0T_k→H1R0 has kernel H0B_Q(k). Its projection p_k to the last term is dual to

D^-1 H0O_Q(7-k)→D^-1 H0O_Z(7-k).

The global dualizing calculation is the same as for k4: ω_Z=D^-1 O_Z(2)ell², hence T_k*ω_Z=D^-1 O_Z(7-k). No independent point weights are chosen. Local Koszul duality identifies the map with ordinary restriction.

Consequently there is an injection

H0B_Q(k) → D⊗H1I_{Z,Q}(7-k)*.

More exactly, its image is the kernel of the remaining boundary from that dual interpolation cokernel to U H1V(k-2). This is an actual-map criterion, not a dimension-only model.

Since I_C(3)=I_C(2)=0, restriction to Q gives

H1I_{Z,Q}(5)=coker[q:M3→M5],
H1I_{Z,Q}(4)=coker[q:M2→M4],

provided H2I_C(3)=H2I_C(2)=0. These vanish because C is a disjoint union of lines and H1O_C(d)=0 for d≥-1. Therefore

q:M3→M5 onto ⇒ H0B_Q(2)=0,
q:M2→M4 onto ⇒ H0B_Q(3)=0.

Converses are not claimed: a nonzero interpolation cokernel can still be killed by the remaining primary boundary.

For clarity, the primary boundary targets have dimensions28 for k2 and40 for k3. Indeed 0→A0 (dimension5)→H1V→H2F(-2) (dimension2)→0, and H1V(1)=A1 (dimension10). The raw targets of p_k have dimensions h0O_Q5=91 and h0O_Q4=55, respectively, whereas H0T_k always has dimension50.

These exact gates require surjectivity in the downward Rao range. The already proved injectivity of generic square multiplication M1→M3 does not imply either. Neither does scheme generation of I_C(5), which is a sheaf-generation statement rather than surjectivity of these finite-dimensional cohomology multiplications.

This note uses the actual resolution from PR538 and primary support, not selected matrices, coefficients, rank samples, or a presumed split extension. No lower-twist exclusion beyond the preceding nef proof for k1 is asserted.
