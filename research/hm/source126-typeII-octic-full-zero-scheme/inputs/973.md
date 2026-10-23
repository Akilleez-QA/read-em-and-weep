# Full-radical naturality selects the Type II hidden scalar and factors the actual second symbol

## Result and limits

Assume an actual source126 Type II occurrence and compatibility of its
ENTIRE two-dimensional negative-pencil radical J with the canonical
invariant positive product Q. PR970 leaves only the joint-annihilator
footprint (r,epsilon,d)=(2,0,0). Set

    S=[U --Q--> Z],  M=[N2 --Q--> N4],
    T=[N2/U --Qbar--> N4/Z],
    U=Ann_J N2=F2,  Z=Ann_J N4.                          (1)

We place sources in cochain degree zero and targets in degree one.
Each is also a two-term family with differential Q+tT_a, where T_a
is actual multiplication by a negative quadratic a∈A=Sym²W.

Then the entire internal first symbol of S is

    b_S,a(k,h)=lambda·a k,  (k,h)∈A+D,  lambda≠0.        (2)

In particular its D-part scalar mu from PR965 is ZERO. The conditional
mu≠0 universal models in PR965 and PR969 cannot arise under the full-J
Type II hypotheses of this theorem. Those universal calculations remain
valid as calculations under their stated scalar alternative; that
alternative is now excluded here, not retrospectively miscomputed.

The connecting map and cokernel projection at t=0 are isomorphisms

    delta:H0(T)=D→H1(S)=D,
    eta:H1(M)=P→H1(T)=P.                                (3)

Use the sign convention delta([xbar])=[Qx] for any lift x of a quotient
kernel vector. The original canonical second Bockstein satisfies

    eta beta2_M,a = - b_T,a delta^(-1) b_S,a             (4)

on the ENTIRE original kernel A+D, where b_T is the quotient first
Bockstein. Consequently b_T is a nonzero equivariant bilinear map

    A⊗D→P,

and after equivariant identifications it is a nonzero scalar multiple
of ordinary multiplication followed by the projection

    Sym²W⊗Sym⁴W→Sym⁶W→Sym⁶W/V6=P.                       (5)

Thus b_T,a has rank four except at the ten reduced projective directions
identified by PR966, where it has rank three. Every nonzero square has
rank four. This is now a statement about the ACTUAL quotient first
symbol, conditional on full-J Type II occurrence, rather than a rank
analogy between unrelated maps.

The theorem does not prove or disprove full-J compatibility itself,
exclude source126, select a remaining radical line, or remove a source-dual
pair. Original maximal rank and the original proof repair remain open.
The quotient is still non-acyclic at Q and is not cancelled.

## 1. Immutable interfaces

INPUTS.json records exact public commits, paths, Git blobs and SHA256
hashes. All files are in Akilleez-QA/read-em-and-weep.

- PR970, b4267159972c8999ea3cfff53fbb631008d1e482,
  research/hm/source126-polar-integrability/PROOF.md, proves joint P-row
  injectivity and the sole Type II footprint under full-J compatibility.
- PR961, cc3215b97a5c92a9253a9774d0f25ade0648b6e5,
  research/hm/source126-typeII-joint-annihilator/PROOF.md, gives the actual
  subcomplex, quotient, connecting sequence and nonzero internal A symbol.
- PR965, de8e1d1a90d6f41dffa74df7cc7220c4e84bf4e7,
  research/hm/source126-typeII-internal-discriminant/PROOF.md, identifies
  the full internal symbol as lambda ak+mu{a,h}_1 with lambda≠0, and
  retains the exact G-representation identities used below.
- The original first-vanishing proof at
  eeb1a11799ca38a60c37f6ba96f263ef8e20dd1c and original second-nonvanishing
  proof at 6c724c3b74e2ae4d6992d8c7b99b41c0715d69c0, both in
  research/hm/order-four-quadratic-load/, retain the canonical actual
  correction and nonzero A-to-P second family. Their full filenames are
  included in the manifest and inputs/.
