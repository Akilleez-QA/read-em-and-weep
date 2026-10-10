"use strict";
const MODEL=require('../data/model.json');


// Eighteen pole channels: two per primary carrier, four for the
// auxiliary carrier, then one legal-line channel per coordinate.
// Constants remain exact; all other scalars are monotone upper bounds.
const nodes=[],cache=new Map();
function node(v){const k=JSON.stringify(v);if(cache.has(k))return cache.get(k);const i=nodes.length;nodes.push(v);cache.set(k,i);return i;}
function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){const t=a%b;a=b;b=t;}return a;}
function R(n,d=1n){if(typeof n==='string')return B(Array(18).fill(0));if(!n)d=1n;if(d<0n){n=-n;d=-d;}const g=gcd(n,d);return node(['const',String(n/g),String(d/g)]);}
const z=R(0n),o=R(1n),minus=R(-1n),isconst=i=>nodes[i][0]==='const';
const B=b=>node(['bound',...b]),bp=i=>isconst(i)?Array(18).fill(0):nodes[i].slice(1);
function add(a,b){if(a===z)return b;if(b===z)return a;if(isconst(a)&&isconst(b)){const A=nodes[a],C=nodes[b];return R(BigInt(A[1])*BigInt(C[2])+BigInt(C[1])*BigInt(A[2]),BigInt(A[2])*BigInt(C[2]));}const p=bp(a),q=bp(b);return B(p.map((v,i)=>Math.max(v,q[i])));}
function mul(a,b){if(a===z||b===z)return z;if(a===o)return b;if(b===o)return a;if(isconst(a)&&isconst(b)){const A=nodes[a],C=nodes[b];return R(BigInt(A[1])*BigInt(C[1]),BigInt(A[2])*BigInt(C[2]));}const p=bp(a),q=bp(b);return B(p.map((v,i)=>v+q[i]));}
const neg=a=>mul(minus,a),sub=(a,b)=>add(a,neg(b));
function div(a,b){if(a===z)return z;if(!isconst(b)||nodes[b][1]==='0')throw Error('Uncertified inverse');return mul(a,R(BigInt(nodes[b][2]),BigInt(nodes[b][1])));}
const mat=(r,c)=>Array.from({length:r},()=>Array(c).fill(z)),tr=A=>A[0].map((_,j)=>A.map(r=>r[j])),mm=(A,B)=>A.map(row=>B[0].map((_,j)=>row.reduce((s,x,k)=>add(s,mul(x,B[k][j])),z))),ma=(A,B)=>A.map((row,i)=>row.map((x,j)=>add(x,B[i][j]))),ms=(A,B)=>A.map((row,i)=>row.map((x,j)=>sub(x,B[i][j]))),scale=(A,s)=>A.map(row=>row.map(x=>mul(x,s))),trace=A=>A.reduce((s,row,i)=>add(s,row[i]),z);
const masks=[0,1,2,4,8,3,5,9,6,10,12], jc=x=>{const a=Array(16).fill(z);a[0]=x;return a}, jz=jc(z),jo=jc(o);
const ja=(a,b)=>a.map((x,i)=>add(x,b[i])),jn=a=>a.map(neg),js=(a,b)=>ja(a,jn(b));
function jm(a,b){const c=Array(16).fill(z);for(const m of masks)for(let s=m;;s=(s-1)&m){c[m]=add(c[m],mul(a[s],b[m^s]));if(!s)break}return c}
function ji(a){const c=Array(16).fill(z);c[0]=div(o,a[0]);for(const m of masks.slice(1)){let s=z;for(let t=m;t;t=(t-1)&m)s=add(s,mul(a[t],c[m^t]));c[m]=neg(div(s,a[0]))}return c}
const jd=(a,b)=>jm(a,ji(b)),jder=(a,i)=>a.map((_,m)=>(m&(1<<i))?z:a[m|(1<<i)]),jscale=(a,s)=>a.map(x=>mul(x,s));
function jp(a,n){let b=jo;for(let i=0;i<n;i++)b=jm(b,a);return b}
function poly(p,vars){let v=jz;for(const[k,c]of p){const e=k.split(",").map(Number);let t=jc(R(BigInt(c)));for(let i=0;i<4;i++)t=jm(t,jp(vars[i],e[i]));v=ja(v,t)}return v}
const zm=(r,c)=>Array.from({length:r},()=>Array(c).fill(jz)),mt=A=>A[0].map((_,j)=>A.map(row=>row[j])),madd=(A,B)=>A.map((row,i)=>row.map((x,j)=>ja(x,B[i][j]))),mneg=A=>A.map(row=>row.map(jn)),msub=(A,B)=>madd(A,mneg(B)),mtimes=(A,B)=>A.map(row=>B[0].map((_,j)=>row.reduce((s,x,k)=>ja(s,jm(x,B[k][j])),jz))),msc=(A,r)=>A.map(row=>row.map(x=>jscale(x,r))),md=(A,a)=>A.map(row=>row.map(x=>jder(x,a))),mv=A=>A.map(row=>row.map(x=>x[0])),mtrace=A=>A.reduce((s,row,i)=>ja(s,row[i]),jz);
const horiz=(...A)=>A[0].map((_,r)=>A.flatMap(M=>M[r])),vert=(...A)=>A.flat();

