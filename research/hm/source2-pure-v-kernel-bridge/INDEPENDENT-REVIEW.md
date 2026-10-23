# Independent kernel-bundle bridge review

Result: PASS. No mathematical blocker found.

Read the complete final proof, checker, manifest and both immutable inputs.
Independently ran normal and optimized verification. Both pass 28 checks,
produce byte-identical output, and match RESULT.json. All four frozen
artifact hashes match.

## Exact maps, twists and local freeness

Normalizing the nonic and degree-ten rows gives F:P O->I_B(9) and
H:D O->I_B(10), with H=F(1)L. Equality of their image ideal sheaves is the
necessary actual input for the diagram: its right vertical arrow really
is the identity, not a generic equality. The snake lemma gives
0->O(-4)->K_H->K_F(1)->C_L->0. The proof explicitly defines C_L as the
twisted finite cokernel here and does not assert an unjustified equivariant
identification of its different twists. The sign in the original-fourth
comparison does not change its kernel.

Every finite-colength ideal in a regular surface local ring has projective
dimension one. Kernels of the displayed free surjections are therefore
free locally, even when the base ideal is not a complete intersection.
Their ranks three and four are correct. This reasoning does not assume
that m^2 or m^3 is two-generated.

## Compatible local forms and singular modification

At a rank-three C3 point, reduced maximal minors put L in the form
 diag(I3,(u,v)). Equality J+(f4)=J+m(f4) forces f4 into J by Nakayama on
the cyclic quotient. The target shear removing f4 and source shears
removing the induced upper u,v entries are compatible invertible changes.
The checker verifies them symbolically, including preservation of the
Koszul generator. Thus the simultaneous forms for F,H,L are justified.

With S the rank-two free syzygy module of the first three generators, the
kernel map is identity on S plus R^2->R, (a,b)->ua+vb. Consequently its
image is S plus m, and its cokernel is the residue field. This proves
surjectivity onto C_L for every nonzero coefficient direction and proves
that the intermediate rank-three sheaf is not locally free at any C3
axis. The local extension is the nonsplit Koszul extension; splitting
would make m projective. The line-sheaf injection is not a subbundle at
these points, and its section zero ideal is exactly (u,v). Hence its
zero scheme is precisely the ten reduced axes.

The fiber-image distinction in the proof is also correct. The kernel
bundles keep constant ranks, but their images in the source fibers have
dimensions n-mu(I_B). This gives the claimed change from two to one for
K_F and three to two for K_H on ell3. The residue map detects the remaining
redundant fourth generator, while syzygies whose source fiber image is
zero map to zero. No fiber rank is confused with a bundle rank.

## Chern and reflexive-hull checks

The defining presentations give c2(K_F)=81-b and c2(K_H)=100-b. Twisting
the rank-three K_F by one gives c1=-6 and c2=66-b. Subtracting the
length-ten cokernel in the Chern character raises c2 of the modification
to 76-b. The extension by O(-4) then adds 24, recovering 100-b. Omitting
the finite cokernel would indeed lose ten.

Because the modification agrees with K_F(1) off codimension two, its
reflexive hull is canonically K_F(1); its defect is exactly C_L. This is
consistent with the explicit local R^2 plus m description.

## Provenance and scope

Fresh direct GitHub read authenticated PR1046 at
56c1ee605ba1886d7e837d6a686b3e8a00af1dc9, blob
018672738b8f206aef51ae163053ecad3400075a. PR1025 at
09f1377f83b027ca27eea0b3a9f40a1b92c6c466, blob
d036adcf5bc2bfc53e07cd752ff180c5993251f7, was freshly authenticated earlier
in this same review session. Both local copies match their declared hashes.
INPUTS.json retains exact paths and URLs.

This is an actual kernel-sheaf consequence of the previously proved ideal
bridge, not an actual coefficient selection, rank computation on a source
instance, or treatment of additional specialized A-kernel classes. The
checker covers symbolic basis and K-class identities; the written proof
supplies depth, exactness, nonsplitting and reflexive-hull arguments.

## Frozen hashes

SHA256:

- PROOF.md: cefc1840cc869aaa97f2e2cc3852f1771f8a8fc8ad36a6fd2e087cdd1105e372
- verify.py: dd6d5a0dc2b448d36ef4ed236a012cf7b75941cb296cc827351f9f67186bd80f
- INPUTS.json: 9ce1287d0d8c62cf8979cb24c066666c6f89ca680f31e4d549e2ac25d2e226cb
- RESULT.json: c1dd5b497c84b5b0703b1ed19458c2835503a10cee05f0aa1deb3f1682e120c1

No actual HM coefficients or source instances were evaluated. No public
files were changed.
