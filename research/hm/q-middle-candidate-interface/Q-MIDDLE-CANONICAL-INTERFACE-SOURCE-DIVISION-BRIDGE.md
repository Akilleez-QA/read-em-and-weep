# Canonical q-middle interface: source and divided-arrow bridge

This is an additive verification supplement to the frozen
`Q-DIVISIBLE-CUBIC-MIDDLES-HAVE-EXACT-C-REPRESENTATIVES.md` and its
35-file manifest. It changes no frozen construction.

For every symmetric positive-linear physical twelve-by-twelve B, the
canonical completion has already been checked with all 234 coefficients
free. Using the actual q0=(xy+z²)/theta, its full C residual is

    (kAt/kappa) T_qB(cm C)
      =kAt cm [q0(kappa^-1 N1-p(ZN))+D3+kappa p(G5)].

D3 is literally closed and has no WW component, after the checked
zero-WW Koszul conversion. It is therefore a valid input to the existing
unconditional source extension. Let that extension return Pc,y,Vnorm,
the full high remainder Efull, the harmonic wedge Eharm, and the full
low remainder Elow=p(G5)-Bsource(Pc). Its checked identity is

    D3-A(Pc)+C(y)+q0 Vnorm=Efull+Eharm.

Consequently the actual normalized residual and divided arrow obey

    R=(1/kappa)T_qB(C)-A(Pc)-kappa Bsource(Pc)+C(y),
    V=Vnorm-kappa^-1 N1+p(ZN),
    R+q0 V=Efull+Eharm+kappa Elow.                       (1)

All factors kAt cm are restored on the C columns. The actual source
increment is kAt [[0,(cm/am)Pc],[0,-y]], and its right endpoint is its
fixed negative transpose. The U columns of the divided left arrow are
zero for this canonical choice. The fixed right arrow is the negative
determinant dual, not an independently chosen correction.

No error in (1) is set to zero. Taking exterior contraction yields

    q0 contraction(V)=contraction(E).

Taking the five-source monad differential yields

    q0 d(V)=d(E),                                      (2)

including all U,C and C,C pairs. Thus joint error vanishing implies full
divided-arrow closure by q0 regularity. Neither the subtracted N nor the
reduced C residual is incorrectly asserted to be an independently closed
five-source cochain.

`verify_q_middle_source_extension_bridge.py` executes the frozen adapter
and restoration on all 234 independent coefficients, checks (1), its
exterior defect, the high-spin/low-tail compatibility, both source ends,
and all ten skew source pairs in (2), keeping am,bm,cm,kAt and all marking
units formal. The full-U canonical identity and the C,C anomaly checks
remain in the separate frozen bundle.

This is a source/interface verification, not a source-equation solve. It
makes no claim of full-family independence, unrestricted completeness,
or an obstruction value. There are no selected physical coefficients,
points, rank experiments, frozen edits, or external writes.

## Constructive physical projection from 234 to 135 coefficients

The constant physical split gives P=I-C Zeta=Rsplit D. For every symmetric
linear B, define

    B9=D B D^t,
    Bprojected=Rsplit B9 Rsplit^t,
    F=B Zeta^t-(1/2)C Zeta B Zeta^t.

The literal identity

    B-Bprojected=C F^t+F C^t                             (3)

holds with every marking factor unchanged. Thus B9 is the complete
symmetric-linear coefficient on the constant nine-dimensional quotient;
its 135 coefficients need not be fitted or chosen from any actual example.

For each positive-linear column f=F_j, define

    H_j=q0 L_1(f)+sum_i v_i L_2(q0 partial_i f).

Its entire mixed and VWW parts are

    Hmixed_j=2q0 f,
    HZ_j=q0 Z_1(f)+(1/2)p(J grad(q0) r_f),
    H_j=Hmixed_j-kappa HZ_j.                             (4)

Here the displayed p in HZ denotes the VWW exterior realization; the
exported HZ field stores its six-vector coefficient. Each H_j annihilates
the whole U arrow. By the frozen full-completion C-factor identity,

    T_qB-T_qBprojected=sum_j sym(C_j,H_j),                (5)

where sym(a,b)=(a b*+b a*)/2. This is a literal full-source middle
homotopy, not just a lower identity. The general source-boundary lemma
supplies both endpoints. No endpoint is dropped by the projection.

`universal_q_middle_C_source_projection.py::project_q_middle_C_sources`
returns B9, Bprojected, F, Hmixed and HZ. Its verifier checks (3)-(4) with
all 234 original coefficients independent, and (5) then follows by the
already checked universal factor identity and linearity. This supplies
an explicit adapter for the full135 family without changing the frozen
q-middle completion or introducing a new coefficient solve.

For efficiency, a second source-extension verifier uses B=phi*g*g^t,
with all twelve entries of g and all three coefficients of phi free.
This is polynomial polarization, not specialization: the distinct
monomials phi_k g_i g_j recover all 234 symmetric-linear input components
because the complete adapter is linear in B. It checks the same entire
source/error/division identities as the independent-coefficient verifier.
