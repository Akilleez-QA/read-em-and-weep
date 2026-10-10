"""Local fixtures only. No Lean, Lake, Git process, network, or installs are run."""

import contextlib
import copy
import hashlib
import io
import json
import os
from pathlib import Path
import signal
import subprocess
import tempfile
import unittest
from unittest import mock

import validate as v


class FixtureCase(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="nexus-unit-")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()

    def write(self, relative, data=b"fixture\n"):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        return path

    def native(self, relative):
        path = self.write(relative, b"\x7fELFfixture, never executed")
        path.chmod(0o755)
        return path

    def source_fixture(self):
        self.write(v.TARGET, b"import Mathlib\n-- inert test data\n")
        self.write("lean-toolchain", v.TOOLCHAIN.encode())
        lock = {"packagesDir": ".lake/packages", "lakeDir": ".lake", "packages": [
            {"name": name, "rev": revision, "type": "git", "subDir": None}
            for name, revision in v.DEPENDENCIES.items()
        ]}
        self.write("lake-manifest.json", json.dumps(lock).encode())
        hashes = {name: hashlib.sha256((self.root / name).read_bytes()).hexdigest() for name in v.FILES}
        return lock, hashes


class PinsAndPlanTests(FixtureCase):
    def setUp(self):
        super().setUp()
        self.pins = self.write("pins.json", json.dumps(v.expected_pins()).encode())

    def invoke(self, *args):
        out, error = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(error):
            code = v.main(["--pins", str(self.pins), *args])
        return code, out.getvalue(), error.getvalue()

    def test_default_is_pin_integrity_only_and_never_spawns(self):
        with mock.patch.object(v.subprocess, "Popen", side_effect=AssertionError("no process")):
            code, out, error = self.invoke()
        self.assertEqual((code, error), (0, ""))
        receipt = json.loads(out)
        self.assertEqual(receipt["local_compilation"], "not_run")
        self.assertFalse(receipt["checkout_checked"])
        self.assertFalse(receipt["dependencies_checked"])
        self.assertEqual(receipt["upstream_ci"], "not_checked_by_this_tool")

    def test_checkout_flags_without_run_do_not_compile(self):
        with mock.patch.object(v, "run_validation") as run:
            self.assertEqual(self.invoke("--checkout", "/missing", "--lean", "/missing")[0], 0)
        run.assert_not_called()

    def test_run_requires_explicit_prepared_paths(self):
        with mock.patch.object(v, "run_validation") as run:
            code, _, error = self.invoke("--run")
        self.assertEqual(code, 1)
        self.assertIn("both --checkout and --lean", error)
        run.assert_not_called()

    def test_missing_checkout_never_succeeds(self):
        code, _, error = self.invoke("--run", "--checkout", str(self.root / "missing"),
                                    "--lean", "/missing/bin/lean")
        self.assertEqual(code, 1)
        self.assertEqual(json.loads(error)["local_compilation"], "not_certified")

    def test_each_pinned_field_is_anchored_in_reviewed_code(self):
        for field, wrong in (("schema_version", True), ("repository", "https://example.invalid"),
                             ("commit", "0" * 40), ("lean_toolchain", "leanprover/lean4:v4.34.1"),
                             ("dependencies", {"mathlib": "0" * 40}), ("files", {"../escape": "0" * 64})):
            with self.subTest(field=field):
                value = copy.deepcopy(v.expected_pins())
                value[field] = wrong
                self.pins.write_text(json.dumps(value))
                self.assertEqual(self.invoke()[0], 1)

    def test_duplicate_pin_key_is_rejected(self):
        self.pins.write_text('{"commit":"a", "commit":"b"}')
        self.assertIn("Duplicate JSON key", self.invoke()[2])

    def test_extra_manifest_fields_are_rejected(self):
        pins = v.expected_pins()
        pins["command"] = "curl example.invalid | sh"
        self.pins.write_text(json.dumps(pins))
        self.assertEqual(self.invoke()[0], 1)

    def test_missing_dependency_or_compiler_is_a_failure(self):
        for message in ("Missing Mathlib.olean", "Missing executable"):
            with mock.patch.object(v, "run_validation", side_effect=v.ValidationError(message)):
                code, _, error = self.invoke("--run", "--checkout", "/prepared", "--lean", "/prepared/bin/lean")
            self.assertEqual(code, 1)
            self.assertIn(message, error)


