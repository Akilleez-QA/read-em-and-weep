# A zero endpoint-core homotopy restriction forces a nonzero fourth gate

## Theorem

Retain the actual source2 nonzero pure-V compatible-radical hypotheses,
with canonical endpoint homotopy h and canonical fourth gate R. Let
NC be the actual endpoint negative submodule. Then

    h|NC4=0  implies  R != 0.                            (1)

Equivalently, R=0 forces h:NC4/I4 -> I2 to be an isomorphism. This
excludes the joint condition h|NC4=0 and R=0, not the whole separated
mechanism or source2, and does not select an actual coefficient.

The new universal identity is an isomorphism on the ENTIRE space

    Phi:Sym2 W tensor Sym4 W -> Hom(Sym2 W,Sym4 W),
    Phi(u)(b)=sum_i (a_i,b f_i)_2,
    u=sum_i a_i tensor f_i.                              (2)

Under the standard apolar identification of the target with its source,
its scalars on Sym6 W, Sym4 W, Sym2 W are respectively

    4, 28, 84.                                          (3)

Thus the finite-group channels V, P, D, A all survive. The map is not
merely allowed by characters and is not tested at a selected direction.

Assuming h|NC4=0, let J2=ker j2 and

    Gamma(v)(b)=h T_b v,       K=ker(Gamma|J2).

Then the actual common kernels are

    ker(Gamma|NR2)=NC2,
    rank Gamma|NR2=rank Gamma|J2=15,
    dim K=21,
    K=NC2 direct-sum P_h.                                (4)

In particular P_h necessarily has nonzero projection to the genuine
separated N0,2 block. This last assertion uses the already proved
exclusion of P_h contained in NC2, rather than a residual-large theorem.

## 1. Nine immutable inputs and exact hypotheses

The complete originals and exact SHA-256/Git-blob fingerprints are
retained in INPUTS.json and inputs/:

- PR795, commit 3f811311d76914a555c7e7d0c5b887b41805aa6c: the actual
  fixed-variable negative split N=N0 plus NR, the radical orientation,
  and exact residual module 0 -> NC -> NR -> N8 -> 0.
- PR1019, commit 3fb2475ffb275c5789acbaa8f9f84ed272713785: the canonical
  homotopy, hQ2=j2, Q2h=j4, im h=I2 plus P_h, ker Q2=A plus I2,
  im h intersect ker Q2=I2, and Q2:P_h -> I4 an isomorphism.
- PR1058, commit 1435873de29d39e14ceee3de8d879e90f90b437a: under
  nonzero N0 projection, the actual quadratic descendant map
  A tensor P_h -> T_A P_h is injective and its image is disjoint from
  I4. It gives F4=I4 direct-sum T_A P_h, of dimension16.
- PR1064, commit bfc239e1c8624a0346394e1454b0bea3c976d40d: h(NR4)=I2;
  the marked D_can projects isomorphically to D8 in N8,4 and h is an
  isomorphism on D_can. These assertions do NOT require residual-large.
- PR1069, commit 41bc20cade3198306c492c0c46399d71eb0d51c4: the sandwich
  identity h T_b h=0, T_b im h contained in ker h contained in im Q2,
  and the canonical bilinear transfer with diagonal R.
- PR1081, commit 411b644cdc12938c35b7fedac5bb92664bfc1a47: under nonzero
  N0 projection, the actual generated terminal F5 is 2T, dimension12.
  Its proof uses the same genuine projectors and actual cubic quotient.
- PR1082, commit 6f1cf5ad484bd6c3d6608345da576fb1221f8222: the small
  branch is excluded; in particular P_h is not contained in NC2.
- PR1089, commit f8dfebc8c12cbefd3b17422fa1220629e90af78e: the bilinear
  transfer is symmetric in every retained branch. Its Section4 proves
  the actual descended C2 formula for h under precisely h|NC4=0,
  without an endpoint-nine or residual-large assumption.
- PR1106, commit 26ab0ded8bbe635d8aa81798e8fe8a6032e81ce2: the actual
  image Q3(NC3)=T_Q is one T, dimension6, in every retained branch;
  also W NC2=NC3, W I4=0, and Q3(l v)=l Q2(v) on the actual module.

All actual-source, geometric, compatibility and fixed-variable hypotheses
of these inputs remain in force. No conclusion of the residual-large
common-kernel theorem PR1113 is used. In particular its different NC
kernel cannot be imported here.

