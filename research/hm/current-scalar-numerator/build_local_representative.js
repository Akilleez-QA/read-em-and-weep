'use strict';
// One exact Q local-duality representative. No coefficient extraction.
const fs=require('fs'),path=require('path'),crypto=require('crypto');
const {makeRing}=require('./tagged_ring');
const {maskBasis}=require('./weighted_mask_moments');
const H=__dirname,read=f=>JSON.parse(fs.readFileSync(path.join(H,f))),hash=b=>crypto.createHash('sha256').update(b).digest('hex');
const args=process.argv.slice(2);
if(args.length!==4||args[0]!=='--source'||args[2]!=='--output-dir'){
 console.error('Usage: node build_local_representative.js --source carriers-234.json --output-dir NEW_DIRECTORY');process.exit(2);
}
const sourcePath=path.resolve(args[1]),outDir=path.resolve(args[3]);
// An exclusive new directory prevents clobbering completed or sealed results.
fs.mkdirSync(outDir);

const seeds=read('inverse_seeds.json'),denoms=read('model_denominators.json'),pref=read('public_hm_scalar_prefactors.json'),features=read('feature-moments.json');
const raw=fs.readFileSync(sourcePath),sourceSHA=hash(raw);
if(sourceSHA!=='31cd62eb3062801ca19073464c276fbe016fa4024fbcdcf48d3893358e3fcc18'||sourceSHA!==seeds.files['carriers-234.json'].sha256)throw Error('Source pin mismatch');
const R=makeRing(),{zero,one,add,mul,neg,pow}=R;
const ev=(P,vars)=>P.reduce((v,[key,c])=>add(v,key.split(',').reduce((a,e,i)=>mul(a,pow(vars[i],+e)),R.fromBigInt(c))),zero);
const invden=(j,key)=>{const f=denoms[j][key],q=f.coefficient.split('/');return R.scalar(R.rational(q[1]||1,q[0]).n,f.powers.map(e=>-e))};
const a=pref.aNumerators.map(P=>mul(ev(P,R.V.slice(1)),mul(invden(1,'di'),invden(2,'di'))));
const b=pref.bNumerators.map(P=>mul(ev(P,R.V.slice(1)),mul(R.inv(R.V[1]),invden(2,'dp'))));
const h=R.V.map((v,j)=>mul(v,R.F[j]));
const moments={};
for(const j of [2,3,4])moments[j]=features.moments[j].map(f=>{if(f.identity)return one;let v=ev(f.topCoefficient,R.x);for(let i=0;i<4;i++)if(f.subset>>i&1)v=mul(v,mul(pow(R.x[i],3),R.tag(4+i)));return mul(v,R.inv(h[j]))});
const C=R.importDAG(JSON.parse(raw),seeds.files['carriers-234.json']);
console.error(JSON.stringify({stage:'imported',nodes:R.nodes.length}));
const M=Array.from({length:2},()=>[zero,zero]);let nonzeroFeatures=0;
for(let code=0;code<256;code++){
 const S=maskBasis(code),w=S.reduce((v,s,i)=>mul(v,moments[i+2][s]),one);
 if(w.n!==zero.n)nonzeroFeatures++;
 for(let r=0;r<2;r++)for(let c=0;c<2;c++)M[r][c]=add(M[r][c],mul(w,C[code][r][c]));
}
let scalar=zero;
for(let r=0;r<2;r++)for(let c=0;c<2;c++)scalar=add(scalar,mul(a[r],mul(M[c][r],b[c])));
scalar=neg(scalar); // The original coefficient DAG is unsigned; exactly one J2 minus.
const orders=[13,14,14,14],denominator=orders.reduce((v,e,j)=>mul(v,pow(h[j+1],e)),one),numerator=mul(scalar,denominator);
const failures=numerator.n===zero.n?[]:numerator.e.flatMap((e,j)=>e<0?[{tag:seeds.tag_names[j],power:e}]:[]);
const report={schema:'hm-scalar-local-residue-probe-v1',coefficientField:'Q',sourceTail:[2,3,4],sourceCoefficientSHA256:sourceSHA,sourceUnsigned:true,explicitScalarJ2MinusCount:1,featureCodes:256,nonzeroFeatureMoments:nonzeroFeatures,all4096MaskChoicesRetainedByExactMoments:true,carrierDenominatorOrders:orders,carrierDenominatorDefinition:'hj=vj Fj; j=1,2,3,4; v0=1',denominatorTagPowers:denominator.e,rawScalarTagPowers:scalar.e,numeratorTagPowers:numerator.e,remainingDenominatorTags:failures,allPolynomialNodes:R.nodes.length,noDeterminantOrCubeOrientation:'This is the separately proved coarse-carrier projection, not a tensor-simplex comparison.',coefficientExtractionPerformed:false};
fs.writeFileSync(path.join(outDir,'local-representative.report.json'),JSON.stringify(report,null,2)+'\n');
if(failures.length)throw Error('Declared h denominator did not clear '+JSON.stringify(failures));
const out=R.pruneExport([numerator]);Object.assign(out,report,{outputsMeaning:'Polynomial numerator N, with local scalar f=N/(h1^13 h2^14 h3^14 h4^14)',tagNames:seeds.tag_names,tagPolynomials:seeds.tags});
fs.writeFileSync(path.join(outDir,'local-numerator.dag.json'),JSON.stringify(out));
console.error(JSON.stringify({stage:'saved',nodes:out.nodes.length,bytes:fs.statSync(path.join(outDir,'local-numerator.dag.json')).size,numeratorPowers:numerator.e,nonzeroFeatures}));
