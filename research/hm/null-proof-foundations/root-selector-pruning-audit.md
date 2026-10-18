# Independent audit of formal selector pruning

The independent formal-pruner audit reports nine passing unit tests. Independent generated counts are raw4038, same-owner split-identity zeros3792, graded-block zeros96, terminal-block mismatches72, survivors78.

The recursion's signs are correct: depth1 applies H0 delta; depth2 applies -H(-1) delta to depth1. Starting j has source/target block (1,1). A left H lowers target degree; a right branch E F H raises source degree and requires target1 because E=IP is supported there. These grade checks justify the zero flags without assumptions about different-owner matrix entries.

The same-owner zero-word rules H H, H E, E H, H I, P H follow from the fixed splitting side conditions. The pruner does not silently apply these to different owners. Four-term expansion of h_i squared is killed termwise by these rules.

Each surviving tail is the last three positions; all original outer owners remain weighted. The selected degree1 blocks distinguish left versus right homotopy branches. At degree2 the M20 and M31 terminal selectors distinguish the two surviving two-homotopy words. The negative M20 terminal row cancels the J2 source minus; the M31 row instead cancels that source minus against the odd-degree right-homotopy sign. Both final degree4 row coefficients equal the staircase orientation.

This is a formal linear-map reduction only. It does not count physical polynomial products and does not supply numerical obstruction data. Additional equal-carrier identities require the separate authenticated common-frame argument; tail labels are not assumed distinct.

## Dependency scope

Companion references are identified by basename. A referenced file not supplied with this collection is an external prerequisite, not an embedded proof or a verified relative link. The reading order and unresolved conditions are listed in `proof-notes-index.md`. Reported test results describe the source audit; this proof copy does not by itself constitute a new test run.
