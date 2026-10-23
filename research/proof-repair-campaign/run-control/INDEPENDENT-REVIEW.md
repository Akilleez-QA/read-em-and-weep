# Independent bounded-run guard review

PASS for the bounded, trusted-command namespace smoke, with the stated
process-group limitations. No q-middle module, initializer or mathematical
workload was executed during this review.

Reviewed frozen bytes:

- `burn_guard.py`: `6915a220408dc3bb5045b6cfaaaef8267a6516319cdb98deca5ba5717614c6fc`
- `test_burn_guard.py`: `eeab230bc69e84126b6b47903e25a1067c608652a48f215fe45e265c94990484`
- `README.md`: `4f37533abe9592fff11d533b7d6695956ec0681e0c9aaca49368398cf291fe54`

Independent execution:

    work/swarm/math-runtime/bin/python work/swarm/run-control/test_burn_guard.py
    Ran 9 tests in 2.874s — OK, exit 0.

The fixtures exercise output capture, invalid configuration, CPU termination,
wall timeout, tiny RSS rejection, aggregate group RSS, lingering descendants,
TERM-resistant descendant escalation to KILL, and supervisor interruption.
They launch only short synthetic commands. Sleep descendants terminate after
five seconds even if the fixture harness fails; the CPU fixture has its own
one-second process limit. No existing external process group is supplied by
the fixture or the guard interface.

## Ownership and cleanup

The first draft reaped its child before later killpg calls, allowing a PID
reuse race in principle. The reviewed version repairs this: the leader
starts a new session/group and stays unreaped until every group signal has
finished. Its reserved PID anchors the group identity. SIGCHLD is reset to
default before spawning so inherited ignored disposition cannot auto-reap
that anchor. The only signal target is that created child's group ID; no
CLI-supplied PID/group is accepted. Final wait4 occurs after the last
possible group signal.

The monitor reads only numeric state for the created group/session and then
filters by exact process group. It distinguishes the unreaped zombie leader
from live descendants. A zero-exit leader with live descendants is failed
and cleaned. Monitor failures trigger TERM/KILL cleanup; inability to confirm
cleanup is recorded as failure. The helper ps processes have a timeout and
are synchronously reaped. No shell invocation is used.

## Limit and receipt semantics

Defaults are CPU60 seconds per process, wall75 seconds, sampled aggregate
RSS1,610,612,736 bytes (1.5GiB), sampling0.1 seconds. Twenty CPU-minutes is
the campaign ceiling; it is not a guard default or an aggregate-CPU promise.
RLIMIT_CPU applies per process and is inherited; wait4 records direct-child
usage including descendants it waited for, not total group CPU.

RSS is explicitly a sampled watchdog, may double-count shared pages, and
has no finite guaranteed byte overshoot bound. RLIMIT_AS is neither set nor
claimed, including on Darwin. Wall detection can lag scheduling/ps latency;
runtime and overshoot include cleanup. Darwin/Linux peak-RSS unit conversion
is explicit. These limitations are accurately recorded in receipts.

Receipts/output paths are reserved exclusively; success requires an exited,
empty live group and child exit0. Interruption, limits, launch/monitor errors,
unfinished cleanup and changed inputs cannot become success. Recorded limits,
command/executable/supervisor/input hashes, output files, sampled peaks,
signals, child status and cleanup state make the smoke reviewable. Hash
checks do not themselves validate the command's mathematical result.

## Scope boundary

This is a cooperative process-group guard, not containment against commands
that detach/change groups or against forcibly killing the supervisor with
SIGKILL. It cannot guarantee cleanup of kernel-uninterruptible processes or
recover from all OS failures; those situations must remain failed/incomplete
runs. “Cleanup complete” concerns no live member in the created group,
not the immediate disappearance of every reparented zombie. These are
compatible with the proposed trusted namespace-only smoke and do not justify
an unbounded workload or escalation of its60/75 limits.

Reviewer: frontier_plan. Review concerns the three hashes above only.
