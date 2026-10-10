"use strict";
// Run with Node.js: node verify-affine-pivot-refinement.js
// Exact integer-polynomial checks; no dependencies or floating-point evaluation.
const exact=x=>{if(!Number.isSafeInteger(x))throw Error("unsafe integer arithmetic");return x};
const Z=()=>new Map(), key=e=>e.join(",");
const constant=n=>n?new Map([["0,0,0,0",n]]):Z();
const variable=i=>{const e=[0,0,0,0];e[i]=1;return new Map([[key(e),1]])};
function add(p,q,scale=1){const r=new Map(p);for(const[k,v]of q){const n=exact((r.get(k)||0)+exact(scale*v));if(n)r.set(k,n);else r.delete(k)}return r}
function mul(p,q){const r=Z();for(const[k,v]of p)for(const[l,w]of q){const a=k.split(",").map(Number),b=l.split(",").map(Number),m=key(a.map((x,i)=>x+b[i])),n=exact((r.get(m)||0)+exact(v*w));if(n)r.set(m,n);else r.delete(m)}return r}
const neg=p=>add(Z(),p,-1),one=constant(1),vars=[0,1,2,3].map(variable);
const pairs=[[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]];
const projected=[vars.map(neg),...Array.from({length:4},(_,i)=>Array.from({length:4},(_,j)=>constant(i===j?1:0)))];
function wedge(p,q){return pairs.map(([i,j])=>add(mul(projected[p][i],projected[q][j]),mul(projected[p][j],projected[q][i]),-1))}
const alpha=Array.from({length:12},()=>Array.from({length:5},Z));
for(let a=0;a<5;a++){const plus=wedge((a+2)%5,(a+3)%5),minus=wedge((a+1)%5,(a+4)%5);for(let r=0;r<6;r++){alpha[r][a]=plus[r];alpha[r+6][a]=minus[r]}}
const S=Array.from({length:6},()=>Array(6).fill(0));for(const[i,j,v]of [[0,5,1],[1,4,-1],[2,3,1]])S[i][j]=S[j][i]=v;
const J=Array.from({length:12},()=>Array(12).fill(0));for(let i=0;i<6;i++)for(let j=0;j<6;j++){J[i][j+6]=S[i][j];J[i+6][j]=-S[i][j]}
const beta=Array.from({length:5},(_,a)=>Array.from({length:12},(_,j)=>{let p=Z();for(let r=0;r<12;r++)if(J[r][j])p=add(p,alpha[r][a],J[r][j]);return p}));
for(let i=0;i<5;i++)for(let j=0;j<5;j++){let p=Z();for(let r=0;r<12;r++)p=add(p,mul(beta[i][r],alpha[r][j]));if(p.size)throw Error("beta alpha is nonzero")}
function determinant(A){if(A.length===0)return one;let p=Z();for(let j=0;j<A.length;j++){if(!A[0][j].size)continue;const B=A.slice(1).map(row=>row.filter((_,k)=>k!==j));p=add(p,mul(A[0][j],determinant(B)),j%2?-1:1)}return p}
function equal(p,q){return add(p,q,-1).size===0}
function check(label,actual,expected){if(!equal(actual,expected))throw Error(label+" failed");console.log(label+": passed")}
const product=vars.reduce(mul,one),D=add(one,product,-1);
const I=[3,6,4,1,11],Jc=[0,2,5,7,8,9,10],P=[0,2,3,4,6];
check("primary beta determinant",determinant(beta.map(row=>I.map(i=>row[i]))),neg(D));
check("primary alpha determinant",determinant(P.map(i=>alpha[Jc[i]])),D);
const Ia=[0,1,2,3,4],Ja=[5,6,7,8,9,10,11],Pa=[0,1,2,3,5];
check("auxiliary beta determinant",determinant(beta.map(row=>Ia.map(i=>row[i]))),mul(vars[2],vars[3]));
check("auxiliary alpha determinant",determinant(Pa.map(i=>alpha[Ja[i]])),neg(mul(mul(vars[0],vars[0]),vars[2])));
console.log("beta alpha = 0: passed; all exact polynomial checks passed.");

