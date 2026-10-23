# Actual residual Koszul lifts force global alternating-transfer vanishing

## Result

Retain the conditional actual source2 nonzero pure-V compatible-radical
hypotheses. Let Q2:M2_+→M4_+ and Q3:M3_-→M5_- be multiplication by
the SAME invariant quadratic. Let h:M4_+→M2_+ be the canonical endpoint
homotopy and j the actual fixed-negative radical. Then

    j3(ker Q3)=I3,
    rank_T(Q3,j3)=4,
    κ=0.                                                   (1)

Here I3=im j3=T, rank_T is rank on irreducible T multiplicity spaces,
and κ is the alternating coefficient of the full bilinear transfer B
in PR1085. Consequently B is symmetric and is determined by its diagonal
R through polarization. This does not prove R nonzero, exclude B=0,
or assert commutation of the full pencil or of mixed homotopy operators.

Put K3=ker Q3∩ker j3 and F3=W im h, the actual generated middle space.
There is an exact sequence and a precise quotient character

    0→K3→ker Q3 --j3→ I3→0,
    K3/F3 ≅ 2W′+3S as a representation.                    (2)

Thus this actual quotient has dimension16 and contains no T. The odd
endomorphism (j3,0) of M3 --Q3→ M5 is not nullhomotopic. No canonical
splitting of (2), source realization, or selection of a remaining
endpoint-sixteen mechanism is asserted.

## 1. Seven exact inputs and actual domains

INPUTS.json pins complete public proofs at immutable commits:

- PR1019: hQ2=j2, Q2h=j4, ker j4=im Q2, h j4=0,
  im h∩ker Q2=I2=D, and the actual radical image I=(D,T,P).
- PR1064: NR4⊂im Q2, h(NR4)=I2, h(I4)=0, NC4=P+D;
  the actual marked D_can lies in NR4, projects isomorphically onto
  D8⊂N8,4, and h|D_can is an isomorphism to I2. Its fixed-variable
  realization of N8,4 uses the transvectants C1,C2 below.
- PR1068: the actual Koszul exact sequence

      0→M3 --δ→ W⊗M4 --μ→ M5→0,
      δz=x⊗Y_yz−y⊗Y_xz,                              (3)

  and the actual restriction δ:NC3→W⊗NC4 is an isomorphism.
  Here Y_l:M3→M4 is negative multiplication. NC4 is the full
  joint-negative kernel, not an arbitrary equal-character subspace.
- PR1085: F3=W′+2T lies in K3, and κ≠0 implies
  rank_T(Q3,j3)≤3; its canonical mixed-syzygy map is
  Hbar:W⊗I4=W′+T→K3/F3. Its normalization is
  Alt B(a,b)=(B(a,b)−B(b,a))/2=κ L_[a,b]*.
- PR1086: ker Q3=3W′+3S+3T and rank_T Q3=3, with image the full
  3T in M5=W′+3T. An odd nullhomotopy exists exactly when
  j3(ker Q3)=0.
- PR795: the ACTUAL exact negative module 0→NC→NR --π→N8→0,
  with quotient maps intertwining both original negative arrows,
  N8,3=A⊗Sym5 W and N8,4=(A⊗Sym6 W)/Delta(Sym8 W).
  The arrows multiply the second polynomial factor.
- PR792: coherent actual inclusions

      I2=f12 Sym4 W,     I3=f12 Sym5 W,

  where f12 is a nonzero invariant form, with inherited arrow ordinary
  multiplication on those polynomial factors. This fixes the relative
  normalization between degrees two and three, not just their characters.

All inherited actual-source hypotheses are retained. Put Z=im Q2 and
write X:W⊗M2→M3 for actual multiplication. Then

    Q3 X = μ(Id_W⊗Q2),
    j3 X = X(Id_W⊗j2).                                (4)

The first equality is multiplication by the same polynomial, not
Q-stability of NC or NR. The second is radical intertwining. The
quadratic is central-even, W is central-odd, and both sides of the
first equality land in the full negative-parity space M5_-.

