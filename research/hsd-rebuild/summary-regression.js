'use strict';

// Regression for publicSummary: multiplicity follows entry.weight, not the
// position of the weight in the requested list. Covers every singleton and
// two subsets whose array positions disagree with those weights.

const fs = require('fs');
const path = require('path');
const model = require('./hm-model');

const EXPECTED_H1 = [79, 2, 0, 0, 0];
const PINNED_HASHES = {
  0: {
    d1: 'c56216cb43fe35e86480ade0bced0314e5c8302f4bc86ca1ddc05d573d39f65d',
    len5: 'a9758b7d1a8155a960708df02baf70a9c5983b6effc4942ef66960dfd1d4d2c4',
    positive: 'a76318e4a5503ae2d8955d2a0f0709a4e589892f5bdeee9b2a6a232f78ddeb12',
    boundary: 'a0ce60e16b994a439f764b6c23e1339dd52ba70b8efab436fd6d739212ccefef'
  },
  1: {
    d1: '1b8ebddc75d83869512204ebaa646d9cac09c8981f1b47c3b52de62136d7f5a3',
    len5: 'cd4fcc1362787b13cc89aa9b53bc9547b1f265b5d6acd26619e388b767336a1b',
    diagonal: 'ce7336ba7087851ce6b63f4fad4c07dd2a3bcd66a665eb993c2584af46c19b84'
  },
  2: {
    d1: 'f9080c589158d508c301ab4d7ca068f162b81f99a1a5af9ae9f804f5a641c861',
    len5: '935ced65c9db84b4bd50f9720268f68206f914ceeb80ff7a33afea82cd2877ed',
    len3: 'dc7a4169c61bc6aff0a2530dee52208b0fbe8e2d9eced8cde053c842cc683bd3'
  },
  3: {
    d1: '24bfa3775f0e7f966645ae08a50efa99a7bc0c7c78dd67b803a13b456b8e25a0',
    len5: '6b20f7e86e4dd7e28473e133a85b853e8763859724b8391e00c750d445cd0076'
  },
  4: {
    d1: 'a829d202619ae3112438345e52266e5ff8dadbd268c5f58a3911fcde16ed480d',
    len5: 'e9d80d043ab16b51f4b360a203a34043e26c8d19be6a81e6ae2282feb4b8d8b3'
  }
};

function fail(message) {
  console.error(message);
  process.exitCode = 1;
  throw new Error(message);
}

function contribution(weight, h1) {
  return model.MULTIPLICITIES[weight] * h1;
}

function runSummary(weights) {
  const summary = model.publicSummary(model.computeExt1({weights}));
  const byEntry = summary.byWeight.reduce((sum, entry) => sum + contribution(entry.weight, entry.h1), 0);
  console.error(`weights ${weights.join(',')}: h1=${JSON.stringify(summary.h1ByWeight)} h1Total=${summary.h1Total} entrySum=${byEntry}`);
  if (byEntry !== summary.h1Total) {
    fail(`weights ${weights}: h1Total ${summary.h1Total} is not the entry.weight sum ${byEntry}`);
  }
  return summary;
}

function assertSummary(summary, weights, expectedH1, expectedTotal) {
  if (JSON.stringify(summary.h1ByWeight) !== JSON.stringify(expectedH1)) {
    fail(`weights ${weights}: h1 ${summary.h1ByWeight} expected ${expectedH1}`);
  }
  if (summary.h1Total !== expectedTotal) {
    fail(`weights ${weights}: h1Total ${summary.h1Total} expected ${expectedTotal}`);
  }
  for (const entry of summary.byWeight) {
    const pinned = PINNED_HASHES[entry.weight];
    for (const key of Object.keys(pinned)) {
      if (entry.hashes[key] !== pinned[key]) {
        fail(`weight ${entry.weight} ${key} hash ${entry.hashes[key]} != ${pinned[key]}`);
      }
    }
  }
}

function main() {
  const recorded = JSON.parse(fs.readFileSync(path.join(__dirname, 'comparison.json'), 'utf8'));
  const recordedHashes = recorded.matrices.map((item) => item.rebuiltHash);
  const pinnedList = Object.values(PINNED_HASHES).flatMap((block) => Object.values(block));
  if (pinnedList.length !== 14 || recordedHashes.length !== 14) {
    fail(`expected 14 block hashes, recorded ${recordedHashes.length}, listed ${pinnedList.length}`);
  }
  for (const hash of pinnedList) {
    if (!recordedHashes.includes(hash)) fail(`comparison.json is missing ${hash}`);
  }

  const singletons = [];
  for (let weight = 0; weight <= 4; weight++) singletons.push(runSummary([weight]));
  const singletonTotals = singletons.map((summary) => summary.h1Total);
  const singletonSum = singletonTotals.reduce((sum, value) => sum + value, 0);
  console.error(`singleton contributions ${singletonTotals.join('+')} = ${singletonSum}`);
  if (singletonSum !== 87) {
    fail(`singleton contributions sum to ${singletonSum}, not 87`);
  }
  singletons.forEach((summary, weight) => {
    assertSummary(summary, [weight], [EXPECTED_H1[weight]], contribution(weight, EXPECTED_H1[weight]));
  });

  // Position 0 would apply multiplicity 1. Weight 1's multiplicity is 4.
  const subset10 = runSummary([1, 0]);
  assertSummary(subset10, [1, 0], [2, 79], 8 + 79);
  // Position 1 would apply multiplicity 4. Weight 0's multiplicity is 1.
  const subset20 = runSummary([2, 0]);
  assertSummary(subset20, [2, 0], [0, 79], 79);

  console.log(JSON.stringify({
    singletonContributions: singletonTotals,
    singletonSum,
    subsets: {
      '1,0': 87,
      '2,0': 79
    }
  }));
}

main();
