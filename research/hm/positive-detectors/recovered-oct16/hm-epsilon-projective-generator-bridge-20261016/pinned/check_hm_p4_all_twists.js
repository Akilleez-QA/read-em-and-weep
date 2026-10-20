// Exact integral certificate for the four P4 End(L) twists and the D8 sector.
// This concerns the pinned perfect line complex; it does not certify HM exactness in F3.
// Uses the pinned four-term HM complex; never invokes the 80,384-dimensional model.
// Source: add03476d9055aa00e1e00778eea6332cf8e01cc, research/hm/verify-hm-ext.js.
// Pinned source blob: fa5231de92b61143e3406111d4af028284db6d55.
// Run: node check_hm_p4_all_twists.js
  const exact=x=>{if(!Number.isSafeInteger(x))throw Error("Unsafe integer arithmetic");return x;};
  const ranks=[5,15,10,2];
  const wp=i=>[(i+2)%5,(i+3)%5], wm=i=>[(i+1)%5,(i+4)%5];
  function eps(a){if(new Set(a).size<5)return 0;let n=0;for(let i=0;i<5;i++)for(let j=i+1;j<5;j++)if(a[i]>a[j])n++;return(-1)**n;}
  const gamma=Array.from({length:15},(_,r)=>Array.from({length:5},(_,a)=>Array.from({length:5},(_,k)=>eps([k,...(r<5||r>=10?wp(a):wm(a)),...(r<5?wp(r):r<10?wm(r-5):wm(r-10))]))));
  const d=Array.from({length:3},(_,l)=>Array.from({length:ranks[l]},()=>[]));
  for(let a=0;a<5;a++)for(let r=0;r<15;r++)for(let k=0;k<5;k++)if(gamma[r][a][k])d[0][a].push([r,k,gamma[r][a][k]]);
  function form(c,h,[p,q]){d[1][c].push([5*h+q,p,1],[5*h+p,q,-1]);}
  for(let i=0;i<5;i++){form(i,0,wp(i));form(i+5,1,wm(i));form(i+10,0,wm(i));form(i+10,1,wp(i));}
  for(let b=0;b<2;b++)for(let k=0;k<5;k++)d[2][b*5+k].push([b,k,1]);
  const incoming=d.map((cols,l)=>Array.from({length:ranks[l+1]},(_,row)=>cols.flatMap((ts,col)=>ts.filter(t=>t[0]===row).map(t=>[col,t[1],t[2]]))));
  for(let l=0;l<2;l++)for(let a=0;a<ranks[l];a++){let c=new Map();for(let[b,k,z]of d[l][a])for(let[r,j,w]of d[l+1][b])add(c,[r,Math.min(k,j),Math.max(k,j)].join(","),z*w);if(c.size)throw Error("Line differential does not square to zero");}


