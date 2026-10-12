"""Identification audit of one exported cokernel.

The cokernel is called C. It is not called R. Pins are assembled before any
polynomial identity is evaluated. No length is computed.
"""

from __future__ import annotations

import json
import sympy as sp

FORMAL_CHART = "6b69eefd57098d9a0c1d9f43ed993d36e1e54bcb"
PLANE_COMPLETION = "fa685b9dd33e1c8a4336f6a8086c56f3ceb3bc3b"
HM_ATLAS = "3bdc6cb28ecd75cfefb3cb0d85f42d5bcde8cc7f"
EMPTY_DEFECT_BRANCH = "fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb"

REPO = "Akilleez-QA/read-em-and-weep"

MISSING_MAP = (
    "Chartwise matrices phi_i with entries in Q[z,X,Y,W,h]/(h^3), one on each "
    "chart of the common cover, valued in the stabilizer of the marked inclusion "
    "alpha: P -> V. Pointwise means phi_i(v_i)=v'_i for a local generator of P, "
    "which is stronger than phi(P) contained in P. "
    "The Lie sheaf of that stabilizer is Sym^2(G) tensor L^{-1}, of rank 6, "
    "not sp(G). The identities required mod h^3 on every chart and overlap are "
    "(a) g'_ij = phi_i g_ij phi_j^{-1}, "
    "(b) phi^T Omega phi = Omega with the line bundles identified exactly, "
    "(c') phi_i(v_i)=v'_i, "
    "(d) beta' composed with phi equals beta, "
    "(e) the torus weight of every entry. "
    "No such phi_i is in the pinned commits. "
    "The order-0 frame maps of the plane completion are the identity on the B "
    "basis, so they fix a generator of P, and they contain no positive power of h. "
    "The overlap formula I - h A_eta + h^2 (1/2 A_eta^2 - A_kappa) is an operator "
    "on Hamiltonian cochains. The second-normal note infers its cocycle and form "
    "preservation from a Lie homomorphism and says that it fixes the isotropic "
    "line. That inference is not the matrix identity (a) or (b), and fixing the "
    "line is not (c'). first_jet.json and the certificate primitives are those "
    "cochains. order_1.json through order_6.json are deformation-complex maps, "
    "not phi_i. The Horrocks-Mumford pullback on C^4 is not used."
)


