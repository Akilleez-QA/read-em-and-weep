# Low generators and nonvanishing middle generalized determinantal defects

## Scope and notation

Let S=Sym(T) be the established five-variable polynomial ring over a characteristic-zero field. Let phi:F=S(-2) tensor U -> G=S tensor W present H, with dim U=10 and dim W=2. Let C^a, 0<=a<=8, be the classical generalized Eagon–Northcott complex, with C^0 the ordinary complex. For 0<=i<=a its term is Lambda^i F tensor Sym^(a-i)G; for a+1<=i<=9 its term is Lambda^(i+1)F tensor D_(i-a-1)G* tensor det(G)*. Write M_i^a=H_i(C^a).

All statements concern these auxiliary S-modules. They do not settle selected HM/source values, the original fixed-pair lifting problem, higher-order lifting, algebraicity, or the remaining determinantal parameter k. No selected-instance matrix evaluation or coefficient search is used.

The companion generalized-duality result gives finite-length homology, vanishing for i>4, and

M_i^a = (M_(4-i)^(8-a))^vee(-15) tensor Omega,

where Omega=det(U) tensor det(W)* tensor det(T)*. Here M^vee_j=Hom_k(M_(-j),k). Its proof is reverse duality of the length-nine free complexes followed by finite-length hyper-Ext in dimension five. Hilbert-function consequences below forget this one-dimensional orientation, not the internal shift.

## 1. Injectivity on the initial degree of each left-strand differential

The pinned universal quadratic relation inclusion has the form

U=E tensor W -> S_2 tensor W=(E tensor Sym^2 W) tensor W,

with binary-factor map

x |-> x^2 tensor y - xy tensor x,
y |-> xy tensor y - y^2 tensor x.

For a covector lambda with lambda(x)=alpha and lambda(y)=beta, contraction of the final W factor gives

x |-> x(beta x-alpha y),
y |-> y(beta x-alpha y).

Thus the evaluated map q_lambda:U -> S_2 is injective whenever lambda is nonzero: it is the identity on E tensor multiplication by a nonzero binary linear form. This remains true after a field extension and, in particular, at the generic binary covector.

For 1<=i<=a, the degree-2i part of the left-strand differential is

Lambda^i U tensor Sym^(a-i)W -> S_2 tensor Lambda^(i-1)U tensor Sym^(a-i+1)W.

Evaluate the symmetric W coefficients at the generic covector. The map becomes exterior coproduct followed by q_lambda on the removed U factor. It is injective: choose a left inverse S_2 -> U of q_lambda and then wedge; the composite is multiplication by i on Lambda^i U, up to the harmless consistent sign. Characteristic zero makes i invertible. A polynomial tensor which evaluates to zero at the generic covector is zero. Equivalently one can vary all nonzero covectors over the infinite characteristic-zero field and use polynomial vanishing. Consequently the displayed differential is injective.

Therefore M_i^a has zero degree-2i part for 1<=i<=a, and it has no components below degree 2i because C_i^a starts there. In particular M_1^a starts in degree at least 3 for a>=1, M_2^a starts in degree at least 5 for a>=2, and M_3^a starts in degree at least 7 for a>=3.

The argument evaluates only the universal binary tensor identity, not any selected HM/source-instance matrix.

## 2. Exact low components of the first defect

For 2<=a<=8, C_1^a=10a S(-2) and C_2^a=45(a-1)S(-4). Its zeroth homology is Sym^a_S H. Thus degree three has no boundaries, and

dim M_1^a_3 = 50a - 35(a+1) + dim(Sym^a H)_3
              = 15a-35+dim(Sym^a H)_3.

These are minimal generators because M_1^a has no degree <=2 components. Using the pinned symmetric-power Hilbert functions gives, in order a=2,3,4,5,6,7,8,

10, 20, 30, 40, 55, 70, 85.

In degree four, Section 1 proves that the boundary map from C_2^a has rank exactly 45(a-1), without a numerical rank computation. Therefore

dim M_1^a_4 = 150a - 70(a+1) + dim(Sym^a H)_4 -45(a-1)
              = 35a-25+dim(Sym^a H)_4.

The corresponding dimensions are

50, 80, 115, 150, 185, 220, 255.

These degree-four numbers are component dimensions, not asserted new-generator counts.

Duality consequently gives M_3^b_12 and M_3^b_11 for b=0,1,2,3,4,5,6, respectively:

M_3^b_12: 85, 70, 55, 40, 30, 20, 10;
M_3^b_11: 255, 220, 185, 150, 115, 80, 50.

There are no M_3^b components above degree 12 in this range. Hence the entire displayed degree 12 component is socle. No claim is made that this is the full socle.

## 3. The two endpoint first defects

For a=0, C_1^0=45S(-4) maps onto D=I_2(phi), whose degree-four component has dimension 35. Thus M_1^0_4 has dimension 10. C_2^0 starts in degree 6, so there are no degree-four or degree-five boundaries. Since D_5=I_5 and dim I_5=126-3=123,