function add(M,k,v){let z=exact((M.get(k)||0)+v);if(z)M.set(k,z);else M.delete(k);}
function monomials(degree,variables=5){
  if(degree<0)return[];
  if(variables===1)return[[degree]];
  const out=[];
  for(let a=0;a<=degree;a++)for(const tail of monomials(degree-a,variables-1))out.push([a,...tail]);
  return out;
}
function basis(r,t){
  const out=[];
  for(let u=0;u<4;u++){const v=u+r;if(v<0||v>=4)continue;
    for(let a=0;a<ranks[v];a++)for(let b=0;b<ranks[u];b++)
      for(const m of monomials(r+t))out.push([u,v,a,b,...m]);
  }
  return out;
}
function matrix(r,t){
  const src=basis(r,t),dst=basis(r+1,t),idx=new Map(dst.map((x,i)=>[x.join(','),i]));
  const rows=dst.map(()=>new Map());
  for(let col=0;col<src.length;col++){
    const [u,v,a,b,...m]=src[col];
    function emit(uu,vv,aa,bb,k,z){
      const mm=m.slice();mm[k]++;
      const row=idx.get([uu,vv,aa,bb,...mm].join(','));
      if(row===undefined)throw Error('Missing target');add(rows[row],col,z);
    }
    if(v<3)for(const[c,k,z]of d[v][a])emit(u,v+1,c,b,k,z);
    if(u>0)for(const[c,k,z]of incoming[u-1][b])emit(u-1,v,a,c,k,z*(r%2===0?-1:1));
  }
  return{rows,cols:src.length};
}
function rankExact(input,ncols){
  const A=input.map(r=>new Map(r));let rank=0,max=1;
  for(let c=0;c<ncols;c++){
    let r=rank;while(r<A.length&&Math.abs(A[r].get(c)||0)!==1)r++;
    if(r===A.length){if(A.slice(rank).some(row=>row.get(c)))break;continue;}
    [A[r],A[rank]]=[A[rank],A[r]];const ar=A[rank];
    if(ar.get(c)===-1)for(const[j,v]of ar)ar.set(j,-v);
    for(let i=rank+1;i<A.length;i++){
      const ai=A[i],m=ai.get(c);if(!m)continue;
      for(const[j,v]of ar){const z=exact((ai.get(j)||0)-exact(m*v));if(z)ai.set(j,z);else ai.delete(j);max=Math.max(max,Math.abs(z));}
    }
    rank++;
  }
  const unitRank=rank;
  const B=A.slice(rank).map(r=>new Map(Array.from(r,([j,v])=>[j,BigInt(v)])));
  let rr=0,tailMaxBits=0;
  function abs(x){return x<0n?-x:x;}
  function gcd(a,b){a=abs(a);b=abs(b);while(b){const t=a%b;a=b;b=t;}return a;}
  for(let c=0;c<ncols;c++){
    let r=rr;while(r<B.length&&!B[r].get(c))r++;if(r===B.length)continue;
    [B[r],B[rr]]=[B[rr],B[r]];const ar=B[rr],p=ar.get(c);
    for(let i=rr+1;i<B.length;i++){
      const ai=B[i],m=ai.get(c);if(!m)continue;
      const g=gcd(p,m),f=p/g,t=m/g;
      for(const[j,v]of ai)ai.set(j,v*f);
      for(const[j,v]of ar){const z=(ai.get(j)||0n)-t*v;if(z)ai.set(j,z);else ai.delete(j);}
      let gg=0n;for(const v of ai.values())gg=gcd(gg,v);
      if(gg>1n)for(const[j,v]of ai)ai.set(j,v/gg);
      for(const v of ai.values())tailMaxBits=Math.max(tailMaxBits,abs(v).toString(2).length);
    }
    rr++;
  }
  if(B.slice(rr).some(r=>r.size))throw Error('Nonzero rank-certificate remainder');
  return{rank:rank+rr,unitRank,max,tailMaxBits};
}
function checkComposition(A,B){
  if(B.cols!==A.rows.length)throw Error('Composition shape mismatch');
  for(const row of B.rows){const acc=new Map();for(const[j,z]of row)for(const[k,w]of A.rows[j])add(acc,k,exact(z*w));if(acc.size)throw Error('Differentials do not compose to zero');}
}