const ENTRY_SEEDS=require('../data/divisor-seeds.json');
const pop=m=>m.toString(2).replaceAll('0','').length;
function poleJet(carrier,line=[0,0,0,0],derivativeCarrier=true,owner=0){return Array.from({length:16},(_,m)=>{if(!masks.includes(m))return z;const c=Array(14).fill(0),v=Array.isArray(carrier)?carrier:[carrier,0];for(let i=0;i<v.length;i++)c[(owner<5?2*owner:10)+i]=v[i]+(derivativeCarrier&&v[i]>0?pop(m):0);return B([...c,...line]);});}
function primitive(A,cost,polynomial=false){return A.map(row=>row.map(p=>p.length?poleJet(cost,[0,0,0,0],!polynomial):jz));}
function entryPrimitive(A,costs,owner){return A.map((row,i)=>row.map((p,k)=>p.length?poleJet(costs[i][k],[0,0,0,0],costs[i][k].some(x=>x>0),owner):jz));}
function joinScalars(ids){if(ids.every(i=>i===ids[0]))return ids[0];return B(ids.reduce((r,i)=>r.map((x,j)=>Math.max(x,bp(i)[j])),Array(18).fill(0)));}
function deepJoin(values){return typeof values[0]==='number'?joinScalars(values):values[0].map((_,j)=>deepJoin(values.map(v=>v[j])));}
function build2(xs,ids,join=true){
const gamma=primitive(MODEL.gamma,0,true),delta=primitive(MODEL.delta,0,true),ev=primitive(MODEL.ev,0,true),charts=[];
for(const id of ids){const c=MODEL.charts[id],I=entryPrimitive(c.I,ENTRY_SEEDS[id].I,id),P=entryPrimitive(c.P,ENTRY_SEEDS[id].P,id),H0=entryPrimitive(c.H0,ENTRY_SEEDS[id].H0,id),H1=entryPrimitive(c.H1,ENTRY_SEEDS[id].H1,id),j=c.pivot,W=zm(10,8),eta=zm(10,2),L=zm(8,10);
for(let h=0;h<2;h++){eta[h*5+j][h]=poleJet(1,undefined,true,id);for(let k=1;k<5;k++){const kk=(j+k)%5,col=h*4+k-1;W[h*5+kk][col]=jo;W[h*5+j][col]=poleJet(1,undefined,true,id);L[col][h*5+kk]=jo;}}
const U0=horiz(gamma,I,mtimes(H1,W)),Q0=vert(H0,P,mtimes(L,delta)),U1=horiz(W,eta),Q1=vert(L,ev);
charts.push({I,P,H0,H1,eta,U0,Q0,U1,Q1});
}
const joined=Object.fromEntries(Object.keys(charts[0]).map(k=>[k,deepJoin(charts.map(c=>c[k]))]));
return {charts:join?ids.map(()=>joined):charts,gamma,delta,ev};}
function lineJet(a,order=1){const r=Array(16).fill(z);for(const m of [0,1<<a]){const l=[0,0,0,0];l[a]=order+pop(m);r[m]=B([...Array(14).fill(0),...l]);}return r;}
function crossResidual(D,i,j,k){const {g,u12:A,u34:B}=D,mu=(F,G,a,b)=>scale(ms(mm(mv(md(F,a)),mv(md(G,b))),mm(mv(md(F,b)),mv(md(G,a)))),R(1n,2n));
let R0=ma(mm(mv(A[j][k]),mv(B[i][j])),mm(mv(B[j][k]),mv(A[i][j])));
for(const[F,G,a,b]of [[B[j][k],g[i][j],0,1],[A[j][k],g[i][j],2,3],[g[j][k],B[i][j],0,1],[g[j][k],A[i][j],2,3]])R0=ma(R0,mu(F,G,a,b));
const dd=(G,a,b)=>G.map(row=>row.map(x=>x[(1<<a)|(1<<b)]));
const cross=ma(ms(ms(mm(dd(g[j][k],0,2),dd(g[i][j],1,3)),mm(dd(g[j][k],0,3),dd(g[i][j],1,2))),mm(dd(g[j][k],1,2),dd(g[i][j],0,3))),mm(dd(g[j][k],1,3),dd(g[i][j],0,2)));
return ma(R0,scale(cross,R(1n,4n)))}

