'use strict';
// Exact Q polynomial circuits with exposed Laurent factor monomials.
// A scalar denotes P_n * product(tag_i ** e_i). P_n is division-free.
const NT=16;
function gcd(a,b){a=a<0n?-a:a;b=b<0n?-b:b;while(b){[a,b]=[b,a%b]}return a}
function makeRing(){
 const nodes=[],pcache=new Map();let counters={add:0,mul:0};
 function node(v){const k=JSON.stringify(v);if(pcache.has(k))return pcache.get(k);const id=nodes.length;nodes.push(v);pcache.set(k,id);return id}
 function constant(n,d=1n){if(!d)throw Error('zero constant denominator');if(!n)d=1n;if(d<0n){n=-n;d=-d}const g=gcd(n,d);return node(['const',String(n/g),String(d/g)])}
 const pnzero=constant(0n),pnone=constant(1n),pnminus=constant(-1n),E0=Object.freeze(Array(NT).fill(0));
 const scalar=(n,e=E0)=>n===pnzero?zero:{n,e};let zero={n:pnzero,e:E0},one=scalar(pnone);
 const isconst=n=>nodes[n][0]==='const';
 function padd(a,b){if(a===pnzero)return b;if(b===pnzero)return a;if(isconst(a)&&isconst(b)){const A=nodes[a],B=nodes[b];return constant(BigInt(A[1])*BigInt(B[2])+BigInt(B[1])*BigInt(A[2]),BigInt(A[2])*BigInt(B[2]))}return node(['add',Math.min(a,b),Math.max(a,b)])}
 function pmul(a,b){if(a===pnzero||b===pnzero)return pnzero;if(a===pnone)return b;if(b===pnone)return a;if(isconst(a)&&isconst(b)){const A=nodes[a],B=nodes[b];return constant(BigInt(A[1])*BigInt(B[1]),BigInt(A[2])*BigInt(B[2]))}return node(['mul',Math.min(a,b),Math.max(a,b)])}
 function ptags(e){if(e.every(x=>x===0))return pnone;if(e.some(x=>x<0))throw Error('Negative tag in polynomial numerator');return node(['tags',...e])}
 function add(a,b){counters.add++;if(a.n===pnzero)return b;if(b.n===pnzero)return a;const e=a.e.map((v,i)=>Math.min(v,b.e[i])),A=pmul(a.n,ptags(a.e.map((v,i)=>v-e[i]))),B=pmul(b.n,ptags(b.e.map((v,i)=>v-e[i])));return scalar(padd(A,B),e)}
 function mul(a,b){counters.mul++;if(a.n===pnzero||b.n===pnzero)return zero;if(a===one)return b;if(b===one)return a;return scalar(pmul(a.n,b.n),a.e.map((v,i)=>v+b.e[i]))}
 const neg=a=>scalar(pmul(pnminus,a.n),a.e),fromBigInt=a=>scalar(constant(BigInt(a))),rational=(n,d)=>scalar(constant(BigInt(n),BigInt(d)));
 const tag=i=>{let e=Array(NT).fill(0);e[i]=1;return scalar(pnone,e)};
 const pow=(a,n)=>{if(n<0)return pow(inv(a),-n);let r=one;while(n){if(n%2)r=mul(r,a);n=Math.floor(n/2);if(n)a=mul(a,a)}return r};
 function inv(a){if(!isconst(a.n))throw Error('Only exactly factored denominators may be inverted');const c=nodes[a.n];return scalar(constant(BigInt(c[2]),BigInt(c[1])),a.e.map(v=>-v))}
 const x=Array.from({length:4},(_,i)=>tag(i));
 const V=[one,tag(8),tag(9),tag(10),x.reduce(mul,one)],F=Array.from({length:5},(_,j)=>tag(11+j));
 const R={zero,one,add,mul,neg,inv,fromBigInt,rational,pow,tag,x,V,F,scalar,nodes,counters};
 R.projectiveCoordinate=(j,tau,computed)=>mul(tau,V[j]);
 R.carrierGenerator=(j,tau,computed)=>j<5?mul(pow(tau,5),mul(V[j],F[j])):mul(pow(tau,4),[V[1],V[3],V[4]].reduce(mul,one));
 R.legalLine=(i,computed)=>mul(tag(4+i),pow(x[i],-2));
 R.importDAG=(data,seed)=>{const positiveSeeds=new Map();for(let j=0;j<data.nodes.length;j++)if(data.nodes[j][0]==="inv"){const f=seed.inverse_nodes[j];if(!f)throw Error("Unverified inverse seed");positiveSeeds.set(data.nodes[j][1],f)}const a=new Array(data.nodes.length);for(let i=0;i<a.length;i++){const n=data.nodes[i];if(positiveSeeds.has(i)){const f=positiveSeeds.get(i),q=f.coefficient.split("/");a[i]=scalar(constant(BigInt(q[0]),BigInt(q[1]||1)),f.powers)}else if(n[0]==='const')a[i]=rational(n[1],n[2]);else if(n[0]==='var')a[i]=x[n[1]];else if(n[0]==='add')a[i]=add(a[n[1]],a[n[2]]);else if(n[0]==='mul')a[i]=mul(a[n[1]],a[n[2]]);else if(n[0]==='inv'){const f=seed.inverse_nodes[i];if(!f)throw Error('Unverified inverse seed');const c=f.coefficient.split('/');a[i]=scalar(constant(BigInt(c[1]||1),BigInt(c[0])),f.powers.map(v=>-v))}else throw Error('Unknown source op')}
 return Array.from({length:256},(_,code)=>Array.from({length:2},(_,r)=>Array.from({length:2},(_,c)=>{const found=data.coefficients[r][c].find(a=>a[0]===code);return found?a[found[1]]:zero})));};
 R.pruneExport=outputs=>{const seen=new Set();function visit(n){if(seen.has(n))return;seen.add(n);const a=nodes[n];if(a[0]==='add'||a[0]==='mul'){visit(a[1]);visit(a[2])}}outputs.forEach(a=>visit(a.n));const ids=[...seen].sort((a,b)=>a-b),map=new Map(ids.map((a,i)=>[a,i]));return {nodes:ids.map(id=>{const n=nodes[id];return n[0]==='add'||n[0]==='mul'?[n[0],map.get(n[1]),map.get(n[2])]:n}),outputs:outputs.map(a=>({numerator:map.get(a.n),powers:a.e})),retainedNodes:ids.length,allNodes:nodes.length}};
 return R;
}
module.exports={makeRing};
