'use strict';
const fs=require('fs'),vm=require('vm');
const dag=JSON.parse(fs.readFileSync('hm-second-order-dag.json','utf8'));
const abs=x=>x<0n?-x:x;
function gcd(a,b){a=abs(a);b=abs(b);while(b){[a,b]=[b,a%b]}return a}
function rat(a,b=1n){if(b===0n)throw Error('zero denominator');if(!a)return[0n,1n];if(b<0n){a=-a;b=-b}const g=gcd(a,b);return[a/g,b/g]}
const add=(a,b)=>rat(a[0]*b[1]+b[0]*a[1],a[1]*b[1]);
const mul=(a,b)=>rat(a[0]*b[0],a[1]*b[1]);
const values=[],point=[2n,3n,4n,5n];
for(const n of dag.nodes){switch(n[0]){case 'const': values.push(rat(BigInt(n[1]),BigInt(n[2]||1)));break;case 'var':values.push(rat(point[n[1]]));break;case 'add':values.push(add(values[n[1]],values[n[2]]));break;case 'mul':values.push(mul(values[n[1]],values[n[2]]));break;case 'inv':values.push(rat(values[n[1]][1],values[n[1]][0]));break;default:throw Error('unknown node '+JSON.stringify(n));}}
const context=vm.createContext({console:{log:()=>{}}});
vm.runInContext(fs.readFileSync('verify-hm-end-transfer.js','utf8'),context);
const expected=vm.runInContext('(()=>{const G=mv(D.g[0][5]),GI=[[G[1][1],neg(G[0][1])],[neg(G[1][0]),G[0][0]]];return mm(GI,crossResidual(D,0,1,5));})()',context);
for(let i=0;i<2;i++)for(let j=0;j<2;j++){const a=values[dag.normalizedRowMatrix[i][j]],b=expected[i][j];if(a[0]*b[1]!==b[0]*a[1])throw Error('mismatch '+i+','+j);}
console.log(JSON.stringify({dagNodes:dag.nodes.length,matrixEntries:4,matches:true,point:['2','3','4','5'],charts:[0,1,5]}));
