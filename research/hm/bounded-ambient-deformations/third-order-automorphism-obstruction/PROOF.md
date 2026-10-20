# Universal order-three algebra-homomorphism and inner-gluing conditions

## Scope and sources

This is a formal coefficient calculation over a characteristic-zero field. It does not evaluate the source's particular derivation cochain, functions, module residual, ranks, or detector values. No conclusion that its particular T is Poisson is asserted.

Pinned public mathematical source:
https://github.com/Akilleez-QA/read-em-and-weep/blob/c8aec970fd65a105f39f4e8aeb8a17f0f0053f89/research/hm/second-order-algebroid.md

Its sections 1 and 3 prescribe a commutative scalar classical algebra, normalized μ1(f,g)={f,g}/2, the same restricted Moyal algebra on every cover member, F_ij=id+h²T_ij modulo h³, and δT={b,−}. Its descent orientation is F_ij F_jk=Ad_star(A_ijk) F_ik. Matrix-valued products elsewhere in the note are not the classical algebra used in the symmetry argument below.

The complementary public comment, also part of the public mathematical record, takes A=exp(hb)+h³c modulo h⁴ and establishes the separate scalar unit equation δc=Ψ in existence:
https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6259198993

Here exp(hb) means the ordinary exponential, with coefficients 1,b,b²/2,b³/6. All equalities below are modulo h⁴ unless specified.

## 1. Exact fixed-product criterion

Let R be commutative and let an associative normalized star product be

f star g = fg + h μ1(f,g) + h² μ2(f,g) + h³ μ3(f,g),

where μ1(f,g)={f,g}/2. Let F=id+h²T+h³S be coefficient-linear and unital. Define the classical Hochschild differential by

(d_H U)(f,g)=f U(g)-U(fg)+U(f)g.

Define

(L_T μ1)(f,g)=T(μ1(f,g))-μ1(Tf,g)-μ1(f,Tg).

Expanding the two sides of F(f star g)=F(f) star F(g) gives:

- Left h² coefficient: μ2(f,g)+T(fg).
- Right h² coefficient: μ2(f,g)+(Tf)g+f(Tg).
- Left h³ coefficient: μ3(f,g)+T(μ1(f,g))+S(fg).
- Right h³ coefficient: μ3(f,g)+μ1(Tf,g)+μ1(f,Tg)+(Sf)g+f(Sg).

Consequently the exact necessary and sufficient equations are

(1) d_H T=0,
(2) d_H S=L_T μ1.

No coefficient of μ2 or μ3 remains in these equations. This independence holds for any single fixed normalized associative extension, not only Moyal.

For EVERY linear map S on a commutative R, d_H S is symmetric in f,g. For EVERY linear map T, L_T μ1 is antisymmetric because μ1 is. Hence (2), in characteristic zero, forces both sides to vanish. Equation (1) makes T a derivation, and then L_T μ1=0 is precisely

T{f,g}={Tf,g}+{f,Tg},

or L_T π=0 in the geometric setting. Conversely, these conditions make all coefficients agree.

**Fixed-product theorem.** F=id+h²T+h³S is an algebra automorphism modulo h⁴ if and only if T is an ordinary derivation preserving the Poisson bracket and S is an ordinary derivation. Its inverse is id−h²T−h³S modulo h⁴. Derivations annihilate 1, so these conditions also supply unitality.

In particular, choosing a more general third-order operator S cannot repair failure of Poisson preservation by the fixed T. No HKR theorem or quotient by coboundaries is needed: the symmetry separation is an equality of cochains.

## 2. What changes if local products differ?

This is a qualification, not the pinned source's presentation. Let F_ij map (R,star_j) to (R,star_i), with common μ0 and common μ1, but μ2^i, μ3^i possibly distinct. Put Δμr=μr^j−μr^i. Direct expansion gives

d_H T_ij=Δμ2,
d_H S_ij=Δμ3+L_{T_ij} μ1.

If the fixed second-order product is retained, Δμ2=0 and T remains an ordinary derivation. Write Alt(B)(f,g)=(B(f,g)−B(g,f))/2. The order-three antisymmetric constraint is

Alt(Δμ3)+L_T μ1=0,

