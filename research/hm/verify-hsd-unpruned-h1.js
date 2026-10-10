// Exhaustive unpruned A/B/C contraction for the pinned Horrocks–Mumford Ext model.
// Run: node research/hm/verify-hsd-unpruned-h1.js
//
// Pins PR #5 at add03476d9055aa00e1e00778eea6332cf8e01cc and reuses that file's
// finite model (normalized HM monad, Euler coresolution, four two-chart
// factors). The transferred differential pΔ(1+HΔ)^{-1}i is recomputed here
// with every A, B, and C chart retained and with no exponent filter. Each
// degree-one source column is compared with the pinned pruned operator.
// Ranks are certified over Q by fraction-free BigInt Bareiss: a nonzero
// r×r minor for each lower bound, and kernel vectors checked on the original
// matrix for each upper bound.
//
// Dependency-free. This file does not modify the pinned model.

'use strict';

const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const vm = require('vm');

const PINNED_HEAD = 'add03476d9055aa00e1e00778eea6332cf8e01cc';
const PINNED_MODEL_SHA256 = '1fe4608ed77f3767691e7ef4de375fc55b052ccf26159a4aae3ec6d35fe96414';
const EXPECTED_H1 = [79, 2, 0, 0, 0];
const EXPECTED_D1 = [50, 150, 450, 1250, 2550];
const EXPECTED_REMAINING = [3598, 522, 90, 30, 10];
const EXPECTED_D1_NONZEROS = [320, 960, 2880, 8640, 25920];
const MULTIPLICITIES = [1, 4, 6, 4, 1];

function loadOracle() {
  const file = path.join(__dirname, 'verify-hm-ext.js');
  const buf = fs.readFileSync(file);
  const hash = crypto.createHash('sha256').update(buf).digest('hex');
  if (hash !== PINNED_MODEL_SHA256) {
    throw new Error('verify-hm-ext.js does not match pinned #5 head ' + PINNED_HEAD);
  }
  let src = buf.toString('utf8');
  const cut = src.indexOf('const result=verifyHMExt();');
  if (cut < 0) throw new Error('Pinned verifier tail is missing');
  src = src.slice(0, cut) + 'verifyHMExt();\n';
  const anchor = '  const summaries=[];';
  if (!src.includes(anchor)) throw new Error('Pinned verifier anchor is missing');
  src = src.replace(anchor, `  globalThis.__HSD_ORACLE = {exact, ranks, gamma, d, incoming, subsets, add, mons, negativeD1, delta, homotopy, run, projectR2, echelon, rankOnly};
  return null;
${anchor}`);
  vm.runInThisContext(src, {filename: file});
  return globalThis.__HSD_ORACLE;
}

function gcd(a, b) {
  a = a < 0n ? -a : a;
  b = b < 0n ? -b : b;
  while (b) {
    const t = a % b;
    a = b;
    b = t;
  }
  return a;
}

function lcm(a, b) {
  if (a === 0n || b === 0n) return 0n;
  return a / gcd(a, b) * b;
}

class Q {
  constructor(n, d = 1n) {
    if (typeof n !== 'bigint') n = BigInt(n);
    if (typeof d !== 'bigint') d = BigInt(d);
    if (d < 0n) { n = -n; d = -d; }
    if (d === 0n) throw new Error('Zero denominator');
    const g = gcd(n, d);
    this.n = n / g;
    this.d = d / g;
  }
  add(o) { return new Q(this.n * o.d + o.n * this.d, this.d * o.d); }
  mul(o) { return new Q(this.n * o.n, this.d * o.d); }
  neg() { return new Q(-this.n, this.d); }
  div(o) { return new Q(this.n * o.d, this.d * o.n); }
}

function addNum(map, key, value) {
  const z = (map.get(key) || 0) + value;
  if (!Number.isSafeInteger(z)) throw new Error('Unsafe integer in contraction');
  if (z) map.set(key, z);
  else map.delete(key);
}

function signature(map) {
  return JSON.stringify([...map.entries()].sort((a, b) => (a[0] < b[0] ? -1 : a[0] > b[0] ? 1 : 0)));
}

