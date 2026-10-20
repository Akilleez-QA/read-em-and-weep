> Publication scope: Coefficient-action-marked classical Hochschild comparison only; not the weaker unmarked ideal-action problem or module obstruction. Historical statements about unresolved mixed classes refer to the source stage; this packet does not supersede the separately stated conditional mixed-vanishing result in PR145.

# Vanishing of the full mixed ambient deformation complex

## Result and exact scope

Let

\[
X=\mathbf P^2_z\times\mathbf P^2_h,\qquad
L=\omega_{\mathbf P^2_z}\boxtimes\mathcal O,\quad
M=\mathcal O\boxtimes\omega_{\mathbf P^2_h},\quad
J=L\otimes M=\omega_X=\mathcal O(-3,-3).
\]

For the **classical** structure sheaf, with its symmetric coefficient bimodule (J),

\[
\boxed{HH^n(X,J):=\operatorname{Ext}^n_{X\times X}
(\Delta_*\mathcal O_X,\Delta_*J)
=0\quad(n\ne4),\qquad\dim HH^4(X,J)=9.}
\tag{1}
\]

In particular all of (HH^0,HH^1,HH^2,HH^3) vanish. This includes local-product, overlap-map, and scalar-gerbe directions, rather than merely the scalar groups (H^1(J)) and (H^2(J)).

Consequently a **coefficient-action-marked** bounded mixed algebroid lifting problem, precisely as defined in Section 3, has no remaining mixed ambient deformation classes, no relative 1-automorphism classes, and no relative 2-automorphisms. Its standard small-extension obstruction in (HH^3(X,J)) vanishes. These are statements about the relative 2-groupoid of mixed lifts, with the pure data and the indicated coefficient-action markings fixed.

Fixing only the two pure quotients, the associated coefficient lines, and the multiplication (L\otimes M\to J) is a weaker condition. That weaker problem can include changes of the action on the lifted pure coefficient ideals. We do **not** identify its deformation complex with (C^\bullet(\mathcal O_X,J)); see Section 6.

For the actual bounded ambient comparison in the neighboring proofs, both objects are supplied literal external products. Their comparison already follows by tensoring the marked pure equivalences. This proof supplies an additional structural rigidity statement in the controlled category; it is not needed to fill a gap in that external-product comparison. It makes no claim that a carrier module exists or that any module obstruction or retained physical value vanishes.

## 1. Sources and conventions

The following existing constructions were read:

- `premise:coarse-quantum-atlas/PROOF.md`, especially Sections 6 and 8: actual coefficient lines and the retained mixed ideal;
- `../external-morita-descent/PROOF.md`, especially Sections 4 and 6: the full coefficient square and its mixed square-zero extension;
- `premise:pure-downstairs-identification/PROOF.md`, Sections 8–9: marked pure equivalences and their actual external tensor product.

Primary structural references checked:

