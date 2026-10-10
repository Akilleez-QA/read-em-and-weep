#!/usr/bin/env node
'use strict';

// Exact Q-linear membership in the full-sign degree-two finite HM complex.
// Source pin: PR #5, add03476d9055aa00e1e00778eea6332cf8e01cc.
// No geometric residual is constructed or assumed by this program.
const fs = require('node:fs');
const crypto = require('node:crypto');
const assert = require('node:assert/strict');
const SOURCE_COMMIT = 'add03476d9055aa00e1e00778eea6332cf8e01cc';
const BASIS = 'hm-pr5-full-sign-harmonic-v1';
const ranks = [5, 15, 10, 2];
const checked = n => { if (!Number.isSafeInteger(n)) throw Error('Unsafe integer'); return n; };
function add(M, k, z) {
  if (!z) return;
  const v = (M.get(k) || (typeof z === 'bigint' ? 0n : 0)) + z;
  if (typeof v === 'number') checked(v);
  if (v) M.set(k, v); else M.delete(k);
}
function mons(lo, hi) {
  const out = [];
  for (let a=lo;a<=hi;a++) for (let b=lo;b<=hi;b++)
    for (let c=lo;c<=hi;c++) for (let d=lo;d<=hi;d++) out.push([a,b,c,d]);
  return out;
}
const subsets = Array.from({length:5},()=>[]);
for (let s=0;s<16;s++) {
  const e = [0,1,2,3].map(i=>(s>>i)&1);
  subsets[e.reduce((a,b)=>a+b,0)].push(e);
}
const wp=i=>[(i+2)%5,(i+3)%5], wm=i=>[(i+1)%5,(i+4)%5];
function epsilon(a) {
  if (new Set(a).size!==5) return 0;
  let n=0; for(let i=0;i<5;i++) for(let j=i+1;j<5;j++) n+=a[i]>a[j];
  return n%2 ? -1 : 1;
}
const d = Array.from({length:3},(_,l)=>Array.from({length:ranks[l]},()=>[]));
for (let a=0;a<5;a++) for(let r=0;r<15;r++) for(let k=0;k<5;k++) {
  const z=epsilon([k,...(r<5||r>=10?wp(a):wm(a)),...(r<5?wp(r):r<10?wm(r-5):wm(r-10))]);
  if(z) d[0][a].push([r,k,z]);
}
function form(c,h,[p,q]) { d[1][c].push([5*h+q,p,1],[5*h+p,q,-1]); }
for(let i=0;i<5;i++) { form(i,0,wp(i)); form(i+5,1,wm(i)); form(i+10,0,wm(i)); form(i+10,1,wp(i)); }
for(let b=0;b<2;b++) for(let k=0;k<5;k++) d[2][b*5+k].push([b,k,1]);
const incoming=d.map((cols,l)=>Array.from({length:ranks[l+1]},(_,r)=>
  cols.flatMap((ts,c)=>ts.filter(t=>t[0]===r).map(t=>[c,t[1],t[2]]))));
for(let l=0;l<2;l++) for(let a=0;a<ranks[l];a++) {
  const M=new Map();
  for(const [b,k,z] of d[l][a]) for(const [c,j,w] of d[l+1][b]) add(M,[c,Math.min(k,j),Math.max(k,j)].join(','),z*w);
  assert.equal(M.size,0,'K differential squares to zero');
}

function blocks(r) {
  const out=[];
  for(let u=0;u<4;u++) {const v=u+r;if(v>=0&&v<4) out.push([u,v]);}
  return out;
}
function makeBasis(r,p) {
  const out=[];
  const n=r-2;
  const exponents=p===4?mons(n+1,-1):mons(0,n);
  for(const [u,v] of blocks(r)) for(let a=0;a<ranks[v];a++) for(let b=0;b<ranks[u];b++)
    for(const e of exponents) out.push([u,v,a,b,...e]);
  return out;
}
const basis={
  source:makeBasis(-3,4), negative:makeBasis(-2,4), positive:makeBasis(2,0),
  outNegative:makeBasis(-1,4), outPositive:makeBasis(3,0)
};
const indexes=Object.fromEntries(Object.entries(basis).map(([k,bs])=>[k,new Map(bs.map((b,i)=>[b.join(','),i]))]));
assert.deepEqual(Object.fromEntries(Object.entries(basis).map(([k,v])=>[k,v.length])),
  {source:2560,negative:6480,positive:80,outNegative:3920,outPositive:160});