function bareissEliminate(inputRows, ncols) {
  const nRows = inputRows.length;
  const A = inputRows.map(row => new Map(row));
  const origin = A.map((_, i) => i);
  let prev = 1n;
  let sign = 1n;
  let rank = 0;
  const pivotCols = [];
  const pivotRows = [];
  for (let c = 0; c < ncols; c++) {
    let chosen = -1;
    for (let i = rank; i < nRows; i++) {
      const v = A[i].get(c);
      if (v === undefined || v === 0n) continue;
      chosen = i;
      if (v === 1n || v === -1n) break;
    }
    if (chosen < 0) continue;
    if (chosen !== rank) {
      [A[chosen], A[rank]] = [A[rank], A[chosen]];
      [origin[chosen], origin[rank]] = [origin[rank], origin[chosen]];
      sign = -sign;
    }
    const pivot = A[rank].get(c);
    const pivotRow = A[rank];
    for (let i = rank + 1; i < nRows; i++) {
      const mik = A[i].get(c) || 0n;
      const ai = A[i];
      if (mik === 0n && pivot === prev) continue;
      const next = new Map();
      if (mik === 0n) {
        for (const [j, v] of ai) {
          const z = pivot * v;
          if (z % prev !== 0n) throw new Error('Bareiss scale was not exact');
          const q = z / prev;
          if (q !== 0n) next.set(j, q);
        }
      } else {
        const cols = new Set(ai.keys());
        for (const j of pivotRow.keys()) cols.add(j);
        for (const j of cols) {
          const z = pivot * (ai.get(j) || 0n) - mik * (pivotRow.get(j) || 0n);
          if (z % prev !== 0n) {
            throw new Error(`Bareiss division was not exact at rank ${rank} col ${c} j ${j}: pivot ${pivot} prev ${prev} mik ${mik} z ${z} rem ${z % prev}`);
          }
          const q = z / prev;
          if (q !== 0n) next.set(j, q);
        }
      }
      A[i] = next;
    }
    prev = pivot;
    pivotCols.push(c);
    pivotRows.push(origin[rank]);
    rank++;
  }
  for (let i = rank; i < nRows; i++) {
    if (A[i].size) throw new Error('Bareiss left a nonzero residual row');
  }
  return {A, rank, sign, prev, pivotCols, pivotRows};
}

function bareissDet(rows) {
  const n = rows.length;
  if (n === 0) return 1n;
  const eliminated = bareissEliminate(rows, n);
  if (eliminated.rank < n) return 0n;
  return eliminated.sign * eliminated.prev;
}

function extractMinor(rows, pivotRows, pivotCols) {
  const index = new Map(pivotCols.map((col, i) => [col, i]));
  return pivotRows.map(rowIndex => {
    const out = new Map();
    for (const [col, value] of rows[rowIndex]) {
      const j = index.get(col);
      if (j !== undefined && value !== 0n) out.set(j, value);
    }
    return out;
  });
}

function certify(inputRows, ncols) {
  const original = inputRows.map(row => new Map(row));
  const eliminated = bareissEliminate(original, ncols);
  const {A, rank, pivotCols, pivotRows} = eliminated;
  const pivotSet = new Set(pivotCols);
  const free = [];
  for (let c = 0; c < ncols; c++) if (!pivotSet.has(c)) free.push(c);
  const kernel = [];
  for (const f of free) {
    const coeff = Array.from({length: ncols}, () => new Q(0n));
    coeff[f] = new Q(1n);
    for (let i = rank - 1; i >= 0; i--) {
      const pc = pivotCols[i];
      const row = A[i];
      const piv = row.get(pc);
      let sum = new Q(0n);
      for (const [j, a] of row) {
        if (j !== pc) sum = sum.add(new Q(a).mul(coeff[j]));
      }
      coeff[pc] = sum.neg().div(new Q(piv));
    }
    let den = 1n;
    for (const x of coeff) den = lcm(den, x.d);
    const vector = coeff.map(x => x.n * (den / x.d));
    if (vector[f] === 0n) throw new Error('Kernel vector is missing its free coordinate');
    for (const g of free) if (g !== f && vector[g] !== 0n) throw new Error('Kernel vectors are not independent');
    for (const row of original) {
      let acc = 0n;
      for (const [j, a] of row) acc += a * vector[j];
      if (acc !== 0n) throw new Error('Kernel vector failed on the original matrix');
    }
    kernel.push(vector);
  }
  const det = bareissDet(extractMinor(original, pivotRows, pivotCols));
  if (det === 0n) throw new Error('Selected minor has determinant zero');
  if (kernel.length !== ncols - rank) throw new Error('Kernel dimension does not match the corank');
  return {
    rank,
    determinant: det,
    kernel,
    pivotRows,
    pivotCols,
    kernelDimension: kernel.length
  };
}

