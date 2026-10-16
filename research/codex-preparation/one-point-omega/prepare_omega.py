"""One fixed Omega specialization PREPARATION. Physical routes always refuse.

plan/static authenticate bytes and metadata only. artificial runs a literal
invented model. This file NEVER grants physical execution, including through
its private child/body paths. A later reviewed change is needed for that task.
"""
from pathlib import Path
import argparse
import hashlib
import importlib.util
import itertools
import json
import os
import resource
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
SPEC_SHA = '55082c8ddb7182230ec1b7d5f0013a4edc8d8bf2bbfbe8337a67847b0975fd06'
PINS_SHA = 'efffbacd3866e293bd3da3e1b52e8bf6eabca812d9e342e7569e00f8185462ef'
sp = importlib.util.spec_from_file_location('omega_preparation_exact', HERE/'bounded_exact.py')
E = importlib.util.module_from_spec(sp)
sp.loader.exec_module(E)
SLOTS = ((0, 2), (0, 3), (1, 2), (1, 3))
EPSILON = (1, -1, -1, 1)
VERTICES = ((0, 0), (1, 5), (2, 10))


class PhysicalHeld(E.Refusal):
    pass


def need(ok, message):
    if not ok:
        raise E.Refusal(message)


def physical_review_required():
    raise PhysicalHeld('PREPARATION ONLY: no reviewed physical execution authority')


def read_capped(path, size=131072):
    with path.open('rb') as f:
        raw = f.read(size+1)
    need(len(raw) <= size, 'input byte cap')
    return raw


def fixed_spec():
    raw = read_capped(HERE/'spec.json')
    need(hashlib.sha256(raw).hexdigest() == SPEC_SHA, 'fixed selection drift')
    return json.loads(raw)


def authenticate_sources():
    """Byte authentication only; never substitutes values into a polynomial."""
    fixed_spec()
    raw = read_capped(HERE/'source-pins.json')
    need(hashlib.sha256(raw).hexdigest() == PINS_SHA, 'public source pin drift')
    pins = json.loads(raw)
    result = {}
    for row in pins['files']:
        p = HERE/row['local']
        need(p.resolve().is_relative_to(HERE), 'source path escapes package')
        data = read_capped(p)
        need(len(data) == row['bytes'], 'source byte length')
        need(hashlib.sha256(data).hexdigest() == row['sha256'], 'source digest drift')
        header = b'blob '+str(len(data)).encode()+b'\0'
        need(hashlib.sha1(header+data).hexdigest() == row['git_blob'], 'source Git blob drift')
        result[row['local']] = data
    return result


def static_report():
    raw = authenticate_sources()
    model = json.loads(raw['sources/model.json'])
    expected = (
        [['1,1,1,1', 1], ['0,0,0,0', -1]],
        [['5,0,0,0', -1], ['1,1,1,1', 1]],
        [['1,1,1,1', 1], ['0,5,0,0', -1]],
    )
    rows = []
    for c in range(3):
        ch = model['charts'][c]
        need(ch['di'] == ch['dp'] == expected[c], 'selected denominator definition drift')
        need(len(ch['I']) == 15 and all(len(r) == 2 for r in ch['I']), 'I shape')
        need(len(ch['P']) == 2 and all(len(r) == 15 for r in ch['P']), 'P shape')
        rows.append(dict(carrier=c, I_shape=[15, 2], P_shape=[2, 15],
                         denominator_terms=expected[c]))
    # Interval-certificate CONSTANT comparisons, not source values at x*.
    need(8*24*32*16 > 1, 'h0 interval certificate')
    need(24*32*16 > 10**4, 'h1 interval certificate')
    need(10*125*625 < 24**4*32, 'h2 interval certificate')
    return dict(status='STATIC_ONLY', source_files_authenticated=5,
                selected_metadata=rows, interval_certificate=True,
                interval='2 <= x_i <= 5/2; see PLAN.md',
                source_values_evaluated=False, physical_execution=False)


def parse_rat(m, text):
    parts = text.split('/')
    need(1 <= len(parts) <= 2, 'literal rational')
    return E.Rat(m, int(parts[0]), int(parts[1]) if len(parts) == 2 else 1)


def elementary_by_products(x):
    one = E.scalar(x[0], 1)
    v = [one] + [E.scalar(x[0], 0) for _ in range(4)]
    for a in x:
        for k in range(4, 0, -1):
            v[k] = v[k] + a*v[k-1]
    return v