dim M_1^0_5 = 45*5-123=102.

The constant ten-dimensional kernel in degree 4 spans a free submodule of C_1^0, so multiplication by T on it is injective in degree 5 and has dimension 50. Hence M_1^0 has exactly ten minimal generators in degree 4 and exactly 52 in degree 5. Further generator degrees are not excluded.

For a=1, the Buchsbaum–Rim complex has C_1^1=10S(-2) and C_2^1 starts in degree 6. The complete resolution of H says ker(C_1^1 -> C_0^1) is generated by 20 elements in degree 4. Quotienting by boundaries starting in degree 6 preserves these generators and creates none. Thus M_1^1 has exactly 20 minimal generators, all degree 4; dim M_1^1_4=20 and dim M_1^1_5=100, because the next syzygies of H start in degree 6. By reciprocity, M_3^7 is therefore level, with socle dimension 20 in degree 11, and its degree-10 component has dimension 100.

## 4. A forced nonzero middle defect in the self-dual case

Set a=4 and h_j=dim M_1^4_j. Section 1 and reciprocity give

M_1^4 supported in degrees 3 through8;
M_2^4 supported in degrees 5 through10;
M_3^4 supported in degrees 7 through12.

The middle module is self-dual across total internal degree 15 (with Omega). In particular its Hilbert function is symmetric about 7.5. Also h_3=30 and h_4=115 by Section 2.

The alternating Hilbert series of the free complex C^4 is

[5-40t^2+135t^4-240t^6+210t^8-210t^12+240t^14-135t^16+40t^18-5t^20]/(1-t)^5.

Its coefficients in degrees 5,6,7 are respectively -95,35,135. Zeroth homology Sym^4 H has Hilbert function (5,25,35,5) in degrees 0..3, and fourth homology is its dual shifted by -15, supported in degrees 12..15. Hence neither contributes in degrees 5..10. Alternating homology and the H1/H3 reciprocity give

dim M_2^4_5 = dim M_2^4_10 = h_5-95;
dim M_2^4_6 = dim M_2^4_9 = h_6+35;
dim M_2^4_7 = dim M_2^4_8 = h_7+h_8+135.

It follows that h_5>=95 and length(M_2^4)>=340. More specifically M_2^4 has at least 35 dimensions in each of degrees 6,9 and at least 135 dimensions in each of degrees 7,8. Thus the middle generalized determinantal defect cannot vanish. This conclusion does not require any unresolved rank or k value, and does not assert an exact full Hilbert function.

## Dependencies, public sources, and verification status

The generalized-complex reciprocity is recorded in PR507 at exact commit 87c9b317bd4b1116e63212a6d7ec2730486b2032, https://github.com/Akilleez-QA/read-em-and-weep/blob/87c9b317bd4b1116e63212a6d7ec2730486b2032/research/hm/generalized-en-defects/PROOF.md, based on the explicit classical complexes in Andrew R. Kustin, “Canonical complexes associated to a matrix,” Section 3, https://arxiv.org/abs/1509.04367 . The duality is also stated in the introduction, equation following (1.0.2). No generic grade-nine exactness is assumed; the actual finite-length support in dimension five is used.

Exact already-published inputs:
- Universal quadratic relation inclusion: https://github.com/Akilleez-QA/read-em-and-weep/blob/1c5ad353bb5f1808150f64cde3c29b92c6e13d91/research/hm/dual-tensor-bridge/VERIFICATION.md
- Canonical square Sym^2 H=R^vee(-5): https://github.com/Akilleez-QA/read-em-and-weep/blob/e9ed26058f69f3b96bdcdf920cb638e9dd68def8/research/hm/endomorphism-rigidity/INDEPENDENT-DERIVATION.md
- Higher symmetric-power Hilbert functions: https://github.com/Akilleez-QA/read-em-and-weep/blob/72ab9a7524aef8c9d1c1fd989f8b0e83826dc916/research/hm/higher-symmetric-powers/PROOF.md
- Complete H resolution: https://github.com/Akilleez-QA/read-em-and-weep/blob/1112189481554b0353c64178e3adc0dede2c3fbe/research/hm/middle-euler-ghost-exclusion/PROOF.md
- Determinantal quartic image and D_d=I_d for d>=5: https://github.com/Akilleez-QA/read-em-and-weep/blob/b972aa22b72658b419e2c8948a56e0eec7f59e13/research/hm/fitting-thickening/PROOF.md
- Scalar quotient Hilbert function: https://github.com/Akilleez-QA/read-em-and-weep/blob/86d7e1b5d3aee770ea3e7652c950b29bca1aba10/research/hm/scalar-last-ghost-exclusion/PROOF.md

Authored structural derivation, conditional on these inputs and the companion reciprocity proof. Independent review is required before publication. Not formally proof-assistant checked. All arithmetic above consists of small free-module dimension counts, not selected-instance computation.
