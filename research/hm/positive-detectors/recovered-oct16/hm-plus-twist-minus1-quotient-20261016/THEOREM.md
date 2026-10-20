> Historical mathematical record, 16 October 2026. Statements of PASS and check counts below refer to the original recorded verification, not a new execution. See PUBLICATION-SCOPE.md at the common series root for current scope, imported premises, and source/public hash bindings.

# An explicit four-coordinate positive twist−1 quotient

The pinned polynomial End differential, with genuine complex degrees−1,0,1,2, is restricted to the +1 eigenspaces of the already authenticated coordinate reversal BEFORE any elimination. The resulting complex is

Q^123 --A--> Q^196 --B--> Q^72.

Its ranks are120 and72. Four explicit cycles provide an isomorphism ker(B)/im(A)≅Q^4. All matrices, cycles, coordinate maps and lift maps are supplied in certificate.json. This is a symbolic comparison of the perfect complex, with no physical source coefficient input.

## Basis and signs

The ambient basis is (source term u,target term v,target row a,source column b,monomial exponents v0,…,v4), in exactly the pinned script ordering. The monomial exponent list is lexicographic with the first exponent increasing. Differential is dF−(−1)^degree(F)Fd. The four constant reversal matrices are −J5,−diag(J5,J5,J5),diag(J5,J5),I2.

For each two-element reversal orbit, its positive basis element is e_i+s e_j with i<j and reversal(e_i)=s e_j. Fixed positive elements are retained once and fixed negative elements omitted. No factor1/2 is built into this basis. The projector on arbitrary inputs is (1+R)/2. positive_orbits and full_bases specify this convention without implicit indexing choices.

The polynomial differential is a literal Python translation of the inspected pinned generator. Every homogeneous gamma/delta/ev coefficient is independently matched against the authenticated original literal arrays before constructing the End matrices. For each projected column, re-inclusion is checked to equal the original full differential of its included source. Thus this is an exact subcomplex, not a clipped or inferred matrix.

## Explicit cycles

Write e_i for the specified196-dimensional positive degree2 basis, indexed from0. The four quotient representatives are

c0=e16+e30,
c1=e11+e35,
c2=e6+e40,
c3=e31+e41.

Let C be their column matrix. The certificate supplies a coordinate map Q:Q^196→Q^4 and a boundary-lift map L:Q^196→Q^123. They satisfy

BC=0, QC=I4, QA=0,
z=A Lz+C Qz for every z∈ker B.

The final identity is checked on the supplied124-element basis of ker B. It implies both surjectivity and injectivity of the four-coordinate quotient description. The120 independent image basis vectors each have an explicit lift in the original123 columns of A, and those identities are checked directly. The matrix product BA is checked exactly. No rank-only assertion substitutes for these certificates.

The coordinate and lift maps are extensions to the ambient196-dimensional space. The decomposition identity is asserted only on cycles, not on arbitrary nonclosed vectors. For any cycle z, Qz is its four quotient coordinates, and Lz witnesses its difference from C Qz as an original differential boundary.

## Actual detector images

The sparse authenticated dual cycles are the4v2E_d records of hm-epsilon-projective-generator-bridge-20261016/detector-dual-cycles.json. Their factor4 and genuine supertrace block signs are already included. Applying (1+R)/2 and the exact coordinate map gives

h↦−2c1, j↦0, p↦0, r↦−2c3.

Their transported positive projections have the same images. detectors.json records every projected cycle and explicit original-column boundary lift. In particular, j and p are exact boundaries in this positive twist−1 component. This does not assert they vanish on the other target summands or on an arbitrary source lacking the required symmetry.
