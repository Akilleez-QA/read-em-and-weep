# Exact nonnormality locus of the resolved cubic map: sixty intersection-kernel tests

Status: structural mathematical derivation. Independent mathematical review is recorded in REVIEW.md; not formally checked. Work over C. No selected actual HM/source coefficients, vectors, matrices, point evaluations, numerical ranks, searches, or computer algebra are used. The kernels below are intrinsic unevaluated constructions from the pinned actual linear syzygy. Their dimension is not chosen or calculated.

## 1. Inputs, notation, and result

Let S in P(A)=P4 be the actual integral primary surface, Z its thirty reduced transverse double points, and nu:X=S(5)->S its smooth normalization. Let

    pi:M=Bl_Z(P4)->P4,    Y=Bl_(nu^(-1)Z)(X) subset M,
    D=3H-E,              Phi:M->V subset P9,
    Phi_Y:Y->T subset V.

Here V and T carry their reduced image structures. The immutable dependencies are:

1. PR602 at 13647efe962d87c3344729e28c2a5e9ceeb0f2ba, research/hm/cubic-map-geometry/PROOF.md: the ten cubics c generate J=I_Z and form a basis of J_3; they generate D on M. The actual primary resolution has linear middle matrix L(x), of ranks 9 off S, 8 on S minus Z, and 6 at Z. The identity L(x)c(x)=0 defines B(y) by B(y)x=L(x)y. Incidence B(Phi(m))pi(m)=0 holds on M. Both cubic maps are birational, with deg(V)=51 and deg(T)=75. On the rank-four locus of B, its kernel defines a morphism q to P4 satisfying q Phi=pi. Every E_z=P3 maps by a linear embedding.
2. PR603 at c9d38741e6a4c4eb714f61abe62aafdd9bb9ba81, research/hm/no-node-trisecants/PROOF.md: no three nodes are collinear. Consequently Phi and Phi_Y are finite normalization morphisms, and D and D|Y are ample.
3. PR570 at e5e55594ef2b99cefb81c4c02b22cb45e1ff0025, research/hm/primary-surface-dictionary/PROOF.md, and PR574 at 3c92fdc469f6870520e7a9d905b5ab9199a5bf37, research/hm/primary-conductor/PROOF.md: the actual coordinate-copy dictionary gives H_X=nu*O_S(1)=I+2F on the modular surface, and transfers BHM's normalization geometry.
4. PR563 at 56c3c4c37bd51fc710eec4b80662c5506f357f8f, research/hm/rank-nine-line-transversality/KERNEL-SPLITTING.md: a distinguished line L is P(R), where R is the two-dimensional odd eigenspace for a stabilizing SL2(F5) complement. The Heisenberg translations carry this line to the twenty-five distinguished lines.

The primary source for modular geometry is Barth–Hulek–Moore, *Shioda's Modular Surface S(5) and the Horrocks–Mumford Bundle*, Sections 3.3, 4.2–4.5 and 5.2:

https://mathweb.tifr.res.in/Documents/Publications/Studies/Vector-Bundles-On-Algebraic-Varieties.pdf

Its twelve singular fibers are pentagons, each with five rational components; all other fibers are smooth elliptic curves. The divisor 5I is the sum of the twenty-five torsion sections. The map nu restricts to an isomorphism on each pentagon, pairing only the sixty vertices into thirty nodes. Proposition 13 identifies the torsion-section images with the HM lines; it does NOT classify all lines on S.

Write C for the set of sixty pentagon-component lines. Each ell in C has two distinct endpoint nodes z,w. Define the vector subspace and its projectivization

    K_ell=ker L(z) intersect ker L(w) subset C^10,
    Sigma_ell=P(K_ell),     Sigma=union_(ell in C) Sigma_ell,

with P(0)=empty. Changing representatives z,w or bases in the actual resolution changes no geometric assertion.

**Theorem.**

(a) S contains exactly eighty-five geometric lines: twenty-five node-free HM lines and sixty two-node pentagon-component lines. The cubic map embeds each HM line as a rational normal cubic, and embeds the strict transform of each component line as a projective line.

