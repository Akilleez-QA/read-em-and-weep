"""Explicit universal initialization. Import performs no symbolic work or frozen imports."""
from pathlib import Path
import hashlib
import json

PAYLOAD = Path(__file__).resolve().parents[1] / 'q-middle-candidate-interface'
PINNED_FILES = {'COMPLETE-55-HARMONIC-Q-MIDDLE-QUOTIENT-COEFFICIENTS.md': '3cb57cfeaa7526ebbb7e7bea9206ddc483816cea7ec093347907b277ef2619ed', 'FULL-GRADED-C-ORTHOGONAL-LEG-RESOLUTION-AND-CUBIC-SATURATION.md': '66f12a5fe2ea577a8ffdc798ee7c818c6b4f60983715f0f3c708aec9b0e4617f', 'GRADED-C-ORTHOGONAL-MODULE.sha256': 'f6daefe42915ce4603ef3b6e61502ef9e1670a40d922b8f351b2cfc4dc129c5e', 'Q-CUBIC-KERNEL-LIFT-AND-FULL-COMPLETION.sha256': '8a51729d04e922910d8b5e61e7651fbc7b006ae2a0f6a5597335660e3636e2d2', 'Q-DIVISIBLE-CUBIC-MIDDLES-HAVE-EXACT-C-REPRESENTATIVES.md': '56ae001faa6738549104a452ce9349171ffbef1bf35a6a69f1db8fac58fb8895', 'Q-LOWER-MIDDLE-HIGHER-WEIGHT-NORMAL-FORM.sha256': '08f71bb924254fb34fce3e35acd5b723b4be9c384371dfa2625cf682fd75447f', 'Q-MIDDLE-55-PLUS-10-AUDIT-INPUT.sha256': 'a05dd6e00a203cafa908b611c002824072d3109da16b3103ac1c038eb1ecdb56', 'Q-MIDDLE-CANONICAL-INTERFACE-SOURCE-DIVISION-BRIDGE.md': '633a0a9a8543e70ca505ad353954aea12174031d69ba3d601002c129515e99d6', 'Q-MULTIPLIED-LOWER-MIDDLE-COMPLETION-HAS-A-HIGHER-WEIGHT-NORMAL-FORM.md': '8fd5fba7823d837a6f4f4c32dedf8a111489d4af526a5bd609d96d9c1645737c', 'SPARSE-Q-ORTHOGONAL8-ADDITIVE-SOURCE-ADAPTER.md': 'c978fcfde2520f524c33c9092f50f0dc3fef33ec0ad759e757556343c5d31b26', 'SPARSE-Q-ORTHOGONAL8-ADDITIVE-SOURCE-ADAPTER.sha256': 'b82f4a53c708ae106b98f516882b473d67b7c8ed3d4a1ac8bbfd5eaa4c76354d', 'audit-q-middle-full-source-independent/AUDIT-Q-MIDDLE-FULL-SOURCE.md': 'df1e6f4f2f98b79128cf7f3d3f7f4809275187cfb07c092c653f96a7716dc1f5', 'audit-q-middle-full-source-independent/INDEPENDENT-AUDIT.sha256': '7368cbcd8ecb9134dbd3f448ab2343ba3e508c41175106879bce8f5e61cb5bd7', 'audit-q-middle-full-source-independent/verify_q_middle_boundary_and_quotient_independent.log': '13e5092847af09bc8d9e6a65c03e2f02d80e7855a072e4d9b372e5314791cb26', 'audit-q-middle-full-source-independent/verify_q_middle_full_source_independent.log': 'eb50e168bd997256828a5e3a1d65c991fef77f445432aa97a7f958eb9c6cc653', 'derive_c_only140_unfiltered_principal_quotient.py': '302a4198d813b89c1dcfb871154bbb057d36cec58e845e83a2cfba6c280cf9a9', 'graded-leg-module/conic_kernel_lifting.log': '0917db5f83d682f8cca0f94595e5bf32d3d825cb7bc6d1e2a30ce42259ef667f', 'graded-leg-module/conic_kernel_lifting.md': 'fcdc245a3ec48ec14cbc8de7eced4083bbc45059d9fc1a66281d6297bef60665', 'graded-leg-module/conic_kernel_lifting.py': 'a3eb28a82711594ab5413527c4625e74672710e319dd0459b9a77c9539e47e5d', 'graded-leg-module/conic_verify_kernel_lifting.py': 'b7d78841734e0124a19e7ff5faa93bd599bdc8033f64f2552da0ed6730a0b262', 'graded-leg-module/symmetric_kernel_saturation.md': '27e1713742255dca307ec26b06ff822f68e035288a9d7d3bc9d3d2f48b9ea040', 'graded-leg-module/verify_symmetric_kernel_saturation.log': 'f734f286f85a75210384540f60017fa40e4b2af44bddcecb241fa81d689ffa5f', 'graded-leg-module/verify_symmetric_kernel_saturation.py': '034db0fc16cf9072ca2acdc4e17f335f3010dbb338846d2a70ec7e360a6fb93d', 'unconditional216-source-map-cache/joint_error_rows_summary.json': 'eac1a7ab8321e228f42573eee0b1d176803e65630775116ffc414e0f00f764b2', 'universal_c_orthogonal_mixed_leg.py': '76c9261fdbc465945ab1ccd8481ec1b646cc75ce37984bcd85f11fabee1c00de', 'universal_cached_lex_module.py': '454c5440f440c1a4758618be68356170b689168bcb10e0ec060ace9b78050ed0', 'universal_complete_identity_w_coefficients.py': 'fe72704531b5afd2b14362bfb29574962837eb044fed942313062ab20e4ca619', 'universal_complete_identity_w_spin_symbols.py': 'a1090c13b7e86a3eed9641197eb263339556dcc65f7c79ac81692667e002abd8', 'universal_complete_traceless_w_coefficients.py': '1827db7b38d2ee62e6b8b3534f5581bcc02a77e5e562616feb55409c8d58821e', 'universal_complete_w_action_symbols.py': 'ba1f6793a586485afbcbf358b274e63b3102be9b1b7f40ead2204ab0c67cb304', 'universal_degree_one_c_orthogonal_module.py': 'b059c747a36cda5850f037b895bf9d6d64330cb1579161bf59cf320d485219a4', 'universal_graded_c_orthogonal_module.py': '21a3d7c3ca808c0574c9078e701b6dacde46aad74c714fa2e2673fced328f2be', 'universal_laurent_lex_module.py': 'a8ee1b8b6a8f265fe9a0a528c8a2a024ecda9761285aa9d81b90b62dadbf32bd', 'universal_minimal_traceless_w_target_routes.py': '38fd4147e0c206eafa40ad39997a7e1b71473e177c8effe4c8a5dead026dc7f0', 'universal_new_d5_leg_coefficients.py': '5b7929304e78b370e4fadd60acab2ca632c94b8eeafbccba49d3bd094222d45b', 'universal_orthogonal_leg_source_map_extension.py': '8b23436e1513b6f0ab788c313812830e62dfe48d7434424c42c4ab6f9b16cded', 'universal_physical_mixed_leg_foundation.py': '45f2405983bdbddeb9414abcf2b8c86309fd1aa237acb1b31ae4a56676c375ed', 'universal_q_cubic_kernel_lift.py': '83b79e039fb3e482ca85608369c70a3d376116be02078524d7fccdce8d26465c', 'universal_q_leg_equivariant_labeling.py': 'bf52b62c3a5761659a5896747817c74629a2ee03038295d64b6e162abd307917', 'universal_q_middle_C_interface.py': 'ef6f637c8d0c13d74a5f6b0e7c42c70c3e3b5743f0df0024b93c297723179ab5', 'universal_q_middle_completion_transport.py': '78ac1fb5ece9c5586ea6992ffa318872eb1afe765f465e948c656267085a7f0e', 'universal_q_middle_quotient_coefficients.py': '303200e58b5aafd6fd7cd6f7eeafaba1b43094c281214706eb247da37cc9fb1a', 'universal_q_orthogonal_leg_coefficients.py': '0749a26922669b57e2a3d15c46f1e549fae06d9e6f96fabb3e65f5f3386b144f', 'universal_q_orthogonal_leg_completion.py': '3864e8a3c291c0ac8e918fb88604fa5033524d999043cf35cc71fec3c71d1ecd', 'universal_regular_negative_ell_inverse.py': '08d417dbdca1c4327aca308439f42645e491f72826f9d5a7f2e38b532f363b7a', 'universal_source_balance_helpers.py': '15069fcc8138d2742bfdebd3db650efb84bd74abf1c2909585d2b6e988b276c3', 'universal_sparse_double_fischer_rows.py': '1e6512cfdebbd650ae0fce971cab5eefa6ef75d551a9d2223f5f2da8f91c1103', 'universal_sparse_orthogonal_c_source_extension.py': 'dc51cfa322fb00f08e0eb6d7971598cbeacfe76bd55c6b1f987d6fc96e348610', 'universal_sparse_positive_cubic_fischer.py': '164158f8359eb069c8f39bf1213abc5394229e8d7097bb668bd33def0ee194cb', 'universal_sparse_q_middle_source_adapter.py': '2913780fa66b0c781b97de9d2cb2fa36a1e81e77c1b5c11fdb8322a102cd3496', 'universal_sparse_q_orthogonal_c_source_adapter.py': '46c189d089baaee0cee49c5797195cadc011a36434b4f18f76b0cefe450750b4', 'universal_unconditional216_source_map.py': '53001573b7b8c585256d6283ece7f68eac9a7ce1304e11be938764541d7c5d04', 'verify_full_six_space_vertex_correction.py': 'f696bee747599e97e1abc00a91c704d8d3bafc38538476b5dc1fa267c79485ed', 'verify_graded_c_orthogonal_module.log': '3309e6b83ddfb41eb74ce2c3e4cadc44f4dae18c9aae5955a5e79cbc208de0d0', 'verify_graded_c_orthogonal_module.py': '18d8563f0297269a0a3beddc5b821db733cdd9eefab60f9bc2ff0f2afc9e015f', 'verify_q_cubic_actual_leg_bridge.log': '6453f1b8c5de13f81509bc680b6bcb5a018f47583968e6d852b3cd29b314292f', 'verify_q_cubic_actual_leg_bridge.py': 'c99ceaae5c015490ff253d39457327b7a02c60fa28cf723d287372065c52579e', 'verify_q_cubic_kernel_lift.log': '385edaad60986b105cb7054097161dbd0acc44392762d6508fabe98e43050a29', 'verify_q_cubic_kernel_lift.py': '2d2392a93d75b588aac4bb7fbf2979530f608e9b55cb78547ecb5c3703358227', 'verify_q_middle_C_interface.log': 'cc553988aa85dd8dd15ae4c530664597dc083fc954cc491a9f550686580c1429', 'verify_q_middle_C_interface.py': '9974ac06a70ef84fd7cddd2709874af378f35f28ebfddb2adb44457937696ad0', 'verify_q_middle_C_source_factor.log': '11d039ea549d21665f390d580e7cc8313fc9b3fdaeaca0db8eddb4675b2f6e13', 'verify_q_middle_C_source_factor.py': '407216ecb502354e861ba53071dae8aa5cfe163701bb2e1d58a15938a08c39fb', 'verify_q_middle_completion_transport.log': '1050e5bc61634c44691ec37e4fa6e6b97fa89e46a1c962fdf7239a10efe23c8b', 'verify_q_middle_completion_transport.py': 'cafaefd7f5974c96b3bfc00e649aab7bb1a880094e05940a097a501b8a8299a2', 'verify_q_middle_quotient_boundary.log': '174b6d20ff121ead2f6f3848fc191e381127ca222d007419e41787a9c9b0e05d', 'verify_q_middle_quotient_boundary.py': '4202c5a363274f8005de8315da3dbe4f5eff563e7326674e69ef3d71d82f4f48', 'verify_q_middle_quotient_coefficients.log': 'c6f9186df81b8a9d199987becd0e9e3329d3e72d71d66955ecd45963fe1c6ba1', 'verify_q_middle_quotient_coefficients.py': 'cee8781a4b9419d9fcc9cdd4c06e284356ad719f517025e5a55300c3e7424745', 'verify_q_middle_source_extension_bridge.log': 'cc9e9275f8daa6c5fa9894f230f9818255c8a95e4a5fa67deece5c303df06479', 'verify_q_middle_source_extension_bridge.py': '8ddec08f94ac8381be571c24313f7a6a30c301c3e99e8134416bf54b710a2b25', 'verify_q_middle_source_extension_polar_bridge.log': 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855', 'verify_q_middle_source_extension_polar_bridge.py': '9e6fdd312a63f815430fb687872e894b09573877f6fbff800f68122318319297', 'verify_sparse_q_full_cochain_external_duality.log': 'e837726c51e43f48e16b3403fd2a602febc7751083ab4a98676f027b947d36f5', 'verify_sparse_q_full_cochain_external_duality.py': 'd747e403bcd67a5ba47eca3c2db599c9c170f65fb0aa45952fe7e7d475b2c7bf', 'verify_sparse_q_middle_source_adapter.log': 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855', 'verify_sparse_q_middle_source_adapter.py': '07acc6ef811ec69a90cc8889a215ba8721ff1bee22470c7305a769ed14bfd3ed', 'verify_true_lex_curve_normal_form_audit.py': 'a3dc7a4970d264713450ad53e8ecc6d93b66b25d27368b2f47b598e447b1fcdf', 'verify_universal_monad_clifford_homotopy.py': '4e71b3c14ad9a85b099a9ee4261e4ebccd61e5aca1760462069bfe939982317b', 'verify_w_action_mixed_interface_one_ninth.py': '3fe772f53a934f05cca5d2845e23aa5102781e6b575742298f73b63bf41153db'}

