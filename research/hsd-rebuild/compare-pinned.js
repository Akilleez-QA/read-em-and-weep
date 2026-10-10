'use strict';

// Entrywise comparison of the rebuilt finite model with PR #5 at
// add03476d9055aa00e1e00778eea6332cf8e01cc. The pinned program is executed
// only as a black-box oracle. Ranks below are recomputed by hm-model.js.
//
// From this directory:
//   node compare-pinned.js > comparison.json

const crypto = require('crypto');
const {execFileSync} = require('child_process');
const vm = require('vm');
const model = require('./hm-model');

const PINNED_HEAD = 'add03476d9055aa00e1e00778eea6332cf8e01cc';
const PINNED_MODEL_SHA256 = '1fe4608ed77f3767691e7ef4de375fc55b052ccf26159a4aae3ec6d35fe96414';

function loadOracle() {
  const source = execFileSync('git', ['show', `${PINNED_HEAD}:research/hm/verify-hm-ext.js`], {encoding: 'utf8'});
  const hash = crypto.createHash('sha256').update(source).digest('hex');
  if (hash !== PINNED_MODEL_SHA256) {
    throw new Error(`Pinned model hash ${hash} does not match ${PINNED_MODEL_SHA256}`);
  }
  const cut = source.indexOf('const result=verifyHMExt();');
  if (cut < 0) throw new Error('Pinned verifier tail is missing');
  let program = source.slice(0, cut) + 'verifyHMExt();\n';
  const anchor = '  const summaries=[];';
  if (!program.includes(anchor)) throw new Error('Pinned verifier anchor is missing');
  program = program.replace(anchor, `  globalThis.__PINNED_ORACLE = {gamma, d, ranks, negativeD1, run, mons, delta, homotopy};
  return null;
${anchor}`);
  vm.runInThisContext(program, {filename: 'verify-hm-ext.js'});
  return {oracle: globalThis.__PINNED_ORACLE, hash, bytes: Buffer.byteLength(source)};
}

function pinnedCharts(mask) {
  let charts = 0;
  for (let i = 0; i < 4; i++) if ((mask >> i) & 1) charts += model.POW3[i];
  return charts;
}

function pinnedToStates(raw) {
  const states = new Map();
  for (const [key, value] of raw) {
    if (!value) continue;
    const parts = key.split(',').map(Number);
    const [u, v, a, b, mask, e0, e1, e2, e3] = parts;
    const packed = model.pack(u, v, a, b, pinnedCharts(mask), [e0, e1, e2, e3]);
    const next = (states.get(packed) || 0n) + BigInt(value);
    if (next === 0n) states.delete(packed);
    else states.set(packed, next);
  }
  return states;
}

function columnMap(rows) {
  const columns = [];
  const width = rows.reduce((max, row) => {
    for (const column of row.keys()) if (column + 1 > max) max = column + 1;
    return max;
  }, 0);
  for (let column = 0; column < width; column++) columns.push(new Map());
  rows.forEach((row, index) => {
    for (const [column, value] of row) {
      if (value) columns[column].set(index, BigInt(value));
    }
  });
  return columns;
}

function diffColumns(rebuilt, pinned, limit = 12) {
  const width = Math.max(rebuilt.length, pinned.length);
  const mismatches = [];
  let count = 0;
  for (let column = 0; column < width; column++) {
    const left = rebuilt[column] || new Map();
    const right = pinned[column] || new Map();
    const rows = new Set([...left.keys(), ...right.keys()]);
    for (const row of rows) {
      const a = left.get(row) || 0n;
      const b = right.get(row) || 0n;
      if (a !== b) {
        count++;
        if (mismatches.length < limit) {
          mismatches.push({column, row, rebuilt: a.toString(), pinned: b.toString()});
        }
      }
    }
  }
  return {count, mismatches, rebuiltColumns: rebuilt.length, pinnedColumns: pinned.length};
}

function sortedTriples(edges) {
  const triples = [];
  for (const edge of edges) {
    triples.push(Array.isArray(edge) ? [edge[0], edge[1], edge[2]] : [edge.to, edge.k, edge.z]);
  }
  triples.sort((a, b) => a[0] - b[0] || a[1] - b[1] || a[2] - b[2]);
  return triples;
}

