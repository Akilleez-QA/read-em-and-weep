# Independent whole-proof review: uniform forward length three

## Verdict

PASS. No mathematical repair or extra hypothesis is required. The argument excludes l=3 for every k>=1 in the original rank-30 actual Gauss setting. In particular, the additional saturation W' O + O(15) is validly retained and then excluded. The proof does not need the historical 28-type recursion, any high-Q target filter, or a negative-kernel-tail classification.

Reviewed exact files:

- PROOF-L3.md, SHA256 89a36e52dccd99f7fe7193c7c2d2d120d782f69dda2582fc7c1fb6679bc0cacb.
- verify_l3.py, SHA256 ec10093ec39f93bc4444722d4f0e4069f9697f550bb7cdbfc5bae139ebea2f72.

The proof is conditional only on its explicitly retained established actual-ambient/cohomological inputs. It does not claim to re-prove the entire underlying HM setup.

## 1. Persistence, orientation and first splitting

The convention F_k=E, m=k+l is consistent. For l=3, persistence at E gives H0(E(2))=0. At K=F_(k-1), the needed index sum is k-1+3=k+2<m. Thus top(K)<=-4 holds even at k=1, where K is the lower endpoint. The endpoint has no constant subbundle because it is contained in E, so the persistence argument remains valid there.

The reversed dual plateau has central term Q* at index 3 and forward length k. Its successive backward ranks are 10,7,4, with last term at index zero. The index sum for its twist-three sections is 0+3<m=k+3 whenever k>=1. Thus both dual derivative stages used in the envelope are interior rank-three stages for every k>=1; no hidden k=1 assumption is present.