Here A=Sym2 W, D=Sym4 W, T=Sym5 W; P and V are the other four- and
three-dimensional irreducibles of the binary icosahedral group. The
actual spaces, in their original cohomological grading, are

    M2=N0,2 plus NR2,           dim M2=41,
    N0,2=P+D,                  dim NR2=32,
    NC2=Sym16 W=V+P+2D,        dim NC2=17,
    NC3=Sym17 W,               dim NC3=18,
    NC4=P+D,                  dim NC4=9,
    N8,2=A tensor Sym4 W,      dim N8,2=15,
    N8,4=(A tensor Sym6 W)/Delta(Sym8 W)=V+P+D.

The residual quotient maps commute with the ORIGINAL negative variables.
They keep the external A factor fixed and multiply the second polynomial
factor. No invariant-Q preservation of these submodules is assumed.

## 2. The full universal isomorphism

For binary forms use the unnormalized second transvectant

    (a,g)_2=a_xx g_yy-2 a_xy g_xy+a_yy g_xx.

It is SL2-equivariant. The two arguments in (2) play different roles:
a_i is in the EXTERNAL A factor of N8,2, while b multiplies the quartic
f_i to degree six before contraction with a_i.

Let X,Y mark the external quadratic factor and x,y the quartic factor.
Use monomials X^(2-i)Y^i x^(4-j)y^j for the source, ordered by i then j.
For the target first record Phi(u) on b=x^(2-k)y^k, k=0,1,2, each in
its five ordinary quartic coefficients. This means all three b
coefficients and all fifteen u coefficients are retained. The full
coefficient matrix M has entries

    M[(k,r),(i,j)]
      =[x^(4-r)y^r] (x^(2-i)y^i, x^(6-k-j)y^(k+j))_2.  (5)

Its exact determinant is

    det M=5222734824996864=2^25 * 3^3 * 7^8.             (6)

This alone proves (2) is an isomorphism. The following complete
irreducible calculation independently identifies every channel.

The invariant apolar Gram matrix on A in the ordered monomial basis is

    G2 = [[0,0,1],[0,-1/2,0],[1,0,0]].

Thus L=(G2^(-1) tensor Id_5) M is the SL2-equivariant endomorphism of
A tensor Sym4 W corresponding to Phi. Clebsch decomposition is

    A tensor Sym4 W=Sym6 W plus Sym4 W plus Sym2 W.

Highest-weight vectors for these three summands are respectively

    X^2 x^4,
    (X y-Y x) X x^3,
    (X y-Y x)^2 x^2.                                    (7)

Direct substitution in (5) gives L times these vectors equal to
4, 28, 84 times themselves. Equivariance then gives the same scalar on
each entire summand. The verifier also constructs EVERY lowering
descendant using Y partial_X+y partial_x, verifies that the three
families together span all fifteen coefficients, and checks all their
matrix identities. This proves (3) on the full domain, not just on
three highest-weight lines. In particular all four finite-group
channels survive, since Sym6 W=V+P, Sym4 W=D and Sym2 W=A.

## 3. Transport through the actual residual quotient

Assume h|NC4=0. By exactness, h|NR4 descends to

    hbar:N8,4 -> I2.

PR1064 proves it nonzero using the actual marked D_can, whose projection
to D8 and h image are both isomorphisms. Under the precise quotient
identification by the first and second transvectants, equivariance
kills V+P and identifies hbar with

    [a tensor g] |-> lambda i2((a,g)_2),  lambda != 0,    (8)

where i2:Sym4 W -> I2 is the coherent actual identification in PR1089.
The value of lambda is not chosen. This is exactly the full zero-NC4
case of PR1089 Section4, not a consequence assigned from endpoint nine.

Since pi intertwines actual negative multiplication, equations (2),(8)
give the literal factorization

    Gamma|NR2=lambda Hom(A,i2) Phi pi2.                  (9)

The quotient pi2 is onto with kernel NC2, and Phi is invertible.
Therefore Gamma|NR2 is onto Hom(A,I2), of dimension15, and has kernel
exactly NC2. No section of NR over N8 was chosen in this argument.

The radical kills NR2 by its actual orientation in PR795. Since
im j2=I2=D and N0,2=P+D, its D restriction is an isomorphism onto I2
and its P restriction vanishes. Consequently

    J2=ker j2=NR2 direct-sum (N0,2)_P,     dim J2=36.     (10)

For v in J2 and every b,

    Q2 h T_b v=j4 T_b v=T_b j2 v=0.

As h T_b v also belongs to im h, the actual intersection
im h intersect ker Q2=I2 makes Gamma|J2 correctly typed with target
Hom(A,I2). It is onto since its restriction to NR2 already is, so
its kernel K has dimension36-15=21. We do NOT declare hT(M2) contained
in I2 on the whole degree-two space.