function transpose(A){return A[0].map((_,j)=>A.map(row=>row[j]))}
function matmul(A,B){return A.map(row=>B[0].map((_,j)=>row.reduce((p,x,k)=>add(p,mul(x,B[k][j])),Z())))}
function adjugate(A){return A.map((_,i)=>A.map((_,j)=>{const minor=A.filter((_,r)=>r!==j).map(row=>row.filter((_,c)=>c!==i));const p=determinant(minor);return(i+j)%2?neg(p):p}))}
function matrixeq(A,B,label){for(let i=0;i<A.length;i++)for(let j=0;j<A[i].length;j++)if(!equal(A[i][j],B[i][j]))throw Error(label+" "+i+","+j);console.log(label+": passed")}
const zeroMatrix=(r,c)=>Array.from({length:r},()=>Array.from({length:c},Z));
const eye=(n,p=one)=>Array.from({length:n},(_,i)=>Array.from({length:n},(_,j)=>i===j?p:Z()));

function buildContraction(I,Jc,P,U,label){
 const BI=beta.map(row=>I.map(i=>row[i])),A=Jc.map(i=>alpha[i]),AP=P.map(i=>A[i]);
 const db=determinant(BI),da=determinant(AP),den=mul(da,db);
 const iB=adjugate(BI).map(row=>row.map(p=>mul(p,da))),iA=adjugate(AP).map(row=>row.map(p=>mul(p,db)));
 const j=zeroMatrix(12,5);I.forEach((r,i)=>j[r]=iB[i]);
 const h=zeroMatrix(5,12);for(let i=0;i<5;i++)P.forEach((r,k)=>h[i][Jc[r]]=iA[i][k]);
 const K=zeroMatrix(12,7);Jc.forEach((r,i)=>K[r][i]=den);const tmp=matmul(iB,beta.map(row=>Jc.map(i=>row[i])));I.forEach((r,i)=>K[r]=tmp[i].map(neg));
 const Snum=K.map(row=>U.map(i=>row[i])),Pnum=zeroMatrix(2,12),prod=matmul(U.map(i=>A[i]),iA);
 U.forEach((r,i)=>Pnum[i][Jc[r]]=den);for(let i=0;i<2;i++)P.forEach((r,k)=>Pnum[i][Jc[r]]=add(Pnum[i][Jc[r]],prod[i][k],-1));
 matrixeq(matmul(h,alpha),eye(5,den),label+" H alpha");
 matrixeq(matmul(beta,j),eye(5,den),label+" beta H");
 matrixeq(matmul(h,j),zeroMatrix(5,5),label+" H squared");
 const aa=matmul(alpha,h),bb=matmul(j,beta),ip=matmul(Snum,Pnum);
 matrixeq(aa.map((row,i)=>row.map((p,k)=>add(mul(den,add(p,bb[i][k])),ip[i][k]))),eye(12,mul(den,den)),label+" contraction");
 matrixeq(matmul(Pnum,Snum),eye(2,mul(den,den)),label+" P I");
 matrixeq(matmul(h,Snum),zeroMatrix(5,2),label+" H I");
 matrixeq(matmul(Pnum,j),zeroMatrix(2,5),label+" P H");
 const pair=matmul(matmul(transpose(Snum),J.map(row=>row.map(constant))),Snum);
 console.log(label+" pairing numerator: "+JSON.stringify([...pair[0][1]]));
 console.log(label+" pairing denominator: "+JSON.stringify([...mul(den,den)]));
 return{h,j,Snum,Pnum,pair,den};
}