function columnsToRows(columns, nrows) {
  const rows = Array.from({length: nrows}, () => new Map());
  columns.forEach((column, j) => {
    for (const [i, value] of column) {
      const z = typeof value === 'bigint' ? value : BigInt(value);
      if (z !== 0n) rows[i].set(j, z);
    }
  });
  return rows;
}

function selfTestBareiss() {
  const row = (entries) => new Map(entries);
  const det2 = bareissDet([row([[0, 2n], [1, 1n]]), row([[0, 1n], [1, 2n]])]);
  if (det2 !== 3n) throw new Error('Bareiss det 3 failed: ' + det2);
  const swap = bareissDet([row([[1, 1n]]), row([[0, 1n]])]);
  if (swap !== -1n) throw new Error('Bareiss swap det failed: ' + swap);
  const known = bareissDet([
    row([[0, 2n], [1, 1n], [2, 1n]]),
    row([[0, 4n], [1, 3n], [2, 5n]]),
    row([[0, 2n], [1, 1n], [2, 2n]])
  ]);
  if (known !== 2n) throw new Error('Bareiss det 2 failed: ' + known);
  const certified = certify([row([[0, 2n], [1, 4n], [2, 1n]]), row([])], 3);
  if (certified.rank !== 1 || certified.determinant !== 2n || certified.kernelDimension !== 2) {
    throw new Error('Bareiss kernel certificate failed');
  }
}

function chartAt(code, i) {
  return Math.floor(code / (3 ** i)) % 3;
}

function isHarmonic(charts, exponents, internal, weight) {
  for (let i = 0; i < 4; i++) {
    const n = internal - (i < weight ? 2 : 0);
    const chart = chartAt(charts, i);
    const e = exponents[i];
    if (chart === 2) return false;
    if (chart === 0) {
      if (!(e > n && e < 0)) return false;
    } else if (chart === 1) {
      if (!(e >= 0 && e <= n)) return false;
    } else return false;
  }
  return true;
}

function makeContraction(oracle) {
  const {d, incoming, subsets} = oracle;

  function fullDelta(M, internal) {
    const out = new Map();
    const rs = internal % 2 === 0 ? -1 : 1;
    for (const [key, value] of M) {
      const p = key.split(',').map(Number);
      const u = p[0], v = p[1], a = p[2], b = p[3], charts = p[4];
      const exponents = p.slice(5);
      let cech = 0;
      for (let i = 0; i < 4; i++) if (chartAt(charts, i) === 0) cech++;
      const sgn = cech % 2 ? -1 : 1;
      function emit(uu, vv, aa, bb, k, z) {
        for (const sm of subsets[k]) {
          const mm = exponents.map((x, j) => x + sm[j]);
          addNum(out, [uu, vv, aa, bb, charts, ...mm].join(','), value * z * sgn);
        }
      }
      if (v < 3) for (const [c, k, z] of d[v][a]) emit(u, v + 1, c, b, k, z);
      if (u > 0) for (const [c, k, z] of incoming[u - 1][b]) emit(u - 1, v, a, c, k, z * rs);
    }
    return out;
  }

  function fullHomotopy(M, internal, weight) {
    const out = new Map();
    const n = [0, 1, 2, 3].map(i => internal - (i < weight ? 2 : 0));
    for (const [key, value] of M) {
      const p = key.split(',').map(Number);
      const u = p[0], v = p[1], a = p[2], b = p[3], charts = p[4];
      const exponents = p.slice(5);
      for (let j = 0; j < 4; j++) {
        if (chartAt(charts, j) !== 0) continue;
        let good = true;
        let cBefore = 0;
        for (let i = 0; i < j; i++) {
          const chart = chartAt(charts, i);
          if (chart === 0) {
            cBefore++;
            if (exponents[i] <= n[i] || exponents[i] >= 0) good = false;
          } else if (chart === 1) {
            if (exponents[i] < 0 || exponents[i] > n[i]) good = false;
          } else good = false;
        }
        if (!good) continue;
        const sign = cBefore % 2 ? -1 : 1;
        const e = exponents[j];
        if (e >= 0) {
          const code = charts + (2 - chartAt(charts, j)) * (3 ** j);
          addNum(out, [u, v, a, b, code, ...exponents].join(','), value * sign * -1);
        } else if (e <= n[j]) {
          const code = charts + (1 - chartAt(charts, j)) * (3 ** j);
          addNum(out, [u, v, a, b, code, ...exponents].join(','), value * sign);
        }
      }
    }
    return out;
  }

  function fullSnapshots(vector, src, weight) {
    let M = new Map();
    for (let j = 0; j < vector.length; j++) {
      if (!vector[j]) continue;
      const unit = Math.floor(j / src.length);
      const key = [3, 0, Math.floor(unit / 2), unit % 2, 0, ...src[j % src.length]].join(',');
      addNum(M, key, vector[j]);
    }
    const snaps = [];
    for (let step = 1; step <= 5; step++) {
      M = fullDelta(M, step - 4);
      snaps.push(M);
      if (step < 5) M = fullHomotopy(M, step - 3, weight);
    }
    return snaps;
  }

  return {fullDelta, fullHomotopy, fullSnapshots};
}