- PR966, 4d0a6713a9c81fe669967e1d23838bdc8f4162b6,
  research/hm/source2-pureV-quadratic-discriminant/PROOF.md, proves the
  uniform ranks and reduced rank-drop scheme of the universal family (5).
  Its source2 realization is not imported; only this explicitly defined
  universal family is used after the actual identification below.

All hypotheses of these inputs remain in force. The two-term maps use
the same fixed negative variables under the published actual-pencil
reconstruction. No actual coefficient, selected point, derivative,
parameter value or instance matrix is evaluated.

## 2. Actual subcomplex and connecting isomorphisms

PR970 gives

    U=A+2V+2P+2D,  dim U=27,
    Z=2V+2P+2D,    dim Z=24.

Here U equals the genuine F first endpoint, not merely an isomorphic
representation: it contains F2 and has exactly its dimension. The
pinned full algebra says j2 kills F2 and maps the residual into F2,
while j4 kills F4 and maps the residual into F4. The full annihilator
Z contains F4. As annihilators, U and Z are preserved by the negative
quadratic maps, so (1) is a short exact sequence of two-term families.

Their t=0 cohomology and natural maps are

    H0(S)=A+D --identity--> H0(M)=A+D → H0(T)=D,
    H1(S)=D → H1(M)=P --eta--> H1(T)=P.

The first identity follows because S contains the whole original
kernel, not a different copy of it. The long exact sequence therefore
makes delta injective; its source and target are both D of dimension
five, so it is an isomorphism. The map H1(S)→H1(M) is zero, and eta
is an isomorphism. These facts also follow from PR961's actual quotient
and cokernel maps, not just their equal characters.

## 3. Every radical element descends to a chain map T→S

For j∈J, the endpoint maps have

    j2(N2)⊂F2=U,    j2(U)=0,
    j4(N4)⊂F4⊂Z,  j4(Z)=0.                            (6)

The last equality is the definition of the common annihilator. Thus
j induces maps

    jbar0:N2/U→U,  jbar1:N4/Z→Z.

Full-J compatibility gives j4Q=Qj2; fixed negative-pencil commutation
gives j4T_a=T_a j2 for every a. Hence these descended maps form a
chain map T→S for the ENTIRE Q+tT_a family, not only for Q.

At Q its induced cohomology maps are

    j^0:D→A+D,  j^1:P→D.

They are G-equivariant. Since P and D are nonisomorphic irreducibles,
j^1=0. Since A and D are nonisomorphic, j^0 lands in the unique D
summand of H0(S); it is a scalar map between irreducible D copies.
At least one j has a nonzero scalar. Indeed if every induced j^0
were zero, for any quotient-kernel lift x with Qx∈Z, each j2x would
be zero. Here j2x is a genuine degree-zero cycle in S, because
Qj2x=j4Qx=0. There are no degree-minus-one boundaries to hide a
nonzero such vector. The equality j2x=0 for every j would give x∈U,
so every quotient-kernel vector would be zero, contradicting H0(T)=D.
Thus some j^0 is an isomorphism onto the D summand of H0(S).

## 4. First-symbol naturality forces the D scalar to vanish

For any two-term family Q+tL its first Bockstein is the map from
ker Q to coker Q sending k to [Lk]. For the chain map above,

    b_S,a j^0 = j^1 b_T,a.                              (7)

This is immediate on representatives: j2x represents j^0[x], and
T_a j2x=j4T_a x; passing to the appropriate cokernels gives (7).
Thus it uses exact family commutation, not a guessed identification
of higher obstructions.

Since j^1=0 for every j and some j^0 surjects onto D, equation (7)
forces b_S,a to vanish on the whole D kernel for every a. PR965's
D channel is mu times a nonzero first-transvectant family. Therefore
mu=0. Its A channel remains the nonzero binary multiplication from
PR961. This proves (2) and excludes the nonzero-mu branch under the
current actual full-J hypotheses.

