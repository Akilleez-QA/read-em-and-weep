'use strict';

// Independent finite model for the Horrocks–Mumford pullback Ext^1 calculation.
//
// Built from the definitions in research/hm/ext-model.md (PR #5) and the bundle
// in research/hm-smooth-family.md (PR #3). This file does not import or adapt
// the pinned verifier. Arithmetic is dependency-free BigInt.
//
// Complex. V has basis e0..e4 and vol(e0,...,e4)=1. For i mod 5,
//   w+_i = e_{i+2}∧e_{i+3},  w-_i = e_{i+1}∧e_{i+4}.
// W = ker(b: (Λ²V*)² → C^5), b(η+,η-)_i = η+(w-_i)−η-(w+_i), with basis
//   U_i=(dual(w+_i),0), V_i=(0,dual(w-_i)), Z_i=(dual(w-_i),dual(w+_i)).
// φ_v(w)(u1,u2)=vol(v,w,u1,u2), γ_i(v)=(φ_v(w+_i), φ_v(w-_i)).
// The monad, after cancelling the constant surjection, is
//   5 O(−1) --γ--> W⊗O --ι_v--> (V*)²⊗O(1) --ev_v--> C²⊗O(2).
// ι_v(dual(e_p∧e_q)) = v_p e*_q − v_q e*_p, and ev evaluates each copy on v.
// On Y=(P¹)^4 the coordinates are the elementary symmetric polynomials
// v_k = e_k(x1,x2,x3,x4), expanded as squarefree monomials.
//
// Deck character of weight w is represented by S={1,...,w} on the first w
// factors, twisting those factors by O(−2). Čech data use the two-chart model
//   C⁰ = C[x] ⊕ x^n C[x^{−1}],  C¹ = C[x,x^{−1}],  d(a,b)=b−a,
// charts A (finite), B (infinity, finite-chart frame), C (overlap).
//   h(x^e) = (−x^e, 0) if e≥0; (0, x^e) if e<0 and e≤n; 0 otherwise.
// The four-factor homotopy is the Koszul tensor contraction
//   H = Σ_j (ip)_1⊗···⊗(ip)_{j−1}⊗h_j⊗id_{j+1}⊗···⊗id_4.
// For internal degree r and Čech degree p, Δ=(−1)^p[d,−], with the graded
// commutator [d,f]=df−(−1)^r fd. The transferred differential is
//   D_fin = p Δ Σ_{j=0}^{4} (−HΔ)^j i.
// H⁰ inclusion is x^e ↦ (x^e, x^e). H¹ inclusion is the Laurent monomial.
// Projection keeps H¹ exponents on C and the nonnegative part of B.

const crypto = require('crypto');

const RANKS = [5, 15, 10, 2];
const BLOCK = [10, 80, 245, 354, 245, 80, 10]; // internal degrees −3..3
const MULTIPLICITIES = [1, 4, 6, 4, 1];
const POW3 = [1, 3, 9, 27];
const CECH_OF = Array.from({length: 81}, (_, code) => {
  let degree = 0;
  for (let i = 0; i < 4; i++) if (Math.floor(code / POW3[i]) % 3 === 0) degree++;
  return degree;
});

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

function permutationSign(indices) {
  if (new Set(indices).size < indices.length) return 0;
  let inversions = 0;
  for (let i = 0; i < indices.length; i++) {
    for (let j = i + 1; j < indices.length; j++) if (indices[i] > indices[j]) inversions++;
  }
  return inversions % 2 === 0 ? 1 : -1;
}

function wPlus(i) {
  return [(i + 2) % 5, (i + 3) % 5];
}

function wMinus(i) {
  return [(i + 1) % 5, (i + 4) % 5];
}

function volume(indices) {
  return permutationSign(indices);
}