def assemble_pins():
    """Source pins only. This function does not expand a polynomial identity."""
    return {
        "repo": REPO,
        "inputs": [
            {
                "role": "formal chart, central equation, required pairing",
                "commit": FORMAL_CHART,
                "path": "research/carrier/formal-five-parameter-chart/formal-chart.md",
            },
            {
                "role": "deformation-complex matrices, not a comparison map",
                "commit": FORMAL_CHART,
                "path": "research/carrier/formal-five-parameter-chart/data/order_1.json",
            },
            {
                "role": "plane completion, local form, and the pullback obstruction",
                "commit": PLANE_COMPLETION,
                "path": "research/carrier/plane-completion-lemma/PLANE_COMPLETION_LEMMA.md",
            },
            {
                "role": "exported base-overlap frames of the plane completion",
                "commit": PLANE_COMPLETION,
                "path": "research/carrier/plane-completion-lemma/EXPLICIT_BASE_ISOMETRY.md",
            },
            {
                "role": "finite jets on the completed plane object, not a carrier",
                "commit": PLANE_COMPLETION,
                "path": "research/carrier/plane-completion-lemma/first-normal-comparison/FIRST_NORMAL_COMPARISON.md",
            },
            {
                "role": "Horrocks-Mumford pullback on C^4, excluded",
                "commit": HM_ATLAS,
                "path": "research/hm-carrier-and-atlas.md",
                "used_as_presentation_of_R": False,
            },
            {
                "role": "named defect branch with an empty research tree, excluded",
                "commit": EMPTY_DEFECT_BRANCH,
                "path": "research/",
                "used_as_presentation_of_R": False,
            },
        ],
        "module": {
            "name": "C",
            "labelled_R": False,
            "presentation": "coker of one column u: A -> A^5",
            "generators": ["P", "E0", "E1", "E2", "D"],
            "column_w1": [
                "-(x^3+y^3)",
                "1",
                "-(x^2+y^2-z)",
                "x*y",
                "0",
            ],
            "source_column": "(-a0, W^6, -g, F, 0) at W=1, extended constantly in h",
        },
        "ambient_ring": {
            "required": (
                "a local ring of P^1 x P^3 at the central points of t0=0, "
                "or an affine chart containing those points"
            ),
            "exported": "A = Q[z, x, y, h]",
            "exported_chart": (
                "finite base chart times W != 0, with x=X/W, y=Y/W, h=H/W"
            ),
            "central_points_pinned": False,
            "central_point_note": (
                "PR #1 comment 6118997562 exports finiteness of support only; "
                "no support ideal or point list is pinned, so this chart is not "
                "certified to contain every central point"
            ),
        },
        "central_equation": {
            "equation": "t0 = 0",
            "finite_representative": "z",
            "infinity_representative": "1",
            "source_commit": FORMAL_CHART,
        },
        "required_pairing": {
            "value": "+t0 h",
            "finite_representative": "z*h",
            "source_commit": FORMAL_CHART,
        },
        "torus_weights": {
            "source_commit": FORMAL_CHART,
            "wt_z_X_Y_W_h": [2, 1, 1, 0, -1],
            "d_finite_P_E0_E1_E2": [3, 0, 2, 2],
            "d_infinity_P_E0_E1_E2": [3, 6, 0, 2],
            "t0_finite": "z",
            "t0_infinity": "1",
        },
        "structure_group": {
            "V": "symplectic rank-four completion",
            "G": "P-perpendicular, rank three, radical P",
            "P": "isotropic line, not a Lagrangian",
            "lifting_group": "subgroup of Sp(V, Omega) fixing alpha: P -> V pointwise",
            "lie_sheaf": "Sym^2(G) tensor L^{-1}",
            "lie_sheaf_rank": 6,
            "not_the_lie_sheaf": "sp(G)",
            "form": "strict L-valued equality with fixed line-bundle identifications",
            "source": "PR #1 comment 6120632461",
        },
        "proposed_comparison": {
            "full_neighborhood": (
                "not exported; the zero-section pullback pairs to 0 rather than +t0 h"
            ),
            "route": "finite jet over D2 = {h^3 = 0}",
            "target": "checked plane-completion model",
            "required_map": (
                "phi_i in the stabilizer of alpha, entries in Q[...]/(h^3), "
                "built from transition equations and gauge"
            ),
            "phi_mod_h3_exported": False,
            "hm_pullback_on_C4": "excluded",
        },
    }


def _symbols():
    z, X, Y, W, h = sp.symbols("z X Y W h")
    x, y = sp.symbols("x y")
    psi0, psi1, psi2 = sp.symbols("psi_E0 psi_E1 psi_E2")
    return z, X, Y, W, h, x, y, psi0, psi1, psi2


def plane_data():
    z, X, Y, W, h, x, y, psi0, psi1, psi2 = _symbols()
    S = X**2 + Y**2
    F = X * Y
    a0 = X**3 + Y**3
    g = S - z * W**2
    Cpoly = S**2 + z * S * W**2 + z**2 * W**4
    T = -3 * S + 2 * F
    r0 = sp.Matrix([-a0, W**6, -g, F])
    ri = sp.Matrix([-a0, S**3, -g / z, F])
    TB = sp.Matrix(
        [
            [z**3, 0, 0, 0],
            [0, 1, z * Cpoly, 0],
            [0, 0, z**4, 0],
            [0, 0, 0, z**3],
        ]
    )
    return {
        "z": z,
        "X": X,
        "Y": Y,
        "W": W,
        "h": h,
        "x": x,
        "y": y,
        "psi": (psi0, psi1, psi2),
        "S": S,
        "F": F,
        "a0": a0,
        "g": g,
        "Cpoly": Cpoly,
        "T": T,
        "r0": r0,
        "ri": ri,
        "TB": TB,
    }


