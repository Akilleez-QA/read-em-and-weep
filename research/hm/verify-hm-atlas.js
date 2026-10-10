"use strict";
// Run with Node.js: node research/hm/verify-hm-atlas.js
// Exact integer-polynomial checks; no dependencies or floating-point evaluation.
const exact=x=>{if(!Number.isSafeInteger(x))throw Error("unsafe integer arithmetic");return x};
const Z=()=>new Map(), key=e=>e.join(",");
const constant=n=>n?new Map([["0,0,0,0",n]]):Z();
const variable=i=>{const e=[0,0,0,0];e[i]=1;return new Map([[key(e),1]])};
function add(p,q,scale=1){const r=new Map(p);for(const[k,v]of q){const n=exact((r.get(k)||0)+exact(scale*v));if(n)r.set(k,n);else r.delete(k)}return r}
function mul(p,q){const r=Z();for(const[k,v]of p)for(const[l,w]of q){const a=k.split(",").map(Number),b=l.split(",").map(Number),m=key(a.map((x,i)=>x+b[i])),n=exact((r.get(m)||0)+exact(v*w));if(n)r.set(m,n);else r.delete(m)}return r}
const neg=p=>add(Z(),p,-1),one=constant(1),vars=[0,1,2,3].map(variable);
const pairs=[[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]];
const projected=[vars.map(neg),...Array.from({length:4},(_,i)=>Array.from({length:4},(_,j)=>constant(i===j?1:0)))];
function wedge(p,q){return pairs.map(([i,j])=>add(mul(projected[p][i],projected[q][j]),mul(projected[p][j],projected[q][i]),-1))}
const alpha=Array.from({length:12},()=>Array.from({length:5},Z));
for(let a=0;a<5;a++){const plus=wedge((a+2)%5,(a+3)%5),minus=wedge((a+1)%5,(a+4)%5);for(let r=0;r<6;r++){alpha[r][a]=plus[r];alpha[r+6][a]=minus[r]}}
const S=Array.from({length:6},()=>Array(6).fill(0));for(const[i,j,v]of [[0,5,1],[1,4,-1],[2,3,1]])S[i][j]=S[j][i]=v;
const J=Array.from({length:12},()=>Array(12).fill(0));for(let i=0;i<6;i++)for(let j=0;j<6;j++){J[i][j+6]=S[i][j];J[i+6][j]=-S[i][j]}
const beta=Array.from({length:5},(_,a)=>Array.from({length:12},(_,j)=>{let p=Z();for(let r=0;r<12;r++)if(J[r][j])p=add(p,alpha[r][a],J[r][j]);return p}));
for(let i=0;i<5;i++)for(let j=0;j<5;j++){let p=Z();for(let r=0;r<12;r++)p=add(p,mul(beta[i][r],alpha[r][j]));if(p.size)throw Error("beta alpha is nonzero")}
function determinant(A){if(A.length===0)return one;let p=Z();for(let j=0;j<A.length;j++){if(!A[0][j].size)continue;const B=A.slice(1).map(row=>row.filter((_,k)=>k!==j));p=add(p,mul(A[0][j],determinant(B)),j%2?-1:1)}return p}
function equal(p,q){return add(p,q,-1).size===0}
function check(label,actual,expected){if(!equal(actual,expected))throw Error(label+" failed");console.log(label+": passed")}
const product=vars.reduce(mul,one),D=add(one,product,-1);
const I=[3,6,4,1,11],Jc=[0,2,5,7,8,9,10],P=[0,2,3,4,6];
check("primary beta determinant",determinant(beta.map(row=>I.map(i=>row[i]))),neg(D));
check("primary alpha determinant",determinant(P.map(i=>alpha[Jc[i]])),D);
const Ia=[0,1,2,3,4],Ja=[5,6,7,8,9,10,11],Pa=[0,1,2,3,5];
check("auxiliary beta determinant",determinant(beta.map(row=>Ia.map(i=>row[i]))),mul(vars[2],vars[3]));
check("auxiliary alpha determinant",determinant(Pa.map(i=>alpha[Ja[i]])),neg(mul(mul(vars[0],vars[0]),vars[2])));
console.log("beta alpha = 0: passed; all exact polynomial checks passed.");