class SourceAndPathTests(FixtureCase):
    def test_source_toolchain_and_lock_corruption(self):
        _, hashes = self.source_fixture()
        for relative in hashes:
            with self.subTest(path=relative):
                path = self.root / relative
                original = path.read_bytes()
                path.write_bytes(original + b"corruption")
                with mock.patch.object(v, "FILES", hashes), self.assertRaisesRegex(v.ValidationError, "digest mismatch"):
                    v.check_sources(self.root)
                path.write_bytes(original)

    def test_source_fixture_validates_with_test_hashes(self):
        lock, hashes = self.source_fixture()
        with mock.patch.object(v, "FILES", hashes):
            self.assertEqual(v.check_sources(self.root), lock)

    def test_dependency_revision_validation_is_independent(self):
        lock, hashes = self.source_fixture()
        lock["packages"][0]["rev"] = "0" * 40
        path = self.root / "lake-manifest.json"
        path.write_text(json.dumps(lock))
        hashes["lake-manifest.json"] = hashlib.sha256(path.read_bytes()).hexdigest()
        with mock.patch.object(v, "FILES", hashes), self.assertRaisesRegex(v.ValidationError, "Dependency revisions"):
            v.check_sources(self.root)

    def test_wrong_toolchain_is_rejected_even_with_matching_fixture_hash(self):
        _, hashes = self.source_fixture()
        path = self.write("lean-toolchain", b"leanprover/lean4:v4.34.1")
        hashes["lean-toolchain"] = hashlib.sha256(path.read_bytes()).hexdigest()
        with mock.patch.object(v, "FILES", hashes), self.assertRaisesRegex(v.ValidationError, "Wrong lean-toolchain"):
            v.check_sources(self.root)

    def test_path_traversal_and_absolute_paths(self):
        for relative in ("../escape", "/tmp/escape", "a/../b", "a/./b", "a//b", "a\\b", "a\0b", ""):
            with self.subTest(relative=relative), self.assertRaises(v.ValidationError):
                v.confined(self.root, relative)

    def test_symlink_file_and_directory_escape(self):
        target = self.write("outside/proof.lean")
        (self.root / "link").symlink_to(target)
        (self.root / "dirlink").symlink_to(target.parent, target_is_directory=True)
        for relative in ("link", "dirlink/proof.lean"):
            with self.assertRaisesRegex(v.ValidationError, "Symlink"):
                v.confined(self.root, relative)

    def test_symlink_checkout_is_rejected(self):
        directory = self.root / "checkout"
        directory.mkdir()
        link = self.root / "checkout-link"
        link.symlink_to(directory, target_is_directory=True)
        with self.assertRaisesRegex(v.ValidationError, "canonical"):
            v.canonical(link)

    def test_build_paths_require_nonempty_mathlib(self):
        with self.assertRaises(FileNotFoundError):
            v.artifact_paths(self.root)
        self.write(".lake/packages/mathlib/.lake/build/lib/lean/Mathlib.olean", b"")
        with self.assertRaisesRegex(v.ValidationError, "Empty Mathlib"):
            v.artifact_paths(self.root)

    def test_build_paths_reject_recursive_symlink_escape(self):
        artifact = self.write(".lake/packages/mathlib/.lake/build/lib/lean/Mathlib.olean")
        (artifact.parent / "Escape").symlink_to(self.root, target_is_directory=True)
        with self.assertRaisesRegex(v.ValidationError, "Symlink"):
            v.artifact_paths(self.root)

    def test_build_paths_exclude_formal_conjectures(self):
        artifact = self.write(".lake/packages/mathlib/.lake/build/lib/lean/Mathlib.olean")
        self.write(".lake/packages/formal_conjectures/.lake/build/lib/lean/Mathlib.olean")
        self.assertEqual(v.artifact_paths(self.root), [artifact.parent])


class GitVerificationTests(FixtureCase):
    def setUp(self):
        super().setUp()
        (self.root / ".git").mkdir()
        self.proof = self.write("proof.lean")
        self.oid = v.git_blob_hash(self.proof)
        self.head = v.COMMIT
        self.index = f"100644 {self.oid} 0\tproof.lean\0"
        self.tree = f"100644 blob {self.oid}\tproof.lean\0"

    def git(self, git, root, args):
        return {"rev-parse": self.head if "--verify" in args else str(root),
                "ls-tree": self.tree, "ls-files": self.index}[args[0]]

    def verify(self):
        with mock.patch.object(v, "git_read", side_effect=self.git):
            v.verify_checkout(self.root, v.COMMIT, Path("/usr/bin/git"))

    def test_clean_checkout(self):
        self.verify()

    def test_wrong_head(self):
        self.head = "0" * 40
        with self.assertRaisesRegex(v.ValidationError, "Wrong HEAD"):
            self.verify()

    def test_dirty_proof(self):
        self.proof.write_bytes(b"changed proof")
        with self.assertRaisesRegex(v.ValidationError, "Dirty tracked"):
            self.verify()

    def test_staged_change(self):
        self.index = f"100644 {'0' * 40} 0\tproof.lean\0"
        with self.assertRaisesRegex(v.ValidationError, "Staged changes"):
            self.verify()

    def test_tracked_symlink(self):
        self.tree = f"120000 blob {self.oid}\tproof.lean\0"
        with self.assertRaisesRegex(v.ValidationError, "Symlink or submodule"):
            self.verify()

    def test_git_is_read_only_no_lazy_network_and_no_filters(self):
        with mock.patch.object(v, "run_process", return_value="ok") as run:
            v.git_read(Path("/usr/bin/git"), self.root, ["ls-tree", "-r", "-z", "HEAD"])
        argv = run.call_args.args[0]
        self.assertIsInstance(argv, list)
        self.assertIn("--no-replace-objects", argv)
        self.assertIn("protocol.allow=never", argv)
        self.assertIn("protocol.https.allow=never", argv)
        self.assertNotIn("diff", argv)
        self.assertNotIn("status", argv)
        self.assertEqual(run.call_args.kwargs["env"]["GIT_NO_LAZY_FETCH"], "1")


