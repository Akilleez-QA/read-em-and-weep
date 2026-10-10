# Independent BigInt review of #32 and #33

This directory is a review. It does not import or run the authors' checkers, and it does not regenerate source DAGs.

```sh
node research/hsd-review/32-33/bigint_review.mjs
```

Node 18 or newer, with the pinned commits already fetched. The script uses JavaScript `BigInt` only. It reads blobs with `git cat-file` and writes `results.json`. Exit 0 means every check in the script passed.

Pins:

| PR | Role | Commit |
| --- | --- | --- |
| #32 | signed-integer arithmetic | `338bec6395f89c9a8f2e14bf98d025c9c2f4c7a9` |
| #33 | recorded exact-Q image | `a0d02c2986d15d784bef8a226865cefac966bc3f` |
| #36 | numerator pin | `d7efdbeb2def45af2fcfe2253f7d1eb61ab5bf1c` |
| #37 | jet and clearing pins | `67910d41054e5237f4dbe77fb32c3d3ad5ca6897` |
| #40 | degree and factor pins | `dc60a859a0157b1d2d1b57b37324509abc22c600` |
| #41 | scalar-formula pin | `08b73637d4136f91606aad332c46cafd064417f8` |
| #39 | prior review of #36/#37 | `5147e097ed9721eb4ad55f8f5cd20cd6427acb8c` |
| #44 | prior review of #40 | `650fc2a2b653a8d74854dd8c4bbfbb4871b7e371` |

The verdict is in `REVIEW.md`.