function buildLineComplex() {
  const gamma = Array.from({length: 15}, () => Array.from({length: 5}, () => Array(5).fill(0)));
  for (let target = 0; target < 5; target++) {
    for (let vector = 0; vector < 5; vector++) {
      const plus = wPlus(target);
      const minus = wMinus(target);
      for (let r = 0; r < 5; r++) {
        gamma[r][target][vector] = volume([vector, ...plus, ...wPlus(r)]);
        gamma[5 + r][target][vector] = volume([vector, ...minus, ...wMinus(r)]);
        gamma[10 + r][target][vector] = volume([vector, ...plus, ...wMinus(r)]);
      }
    }
  }

  for (let target = 0; target < 5; target++) {
    for (let vector = 0; vector < 5; vector++) {
      for (let i = 0; i < 5; i++) {
        const onMinus = volume([vector, ...wPlus(target), ...wMinus(i)]);
        const onPlus = volume([vector, ...wMinus(target), ...wPlus(i)]);
        if (onMinus !== onPlus) {
          throw new Error(`γ_${target}(e_${vector}) is not in ker b at coordinate ${i}`);
        }
      }
    }
  }

  const forward = [0, 1, 2].map((level) => Array.from({length: RANKS[level]}, () => []));
  for (let source = 0; source < 5; source++) {
    for (let row = 0; row < 15; row++) {
      for (let sym = 0; sym < 5; sym++) {
        const coefficient = gamma[row][source][sym];
        if (coefficient) forward[0][source].push({to: row, k: sym, z: coefficient});
      }
    }
  }

  function addContraction(source, copy, p, q) {
    forward[1][source].push({to: copy * 5 + q, k: p, z: 1});
    forward[1][source].push({to: copy * 5 + p, k: q, z: -1});
  }
  for (let i = 0; i < 5; i++) {
    addContraction(i, 0, ...wPlus(i));
    addContraction(5 + i, 1, ...wMinus(i));
    addContraction(10 + i, 0, ...wMinus(i));
    addContraction(10 + i, 1, ...wPlus(i));
  }
  for (let copy = 0; copy < 2; copy++) {
    for (let vector = 0; vector < 5; vector++) {
      forward[2][copy * 5 + vector].push({to: copy, k: vector, z: 1});
    }
  }

  const incoming = forward.map((columns, level) => Array.from({length: RANKS[level + 1]}, () => []));
  forward.forEach((columns, level) => {
    columns.forEach((edges, source) => {
      for (const edge of edges) incoming[level][edge.to].push({from: source, k: edge.k, z: edge.z});
    });
  });

  for (let level = 0; level < 2; level++) {
    for (let source = 0; source < RANKS[level]; source++) {
      const accumulator = new Map();
      for (const first of forward[level][source]) {
        for (const second of forward[level + 1][first.to]) {
          const lo = Math.min(first.k, second.k);
          const hi = Math.max(first.k, second.k);
          const key = `${second.to},${lo},${hi}`;
          accumulator.set(key, (accumulator.get(key) || 0) + first.z * second.z);
        }
      }
      for (const value of accumulator.values()) {
        if (value !== 0) throw new Error(`Line complex composition ${level} is not zero`);
      }
    }
  }

  return {gamma, forward, incoming};
}

function monomials(lo, hi) {
  const out = [];
  for (let e0 = lo[0]; e0 <= hi[0]; e0++) {
    for (let e1 = lo[1]; e1 <= hi[1]; e1++) {
      for (let e2 = lo[2]; e2 <= hi[2]; e2++) {
        for (let e3 = lo[3]; e3 <= hi[3]; e3++) out.push([e0, e1, e2, e3]);
      }
    }
  }
  return out;
}

function squarefreeFamilies() {
  const families = Array.from({length: 5}, () => []);
  for (let mask = 0; mask < 16; mask++) {
    const bits = [0, 1, 2, 3].map((i) => (mask >> i) & 1);
    families[bits.reduce((sum, bit) => sum + bit, 0)].push(bits);
  }
  return families;
}

function bundleDegrees(internal, weight) {
  return [0, 1, 2, 3].map((i) => internal - (i < weight ? 2 : 0));
}

function harmonicDimension(degree, cohomological) {
  if (cohomological === 0) return degree >= 0 ? degree + 1 : 0;
  if (cohomological === 1) return degree <= -2 ? -degree - 1 : 0;
  throw new Error('Only Čech/H degrees 0 and 1 occur on P¹');
}

function finiteSpaceDimensions() {
  const byTotal = [0, 0, 0, 0, 0];
  let all = 0;
  for (let weight = 0; weight <= 4; weight++) {
    for (let internal = -3; internal <= 3; internal++) {
      const degrees = bundleDegrees(internal, weight);
      const blocks = BLOCK[internal + 3];
      for (let mask = 0; mask < 16; mask++) {
        let dimension = 1;
        let cech = 0;
        for (let i = 0; i < 4; i++) {
          const useH1 = (mask >> i) & 1;
          dimension *= harmonicDimension(degrees[i], useH1);
          if (useH1) cech++;
        }
        const contribution = MULTIPLICITIES[weight] * blocks * dimension;
        all += contribution;
        const total = internal + cech;
        if (total >= 0 && total <= 4) byTotal[total] += contribution;
      }
    }
  }
  return {byTotal, all};
}

const BIAS = 16;
const EXP_RADIX = 40;

function pack(u, v, a, b, charts, exp) {
  let key = u;
  key = key * 4 + v;
  key = key * 16 + a;
  key = key * 16 + b;
  key = key * 81 + charts;
  key = key * EXP_RADIX + (exp[0] + BIAS);
  key = key * EXP_RADIX + (exp[1] + BIAS);
  key = key * EXP_RADIX + (exp[2] + BIAS);
  key = key * EXP_RADIX + (exp[3] + BIAS);
  return key;
}

