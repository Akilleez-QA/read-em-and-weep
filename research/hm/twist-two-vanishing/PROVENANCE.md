# Exact-file provenance

This publication consolidates a numerical reduction and a subsequent closure into one proof. The source texts are identified below by descriptive role and exact SHA-256, not by filesystem location. These hashes preserve the identity of the source artifacts; they do not make those artifacts public dependencies. All mathematical inputs needed for review are restated in PROOF.md or linked in SOURCES.md.

The historical reduction audit did not record a cryptographic binding to its reviewed proof. The source reduction text was subsequently updated to point to the closure. Therefore no claim is made that the old audit certified the exact final reduction bytes. A fresh independent review of the final public proof is recorded in AUDIT.md and bound to that proof's hash. The publication manifest is regenerated from the final bytes.

## Source-artifact SHA-256

- Numerical reduction and optional refinements: `807514c9ccc2e42bf38e0f326441826695d671abcc7d6c122c3b33680ffa0f76`.
- Historical reduction audit: `eb77301bb1b4cf02471e597c780f409720121c570088bf7036e8b9fb291e88b4`.
- Closure argument: `d72bfc0005ff0bcc5573c0577e055257bf76b11c08404d9e59c4c59fbcd3ff8f`.
- Historical closure audit: `a200842f7d4c5cfe34e3da9b8e6b04d9a67d744bd1c33c8ce236d7183831df66`.
- Fresh recovery verification: `3c1ae957191586e741438686442842106e925c70a10680ed4adc62f8fa854b3e`.
- Section-resolution derivation: `afc9f8a76484933f161592841c80175a072d95ca535bee0ff64489d75f542cd1`.

## Public dependency identity

The twist-one prerequisite is pinned to [ee7c4d4627c2efa07ea167a535cf1582002ef335](https://github.com/Akilleez-QA/read-em-and-weep/commit/ee7c4d4627c2efa07ea167a535cf1582002ef335) in [PR #91](https://github.com/Akilleez-QA/read-em-and-weep/pull/91). Its published PROOF.md SHA-256 is `16b368ac93ae42eb14098644aaccf19df07f19360338992cd8040e9645b188ee`. This is a stacked dependency, not a statement that the prerequisite is merged.
