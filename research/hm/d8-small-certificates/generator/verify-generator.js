'use strict';
const g=require('./generator-action.js'),fs=require('node:fs'),assert=require('node:assert/strict'),crypto=require('node:crypto');
const {O,basis}=g,{delta,stateVector}=O._operators;
const start=Date.now();
function add(M,k,z){const v=(M.get(k)||0n)+z;if(v)M.set(k,v);else M.delete(k);}
function sparse(v){return new Map(v.flatMap((z,i)=>z?[[i,z]]:[]));}
function vec(M,n){const v=Array(n).fill(0n);for(const [i,z]of M)v[i]=z;return v;}
function apply(cols,v){const w=new Map();for(const [j,z]of v)for(const [i,a]of cols[j])add(w,i,a*z);return w;}
function eq(a,b,msg){assert.equal(a.size,b.size,msg);for(const [i,z]of a)assert.equal(z,b.get(i),msg+' row '+i);}
function sum(a,b){const x=new Map(a);for(const [i,z]of b)add(x,i,z);return x;}
function columnBuilder(n,f,label){const cols=[];for(let j=0;j<n;j++){cols.push(sparse(f(j)));if(j&&j%1000===0)console.error(`${label}: ${j}/${n}, ${Date.now()-start}ms`);}return cols;}
function stat(cols){return {rows:1+Math.max(-1,...cols.flatMap(c=>[...c.keys()])),columns:cols.length,nonzeroColumns:cols.filter(c=>c.size).length,nonzeros:cols.reduce((n,c)=>n+c.size,0),maxCoefficient:cols.reduce((n,c)=>[...c.values()].reduce((n,z)=>Math.max(n,Number(z<0n?-z:z)),n),0)};}
function permutation(which){return basis[which].map((_,j)=>sparse(g.harmonic(g.unit(which,j),which)));}
function hash(x){return crypto.createHash('sha256').update(JSON.stringify(x)).digest('hex');}
function encode(cols){return cols.flatMap((c,j)=>[...c].sort((a,b)=>a[0]-b[0]).map(([i,z])=>[i,j,z.toString()]));}
function negative3(v){
 const M=delta(stateVector(v,'outNegative',4),-1,1,1,-1,-1),out=Array(354).fill(0n),ix=new Map(basis.degree4.map((b,i)=>[b.join(','),i]));
 for(const [key,z]of M){const [u,v,a,b,mask,...e]=key.split(',').map(Number);assert.equal(mask,0);const j=ix.get([u,v,a,b,...e].join(','));assert.notEqual(j,undefined);out[j]+=z;}return out;
}
const S1=permutation('source'),S2=permutation('negative'),S3=permutation('outNegative'),S4=permutation('degree4'),SP2=permutation('positive'),SP3=permutation('outPositive');
for(const S of [S1,S2,S3,S4,SP2,SP3])for(let j=0;j<S.length;j++)eq(apply(S,S[j]),new Map([[j,1n]]),'harmonic involution col'+j);
const termCounts={degree2:[0,0,0],degree3:[0,0,0]};
function buildK(which,label){return columnBuilder(basis[which].length,j=>{const ts=g.correctionTerms(g.unit(which,j),which);ts.forEach((v,i)=>termCounts[label][i]+=v.filter(Boolean).length);return ts[0].map((_,i)=>ts.reduce((z,t)=>z+t[i],0n));},label);}
const K2=buildK('negative','degree2'),K3=buildK('outNegative','degree3');
console.error('Building pinned differential blocks');
const A=columnBuilder(2560,j=>O.sourceD1(g.unit('source',j)),'D1 negative'),B=columnBuilder(2560,j=>O.sourceD5(g.unit('source',j)),'D1 positive');
const C=columnBuilder(6480,j=>O.outgoingD1(g.unit('negative',j)),'D2 negative'),E=columnBuilder(6480,j=>O.outgoingD5(g.unit('negative',j)),'D2 positive');
const F=columnBuilder(80,j=>O.positiveD1(g.unit('positive',j)),'D2 positive-source');
const G=columnBuilder(3920,j=>negative3(g.unit('outNegative',j)),'D3 negative');
// In each degree these verify every source basis vector and every target row.
for(let j=0;j<2560;j++){
 eq(apply(S2,A[j]),apply(A,S1[j]),'dT=Td degree1 negative col'+j);
 eq(sum(apply(K2,A[j]),apply(SP2,B[j])),apply(B,S1[j]),'dT=Td degree1 positive col'+j);
 eq(apply(C,A[j]),new Map(),'d2=0 degree1 negative col'+j);
 eq(sum(apply(E,A[j]),apply(F,B[j])),new Map(),'d2=0 degree1 positive col'+j);
}
for(let j=0;j<6480;j++){
 eq(apply(C,S2[j]),apply(S3,C[j]),'dT=Td degree2 negative col'+j);
 eq(sum(apply(E,S2[j]),apply(F,K2[j])),sum(apply(K3,C[j]),apply(SP3,E[j])),'dT=Td degree2 positive col'+j);
 eq(apply(G,C[j]),new Map(),'d2=0 degree2 col'+j);
}
for(let j=0;j<80;j++)eq(apply(F,SP2[j]),apply(SP3,F[j]),'dT=Td degree2 positive-source col'+j);
for(let j=0;j<3920;j++)eq(apply(G,S3[j]),apply(S4,G[j]),'dT=Td degree3 col'+j);
// Optional observed stronger property for this one adjacent generator only.
for(let j=0;j<6480;j++)eq(sum(apply(K2,S2[j]),apply(SP2,K2[j])),new Map(),'T_a^2=1 degree2 col'+j);
for(let j=0;j<3920;j++)eq(sum(apply(K3,S3[j]),apply(SP3,K3[j])),new Map(),'T_a^2=1 degree3 col'+j);
const matrices={basis:O.BASIS,source_commit:O.SOURCE_COMMIT,generator:[1,0,2,3],coefficient_ring:'Z',coefficient_field:'Q',entry_format:['target_row','source_column','integer_coefficient'],degree2:{shape:[80,6480],entries:encode(K2)},degree3:{shape:[160,3920],entries:encode(K3)}};
const result={passed:true,source_pins:g.pins,oracle_repository_commit:'a100f4e0be453d6e182320b792359f8a04e32b4d',oracle_git_blob:'8f534fd7a074e333fa031a6d8c51b864faf76d42',coefficient_ring:'Z',coefficient_field:'Q',generator:'a=(12)',basis:O.BASIS,fullSignDimensions:[0,2560,6560,4080,354],degree2Correction:{...stat(K2),rows:80},degree3Correction:{...stat(K3),rows:160},termNonzerosInOrder_v1_v2_v3:termCounts,
 chainIdentity:{exhaustive:true,degree1Columns:2560,degree2Columns:6560,degree3Columns:4080,degree0And4:'zero outgoing differential'},differentialSquare:{exhaustive:true,degree1Columns:2560,degree2Columns:6560},
 involution:{exhaustive:true,allFiniteDegrees:true,qualification:'Observed for a=(12); do not infer strict relations for other generators.'},matrices_sha256:hash(matrices),milliseconds:Date.now()-start};
fs.writeFileSync(__dirname+'/generator-a-matrices.json',JSON.stringify(matrices,null,2)+'\n');fs.writeFileSync(__dirname+'/certificate.json',JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify(result,null,2));