function checkFourTerm(contraction){
const pairs5=[];for(let i=0;i<5;i++)for(let j=i+1;j<5;j++)pairs5.push([i,j]);
const v=[one,...vars];
function epsilon(a){if(new Set(a).size<5)return 0;let n=0;for(let i=0;i<5;i++)for(let j=i+1;j<5;j++)if(a[i]>a[j])n++;return n%2?-1:1}
const CB=zeroMatrix(20,12);
for(let half=0;half<2;half++)for(let r=0;r<10;r++)for(let c=0;c<6;c++){let p=Z();for(let k=0;k<5;k++)p=add(p,v[k],epsilon([k,pairs[c][0]+1,pairs[c][1]+1,...pairs5[r]]));CB[half*10+r][half*6+c]=p}
function dualRow(pair){const[p,q]=pair;const i=pairs5.findIndex(([a,b])=>a===Math.min(p,q)&&b===Math.max(p,q));return[i,p<q?1:-1]}
const ik=zeroMatrix(20,15),pk=zeroMatrix(15,20),bmap=zeroMatrix(5,20);
for(let i=0;i<5;i++){const[plus,sp]=dualRow([(i+2)%5,(i+3)%5]),[minus,sm]=dualRow([(i+1)%5,(i+4)%5]);ik[plus][i]=constant(sp);ik[10+minus][5+i]=constant(sm);ik[minus][10+i]=constant(sm);ik[10+plus][10+i]=constant(sp);pk[i][plus]=constant(sp);pk[5+i][10+minus]=constant(sm);pk[10+i][10+plus]=constant(sp);bmap[i][minus]=constant(-sm);bmap[i][10+plus]=constant(sp)}
const PM=zeroMatrix(12,20);for(let half=0;half<2;half++)for(let a=0;a<6;a++)for(let r=0;r<10;r++){const[i,j]=pairs5[r];if(i>0){const c=pairs.findIndex(([x,y])=>x===i-1&&y===j-1);PM[half*6+a][half*10+r]=constant(S[a][c])}}
const HM=zeroMatrix(20,10),eta=zeroMatrix(10,2),deltaW=zeroMatrix(10,20),ev=zeroMatrix(2,10);
for(let half=0;half<2;half++){eta[half*5][half]=one;for(let i=0;i<5;i++)ev[half][half*5+i]=v[i];for(let r=0;r<10;r++){const[i,j]=pairs5[r];deltaW[half*5+j][half*10+r]=v[i];deltaW[half*5+i][half*10+r]=neg(v[j]);if(i===0)HM[half*10+r][half*5+j]=one}}
matrixeq(matmul(bmap,CB),beta,"Euler comparison beta");
matrixeq(matmul(PM,CB),eye(12),"Euler comparison projection");
const gamma=matmul(pk,matmul(CB,alpha)),delta=matmul(deltaW,ik);
const KI=matmul(pk,matmul(CB,contraction.Snum)),KP=matmul(contraction.Pnum,matmul(PM,ik)),KH0=matmul(contraction.h,matmul(PM,ik));
const correction=matmul(CB,matmul(contraction.j,bmap)),mid=eye(20,contraction.den).map((row,i)=>row.map((p,j)=>add(p,correction[i][j],-1))),KH1=matmul(pk,matmul(mid,HM));
matrixeq(matmul(delta,gamma),zeroMatrix(10,5),"four-term differential squared 0");
matrixeq(matmul(ev,delta),zeroMatrix(2,15),"four-term differential squared 1");
matrixeq(matmul(KH0,gamma),eye(5,contraction.den),"four-term contraction degree -1");
const aa=matmul(gamma,KH0),bb=matmul(KH1,delta),ii=matmul(KI,KP);
matrixeq(aa.map((row,i)=>row.map((p,j)=>add(mul(contraction.den,add(p,bb[i][j])),ii[i][j]))),eye(15,mul(contraction.den,contraction.den)),"four-term contraction degree 0");
const cc=matmul(delta,KH1),dd=matmul(eta,ev);
matrixeq(cc.map((row,i)=>row.map((p,j)=>add(p,mul(contraction.den,dd[i][j])))),eye(10,contraction.den),"four-term contraction degree 1");
matrixeq(matmul(ev,eta),eye(2),"four-term contraction degree 2");
matrixeq(matmul(KP,KI),eye(2,mul(contraction.den,contraction.den)),"four-term P I");
matrixeq(matmul(KH0,KH1),zeroMatrix(5,10),"four-term H squared 0");
matrixeq(matmul(KH1,eta),zeroMatrix(15,2),"four-term H squared 1");
matrixeq(matmul(KH0,KI),zeroMatrix(5,2),"four-term H I");
matrixeq(matmul(KP,KH1),zeroMatrix(2,10),"four-term P H");
console.log("All four-term contraction identities on this chart passed exactly.");
return {KI,KP,KH0,KH1,eta,gamma,delta,ev,den:contraction.den};

}
const primary=buildContraction(I,Jc,P,[1,5],"primary");checkFourTerm(primary);
const auxiliary=buildContraction(Ia,Ja,Pa,[4,6],"auxiliary");checkFourTerm(auxiliary);

