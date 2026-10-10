// Exact polynomial checks over Z[a,b,c,d]. Node.js 18+; no dependencies.
const exact=x=>{if(!Number.isSafeInteger(x))throw Error('Unsafe integer arithmetic');return x;};
const zero=()=>({});
const C=n=>n?{"0,0,0,0":n}:{};
const V=i=>({[Array.from({length:4},(_,j)=>Number(i===j)).join(",")]:1});
const add=(p,q)=>{const r={...p};for(const [k,v] of Object.entries(q)){r[k]=exact((r[k]||0)+v);if(!r[k])delete r[k];}return r;};
const scale=(p,n)=>Object.fromEntries(Object.entries(p).map(([k,v])=>[k,exact(n*v)]).filter(([,v])=>v));
const sub=(p,q)=>add(p,scale(q,-1));
const mul=(p,q)=>{let r={};for(const [k,v] of Object.entries(p))for(const [l,w] of Object.entries(q)){const m=k.split(",").map((x,i)=>+x+(+l.split(",")[i])).join(",");r[m]=exact((r[m]||0)+exact(v*w));}return Object.fromEntries(Object.entries(r).filter(([,v])=>v));};
const pow=(p,n)=>{let r=C(1);for(let i=0;i<n;i++)r=mul(r,p);return r;};
const [a,b,c,d]=[0,1,2,3].map(V), B=add(b,c), bc=mul(b,c);
const moment=n=>sub(add(pow(sub(a,b),n),pow(sub(a,c),n)),pow(sub(a,B),n));
const D=sub(scale(bc,2),pow(a,2));
const tests={};
tests.ci_ch2= sub(moment(2),scale(D,-1));
tests.ci_ch3=sub(add(moment(3),mul(a,D)),mul(bc,sub(scale(B,3),scale(a,4))));
const q4=sub(moment(4),pow(D,2));
tests.ci_ch4=sub(q4,mul(bc,sub(add(scale(pow(a,2),-8),scale(mul(a,B),12)),add(scale(pow(B,2),4),scale(bc,2)))));
// After a=3B/4, the bracket in q4 is B^2/2 - 2bc.
tests.ci_substitution=sub(add(add(scale(pow(B,2),-72),scale(pow(B,2),144)),scale(pow(B,2),-64)),scale(pow(B,2),8));
// Proportional-canonical equation: 9(7a^4+6a^2d-d^2)-64a^2(a^2+d).
const A2=pow(a,2), A4=pow(a,4), d2=pow(d,2);
const lhs=sub(scale(sub(add(scale(A4,7),scale(mul(A2,d),6)),d2),9),scale(mul(A2,add(A2,d)),64));
tests.surface_factorization=add(lhs,mul(add(A2,d),add(A2,scale(d,9))));
for(const [name,p] of Object.entries(tests))if(Object.keys(p).length)throw new Error(name+": "+JSON.stringify(p));
console.log(JSON.stringify({passed:Object.keys(tests),count:Object.keys(tests).length}));
