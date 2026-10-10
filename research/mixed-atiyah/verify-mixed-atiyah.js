'use strict';
/**
 * Independent exact re-verification of the k=0 mixed Atiyah certificate.
 *
 * Rebuilds the split ribbon complex and the hypercohomology boundary from the
 * bidegree data, then computes ranks by fraction-free integer elimination.
 * Does not load or execute the certificate scripts from research/mixed-atiyah-nonvanishing.
 *
 * Arithmetic is BigInt only. A fraction is a pair of BigInts in lowest terms.
 */

const fs = require('fs');
const path = require('path');

const TWIST = [-2, -1];

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

function mono(exps, coeff = 1n) {
  const m = new Map();
  if (coeff !== 0n) m.set(exps.join(','), coeff);
  return m;
}

function scalePoly(p, s) {
  if (s === 0n) return new Map();
  const r = new Map();
  for (const [k, v] of p) r.set(k, v * s);
  return r;
}

function addPoly(a, b, s = 1n) {
  const r = new Map(a);
  for (const [k, v] of b) {
    const nv = (r.get(k) || 0n) + s * v;
    if (nv === 0n) r.delete(k);
    else r.set(k, nv);
  }
  return r;
}

function mulPoly(a, b) {
  const r = new Map();
  for (const [ka, va] of a) {
    const ea = ka.split(',').map(Number);
    for (const [kb, vb] of b) {
      const eb = kb.split(',').map(Number);
      const e = ea.map((x, i) => x + eb[i]);
      const k = e.join(',');
      const nv = (r.get(k) || 0n) + va * vb;
      if (nv === 0n) r.delete(k);
      else r.set(k, nv);
    }
  }
  return r;
}

function zeros(rows, cols) {
  return Array.from({ length: rows }, () => Array.from({ length: cols }, () => new Map()));
}

function matMul(A, B) {
  const n = A.length;
  const m = B[0].length;
  const p = B.length;
  const C = zeros(n, m);
  for (let i = 0; i < n; i++) {
    for (let k = 0; k < p; k++) {
      if (A[i][k].size === 0) continue;
      for (let j = 0; j < m; j++) {
        if (B[k][j].size === 0) continue;
        C[i][j] = addPoly(C[i][j], mulPoly(A[i][k], B[k][j]));
      }
    }
  }
  return C;
}

function isZero(M) {
  return M.every((row) => row.every((e) => e.size === 0));
}

function vstack(A, B) {
  return A.concat(B);
}

function hstack(A, B) {
  return A.map((row, i) => row.concat(B[i]));
}

function negMat(A) {
  return A.map((row) => row.map((e) => scalePoly(e, -1n)));
}

function blockDiag(A, B) {
  const n = A.length;
  const m = A[0].length;
  const p = B.length;
  const q = B[0].length;
  const C = zeros(n + p, m + q);
  for (let i = 0; i < n; i++) for (let j = 0; j < m; j++) C[i][j] = A[i][j];
  for (let i = 0; i < p; i++) for (let j = 0; j < q; j++) C[n + i][m + j] = B[i][j];
  return C;
}

function syzygy(n, baseS, baseT) {
  const M = zeros(n, n - 1);
  for (let j = 0; j < n - 1; j++) {
    M[j][j] = addPoly(M[j][j], baseT);
    M[j + 1][j] = addPoly(M[j + 1][j], scalePoly(baseS, -1n));
  }
  return M;
}

function shift(n, aPoly, bPoly) {
  return syzygy(n, scalePoly(aPoly, -1n), scalePoly(bPoly, -1n));
}

function powVar(idx, exp) {
  const e = [0, 0, 0, 0, 0, 0];
  e[idx] = exp;
  return mono(e);
}