def polynomial(terms, v):
    out = E.scalar(v[0], 0)
    for key, coefficient in terms:
        a = tuple(map(int, key.split(',')))
        need(len(a) == 4 and all(0 <= n <= 64 for n in a), 'sparse exponent domain')
        term = E.scalar(v[0], coefficient)
        for j, n in enumerate(a):
            term = term*E.power(v[j+1], n)
        out = out+term
    return out


def primary_primitives(model, point, denominators):
    m = point[0].m
    v = elementary_by_products([E.Jet11.coordinate(m, x, i) for i, x in enumerate(point)])
    result = []
    for c, _ in VERTICES:
        ch = model['charts'][c]
        matrices = {}
        for name, den in (('I', 'di'), ('P', 'dp')):
            d = polynomial(ch[den], v)
            need(not d.v[0].is_zero(), 'selected primitive denominator zero')
            denominators.append(dict(label=f'carrier{c}:{den}', value=d.v[0].text(), nonzero=True))
            r = d.inv()
            matrices[name] = [[polynomial(p, v)*r for p in row] for row in ch[name]]
        result.append(matrices)
    return result


def scalar_elementary_derivative(point, degree, excluded):
    """Direct subset formula; independent of the primary descending recurrence."""
    available = [k for k in range(4) if k not in excluded]
    if degree < 0 or degree > len(available):
        return E.Rat(point[0].m, 0)
    out = E.Rat(point[0].m, 0)
    for subset in itertools.combinations(available, degree):
        term = E.Rat(point[0].m, 1)
        for k in subset:
            term = term*point[k]
        out = out+term
    return out


def direct_polynomial_mixed(terms, point, pair):
    """Differentiate p(v) explicitly, then use FULL elementary chain rule.

    p_ij = sum_ab p_ab (v_a)_i(v_b)_j + sum_a p_a(v_a)_ij.
    The second sum is required even for distinct x coordinates.
    """
    m = point[0].m
    i, j = pair
    v = [scalar_elementary_derivative(point, k, ()) for k in range(1, 5)]
    vi = [scalar_elementary_derivative(point, k-1, (i,)) for k in range(1, 5)]
    vj = [scalar_elementary_derivative(point, k-1, (j,)) for k in range(1, 5)]
    vij = [scalar_elementary_derivative(point, k-2, (i, j)) for k in range(1, 5)]

    def derivative(directions):
        out = E.Rat(m, 0)
        for key, coefficient in terms:
            exponents = list(map(int, key.split(',')))
            need(len(exponents) == 4 and all(0 <= n <= 64 for n in exponents), 'sparse derivative domain')
            t = E.Rat(m, coefficient)
            for axis in directions:
                if exponents[axis] == 0:
                    t = E.Rat(m, 0)
                    break
                t = t*E.Rat(m, exponents[axis])
                exponents[axis] -= 1
            for a, n in enumerate(exponents):
                t = t*E.power(v[a], n)
            out = out+t
        return out

    p = derivative(())
    grad = [derivative((a,)) for a in range(4)]
    hess = {}
    for a in range(4):
        for b in range(a, 4):
            hess[a, b] = hess[b, a] = derivative((a, b))
    pi = sum((grad[a]*vi[a] for a in range(4)), E.Rat(m, 0))
    pj = sum((grad[a]*vj[a] for a in range(4)), E.Rat(m, 0))
    pij = sum((hess[a, b]*vi[a]*vj[b] for a in range(4) for b in range(4)), E.Rat(m, 0))
    pij = pij+sum((grad[a]*vij[a] for a in range(4)), E.Rat(m, 0))
    return E.Mixed4(m, (p, pi, pj, pij))


def secondary_primitives(model, point, pair):
    out = []
    for c, _ in VERTICES:
        ch = model['charts'][c]
        matrices = {}
        for name, den in (('I', 'di'), ('P', 'dp')):
            r = direct_polynomial_mixed(ch[den], point, pair).inv()
            matrices[name] = [[direct_polynomial_mixed(p, point, pair)*r for p in row] for row in ch[name]]
        out.append(matrices)
    return out


def core(primitives, a, b):
    return E.transpose(E.mmul(primitives[a]['P'], primitives[b]['I']))