function stateVector(vector,which,p) {
  const out=new Map();
  for(let j=0;j<vector.length;j++) if(vector[j]) {
    const [u,v,a,b,...e]=basis[which][j];
    out.set([u,v,a,b,p===4?0:15,...e].join(','),BigInt(vector[j]));
  }
  return out;
}
function vectorFromState(M,which) {
  const out=Array(basis[which].length).fill(0n);
  for(const [key,z] of M) {
    const [u,v,a,b,mask,...e]=key.split(',').map(Number);
    const i=indexes[which].get([u,v,a,b,...e].join(','));
    assert.notEqual(i,undefined,`Bad harmonic output ${which}: ${key}`);
    assert.equal(mask,which==='positive'||which==='outPositive'?15:0);
    out[i]+=z;
  }
  return out;
}
// Only B/C chart states are needed: an A state is killed by final projection,
// and neither Delta nor H can turn an A state back into B or C.
// mask bit 1 = B, bit 0 = C; p = 4-popcount(mask).
function delta(M,r,step,steps,lo,hi) {
  const R=new Map(), rightSign=r%2===0?-1:1, left=steps-step;
  for(const [key,value] of M) {
    const [u,v,a,b,mask,...e]=key.split(',').map(Number);
    let p=4; for(let j=0;j<4;j++) p-=(mask>>j)&1;
    const totalSign=p%2?-1:1;
    function emit(uu,vv,aa,bb,k,z) {
      for(const sm of subsets[k]) {
        const ee=e.map((x,j)=>x+sm[j]);
        // A remaining Delta can only add zero or one to each exponent.
        if(ee.some(x=>x<lo-left||x>hi)) continue;
        add(R,[uu,vv,aa,bb,mask,...ee].join(','),value*BigInt(z*totalSign));
      }
    }
    if(v<3) for(const [c,k,z] of d[v][a]) emit(u,v+1,c,b,k,z);
    if(u>0) for(const [c,k,z] of incoming[u-1][b]) emit(u-1,v,a,c,k,z*rightSign);
  }
  return R;
}
function homotopy(M,r) {
  const R=new Map(), n=r-2;
  for(const [key,value] of M) {
    const [u,v,a,b,mask,...e]=key.split(',').map(Number);
    for(let j=0;j<4;j++) {
      if((mask>>j)&1||e[j]>=0||e[j]>n) continue;
      let good=true,cBefore=0;
      for(let i=0;i<j;i++) {
        if((mask>>i)&1) {if(e[i]<0||e[i]>n) good=false;}
        else {cBefore++;if(e[i]<=n||e[i]>=0) good=false;}
      }
      if(good) add(R,[u,v,a,b,mask|(1<<j),...e].join(','),value*(cBefore%2?-1n:1n));
    }
  }
  return R;
}
function transfer(vector,which,r,p,steps,target,lo,hi) {
  let M=stateVector(vector,which,p);
  for(let step=1;step<=steps;step++) {
    M=delta(M,r+step-1,step,steps,lo,hi);
    if(step<steps) M=homotopy(M,r+step);
  }
  // D_fin = p Delta sum_j (-H Delta)^j i.
  if((steps-1)%2) for(const [k,v] of M) M.set(k,-v);
  return vectorFromState(M,target);
}
function sourceD1(v) {return transfer(v,'source',-3,4,1,'negative',-3,-1);}
function sourceD5(v) {return transfer(v,'source',-3,4,5,'positive',0,0);}
function outgoingD1(v) {return transfer(v,'negative',-2,4,1,'outNegative',-2,-1);}
function outgoingD5(v) {return transfer(v,'negative',-2,4,5,'outPositive',0,1);}
function positiveD1(v) {return transfer(v,'positive',2,0,1,'outPositive',0,1);}

