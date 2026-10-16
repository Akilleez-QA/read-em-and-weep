// Exact function excerpts from the public reduced source generator.
function build2(xs,ids){const X=xs.map((x,i)=>{const a=jc(R(x));a[1<<i]=o;return a}),es=[jo,jz,jz,jz,jz];for(const x of X)for(let k=4;k>0;k--)es[k]=ja(es[k],jm(x,es[k-1]));const vars=es.slice(1),data=MODEL;
const evm=(A,d)=>{const inv=ji(poly(d,vars));return A.map(row=>row.map(p=>jm(poly(p,vars),inv)))},one=[["0,0,0,0",1]];
const gamma=evm(data.gamma,one),delta=evm(data.delta,one),ev=evm(data.ev,one),charts=[];
for(const id of ids){const c=data.charts[id],I=evm(c.I,c.di),P=evm(c.P,c.dp),H0=evm(c.H0,c.dh),H1=evm(c.H1,c.dh),j=c.pivot,W=zm(10,8),eta=zm(10,2),L=zm(8,10);
for(let h=0;h<2;h++){eta[h*5+j][h]=ji(es[j]);for(let k=1;k<5;k++){const kk=(j+k)%5,col=h*4+k-1;W[h*5+kk][col]=jo;W[h*5+j][col]=jn(jd(es[kk],es[j]));L[col][h*5+kk]=jo}}
const U0=horiz(gamma,I,mtimes(H1,W)),Q0=vert(H0,P,mtimes(L,delta)),U1=horiz(W,eta),Q1=vert(L,ev);
const B0=Array.from({length:4},(_,a)=>mneg(mtimes(md(U0,a),Q0))),B1=Array.from({length:4},(_,a)=>mneg(mtimes(md(U1,a),Q1)));charts.push({I,P,B0,B1,H0,H1,eta,U0,Q0,U1,Q1})}
return {charts,gamma,delta,ev};}

function crossResidual(D,i,j,k){const {g,u12:A,u34:B}=D,mu=(F,G,a,b)=>scale(ms(mm(mv(md(F,a)),mv(md(G,b))),mm(mv(md(F,b)),mv(md(G,a)))),R(1n,2n));
let R0=ma(mm(mv(A[j][k]),mv(B[i][j])),mm(mv(B[j][k]),mv(A[i][j])));
for(const[F,G,a,b]of [[B[j][k],g[i][j],0,1],[A[j][k],g[i][j],2,3],[g[j][k],B[i][j],0,1],[g[j][k],A[i][j],2,3]])R0=ma(R0,mu(F,G,a,b));
const dd=(G,a,b)=>G.map(row=>row.map(x=>x[(1<<a)|(1<<b)]));
const cross=ma(ms(ms(mm(dd(g[j][k],0,2),dd(g[i][j],1,3)),mm(dd(g[j][k],0,3),dd(g[i][j],1,2))),mm(dd(g[j][k],1,2),dd(g[i][j],0,3))),mm(dd(g[j][k],1,3),dd(g[i][j],0,2)));
return ma(R0,scale(cross,R(1n,4n)))}

function mtraceProduct(A,B){let sum=jz;for(let i=0;i<A.length;i++)for(let j=0;j<A[i].length;j++)sum=ja(sum,jm(A[i][j],B[j][i]));return sum}