The direct proof of E=(W'+2T) O(-3)+V O(-4) is exhaustive. With H1(E(2))=V, any tail block R O(-j) costs R Sym^(j-4) W. A block at j=5 has cost at least four dimensions; at j=6 the sole possible three-dimensional scalar cost is A rather than V; all j>=7 costs exceed three by parity and dimension. Exactly one V O(-4) remains. Its contribution V W=T to H1(E(1)) leaves W'+2T in degree -3. No enumeration is being concealed in this argument.

## 2. Source and saturation facts

The degree formula deg I=-45-deg K is correct for I=(E/K)(3), rank three. Since rank K=14 and top(K)<=-4, deg I>=11. The injection U -> H0(I) is the exact quotient-section map using H0(K(3))=0.

E(4) is globally generated, so its generically surjective map to Sbar(1) forces every ordinary summand of Sbar to have degree at least -1. If an irreducible degree -1 block occurs, its coefficient is center-even and has dimension at most three. The U O part has no map there, and V O(-1) can project nontrivially only to a V O(-1) block. That block already has the entire rank three. Its lack of global sections contradicts the injection of U. Thus top/bottom information is derived from the actual map: all Sbar degrees are nonnegative.

Negative-transpose duality identifies the saturation, not the possibly defective image, with (Q*/Kd)^*(1). The ensuing dual envelope has the correct twists:

    H0(Kd(3)) <= H0(Sbar*(2))+H0(Sbar*),
    chi(Q*(3)) = chi(Kd(3))+chi(Sbar*(4)).

This gives the displayed inequality with chi(Q*(3))=T-2W-S. There is no sign reversal or premature saturation equality.

## 3. Exhaustiveness of the four Phi shapes

The seven displayed Phi formulas follow directly from H0(O(2-e)), H0(O(-e)), and chi(O(4-e)). Sbar has odd central character, so scalar/triplet blocks have odd degrees and doublet blocks have even degrees.

Every rank-three equivariant splitting is one of: three scalar blocks; one irreducible triplet block; one irreducible doublet plus one scalar. Multiplicities do not introduce a fourth partition. Every direct summand receives a nonzero projection from U O+V O(-1), because that full source is generically onto Sbar.

Scalar degrees 1 and 3 are impossible: Hom(U,Sym1)=Hom(U,Sym3)=0, and Hom(V,Sym2)=Hom(V,Sym4)=0. Hence scalar degrees are odd and at least five. Three such scalars yield no positive T in Phi. A triplet at degrees 1 or 3 has fewer than fourteen sections, while at degrees at least five its Phi has no positive T. Thus only doublet-plus-scalar remains.

For a doublet degree a>=4, Phi has no T, and the scalar Phi is nonpositive. For W at a=0 or 2, both full-source Hom contributions vanish as stated. Therefore the doublet is necessarily W', with a=0 or 2.

The budgets are correctly computed:

    B0=2W+W'+2S+T, dimension 20;
    B2=2W+W'+S, dimension 10.

The scalar degree b=5 is excluded by total degree 2a+b>=11. For odd b>=7, its cost is Sym^(b-6), whose dimension is b-5. Thus b<=25 or b<=15 respectively. These two explicit finite degree lists are exhaustive.

For a=0, b=7,9,11,13 fails the two-T section requirement; b=21,23,25 exceeds the single-T cost budget. Exactly b=15,17,19 passes the stated necessary conditions. For a=2, b=9,11 lacks W', while b=13,15 has forbidden T cost. Exactly b=7 remains. The necessary four-shape list is therefore correct without the old target filter.

An independent check using the separate profile31 audit character implementation recomputed Phi directly from line cohomology, instead of reusing the two stated budgets, and obtained exactly (a,b)=(0,15),(0,17),(0,19),(2,7).

## 4. Defect and top-multiplicity contradiction

The four saturation degrees are 15,17,19,11. The actual-image defect is nonnegative and at most 4,6,8,0 respectively, hence is zero by the minimum positive invariant divisor degree twelve. It follows that I=Sbar as sheaves, not merely generically. Twisting by -3 gives precisely the four A0 shapes stated in the proof.

All four full signed chi(K(4)) characters in (10) are correct. In particular the O(15) saturation gives chi(K(4))=2V+P and is not an exceptional unresolved case. Since H1 is genuine, these identities each force at least two V copies in H0(K(4)). The earlier bound top(K)<=-4 makes this exactly the top degree -4 coefficient space; it is not a bound inferred only from an Euler dimension.

For each A0, Hom_G(V O(-4),A0(-2)) has dimension exactly one. The doublet target contribution is zero: by ordinary degree in the first three cases, and by V not occurring in W' W=P in the last. The scalar contribution is one for Sym14, Sym16, Sym18, or Sym6 respectively.

A nonzero vector in the kernel of the linear map from a chosen two-dimensional V multiplicity space to this one-dimensional Hom space therefore gives an actual direct subbundle C=V O(-4) of K killed by beta_K. This is not an assumption that the equivariant splitting is horizontal.

Because beta_K kills C, its actual derivative factors through (K/C)(-2). The chosen C is a direct top summand, so all degrees of K/C are at most -4 and the target has all degrees at most -6. Every ordinary Hom from O(-4) to that target is zero. Hence beta_C=0 in the original ambient constant bundle. The saturation of C in that ambient follows from the locally free quotients K/C and H O/K. The characteristic-zero constant-Grassmannian argument now forces deg C=0, contradicting -12. This final implication is valid for every k>=1 and does not transfer a stronger top estimate from another profile.

## 5. Reproduction and scope

Normal and optimized execution of verify_l3.py both pass all 388 explicit requirements and produce byte-identical JSON. Review logs are review-l3-normal.json and review-l3-optimized.json. The independent fixed-degree Phi and full signed Euler/Hom check is in review_l3_independent_check.py, with output review-l3-independent.json. No historical verifier was imported or historical profile/tail enumeration executed.

The script's first three kernel-character checks deliberately require only the V coefficient needed in the proof, then print the full character. The independent check additionally verifies all four complete signed expressions in (10). Thus there is no correctness gap. Optionally, the production verifier could compare the first three entire characters explicitly for stronger editorial regression coverage, but this is not a required mathematical fix.

The geometric claims remain supported by the proof, not inferred from arithmetic execution: generic-generation degree bounds, transpose/saturation identification, invariant divisor defect, actual derivative factorization, saturation of C, and zero-derivative constancy have each been reviewed separately above.