def validate_dependencies(root=PAYLOAD):
    """Validate immutable input bytes before symbolic construction; no code execution."""
    root = Path(root)
    for name, expected in PINNED_FILES.items():
        actual = hashlib.sha256((root / name).read_bytes()).hexdigest()
        if actual != expected:
            raise ValueError('Dependency hash mismatch: ' + name)
    return len(PINNED_FILES)

def error_schemas(root=PAYLOAD):
    validate_dependencies(root)
    schemas = json.loads((Path(root) / 'unconditional216-source-map-cache/joint_error_rows_summary.json').read_text())['error_schemas']
    if len(schemas) != 26:
        raise ValueError('Expected complete 26-sector schema')
    return schemas

def _complete_symbols():
    import sympy as s
    (S, T) = s.symbols('bs bt')
    mon = lambda n: [S ** (n - j) * T ** j for j in range(n + 1)]
    def coeff(p, n):
        return s.Matrix([s.Poly(s.expand(p), S, T).coeff_monomial(m) for m in mon(n)])
    def tv(p, q, r):
        return s.expand(sum(((-1) ** j * s.binomial(r, j) * s.diff(p, S, r - j, T, j) * s.diff(q, S, j, T, r - j) for j in range(r + 1))))
    def rep(fun, n):
        return s.Matrix.hstack(*[coeff(fun(p), n) for p in mon(n)])
    E = rep(lambda p: S * s.diff(p, T), 3)
    F = rep(lambda p: T * s.diff(p, S), 3)
    HH = rep(lambda p: S * s.diff(p, S) - T * s.diff(p, T), 3)
    E1 = s.Matrix([[0, 1], [0, 0]])
    F1 = E1.T
    H1 = s.diag(1, -1)
    J1 = s.Matrix([[0, 1], [-1, 0]])
    J3 = s.zeros(4)
    for j in range(4):
        J3[j, 3 - j] = (-1) ** j / s.binomial(3, j)
    def simp(X):
        return X.applyfunc(s.factor)
    def op4(p):
        return rep(lambda z: tv(p, z, 2) / 12, 3)
    def op6(p):
        return rep(lambda z: tv(p, z, 3) / 120, 3)
    g = s.symbols('g0:5')
    gen4 = sum((c * m for (c, m) in zip(g, mon(4))))
    OG = op4(gen4)
    entries = [(0, 2), (0, 1), (0, 0), (1, 0), (2, 0)]
    GG = s.symbols('o0:5')
    recovery = s.solve([OG[i, j] - v for ((i, j), v) in zip(entries, GG)], g, dict=True)[0]
    def quartic(Q):
        vals = dict(zip(GG, [Q[i, j] for (i, j) in entries]))
        return s.expand(sum((recovery[c].subs(vals) * m for (c, m) in zip(g, mon(4)))))
    assert s.expand(quartic(OG) - gen4) == 0
    def mixed5(p):
        return s.Matrix.hstack(*[coeff(tv(p, z, 1) / 4, 3) for z in mon(1)])
    def spinrep(X):
        return s.trace(F * X) * E1 / 10 + s.trace(E * X) * F1 / 10 + s.trace(HH * X) * H1 / 20
    def mixedV(X):
        v = s.trace(F * X) * S * S / 10 - s.trace(HH * X) * S * T / 10 - s.trace(E * X) * T * T / 10
        return s.Matrix.hstack(*[coeff(v * z, 3) for z in mon(1)])
    def casimir_mixed(B):
        action = lambda A, A1, X: A * X - X * A1
        return action(HH, H1, action(HH, H1, B)) + 2 * (action(E, E1, action(F, F1, B)) + action(F, F1, action(E, E1, B)))
    def splitmixed(B):
        cb = casimir_mixed(B)
        return (simp((24 * B - cb) / 16), simp((cb - 8 * B) / 16))
    def build_symbols(f, H0, D, N, a):
        neg = [simp(f * Z * f.inv()) for Z in (E, F, HH)]

        def psl(X, b):
            (e, g, h) = b
            return simp(s.trace(h * X) * h / 20 + (s.trace(g * X) * e + s.trace(e * X) * g) / 10)

        def pskew(X):
            v = psl(X, (E, F, HH))
            aa = psl(X, neg)
            return [aa, v, simp(X - aa - v)]
        JP = -J3 / 2
        JS = -J1 / 3
        zero = s.zeros(6)
        rq = []
        rh = []

        def EC(X):
            out = s.zeros(6)
            out[:4, :4] = X
            return out

        def ES(X):
            out = s.zeros(6)
            out[4:, 4:] = X
            return out

        def E10(B):
            out = s.zeros(6)
            out[:4, 4:] = B
            return out

        def E01(B):
            out = s.zeros(6)
            out[4:, :4] = JS.inv() * B.T * JP
            return out

        def add(lst, name, M):
            lst.append((name, simp(M)))
        hp = quartic(H0)
        B = mixed5(hp)
        assert simp(op4(hp) - H0) == s.zeros(4)
        for (name, M) in [('C', EC(H0)), ('10', E10(B)), ('01', E01(B))]:
            add(rq, 'scalarH_' + name, a * M)
        X = simp(D * N - N * D)
        anti = simp(H0 * X + X * H0)
        (PA, PV, P4) = pskew(anti)
        add(rq, 'A_C5', EC(H0 * X - X * H0))
        for (name, Q) in [('A', PA), ('V', PV), ('P4', P4)]:
            add(rq, 'A_C' + name, EC(Q))
        add(rq, 'A_SV', ES(spinrep(PV)))
        (Vmix, Dmix) = splitmixed(X * B)
        for (name, Y) in [('V', Vmix), ('D5', Dmix)]:
            add(rq, 'A_10' + name, E10(Y))
            add(rq, 'A_01' + name, E01(Y))
        Q = simp(D * N + N * D + 20 * a * s.eye(4))
        sp = quartic(Q)
        assert simp(op4(sp) - Q) == s.zeros(4)
        scalar = tv(hp, sp, 4) / s.factorial(4) ** 2
        add(rq, 'D_SC', EC(scalar * s.eye(4)))
        add(rq, 'D_SS', ES(scalar * s.eye(2)))
        (PA, PV, P4) = pskew(H0 * Q - Q * H0)
        for (name, Y) in [('A', PA), ('V', PV), ('P4', P4)]:
            add(rq, 'D_C' + name, EC(Y))
        add(rq, 'D_SV', ES(spinrep(PV)))
        MV = mixedV(PV)
        add(rq, 'D_10V', E10(MV))
        add(rq, 'D_01V', E01(MV))
        (R0, R1, Z0, Z1) = s.symbols('pr0 pr1 nw0 nw1')
        Fpol = s.expand((s.Matrix([[Z0 ** 3, Z0 ** 2 * Z1, Z0 * Z1 ** 2, Z1 ** 3]]) * f.inv() * s.Matrix([R0 ** 3, 3 * R0 ** 2 * R1, 3 * R0 * R1 ** 2, R1 ** 3]))[0])
        cf = s.factor((f.T * J3 * f)[0, 3])
        assert simp(f.T * J3 * f - cf * J3) == s.zeros(4)
        cs = [s.Poly(Fpol, Z0, Z1).coeff_monomial(Z0 ** (3 - j) * Z1 ** j) for j in range(4)]
        (aa, bb, cc, dd) = cs
        disc = s.factor(bb ** 2 * cc ** 2 - 4 * aa * cc ** 3 - 4 * bb ** 3 * dd - 27 * aa ** 2 * dd ** 2 + 18 * aa * bb * cc * dd)
        theta = s.expand((cf ** 2 * disc).subs({R0: -T, R1: S}, simultaneous=True))
        d1 = tv(hp, sp, 2) / 144
        d2 = tv(hp * sp, theta, 8) / (s.factorial(8) * s.factorial(12) / s.factorial(4))
        p4 = tv(hp * sp, theta, 7) / (s.factorial(8) / s.factorial(1) * (s.factorial(12) / s.factorial(5)))
        for (name, pp) in [('Jordan', d1), ('Theta5', d2)]:
            b = mixed5(pp)
            add(rq, 'D_C' + name, EC(op4(pp)))
            add(rq, 'D_10' + name, E10(b))
            add(rq, 'D_01' + name, E01(b))
        sext = op6(p4)
        assert psl(sext, neg) == s.zeros(4)
        assert psl(sext, (E, F, HH)) == s.zeros(4)
        add(rq, 'D_CTheta4', EC(sext))
        add(rh, 'Rh_SC', a * EC(s.eye(4)))
        add(rh, 'Rh_SS', a * ES(s.eye(2)))
        add(rh, 'Rh_A', EC(X))
        add(rh, 'Rh_D5', EC(Q))
        b = mixed5(sp)
        add(rh, 'Rh_10', E10(b))
        add(rh, 'Rh_01', E01(b))
        assert len(rq) == 27 and len(rh) == 6
        return (rq, rh, theta)
    return locals()

