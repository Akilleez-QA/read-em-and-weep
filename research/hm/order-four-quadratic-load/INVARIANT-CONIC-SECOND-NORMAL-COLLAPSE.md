# Actual representation and second-normal collapse at the invariant conic

## Theorem

Let F be normalized HM on P4. Write its ambient normalizer representation as V_5=V directsum V_-, where inversion is positive on the three-space V and negative on the two-space V_-. Put R=P(V), W=V_-*, A=H1(F_R), D=H0(F_R(2)), and B_R=End_0(F_R). Let C0 be the unique A5-invariant conic in R. The established fixed-plane and conic theorems give the actual stable Steiner resolution

       0 -> A tensor O_R(-3) -> D tensor O_R(-2) -> F_R -> 0

and show that C0 is smooth and F_C0=O_P1(-1)^2.

The following stronger representation and infinitesimal statements hold:

1. A is the irreducible A5 three-space different from V. Moreover Sym^2 W=A.
2. The actual coefficient representation H0(B_C0) is A, not V. The underlying bundle B_C0 is trivial, but its linearization is not a trivial three-dimensional representation.
3. The actual projective extension class eta_C0 of End(F_R) on the doubled plane conic is zero. Consequently H0(B_R|2C0)=A has dimension three.
4. The restriction zeta_C0 of the ambient second-normal class is also zero. Thus the actual affine law gives

       xi(q_-)=zeta_C0-eta_C0 tensor q_-=0

   for every negative quadratic block q_- over this positive conic, including every nondegenerate block defining a smooth even quadric.
5. H0(B_R(1))=0 and H1(B_R(1))=V directsum A. In particular H1(B_R(-4)) has dimension six, and multiplication by q0 squared has an exact three-dimensional kernel A.

This rules out the invariant conic as a witness for a noncommuting second-normal class. It does not show that the corresponding classes vanish for general conics. Projective splitting of the endomorphism algebra is not splitting of the geometric conic neighborhood: its conormal extension remains nonzero.

## 1. The actual central weight

Use the actual normalizer N=H5 semidirect G, G=SL2(F5). Choose the central generator z so that it acts by a primitive fifth root zeta on the ambient five-space. Its action on O(1) is then zeta inverse.

The actual four-space U=H0(F(3)) is Heisenberg-trivial. Evaluation is generically onto F(3), so z acts trivially on F(3) and hence acts by zeta cubed on F. Therefore the five-dimensional group H1(F) has Heisenberg central weight three relative to the ambient weight one. It is the unique irreducible Schrödinger module of that weight, since the nontrivial-center irreducible Heisenberg modules have dimension five.

These are genuine normalizer actions. Two extensions of a fixed irreducible Heisenberg module to the chosen semidirect product differ by a character of G, and G is perfect, so there is no character ambiguity.

The primary inputs here are the normalizer construction in Horrocks--Mumford Section 1 and its Heisenberg-trivial section representation in equation (4.12). The normalized monad gives h1(F)=5, F(-1) acyclic, and H^i(F(-2))=0 except h2=2. No selected bundle coefficient enters these representation statements.

## 2. A universal character calculation fixes both three-spaces

For completeness, consider the abstract weight-a Schrödinger representation of H5, extended to G. In its universal function model on F5, the intertwiner of a transvection is, up to a scalar c,

       f(x) -> zeta^(a b x^2) f(x),

where b is a fixed nonzero element of F5 determined by the transvection convention. The same b is used for every weight a. There is no unknown phase: the transvection has order five, giving c^5=1. Conjugating it by the diagonal element whose square is 4 sends it to its fourth power; the corresponding permutation of the function variable sends the displayed diagonal operator to its fourth power. Consequently c=c^4, so c^3=1 and c=1.

Central inversion acts by reflection f(x)->f(-x), not its negative. Covariance determines it up to a scalar lambda with lambda^2=1. Reflection on five functions has determinant one. Since the determinant of a G representation is a character and G is perfect, lambda^5=1 as well; hence lambda=1.

Its positive three-space has transvection trace

       1 + zeta^(a b) + zeta^(-a b),

