'use strict';
// Exact top-two coefficient circuits, with syntactic degree bounds retained.
function leadingTwo(D,axis,makeRing){
 if(!Number.isInteger(axis)||axis<0||axis>3)throw Error('Axis must be 0..3');
 if(typeof makeRing!=='function')throw Error('Exact tagged-ring constructor required');
 const R=makeRing(),{zero,one,add,mul,neg,pow}=R;
 const other=R.x.filter((_,i)=>i!==axis),E=[one,other.reduce(add,zero),zero,other.reduce(mul,one)];
 for(let i=0;i<3;i++)for(let j=i+1;j<3;j++)E[2]=add(E[2],mul(other[i],other[j]));
 const A=[one,one,E[1],E[2],E[3]],B=[zero,E[1],E[2],E[3],zero];
 const J=[];for(let i=0;i<4;i++)J.push(i===axis?{d:1,a:one,b:zero}:{d:0,a:R.x[i],b:zero});
 for(let i=0;i<4;i++)J.push(i===axis?{d:2,a:one,b:zero}:{d:0,a:R.tag(4+i),b:zero});
 for(let j=1;j<4;j++)J.push({d:1,a:A[j],b:B[j]});
 let f0a=one,f0b=zero;for(let j=1;j<5;j++){f0b=add(mul(f0b,A[j]),mul(f0a,B[j]));f0a=mul(f0a,A[j])}J.push({d:4,a:neg(f0a),b:neg(f0b)});
 for(let j=1;j<5;j++){let otherLead=one;for(let k=1;k<5;k++)if(k!==j)otherLead=mul(otherLead,A[k]);J.push({d:4,a:pow(A[j],4),b:add(mul(R.fromBigInt(4),mul(pow(A[j],3),B[j])),neg(otherLead))})}
 if(J.length!==16)throw Error('Tag basis mismatch');
 const zeroJet={d:-Infinity,a:zero,b:zero};
 function times(U,V){if(U.d===-Infinity||V.d===-Infinity)return zeroJet;return{d:U.d+V.d,a:mul(U.a,V.a),b:add(mul(U.a,V.b),mul(U.b,V.a))}}
 function plus(U,V){if(U.d===-Infinity)return V;if(V.d===-Infinity)return U;let d=Math.max(U.d,V.d);return{d,a:add(U.d===d?U.a:zero,V.d===d?V.a:zero),b:add(U.d===d?U.b:U.d===d-1?U.a:zero,V.d===d?V.b:V.d===d-1?V.a:zero)}}
 function tagJet(e){let v={d:0,a:one,b:zero};for(let i=0;i<16;i++)if(e[i]){const n=e[i],t=J[i];if(n<0)throw Error('Rational input forbidden');v=times(v,{d:n*t.d,a:pow(t.a,n),b:n&&t.d?mul(R.fromBigInt(n),mul(pow(t.a,n-1),t.b)):zero})}return v}
 const nodes=[];
 for(const n of D.nodes){if(n[0]==='const'){const a=R.rational(n[1],n[2]);nodes.push(a.n===zero.n?zeroJet:{d:0,a,b:zero})}else if(n[0]==='tags')nodes.push(tagJet(n.slice(1)));else if(n[0]==='add')nodes.push(plus(nodes[n[1]],nodes[n[2]]));else if(n[0]==='mul')nodes.push(times(nodes[n[1]],nodes[n[2]]));else throw Error('Unsupported source operation')}
 const results=D.outputs.map(o=>times(nodes[o.numerator],tagJet(o.powers)));
 const out=R.pruneExport(results.flatMap(j=>[j.a,j.b]));
 Object.assign(out,{coefficientField:D.coefficientField,tagNames:D.tagNames,tagPolynomials:D.tagPolynomials,eliminatedAxis:axis,rootDegreeBounds:results.map(j=>j.d),coefficientOrder:'For each original output: degree-bound layer, then one degree lower. Bounds are not lowered when leading coefficients cancel.',unfilteredTopLayers:true});
 for(const n of out.nodes)if(n[0]==='tags'&&(n[axis+1]||n[axis+5]||n.slice(9).some(v=>v)))throw Error('Eliminated coordinate or old symmetric tag leaked');
 return out;
}
module.exports={leadingTwo};
