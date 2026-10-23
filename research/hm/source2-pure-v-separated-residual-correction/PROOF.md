# Universal homotopy rank and a separated residual correction section

## Theorem

Retain the actual source2 nonzero pure-V compatible-radical hypotheses.
Fix a genuine negative separation N=N0 plus NR and the actual residual
sequence 0 -> NC -> NR --pi--> N8 -> 0, with original negative variables.
Put J2=ker j2 and define the correctly typed map

    Gamma:J2 -> Hom(A,I2),        Gamma(v)(a)=h T_a v,
    K=ker Gamma,                 K_{R,2}=K intersect NR2.

Here K_{R,2} is a DEGREE-TWO common kernel, not the older endpoint
kernel ker h intersect NR4. In every retained mechanism,

    rank Gamma|NR2=rank Gamma=15,
    dim K_{R,2}=17,      dim K=21.                       (1)

If h|NC4=0 then K_{R,2}=NC2. If h|NC4 is nonzero, there is the actual
exact sequence

    0 -> I2 -> K_{R,2} --pi2--> (N8,2)_(V+P+D) -> 0.     (2)

Now additionally assume R=0 and that the canonical P_h has NONZERO
projection to N0,2. The zero-gate assumption forces the nonzero NC4 row,
so (2) applies. Let sigma:(N0,2)_P -> P_h be the inverse of e0|P_h,
including its actual embedding into J2, and define

    r=Id_J2-sigma e0 : J2 -> NR2.                        (3)

For any equivariant right inverse G of Q2 on its image Z, set

    s:I4 -> P_h, Q2s=Id_I4,
    k(a,p)=G T_a s(p),       ktilde=r k.                  (4)

Then ktilde is injective and supplies a degree-two direct sum

    K_{R,2}=I2 direct-sum ktilde(A tensor I4).             (5)

Both [ktilde]:A tensor I4 -> K_{R,2}/I2 and
pi2 ktilde:A tensor I4 -> (N8,2)_(V+P+D) are isomorphisms independent
of G. Its P component is the unique residual P in K_{R,2}, which is
DISTINCT from P_h. Its V and P components are independent of G as actual
maps; only its D component has an I2-valued ambiguity.

There is an exact, potentially nonzero normalization defect

    delta=Q2 sigma e0 k : A tensor I4 -> I4,
    Q2 ktilde(a,p)=T_a s(p)-delta(a,p).                  (6)

The defect is independent of G and supported on the unique P input channel.
It is not asserted zero or nonzero. Subtracting P_h is NOT subtraction
of a Q2-kernel vector; the raw correction equation must retain (6).

Let E0 denote the actual twelve-dimensional image of the quadratic
P descendants in N0,4. Then the actual cross-block map descends to an
isomorphism

    e0 Q2 : K_{R,2}/I2 -> E0.                            (7)

Consequently

    F4=I4 direct-sum Q2(K_{R,2}),
    Q3(W K_{R,2})=F5,       dim F5=12.                  (8)

These are coefficient-space and actual multiplication identities. They
do not split the residual negative module horizontally, preserve a raw
corrected string, select a fifth obstruction, or claim that the separated
zero-gate mechanism occurs.

## 1. Exact inputs and type conventions

Ten complete immutable public proofs are retained in INPUTS.json:

- PR795 at 3f811311d76914a555c7e7d0c5b887b41805aa6c gives the genuine
  negative split, the residual short exact sequence, radical orientation,
  and the original polynomial arrows.
- PR792 at 2f01f18960ce56b8b2a0c1260c277de3c5f916bf identifies the actual
  radical image I2=F12 Sym4 W and I3=F12 Sym5 W with coherent products.
- PR1019 at 3fb2475ffb275c5789acbaa8f9f84ed272713785 gives
  hQ2=j2, Q2h=j4, im h=I2 plus P_h, ker Q2=A plus I2, and the actual
  nonzero canonical A row h T_a a_A(f)=mu i2(a f), mu nonzero.
- PR1058 at 1435873de29d39e14ceee3de8d879e90f90b437a gives, under the
  nonzero N0 projection, injectivity of the actual quadratic descendant
  map A tensor P_h -> F4 and of its genuine separated projection;
  its image is disjoint from I4 and F4=I4 plus T_A P_h.
- PR1064 at bfc239e1c8624a0346394e1454b0bea3c976d40d gives the
  unconditional h(NR4)=I2 and the canonical A,S,D string lying in NR.
- PR1069 at 41bc20cade3198306c492c0c46399d71eb0d51c4 gives the sandwich
  h T_a h=0, Q2:P_h -> I4, T_A im h contained in Z, and the bilinear
  transfer B(a,b)=h T_a G T_b s with diagonal R.
- PR1081 at 411b644cdc12938c35b7fedac5bb92664bfc1a47 proves F5 has
  dimension12 in the nonzero N0 mechanism, and retains W I4=0.
- PR1089 at f8dfebc8c12cbefd3b17422fa1220629e90af78e proves B symmetric
  in every retained mechanism, so R=0 implies B=0.
