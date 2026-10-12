'use strict';
// Corrected HM action for a=(12), exact integer/rational coefficient model.
// This loads, but does not alter, the hash-pinned full-sign boundary oracle.
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict'),crypto=require('node:crypto'),Module=require('node:module');
const dir=__dirname;
const pins={
  'pinned-verify-hm-ext.js':'1fe4608ed77f3767691e7ef4de375fc55b052ccf26159a4aae3ec6d35fe96414',
  'full-sign-boundary-oracle.js':'29bbe778ed43ce91b52390d27fd78678879bb39c877982afb8063676b3fe1558'
};
for(const [name,hash] of Object.entries(pins)) assert.equal(crypto.createHash('sha256').update(fs.readFileSync(path.join(dir,name))).digest('hex'),hash,`Source pin ${name}`);
const filename=path.join(dir,'full-sign-boundary-oracle.js');
const source=fs.readFileSync(filename,'utf8');
const mod=new Module(filename,module);mod.filename=filename;mod.paths=module.paths;
mod._compile(source+'\nmodule.exports._operators={delta,homotopy,stateVector,vectorFromState,indexes,d,incoming,subsets,makeBasis,parseInput};\n',filename);
const O=mod.exports,{delta,homotopy,stateVector,vectorFromState,indexes,makeBasis}=O._operators;
const basis={...O.basis,degree4:makeBasis(0,4)};
const idx={...indexes,degree4:new Map(basis.degree4.map((x,i)=>[x.join(','),i]))};
function add(M,k,z){const x=(M.get(k)||0n)+z;if(x)M.set(k,x);else M.delete(k);}
function rho(M){
 const R=new Map();
 for(const [key,z] of M){const [u,v,a,b,mask,x0,x1,x2,x3]=key.split(',').map(Number);
  const m=(mask&12)|((mask&1)<<1)|((mask&2)>>1),sgn=(mask&3)===0?-1n:1n;
  add(R,[u,v,a,b,m,x1,x0,x2,x3].join(','),z*sgn);
 }return R;
}
function harmonic(vector,which){
 const out=Array(basis[which].length).fill(0n),sign=(which==='positive'||which==='outPositive')?1n:-1n;
 for(let j=0;j<vector.length;j++)if(vector[j]){const [u,v,a,b,e0,e1,e2,e3]=basis[which][j];out[idx[which].get([u,v,a,b,e1,e0,e2,e3].join(','))]+=sign*BigInt(vector[j]);}
 return out;
}
// Evaluates p(-Delta h)^u rho (-h Delta)^v i with u+v=4.
// Four minus signs cancel. All windows are permutation-invariant.
function correctionTerms(vector,which='negative'){
 assert(which==='negative'||which==='outNegative');
 const r=which==='negative'?-2:-1,target=which==='negative'?'positive':'outPositive',hi=r+2;
 let right=stateVector(vector,which,4);const terms=[];
 for(let v=1;v<=3;v++){
  right=homotopy(delta(right,r+v-1,v,4,0,hi),r+v);
  let M=rho(right);
  for(let step=v+1;step<=4;step++)M=delta(homotopy(M,r+step-1),r+step-1,step,4,0,hi);
  terms.push(vectorFromState(M,target));
 }
 return terms;
}
function correction(vector,which='negative'){
 const ts=correctionTerms(vector,which);return ts[0].map((_,i)=>ts.reduce((z,t)=>z+t[i],0n));
}
function applyDegree2(input){
 assert.equal(input.negative.length,6480);assert.equal(input.positive.length,80);
 return {negative:harmonic(input.negative,'negative'),positive:correction(input.negative).map((z,i)=>z+BigInt(input.positive[i]))};
}
function applyDegree3(input){
 assert.equal(input.negative.length,3920);assert.equal(input.positive.length,160);
 const p=harmonic(input.positive,'outPositive');
 return {negative:harmonic(input.negative,'outNegative'),positive:correction(input.negative,'outNegative').map((z,i)=>z+p[i])};
}
function unit(which,j){const v=Array(basis[which].length).fill(0n);v[j]=1n;return v;}
function equal(a,b,msg){assert.deepEqual(a,b,msg);}
function debugCheck(indices=[0,17,81,1200,2300,4050,6479]){
 const start=Date.now();let nz=0,termNonzeros=[0,0,0],max=0;
 for(const j of indices){const n=unit('negative',j),ts=correctionTerms(n),k=ts[0].map((_,i)=>ts.reduce((z,t)=>z+t[i],0n));
  ts.forEach((t,k)=>termNonzeros[k]+=t.filter(Boolean).length);nz+=k.filter(Boolean).length;max=Math.max(max,...k.map(x=>Number(x<0n?-x:x)));
  const s=harmonic(n,'negative'),dN=O.outgoingD1(n),dP=O.outgoingD5(n);
  const left=O.outgoingD5(s),dk=O.positiveD1(k),rightK=correction(dN,'outNegative'),rightP=harmonic(dP,'outPositive');
  equal(O.outgoingD1(s),harmonic(dN,'outNegative'),'negative dT=Td '+j);
  equal(left.map((z,i)=>z+dk[i]),rightK.map((z,i)=>z+rightP[i]),'positive dT=Td '+j);
 }
 return {passed:true,field:'Q (integer arithmetic)',selectedColumns:indices,correctionNonzeros:nz,correctionTermNonzeros:termNonzeros,maxCoefficient:max,milliseconds:Date.now()-start};
}
module.exports={O,basis,rho,harmonic,correctionTerms,correction,applyDegree2,applyDegree3,unit,debugCheck,pins};
if(require.main===module){
 const args=process.argv.slice(2);
 if(args[0]==='--debug')console.log(JSON.stringify(debugCheck(args.length>1?args.slice(1).map(Number):undefined),null,2));
 else if(args[0]==='--apply'&&args[1]){const x=O._operators.parseInput(JSON.parse(fs.readFileSync(args[1],'utf8'))),y=applyDegree2(x);console.log(JSON.stringify(O.sparseInput(y.negative,y.positive,x.denominator),null,2));}
 else if(args[0]==='--column') {const which=args[1]||'negative',j=Number(args[2]||0),t=correctionTerms(unit(which,j),which);console.log(JSON.stringify({which,column:j,basisKey:basis[which][j],terms:t.map(x=>x.map(String)),total:t[0].map((_,i)=>t.reduce((z,v)=>z+v[i],0n).toString())},null,2));}
 else {console.error('Usage: node generator-action.js --debug [columns...] | --column [negative|outNegative] [index] | --apply INPUT.json');process.exitCode=2;}
}