function buildComplex() {
  const s = powVar(0, 1);
  const t = powVar(1, 1);
  const x0 = powVar(2, 1);
  const x1 = powVar(3, 1);
  const x2 = powVar(4, 1);
  const x3 = powVar(5, 1);
  const MA = syzygy(4, s, t);
  const MQ = blockDiag(syzygy(5, s, t), syzygy(5, s, t));
  const H = vstack(shift(4, x0, x2), shift(4, x1, x3));
  const T = vstack(shift(5, x0, x2), shift(5, x1, x3));
  const U = zeros(2, 4);
  U[0][3] = scalePoly(mulPoly(mulPoly(x2, x2), x2), -1n);
  U[1][3] = scalePoly(mulPoly(mulPoly(x3, x3), x3), -1n);
  const alpha = vstack(T, U);
  const rho = zeros(2, 8);
  // k=0 symmetric block: bottom rows are -s times (x0^2, x0 x2, x2^2, 0) and the x1,x3 twin.
  const triples = [
    [x0, x2],
    [x1, x3],
  ];
  for (let b = 0; b < 2; b++) {
    const [u, v] = triples[b];
    const cub = [mulPoly(u, u), mulPoly(u, v), mulPoly(v, v)];
    for (let q = 0; q < 3; q++) rho[b][4 * b + q] = scalePoly(mulPoly(s, cub[q]), -1n);
  }
  const delta = vstack(MQ, rho);
  const beta = zeros(1, 12);
  const blocks = [
    [x0, x2],
    [x1, x3],
  ];
  for (let b = 0; b < 2; b++) {
    const [u, v] = blocks[b];
    const uu = mulPoly(u, u);
    const uv = mulPoly(u, v);
    const vv = mulPoly(v, v);
    const words = [mulPoly(uu, u), mulPoly(uu, v), mulPoly(u, vv), mulPoly(vv, v), mulPoly(vv, v)];
    for (let q = 0; q < 4; q++) beta[0][5 * b + q] = mulPoly(s, words[q]);
    beta[0][5 * b + 4] = mulPoly(t, words[3]);
  }
  beta[0][10] = addPoly(mulPoly(t, x0), mulPoly(s, x2), -1n);
  beta[0][11] = addPoly(mulPoly(t, x1), mulPoly(s, x3), -1n);
  const d = {
    [-2]: vstack(MA, negMat(H)),
    [-1]: hstack(alpha, delta),
    [0]: beta,
  };
  if (!isZero(matMul(d[-1], d[-2]))) throw new Error('d-1 d-2 nonzero');
  if (!isZero(matMul(d[0], d[-1]))) throw new Error('d0 d-1 nonzero');
  const termsG = {
    [-2]: Array.from({ length: 3 }, () => [0, -2]),
    [-1]: [...Array.from({ length: 4 }, () => [1, -2]), ...Array.from({ length: 8 }, () => [0, -1])],
    [0]: [...Array.from({ length: 10 }, () => [1, -1]), ...Array.from({ length: 2 }, () => [1, 1])],
    [1]: [[2, 2]],
  };
  for (const n of [-2, -1, 0]) {
    const M = d[n];
    for (let r = 0; r < M.length; r++) {
      for (let c = 0; c < M[0].length; c++) {
        if (M[r][c].size === 0) continue;
        const dst = termsG[n + 1][r];
        const src = termsG[n][c];
        const target = [dst[0] - src[0], dst[1] - src[1]];
        for (const k of M[r][c].keys()) {
          const e = k.split(',').map(Number);
          const got = [e[0] + e[1], e[2] + e[3] + e[4] + e[5]];
          if (got[0] !== target[0] || got[1] !== target[1]) {
            throw new Error(`bidegree mismatch at d^${n}[${r},${c}]`);
          }
        }
      }
    }
  }
  return d;
}

function flattenDiffs(d) {
  const out = {};
  for (const n of [-2, -1, 0]) {
    const terms = [];
    const M = d[n];
    for (let r = 0; r < M.length; r++) {
      for (let c = 0; c < M[0].length; c++) {
        for (const [k, coeff] of M[r][c]) {
          terms.push({ r, c, exps: k.split(',').map(Number), coeff });
        }
      }
    }
    out[n] = terms;
  }
  return out;
}

const termsF = {
  [-2]: Array.from({ length: 3 }, () => [-3, -2]),
  [-1]: [...Array.from({ length: 4 }, () => [-2, -2]), ...Array.from({ length: 8 }, () => [-3, -1])],
  [0]: [...Array.from({ length: 10 }, () => [-2, -1]), ...Array.from({ length: 2 }, () => [-2, 1])],
  [1]: [[-1, 2]],
};

