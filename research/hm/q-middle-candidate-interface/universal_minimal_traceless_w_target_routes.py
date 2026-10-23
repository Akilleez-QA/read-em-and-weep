"""Separate minimal TARGET adapter for public746; no source-basis claim.

The 28 target intertwiners give 261 Rq / 33 Rh outputs on the existing
38 / 5 source maps. Only universal symbolic formulas are used. Frozen
public helpers remain unchanged. See MINIMAL-TRACELESS-W-TARGET-ROUTES.md.
"""
from universal_complete_traceless_w_coefficients import *

# (first representation, input representation) -> (CG order, binary degree).
# Fixed before constructing any marking-dependent template.
MINIMAL_TARGET_CHOICES = {
    ('1', 'A'): (0, 6),
    ('V', 'P4'): (0, 8), ('V', 'D5'): (0, 8),
    ('D5', 'A'): (0, 10), ('D5', 'V'): (0, 10),
    ('D5', 'P4'): (1, 8), ('D5', 'D5'): (0, 10),
    ('A', '1'): (0, 12), ('A', 'A'): (1, 10),
    ('A', 'D5'): (0, 12),
    ('P4', 'V'): (0, 12), ('P4', 'P4'): (0, 12),
    ('P4', 'D5'): (0, 12),
}


def minimal_target_routes(kind):
    """One nonzero intertwiner per admissible (first block,input type)."""
    for degree, blocks in FIRST_BLOCKS.items():
        for block in blocks:
            if kind not in TARGET_TYPES[block]:
                continue
            sigma = '1' if degree == 0 else block.split('_')[-1]
            order, target_degree = MINIMAL_TARGET_CHOICES[sigma, kind]
            yield TargetRoute(kind, degree, order, target_degree, block)


class MinimalTargetTracelessWBuilder(TracelessWBuilder):
    """Public lazy basis templates, with only the 28 fixed target routes.

    A template is constructed only when requested, then cached. The sextic
    template is valid on its typed subspace; coefficient iteration supplies
    precisely that typed source. This does not select a source basis.
    """
    def iter_coefficients(self, f, H0, expand=True):
        assert f == self.f
        rq, rh = typed_source_polynomials(f, H0)
        for category, source in [('Rq', rq), ('Rh', rh)]:
            for name, kind, p in source:
                for route in minimal_target_routes(kind):
                    yield category, name+'_'+route.label, self.apply(p, route, expand)


def build_minimal_target_traceless_w_coefficients(f, H0, expand=True):
    """Return 261 / 33 generators, not a 162 / 33 source-minimal basis."""
    builder = MinimalTargetTracelessWBuilder(f)
    rq, rh = [], []
    for category, label, matrix in builder.iter_coefficients(f, H0, expand):
        (rq if category == 'Rq' else rh).append((label, matrix))
    assert len(rq) == 261 and len(rh) == 33
    return rq, rh
