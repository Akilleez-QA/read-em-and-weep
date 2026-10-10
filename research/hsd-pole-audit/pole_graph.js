"use strict";
/**
 * Independent abstract pole graph for the pinned scalar.
 *
 * Channel layout, 18 entries:
 *   primary carrier j: (v_j, F_j) at 2j, 2j+1
 *   auxiliary (*, owner 5): (v0, v1, v3, v4) at 10..13
 *   legal lines: four coordinates at 14..17
 * Constants stay exact rationals. Nonconstant addition takes coordinate
 * maxima and multiplication adds orders. No rational cancellation is used.
 *
 * This file does not load or call checks/compute_pole_bounds.js.
 * Modes:
 *   published  source nu encoding and lineJet replacement used by PR #40
 *   qzero      same, but the equal-mask overlap ratio q is the zero jet
 *   fulljet    nu is the classical product of the univariate line jets
 */
const fs = require("fs");
const path = require("path");

const ROOT = path.resolve(
  __dirname,
  "../hm/current-scalar-geometric-dependencies"
);
const MODEL = require(path.join(ROOT, "data/model.json"));
const SEEDS = require(path.join(ROOT, "data/divisor-seeds.json"));
const MODE = process.argv[2] || "published";
if (!["published", "qzero", "fulljet"].includes(MODE)) {
  throw new Error("mode must be published, qzero, or fulljet");
}