// Independent unpruned A/B/C tensor contraction, used only for validation.
// chart[j] is 0=A, 1=B, 2=C. Unlike the production path this keeps A terms,
// includes every H0 diagonal chart, and applies no exponent bounds.
function unprunedTransfer(vector,which,r,p,steps,target) {
  let M=new Map();
  for(let i=0;i<vector.length;i++) if(vector[i]) {
    const [u,v,a,b,...e]=basis[which][i];
    if(p===4) add(M,[u,v,a,b,2,2,2,2,...e].join(','),BigInt(vector[i]));
    else for(let s=0;s<16;s++) add(M,[u,v,a,b,...[0,1,2,3].map(j=>(s>>j)&1),...e].join(','),BigInt(vector[i]));
  }
  function fullDelta(input,rr) {
    const out=new Map();
    for(const [key,z] of input) {
      const parts=key.split(',').map(Number),[u,v,a,b]=parts,c=parts.slice(4,8),e=parts.slice(8);
      const sign=c.filter(x=>x===2).length%2?-1:1,right=rr%2===0?-1:1;
      function emit(uu,vv,aa,bb,k,w) {for(const sm of subsets[k]) add(out,[uu,vv,aa,bb,...c,...e.map((x,j)=>x+sm[j])].join(','),z*BigInt(sign*w));}
      if(v<3)for(const [a1,k,w] of d[v][a])emit(u,v+1,a1,b,k,w);
      if(u>0)for(const [b1,k,w] of incoming[u-1][b])emit(u-1,v,a,b1,k,w*right);
    }return out;
  }
  function fullH(input,rr) {
    const out=new Map(),n=rr-2;
    for(const [key,z] of input) {
      const parts=key.split(',').map(Number),head=parts.slice(0,4),c=parts.slice(4,8),e=parts.slice(8);
      for(let j=0;j<4;j++) {
        if(c[j]!==2)continue;
        let hs=0,hc=-1;
        if(e[j]>=0){hs=-1;hc=0;}else if(e[j]<=n){hs=1;hc=1;}
        if(!hs)continue;
        let partial=[[]],good=true,cs=0;
        for(let i=0;i<j;i++) {
          if(c[i]===0){good=false;break;}
          if(c[i]===1){if(e[i]<0||e[i]>n){good=false;break;}partial=partial.flatMap(a=>[[...a,0],[...a,1]]);}
          else {if(e[i]<=n||e[i]>=0){good=false;break;}partial=partial.map(a=>[...a,2]);cs++;}
        }
        if(good)for(const prefix of partial)add(out,[...head,...prefix,hc,...c.slice(j+1),...e].join(','),z*BigInt(hs*(cs%2?-1:1)));
      }
    }return out;
  }
  for(let step=1;step<=steps;step++){M=fullDelta(M,r+step-1);if(step<steps)M=fullH(M,r+step);}
  const out=Array(basis[target].length).fill(0n),n=r+steps-2;
  for(const [key,z] of M) {
    const parts=key.split(',').map(Number),head=parts.slice(0,4),c=parts.slice(4,8),e=parts.slice(8);
    if(c.some((x,j)=>x===0||(x===1?(e[j]<0||e[j]>n):(e[j]<=n||e[j]>=0))))continue;
    const i=indexes[target].get([...head,...e].join(','));assert.notEqual(i,undefined,'unpruned harmonic target');out[i]+=z*((steps-1)%2?-1n:1n);
  }return out;
}

function validateTransfers(exhaustive=false) {
  const start=Date.now();let comparisons=0,nonzero=0;
  for(const [which,r,p,steps,target,lo,hi,indices] of [
    ['source',-3,4,1,'negative',-3,-1,[0,73,512,1024,1801,2559]],
    ['source',-3,4,5,'positive',0,0,[0,73,512,1024,1801,2559]],
    ['negative',-2,4,1,'outNegative',-2,-1,[0,17,81,1200,2300,4050,6480-1]],
    ['negative',-2,4,5,'outPositive',0,1,[0,17,81,1200,2300,4050,6480-1]],
    ['positive',2,0,1,'outPositive',0,1,[0,17,50,79]]
  ])for(const j of indices) {
    const x=Array(basis[which].length).fill(0n);x[j]=1n;
    const expected=unprunedTransfer(x,which,r,p,steps,target),actual=transfer(x,which,r,p,steps,target,lo,hi);
    assert.deepEqual(actual,expected,`Unpruned comparison ${which} ${steps} ${j}`);
    comparisons++;if(actual.some(z=>z))nonzero++;
  }
  // Include every nonzero higher-boundary kernel direction, not zero-only samples.
  for(const x of prepare().K) {
    const expected=unprunedTransfer(x,'source',-3,4,5,'positive');assert.deepEqual(sourceD5(x),expected);
    comparisons++;if(expected.some(z=>z))nonzero++;
  }
  let chainColumns=0;
  const ids=exhaustive?Array.from({length:2560},(_,i)=>i):[0,73,512,1024,1801,2559];
  for(const j of ids) {
    const x=Array(2560).fill(0n);x[j]=1n;
    const a=sourceD1(x),t=sourceD5(x),low=outgoingD1(a),high=outgoingD5(a),ct=positiveD1(t);
    assert(low.every(z=>!z),`D2 D1 negative column ${j}`);
    assert(high.every((z,i)=>z+ct[i]===0n),`D2 D1 positive column ${j}`);chainColumns++;
  }
  return {passed:true,unpruned_comparisons:comparisons,nonzero_comparisons:nonzero,chain_identity_columns:chainColumns,
    chain_identity_exhaustive:exhaustive,milliseconds:Date.now()-start};
}

