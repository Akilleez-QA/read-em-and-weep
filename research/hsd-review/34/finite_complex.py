"""Independent rebuild of the pinned full-sign finite complex.

The differential rules are the published four-term monad and the full-sign
harmonic transfer. Matrix arithmetic below uses Python integers only.
"""

from __future__ import annotations

RANKS = (5, 15, 10, 2)


def _epsilon(values):
    if len(set(values)) != 5:
        return 0
    inversions = 0
    for i in range(5):
        for j in range(i + 1, 5):
            inversions += values[i] > values[j]
    return -1 if inversions % 2 else 1


def _plus(i):
    return ((i + 2) % 5, (i + 3) % 5)


def _minus(i):
    return ((i + 1) % 5, (i + 4) % 5)


def gamma_tensor():
    gamma = [[[0] * 5 for _ in range(5)] for _ in range(15)]
    for row in range(15):
        for column in range(5):
            for variable in range(5):
                right = _plus(column) if row < 5 or row >= 10 else _minus(column)
                if row < 5:
                    left = _plus(row)
                elif row < 10:
                    left = _minus(row - 5)
                else:
                    left = _minus(row - 10)
                gamma[row][column][variable] = _epsilon((variable, *right, *left))
    return gamma


def monad_columns(gamma):
    """Columns of gamma, delta_K, and ev as (target, variable, coefficient)."""
    columns = [[[] for _ in range(RANKS[level])] for level in range(3)]
    for source in range(5):
        for target in range(15):
            for variable in range(5):
                coefficient = gamma[target][source][variable]
                if coefficient:
                    columns[0][source].append((target, variable, coefficient))
    for i in range(5):
        for column, height, pair in (
            (i, 0, _plus(i)),
            (i + 5, 1, _minus(i)),
            (i + 10, 0, _minus(i)),
            (i + 10, 1, _plus(i)),
        ):
            first, second = pair
            columns[1][column].append((5 * height + second, first, 1))
            columns[1][column].append((5 * height + first, second, -1))
    for block in range(2):
        for variable in range(5):
            columns[2][block * 5 + variable].append((block, variable, 1))
    incoming = []
    for level, columns_at_level in enumerate(columns):
        rows = []
        for target in range(RANKS[level + 1]):
            terms = []
            for source, entries in enumerate(columns_at_level):
                for row, variable, coefficient in entries:
                    if row == target:
                        terms.append((source, variable, coefficient))
            rows.append(terms)
        incoming.append(rows)
    return columns, incoming


SUBSETS = [[] for _ in range(5)]
for mask in range(16):
    exponents = tuple((mask >> bit) & 1 for bit in range(4))
    SUBSETS[sum(exponents)].append(exponents)


def _monomials(low, high):
    return [
        (a, b, c, d)
        for a in range(low, high + 1)
        for b in range(low, high + 1)
        for c in range(low, high + 1)
        for d in range(low, high + 1)
    ]


def _blocks(internal_degree):
    return [
        (source, source + internal_degree)
        for source in range(4)
        if 0 <= source + internal_degree < 4
    ]


def _basis(internal_degree, positive_chart):
    low_degree = internal_degree - 2
    if positive_chart == 4:
        exponents = _monomials(low_degree + 1, -1)
    else:
        exponents = _monomials(0, low_degree)
    vectors = []
    for source, target in _blocks(internal_degree):
        for target_index in range(RANKS[target]):
            for source_index in range(RANKS[source]):
                for exponent in exponents:
                    vectors.append((source, target, target_index, source_index, *exponent))
    return vectors


def build_bases():
    basis = {
        "source": _basis(-3, 4),
        "negative": _basis(-2, 4),
        "positive": _basis(2, 0),
        "out_negative": _basis(-1, 4),
        "out_positive": _basis(3, 0),
    }
    indexes = {name: {vector: index for index, vector in enumerate(vectors)} for name, vectors in basis.items()}
    return basis, indexes


def _store(state, key, value):
    if not value:
        return
    updated = state.get(key, 0) + value
    if updated:
        state[key] = updated
    else:
        del state[key]


def cech_delta(state, internal_degree, step, steps, low, high, columns, incoming):
    output = {}
    right_sign = -1 if internal_degree % 2 == 0 else 1
    remaining = steps - step
    for (source, target, target_index, source_index, mask, e0, e1, e2, e3), value in state.items():
        free = 4 - ((mask & 1) + ((mask >> 1) & 1) + ((mask >> 2) & 1) + ((mask >> 3) & 1))
        total_sign = -value if free % 2 else value
        exponents = (e0, e1, e2, e3)
        if target < 3:
            for next_target_index, variable, coefficient in columns[target][target_index]:
                weight = total_sign * coefficient
                for shift in SUBSETS[variable]:
                    moved = (
                        exponents[0] + shift[0],
                        exponents[1] + shift[1],
                        exponents[2] + shift[2],
                        exponents[3] + shift[3],
                    )
                    if moved[0] < low - remaining or moved[0] > high or moved[1] < low - remaining or moved[1] > high or moved[2] < low - remaining or moved[2] > high or moved[3] < low - remaining or moved[3] > high:
                        continue
                    _store(output, (source, target + 1, next_target_index, source_index, mask, *moved), weight)
        if source > 0:
            signed = total_sign * right_sign
            for next_source_index, variable, coefficient in incoming[source - 1][source_index]:
                weight = signed * coefficient
                for shift in SUBSETS[variable]:
                    moved = (
                        exponents[0] + shift[0],
                        exponents[1] + shift[1],
                        exponents[2] + shift[2],
                        exponents[3] + shift[3],
                    )
                    if moved[0] < low - remaining or moved[0] > high or moved[1] < low - remaining or moved[1] > high or moved[2] < low - remaining or moved[2] > high or moved[3] < low - remaining or moved[3] > high:
                        continue
                    _store(output, (source - 1, target, target_index, next_source_index, mask, *moved), weight)
    return output


