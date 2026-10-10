#!/usr/bin/env node
'use strict';
// Rebuild the full outgoing differential and check exact integer witnesses.
// The unchanged oracle is loaded as a pinned implementation; no file is written.
const fs = require('node:fs'), path = require('node:path');
const vm = require('node:vm'), crypto = require('node:crypto');
const assert = require('node:assert/strict');
const root = path.resolve(__dirname, '..');
const sourceFile = path.join(root, 'finite-model/full-sign-boundary-oracle.js');
const source = fs.readFileSync(sourceFile, 'utf8');
const hash = x => crypto.createHash('sha256').update(x).digest('hex');
assert.equal(hash(source), '29bbe778ed43ce91b52390d27fd78678879bb39c877982afb8063676b3fe1558');
const context = vm.createContext({require, module: {exports: {}}, __dirname: path.dirname(sourceFile), console});
vm.runInContext(source + '\nmodule.exports.extra={initialMatrix,delta,homotopy,indexes,exactRank};', context, {filename: sourceFile});
const oracle = context.module.exports;
const {basis, prepare, positiveD1, integerRows, UnitEchelon} = oracle;
const {initialMatrix, delta, homotopy, indexes, exactRank} = oracle.extra;
const sorted = r => [...r].sort((a, b) => a[0] - b[0]);
const checked = x => { assert(Number.isSafeInteger(x)); return x; };
const add = (r, j, x) => { const z = checked((r.get(j) || 0) + x); if(z) r.set(j,z); else r.delete(j); };
function multiplyRow(w, matrix) {
  const out = new Map();
  for (const [i,z] of w) for (const [j,a] of matrix[i]) add(out,j,checked(z*a));
  return out;
}
function outgoingMatrices() {
  const B=Array.from({length:3920},()=>new Map()), D=Array.from({length:4080},()=>new Map());
  function append(M,col,positive) {
    for(const [key,z] of M) {
      const [u,v,a,b,mask,...e]=key.split(',').map(Number);
      const j=indexes[positive?'outPositive':'outNegative'].get([u,v,a,b,...e].join(','));
      assert.notEqual(j,undefined); const value=checked(Number(z)); assert.equal(BigInt(value),z);
      if(positive)D[3920+j].set(col,value); else { B[j].set(col,value); D[j].set(col,value); }
    }
  }
  for(let j=0;j<6480;j++) {
    const [u,v,a,b,...e]=basis.negative[j];
    const input=new Map([[[u,v,a,b,0,...e].join(','),1n]]);
    append(delta(input,-2,1,1,-2,-1),j,false); let M=input;
    for(let step=1;step<=5;step++) { M=delta(M,-2+step-1,step,5,0,1); if(step<5)M=homotopy(M,-2+step); }
    append(M,j,true);
  }
  for(let j=0;j<80;j++) {
    const [u,v,a,b,...e]=basis.positive[j];
    append(delta(new Map([[[u,v,a,b,15,...e].join(','),1n]]),2,1,1,0,1),6480+j,true);
  }
  return {B,D};
}
function modularSpace(rows,p) {
  const mod=x=>((x%p)+p)%p, pivots=new Map();
  function addScaled(r,s,a) {for(const [j,z]of s){const q=mod((r.get(j)||0)+a*z);if(q)r.set(j,q);else r.delete(j);}}
  function inverse(a){for(let z=1;z<p;z++)if(mod(a*z)===1)return z;throw Error('zero pivot');}
  for(const input of rows) {
    const r=new Map([...input].map(([j,z])=>[j,mod(z)]).filter(([,z])=>z));
    while(r.size) {
      const c=Math.min(...r.keys());
      if(pivots.has(c))addScaled(r,pivots.get(c),-r.get(c));
      else {const scale=inverse(r.get(c));for(const [j,z]of r)r.set(j,mod(z*scale));pivots.set(c,r);break;}
    }
  }
  const order=[...pivots.keys()].sort((a,b)=>a-b);
  return {rank:pivots.size, reduce(input) {
    const r=new Map([...input].map(([j,z])=>[j,mod(z)]).filter(([,z])=>z));
    for(const c of order)if(r.has(c))addScaled(r,pivots.get(c),-r.get(c));return r;
  }};
}
const A=initialMatrix(), {B,D}=outgoingMatrices();
const cert=JSON.parse(fs.readFileSync(path.join(root,'data/integer-relations.json')));
assert.equal(hash(JSON.stringify(A.map(sorted))),cert.negative_incoming_matrix_sha256);
assert.equal(hash(JSON.stringify(D.map(sorted))),cert.outgoing_matrix_sha256);
const current=Array.from({length:81},(_,k)=>new Map([[k,1],[5670+k,-1]]));
for(const row of current)assert.equal(multiplyRow(row,A).size,0);
let witnessTerms=0;
for(const rel of cert.relations) {
  const target=new Map(), proof=new Map();
  for(const {index,coefficient}of rel.terms)for(const [j,z]of current[index])add(target,j,coefficient*z);
  for(const {row,coefficient}of rel.integer_outgoing_row_certificate) {
    assert(row<3920); witnessTerms++;
    for(const [j,z]of B[row])add(proof,j,coefficient*z);
  }
  assert.deepEqual(sorted(target),sorted(proof));
}
const cols=cert.relation_identity_minor_columns;
assert.equal(cols.length,47);assert.equal(new Set(cols).size,47);
for(let i=0;i<47;i++) {
  const row=new Map(cert.relations[i].terms.map(t=>[t.index,t.coefficient]));
  for(let j=0;j<47;j++)assert.equal(row.get(cols[j])||0,Number(i===j));
}
assert.equal(cert.relations.filter(r=>r.terms.length===1).length,35);
const model=JSON.parse(fs.readFileSync(path.join(root,'data/model.json'))), all=[];
for(let i=0;i<15;i++)for(let b=0;b<2;b++) {
  const terms=new Map([[50+2*i+b,1]]);
  for(let a=0;a<5;a++)for(const [mon,z]of model.gamma[i][a]) {
    const e=mon.split(',').map(Number),k=e.every(x=>x===0)?0:e.indexOf(1)+1;
    add(terms,10*a+5*b+k,-z);
  }
  for(let k=0;k<81;k++) {const row=new Map([...terms].map(([j,z])=>[81*j+k,z]));assert.equal(multiplyRow(row,A).size,0);all.push(row);}
}
const exactD=exactRank(D,6560), exactCurrent=exactRank(D.concat(current),6560), exactAll=exactRank(D.concat(all),6560);
assert.equal(exactD.rank,3648);assert.equal(exactCurrent.rank-exactD.rank,34);assert.equal(exactAll.rank-exactD.rank,332);
const RD13=modularSpace(D,13),RB13=modularSpace(B,13),RD29=modularSpace(D,29);
assert.equal(RD13.rank,3648);assert.equal(RB13.rank,3488);
assert.equal(modularSpace(current.map(r=>RD13.reduce(r)),13).rank,34);
assert.equal(modularSpace(current.map(r=>RB13.reduce(r)),13).rank,34);
assert.equal(RD29.rank,3648);assert.equal(modularSpace(all.map(r=>RD29.reduce(r)),29).rank,332);
const {EA,K,T,ET}=prepare(), Ccols=[];
for(let j=0;j<80;j++){const v=Array(80).fill(0n);v[j]=1n;Ccols.push(positiveD1(v));}
const EC=new UnitEchelon(integerRows(160,Ccols),80);
assert.equal(EC.rank,50);assert.equal(K.length,10);assert.equal(ET.rank,10);
for(const t of T)assert(positiveD1(t).every(z=>z===0n));
const n=Array(6480).fill(0n),p=Array(80).fill(0n);p[7]=p[23]=p[50]=1n;
const invisible=oracle.check(oracle.sparseInput(n,p));
assert.equal(invisible.status,'nonzero_cohomology_class');assert.equal(invisible.nonmembership_witness.pairing,'-1');
assert.equal(EA.rank+ET.rank,2560);
assert.equal(6560-exactD.rank-EA.rank-ET.rank,352);
console.log(JSON.stringify({passed:true,integer_relation_count:47,integer_relation_witness_terms:witnessTerms,
  identity_minor_size:47,structural_coordinate_zeros:35,current_scalar_rank_Q:34,current_scalar_rank_F13:34,
  constant_scalar_maps:30,combined_scalar_coordinates:all.length,combined_scalar_rank_Q:332,combined_scalar_rank_F29:332,
  outgoing_rank_Q:exactD,incoming_rank_Q:2560,full_sign_cohomology_dimension_Q:352,
  current_scalar_kernel_dimension_Q:318,all_constant_scalars_kernel_dimension_Q:20,
  pure_positive_cycle_dimension:80-EC.rank,pure_positive_boundary_dimension:ET.rank,
  invisible_integer_cycle:{positive_indices:[7,23,50],coefficients:[1,1,1],status:invisible.status,separating_pairing:'-1'},
  scope:'Finite-model algebra only; no geometric numerator or residue evaluated.'},null,2));
