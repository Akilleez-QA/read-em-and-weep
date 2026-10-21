# A binary-quadratic injection lemma

Let U be two-dimensional and T finite-dimensional over C. Let N be a five-dimensional subspace of Sym^2(U) tensor T. Assume that no nonzero z in U tensor T satisfies U z contained in N. Then for a general q in Sym^2(U),

    N intersect (q tensor T)=0.

This is independent of HM geometry and the Banica–Manolache section theorem.

Proof. Evaluate N on P(U*) and saturate its image in T tensor O(2), obtaining a vector bundle E. Its splitting summands all have degree at most two, and h^0(E)>=5. If generic evaluation rank were at most two, rank one would be impossible and rank two would have splitting (2,1) or (2,2). In the first case N=H^0(E) contains Sym^2(U) tensor a for a nonzero constant a in T. In the second case E=E0 tensor O(2) for a constant two-dimensional E0, and N is a hyperplane in Sym^2(U) tensor E0. Requiring both xz and yz to belong to that hyperplane imposes at most two conditions on the four-dimensional U tensor E0. Either case produces a forbidden nonzero z. Thus generic evaluation kernels B_p have dimension b<=2.

If b=0, two generic kernels are disjoint. If b=1 and all pairs intersect, they are one common line, containing a nonzero polynomial vanishing at all p, impossible. If b=2 and all pairs intersect, choose distinct planes B_p,B_q meeting in L and spanning S of dimension three. Any plane meeting both contains L or is contained in S. Irreducibility of the parameter curve forces one of these alternatives for the whole generic family. A common L again forces a nonzero polynomial to vanish everywhere. Otherwise all B_p lie in S. Evaluation of S has rank at most one. Its saturated image is a line O(d) in T tensor O(2), so d<=2; the three independent global sections force d=2. Thus S=Sym^2(U) tensor a for a nonzero constant a, again yielding a forbidden common degree-one annihilator.

Hence two distinct points p,q have B_p intersect B_q=0. A vector-valued binary quadratic vanishing at both is divisible by the product of their linear equations. Thus N intersects that product tensor T trivially. Injectivity is open in the binary quadratic parameter space, proving the claim.

The lemma does not assert a good square. ABSTRACT-SQUARE-BOUNDARY.md gives a counterexample to that stronger conclusion with dim T=5.
