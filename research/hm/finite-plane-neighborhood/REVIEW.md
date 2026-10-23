# Independent structural review

Verdict: PASS for the finite ordinary-neighborhood corollary, conditional on the explicitly pinned exceptional-polar theorem and its retained geometric inputs. This is a mathematical review, not formal proof-assistant verification. The reviewer did not modify PROOF.md.

## Reviewed byte identities

SHA256 of the final four artifacts reviewed:

- PROOF.md: f210d928117d0a6f05a7102dd8252b7e0d4220bc5c1311271359e2fed21cf5da
- INPUTS.json: 24c95a450b272b0db2c2d67ba810033f18ce73935b86fe542ff417d8eeae7eff
- REPRODUCE.md: a9e4ce7935d2ead58660677eff0e138ee2d2a9b64f8aa8bd4a40312a86dc7fce
- verify.py: 98ee7b8fab2cdad664e96405edc24f908989ce9792a1dbe94f1c2ce07770e973

The reconstructed audit-inputs/POLAR.md has SHA256 03f7909a73ebe2cd2ff7c8639f3bea3384741058297156f51f38b2b6094354e6 and Git blob d8e950886eee0bc7fc3844b85301b55edb449450. Its bytes match the previously frozen, independently reviewed local parent theorem. INPUTS.json identifies the publication at commit 13d0e53e0a64ec6935a2ca83af776942e201c4e9, research/hm/exceptional-polar-obstruction/PROOF.md, in Akilleez-QA/read-em-and-weep. This review authenticated the available input bytes against that manifest; it did not independently perform a remote repository fetch.

## Geometric checks

1. The relative dualizing line is O_X(E), with no dimension shift, because both smooth spaces have dimension four. Duality therefore sends Rp_*O_X(jE) to Rp_*O_X((1-j)E)=I^(j-1). The negative exceptional direct-image statement is the ordinary Rees/blowup statement for a regular codimension-two ideal, including higher-direct-image vanishing. It does not replace an ordinary power with a symbolic power.

2. The dual of O→Rp_*O_X(jE) is the canonical ideal inclusion. More explicitly, dualizing upstairs gives O_X((1-j)E)→O_X(E); pushforward and the canonical trace identification Rp_*O_X(E)=O give I^(j-1)→O. This checks the arrow itself, not only its source and target.

3. Dualizing O→Rp_*O_X(jE)→L_j[-1] gives the cone identity RHom(L_j,O)[2]=O/I^(j-1). Consequently RHom(K_j,ω_P4)=B(4)|_(j-1)R[-2]. Both the shift and the index j−1 are correct; B*=B and the ambient twist is 9−5=4. This is a full sheaf-derived identity: Ext² is the stated ordinary-thickening sheaf and all other sheaf Ext groups vanish.

4. Four-dimensional global Serre duality identifies H²(K_j)* with Ext²(K_j,ω_P4), and the concentrated sheaf Ext identity identifies the latter with H⁰(B(4)|_(j-1)R). Finite-group invariants commute with duals over C. The retained determinant/linearization conventions make these identifications equivariant. Thus the pinned H²(K4)^G=C and H²(K8)^G=0 really imply the ordinary third- and seventh-neighborhood section dimensions.

5. The candidate is identified directly in the ordinary ideal filtration. The k=0 and k=1 layers have no invariant H⁰, so the k=2 layer injects into the third neighborhood and supplies its entire invariant section line. The k=2 character is (A⊗A)^G=C. No splitting of the neighborhood or of the polar filtration is used. For every k≥3, H⁰(B_R(4−k))=0 by the pinned twist-one vanishing and nonpositive-twist vanishing. Hence H⁰((m+1)R)^G→H⁰(mR)^G is injective for m≥3. The corrected explicit indexing matters: restriction from 3R to 2R is not injective.

6. Sheaf Ext² duality sends the polar short exact sequence to the actual ordinary restriction sequence, with kernel i_*(Sym^(j−2)W*⊗B_R(6−j)). Indeed Ext²(i_*G_j,ω_P4)=i_*(G_j*⊗ω_R), with all other sheaf Ext groups zero. This identifies the map orientations and the actual extension classes, not just associated-graded dimensions. At j=6 and j=8 the new ordinary layers have indices 4 and 6. Serre duality identifies the ordinary boundaries with α* and β*, under compatible boundary signs.

7. Odd layers have no invariant cohomology by central parity. Thus the unique candidate extends uniquely from 3R to 4R; if it survives order four, it extends uniquely from 5R to 6R. The order-four obstruction target has dimension one. The order-six target has dimension two; its plane character also follows from H¹(B_R(−2))=H¹(B_R(−1))* by plane Serre duality. The parent rank relation forces either the order-four obstruction to kill the line or, if α=0, the order-six obstruction β* to inject it into its two-dimensional target. The proof correctly leaves that alternative undecided.

## Reproduction and scope

Executed python3 verify.py and python3 -O verify.py successfully on the final bytes. The script authenticates the pinned input Git blob and checks fixed nine-class character arithmetic, dimensions, elementary duality-index arithmetic, and the two abstract rank alternatives. It does not itself prove Grothendieck duality or select a geometric instance; those claims were checked in the mathematical review above. REPRODUCE.md correctly requires reconstruction and authentication of the omitted copied parent proof before verification.

No selected actual HM/source coefficient, point, parameter, matrix, derivative, or instance rank was evaluated. No external write was made. This review does not determine the actual first failing order, a bundle classification row, the vertex functional, or any source/frontier-ledger change. The conclusion is precisely finite nonextension of the unique invariant ordinary third-neighborhood section to the seventh neighborhood, with first failure at normal order four or six.
