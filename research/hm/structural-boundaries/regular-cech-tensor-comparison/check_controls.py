#!/usr/bin/env python3
"""Invented finite cube-chain and regular Laurent controls; no input files read."""
from collections import defaultdict
from functools import lru_cache
from itertools import combinations, permutations, product
import json

COUNTS = defaultdict(int)

def clean(a):
    return {k: v for k, v in a.items() if v}

def plus(*terms):
    out = defaultdict(int)
    for scale, a in terms:
        for k, v in a.items():
            out[k] += scale * v
    return clean(out)

def linear(f, a):
    out = {}
    for k, v in a.items():
        out = plus((1, out), (v, f(k)))
    return out

def check(condition, label):
    # Explicit check remains live under python -O.
    if not condition:
        raise RuntimeError(label)
    COUNTS[label] += 1

def normalize(seq):
    if len(set(seq)) != len(seq):
        return {}
    inversions = sum(seq[i] > seq[j] for i in range(len(seq))
                     for j in range(i + 1, len(seq)))
    return {tuple(sorted(seq)): (-1) ** inversions}

def boundary(s):
    if len(s) <= 1:
        return {}
    return plus(*[((-1) ** i, {s[:i] + s[i + 1:]: 1})
                  for i in range(len(s))])

def qboundary(q):
    out = {}
    active_before = 0
    for i, a in enumerate(q):
        if a == 2:
            for endpoint, coefficient in ((1, 1), (0, -1)):
                face = q[:i] + (endpoint,) + q[i + 1:]
                out = plus((1, out), ((-1) ** active_before * coefficient, {face: 1}))
            active_before += 1
    return out

def box(s):
    return tuple(frozenset(v[i] for v in s) for i in range(len(s[0])))

def inside(s, b):
    return all(v[i] in b[i] for v in s for i in range(len(b)))

def cell_inside(q, b):
    return all(({0, 1} if a == 2 else {a}) <= b[i] for i, a in enumerate(q))

def cell_box(q):
    return tuple(frozenset((0, 1)) if a == 2 else frozenset((a,)) for a in q)

def minbox(s):
    return tuple(min(values) for values in box(s))

def shuffle(q, signed=True):
    active = [i for i, a in enumerate(q) if a == 2]
    out = {}
    for order in permutations(active):
        inv = sum(order[i] > order[j] for i in range(len(order))
                  for j in range(i + 1, len(order)))
        sign = (-1) ** inv if signed else 1
        current = tuple(0 if a == 2 else a for a in q)
        path = [current]
        for i in order:
            current = current[:i] + (1,) + current[i + 1:]
            path.append(current)
        out = plus((1, out), (sign, normalize(tuple(path))))
    return out

def aw_raw(s):
    """Cut formula; only a legal alternating AW when s is increasing."""
    m, n = len(s[0]), len(s) - 1
    out = {}
    for lengths in product((0, 1), repeat=m):
        if sum(lengths) != n:
            continue
        pos, sign, cell = 0, 1, []
        for i, length in enumerate(lengths):
            if length == 0:
                cell.append(s[pos][i])
            else:
                a, b = s[pos][i], s[pos + 1][i]
                if a == b:
                    sign = 0
                    break
                cell.append(2)
                sign *= b - a
                pos += 1
        if sign:
            out = plus((1, out), (sign, {tuple(cell): 1}))
    return out

def aw(s):
    return linear(aw_raw, normalize(s))

def defect(s):
    return plus((1, {s: 1}), (-1, linear(shuffle, aw(s))))

@lru_cache(None)
def K(s):
    residual = plus((1, defect(s)), (-1, linear(K, boundary(s))))
    b = minbox(s)
    return linear(lambda t: normalize((b,) + t), residual)

def p(s):
    return normalize(s)

@lru_cache(None)
def L(s):
    residual = plus((1, {s: 1}), (-1, p(s)), (-1, linear(L, boundary(s))))
    b = min(s)
    return {(b,) + t: a for t, a in residual.items()}

def simplices(vertices, degree):
    return tuple(combinations(vertices, degree + 1))

