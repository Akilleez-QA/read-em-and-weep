# Independent entire-proof review

## Verdict and exact binding

PASS for the entire conditional theorem, not merely for its arithmetic checks.

This is a new independent review of the complete frozen `PROOF.md`, including its statement, Sections 1–7, all displayed equations, and all exclusions and retained boundaries. The reviewed file has exactly **15,127 UTF8 bytes**, with SHA256:

`205256f2772d21d81025e6c511a52de564bfd7e9e0d94cce79fc3f684b6d17ba`

No proof flaw or required correction was found. The verdict is conditional on the actual-geometric hypotheses expressly retained from the two direct originals and their transitive assumptions. It does not establish the occurrence of that configuration, or exclude a branch. It is not a review of any later edit with another hash.

The reviewer read both complete direct originals, `INPUTS.json`, `REPRODUCE.md`, `verify.py`, and `characters.py`. Neither the author's fetch records nor its scratch audit or previous replay outputs were used as evidence. No frozen selected file was edited. No GitHub write was performed.

## Fresh authentication and exact selected-only replay

Both originals were freshly fetched independently through two read-only GitHub routes: full repository path at the exact immutable commit, with no line limits and base64 encoding; and the exact pinned Git blob. Each route's complete content was compared byte-for-byte with the selected local original. Length, SHA256 and the Git SHA1 of `blob <length>\0<bytes>` were independently recomputed for all three copies. The immutable-path route's reported blob SHA and URL were also checked.

* PR1224, commit `317cf0c533b6ab8ce650d566e08c87610dd11ccd`, path `research/hm/rankfour-profile11-triplet-top-jet-complement/PROOF.md`: 11,240 bytes; SHA256 `08708a646f51fb6b10ef94c1eab1b5e4ee56a775fb8e377d6a92e8d34df54259`; Git blob `63abea7d4412fced453c728d9f1e3c7dd4870521`.
* PR1222, commit `f7abba83fedd46a9d91f5abbd9e40d3b02ae65f1`, path `research/hm/rankfour-profile11-triplet-nonsplit-quotient/PROOF.md`: 13,619 bytes; SHA256 `d4ff280dc943c2a112ea68ff4d9c4750fe5f93b3892d8a104fa9c08aa5960568`; Git blob `1974a5c3b20546dcb414539096511388f495cdab`.

Every comparison passed. Detailed non-raw evidence is in `REVIEWER-AUTHENTICATION.json`. Fresh raw fetch payloads are local and excluded from the publication and reproduction inputs.

Exactly the seven files listed in `REPRODUCE.md` were copied, preserving relative paths, into a newly created empty isolated directory. The prescribed commands were run there with bytecode disabled and empty `PYTHONPATH`, both normally and with `-O`. Both returned identical PASS output, 40 explicit checks, the bound whole-proof hash, exit code zero and empty stderr. The imported character checks were also independently observed to number 81 in both modes. Each run therefore includes 121 fixed checks, not 121 proof-verification steps.

Before/after manifests match for all seven files in the isolated directory and for the corresponding source files. The exact seven-file set remained unchanged; no caches or extra replay inputs appeared. `REVIEWER-REPLAY.json` contains the manifests, full identical outputs, check counts and exact whole-proof binding.

## Complete direct-input review

### PR1224: statement and Sections 1–6

The input's actual `Q1`, `Q2`, `Uj`, and `L10` are distinguished from abstract isomorphic bundles. Its sum and intersection give an everywhere isomorphism `Q1/U3 -> L10`, so the graph argument is not based merely on generic fibers. The universal quartic first-jet kernel is `A(-2)`, its quotient is `W(3)`, and twisting by -14 gives the stated sequence. The physical multiplicity of `A` in `D tensor Sym2 W` is one. Hence a nonzero graph would identify `Q1` with `D(-14)` and force its actual `A(-16)` quotient to be `W(-11)`, contradicting `O(-10)+O(-12)`.

The resulting zero graph places the actual `L10` in the full backward kernel. Its intrinsic first-jet source is `W(-9)` independently of coefficient completeness. The nonzero map to the actual quotient `F6/U4=W(-9)` is a Schur isomorphism, so its image is an everywhere saturated complement, not an assumed splitting. The zero Hom to `D(-14)` gives uniqueness. The coherent derivative-column argument uses the negative-degree coherent images and their actual surjectivity, not their saturations. Its kernel, degree and nonhorizontal-splitting assertions are consistent. The original's final scope correctly leaves completeness and later original jets unproved there.

### PR1222: statement and Sections 1–8

