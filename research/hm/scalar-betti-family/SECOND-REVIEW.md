# Independent second audit of the scalar Betti bridge

Reviewed artifact: PROOF.md, SHA256 e3547bbfaf38b386b592b882c4bfdd9889b7b18fc882e9b57c69b57f738b89d6. The final repository-ready proof was reread in full; its definitions, pinned dependencies and explicit preceding-zero justification agree with this audit.

Verdict: the exact sequence and entire necessary Betti family are mathematically valid conditional on the pinned inputs. This audit checked the local proofs for PR483, PR489 and PR491. It is not formal proof-assistant verification.

## Exact sequence

For P=S⊗W and L⊂P, freeness of P identifies L⊗_S P with a submodule of P⊗_S P. The defining quotient Sym²(P/L) is Sym²P modulo the products of L and P, so its relation module B is the image of L⊗W. The kernel of P⊗P→Sym²P is S⊗detW. Relative to a basis e₁,e₂, the second-factor coefficients of a(e₁⊗e₂−e₂⊗e₁) are −ae₂ and ae₁. Both lie in L exactly when a kills both generators of H, hence exactly when a lies in Ann(H). This proves the claimed kernel, including its determinant factor, without confusing the scalar ideal with L.

## Tor and representations

The presentations have degree-zero free covers, so positive Tor of L and B shifts homological index by one toward H and N, respectively. The degree-three map on minimal generators has source A⊗W′ and target zero or A⊗(W′⊕Qspin). Its rank is zero or ten by equivariance and irreducibility. This proves q=0 when r=0, and q=20 or 30 when r=15. Thus q=0 if and only if r=0.

In degree four, the preceding term Tor₂(L)₄⊗W=Tor₃(H)₄⊗W vanishes. The kernel of the map from the irreducible ten-dimensional Tor₁(I)₄ into the forty-dimensional Tor₂(H)₄⊗W is therefore Tor₃(N)₄ and has dimension zero or ten. Its cokernel has dimension 30+v; adjoining the fifteen-dimensional minimal quartic generator quotient gives dim Tor₂(N)₄=45+v.

In degree five the vanishing of (I/mI)₅ makes Tor₂(N)₅ a quotient of sW′. Since W′ is irreducible, its dimension is zero or two, bounded by 2s. The additional injection Tor₂(I)₅→sW′ is also valid: its preceding term is Tor₃(B)₅=Tor₄(N)₅, which duality identifies with Tor₁(R)₅*, zero by absence of quintic generators. This agrees with the explicit preceding-zero justification in the final proof.

## Support and grading

Pairing R_j with N_(5−j) in the five-variable Koszul complex complements homological index to five and internal degree to ten. Thus β_(i,d)(R)=β_(5−i,10−d)(N), not a complement to five in internal degree.

Minimality propagates the lowest relation degree three of R to degree i+2 at homological position i≥1. The lowest relation degree two of N propagates to j+1 at position j≥1. Applying the duality consequently restricts R's second module to degrees 4,5,6 and its third to 5,6,7. The complete quadratic/cubic presentation of N restricts the fourth module to 7,8. Level socle degree five and type three determine the fifth module as 3S(−10). These bounds account for every possible Betti entry.

The Hilbert numerator is 1−10t³−5t⁴+52t⁵−45t⁶−10t⁷+20t⁸−3t¹⁰. In the allowed support, its degree-five coefficient forces β₂,₅=52+u, its degree-six coefficient forces β₃,₆=45+v, and its degree-seven coefficient forces β₃,₇=10+q. Together with the known generators and degree-four syzygies, these are precisely the displayed family. Equal-degree adjacent summands do not contradict minimality, and no independent realization of parameter combinations follows.

No actual HM/source-instance evaluation, matrix rank evaluation, coefficient search, or large computation was used. The result concerns graded presentations and syzygies only; it makes no higher-order or algebraicity claim.
