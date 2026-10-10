'use strict';
// Relocatable wrapper. The mathematical top-two-jet algorithm is unchanged.
const fs=require('fs'),path=require('path'),crypto=require('crypto');
const {leadingTwo}=require('./leading_two_jet');
const hash=b=>crypto.createHash('sha256').update(b).digest('hex');
const [source,dest,axisString,ringPath]=process.argv.slice(2),axis=Number(axisString);
if(!source||!dest||!axisString||!ringPath||!Number.isInteger(axis)||axis<0||axis>3)
 throw Error('Usage: node build_leading_source.js NUMERATOR OUTPUT AXIS TAGGED_RING_MODULE');
const pins=JSON.parse(fs.readFileSync(path.join(__dirname,'pins.json')));
const raw=fs.readFileSync(source),sourceHash=hash(raw),D=JSON.parse(raw);
if(D.coefficientField!=='Q'||sourceHash!==pins.numeratorSHA256)
 throw Error('Exact current-L Q numerator pin mismatch');
const provenance=JSON.parse(fs.readFileSync(path.join(__dirname,'implementation-provenance.json')));
if(hash(fs.readFileSync(ringPath))!==provenance.taggedRing.sha256)throw Error('Exact tagged-ring dependency pin mismatch');
const {makeRing}=require(path.resolve(ringPath));
const out=leadingTwo(D,axis,makeRing);
if(out.rootDegreeBounds.length!==1||out.rootDegreeBounds[0]!==273)
 throw Error('Unexpected syntactic degree bound');
const construction=axis===3
 ? 'Fresh fourth-axis leading layers of the pinned A_Q polynomial; no finite-field arrays used.'
 : 'Fresh exact rational source; no modular coefficient arrays used.';
const gate=axis===0
 ? 'Requires independent exact rational source identification with the regular O(272)^4 scalar numerator.'
 : axis===3
 ? 'Same characteristic-independent H0 source identity; separate source audit receipt.'
 : 'Same independently certified exact regular O(272)^4 numerator.';
Object.assign(out,{sourceSHA256:sourceHash,targetDegrees:[273,272],filterApplied:false,
 sourceConstruction:construction,degree273Gate:gate});
const bytes=JSON.stringify(out),sha256=hash(bytes);
if(sha256!==pins.axes[String(axis)].leadingSHA256)throw Error('Leading source pin mismatch');
fs.writeFileSync(dest,bytes,{flag:'wx'});
console.log(JSON.stringify({axis,sha256,nodes:out.nodes.length,bytes:Buffer.byteLength(bytes)}));
