#!/usr/bin/env node
/**
 * Independent exact review of PR #32 and PR #33.
 * Native BigInt only. Does not import or execute the authors' checkers.
 * Reads pinned blobs with git cat-file. No source-DAG replay.
 */
import { createHash } from "node:crypto";
import { execFileSync } from "node:child_process";
import { writeFileSync } from "node:fs";

const PINS = {
  pr32: "338bec6395f89c9a8f2e14bf98d025c9c2f4c7a9",
  pr33: "a0d02c2986d15d784bef8a226865cefac966bc3f",
  pr36: "d7efdbeb2def45af2fcfe2253f7d1eb61ab5bf1c",
  pr37: "67910d41054e5237f4dbe77fb32c3d3ad5ca6897",
  pr39: "5147e097ed9721eb4ad55f8f5cd20cd6427acb8c",
  pr40: "dc60a859a0157b1d2d1b57b37324509abc22c600",
  pr41: "08b73637d4136f91606aad332c46cafd064417f8",
  pr44: "650fc2a2b653a8d74854dd8c4bbfbb4871b7e371",
};

const V = 6;
const W = 37;
const Z = 22;
const RV = 11;
const RW = 73;
const QZ = 803;
const DENOMINATOR = 64n;

const defects = [];
const seenDefect = new Set();
function check(cond, name, detail) {
  if (!cond && !seenDefect.has(name)) {
    seenDefect.add(name);
    defects.push({ name, detail: detail ?? null });
  }
}

function gitBytes(rev, path) {
  const id = execFileSync("git", ["rev-parse", `${rev}:${path}`], {
    encoding: "utf8",
  }).trim();
  return execFileSync("git", ["cat-file", "blob", id], {
    maxBuffer: 64 * 1024 * 1024,
  });
}

function gitText(rev, path) {
  return gitBytes(rev, path).toString("utf8");
}

function gitJson(rev, path) {
  return JSON.parse(gitText(rev, path));
}

function sha256(bytes) {
  return createHash("sha256").update(bytes).digest("hex");
}