const MASKS = [0, 1, 2, 4, 8, 3, 5, 9, 6, 10, 12];
const nodes = [];
const cache = new Map();
function intern(value) {
  const key = JSON.stringify(value);
  if (cache.has(key)) return cache.get(key);
  const id = nodes.length;
  nodes.push(value);
  cache.set(key, id);
  return id;
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
function exact(numerator, denominator = 1n) {
  if (typeof numerator === "string") return bound(Array(18).fill(0));
  if (!numerator) denominator = 1n;
  if (denominator < 0n) {
    numerator = -numerator;
    denominator = -denominator;
  }
  const g = gcd(numerator, denominator);
  return intern(["const", String(numerator / g), String(denominator / g)]);
}
const ZERO = exact(0n);
const ONE = exact(1n);
const MINUS = exact(-1n);
const isConst = (id) => nodes[id][0] === "const";
const bound = (vector) => intern(["bound", ...vector]);
function ordersOf(id) {
  return isConst(id) ? Array(18).fill(0) : nodes[id].slice(1);
}
function add(a, b) {
  if (a === ZERO) return b;
  if (b === ZERO) return a;
  if (isConst(a) && isConst(b)) {
    const A = nodes[a];
    const B = nodes[b];
    return exact(
      BigInt(A[1]) * BigInt(B[2]) + BigInt(B[1]) * BigInt(A[2]),
      BigInt(A[2]) * BigInt(B[2])
    );
  }
  const p = ordersOf(a);
  const q = ordersOf(b);
  return bound(p.map((value, i) => Math.max(value, q[i])));
}
function mul(a, b) {
  if (a === ZERO || b === ZERO) return ZERO;
  if (a === ONE) return b;
  if (b === ONE) return a;
  if (isConst(a) && isConst(b)) {
    const A = nodes[a];
    const B = nodes[b];
    return exact(BigInt(A[1]) * BigInt(B[1]), BigInt(A[2]) * BigInt(B[2]));
  }
  const p = ordersOf(a);
  const q = ordersOf(b);
  return bound(p.map((value, i) => value + q[i]));
}
const neg = (a) => mul(MINUS, a);
const sub = (a, b) => add(a, neg(b));
function div(a, b) {
  if (a === ZERO) return ZERO;
  if (!isConst(b) || nodes[b][1] === "0") throw new Error("Uncertified inverse");
  return mul(a, exact(BigInt(nodes[b][2]), BigInt(nodes[b][1])));
}
const zeros = (rows, cols, fill) =>
  Array.from({ length: rows }, () => Array(cols).fill(fill));
const transpose = (A) => A[0].map((_, j) => A.map((row) => row[j]));
function matmul(A, B, addOp, mulOp, zero) {
  return A.map((row) =>
    B[0].map((_, j) =>
      row.reduce((sum, value, k) => addOp(sum, mulOp(value, B[k][j])), zero)
    )
  );
}
const matAdd = (A, B) => A.map((row, i) => row.map((value, j) => add(value, B[i][j])));
const matSub = (A, B) => A.map((row, i) => row.map((value, j) => sub(value, B[i][j])));
const matScale = (A, s) => A.map((row) => row.map((value) => mul(value, s)));
const matTrace = (A) => A.reduce((sum, row, i) => add(sum, row[i]), ZERO);

const jetZero = () => Array(16).fill(ZERO);
const jetOne = () => {
  const jet = jetZero();
  jet[0] = ONE;
  return jet;
};
function jetAdd(a, b) {
  return a.map((value, i) => add(value, b[i]));
}
function jetMul(a, b) {
  const out = jetZero();
  for (const mask of MASKS) {
    for (let subset = mask; ; subset = (subset - 1) & mask) {
      out[mask] = add(out[mask], mul(a[subset], b[mask ^ subset]));
      if (!subset) break;
    }
  }
  return out;
}
function jetInv(a) {
  const out = jetZero();
  out[0] = div(ONE, a[0]);
  for (const mask of MASKS.slice(1)) {
    let sum = ZERO;
    for (let subset = mask; subset; subset = (subset - 1) & mask) {
      sum = add(sum, mul(a[subset], out[mask ^ subset]));
    }
    out[mask] = neg(div(sum, a[0]));
  }
  return out;
}
const jetScale = (a, s) => a.map((value) => mul(value, s));
const jetNeg = (a) => a.map(neg);
const jetSub = (a, b) => jetAdd(a, jetNeg(b));
function jetDer(a, coordinate) {
  const bit = 1 << coordinate;
  return a.map((_, mask) => ((mask & bit) ? ZERO : a[mask | bit]));
}
function jetMat(rows, cols) {
  return Array.from({ length: rows }, () => Array.from({ length: cols }, jetZero));
}
const jetTranspose = (A) => A[0].map((_, j) => A.map((row) => row[j]));
const jetMatAdd = (A, B) =>
  A.map((row, i) => row.map((value, j) => jetAdd(value, B[i][j])));
const jetMatNeg = (A) => A.map((row) => row.map(jetNeg));
const jetMatMul = (A, B) =>
  A.map((row) =>
    B[0].map((_, j) =>
      row.reduce((sum, value, k) => jetAdd(sum, jetMul(value, B[k][j])), jetZero())
    )
  );
const jetMatScale = (A, s) => A.map((row) => row.map((value) => jetScale(value, s)));
const jetMatDer = (A, coordinate) =>
  A.map((row) => row.map((value) => jetDer(value, coordinate)));
const values = (A) => A.map((row) => row.map((jet) => jet[0]));
const jetTrace = (A) => A.reduce((sum, row, i) => jetAdd(sum, row[i]), jetZero());
const horizontal = (...blocks) =>
  blocks[0].map((_, row) => blocks.flatMap((matrix) => matrix[row]));
const vertical = (...blocks) => blocks.flat();

function popcount(mask) {
  return mask.toString(2).replaceAll("0", "").length;
}
function poleJet(carrier, line = [0, 0, 0, 0], differentiate = true, owner = 0) {
  const jet = [];
  for (let mask = 0; mask < 16; mask++) {
    if (!MASKS.includes(mask)) {
      jet.push(ZERO);
      continue;
    }
    const orders = Array(14).fill(0);
    const exponents = Array.isArray(carrier) ? carrier : [carrier, 0];
    for (let i = 0; i < exponents.length; i++) {
      const slot = (owner < 5 ? 2 * owner : 10) + i;
      orders[slot] =
        exponents[i] + (differentiate && exponents[i] > 0 ? popcount(mask) : 0);
    }
    jet.push(bound([...orders, ...line]));
  }
  return jet;
}
function seedMatrix(matrix, costs, owner, polynomial) {
  return matrix.map((row, i) =>
    row.map((polynomialTerms, j) => {
      if (!polynomialTerms.length) return jetZero();
      if (polynomial) return poleJet(0, [0, 0, 0, 0], false, owner);
      const exponents = costs[i][j];
      return poleJet(exponents, [0, 0, 0, 0], exponents.some((value) => value > 0), owner);
    })
  );
}
function joinScalars(ids) {
  if (ids.every((id) => id === ids[0])) return ids[0];
  return bound(
    ids.reduce(
      (acc, id) => acc.map((value, j) => Math.max(value, ordersOf(id)[j])),
      Array(18).fill(0)
    )
  );
}
function deepJoin(valuesToJoin) {
  return typeof valuesToJoin[0] === "number"
    ? joinScalars(valuesToJoin)
    : valuesToJoin[0].map((_, j) => deepJoin(valuesToJoin.map((value) => value[j])));
}
function lineJet(coordinate, order = 1) {
  const jet = jetZero();
  for (const mask of [0, 1 << coordinate]) {
    const line = [0, 0, 0, 0];
    line[coordinate] = order + popcount(mask);
    jet[mask] = bound([...Array(14).fill(0), ...line]);
  }
  return jet;
}
function buildCharts(ownerIds, join) {
  const gamma = seedMatrix(MODEL.gamma, null, 0, true);
  const delta = seedMatrix(MODEL.delta, null, 0, true);
  const ev = seedMatrix(MODEL.ev, null, 0, true);
  const charts = ownerIds.map((owner) => {
    const chart = MODEL.charts[owner];
    const seed = SEEDS[owner];
    const I = seedMatrix(chart.I, seed.I, owner, false);
    const P = seedMatrix(chart.P, seed.P, owner, false);
    const H0 = seedMatrix(chart.H0, seed.H0, owner, false);
    const H1 = seedMatrix(chart.H1, seed.H1, owner, false);
    const pivot = chart.pivot;
    const W = jetMat(10, 8);
    const eta = jetMat(10, 2);
    const L = jetMat(8, 10);
    for (let half = 0; half < 2; half++) {
      eta[half * 5 + pivot][half] = poleJet(1, undefined, true, owner);
      for (let step = 1; step < 5; step++) {
        const other = (pivot + step) % 5;
        const column = half * 4 + step - 1;
        W[half * 5 + other][column] = jetOne();
        W[half * 5 + pivot][column] = poleJet(1, undefined, true, owner);
        L[column][half * 5 + other] = jetOne();
      }
    }
    return {
      I,
      P,
      H0,
      H1,
      eta,
      U0: horizontal(gamma, I, jetMatMul(H1, W)),
      Q0: vertical(H0, P, jetMatMul(L, delta)),
      U1: horizontal(W, eta),
      Q1: vertical(L, ev),
    };
  });
  const joined = Object.fromEntries(
    Object.keys(charts[0]).map((key) => [key, deepJoin(charts.map((chart) => chart[key]))])
  );
  return {
    charts: join ? ownerIds.map(() => joined) : charts,
    gamma,
    delta,
    ev,
  };
}

function crossResidual(data, i, j, k) {
  const half = exact(1n, 2n);
  const pair = (F, G, a, b) =>
    matScale(
      matSub(
        matmul(values(jetMatDer(F, a)), values(jetMatDer(G, b)), add, mul, ZERO),
        matmul(values(jetMatDer(F, b)), values(jetMatDer(G, a)), add, mul, ZERO)
      ),
      half
    );
  let residual = matAdd(
    matmul(values(data.u12[j][k]), values(data.u34[i][j]), add, mul, ZERO),
    matmul(values(data.u34[j][k]), values(data.u12[i][j]), add, mul, ZERO)
  );
  for (const [F, G, a, b] of [
    [data.u34[j][k], data.g[i][j], 0, 1],
    [data.u12[j][k], data.g[i][j], 2, 3],
    [data.g[j][k], data.u34[i][j], 0, 1],
    [data.g[j][k], data.u12[i][j], 2, 3],
  ]) {
    residual = matAdd(residual, pair(F, G, a, b));
  }
  const mixed = (G, a, b) => G.map((row) => row.map((jet) => jet[(1 << a) | (1 << b)]));
  const cross = matAdd(
    matSub(
      matSub(
        matmul(mixed(data.g[j][k], 0, 2), mixed(data.g[i][j], 1, 3), add, mul, ZERO),
        matmul(mixed(data.g[j][k], 0, 3), mixed(data.g[i][j], 1, 2), add, mul, ZERO)
      ),
      matmul(mixed(data.g[j][k], 1, 2), mixed(data.g[i][j], 0, 3), add, mul, ZERO)
    ),
    matmul(mixed(data.g[j][k], 1, 3), mixed(data.g[i][j], 0, 2), add, mul, ZERO)
  );
  return matAdd(residual, matScale(cross, exact(1n, 4n)));
}

function globalBuild(vertices) {
  const owners = [0, 1, 2, 3, 4];
  const base = buildCharts(owners, true);
  const symbols = ["x1", "x2", "x3", "x4"].map((name, i) => {
    const jet = jetZero();
    jet[0] = exact(name);
    jet[1 << i] = ONE;
    return jet;
  });
  const frame = symbols.map((_, coordinate) => lineJet(coordinate));
  const logarithmic = symbols.map((_, coordinate) => lineJet(coordinate));
  const charts = vertices.map(([owner, mask]) => {
    const chart = base.charts[owners.indexOf(owner)];
    const nu = jetZero();
    if (MODE === "fulljet") {
      let product = jetOne();
      for (let coordinate = 0; coordinate < 4; coordinate++) {
        if (mask & (1 << coordinate)) product = jetMul(product, frame[coordinate]);
      }
      for (let slot = 0; slot < 16; slot++) nu[slot] = product[slot];
    } else {
      for (const subset of MASKS) {
        let term = ONE;
        for (let coordinate = 0; coordinate < 4; coordinate++) {
          if (subset & (1 << coordinate)) {
            term = mul(term, mask & (1 << coordinate) ? frame[coordinate][0] : ZERO);
          }
        }
        nu[subset] = term;
      }
    }
    const nuSquared = jetMul(nu, nu);
    const nuInverseSquared = jetInv(nuSquared);
    const weight0 = [
      ...Array(5).fill(nuInverseSquared),
      jetOne(),
      nuInverseSquared,
      ...Array(8).fill(nuSquared),
    ];
    const weight1 = [...Array(8).fill(jetOne()), nuSquared, nuSquared];
    const U0 = chart.U0.map((row) => row.map((value, column) => jetMul(value, weight0[column])));
    const Q0 = chart.Q0.map((row, i) => row.map((value) => jetMul(value, jetInv(weight0[i]))));
    const U1 = chart.U1.map((row) => row.map((value, column) => jetMul(value, weight1[column])));
    const Q1 = chart.Q1.map((row, i) => row.map((value) => jetMul(value, jetInv(weight1[i]))));
    const blocks = [];
    for (let coordinate = 0; coordinate < 4; coordinate++) {
      const gamma = mask & (1 << coordinate) ? logarithmic[coordinate] : jetZero();
      const curvature0 = jetMatNeg(jetMatMul(jetMatDer(U0, coordinate), Q0));
      const curvature1 = jetMatNeg(jetMatMul(jetMatDer(U1, coordinate), Q1));
      const out = [];
      for (const [dimension, coefficient, sign, raw] of [
        [5, -1, -1, null],
        [15, 1, 1, curvature0],
        [10, 3, -1, curvature1],
        [2, 5, 1, null],
      ]) {
        const block = raw || jetMat(dimension, dimension);
        for (let row = 0; row < dimension; row++) {
          block[row][row] = jetSub(block[row][row], jetScale(gamma, exact(BigInt(coefficient))));
        }
        out.push({ B: block, k: coefficient, sign });
      }
      blocks.push(out);
    }
    return { ...chart, mask, nu, blocks };
  });
  const n = charts.length;
  const g = Array.from({ length: n }, (_, i) =>
    Array.from({ length: n }, (_, j) => {
      const core = jetMatMul(charts[i].P, charts[j].I);
      const left = [jetInv(charts[i].nu), charts[i].nu];
      const right = [charts[j].nu, jetInv(charts[j].nu)];
      return jetTranspose(
        core.map((row, a) => row.map((value, b) => jetMul(jetMul(left[a], value), right[b])))
      );
    })
  );
  const overlap = MODE === "qzero" ? () => jetZero() : (_i, _j, coordinate) => lineJet(coordinate);
  function first(a, b) {
    return Array.from({ length: n }, (_, i) =>
      Array.from({ length: n }, (_, j) => {
        let sum = jetZero();
        const ta = jetScale(overlap(i, j, a), exact(1n, 2n));
        const tb = jetScale(overlap(i, j, b), exact(1n, 2n));
        for (let block = 0; block < 4; block++) {
          const Ai = charts[i].blocks[a][block];
          const Bi = charts[i].blocks[b][block];
          const Aj = charts[j].blocks[a][block];
          const Bj = charts[j].blocks[b][block];
          const wedge = jetSub(
            jetTrace(jetMatMul(Ai.B, Bj.B)),
            jetTrace(jetMatMul(Bi.B, Aj.B))
          );
          const linear = jetScale(
            jetSub(
              jetMul(ta, jetAdd(jetTrace(Bi.B), jetTrace(Bj.B))),
              jetMul(tb, jetAdd(jetTrace(Ai.B), jetTrace(Aj.B)))
            ),
            exact(BigInt(Ai.k))
          );
          sum = jetAdd(sum, jetScale(jetAdd(wedge, linear), exact(BigInt(Ai.sign))));
        }
        const scalar = jetSub(
          jetScale(sum, exact(1n, 4n)),
          jetScale(jetMul(overlap(i, j, a), overlap(i, j, b)), exact(15n, 8n))
        );
        const G = g[i][j];
        const inverse = [
          [G[1][1], jetNeg(G[0][1])],
          [jetNeg(G[1][0]), G[0][0]],
        ];
        const K = jetMatScale(
          jetMatSub(
            jetMatMul(jetMatDer(inverse, a), jetMatDer(G, b)),
            jetMatMul(jetMatDer(inverse, b), jetMatDer(G, a))
          ),
          exact(1n, 2n)
        );
        const Z = jetMatScale(K, exact(-1n, 2n));
        Z[0][0] = jetAdd(Z[0][0], scalar);
        Z[1][1] = jetAdd(Z[1][1], scalar);
        return jetMatMul(G, Z);
      })
    );
  }
  function jetMatSub(A, B) {
    return A.map((row, i) => row.map((value, j) => jetSub(value, B[i][j])));
  }
  const u12 = first(0, 1);
  const u34 = first(2, 3);
  const coefficient = (i, j, k, a, b) =>
    mul(exact(15n, 4n), mul(overlap(i, j, a)[0], overlap(j, k, b)[0]));
  return { g, u12, u34, charts, coefficient, gamma: base.gamma, delta: base.delta, ev: base.ev };
}

function globalCross(data, i, j, k) {
  const left = data.coefficient(i, j, k, 0, 1);
  const right = data.coefficient(i, j, k, 2, 3);
  let out = crossResidual(data, i, j, k);
  out = matSub(out, matScale(values(data.u34[i][k]), left));
  out = matSub(out, matScale(values(data.u12[i][k]), right));
  out = matSub(out, matScale(values(data.g[i][k]), mul(left, right)));
  return out;
}
function collect(value, acc = Array(18).fill(0)) {
  if (typeof value === "number") {
    ordersOf(value).forEach((order, j) => {
      acc[j] = Math.max(acc[j], order);
    });
  } else if (Array.isArray(value)) {
    for (const entry of value) collect(entry, acc);
  } else {
    for (const entry of Object.values(value)) collect(entry, acc);
  }
  return acc;
}
function compress(vector) {
  return [
    ...Array.from({ length: 5 }, (_, j) => Math.max(vector[2 * j], vector[2 * j + 1])),
    Math.max(...vector.slice(10, 14)),
    ...vector.slice(14),
  ];
}

let built;
try {
  built = globalBuild([
    [0, 15],
    [0, 15],
    [0, 15],
  ]);
} catch (error) {
  if (error.message !== "Uncertified inverse") throw error;
  process.stdout.write(
    JSON.stringify({
      mode: MODE,
      status: "uncertified-inverse",
      abstractNodes: nodes.length,
      reason:
        "Classical product of line jets has a nonconstant value, so its reciprocal is rejected. The published encoding keeps that value equal to 1.",
    })
  );
  process.exit(0);
}
const transition = values(built.g[0][2]);
const inverseTransition = [
  [transition[1][1], neg(transition[0][1])],
  [neg(transition[1][0]), transition[0][0]],
];
const included = matmul(
  matmul(
    values(built.charts[0].I),
    transpose(matmul(inverseTransition, globalCross(built, 0, 1, 2), add, mul, ZERO)),
    add,
    mul,
    ZERO
  ),
  values(built.charts[0].P),
  add,
  mul,
  ZERO
);
const tail = compress(collect(included));
const separated = buildCharts([0, 1, 2, 3, 4, 5], false);
const gamma = values(separated.gamma);
const delta = values(separated.delta);
const identity15 = zeros(15, 15, ZERO);
for (let i = 0; i < 15; i++) identity15[i][i] = ONE;
const charts = separated.charts.map((chart) => ({
  ...Object.fromEntries(["I", "P", "H0", "H1", "eta"].map((key) => [key, values(chart[key])])),
  E: matSub(matSub(identity15, matmul(gamma, values(chart.H0), add, mul, ZERO)), matmul(values(chart.H1), delta, add, mul, ZERO)),
}));
const genericTail = zeros(15, 15, null).map((row) =>
  row.map(() => bound([...Array(14).fill(0), 1, 1, 1, 1]))
);
const order = [5, 0, 1, 2, 3, 4];
const q2 = [];
const q3 = [];
for (let ia = 0; ia < order.length; ia++) {
  for (let ib = ia + 1; ib < order.length - 1; ib++) {
    const a = order[ia];
    const b = order[ib];
    const A = charts[a];
    const B = charts[b];
    const Z = matmul(matmul(B.E, genericTail, add, mul, ZERO), B.H1, add, mul, ZERO);
    const X02 = matmul(A.H0, Z, add, mul, ZERO);
    const X13 = matScale(matmul(matmul(A.E, Z, add, mul, ZERO), A.eta, add, mul, ZERO), MINUS);
    let scalarBound = collect(sub(X02[0][0], X13[10][0]));
    if (a === 5) {
      scalarBound = collect(mul(poleJet([1, 0, 0, 0], undefined, false, 5)[0], Z[10][0]));
    }
    q2.push({
      a,
      b,
      tailCarriers: order.slice(ib + 1),
      blocks: compress(collect([X02, X13])),
      scalar: compress(scalarBound),
    });
    for (let ic = ib + 1; ic < order.length - 1; ic++) {
      const c = order[ic];
      const C = charts[c];
      const middle = matmul(matmul(C.E, genericTail, add, mul, ZERO), C.H1, add, mul, ZERO);
      const block = matmul(
        A.H0,
        matmul(matmul(B.E, middle, add, mul, ZERO), B.eta, add, mul, ZERO),
        add,
        mul,
        ZERO
      );
      q3.push({
        a,
        b,
        c,
        tailCarriers: order.slice(ic + 1),
        block: compress(collect(block)),
      });
    }
  }
}

const report = {
  mode: MODE,
  abstractNodes: nodes.length,
  tailPrimaryJ0: tail,
  q2,
  q3,
};
process.stdout.write(JSON.stringify(report));
