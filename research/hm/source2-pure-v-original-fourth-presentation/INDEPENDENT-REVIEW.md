# Independent mixed-presentation and equivariant-extension review

Result: PASS. No mathematical blocker found.

Read the full proof, checker, actual S.json and immutable model, and the
kernel-bridge and cubic-syzygy inputs. Independently ran both final modes:
30 checks pass, normal and optimized output are byte-identical, and match
RESULT.json.

## Actual mixed-degree presentation

The cubic inclusion S is the actual Hilbert-Burch inclusion, with the
source representation action in its recorded syzygy basis. The proof
correctly does not substitute the standard monomial action on that basis.
Twisting gives S:A O(-2)->P O(1), alongside L:D O->P O(1).

The cokernel of [L,-S] is the cokernel of the induced A O(-2)->C_L. The
kernel bridge makes this zero. Since the target is locally free, this is
fiberwise surjectivity and yields a bundle kernel. Projection of the
fiber product (d,a) with Ld=Sa onto d identifies it canonically with K_H:
S is injective and its image is the full kernel of F(1). Thus both existence
and uniqueness of a follow. This is not merely a presentation with matching
rank or Chern data. The formal local right inverse and compatible kernel
map in the checker agree with this argument. Linear and cubic block degrees
match the stated twists.

## Global and equivariant Ext

Applying global Ext to the elementary-modification sequence gives the
canonical isomorphism Ext1(E,O(-4))=Ext2(C_L,O(-4)), because the outer
Ext1 and Ext2 groups for A O(-2) vanish by H1(O(-2))=H2(O(-2))=0.
Taking finite-group invariants is exact in characteristic zero, so the
invariant group computes equivariant extensions.

At a C3 axis the full S3 stabilizer, not just C3, is necessary. Its axis
line has sign character. Hence the even twists O(-2), O(-4) are trivial,
and A restricts as sign plus standard. The actual surjection from A O(-2)
to the one-dimensional C_L fiber forces the sign quotient. No trivial
quotient is available.

Local Koszul duality gives the character of Ext2(k_chi,L) as chi-dual
times L times determinant(tangent). Here the latter determinant is sign,
so the two signs cancel. This checks the tangent-versus-cotangent convention
explicitly. The local Hom and Ext1 sheaves for a finite-length module into
a regular surface line bundle vanish; the local-to-global spectral sequence
therefore has only the Ext2 skyscraper contribution. Its ten-dimensional
representation is induced from the trivial stabilizer character. Frobenius
reciprocity gives invariant dimension one.

The actual extension is locally nonsplit Koszul at every axis, hence its
global equivariant class is nonzero. All nonzero classes form a single
orbit under nonzero scalar rescaling of the line injection. The wording
correctly retains that qualification: distinct scalar classes remain
distinct Yoneda classes when both endpoint markings are fixed. Nothing
asserts that the ten-dimensional nonequivariant extension space has just
one nonzero class, or that K_H splits.

## Source authentication and scope

Fresh direct GitHub reads matched all three PR1053 files at commit
9658196f793afda6767565307ebc818ddfe341a5:

- proof blob 7fd12c81e863f0e6b81835e739828f90c9dabbcd;
- S.json blob a5c10967b2d2d0f738159e18e09b9758d9112f0f;
- model.py blob a7ca4755e50c85fe7fc20a757125127a05de4056.

PR1049 at 6210a276622e15c6977b8070bc1fd12744fe2f07, blob
88e8f27f6a783bbb6d77a07bb4db88b820e80149, was freshly authenticated earlier
in this same review session. All local bytes match the manifest; exact
paths and URLs are retained there.

The Chern values rank four, c1=-10, c2=46 agree with the presentation and
remain consistency checks, not its proof. Statements concern the surviving
original-fourth D kernel conditional on a nonzero gate on ell3, without
selecting that coefficient line for the actual source or claiming anything
about additional specialized A-kernel classes.

## Frozen artifact hashes

SHA256:

- PROOF.md: 1715df83bfd8c9674dfc8ca7dd85c08e18c95f2434a41a79fa7a6c15017f0da1
- verify.py: 8999802adff84c363f0f799501805724f3e7e67dd0ada480891076586627c34c
- INPUTS.json: cb1decd4cbfe8e8dede37a2d3ecd33cd3b7905ede457d07717b7f32fa55c82e8
- RESULT.json: 66c1881ad0c3c73c459faae034d6e3045abfbf9d5d6dad6370e2b469ff35112d

No actual coefficients, selected directions or source-instance ranks were
evaluated. No public files were changed.