def eye(sample):
    return [[E.scalar(sample, int(i == j)) for j in range(2)] for i in range(2)]


def checked_cores(primitives):
    cores = {(a, b): core(primitives, a, b) for a, b in ((0, 1), (1, 2), (0, 2))}
    for c in range(3):
        pi = E.mmul(primitives[c]['P'], primitives[c]['I'])
        need(E.equal_matrix(pi, eye(pi[0][0])), 'P_c I_c != identity germ')
    for k in cores.values():
        need(E.det2(k) == E.scalar(k[0][0], 1), 'transition determinant != one germ')
    need(E.equal_matrix(E.mmul(cores[1, 2], cores[0, 1]), cores[0, 2]), 'row cocycle germ mismatch')
    return cores


def qdiag(point, mask, axis):
    # This is partial_x log(nu), NOT the old gamma = mask/[x(x^2-1)].
    x = point[axis]
    lam = (x*x+1)/(2*x*(x*x-1)) if (mask >> axis) & 1 else E.Rat(x.m, 0)
    z = E.Rat(x.m, 0)
    return [[lam, z], [z, -lam]]


def covariant_second(kjet, point, left_mask, right_mask, pair):
    i, j = pair
    k = E.entries(kjet, 0)
    ki = E.entries(kjet, E.INDEX[1 << i])
    kj = E.entries(kjet, E.INDEX[1 << j])
    kij = E.entries(kjet, E.INDEX[(1 << i) | (1 << j)])
    qai, qaj = qdiag(point, left_mask, i), qdiag(point, left_mask, j)
    qbi, qbj = qdiag(point, right_mask, i), qdiag(point, right_mask, j)
    ti = E.msub(E.madd(ki, E.mmul(qbi, k)), E.mmul(k, qai))
    # Here i!=j and partial_j Q_i=0 because each Q_i depends only on x_i.
    dt = E.msub(E.madd(kij, E.mmul(qbi, kj)), E.mmul(kj, qai))
    return E.msub(E.madd(dt, E.mmul(qbj, ti)), E.mmul(ti, qaj))


def unit_frame(point, mask, pair):
    """Direct local germ of D(x)/D(x*), obtained from nu^2, not from Q."""
    m = point[0].m
    s = E.Mixed4.constant(m, 1)
    for axis in range(4):
        if (mask >> axis) & 1:
            x = E.Mixed4.coordinate(m, point[axis], axis, pair)
            w = (x*x-1)/x
            s = s*(w/E.Mixed4.constant(m, w.v[0]))
    f = s.unit_sqrt()
    need(f*f == s, 'moving frame square-root germ mismatch')
    z = E.Mixed4.constant(m, 0)
    return [[f, z], [z, f.inv()]]


def sl2_components(a):
    return ((a[0][0]-a[1][1])/2, a[0][1], a[1][0])


def omega_and_gram(h, j):
    m = h[0][0][0].m
    result = [[E.Rat(m, 0) for _ in range(2)] for _ in range(2)]
    gram = [[E.Rat(m, 0) for _ in range(3)] for _ in range(3)]
    for r, s, sign in ((0, 3, 1), (1, 2, -1), (2, 1, -1), (3, 0, 1)):
        result = E.madd(result, E.mscale(E.commutator(j[r], h[s]), E.Rat(m, sign, 8)))
        u, v = sl2_components(j[r]), sl2_components(h[s])
        for a in range(3):
            for b in range(3):
                gram[a][b] = gram[a][b]+E.Rat(m, sign)*u[a]*v[b]
    skew = (gram[1][2]-gram[2][1], gram[0][1]-gram[1][0], gram[2][0]-gram[0][2])
    from_gram = [[skew[0]/8, skew[1]/4], [skew[2]/4, -skew[0]/8]]
    need(E.equal_matrix(result, from_gram), 'Omega / cross-Gram criterion mismatch')
    return result, gram, skew


