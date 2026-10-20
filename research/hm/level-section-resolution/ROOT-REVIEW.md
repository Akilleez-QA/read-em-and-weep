# Root mathematical review

Reviewed proof SHA256: `0e7df08243d9cd60c812d29f57a88edd8bd87880670f640f7e6ac4562d740e41`.

Accepted conditional on the pinned actual module and cohomological inputs. I independently checked the levelness argument, local-duality shift, all-degree image/residue sequence, and decisive degree-nine Tor isomorphism.

The primary socle argument correctly uses the kernel inside H_d of the adjoint map to Hom(T,H_(d+1)), rather than the kernel of T tensor H_d onto H_(d+1). Nonzero multiplication and irreducibility exclude the former kernel. The Rao module is generated in degree zero by its exact restriction cokernel, so its shifted dual and every submodule have no lower socle. The actual extension consequently makes K level in degree six, of type32, without splitting it.

Graded local duality gives Ext^3(G,S(-5))=K^vee. Minimality identifies its minimal generators with the duals of the last free module. The equality 5-b=-6 fixes b=11 and yields precisely32 last summands. The stated Hilbert numerator and PR485 shift windows then reduce the remaining table to the single parameter a.

The global sections of the compact evaluation complex remain exact in the needed positions in every integer twist because intermediate cohomology of line bundles on P^4 vanishes. The only possible obstruction to G onto the residue module is supported in degrees3..6, whereas the residue module starts in degree8. This proves the actual short exact module sequence. The residue is a direct sum of25 line coordinate modules shifted by8 as an ordinary graded module, without an unproved equivariant splitting.

The mapping cone of the image-module injection has six degree-six scalar pairs from the alternating inclusion. Canceling these leaves a valid free resolution with first term140S(-8) and zeroth terms in degrees6,7. It therefore has zero Tor_1 and Tor_0 in internal degree9, regardless of any further nonminimal terms. The residue module has75 first syzygies in degree9 by the line Koszul resolutions. The exact Tor sequence forces Tor_1(G)_9 to be that whole75-dimensional space. Thus a=75, not merely a<=75.

In particular an imagined constant map from the80 degree-nine image-module second syzygies to the75 residue first syzygies cannot be used to cancel them: that is the wrong off-diagonal direction for the horseshoe resolution. The Tor argument avoids this pitfall entirely. The high-tail isomorphisms then determine every listed K entry above degree six.

This is mathematical review, not formal proof-assistant verification or recertification of every antecedent. No selected HM/source-instance evaluation, numerical rank computation or coefficient search was used. The lower cubic ambiguity, original fixed-pair quotient, source membership, higher-order lifting and algebraicity remain unresolved.
