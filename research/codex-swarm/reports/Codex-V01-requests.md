> Reviewed metadata record; scope in STATUS.md.

# Independent review of two concrete UNKNOWN requests

Source PR79 commit6e28c6b59f8245779f6c03a20798e4de6842ae19. Metadata-only script Codex-V01-requests.py checks pinned fingerprint SHA256abbd6fdd01c7b7d0f2c0c272238f4d0c11a3d9c6301f82b7d36e25c12e33eb92, model authentication through independent Boolean checker, flags, bit dictionaries, full-owner sorting and selector paths. Exact machine-readable requests are Codex-V01-requests.json. No source arithmetic, support expansion or nonzero certificate.

## A01: cloudseed12 E34

Cloudrow4, q3 localrank6, terminal2M10[2,6], kappa(-1,-2,-3,-3), positive staircase standard(1,9,13,15). Full owners in source-first order (seed,position,carrier,legalmask,standard):
(12,0,5,8,1); (12,1,1,9,9); (12,2,2,11,13); (12,3,4,15,15).
Carrier5 is canonical auxiliary, sorting key-1. Strictly increasing carriers imply identity sorting permutation and sign+1 regardless of masks. Standard bits use highbit3-i, legal masks lowbiti: masks8,9,11,15 exactly place mask1 on each infinity coordinate and mask0 on finite coordinates. All known carrier/endpoint flags pass; actual weight nonzero remains unproved.

Bare selector L R^t U: L=row2(H0_aux I_1), U=col6(P_1), tailowners(1,2,3); deletedprefixowner0 remains weighted/kernel-owned. Boolean residual paths are ONLY R[1,0],R[1,1]. Effective coefficient2 before E34 factor1/2. Therefore four branch scalar coefficients are +1,-1,+1,-1, retaining selector kernels and ALL four outer weights.

## A02: cloudseed30 E34

Cloudrow7, q4 localrank0, terminal-M20[0,0], kappa(-1,-2,-3,-4), positive staircase standard(0,8,12,14,15). Owners:
(30,0,0,0,0); (30,1,1,1,8); (30,2,2,3,12); (30,3,3,7,14); (30,4,4,15,15).
Sorted carriers0<1<2<3<4 imply identity sorting/sign+1; strictprefixanchors(0,1,2). Mask bits again exactly match standard infinity coordinates under distinct dictionaries. All flags pass.

Selector L=row0(H0_0 E_1 I_2), U=col0(P_2 H1_1), tailowners(2,3,4). Deletedprefixowners0,1 retain weights/kernel ownership. All four residual paths remain Boolean UNKNOWN. Terminal minus cancels J2 minus, effective coefficient+1, so E34 branch scalar coefficients +1/2,-1/2,+1/2,-1/2. Never apply another terminal minus.

## Four derivative families and prefix-mask accounting

For tail(i,j,k), let Ld=g_ij^-1 Vd(g_ij), Dd=g_ik^-1 Vd(g_ik)-Ld; s=T12F12 with separate N14 insertion owners. E34 is 1/2[L4 V3s_jk-L3 V4s_jk+D3 V4s_ij-D4 V3s_ij]. The JSON lists concrete scalar edge owners: A01 uses(2,3)/(1,2); A02 uses(3,4)/(2,3). Coordinates3,4 here are one-based; input pair12 is complementary. Frame conversion and cancel-before-differentiate obligations remain explicit.

Both JSON records are ONE concrete FIXED-MASK term, with prefix_mask_collapse_applied=false. Retain its selected prefix line factors. Do not silently reinterpret it as prefix-summed. To form the separate prefix-summed family: A01 owner0 must sum legal masks0 and8; A02 owner0 onlymask0 and owner1 masks0 and1. Those line-weight sums are1, replacing that prefix line weight exactly once, with no cardinality factor and no second summation. Tail masks/owners stay fixed. Carrier and standard owners persist through collapse. A fixed-mask term's derivative-demand value is not the family's value.

Disposition: both requests are valid candidate UNKNOWN metadata representatives in the surviving flag/Boolean domains, not certified source support or nonzero sectors. No incumbentseed4 overlap. Next: A workers must consume the JSON request scope and choose fixed-term versus prefix-summed computation explicitly before any lowering or schedule.
