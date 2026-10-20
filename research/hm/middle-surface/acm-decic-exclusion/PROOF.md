# No ACM invariant decic surface

## Statement

Over C, let H be the order-125 Heisenberg group, let Z=Z(H), and let A=H/Z be F5^2. Let N normalize H, with its conjugation action on A containing SL2(F5) in the standard representation. Let S=C[x0,...,x4], with S1 the irreducible five-dimensional H representation of primitive central character. Suppose Y in P4 is an integral N-invariant surface of degree 10. Then Y is **not arithmetically Cohen–Macaulay**.

This statement does not need sectional genus 11, any rank-locus hypothesis, smoothness, normality, or local Cohen–Macaulayness. It applies in particular to the hypothetical decic of /research/hm/middle-surface/decic-middle-surface-constraints/PROOF.md. The proof concerns its saturated homogeneous prime ideal I and its homogeneous coordinate ring R=S/I. Invariance means the linear normalizer acts on this ideal; scalar lifts make no difference to the argument.

## 1. Representation facts, including conventions

Choose the generator z of Z so that it acts on S1 by a primitive fifth root zeta. It acts on Sd, and therefore Id, by zeta^d. The sign of the original projective-coordinate convention is immaterial: replacing zeta by its inverse changes every exponent consistently.

For each nontrivial central character, H has exactly one irreducible representation with that central character, and its dimension is five. One elementary verification uses generators u,v,z with u^5=v^5=z^5=1 and uv=zvu: in a representation with z acting by a nontrivial fifth root, v carries a u-eigenspace cyclically through all five distinct u-eigenvalues. Choosing a vector and its five translates gives the unique clock-and-shift irreducible representation; semisimplicity gives the general decomposition. Thus every H module of a fixed nontrivial central character has dimension divisible by five.

A representation with trivial central action factors through the abelian group A and splits into character spaces. For an N-stable such module, multiplicities of characters are constant on the SL2(F5) orbits. There are two orbits in A^*: the trivial character and all 24 nontrivial characters. Consequently any such N module of dimension less than 24 is A-trivial.

In particular, if G is a five-dimensional H module of central character zeta^4, then G is irreducible and isomorphic to (S1)^*. Hence

    dim (G tensor S1)^A = dim (G tensor S1)^H = 1.

The first equality holds because the tensor product has trivial central action; the second is Schur's lemma. No extension of an H-module isomorphism to N is needed.

## 2. There are no equations of degree at most three

First I1=0: the linear span of Y is H-stable, and irreducibility of S1 forces every proper H-stable projective linear subspace to be empty. Equivalently, I1 is either zero or all of S1, the latter being impossible.

Suppose d in {2,3} is the smallest degree of a nonzero element of I. Then dim Id is a positive multiple of five. Choose independent f,g in Id. They have no common nonconstant factor. Indeed, if q=gcd(f,g) has positive degree, its degree is less than d (independence excludes degree d). Minimality implies q is not in I. Since I is prime and f=q f', this forces f' into I, contradicting its degree less than d.

Thus f,g are a regular sequence in the polynomial ring and their projective intersection is a pure two-dimensional complete intersection of degree d^2. The integral surface Y is one of its components, so degree Y is at most d^2. But 10>9>=d^2. This contradiction proves

    I1=I2=I3=0.

This is a prime-ideal argument; merely asserting that two arbitrary cubics are coprime would be insufficient.

## 3. The ACM hypothesis forces the entire graded resolution

Assume R is Cohen–Macaulay. Its Krull dimension is three. Choose a general sequence of three linear forms ell1,ell2,ell3 that is R-regular. Write

    B=R/(ell1,ell2,ell3)R,    T=S/(ell1,ell2,ell3)=C[u,v].

Then B is an Artinian quotient of T, its length is deg Y=10, and its Hilbert series is the h-polynomial of R. Since I has no elements below degree four, the defining ideal of B in T also has no elements below degree four. Therefore

    dim B0=1, dim B1=2, dim B2=3, dim B3=4.

These already sum to ten. All higher graded pieces vanish. It follows that

    B=T/(u,v)^4,
    h_R(t)=1+2t+3t^2+4t^3,
    Hilb_R(t)=(1+2t+3t^2+4t^3)/(1-t)^3.