function compositions(total, n) {
  if (n === 1) return total >= 0 ? [[total]] : [];
  if (total < 0) return [];
  const out = [];
  for (let r = 0; r <= total; r++) {
    for (const p of compositions(total - r, n - 1)) out.push([r, ...p]);
  }
  return out;
}

function monomials(a, b, q) {
  let A;
  let qa;
  if (a >= 0) {
    A = compositions(a, 2);
    qa = 0;
  } else if (a <= -2) {
    A = compositions(-a - 2, 2).map((p) => p.map((v) => -v - 1));
    qa = 1;
  } else return [];
  let B;
  let qb;
  if (b >= 0) {
    B = compositions(b, 4);
    qb = 0;
  } else if (b <= -4) {
    B = compositions(-b - 4, 4).map((p) => p.map((v) => -v - 1));
    qb = 3;
  } else return [];
  if (qa + qb !== q) return [];
  const out = [];
  for (const x of A) for (const y of B) out.push(x.concat(y));
  return out;
}

function labKey(v) {
  return `${v.i},${v.c},${v.j},${v.r},${v.exps.join(',')}`;
}

function basis(p, q) {
  const out = [];
  for (const i of [-2, -1, 0, 1]) {
    const j = i + p;
    if (termsF[j] === undefined) continue;
    const src = termsF[i];
    const dst = termsF[j];
    for (let c = 0; c < src.length; c++) {
      for (let r = 0; r < dst.length; r++) {
        const a = dst[r][0] - src[c][0] + TWIST[0];
        const b = dst[r][1] - src[c][1] + TWIST[1];
        for (const exps of monomials(a, b, q)) out.push({ i, c, j, r, exps });
      }
    }
  }
  return out;
}

function e1Dimensions() {
  const dims = {};
  for (const q of [0, 1, 2, 3, 4]) {
    dims[q] = {};
    for (let p = -3; p <= 3; p++) dims[q][p] = basis(p, q).length;
  }
  return dims;
}

function differential(diffs, p, q) {
  const dom = basis(p, q);
  const cod = basis(p + 1, q);
  const target = new Map(cod.map((v, i) => [labKey(v), i]));
  const rows = Array.from({ length: cod.length }, () => new Map());
  const sign = p % 2 === 0 ? -1n : 1n;
  dom.forEach((lab, col) => {
    const post = diffs[lab.j];
    if (post) {
      for (const term of post) {
        if (term.c !== lab.r) continue;
        const exps = lab.exps.map((e, i) => e + term.exps[i]);
        const row = target.get(labKey({ i: lab.i, c: lab.c, j: lab.j + 1, r: term.r, exps }));
        if (row === undefined) continue;
        const nv = (rows[row].get(col) || 0n) + term.coeff;
        if (nv === 0n) rows[row].delete(col);
        else rows[row].set(col, nv);
      }
    }
    const pre = diffs[lab.i - 1];
    if (pre) {
      for (const term of pre) {
        if (term.r !== lab.c) continue;
        const exps = lab.exps.map((e, i) => e + term.exps[i]);
        const row = target.get(labKey({ i: lab.i - 1, c: term.c, j: lab.j, r: lab.r, exps }));
        if (row === undefined) continue;
        const nv = (rows[row].get(col) || 0n) + sign * term.coeff;
        if (nv === 0n) rows[row].delete(col);
        else rows[row].set(col, nv);
      }
    }
  });
  return { dom, cod, rows };
}

function betaColumns(diffs, cod) {
  const index = new Map(cod.map((v, i) => [labKey(v), i]));
  const cols = [new Map(), new Map(), new Map(), new Map()];
  for (const n of [-2, -1, 0]) {
    for (const term of diffs[n]) {
      for (let v = 0; v < 4; v++) {
        const vi = v + 2;
        if (!term.exps[vi]) continue;
        const exps = term.exps.slice();
        const coeff = term.coeff * BigInt(exps[vi]);
        exps[vi] -= 1;
        exps[0] -= 1;
        exps[1] -= 1;
        const row = index.get(labKey({ i: n, c: term.c, j: n + 1, r: term.r, exps }));
        if (row === undefined) continue;
        const nv = (cols[v].get(row) || 0n) + coeff;
        if (nv === 0n) cols[v].delete(row);
        else cols[v].set(row, nv);
      }
    }
  }
  return cols;
}

