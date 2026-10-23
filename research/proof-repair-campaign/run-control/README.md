# Local bounded process-group guard

Only the small fixture suite has execution authorization in this lane.
The q-middle namespace smoke is not run by this implementation task.

Use Darwin or Linux Python with the standard library:

```sh
python burn_guard.py --receipt RUN/receipt.json --stdout RUN/stdout.txt --stderr RUN/stderr.txt --input INPUT_FILE -- COMMAND ARGUMENTS
python test_burn_guard.py
```

The three output paths must be distinct and absent. Parent directories are
created as needed. Receipts are reserved exclusively and never overwrite
an earlier run. Inputs are hashed before launch and checked again afterward;
existing regular-file arguments are included automatically. The executable,
supervisor and complete argument-vector hash are recorded separately.

Defaults: CPU soft and hard limits are both 60 seconds per process, wall
watchdog 75 seconds, aggregate process-group RSS watchdog 1,610,612,736 bytes,
and nominal sampling interval 0.1 seconds. Override with `--cpu-seconds`,
`--wall-seconds`, `--rss-bytes`, and `--sample-interval`. `/bin/ps` calls have
a 0.5-second timeout and are synchronously reaped. Its numeric `-g` selector
selects the created group on Darwin or its same-id created session on Linux;
the result is explicitly filtered by process group. Unrelated data is not
requested or written to the receipt. No shell is invoked.

RLIMIT_AS is not used or claimed. RSS is the sampled sum across live members
of the created group. RSS accounting can double-count shared pages and can
miss short-lived processes or peaks. There is **no finite guaranteed byte
overshoot bound** between samples or under scheduler delay. The receipt
records observed overshoot, sampling interval, ps timeout, sampled group
peak, and the separate OS-reported direct-child peak. Wall detection can
also be delayed by sampling and scheduling; reported runtime includes
cleanup, and wall overshoot is explicit. RLIMIT_CPU is inherited per
process, not an aggregate group limit. CPU usage comes from wait4 for the
direct child, including descendants it waited for, not every group member.

The child starts a new session and process group. On RSS/wall/interruption
or monitor failure the guard sends TERM, waits up to 0.5 seconds, then sends
KILL and waits up to 2 seconds. Only its own created group is targeted.
A zombie leader is kept unreaped until all group signaling is finished;
its reserved PID prevents an unrelated recycled process group being killed.
The guard explicitly restores default SIGCHLD handling while it owns that
child, so an inherited ignored SIGCHLD cannot silently remove this anchor.
A successfully exited leader with live children is a failed run and triggers
the same cleanup. Cleanup failure is reported, never labeled success.
This is not a sandbox: approved commands must not detach, change process
groups, or create new sessions. Such deliberate escapes cannot be contained
by a portable process-group watchdog. Kernel-uninterruptible processes and
unrecoverable OS failures may prevent cleanup; that limitation is explicit.

Exit 0 means `success`; exit 1 means a launched run failed a guard/child
condition; exit 2 means invalid configuration or inability to reserve the
receipt. An argparse syntax error can exit 2 before a receipt is reserved.
CPU-limit classification uses the exit signal and wait4 CPU measurement.
No successful run receipt certifies the mathematical result of its command.

Fixtures cover output capture, an intentional one-byte RSS threshold, a
short wall timeout, invalid limits, lingering-child cleanup and a one-second
CPU limit, aggregate multi-process RSS, KILL escalation for a TERM-ignoring
descendant, and supervisor interruption. They contain no actual HM/source
coefficients, tensors or ranks.
