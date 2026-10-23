#!/usr/bin/env python3
"""Fixed restriction/duality arithmetic and exact source authentication only."""
from pathlib import Path
import hashlib,json

def require(ok,message):
    if not ok: raise RuntimeError(message)

# All numbers refer to proved bundle ranks/degrees, not evaluated map ranks.
require(2-9==-7 and 3-9==-6,'Cartier restriction twists')
require(-(-7)-4==3 and -(-6)-4==2,'relative threefold dual coefficients')
require(9-1==8 and (9-1)%2==0,'base twist and parity cancellation')
require(-1-5==-6,'ambient H4B1 dual twist')
require(4>3,'uniform section multiplication exclusion')
theta_rank,theta_deg=18,42
c_rank,c_deg=5,26
dual_c_deg=8*c_rank-c_deg
j_rank=theta_rank-c_rank
j_deg=theta_deg-dual_c_deg
require((dual_c_deg,j_rank,j_deg)==(14,13,28),'first bridge degrees')
h9_deg=8*theta_rank-theta_deg
dual_j_deg=8*j_rank-j_deg
require((h9_deg,dual_j_deg)==(102,76),'dual restriction degrees')
require(c_deg+dual_j_deg==h9_deg,'actual dual exact sequence')
require(j_deg+j_rank==41,'Steiner coefficient dimensions 28 and41')
require(3*4+2*5==22,'selected finite summand degree')
require(dual_c_deg-22==-8,'selected summand determinant exclusion')
require(20-j_deg==-8,'residual projection determinant exclusion')
require(j_deg!=20,'global and residual rank13 bundles differ')
root=Path(__file__).resolve().parent
for item in json.loads((root/'INPUTS.json').read_text()):
    b=(root/'audit-inputs'/(item['key']+'.md')).read_bytes()
    require(len(b)==item['bytes'],'input byte count')
    require(hashlib.sha256(b).hexdigest()==item['sha256'],'input SHA256')
    require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==item['blob'],'input Git blob')
print('PASS: fixed Cartier/duality twists and parity, bundle ranks/degrees, determinant degrees and six exact originals. No actual instance evaluated.')