def run_chain_controls():
    for m in (2, 4):
        vertices = tuple(product((0, 1), repeat=m))
        for q in product((0, 1, 2), repeat=m):
            sh = shuffle(q)
            check(linear(boundary, sh) == linear(shuffle, qboundary(q)), "shuffle_chain_map")
            check(linear(aw, sh) == {q: 1}, "aw_shuffle_identity")
            check(all(box(s) == cell_box(q) for s in sh), "shuffle_equal_domains")
            check(linear(qboundary, qboundary(q)) == {}, "cubical_boundary_squared")
        if m == 2:
            chosen = [s for r in range(1, 5) for s in combinations(vertices, r)]
        else:
            chosen = list(combinations(vertices, 1)) + list(combinations(vertices, 2))
            for r, limit in ((3, 24), (4, 12), (5, 6), (6, 2)):
                candidates = tuple(combinations(vertices, r))
                step = max(1, len(candidates) // limit)
                chosen += list(candidates[::step][:limit])
        for s in chosen:
            check(linear(qboundary, aw(s)) == linear(aw, boundary(s)), "aw_chain_map")
            check(linear(boundary, boundary(s)) == {}, "simplicial_boundary_squared")
            check(all(cell_inside(q, box(s)) for q in aw(s)), "aw_box_support")
            check(plus((1, linear(boundary, K(s))), (1, linear(K, boundary(s)))) == defect(s),
                  "box_cone_homotopy")
            check(all(inside(t, box(s)) for t in K(s)), "homotopy_box_support")
            if len(s) >= 2:
                rev = (s[1], s[0]) + s[2:]
                check(aw(rev) == plus((-1, aw(s))), "alternating_extension")
        # Repeated tuples are retained in E, then killed by p only.
        tuple_inputs = list(product(vertices[:min(4, len(vertices))], repeat=3))
        tuple_inputs += [(vertices[-1], vertices[0]), (vertices[0],) * 4]
        for s in tuple_inputs:
            check(linear(boundary, p(s)) == linear(p, boundary(s)), "normalization_chain_map")
            rhs = plus((1, {s: 1}), (-1, p(s)))
            lhs = plus((1, linear(boundary, L(s))), (1, linear(L, boundary(s))))
            check(lhs == rhs, "all_tuple_homotopy")
            check(all(set(t) <= set(s) for t in L(s)), "all_tuple_original_vertex_support")
    s = ((0, 1), (1, 0))
    check(aw_raw(tuple(reversed(s))) != plus((-1, aw_raw(s))), "negative_unsorted_aw")
    q = (2, 2)
    check(linear(boundary, shuffle(q, False)) != linear(lambda t: shuffle(t, False), qboundary(q)),
          "negative_unsigned_shuffle")
    s = ((0, 0), (1, 1))
    check(bool(defect(s)), "nontrivial_homotopy_control")
    wrong = plus((-1, linear(boundary, K(s))), (-1, linear(K, boundary(s))))
    check(wrong != defect(s), "negative_wrong_homotopy_sign")

# Laurent polynomials use one common rational reference frame e_(0,0,0,0).
# This is intrinsic coefficient bookkeeping, not an assertion that every
# regular section has a pole-free coefficient in that rational frame.

def regular(exponents, b):
    return all((values == {0, 1}) or
               (values == {0} and exponent >= 0) or
               (values == {1} and exponent <= -2)
               for exponent, values in zip(exponents, b))

def pair(cochain, chain):
    return plus(*[(n, cochain.get(s, {})) for s, n in chain.items()])

def delta_c(f, vertices, output_degree):
    return {s: val for s in simplices(vertices, output_degree)
            if (val := pair(f, boundary(s)))}

def B(f, degree, m=4):
    return {q: val for q in product((0, 1, 2), repeat=m)
            if q.count(2) == degree and (val := pair(f, shuffle(q)))}

def A(f, vertices, degree):
    return {s: val for s in simplices(vertices, degree)
            if (val := pair(f, aw(s)))}

def kstar(f, vertices, output_degree):
    return {s: val for s in simplices(vertices, output_degree)
            if (val := pair(f, K(s)))}

def add_cochains(*terms):
    out = {}
    for scale, cochain in terms:
        for key, poly in cochain.items():
            val = plus((1, out.get(key, {})), (scale, poly))
            if val:
                out[key] = val
            elif key in out:
                del out[key]
    return out

def H(f):
    out = {}
    for q, poly in f.items():
        for exponent, coefficient in poly.items():
            for i in range(len(q)):
                if not all(q[j] == 2 and exponent[j] == -1 for j in range(i)):
                    continue
                if q[i] != 2 or exponent[i] == -1:
                    continue
                endpoint = 0 if exponent[i] >= 0 else 1
                sign = (-1) ** sum(q[j] == 2 for j in range(i))
                if endpoint == 0:
                    sign *= -1
                target = q[:i] + (endpoint,) + q[i + 1:]
                out = add_cochains((1, out), (sign * coefficient, {target: {exponent: 1}}))
    return out

def delta_t(f, output_degree, m=4):
    return {q: val for q in product((0, 1, 2), repeat=m)
            if q.count(2) == output_degree and (val := pair(f, qboundary(q)))}

def J(f, vertices, degree):
    return add_cochains((1, A(H(B(f, degree)), vertices, degree - 1)),
                        (1, kstar(f, vertices, degree - 1)))

def run_laurent_controls():
    vertices = tuple(product((0, 1), repeat=4))
    f = {
        (vertices[0], vertices[15]): {(-1, -1, -1, -1): 2},
        (vertices[0], vertices[10]): {(-1, 0, 1, 2): 3},
        (vertices[5], vertices[7]): {(0, -2, -1, -3): -1},
    }
    for s, poly in f.items():
        check(all(regular(e, box(s)) for e in poly), "invented_input_regular")
    c = delta_c(f, vertices, 2)
    check(delta_c(c, vertices, 3) == {}, "invented_c_closed")
    bc = B(c, 2)
    hbc = H(bc)
    for q, poly in bc.items():
        check(all(regular(e, cell_box(q)) for e in poly), "shuffle_pullback_regular")
    for q, poly in hbc.items():
        check(all(regular(e, cell_box(q)) for e in poly), "tensor_h_regular")
    ahb = A(hbc, vertices, 1)
    kc = kstar(c, vertices, 1)
    check(bool(ahb) and bool(kc), "both_primitive_terms_used")
    check(delta_c(ahb, vertices, 2) != c, "negative_omitted_homotopy")
    check(delta_c(kc, vertices, 2) != c, "negative_omitted_tensor_solver")
    primitive = J(c, vertices, 2)
    check(delta_c(primitive, vertices, 2) == c, "ordinary_primitive_identity")
    for s, poly in primitive.items():
        check(all(regular(e, box(s)) for e in poly), "ordinary_primitive_regular")
    # An invented nonclosed ordinary cochain requires the Jd correction.
    nonclosed = {(vertices[0], vertices[1], vertices[2]): {(0, 0, -1, -1): 1}}
    d_nonclosed = delta_c(nonclosed, vertices, 3)
    dj_nonclosed = delta_c(J(nonclosed, vertices, 2), vertices, 2)
    check(bool(d_nonclosed), "invented_nonclosed_control")
    check(dj_nonclosed != nonclosed, "negative_omitted_Jd")
    check(add_cochains((1, dj_nonclosed), (1, J(d_nonclosed, vertices, 3))) == nonclosed,
          "ordinary_full_homotopy_nonclosed")
    # Tensor identity on a fixed small monomial grid in each cell degree.
    for q in product((0, 1, 2), repeat=4):
        degree = q.count(2)
        choices = [[0, 1] if a == 0 else [-2, -3] if a == 1 else [-2, -1, 0] for a in q]
        for e in (tuple(values[0] for values in choices), tuple(values[-1] for values in choices)):
            t = {q: {e: 1}}
            dh = delta_t(H(t), degree) if degree else {}
            hd = H(delta_t(t, degree + 1)) if degree < 4 else {}
            projection = t if degree == 4 and all(a == -1 for a in e) else {}
            check(add_cochains((1, dh), (1, hd)) == add_cochains((1, t), (-1, projection)),
                  "tensor_contraction")
    top = {(2, 2, 2, 2): {(-1, -1, -1, -1): 1}}
    check(H(top) == {}, "top_harmonic_retained")
    # Explicit transition round-trip: local coefficient exponent is reference+2*frame.
    reference = (-1, 0, -3, 2)
    v, w = vertices[0], vertices[15]
    local_w = tuple(reference[i] + 2 * w[i] for i in range(4))
    converted_v = tuple(local_w[i] - 2 * (w[i] - v[i]) for i in range(4))
    check(converted_v == tuple(reference[i] + 2 * v[i] for i in range(4)), "line_frame_transition")
    check(not regular((-2, 0, 0, 0), box((vertices[0],))), "negative_outside_box_restriction")
    # All-ordered-tuple degree-2 controls on two-factor invented regular sections.
    vs = tuple(product((0, 1), repeat=2))
    all_edges = tuple(product(vs, repeat=2))
    repeated_f = {(vs[0], vs[0]): {(0, 0): 1}, (vs[3], vs[0]): {(-1, -1): 2}}
    all_c = {s: val for s in product(vs, repeat=3) if (val := pair(repeated_f, boundary(s)))}
    increasing_c = {s: val for s, val in all_c.items() if s == tuple(sorted(set(s)))}
    # Here we test only the convention homotopy, independent of degree-2 H for two factors.
    lhs = {}
    lstar_c = {s: val for s in all_edges if (val := pair(all_c, L(s)))}
    for s in product(vs, repeat=3):
        left = pair(lstar_c, boundary(s))  # L* dc = 0, since all_c is a boundary.
        right = plus((1, all_c.get(s, {})), (-1, pair(increasing_c, p(s))))
        check(left == right, "all_tuple_regular_cochain_identity")
        check(all(regular(e, box(s)) for e in left), "all_tuple_regular_cochain_domain")
    check(bool(all_c.get((vs[0], vs[0], vs[0]), {})), "repeated_component_not_discarded")

if __name__ == '__main__':
    run_chain_controls()
    run_laurent_controls()
    print(json.dumps({"status": "PASS", "checks": dict(sorted(COUNTS.items())),
                      "total_checks": sum(COUNTS.values()),
                      "scope": "Invented integer chains and Laurent monomials only; no input files read."},
                     indent=2, sort_keys=True))