function certifyFullSignDimension() {
  const start=Date.now(),rows=Array.from({length:4080},()=>new Map());
  for(let j=0;j<6480;j++) {
    const v=Array(6480).fill(0n);v[j]=1n;
    const lo=outgoingD1(v),hi=outgoingD5(v);
    for(let i=0;i<3920;i++)if(lo[i]){const z=checked(Number(lo[i]));assert.equal(BigInt(z),lo[i]);rows[i].set(j,z);}
    for(let i=0;i<160;i++)if(hi[i]){const z=checked(Number(hi[i]));assert.equal(BigInt(z),hi[i]);rows[3920+i].set(j,z);}
  }
  for(let j=0;j<80;j++) {
    const v=Array(80).fill(0n);v[j]=1n;const hi=positiveD1(v);
    for(let i=0;i<160;i++)if(hi[i]){const z=checked(Number(hi[i]));assert.equal(BigInt(z),hi[i]);rows[3920+i].set(6480+j,z);}
  }
  const E=exactRank(rows,6560),{EA,ET}=prepare(),h2=6560-E.rank-EA.rank-ET.rank;
  assert.equal(E.rank,3648);assert.equal(h2,352);
  return {passed:true,coefficient_field:'Q',sector:'full-sign',outgoing_shape:[4080,6560],outgoing_rank:E.rank,
    outgoing_nonzeros:rows.reduce((n,r)=>n+r.size,0),rank_certificate:E,cycle_dimension:6560-E.rank,
    boundary_rank:EA.rank+ET.rank,ext2_dimension:h2,milliseconds:Date.now()-start};
}

// Rank-only fraction-free fallback. The boundary solvers use unit pivots;
// this optional full outgoing-rank check need not force that pivot order.
function exactRank(input,ncols) {
  const rows=input.map(r=>new Map(r));let rank=0,c=0,max=1;
  for(;c<ncols;c++) {
    let p=rank;while(p<rows.length&&Math.abs(rows[p].get(c)||0)!==1)p++;
    if(p===rows.length){if(rows.slice(rank).some(r=>r.get(c)))break;continue;}
    [rows[rank],rows[p]]=[rows[p],rows[rank]];const pivot=rows[rank];
    if(pivot.get(c)===-1)for(const [j,z] of pivot)pivot.set(j,-z);
    for(let i=rank+1;i<rows.length;i++) {
      const m=rows[i].get(c);if(!m)continue;
      for(const [j,z] of pivot){const value=checked((rows[i].get(j)||0)-checked(m*z));if(value)rows[i].set(j,value);else rows[i].delete(j);max=Math.max(max,Math.abs(value));}
    }rank++;
  }
  const unitRank=rank,tail=rows.slice(rank).filter(r=>r.size).map(r=>new Map([...r].map(([j,z])=>[j,BigInt(z)])));
  let trank=0,maxBits=0;
  for(;c<ncols;c++) {
    let p=trank;while(p<tail.length&&!tail[p].get(c))p++;
    if(p===tail.length)continue;
    [tail[trank],tail[p]]=[tail[p],tail[trank]];const pivot=tail[trank],a=pivot.get(c);
    for(let i=trank+1;i<tail.length;i++) {
      const b=tail[i].get(c);if(!b)continue;const g=gcd(a,b),m=a/g,n=b/g;
      for(const [j,z] of tail[i])tail[i].set(j,z*m);
      for(const [j,z] of pivot)add(tail[i],j,-n*z);
      let content=0n;for(const z of tail[i].values())content=gcd(content,z);
      if(content>1n)for(const [j,z] of tail[i])tail[i].set(j,z/content);
      for(const z of tail[i].values())maxBits=Math.max(maxBits,(z<0n?-z:z).toString(2).length);
    }trank++;
  }
  assert(tail.slice(trank).every(r=>!r.size),'Nonzero exact rank residual');
  return {rank:unitRank+trank,unit_rank:unitRank,fraction_free_tail_rank:trank,unit_max:max,tail_max_bits:maxBits};
}

