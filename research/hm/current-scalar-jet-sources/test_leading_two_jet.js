'use strict';
const assert=require('assert'),path=require('path');
const {leadingTwo}=require('./leading_two_jet');
const {makeRing}=require(path.resolve(process.argv[2]||path.join(__dirname,'../current-scalar-numerator/tagged_ring.js')));
const trim=p=>{while(p.length>1&&p[p.length-1]===0n)p.pop();return p};
const plus=(a,b)=>trim(Array.from({length:Math.max(a.length,b.length)},(_,i)=>(a[i]||0n)+(b[i]||0n)));
const neg=a=>a.map(v=>-v);
const mul=(a,b)=>{const c=Array(a.length+b.length-1).fill(0n);for(let i=0;i<a.length;i++)for(let j=0;j<b.length;j++)c[i+j]+=a[i]*b[j];return trim(c)};
const power=(a,e)=>{let p=[1n];for(let k=0;k<e;k++)p=mul(p,a);return p};
function concreteTags(xs){
 const E=[[1n],[0n],[0n],[0n],[1n]];
 E[4]=xs.reduce(mul,[1n]);
 for(let i=0;i<4;i++)E[1]=plus(E[1],xs[i]);
 for(let i=0;i<4;i++)for(let j=i+1;j<4;j++)E[2]=plus(E[2],mul(xs[i],xs[j]));
 for(let i=0;i<4;i++)for(let j=i+1;j<4;j++)for(let k=j+1;k<4;k++)E[3]=plus(E[3],mul(mul(xs[i],xs[j]),xs[k]));
 const F=[neg(E.slice(1).reduce(mul,[1n]))];
 for(let j=1;j<5;j++)F.push(plus(power(E[j],4),neg(E.filter((_,k)=>k>0&&k!==j).reduce(mul,[1n]))));
 return [...xs,...xs.map(x=>plus(power(x,2),[-1n])),...E.slice(1,4),...F];
}
function evaluate(D,tags){
 const nodes=D.nodes.map((n,i)=>null);
 for(let i=0;i<D.nodes.length;i++){
  const n=D.nodes[i];
  if(n[0]==='const'){assert.equal(n[2],'1');nodes[i]=[BigInt(n[1])]}
  else if(n[0]==='tags')nodes[i]=n.slice(1).reduce((p,e,j)=>mul(p,power(tags[j],e)),[1n]);
  else if(n[0]==='add')nodes[i]=plus(nodes[n[1]],nodes[n[2]]);
  else if(n[0]==='mul')nodes[i]=mul(nodes[n[1]],nodes[n[2]]);
  else throw Error('Unexpected test node');
 }
 return D.outputs.map(o=>o.powers.reduce((p,e,j)=>mul(p,power(tags[j],e)),nodes[o.numerator]));
}
let checks=0;
for(let axis=0;axis<4;axis++){
 const R=makeRing(),{add,mul,pow,neg}=R;
 const other=(axis+1)%4,x=R.x[axis],y=R.x[other];
 const samples=[...Array.from({length:16},(_,i)=>R.tag(i)),
  mul(add(x,y),add(x,mul(R.fromBigInt(2),y))),
  add(add(pow(add(x,y),2),neg(pow(x,2))),neg(mul(R.fromBigInt(2),mul(x,y)))),
  mul(pow(R.tag(11),2),add(R.tag(8),R.tag(9))),
  add(pow(x,7),pow(x,5))];
 const D=R.pruneExport(samples);Object.assign(D,{coefficientField:'Q',tagNames:[],tagPolynomials:[]});
 const J=leadingTwo(D,axis,makeRing);
 const xs=[2n,3n,5n,7n].map((v,i)=>i===axis?[0n,1n]:[v]);
 const expected=evaluate(D,concreteTags(xs));
 const actual=evaluate(J,concreteTags(xs.map((v,i)=>i===axis?[0n]:v)));
 for(let i=0;i<samples.length;i++){
  const degree=J.rootDegreeBounds[i];
  assert.deepEqual(actual[2*i],[expected[i][degree]||0n]);
  assert.deepEqual(actual[2*i+1],[expected[i][degree-1]||0n]);checks+=2;
 }
 // Cancellation must not lower the syntactic degree enclosure.
 assert.equal(J.rootDegreeBounds[17],2);
 assert.deepEqual(actual[34],[0n]);
 assert.deepEqual(actual[35],[0n]);
 const bad=JSON.parse(JSON.stringify(D));bad.outputs[0].powers[0]=-1;
 assert.throws(()=>leadingTwo(bad,axis,makeRing),/Rational input forbidden/);
}
assert.throws(()=>leadingTwo({nodes:[],outputs:[]},4,makeRing),/Axis/);
console.log(JSON.stringify({status:'PASS',exactCoefficientChecks:checks,axes:4,cancellationBoundPreserved:true,negativeExponentRejected:true}));
