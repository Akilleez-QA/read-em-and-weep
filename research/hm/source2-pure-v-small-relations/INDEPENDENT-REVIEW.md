# Independent review of the nine-dimensional branch relations

Verdict: PASS. The complete proof and final verifier were independently read
and the final normal and optimized runs were independently replayed. There is
no mathematical blocker. This is not a formal proof-assistant verification.

## The new forced P relation

The actual balancedness premise is sufficient: the evaluation kernel is
(P+D)O(-2), so after twisting by one both H0 and H1 vanish. Consequently
H_t tensor W -> Sym19 W is an isomorphism of the actual polynomial spaces.
This is stronger than matching their dimensions or characters.

PR1054's injected W tensor P16 supplies an actual nonzero W' subspace U
in Sym17 W. Multiplication W tensor U is nonzero and has irreducible domain
P, hence its image P_desc is four-dimensional. Associativity places it in
the polynomial image of Sym²W tensor P16; multiplicity one identifies the
P summand whose image it is. This establishes its nonzero image rather than
assuming that a character constituent survives multiplication.

The next multiplication factors through Sym²W tensor U=T. It is nonzero
because polynomial multiplication in two variables has no zero divisors.
Irreducibility makes its rank six. Thus W tensor P_desc has a nonzero
W' kernel. If P_desc equalled the endpoint P_t, that kernel would contradict
the actual balancedness isomorphism. The P-isotypical part of H_t is exactly
P_t, so the quotient kills P_desc precisely in the excluded equality case.
The resulting P image is the actual I4, not an independently chosen copy.
This proves a genuinely nonzero graph relation without choosing an endpoint
parameter, actual coefficient, or source-instance rank.

The nonsplitting argument is sound. An equivariant splitting must lift the
P generators to the unique P_h because Hom(P,I2)=0, whereas their P
quadratic descendants map nontrivially into I4. An arbitrary negative-module
splitting could be averaged over the finite group, yielding the forbidden
equivariant splitting.

## Relations, socle, and normalization

The four literal linear Koszul relations in the I2 factor are correct, and
their bidiagonal matrix is injective over the polynomial ring. Their eight
linear multiples are independent. Quotienting these leaves the specified
V_I+P_I and V_h+P_h^(2)+D_h summands. The two P maps are nonzero, D_h
maps isomorphically onto D, and both V summands vanish, giving precisely
2V+P minimal quadratic relations with two nonzero graph projections.

The degree-one socle argument retains both actual T summands. The W'
constituent is excluded by its nonzero P multiplication. The D projection
kills T_I but is nonzero on T_h; since W tensor T has D once, its kernel
in the T multiplicity space is exactly T_I. The remaining T_I has nonzero
multiplication to I4. Thus no T graph can be a socle constituent. Degree
zero has no joint annihilator by its actual polynomial embedding.

For the explicitly artificial truncation, the only socle is P+D in degree
two. The two-variable Koszul identification gives Tor2 in degree four,
with no determinant twist because det W is trivial. The representation
Hilbert numerator then gives the displayed minimal resolution and the
scalar numerator 9-4t-10t²-4t³+9t⁴. No conclusion about actual degree-five
arrows or a resolution of the full actual module is used.

The Q-preserving coordinate argument is also correct with its stated fixed
reference intertwiners: first multiplication determines the middle changes,
I multiplication determines the scalar b on I4, and the equations
b lambda=a lambda' and b q=a q' preserve lambda/q. This proves an invariant
ratio, not its numerical value, universality, or an extension of those
changes to the entire actual source module.

## Independent authentication and replay

Fresh immutable GitHub fetches authenticated all five inputs:

- PR792: blob 76bee93507d1a2d0840926d4e4e27edadfebb7d7.
- PR794: blob 3ad30b9aa1920408cc34778e78405f544b5adc8e.
- PR1054: blob 64e6bf9f1bf46440700ebab7c90a18f9d8155fd8.
- Universal symbols: blob 0ff4a2fd717842d8df9cf3ce3e3d29fd189bcd6e.
- PR1059: blob 2b00a40de04a7084ff2f08c767fdd2f4f13ae5f4.

An extra terminal newline in the initially retained PR1059 file was detected
and reported. The author removed it and corrected the manifest. The final
retained bytes now match the immutable remote blob exactly. This correction
changed no mathematical premise.

The verifier's polynomial realization uses only fixed universal representation
constants and symbolic binary variables. Its P16 construction and rank-six
P_desc multiplication supplement the intrinsic proof; they are not evaluations
of an actual source or selection of P_t. The historical source script is
retained for provenance, not executed.

Independent python verify.py and python -O verify.py both pass all39 checks.
Their outputs agree byte-for-byte with each other and the final RESULT.json.
The review is bound to these SHA256 hashes:

- PROOF.md: 0707fb58aecd1c0483051c6be17329bb3aad6e5438ee99f4af7edc234913b6f8.
- verify.py: 69379a627e6ebaea54105588822eface87a596249695ce0de972f8b1cad208fa.
- INPUTS.json: 6467363185589c89b376cd5dd387ba44305dcceba6404bd2fbbebffa27bd44cb.
- RESULT.json: 52941071142303102843287ad89a372abda6222940467107fbd5311f24aeaf78.

The nine-dimensional branch remains conditional. No actual scalar, source
occurrence, original higher-obstruction value, or full repair is selected.