(b) For every ell in C, 0<=dim K_ell<=2 and Sigma_ell is contained in V. The nonempty Sigma_ell are pairwise disjoint.

(c) Phi restricts to an isomorphism

    M minus Phi^(-1)(Sigma) -> V minus Sigma.

The reduced nonnormal locus and the reduced singular locus of V are both exactly Sigma. Thus this is an exact failure locus, not only a containing set. In particular Phi_Y is an isomorphism over T minus Sigma, which is smooth.

(d) The normalizer acts transitively on C. Therefore dim K_ell is a constant r in {0,1,2}. Accordingly Sigma is either empty, sixty distinct points, or sixty pairwise disjoint projective lines. The cubic map Phi is a closed immersion, equivalently V is normal, if and only if r=0. This proof does not determine r.

The equalities in (c) concern underlying reduced closed subsets. No scheme structure or local analytic type of the singular locus is asserted. In particular the exact nonnormal locus of the surface T is not identified with T intersect Sigma.

## 2. The missing line classification

Let ell be any line in S and C_ell the reduced closure of nu^(-1)(ell minus Z). The map C_ell->ell is finite birational. Because ell is normal, it is an isomorphism: its finite affine algebra is integral over the normal affine algebra of ell and lies in the same function field. Hence C_ell is P1 and H_X.C_ell=1.

Put n=F.C_ell>=0. If n>0, then

    I.C_ell=1-2n<0.

Since 5I is the effective sum of the torsion sections, intersection positivity between distinct integral curves on the smooth surface X forces C_ell to be one of those sections. If n=0, C_ell lies in a fiber. It cannot equal a smooth elliptic fiber, so it is a component of one of the twelve pentagons.

Conversely the torsion sections map to the twenty-five distinguished lines, and the sixty pentagon components map to lines. Their images are all distinct, since nu is injective off the finite vertex set. The section lines avoid Z; every component line meets Z in exactly its two endpoint vertices. This proves the classification in (a). It is set-theoretic classification of geometric lines, not a claim that the Fano scheme is reduced.

For source locations, 5I and the fiber configuration occur in BHM Section 4.3, printed pp.58–59; the degree-one component restriction is explicit in Lemma 12, printed p.63; the pentagon embeddings and vertex pairing are Proposition 9, printed pp.63–64. Their identification with the actual ambient S uses input 3 rather than numerical agreement.

## 3. Cubic embeddings on all eighty-five lines

Fix a distinguished L=P(R) with stabilizer G=SL2(F5). The central involution has eigenvalue -1 on R. Since G is perfect, every one-dimensional representation is trivial. Complete reducibility therefore implies R is irreducible. Its projective A5 action on L is nontrivial, and hence faithful by simplicity of A5.

Every point stabilizer for a finite subgroup of PGL2(C) is cyclic. Indeed the derivative at its fixed point is faithful: a finite-order projective automorphism with derivative one there is the identity. Cyclic subgroup orders in A5 are at most five. Thus all A5 orbits in L have size at least twelve, and a nonzero invariant effective divisor has degree at least twelve.

We need no character-table evaluation to prove Sym^3(R*) irreducible. Its dimension is four and the central involution acts by -1, so it has no one-dimensional constituent. If it were reducible, it would contain a two-dimensional invariant subspace U of H0(L,O_L(3)). The base divisor of U is invariant and has degree at most three, hence is empty. The pencil gives an equivariant degree-three morphism L->P(U*). Its ramification divisor is invariant and has degree four by Riemann–Hurwitz, contradicting the orbit bound. Thus Sym^3(R*) is irreducible.

The restriction J_3->H0(L,O_L(3)) is equivariant. It is nonzero because the base scheme is exactly Z and L avoids Z. Its image is therefore the entire irreducible target. Consequently Phi|L is the complete cubic Veronese embedding in its linear span. Translation gives this result on all twenty-five lines.