The minimal resolution of T/(u,v)^4 is explicit: its five degree-four generators are u^4,u^3v,u^2v^2,uv^3,v^4; the four adjacent relations are v e_i-u e_(i+1). These generate all relations (for instance, eliminate the coefficients successively starting with the first monomial). Thus

    0 -> T(-5)^4 -> T(-4)^5 -> T -> B -> 0.

Tensoring a minimal graded S-free resolution of R with T remains exact because the three linear forms are R-regular: the Koszul complex on them computes Tor^S(R,T), which vanishes in positive degrees. Minimality is preserved, since all matrix entries remain in the homogeneous maximal ideal or become zero. Consequently the minimal graded Betti numbers of R and B agree. The minimal S-resolution is therefore

    0 -> S(-5)^4 -> S(-4)^5 -> S -> R -> 0,

or, equivalently,

    0 -> S(-5)^4 -> S(-4)^5 -> I -> 0.

Sheafifying gives the claimed resolution by four O(-5)'s and five O(-4)'s. This derivation avoids any assumption about the canonical class or singularities, and proves that no alternative h-vector or additional high-degree generators are possible.

As an independent numerical check,

    (1-t)^2(1+2t+3t^2+4t^3)=1-5t^4+4t^5.

The Hilbert polynomial obtained from the displayed Hilbert series is

    P_Y(n)=sum_(i=0)^3 (i+1) binom(n-i+2,2)
          =5n^2-5n+5.

Thus the ACM hypothesis itself forces sectional genus 11 and chi(O_Y)=5, consistently with the inherited Hilbert congruences.

## 4. The linear syzygies contradict the normalizer action

Put G=I4. The resolution gives dim G=5 and says that I is generated by G. Define the degree-five linear syzygy space intrinsically by

    W=ker(G tensor S1 -> I5),

where the map is multiplication. This definition makes W N-stable without requiring any choice of equivariant resolution. The same resolution gives dim W=4.

The center acts on G with character zeta^4 and on S1 with character zeta. It therefore acts trivially on W. W factors through A, and its N-stability makes its character multiplicities SL2(F5)-invariant. Since dim W=4<24, Section 1 shows that A acts trivially on W. Hence

    W is contained in (G tensor S1)^A.

But G is the unique five-dimensional irreducible H module of central character zeta^4, so the latter invariant space has dimension one. This would give 4=dim W<=1, a contradiction.

This proves the theorem.

## 5. Precise deficiency consequence and limits

For every hypothetical Y in the statement, there is an integer t such that at least one of

    H^1(P4,I_Y(t)),    H^2(P4,I_Y(t))

is nonzero. This is the standard cohomological ACM criterion for a surface. More explicitly, I is saturated, so H^0_m(R)=0 and H^1_m(R) is the graded module measuring the failure of R_t -> H^0(Y,O_Y(t)) to be surjective. The next local-cohomology module has graded pieces H^1(Y,O_Y(t)). Vanishing of these two modules is equivalent to depth R=3. The ideal-sheaf sequence identifies them with the two displayed groups, respectively.

Thus the conclusion is an actual necessary cohomological deficiency, not a conclusion that Y must have a non-Cohen–Macaulay local singularity: a locally Cohen–Macaulay, even smooth, projective surface can fail to be ACM. The argument does not specify t, choose which deficiency group is nonzero, prove a numerical lower bound for its total length, or exclude the remaining non-ACM genus-eleven case.

Each displayed cohomology group inherits the N action and the degree-t central character. Consequently any nonzero such group has dimension at least five when 5 does not divide t. When 5 divides t, the A-nontrivial character spaces, if any, occur in a complete orbit of 24 equal multiplicities; a smaller group can be A-trivial. These are representation restrictions, not assertions that a particular degree is nonzero.

## References and verification

The argument above supplies the two-variable resolution and representation calculations directly. Standard general codimension-two context is the Hilbert–Burch theorem, stated in Robin Hartshorne's *Deformation Theory* notes, Theorem 8.1 and its graded projective version Theorem 8.8 (Section 8, Cohen–Macaulay in Codimension Two). Proposition 8.7 explicitly gives the cohomological ACM criterion used in Section 5; see printed pages 49–50 (PDF pages 55–56):

https://math.berkeley.edu/~robin/math274root.pdf

The full resolution here is established by Artinian reduction rather than inferred from the theorem alone. All original hypotheses and the conditional rank-locus application are recorded in /research/hm/middle-surface/decic-middle-surface-constraints/PROOF.md.