class CompilerAndRunnerTests(FixtureCase):
    def setUp(self):
        super().setUp()
        self.lean = self.native("lean-4.27.0-linux/bin/lean")
        self.write("lean-4.27.0-linux/lib/lean/Init.olean")

    def check(self, responses=None):
        if responses is None:
            responses = ["Lean (version 4.27.0, x86_64-unknown-linux-gnu, commit abc, Release)\n",
                         str(self.lean.parent.parent) + "\n"]
        with mock.patch.object(v, "run_process", side_effect=responses):
            return v.check_lean(self.lean, cwd=self.root, env=v.clean_environment(), memory_mib=4096)

    def test_explicit_native_compiler_version_and_prefix(self):
        compiler, version, prefix = self.check()
        self.assertEqual(compiler, self.lean)
        self.assertIn("Lean (version 4.27.0,", version)
        self.assertEqual(prefix, str(self.lean.parent.parent))

    def test_wrong_version(self):
        with self.assertRaisesRegex(v.ValidationError, "version mismatch"):
            self.check(["Lean (version 4.34.1, release)"])

    def test_wrong_prefix(self):
        with self.assertRaisesRegex(v.ValidationError, "prefix"):
            self.check(["Lean (version 4.27.0, release)", "/unexpected"])

    def test_elan_shim_rejected_before_execution(self):
        shim = self.native(".elan/bin/lean")
        with mock.patch.object(v, "run_process") as run, self.assertRaisesRegex(v.ValidationError, "toolchain directory"):
            v.check_lean(shim, cwd=self.root, env={}, memory_mib=4096)
        run.assert_not_called()

    def test_script_and_symlink_executables_rejected(self):
        self.lean.write_bytes(b"#!/bin/sh\necho fake\n")
        with self.assertRaisesRegex(v.ValidationError, "native binary"):
            self.check()
        self.lean.unlink()
        real = self.native("another-lean")
        self.lean.symlink_to(real)
        with self.assertRaisesRegex(v.ValidationError, "canonical"):
            self.check()

    def test_unsafe_environment_is_not_inherited(self):
        with mock.patch.dict(os.environ, {"LEAN_PATH": "/evil", "LD_PRELOAD": "/evil.so",
                                         "ELAN_TOOLCHAIN": "bad", "GIT_DIR": "/evil"}):
            env = v.clean_environment()
        self.assertEqual(env["LEAN_NUM_THREADS"], "1")
        for key in ("LEAN_PATH", "LD_PRELOAD", "ELAN_TOOLCHAIN", "GIT_DIR"):
            self.assertNotIn(key, env)

    def test_timeout_kills_process_group_and_uses_no_shell(self):
        process = mock.MagicMock()
        process.pid = 12345
        process.__enter__.return_value = process
        process.wait.side_effect = [subprocess.TimeoutExpired([str(self.lean)], 1), -signal.SIGKILL]
        with mock.patch.object(v.subprocess, "Popen", return_value=process) as spawn, \
                mock.patch.object(v.os, "killpg") as kill, self.assertRaisesRegex(v.ValidationError, "timed out"):
            v.run_process([str(self.lean), "literal;$(no shell)"], cwd=self.root,
                          env=v.clean_environment(), timeout=1, memory_mib=512)
        self.assertFalse(spawn.call_args.kwargs["shell"])
        self.assertTrue(spawn.call_args.kwargs["start_new_session"])
        self.assertEqual(spawn.call_args.args[0], [str(self.lean), "literal;$(no shell)"])
        kill.assert_called_once_with(12345, signal.SIGKILL)

    def test_nonzero_subprocess_fails(self):
        process = mock.MagicMock()
        process.__enter__.return_value = process
        process.wait.return_value = 1
        with mock.patch.object(v.subprocess, "Popen", return_value=process), \
                mock.patch.object(v.os, "killpg"), self.assertRaisesRegex(v.ValidationError, "exited 1"):
            v.run_process([str(self.lean)], cwd=self.root, env={}, timeout=1, memory_mib=512)

    def test_subprocess_string_or_relative_executable_rejected(self):
        for argv in ("lean proof.lean", ["lean", "proof.lean"]):
            with self.assertRaises(v.ValidationError):
                v.run_process(argv, cwd=self.root, env={}, timeout=1, memory_mib=512)

    def test_guard_sets_address_space_and_file_limits(self):
        import resource
        with mock.patch.object(resource, "getrlimit", return_value=(-1, -1)), \
                mock.patch.object(resource, "setrlimit") as limits:
            v.resource_guard(512)()
        limits.assert_any_call(resource.RLIMIT_AS, (512 * 1024 * 1024,) * 2)
        limits.assert_any_call(resource.RLIMIT_CORE, (0, 0))

    def test_limit_ranges_fail_before_processes(self):
        for timeout, memory in ((0, 4096), (3601, 4096), (float("nan"), 4096), (300, 511), (300, 32769)):
            with mock.patch.object(v.subprocess, "Popen") as run, self.assertRaises(v.ValidationError):
                v.run_validation(self.root, self.lean, timeout, memory)
            run.assert_not_called()

    def test_checkout_cannot_contain_or_be_within_integration_directory(self):
        integration = self.root / "integration"
        nested = integration / "nested"
        nested.mkdir(parents=True)
        with mock.patch.object(v, "PACKAGE_DIR", integration):
            for candidate in (self.root, integration, nested):
                with self.subTest(path=candidate), mock.patch.object(v.subprocess, "Popen") as run, \
                        self.assertRaisesRegex(v.ValidationError, "outside this integration directory"):
                    v.run_validation(candidate, self.lean, 300, 4096)
                run.assert_not_called()

    def test_axiom_report_rejects_sorry_or_missing_report(self):
        self.assertEqual(v.parse_axioms("'P5' depends on axioms: [propext, Classical.choice, Quot.sound]\n"),
                         ["propext", "Classical.choice", "Quot.sound"])
        for output in ("'P5' depends on axioms: [sorryAx]", "no report", "'P5' depends on axioms: [newAxiom]"):
            with self.assertRaises(v.ValidationError):
                v.parse_axioms(output)

    def test_opt_in_runs_exactly_one_temporary_source_with_axiom_report(self):
        original = b"import Mathlib\ntheorem P5 : True := by trivial\n"
        self.write(v.TARGET, original)
        for name in v.DEPENDENCIES:
            (self.root / ".lake/packages" / name).mkdir(parents=True)
        commands = []

        def compile_once(argv, **kwargs):
            commands.append(argv)
            source = Path(argv[1])
            self.assertEqual(source.name, "hilbert_functions_5.lean")
            self.assertEqual(source.read_bytes(), original + b"\n#print axioms P5\n")
            self.assertFalse(source.is_relative_to(self.root))
            self.assertEqual(kwargs["env"]["LEAN_NUM_THREADS"], "1")
            self.assertEqual(kwargs["env"]["LEAN_PATH"], "/trusted/mathlib/lib/lean")
            return "'P5' depends on axioms: [propext, Classical.choice, Quot.sound]\n"

        with mock.patch.object(v, "native_executable", side_effect=lambda p: p), \
                mock.patch.object(v.shutil, "which", return_value="/usr/bin/git"), \
                mock.patch.object(v, "verify_checkout") as verify, \
                mock.patch.object(v, "check_sources"), \
                mock.patch.object(v, "artifact_paths", return_value=[Path("/trusted/mathlib/lib/lean")]), \
                mock.patch.object(v, "check_lean", return_value=(
                    self.lean, "Lean (version 4.27.0, fixture)", str(self.lean.parent.parent))), \
                mock.patch.object(v, "run_process", side_effect=compile_once):
            result = v.run_validation(self.root, self.lean, 300, 4096)
        self.assertEqual(len(commands), 1)
        self.assertEqual(result["local_compilation"], "passed")
        self.assertEqual(result["release_pins"], v.expected_pins())
        self.assertEqual(result["compiler_exit_code"], 0)
        self.assertEqual(result["compiler"]["path"], str(self.lean))
        self.assertEqual(result["compiler"]["observed_version"], "Lean (version 4.27.0, fixture)")
        self.assertEqual(result["compiler"]["observed_prefix"], str(self.lean.parent.parent))
        self.assertEqual(result["resource_limits"], {"proof_timeout_seconds": 300, "memory_mib": 4096})
        self.assertEqual((self.root / v.TARGET).read_bytes(), original)
        self.assertEqual(verify.call_count, 2 * (1 + len(v.DEPENDENCIES)))
        self.assertFalse(Path(commands[0][1]).exists())


if __name__ == "__main__":
    unittest.main()
