# Simple surface fibers admit joint formal quantization with the prescribed ambient two-jet

## Result

Yes, under the stated genuine-bundle and genuine-ambient-two-jet hypotheses, every good surface fiber admits a locally free rank-two formal module over a jointly chosen formal differential algebroid, preserving the supplied ambient coefficients through order two literally. The first-order module obstruction vanishes by the trace/Chern-class calculation; a deck-equivariant first-order lift then has zero obstruction at order two for this **fixed** ambient two-jet. Beyond order two, permitted new scalar gerbe coefficients cancel every module obstruction, while diagonal inversion removes the ambient extension obstruction.

Full factor-swap equivariance is unnecessary. It is preferable to omit it: the shorter Alexander–Whitney cocycle q1 cup q2 is swap-odd only in cohomology on an ordinary nerve, not necessarily as a literal cochain. The deck subgroup alone proves the result without changing that representative or its two-jet.

The theorem is fiberwise, not a theorem over the whole parameter base, not a fixed all-order Moyal theorem, and not an evaluation or vanishing proof of the thirty retained global obstruction coordinates.

## 1. Precise premises and notation

Let Y=C×C be a good fiber in the supplied surface report. Let F=N_Y tensor p*E_h be the actual locally free rank-two bundle, with E_h a stable plane restriction, so F is simple. Assume the geometric identification with this bundle, rather than merely a numerical identification of a complex. Write theta=c1(N_Y). Then

    c1(F)=0,    c2(F)=15 theta².

Let H=(Z/2)² act by the two elliptic deck involutions, and let chi(epsilon1,epsilon2)=epsilon1 epsilon2. Put pi=V1 wedge V2 and Pi=(1/2) i_pi(theta²). The deformation parameter transforms by h -> chi(g) h.

Use exactly the supplied ambient two-jet, restricted to this pair:

    mu = ordinary multiplication + h mu1 + h² mu2,
    mu1(f,g)=(1/2) pi(df,dg),
    F_ij=id+h² T_ij,
    A_ijk=1+h b_ijk+(h²/2)b_ijk²,
    b=(15/4) q1 cup q2,
    T=(15/4)[(a1 cup q2)V2+(q1 cup a2)V1].

The source proves that these are genuine ambient descent data modulo h³. Their cohomological scalar class is [b]=-15 Pi. All conclusions preserve this actual chosen representative and its actual T through order two, not only their cohomology classes.

The normalized polydifferential ambient complex includes arity zero, and its cohomology is identified by HKR with HH. Use an acyclic refinement if required for module frames and coherent Čech cohomology; the supplied ambient operations are restricted, never changed. Literal preservation refers to these restrictions as well. No claim is made that an arbitrary coarse cover trivializes F.

## 2. Genuine deck equivariance and scalar Ext²

The morphism p:C² -> Sym²(P¹) is H-invariant, so p*E_h has the canonical genuine H-linearization. The root line is the exterior product of O_C(infinity) on the two varying factors, up to a fixed one-dimensional factor. The divisor infinity is fixed by elliptic inversion. The action on rational functions gives O_C(infinity) its genuine divisor-induced linearization; tensor products give one on N_Y and hence F. No assumption that an invariant isomorphism class automatically linearizes is used. On End(F) the line action cancels canonically.

Simplicity and Serre duality on the abelian surface imply H²(End_0 F)=0. Consequently scalar inclusion is an isomorphism

    s:H²(O_Y) -> Ext²(F,F),    a -> a Id_F.

Trace is also an isomorphism, with tr composed with s equal to multiplication by 2. Both maps are H-equivariant. Künneth identifies H²(O_Y)=H¹(O_C) tensor H¹(O_C); each deck involution acts by minus one on its own H¹. Therefore Ext²(F,F) has the one-dimensional character chi.

This proves the character without forgetting the equivariant canonical-bundle character in Serre duality. The inner factor swap, if included, acts by minus one on H²(O_Y), but is not needed below.

