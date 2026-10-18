# Independent audit: graded overlap reduction

## Verdict

The formal identity is correct under the stated common-complex, normalized contraction, physical frame/transition, fixed ambient restriction, and selector hypotheses. Insertion notation must be consistently R; the older comparison primitive K is a different object. The source is not executed and no actual model, owner, jet, matrix-polynomial product, or retained test is evaluated.

## Independent checks

1. Since both split connections parallelize the same differential, A′=Γ_j−Γ_i is End-closed. The column induced connection is −V(G)G⁻¹=−θᵗ for G=gᵗ and θ=g⁻¹Vg. The single transpose in π gives π_i A′=−θ, hence A′=j_i(−θ)+dH_i A′. No literal equality of inclusion columns A_j=A_iG is required; induced cohomology connections supply the result.
2. For |Xi|=−1, graded derivation gives d ad_Xi+ad_Xi d=ad_(dXi). Therefore C=C0+dR+Rd, and R is an anticommutator on degree −1 inputs. First-face signs are positive.
3. All internal deleted-prefix owners survive. δR+Rδ inserts ζ=Xi_jk−Xi_ik+Xi_ij, with Xi_jk computed using H_j. Telescoping A′ gives ζ=(H_j−H_i)A′_jk and dζ=−δa. Twisted row closure Δθ=0 does not imply δa=0.
4. Direct expansion of all four terms produced by C−C0=dR+Rd, followed only by Hd=1−P−dH, dJ1=δj−jΔ, dj=0, dδ=δd, Ld=0 and Lδ=δL gives

   LRJ1 + LHRδj + LHδRj − δLHRj − LHRjΔ.

   The projection P kills the applicable negative-internal-degree suffixes; it is not globally discarded. This proves both homotopy corrections, the boundary sign and the nonclosed-input sign. Combining the middle terms gives LHWj. The supplied independent checker implements these rewrites rather than merely listing the final formula.
5. Actual H_r[a,X]=(-1)^r aXh−hXa follows from ha=ah=0, ea=a. Substitution a=−jθ gives the author's two displayed C0 signs. A shifted-owner X must not be replaced by an i-owner lift.
6. π is product-reversing on induced degree-zero cohomology maps. Therefore π[j(−θ),X]=[θ,πX] for closed X. The induced Δ′=−πCj has the sign −[θ,tR], agreeing with differentiation of g⁻¹Rg for fixed R.

## Separate conditional domain theorem

See DOMAIN.md for the independently audited representation covariance, per-occurrence envelope, full ordinary comparison and Serre-boundary result. It does not include the individual selector connection term.

## Controls and limitations

check.py is an independent portable formal rewrite check using only standard-library strings, integer coefficients and explicit nonzero-internal-degree projection rules. It has 13 positive/negative controls, passes normal and optimized Python, and uses no assertions whose disabling could remove checks. The frame-anomaly and envelope controls test only algebra/arithmetic: the imported physical/geometric premises are supplied by the cited proofs, not established by these controls. Omission of any of the five surviving operator words or reversal of the nonclosed sign is detected. No actual-model correctness, execution admission, complete divergence certificate, or zero-obstruction conclusion follows.

Premise sources are bundled in dependencies/ and individually identified in pins.json. They are frozen supplied text, not fresh remote attestations.