def build_namespace(root=PAYLOAD):
    """Construct all universal mathematical names loaded by the frozen prefix.

    No historical module is imported or executed. No family builder is called.
    The complete-symbol helper retains its independent lexical namespace.
    """
    validate_dependencies(root)
    import sympy as s
    from itertools import combinations
    from math import comb
    # BEGIN verify_universal_monad_clifford_homotopy.py
    (x, y, z, u, w) = s.symbols('x y z u w')
    coords = [x, y, z, u, w]
    zero = {}
    def add(*fs):
        out = {}
        for f in fs:
            for (I, c) in f.items():
                out[I] = out.get(I, 0) + c
        return {I: s.expand(c) for (I, c) in out.items() if s.expand(c) != 0}
    def scale(c, f):
        return add({I: c * d for (I, d) in f.items()})
    def wedge(f, g):
        out = {}
        for (I, c) in f.items():
            for (J, d) in g.items():
                if set(I) & set(J):
                    continue
                k = sum((i > j for i in I for j in J))
                key = tuple(sorted(I + J))
                out[key] = out.get(key, 0) + (-1) ** k * c * d
        return add(out)
    def contract(v, f):
        return add(*[{I[:j] + I[j + 1:]: (-1) ** j * v[i] * c} for (I, c) in f.items() for (j, i) in enumerate(I)])
    def action(P, f):
        out = {}
        for (I, c) in f.items():
            for (j, i) in enumerate(I):
                for k in range(5):
                    term = {(k,): P[k, i]}
                    out = add(out, scale(c, wedge(wedge({I[:j]: 1}, term), {I[j + 1:]: 1})))
        return out
    def eq(f, g):
        assert not add(f, scale(-1, g)), add(f, scale(-1, g))
    def pair(F, G):
        return add(wedge(F[0], G[1]), scale(-1, wedge(F[1], G[0])))
    def vecform(M):
        return [{(i,): M[i][j] for i in range(3)} for j in range(2)]
    tau = {(0, 1, 2): 1}
    omega = {(3, 4): 1}
    Omega = wedge(tau, omega)
    ixOmega = contract(coords, Omega)
    M0 = s.Matrix([[0, 1], [0, 0]])
    M1 = s.Matrix([[0, 0], [1, 0]])
    M2 = s.Matrix([[1, 0], [0, -1]])
    Ms = [M0, M1, M2]
    M = x * M0 + y * M1 + z * M2
    Q = z * z + x * y
    assert M * M == Q * s.eye(2)
    J = s.Matrix([[0, 1], [-1, 0]])
    assert M.T * J + J * M == s.zeros(2)
    nu = s.symbols('nu', nonzero=True)
    M_pair_new = M / nu
    assert (M_pair_new * M_pair_new - Q / nu ** 2 * s.eye(2)).applyfunc(s.simplify) == s.zeros(2)
    assert nu * M_pair_new == M
    def A(v):
        return [scale(v[i], contract(coords, tau)) for i in range(2)]
    def Bcoef(v):
        return [wedge({(j,): (Ms[j] * v)[i] for j in range(3)}, omega) for i in range(2)]
    def B(v):
        return [contract(coords, f) for f in Bcoef(v)]
    (p0, p1, q0, q1) = s.symbols('p0 p1 q0 q1')
    p = s.Matrix([p0, p1])
    q = s.Matrix([q0, q1])
    eq(pair(A(p), B(q)), scale((p.T * J * M * q)[0], ixOmega))
    eq(pair(B(p), A(q)), scale(-(p.T * J * M * q)[0], ixOmega))
    eq(pair(A(p), A(q)), zero)
    eq(pair(B(p), B(q)), zero)
    cs = s.symbols('c0:8')
    C = [{}, {}]
    for k in range(2):
        (c0, c1, c2, c3) = cs[4 * k:4 * k + 4]
        sv = [s.Matrix([c0, c1]), s.Matrix([c2, c3]), s.Matrix([-c1, c2])]
        assert sum((Ms[j] * sv[j] for j in range(3)), s.zeros(2, 1)) == s.zeros(2, 1)
        for j in range(2):
            cv = contract([sv[i][j] for i in range(3)] + [0, 0], tau)
            C[j] = add(C[j], wedge(cv, {(3 + k,): 1}))
    Cx = [contract(coords, f) for f in C]
    eq(pair(A(p), Cx), zero)
    eq(pair(B(p), Cx), zero)
    (h, k, l) = s.symbols('h k l')
    D = s.zeros(5)
    D[3, 3] = h
    D[3, 4] = k
    D[4, 3] = l
    D[4, 4] = -h
    theta = s.symbols('theta', nonzero=True)
    phys = Q / theta
    r = s.Matrix([y / (2 * theta), x / (2 * theta), z / theta, 0, 0])
    ell = s.Matrix(1, 5, list(s.Matrix(1, 5, coords) * D))
    P = phys * D - r * ell
    assert s.simplify((s.Matrix(1, 5, coords) * r)[0] - phys) == 0
    assert all((s.simplify(v) == 0 for v in s.Matrix(1, 5, coords) * P))
    assert s.trace(P) == 0
    assert action(P, ixOmega) == {}
    from itertools import combinations
    basis = list(combinations(range(5), 3))
    zs = s.symbols('Z0:10')
    Z = dict(zip(basis, zs))
    eq(contract(coords, action(D, Z)), add(action(D, contract(coords, Z)), contract(list(ell), Z)))
    lhs = add(scale(phys, contract(coords, action(D, Z))), scale(-1, action(P, contract(coords, Z))))
    rform = {(i,): r[i] for i in range(5)}
    rhs = contract(coords, wedge(rform, contract(list(ell), Z)))
    eq(lhs, rhs)
    t = contract(list(ell), omega)
    for j in range(2):
        bcoef = Bcoef(p)[j]
        defect = contract(coords, wedge(rform, contract(list(ell), bcoef)))
        Lv = {(i,): (Ms[i] * p)[j] for i in range(3)}
        eq(defect, contract(coords, wedge(wedge(Lv, rform), t)))
        rc = wedge(rform, contract(list(ell), C[j]))
        assert set(rc).issubset({(0, 1, 2)})
        sD = rc.get((0, 1, 2), 0)
        eq(contract(coords, rc), scale(sD, contract(coords, tau)))
    (a_m, b_m, c_m, chi) = s.symbols('a_m b_m c_m chi', nonzero=True)
    assert s.simplify(-2 * b_m / (a_m * chi) * (-a_m * Q) - 2 * b_m * Q / chi) == 0
    left_sign = 1
    adjoint_skew_sign = -1
    right_required_sign = -1
    assert left_sign * adjoint_skew_sign == right_required_sign
    assert s.simplify(-c_m + a_m * c_m / a_m) == 0
    assert s.simplify(b_m * c_m / a_m - b_m * c_m / a_m) == 0
    # END verify_universal_monad_clifford_homotopy.py
    # BEGIN verify_full_six_space_vertex_correction.py
    G = s.Matrix([[0, s.Rational(1, 2), 0], [s.Rational(1, 2), 0, 0], [0, 0, 1]])
    Kinc = s.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [0, -1, 0, 0], [0, 0, 1, 0]])
    cliff = Ms[0].row_join(Ms[1]).row_join(Ms[2])
    spin = s.Matrix.vstack(2 * M1, 2 * M0, M2) / 3
    assert cliff * spin == s.eye(2)
    Pi = s.eye(6) - spin * cliff
    extract = s.eye(6)[:4, :] * Pi
    assert Kinc * extract == Pi and Pi * Pi == Pi
    up = s.kronecker_product(G, s.eye(2))
    low = up.inv()
    J4 = Kinc.T * s.kronecker_product(G, J) * Kinc
    assert J4.T == -J4 and J4.det() != 0
    def getp(F, extra=()):
        return s.Matrix([F[j].get(tuple(sorted(I + extra)), 0) * sgn for (I, sgn) in [((1, 2), 1), ((0, 2), -1), ((0, 1), 1)] for j in range(2)])
    def putp(p, extra=()):
        return [{tuple(sorted(I + extra)): sgn * p[2 * i + j] for (i, (I, sgn)) in enumerate([((1, 2), 1), ((0, 2), -1), ((0, 1), 1)])} for j in range(2)]
    def getY(F, extra):
        return s.Matrix([F[j].get((i,) + extra, 0) for i in range(3) for j in range(2)])
    def putY(Y, extra):
        return [{(i,) + extra: Y[2 * i + j] for i in range(3)} for j in range(2)]
    def adds(*Fs):
        return [add(*(F[j] for F in Fs)) for j in range(2)]
    def sc(c, F):
        return [scale(c, f) for f in F]
    def eqvec(F, G):
        for (f, g) in zip(F, G):
            eq(f, g)
    def zero_matrix(M):
        assert M.applyfunc(s.expand) == s.zeros(*M.shape)
    def embeddings(R):
        Radj = J4.inv() * R.T * J4
        return (Kinc * R * extract, up * Kinc * Radj * extract * low)
    def E_R(R, F):
        (Rp, RadjY) = embeddings(R)
        out = putp(Rp * getp(F))
        for i in [3, 4]:
            out = adds(out, putY(-RadjY * getY(F, (i,)), (i,)))
        return out
    def F_R(R, F):
        (Rp, RadjY) = embeddings(R)
        out = [{}, {}]
        for i in [3, 4]:
            out = adds(out, putp(Rp * getp(F, (i,)), (i,)))
        return adds(out, putY(-RadjY * getY(F, (3, 4)), (3, 4)))
    J6 = s.kronecker_product(G, J)
    def adj6(R):
        return J6.inv() * R.T * J6
    def fullE(R, F):
        out = putp(R * getp(F))
        for i in [3, 4]:
            out = adds(out, putY(-up * adj6(R) * low * getY(F, (i,)), (i,)))
        return out
    def fullF(R, F):
        out = [{}, {}]
        for i in [3, 4]:
            out = adds(out, putp(R * getp(F, (i,)), (i,)))
        return adds(out, putY(-up * adj6(R) * low * getY(F, (3, 4)), (3, 4)))
    def fullT(R, degree, F):
        out = [{}, {}]
        for (wi, i) in [(u, 3), (w, 4)]:
            out = adds(out, [contract(coords, wedge({(i,): 1}, ff)) for ff in fullE(R.diff(wi) / degree, F)])
        return out
    # END verify_full_six_space_vertex_correction.py
    # BEGIN verify_w_action_mixed_interface_one_ninth.py
    (ha, hb, hc, hd, hf) = s.symbols('ha hb hc hd hf')
    H3 = s.Matrix([[ha, hb, hc], [hd, ha, hf], [2 * hf, 2 * hc, -2 * ha]])
    H5 = s.zeros(5)
    H5[:3, :3] = H3
    HH = s.kronecker_product(-H3.T, s.eye(2))
    rh = H5 * r
    jw = contract(coords, omega)
    jvec = s.Matrix([jw.get((i,), 0) for i in range(5)])
    Hb = (s.Matrix(1, 5, coords) * D * jvec)[0]
    abase = Hb / 2
    def FW(K, F):
        out = [{}, {}]
        for i in [3, 4]:
            for j in [3, 4]:
                out = adds(out, putp(D[j, i] * K * getp(F, (i,)), (j,)))
        return out
    def FWadj(K, F):
        out = [{}, {}]
        for i in [3, 4]:
            for j in [3, 4]:
                out = adds(out, putY(-D[j, i] * up * adj6(K) * low * getY(F, (i,)), (j,)))
        return out
    def TP(K, F):
        out = [{}, {}]
        for i in range(3):
            ffirst = FW(K, [wedge({(i,): 1}, ff) for ff in F])
            fsecond = [wedge({(i,): 1}, ff) for ff in FWadj(K, F)]
            out = adds(out, sc(abase * rh[i], [contract(coords, ff) for ff in adds(ffirst, sc(-1, fsecond))]))
        return out
    # END verify_w_action_mixed_interface_one_ninth.py
    ns = _complete_symbols()
    # BEGIN derive_c_only140_unfiltered_principal_quotient.py
    (r0, r1) = s.symbols('r0 r1')
    rr = s.Matrix([r0, r1])
    vv = {x: r0 * r0, y: -r1 * r1, z: -r0 * r1}
    Ap = s.Matrix.hstack(*[extract * getp(A(s.eye(2)[:, j])) for j in range(2)])
    Av = Ap.subs(vv, simultaneous=True)
    pure = (Av * rr).applyfunc(s.expand)
    Pstd = s.Matrix.hstack(*[s.Matrix([s.Poly(e, r0, r1).coeff_monomial(r0 ** (3 - j) * r1 ** j) for e in pure]) / s.binomial(3, j) for j in range(4)])
    B6 = (Kinc * Pstd).row_join(spin)
    B6inv = B6.inv()
    JB = s.diag(-ns['J3'] / 2, -J / 3)
    assert B6.T * J6 * B6 == JB
    (FB, FC, FD) = s.symbols('FB FC FD', nonzero=True)
    FA = -9 * FB * FC / FD
    fstd = s.Matrix([[0, 0, FC, 0], [FA, 0, 0, 0], [0, 0, 0, FD], [0, FB, 0, 0]])
    fmat = Pstd * fstd
    finv = fmat.inv()
    (S, T) = s.symbols('S T')
    mons = [S ** 3, S * S * T, S * T * T, T ** 3]
    DD = lambda p: s.expand((h * S + l * T) * s.diff(p, S) + (k * S - h * T) * s.diff(p, T))
    ellpoly = -w * S + u * T
    NN = lambda p: s.expand(-2 * ellpoly * (u * s.diff(p, S) + w * s.diff(p, T)))
    rep = lambda fun: s.Matrix([[s.Poly(fun(p), S, T).coeff_monomial(m) for p in mons] for m in mons])
    (D0, N0) = (rep(DD), rep(NN))
    DP = fstd * D0 * fstd.inv()
    NP = fstd * N0 * fstd.inv()
    H0 = Pstd.inv() * extract * HH * Kinc * Pstd
    # END derive_c_only140_unfiltered_principal_quotient.py
    return locals()