## 3. First-order cancellation, including the factor of two

In the source's normalized HKR and row-module convention, the characteristic class of the bivector is

    ev_F(pi)=(1/2) i_pi At(F)²,

and the arity-zero/gerbe contribution is -[b] Id_F. The trace identity ch2(F)=(1/2)tr At(F)² therefore gives

    tr ev_F(pi) = i_pi ch2(F)
                 = -i_pi c2(F)
                 = -15 i_pi(theta²)
                 = -30 Pi.

Since every Ext² class is scalar and tr(a Id_F)=2a, this implies

    ev_F(pi)=-15 Pi Id_F=[b] Id_F.

Thus the first-order obstruction ev_F(pi)-[b]Id_F is zero. This is an equality of cohomology classes, which is precisely what is needed to solve the linear first-order transition equation. It is not an assertion that a displayed cocycle vanishes identically.

Only the trace version of the characteristic formula is needed here. It can also be checked universally from the first-order normalized defect

    g_ik^(-1) mu1(g_jk,g_ij) - b_ijk Id_F.

Substitute mu1=(1/2)pi(d-,d-), use dg_ik=d(g_jk g_ij), and move factors cyclically under trace. The differential-of-transition representatives of At(F) then give (1/2)i_pi tr At(F)², with the same total Čech–forms minus sign as the source's line calculation. This is a formal transition/trace identity for an arbitrary bundle, not an evaluation of any physical matrix. Thus one may use this trace identity directly, rather than requiring any independent source-level claim that ev itself was already evaluated. The source's line-bundle calculation fixes its sign and the 1/2 normalization. In particular there is no extra rank-two factor in tr ev; the rank enters only when recovering the scalar coefficient from trace. The coefficient 15/4 follows from Pi=-(1/4)[q1 cup q2].

## 4. Why the frozen order-two module test now vanishes

The deck action satisfies, as literal cochains/operators,

    g(q_r)=epsilon_r q_r,    g(V_r)=epsilon_r V_r,    g(a_r)=a_r.

Hence b and pi have character chi; T and mu2 are invariant. With h of character chi, every term of the supplied ambient two-jet is H-invariant. This uses no interchange of Čech factors.

The first-order module lifting equation is linear. Its zero obstruction admits an H-equivariant solution by exactness of invariants in characteristic zero, using the genuine classical linearization of F and the parameter-weighted action. This does not mean averaging full nonlinear modules. Equivalently, equivariant small-extension obstruction theory is ordinary Ext obstruction theory followed by H-invariants: the group-cohomology terms vanish by the finite-group averaging contraction. If frames require refinement, use a group-saturated affine refinement with free H-labeled copies of cover members and transport the classical frames using the coherent linearization. This makes coefficientwise equivariant lifts available. The finite-group averaging argument applies to the linear correction; there is no new group-cohomology obstruction. The ambient lemma and HKR comparison remain valid on this acyclic refinement.

Fix this equivariant first-order module. Apply the supplied module small-extension lemma to the fixed ambient extension modulo h³. Its obstruction belongs to

    (Ext²(F,F) tensor span(h²))^H.

But h² has trivial character and Ext² has nontrivial character chi. The displayed invariant space is zero. Hence the module lifts through order two, preserving the ambient two-jet **without any change**. A solution may again be chosen equivariantly by averaging the linear correction.

This is the missing frozen-two-jet argument in this simple-fiber setting. An arbitrary nonequivariant first-order module choice need not satisfy this argument; the theorem selects an equivariant one.

## 5. All-order joint induction

Suppose an H-equivariant joint ambient/module lift is given modulo h^n, where n>=3. Seek its coefficient of h^n, leaving all previous coefficients unchanged.

### Ambient extension

The ambient obstruction lies in

    (HH³(Y) tensor span(h^n))^H.