function unpack(key) {
  let x = key;
  const exp = [0, 0, 0, 0];
  for (let i = 3; i >= 0; i--) {
    exp[i] = (x % EXP_RADIX) - BIAS;
    x = Math.floor(x / EXP_RADIX);
  }
  const charts = x % 81;
  x = Math.floor(x / 81);
  const b = x % 16;
  x = Math.floor(x / 16);
  const a = x % 16;
  x = Math.floor(x / 16);
  const v = x % 4;
  const u = Math.floor(x / 4);
  return {u, v, a, b, charts, exp};
}

function chartAt(charts, i) {
  return Math.floor(charts / POW3[i]) % 3;
}

function setChart(charts, i, value) {
  const current = Math.floor(charts / POW3[i]) % 3;
  return charts + (value - current) * POW3[i];
}

function addBig(map, key, value) {
  const next = (map.get(key) || 0n) + value;
  if (next === 0n) map.delete(key);
  else map.set(key, next);
}

function canReach(exp, remaining, window) {
  for (let i = 0; i < 4; i++) {
    if (window[i][0] > window[i][1]) return false;
    if (exp[i] > window[i][1]) return false;
    if (exp[i] + remaining < window[i][0]) return false;
  }
  return true;
}

function applyDelta(states, internal, forward, incoming, families, remainingAfter, window) {
  const out = new Map();
  const rightSign = internal % 2 === 0 ? -1n : 1n;
  for (const [key, coeff] of states) {
    const state = unpack(key);
    const sign = CECH_OF[state.charts] % 2 === 0 ? 1n : -1n;
    const base = coeff * sign;
    if (state.v < 3) {
      for (const edge of forward[state.v][state.a]) {
        const scale = base * BigInt(edge.z);
        for (const shift of families[edge.k]) {
          const exp = [
            state.exp[0] + shift[0],
            state.exp[1] + shift[1],
            state.exp[2] + shift[2],
            state.exp[3] + shift[3]
          ];
          if (!canReach(exp, remainingAfter, window)) continue;
          addBig(out, pack(state.u, state.v + 1, edge.to, state.b, state.charts, exp), scale);
        }
      }
    }
    if (state.u > 0) {
      for (const edge of incoming[state.u - 1][state.b]) {
        const scale = base * rightSign * BigInt(edge.z);
        for (const shift of families[edge.k]) {
          const exp = [
            state.exp[0] + shift[0],
            state.exp[1] + shift[1],
            state.exp[2] + shift[2],
            state.exp[3] + shift[3]
          ];
          if (!canReach(exp, remainingAfter, window)) continue;
          addBig(out, pack(state.u - 1, state.v, state.a, edge.from, state.charts, exp), scale);
        }
      }
    }
  }
  return out;
}

function applyHomotopy(states, internal, weight) {
  const degree = bundleDegrees(internal, weight);
  const out = new Map();
  for (const [key, coeff] of states) {
    const state = unpack(key);
    for (let j = 0; j < 4; j++) {
      if (chartAt(state.charts, j) !== 0) continue;
      let preceding = 0;
      let good = true;
      for (let i = 0; i < j; i++) {
        const chart = chartAt(state.charts, i);
        const exponent = state.exp[i];
        if (chart === 0) {
          preceding++;
          if (!(exponent > degree[i] && exponent < 0)) good = false;
        } else if (chart === 1) {
          if (!(exponent >= 0 && exponent <= degree[i])) good = false;
        } else {
          good = false;
        }
        if (!good) break;
      }
      if (!good) continue;
      const exponent = state.exp[j];
      const koszul = preceding % 2 === 0 ? 1n : -1n;
      if (exponent >= 0) {
        addBig(out, pack(state.u, state.v, state.a, state.b, setChart(state.charts, j, 2), state.exp), coeff * koszul * -1n);
      } else if (exponent <= degree[j]) {
        addBig(out, pack(state.u, state.v, state.a, state.b, setChart(state.charts, j, 1), state.exp), coeff * koszul);
      }
    }
  }
  return out;
}

function negateStates(states) {
  const out = new Map();
  for (const [key, coeff] of states) out.set(key, -coeff);
  return out;
}

function transfer(initial, steps, internalStart, weight, window, forward, incoming, families) {
  let current = initial;
  let last = current;
  for (let j = 0; j < steps; j++) {
    last = applyDelta(current, internalStart + j, forward, incoming, families, steps - j - 1, window);
    current = j + 1 < steps ? negateStates(applyHomotopy(last, internalStart + j + 1, weight)) : last;
  }
  return last;
}

function exponentWindow(internal, weight) {
  return bundleDegrees(internal, weight).map((degree) => {
    if (degree >= 0) return [0, degree];
    if (degree <= -2) return [degree + 1, -1];
    return [1, 0];
  });
}

function indexBox(exponents, lo, rad) {
  let index = 0;
  for (let i = 0; i < 4; i++) {
    const shifted = exponents[i] - lo[i];
    if (shifted < 0 || shifted >= rad[i]) return null;
    index = index * rad[i] + shifted;
  }
  return index;
}

