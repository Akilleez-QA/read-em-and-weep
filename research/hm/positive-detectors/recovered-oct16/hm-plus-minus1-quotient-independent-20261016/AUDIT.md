> Historical mathematical record, 16 October 2026. Statements of PASS and check counts below refer to the original recorded verification, not a new execution. See PUBLICATION-SCOPE.md at the common series root for current scope, imported premises, and source/public hash bindings.

# Independent positive twist−1 quotient audit

## Result

PASS. The supplied123→196→72 complex, its four quotient representatives, full coordinate and boundary-lift maps, and all eight original/transported detector records are correct. The independent checker performs1,094 direct exact checks in0.025seconds and12MiB without elimination or source evaluation. Certificate SHA256:616006681d2952a3d895e2bf369d2c5813a9091c38a490b9bd936c2299e5de3c.

In this positive twist−1 dual-cohomology component, the recorded detector classes are h=−2c1, j=0, p=0, r=−2c3. The zero assertions include explicit original degree1 boundary lifts. They concern this component only; they do not alone prove a named detector vanishes on the full obstruction.

## Independent construction

The checker does not import or execute build.py. It reads the authenticated original sparse gamma,delta,ev coefficient arrays in pinned-model-input.json and homogenizes their affine constant term as v0. From these literals it reconstructs the End differential by postcomposition and signed precomposition dF−(−1)^r Fd. The reconstructed ambient bases agree with every supplied basis key, not just the dimensions.

It independently reconstructs every signed reversal orbit using the actual four chain matrices. Each positive pair vector is e_i+s e_j, with no half factor; fixed positive vectors occur once and fixed negative vectors are absent. Each projected differential column, re-included into the full basis, equals the full literal differential applied to the included source. Both resulting projected matrices match the certificate entry by entry. This authenticates the Python translation against the literal model and the pinned Hom signs.

## Quotient certificate without a rank rerun

All columns of A, all124 supplied kernel vectors and all four c_i are annihilated by B. The kernel basis has an identity submatrix on124 distinct free coordinates. On the complementary72 columns, B is a signed permutation matrix: every column has exactly one entry±1 and all72 rows occur. This is an explicit surjective minor, requiring no determinant expansion or elimination. It proves the124 vectors form the entire kernel.

The120 image vectors each equal A times their supplied lift. Their successive distinct unit pivots and vanishing at preceding pivots directly prove independence. Thus the image rank is120.

For every kernel basis vector z, independently checked

z=A Lz+C Qz,

where C has the four supplied cycle columns. Also QC=I and QA=0. These products prove that Q induces an isomorphism ker B/im A→Q^4. The ambient extensions of Q and L are not asserted to decompose noncycles.

## Detector binding

The checker rereads the complete signed detector-dual-cycles records from the existing epsilon/projective bridge. It reconstructs (1+R)/2 with the actual physical row reversal, rather than trusting the supplied projected columns. Every full basis key, coefficient, and resulting positive column is checked. The inherited factor4 in the bridge is retained, and the only new half factor is the positive projector. All coordinates and original-column boundary witnesses match detectors.json. Original and transported records have identical positive quotient images, as required.

## Interpretation boundary

The mathematical certificate is for the pinned perfect line complex. Its characteristic-zero interpretation as End(H) uses the separate authenticated HM monad/Euler-coresolution identification, not a rank transfer from characteristic3. Serre duality identifies this positive twist−1 dual space with the positive twist−4 target; no inference is made about the remaining twist−3 target component.
