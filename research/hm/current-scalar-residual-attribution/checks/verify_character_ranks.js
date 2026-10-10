#!/usr/bin/env node
'use strict';
// Execute the exact public finite model, and bind its classical matrices.
const fs = require('node:fs'), vm = require('node:vm');
const crypto = require('node:crypto'), assert = require('node:assert/strict');
const path = require('node:path');
const hash = x => crypto.createHash('sha256').update(x).digest('hex');
const args = process.argv.slice(2);
if (args.length !== 2) throw Error('Usage: verify_character_ranks.js PINNED_SOURCE MODEL_JSON');
const root = path.resolve(__dirname, '..');
const pins = JSON.parse(fs.readFileSync(path.join(root, 'pins.json')));
const original = fs.readFileSync(args[0]);
assert.equal(hash(original), pins.dependencies.finiteModel.sha256, 'Finite source hash mismatch');
const modelBytes = fs.readFileSync(args[1]);
assert.equal(hash(modelBytes), pins.dependencies.model.sha256, 'Geometric model hash mismatch');
const model = JSON.parse(modelBytes);
let source = original.toString('utf8');
const anchor = '  const summaries=[];';
assert.equal(source.split(anchor).length, 2, 'Unique export anchor required');
// Add a read-only observation point. No differential, contraction, pruning,
// expected-rank assertion, or elimination algorithm is changed.
source = source.replace(anchor, '  globalThis.classical = {d,ranks};\n' + anchor);
const context = vm.createContext({console: {log() {}}});
vm.runInContext(source + '\nglobalThis.answer = result;', context,
                {timeout: 290000, filename: path.basename(args[0])});
const {d,ranks} = context.classical;
assert.equal(JSON.stringify(ranks), '[5,15,10,2]');
let entries = 0;
for (const [l,key] of ['gamma','delta','ev'].entries()) {
  const matrices = Array.from({length:ranks[l+1]}, () =>
    Array.from({length:ranks[l]}, () => new Map()));
  for (let col=0; col<d[l].length; col++) for (const [row,k,value] of d[l][col]) {
    const e = [0,0,0,0]; if(k) e[k-1] = 1;
    const monomial = e.join(',');
    const terms = matrices[row][col];
    terms.set(monomial, (terms.get(monomial)||0)+value);
  }
  const canonical = p => JSON.stringify([...p].filter(([,v])=>v).sort(([a],[b])=>a.localeCompare(b)));
  for (let row=0; row<ranks[l+1]; row++) for (let col=0; col<ranks[l]; col++) {
    assert.equal(canonical(matrices[row][col]), canonical(model[key][row][col]),
                 'Classical coefficient mismatch: '+key+' '+row+','+col);
    entries++;
  }
}
const result = JSON.parse(JSON.stringify(context.answer));
const perCharacter = result.summaries.map(x=>x.h1);
assert.deepEqual(perCharacter, [79,2,0,0,0]);
assert.deepEqual(result.summaries.map(x=>x.d1.rank), [50,150,450,1250,2550]);
assert.deepEqual(result.summaries.map(x=>x.remaining.rank), [3598,522,90,30,10]);
assert.equal(result.summaries[2].d3.rank, 100);
assert.equal(result.summaries[0].boundaryRank, 353);
const multiplicities = [1,4,6,4,1];
assert.equal(perCharacter.reduce((s,x,i)=>s+x*multiplicities[i],0),87);
console.log(JSON.stringify({status:'PASS', exactFiniteSourceSHA256:hash(original),
  classicalMatrixEntryIdentities:entries, perCharacterH1BySupportSize:perCharacter,
  characterMultiplicities:multiplicities, totalH1:87,
  initialRanks:result.summaries.map(x=>x.d1.rank), weightTwoLengthThreeRank:100,
  remainingRanks:result.summaries.map(x=>x.remaining.rank), trivialBoundaryRank:353,
  scope:'Exact rational ranks of the pinned finite model. Geometric model identification and symmetry are stated in the proof.'},null,2));