## 2. Lift every residual Koszul relation

Choose an equivariant right inverse G:Z→M2 of Q2, which exists by
semisimplicity. It is only defined on im Q2, not on all of M4. Since NR
is an actual negative submodule, δ(NR3)⊂W⊗NR4. The actual containment
NR4⊂Z from PR1064 therefore makes the following map well-defined:

    v_G=X(Id_W⊗G)δ|NR3 : NR3→M3.                     (5)

Its exact compositions are

    Q3 v_G=μ(Id_W⊗Q2G)δ|NR3=μδ|NR3=0,
    j3 v_G=X(Id_W⊗j2G)δ|NR3
           =X(Id_W⊗h|NR4)δ|NR3=:θ.                  (6)

Indeed hQ2=j2 gives j2G=h on Z. Thus v_G takes values in the ACTUAL
kernel of Q3. The determinant signs in (3) are essential: this lifts
x⊗Y_yz−y⊗Y_xz rather than the sum of those terms.

The map θ is independent of G even though v_G need not be. For another
section G′, Q2(G−G′)=0 and j2(G−G′)=hQ2(G−G′)=0. Thus v_G−v_G′
has image in K3. No extension of h to another degree is used.

We prove θ(NR3)=I3 in both possible cases for h|NC4. All of θ lands
in I3, since h(NR4)=I2 and X(W⊗I2)=I3.

## 3. Nonzero h on NC4

Because h kills I4 and maps NC4 into I2, a nonzero h|NC4 induces an
isomorphism NC4/I4=D→I2=D. Hence W⊗h is onto W⊗I2. The actual
isomorphism δ|NC3 in PR1068, followed by this surjection and ordinary
multiplication W⊗I2→I3, proves

    θ(NC3)=I3.                                        (7)

In particular θ(NR3)=I3 in this case. This uses the actual δ isomorphism,
not an arbitrary representation isomorphism of two eighteen-dimensional
spaces.

## 4. Zero h on NC4: the genuine quotient still detects I3

Suppose instead that h|NC4=0. The actual exact sequence
0→NC4→NR4 --π4→N8,4→0 and h(NR4)=I2 give a unique descended map

    hbar:N8,4→I2,          h|NR4=hbar π4.              (8)

It is nonzero: h is an isomorphism on the particular D_can⊂NR4,
whose projection to D8 is an isomorphism by PR1064. This descent is
proved directly from the assumed zero restriction. It does not discard
any hypothesis of an older endpoint-nine argument, and makes no
endpoint-nine assumption.

Use formal variables x,y in the second polynomial factor of N8 and
A=Sym2 W in the first factor. The fixed quotient in PR1064 is

    C=(C1,C2):A⊗Sym6 W→Sym6 W⊕Sym4 W,
    Ck(a⊗f)=(a,f)_k,
    (a,f)_k=Σ_j (−1)^j binom(k,j)
                (∂x^(k−j)∂y^j a)(∂x^j∂y^(k−j) f).   (9)

It has kernel Delta(Sym8 W) and identifies the actual quotient N8,4
with (V+P)⊕D. Equivariance of (8) kills its V+P part. Under the coherent
inclusion i2(f)=f12 f of PR792, equation (8) is therefore

    hbar([a⊗f])=λ i2((a,f)_2),          λ≠0.          (10)

The value of λ is not chosen. Its nonzero status follows from D_can,
not from a hypothetical horizontal splitting of NR.

Because π commutes with the actual negative arrows, formula (6) now
kills NC3 and descends through π3:NR3→N8,3=A⊗Sym5 W. Writing
i3(g)=f12 g, coherence of I2→I3 gives on this quotient

    θbar(a⊗g)
       =λ i3(x(a,yg)_2−y(a,xg)_2)
       =2λ i3((a,g)_1).                               (11)