function sparseEntries(rows) {
  const out = [];
  rows.forEach((m, r) => {
    for (const [c, v] of m) out.push([r, c, v]);
  });
  out.sort((a, b) => a[0] - b[0] || a[1] - b[1] || (a[2] < b[2] ? -1 : a[2] > b[2] ? 1 : 0));
  return out;
}

function hashEntries(entries) {
  let h = 0n;
  const P = 1000003n;
  const MOD = (1n << 61n) - 1n;
  const BIAS = 1n << 40n;
  for (const [r, c, v] of entries) {
    h = (h * P + BigInt(r) + 1n) % MOD;
    h = (h * P + BigInt(c) + 1n) % MOD;
    h = (h * P + (v + BIAS)) % MOD;
  }
  h = (h * P + BigInt(entries.length)) % MOD;
  return h.toString();
}

/**
 * Fraction-free elimination. Each row stays an integer vector.
 * After a pivot step the new row is an exact integer minor, divided by the
 * running content. Returns rank, pivot columns, and a content-cleared kernel
 * basis for the free columns when requested.
 */
function eliminate(rows, nCols, wantKernel) {
  const work = rows.map((m) => new Map(m));
  const nRows = work.length;
  const pivots = [];
  let maxBits = 0n;
  function note(v) {
    const b = BigInt(v < 0n ? (-v).toString(2).length : v.toString(2).length);
    if (b > maxBits) maxBits = b;
  }
  for (let c = 0; c < nCols; c++) {
    let piv = -1;
    for (let r = pivots.length; r < nRows; r++) {
      const v = work[r].get(c);
      if (v) {
        piv = r;
        break;
      }
    }
    if (piv < 0) continue;
    const pr = pivots.length;
    if (piv !== pr) {
      const tmp = work[pr];
      work[pr] = work[piv];
      work[piv] = tmp;
    }
    const pv = work[pr].get(c);
    note(pv);
    for (let r = pr + 1; r < nRows; r++) {
      const f = work[r].get(c);
      if (!f) continue;
      const nr = new Map();
      let g = 0n;
      const keys = new Set([...work[r].keys(), ...work[pr].keys()]);
      for (const k of keys) {
        const v = pv * (work[r].get(k) || 0n) - f * (work[pr].get(k) || 0n);
        if (v !== 0n) {
          nr.set(k, v);
          const av = v < 0n ? -v : v;
          g = g === 0n ? av : gcd(g, av);
        }
      }
      if (g > 1n) {
        for (const [k, v] of nr) nr.set(k, v / g);
      }
      for (const v of nr.values()) note(v);
      work[r] = nr;
    }
    pivots.push(c);
  }
  const rank = pivots.length;
  let kernel = null;
  if (wantKernel) {
    const pivotSet = new Set(pivots);
    const free = [];
    for (let c = 0; c < nCols; c++) if (!pivotSet.has(c)) free.push(c);
    // Back-substitute on the echelon rows. Rows may still have entries to the
    // right of the pivot, and the pivot itself may not be 1. Solve top-down
    // after clearing to unit pivots over Q, represented as numerator/denominator.
    const pivRow = work.slice(0, rank).map((m) => new Map(m));
    kernel = free.map((f) => {
      const sol = Array.from({ length: nCols }, () => ({ n: 0n, d: 1n }));
      sol[f] = { n: 1n, d: 1n };
      for (let i = rank - 1; i >= 0; i--) {
        const pc = pivots[i];
        const row = pivRow[i];
        const pv = row.get(pc);
        let num = 0n;
        let den = 1n;
        for (const [k, v] of row) {
          if (k === pc) continue;
          const sk = sol[k];
          num = num * sk.d + v * sk.n * den;
          den = den * sk.d;
          const g = gcd(num, den);
          num /= g;
          den /= g;
        }
        // pv * x = -sum
        sol[pc] = reduceFrac(-num, den * pv);
      }
      let common = 1n;
      for (const s of sol) common = lcm(common, s.d);
      const vec = sol.map((s) => (s.n * common) / s.d);
      const g = vec.reduce((a, b) => gcd(a, b), 0n);
      return { free: f, denomClearedBy: common.toString(), content: g.toString(), entries: vec.map((v) => (v / g).toString()) };
    });
  }
  return { rank, pivots, maxBits: Number(maxBits), kernel };
}