function bitLength(n) {
  if (n < 0n) n = -n;
  if (n === 0n) return 0;
  return n.toString(2).length;
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

function denseKey(ex, dims) {
  let key = 0;
  let stride = 1;
  for (let i = 0; i < dims.length; i++) {
    key += ex[i] * stride;
    stride *= dims[i];
  }
  return key;
}

function denseExponents(key, dims) {
  const ex = [];
  for (let i = 0; i < dims.length; i++) {
    ex.push(key % dims[i]);
    key = Math.floor(key / dims[i]);
  }
  return ex;
}

function polyMul(a, b, dims) {
  const out = new Map();
  for (const [ka, ca] of a) {
    const ea = denseExponents(ka, dims);
    for (const [kb, cb] of b) {
      const eb = denseExponents(kb, dims);
      const sum = new Array(dims.length);
      let legal = true;
      for (let i = 0; i < dims.length; i++) {
        const s = ea[i] + eb[i];
        if (s >= dims[i]) {
          legal = false;
          break;
        }
        sum[i] = s;
      }
      if (!legal) continue;
      const k = denseKey(sum, dims);
      const next = (out.get(k) ?? 0n) + ca * cb;
      if (next === 0n) out.delete(k);
      else out.set(k, next);
    }
  }
  return out;
}

function polyPow(base, exp, dims) {
  let result = new Map([[denseKey(dims.map(() => 0), dims), 1n]]);
  let b = base;
  let e = exp;
  while (e > 0n) {
    if (e & 1n) result = polyMul(result, b, dims);
    e >>= 1n;
    if (e > 0n) b = polyMul(b, b, dims);
  }
  return result;
}

function canonical(poly, dims) {
  const out = new Map();
  for (const [k, c] of poly) {
    if (c !== 0n) out.set(denseExponents(k, dims).join(","), c);
  }
  return out;
}

function strideEncode(r, w, z) {
  return r + RV * w + QZ * z;
}

function strideDecode(q) {
  return [q % RV, Math.floor(q / RV) % RW, Math.floor(q / QZ)];
}

function splitPack(poly, width) {
  let plus = 0n;
  let minus = 0n;
  const shiftBits = BigInt(8 * width);
  for (const [q, c] of poly) {
    const mag = c < 0n ? -c : c;
    const piece = mag << (BigInt(q) * shiftBits);
    if (c > 0n) plus += piece;
    else minus += piece;
  }
  return [plus, minus];
}

function packedMul(a, b) {
  if (a.size === 0 || b.size === 0) return new Map();
  let maxA = 1n;
  let maxB = 1n;
  let maxQa = 0;
  let maxQb = 0;
  for (const [q, c] of a) {
    const mag = c < 0n ? -c : c;
    if (mag > maxA) maxA = mag;
    if (q > maxQa) maxQa = q;
  }
  for (const [q, c] of b) {
    const mag = c < 0n ? -c : c;
    if (mag > maxB) maxB = mag;
    if (q > maxQb) maxQb = q;
  }
  const bound = BigInt(Math.min(a.size, b.size)) * maxA * maxB;
  const width = Math.ceil(bitLength(bound) / 8);
  const base = 1n << BigInt(8 * width);
  if (!(width > 0 && base > bound)) {
    throw new Error("digit base is not strictly above the coefficient bound");
  }
  if (width > 512) throw new Error("4096-bit packed digit guard");
  const [ap, an] = splitPack(a, width);
  const [bp, bn] = splitPack(b, width);
  const plus = ap * bp + an * bn;
  const minus = ap * bn + an * bp;
  const n = maxQa + maxQb + 1;
  const mask = base - 1n;
  const shiftBits = BigInt(8 * width);
  const out = new Map();
  for (let z = 0; z < Z; z++) {
    for (let w = 0; w < W; w++) {
      for (let r = 0; r < V; r++) {
        const q = strideEncode(r, w, z);
        if (q >= n) continue;
        const shifted = BigInt(q) * shiftBits;
        const c = ((plus >> shifted) & mask) - ((minus >> shifted) & mask);
        if (c !== 0n) out.set(q, c);
      }
    }
  }
  return out;
}

function toStride(densePoly) {
  const out = new Map();
  for (const [k, c] of densePoly) {
    const [r, w, z] = denseExponents(k, [V, W, Z]);
    out.set(strideEncode(r, w, z), c);
  }
  return out;
}

function fromStride(packed) {
  const out = new Map();
  for (const [q, c] of packed) {
    out.set(strideDecode(q).join(","), c);
  }
  return out;
}

function mapsEqual(left, right) {
  if (left.size !== right.size) return false;
  for (const [k, v] of left) if (right.get(k) !== v) return false;
  return true;
}

function makeRng(seed) {
  let state = seed >>> 0;
  return () => {
    state = (Math.imul(1664525, state) + 1013904223) >>> 0;
    return state;
  };
}

function randBelow(rng, bound) {
  if (bound <= 0) throw new Error("empty sample");
  return rng() % bound;
}

function randBits(rng, bits) {
  let value = 0n;
  let left = bits;
  while (left > 0) {
    const take = Math.min(left, 16);
    const chunk = BigInt(rng() & ((1 << take) - 1));
    value = (value << BigInt(take)) | chunk;
    left -= take;
  }
  if (value === 0n) value = 1n;
  return value;
}

function sampleKeys(rng, count, universe) {
  const copy = universe.slice();
  const out = [];
  for (let i = 0; i < count; i++) {
    const j = randBelow(rng, copy.length - i);
    const swap = copy[j];
    copy[j] = copy[copy.length - 1 - i];
    copy[copy.length - 1 - i] = swap;
    out.push(copy[copy.length - 1 - i]);
  }
  return out;
}

function randomPoly(rng, count, bits, universe) {
  const poly = new Map();
  if (count === 0) return poly;
  for (const key of sampleKeys(rng, count, universe)) {
    const mag = randBits(rng, bits);
    poly.set(key, rng() & 1 ? mag : -mag);
  }
  return poly;
}

function binomial(n, k) {
  let c = 1n;
  for (let i = 1; i <= k; i++) {
    c = (c * BigInt(n - k + i)) / BigInt(i);
  }
  return c;
}

function checkStrideNonalias() {
  let pairs = 0;
  let aliases = 0;
  for (let z1 = 0; z1 < Z; z1++) {
    for (let w1 = 0; w1 < W; w1++) {
      for (let r1 = 0; r1 < V; r1++) {
        for (let z2 = 0; z2 < Z; z2++) {
          for (let w2 = 0; w2 < W; w2++) {
            for (let r2 = 0; r2 < V; r2++) {
              pairs++;
              const q =
                r1 + r2 + RV * (w1 + w2) + QZ * (z1 + z2);
              const [r, w, z] = strideDecode(q);
              const inside = r1 + r2 < V && w1 + w2 < W && z1 + z2 < Z;
              const decodedLegal = r < V && w < W && z < Z;
              if (inside) {
                if (r !== r1 + r2 || w !== w1 + w2 || z !== z1 + z2) aliases++;
              } else if (decodedLegal) aliases++;
            }
          }
        }
      }
    }
  }
  check(RV * RW === QZ, "stride-factor", `${RV}*${RW}!==${QZ}`);
  check(pairs === V * W * Z * V * W * Z, "stride-pair-count", String(pairs));
  check(aliases === 0, "stride-alias", String(aliases));
  return { pairs, aliases };
}

function checkArithmetic() {
  check(RV * RW === QZ, "qz-equals-rv-rw");
  const stride = checkStrideNonalias();
  const dims = [V, W, Z];
  const universe = [];
  for (let z = 0; z < Z; z++) {
    for (let w = 0; w < W; w++) {
      for (let r = 0; r < V; r++) universe.push(denseKey([r, w, z], dims));
    }
  }
  check(universe.length === 4884, "slot-count", String(universe.length));

  const rng = makeRng(20261010);
  let randomProducts = 0;
  const sizes = [0, 1, 2, 7, 31, 67];
  const bitChoices = [1, 8, 31, 127, 269, 423, 777];
  for (let n = 0; n < 48; n++) {
    const a = randomPoly(
      rng,
      sizes[randBelow(rng, sizes.length)],
      bitChoices[randBelow(rng, bitChoices.length)],
      universe,
    );
    const b = randomPoly(
      rng,
      [0, 1, 3, 19, 41][randBelow(rng, 5)],
      bitChoices[randBelow(rng, bitChoices.length)],
      universe,
    );
    const expected = canonical(polyMul(a, b, dims), dims);
    const got = fromStride(packedMul(toStride(a), toStride(b)));
    check(mapsEqual(expected, got), "random-packed-product", String(n));
    randomProducts++;
  }

  const hand = [
    [new Map([[denseKey([0, 0, 0], dims), 2n], [denseKey([1, 0, 0], dims), -3n]]),
      new Map([[denseKey([0, 0, 0], dims), 5n], [denseKey([0, 1, 0], dims), 7n]])],
    [new Map([[denseKey([5, 0, 0], dims), -9n]]), new Map([[denseKey([1, 0, 0], dims), 17n]])],
    [new Map([[denseKey([0, 36, 0], dims), -9n]]), new Map([[denseKey([0, 1, 0], dims), 17n]])],
    [new Map([[denseKey([0, 0, 21], dims), -9n]]), new Map([[denseKey([0, 0, 1], dims), 17n]])],
    [new Map([[denseKey([5, 36, 21], dims), -9n]]), new Map([[denseKey([5, 36, 21], dims), 17n]])],
    [new Map([[denseKey([5, 0, 0], dims), 5n]]), new Map([[denseKey([5, 0, 0], dims), 7n]])],
    [new Map([[denseKey([0, 0, 0], dims), -2n]]), new Map([[denseKey([0, 0, 0], dims), -3n]])],
  ];
  const handExpected = [
    new Map([
      ["0,0,0", 10n],
      ["0,1,0", 14n],
      ["1,0,0", -15n],
      ["1,1,0", -21n],
    ]),
    new Map(),
    new Map(),
    new Map(),
    new Map(),
    new Map(),
    new Map([["0,0,0", 6n]]),
  ];
  hand.forEach(([a, b], i) => {
    const got = fromStride(packedMul(toStride(a), toStride(b)));
    const direct = canonical(polyMul(a, b, dims), dims);
    check(mapsEqual(got, direct) && mapsEqual(got, handExpected[i]), "hand-product", String(i));
  });

  const denseCases = [];
  for (const [bits, alternating] of [[1, true], [64, true], [423, false]]) {
    const M = (1n << BigInt(bits)) - 1n;
    const a = new Map();
    for (const key of universe) {
      const [r, w, z] = denseExponents(key, dims);
      const sign = alternating && ((r + w + z) & 1) ? -1n : 1n;
      a.set(key, sign * M);
    }
    const got = fromStride(packedMul(toStride(a), toStride(a)));
    let mismatches = 0;
    for (const key of universe) {
      const [r, w, z] = denseExponents(key, dims);
      const count = BigInt(r + 1) * BigInt(w + 1) * BigInt(z + 1);
      const sign = alternating && ((r + w + z) & 1) ? -1n : 1n;
      const expected = sign * count * M * M;
      if (got.get(`${r},${w},${z}`) !== expected) mismatches++;
    }
    check(got.size === universe.length && mismatches === 0, "dense-closed-form", `${bits}/${alternating}`);
    denseCases.push({ bits, alternating, mismatches, slots: got.size });
  }

  const powers = [];
  for (const exponent of [0, 1, 2, 3, 13, 71, 72, 142]) {
    const a = new Map([
      [denseKey([0, 0, 0], dims), 2n],
      [denseKey([1, 0, 0], dims), -3n],
      [denseKey([0, 1, 0], dims), 1n],
    ]);
    const direct = canonical(polyPow(a, BigInt(exponent), dims), dims);
    let packed = new Map([[0, 1n]]);
    let base = toStride(a);
    let e = exponent;
    while (e > 0) {
      if (e & 1) packed = packedMul(packed, base);
      e = Math.floor(e / 2);
      if (e) base = packedMul(base, base);
    }
    check(mapsEqual(fromStride(packed), direct), "ordinary-power", String(exponent));
    powers.push(exponent);
  }

  const onePlusV = new Map([
    [denseKey([0, 0, 0], dims), 1n],
    [denseKey([1, 0, 0], dims), 1n],
  ]);
  for (const exponent of [0, 1, 2, 6, 71, 72, 142]) {
    const got = canonical(polyPow(onePlusV, BigInt(exponent), dims), dims);
    for (let k = 0; k < V; k++) {
      const expected = k <= exponent ? binomial(exponent, k) : 0n;
      check((got.get(`${k},0,0`) ?? 0n) === expected, "binomial-v", `${exponent},${k}`);
    }
    check(got.get("6,0,0") === undefined, "v6-absent", String(exponent));
  }
  const v71 = canonical(polyPow(onePlusV, 71n, dims), dims);
  check(v71.get("1,0,0") === 71n, "characteristic-zero-cross-term", String(v71.get("1,0,0")));

  let guard = 0;
  try {
    packedMul(new Map([[0, 1n << 4096n]]), new Map([[0, 1n]]));
  } catch (error) {
    if (String(error.message).includes("4096-bit")) guard++;
  }
  check(guard === 1, "width-guard");

  return {
    stride,
    randomProducts,
    randomSeed: 20261010,
    denseCases,
    ordinaryPowers: powers,
    characteristicZeroCrossTerm: "71",
    widthGuardRejected4096BitDigit: guard === 1,
  };
}

function kernels() {
  const dims = [6, 22];
  const h = new Map();
  for (const [t, z, c] of [
    [0, 1, 1n],
    [1, 0, 1n],
    [1, 1, 3n],
    [1, 2, 1n],
    [2, 1, 1n],
    [2, 2, 1n],
  ]) {
    h.set(denseKey([t, z], dims), c);
  }
  let current = new Map([[0, 1n]]);
  const inv = new Map([[0, 1n]]);
  let n = 0;
  while (true) {
    current = polyMul(current, h, dims);
    n++;
    if (current.size === 0) break;
    const sign = n % 2 === 1 ? -1n : 1n;
    for (const [k, c] of current) {
      const next = (inv.get(k) ?? 0n) + sign * c;
      if (next === 0n) inv.delete(k);
      else inv.set(k, next);
    }
    if (n > 40) throw new Error("G series did not become nilpotent");
  }
  const g = new Map(h);
  g.set(0, (g.get(0) ?? 0n) + 1n);
  const product = polyMul(g, inv, dims);
  check(product.size === 1 && product.get(0) === 1n, "kernel-inverse");
  const answer = polyPow(inv, 70n, dims);
  const back = polyMul(polyPow(g, 70n, dims), answer, dims);
  check(back.size === 1 && back.get(0) === 1n, "kernel-seventieth-power");
  const matrix = Array.from({ length: 6 }, () => Array(22).fill(0n));
  let negative = 0;
  let positive = 0;
  let content = 0n;
  for (const [k, c] of answer) {
    const [t, z] = denseExponents(k, dims);
    matrix[t][z] = c;
    if (c < 0n) negative++;
    if (c > 0n) positive++;
    content = content === 0n ? (c < 0n ? -c : c) : gcd(content, c);
  }
  check(matrix[0][0] === 1n, "kernel-constant-term", String(matrix[0][0]));
  check(n === 27, "kernel-nilpotency-index", String(n));
  return {
    matrix,
    nilpotencyIndex: n,
    nonzero: answer.size,
    positive,
    negative,
    content: content.toString(),
    constantTerm: matrix[0][0].toString(),
  };
}

function permutations(values) {
  if (values.length === 0) return [[]];
  const out = [];
  for (let i = 0; i < values.length; i++) {
    const rest = values.slice(0, i).concat(values.slice(i + 1));
    for (const tail of permutations(rest)) out.push([values[i], ...tail]);
  }
  return out;
}

function rowAtMost(left, right) {
  for (let i = 0; i < 3; i++) {
    if (left[i] < right[i]) return true;
    if (left[i] > right[i]) return false;
  }
  return String(left[3]) <= String(right[3]);
}

function monomials() {
  const out = [];
  for (let a = 0; a < 3; a++) {
    for (let b = 0; b < 3; b++) {
      for (let c = 0; c < 3; c++) {
        for (let d = 0; d < 3; d++) out.push([a, b, c, d]);
      }
    }
  }
  return out;
}

function coordinateIndex(m) {
  return (2 - m[0]) * 27 + (2 - m[1]) * 9 + (2 - m[2]) * 3 + (2 - m[3]);
}

function checkExactZero(kernel) {
  const root = "research/hm/current-scalar-result";
  const pinBytes = gitBytes(PINS.pr33, `${root}/data-pins.json`);
  const pins = JSON.parse(pinBytes.toString("utf8"));
  const fileHashes = {};
  for (const [name, digest] of Object.entries(pins.files)) {
    const bytes = gitBytes(PINS.pr33, `${root}/${name}`);
    const got = sha256(bytes);
    fileHashes[name] = got;
    check(got === digest, "data-pin", name);
  }
  const finalBytes = gitBytes(PINS.pr33, `${root}/final-result.json`);
  const finalHash = sha256(finalBytes);
  check(finalHash === pins.originalFinalResultSHA256, "final-result-hash", finalHash);
  check(
    finalHash === "0ae5a9176b5d47afe85ae3a144fed2df55079396ae5e789461ef9358ea98f791",
    "published-final-hash",
  );
  const expected = JSON.parse(finalBytes.toString("utf8"));
  const relations = gitJson(PINS.pr33, `${root}/relation-rows.json`);

  const matrix = relations.relations.map((relation) => {
    const row = Array(81).fill(0n);
    for (const term of relation.terms) row[term.index] += BigInt(term.coefficient);
    return row;
  });
  const pivots = relations.relation_identity_minor_columns;
  check(matrix.length === 47 && pivots.length === 47, "relation-shape");
  let minorDefects = 0;
  for (let i = 0; i < matrix.length; i++) {
    for (let j = 0; j < pivots.length; j++) {
      const want = i === j ? 1n : 0n;
      if (matrix[i][pivots[j]] !== want) minorDefects++;
    }
  }
  check(minorDefects === 0, "identity-minor", String(minorDefects));

  const structural = relations.relations
    .filter((relation) => relation.kind === "coordinate_zero")
    .map((relation) => relation.terms[0].index)
    .sort((a, b) => a - b);
  check(structural.length === 35 && new Set(structural).size === 35, "structural-count");
  check(
    JSON.stringify(structural) === JSON.stringify(expected.theoremDerivedZeroIndices),
    "structural-index-match",
  );
  const numericalFromComplement = [];
  for (let i = 0; i < 81; i++) if (!structural.includes(i)) numericalFromComplement.push(i);
  check(
    JSON.stringify(numericalFromComplement) === JSON.stringify(expected.numericallyEvaluatedIndices),
    "numerical-index-match",
  );

  const degreeByIndex = new Map();
  const outsideWindow = [];
  for (const m of monomials()) {
    const index = coordinateIndex(m);
    const laurent = m.map((x) => -x - 1);
    const alt = laurent.reduce((sum, e, i) => sum + (e + 3) * 3 ** (3 - i), 0);
    check(alt === index, "laurent-index", String(index));
    const attr = expected.coordinateAttribution[index];
    check(attr.index === index && JSON.stringify(attr.m) === JSON.stringify(m), "attribution-m", String(index));
    check(JSON.stringify(attr.laurentExponents) === JSON.stringify(laurent), "attribution-laurent", String(index));
    const S = m.reduce((s, x) => s + x, 0);
    degreeByIndex.set(index, S);
    if (S < 3 || S > 6) outsideWindow.push(index);
  }
  outsideWindow.sort((a, b) => a - b);
  check(outsideWindow.every((index) => structural.includes(index)), "outside-window-is-structural");
  check(numericalFromComplement.every((index) => {
    const S = degreeByIndex.get(index);
    return S >= 3 && S <= 6;
  }), "numerical-inside-window");
  check(indexOfRecordedSlots(expected), "scalar-slots");

  const polys = new Map();
  let negativeNumerators = 0;
  let positiveNumerators = 0;
  let maxNumeratorBits = 0;
  let outsideInterpretedNonzeros = 0;
  let retained = 0;
  const denominatorSet = new Set();
  for (const roles of permutations([0, 1, 2, 3])) {
    const name = `quotients/edge-${roles.join("")}.json`;
    const q = gitJson(PINS.pr33, `${root}/${name}`);
    check(JSON.stringify(q.roles) === JSON.stringify(roles), "roles", name);
    check(q.field === "Q" && JSON.stringify(q.quotientShape) === "[6,37,22]", "shape", name);
    check(q.homogeneousDegreesRemainSeparated === true && q.pairingAggregated === false, "separation", name);
    check(q.commonDenominator === "64", "denominator-string", `${name}:${q.commonDenominator}`);
    denominatorSet.add(q.commonDenominator);
    const rows = q.integerQuotientCoefficients;
    check(rows.length === q.retainedNonzeros, "retained-count", name);
    const rowHash = sha256(Buffer.from(JSON.stringify(rows)));
    check(rowHash === q.integerCoefficientSHA256, "row-hash", name);
    const sorted = rows.every((row, i) => i === 0 || rowAtMost(rows[i - 1], row));
    check(sorted, "row-sorted", name);
    const poly = new Map();
    for (const row of rows) {
      check(row.length === 4, "row-width", name);
      const [r, w, z, raw] = row;
      check(Number.isInteger(r) && Number.isInteger(w) && Number.isInteger(z), "exponent-type", name);
      check(r >= 0 && r < V && w >= 0 && w < W && z >= 0 && z < Z, "exponent-range", name);
      check(typeof raw === "string" && /^-?[1-9][0-9]*$/.test(raw), "numerator-canonical", `${name}:${raw}`);
      const numerator = BigInt(raw);
      check(!poly.has(`${r},${w},${z}`), "duplicate-slot", name);
      poly.set(`${r},${w},${z}`, numerator);
      if (numerator < 0n) negativeNumerators++;
      else positiveNumerators++;
      maxNumeratorBits = Math.max(maxNumeratorBits, bitLength(numerator));
      if (w < 33 || w > 36) outsideInterpretedNonzeros++;
      retained++;
    }
    polys.set(roles.join(""), poly);
  }
  check(polys.size === 24, "quotient-count", String(polys.size));
  check(denominatorSet.size === 1 && denominatorSet.has("64"), "denominator-set");

  const values = Array(81).fill(0n);
  const seen = new Map();
  let requests = 0;
  let sourceRows = 0;
  let nonzeroRows = 0;
  let nonzeroEdges = 0;
  let positiveContributions = 0;
  let negativeContributions = 0;
  let maxAbsPartial = 0n;
  let maxAbsEdge = 0n;
  const degreeCounts = { 3: 0, 4: 0, 5: 0, 6: 0 };
  const signByRoles = {};
  const numericalSet = new Set(numericalFromComplement);
  const structuralRecipe = [];
  const windowActivity = new Map();
  for (const m of monomials()) {
    const index = coordinateIndex(m);
    const S = m[0] + m[1] + m[2] + m[3];
    if (S < 3 || S > 6) continue;
    if (numericalSet.has(index)) degreeCounts[S]++;
    for (const roles of permutations([0, 1, 2, 3])) {
      const [i, j, k, l] = roles;
      if (m[i] !== 2) continue;
      let inversions = 0;
      for (let a = 0; a < 4; a++) {
        for (let b = a + 1; b < 4; b++) if (roles[a] > roles[b]) inversions++;
      }
      const sign = inversions % 2 === 0 ? 1n : -1n;
      signByRoles[roles.join("")] = sign.toString();
      const d = 3 + m[j];
      const limit = 21 - m[l];
      const w = 30 + S;
      check(w >= 33 && w <= 36, "interpreted-window", String(w));
      let unsigned = 0n;
      const poly = polys.get(roles.join(""));
      for (let r = 0; r <= d; r++) {
        for (let ell = 0; ell <= limit; ell++) {
          const ex = [0, 0, 0, 0];
          ex[i] = 272;
          ex[j] = 212 - r;
          ex[k] = 159 - S + r - ell;
          ex[l] = 48 + ell;
          const exSum = ex[0] + ex[1] + ex[2] + ex[3];
          check(exSum === 691 - S, "exponent-sum", `${exSum}!=${691 - S}`);
          const triple = ex[j] + ex[k] + ex[l];
          check(449 - triple === w, "total-cap-slot", `${449 - triple}!=${w}`);
          check(212 - ex[j] === r && ex[l] - 48 === ell && ex[i] === 272, "axis-caps");
          const numerator = poly.get(`${r},${w},${ell}`) ?? 0n;
          const weight = kernel.matrix[d - r][limit - ell];
          const contribution = sign * numerator * weight;
          unsigned += numerator * weight;
          if (contribution > 0n) positiveContributions++;
          if (contribution < 0n) negativeContributions++;
          const key = ex.join(",");
          if (seen.has(key)) check(seen.get(key) === numerator.toString(), "shared-exponent", key);
          else seen.set(key, numerator.toString());
          const activity = windowActivity.get(index) ?? { sourceRows: 0, nonzeroRows: 0 };
          activity.sourceRows++;
          if (numerator !== 0n) activity.nonzeroRows++;
          windowActivity.set(index, activity);
          if (numericalSet.has(index)) {
            sourceRows++;
            if (numerator !== 0n) nonzeroRows++;
          }
        }
      }
      const edge = sign * unsigned;
      const edgeAbs = edge < 0n ? -edge : edge;
      if (edgeAbs > maxAbsEdge) maxAbsEdge = edgeAbs;
      values[index] += edge;
      const abs = values[index] < 0n ? -values[index] : values[index];
      if (abs > maxAbsPartial) maxAbsPartial = abs;
      const activity = windowActivity.get(index) ?? { sourceRows: 0, nonzeroRows: 0, requests: 0, nonzeroEdges: 0 };
      activity.requests = (activity.requests ?? 0) + 1;
      if (unsigned !== 0n) activity.nonzeroEdges = (activity.nonzeroEdges ?? 0) + 1;
      windowActivity.set(index, activity);
      if (!numericalSet.has(index)) continue;
      requests++;
      if (unsigned !== 0n) nonzeroEdges++;
    }
  }
  for (const m of monomials()) {
    const index = coordinateIndex(m);
    if (!structural.includes(index)) continue;
    const S = m[0] + m[1] + m[2] + m[3];
    const active = m.filter((x) => x === 2).length;
    const slot = 30 + S;
    const inWindow = slot >= 33 && slot <= 36;
    let reducedNumerator = null;
    if (inWindow) {
      const g = gcd(values[index], DENOMINATOR);
      reducedNumerator = (values[index] / g).toString() + "/" + (DENOMINATOR / g).toString();
    }
    const activity = windowActivity.get(index);
    structuralRecipe.push({
      index,
      m,
      S,
      activeAnchors: active,
      slot,
      inInterpretedWindow: inWindow,
      recipeNumerator: inWindow ? values[index].toString() : null,
      recipeReduced: reducedNumerator,
      requests: activity?.requests ?? 0,
      nonzeroEdges: activity?.nonzeroEdges ?? 0,
      sourceRows: activity?.sourceRows ?? 0,
      nonzeroRows: activity?.nonzeroRows ?? 0,
    });
  }
  check(JSON.stringify(degreeCounts) === JSON.stringify({ 3: 12, 4: 18, 5: 12, 6: 4 }), "degree-counts");
  check(signByRoles["0123"] === "1", "identity-permutation-sign", signByRoles["0123"]);

  const reduced = values.map((numerator) => {
    if (numerator === 0n) return ["0", "1"];
    const g = gcd(numerator, DENOMINATOR);
    const den = DENOMINATOR / g;
    let num = numerator / g;
    if (den < 0n) {
      num = -num;
    }
    return [num.toString(), (den < 0n ? -den : den).toString()];
  });
  for (const index of structural) reduced[index] = ["0", "1"];
  let nonzeroNumerical = 0;
  for (const index of numericalFromComplement) {
    if (values[index] !== 0n) nonzeroNumerical++;
  }
  check(nonzeroNumerical === 0, "numerical-zero", String(nonzeroNumerical));
  check(JSON.stringify(reduced) === JSON.stringify(expected.coordinates), "recorded-coordinates");
  check(expected.coordinates.every((pair) => pair[0] === "0" && pair[1] === "1"), "recorded-reduced-zero");

  let residualDefects = 0;
  for (const row of matrix) {
    let residual = 0n;
    for (let i = 0; i < 81; i++) residual += row[i] * values[i];
    if (residual !== 0n) residualDefects++;
  }
  check(residualDefects === 0, "relation-residual-on-replay", String(residualDefects));

  const numericalExponents = new Set();
  for (const m of monomials()) {
    const index = coordinateIndex(m);
    if (!numericalSet.has(index)) continue;
    const S = m[0] + m[1] + m[2] + m[3];
    for (const roles of permutations([0, 1, 2, 3])) {
      const [i, j, k, l] = roles;
      if (m[i] !== 2) continue;
      const d = 3 + m[j];
      const limit = 21 - m[l];
      for (let r = 0; r <= d; r++) {
        for (let ell = 0; ell <= limit; ell++) {
          const ex = [0, 0, 0, 0];
          ex[i] = 272;
          ex[j] = 212 - r;
          ex[k] = 159 - S + r - ell;
          ex[l] = 48 + ell;
          numericalExponents.add(ex.join(","));
        }
      }
    }
  }
  let distinctNonzero = 0;
  for (const key of numericalExponents) if (seen.get(key) !== "0") distinctNonzero++;
  const structuralOnlyExponents = [...seen.keys()].filter((key) => !numericalExponents.has(key)).length;
  const stats = {
    acceptedFullQuotients: polys.size,
    requests,
    sourceRows,
    distinctSourceExponents: numericalExponents.size,
    nonzeroSourceRows: nonzeroRows,
    nonzeroDistinctSourceCoefficients: distinctNonzero,
    nonzeroSignedEdgeSelections: nonzeroEdges,
  };
  for (const [key, value] of Object.entries(stats)) {
    check(value === expected[key], "stat-" + key, `${value}!=${expected[key]}`);
  }

  const cross = relations.relations
    .filter((relation) => relation.kind === "cross_coordinate_relation")
    .map((relation) => ({
      id: relation.id,
      terms: relation.terms.map((term) => ({
        index: term.index,
        coefficient: String(term.coefficient),
      })),
    }));

  return {
    finalResultSHA256: finalHash,
    commonDenominator: "64",
    denominatorFiles: 24,
    positiveNumerators,
    negativeNumerators,
    maxNumeratorBits,
    retained,
    outsideInterpretedWindowNonzeros: outsideInterpretedNonzeros,
    positiveContributions,
    negativeContributions,
    maxAbsRunningNumerator: maxAbsPartial.toString(),
    maxAbsEdgeNumerator: maxAbsEdge.toString(),
    identityPermutationSign: signByRoles["0123"],
    permutationSigns: signByRoles,
    stats,
    numericalCoordinates: numericalFromComplement.length,
    structuralCoordinates: structural.length,
    nonzeroNumerical,
    relationRows: matrix.length,
    crossRelations: cross.length,
    minorIsIdentity: minorDefects === 0,
    coordinatesReduced: reduced.every((pair) => pair[0] === "0" && pair[1] === "1"),
    structuralOnlyExponents,
    structuralRecipe,
  };
}

function indexOfRecordedSlots(expected) {
  const slot0 = expected.coordinateAttribution[0];
  const slot70 = expected.coordinateAttribution[70];
  return (
    expected.scalarMap === "matrix slot0 minus matrix slot70" &&
    JSON.stringify(slot0.m) === "[2,2,2,2]" &&
    JSON.stringify(slot70.m) === "[0,1,0,1]" &&
    JSON.stringify(slot0.laurentExponents) === "[-3,-3,-3,-3]" &&
    JSON.stringify(slot70.laurentExponents) === "[-1,-2,-1,-2]"
  );
}

function checkConsistency(exact) {
  const numerator = gitJson(
    PINS.pr36,
    "research/hm/current-scalar-numerator/expected.json",
  );
  const final = gitJson(
    PINS.pr33,
    "research/hm/current-scalar-result/final-result.json",
  );
  check(
    numerator.numerator.sha256 === "0254c93650e6ca6c1e9cbbb01810704eede98d10d0b75229fcff5d8fa2123e66",
    "numerator-pin",
  );
  check(final.sourceNumeratorSHA256 === numerator.numerator.sha256, "result-numerator-hash");

  const jetPins = gitJson(PINS.pr37, "research/hm/current-scalar-jet-sources/pins.json");
  const roots = [];
  for (const [pair, entry] of Object.entries(jetPins.pairs)) {
    roots.push({
      pair,
      denominator: entry.root.denominator,
      integerWeight: entry.root.integerWeight,
    });
    check(entry.root.denominator === "64", "jet-root-denominator", pair);
  }
  const byPair = Object.fromEntries(roots.map((row) => [row.pair, row.integerWeight]));
  check(byPair["01"] === "1" && byPair["10"] === "-1" && byPair["30"] === "1", "clearing-signs-01-10-30");

  const audit = gitJson(PINS.pr44, "research/hsd-pole-audit/results/audit-exact.json");
  const gate = audit.gates_3_and_4;
  check(audit.pin === PINS.pr40, "audit-pin");
  check(gate.frameExponent === -4, "frame-exponent");
  check(gate.clearingExponentSum === 55, "clearing-sum");
  check(gate.regularSectionDegree === 272, "degree-272");
  check(gate.degree273Coefficient === 0, "degree-273");
  check(gate.bundle === "O(272,272,272,272)", "bundle");
  const degreeFormula = gate.frameExponent + 1 + 5 * gate.clearingExponentSum;
  check(degreeFormula === 272 && degreeFormula === gate.regularSectionDegree, "degree-formula");

  const factor = gitJson(PINS.pr44, "research/hsd-pole-audit/results/factor48.json");
  check(factor.status === "PASS" && factor.axes.length === 4, "factor48-status");
  for (const axis of factor.axes) {
    const output = axis.outputs[1];
    const others = [0, 1, 2, 3].filter((i) => i !== axis.axis);
    check(output.totalMaximum === 449, "total-449", String(axis.axis));
    for (const coordinate of others) {
      check(output.coordinateMaximum[coordinate] === 212, "cap-212", `${axis.axis}:${coordinate}`);
      check(axis.exposedCoordinatePowers[String(coordinate)] === 48, "factor-48", `${axis.axis}:${coordinate}`);
    }
    check(axis.strippedCoordinateUpperBound === 212 - 48, "window-164", String(axis.axis));
    check(axis.strippedTotalUpperBound === 449 - 3 * 48, "window-305", String(axis.axis));
  }

  const attribution = gitJson(
    PINS.pr41,
    "research/hm/current-scalar-residual-attribution/pins.json",
  );
  check(attribution.publicDependencies.geometric.commit === PINS.pr40, "attribution-geometric-pin");
  const attributionReadme = gitText(
    PINS.pr41,
    "research/hm/current-scalar-residual-attribution/README.md",
  );
  check(attributionReadme.includes("L(X)=X02[0,0]-X13[10,0]"), "attribution-scalar-formula");

  const oracle32 = sha256(gitBytes(PINS.pr32, "research/hm/current-scalar-arithmetic/exact_oracle.py"));
  const oracle33 = sha256(gitBytes(PINS.pr33, "research/hm/current-scalar-result/exact_oracle.py"));
  const ring = sha256(gitBytes(PINS.pr32, "research/hm/current-scalar-arithmetic/integer_quotient_ring.py"));
  check(oracle32 === oracle33, "oracle-bytes");

  check(272 + 212 + 159 + 48 === 691, "base-sum");
  check(449 - (691 - 272) === 30, "slot-offset");
  check(exact.commonDenominator === "64", "replay-denominator");

  return {
    numeratorSHA256: numerator.numerator.sha256,
    resultNumeratorSHA256: final.sourceNumeratorSHA256,
    jetRootDenominators: roots,
    reviewedClearingSigns: { "01": byPair["01"], "10": byPair["10"], "30": byPair["30"] },
    frameExponent: gate.frameExponent,
    clearingExponentSum: gate.clearingExponentSum,
    regularSectionDegree: gate.regularSectionDegree,
    degree273Coefficient: gate.degree273Coefficient,
    degreeFormula,
    factor48: { exposed: 48, coordinateCap: 212, totalCap: 449, strippedCoordinate: 164, strippedTotal: 305 },
    oracleSHA256: oracle32,
    oraclesByteIdentical: oracle32 === oracle33,
    integerRingSHA256: ring,
    scalarFormulaPinnedBy41: true,
    slotArithmetic: "449-(691-S-272)=30+S",
  };
}

const started = Date.now();
const arithmetic = checkArithmetic();
const kernel = kernels();
const exact = checkExactZero(kernel);
const consistency = checkConsistency(exact);
const kernelSummary = {
  nilpotencyIndex: kernel.nilpotencyIndex,
  nonzero: kernel.nonzero,
  positive: kernel.positive,
  negative: kernel.negative,
  content: kernel.content,
  constantTerm: kernel.constantTerm,
};

const report = {
  status: defects.length === 0 ? "PASS" : "FAIL",
  pins: PINS,
  arithmetic,
  kernel: kernelSummary,
  exact,
  consistency,
  defects,
  elapsedSeconds: Number(((Date.now() - started) / 1000).toFixed(3)),
};

const outPath = process.argv[2] ?? "research/hsd-review/32-33/results.json";
writeFileSync(outPath, JSON.stringify(report, null, 2) + "\n");
console.log(JSON.stringify({
  status: report.status,
  defects: report.defects,
  elapsedSeconds: report.elapsedSeconds,
  stats: exact.stats,
  kernel: kernelSummary,
  signs: {
    positiveNumerators: exact.positiveNumerators,
    negativeNumerators: exact.negativeNumerators,
    positiveContributions: exact.positiveContributions,
    negativeContributions: exact.negativeContributions,
    identityPermutationSign: exact.identityPermutationSign,
  },
  structuralRecipe: exact.structuralRecipe.map((row) => ({
    index: row.index,
    m: row.m.join(""),
    S: row.S,
    activeAnchors: row.activeAnchors,
    inInterpretedWindow: row.inInterpretedWindow,
    recipeReduced: row.recipeReduced,
  })),
  structuralOnlyExponents: exact.structuralOnlyExponents,
  maxAbsEdgeNumerator: exact.maxAbsEdgeNumerator,
}, null, 2));
if (defects.length) process.exit(1);
