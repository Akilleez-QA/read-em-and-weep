# Complete polynomial systems remove coefficient graphs in a constant ambient bundle

## Scope and hypotheses

Work over C on P1. Let H and V be finite-dimensional constant vector spaces, let pi:H->V be surjective, and put R=ker(pi). Let e>=0 and dim(V)=e+1. Let j:L=O(-e)->V tensor O be a complete polynomial system: its coefficient map

    c_j:H0(O(e))* -> V

is an isomorphism. In particular j is a saturated rational-normal line inclusion. Let E be a saturated subbundle of H tensor O. Assume its actual projection factors as j q, with q:E->L surjective, and assume q has a bundle section s:L->E. Put Ehat=ker(q).

These hypotheses include an actual ambient inclusion and a complete coefficient map; an abstract Birkhoff splitting alone is NOT the conclusion or a replacement for these hypotheses.

## Theorem 1: actual constant-ambient splitting

There is a constant subspace V1 of H, of dimension e+1, such that pi|V1 is an isomorphism onto V, H=R direct-sum V1, and the actual inclusion of E decomposes as

    E = Ehat direct-sum s(L) inside (R tensor O) direct-sum (V1 tensor O).

Ehat is saturated in R tensor O. The line s(L) is a complete degree-e polynomial system in V1. The complement V1 depends naturally on the chosen section s, not canonically on q alone.

Proof. Compose s with the actual inclusion into H tensor O and take its coefficient map c_s:H0(O(e))*->H. We have pi c_s=c_j. Thus c_s is injective, its image V1 has dimension e+1, and pi maps V1 isomorphically to V. It follows that H=R direct-sum V1. The image of s is in V1 tensor O by the definition of a coefficient span. Since q s=id, the identity x=(x-sq(x))+sq(x) gives the bundle direct sum E=Ehat direct-sum s(L). The projection of Ehat to V is zero, so Ehat lies in R tensor O. This proves the asserted equality as actual embedded subbundles.

The quotient decomposes as

    (H tensor O)/E = ((R tensor O)/Ehat) direct-sum ((V1 tensor O)/s(L)).

The left side is locally free by saturation. Both right summands are therefore locally free; in particular Ehat is saturated. Completeness of s(L) in V1 follows because c_s maps isomorphically onto V1. QED.

Equivalently, choose any preliminary constant splitting H=R direct-sum V. Write s=(g,j). Since c_j is invertible, there is a unique constant map phi:V->R with c_g=phi c_j. Hence g=phi j and V1 is the graph of phi. The constant shear (r,v) |-> (r-phi(v),v) removes the entire graph. This statement concerns all degree-e graph coefficients simultaneously, not coefficients at selected points.

Completeness is necessary. For e=2 take j=(x^2,y^2) into a two-dimensional V, and g=xy into R=C. This j is basepoint-free, but g is not a constant linear combination of its coordinates. Its lifted coefficient span has dimension three and is not a complement of R projecting isomorphically to V. Basepoint-freeness by itself does not imply the theorem.

## Naturality, symmetry and choices

The construction c_s and its image commutes with constant ambient isomorphisms and compatible isomorphisms of the parameter line and line bundle. With a finite group G acting on all the data, an equivariant section s makes c_s equivariant, hence V1 and the resulting splitting equivariant. If q is G-equivariant and admits any bundle section, average that section by |G|^{-1} sum_g g s g^{-1}; its composite with q remains the identity. Thus an equivariant section exists whenever the extension splits non-equivariantly. No canonical choice is asserted.

Sections of q form an affine space under Hom(L,Ehat). Different sections can give different constant complements. This does not affect existence of a constant-ambient splitting. The theorem does not make arbitrary other Birkhoff summands horizontal.

## Theorem 2: second fundamental forms split

Write beta_F:F->((H tensor O)/F) tensor Omega1 for the actual second fundamental form of a subbundle. The constant ambient direct sum of Theorem 1 commutes with differentiation. Consequently

    beta_E = beta_Ehat direct-sum beta_L,
    E^- = Ehat^- direct-sum ker(beta_L).

Here beta_L is computed in V1 tensor O, beta_Ehat in R tensor O, and the equality is an equality of actual maps after the displayed constant identifications. The quotient and target splittings come from Theorem 1, not from an assumed horizontal Birkhoff decomposition.