function globalBuild2(xs,vertices){
const ids=[...new Set(vertices.map(v=>v[0]))],base=build2(xs,ids),X=xs.map((x,i)=>{const a=jc(R(x));a[1<<i]=o;return a}),rf=X.map(x=>jd(ja(jm(x,x),jo),jscale(jm(x,js(jm(x,x),jo)),R(2n)))),ga=X.map(x=>ji(jm(x,js(jm(x,x),jo))));
const charts=vertices.map(([id,mask])=>{const c=base.charts[ids.indexOf(id)],nu=Array(16).fill(z);for(const m of masks){let t=o;for(let a=0;a<4;a++)if(m&(1<<a))t=mul(t,mul(mask[a],rf[a][0]));nu[m]=t}
const nu2=jm(nu,nu),nui2=ji(nu2),w0=[...Array(5).fill(nui2),jo,nui2,...Array(8).fill(nu2)],w1=[...Array(8).fill(jo),nu2,nu2];
const U0=c.U0.map(row=>row.map((x,i)=>jm(x,w0[i]))),Q0=c.Q0.map((row,i)=>row.map(x=>jd(x,w0[i]))),U1=c.U1.map(row=>row.map((x,i)=>jm(x,w1[i]))),Q1=c.Q1.map((row,i)=>row.map(x=>jd(x,w1[i])));
const blocks=[];for(let a=0;a<4;a++){const gamma=jscale(ga[a],mask[a]),raw0=mneg(mtimes(md(U0,a),Q0)),raw1=mneg(mtimes(md(U1,a),Q1)),out=[];for(const[dim,k,sign,BB]of [[5,-1,-1,null],[15,1,1,raw0],[10,3,-1,raw1],[2,5,1,null]]){const B=BB||zm(dim,dim);for(let r=0;r<dim;r++)B[r][r]=js(B[r][r],jscale(gamma,R(BigInt(k))));out.push({B,k,sign})}blocks.push(out)}
return{...c,mask,nu,blocks}});
const n=charts.length,g=Array.from({length:n},(_,i)=>Array.from({length:n},(_,j)=>{const core=mtimes(charts[i].P,charts[j].I),li=[ji(charts[i].nu),charts[i].nu],rj=[charts[j].nu,ji(charts[j].nu)];return mt(core.map((row,a)=>row.map((x,b)=>jm(jm(li[a],x),rj[b]))))}));
const q=(i,j,a)=>jd(jc(sub(charts[j].mask[a],charts[i].mask[a])),X[a]);
function first(a,b){return Array.from({length:n},(_,i)=>Array.from({length:n},(_,j)=>{let sum=jz;const ta=jscale(q(i,j,a),R(1n,2n)),tb=jscale(q(i,j,b),R(1n,2n));
for(let k=0;k<4;k++){const Ai=charts[i].blocks[a][k],Bi=charts[i].blocks[b][k],Aj=charts[j].blocks[a][k],Bj=charts[j].blocks[b][k],wedge=js(mtraceProduct(Ai.B,Bj.B),mtraceProduct(Bi.B,Aj.B)),linear=jscale(js(jm(ta,ja(mtrace(Bi.B),mtrace(Bj.B))),jm(tb,ja(mtrace(Ai.B),mtrace(Aj.B)))),R(BigInt(Ai.k)));sum=ja(sum,jscale(ja(wedge,linear),R(BigInt(Ai.sign))))}
const scalar=js(jscale(sum,R(1n,4n)),jscale(jm(q(i,j,a),q(i,j,b)),R(15n,8n))),G=g[i][j],inv=[[G[1][1],jn(G[0][1])],[jn(G[1][0]),G[0][0]]],K=msc(msub(mtimes(md(inv,a),md(G,b)),mtimes(md(inv,b),md(G,a))),R(1n,2n)),Z=msc(K,R(-1n,2n));Z[0][0]=ja(Z[0][0],scalar);Z[1][1]=ja(Z[1][1],scalar);return mtimes(G,Z)}))}
const u12=first(0,1),u34=first(2,3),bcoef=(i,j,k,a,b)=>mul(R(15n,4n),mul(q(i,j,a)[0],q(j,k,b)[0]));
return{g,u12,u34,charts,bcoef};}

function globalCross(D,i,j,k){const A=D.bcoef(i,j,k,0,1),B=D.bcoef(i,j,k,2,3);let out=crossResidual(D,i,j,k);out=ms(out,scale(mv(D.u34[i][k]),A));out=ms(out,scale(mv(D.u12[i][k]),B));out=ms(out,scale(mv(D.g[i][k]),mul(A,B)));return out}
