> Publication scope: preserved mathematical proof/audit. Historical statements that rank eight remains open are superseded only after the final assembly and all its prerequisites. No source-instance evaluation or formal verification is claimed here.

# A finite third-Chern alternative for the conditional rank-eight branch

## Result

Assume the conditional rank-eight hypotheses and conclusions in `../rank-eight-singularity-chern/PROOF.md`: on X=P^4 over C, B is slope-stable, reflexive of rank two, c1(B)=0, c2(B)=5h², and c3(B)=10n h³ with n≥0. Put T=Ext²_X(B,O_X), whose support is finite.

Then

    0 ≤ c3(B) ≤ 30,     n ∈ {0,1,2,3}.

For a general hyperplane H, E=B|H is reflexive and slope-semistable. If E is slope-stable, then c3(B)≤22 and n∈{0,1,2}. If n=3, E is necessarily properly slope-semistable and fits into

    0 → O_H → E → I_{C/H} → 0,

where C is a plane quintic in H≅P³. In this case h⁰(E)=1, and E has a resolution

    0 → O_H(−6) → O_H ⊕ O_H(−1) ⊕ O_H(−5) → E → 0.

In particular n=3 forces a very specific general-hyperplane restriction. No stability of the restriction is silently assumed. This does not exclude rank eight, bound length(T), or prove n=3 realizable by the original B.

## 1. Restriction is genuinely reflexive

Choose H in the nonempty open set of hyperplanes avoiding Supp(T), containing no component of the at-most-one-dimensional singular locus of B, and satisfying the semistability restriction theorem in §2. Thus H meets Sing(B) in at most finitely many points.

A local equation l of H is a nonzerodivisor on B, since B is torsion-free. Consequently Tor¹_X(B,O_H)=0 and

    0 → B(−1) --l--> B → i_*E → 0

is exact. More generally, tensoring a local free resolution of B with O_H remains exact in positive degree: O_H has the two-term resolution defined by l, so all higher Tor vanish.

On a neighborhood of H, B has projective dimension at most one. Indeed the prior reflexivity calculation gives projective dimension at most two everywhere, and a nonzero degree-two term in a minimal free resolution would give nonzero Ext²(B,O); H avoids precisely that obstruction. Hence E has a free resolution of length at most one over every local ring of H.

Away from the finite set H∩Sing(B), E is locally free. At each exceptional closed point, the local ring of H is regular of dimension three, so Auslander–Buchsbaum yields depth(E_x)≥2. A torsion subsheaf of E would have finite support, since E is locally free off that finite set. Such a subsheaf contradicts positive depth at its support. Thus E is torsion-free and S₂, hence reflexive on smooth H.

The Tor vanishing also means the derived restriction is the ordinary restriction. Naturality of Chern classes, computed through finite locally free resolutions, gives

    c1(E)=0,   c2(E)=5,   c3(E)=c3(B)=10n.

Avoiding a finite set is essential: simply asserting that reflexive sheaves restrict reflexively to every hyperplane would be incorrect.

## 2. Flenner supplies slope-semistability, not stability

The projective-space hypersurface form of Flenner's restriction theorem says that a slope-semistable torsion-free sheaf of rank r on P^N restricts slope-semistably to a general degree-d hypersurface if

    binom(N+d,d) − d − 1 > d·max{(r²−1)/4,1}.

Here characteristic zero is understood. This is Flenner, Theorem 1.2, specialized to codimension one and deg(P^N)=1. Its precise projective-space formula is also stated in Brambilla, Theorem 1.3 in the published version, or Theorem 2.3 on p.2 of the directly read arXiv version; references and source-verification scope appear below.

For N=4, r=2, d=1, the inequality reads

    5−1−1 = 3 > max{3/4,1}=1.

B is stable and thus semistable, and it is torsion-free. Every hypothesis is satisfied. Therefore E is slope-semistable for general H. This theorem makes no claim that E is slope-stable or Gieseker-semistable.

## 3. The stable case

If E is slope-stable, it is Gieseker-stable. Write its character as

    ch(E)=(2,0,−5,c3(B)/2).

Schmidt, Theorem 1.1(ii)(e), gives, for Gieseker-semistable rank-two sheaves with character (2,0,d,e), d≤−4,

    e ≤ d²/2+d/2+1.

Putting d=−5 gives e≤11, hence c3(B)≤22. Combining with c3(B)=10n gives n≤2.

## 4. The properly slope-semistable case

If E is not slope-stable, choose a saturated rank-one subsheaf A of slope zero. Its quotient Q=E/A is torsion-free of rank one. A is reflexive: locally, the depth lemma applied to A→E→Q gives the S₂ condition on A, since E is reflexive and Q is torsion-free. A rank-one reflexive sheaf on P³ is a line bundle, and its zero slope forces A≅O_H. Also Q**≅O_H, by additivity of first Chern classes. Hence Q=I_Z for a subscheme Z⊂H of codimension at least two, and

    0 → O_H → E → I_Z → 0,
    ch(I_Z)=(1,0,−5,c3(B)/2).