### Universal bundle consequence in the surviving scalar branch

On P(A), equation (2) has constant rank three: multiplication by every
nonzero binary quadratic is injective on A. Its entire kernel bundle is
D⊗O(-1), and its cokernel is a rank-two vector bundle E with presentation

    0→A⊗O(-1)→D⊗O→E→0.

Consequently c(E)=(1-H)^(-3), so c1(E)=3H and c2(E)=6H².
In particular there is no projective rank-drop locus for the internal
symbol in this full-J branch. This replaces, rather than coexists with,
the conditional nonzero-mu discriminant geometry when the present
hypotheses hold. It says nothing about surjectivity of the original map.

## 5. Exact factorization of the ORIGINAL second symbol

Let k∈H0(M)=H0(S). Original first-Bockstein vanishing guarantees a
first correction u∈N2 such that

    Qu=-T_a k.                                         (8)

Because T_a k∈Z, the quotient class ubar∈N2/U lies in ker Qbar=H0(T).
The connecting-map convention gives

    delta([ubar])=[Qu]=-[T_a k]=-b_S,a(k).              (9)

As delta is an isomorphism, [ubar]=-delta^(-1)b_S,a(k).
The canonical original second symbol is beta2_M,a(k)=[T_a u] in
H1(M). To check the normalization, the pinned original theorem uses
k=h xi and u0=-h zeta_a, with a xi=q0 zeta_a. Any u solving (8)
differs from u0 by an original kernel vector. Original first vanishing
makes [T_a(u-u0)]=0. Thus the class just used is EXACTLY the imported
canonical second Bockstein, independently of choices.

Projecting [T_a u] to H1(T) gives b_T,a([ubar]). Combining with (9)
proves (4), with its stated minus sign. This holds for the whole
original kernel A+D; on D it is zero because b_S,a|D=0. No assumption
about an unrelated Schur complement or higher gate enters the argument.

Since the original second symbol is a nonzero family on A, (4) implies
b_T is not the zero family. It is bilinear and G-equivariant in a and
the quotient D input. The decomposition

    A⊗D=Sym⁶W+Sym⁴W+Sym²W=V+P+D+A

contains P exactly once. Ordinary multiplication onto Sym⁶W, followed
by quotient by its unique V constituent, is a nonzero equivariant map
onto P. Hence it spans Hom_G(A⊗D,P), and the actual b_T is its nonzero
scalar multiple after fixed equivariant identifications. This proves
(5). The identifications of irreducible copies are scalar ambiguities;
they do not alter the projective directions in the original fixed A.

## 6. Exact transfer of the ten-direction quotient rank theorem

PR966 proves that the universal family s↦[a s] from Sym⁴W to
Sym⁶W/V6 has rank four except at one reduced orbit of ten directions,
with rank three there. The directions are the unordered fixed-point
pairs of the ten cyclic order-three subgroups of the projective
icosahedral group. They are nonsquares; every nonzero square has rank
four. Its Fitting-ideal calculation proves reducedness scheme-theoretically.

Because Section 5 identifies the WHOLE actual quotient first family
with this map by fixed invertible scalar identifications, it transports
both ranks and the determinantal scheme. This is not an inference
from a common source/target dimension or from a source2 occurrence.
No pure-V compatible radical is assumed in this Type II argument.

The known sextic geometry behind the universal family is not claimed
as a new curve. The new content here is its identification with this
actual Type II quotient obstruction and the radical-naturality
selection mu=0. The original full-J hypothesis remains unproved,
and no catalogue pair is removed.

## Verification

The verifier authenticates the inputs, checks the cohomology dimensions,
unique representation channels, and exact synthetic short-exact-complex
identities. A symbolic minimal model verifies (7), the obstruction to a
nonzero internal D scalar, and the minus sign in (4), including arbitrary
first-correction choices. Synthetic diagrams test linear-algebra
implications, not actual HM realizations or coefficients. The written
argument supplies the actual-chain and geometric input identifications.