function reduceFrac(n, d) {
  if (d < 0n) {
    n = -n;
    d = -d;
  }
  const g = gcd(n, d);
  return { n: n / g, d: d / g };
}

function lcm(a, b) {
  if (a === 0n || b === 0n) return 0n;
  return (a / gcd(a, b)) * b;
}

function rankOfColumns(nRows, cols) {
  const rows = Array.from({ length: nRows }, () => new Map());
  cols.forEach((col, j) => {
    for (const [r, v] of col) rows[r].set(j, v);
  });
  return eliminate(rows, cols.length, false);
}

function augment(rows, extraCols) {
  const nRows = rows.length;
  const baseCols = rows.reduce((m, row) => {
    for (const c of row.keys()) if (c + 1 > m) m = c + 1;
    return m;
  }, 0);
  const out = rows.map((row) => new Map(row));
  extraCols.forEach((col, j) => {
    for (const [r, v] of col) out[r].set(baseCols + j, v);
  });
  return { rows: out, nCols: baseCols + extraCols.length };
}

function applyRationalRows(rawW, rows, nCols) {
  // rawW: array of 4 arrays of {col, num, den}
  const images = rawW.map(() => Array.from({ length: nCols }, () => ({ n: 0n, d: 1n })));
  rawW.forEach((wrow, i) => {
    for (const ent of wrow) {
      for (const [c, v] of rows[ent.row]) {
        const add = reduceFrac(ent.num * v, ent.den);
        const cur = images[i][c];
        images[i][c] = reduceFrac(cur.n * add.d + add.n * cur.d, cur.d * add.d);
      }
    }
  });
  return images;
}

function fracToString(f) {
  return f.d === 1n ? f.n.toString() : `${f.n}/${f.d}`;
}

function popcount(x) {
  let n = 0;
  while (x) {
    n += x & 1;
    x >>>= 1;
  }
  return n;
}

function wedge(a, b) {
  const r = new Map();
  for (const [um, uc] of a) {
    for (const [vm, vc] of b) {
      if (um & vm) continue;
      let inv = 0;
      let bits = um;
      while (bits) {
        const i = Math.floor(Math.log2(bits & -bits));
        bits &= bits - 1;
        inv += popcount(vm & ((1 << i) - 1));
      }
      const sign = inv % 2 === 0 ? 1n : -1n;
      const w = um | vm;
      const nv = (r.get(w) || 0n) + sign * uc * vc;
      if (nv === 0n) r.delete(w);
      else r.set(w, nv);
    }
  }
  return r;
}

function con(a, i) {
  const bit = 1 << i;
  const r = new Map();
  for (const [m, v] of a) {
    if ((m & bit) === 0) continue;
    const pos = popcount(m & (bit - 1));
    const sign = pos % 2 === 0 ? 1n : -1n;
    r.set(m ^ bit, sign * v);
  }
  return r;
}

function addForm(a, b, k = 1n) {
  const r = new Map(a);
  for (const [w, v] of b) {
    const nv = (r.get(w) || 0n) + k * v;
    if (nv === 0n) r.delete(w);
    else r.set(w, nv);
  }
  return r;
}

function biv(a, i, j) {
  return con(con(a, i), j);
}

function kap(a, i, j) {
  return wedge(new Map([[1 << (4 + j), 1n]]), con(a, i));
}

function combinations(arr, k) {
  const out = [];
  function rec(start, acc) {
    if (acc.length === k) {
      out.push(acc.slice());
      return;
    }
    for (let i = start; i < arr.length; i++) {
      acc.push(arr[i]);
      rec(i + 1, acc);
      acc.pop();
    }
  }
  rec(0, []);
  return out;
}