The ideal sheaf I_Z is a rank-one torsion-free sheaf, so it is Gieseker-stable and in particular 2-Gieseker-semistable. Schmidt, Proposition 2.5, makes it tilt-semistable for β<0 and sufficiently large α. Proposition 2.18 of the same paper then applies: for rank-one character (1,0,−d,e), it gives

    e ≤ d(d+1)/2.

Thus c3(B)/2≤5·6/2=15, proving c3(B)≤30. This avoids any unstated reducedness, irreducibility, or connectedness assumption in a space-curve genus bound.

Combining the two cases proves n∈{0,1,2,3}.

## 5. Equality c3(B)=30

The stable case cannot reach 30. Equality in Schmidt's rank-one Proposition 2.18 says that I_Z is the ideal sheaf of a plane curve. Its degree, read from ch₂(I_Z), is five. Thus Z=C is a plane quintic as a scheme; no reducedness is asserted.

Its ideal has the complete-intersection resolution

    0 → O_H(−6) → O_H(−1)⊕O_H(−5) → I_C → 0.

Pull this extension back along O_H(−1)⊕O_H(−5)→I_C. The resulting extension by O_H splits, because H¹(O_H(1))=H¹(O_H(5))=0. Splicing yields the displayed resolution of E.

The first map has components of degrees 6,5,1 (in the displayed target order), with the degree-five and degree-one components defining C, up to signs. Reflexivity of E forces their simultaneous vanishing locus to have codimension at least three. It is nonempty: otherwise E would be locally free of rank two on P³ and would have c3=0. Thus its singularity scheme is a complete intersection of degrees 1,5,6, of length 30. Equivalently sheaf Ext¹_H(E,O_H) is O_D(6) for that complete intersection D, after choosing the resolution.

Finally H⁰(I_C)=0, since C is nonempty, so the extension gives h⁰(E)=1. Since stability gives H⁰(B)=0, the restriction sequence also implies the additional necessary condition

    dim ker[H¹(B(−1)) --l--> H¹(B)] = 1

for general l when n=3.

## 6. Verified sources and distinctions

1. H. Flenner, *Restrictions of semistable bundles on projective varieties*, Comment. Math. Helv. 59 (1984), 635–650, Theorem 1.2, p.637. Original digitized paper: https://www.e-periodica.ch/cntmng?pid=com-001%3A1984%3A59%3A%3A39 . The indexed original text verifies torsion-free semistable hypotheses and the general-complete-intersection conclusion. Direct retrieval encountered the repository's verification page; the formula was cross-checked in the published research source below rather than reconstructed from broken OCR.
2. M. C. Brambilla, *Semistability of Certain Bundles on a Quintic Calabi–Yau Threefold*, Rev. Mat. Complut. 22 (2009), 53–61, Theorem 1.3, p.55. https://www.mat.ucm.es/serv/revista/vol22-1/vol22-1c_p.pdf . Indexed published full text explicitly states the formula and its applicability to semistable sheaves. Additionally the original arXiv PDF was directly read: https://arxiv.org/pdf/math/0509599 , Theorem 2.3, p.2, which confirms exactly the same formula and sheaf hypothesis; its introduction explicitly defines semistability as slope-semistability. This is a research-paper statement of Flenner's theorem, not an independent proof of it.
3. B. Schmidt, *Rank two sheaves with maximal third Chern character in three-dimensional projective space*, arXiv:1811.11951v1, Theorem 1.1(ii)(e) (pp.1–2), Proposition 2.5 (p.4), Proposition 2.18 (p.7). Full PDF directly read: https://arxiv.org/pdf/1811.11951 . Crucially Theorem 1.1 says **Gieseker**-semistable; it cannot be applied directly to an arbitrary slope-semistable E. The properly slope-semistable case above instead applies the rank-one proposition to I_Z.

The genus interpretation in the equality case is consistent: χ(O_C)=1−6=−5 and ch₃(I_C)=2·5−χ(O_C)=15. A plane quintic extension is therefore precisely the numerical obstruction to inferring the bound22 from slope-semistability alone.

## Scope and remaining limitations

This proof uses the established conditional B, universal homological algebra, verified restriction and Chern-character theorems, and local symbolic deductions. No actual source object, operation, matrix, selected input, rank instance, jet, residue, or large computation was introduced. No claim that length(T) vanishes or that the singularity sheaf on P⁴ is pure is used. The earlier congruence c4≡15(n−1) mod30 and finite-point alternatives remain unchanged.