function prunedChart(mask) {
  let code = 0;
  for (let i = 0; i < 4; i++) if ((mask >> i) & 1) code += 3 ** i;
  return code;
}

function harmonicMap(M, internal, weight, mode) {
  const out = new Map();
  for (const [key, z] of M) {
    const p = key.split(',').map(Number);
    const charts = mode === 'pruned' ? prunedChart(p[4]) : p[4];
    const exponents = p.slice(5);
    if (p[1] - p[0] !== internal) continue;
    if (!isHarmonic(charts, exponents, internal, weight)) continue;
    addNum(out, [p[0], p[1], p[2], p[3], charts, ...exponents].join(','), z);
  }
  return out;
}

function len1Rows(M, weight, targetIndex, targetLength) {
  const out = new Map();
  for (const [key, z] of M) {
    const p = key.split(',').map(Number);
    const exponents = p.slice(5);
    if (p[1] - p[0] !== -2) continue;
    if (!isHarmonic(p[4], exponents, -2, weight)) continue;
    const j = targetIndex.get(exponents.join(','));
    if (j === undefined) throw new Error('Length-one harmonic exponent is outside the model target');
    let base;
    if (p[0] === 2 && p[1] === 0) base = p[2] * 10 + p[3];
    else if (p[0] === 3 && p[1] === 1) base = 50 + p[2] * 2 + p[3];
    else throw new Error('Unexpected length-one bidegree');
    addNum(out, base * targetLength + j, z);
  }
  return out;
}

function len5Rows(M, weight) {
  const rad = [0, 1, 2, 3].map(i => (i < weight ? 1 : 3));
  const nm = rad.reduce((s, x) => s * x, 1);
  const out = new Map();
  for (const [key, z] of M) {
    const p = key.split(',').map(Number);
    const u = p[0], v = p[1], a = p[2], b = p[3];
    const exponents = p.slice(5);
    if (v - u !== 2) continue;
    if (!isHarmonic(p[4], exponents, 2, weight)) continue;
    if (exponents.some((e, i) => e < 0 || e >= rad[i])) continue;
    let mi = 0;
    for (let i = 0; i < 4; i++) mi = mi * rad[i] + exponents[i];
    const unit = u === 0 ? a * 5 + b : 50 + a * 15 + b;
    addNum(out, unit * nm + mi, z);
  }
  return out;
}

function projectPrunedLen5(M, weight) {
  const rad = [0, 1, 2, 3].map(i => (i < weight ? 1 : 3));
  const nm = rad.reduce((s, x) => s * x, 1);
  const out = new Map();
  for (const [key, z] of M) {
    const p = key.split(',').map(Number);
    const [u, v, a, b, mask] = p;
    const exponents = p.slice(5);
    if (v - u !== 2 || mask !== 15) continue;
    if (exponents.some((e, i) => e < 0 || e >= rad[i])) continue;
    let mi = 0;
    for (let i = 0; i < 4; i++) mi = mi * rad[i] + exponents[i];
    const unit = u === 0 ? a * 5 + b : 50 + a * 15 + b;
    addNum(out, unit * nm + mi, z);
  }
  return out;
}

function len3Rows(M, ranks) {
  const offset = [0, 25, 250, 350];
  const out = new Map();
  for (const [key, z] of M) {
    const p = key.split(',').map(Number);
    const u = p[0], v = p[1], a = p[2], b = p[3];
    const exponents = p.slice(5);
    if (u !== v) continue;
    if (!isHarmonic(p[4], exponents, 0, 2)) continue;
    const row = offset[u] + a * ranks[u] + b;
    if (row < 0 || row >= 354) throw new Error('Length-three row is outside 0..353');
    addNum(out, row, z);
  }
  return out;
}