function integerRows(nrows,columns) {
  const out=Array.from({length:nrows},()=>new Map());
  for(let j=0;j<columns.length;j++) for(let i=0;i<columns[j].length;i++) if(columns[j][i]) {
    const z=Number(columns[j][i]); assert.equal(BigInt(checked(z)),columns[j][i]); out[i].set(j,z);
  }
  return out;
}
function initialMatrix() {
  const A=Array.from({length:6480},()=>new Map());
  // Degree-one source has p=4 and odd r, so both commutator terms have + sign.
  for(let col=0;col<2560;col++) {
    const [u,v,a,b,...e]=basis.source[col];
    function emit(uu,vv,aa,bb,k,z) {
      for(const sm of subsets[k]) {
        const ee=e.map((x,j)=>x+sm[j]); if(ee.some(x=>x<-3||x>-1)) continue;
        add(A[indexes.negative.get([uu,vv,aa,bb,...ee].join(','))],col,z);
      }
    }
    for(const [c,k,z] of d[v][a]) emit(u,v+1,c,b,k,z);
    for(const [c,k,z] of incoming[u-1][b]) emit(u-1,v,a,c,k,z);
  }
  return A;
}
class UnitEchelon {
  constructor(input,ncols) {
    this.rows=input.map(r=>new Map(r)); this.ops=[]; this.pivots=[]; this.ncols=ncols;
    let rank=0,max=1;
    for(let c=0;c<ncols;c++) {
      let r=rank; while(r<this.rows.length&&Math.abs(this.rows[r].get(c)||0)!==1) r++;
      if(r===this.rows.length) {
        if(this.rows.slice(rank).some(row=>row.get(c))) throw Error('Nonunit pivot: this model requires an exact rational matrix fallback');
        continue;
      }
      if(r!==rank) { [this.rows[r],this.rows[rank]]=[this.rows[rank],this.rows[r]]; this.ops.push([0,r,rank]); }
      const ar=this.rows[rank];
      if(ar.get(c)===-1) {for(const [j,z] of ar) ar.set(j,-z);this.ops.push([1,rank]);}
      for(let i=rank+1;i<this.rows.length;i++) {
        const m=this.rows[i].get(c);if(!m) continue;
        for(const [j,z] of ar) {const zz=checked((this.rows[i].get(j)||0)-checked(m*z));if(zz)this.rows[i].set(j,zz);else this.rows[i].delete(j);max=Math.max(max,Math.abs(zz));}
        this.ops.push([2,i,rank,m]);
      }
      this.pivots.push(c);rank++;
    }
    assert(this.rows.slice(rank).every(r=>!r.size));this.rank=rank;this.max=max;
    this.input=input;
  }
  solve(rhs) {
    assert.equal(rhs.length,this.rows.length);
    const b=rhs.map(BigInt);
    for(const [op,i,j,m] of this.ops) {
      if(op===0) [b[i],b[j]]=[b[j],b[i]];
      else if(op===1) b[i]=-b[i];
      else b[i]-=BigInt(m)*b[j];
    }
    const failures=[];
    for(let i=this.rank;i<b.length;i++) if(b[i]) failures.push([i,b[i].toString()]);
    if(failures.length) return {ok:false,failures};
    const x=Array(this.ncols).fill(0n);
    for(let i=this.rank-1;i>=0;i--) {
      let z=b[i];const c=this.pivots[i];
      for(const [j,a] of this.rows[i]) if(j!==c) z-=BigInt(a)*x[j];
      x[c]=z;
    }
    assert.deepEqual(matvec(this.input,x),rhs.map(BigInt),'Exact solve witness failed');
    return {ok:true,x};
  }
  kernel() {
    const P=new Set(this.pivots),K=[];
    for(let f=0;f<this.ncols;f++) if(!P.has(f)) {
      const x=Array(this.ncols).fill(0n); x[f]=1n;
      for(let i=this.rank-1;i>=0;i--) {
        let z=0n;const c=this.pivots[i];
        for(const [j,a] of this.rows[i]) if(j!==c) z+=BigInt(a)*x[j];
        x[c]=-z;
      }
      assert(matvec(this.input,x).every(z=>z===0n));K.push(x);
    }
    return K;
  }
  annihilator(row) {
    assert(row>=this.rank&&row<this.rows.length,'Annihilator must come from a zero echelon row');
    const w=new Map([[row,1n]]);
    for(let k=this.ops.length-1;k>=0;k--) {
      const [op,i,j,m]=this.ops[k];
      if(op===0) {const a=w.get(i)||0n,b=w.get(j)||0n;w.delete(i);w.delete(j);if(a)w.set(j,a);if(b)w.set(i,b);}
      else if(op===1) {if(w.has(i))w.set(i,-w.get(i));}
      else if(w.has(i)) add(w,j,-BigInt(m)*w.get(i));
    }
    const check=new Map();for(const [i,z] of w)for(const [j,a] of this.input[i])add(check,j,z*BigInt(a));
    assert.equal(check.size,0,'Nonmembership annihilator does not annihilate matrix');
    return w;
  }
}
function matvec(A,x) {return A.map(row=>{let z=0n;for(const [j,a] of row) z+=BigInt(a)*x[j];return z;});}
function gcd(a,b) {a=a<0n?-a:a;b=b<0n?-b:b;while(b)[a,b]=[b,a%b];return a;}
function parseQ(x) {
  if(typeof x==='number') {if(!Number.isSafeInteger(x))throw Error('JSON numbers must be safe integers; use strings for rationals');return [BigInt(x),1n];}
  if(typeof x!=='string'||!/^[-+]?\d+(\/[1-9]\d*)?$/.test(x)) throw Error(`Invalid rational: ${x}`);
  const s=x.split('/'),n=BigInt(s[0]),d=s.length===2?BigInt(s[1]):1n,g=gcd(n,d);return [n/g,d/g];
}
function rationalString(n,d=1n) {const g=gcd(n,d);n/=g;d/=g;return d===1n?n.toString():`${n}/${d}`;}
function parseInput(input) {
  if(input.basis!==undefined) assert.equal(input.basis,BASIS);
  if(input.source_commit!==undefined) assert.equal(input.source_commit,SOURCE_COMMIT);
  let n=input.negative,p=input.positive;
  if(input.entries!==undefined) {
    assert(n===undefined&&p===undefined,'Choose dense blocks or sparse entries');
    n=Array(6480).fill('0');p=Array(80).fill('0');const seen=new Set();
    for(const entry of input.entries) {
      assert(Array.isArray(entry.key)&&entry.key.length===8);
      const k=entry.key.join(',');assert(!seen.has(k),'Duplicate sparse basis key');seen.add(k);
      if(indexes.negative.has(k))n[indexes.negative.get(k)]=entry.coefficient;
      else if(indexes.positive.has(k))p[indexes.positive.get(k)]=entry.coefficient;
      else throw Error(`Invalid full-sign degree-two basis key ${k}`);
    }
  }
  assert(Array.isArray(n)&&n.length===6480,'negative must have 6480 entries');
  assert(Array.isArray(p)&&p.length===80,'positive must have 80 entries');
  const all=n.concat(p).map(parseQ);let denominator=1n;
  for(const [,d] of all) denominator=denominator/gcd(denominator,d)*d;
  const v=all.map(([n,d])=>n*(denominator/d));
  return {negative:v.slice(0,6480),positive:v.slice(6480),denominator};
}
function nonzeros(v,denominator=1n,which) {
  const out=[];for(let i=0;i<v.length;i++) if(v[i]) {
    const e={index:i,coefficient:rationalString(v[i],denominator)};
    if(which)e.key=basis[which][i];out.push(e);
  }return out;
}
function sparseInput(n,p,denominator=1n) {
  return {basis:BASIS,source_commit:SOURCE_COMMIT,entries:
    [...nonzeros(n,denominator,'negative'),...nonzeros(p,denominator,'positive')].map(({key,coefficient})=>({key,coefficient}))};
}
function hash(v) {return crypto.createHash('sha256').update(JSON.stringify(v,(_,x)=>typeof x==='bigint'?x.toString():x)).digest('hex');}
let prepared;
function prepare() {
  if(prepared)return prepared;
  const A=initialMatrix(),EA=new UnitEchelon(A,2560),K=EA.kernel();
  assert.equal(EA.rank,2550);assert.equal(K.length,10);
  const T=K.map(sourceD5),ET=new UnitEchelon(integerRows(80,T),10);
  assert.equal(ET.rank,10);
  for(const t of T)assert(positiveD1(t).every(x=>!x),'Length-five kernel boundary is closed');
  prepared={A,EA,K,T,ET};return prepared;
}
function check(input) {
  const {negative:n,positive:p,denominator}=parseInput(input);
  const {EA,K,ET}=prepare();
  const dn=outgoingD1(n), cp=positiveD1(p), dp=outgoingD5(n).map((z,i)=>z+cp[i]);
  const result={basis:BASIS,source_commit:SOURCE_COMMIT,input_sha256:hash(input),
    coefficient_field:'Q',is_cocycle:dn.every(x=>!x)&&dp.every(x=>!x),is_boundary:false,
    model:{degree1:2560,degree2:6560,degree3:4080,initial_boundary_rank:EA.rank,length5_kernel_rank:ET.rank,boundary_rank:2560}};
  if(!result.is_cocycle) {
    result.status='not_a_cocycle';result.differential={negative:nonzeros(dn,denominator,'outNegative'),positive:nonzeros(dp,denominator,'outPositive')};return result;
  }
  const s=EA.solve(n);
  if(!s.ok) {
    result.status='nonzero_cohomology_class';result.obstruction_stage='negative_block_not_in_image_d1';
    result.echelon_residual=s.failures.map(([i,z])=>[i,rationalString(BigInt(z),denominator)]);
    const w=EA.annihilator(s.failures[0][0]);let pairing=0n;for(const [i,z] of w)pairing+=z*n[i];assert(pairing!==0n);
    result.nonmembership_witness={type:'negative_block_annihilator',functional:[...w].sort((a,b)=>a[0]-b[0]).map(([index,z])=>({index,coefficient:z.toString(),key:basis.negative[index]})),
      pairing:rationalString(pairing,denominator),verified_annihilates_initial_boundary_matrix:true};return result;
  }
  const d5=sourceD5(s.x),remainder=p.map((z,i)=>z-d5[i]),t=ET.solve(remainder);
  if(!t.ok) {
    result.status='nonzero_cohomology_class';result.obstruction_stage='positive_correction_not_in_d5_kernel_image';
    result.echelon_residual=t.failures.map(([i,z])=>[i,rationalString(BigInt(z),denominator)]);
    result.positive_remainder=nonzeros(remainder,denominator,'positive');
    const w=ET.annihilator(t.failures[0][0]);let pairing=0n;for(const [i,z] of w)pairing+=z*remainder[i];assert(pairing!==0n);
    result.nonmembership_witness={type:'positive_correction_annihilator',initial_preimage:nonzeros(s.x,denominator,'source'),
      functional:[...w].sort((a,b)=>a[0]-b[0]).map(([index,z])=>({index,coefficient:z.toString(),key:basis.positive[index]})),
      pairing:rationalString(pairing,denominator),verified_annihilates_length5_kernel_image:true};return result;
  }
  const x=s.x.slice();
  for(let j=0;j<K.length;j++) if(t.x[j]) for(let i=0;i<x.length;i++) x[i]+=t.x[j]*K[j][i];
  assert.deepEqual(sourceD1(x),n,'Boundary witness negative block');
  assert.deepEqual(sourceD5(x),p,'Boundary witness length-five block');
  result.is_boundary=true;result.status='boundary';result.preimage=nonzeros(x,denominator,'source');return result;
}