function canonicalizeComplex(levels) {
  return levels.map((sources) => sources.map((edges) => sortedTriples(edges)));
}

function compareLineComplex(complex, oracle) {
  let gammaMismatches = 0;
  const samples = [];
  for (let row = 0; row < 15; row++) {
    for (let source = 0; source < 5; source++) {
      for (let vector = 0; vector < 5; vector++) {
        if (complex.gamma[row][source][vector] !== oracle.gamma[row][source][vector]) {
          gammaMismatches++;
          if (samples.length < 8) {
            samples.push({
              row, source, vector,
              rebuilt: complex.gamma[row][source][vector],
              pinned: oracle.gamma[row][source][vector]
            });
          }
        }
      }
    }
  }
  const rebuiltEdges = JSON.stringify(canonicalizeComplex(complex.forward));
  const pinnedEdges = JSON.stringify(canonicalizeComplex(oracle.d));
  let firstEdgeDifference = null;
  if (rebuiltEdges !== pinnedEdges) {
    const left = canonicalizeComplex(complex.forward);
    const right = canonicalizeComplex(oracle.d);
    for (let level = 0; level < 3 && !firstEdgeDifference; level++) {
      const count = Math.max(left[level].length, right[level].length);
      for (let source = 0; source < count; source++) {
        const a = JSON.stringify(left[level][source] || null);
        const b = JSON.stringify(right[level][source] || null);
        if (a !== b) {
          firstEdgeDifference = {level, source, rebuilt: left[level][source] || null, pinned: right[level][source] || null};
          break;
        }
      }
    }
  }
  return {
    gammaEntries: 15 * 5 * 5,
    gammaMismatches,
    gammaSamples: samples,
    differentialEdgesMatch: rebuiltEdges === pinnedEdges,
    firstEdgeDifference
  };
}

function pinnedNegativeImages(oracle, weight) {
  const built = oracle.negativeD1(weight);
  const src = built.src;
  const ranges5 = [0, 1, 2, 3].map((i) => [0, i < weight ? 0 : 2]);
  const len5 = [];
  const len3 = weight === 2 ? [] : null;
  for (let column = 0; column < 10 * src.length; column++) {
    const vector = Array(10 * src.length).fill(0);
    vector[column] = 1;
    const fifth = oracle.run(vector, src, weight, 5, 15, ranges5);
    len5.push(model.projectLengthFive(pinnedToStates(fifth), weight).image);
    if (weight === 2) {
      const third = oracle.run(vector, src, weight, 3, 12, [[-1, -1], [-1, -1], [0, 0], [0, 0]]);
      len3.push(model.projectLengthThree(pinnedToStates(third)).image);
    }
  }
  return {
    d1: columnMap(built.A),
    len5,
    len3,
    d1Rows: built.A.length
  };
}

function pinnedPositive(oracle) {
  const monomials = oracle.mons([0, 0, 0, 0], [1, 1, 1, 1]);
  const ranges = [[0, 2], [0, 2], [0, 2], [0, 2]];
  const columns = [];
  for (let u = 0; u < 3; u++) {
    for (let a = 0; a < oracle.ranks[u + 1]; a++) {
      for (let b = 0; b < oracle.ranks[u]; b++) {
        for (let index = 0; index < monomials.length; index++) {
          let state = new Map([[[u, u + 1, a, b, 15, ...monomials[index]].join(','), 1]]);
          state = oracle.delta(state, 1, 1, 1, ranges);
          columns.push(model.projectLengthFive(pinnedToStates(state), 0).image);
        }
      }
    }
  }
  return columns;
}

function pinnedBoundary(oracle) {
  const ranges = [[0, 1], [0, 1], [0, 1], [0, 1]];
  const columns = [];
  for (let u = 0; u < 4; u++) {
    for (let a = 0; a < oracle.ranks[u]; a++) {
      for (let b = 0; b < oracle.ranks[u]; b++) {
        let state = new Map([[[u, u, a, b, 15, 0, 0, 0, 0].join(','), 1]]);
        state = oracle.delta(state, 0, 1, 1, ranges);
        columns.push(model.projectPositive(pinnedToStates(state)).image);
      }
    }
  }
  return columns;
}

