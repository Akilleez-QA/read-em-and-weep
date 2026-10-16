'use strict';
// Evaluate ONLY the authenticated constant matrices/basis constructor prefix.
// Never evaluate the source's rank functions, main, zigzag, or full HM oracle.
const cp=require('node:child_process'), crypto=require('node:crypto'), vm=require('node:vm');
const PIN='f968b53943ba2312f09fbc3e8f9d462e86bcaa34';
const PATH='research/hm/d8-small-certificates/p4/check_hm_p4_all_twists.js';
const BLOB='7adc1d6a733636204b1dd613870c168717be6277';
const source=cp.execFileSync('git',['show',`${PIN}:${PATH}`],{maxBuffer:65536});
const actual=crypto.createHash('sha1').update(Buffer.from(`blob ${source.length}\0`)).update(source).digest('hex');
if(actual!==BLOB)throw Error('source blob mismatch');
const text=source.toString('utf8'), marker='function rankExact(input,ncols){';
if(text.split(marker).length!==2)throw Error('extraction boundary not unique');
const prefix=text.slice(0,text.indexOf(marker));
if(!prefix.endsWith('  return{rows,cols:src.length};\n}\n'))throw Error('unexpected constructor suffix');
const sandbox={};
vm.createContext(sandbox);
vm.runInContext(prefix+`
this.exported={gamma,bases:{minus2:basis(2,-2),minus1:basis(2,-1),zero:basis(2,0)},matrices:{E:matrix(2,-2),B1:matrix(1,-1),C1:matrix(2,-1),B0:matrix(1,0),C0:matrix(2,0)}};
`,sandbox,{timeout:5000});
const rankPath='research/hm/d8-small-certificates/p4/certificate.json';
const rankBlob='304d031083bb2a19fb9bc012cfd338bbe0129980';
const rankBytes=cp.execFileSync('git',['show',`${PIN}:${rankPath}`],{maxBuffer:65536});
if(crypto.createHash('sha1').update(Buffer.from(`blob ${rankBytes.length}\0`)).update(rankBytes).digest('hex')!==rankBlob)throw Error('rank receipt blob mismatch');
const rankReceipt=JSON.parse(rankBytes);
const rationalRanks={B1:rankReceipt.p4Twists.find(x=>x.twist===-1).matrices[1],B0:rankReceipt.p4Twists.find(x=>x.twist===0).matrices[1]};
for(const[name,r]of Object.entries(rationalRanks))if(r.rank!==(name==='B1'?240:848)||r.unitRank!==r.rank||r.tailMaxBits!==0)throw Error('rational upper receipt mismatch');
const out={rank_receipt:{commit:PIN,path:rankPath,blob:rankBlob,bytes:rankBytes.length,ranks:rationalRanks},source:{commit:PIN,path:PATH,blob:BLOB,bytes:source.length,prefix_bytes:Buffer.byteLength(prefix)},gamma:sandbox.exported.gamma,bases:sandbox.exported.bases,matrices:{}};
for(const[name,M]of Object.entries(sandbox.exported.matrices)){
 const columns=Array.from({length:M.cols},()=>[]);
 for(let row=0;row<M.rows.length;row++)for(const[col,value]of M.rows[row])columns[col].push([row,value]);
 out.matrices[name]={rows:M.rows.length,columns:M.cols,data:columns};
}
const result=JSON.stringify(out);
if(Buffer.byteLength(result)>500000)throw Error('constant extraction output cap');
process.stdout.write(result+'\n');