The order-twelve mixed pairing gives isotropy of `T5`, the nondegenerate rank-three quotient, and the norm of `T6/T5`; the factorial contribution is nonzero in characteristic zero and no actual coefficient is evaluated. The equivariant Euler-character argument uses the correct Serre-duality signs. For a nontrivial self-dual rank-three bundle the canonical Harder–Narasimhan filtration has degrees `(d,0,-d)`; its scalar linearizations and physical central parity force even `d`. The norm rules out `d>6`, and the fixed Euler characters rule out `d=2,4,6`. Thus the quotient is canonically trivialized by evaluation with representation `V_alt`.

The perpendicular kernel remains an everywhere rank-two bundle even where the restricted norm vanishes: the surjection follows from the ambient nondegenerate pairing and saturated line. Its degree, excluded unequal types, and Euler character give `W'(-3)`. The identification here is `B6/U5`, whereas the preceding rank-three orthogonal quotient is `B5/U5`. The extension splitting of `B6/U4` is unique for the stated Hom and Ext reasons and preserves its actual `U5/U4` line. The saturated `L10` lies in the `W'(-3)` component. The graph of `F6/G6` cannot project trivially to the `O(-8)` axis, and its other component cannot vanish because of the actual lower derivative column. Pullback along its nonzero invariant component is nonzero by invariant Serre duality; the Euler sequence then gives `F6/U4=W(-9)`.

These arguments justify the particular imported identifications and coherent images. Their exclusions concern the indicated split quotient only; they do not supply an occurrence theorem or the stronger conclusions expressly left open.

## Whole-proof geometric audit

### Statement and Section 1: ambient geometry and actual quotients

The statement consistently distinguishes a sheaf-exact full-rank inclusion from a subbundle direct sum. The actual quotient used for the normal projection is the rank-three `B5/U5`, not the rank-two `B6/U5`. The constant isomorphism `h` transfers `T5^(perp_h)/T5` to that actual quotient. The ranks and degrees are correct: `U5` has rank six and degree -78; `B5`, as the annihilator of `T5`, has rank nine and degree -78. The decomposition `F6=U4 direct-sum Z1` has degree -88, so `B5/F6` has rank two and degree ten, consistent with `(B5/F6)(-2)=O(4)+O(2)`.

Crucially, the simultaneous-image hypothesis is the exact coherent equality `I6=E6(-D12)`, not just a total-length assertion. Its saturation implies `F6^+=B5`, but the proof defers the unsaturated sum until Section 3. No quotient connection is introduced.

### Section 2: Wronskians, global span and intrinsic second jets

The coefficient span is a nonzero quotient of `Sym10 W` in the constant ambient dual representation. Characteristic-zero Wronskian nonvanishing is used in its valid form over `C(t)`, whose constant field is `C`. Dividing by a nonzero first function and differentiating ratios proves the induction: a constant relation among their derivatives integrates to a constant relation among the ratios and 1. This establishes generic jet rank `r` at order `r-1`, without choosing or evaluating an actual point.

For a local section of `Bj`, differentiation of its pairing with `T_(j-1)` places the derivative in `B_(j-1)`. Thus `L10 subset B7` places its first `k` derivatives in `B_(7-k)` for every needed `k<=7`. If `r<=8`, the generic `(r-1)`-jet span is the entire constant `r`-space, in `B_(8-r)`. The resulting morphism from the constant bundle to the locally free quotient is generically zero, hence identically zero. This is the necessary global step, not a deduction from one fiber. Since `B_(8-r) subset B0`, any nonzero constant vector in this space would give a nonzero section of `B0`, contradicting full span of the ORIGINAL degree-eighteen curve. No auxiliary completeness is assumed in obtaining the contradiction.

The fixed decomposition `Sym10 W=A+V_alt+D` is multiplicity-free with dimensions 3,3,5. A proper quotient has dimension at most eight. Semisimplicity therefore upgrades `r>=9` to `r=11`. The coefficient quotient is an isomorphism; complete degree-ten evaluation separates jets through order ten. Its dual principal-parts images are everywhere saturated with the stated types. In particular `Z2=A(-8)`, of rank three and degree -24, lies in `B5`. These are intrinsic jets of `L10`, not an extension of the original degree-eighteen jet assertion past order nine.

### Section 3: coherent derivative sum, torsion layers and fibers

The established separated jet evaluations make the coherent first-derivative spans of `U4` and `Z1` exactly `U5` and `Z2`, respectively. Consequently the coherent derivative span of `F6` is `S=U5+Z2`, without taking another saturation. Contracting the second fundamental form with the tangent line gives `S/F6=I6(2)` as an actual subsheaf of `B5/F6`. The tangent twist is +2 and is used correctly.

