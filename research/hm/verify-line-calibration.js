"use strict";
// Run: node research/hm/verify-line-calibration.js
// Universal Cech identity. All denominators are cleared by multiplying by 8.
const nvars=10;
const zero=()=>new Map(), one=()=>new Map([[Array(nvars).fill(0).join(","),1]]);
function variable(i){const e=Array(nvars).fill(0);e[i]=1;return new Map([[e.join(","),1]])}
function add(p,q,s=1){const r=new Map(p);for(const[k,v]of q){const n=(r.get(k)||0)+s*v;if(!Number.isSafeInteger(n))throw Error("unsafe integer");if(n)r.set(k,n);else r.delete(k)}return r}
function scale(p,s){return add(zero(),p,s)}
function mul(p,q){const r=zero();for(const[k,v]of p)for(const[l,w]of q){const a=k.split(",").map(Number),b=l.split(",").map(Number),m=a.map((x,i)=>x+b[i]).join(","),n=(r.get(m)||0)+v*w;if(!Number.isSafeInteger(n))throw Error("unsafe integer");if(n)r.set(m,n);else r.delete(m)}return r}
const q1=[[zero(),variable(0),add(variable(0),variable(1))],[zero(),zero(),variable(1)]];
const q2=[[zero(),variable(2),add(variable(2),variable(3))],[zero(),zero(),variable(3)]];
const c1=[variable(4),variable(5),variable(6)],c2=[variable(7),variable(8),variable(9)];
const R=(q,c,i,j)=>add(q[i][j],scale(add(c[j],c[i],-1),2));
function H(i,j){return add(add(scale(mul(c1[i],R(q2,c2,i,j)),4),scale(mul(q1[i][j],c2[j]),-4)),mul(R(q1,c1,i,j),R(q2,c2,i,j)))}
const deltaH=add(add(H(1,2),H(0,2),-1),H(0,1));
const eightMu=add(mul(R(q2,c2,0,1),R(q1,c1,1,2)),mul(R(q1,c1,0,1),R(q2,c2,1,2)),-1);
const residual=add(add(eightMu,scale(mul(q1[0][1],q2[1][2]),2)),deltaH);
if(residual.size)throw Error("line calibration Cech identity failed");
console.log("8(mu + q1 cup q2/4 + delta h)=0: passed.");
console.log("With b=15(q1 cup q2)/4, mu-b is cohomologous to -4(q1 cup q2).");
console.log("Apply independently to pairs (1,2) and (3,4). The inverse line has the same quadratic defect.");
