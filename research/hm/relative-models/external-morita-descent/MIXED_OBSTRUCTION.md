# Optional mixed transition-obstruction extension

This separate conditional addendum uses Sections 1–6 of PROOF.md. It is not needed for the bounded external ideal theorem. It treats only a supplied framed transition problem and its explicit square-zero obstruction; it neither constructs the physical problem nor evaluates its class.

## Framed square-zero transition problem

This section adds an obstruction statement to the coefficient-square calculation. Work on a fixed cover carrying an actual sheaf of algebras \(\mathcal A\) with the ideals above. The explicit matrix formulas below are for this ordinary sheaf-of-algebras situation. An algebroid presentation has additional overlap algebra maps and coherence units; its defects are not given by the untwisted formulas (29)–(32). The more limited conditional statement for such a presentation is distinguished below.

Let \(\overline{\mathcal A}=\mathcal A/\mathfrak k\). Suppose two pure locally free module transition systems are supplied, of the same rank \(r\), with a specified identification over \(\mathcal A/(\mathfrak i+\mathfrak j)\). Choose compatible local frames, so that (22) combines them into actual invertible transition matrices

\[
\overline T_{ij}\in\operatorname{GL}_r(\overline{\mathcal A}(U_{ij})),
\qquad
\overline T_{ij}\overline T_{jk}=\overline T_{ik}.
\tag{29}
\]

One can take these as transitions of finite free right modules, so that the displayed matrix composition order has its usual meaning. For left-module conventions use the corresponding endomorphism convention consistently. If lifts of sections require a refinement, take a supplied common refinement. Choose actual lifts \(T_{ij}\) to \(\mathcal A\). They are invertible because \(\mathfrak k^2=0\): a lift of a matrix inverse has left and right errors in a square-zero matrix ideal, and \((1+X)^{-1}=1-X\) corrects those errors.

Set

\[
c_{ijk}=T_{ij}T_{jk}T_{ik}^{-1}-1
 \in\operatorname{Mat}_r(\mathfrak k)(U_{ijk}).
\tag{30}
\]

Define the coefficient sheaf \(\mathcal E\) by these local matrix sheaves, glued by \(X\mapsto\overline T_{ij}X\overline T_{ij}^{-1}\). This action on \(\operatorname{Mat}_r(\mathfrak k)\) is well-defined independently of the lift of \(\overline T_{ij}\), because \(\mathfrak k^2=0\). By (27) it depends only on the common classical transitions modulo \(\mathfrak i+\mathfrak j\).

Associativity of the actual matrices gives exactly

\[
c_{ijk}+c_{ikl}
 =\operatorname{Ad}(\overline T_{ij})(c_{jkl})+c_{ijl}.
\tag{31}
\]

For example expand \((T_{ij}T_{jk})T_{kl}\) and \(T_{ij}(T_{jk}T_{kl})\) as a factor \(T_{il}\) on the right; all products of two error matrices vanish. Thus \(c\) is a Čech 2-cocycle in \(\mathcal E\). For a correction \(T'_{ij}=(1+b_{ij})T_{ij}\), with \(b_{ij}\in\operatorname{Mat}_r(\mathfrak k)\), direct expansion gives

\[
c'_{ijk}=c_{ijk}+b_{ij}
 +\operatorname{Ad}(\overline T_{ij})(b_{jk})-b_{ik}.
\tag{32}
\]

Consequently \([c]\in\check H^2(\mathcal U,\mathcal E)\) is independent of the chosen lifts, and it vanishes exactly when these pure transitions admit a compatible mixed lift on this cover. A statement in sheaf cohomology requires the usual additional hypothesis that the chosen cover/complex computes it, or passage through allowed refinements. We make no unconditional Čech-to-derived-cohomology identification.

Now suppose the data come from the supplied equivariant product ambient \(\mathcal D\) and a module problem with invariant local frames. The equivariant transition maps have exactly the same matrices, with entries in \(\mathcal A\). The coefficient comparison is the actual isomorphism

\[
\operatorname{Mat}_r(K)^G
 =\operatorname{Mat}_r(K^G)
 =\operatorname{Mat}_r(\mathfrak k).
\tag{33}
\]

For an ordinary equivariant sheaf-of-algebras problem on a supplied compatible group/quotient cover, equivariance makes (33) compatible with the transition conjugations, the Čech differentials, and the error formulas (30)–(32). Thus its framed equivariant coefficient complex and its specific cocycle are identified with the downstairs complex and cocycle. This does not identify arbitrary cohomology of an upstairs geometric cover with coarse-space cohomology: the cover, group/Čech action and quotient-atlas descent must be supplied.

**Separate algebroid qualification.** In a genuine algebroid atlas the overlap maps \(F_{ij}\) and triple coherence units enter the actual transition, defect and differential formulas. Equations (29)–(32) are not those formulas with these data suppressed, and this addendum does not construct a general algebroid obstruction theory. The justified conditional transport statement is the following: if the actual equivariant framed defect complex is supplied, its coefficients are the specified module/Hom coefficient sheaves, and its differential and defect maps are the actual maps built compatibly from the supplied atlas compositions, then the invariant-frame identifications compare that complex and those maps entry by entry. This is a statement about the supplied complex; it does not license substituting the ordinary untwisted complex. The earlier source's root/Morita normalized-defect comparison must be applied in its own written noncommutative order and with its own hypotheses.

In the ordinary matrix setting the result is stable under the following actual change of frames. For a root/Morita or algebroid comparison, compatibility is asserted only when its actual compatible defect comparison has separately been supplied, as above. For an ordinary chart comparison given by units \(B_i\), transported transitions are \(T'_{ij}=B_iT_{ij}B_j^{-1}\), and direct multiplication gives

\[
c'_{ijk}=B_i c_{ijk} B_i^{-1}.
\tag{34}
\]

Here units may be read as scalar matrices in the chosen frames; (34) is a semilinear comparison over the conjugated chart ring. Because these inner maps preserve \(K,\mathfrak I,\mathfrak J\), they compare the **same mixed extension**, rather than a quotient in which the mixed term has disappeared. For the source's root-line change, its exact unnormalized error multiplier and classical normalization give the stated End-valued coefficient identification; that hypothesis is separate from external factorization.

This optional extension proves coefficientwise invariant compatibility for the ordinary framed square-zero lifting problem. In an algebroid presentation it gives only the expressly conditional comparison of its separately supplied actual defect complex. It determines no particular obstruction value and creates no pure lift or invariant frame.