It follows that `B5/S=(B5/F6)|D12`. Since `S` has saturation `B5`, the map `U5 direct-sum Z2 -> B5` is generically surjective between rank-nine bundles. A generically zero kernel subsheaf of a vector bundle on this integral curve is zero, proving the sheaf direct sum and zero sheaf intersection. The rank-two quotient is free over the reduced divisor, so its local module is two copies of the residue ring, not an arbitrary length-two module. Hence the nine elementary orders are seven zeros and two ones.

The individual maps of `U5` and `Z2` into `B5` are subbundle maps, while their sum is not on `D12`. The fiber-intersection dimension is therefore `6+3-7=2` on the divisor and zero away. There is no illicit interchange of a sheaf intersection with fiber restriction. The degree difference 24 corroborates, but does not replace, the exact quotient argument.

### Section 4: actual normal projection and exact exterior divisibility

Quotienting by the actual `U5` produces `0 -> Z2 -> H -> (B5/F6)|D12 -> 0`. Thus the local elementary orders of `q` are exactly `(0,1,1)`, with no defect elsewhere. These are deductions from the exact module quotient, not evaluated Smith forms of an actual matrix. They yield fiber rank one and determinant divisor `2D12`.

The universal exterior-module rule gives orders `(1,1,2)` for `Lambda^2 q`. There is exactly one common divisor factor along `D12`, and none away. Division glues as a morphism `c:Lambda^2 E tensor L -> Lambda^2 F`; the twist is `2*(-8)+12=-4`. Its orders `(0,0,1)`, fiber rank two, and determinant divisor `D12` follow. The common factor cannot be divided twice. The section `f12` is an arbitrary nonzero universal invariant, and rescaling it changes only the scale of `c`.

### Section 5: physical Hom spaces and conditional universal class

For both self-dual rank-three representations with trivial determinant, the second exterior power has the same representation type. This does not specify a volume form. The physical McKay identities give `V_alt tensor Sym4 W=A+D+V_alt+P`, hence quartic Hom dimension one. Independently following the same fixed recurrence through degree eight gives `V_alt tensor Sym8 W=2A+2D+V_alt+2P`, so the degree-eight Hom dimension is two. The distinction is substantive.

The actual nonzero `c` therefore fixes a universal projective class. Its generic invertibility and divisor properties here are conditional consequences of the retained actual configuration, not an independently asserted realization of that configuration.

### Section 6: determinant lines, direction and recovery

The determinant quotient `d=det(q)/s^2` is an everywhere isomorphism `det E tensor L^2 -> det F`, because the determinant divisor is exactly `2D12`. The rank-three natural isomorphism `Lambda^2(Lambda^2 J)=J tensor det J` is functorial. Applying it to `q`, taking the second exterior power of the factorization by `s`, and cancelling the same nonzero-divisor factor `s^2` gives precisely `Lambda^2 c=q tensor d`.

The source is `E tensor det E tensor L^2` and the target is `F tensor det F`. These are the correct directions and determinant twists; no unqualified same-direction adjugate is being used. The source degree becomes -8 in each rank-three multiplicity component, while `det E tensor L^2` has degree zero. Thus `d` is a nonzero constant determinant-line comparison. It affects only scale, so the projective class of `q` is recovered from the projective class of `c`. Equivariant identifications of the irreducible source and target types also differ only by scalars. No determinant normalization or actual matrix is needed.

### Section 7 and all scope boundaries

The contribution is the embedded second-jet normal-map constraint, its exact torsion quotient, and the resulting unique projective class within the two-dimensional degree-eight Hom. Neither the coefficient-span argument nor the exterior identity is turned into an unsupported exclusion or existence claim. The proof does not differentiate `H`, claim a horizontal decomposition, transfer full span without proof, establish original tenth jets, or identify these normal-map orders with original higher ramification or algebraicity. All stated remaining cases remain open.

## Checker and restriction audit

The explicit guards are exceptions, not optimization-sensitive assertions. `characters.py` performs exactly nine-by-nine fixed exact-rational McKay checks at import, then uses bounded symmetric-power recursion for the listed fixed representations and degrees. Its unused helpers do not initiate any search. The representation labels, dimensions, adjacency and fixed trace values are consistent with the physical binary-icosahedral action. The elementary-order and exterior-weight computations are formal universal arithmetic, not instance computations. The three exterior weight checks support the twist accounting but do not by themselves prove naturality; the geometric review above separately verifies the functorial identity.

The replay makes no network requests, performs no remote writes, installs nothing, and evaluates no selected actual HM/source coefficient, parameter, graph scalar, point, jet, tensor, matrix, instance rank or invariant normalization. No broad scan or large computation was performed. Fresh repository reads were limited to the two explicitly selected originals by immutable path and blob.

**Final whole-proof conclusion:** the exact frozen proof bound above is mathematically coherent and establishes its stated conditional normal-map theorem with the declared restrictions and retained boundaries.
