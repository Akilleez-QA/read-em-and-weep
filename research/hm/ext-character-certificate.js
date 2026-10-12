// Deterministic exact integer certificate for the specified HM pullback.
// Run with Node.js: node research/hm/ext-character-certificate.js
// See ext-model.md for the mathematical model and its limitations.

function verifyHMCharacters() {
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
  const subsets=Array.from({length:5},()=>[]);
  for(let s=0;s<16;s++){let x=Array.from({length:4},(_,j)=>(s>>j)&1);subsets[x.reduce((a,b)=>a+b,0)].push(x);}
  function add(M,k,v){let z=(M.get(k)||0)+v;if(z)M.set(k,z);else M.delete(k);}
  function mons(lo,hi){let out=[];for(let a=lo[0];a<=hi[0];a++)for(let b=lo[1];b<=hi[1];b++)for(let c=lo[2];c<=hi[2];c++)for(let e=lo[3];e<=hi[3];e++)out.push([a,b,c,e]);return out;}
  function echelon(input,ncols){
    let A=input.map(r=>new Map(r)),rank=0,pivots=[],max=1;
    for(let c=0;c<ncols;c++){let r=rank;while(r<A.length&&Math.abs(A[r].get(c)||0)!==1)r++;
      if(r===A.length){if(A.slice(rank).some(row=>row.get(c)))throw Error("Nonunit pivot: need rational arithmetic");continue;}
      [A[r],A[rank]]=[A[rank],A[r]];let ar=A[rank];if(ar.get(c)===-1)for(let[j,v]of ar)ar.set(j,-v);
      for(let i=rank+1;i<A.length;i++){let ai=A[i],m=ai.get(c);if(!m)continue;for(let[j,v]of ar){let z=(ai.get(j)||0)-m*v;if(!Number.isSafeInteger(z))throw Error("Integer overflow");if(z)ai.set(j,z);else ai.delete(j);max=Math.max(max,Math.abs(z));}}
      pivots.push(c);rank++;
    }
    if(A.slice(rank).some(r=>r.size))throw Error("Nonzero residual rows");
    let P=new Set(pivots),kernel=[];
    for(let f=0;f<ncols;f++)if(!P.has(f)){let v=Array(ncols).fill(0);v[f]=1;for(let i=rank-1;i>=0;i--){let z=0;for(let[j,a]of A[i])if(j!==pivots[i])z+=a*v[j];v[pivots[i]]=-z;}
      for(let row of input){let z=0;for(let[j,a]of row)z+=a*v[j];if(z)throw Error("Kernel certificate failed");}kernel.push(v);
    }
    return {rank,max,kernel,nonzeros:input.reduce((s,r)=>s+r.size,0)};
  }
  function negativeD1(weight){
    let src=mons(Array.from({length:4},(_,i)=>i<weight?-4:-2),[-1,-1,-1,-1]);
    let target=mons(Array.from({length:4},(_,i)=>i<weight?-3:-1),[-1,-1,-1,-1]),ti=new Map(target.map((x,i)=>[x.join(","),i]));
    let A=Array.from({length:80*target.length},()=>new Map());
    for(let a=0;a<5;a++)for(let b=0;b<2;b++)for(let m=0;m<src.length;m++){let col=(2*a+b)*src.length+m;
      for(let k=0;k<5;k++)for(let sm of subsets[k]){let j=ti.get(src[m].map((x,t)=>x+sm[t]).join(","));if(j===undefined)continue;
        add(A[(a*10+b*5+k)*target.length+j],col,1);
        for(let r=0;r<15;r++)if(gamma[r][a][k])add(A[(50+r*2+b)*target.length+j],col,gamma[r][a][k]);
      }
    }return {A,src};
  }
  function delta(M,r,step,steps,ranges){
    let R=new Map(),rs=r%2===0?-1:1,left=steps-step;
    for(let[key,value]of M){let[u,v,a,b,mask,...m]=key.split(",").map(Number),p=4-((mask&1)+((mask>>1)&1)+((mask>>2)&1)+((mask>>3)&1)),sgn=p%2?-1:1;
      function emit(uu,vv,aa,bb,k,z){for(let sm of subsets[k]){let mm=m.map((x,j)=>x+sm[j]);if(mm.some((x,j)=>x<ranges[j][0]-left||x>ranges[j][1]))continue;add(R,[uu,vv,aa,bb,mask,...mm].join(","),value*z*sgn);}}
      if(v<3)for(let[c,k,z]of d[v][a])emit(u,v+1,c,b,k,z);
      if(u>0)for(let[c,k,z]of incoming[u-1][b])emit(u-1,v,a,c,k,z*rs);
    }return R;
  }
  function homotopy(M,r,weight,targetMask){
    let R=new Map(),n=Array.from({length:4},(_,i)=>r-(i<weight?2:0));
    for(let[key,value]of M){let[u,v,a,b,mask,...m]=key.split(",").map(Number);
      for(let j=0;j<4;j++){if((mask>>j)&1||!((targetMask>>j)&1)||m[j]>=0||m[j]>n[j])continue;let good=true,cBefore=0;
        for(let i=0;i<j;i++){if((mask>>i)&1){if(m[i]<0||m[i]>n[i])good=false;}else{cBefore++;if(m[i]<=n[i]||m[i]>=0)good=false;}}
        if(good)add(R,[u,v,a,b,mask|(1<<j),...m].join(","),value*(cBefore%2?-1:1));
      }
    }return R;
  }
  function run(vector,src,weight,steps,targetMask,ranges){
    let M=new Map();
    for(let j=0;j<vector.length;j++)if(vector[j]){let unit=Math.floor(j/src.length);add(M,[3,0,Math.floor(unit/2),unit%2,0,...src[j%src.length]].join(","),vector[j]);}
    for(let step=1;step<=steps;step++){M=delta(M,step-4,step,steps,ranges);if(step<steps)M=homotopy(M,step-3,weight,targetMask);}
    return M;
  }
  let output=[];
  for(let weight of [2,3,4]){
    let {A,src}=negativeD1(weight),r1=echelon(A,10*src.length),K=r1.kernel,r3=null;
    if(weight===2){
      let B=Array.from({length:354},()=>new Map()),offset=[0,25,250,350];
      for(let j=0;j<K.length;j++)for(let[key,z]of run(K[j],src,weight,3,12,[[-1,-1],[-1,-1],[0,0],[0,0]])){let[u,v,a,b,mask]=key.split(",").map(Number);if(u!==v||mask!==12)throw Error("Bad d3 target");add(B[offset[u]+a*ranks[u]+b],j,z);}
      r3=echelon(B,K.length);K=r3.kernel.map(v=>{let out=Array(10*src.length).fill(0);for(let i=0;i<v.length;i++)if(v[i])for(let j=0;j<out.length;j++)out[j]+=v[i]*r1.kernel[i][j];return out;});
    }
    let ranges=Array.from({length:4},(_,i)=>[0,i<weight?0:2]),tm=mons([0,0,0,0],ranges.map(r=>r[1])),ti=new Map(tm.map((m,i)=>[m.join(","),i])),B=Array.from({length:80*tm.length},()=>new Map());
    for(let j=0;j<K.length;j++)for(let[key,z]of run(K[j],src,weight,5,15,ranges)){let[u,v,a,b,mask,...m]=key.split(",").map(Number);if(v-u!==2||mask!==15)throw Error("Bad d5 target");let unit=u===0?a*5+b:50+a*15+b;add(B[unit*tm.length+ti.get(m.join(","))],j,z);}
    let r5=echelon(B,K.length);
    output.push({weight,d1:{shape:[A.length,10*src.length],rank:r1.rank,nonzeros:r1.nonzeros,max:r1.max},d3:r3?{shape:[354,r1.kernel.length],rank:r3.rank,nonzeros:r3.nonzeros,max:r3.max}:null,d5:{shape:[B.length,K.length],rank:r5.rank,nonzeros:r5.nonzeros,max:r5.max},ext1:r5.kernel.length});
  }
  return output;
}
const result = verifyHMCharacters();
const expected = [[450, 100, 90], [1250, null, 30], [2550, null, 10]];
for (let i = 0; i < result.length; i++) {
  const r = result[i];
  const actual = [r.d1.rank, r.d3 ? r.d3.rank : null, r.d5.rank];
  if (JSON.stringify(actual) !== JSON.stringify(expected[i]) || r.ext1 !== 0) {
    throw new Error('Unexpected exact certificate result');
  }
}
console.log(JSON.stringify(result, null, 2));