and its negative two-space has trace zeta^(a b)+zeta^(-a b). Multiplication of a by the nonsquare 3 interchanges the two possible positive traces. They are the two roots phi and phi' of x^2-x-1, and distinguish the two irreducible three-dimensional A5 representations. This is a universal character calculation, not an evaluation of an HM presentation.

The plane Koszul resolution and the negative-twist cohomology in Section 1 give an equivariant exact sequence

       0 -> H2(F(-2)) tensor wedge^2 W -> H1(F) -> H1(F_R) -> 0.

The action on F_R is inversion-even: the actual U evaluates onto F_R(3), inversion acts trivially on U, and O_R(1) has positive inversion character. Thus A=H1(F_R) is the positive three-dimensional constituent of the weight-three Schrödinger module. The ambient V is the positive constituent of weight one. Therefore A and V are the different three-dimensional irreducibles.

For the ambient negative two-space, put e=zeta^b+zeta^(-b). Then e^2+e-1=0, the trace on V is 1+e, and the trace on Sym^2 W is e^2-1=-e. The last value is the other three-dimensional character. Sym^2 W is irreducible: W is an irreducible determinant-one binary two-space, whose symmetric square has no invariant vector, while A5 has no nontrivial two-dimensional representation. Hence Sym^2 W=A.

## 3. The actual adjoint representation on C0

Let T be the determinant-one binary two-space parametrizing C0=P(T), so Sym^2 T=V. Write the equivariant balanced splitting as

       F_C0=O_P1(-1) tensor S.

Here S is a two-dimensional representation of the binary group G, with central inversion negative, since F_C0 itself is inversion-even. It is irreducible, because G has no nontrivial one-dimensional characters.

The conic restriction sequence and acyclicity of F_R(1) give

       H0(F_C0(1)) = H1(F_R(-1)).

The Steiner resolution identifies the latter group with the kernel of the onto coefficient map A tensor V -> D. The surjectivity of this coefficient map was proved in the actual conic-pencil theorem. Now A and V are different, so

       A tensor V=4 directsum 5,  D=5,
       H0(F_C0(1))=4.

The ambient twist (1) has degree two on C0, and hence this same representation is S tensor T*. Thus S tensor T=4, using self-duality of determinant-one two-spaces.

It follows that End_0(S)=Sym^2 S is the other three-dimensional representation A. One can check the identification without guessing a binary character label: on an order-five element the character of 4 is -1, so chi_S chi_T=-1. Therefore

       chi_(Sym^2 S) = chi_T^(-2)-1.

Since chi_T^2-1 is either phi or phi', the displayed value is the other root. Sym^2 S is irreducible by the same invariant-form argument as for Sym^2 W. This proves

       H0(B_C0)=End_0(S)=A.

Serre duality on the conic also gives H1(O_C0(-2))=V; the twist here is the plane twist, so O_C0(-2)=O_P1(-4). All genuine A5 linearizations used in these identifications are unique up to the trivial character.

## 4. Both actual extension classes vanish

The doubled-conic projective extension class is canonical and normalizer-equivariant. It therefore belongs to

       eta_C0 in (A tensor V)^A5=0.

This uses the actual class, not an arbitrary representative or merely a dimension comparison. The comparison-torsor description then identifies End(F_R)|2C0 with the constant evaluation matrix algebra on the doubled conic. Its trace-free global sections are exactly A: the ideal of C0 in 2C0 is O_P1(-4), which has no sections, and H0(O_2C0)=C. Hence h0(B_R|2C0)=3.

The ambient class zeta is defined using the canonical normalizer-equivariant projection of the complement of P(V_-) onto R. Its restriction is an actual invariant tensor

       zeta_C0 in (H0(B_C0) tensor H1(O_C0(-2)) tensor Sym^2 W)^A5
                  = (A tensor V tensor A)^A5.

But A tensor A=1 directsum A directsum 5 contains no V. Thus this invariant space is zero, and zeta_C0=0.

The actual affine law now proves xi(q_-)=0 for all blocks q_-. The 15-to-63 top-factor commutator map therefore vanishes for these quadrics. This does not imply that top-order jets extend to global adjoint sections, nor that subsequent boundary maps vanish.