function globalBuild2(xs,vertices){
const ids=[0,1,2,3,4],base=build2(xs,ids),X=xs.map((x,i)=>{const a=jc(R(x));a[1<<i]=o;return a}),rf=X.map((x,a)=>lineJet(a)),ga=X.map((x,a)=>lineJet(a));
const charts=vertices.map(([id,mask])=>{const c=base.charts[ids.indexOf(id)],nu=Array(16).fill(z);for(const m of masks){let t=o;for(let a=0;a<4;a++)if(m&(1<<a))t=mul(t,(mask&(1<<a))?rf[a][0]:z);nu[m]=t}
const nu2=jm(nu,nu),nui2=ji(nu2),w0=[...Array(5).fill(nui2),jo,nui2,...Array(8).fill(nu2)],w1=[...Array(8).fill(jo),nu2,nu2];
const U0=c.U0.map(row=>row.map((x,i)=>jm(x,w0[i]))),Q0=c.Q0.map((row,i)=>row.map(x=>jd(x,w0[i]))),U1=c.U1.map(row=>row.map((x,i)=>jm(x,w1[i]))),Q1=c.Q1.map((row,i)=>row.map(x=>jd(x,w1[i])));
const blocks=[];for(let a=0;a<4;a++){const gamma=mask&(1<<a)?ga[a]:jz,raw0=mneg(mtimes(md(U0,a),Q0)),raw1=mneg(mtimes(md(U1,a),Q1)),out=[];for(const[dim,k,sign,BB]of [[5,-1,-1,null],[15,1,1,raw0],[10,3,-1,raw1],[2,5,1,null]]){const B=BB||zm(dim,dim);for(let r=0;r<dim;r++)B[r][r]=js(B[r][r],jscale(gamma,R(BigInt(k))));out.push({B,k,sign})}blocks.push(out)}
return{...c,mask,nu,blocks}});
const n=charts.length,g=Array.from({length:n},(_,i)=>Array.from({length:n},(_,j)=>{const core=mtimes(charts[i].P,charts[j].I),li=[ji(charts[i].nu),charts[i].nu],rj=[charts[j].nu,ji(charts[j].nu)];return mt(core.map((row,a)=>row.map((x,b)=>jm(jm(li[a],x),rj[b]))))}));
const q=(i,j,a)=>lineJet(a);
function first(a,b){return Array.from({length:n},(_,i)=>Array.from({length:n},(_,j)=>{let sum=jz;const ta=jscale(q(i,j,a),R(1n,2n)),tb=jscale(q(i,j,b),R(1n,2n));
for(let k=0;k<4;k++){const Ai=charts[i].blocks[a][k],Bi=charts[i].blocks[b][k],Aj=charts[j].blocks[a][k],Bj=charts[j].blocks[b][k],wedge=js(mtrace(mtimes(Ai.B,Bj.B)),mtrace(mtimes(Bi.B,Aj.B))),linear=jscale(js(jm(ta,ja(mtrace(Bi.B),mtrace(Bj.B))),jm(tb,ja(mtrace(Ai.B),mtrace(Aj.B)))),R(BigInt(Ai.k)));sum=ja(sum,jscale(ja(wedge,linear),R(BigInt(Ai.sign))))}
const scalar=js(jscale(sum,R(1n,4n)),jscale(jm(q(i,j,a),q(i,j,b)),R(15n,8n))),G=g[i][j],inv=[[G[1][1],jn(G[0][1])],[jn(G[1][0]),G[0][0]]],K=msc(msub(mtimes(md(inv,a),md(G,b)),mtimes(md(inv,b),md(G,a))),R(1n,2n)),Z=msc(K,R(-1n,2n));Z[0][0]=ja(Z[0][0],scalar);Z[1][1]=ja(Z[1][1],scalar);return mtimes(G,Z)}))}
const u12=first(0,1),u34=first(2,3),bcoef=(i,j,k,a,b)=>mul(R(15n,4n),mul(q(i,j,a)[0],q(j,k,b)[0]));
return{g,u12,u34,charts,bcoef,gamma:base.gamma,delta:base.delta,ev:base.ev};}
function globalCross(D,i,j,k){const A=D.bcoef(i,j,k,0,1),B=D.bcoef(i,j,k,2,3);let out=crossResidual(D,i,j,k);out=ms(out,scale(mv(D.u34[i][k]),A));out=ms(out,scale(mv(D.u12[i][k]),B));out=ms(out,scale(mv(D.g[i][k]),mul(A,B)));return out}