1. Amnon Yekutieli, [The Continuous Hochschild Cochain Complex of a Scheme](https://arxiv.org/abs/math/0111094): coefficient-valued Hochschild cochains compute the diagonal derived Hom, and the characteristic-zero HKR decomposition applies with coefficient modules.
2. [Stacks Project, Lemma 50.11.2](https://stacks.math.columbia.edu/tag/0FMG): cohomology of differential forms on projective space, proved from the Euler sequence and cohomology of line bundles.
3. [Stacks Project, Lemma 33.29.1](https://stacks.math.columbia.edu/tag/0BEC): coherent Künneth over a field.
4. Amnon Yekutieli, [Twisted Deformation Quantization of Algebraic Varieties](https://arxiv.org/html/0905.0488): differential associative deformations and their algebroid descent/inner 2-morphism framework.

All rings and varieties here are over \(\mathbf C\). Positive-arity cochains are normalized to vanish if any input is 1. Arity-zero cochains are retained. Coefficient-valued cochains are polydifferential in their classical function inputs. We use a finite affine cover with affine intersections, refined when necessary; the standard product cover suffices for the cohomology calculation. No formal-neighborhood-only effectivity assertion is used.

## 2. Calculation of every weighted Hochschild group

The coefficient HKR decomposition is

\[
HH^n(X,J)\cong\bigoplus_{p+q=n}
H^q(X,\Lambda^pT_X\otimes J).
\tag{2}
\]

For a rank-two vector bundle (V), contraction gives

\[
\Lambda^a V\otimes\det(V^*)\cong\Lambda^{2-a}V^*.
\]

Thus on each projective-plane factor

\[
\Lambda^aT_{\mathbf P^2}\otimes\omega_{\mathbf P^2}
\cong\Omega_{\mathbf P^2}^{2-a},\qquad 0\le a\le2.
\tag{3}
\]

The tangent splitting on the product gives

\[
\Lambda^pT_X\otimes J
\cong\bigoplus_{a+b=p}
\Omega_z^{2-a}\boxtimes\Omega_h^{2-b}.
\tag{4}
\]

The elementary projective-space cohomology formula is

\[
H^r(\mathbf P^2,\Omega^c)=
\begin{cases}\mathbf C,&r=c,\ 0,&r\ne c.\end{cases}
\tag{5}
\]

For (c=0) and (c=2), this follows from the cohomology of (mathcal O) and (mathcal O(-3)). For (c=1), the Euler sequence (0\to\Omega^1\to\mathcal O(-1)^3\to\mathcal O\to0), together with the total acyclicity of (mathcal O(-1)), gives the assertion directly.

Künneth now shows that the summand indexed by ((a,b)) in (4) has exactly one cohomology group, in degree

\[
q=(2-a)+(2-b)=4-p,
\]

and that group is one-dimensional. Every summand therefore has total Hochschild degree (p+q=4). The nine pairs (0\le a,b\le2) give nine dimensions. More explicitly, the only nonzero positions ((p,q)), with their dimensions, are

\[
(0,4):1,\quad(1,3):2,\quad(2,2):3,\quad
(3,1):2,\quad(4,0):1.
\tag{6}
\]

This proves (1).

There is also a proof that does not require a choice of global HKR splitting. The diagonal is a regular immersion, and its local Koszul resolution gives

\[
\mathcal Ext^p_{X\times X}(\Delta_*\mathcal O_X,\Delta_*J)
\cong\Delta_*(\Lambda^pT_X\otimes J).
\]

The local-to-global Ext spectral sequence has the groups in (6) on its (E_2) page. Every nonzero term lies on total degree 4, so every differential vanishes. Its abutment has the stated vanishing and dimension. This also checks the degree convention independently.

## 3. The exact mixed lifting category

### 3.1 Coefficient square

A bounded two-axis presentation has positive coefficient ideal (N=\mathfrak i+\mathfrak j), with

\[
\mathfrak i^2=\mathfrak j^2=0,\qquad
\mathfrak i\cap\mathfrak j=\mathfrak i\mathfrak j
=\mathfrak j\mathfrak i=J,\qquad NJ=JN=0.
\tag{7}
\]

Its reduction by (N) is the marked (mathcal O_X)-algebroid. The pure associated layers are (L=\mathfrak i/J) and (M=\mathfrak j/J); their cross product is the fixed line identification (L\otimes M\cong J). The reduction modulo (J) is the fixed fiber-product pure-axis algebroid, denoted \(\overline{\mathcal A}\).

The action of the full algebra on (J) is the ordinary left and right (mathcal O_X)-action. In particular (J) is central, even though (mathfrak i) and (mathfrak j) need not be central in the full mixed algebra.

### 3.2 Extra marking that is actually required

Choose compatible local additive presentations of the coefficient square. In addition to fixing \(\overline{\mathcal A}\) and (7), fix:

- every multiplication operation having at least one input in (N), including the (mathcal O)-lift actions on the pure coefficient layers;
- the restriction of every overlap map to (N), with the specified line transitions on (J);
- the classical reductions of chart maps and of triple composition units;
- the coefficient-compatible underlying presentations needed to compare these operations.

Only the (J)-valued correction to the product on two classical function inputs, the (J)-valued correction to overlap maps on classical inputs, and the (1+J) correction to triple units may vary. Relative chart gauges act as the identity on (N), induce the identity modulo (J), and have normalized polydifferential correction (mathcal O\to J). Relative edge gauges lie in (1+J).

All fixed coefficient-input operations must already satisfy their associative and descent identities. This hypothesis is necessary for the existence statement: modifying an (mathcal O)-input-only cochain cannot repair an independently defective coefficient action.

These conditions are a concrete, sufficient **coefficient-action marking**. In a local central-parameter model

\[
\mathcal O_U\otimes\mathbf C[s,t]/(s^2,t^2),
\]

with (s,t)-linear multiplication and fixed compatible parameter transport, the positive-input operations are forced from the pure operations. For example

\[
(sf)\star g=sfg+st\,\mu_h(f,g),\qquad
(tf)\star g=tfg+st\,\mu_z(f,g),
\]

whereas the unknown mixed operation occurs in (f\star g) as (st\,\mu_{zh}(f,g)). The multiplication of the pure coefficients is (sf\star tg=stfg). Compatible local parameter transports and their coefficient-input identities are part of the marking, rather than a consequence of merely naming the line bundles.

Literal external products satisfy this condition when their factor data are fixed. One must check it before applying the theorem to an independently supplied mixed presentation. The word “bigraded” alone is insufficient unless it includes these coefficient-linearity and transport requirements.

## 4. Exact linearization and relative 2-groupoid

Let \(C^q=C^q_{\rm diff}(\mathcal O_X,J)\), including \(C^0=J\), and form the unshifted Čech–Hochschild complex

\[
K^n=\bigoplus_{p+q=n}\check C^p(\mathcal U,C^q),
\qquad D=\delta+(-1)^p b.
\tag{8}
\]

Here (b) uses ordinary multiplication in (mathcal O_X) and the symmetric (mathcal O_X)-action on (J). In particular (b:C^0\to C^1) is zero. HKR and affine Čech descent give (H^n(K)=HH^n(X,J)).

### Differences of genuine lifts

Two marked genuine lifts have difference

\[
z=(u,v,a)\in
\check C^0 C^2\oplus\check C^1 C^1\oplus\check C^2 C^0=K^2.
\tag{9}
\]

The difference has this form because the extra marking forces product and overlap differences to vanish whenever a coefficient input is present. The triple-unit ratio is (1+a), with (a\in J).

Subtracting associativity, overlap multiplicativity, triple compatibility, and the pentagon gives

\[
Dz=(bu,\ \delta u-bv,\ \delta v+ba,\ \delta a)=0.
\tag{10}
\]

This is exact, not an approximation. A term containing two new corrections vanishes because (J^2=0). A new correction applied to a positive coefficient vanishes by the marking. Multiplying an output in (J) by a positive coefficient vanishes by (NJ=JN=0). Thus every surviving linear term uses only the classical product and the classical overlap action, which is precisely (8).

Conversely, adding any degree-two cocycle (z) to a genuine lift gives another genuine marked lift. Therefore the set of literal lifts, if nonempty, is an affine space under (Z^2(K)).

### Gauges and 2-morphisms

For (w=(e,c)\in\check C^0C^1\oplus\check C^1C^0=K^1), use chart maps (E_i=1+e_i) and edge units (B_{ij}=1+c_{ij}). Extend (e_i) by zero on (N). Then (e_i^2=0), (E_i^{-1}=1-e_i), and (B_{ij}^{-1}=1-c_{ij}). With the usual convention

\[
\mu_i'=E_i^{-1}\mu_i(E_i\cdot,E_i\cdot),\qquad
F_{ij}'=E_i^{-1}\operatorname{Ad}(B_{ij})F_{ij}E_j,
\]

and the correspondingly transported triple units, the difference is exactly

\[
Dw=(be,\ \delta e-bc,\ \delta c).
\tag{11}
\]

The term (bc) is zero for the symmetric coefficient bimodule, but its inclusion records the standard sign convention. Section 3's fixed coefficient operations remain fixed under these gauges: every possible extra term has a factor from (NJ) or is a correction with a coefficient input.

Chart units (1+r_i), (r\in K^0=\check C^0J), give the relative inner 2-morphisms. Their changes of gauge are (Dr=(br,\delta r)). Thus:

- equivalence classes of genuine marked mixed lifts form a torsor under (HH^2(X,J));
- relative 1-automorphisms modulo 2-isomorphism form (HH^1(X,J));
- relative 2-automorphisms of the identity form (HH^0(X,J)).

Equation (1) makes all three groups zero. Consequently any two objects in this nonempty marked lifting category are equivalent, and any two such equivalences are connected by a unique relative 2-isomorphism. This is uniqueness in the marked 2-groupoid, not uniqueness of literal formulas or of gauges before 2-isomorphism.

## 5. The bounded existence statement

Suppose the fixed lower data admit local preliminary mixed lifts as normalized differential operations and invertible overlap maps/triple units, with all coefficient-input identities already satisfied as in Section 3. The remaining defects of associativity and algebroid descent lie in

\[
K^3=\check C^0C^3\oplus\check C^1C^2
\oplus\check C^2C^1\oplus\check C^3C^0.
\]

The small-extension defect identities give a closed total cochain \(\kappa\in Z^3(K)\). Concretely these identities compare the parenthesizations of a fourfold product, compatibility of multiplication with composed overlap maps, and the successive coherence diagrams. After cancellation of their lower-order identities, every remaining term contains one (J)-defect. The same annihilation and coefficient-input argument used for (10) reduces these identities to (D\kappa=0). No nonlinear defect products survive.

Changing the preliminary operations by (z\in K^2) changes the defect by (Dz), with signs fixed as in (10). Since (HH^3(X,J)=0), choose (z\) with (Dz=-\kappa). This produces a genuine mixed lift. Its overlap maps and units remain invertible because their changes are square-zero and their reductions are invertible.

The cochains are actual regular differential cochains on an affine refinement: the complex (8) computes the cohomology in question. Thus the statement is about bounded algebroid presentations and ordinary descent, not isolated completed stalks. It is conditional on the stated local coefficient-compatible preliminary-lift setup. It does not say that arbitrary choices of coefficient transport or pure-ideal bimodule actions admit such a setup.

For the specific external-product category, existence is simpler: the external tensor product itself is an actual lift. Section 4 then proves its uniqueness within the indicated relative marked category without needing the obstruction construction.

## 6. Why bare bands and pure reductions do not justify this complex

Already locally, the extra action freedom is real. Put (R=\mathbf C[s,t]/(s^2,t^2)), and let \(\delta_\lambda\) be the derivation

\[
\delta_\lambda(s)=\lambda st,\qquad\delta_\lambda(t)=0.
\]

It is well defined because it preserves both defining square-zero relations. Form the Ore extension

\[
A_\lambda=R[x;\delta_\lambda],\qquad xr=rx+\delta_\lambda(r).
\tag{12}
\]

It is associative and has the usual normal form with basis (1,s,t,st) over \(\mathbf C[x]\) as a vector-space coefficient presentation. Its pure reductions are the same commutative dual-number algebras for every \(\lambda\), its mixed line is \(\mathbf C[x]st\), and its marked cross product is (s\cdot t=st). Nevertheless

\[
[x,s]=\lambda st.
\tag{13}
\]

The mixed ideal is central and annihilated by the positive coefficient ideal. A marked isomorphism inducing identity modulo (st) and fixing (st) cannot change \(\lambda\): its allowed changes of (x,s,t) are multiples of (st), all of which are central. In particular (13) survives them.

This freedom changes multiplication on a classical input and a pure coefficient input. It is excluded by Section 3 and is invisible in a cochain that only accepts classical inputs. This local example is not asserted to globalize to (\mathbf P^2\times\mathbf P^2); its role is to disprove the automatic identification of deformation complexes based only on the listed bands and quotient data.

In general a square-zero extension of \(\overline{\mathcal A}\) by (J) is controlled by Hochschild/derived extension data of \(\overline{\mathcal A}\), with whatever relative constraints are actually imposed. Replacing it by (HH(\mathcal O_X,J)) requires the factorization of all differences through classical inputs, proved here only using the extra coefficient-action marking. No claim about the unrestricted global extension problem follows from (1) alone.

## 7. Relation to the actual ambient and to the module obstruction

The actual coarse ambient has the coefficient square (7) by the supplied coarse construction. The independently corrected bounded model and the actual bounded model are both literal external products under their pinned source premises. Section 9 of `premise:pure-downstairs-identification/PROOF.md` tensors the exact, coefficient-preserving pure equivalences. This already identifies the full mixed ambients while retaining the (st) term. The present theorem says that there is no further ambient tuning **within the coefficient-action-marked mixed category** once these pure data and coefficient operations are fixed. It is not needed to infer externality from pure classes, and it does not infer externality for arbitrary mixed models.

The module obstruction for a fixed vector bundle (E) lies in a different group, typically

\[
\operatorname{Ext}^2_X(E,E\otimes J)
=H^2(X,\operatorname{End}(E)\otimes J)
\]

for locally free (E). Nothing in (1) makes this group zero. As an elementary illustration of the distinction, (E=\mathcal O_X\oplus\mathcal O_X(3,0)) has an endomorphism summand yielding \(H^2(X,\mathcal O(0,-3))\cong\mathbf C\). This example concerns only the coefficient groups, not an evaluated obstruction.

Accordingly all carrier-lifting, equivariance-existence, actual module-obstruction, and thirty retained-value questions stay separate. There is no assertion about same-pair second order, higher orders, or all-order rigidity. No physical operation, matrix, detector, retained value, source mutation, or large computation was performed.