function columnFromMatrix(rows, col) {
  const out = new Map();
  for (let r = 0; r < rows.length; r++) {
    const z = rows[r].get(col);
    if (z) out.set(r, z);
  }
  return out;
}

function combine(images, coeffs) {
  const out = new Map();
  for (let i = 0; i < coeffs.length; i++) {
    const c = coeffs[i];
    if (c === 0n) continue;
    const image = images[i];
    if (!image) continue;
    for (const [row, value] of image) {
      const z = (out.get(row) || 0n) + c * BigInt(value);
      if (z === 0n) out.delete(row);
      else out.set(row, z);
    }
  }
  return out;
}

function composeKernels(outer, inner) {
  return outer.map(vector => {
    const acc = Array.from({length: inner[0].length}, () => 0n);
    for (let j = 0; j < vector.length; j++) {
      if (vector[j] === 0n) continue;
      const basis = inner[j];
      for (let i = 0; i < basis.length; i++) {
        if (basis[i] !== 0n) acc[i] += vector[j] * basis[i];
      }
    }
    return acc;
  });
}

function recordMismatch(mismatches, detail) {
  mismatches.push(detail);
}

function compareMaps(mismatches, detail, left, right) {
  if (signature(left) !== signature(right)) {
    recordMismatch(mismatches, detail);
    return false;
  }
  return true;
}

function unitVector(length, index) {
  const vector = Array(length).fill(0);
  vector[index] = 1;
  return vector;
}

function prunedWideSnapshots(oracle, vector, src, weight) {
  let M = new Map();
  for (let j = 0; j < vector.length; j++) {
    if (!vector[j]) continue;
    const unit = Math.floor(j / src.length);
    const key = [3, 0, Math.floor(unit / 2), unit % 2, 0, ...src[j % src.length]].join(',');
    oracle.add(M, key, vector[j]);
  }
  const wide = [[-40, 40], [-40, 40], [-40, 40], [-40, 40]];
  const snaps = [];
  for (let step = 1; step <= 5; step++) {
    M = oracle.delta(M, step - 4, step, 5, wide);
    snaps.push(M);
    if (step < 5) M = oracle.homotopy(M, step - 3, weight, 15);
  }
  return snaps;
}

function certifyReport(rows, ncols, label) {
  const t0 = Date.now();
  const certificate = certify(rows, ncols);
  const bits = certificate.determinant < 0n ? certificate.determinant.toString(2).length - 1 : certificate.determinant.toString(2).length;
  console.error(`  certified ${label}: rank ${certificate.rank}, det bits ${bits}, kernel ${certificate.kernelDimension}, ${Date.now() - t0}ms`);
  return {
    rows: rows.length,
    columns: ncols,
    rank: certificate.rank,
    minorDeterminant: certificate.determinant.toString(),
    kernelDimension: certificate.kernelDimension,
    kernelVectorsChecked: certificate.kernel.length,
    pivotRows: certificate.pivotRows,
    kernel: certificate.kernel
  };
}

function publicRank(report) {
  return {
    rows: report.rows,
    columns: report.columns,
    rank: report.rank,
    minorDeterminant: report.minorDeterminant,
    kernelDimension: report.kernelDimension,
    kernelVectorsChecked: report.kernelVectorsChecked
  };
}

