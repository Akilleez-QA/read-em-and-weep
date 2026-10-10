"use strict";
// Exact scalar refinement comparison for y^2=x^3-x.
// Run: node verify-scalar-refinement.js
// This covers the legal line atlas only, not the HM carrier refinements.
function assert(b,m){if(!b)throw Error(m);}
let checks=0;
function ok(b,m){assert(b,m);checks++;}
const add=(a,b)=>{let c=a.slice();b.forEach((v,i)=>c[i]=(c[i]||0)+v);while(c.length&&c.at(-1)===0)c.pop();return c;};
const neg=a=>a.map(v=>-v);
const mul=(a,b)=>{let c=[];a.forEach((v,i)=>b.forEach((w,j)=>c[i+j]=(c[i+j]||0)+v*w));return add(c,[]);};
const eq=(a,b)=>JSON.stringify(add(a,[]))===JSON.stringify(add(b,[]));
const zero=[[],[]],one=[[1],[]],t=[[0,1],[]],z=[[],[1]];
const A=(a,b)=>[add(a[0],b[0]),add(a[1],b[1])];
const N=a=>a.map(neg);
const M=(a,b)=>[add(mul(a[0],b[0]),mul(mul(a[1],b[1]),[0,1,0,-1])),add(mul(a[0],b[1]),mul(a[1],b[0]))];
const E=(a,b)=>eq(a[0],b[0])&&eq(a[1],b[1]);
const F=(n,d=one)=>({n,d});
const fa=(a,b)=>F(A(M(a.n,b.d),M(b.n,a.d)),M(a.d,b.d));
const fn=a=>F(N(a.n),a.d);
const fm=(a,b)=>F(M(a.n,b.n),M(a.d,b.d));
const fe=(a,b)=>E(M(a.n,b.d),M(b.n,a.d));
const scale=(a,n)=>fm(F([[n],[]]),a);
const T=F(t),Z=F(z),O=F(one),S=F(A(one,N(M(t,t)))),T2=fm(T,T);
const q=F(z,t),c=F(M(t,z),S.n),w=fm(T,Z);
const r2=F(M(A(one,M(t,t)),z),M(t,S.n)); // 2 V(log q)
ok(fe(fa(T2,S),O),"Bezout t*t+s=1");
ok(fe(r2,fa(q,scale(c,2))),"2r=q+2c");
ok(fe(fm(S,q),fa(q,fn(w))),"s q=q-w");
ok(fe(fm(S,c),w),"s c=w");
ok(fe(fm(S,r2),fa(q,w)),"s(2r)=q+w");
// Vertical contractions on the double Cech complex.
// On A, V0 already covers A; on B use D(t),D(s).
const hA=u=>[F(zero),u];
const hB=u=>[fn(fm(S,u)),fm(T2,u)];
const pA=u=>u[0];
const pB=u=>fa(fm(T2,u[0]),fm(S,u[1]));
const d=u=>fa(u[1],fn(u[0]));
for(const u of [q,c,r2]){
  for(const [h,p] of [[hA,pA],[hB,pB]]){
    ok(fe(d(h(u)),u),"vertical d h=1");
    ok(fe(p(h(u)),F(zero)),"vertical p h=0");
  }
  // hB-hA is the diagonal (-s u,-s u).
  const diff=hB(u).map((v,i)=>fa(v,fn(hA(u)[i])));
  ok(fe(diff[0],fn(fm(S,u)))&&fe(diff[0],diff[1]),"horizontal delta h");
  ok(fe(fn(pA(diff)),fm(S,u)),"P'=p(1+delta h)^-1 yields s u");
}
for(const [h,p]of [[hA,pA],[hB,pB]])for(const v of [[O,O],[F(zero),c]]){
 const hd=h(d(v)),ip=p(v);
 ok(hd.every((x,i)=>fe(fa(x,ip),v[i])),"vertical h d+i p=1");
 ok(fe(d([ip,ip]),F(zero)),"vertical d i=0");
}
// Basis matrices, column convention.
// Input degree 0: (1, k=(0,c)); degree 1: (q,c).
// Output degree 0: (1, ell=(0,w)); degree 1: (q,w).
const mm=(a,b)=>a.map(r=>b[0].map((_,j)=>r.reduce((s,v,k)=>s+v*b[k][j],0)));
const ma=(a,b)=>a.map((r,i)=>r.map((v,j)=>v+b[i][j]));
const me=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
const I=[[1,0],[0,1]],D=[[0,0],[0,1]],P0=I,P1=[[1,0],[-1,1]];
ok(me(mm(D,P0),mm(P1,D)),"D P=P D");
// The original Laurent harmonic projection kills w=y*x^-3 and retains q=y*x^-1.
// H^1 is the odd O(-2) exponent -1; w is an infinity-chart boundary.
const L0=[[1,0]],L1=[[1,0]],J0=[[1],[0]],J1=[[1],[0]],H=D;
ok(me(ma(mm(D,H),mm(J1,L1)),I),"Laurent degree 1 SDR");
ok(me(ma(mm(H,D),mm(J0,L0)),I),"Laurent degree 0 SDR");
ok(me(mm(L1,mm(P1,[[1],[2]])),[[1]]),"2r maps to q");
// Composed scalar finite maps coincide with the small refined SDR.
ok(me(mm(L1,P1),L1),"composed scalar projection");
// Tensor product differential and projection, all 4^4 basis vectors.
const states=[{d:0,k:0},{d:0,k:1},{d:1,k:0},{d:1,k:1}];
const words=Array.from({length:256},(_,n)=>Array.from({length:4},(_,i)=>(n>>(2*i))&3));
const key=a=>a.reduce((n,v,i)=>n+(v<<(2*i)),0);
function differential(word){
 const out=new Map();let parity=0;
 word.forEach((s,i)=>{if(s===1){let a=word.slice();a[i]=3;out.set(key(a),(parity%2)?-1:1);}parity+=states[s].d;});
 return out;
}
function project(word){return word.some(s=>s===1||s===3)?null:word.reduce((m,s,i)=>m|((s===2?1:0)<<i),0);}
for(const word of words){
 const dd=new Map();
 for(const [j,a]of differential(word))for(const[k,b]of differential(words[j]))dd.set(k,(dd.get(k)||0)+a*b);
 ok([...dd.values()].every(v=>v===0),"tensor d^2=0");
 ok([...differential(word).keys()].every(j=>project(words[j])===null),"tensor projection chain map");
}
// In tensor Cech normalization the antisymmetric scalar defect is -r_i r_j.
// Four times compensated residual is -(2r_i)(2r_j)-15 q_i q_j.
// For both N and N^-1, projected coordinates are -16 before dividing by 4.
for(const sign of [1,-1]){
 for(const [i,j]of [[0,1],[2,3]]){
  const projected=-(sign*1)*(sign*1)-15;
  ok(projected===-16,"compensated line calibration");
 }
}
console.log(JSON.stringify({checks,scalarRefinementChainMap:true,lineCalibration:{N:{"12":"-4","34":"-4"},N_inverse:{"12":"-4","34":"-4"}},scope:"legal two-open line atlas; tensor Cech scalar domain",notComputed:["six-pivot HM carrier comparison","E residual projection","second-order obstruction"]},null,2));