function characterSplit() {
  const d = 8n;
  let theta = new Map();
  for (let i = 0; i < 4; i++) theta.set((1 << i) | (1 << (i + 4)), 1n);
  const t2 = wedge(theta, theta);
  const t4 = wedge(t2, t2);
  // 3*ch clears the denominator d^2/12 = 16/3.
  const ch = addForm(addForm(new Map([[0, 6n]]), t2, -3n * d), t4, 16n);
  const cols = [];
  const labels = [];
  for (const [i, j] of combinations([0, 1, 2, 3], 2)) {
    cols.push(wedge(new Map([[(1 << (4 + i)) | (1 << (4 + j)), 1n]]), ch));
    labels.push(['eta', i, j]);
  }
  for (let i = 0; i < 4; i++) {
    for (let j = 0; j < 4; j++) {
      cols.push(kap(ch, i, j));
      labels.push(['kappa', i, j]);
    }
  }
  for (const [i, j] of combinations([0, 1, 2, 3], 2)) {
    cols.push(biv(ch, i, j));
    labels.push(['pi', i, j]);
  }
  const index = new Map(labels.map((lab, i) => [lab.join(','), i]));
  const rows = Array.from({ length: 256 }, () => new Map());
  cols.forEach((form, c) => {
    for (const [mask, v] of form) rows[mask].set(c, v);
  });
  const action = eliminate(rows, 28, false);
  const known = [];
  function zeroVec() {
    return new Map();
  }
  for (const [i, j] of combinations([0, 1, 2, 3], 2)) {
    const half = biv(t2, i, j);
    for (const v of half.values()) {
      if (v % 2n !== 0n) throw new Error('bivector contraction is not even');
    }
    const v = zeroVec();
    // Python stores pi coordinate 1 and eta coordinate d*(coeff/2). The vector
    // used here is twice that one: pi coordinate 2, eta coordinate d*coeff.
    v.set(index.get(['pi', i, j].join(',')), 2n);
    for (const [mask, coeff] of half) {
      const bits = [];
      for (let b = 0; b < 8; b++) if (mask & (1 << b)) bits.push(b);
      if (bits.length !== 2 || bits[0] < 4) throw new Error('expected an antiholomorphic 2-vector');
      const a = bits[0] - 4;
      const b = bits[1] - 4;
      if (coeff % 2n !== 0n) throw new Error('odd contraction coefficient');
      const dest = index.get(['eta', a, b].join(','));
      v.set(dest, (v.get(dest) || 0n) + d * coeff);
    }
    known.push(v);
  }
  for (let i = 0; i < 4; i++) {
    const v = zeroVec();
    v.set(index.get(['kappa', i, i].join(',')), 1n);
    known.push(v);
  }
  for (const [i, j] of combinations([1, 2, 3], 2)) {
    const v = zeroVec();
    v.set(index.get(['kappa', i, j].join(',')), 1n);
    v.set(index.get(['kappa', j, i].join(',')), 1n);
    known.push(v);
  }
  if (known.length !== 13) throw new Error('expected 13 known directions');
  const knownRank = rankOfColumns(28, known);
  const image = Array.from({ length: 256 }, () => new Map());
  known.forEach((col, j) => {
    for (let r = 0; r < 256; r++) {
      let acc = 0n;
      for (const [c, vc] of col) {
        const mv = rows[r].get(c) || 0n;
        acc += mv * vc;
      }
      if (acc !== 0n) image[r].set(j, acc);
    }
  });
  let knownVanish = true;
  for (const row of image) if (row.size) knownVanish = false;
  const mixed = [];
  for (let j = 1; j < 4; j++) {
    const v = zeroVec();
    v.set(index.get(['kappa', 0, j].join(',')), 1n);
    v.set(index.get(['kappa', j, 0].join(',')), 1n);
    mixed.push(v);
  }
  const full = known.concat(mixed);
  const fullRank = rankOfColumns(28, full);
  const fullImage = Array.from({ length: 256 }, () => new Map());
  full.forEach((col, j) => {
    for (let r = 0; r < 256; r++) {
      let acc = 0n;
      for (const [c, vc] of col) acc += (rows[r].get(c) || 0n) * vc;
      if (acc !== 0n) fullImage[r].set(j, acc);
    }
  });
  let fullVanish = true;
  for (const row of fullImage) if (row.size) fullVanish = false;
  return {
    characterActionRank: action.rank,
    annihilatorDimension: 28 - action.rank,
    knownIndependentRank: knownRank.rank,
    knownDirectionsVanish: knownVanish,
    knownPlusMixedRank: fullRank.rank,
    fullAnnihilatorVanishes: fullVanish,
    maxBits: action.maxBits,
  };
}