def omega_E(e, e2, F, g, w):
    matrix = sp.Matrix(
        [
            [0, F, g],
            [-F, 0, w],
            [-g, -w, 0],
        ]
    )
    return (sp.Matrix(3, 1, list(e)).T * matrix * sp.Matrix(3, 1, list(e2)))[0]


def omega(p, e, d, p2, e2, d2, psi, F, g, w):
    psi_e = sum(psi[i] * e[i] for i in range(3))
    psi_e2 = sum(psi[i] * e2[i] for i in range(3))
    return (
        omega_E(e, e2, F, g, w)
        + p * d2
        - d * p2
        + psi_e * d2
        - d * psi_e2
    )


def structure_group_counts():
    """Linear algebra of Stab(alpha) on a 4-dimensional symplectic space.

    This is the corrected structure group. It is not a jet matrix phi_i.
    """
    omega = sp.Matrix(
        [
            [0, 0, 1, 0],
            [0, 0, 0, 1],
            [-1, 0, 0, 0],
            [0, -1, 0, 0],
        ]
    )
    generator = sp.Matrix([1, 0, 0, 0])
    isotropic = (generator.T * omega * generator)[0] == 0
    perpendicular = (generator.T * omega).nullspace()
    restricted = sp.Matrix(
        [
            [(u.T * omega * w)[0] for w in perpendicular]
            for u in perpendicular
        ]
    )
    radical = restricted.nullspace()
    entries = sp.Matrix(4, 4, lambda i, j: sp.symbols(f"x{i}{j}"))
    pointwise = list(entries * generator)
    infinitesimal = list(entries.T * omega + omega * entries)
    solved = sp.solve(pointwise + infinitesimal, list(entries))
    free = [symbol for symbol in list(entries) if symbol not in solved]
    b = sp.Matrix(4, 1, sp.symbols("b0 b1 b2 b3"))
    frame = sp.eye(5)
    frame[:4, 4] = b
    generator_p = sp.eye(5)[:, 0]
    return {
        "line_is_isotropic": bool(isotropic),
        "perpendicular_rank": len(perpendicular),
        "radical_of_perpendicular_rank": len(radical),
        "lagrangian_would_have_rank": 2,
        "P_is_lagrangian": len(perpendicular) == 2 and len(radical) == 0,
        "stabilizer_lie_rank": len(free),
        "sym2_of_rank3_bundle_rank": 6,
        "order0_frame_fixes_P_generator": frame * generator_p == generator_p,
        "order0_frame_depends_on_h": "h" in {str(s) for s in frame.free_symbols},
    }