def calculate_one(model, point, label):
    """Generic point-germ kernel. Actual entry below remains hard refused.

    Intended caller integrity is assumed; arbitrary Python monkeypatching or
    manual routing of physical data through this mathematical kernel is not
    an execution authorization mechanism.
    """
    need(label in ('ARTIFICIAL', 'PHYSICAL_FIXED'), 'calculation provenance')
    m = point[0].m
    denominators = []
    for i, x in enumerate(point):
        for name, value in (('x', x), ('x2-1', x*x-1), ('curve', x*(x*x-1))):
            need(not value.is_zero(), 'curve/frame denominator zero')
            denominators.append(dict(label=f'{name}{i}', value=value.text(), nonzero=True))
    primary = checked_cores(primary_primitives(model, point, denominators))
    a, b = E.entries(primary[0, 1], 0), E.entries(primary[1, 2], 0)
    ai, bi = E.inverse2(a), E.inverse2(b)
    h, j = [], []
    for pair in SLOTS:
        va = covariant_second(primary[0, 1], point, VERTICES[0][1], VERTICES[1][1], pair)
        vb = covariant_second(primary[1, 2], point, VERTICES[1][1], VERTICES[2][1], pair)
        h.append(E.mmul(ai, va))
        j.append(E.mmul(E.mmul(E.mmul(ai, bi), vb), a))
        secondary = checked_cores(secondary_primitives(model, point, pair))
        indexes = (0, E.INDEX[1 << pair[0]], E.INDEX[1 << pair[1]], E.INDEX[(1 << pair[0]) | (1 << pair[1])])
        for edge in primary:
            for r, index in enumerate(indexes):
                need(E.equal_matrix(E.entries(primary[edge], index), E.entries(secondary[edge], r)), 'independent elementary chain-rule mismatch')
        frames = [unit_frame(point, mask, pair) for _, mask in VERTICES]
        ga = E.mmul(E.mmul(frames[1], secondary[0, 1]), E.inverse2(frames[0]))
        gb = E.mmul(E.mmul(frames[2], secondary[1, 2]), E.inverse2(frames[1]))
        gac = E.mmul(E.mmul(frames[2], secondary[0, 2]), E.inverse2(frames[0]))
        for g in (ga, gb, gac):
            need(E.det2(g) == E.scalar(g[0][0], 1), 'physical transition determinant germ mismatch')
        need(E.equal_matrix(E.mmul(gb, ga), gac), 'physical transition cocycle germ mismatch')
        av, bv = E.entries(ga, 0), E.entries(gb, 0)
        hd = E.mmul(E.inverse2(av), E.entries(ga, 3))
        jd = E.mmul(E.mmul(E.mmul(E.inverse2(av), E.inverse2(bv)), E.entries(gb, 3)), av)
        need(E.equal_matrix(h[-1], hd) and E.equal_matrix(j[-1], jd), 'direct physical-frame second derivative mismatch')
    omega, gram, skew = omega_and_gram(h, j)
    nonzero = any(not v.is_zero() for row in omega for v in row)
    text = lambda a: [[v.text() for v in row] for row in a]
    return dict(status=label+'_EXACT_GERM_COMPLETE', physical_source_evaluated=label=='PHYSICAL_FIXED',
                cross_slots_zero_based=[list(p) for p in SLOTS], gram_basis=['h', 'e', 'f'],
                H=[text(a) for a in h], J=[text(a) for a in j],
                gram=text(gram), skew=[x.text() for x in skew], omega_stripped=text(omega),
                omega_stripped_nonzero=nonzero, denominator_checks=denominators,
                independent_chain_rule_and_direct_frame_checks=True,
                PI_determinant_and_cocycle_germ_checks=True, counts=dict(m.counts),
                interpretation='one source point only; never a detector/global obstruction value',
                execution_release=False)


def _physical_body():
    physical_review_required()  # Also refuses a direct private invocation.
    # Dormant complete lowering, inspectable but NEVER executed in preparation.
    data = authenticate_sources()
    spec = fixed_spec()
    caps = spec['proposed_limits']
    m = E.Meter(caps['rational_ops'], caps['integer_ops'], caps['integer_bit_height'])
    point = [parse_rat(m, x) for x in spec['x_rationals']]
    result = calculate_one(json.loads(data['sources/model.json']), point, 'PHYSICAL_FIXED')
    result.update(spec_sha256=SPEC_SHA, source_pins_sha256=PINS_SHA,
                  physical_vertices=spec['physical_vertices'], x_rationals=spec['x_rationals'])
    return result