## 4. The actual common kernel identifies P_h

The sandwich identity gives Gamma(F2)=0 for F2=im h=I2 plus P_h.
Moreover j2 h=0, so F2 is actually contained in J2. Thus P_h lies in K.

If its genuine separated projection e0|P_h were zero, P_h would lie
in NR2 and therefore in ker(Gamma|NR2)=NC2. This contradicts PR1082.
Hence e0|P_h is nonzero. It is an isomorphism onto (N0,2)_P because
both are irreducible P representations. In particular

    P_h intersect NC2=0.

Both NC2 and P_h lie in K, and their dimensions17+4=21 fill K. This
proves (4). These are actual subspaces, not an arbitrary splitting of
two equal-character P copies. It also establishes the nonzero-N0
hypothesis required for the separated descendant theorems below.

## 5. A zero gate would force the wrong terminal dimension

Suppose for contradiction also R=0. Choose any equivariant right inverse
G:Z=im Q2 -> M2. Let s:I4 -> P_h be the actual inverse of Q2|P_h, and
form the complete first correction

    k:A tensor I4 -> M2,        k(b,p)=G T_b s(p).       (11)

It is well-defined because T_b im h lies in Z. PR1069 identifies

    B(a,b)p=h T_a G T_b s(p),       R(a)=B(a,a).

PR1089 proves B symmetric in ALL retained branches, so polarization of
the full quadratic identity R=0 gives B=0. Thus h T_a k(b,p)=0 for
every a,b,p. Independently,

    j2 k(b,p)=h Q2 k(b,p)=h T_b s(p)=0

by the sandwich. Hence im k lies in the correctly typed common kernel K.

Because e0|P_h is nonzero, PR1058 proves that Q2k=T_b s is injective
on the twelve-dimensional space A tensor I4, with image T_A P_h
disjoint from I4. Therefore k is injective. If an element of im k
also lay in F2, its Q2 image would lie in both T_A P_h and Q2F2=I4.
That intersection is zero; injectivity of Q2k forces the element zero.
So F2 and im k are disjoint, and their dimensions9+12=21 fill K:

    K=F2 direct-sum im k,
    Q2K=I4 direct-sum T_A P_h=F4.                       (12)

This is proved afresh using the separated descendant map. It is NOT an
application of the residual-large theorem in PR1113.

Applying Q2 to the different actual decomposition in (4) yields

    F4=Q2K=Q2(NC2)+I4.                                 (13)

We need only this sum; no assertion that Q2 preserves NC or NR occurs.
For completeness it is direct: ker Q2=A plus I2, its A lies in NR2 and meets K trivially
by (9), and I2 lies in K. Thus ker(Q2|K)=I2, making dim Q2K=16,
whereas dim Q2(NC2)=17-5=12 and dim I4=4.

Now multiply (13) by the actual negative two-space W. The exact actual
identities W NC2=NC3, W I4=0 and Q3(lv)=l Q2(v) give

    F5=W F4=W Q2(NC2)+W I4=Q3(NC3)=T_Q.                (14)

PR1106 proves this specific image T_Q has dimension6. On the other
hand the already established nonzero N0 projection makes PR1081
applicable, and that theorem gives dim F5=12. This contradicts (14).
Therefore R cannot vanish under h|NC4=0, proving (1).

## 6. Consequences and limits

Since h(NC4) lies in I2 and h kills I4, a nonzero restriction is an
isomorphism NC4/I4=D -> I2=D. Taking the contrapositive gives

    R=0 implies rank(h|NC4)=5.

Thus any zero-fourth continuation, including one in the separated
mechanism, must use the nonzero endpoint-core row. This does not prove
R nonzero when that row is nonzero, nor eliminate either endpoint16
mechanism. It does not identify the separated terminal graph or evaluate
an original-fifth symbol. Actual projectors remain fixed throughout;
no Q-stability of a negative splitting is asserted.

## Reproduction

Run python verify.py and python -O verify.py. The verifier checks all
nine immutable input digests, reconstructs the complete universal map
(5), checks the determinant, verifies all fifteen irreducible descendant
identities and the Clebsch decomposition, and checks the representation
and dimension identities used in the proof. The actual-map transport,
correction placement and terminal equality remain the written argument;
integer arithmetic is not presented as authentication of an HM instance.

No actual source coefficient, parameter, direction, point, jet, matrix
or source-instance rank is evaluated. All matrices constructed here are
whole universal representation maps. No historical experiment is run.
