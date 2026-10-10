"use strict";
// Ring-generic contraction for the actual group-multilinear mixed residual.
// Scalar ring interface: {zero,one,add,mul,neg}. No division or truncation.
function maskBasis(code){const subsets=[0,0,0];for(let a=0;a<4;a++){const b=code%4;code=Math.floor(code/4);if(b)subsets[b-1]|=1<<a;}return subsets;}
const BASIS=Array.from({length:256},(_,code)=>maskBasis(code));
const PERMS=[[[0,1,2],1],[[0,2,1],-1],[[1,0,2],-1],[[1,2,0],1],[[2,0,1],1],[[2,1,0],-1]];
function choose(n,k,start=0,prefix=[],out=[]){if(!k){out.push(prefix);return out;}for(let i=start;i<=n-k;i++)choose(n,k-1,i+1,[...prefix,i],out);return out;}
function makeOrderedMaskMoment(R,lambda){
  const sum=A=>A.reduce(R.add,R.zero),feature=lambda.map(row=>Array.from({length:16},(_,s)=>row.map((v,m)=>(m&s)===s?v:R.zero)));
  function pair(A,B){let prefix=R.zero,total=R.zero;for(let m=0;m<16;m++){total=R.add(total,R.mul(prefix,B[m]));prefix=R.add(prefix,A[m]);}return total;}
  const cache=new Map();
  return function moment(type,rows,code){
    const key=type+':'+rows.join(',')+':'+code;if(cache.has(key))return cache.get(key);
    const f=rows.map((row,r)=>feature[row][BASIS[code][r]]);let value;
    if(type===0)value=R.mul(R.mul(sum(f[0]),sum(f[1])),sum(f[2]));
    else if(type===1)value=R.mul(pair(f[0],f[1]),sum(f[2]));
    else if(type===2)value=R.mul(sum(f[0]),pair(f[1],f[2]));
    else{let p=R.zero,q=R.zero,total=R.zero;for(let m=0;m<16;m++){total=R.add(total,R.mul(q,f[2][m]));q=R.add(q,R.mul(p,f[1][m]));p=R.add(p,f[0][m]);}value=total;}
    cache.set(key,value);return value;
  };
}
function contractResidualMoments({ring:R,kappa,lambda,coefficients,minCarrier=kappa.length-3}){
  // coefficients(C,D,E) returns256 normalized ROW 2x2 matrices:
  // C(mask0,mask1,mask2)=sum_code coefficient[code]*basis[code].
  // Carrier triples are weakly increasing. Raw formulas are used to define this
  // polynomial only; strict mask order is imposed here for tied carriers.
  const m=kappa.length,nCarrier=kappa[0].length,rows3=choose(m,3),moment=makeOrderedMaskMoment(R,lambda),out=new Map();
  const zeroMatrix=()=>Array.from({length:2},()=>[R.zero,R.zero]);
  for(let C=minCarrier;C<nCarrier;C++){
    const byRows=new Map(rows3.map(rows=>[rows.reduce((s,r)=>s|(1<<r),0),zeroMatrix()]));out.set(C,byRows);
    for(let D=C;D<nCarrier;D++)for(let E=D;E<nCarrier;E++){
      const type=(C===D?1:0)+(D===E?2:0),coef=coefficients(C,D,E);
      for(const rows of rows3){
        const target=byRows.get(rows.reduce((s,r)=>s|(1<<r),0));
        const terms=PERMS.map(([p,sign])=>{const r=p.map(i=>rows[i]);let w=R.mul(R.mul(kappa[r[0]][C],kappa[r[1]][D]),kappa[r[2]][E]);if(sign<0)w=R.neg(w);return{r,w};});
        for(let code=0;code<256;code++){
          let w=R.zero;for(const t of terms)w=R.add(w,R.mul(t.w,moment(type,t.r,code)));
          for(let a=0;a<2;a++)for(let b=0;b<2;b++)target[a][b]=R.add(target[a][b],R.mul(w,coef[code][a][b]));
        }
      }
    }
  }
  return out;
}
function prefixContributions({ring:R,kappa,moments}){
  // Returns unembedded row2x2 moments labeled by the ordered anchor carriers
  // and residual first carrier. Embed as I_C transpose(matrix) P_C, then apply
  // h_anchors in composition order. The totalization sign is already included.
  const m=kappa.length,r=m-3;if(r<0||r>2)throw Error('Supported source degrees2..4');
  const full=(1<<m)-1,out=[];
  for(const[C,byRows]of moments)for(const anchors of choose(C,r)){
    const matrix=Array.from({length:2},()=>[R.zero,R.zero]);
    for(const[bits,M]of byRows){
      const rest=full^bits,rows=Array.from({length:m},(_,i)=>i).filter(i=>rest&(1<<i));let s=0;
      for(const a of rows)for(let b=0;b<a;b++)if(bits&(1<<b))s^=1;
      let w=R.one;if(r===1)w=kappa[rows[0]][anchors[0]];
      if(r===2)w=R.add(R.mul(kappa[rows[0]][anchors[0]],kappa[rows[1]][anchors[1]]),R.neg(R.mul(kappa[rows[0]][anchors[1]],kappa[rows[1]][anchors[0]])));
      if(s^(r*(r-1)/2%2))w=R.neg(w);
      for(let a=0;a<2;a++)for(let b=0;b<2;b++)matrix[a][b]=R.add(matrix[a][b],R.mul(w,M[a][b]));
    }
    out.push({anchors,residualCarrier:C,matrix});
  }
  return out;
}
module.exports={maskBasis,makeOrderedMaskMoment,contractResidualMoments,prefixContributions};
