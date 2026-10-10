'use strict';
const {maskBasis}=require('./weighted_mask_moments');
process.stdout.write(JSON.stringify(Array.from({length:256},(_,code)=>maskBasis(code))));