def cech_homotopy(state, internal_degree):
    output = {}
    pole = internal_degree - 2
    for (source, target, target_index, source_index, mask, *exponents), value in state.items():
        for coordinate in range(4):
            if (mask >> coordinate) & 1 or exponents[coordinate] >= 0 or exponents[coordinate] > pole:
                continue
            valid = True
            earlier = 0
            for previous in range(coordinate):
                if (mask >> previous) & 1:
                    if exponents[previous] < 0 or exponents[previous] > pole:
                        valid = False
                else:
                    earlier += 1
                    if exponents[previous] <= pole or exponents[previous] >= 0:
                        valid = False
            if valid:
                _store(
                    output,
                    (source, target, target_index, source_index, mask | (1 << coordinate), *exponents),
                    value * (-1 if earlier % 2 else 1),
                )
    return output


def scatter(matrix, state, column, index, offset=0):
    for (source, target, target_index, source_index, _mask, *exponents), value in state.items():
        row = offset + index[(source, target, target_index, source_index, *exponents)]
        _store(matrix[row], column, value)


def initial_matrix(basis, indexes, columns, incoming):
    matrix = [{} for _ in range(len(basis["negative"]))]
    for column, vector in enumerate(basis["source"]):
        source, target, target_index, source_index, *exponents = vector

        def emit(next_source, next_target, next_target_index, next_source_index, variable, coefficient):
            for shift in SUBSETS[variable]:
                moved = tuple(exponents[i] + shift[i] for i in range(4))
                if any(coordinate < -3 or coordinate > -1 for coordinate in moved):
                    continue
                row = indexes["negative"][(next_source, next_target, next_target_index, next_source_index, *moved)]
                _store(matrix[row], column, coefficient)

        for next_target_index, variable, coefficient in columns[target][target_index]:
            emit(source, target + 1, next_target_index, source_index, variable, coefficient)
        for next_source_index, variable, coefficient in incoming[source - 1][source_index]:
            emit(source - 1, target, target_index, next_source_index, variable, coefficient)
    return matrix


def outgoing_matrices(basis, indexes, columns, incoming):
    negative_rows = len(basis["out_negative"])
    pure_negative = [{} for _ in range(negative_rows)]
    outgoing = [{} for _ in range(negative_rows + len(basis["out_positive"]))]
    for column, vector in enumerate(basis["negative"]):
        state = {(*vector[:4], 0, *vector[4:]): 1}
        scatter(
            pure_negative,
            cech_delta(state, -2, 1, 1, -2, -1, columns, incoming),
            column,
            indexes["out_negative"],
        )
        for step in range(1, 6):
            state = cech_delta(state, -2 + step - 1, step, 5, 0, 1, columns, incoming)
            if step < 5:
                state = cech_homotopy(state, -2 + step)
        scatter(outgoing, state, column, indexes["out_positive"], negative_rows)
    for row, entries in enumerate(pure_negative):
        outgoing[row] = entries
    for column, vector in enumerate(basis["positive"]):
        state = {(*vector[:4], 15, *vector[4:]): 1}
        scatter(
            outgoing,
            cech_delta(state, 2, 1, 1, 0, 1, columns, incoming),
            len(basis["negative"]) + column,
            indexes["out_positive"],
            negative_rows,
        )
    return pure_negative, outgoing


def positive_differential(basis, indexes, columns, incoming):
    rows = [{} for _ in range(len(basis["out_positive"]))]
    for column, vector in enumerate(basis["positive"]):
        state = {(*vector[:4], 15, *vector[4:]): 1}
        image = cech_delta(state, 2, 1, 1, 0, 1, columns, incoming)
        scatter(rows, image, column, indexes["out_positive"])
    return rows


def length_five_image(vector, basis, indexes, columns, incoming):
    """Image in the positive block of one degree -3 vector, including the transfer sign."""
    source, target, target_index, source_index, *exponents = vector
    state = {(source, target, target_index, source_index, 0, *exponents): 1}
    for step in range(1, 6):
        state = cech_delta(state, -3 + step - 1, step, 5, 0, 0, columns, incoming)
        if step < 5:
            state = cech_homotopy(state, -3 + step)
    if (5 - 1) % 2:
        state = {key: -value for key, value in state.items()}
    image = [0] * len(basis["positive"])
    for (source, target, target_index, source_index, _mask, *exponents), value in state.items():
        image[indexes["positive"][(source, target, target_index, source_index, *exponents)]] += value
    return image