For a pentagon-component line ell, the strict transform ell_tilde is P1 and D|ell_tilde=O_P1(1), since ell meets exactly two reduced nodes. The restricted sections generate this line bundle, so they span all its two-dimensional space of sections. Thus Phi|ell_tilde is a linear embedding. This completes (a).

## 4. All positive-dimensional incidence kernels are lines on S

For y in V set Lambda_y=P(ker B(y)). It is nonempty, by incidence and surjectivity of M->V. All 5-by-5 minors of B vanish on V, so its rank is at most four.

If Lambda_y has positive dimension and meets P4 minus S, PR602 Section 4 proves it is a line through three nodes: the cubics become proportional on the dense open Lambda_y minus S, and their common scalar cubic cuts out the reduced scheme Z intersect Lambda_y. The no-trisecant theorem excludes this. Consequently every positive-dimensional Lambda_y is contained in S.

It has dimension at most one. A projective plane contained in the integral surface S would equal S, contradicting degree fifteen; any larger linear space is impossible by dimension. Thus every positive-dimensional Lambda_y is exactly one of the eighty-five lines classified above. In particular every y in V has rank B(y) equal to three or four, never less.

Every point m of Phi^(-1)(y) has pi(m) in Lambda_y. If Lambda_y is a node-free HM line, the whole fiber lies on that line. If Lambda_y=ell is a pentagon-component line with endpoints z,w, the fiber is contained in

    ell_tilde union E_z union E_w.

These are necessary incidence restrictions; no assertion that every point of these sets is in the fiber is made.

## 5. Exact exceptional-image intersections

For a node z, incidence gives Phi(E_z) subset P(ker L(z)). The left side is a linearly embedded P3; the right side is P3 because rank L(z)=6. Hence they are equal:

    Phi(E_z)=P(ker L(z)).                                      (1)

Equivalently, the first jets of the cubic generators span the ambient maximal ideal modulo its square; Lc=0 puts their image in ker L(z), and both spaces have dimension four. Equation (1) needs no selected jet calculation.

Linearity of L gives

    K_ell=intersection_(x in ell) ker L(x)                      (2)

for any component line ell=zw. At a non-node point of ell the kernel of L has dimension two, so dim K_ell<=2. By (1),

    Sigma_ell=Phi(E_z) intersect Phi(E_w).                      (3)

Every nonempty Sigma_ell therefore lies in V. Every y in it has at least two distinct preimages, one in E_z and one in E_w, since distinct exceptional divisors are disjoint. Also (2) implies ell subset Lambda_y, and Section 4 implies equality Lambda_y=ell.

If y belonged to Sigma_ell and Sigma_ell' for distinct component lines, Lambda_y would contain two distinct lines. Their linear span has dimension at least two, contradicting Section 4. Thus the nonempty Sigma_ell are pairwise disjoint, proving (b).

## 6. Point and tangent separation outside Sigma

Let y in V minus Sigma.

### Rank four, including the ambient exceptional divisors

If rank B(y)=4, q is regular near y and q Phi=pi. Any two preimages of y have the same pi-image. Away from Z there is only one point over that image. Over a node they both belong to E_z, where Phi is a linear embedding. Thus the fiber has one geometric point m.

For v in T_m M with dPhi(v)=0, differentiation gives dpi(v)=0. Off E, pi is an isomorphism, so v=0. At E_z, ker dpi=T_m E_z. For clarity, on a universal blowup chart one has x_1=t, x_i=t u_i; at t=0 the differential sends (dt,du) to dt(1,u_2,u_3,u_4), so its kernel is exactly tangent to E_z. The linear embedding Phi|E_z then gives v=0. Thus dPhi is injective also at every exceptional point mapping to rank-four targets.

### Rank three on an HM line

Otherwise Lambda_y is a line on S. It cannot be a component line ell, because then L(z)y=L(w)y=0 at its endpoints and y would belong to Sigma_ell. Hence Lambda_y is a node-free HM line L. The fiber lies on L, so its cubic embedding from Section 3 makes that fiber a singleton.