## 5. A coefficient-free exact six-dimensional square gate

The symmetric-square resolution of the actual Steiner presentation gives

       0 -> wedge^2 A tensor O_R(-4)
         -> A tensor D tensor O_R(-3)
         -> Sym^2 D tensor O_R(-2)
         -> B_R(1) -> 0.

Its cohomology identifies H0(B_R(1)) and H1(B_R(1)) with the kernel and cokernel, respectively, of

       phi:wedge^2 A tensor V -> A tensor D.

Let t:A tensor V->D denote the actual coefficient tensor. Then phi is induced by

       (a wedge b) tensor v |-> a tensor t(b,v)-b tensor t(a,v).

Choose a volume on A, identifying wedge^2 A with A*. A kernel tensor is a map T0:A->V satisfying

       t(a,T0(b))=t(b,T0(a)) for all a,b in A.

Every nonzero such T0 is invertible. Indeed, if b is a nonzero kernel vector, choose a with T0(a) nonzero. The relation says t(b,T0(a))=0, contradicting the injectivity of the Steiner fiber map A->D at the point [T0(a)] of R.

A complex linear space of three-by-three maps whose nonzero elements are all invertible has dimension at most one: two independent invertible maps give a pencil with a nonzero singular member by the degree-three determinant polynomial. Thus ker(phi) has dimension at most one. It is invariant under A5, whereas

       wedge^2 A tensor V = A tensor V = 4 directsum 5

has no invariant line. Hence phi is injective. The tensor decomposition A tensor D=V directsum A directsum 4 directsum 5 now gives

       H0(B_R(1))=0,  H1(B_R(1))=V directsum A.

Serre duality and B_R*=B_R yield H1(B_R(-4))=V directsum A. Finally stability gives H0(B_R)=H0(B_R(-4))=0, so the exact sequence

       0 -> B_R(-4) --q0^2--> B_R -> B_R|2C0 -> 0

identifies the kernel of q0 squared on H1 with the just-proved H0(B_R|2C0)=A. The actual source has dimension six and the actual special kernel has dimension three. This calculation is a proof using fiber injectivity, not an evaluated rank test.

## Remaining generic-conic interface

For any balanced smooth conic C, the same restriction sequence identifies H0(B_R|2C) with the kernel of q_C squared from the fixed six-dimensional H1(B_R(-4)) to H1(B_R). Its vanishing is equivalent to the coefficients of the actual eta_C spanning at least two dimensions in sl2. That generic nonvanishing question is not settled by this note.

The invariant conic is now proved to be a special failure of this test, rather than an available witness. Semicontinuity does not transfer its three-dimensional kernel to a general conic, and the reduced conic-pencil isomorphism does not determine this squared adjoint multiplication. A proof that one actual nonsymmetric conic has injective squared multiplication, or an independent structural proof about the conormal Atiyah class, is still required.

## Sources and exact interfaces

- Horrocks--Mumford, *A rank 2 vector bundle on P4 with 15,000 symmetries*, Sections 1 and 4 and the appendix: https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf . The proof above computes the needed relative characters universally and does not import a chosen HM matrix.
- ACTUAL-CONIC-DISCRIMINANT-AND-JUMP-STRATA.md at 313c54bec3f2556518dd531a8ce71f7a8ce22461 supplies the stable Steiner presentation, irreducibility of A and D, coefficient-map surjectivity, and balance on C0.
- LOWER-TWIST-EVEN-QUADRIC-PARITY.md, Section 2, at 028320f238a8a8cae5f14faf6b6836201baa496d supplies the normalized-monad negative cohomology. The short Koszul argument above only needs the underlying cohomology, not an assumed sign for its multiplicity representation.
- ACTUAL-SECOND-NORMAL-AFFINE-LAW.md at 028320f238a8a8cae5f14faf6b6836201baa496d (blob 890d8882942886ba975c44eec5f875a354c9f9a7) supplies the canonical actual torsors, their equivariance and restriction, and xi=zeta_C-eta_C tensor q_-.

No selected HM coefficients, actual matrix or rank evaluations, scans, or experiments are used. No global full-adjoint gate or complete proof repair is asserted.
