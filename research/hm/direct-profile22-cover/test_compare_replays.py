"""Compare both independent finite-cover implementations, including every stage.

Run with Python 3 or Python 3 -O; no external dependencies or source downloads.
"""
from contextlib import redirect_stdout
import importlib.util
from io import StringIO
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
checks = 0


def require(condition, label):
    global checks
    checks += 1
    if not condition:
        raise RuntimeError(label)


def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, ROOT / filename)
    module = importlib.util.module_from_spec(spec)
    with redirect_stdout(StringIO()):
        spec.loader.exec_module(module)
    return module


author = load("direct22_author", "verify_direct22_cover.py")
independent = load("direct22_independent", "independent_mckay_replay.py")
require(set(author.shape_domain()) == set(independent.all_shapes), "complete domains differ")
require(len(author.stages) == len(independent.stages) == 6, "unexpected stage number")
for i, (left, right) in enumerate(zip(author.stages, independent.stages)):
    require(left == right, f"complete stage {i} differs")
for name in author.names:
    for degree in range(31):
        left = dict(zip(author.names, author.prod(name, degree)))
        right = dict(zip(independent.names, independent.tensor(name, degree)))
        require(left == right, f"product {name} tensor Sym^{degree} differs")
require(author.expected == independent.expected, "ordered expected pairs differ")
require(author.survivors == independent.stages[-1], "ordered survivor sets differ")
require(len(author.mutation_controls) == 7, "counterfactual controls missing")
require(author.necessary_cover(lo=-10, hi=26)[0] == independent.expected,
        "wider-window survivor set differs")
result = {
    "status": "pass",
    "comparison_checks": checks,
    "shape_count": len(independent.all_shapes),
    "stage_counts": [len(stage) for stage in independent.stages],
    "products_compared": 279,
    "counterfactual_controls_replayed": len(author.mutation_controls),
    "wider_window": [-10, 26],
    "scope": "Equality of complete abstract domains, every filter-stage set, tensor products, and ordered survivor pairs; not an actual-map rank calculation.",
}
print(json.dumps(result, indent=2))