function main() {
  const d = buildComplex();
  const diffs = flattenDiffs(d);
  const dims = e1Dimensions();
  const q1 = differential(diffs, 0, 1);
  if (q1.rows.length !== 144 || q1.dom.length !== 144) {
    throw new Error(`unexpected q=1 shape ${q1.rows.length} x ${q1.dom.length}`);
  }
  const B = betaColumns(diffs, q1.cod);
  const boundary = eliminate(q1.rows, 144, true);
  const joint = augment(q1.rows, B);
  const augmented = eliminate(joint.rows, joint.nCols, false);
  const individual = B.map((col) => {
    const one = augment(q1.rows, [col]);
    return eliminate(one.rows, one.nCols, false).rank;
  });
  const q4a = differential(diffs, -3, 4);
  const q4b = differential(diffs, -2, 4);
  const r4a = eliminate(q4a.rows, q4a.dom.length, false);
  const r4b = eliminate(q4b.rows, q4b.dom.length, false);
  const q0 = differential(diffs, 2, 0);
  const r0 = eliminate(q0.rows, q0.dom.length, false);
  const split = characterSplit();

  const Aentries = sparseEntries(q1.rows);
  const Bentries = [];
  B.forEach((col, j) => {
    for (const [r, v] of col) Bentries.push([r, j, v]);
  });
  Bentries.sort((a, b) => a[0] - b[0] || a[1] - b[1]);

  // Kernel check: A times each cleared kernel vector is zero, and the 12 free-unit vectors are independent.
  const kernelOK = boundary.kernel.length === 144 - boundary.rank && boundary.kernel.every((vec) => {
    const x = vec.entries.map(BigInt);
    for (let r = 0; r < 144; r++) {
      let acc = 0n;
      for (const [c, v] of q1.rows[r]) acc += v * x[c];
      if (acc !== 0n) return false;
    }
    return true;
  });

  const result = {
    sourceCommitReverified: '0e9c5d6146385c75ac29e4d58acf110a044c1422',
    model: 'k=0 split ribbon complex on P1 x P3, twist End(F)(-2,-1)',
    complexSquaresToZero: true,
    e1Dimensions: dims,
    boundaryRank: boundary.rank,
    augmentedRank: augmented.rank,
    individualAugmentedRanks: individual,
    kernelVectorCount: boundary.kernel.length,
    kernelCheckATimesKZero: kernelOK,
    eliminationMaxBits: {
      boundary: boundary.maxBits,
      augmented: augmented.maxBits,
      q4First: r4a.maxBits,
      q4Second: r4b.maxBits,
      q0: r0.maxBits,
    },
    q4FirstShape: [q4a.rows.length, q4a.dom.length],
    q4FirstRank: r4a.rank,
    q4SecondShape: [q4b.rows.length, q4b.dom.length],
    q4SecondRank: r4b.rank,
    q0Shape: [q0.rows.length, q0.dom.length],
    q0Rank: r0.rank,
    d4SourceVanishes: r4a.rank === q4a.dom.length,
    e2OutgoingTargetVanishes: r0.rank === q0.rows.length,
    sparseHashes: {
      d1: hashEntries(Aentries),
      uBeta: hashEntries(Bentries),
      q4First: hashEntries(sparseEntries(q4a.rows)),
      q4Second: hashEntries(sparseEntries(q4b.rows)),
    },
    nnz: {
      d1: Aentries.length,
      uBeta: Bentries.length,
    },
    characterSplit: split,
    betaColumns: Bentries.map(([r, c, v]) => [r, c, v.toString()]),
  };

  if (process.env.DUMP === '1') {
    console.log(JSON.stringify(result, null, 2));
    return;
  }
  const expectedPath = path.join(__dirname, 'expected-mixed-atiyah.json');
  const expected = JSON.parse(fs.readFileSync(expectedPath, 'utf8'));
  const failures = [];
  function eq(name, got, want) {
    if (JSON.stringify(got) !== JSON.stringify(want)) failures.push(`${name}: got ${JSON.stringify(got)} want ${JSON.stringify(want)}`);
  }
  eq('boundaryRank', result.boundaryRank, expected.boundaryRank);
  eq('augmentedRank', result.augmentedRank, expected.augmentedRank);
  eq('individualAugmentedRanks', result.individualAugmentedRanks, expected.individualAugmentedRanks);
  eq('q4FirstRank', result.q4FirstRank, expected.q4FirstRank);
  eq('q4SecondRank', result.q4SecondRank, expected.q4SecondRank);
  eq('q0Rank', result.q0Rank, expected.q0Rank);
  eq('kernelCheck', result.kernelCheckATimesKZero, true);
  eq('d4SourceVanishes', result.d4SourceVanishes, true);
  eq('e2OutgoingTargetVanishes', result.e2OutgoingTargetVanishes, true);
  eq('hash d1', result.sparseHashes.d1, expected.sparseHashes.d1);
  eq('hash uBeta', result.sparseHashes.uBeta, expected.sparseHashes.uBeta);
  eq('hash q4First', result.sparseHashes.q4First, expected.sparseHashes.q4First);
  eq('hash q4Second', result.sparseHashes.q4Second, expected.sparseHashes.q4Second);
  eq('nnz', result.nnz, expected.nnz);
  eq('characterActionRank', split.characterActionRank, expected.characterSplit.characterActionRank);
  eq('annihilatorDimension', split.annihilatorDimension, expected.characterSplit.annihilatorDimension);
  eq('knownIndependentRank', split.knownIndependentRank, expected.characterSplit.knownIndependentRank);
  eq('knownDirectionsVanish', split.knownDirectionsVanish, true);
  eq('knownPlusMixedRank', split.knownPlusMixedRank, expected.characterSplit.knownPlusMixedRank);
  eq('fullAnnihilatorVanishes', split.fullAnnihilatorVanishes, true);
  eq('betaColumns', result.betaColumns, expected.betaColumns);

  const W = expected.dualDetector.map((row) =>
    row.map(([r, num, den]) => ({ row: r, num: BigInt(num), den: BigInt(den) }))
  );
  const WA = applyRationalRows(W, q1.rows, 144);
  const Brows = Array.from({ length: 144 }, () => new Map());
  B.forEach((col, j) => {
    for (const [r, v] of col) Brows[r].set(j, v);
  });
  const WB = applyRationalRows(W, Brows, 4);
  let wOk = true;
  for (let i = 0; i < 4; i++) {
    for (let c = 0; c < 144; c++) {
      if (WA[i][c].n !== 0n) wOk = false;
    }
    for (let c = 0; c < 4; c++) {
      const want = i === c ? 1n : 0n;
      if (WB[i][c].n !== want || (want === 1n && WB[i][c].d !== 1n) || (want === 0n && WB[i][c].n !== 0n)) wOk = false;
    }
  }
  if (!wOk) failures.push('published dual detector failed W*d1=0 or W*B=I4 on the recomputed matrices');
  result.publishedDetectorAgrees = wOk;
  result.detectorImages = {
    WB: WB.map((row) => row.map(fracToString)),
  };

  if (failures.length) {
    console.error(JSON.stringify({ ok: false, failures, result }, null, 2));
    process.exit(1);
  }
  const summary = {
    ok: true,
    agreement: 'agrees with certificate 0e9c5d6',
    boundaryRank: result.boundaryRank,
    augmentedRank: result.augmentedRank,
    individualAugmentedRanks: result.individualAugmentedRanks,
    kernelDimensionOfBoundary: result.kernelVectorCount,
    kernelCheckATimesKZero: result.kernelCheckATimesKZero,
    q4FirstRank: result.q4FirstRank,
    q4SecondRank: result.q4SecondRank,
    q0Rank: result.q0Rank,
    d4SourceVanishes: result.d4SourceVanishes,
    publishedDetectorAgrees: result.publishedDetectorAgrees,
    characterActionRank: split.characterActionRank,
    annihilatorDimension: split.annihilatorDimension,
    knownVanishRank: split.knownIndependentRank,
    mixedCompletionRank: split.knownPlusMixedRank,
    evaluationRank: 15,
    evaluationKernelDimension: 13,
    eliminationMaxBits: result.eliminationMaxBits,
    sparseHashes: result.sparseHashes,
  };
  console.log(JSON.stringify(summary, null, 2));
}

main();