const DIAGONAL_OFFSET = [0, 25, 250, 350];
const POSITIVE_OFFSET = [0, 75, 225];

function projectLengthOne(states, weight) {
  const lo = [0, 1, 2, 3].map((i) => (i < weight ? -3 : -1));
  const rad = lo.map((value) => -1 - value + 1);
  const count = rad.reduce((product, value) => product * value, 1);
  const image = new Map();
  for (const [key, coeff] of states) {
    const state = unpack(key);
    if (state.v - state.u !== -2 || state.charts !== 0) continue;
    const monomial = indexBox(state.exp, lo, rad);
    if (monomial === null) continue;
    let block = null;
    if (state.u === 2 && state.v === 0) block = state.a * 10 + state.b;
    else if (state.u === 3 && state.v === 1) block = 50 + state.a * 2 + state.b;
    if (block === null || block < 0 || block >= 80) {
      throw new Error('Length-one state is outside the 80 endomorphism blocks');
    }
    addBig(image, block * count + monomial, coeff);
  }
  return {image, rows: 80 * count};
}

function projectLengthFive(states, weight) {
  const rad = [0, 1, 2, 3].map((i) => (i < weight ? 1 : 3));
  const count = rad.reduce((product, value) => product * value, 1);
  const charts = 40; // every factor on B
  const image = new Map();
  for (const [key, coeff] of states) {
    const state = unpack(key);
    if (state.v - state.u !== 2 || state.charts !== charts) continue;
    const monomial = indexBox(state.exp, [0, 0, 0, 0], rad);
    if (monomial === null) continue;
    let block = null;
    if (state.u === 0 && state.v === 2) block = state.a * 5 + state.b;
    else if (state.u === 1 && state.v === 3) block = 50 + state.a * 15 + state.b;
    if (block === null || block < 0 || block >= 80) {
      throw new Error('Length-five state is outside the 80 endomorphism blocks');
    }
    addBig(image, block * count + monomial, coeff);
  }
  return {image, rows: 80 * count};
}

function projectLengthThree(states) {
  const image = new Map();
  const charts = 36; // C, C, B, B
  for (const [key, coeff] of states) {
    const state = unpack(key);
    if (state.u !== state.v || state.charts !== charts) continue;
    if (state.exp[0] !== -1 || state.exp[1] !== -1 || state.exp[2] !== 0 || state.exp[3] !== 0) continue;
    const row = DIAGONAL_OFFSET[state.u] + state.a * RANKS[state.u] + state.b;
    if (row < 0 || row >= 354) throw new Error('Length-three row escaped the diagonal blocks');
    addBig(image, row, coeff);
  }
  return {image, rows: 354};
}

function projectPositive(states) {
  const image = new Map();
  for (const [key, coeff] of states) {
    const state = unpack(key);
    if (state.v !== state.u + 1 || state.charts !== 40 || state.u < 0 || state.u > 2) continue;
    const monomial = indexBox(state.exp, [0, 0, 0, 0], [2, 2, 2, 2]);
    if (monomial === null) continue;
    const row = (POSITIVE_OFFSET[state.u] + state.a * RANKS[state.u] + state.b) * 16 + monomial;
    addBig(image, row, coeff);
  }
  return {image, rows: 3920};
}

function singleton(u, v, a, b, charts, exp, coeff) {
  const map = new Map();
  map.set(pack(u, v, a, b, charts, exp), coeff);
  return map;
}

function tensorInclusion(seed, h0Factors) {
  const terms = [seed];
  for (const factor of h0Factors) {
    const grown = [];
    for (const term of terms) {
      grown.push({charts: setChart(term.charts, factor, 1), coeff: term.coeff});
      grown.push({charts: setChart(term.charts, factor, 2), coeff: term.coeff});
    }
    terms.length = 0;
    terms.push(...grown);
  }
  const map = new Map();
  for (const term of terms) {
    addBig(map, pack(seed.u, seed.v, seed.a, seed.b, term.charts, seed.exp), term.coeff);
  }
  return map;
}

function sourceMonomials(weight) {
  const lo = [0, 1, 2, 3].map((i) => (i < weight ? -4 : -2));
  return monomials(lo, [-1, -1, -1, -1]);
}

function negativeInitial(column, src) {
  const unit = Math.floor(column / src.length);
  const monomial = src[column % src.length];
  return singleton(3, 0, Math.floor(unit / 2), unit % 2, 0, monomial, 1n);
}

class Q {
  constructor(n, d = 1n) {
    if (d < 0n) {
      n = -n;
      d = -d;
    }
    if (d === 0n) throw new Error('Zero denominator');
    const g = gcd(n, d);
    this.n = n / g;
    this.d = d / g;
  }
  add(other) { return new Q(this.n * other.d + other.n * this.d, this.d * other.d); }
  sub(other) { return new Q(this.n * other.d - other.n * this.d, this.d * other.d); }
  mul(other) { return new Q(this.n * other.n, this.d * other.d); }
  div(other) { return new Q(this.n * other.d, this.d * other.n); }
  neg() { return new Q(-this.n, this.d); }
  isZero() { return this.n === 0n; }
}