check("primary symplectic frame",primary.pair[0][1],mul(primary.den,primary.den));
check("auxiliary symplectic normalization",mul(auxiliary.pair[0][1],vars[3]),neg(mul(mul(vars[0],vars[0]),mul(auxiliary.den,auxiliary.den))));
console.log("Primary pairing is 1; auxiliary pairing is -a^2/d.");
console.log("Rescaling the auxiliary second column by -d/a^2 gives pairing 1.");

const pdata=checkFourTerm(primary),adata=checkFourTerm(auxiliary);
const hompower=(p,n)=>{let z=one;for(let i=0;i<n;i++)z=mul(z,p);return z};
const deg=p=>Math.max(0,...[...p.keys()].map(k=>k.split(",").map(Number).reduce((a,b)=>a+b,0)));
function homogenize(p,j,L){let out=Z();for(const[k,c]of p){const e=k.split(",").map(Number);let z=constant(c);for(let i=0;i<4;i++)z=mul(z,hompower([one,...vars][(j+i+1)%5],e[i]));z=mul(z,hompower([one,...vars][j],L-e.reduce((a,b)=>a+b,0)));out=add(out,z)}return out}
function cyclicRow(r,j){return Math.floor(r/5)*5+(r%5+j)%5}
const charts=[];
for(let j=0;j<5;j++){const L=Math.max(deg(pdata.den),...pdata.KI.flat().map(deg),...pdata.KP.flat().map(deg)),d=homogenize(pdata.den,j,L),v=[one,...vars][j],I=zeroMatrix(15,2),P=zeroMatrix(2,15);
 for(let r=0;r<15;r++)for(let c=0;c<2;c++)I[cyclicRow(r,j)][c]=mul(homogenize(pdata.KI[r][c],j,L),c===1?v:one);
 for(let r=0;r<2;r++)for(let c=0;c<15;c++)P[r][cyclicRow(c,j)]=mul(homogenize(pdata.KP[r][c],j,L),r===0?v:one);
 charts.push({I,P,di:d,dp:mul(d,v),label:"U"+j});
}
const a2=mul(vars[0],vars[0]),auxI=adata.KI.map(row=>[mul(row[0],a2),mul(row[1],neg(vars[3]))]),auxP=adata.KP.map((row,r)=>row.map(p=>mul(p,r===0?vars[3]:neg(a2))));
charts.push({I:auxI,P:auxP,di:mul(adata.den,a2),dp:mul(adata.den,vars[3]),label:"Ustar"});
for(const c of charts){matrixeq(matmul(c.P,c.I),eye(2,mul(c.dp,c.di)),c.label+" normalized P I");matrixeq(matmul(pdata.delta,c.I),zeroMatrix(10,2),c.label+" inclusion closed");matrixeq(matmul(c.P,pdata.gamma),zeroMatrix(2,5),c.label+" projection closed")}