function selfTest(writeDirectory) {
  const start=Date.now(),{A,EA,K,T,ET}=prepare();
  const aw=EA.annihilator(EA.rank),arhs=Array(6480).fill(0n);
  assert(aw.size>0);arhs[aw.keys().next().value]=1n;
  assert.equal(EA.solve(arhs).ok,false,'Negative-block nonmembership linear solver control');
  const reference=require('node:vm').runInNewContext(fs.readFileSync(__dirname+'/pinned-verify-hm-ext.js','utf8')
    .replace('const summaries=[];','return {negativeD1,echelon,run}; const summaries=[];'));
  const old=reference.negativeD1(4);
  assert.equal(old.A.length,A.length);
  for(let i=0;i<A.length;i++) assert.equal(JSON.stringify([...A[i]].sort((a,b)=>a[0]-b[0])),JSON.stringify([...old.A[i]].sort((a,b)=>a[0]-b[0])));
  const oldK=reference.echelon(old.A,2560).kernel;
  assert.equal(oldK.length,10);
  for(let j=0;j<K.length;j++) {
    assert.equal(JSON.stringify(K[j].map(String)),JSON.stringify(oldK[j].map(String)));
    const M=reference.run(oldK[j],old.src,4,5,15,[[0,0],[0,0],[0,0],[0,0]]),vv=Array(80).fill(0n);
    for(const [key,z] of M) {const [u,v,a,b,mask,...e]=key.split(',').map(Number);vv[indexes.positive.get([u,v,a,b,...e].join(','))]=BigInt(z);}
    assert.deepEqual(vv,T[j]);
  }
  const z=Array(6480).fill(0n),zeroP=Array(80).fill(0n);
  const controls={};
  const knownBoundary=sparseInput(z,T[0],7n), knownResult=check(knownBoundary);
  assert(knownResult.is_cocycle&&knownResult.is_boundary&&knownResult.preimage.length>0);
  controls.higher_boundary={input:knownBoundary,result:knownResult};
  const x=Array(2560).fill(0n); x[0]=2n;x[73]=-3n;x[1801]=5n;
  const generalBoundary=sparseInput(sourceD1(x),sourceD5(x),11n), generalResult=check(generalBoundary);
  assert(generalResult.is_cocycle&&generalResult.is_boundary);controls.general_boundary={input:generalBoundary,result:generalResult};
  const e=zeroP.slice();e[0]=1n;const bad=sparseInput(z,e),badResult=check(bad);
  assert.equal(badResult.status,'not_a_cocycle');controls.non_cocycle={input:bad,result:badResult};
  const zeroResult=check(sparseInput(z,zeroP));assert.equal(zeroResult.status,'boundary');
  // An independently solved positive-block kernel supplies a nonboundary control.
  const Ccols=[];
  for(let j=0;j<80;j++){const v=zeroP.slice();v[j]=1n;Ccols.push(positiveD1(v));}
  const EC=new UnitEchelon(integerRows(160,Ccols),80),CK=EC.kernel();
  let nonBoundary=null;
  for(const q of CK)if(!ET.solve(q).ok){nonBoundary=sparseInput(z,q);break;}
  assert(nonBoundary,'A positive-block nonboundary control exists');
  const nbResult=check(nonBoundary);assert.equal(nbResult.status,'nonzero_cohomology_class');
  controls.non_boundary={input:nonBoundary,result:nbResult};
  if(writeDirectory) {
    fs.mkdirSync(writeDirectory,{recursive:true});
    for(const [name,{input,result}] of Object.entries(controls)) {
      fs.writeFileSync(`${writeDirectory}/${name}.input.json`,JSON.stringify(input,null,2)+'\n');
      fs.writeFileSync(`${writeDirectory}/${name}.result.json`,JSON.stringify(result,null,2)+'\n');
    }
  }
  const summary={passed:true,basis:BASIS,source_commit:SOURCE_COMMIT,initial_matrix:[6480,2560],initial_rank:EA.rank,
    initial_kernel:K.length,higher_matrix:[80,10],higher_rank:ET.rank,boundary_rank:EA.rank+ET.rank,
    positive_outgoing_rank:EC.rank,positive_kernel:CK.length,unit_elimination_max:[EA.max,ET.max,EC.max],
    reference_checks:{initial_matrix_entries:'all',initial_kernel_vectors:10,length5_kernel_vectors:10},
    negative_block_nonmembership_annihilator_control:true,
    controls:Object.fromEntries(Object.entries(controls).map(([k,v])=>[k,{status:v.result.status,is_cocycle:v.result.is_cocycle,is_boundary:v.result.is_boundary}])),
    milliseconds:Date.now()-start};
  if(writeDirectory)fs.writeFileSync(`${writeDirectory}/self-test-results.json`,JSON.stringify(summary,null,2)+'\n');
  return summary;
}
if(require.main===module) {
  const args=process.argv.slice(2);
  if(args[0]==='--self-test') console.log(JSON.stringify(selfTest(args[1]),null,2));
  else if(args[0]==='--validate-transfers') console.log(JSON.stringify(validateTransfers(args[1]==='--exhaustive'),null,2));
  else if(args[0]==='--certify-dimension') console.log(JSON.stringify(certifyFullSignDimension(),null,2));
  else if(args[0]==='--basis') console.log(JSON.stringify({basis:BASIS,source_commit:SOURCE_COMMIT,bases:basis},null,2));
  else if(args.length===1) console.log(JSON.stringify(check(JSON.parse(fs.readFileSync(args[0],'utf8'))),null,2));
  else {console.error('Usage: node full-sign-boundary-oracle.js INPUT.json | --self-test [OUTPUT_DIRECTORY] | --validate-transfers [--exhaustive] | --basis');process.exitCode=2;}
}
module.exports={BASIS,SOURCE_COMMIT,basis,prepare,check,selfTest,validateTransfers,certifyFullSignDimension,sourceD1,sourceD5,outgoingD1,outgoingD5,positiveD1,sparseInput,UnitEchelon,integerRows,matvec};