Let d=(-1,-1) in H be diagonal inversion. Since chi(d)=+1, d fixes h and every h^n. HKR gives

    HH³(Y)=direct_sum_(p+q=3) H^q(Y, wedge^p T_Y).

Diagonal inversion acts on each summand by (-1)^(p+q)=-1. Thus the invariant obstruction space is zero at every n. The literal ambient lifting lemma produces an H-equivariant genuine ambient extension. All new mu, overlap-map, and triple-unit coefficients are allowed to vary at this stage.

### Module extension and its permitted cancellation

For that genuine ambient extension, the module obstruction is

    c in (Ext²(F,F) tensor span(h^n))^H.

Changing only the new triple-unit coefficient by a scalar Čech 2-cocycle a changes the obstruction by -[a] Id_F, by the explicit characteristic-map lemma. Such (0,0,a) is a closed ambient correction: delta a=0, and its Hochschild differential is zero because the classical algebra is commutative. Therefore adding it preserves **all** ambient descent equations at this small-extension order. It does not require a compensating change of product or overlap map at the same order.

Scalar inclusion H²(O_Y)->Ext²(F,F) is an equivariant isomorphism, so choose [a] with [a] Id_F=c, with the required parameter-weighted character. Represent it by an equivariant cocycle using averaging. Then the corrected obstruction c-[a]Id_F is zero. Solve the module equation, averaging its linear solution to retain equivariance.

For clarity, when n is even the invariant module-obstruction space is already zero; when n is odd it is one-dimensional and the permitted scalar gerbe correction is surjective onto it. After such a correction, the next ambient extension remains unobstructed by the same diagonal-inversion argument. No all-order centrality of the newly chosen gerbe coefficients is presumed: only their small-extension linear effect is used.

Inductively this gives compatible lifts at every order. Their h-adic inverse limit is the required formal differential algebroid with locally free module, retaining the supplied ambient two-jet and the selected equivariant module two-jet literally.

## 6. A useful refinement about a chosen module two-jet

Once *any genuine module two-jet* over this ambient two-jet has been selected, the all-order **existence** argument can preserve it even if it is not H-equivariant. Retain only diagonal inversion on the ambient data. Ambient extension is still unobstructed. Diagonal inversion acts trivially on H²(O_Y), so every scalar cohomology class has a diagonal-invariant representative, and scalar inclusion is onto Ext². Thus the obstruction of the possibly nonequivariant lower module can still be canceled by a diagonal-invariant scalar gerbe correction. The module itself need not be equivariant; the ambient data can remain diagonal-invariant throughout. This proves formal extension preserving an arbitrary already-existing module two-jet. It does not prove that every arbitrary first-order module extends to that two-jet.

## 7. Scope, caveats, and evidence

- Full pair-permutation equivariance is available only if its literal action on the supplied presentation is actually verified. Ordinary AW representatives require care; replacing b by an antisymmetrization would change the prescribed two-jet and is unnecessary here.
- No change at order >=3 can repair a failed order-two test. The proof above solves that test first by deck equivariance on a simple fiber.
- The higher ambient coefficients are not frozen. In particular this does not keep all higher products Moyal or keep all higher overlap maps zero.
- This is a theorem on each good fiber. Relative/global gluing in the parameter base and compatibility between two different pair directions are separate questions.
- The actual bundle/simplicity and actual source two-jet are inputs. No replacement of the physical object by its Euler characteristic is made.
- No physical source or jet values are evaluated in this argument. All thirty retained global values remain unknown.

Inputs: supplied relative-surface report (simplicity and c2); supplied module-lifting report (actual Ext² obstruction and -a Id characteristic map); supplied literal ambient descent lemma (HH³ obstruction and invariant lifting); supplied source second-order-algebroid note §§1–5 (Moyal normalization, b/T coefficients, and row/gerbe sign); supplied deck-character report §2 (divisor-induced line linearization).
