'use strict';
// Exact rational arithmetic and the actual constructor's scalar contraction.
const assert=require('assert/strict'),fs=require('fs'),vm=require('vm');
const {makeRing}=require('./tagged_ring');
const {maskBasis}=require('./weighted_mask_moments');
const R=makeRing();
function fraction(a){assert(a.e.every(v=>v===0));const n=R.nodes[a.n];assert.equal(n[0],'const');return n.slice(1);}
assert.deepEqual(fraction(R.add(R.rational(1,3),R.rational(1,6))),['1','2']);
assert.deepEqual(fraction(R.mul(R.rational(-7,11),R.rational(22,21))),['-2','3']);
assert.deepEqual(fraction(R.inv(R.rational(-2,3))),['-3','2']);
assert.throws(()=>R.inv(R.zero),/zero constant denominator/);
assert.throws(()=>R.inv(R.add(R.x[0],R.one)),/exactly factored denominators/);
assert.deepEqual(R.mul(R.pow(R.x[0],3),R.inv(R.x[0])).e,[2,...Array(15).fill(0)]);
const source=fs.readFileSync(require.resolve('./build_local_representative.js'),'utf8');
const start=source.indexOf('let scalar=zero;'),end=source.indexOf('const orders=',start);
assert(start>=0&&end>start);
const contraction=source.slice(start,end);
// The production expression, including its transpose and explicit minus, is
// executed unchanged on an independent BigInt ring. All four matrix basis
// entries are distinguished by nonsymmetric prefactors.
function testContraction(code){
 for(let r=0;r<2;r++)for(let c=0;c<2;c++){
  let minusCalls=0;const M=[[0n,0n],[0n,0n]];M[c][r]=1n;
  const context={zero:0n,a:[2n,3n],b:[5n,7n],M,
    add:(x,y)=>x+y,mul:(x,y)=>x*y,neg:x=>{minusCalls++;return -x}};
  vm.runInNewContext(code+'\nresult=scalar;',context);
  assert.equal(context.result,-context.a[r]*context.b[c]);
  assert.equal(minusCalls,1,'Exactly one J2 minus in the scalar contraction');
 }
}
testContraction(contraction);
assert.throws(()=>testContraction(contraction.replace('scalar=neg(scalar);','scalar=scalar;')));
assert.throws(()=>testContraction(contraction.replace('scalar=neg(scalar);','scalar=neg(neg(scalar));')));
assert.equal(Array.from({length:256},(_,i)=>maskBasis(i)).length,256);
console.log(JSON.stringify({status:'PASS',exactRationalFixtures:6,scalarMatrixBasisFixtures:4,
  scalarJ2MinusCallsPerFixture:1,rejectedMissingOrDoubleMinus:2,actualConstructorContractionTested:true}));