function pinnedDiagonal(oracle) {
  const ranges = [[0, 0], [0, 2], [0, 2], [0, 2]];
  const columns = [];
  for (let u = 0; u < 4; u++) {
    for (let a = 0; a < oracle.ranks[u]; a++) {
      for (let b = 0; b < oracle.ranks[u]; b++) {
        let state = new Map([[[u, u, a, b, 14, -1, 0, 0, 0].join(','), 1]]);
        state = oracle.delta(state, 0, 1, 2, ranges);
        state = oracle.homotopy(state, 1, 1, 15);
        state = oracle.delta(state, 1, 2, 2, ranges);
        const image = model.projectLengthFive(pinnedToStates(state), 1).image;
        const signed = new Map();
        for (const [row, value] of image) signed.set(row, -value);
        columns.push(signed);
      }
    }
  }
  return columns;
}

function reportMatrix(name, rebuilt, pinned, nrows) {
  const diff = diffColumns(rebuilt, pinned);
  return {
    name,
    rows: nrows,
    columns: rebuilt.length,
    mismatches: diff.count,
    samples: diff.mismatches,
    rebuiltHash: model.hashColumns(rebuilt, nrows),
    pinnedHash: model.hashColumns(pinned, nrows),
    hashesMatch: model.hashColumns(rebuilt, nrows) === model.hashColumns(pinned, nrows)
  };
}

function main() {
  const {oracle, hash, bytes} = loadOracle();
  const computed = model.computeExt1();
  const line = compareLineComplex(computed.complex, oracle);
  const matrixReports = [];
  for (const entry of computed.byWeight) {
    const pinned = pinnedNegativeImages(oracle, entry.weight);
    matrixReports.push(reportMatrix(`weight ${entry.weight} length-one`, entry.matrices.d1, pinned.d1, entry.d1.rows));
    matrixReports.push(reportMatrix(`weight ${entry.weight} length-five`, entry.matrices.len5, pinned.len5, entry.remaining.rows));
    if (entry.weight === 2) {
      matrixReports.push(reportMatrix('weight 2 length-three', entry.matrices.len3, pinned.len3, 354));
    }
    if (entry.weight === 0) {
      matrixReports.push(reportMatrix('weight 0 internal degree one', entry.matrices.positive, pinnedPositive(oracle), entry.remaining.rows));
      matrixReports.push(reportMatrix('weight 0 boundaries', entry.matrices.boundary, pinnedBoundary(oracle), 3920));
    }
    if (entry.weight === 1) {
      matrixReports.push(reportMatrix('weight 1 diagonal', entry.matrices.diagonal, pinnedDiagonal(oracle), entry.remaining.rows));
    }
  }
  const summary = model.publicSummary(computed);
  const h1 = summary.byWeight.map((entry) => entry.h1);
  const ranks = summary.byWeight.map((entry) => ({
    weight: entry.weight,
    h1: entry.h1,
    d1: entry.d1,
    d3: entry.d3,
    remaining: entry.remaining,
    boundaryRank: entry.boundaryRank
  }));
  const total = summary.h1Total;
  const mismatches = matrixReports.reduce((sum, item) => sum + item.mismatches, 0) + line.gammaMismatches + (line.differentialEdgesMatch ? 0 : 1);
  const report = {
    pinnedHead: PINNED_HEAD,
    pinnedModelSha256: hash,
    pinnedModelBytes: bytes,
    finiteSpace: computed.space,
    lineComplex: line,
    matrices: matrixReports.map((item) => ({
      name: item.name,
      rows: item.rows,
      columns: item.columns,
      mismatches: item.mismatches,
      rebuiltHash: item.rebuiltHash,
      pinnedHash: item.pinnedHash,
      samples: item.samples
    })),
    ranks,
    h1ByWeight: h1,
    h1WithMultiplicities: total,
    expectedH1: [79, 2, 0, 0, 0],
    expectedTotal: 87,
    rankAgreesWithExpected: JSON.stringify(h1) === JSON.stringify([79, 2, 0, 0, 0]) && total === 87,
    entrywiseMismatches: mismatches
  };
  console.log(JSON.stringify(report, null, 2));
  if (mismatches || !report.rankAgreesWithExpected) process.exitCode = 1;
}

if (require.main === module) main();