function verify() {
  selfTestBareiss();
  const oracle = loadOracle();
  const {fullDelta, fullHomotopy, fullSnapshots} = makeContraction(oracle);
  const mismatches = [];
  const byWeight = [];
  const rankReports = [];
  let higherColumns = [];

  for (let weight = 0; weight <= 4; weight++) {
    const t0 = Date.now();
    const built = oracle.negativeD1(weight);
    const src = built.src;
    const ncols = 10 * src.length;
    const target = oracle.mons(
      [0, 1, 2, 3].map(i => (i < weight ? -3 : -1)),
      [-1, -1, -1, -1]
    );
    const targetIndex = new Map(target.map((m, i) => [m.join(','), i]));
    const len1 = [];
    const len3 = [];
    const len5 = [];
    let boundaryReport = null;
    const lengthNonzero = [0, 0, 0, 0, 0];
    const higherNonzeroColumns = [];
    let negativeNonzero = 0;
    const ranges5 = [0, 1, 2, 3].map(i => [0, i < weight ? 0 : 2]);

    for (let col = 0; col < ncols; col++) {
      const vector = unitVector(ncols, col);
      const full = fullSnapshots(vector, src, weight);
      const pruned = prunedWideSnapshots(oracle, vector, src, weight);
      let any = false;
      let higher = false;
      for (let step = 1; step <= 5; step++) {
        const internal = -3 + step;
        const left = harmonicMap(full[step - 1], internal, weight, 'full');
        const right = harmonicMap(pruned[step - 1], internal, weight, 'pruned');
        if (left.size || right.size) lengthNonzero[step - 1]++;
        if (left.size) any = true;
        if (step >= 2 && left.size) higher = true;
        compareMaps(mismatches, {family: 'negative', weight, column: col, length: step, kind: 'A-omission'}, left, right);
      }
      const image1 = len1Rows(full[0], weight, targetIndex, target.length);
      const image5 = len5Rows(full[4], weight);
      compareMaps(mismatches, {family: 'negative', weight, column: col, length: 1, kind: 'pinned-d1'}, image1, columnFromMatrix(built.A, col));
      const filtered5 = projectPrunedLen5(oracle.run(vector, src, weight, 5, 15, ranges5), weight);
      compareMaps(mismatches, {family: 'negative', weight, column: col, length: 5, kind: 'pinned-filter'}, image5, filtered5);
      len1.push(image1);
      len5.push(image5);
      if (weight === 2) {
        const image3 = len3Rows(full[2], oracle.ranks);
        const filtered3 = harmonicMap(oracle.run(vector, src, weight, 3, 12, [[-1, -1], [-1, -1], [0, 0], [0, 0]]), 0, weight, 'pruned');
        const full3 = harmonicMap(full[2], 0, weight, 'full');
        compareMaps(mismatches, {family: 'negative', weight, column: col, length: 3, kind: 'pinned-filter'}, full3, filtered3);
        len3.push(image3);
      }
      if (any) negativeNonzero++;
      if (higher) higherNonzeroColumns.push(col);
      if (mismatches.length) {
        throw new Error('Column mismatch: ' + JSON.stringify(mismatches[mismatches.length - 1]));
      }
    }

    const d1nnz = len1.reduce((s, column) => s + column.size, 0);
    if (d1nnz !== EXPECTED_D1_NONZEROS[weight]) {
      throw new Error('Length-one nonzero count changed at weight ' + weight);
    }
    const d1 = certifyReport(columnsToRows(len1, built.A.length), ncols, `weight ${weight} d1`);
    if (d1.rank !== EXPECTED_D1[weight]) throw new Error('Unexpected d1 rank at weight ' + weight);

    let sourceKernel = d1.kernel;
    let d3report = null;
    if (weight === 2) {
      const d3columns = sourceKernel.map(vector => combine(len3, vector));
      d3report = certifyReport(columnsToRows(d3columns, 354), sourceKernel.length, 'weight 2 length-three');
      if (d3report.rank !== 100) throw new Error('Weight-two intermediate rank is not 100');
      sourceKernel = composeKernels(d3report.kernel, d1.kernel);
    }

    const remainingColumns = sourceKernel.map(vector => combine(len5, vector));
    let extraNonzero = 0;
    let extraColumns = 0;
    const extraMismatchesAtStart = mismatches.length;

    if (weight === 1) {
      const ranges = [[0, 0], [0, 2], [0, 2], [0, 2]];
      for (let u = 0; u < 4; u++) {
        for (let a = 0; a < oracle.ranks[u]; a++) {
          for (let b = 0; b < oracle.ranks[u]; b++) {
            extraColumns++;
            let fullM = new Map([[[u, u, a, b, 39, -1, 0, 0, 0].join(','), 1]]);
            fullM = fullDelta(fullM, 0);
            const j0 = harmonicMap(fullM, 1, weight, 'full');
            if (j0.size) throw new Error('Weight-one diagonal has a nonzero length-one harmonic');
            fullM = fullHomotopy(fullM, 1, weight);
            fullM = fullDelta(fullM, 1);
            const image = len5Rows(fullM, weight);
            let prunedM = new Map([[[u, u, a, b, 14, -1, 0, 0, 0].join(','), 1]]);
            prunedM = oracle.delta(prunedM, 0, 1, 2, ranges);
            prunedM = oracle.homotopy(prunedM, 1, weight, 15);
            prunedM = oracle.delta(prunedM, 1, 2, 2, ranges);
            compareMaps(mismatches, {family: 'weight1-diagonal', weight, u, a, b}, image, projectPrunedLen5(prunedM, weight));
            let flipped = new Map([[[u, u, a, b, 42, -1, 0, 0, 0].join(','), 1]]);
            flipped = fullDelta(flipped, 0);
            flipped = fullHomotopy(flipped, 1, weight);
            flipped = fullDelta(flipped, 1);
            if (len5Rows(flipped, weight).size || harmonicMap(flipped, 1, weight, 'full').size) {
              throw new Error('A-chart contribution survived in a weight-one diagonal column');
            }
            if (image.size) extraNonzero++;
            const signed = new Map();
            for (const [row, value] of image) signed.set(row, -value);
            remainingColumns.push(signed);
          }
        }
      }
    }

    if (weight === 0) {
      const monomials = oracle.mons([0, 0, 0, 0], [1, 1, 1, 1]);
      const boundaryColumns = [];
      const r1offset = [0, 75, 225];
      for (let u = 0; u < 4; u++) {
        for (let a = 0; a < oracle.ranks[u]; a++) {
          for (let b = 0; b < oracle.ranks[u]; b++) {
            let fullM = new Map([[[u, u, a, b, 40, 0, 0, 0, 0].join(','), 1]]);
            fullM = fullDelta(fullM, 0);
            let prunedM = new Map([[[u, u, a, b, 15, 0, 0, 0, 0].join(','), 1]]);
            prunedM = oracle.delta(prunedM, 0, 1, 1, [[0, 1], [0, 1], [0, 1], [0, 1]]);
            const fullRows = new Map();
            const prunedRows = new Map();
            function absorb(target, state, mode) {
              for (const [key, z] of state) {
                const p = key.split(',').map(Number);
                const charts = mode === 'pruned' ? prunedChart(p[4]) : p[4];
                const exponents = p.slice(5);
                if (!isHarmonic(charts, exponents, 1, 0)) continue;
                const mi = ((exponents[0] * 2 + exponents[1]) * 2 + exponents[2]) * 2 + exponents[3];
                addNum(target, (r1offset[p[0]] + p[2] * oracle.ranks[p[0]] + p[3]) * 16 + mi, z);
              }
            }
            absorb(fullRows, fullM, 'full');
            absorb(prunedRows, prunedM, 'pruned');
            compareMaps(mismatches, {family: 'boundary', u, a, b}, fullRows, prunedRows);
            boundaryColumns.push(fullRows);
          }
        }
      }
      boundaryReport = certifyReport(columnsToRows(boundaryColumns, 3920), 354, 'trivial boundary');
      if (boundaryReport.rank !== 353) throw new Error('Trivial-character boundary rank is not 353');
      const boundaryRows = columnsToRows(boundaryColumns, 3920);

      for (let u = 0; u < 3; u++) {
        for (let a = 0; a < oracle.ranks[u + 1]; a++) {
          for (let b = 0; b < oracle.ranks[u]; b++) {
            for (const m of monomials) {
              extraColumns++;
              let fullM = new Map([[[u, u + 1, a, b, 40, ...m].join(','), 1]]);
              fullM = fullDelta(fullM, 1);
              const image = len5Rows(fullM, 0);
              let prunedM = new Map([[[u, u + 1, a, b, 15, ...m].join(','), 1]]);
              prunedM = oracle.delta(prunedM, 1, 1, 1, [[0, 2], [0, 2], [0, 2], [0, 2]]);
              compareMaps(mismatches, {family: 'weight0-degree-one', u, a, b, monomial: m}, image, projectPrunedLen5(prunedM, 0));
              const flipped = fullDelta(new Map([[[u, u + 1, a, b, 41, ...m].join(','), 1]]), 1);
              if (len5Rows(flipped, 0).size) throw new Error('A-chart contribution survived in a weight-zero column');
              if (image.size) extraNonzero++;
              remainingColumns.push(image);
            }
          }
        }
      }
      for (const row of columnsToRows(remainingColumns, 80 * (3 ** 4))) {
        const acc = new Map();
        for (const [col, z] of row) {
          if (col < sourceKernel.length) continue;
          const boundary = boundaryRows[col - sourceKernel.length];
          for (const [j, w] of boundary) {
            const t = (acc.get(j) || 0n) + z * w;
            if (t === 0n) acc.delete(j);
            else acc.set(j, t);
          }
        }
        if (acc.size) throw new Error('A degree-zero boundary is not a cycle');
      }
    }

    if (mismatches.length !== extraMismatchesAtStart) {
      throw new Error('Extra-column mismatch: ' + JSON.stringify(mismatches[mismatches.length - 1]));
    }

    const rowCount = 80 * [0, 1, 2, 3].map(i => (i < weight ? 1 : 3)).reduce((s, x) => s * x, 1);
    const remaining = certifyReport(columnsToRows(remainingColumns, rowCount), remainingColumns.length, `weight ${weight} remaining`);
    if (remaining.rank !== EXPECTED_REMAINING[weight]) throw new Error('Unexpected remaining rank at weight ' + weight);
    const boundaryRank = weight === 0 ? boundaryReport.rank : 0;
    const h1 = remainingColumns.length - remaining.rank - boundaryRank;
    if (h1 !== EXPECTED_H1[weight]) throw new Error('Unexpected Ext1 at weight ' + weight + ': ' + h1);

    const weightRecord = {
      weight,
      negativeColumns: ncols,
      negativeNonzero,
      negativeHigherTransferNonzero: higherNonzeroColumns.length,
      negativeHigherTransferColumns: weight === 4 ? higherNonzeroColumns : undefined,
      lengthNonzero,
      extraColumns,
      extraNonzero,
      mismatches: mismatches.filter(item => item.weight === weight || (weight === 0 && item.family === 'boundary')).length,
      d1: publicRank(d1),
      d1Nonzeros: d1nnz,
      lengthThree: d3report ? publicRank(d3report) : null,
      remaining: publicRank(remaining),
      boundaryRank,
      h1
    };
    if (weight !== 4) delete weightRecord.negativeHigherTransferColumns;
    byWeight.push(weightRecord);
    rankReports.push({d1, d3: d3report, remaining, boundary: weight === 0 ? boundaryReport : null, h1});
    if (weight === 4) higherColumns = higherNonzeroColumns;
    console.error(`weight ${weight} columns done in ${Date.now() - t0}ms`);
  }

  if (mismatches.length) throw new Error('Mismatches remain: ' + JSON.stringify(mismatches));
  const h1 = byWeight.map(row => row.h1);
  const ext1 = h1.reduce((sum, dim, weight) => sum + MULTIPLICITIES[weight] * dim, 0);
  if (JSON.stringify(h1) !== JSON.stringify(EXPECTED_H1) || ext1 !== 87) {
    throw new Error('Ext1 confirmation failed');
  }
  const total = byWeight.reduce((s, row) => s + row.negativeColumns + row.extraColumns, 0);
  const nonzero = byWeight.reduce((s, row) => s + row.negativeNonzero + row.extraNonzero, 0);
  const weightFour = byWeight[4];
  return {
    pinnedHead: PINNED_HEAD,
    pinnedModelSha256: PINNED_MODEL_SHA256,
    contraction: 'full A/B/C, no chart omission, no exponent filter',
    columns: {
      total,
      nonzero,
      mismatches,
      byWeight: byWeight.map(row => ({
        weight: row.weight,
        negativeColumns: row.negativeColumns,
        negativeNonzero: row.negativeNonzero,
        negativeHigherTransferNonzero: row.negativeHigherTransferNonzero,
        lengthNonzero: row.lengthNonzero,
        extraColumns: row.extraColumns,
        extraNonzero: row.extraNonzero,
        mismatches: row.mismatches
      })),
      weightFour: {
        columns: weightFour.negativeColumns,
        nonzero: weightFour.negativeNonzero,
        mismatches: [],
        higherTransferNonzero: weightFour.negativeHigherTransferNonzero,
        higherTransferColumns: higherColumns,
        lengthNonzero: weightFour.lengthNonzero
      }
    },
    ext1ByWeight: h1,
    multiplicities: MULTIPLICITIES,
    ext1,
    ranks: byWeight.map(row => ({
      weight: row.weight,
      d1: row.d1,
      d1Nonzeros: row.d1Nonzeros,
      lengthThree: row.lengthThree,
      remaining: row.remaining,
      boundaryRank: row.boundaryRank,
      h1: row.h1
    })),
    namedRanks: {
      weightTwoIntermediate: byWeight[2].lengthThree,
      trivialCharacterBoundary: publicRank(rankReports[0].boundary)
    }
  };
}

function main() {
  const result = verify();
  const text = JSON.stringify(result, null, 2) + '\n';
  const expectedPath = path.join(__dirname, 'expected-hsd-unpruned-h1.json');
  if (process.argv.includes('--write-expected')) {
    fs.writeFileSync(expectedPath, text);
  } else {
    const expected = fs.readFileSync(expectedPath, 'utf8');
    if (expected !== text) throw new Error('Result does not match expected-hsd-unpruned-h1.json');
  }
  process.stdout.write(text);
}

main();