const Q0 = new Q(0n);

function columnsToRows(columns, nrows) {
  const rows = Array.from({length: nrows}, () => new Map());
  columns.forEach((column, index) => {
    for (const [row, value] of column) if (value !== 0n) rows[row].set(index, value);
  });
  return rows;
}

function unitEchelon(rows, ncols) {
  const matrix = rows.map((row) => new Map(row));
  let rank = 0;
  const pivotCols = [];
  let blockedAt = null;
  for (let column = 0; column < ncols; column++) {
    let pivot = -1;
    for (let row = rank; row < matrix.length; row++) {
      const value = matrix[row].get(column);
      if (value === 1n || value === -1n) {
        pivot = row;
        break;
      }
    }
    if (pivot < 0) {
      for (let row = rank; row < matrix.length; row++) {
        if (matrix[row].get(column)) {
          blockedAt = column;
          break;
        }
      }
      if (blockedAt !== null) break;
      continue;
    }
    if (pivot !== rank) [matrix[pivot], matrix[rank]] = [matrix[rank], matrix[pivot]];
    if (matrix[rank].get(column) === -1n) {
      for (const [index, value] of matrix[rank]) matrix[rank].set(index, -value);
    }
    const pivotRow = matrix[rank];
    for (let row = rank + 1; row < matrix.length; row++) {
      const multiplier = matrix[row].get(column);
      if (!multiplier) continue;
      const current = matrix[row];
      for (const [index, value] of pivotRow) {
        const next = (current.get(index) || 0n) - multiplier * value;
        if (next === 0n) current.delete(index);
        else current.set(index, next);
      }
    }
    pivotCols.push(column);
    rank++;
  }
  if (blockedAt === null) {
    for (let row = rank; row < matrix.length; row++) {
      if (matrix[row].size) throw new Error('Unit elimination left a nonzero residual row');
    }
  }
  return {matrix, rank, pivotCols, blockedAt};
}

function rationalTail(intRows, ncols) {
  const rows = intRows.map((row) => {
    const out = new Map();
    for (const [column, value] of row) if (value !== 0n) out.set(column, new Q(value));
    return out;
  });
  let rank = 0;
  const pivotCols = [];
  for (let column = 0; column < ncols; column++) {
    let pivot = -1;
    for (let row = rank; row < rows.length; row++) {
      const value = rows[row].get(column);
      if (value && !value.isZero()) {
        pivot = row;
        break;
      }
    }
    if (pivot < 0) continue;
    if (pivot !== rank) [rows[pivot], rows[rank]] = [rows[rank], rows[pivot]];
    const pivotRow = rows[rank];
    const pivotValue = pivotRow.get(column);
    for (let row = rank + 1; row < rows.length; row++) {
      const multiplier = rows[row].get(column);
      if (!multiplier || multiplier.isZero()) continue;
      const factor = multiplier.div(pivotValue);
      const current = rows[row];
      const columns = new Set(current.keys());
      for (const index of pivotRow.keys()) columns.add(index);
      for (const index of columns) {
        const next = (current.get(index) || Q0).sub(factor.mul(pivotRow.get(index) || Q0));
        if (next.isZero()) current.delete(index);
        else current.set(index, next);
      }
    }
    pivotCols.push(column);
    rank++;
  }
  for (let row = rank; row < rows.length; row++) {
    if (rows[row].size) throw new Error('Rational tail left a nonzero residual row');
  }
  return {rows, rank, pivotCols};
}

function kernelFromEchelon(unit, tail, ncols) {
  const pivotCols = tail ? unit.pivotCols.concat(tail.pivotCols) : unit.pivotCols.slice();
  const rank = pivotCols.length;
  const occupied = new Set(pivotCols);
  const free = [];
  for (let column = 0; column < ncols; column++) if (!occupied.has(column)) free.push(column);
  const rows = [];
  for (let i = 0; i < unit.rank; i++) {
    const row = new Map();
    for (const [column, value] of unit.matrix[i]) row.set(column, new Q(value));
    rows.push(row);
  }
  if (tail) {
    for (let i = 0; i < tail.rank; i++) rows.push(tail.rows[i]);
  }
  const kernel = [];
  for (const variable of free) {
    const coeff = Array.from({length: ncols}, () => Q0);
    coeff[variable] = new Q(1n);
    for (let i = rank - 1; i >= 0; i--) {
      const pivot = pivotCols[i];
      const row = rows[i];
      let sum = Q0;
      for (const [column, value] of row) {
        if (column !== pivot) sum = sum.add(value.mul(coeff[column]));
      }
      coeff[pivot] = sum.neg().div(row.get(pivot));
    }
    let denominator = 1n;
    for (const value of coeff) denominator = lcm(denominator, value.d);
    kernel.push(coeff.map((value) => value.n * (denominator / value.d)));
  }
  return {rank, kernel, pivotCols};
}

