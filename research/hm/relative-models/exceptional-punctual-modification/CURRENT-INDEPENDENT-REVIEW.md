# Current independent mathematical review: punctual quotient and Leray transgression

Verdict: PASS conditional on the explicitly additional hypothesis that T has finite support, including the empty case. CURRENT-REVIEW-BINDING.json binds the complete normalized proof, historical audit and dependency register reviewed here.

## Verified structural argument

1. At codimension-one DVRs, Ext1(D,O)=0 eliminates torsion. Any remaining torsion would have finite support, whereas projective dimension at most one over the regular local surface gives positive depth and excludes a finite-length submodule. Thus D is torsion-free.
2. The canonical inclusion into its reflexive hull gives 0→D→F→Q_exc→0, where F=D**=V* is locally free and Q_exc has finite length. Grade-two vanishings identify T with sheaf Ext2(Q_exc,ω). Finite-length duality preserves stalkwise length and support. Global Serre duality identifies H0(T)=H0(Q_exc)* and H2(E)=H0(F)*.
3. Relative duality has exactly the shift Rs_*K=RHom(D,ω)[−1]. Dualizing the modification and rotating gives the canonical truncation triangle E[−1]→Rs_*K→T[−2]→E. Its connecting map is the derived dual of F→Q_exc up to the conventional rotation sign.
4. Naturality of global Serre duality consequently identifies the actual Leray d2 with the dual of H0(F)→H0(Q_exc), not merely a map of the same rank. Its kernel is the dual evaluation cokernel. The displayed global Ext and modification-cohomology exact sequences agree, including the left injection and final zero.
5. Only the numerical section imports h0(D)=44 and h2(K)=62. It correctly deduces r=h0(F)−44, h2(E)=44+r and h1(E)=62−length(T)+r, with 0≤r≤length(T) and length(T)−r≤62. None determines the length or evaluation rank.

## Dependencies, novelty and limits

PR247 at 01c96a7e1b24685eacd5d1dc52ed0ea026490146 supplies the two-term pushforward, projective-dimension, locally free dual and relative-duality inputs. Its rigidity corollary supplies only the additional numerical input. Those exact public texts were checked. The predecessor leaves d2 abstract; the canonical quotient and natural map identification are the distinct structural contribution here.

The PR116 exceptional-fiber theorem and its supplementary alternative proof are context, not additional premises and not evidence of finite support. Exceptional curves require the divisorial framework instead. The result concerns the full fixed-projection recipient; block exchange changes projections, so it does not identify a retained thirty-dimensional subspace termwise. No quotient entries, length, rank, locus nonemptiness or specified source value are evaluated or established.