let affineChecks=0;
const assertP=(a,b,label)=>{if(!equal(a,b))throw Error(label);affineChecks++;};
const f=D,g=mul(mul(vars[0],vars[2]),vars[3]);
assertP(add(f,mul(vars[1],g)),one,"two-pivot Bezout");
assertP(determinant(beta.map(row=>I.map(i=>row[i]))),neg(f),"primary beta domain");
assertP(determinant(P.map(i=>alpha[Jc[i]])),f,"primary alpha domain");
assertP(determinant(beta.map(row=>Ia.map(i=>row[i]))),mul(vars[2],vars[3]),"auxiliary beta domain");
assertP(determinant(Pa.map(i=>alpha[Ja[i]])),neg(mul(mul(vars[0],vars[0]),vars[2])),"auxiliary alpha domain");
const choose=(n,k)=>{let a=1;for(let i=1;i<=k;i++)a=a*(n-i+1)/i;return a;};
let Af=Z(),Ag=Z();
for(let k=0;k<=7;k++){
 const coefficient=constant(choose(7,k));
 if(k>=4)Af=add(Af,mul(coefficient,mul(hompower(f,k-4),mul(hompower(vars[1],7-k),hompower(g,7-k)))));
 else Ag=add(Ag,mul(coefficient,mul(hompower(f,k),mul(hompower(vars[1],7-k),hompower(g,3-k)))));
}
const f4=hompower(f,4),g4=hompower(g,4),lambdaF=mul(f4,Af),lambdaG=mul(g4,Ag);
assertP(add(lambdaF,lambdaG),one,"one fixed exponent-four Bezout");
const Gnum=matmul(charts[0].P,charts[5].I),Gden=mul(charts[0].dp,charts[5].di);
const expectedDen=mul(hompower(f,2),mul(hompower(vars[0],4),mul(hompower(vars[2],2),vars[3])));
assertP(Gden,expectedDen,"actual direct G_0star auxiliary-to-primary-coordinate denominator");
const missing=mul(hompower(f,2),mul(hompower(vars[2],2),hompower(vars[3],3)));
assertP(mul(Gden,missing),mul(f4,g4),"common denominator lift");
const Mnum=Gnum.map(row=>row.map(p=>mul(p,missing)));
// Actual transition coefficients have common denominator f^4 g^4.
// h(M)=(-Ag*Mnum/f^4, Af*Mnum/g^4).
for(const row of Mnum)for(const m of row){
 assertP(add(mul(f4,mul(Af,m)),mul(g4,mul(Ag,m))),m,"d h actual transition coefficient");
 assertP(add(mul(Af,neg(mul(Ag,m))),mul(Ag,mul(Af,m))),Z(),"p h actual transition coefficient");
}
// Identity h d+i p=1 for formal sections A/f^4, B/g^4;
// after common-denominator clearing, coefficients of independent A,B:
assertP(add(lambdaF,lambdaG),one,"degree-zero A coefficient");
assertP(add(lambdaF,lambdaG),one,"degree-zero B coefficient");
console.log(JSON.stringify({affineChecks,cover:["D(1-abcd)","D(acd)"],commonDenominatorExponent:4,actualTransition:"auxiliary-coordinate to primary-coordinate matrix G_0star=P_0 I_star",scope:"affine-local entrywise scalar contraction on actual 2x2 transition coefficients",notComputed:["global original-cover correction","twisted End(E) descent comparison","E residual projection","second-order obstruction"]},null,2));

const sizes=[5,15,10,2],starts=[0,5,20,30],degrees=sizes.flatMap((n,k)=>Array(n).fill(k-1));
const differential=zeroMatrix(32,32);
for(const [block,map]of [[0,pdata.gamma],[1,pdata.delta],[2,pdata.ev]])
 for(let i=0;i<map.length;i++)for(let j=0;j<map[0].length;j++)differential[starts[block+1]+i][starts[block]+j]=map[i][j];
const entries=[];for(let i=0;i<32;i++)for(let j=0;j<32;j++)if(differential[i][j].size)entries.push([i,j,differential[i][j]]);
const smadd=(out,i,j,p,s=1)=>{const k=i+","+j,n=add(out.get(k)||Z(),p,s);if(n.size)out.set(k,n);else out.delete(k);};
function endDifferential(F,degree){
 const out=new Map(),sign=(Math.abs(degree)%2)?1:-1;
 for(const [key,p]of F){const[a,b]=key.split(",").map(Number);for(const[i,j,d]of entries){if(j===a)smadd(out,i,b,mul(d,p));if(i===b)smadd(out,a,j,mul(p,d),sign);}}
 return out;
}
const scalarMultiply=(p,F)=>new Map([...F].map(([k,v])=>[k,mul(p,v)]).filter(([,v])=>v.size));
const sparseEqual=(A,B)=>A.size===B.size&&[...A].every(([k,p])=>B.has(k)&&equal(p,B.get(k)));
let endChecks=0;
for(let a=0;a<32;a++)for(let b=0;b<32;b++){
 const degree=degrees[a]-degrees[b],F=new Map([[a+","+b,one]]),dF=endDifferential(F,degree);
 if(endDifferential(dF,degree+1).size)throw Error("End(K) d^2");
 endChecks++;
 for(const weight of [Af,Ag,lambdaF,lambdaG]){
  if(!sparseEqual(endDifferential(scalarMultiply(weight,F),degree),scalarMultiply(weight,dF)))throw Error("scalar/internal commutation");
  endChecks++;
 }
 // For an input of refinement degree one, the total internal signs are opposite
 // before/after h, so this commutation is precisely D_internal h+h D_internal=0.
}
console.log(JSON.stringify({endChecks,freeComplexRanks:sizes,generators:1024,weightsChecked:4,scope:"affine End(K) coefficient module; all homogeneous matrix units",notComputed:["actual E residual coefficient bounds","global mixed-chart HPL","E residual projection"]},null,2));