function lcm(a, b) {
  if (a === 0n || b === 0n) return 0n;
  return a / gcd(a, b) * b;
}

function assertKernel(columns, kernel) {
  for (const vector of kernel) {
    if (vector.length !== columns.length) {
      throw new Error(`Kernel vector has length ${vector.length}, expected ${columns.length}`);
    }
    const image = new Map();
    for (let column = 0; column < columns.length; column++) {
      if (vector[column] === 0n) continue;
      for (const [row, value] of columns[column]) {
        const next = (image.get(row) || 0n) + vector[column] * value;
        if (next === 0n) image.delete(row);
        else image.set(row, next);
      }
    }
    if (image.size) throw new Error('Kernel vector failed on the original matrix');
  }
}

function analyzeColumns(columns, nrows, wantKernel) {
  const rows = columnsToRows(columns, nrows);
  const unit = unitEchelon(rows, columns.length);
  let tail = null;
  if (unit.blockedAt !== null) {
    tail = rationalTail(unit.matrix.slice(unit.rank), columns.length);
  }
  const solved = kernelFromEchelon(unit, tail, columns.length);
  if (wantKernel) assertKernel(columns, solved.kernel);
  let nnz = 0;
  let maxAbs = 0n;
  for (const column of columns) {
    nnz += column.size;
    for (const value of column.values()) {
      const abs = value < 0n ? -value : value;
      if (abs > maxAbs) maxAbs = abs;
    }
  }
  return {
    rows: nrows,
    columns: columns.length,
    rank: solved.rank,
    nullity: columns.length - solved.rank,
    kernel: wantKernel ? solved.kernel : null,
    nonzeros: nnz,
    maxAbs: maxAbs.toString(),
    unitRank: unit.rank,
    usedRationalTail: unit.blockedAt !== null
  };
}

function combineImages(images, vectors) {
  return vectors.map((vector) => {
    const out = new Map();
    for (let i = 0; i < vector.length; i++) {
      if (vector[i] === 0n) continue;
      for (const [row, value] of images[i]) {
        const next = (out.get(row) || 0n) + vector[i] * value;
        if (next === 0n) out.delete(row);
        else out.set(row, next);
      }
    }
    return out;
  });
}

function composeVectors(outer, inner) {
  const width = inner[0].length;
  return outer.map((vector) => {
    const acc = Array(width).fill(0n);
    for (let i = 0; i < vector.length; i++) {
      if (vector[i] === 0n) continue;
      const basis = inner[i];
      for (let j = 0; j < width; j++) if (basis[j] !== 0n) acc[j] += vector[i] * basis[j];
    }
    return acc;
  });
}

function hashColumns(columns, nrows) {
  const hash = crypto.createHash('sha256');
  hash.update(`${nrows}x${columns.length}\n`);
  for (let column = 0; column < columns.length; column++) {
    const entries = [...columns[column].entries()].sort((left, right) => left[0] - right[0]);
    hash.update(String(column));
    for (const [row, value] of entries) hash.update(`|${row}:${value.toString()}`);
    hash.update('\n');
  }
  return hash.digest('hex');
}

function testP1Contraction() {
  const degree = -3;
  function homotopy(cochain) {
    const finite = new Map();
    const infinity = new Map();
    for (const [exponent, coeff] of cochain) {
      if (exponent >= 0) finite.set(exponent, -coeff);
      else if (exponent <= degree) infinity.set(exponent, coeff);
    }
    return {finite, infinity};
  }
  function differential(charts) {
    const out = new Map();
    for (const [exponent, coeff] of charts.infinity) out.set(exponent, coeff);
    for (const [exponent, coeff] of charts.finite) out.set(exponent, (out.get(exponent) || 0) - coeff);
    for (const [exponent, coeff] of out) if (coeff === 0) out.delete(exponent);
    return out;
  }
  for (let trial = 0; trial < 30; trial++) {
    const cochain = new Map();
    for (let exponent = -8; exponent <= 6; exponent++) {
      if ((trial * 5 + exponent * 3) % 4 === 0) cochain.set(exponent, ((trial + 3) * exponent) % 7 - 3);
    }
    const applied = differential(homotopy(cochain));
    for (let exponent = -8; exponent <= 6; exponent++) {
      const harmonic = exponent > degree && exponent < 0;
      const expected = harmonic ? 0 : (cochain.get(exponent) || 0);
      if ((applied.get(exponent) || 0) !== expected) {
        throw new Error('Single-factor homotopy failed dh = id − ip');
      }
    }
  }
}

