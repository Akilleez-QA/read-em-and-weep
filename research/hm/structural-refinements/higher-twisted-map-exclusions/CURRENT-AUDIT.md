# Current independent mathematical review

Independent mathematical review, 20 October 2026. This is a check of the written derivation and the stated immediate prerequisites, not a formal verification certificate. Earlier audits are treated as historical evidence, not as a substitute for this review.

Reviewed PROOF.md SHA256: 978deeedef0688991a5304a6fcf50fdc206ad58bbbae3f67c23aa9afabf149bb

Reviewed Git blob SHA1: 2996b13c361253107b3885d30859b20120a71dd8

## Verdict and scope

PASS for the nonzero-map implications at k=2,3,4 under the stated bundle-section and Chern-class inputs. In the actual normalized bundle, the separate twist-two vanishing makes the k=2 nonzero branch vacuous. Neither k=3 nor k=4 vanishing is proved or imported by this review.

## Checks

- A saturated rank-one subsheaf of a vector bundle on the smooth base is reflexive by the depth lemma. Thus the kernel and saturated image of a generic-rank-one map are O(a),O(b). The section input gives a<=-3, b<=k-3, while the induced nonzero map requires H0(O(a+b+1)) nonzero, contradicting a+b+1<=k-5<0. Cayley-Hamilton excludes zero and square determinants.
- The roots of End0(F) are 0, alpha-beta, beta-alpha, giving c2=15H^2 and c3(End0(F)(k))=(k^3+15k)H^3. Nonzero c3 forces a zero; the three-generator height bound forces every zero component to have dimension at least one. Locally q=a^2+bc and its Jacobian ideal is contained in (a,b,c), with the correct scheme-inclusion direction.
- The spectral algebra is finite flat of degree two and integral. The base regular parameters form an M-regular parameter sequence, so its rank-one module is MCM. A nonzero trace-free 2-by-2 matrix has a cyclic vector, proving local freeness away from the zero locus. At a zero, the residue module has dimension two, proving nonfreeness. This gives the set-theoretic nonfree locus, not an identification of nonfree scheme structures.
- On a normal cover M is reflexive, and local factoriality would make it free. Normality is not inferred from integrality. The forced nonfree curve therefore gives the conditional nonfactoriality statement.
- If M were the pullback of O(m), projection formula gives c1=2m-k=-1 and c2=m(m-k)=4; these equalities are incompatible. The integers 38,72,124 are degrees of the zero-locus fundamental cycle only under expected codimension three.

## Primary-source Picard check

The rendered SGA2 revised printed pages 120-121 (PDF pages 128-129) were independently inspected. Corollary XII 3.5 requires an ample invertible sheaf and regular section, not very ampleness. XII 3.6 has non-strict depth inequalities, and XII 3.7 applies to complete intersections of dimension at least three, with no smoothness or reducedness assumption.

For L=pi*O(k), z is a regular section and D=(z) is V(q) scheme-theoretically. X is projective and Cohen-Macaulay of dimension four. The hypersurface sequence on P4 gives H1(D,O_D(-nk))=H2(D,O_D(-nk))=0 for all n>0. Outside D the cover is etale, so closed-point local rings are regular of dimension four and parafactorial. XII 3.6 therefore identifies Pic(X) with Pic(D), and XII 3.7 identifies the latter with Z[O_D(1)]. Restriction identifies the claimed generator pi*O(1). This calculation concerns invertible sheaves only and does not promote M to a line bundle.

Primary source: https://www.cmls.polytechnique.fr/perso/laszlo/sga2/sga2-smf.pdf#page=129