For e>0 the rational-normal map is immersive, so beta_L is nonzero on every fiber and has zero kernel. For example on the x!=0 chart its coordinates may be normalized to (1,t,...,t^e); the first two coordinates of the value and derivative have determinant 1. On y!=0 reverse the coordinates. Thus

    generic rank(beta_E)=1+generic rank(beta_Ehat),
    E/E^- = L direct-sum (Ehat/Ehat^-).

These identities hold equivariantly when the input data and chosen section do. For e=0 the line is constant and its derivative rank is zero instead. If E spans H as a constant space, Ehat spans R: its constant span plus V1 is the span of E, and the sum is direct. No assertion of a derivative-rank bound on Ehat^- follows without an additional hypothesis.

## Conditional height-seven handoff, not a profile exclusion

This paragraph describes exactly how the universal theorem would apply once the actual equality setup is provided. It does NOT establish profile-(1,1) coverage or its quotient/degree identities. PR1138, at c69f97aaf00e116e3a8abebf19a8e02868c4f7c4, Sections 2--4 supplies the relevant general equality argument in its own profile-(2,1) setting. PR1142 at df2fd3d35dac577d7f1e1c4d51fe68b1fcc824ad explicitly leaves the O(-8)+O(2)+O(16) profile-(1,1) shape open. The actual profile-(1,1) equality and its next endpoint application remain Mr. Slop's work, as stated in PR1 comment 6375020455.

Assume, in the original rank-30 constant ambient H, the actual D-type source

    E=D O(-2)+(W'+T)O(-3)+V_rep O(-4)+O(-8),

and assume S=Q* contains the full degree-eight rational-normal line's seventh osculating subbundle in a genuine constant V0=Sym8 W inside H*. Assume H0(S)=0. The osculating bundle is Sym7 W O(-1), and its apolar annihilator in V0* tensor O is a complete line L=O(-8). Therefore the projection pi:H->V0* restricts on E through L. This map cannot be zero: otherwise V0 tensor O lies in S, contrary to H0(S)=0. All source summands other than the unique O(-8) have degrees greater than -8, so their maps to L vanish; the remaining scalar map O(-8)->O(-8) is nonzero and hence an isomorphism. Thus q is surjective and has a section. The kernel Ehat has the exact remaining type

    Ehat=D O(-2)+(W'+T)O(-3)+V_rep O(-4),
    rank(Ehat)=16, degree(Ehat)=-46.

Theorem 1 provides an actual constant ambient decomposition into dimensions 21+9. Theorem 2 reduces generic rank three to generic rank two for Ehat. If additionally the actual derivative quotient is A_q=O(-8)+O(2)+O(16), then

    Ehat/Ehat^- = O(2)+O(16).

This last identification uses uniqueness/cancellation of equivariant splitting types on P1: the direct-sum identity already supplies the actual O(-8) summand. It does not identify a preferred originally written projection A_q->O(-8).

For clarity about recovering completeness: IF the actual height-seven equality chain has the same B=O(6)+O(-4)+O(-18), rank endpoint 10 and degree -38 as in PR1138, and height partition (7,3), its equality-of-determinants argument gives the final line C=O(-8) with eight independent successive derivative directions. The exact representation Sym8 W=P+D has dimensions 4+5, so every proper equivariant quotient has dimension at most 5. A coefficient image of dimension at least eight is therefore the full nine-dimensional system. Saturation extends the seventh osculating containment everywhere. This argument does not use top(S)<=-2. The weaker H0(S)=0 is enough for the nonzero-projection step above.

The missing bridge for an unconditional profile-(1,1) conclusion is the actual profile-(1,1) equality setup and its subsequent residual exclusion, not the complete-system shear. This note proves neither bridge, asserts no contradiction for the rank-two core, and does not import profile-(2,1)'s stronger top bound. It supplies a reusable horizontal decomposition lemma for the owner of that application.

## Evidence and limits

verify.py checks formal coefficient identities over Q[a_ri,t], universal block shear/inverse/derivative identities, rational-normal immersion on both charts, and the incomplete-system negative control. No actual source coefficient, parameter, point, jet, matrix, instance-rank experiment, historical enumeration, or stopped experiment is used. These algebraic checks support, but do not replace, the bundle proof. The original proof repair remains open.