function testRationalRank() {
  const columns = [
    new Map([[0, 2n], [1, 4n]]),
    new Map([[0, 1n], [1, 2n]]),
    new Map([[0, 3n]])
  ];
  const result = analyzeColumns(columns, 2, true);
  if (result.rank !== 2 || result.nullity !== 1) {
    throw new Error(`Expected rank 2, nullity 1, got ${result.rank}, ${result.nullity}`);
  }
}

function buildWeight(weight, complex, families) {
  const src = sourceMonomials(weight);
  const ncols = 10 * src.length;
  const window1 = exponentWindow(-2, weight);
  const window5 = exponentWindow(2, weight);
  const window3 = exponentWindow(0, 2);
  const d1 = [];
  const len5 = [];
  const len3 = weight === 2 ? [] : null;
  for (let column = 0; column < ncols; column++) {
    const initial = negativeInitial(column, src);
    const once = applyDelta(initial, -3, complex.forward, complex.incoming, families, 0, window1);
    d1.push(projectLengthOne(once, weight).image);
    if (weight === 2) {
      const thrice = transfer(initial, 3, -3, weight, window3, complex.forward, complex.incoming, families);
      len3.push(projectLengthThree(thrice).image);
    }
    const fifth = transfer(initial, 5, -3, weight, window5, complex.forward, complex.incoming, families);
    len5.push(projectLengthFive(fifth, weight).image);
  }
  const projected = projectLengthOne(new Map(), weight);
  const lengthFiveRows = projectLengthFive(new Map(), weight).rows;
  return {src, d1, len5, len3, d1Rows: projected.rows, len5Rows: lengthFiveRows};
}

function diagonalColumns(complex, families) {
  const columns = [];
  const window = exponentWindow(2, 1);
  for (let u = 0; u < 4; u++) {
    for (let a = 0; a < RANKS[u]; a++) {
      for (let b = 0; b < RANKS[u]; b++) {
        const seed = {
          u, v: u, a, b, charts: 0, exp: [-1, 0, 0, 0], coeff: 1n
        };
        const initial = tensorInclusion(seed, [1, 2, 3]);
        const image = transfer(initial, 2, 0, 1, window, complex.forward, complex.incoming, families);
        columns.push(projectLengthFive(image, 1).image);
      }
    }
  }
  if (columns.length !== 354) throw new Error('Weight-one diagonal space is not 354-dimensional');
  return columns;
}

function positiveAndBoundary(complex, families) {
  const monomial = monomials([0, 0, 0, 0], [1, 1, 1, 1]);
  const positive = [];
  const windowOut = exponentWindow(2, 0);
  const windowBoundary = exponentWindow(1, 0);
  for (let u = 0; u < 3; u++) {
    for (let a = 0; a < RANKS[u + 1]; a++) {
      for (let b = 0; b < RANKS[u]; b++) {
        for (let index = 0; index < monomial.length; index++) {
          const seed = {u, v: u + 1, a, b, charts: 0, exp: monomial[index], coeff: 1n};
          const initial = tensorInclusion(seed, [0, 1, 2, 3]);
          const image = applyDelta(initial, 1, complex.forward, complex.incoming, families, 0, windowOut);
          positive.push(projectLengthFive(image, 0).image);
        }
      }
    }
  }
  if (positive.length !== 3920) throw new Error('Weight-zero internal-degree-one space is not 3920-dimensional');

  const boundary = [];
  for (let u = 0; u < 4; u++) {
    for (let a = 0; a < RANKS[u]; a++) {
      for (let b = 0; b < RANKS[u]; b++) {
        const seed = {u, v: u, a, b, charts: 0, exp: [0, 0, 0, 0], coeff: 1n};
        const initial = tensorInclusion(seed, [0, 1, 2, 3]);
        const image = applyDelta(initial, 0, complex.forward, complex.incoming, families, 0, windowBoundary);
        boundary.push(projectPositive(image).image);
      }
    }
  }
  if (boundary.length !== 354) throw new Error('Degree-zero space is not 354-dimensional');

  for (let column = 0; column < boundary.length; column++) {
    const image = boundary[column];
    const composed = new Map();
    for (const [row, value] of image) {
      for (const [target, coeff] of positive[row]) {
        const next = (composed.get(target) || 0n) + value * coeff;
        if (next === 0n) composed.delete(target);
        else composed.set(target, next);
      }
    }
    if (composed.size) throw new Error(`Degree-zero generator ${column} is not a cycle`);
  }
  return {positive, boundary};
}

