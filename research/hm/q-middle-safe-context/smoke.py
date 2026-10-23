"""One approved universal namespace construction; no source solver or family loop."""
import argparse
import builtins
import inspect
import json
from pathlib import Path
import sys

assert __debug__, "Initialization assertions must remain enabled"
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--package", type=Path, default=Path(__file__).resolve().parent,
                    help="directory containing safe_context.py and provenance.json")
arguments = parser.parse_args()
CONTEXT = arguments.package.resolve()
if not (CONTEXT / "safe_context.py").is_file():
    parser.error("--package must contain safe_context.py")
if not (CONTEXT / "provenance.json").is_file():
    parser.error("--package must contain provenance.json")
sys.path.insert(0, str(CONTEXT))
original_import = builtins.__import__


def guarded_import(name, *args, **kwargs):
    if name.startswith(("universal_", "verify_", "derive_")):
        raise RuntimeError("Historical module import forbidden in this smoke: " + name)
    return original_import(name, *args, **kwargs)


builtins.__import__ = guarded_import
from safe_context import load_source_balance_api

# Exactly one factory invocation. Its literal initialization obligations run.
api = load_source_balance_api()
expected = json.loads((CONTEXT / "provenance.json").read_text())["exports"]
assert len(expected) == 144
assert set(vars(api)) == set(expected)
s = api.s
assert s.__version__ == "1.14.0"
assert all(a is b for a, b in zip(api.coords, [api.x, api.y, api.z, api.u, api.w]))
assert all(a is b for a, b in zip(api.Ms, [api.M0, api.M1, api.M2]))
for name in ("nu", "theta", "a_m", "b_m", "c_m", "chi"):
    assert getattr(api, name).is_nonzero is True
assert str(api.S) == "bs" and str(api.T) == "bt"
assert api.M * api.M == api.Q * s.eye(2)
assert api.cliff * api.spin == s.eye(2)
assert api.Kinc * api.extract == api.Pi
assert api.Pi * api.Pi == api.Pi
assert api.cliff * api.Kinc == s.zeros(2, 4)
assert api.extract * api.Kinc == s.eye(4)
assert api.J4.T == -api.J4 and api.J4.det() != 0
assert s.expand(api.quartic(api.OG) - api.gen4) == 0

# Check actual returned closure references, including shared initialization data.
closure_bindings = 0
for name in expected:
    function = getattr(api, name)
    if inspect.isfunction(function):
        for dependency, value in inspect.getclosurevars(function).nonlocals.items():
            assert dependency in expected, (name, dependency)
            assert value is getattr(api, dependency), (name, dependency)
            closure_bindings += 1

# Tiny free-symbol exterior fixtures have independent direct formula references.
alpha, beta = s.symbols("fixture_alpha fixture_beta")
f, g = {(0,): alpha}, {(1,): beta}
assert api.wedge(f, g) == {(0, 1): alpha * beta}
assert api.wedge(g, f) == {(0, 1): -alpha * beta}
assert api.wedge(f, f) == {}
assert api.add(f, api.scale(-1, f)) == {}
assert api.contract(api.coords, {(0, 1): alpha}) == {(1,): alpha * api.x, (0,): -alpha * api.y}
assert api.action(s.zeros(5), {(0, 1): alpha}) == {}
api.zero_matrix(s.zeros(2))

print(json.dumps({
    "status": "PASS", "factory_calls": 1, "exports": len(expected),
    "closure_bindings_checked": closure_bindings,
    "sympy": s.__version__, "python": sys.version.split()[0],
    "scope": "namespace, literal initialization, quartic recovery, shared closures, tiny exterior identities",
    "historical_modules_imported": False, "source_feasibility_solve": False,
    "graded_module_constructed": False, "family_loops": False,
}, sort_keys=True))