Both terms have the same λ: the same actual hbar occurs in (10),
and i2,i3 are related by the inherited multiplication, not independent
rescalings of abstract D and T copies. No lift of the quotient N8 to NR
is chosen. Formula (11) uses only surjectivity of π3 and its commuting
arrow squares.

For clarity, (11) is a full polynomial identity, not evaluation at a
source parameter. Differentiating a quadratic a and any quintic g gives

    x(a,yg)_2−y(a,xg)_2
      =2[(x a_xx+y a_xy)g_y−(x a_xy+y a_yy)g_x]
      =2(a_x g_y−a_y g_x)=2(a,g)_1,                  (12)

where Euler's formula for the linear derivatives of a was used. The
checker verifies all eighteen coefficient pairs of the universal map
A⊗Sym5 W→Sym5 W. Its coefficient map has rank six. Equivalently it
is a nonzero equivariant map to the irreducible T=Sym5 W, hence onto.
Since λ≠0 and π3 is onto, (11) proves θ(NR3)=I3 also in this case.

## 5. Odd row independence, alternating vanishing and the quotient

Equations (6), (7), and (11) prove in all cases that

    j3(v_G(NR3))=I3,          v_G(NR3)⊂ker Q3.

Since im j3=I3, this proves j3(ker Q3)=I3 and the exact sequence (2).
For any linear maps A:E→F and b:E→H,

    rank(A,b)=rank A+rank(b|ker A),

as seen by projecting im(A,b) onto im A. Its kernel is
{0}⊕b(ker A). Applying this to T multiplicity spaces, PR1086 gives
rank_T Q3=3 and the proved surjection gives rank_T(j3|ker Q3)=1.
Hence rank_T(Q3,j3)=4. PR1085 says κ≠0 would force rank at most3,
so κ=0. The odd nullhomotopy criterion of PR1086 now rules out such
a nullhomotopy rather than supplying an extension of h.

Subtract I3=T from the exact kernel character of PR1086 to obtain
K3=3W′+3S+2T. The actual inclusion F3⊂K3 from PR1085 makes its
quotient character K3/F3=2W′+3S. This quotient has dimension16, not
merely a bound. In particular the T restriction of Hbar is zero; its
W′ restriction need not be zero and is not determined here.

There is also an exact odd-cohomology consequence. On H0 of the odd
complex, namely ker Q3, the radical action j3 has image I3 and kernel
K3. Its square is zero: I3⊂F3 and j3(F3)=0 by PR1085. On the
three-dimensional T multiplicity space of ker Q3 it is therefore a
rank-one square-zero endomorphism, with Jordan block sizes (2,1).
The T-isotypical part of its kernel K3 is exactly the T-isotypical part
of the actual F3, since the latter is contained in K3 and both contain
two T copies. This nontrivial odd cohomology action does not contradict
the even endpoint homotopy; no homotopy across both complexes is assumed.

Since the unique alternating channel has vanished, B is symmetric.
Over C its diagonal determines it by

    B(a,b)=[R(a+b)−R(a)−R(b)]/2.                      (13)

Thus R=0 implies B=0, but neither is excluded by this theorem. Equation
(13) is polarization of this bilinear transfer only. It is not an
identity T_a h T_b=T_b h T_a on the ambient module, nor a claim that
all fixed-pencil operators commute. Neither endpoint-sixteen mechanism
is selected and no positive/full-adjoint rank conclusion follows here.

## Reproduction and limits

Run python verify.py and python -O verify.py. The bounded checker
authenticates all seven inputs, verifies composition types and parity,
checks the determinant cancellation, proves (12) on all formal
coefficients and its universal rank six, checks the abstract rank
identity in symbolic row normal form, and verifies the exact quotient
characters and polarization formula. The actual-map proof and the
coherent quotient identifications above remain essential.

No actual HM coefficient, source parameter, direction, point, jet,
matrix or instance rank is evaluated. The universal binary-form rank
in Section4 is a representation-channel certificate, not an actual
source calculation. The theorem retains the source hypotheses and does
not claim their realization or complete the original proof repair.