Here pi is an isomorphism near the preimage m. Differentiate the incidence B(Phi(m))pi(m)=0. If dPhi(v)=0, its first-order term is B(y)dpi(v)=0, interpreted in projective tangent spaces. Precisely, using local vector representatives, the variation of y is a scalar multiple of y; its contribution vanishes because B(y)x=0. Thus dpi(v) is tangent to the linear kernel line Lambda_y=L. Since Phi|L is immersive, v=0.

We have proved both single-point fibers and injective differential at every preimage of V minus Sigma. This treats all exceptional points outside the explicitly retained locus, not only points away from E.

## 7. From separation to a genuine isomorphism, and exact failure

We record the elementary finite-morphism argument to avoid replacing tangent separation by a weaker statement. Let f:U->W be finite birational between integral complex varieties, and let a closed w have one preimage u with injective tangent map. Set A=O_(W,w) and B=(f_*O_U)_w. Since the fiber has one point, B is local, with residue field C. Tangent injectivity gives

    m_B/(m_A B+m_B^2)=0.

Nakayama over B implies m_B=m_A B. Thus B/m_A B=C, and A/m_A maps onto this quotient. The finite A-module B/A consequently equals m_A(B/A), so Nakayama over A gives B=A. Finiteness then makes f an isomorphism on a neighborhood of w, since the coherent cokernel of O_W->f_*O_U vanishes there.

Apply this to Phi over V minus Sigma using Section 6. It proves the isomorphism in (c). This open subset is smooth because M is smooth. Its closed subscheme T minus Sigma is isomorphic to Y minus Phi_Y^(-1)(Sigma), and is therefore smooth as well.

Conversely, every y in Sigma has at least two distinct normalization preimages by (3). A finite normalization is an isomorphism over the normal locus, so V is nonnormal at every such y. Nonnormal points are singular, since regular local rings are normal. There are no other singular points by the preceding smooth-open result. Thus both reduced loci are exactly Sigma.

## 8. A constant, unevaluated obstruction of dimension at most two

The normalizer preserves Z, its complete cubic system, and the associated morphism Phi. Therefore its action carries Phi(E_z) intersect Phi(E_w) to the corresponding intersection for the translated node pair. These intrinsic intersections suffice for equivariance; no choice of equivariant matrices is needed.

The normalizer acts transitively on the twelve singular fibers: BHM Section 3.3, Proposition 6 and its proof, printed pp.50–51, show the SL2(F5) action is transitive on the twelve cusp parameters. The Heisenberg translation quotient F5^2 preserves each fiber and acts transitively on its five components. For the latter statement, its action on the pentagon's dual graph has image in the rotation subgroup C5, and the image cannot be trivial because it acts transitively on the twenty-five torsion sections while each component meets exactly five. The section/component incidence is BHM Section 4.2. Thus the full normalizer is transitive on all sixty component lines.

By (3), dim K_ell is the same r for every ell. Section 5 bounds it by two. If r=0 all intersections are empty, and (c) makes Phi an isomorphism onto V, hence a closed immersion into P9. If r=1 the failure locus is sixty distinct points. If r=2 it is sixty pairwise disjoint projective lines. Either positive value prevents normality and an embedding by the explicit two-point fibers.

This proves (d). It leaves r entirely unevaluated, rather than replacing the unresolved intersection calculation by generic-position reasoning.

## 9. Contribution and boundary

The former finite-normalization statement is strengthened to an exact reduced singular/nonnormal locus and an isomorphism everywhere else, with all ambient exceptional divisors accounted for. The proof also corrects the incomplete twenty-five-line picture: there are precisely eighty-five lines on S. The remaining obstruction is sixty symmetric intersections of the actual exceptional image P3s, all with one common vector-space dimension r in {0,1,2}. No point, matrix, or coefficient test is performed to select its value.

The actual global embedding question is therefore equivalent to r=0. The surface image T is smooth off T intersect Sigma, but no exact failure locus for its normalization is claimed here. Local analytic singularity types, scheme-theoretic singular loci, the value of r, and the separate full-adjoint/higher-lifting/algebraicity problems remain open in this proof.