def forbidden_legacy_call(*args, **kwargs):
    raise AssertionError('Old supported source_map must not receive new qB middle data.')

def initialize_sparse(instance, api, root=PAYLOAD):
    """Initialize an allocated sparse adapter using an already audited sparse API.

    The caller supplies the frozen tensor API; this module never imports it.
    The old supported source_map is forbidden on the initialized instance.
    """
    ns = build_namespace(root)
    import sympy as s
    instance.ns = ns
    instance.variables = [ns[name] for name in api.NAMES]
    instance.units = instance.variables[13:17]
    instance.load = lambda e: api.sparse_laurent(e, instance.variables, instance.units)
    instance.lmat = lambda A: [[instance.load(A[i, j]) for j in range(A.cols)] for i in range(A.rows)]
    instance.lforms = lambda F: [{I: instance.load(e) for (I, e) in ff.items() if e != 0} for ff in F]
    for name in ('cliff', 'spin', 'Kinc', 'extract', 'fmat', 'finv', 'up', 'low', 'J6', 'M', 'M2', 'J', 'B6', 'B6inv'):
        setattr(instance, name, instance.lmat(ns[name]))
    instance.J6inv = instance.lmat(ns['J6'].inv())
    instance.Jinv = instance.lmat(ns['J'].inv())
    instance.As = [instance.lforms(ns['A'](s.eye(2)[:, i])) for i in range(2)]
    instance.Bs = [instance.lforms(ns['B'](s.eye(2)[:, i])) for i in range(2)]
    Cp3 = ns['Kinc'] * ns['fmat'] * s.Matrix([[0, 0, 0], [-1, 0, 0], [0, -1, 0], [0, 0, -1]])
    Cp4 = ns['Kinc'] * ns['fmat'] * s.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0]])
    instance.Cp3 = instance.lmat(Cp3)
    instance.Cp4 = instance.lmat(Cp4)
    instance.Cs = [api.vcontract(api.vadd(api.putp(api.col(instance.Cp3, i), (3,)), api.putp(api.col(instance.Cp4, i), (4,)))) for i in range(3)]
    instance.pC = api.matadd(api.matpoly(api.var(3), instance.Cp3), api.matpoly(api.var(4), instance.Cp4))
    aa = s.Matrix.hstack(*[ns['getp'](ns['A'](ns['p'])).diff(v).diff(pp) for v in [ns['x'], ns['y'], ns['z']] for pp in ns['p']])
    instance.AAinv = instance.lmat(aa.inv())
    instance.ellmat = instance.lmat(s.Matrix([[-ns['w'], 0, 0], [ns['u'], -ns['w'], 0], [0, ns['u'], -ns['w']], [0, 0, ns['u']]]))
    instance.cv = api.columns([api.getY(api.vcontract(api.putp(api.col(api.eye(6), i))), ()) for i in range(6)])
    instance.YL = instance.lmat(s.Matrix.vstack(ns['M0'], ns['M1'], ns['M2']))
    instance.q = instance.load((ns['x'] * ns['y'] + ns['z'] ** 2) / ns['theta'])
    instance.j = {(3,): api.scale(-1, api.var(4)), (4,): api.var(3)}
    hp = s.expand((s.Matrix(1, 5, ns['coords']) * ns['rh'])[0])
    dd = s.Matrix([[ns['h'], ns['k']], [ns['l'], -ns['h']]])
    cpp = [Cp3, Cp4]
    target = [(ns['abase'] * hp * sum((dd[j, i] * cpp[i] for i in range(2)), s.zeros(6, 3))).applyfunc(s.expand) for j in range(2)]
    tp = [api.matfun(instance.lmat(A), api.projectD) for A in target]
    instance.targets = [api.vcontract(api.vadd(api.putp(api.col(tp[0], i), (3,)), api.putp(api.col(tp[1], i), (4,)))) for i in range(3)]
    assert all((not api.lapD(p) for F in instance.targets for f in F for p in f.values()))
    instance.source_map = forbidden_legacy_call
    return instance
