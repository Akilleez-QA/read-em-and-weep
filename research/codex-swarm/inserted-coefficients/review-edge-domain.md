# INS-EDGE-R: increasing common-edge domain

Independent reviewer files only: `test_edge_domain.py` and this note. No producer or other reviewer files were modified. All inputs are artificial constants/owners; no actual HM source circuit is imported or evaluated.

## Finding and exact source

At10810ee877fdaf291399198ad60d7dd0c316a42d, `research/hm/null-source-integration/combined-pole/PROOF.md`, section3, Git blob9d7a5a400b48d9b8b46008fbd9fb3d79be601920, the complete numerator formula is defined on an **increasing source-first common edge**. Reversed edges use the alternating extension of the COMPLETE formula; repeated common edges vanish. Re-evaluating the raw ordered prism formula after swapping endpoints is not that alternating extension.

The minimal chosen fix is a strict constructor precondition `edge[0].source_key < edge[1].source_key`. It rejects reversed or repeated common vertices. Comparison must include the standard tag: repeated physical(carrier,mask) alone is not a repeated common vertex when standard tags differ. Distinct occurrence IDs alone do not make two equal common vertices distinct for this domain check.

## Counterexample and controls

Take a=(carrier1,mask0,standard0), b=(carrier2,mask0,standard8), with inserted fibers carrier3 above a's tag and carrier4 above b's. Set standard B=0 and all C_a,C_b,Z,Qhat factors to1. The artificial alternating source has value1 only on sorted carrier triple(2,3,4), and0 on every other sorted triple. Then the raw forward prism numerator is-1, while a raw re-evaluation after swapping a,b gives0, not+1. Hence source alternation inside the triples does not repair the edge-domain error.

The independent control implements that scalar specialization directly, without calling the producer prism on an invalid edge. The API tests require rejection of reversed/repeated common edges and acceptance of valid increasing edges. A separate control accepts equal physical labels with different standard tags. The complete valid forward `WholeNumerator` has value-1.

## Review status

Tests prepared for the constructor guard. Before its addition, the reversed and repeated-edge tests fail; the counterexample and valid-edge controls pass. Acceptance requires rerunning these five controls normally and with optimization after the producer fix. No physical evaluation or obstruction conclusion follows from this edge-domain correction.

## Post-fix acceptance

**Accepted for the increasing-edge domain correction.** Root added the exact strict `edge[0].source_key < edge[1].source_key` constructor precondition. The producer-code diff against the previously accepted provider-binding state is this single guard; README adds its domain/whole-alternation explanation, and the producer marker updates the corresponding hashes and fix note. No coefficient formula or source sorting was changed by this follow-up.

Independent discovery of **all INS tests** (`test*.py`) passed normally and with `-O`: **32 tests per mode, 0 failures, 0 errors**. This comprises9 producer tests,18 existing independent tests, and5 edge-domain controls. The pre-fix two failures above are retained as the regression evidence. After the guard, both invalid edge cases reject, the raw counterexample remains(-1,0), and valid sorted/same-physical-different-standard controls pass.

The two test processes had hard address-space limits512 MiB and CPU limits59 seconds. Measured total discovery/run times were0.553149 seconds normal and0.559743 seconds optimized; peak RSS38496 KiB and38708 KiB, respectively. No physical HM coefficient was evaluated. The all-suite command was `python -B [-O] -m unittest discover -s research/codex-swarm/inserted-coefficients -p 'test*.py'`, executed through an equivalent discovery wrapper setting these hard limits before imports.

All seven producer file hashes in the marker independently matched. `inserted_program.py` SHA256 is `a2b992864449c44de7354c25c1347a9218d3df479f6b94fad2bdb44f67f09452`; the checked producer marker SHA256 is `8da67bd5d175969669cf66737575fe0188ec6871e94c1180d19452ae9298c413`. Reviewer files are not producer marker inputs. This acceptance adds no actual source identity, full-domain admission, arithmetic release, or obstruction verdict.