function combinations(n,k){const out=[];function rec(a,j){if(a.length===k){out.push(a);return}for(let i=j;i<n;i++)rec([...a,i],i+1)}rec([],0);return out}
function embed(A,ro,co){const M=mat(32,32);A.forEach((row,i)=>row.forEach((x,j)=>M[ro+i][co+j]=x));return M}
function endTransfer(D){
const n=D.charts.length,d=ma(ma(embed(mv(D.gamma),5,0),embed(mv(D.delta),20,5)),embed(mv(D.ev),30,20));
const H=D.charts.map(c=>ma(ma(embed(mv(c.H0),0,5),embed(mv(c.H1),5,20)),embed(mv(c.eta),20,30))),EE=D.charts.map(c=>embed(mm(mv(c.I),mv(c.P)),5,5));
const levels=[new Map()];for(const t of combinations(n,3)){const[i,j,k]=t,G=mv(D.g[i][k]),GI=[[G[1][1],neg(G[0][1])],[neg(G[1][0]),G[0][0]]],C=mm(GI,globalCross(D,i,j,k)),J=mm(mm(mv(D.charts[i].I),tr(C)),mv(D.charts[i].P));levels[0].set(t.join(","),embed(J,5,5))}
function cob(level,t){return t.reduce((sum,_,a)=>ma(sum,scale(level.get(t.filter((_,b)=>b!==a).join(",")),R(a%2?-1n:1n))),mat(32,32))}
for(let k=1;k<=3;k++){const out=new Map();for(const t of combinations(n,k+3)){const F=cob(levels[k-1],t),i=t[0],hF=ma(mm(H[i],F),scale(mm(mm(EE[i],F),H[i]),R((k-1)%2?-1n:1n)));out.set(t.join(","),scale(hF,R(k%2?1n:-1n)))}levels.push(out)}
return{levels,d,cob};}