def evaluate_identities():
    """Polynomial checks. Call this only after assemble_pins() has been reported."""
    data = plane_data()
    z = data["z"]
    h = data["h"]
    difference = sp.simplify(data["TB"] * data["ri"] - z**3 * data["r0"])
    gc = sp.expand(data["g"] * data["Cpoly"] + z**3 * data["W"] ** 6 - data["S"] ** 3)
    square = sp.expand(
        data["a0"] ** 2
        - (data["g"] * data["Cpoly"] + z**3 * data["W"] ** 6 + data["T"] * data["F"] ** 2)
    )
    substituted = data["r0"].subs({data["X"]: data["x"], data["Y"]: data["y"], data["W"]: 1})
    column = sp.Matrix(
        [sp.expand(substituted[i]) for i in range(4)] + [sp.Integer(0)]
    )
    expected = sp.Matrix(
        [
            -(data["x"] ** 3 + data["y"] ** 3),
            1,
            -(data["x"] ** 2 + data["y"] ** 2 - z),
            data["x"] * data["y"],
            0,
        ]
    )
    # P = (p=1, e=0, d=0). Zero-section v = E0 has d'=0. Local correction has d'=z*h.
    zero = sp.expand(
        omega(
            1, (0, 0, 0), 0,
            0, (1, 0, 0), 0,
            data["psi"], data["F"], data["g"], data["W"] ** 6,
        )
    )
    corrected = sp.expand(
        omega(
            1, (0, 0, 0), 0,
            0, (1, 0, 0), z * h,
            data["psi"], data["F"], data["g"], data["W"] ** 6,
        )
    )
    structure = structure_group_counts()
    return {
        "tb_ri_equals_z3_r0": difference == sp.Matrix.zeros(4, 1),
        "g_C_plus_z3_W6_equals_S3": gc == 0,
        "a0_square_identity": square == 0,
        "w1_column_matches_r0": column == expected,
        "column_independent_of_h": True,
        "zero_section_pairing": str(zero),
        "corrected_local_pairing": str(corrected),
        "required_finite_pairing": str(sp.expand(z * h)),
        "zero_section_matches_required": sp.expand(zero - z * h) == 0,
        "corrected_local_matches_required": sp.expand(corrected - z * h) == 0,
        "psi_E0_coefficient_in_zero_section": str(zero.coeff(data["psi"][0])),
        "structure_group": structure,
    }


def build_report(pins, identities):
    pairing_matches = identities["zero_section_matches_required"]
    report = {
        "pins": pins,
        "identities": identities,
        "cokernel_name": "C",
        "labelled_R": False,
        "gate_1_reflexivity": {
            "status": "not_run",
            "failed_inequality": None,
            "reason": (
                "The comparison map is not available, so the stop rule fires "
                "before the codimension test. No Ext module was computed. "
                "Ext^1(C,A)=Ext^2(C,A)=0 was not used."
            ),
        },
        "gate_2_identification": {
            "status": "failed",
            "route": "D2 = {h^3 = 0}",
            "actual_isomorphism_exported": False,
            "phi_mod_h3_in_stabilizer_of_alpha": False,
            "checks": {
                "a_transition": "not_run",
                "b_strict_form": "not_run",
                "c_prime_pointwise_alpha": "not_run",
                "d_beta": "not_run",
                "e_weights": "not_run",
            },
            "failed_entry": None,
            "zero_section_pairing_equals_required": pairing_matches,
            "missing_map": MISSING_MAP,
            "deformation_citation": (
                "Uniqueness of a square-zero lift of an isomorphism is H^0 of the "
                "tangent sheaf twisted by the kernel (J. Alper, Notes on "
                "Deformation Theory, UW Math 581J, Fall 2021, Prop. 2.5(1); "
                "the notes cite Hartshorne, Deformation Theory, Cor. 10.3). "
                "Applied to the stabilizer sheaf, that uniqueness does not write "
                "the entries of phi_i."
            ),
        },
        "stopped": True,
        "scope": (
            "Candidate-presentation and identification audit only. "
            "Passing this carrier gate would not prove the Weil-class theorem. "
            "This audit does not pass the carrier gate."
        ),
        "stacks": {
            "reflexivity": "https://stacks.math.columbia.edu/tag/0AVT",
            "reflexive_extension": "https://stacks.math.columbia.edu/tag/0EBJ",
        },
    }
    return report


def run():
    """Return an ordered transcript: pins, then identities, then the stop report."""
    transcript = []
    pins = assemble_pins()
    transcript.append(("pins", pins))
    identities = evaluate_identities()
    transcript.append(("identities", identities))
    transcript.append(("report", build_report(pins, identities)))
    return transcript


def main():
    transcript = run()
    for label, payload in transcript:
        print(label)
        print(json.dumps(payload, indent=2, sort_keys=True))
        print()


if __name__ == "__main__":
    main()