- PR1113 at 09b03061644e417b44b2ea97a00c73618794c268 supplies the full
  UNIVERSAL D18 coefficient projection certificate. Its residual-large
  theorem is NOT applied in another mechanism. Section2 below rederives
  the required transport with the exact weaker hypothesis h|NC4 nonzero.
- PR1117 at 630d92dbca7dba13a99f31f7be94b53e785e18c6 gives the full
  universal N8 quadratic Hom isomorphism, K_{R,2}=NC2 when h|NC4=0,
  and the implication R=0 -> h|NC4 nonzero in all retained mechanisms.

All inherited actual-source and geometric hypotheses remain in force.
The relevant actual spaces and characters are

    N0,2=P+D,
    NR2=A+2V+2P+3D,          dim NR2=32,
    NC2=Sym16 W=V+P+2D,     dim NC2=17,
    NC4=Sym18 W/H_t=P+D,    H_t=A18+V18+P_t,
    N8,2=A tensor Sym4 W=A+V+P+D,
    Hom(A,I2)=A+V+P+D,      dim Hom(A,I2)=15.

The radical kills NR2; its image I2 is D. Hence the actual j2 kernel is
J2=NR2 direct-sum (N0,2)_P, dimension36. For v in J2,

    Q2 h T_a v=j4 T_a v=T_a j2 v=0.

Since im h intersect ker Q2=I2, Gamma is correctly typed on J2.
The same target is not assigned to hT on arbitrary M2.

## 2. Universal rank with the precise nonzero-row hypothesis

Assume for this section only that h|NC4 is nonzero. It kills I4=P and
maps the unique quotient D=NC4/I4 isomorphically to I2. The actual
quadratic arrow NC2 -> NC4 is multiplication followed by the endpoint
quotient, and H_t contains no D. Thus Gamma|NC2, up to an UNEVALUATED
nonzero output identification, is exactly

    f |-> (a |-> projection_D18(a f)).                   (9)

This conclusion needs h|NC4 nonzero, not residual-large placement of
P_h. It retains the actual original multiplication and quotient.

For clarity the full universal coefficient certificate from PR1113 is
reconstructed here, without running its historical executable. In its
fixed normalization the invariant form is

    F12=-2 x^12-(44 sqrt5/5)x^10 y^2+66 x^8 y^4
        +(88 sqrt5/5)x^6 y^6+66 x^4 y^8
        -(44 sqrt5/5)x^2 y^10-2 y^12.

With unnormalized transvectants, set H20=(F12,F12)_2 and
E:Sym4 W -> Sym18 W, d -> (H20,d)_3. Let G18 be the apolar Gram matrix
with antidiagonal entries (-1)^i/binom(18,i). The exact19-by5 matrix E
has rank5. Its equivariant image is the unique D18. Thus E^t G18
projects to its dual and kills the other irreducible constituents.

Stack this projection after multiplication by all three quadratic
monomials, retaining all seventeen input coefficients. Call the resulting
15-by17 matrix M, and let I be the17-by5 matrix for F12 Sym4 W. The
full exact identities are

    rank E=5, rank M=12, M I=0, rank I=5.               (10)

The verifier also checks the exact nonzero twelve-minor recorded in
PR1113. Consequently the kernel in (9) is exactly the ACTUAL I2, and
its image fills the V+P+D part of Hom(A,I2). All three rows survive;
this is not a character-only nonvanishing assertion.

The actual canonical A lies in NR2 since N0,2 has no A. The nonzero
row from PR1019 fills the remaining A in the target. Therefore Gamma
on NR2 is onto. Its kernel has character V+P+2D and dimension17.
Its intersection with NC2 is I2 by (10). Projecting through the ACTUAL
pi2 gives image character V+P+D in multiplicity-free N8,2, proving (2).

Since NR2 is contained in J2, Gamma on J2 is also onto, with kernel
character V+2P+2D and dimension21. If h|NC4 instead vanishes, PR1117
proves the same two ranks by its whole fifteen-dimensional transvectant
Hom map, and identifies K_{R,2}=NC2. This proves (1) in every mechanism.

This argument does NOT use the residual-large assertion P_h contained
in K_{R,2}. In the separated case considered below that assertion is
false: P_h has nonzero separated projection.

## 3. The zero-gate separated correction fills the common kernel

Now impose R=0 and e0|P_h nonzero. PR1117 forces h|NC4 nonzero,
so (2) and its rank consequences apply. The sandwich puts F2=I2 plus
P_h inside K. Since e0|P_h is an isomorphism onto the separated P,
projection gives the actual direct sum

    K=K_{R,2} direct-sum P_h.                            (11)

Indeed the summands have zero intersection and dimensions17+4=21.

The actual k in (4) is well-defined because T_A P_h lies in Z.
Symmetry of B and its diagonal R give B=0, hence Gamma k=0.
Also j2 k=h Q2 k=h T_A s=0 by the sandwich, so im k lies in K with
the proper domain typing. The separated descendant theorem gives
Q2k=T_A s injective on A tensor I4 and disjoint from I4. It follows
that k is injective and im k meets F2 trivially: applying Q2 would
otherwise give a vector in T_A P_h intersect I4, and injectivity
of Q2k then kills it. Dimensions give

    K=F2 direct-sum im k
     =I2 direct-sum P_h direct-sum im k.                 (12)

