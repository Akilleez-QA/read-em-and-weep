"""Exact and modular sparse rank, independent of the pinned verifiers."""

from math import gcd


def _mod(value, prime):
    return value % prime


def modular_rank(rows, prime):
    active = []
    for row in rows:
        reduced = {column: _mod(value, prime) for column, value in row.items() if _mod(value, prime)}
        if reduced:
            active.append(reduced)
    pivots = {}
    for row in active:
        while row:
            column = min(row)
            if column in pivots:
                scale = row[column]
                pivot = pivots[column]
                for index, value in pivot.items():
                    updated = _mod(row.get(index, 0) - scale * value, prime)
                    if updated:
                        row[index] = updated
                    else:
                        row.pop(index, None)
            else:
                inverse = pow(row[column], -1, prime)
                pivots[column] = {index: _mod(value * inverse, prime) for index, value in row.items()}
                break
    return len(pivots), pivots


def reduce_rows(rows, pivots, prime):
    reduced_rows = []
    for row in rows:
        current = {column: _mod(value, prime) for column, value in row.items() if _mod(value, prime)}
        for column in sorted(pivots):
            if column not in current:
                continue
            scale = current[column]
            for index, value in pivots[column].items():
                updated = _mod(current.get(index, 0) - scale * value, prime)
                if updated:
                    current[index] = updated
                else:
                    current.pop(index, None)
        reduced_rows.append(current)
    return reduced_rows


def exact_rank(rows, column_count):
    """Unit-pivot elimination, then fraction-free elimination of the tail."""
    active = [dict(row) for row in rows]
    rank = 0
    column = 0
    max_entry = 1
    while column < column_count:
        pivot = None
        for index in range(rank, len(active)):
            if abs(active[index].get(column, 0)) == 1:
                pivot = index
                break
        if pivot is None:
            if any(active[index].get(column, 0) for index in range(rank, len(active))):
                break
            column += 1
            continue
        active[rank], active[pivot] = active[pivot], active[rank]
        if active[rank].get(column, 0) == -1:
            active[rank] = {index: -value for index, value in active[rank].items()}
        pivot_row = active[rank]
        for index in range(rank + 1, len(active)):
            scale = active[index].get(column, 0)
            if not scale:
                continue
            row = active[index]
            for pivot_column, pivot_value in pivot_row.items():
                updated = row.get(pivot_column, 0) - scale * pivot_value
                if updated:
                    row[pivot_column] = updated
                    if abs(updated) > max_entry:
                        max_entry = abs(updated)
                else:
                    row.pop(pivot_column, None)
        rank += 1
        column += 1
    unit_rank = rank
    tail = [dict(row) for row in active[rank:] if row]
    tail_rank = 0
    max_bits = 0
    for tail_column in range(column, column_count):
        pivot = None
        for index in range(tail_rank, len(tail)):
            if tail[index].get(tail_column, 0):
                pivot = index
                break
        if pivot is None:
            continue
        tail[tail_rank], tail[pivot] = tail[pivot], tail[tail_rank]
        pivot_value = tail[tail_rank][tail_column]
        for index in range(tail_rank + 1, len(tail)):
            other = tail[index].get(tail_column, 0)
            if not other:
                continue
            common = gcd(pivot_value, other)
            left = pivot_value // common
            right = other // common
            updated = {key: value * left for key, value in tail[index].items()}
            for key, value in tail[tail_rank].items():
                combined = updated.get(key, 0) - right * value
                if combined:
                    updated[key] = combined
                else:
                    updated.pop(key, None)
            content = 0
            for value in updated.values():
                content = gcd(content, value)
            if content > 1:
                updated = {key: value // content for key, value in updated.items()}
            for value in updated.values():
                max_bits = max(max_bits, abs(value).bit_length())
            tail[index] = updated
        tail_rank += 1
    if any(tail[tail_rank:]):
        raise RuntimeError("exact rank left a nonzero residual row")
    return {
        "rank": unit_rank + tail_rank,
        "unit_rank": unit_rank,
        "tail_rank": tail_rank,
        "unit_max_entry": max_entry,
        "tail_max_bits": max_bits,
    }


def unit_echelon(rows, column_count):
    """Exact unit-pivot echelon. Returns rank, pivots, row-reduced rows, and kernel vectors."""
    active = [dict(row) for row in rows]
    operations = []
    pivots = []
    rank = 0
    for column in range(column_count):
        pivot = None
        for index in range(rank, len(active)):
            if abs(active[index].get(column, 0)) == 1:
                pivot = index
                break
        if pivot is None:
            if any(active[index].get(column, 0) for index in range(rank, len(active))):
                raise RuntimeError(f"nonunit pivot in column {column}")
            continue
        if pivot != rank:
            active[rank], active[pivot] = active[pivot], active[rank]
            operations.append(("swap", pivot, rank))
        if active[rank].get(column, 0) == -1:
            active[rank] = {index: -value for index, value in active[rank].items()}
            operations.append(("negate", rank))
        pivot_row = active[rank]
        for index in range(rank + 1, len(active)):
            scale = active[index].get(column, 0)
            if not scale:
                continue
            row = active[index]
            for pivot_column, pivot_value in pivot_row.items():
                updated = row.get(pivot_column, 0) - scale * pivot_value
                if updated:
                    row[pivot_column] = updated
                else:
                    row.pop(pivot_column, None)
            operations.append(("add", index, rank, scale))
        pivots.append(column)
        rank += 1
    if any(active[rank:]):
        raise RuntimeError("unit echelon left a nonzero residual row")
    kernel = []
    pivot_set = set(pivots)
    for free in range(column_count):
        if free in pivot_set:
            continue
        vector = [0] * column_count
        vector[free] = 1
        for index in range(rank - 1, -1, -1):
            value = 0
            for column, entry in active[index].items():
                if column != pivots[index]:
                    value += entry * vector[column]
            vector[pivots[index]] = -value
        kernel.append(vector)
    return {"rank": rank, "pivots": pivots, "rows": active, "operations": operations, "kernel": kernel}


def multiply_matrix(rows, vector):
    image = []
    for row in rows:
        value = 0
        for column, entry in row.items():
            value += entry * vector[column]
        image.append(value)
    return image


def dot_sparse(row, vector):
    return sum(value * vector[column] for column, value in row.items())