function computeExt1(options = {}) {
  testP1Contraction();
  testRationalRank();
  const space = finiteSpaceDimensions();
  if (space.all !== 80384 || JSON.stringify(space.byTotal) !== JSON.stringify([354, 18296, 43084, 18296, 354])) {
    throw new Error(`Finite-space dimensions ${space.byTotal} total ${space.all}`);
  }
  const complex = buildLineComplex();
  const families = squarefreeFamilies();
  const selected = options.weights || [0, 1, 2, 3, 4];
  const positiveBundle = selected.includes(0) ? positiveAndBoundary(complex, families) : null;
  const diagonal = selected.includes(1) ? diagonalColumns(complex, families) : null;
  const byWeight = [];
  for (const weight of selected) {
    const started = Date.now();
    const built = buildWeight(weight, complex, families);
    const initial = analyzeColumns(built.d1, built.d1Rows, true);
    let kernel = initial.kernel;
    let lengthThree = null;
    if (weight === 2) {
      const reduced = combineImages(built.len3, kernel);
      lengthThree = analyzeColumns(reduced, 354, true);
      kernel = composeVectors(lengthThree.kernel, initial.kernel);
    }
    let columns = combineImages(built.len5, kernel);
    if (weight === 0) columns = columns.concat(positiveBundle.positive);
    if (weight === 1) columns = columns.concat(diagonal);
    const remaining = analyzeColumns(columns, built.len5Rows, true);
    let boundaryRank = 0;
    let boundary = null;
    if (weight === 0) {
      boundary = analyzeColumns(positiveBundle.boundary, 3920, true);
      boundaryRank = boundary.rank;
    }
    const h1 = columns.length - remaining.rank - boundaryRank;
    byWeight.push({
      weight,
      h1,
      d1: {rows: initial.rows, columns: initial.columns, rank: initial.rank, nonzeros: initial.nonzeros, maxAbs: initial.maxAbs},
      d3: lengthThree && {
        rows: lengthThree.rows,
        columns: lengthThree.columns,
        rank: lengthThree.rank,
        nonzeros: lengthThree.nonzeros,
        maxAbs: lengthThree.maxAbs
      },
      remaining: {
        rows: remaining.rows,
        columns: remaining.columns,
        rank: remaining.rank,
        nonzeros: remaining.nonzeros,
        maxAbs: remaining.maxAbs,
        unitRank: remaining.unitRank,
        usedRationalTail: remaining.usedRationalTail
      },
      boundaryRank,
      milliseconds: Date.now() - started,
      matrices: {
        d1: built.d1,
        len3: built.len3,
        len5: built.len5,
        positive: weight === 0 ? positiveBundle.positive : null,
        boundary: weight === 0 ? positiveBundle.boundary : null,
        diagonal: weight === 1 ? diagonal : null
      }
    });
    console.error(`weight ${weight}: h1=${h1} d1=${initial.rank} remaining=${remaining.rank} boundary=${boundaryRank} ${Date.now() - started}ms`);
  }
  return {complex, space, byWeight};
}

function publicSummary(result) {
  const byWeight = result.byWeight.map((entry) => ({
    weight: entry.weight,
    h1: entry.h1,
    d1: entry.d1,
    d3: entry.d3,
    remaining: entry.remaining,
    boundaryRank: entry.boundaryRank,
    milliseconds: entry.milliseconds,
    hashes: {
      d1: hashColumns(entry.matrices.d1, entry.d1.rows),
      len5: hashColumns(entry.matrices.len5, entry.remaining.rows),
      len3: entry.matrices.len3 ? hashColumns(entry.matrices.len3, 354) : null,
      positive: entry.matrices.positive ? hashColumns(entry.matrices.positive, entry.remaining.rows) : null,
      boundary: entry.matrices.boundary ? hashColumns(entry.matrices.boundary, 3920) : null,
      diagonal: entry.matrices.diagonal ? hashColumns(entry.matrices.diagonal, entry.remaining.rows) : null
    }
  }));
  const h1 = byWeight.map((entry) => entry.h1);
  const total = h1.reduce((sum, value, weight) => sum + MULTIPLICITIES[weight] * value, 0);
  return {
    finiteSpace: result.space,
    h1ByWeight: h1,
    h1Total: total,
    byWeight
  };
}

if (require.main === module) {
  const weights = process.argv.includes('--weights')
    ? process.argv[process.argv.indexOf('--weights') + 1].split(',').map(Number)
    : [0, 1, 2, 3, 4];
  const summary = publicSummary(computeExt1({weights}));
  console.log(JSON.stringify(summary, null, 2));
  if (!process.argv.includes('--weights') && (JSON.stringify(summary.h1ByWeight) !== JSON.stringify([79, 2, 0, 0, 0]) || summary.h1Total !== 87)) {
    throw new Error(`Ext^1 count ${summary.h1ByWeight} total ${summary.h1Total}`);
  }
}

module.exports = {
  RANKS,
  MULTIPLICITIES,
  POW3,
  buildLineComplex,
  computeExt1,
  publicSummary,
  hashColumns,
  finiteSpaceDimensions,
  sourceMonomials,
  exponentWindow,
  pack,
  projectLengthOne,
  projectLengthFive,
  projectLengthThree,
  projectPositive
};