// Completed auxiliary-first residual and sparse-prefix bound.
function collect(v,r=Array(18).fill(0)){if(typeof v==='number')bp(v).forEach((x,j)=>r[j]=Math.max(r[j],x));else if(Array.isArray(v))for(const x of v)collect(x,r);else for(const x of Object.values(v))collect(x,r);return r;}
const compress=b=>[...Array.from({length:5},(_,j)=>Math.max(b[2*j],b[2*j+1])),Math.max(...b.slice(10,14)),...b.slice(14)];
const D=globalBuild2(['x1','x2','x3','x4'],[[0,15],[0,15],[0,15]]);
const G=mv(D.g[0][2]),GI=[[G[1][1],neg(G[0][1])],[neg(G[1][0]),G[0][0]]];
const C=mm(GI,globalCross(D,0,1,2));
const F=mm(mm(mv(D.charts[0].I),tr(C)),mv(D.charts[0].P));
const tail=compress(collect(F));
const base=build2([], [0,1,2,3,4,5],false),gamma=mv(base.gamma),delta=mv(base.delta);
const id15=mat(15,15);for(let i=0;i<15;i++)id15[i][i]=o;
const cs=base.charts.map(c=>({...Object.fromEntries(['I','P','H0','H1','eta'].map(k=>[k,mv(c[k])])),E:ms(ms(id15,mm(gamma,mv(c.H0))),mm(mv(c.H1),delta))}));
// Generic tail coefficient with its primary poles accounted separately.
// Prefix carriers are absent from the tail by strict carrier ordering.
const f=Array.from({length:15},()=>Array.from({length:15},()=>B([...Array(14).fill(0),1,1,1,1])));
const order=[5,0,1,2,3,4],q2=[],q3=[];
for(let ia=0;ia<order.length;ia++)for(let ib=ia+1;ib<order.length-1;ib++){
 const a=order[ia],b=order[ib],A=cs[a],B0=cs[b];
 const Z=mm(mm(B0.E,f),B0.H1),X02=mm(A.H0,Z),X13=scale(mm(mm(A.E,Z),A.eta),minus);
 // These are h_A h_B j_tail; the J2 minus does not affect a pole bound.
 const scalar=sub(X02[0][0],X13[10][0]);
 let scalarBound=collect(scalar);
 if(a===5){
  // Exact homogeneous identities are separately checked by the Python audit:
  // I_*[10,:]=0 and H0_*[0,:]=e10^T/v0.
  scalarBound=collect(mul(poleJet([1,0,0,0],undefined,false,5)[0],Z[10][0]));
 }
 q2.push({a,b,tailCarriers:order.slice(ib+1),blocks:compress(collect([X02,X13])),scalar:compress(scalarBound)});
 for(let ic=ib+1;ic<order.length-1;ic++){
  const c=order[ic],C0=cs[c];
  const z=mm(mm(C0.E,f),C0.H1);
  const x03=mm(A.H0,mm(mm(B0.E,z),B0.eta));
  q3.push({a,b,c,tailCarriers:order.slice(ic+1),block:compress(collect(x03))});
 }
}
function mx(vs){return vs.reduce((a,b)=>a.map((x,i)=>Math.max(x,b[i])),Array(10).fill(0));}
const report={schema:'hm-negative-coset-pole-v1',order,tailPrimaryJ0:tail,q2,q3,
 q2PrefixBounds:mx(q2.map(x=>x.blocks)),q2ScalarPrefixBounds:mx(q2.map(x=>x.scalar)),q3PrefixBounds:mx(q3.map(x=>x.block)),
 completed:{twoColumnJ2:[13,13,13,13,13,3,1,1,1,1],twoColumnJ3:[13,13,13,13,13,2,1,1,1,1],scalar:[13,13,13,13,13,1,1,1,1,1]},
 modelSha256:require('node:crypto').createHash('sha256').update(JSON.stringify(MODEL)).digest('hex'),abstractScalars:nodes.length};
if(report.modelSha256!=='b6b532c4bab5787397a4cddde34210c12fae71853b30cb73ecbe8a9c2b4826b2')throw Error('MODEL pin');
const expected={twoColumnJ2:[13,13,13,13,13,3,1,1,1,1],twoColumnJ3:[13,13,13,13,13,2,1,1,1,1],scalar:[13,13,13,13,13,1,1,1,1,1]};
if(JSON.stringify(report.completed)!==JSON.stringify(expected))throw Error('Unexpected bound');
for(const t of [...q2,...q3]){
 const anchors=[t.a,t.b,...('c' in t?[t.c]:[])];
 if(new Set(anchors).size!==anchors.length||anchors.some(a=>t.tailCarriers.includes(a)))throw Error('Carrier allocation');
}
report.allocation='Primary tail and strictly earlier prefix carriers are disjoint; take max, not sum, after carrier specialization. Each tail pole is allocated only to an occurring tail carrier. Repeated refined vertices of one prefix carrier vanish.';
report.mergedScalar={carrierOrder:['v0',1,2,3,4],carrierPowers:[1,13,13,13,13],legalLinePowers:[1,1,1,1],firstOpenNeedsLineRefinement:false,nonzeroTailCarriers:[2,3,4],formulaForFirstMergedAnchor:'c=-Z[10,0]/v0; Z=E_B (I_C M^t P_C) H1_B',sign:'J2=-h_A h_B j_C(M)'};
report.scope='Completed new auxiliary-first quotient/scalar cochains, their restrictions and Cech boundaries. No denominator claim for old-order lifts or an order-change homotopy.';
console.log(JSON.stringify(report,null,2));
