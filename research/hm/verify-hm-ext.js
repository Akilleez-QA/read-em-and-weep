// Exact cohomology certificate for a Horrocks-Mumford pullback to C^4.
// C: y^2=x^3-x; f is the symmetric product of the four degree-two x maps.
// Dependency-free JavaScript. Run: node verify-hm-ext.js
// Integer pivots are checked exactly; a fraction-free BigInt tail is used
// when unit pivots cease to suffice. Expected ranks and dimensions are asserted.
// This computes Ext dimensions; it does not evaluate a second-order obstruction.


function verifyHMExt() {
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
  const subsets=Array.from({length:5},()=>[]);
  for(let s=0;s<16;s++){let x=Array.from({length:4},(_,j)=>(s>>j)&1);subsets[x.reduce((a,b)=>a+b,0)].push(x);}
  function add(M,k,v){let z=exact((M.get(k)||0)+v);if(z)M.set(k,z);else M.delete(k);}
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
    for(let f=0;f<ncols;f++)if(!P.has(f)){let v=Array(ncols).fill(0);v[f]=1;for(let i=rank-1;i>=0;i--){let z=0;for(let[j,a]of A[i])if(j!==pivots[i])z=exact(z+exact(a*v[j]));v[pivots[i]]=-z;}
      for(let row of input){let z=0;for(let[j,a]of row)z=exact(z+exact(a*v[j]));if(z)throw Error("Kernel certificate failed");}kernel.push(v);
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

  function rankOnly(input,ncols){
    let A=input.map(r=>new Map(r)),rank=0,max=1,blocked=false,nnz=input.reduce((s,r)=>s+r.size,0);
    for(let c=0;c<ncols;c++){let r=rank;while(r<A.length&&Math.abs(A[r].get(c)||0)!==1)r++;
      if(r===A.length){if(A.slice(rank).some(row=>row.get(c))){blocked=true;break;}continue;}
      [A[r],A[rank]]=[A[rank],A[r]];let ar=A[rank];if(ar.get(c)===-1)for(let[j,v]of ar)ar.set(j,-v);
      for(let i=rank+1;i<A.length;i++){let ai=A[i],m=ai.get(c);if(!m)continue;for(let[j,v]of ar){let z=(ai.get(j)||0)-m*v;if(!Number.isSafeInteger(z))throw Error("Unsafe integer");if(z)ai.set(j,z);else ai.delete(j);max=Math.max(max,Math.abs(z));}}rank++;
    }
    let unitRank=rank,tailMaxBits=0;
    if(blocked){
      let B=A.slice(rank).map(r=>new Map(Array.from(r,([j,v])=>[j,BigInt(v)]))),rr=0;
      function abs(x){return x<0n?-x:x;}
      function gcd(a,b){a=abs(a);b=abs(b);while(b){let t=a%b;a=b;b=t;}return a;}
      for(let c=0;c<ncols;c++){let r=rr;while(r<B.length&&!B[r].get(c))r++;if(r===B.length)continue;[B[r],B[rr]]=[B[rr],B[r]];let ar=B[rr],p=ar.get(c);
        for(let i=rr+1;i<B.length;i++){let ai=B[i],m=ai.get(c);if(!m)continue;let g=gcd(p,m),f=p/g,t=m/g;for(let[j,v]of ai)ai.set(j,v*f);for(let[j,v]of ar){let z=(ai.get(j)||0n)-t*v;if(z)ai.set(j,z);else ai.delete(j);}let gg=0n;for(let v of ai.values())gg=gcd(gg,v);if(gg>1n)for(let[j,v]of ai)ai.set(j,v/gg);for(let v of ai.values())tailMaxBits=Math.max(tailMaxBits,abs(v).toString(2).length);}rr++;
      }
      if(B.slice(rr).some(r=>r.size))throw Error("Nonzero exact tail");rank+=rr;
    }else if(A.slice(rank).some(r=>r.size))throw Error("Nonzero residual");
    return{rank,unitRank,max,tailMaxBits,nonzeros:nnz};
  }
  function projectR2(M,A,col,weight,sign=1){
    let rad=Array.from({length:4},(_,i)=>i<weight?1:3),nm=rad.reduce((a,b)=>a*b,1);
    for(let[key,z]of M){let[u,v,a,b,mask,...m]=key.split(",").map(Number);if(v-u!==2||mask!==15)throw Error("Bad positive target");let unit=u===0?a*5+b:50+a*15+b,mi=0;for(let i=0;i<4;i++)mi=mi*rad[i]+m[i];add(A[unit*nm+mi],col,z*sign);}
  }
  const summaries=[];
  for(let weight of [0,1,2,3,4]){
    let{A,src}=negativeD1(weight),r1=echelon(A,10*src.length),K=r1.kernel,r3=null;
    if(weight===2){
      let B=Array.from({length:354},()=>new Map()),offset=[0,25,250,350];
      for(let j=0;j<K.length;j++)for(let[key,z]of run(K[j],src,weight,3,12,[[-1,-1],[-1,-1],[0,0],[0,0]])){let[u,v,a,b,mask]=key.split(",").map(Number);if(u!==v||mask!==12)throw Error("Bad d3");add(B[offset[u]+a*ranks[u]+b],j,z);}
      r3=echelon(B,K.length);K=r3.kernel.map(v=>{let out=Array(10*src.length).fill(0);for(let i=0;i<v.length;i++)if(v[i])for(let j=0;j<out.length;j++)out[j]=exact(out[j]+exact(v[i]*r1.kernel[i][j]));return out;});
    }
    let ranges=Array.from({length:4},(_,i)=>[0,i<weight?0:2]),nm=3**(4-weight),extra=weight===0?3920:weight===1?354:0,B=Array.from({length:80*nm},()=>new Map()),cols=K.length+extra;
    for(let j=0;j<K.length;j++)projectR2(run(K[j],src,weight,5,15,ranges),B,j,weight);
    if(weight===1){
      let offset=[0,25,250,350];
      for(let u=0;u<4;u++)for(let a=0;a<ranks[u];a++)for(let b=0;b<ranks[u];b++){
        let col=K.length+offset[u]+a*ranks[u]+b,M=new Map([[[u,u,a,b,14,-1,0,0,0].join(","),1]]);
        M=delta(M,0,1,2,ranges);M=homotopy(M,1,weight,15);M=delta(M,1,2,2,ranges);
        projectR2(M,B,col,weight,-1);
      }
    }
    if(weight===0){
      let ms=mons([0,0,0,0],[1,1,1,1]),offset=[0,75,225];
      for(let u=0;u<3;u++)for(let a=0;a<ranks[u+1];a++)for(let b=0;b<ranks[u];b++)for(let mi=0;mi<16;mi++){
        let col=K.length+(offset[u]+a*ranks[u]+b)*16+mi,M=new Map([[[u,u+1,a,b,15,...ms[mi]].join(","),1]]);
        projectR2(delta(M,1,1,1,ranges),B,col,weight);
      }
    }
    let finalRank=rankOnly(B,cols),boundaryRank=0;
    if(weight===0){
      let C=Array.from({length:3920},()=>new Map()),offset=[0,25,250,350],r1offset=[0,75,225];
      for(let u=0;u<4;u++)for(let a=0;a<ranks[u];a++)for(let b=0;b<ranks[u];b++){
        let col=offset[u]+a*ranks[u]+b,M=new Map([[[u,u,a,b,15,0,0,0,0].join(","),1]]);
        M=delta(M,0,1,1,[[0,1],[0,1],[0,1],[0,1]]);
        for(let[key,z]of M){let[uu,vv,aa,bb,mask,...m]=key.split(",").map(Number);let mi=((m[0]*2+m[1])*2+m[2])*2+m[3];add(C[(r1offset[uu]+aa*ranks[uu]+bb)*16+mi],col,z);}
      }
      boundaryRank=rankOnly(C,354).rank;
      // Verify D^2=0 on every constant degree-zero generator.
      for(let row of B){let values=new Map();for(let[col,z]of row)if(col>=K.length)for(let[j,w]of C[col-K.length])add(values,j,z*w);if(values.size)throw Error("Boundary is not a cycle");}
    }
    summaries.push({weight,d1:{shape:[A.length,10*src.length],rank:r1.rank,nonzeros:r1.nonzeros,max:r1.max},d3:r3?{shape:[354,r1.kernel.length],rank:r3.rank,nonzeros:r3.nonzeros,max:r3.max}:null,remaining:{shape:[B.length,cols],...finalRank},boundaryRank,h1:cols-finalRank.rank-boundaryRank});
  }
  const h1=summaries.map(x=>x.h1),chi=[274,446,514,446,274];
  const byWeight=h1.map((x,w)=>{let h0=w===0?1:0,h4=w===4?1:0,h3=h1[4-w],h2=chi[w]-h0+x+h3-h4;return[h0,x,h2,h3,h4];});
  const multiplicities=[1,4,6,4,1],dimensions=Array.from({length:5},(_,j)=>byWeight.reduce((s,row,w)=>s+multiplicities[w]*row[j],0));
  if(JSON.stringify(h1)!=="[79,2,0,0,0]"||JSON.stringify(dimensions)!=="[1,87,7372,87,1]")throw Error("Unexpected Ext dimensions");
  const expectedD1=[50,150,450,1250,2550],expectedRemaining=[3598,522,90,30,10];
  for(let w=0;w<5;w++)if(summaries[w].d1.rank!==expectedD1[w]||summaries[w].remaining.rank!==expectedRemaining[w])throw Error("Unexpected intermediate rank");
  return{summaries,byWeight,dimensions,traceFreeDimensions:dimensions.map((x,j)=>x-[1,4,6,4,1][j])};
}
const result=verifyHMExt();
if(typeof console!=="undefined"&&console.log)console.log(JSON.stringify(result,null,2));
result;
