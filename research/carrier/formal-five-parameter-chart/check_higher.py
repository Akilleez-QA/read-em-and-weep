"""Complete-character checks from supplied complete coefficient maps."""
from pathlib import Path
from collections import defaultdict
import json
import sympy as s
from sympy.polys.matrices import DomainMatrix

if not __debug__:
    raise RuntimeError('Run without -O: exact checks use assertions.')
ROOT = Path(__file__).resolve().parent
DATA = ROOT / 'data'
OUT = ROOT / 'build'
OUT.mkdir(exist_ok=True)
WEIGHTS = [3, 0, 2, 2]


def matrix(data, key):
    m = s.zeros(*data[key + '_shape'])
    seen = set()
    for i, j, value in data[key + '_sparse']:
        assert (i, j) not in seen and s.Rational(value) != 0
        assert 0 <= i < m.rows and 0 <= j < m.cols
        seen.add((i, j))
        m[i, j] = s.Rational(value)
    return m


def exact_det(m):
    return DomainMatrix.from_Matrix(m).convert_to(s.QQ).det()


blocks = {}
sections = {}
for k in range(2, 7):
    data = json.loads((DATA / f'order_{k}.json').read_text())
    if k < 5:
        n = matrix(data, f'N{k}')
        minor = data[f'N{k}_rank_minor']
        rows, columns = minor['rows'], minor['columns']
        assert columns == list(range(n.cols))
        assert len(rows) == n.cols and len(set(rows)) == n.cols
        determinant = exact_det(n[rows, columns])
        assert determinant != 0
        expected = {2: 16, 3: -512, 4: -16384}[k]
        assert determinant == expected
        sections[str(k)] = {
            'shape': list(n.shape), 'exact_rank': n.cols,
            'minor_rows': rows, 'minor_columns': columns,
            'minor_determinant': str(determinant),
            'unit_over_Q_parameters': True,
            'H1_GI_full_dimension': 0,
        }
        print(f'N{k}: {n.rows} x {n.cols}, full column rank, determinant {determinant}')
    if k == 2:
        continue
    prefix = f'D{k}'
    source = data[prefix + '_source_basis']
    sw = [2*e-p[0]-p[1]-2-WEIGHTS[ch] for ch, e, p in source]
    columns = [j for j, weight in enumerate(sw) if weight == k-4]
    item = {'source_columns': columns}
    if k < 5:
        target = data[prefix + '_target_basis']
        tw = [2*e+p[0]+p[1]-WEIGHTS[ch[0]]-WEIGHTS[ch[1]] for ch,e,p in target]
    else:
        raw = data[f'raw_W{k}_labels']
        rw = [2*e-p[0]-p[1]-2-WEIGHTS[ch[0]]-WEIGHTS[ch[1]] for ch,e,p in raw]
        free, pivot = data[f'W{k}_kernel_free_columns'], data[f'C{k}_pivot_columns']
        assert len(set(free)) == len(free) and len(set(pivot)) == len(pivot)
        assert not set(free).intersection(pivot)
        assert sorted(free+pivot) == list(range(len(raw)))
        selected = [i for i, weight in enumerate(rw) if weight == k-4]
        assert selected == {5:[532,540], 6:[664]}[k]
        c_entries = data[f'C{k}_sparse']
        assert not any(j in selected and s.Rational(v) for i,j,v in c_entries)
        assert all(j in free and j not in pivot for j in selected)
        row_weights = defaultdict(set)
        for i,j,value in c_entries:
            if s.Rational(value):
                row_weights[i].add(rw[j])
        assert all(len(value) == 1 for value in row_weights.values())
        # Recompute C's pivot set, rather than trusting free-column labels alone.
        c = s.zeros(1 + max(i for i,j,v in c_entries), len(raw))
        for i,j,value in c_entries:
            c[i,j] = s.Rational(value)
        _, actual_pivots = c.rref()
        assert list(actual_pivots) == pivot
        tw = [rw[j] for j in free]
        item.update({
            'raw_prescribed_columns': selected,
            'prescribed_C_columns_identically_zero': True,
            'C_pivots_recomputed': pivot,
            'every_C_row_weight_homogeneous': True,
        })
    d = matrix(data, prefix)
    assert len(sw) == d.cols and len(tw) == d.rows
    assert all(tw[i] == sw[j] for i,j,value in data[prefix+'_sparse'])
    rows = [i for i, weight in enumerate(tw) if weight == k-4]
    block = d[rows, columns]
    size = {3:9, 4:5, 5:2, 6:1}[k]
    assert block.shape == (size, size) and block.det() == 1
    inverse = block.inv()
    assert block*inverse == s.eye(size) and inverse*block == s.eye(size)
    item.update({
        'target_rows': rows, 'shape': list(block.shape),
        'matrix': [[str(value) for value in row] for row in block.tolist()],
        'right_inverse': [[str(value) for value in row] for row in inverse.tolist()],
        'M_times_R': [[str(value) for value in row] for row in (block*inverse).tolist()],
        'determinant': '1', 'all_D_entries_weight_homogeneous': True,
        'H1_n_prescribed_dimension': 0, 'H2_n_prescribed_dimension': 0,
        'inverse_coefficients': 'constant rational numbers',
    })
    blocks[str(k)] = item
    print(f'D{k}: complete {size} x {size} character block; determinant 1; M R = I')
(OUT/'higher_certificate.json').write_text(json.dumps({'blocks':blocks,'sections':sections},indent=2)+'\n')
