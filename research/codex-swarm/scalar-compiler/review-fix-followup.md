# Root follow-up: SC-R2 findings resolved

Accept the symbolic compiler scope after the two specific API fixes identified by SC-R2. The original review is retained as the pre-fix record; this follow-up supersedes its withheld acceptance for those two defects only.

The producer now requires strict non-Boolean integers for all external standard tags and for bottom-selector block indices, entry coordinates and coefficients. I inspected the narrow diff: no mathematical source construction changed. The canonical compiled artifact remains byte-identical, SHA256 `30fa190054411ea8180015be2ad3dbba65bd209abef7ddd78973a6fae024c565`. Current compiler SHA256 is `28e95b87adefaba0d4ec886a7ab272f252f376bbb1fc26e0a387bc05f896a386`.

Actual root commands, after the fix:

```sh
python -B -m unittest discover -s research/codex-swarm/scalar-compiler -v
python -B -O -m unittest discover -s research/codex-swarm/scalar-compiler -v
```

Both pass31 tests (13 producer controls and18 independent controls), including SC-R2's two previously failing regressions. The producer also refreshed its bounded controls receipt and producer-only hash marker; reviewer-owned files are outside that marker. The extra producer regression covers Boolean aliases in all four index/coefficient positions.

The independent semantic checks of all five source branches, gerbe subtraction, actual ordered J0–J3 words, twenty selectors, weighted requests and false physical gates remain applicable. This accepts an executable symbolic operator and finite demand stencil only. Physical matrix payloads, whole source/frame/domain witnesses, standard/partition coefficient realization and arithmetic admission remain unresolved. No obstruction value is inferred.