Applying Q2 gives Q2K=F4. This is a fresh separated-case proof, not
an invocation of PR1113's residual-large correction theorem.

## 4. Residual normalization and its invariant quotient

The actual map sigma in (3) is well-defined by the chosen genuine
separation. For every v in J2, e0 r(v)=0, so r(v) lies in NR2.
Moreover r is identity on NR2, has kernel exactly P_h, and r^2=r.
On K its image is K_{R,2}, by (11), and it fixes I2.

Applying r to (12) proves (5), including directness: if r k(u) lies
in I2, then k(u) lies in I2 plus P_h=F2, so u=0. This simultaneously
proves that ktilde is injective and that its twelve-dimensional image
is a complement to I2. The complement's D component can depend on G;
no horizontal splitting of negative modules has been made.

The quotient K_{R,2}/I2 is V+P+D. Equation (2) identifies it with the
actual canonical isotypical subspace (N8,2)_(V+P+D). Thus both
isomorphisms following (5) hold with their literal maps.

For another equivariant right inverse G', the difference

    k'-k:A tensor I4=V+P+D -> ker Q2=A+I2

is equivariant. Its V and P parts vanish, and its D image lies in I2.
Since r fixes I2, the same statements hold for ktilde'-ktilde. Therefore
[ktilde] and pi2 ktilde are independent of G; V and P are canonical
as actual maps, and D is canonical modulo I2. In addition e0 kills
any such difference, so the defect delta below is independent of G.

K_{R,2} has exactly one P constituent, denote it P_R. The P part of
ktilde is nonzero by injectivity, hence its image is exactly P_R. This
is an actual identification from an actual map. It is not P_h, since
P_R lies in NR2 and e0|P_h is nonzero. The V part similarly fills the
unique V in K_{R,2}. As J2 has only separated P, r does not change the
V or D parts of k: only its P channel needs subtraction.

## 5. The exact Q defect and forced cross-block image

Apply Q2 to the literal identity ktilde=k-sigma e0k:

    Q2 ktilde=T_A s-Q2 sigma e0k=T_A s-delta.            (13)

Because sigma takes values in P_h and Q2 P_h=I4, delta takes values
in I4. Its equivariance and A tensor I4=V+P+D show it is supported
only on the P input constituent. Its independence of G was proved
in Section4. No value is assigned to this one possible channel.

In particular (13) is generally NOT the original raw correction
Q2k=T_A s. Although the two equations agree modulo I4, no unchanged
corrected string or unchanged higher-symbol representative follows
from this observation. The normalization is a coefficient quotient
section, not a Q-kernel gauge.

The actual first-block projector kills I4. Therefore (13) gives

    e0 Q2 ktilde=e0 T_A s.                              (14)

The right side is the exact separated quadratic descendant isomorphism
A tensor I4 -> E0 of PR1058, with all original projectors retained.
Since Q2 I2=0, e0 Q2 descends to K_{R,2}/I2. Composing with the
isomorphism [ktilde] gives (14), so the descended map is an isomorphism,
proving (7). This is an actual CROSS-BLOCK conclusion about Q2, not
an assumption that Q2 preserves a negative summand.

Equation (14) also makes Q2 ktilde injective and puts its image
disjoint from I4. Since K_{R,2}=I2 plus im ktilde, Q2(K_{R,2}) is
that twelve-dimensional image. Combining (11) with Q2K=F4 gives the
first equality in (8), including directness. More precisely the two
actual twelve-dimensional complements T_A P_h and Q2(K_{R,2}) in F4
have the same separated projection and differ by the specific defect
delta. Their V and D parts agree; their P parts need not.

Finally multiply F4=I4 plus Q2(K_{R,2}) by the actual negative W.
PR1081 gives W I4=0. Multiplication by the SAME invariant quadratic
commutes with these negative multiplications, so

    F5=W F4=W Q2(K_{R,2})=Q3(W K_{R,2}).                (15)

The separated terminal theorem gives dimension12, proving (8). Since
NR is negative-stable, W K_{R,2} lies in the actual NR3. Thus (15)
retains the residual source and the genuinely separated terminal
projection without asserting any Q3 preservation of NR.

## Reproduction and limits

Run python verify.py and python -O verify.py. The verifier authenticates
ten complete public inputs; reconstructs the full universal D18
coefficient projection and kernel; checks exact finite-group characters,
Hom multiplicities and dimensions; and verifies the complete abstract
projection, defect and cross-block identities with an arbitrary formal
linear leakage matrix. That last universal linear-algebra test does not
select the actual leakage or model an actual HM instance.

The actual-map arguments, especially naturality of the separated
projectors and the identification of the D18 row, remain essential.
No actual source coefficient, parameter, direction, jet, matrix or
instance rank is evaluated. No historical executable is run. Neither
zero R nor the separated mechanism is asserted realized, and no fifth
symbol or full adjoint rank is decided.