or, with μ1=π/2, L_T π=−2 Alt(Δμ3). The remaining symmetric constraint is d_H S=Sym(Δμ3); solving that is an additional requirement. Thus T need not preserve π when DIFFERENT third-order products are allowed: their antisymmetric discrepancy may compensate it. Merely changing a common μ3 on every chart cannot help, since Δμ3 then vanishes. Associativity, normalization, regularity, and compatibility of the changed local products must still be checked; these equations alone do not construct such products.

If μ2 differs as well, T need not even be an ordinary derivation. Calling L_T π a vector-field Lie derivative in that case would be unjustified; the displayed operator expression remains valid.

If μ1 differs, the ansatz F=id+O(h²) already fails the h coefficient unless those first-order products agree after the classical overlap identification.

## 3. Inner gluing at the next order

Work first with one fixed normalized star product. Put

A=1+hb+h²a+h³d,
C2(b,f)=μ2(b,f)−μ2(f,b).

Commutativity of μ0 and normalization give

[A,f]_star=h²{b,f}+h³(C2(b,f)+{a,f}).

Since A^{-1}=1−hb+O(h²), the identity

Ad_star(A)(f)−f=[A,f]_star star A^{-1}

gives

Ad_star(A)(f)=f+h²{b,f}+h³(C2(b,f)+{a,f}−b{b,f}).

There are no extra first-order product terms against 1, by normalization. The coefficient d is absent because its first possible commutator occurs at h⁴.

For the specified a=b²/2, the Poisson Leibniz rule yields {a,f}=b{b,f}. Hence

Ad_star(exp(hb)+h³c)=id+h²{b,−}+h³C2(b,−).

Also F_ij F_jk=id+h²(T_ij+T_jk)+h³(S_ij+S_jk), since products of the h² corrections start at h⁴. Therefore the specified descent orientation gives precisely

δT={b,−},
δS=C2(b,−).

This fixes the sign: (δS)_ijk=S_ij+S_jk−S_ik. No c appears in this inner-gluing equation.

For the pinned Moyal μ2,

μ2(f,g)=(1/8)Σ π^{ij}π^{kℓ}(V_i V_k f)(V_j V_ℓ g),

interchanging f,g and renaming i↔j and k↔ℓ contributes two minus signs and leaves the scalar expression unchanged. Thus μ2 is symmetric and C2=0. The next inner equation is δS=0.

**Conditional combined consequence.** If every specified T_ij preserves π, then S=0 satisfies both the algebra-homomorphism and inner-gluing equations through h³ for the fixed Moyal extension. Combining this with a regular solution c to the separately established unit equation gives the scalar ambient descent identities modulo h⁴. Under the regular, unital, normalized hypotheses and the public comment’s existence result for c, this gives an exact conditional criterion: the fixed displayed scalar two-jet extends through h³ with the same Moyal products if and only if every specified T_ij is Poisson. Necessity is the fixed-product theorem; sufficiency is S=0 and such a c. This does not evaluate or prove that missing property for the actual T, and is neither an all-orders nor a module result.

For varying local products, conjugation on the right uses the target algebra star_i and its μ2^i. With common μ1 and the same A two-jet, the inner formula becomes δS=C2^i(b,−). Changing only μ3 leaves this inner equation unchanged at this order. The homomorphism qualifications of section 2 still apply.

## 4. Closedness is weaker than vanishing

For an ordinary derivation-valued cochain T, define D_ij=L_{T_ij}π. Since π is a global Poisson bivector and δT={b,−},

δD=L_{δT}π=L_{{b,−}}π=0,

by the Jacobi identity. This only says that the Poisson-preservation defect is a closed Čech 1-cochain of bivectors. It does not show D_ij=0 on any overlap, or that it can be removed while preserving the prescribed presentation. Even vanishing of its Čech cohomology class alone would not prove the fixed-product theorem's pointwise condition for the specified T.

## Audit boundary

All deductions are universal coefficient expansions and use only the source's declared conventions. No actual T_ij or source function has been differentiated or evaluated.  The open task is to assess the specified T under separately established source-model hypotheses, or to establish a permitted replacement presentation with its own full compatibility proof.
