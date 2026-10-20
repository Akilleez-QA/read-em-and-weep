# Independent audit: determinant at the sharp generator bound

## Verdict

The proposed refinement is correct under the stated assumptions. It is stronger than self-duality of the first relation representation and excludes the epsilon=+1 member of the residual length-sixteen family from **every** equivariantly determinant-trivial isolated rank-two reflexive realization, not only from the constant alternating-matrix construction.

This audit is a direct proof check, not a formal proof-assistant verification or an actual source-instance evaluation.

## Assumptions and notation

Let R be a regular local complex algebra of dimension four, with residue field C, and let a finite group H act fixing its closed point. Let M be an H-equivariant reflexive module, free on the punctured spectrum, of rank r, with an H-equivariant isomorphism M ≅ M*. Put P=Ext¹_R(M,R), Q=Ext²_R(M,R), s=μ(P), and V=Tor₁^R(P,C). Suppose dim V=r+2s. Write A=R⊗C(P/mP), with an equivariant minimal cover A→P. The determinant character of a reflexive module means the H-character on the closed fiber of its determinant line, det M=(Λ^r M)**.

## Complete audit of the construction

1. The chosen cover A→P corresponds to an invariant class in Ext¹_R(M,A*)=A*⊗R Ext¹_R(M,R). Finite-group averaging in characteristic zero allows an equivariant extension representing this class:

       0 → A* → E → M → 0.

   Its connecting map A→P is the cover. The long exact Ext sequence gives Ext¹E=0 and Ext²E≅Q. Both E and E* are reflexive and free away from the closed point: for E, use the depth lemma and torsion-freeness; duals over a normal domain are reflexive.

2. Dualizing gives

       0 → M* → E* → I → 0,    I=ker(A→P).

   From 0→I→A→P→0 and the grade-four vanishing Ext^j(P,R)=0 for j<4, one has Ext¹I=Ext²I=0. The preceding sequence therefore identifies Ext¹E* with Ext¹M*, equivariantly. Self-duality of M identifies this with P. This exact identification is what allows the second left-hand free module to be A*, rather than a free module with an uncontrolled character.

3. For every isolated reflexive N in dimension four, the dimension-shifting identity

       Ext¹(N*,R) ≅ Ext⁴(Ext²(N,R),R)

   is equivariant. Apply it to N=E*. Reflexivity identifies E** with E, so Ext¹E=0 implies D(Ext²E*)=0. Finite-length duality is faithful, hence Ext²E*=0. The identity does not require self-duality of E.

4. Use A→P≅Ext¹E* to construct a second equivariant extension

       0 → A* → F → E* → 0.

   Now Ext¹F=Ext²F=0. The depth lemma again shows that F is reflexive, so Auslander–Buchsbaum gives pd F≤2. If F had positive projective dimension, the last nonzero module in a minimal free resolution would give nonzero top Ext by Nakayama. Therefore F is free, of rank r+2s.

5. The composite F→E*→I⊂A gives an exact presentation F→A→P→0. Since A→P is minimal, I⊂mA and Tor₁(P,C)≅I/mI. The surjection F→I induces a surjection F/mF→I/mI. Both vector spaces have dimension r+2s by the equality hypothesis, hence it is an H-equivariant isomorphism. Thus F/mF≅V. This supplies the required minimality without assuming that the two extensions themselves are minimal.

6. On the punctured spectrum U, let K=ker(F|U→A|U). There are exact sequences

       0 → K → F|U → A|U → 0,
       0 → A*|U → K → M*|U → 0.

   Consequently det(M*)|U ≅ det(F)|U⊗det(A)|U^{-1}⊗det(A*)|U^{-1} ≅ det(F)|U, equivariantly. Determinant lines are reflexive, and restriction across a codimension-four complement is fully faithful for these rank-one reflexive modules. Thus the isomorphism extends over Spec R. Taking closed fibers proves

       det(V) = det(M*)|closed fiber.

   Equivalently, an equivariant basis of a free rank-one module can be obtained by lifting its one-dimensional fiber representation and averaging; Nakayama makes the lift a basis. This clarifies why the conclusion is an equality of actual H-characters.

## Canonical character and scope checks

No additional cotangent-determinant twist is needed. D is defined as Ext⁴(-,R), with its natural H-action, and already contains the canonical-character factor. The determinant calculation itself involves only A and its genuine dual A*, whose determinants cancel.

Self-duality of M alone does not mean its determinant character is trivial. The universal conclusion is det V=det M*, and in particular det V has order at most two. The triviality conclusion requires the explicitly stated equivariantly trivial determinant hypothesis.

## Application to the residual length-sixteen family

The established candidate has s=4 and dim V=10, so rank two is exactly the equality case. Its first relation representation is O₂⊕O₃⊕C_epsilon, where O₃≅O₂* and a generator g of C4 acts on C_epsilon by

       [ 0  epsilon ]
       [ 1      0   ].

The determinants of O₂ and O₃ cancel. The determinant on C_epsilon is -epsilon. For epsilon=+1, det V(g)=-1, contradicting equivariantly trivial det M. For epsilon=-1 this particular obstruction vanishes; vanishing alone is not an existence proof, but the separate explicit alternating-monad construction supplies existence in that branch.

This argument does not classify all finite-length modules of length sixteen, does not assert algebraicity for arbitrary formal modules, and does not identify or evaluate an actual HM/source defect.

## Exact text reviewed

The complete author proof at `../equality-defect-determinant/PROOF.md` was read and checked against the above derivation. Its SHA-256 is `85b5c9f9ca62ea7ae021625ecce7ea87b64dc6a1d671d09c4ae53c2c2fb1aa99`. All theorem statements and the epsilon=+1 application in that exact version are valid under their stated assumptions. No mathematical correction is required. The nonzero-P hypothesis is harmless (and not needed for the extension construction). The term “equivariant basis” is used in the representation-valued sense explicitly explained in that proof: R⊗(F/mF)≅F, not a basis of invariant individual vectors.

The equality hypothesis, equivariant self-duality, and equivariantly trivial determinant in the application must remain explicit. The final author statement requesting independent review is now discharged by this audit, not by a formal proof assistant.