def artificial_model():
    """One literal invented SL2 fixture, independent of the source catalog."""
    z, o = [], [['0,0,0,0', 1]]
    v2, v3 = [['0,1,0,0', 1]], [['0,0,1,0', 1]]
    neg = lambda p: [[a, -c] for a, c in p]
    frames = [([[o, z], [z, o]], [[o, z], [z, o]]),
              ([[o, v2], [z, o]], [[o, neg(v2)], [z, o]]),
              ([[o, z], [v3, o]], [[o, z], [neg(v3), o]])]
    charts = []
    for a, inverse in frames:
        charts.append(dict(I=a+[[z, z] for _ in range(13)],
                           P=[r+[z for _ in range(13)] for r in inverse], di=o, dp=o))
    return dict(charts=charts)


def artificial_body():
    m = E.Meter()
    # An invented frame model at its own artificial point; NOT the actual data.
    return calculate_one(artificial_model(), [E.Rat(m, n) for n in (3, 4, 5, 6)], 'ARTIFICIAL')


def process_limits():
    resource.setrlimit(resource.RLIMIT_AS, (268435456, 268435456))
    resource.setrlimit(resource.RLIMIT_CPU, (15, 15))
    resource.setrlimit(resource.RLIMIT_FSIZE, (65536, 65536))
    resource.setrlimit(resource.RLIMIT_CORE, (0, 0))


def parent_limits():
    # Hard limits are inherited: a child may not raise them in preexec_fn.
    resource.setrlimit(resource.RLIMIT_AS, (268435456, 268435456))
    resource.setrlimit(resource.RLIMIT_CPU, (15, 15))
    resource.setrlimit(resource.RLIMIT_CORE, (0, 0))


def deny_descendants():
    """Cooperative child-process boundary, not a hostile-Python sandbox."""
    def refuse(*args, **kwargs):
        raise E.Refusal('child subprocess/network creation forbidden')
    subprocess.Popen = refuse
    for name in ('fork', 'forkpty', 'posix_spawn', 'posix_spawnp',
                 'execv', 'execve', 'execvp', 'execvpe', 'system'):
        if hasattr(os, name):
            setattr(os, name, refuse)
    import socket
    socket.socket = refuse


def supervise_artificial():
    parent_limits()
    start = time.monotonic()
    done = subprocess.run([sys.executable, '-I', '-B', str(Path(__file__).resolve()), '--artificial-child'],
                          timeout=20, preexec_fn=process_limits, capture_output=True,
                          env=dict(os.environ, PYTHONDONTWRITEBYTECODE='1', PYTHONPATH=''))
    need(len(done.stdout) <= 65536 and len(done.stderr) <= 65536, 'child output cap')
    need(done.returncode == 0, 'bounded child failed; inconclusive')
    result = json.loads(done.stdout)
    result['supervision'] = dict(wall_seconds=round(time.monotonic()-start, 4),
                                wall_timeout_seconds=20, child_returncode=0,
                                address_space_bytes=268435456, CPU_seconds=15,
                                parent_address_space_bytes=268435456, parent_CPU_seconds=15,
                                max_simultaneous_processes=2,
                                output_bytes_limit=65536, descendant_creation_forbidden=True)
    return result


def emit(value):
    raw = json.dumps(value, sort_keys=True).encode()
    need(len(raw) <= 65536, 'output byte cap')
    sys.stdout.buffer.write(raw+b'\n')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode', nargs='?', choices=('plan', 'static', 'artificial', 'actual'), default='plan')
    parser.add_argument('--artificial-child', action='store_true', help=argparse.SUPPRESS)
    parser.add_argument('--physical-child', action='store_true', help=argparse.SUPPRESS)
    args = parser.parse_args()
    try:
        if args.mode == 'actual' or args.physical_child:
            physical_review_required()  # Before source reads, limits or spawning.
        if args.artificial_child:
            process_limits()
            deny_descendants()
            emit(artificial_body())
        elif args.mode == 'artificial':
            emit(supervise_artificial())
        elif args.mode == 'static':
            emit(static_report())
        else:
            emit(fixed_spec())
        return 0
    except PhysicalHeld as exc:
        emit(dict(status='PHYSICAL_HELD', reason=str(exc), physical_source_evaluated=False,
                  execution_release=False, zero_value_claimed=False))
        return 3
    except (E.Refusal, MemoryError, subprocess.TimeoutExpired) as exc:
        emit(dict(status='REFUSED_INCONCLUSIVE', reason=str(exc), physical_source_evaluated=False,
                  execution_release=False, zero_value_claimed=False))
        return 3


if __name__ == '__main__':
    raise SystemExit(main())