const results=[];
function certify(A){
  const C=rankExact(A.rows,A.cols);
  if(C.unitRank!==C.rank||C.tailMaxBits!==0)throw Error('Nonunit rank: characteristic-independent certificate failed');
  return {shape:[A.rows.length,A.cols],nonzeros:A.rows.reduce((s,r)=>s+r.size,0),...C};
}
for(const t of [0,-1]){
  const matrices=[0,1,2].map(r=>matrix(r,t));
  checkComposition(matrices[0],matrices[1]);checkComposition(matrices[1],matrices[2]);
  const cert=matrices.map(certify),dims=[0,1,2,3].map(r=>basis(r,t).length);
  const cohomology=dims.map((n,i)=>n-(i?cert[i-1].rank:0)-(i<3?cert[i].rank:0)).concat(0);
  results.push({twist:t,dimensions:dims,matrices:cert,cohomology});
}
const test=matrix(2,-2),testCert=certify(test);
// Standard Cech cover U_i of P4. A Laurent monomial m occurs on
// subsets S containing every index for which m_i<0. Cech degree=|S|-1.
const popcount=s=>{let n=0;for(;s;s>>=1)n+=s&1;return n;};
const pos=(s,j)=>popcount(s&((1<<j)-1));
function cech(M){
  const out=new Map();
  for(const [key,value] of M){const [u,v,a,b,S,...m]=key.split(',').map(Number);
    for(let j=0;j<5;j++)if(!(S&(1<<j)))add(out,[u,v,a,b,S|(1<<j),...m].join(','),value*((pos(S,j)%2)?-1:1));
  }
  return out;
}
function hCech(M){
  const out=new Map();
  for(const[key,value]of M){const[u,v,a,b,S,...m]=key.split(',').map(Number);
    const j=m.findIndex(e=>e>=0);
    if(j<0||!(S&(1<<j))||popcount(S)===1)continue;
    add(out,[u,v,a,b,S^(1<<j),...m].join(','),value*((pos(S,j)%2)?-1:1));
  }
  return out;
}
function deltaCech(M){
  const out=new Map();
  for(const[key,value]of M){const[u,v,a,b,S,...m]=key.split(',').map(Number),r=v-u,q=popcount(S)-1;
    function emit(uu,vv,aa,bb,k,z){const mm=m.slice();mm[k]++;add(out,[uu,vv,aa,bb,S,...mm].join(','),value*z*((q%2)?-1:1));}
    if(v<3)for(const[c,k,z]of d[v][a])emit(u,v+1,c,b,k,z);
    if(u>0)for(const[c,k,z]of incoming[u-1][b])emit(u-1,v,a,c,k,z*((r%2===0)?-1:1));
  }
  return out;
}
function assertEqual(A,B,label){const C=new Map(A);for(const[k,v]of B)add(C,k,-v);if(C.size)throw Error(label+': '+JSON.stringify([...C].slice(0,3)));}
function addMaps(A,B){const C=new Map(A);for(const[k,v]of B)add(C,k,v);return C;}
const target=basis(2,-2),idx=new Map(target.map((x,i)=>[x.join(','),i]));
const d5=target.map(()=>new Map());
let statesMax=0,contractionChecks=0;
for(let a=0;a<5;a++)for(let b=0;b<2;b++){
  const col=2*a+b;
  let M=new Map([[[3,0,a,b,31,-1,-1,-1,-1,-1].join(','),1]]);
  for(let step=0;step<5;step++){
    assertEqual(addMaps(cech(deltaCech(M)),deltaCech(cech(M))),new Map(),'differentials anticommute');
    assertEqual(deltaCech(deltaCech(M)),new Map(),'internal square');
    M=deltaCech(M);statesMax=Math.max(statesMax,M.size);
    if(step<4){
      assertEqual(addMaps(cech(hCech(M)),hCech(cech(M))),M,'contraction identity');contractionChecks++;
      M=hCech(M);
    }
  }
  assertEqual(cech(M),new Map(),'final Cech cocycle');
  assertEqual(deltaCech(M),new Map(),'final internal cycle');
  for(const[key,value]of M){const[u,v,aa,bb,S,...m]=key.split(',').map(Number);if(popcount(S)!==1||m.some(e=>e!==0))throw Error('Final state not constant');if(S!==1)continue;const row=idx.get([u,v,aa,bb,...m].join(','));if(row===undefined)throw Error('Missing target');add(d5[row],col,value);}
}
const d5cert=certify({rows:d5,cols:10});checkComposition({rows:d5,cols:10},test);
const minorRows=[50,60,51,61,52,62,53,63,54,64];
minorRows.forEach((row,col)=>{if(d5[row].size!==1||d5[row].get(col)!==1)throw Error('Expected identity minor absent');});
const neg2=[0,10-d5cert.rank,80-testCert.rank-d5cert.rank,50-testCert.rank,0];
results.push({twist:-2,matrices:{d5:d5cert,ordinary:testCert},cohomology:neg2});
// End(L) is canonically self-dual as a perfect complex over every field.
// Serre duality on P4 pairs t=-3 with t=-2 and degree i with 4-i.
results.push({twist:-3,method:'Serre duality from twist -2',cohomology:neg2.slice().reverse()});
if(JSON.stringify(results.map(x=>x.cohomology))!==JSON.stringify([[1,24,2,0,0],[0,5,10,0,0],[0,0,20,0,0],[0,0,20,0,0]]))throw Error('Unexpected cohomology');
// R_n has a monomial permutation basis. D8 fixed spaces count actual orbits,
// not traces reduced modulo the characteristic. Taking invariants is exact
// whenever 8 is invertible. A is D8-trivial, so the invariant generator
// dimensions are coefficients of (1-t)^5 times these orbit counts.
const choose5=[1,5,10,10,5,1];
const orbits=n=>{const m=n+1;return(m**4+2*m**3+3*m**2+2*m)/8;};
const invariantGenerators=Array.from({length:8},(_,n)=>Array.from({length:Math.min(5,n)+1},(_,j)=>(-1)**j*choose5[j]*orbits(n-j)).reduce((a,b)=>a+b,0));
if(JSON.stringify(invariantGenerators)!=='[1,1,1,0,0,0,0,0]')throw Error('Unexpected invariant generator dimensions');
const generatorDimensions=[1,11,11,1];
const trivialDeckCohomology=Array.from({length:5},(_,i)=>results.reduce((s,x,j)=>s+x.cohomology[i]*generatorDimensions[j],0));
const fullSignCohomology=trivialDeckCohomology.slice().reverse();
const epsilonSector=results.reduce((s,x,j)=>s+x.cohomology[2]*invariantGenerators[j],0);
if(epsilonSector!==32||JSON.stringify(fullSignCohomology)!=='[0,0,352,79,1]')throw Error('Unexpected sector');
console.log(JSON.stringify({scope:'Pinned perfect line complex, every odd characteristic; not obstruction naturality or HM-bundle exactness',p4Twists:results,cech:{statesMax,contractionChecks,d5IdentityMinorRowsZeroBased:minorRows},D8:{invariantGeneratorDimensions:invariantGenerators.slice(0,4),trivialDeckCohomology,fullSignCohomology,epsilonExt2Dimension:epsilonSector}},null,2));
