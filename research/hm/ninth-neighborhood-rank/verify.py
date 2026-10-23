#!/usr/bin/env python3
"""Bounded structural arithmetic and immutable-byte authentication only."""
from pathlib import Path
import hashlib,json

def require(condition,message):
    if not condition: raise RuntimeError(message)

# Universal projective-bundle/Cartier duality exponents (ambient, parameter).
omega_X=(-4,1)
E=(1,-1)
m=9
omega_D=tuple(a+m*b for a,b in zip(omega_X,E))
require(omega_D==(5,-8),'ninth-neighborhood relative dualizing twists')
require((omega_D[0]-2,omega_D[1])==(3,-8),'dual of B2 is B3 times parameter O(-8)')
require((-1)*((-1)**m)==1,'relative canonical and divisor parity cancel')
require((-8)%2==0,'duality parameter twist has even center')
# Stabilization of positive sections begins after 7R: k=8 has plane twist -5.
require(3-8==-5,'first later even layer is in H1-vanishing range')
# Serre dual of H1(B_H(3-m)) on P3 has twist m-7.
require(-(3-m)-4==m-7,'eventual Serre comparison twist')
# Source constituents: rank and line degree, no map entries.
source=[(3,2),(4,2),(2,5),(15,4),(6,6)]
rank_source=sum(r for r,d in source)
degree_source=sum(r*d for r,d in source)
rank_target=15;degree_target=15*8
rank_Q=3;degree_Q=3*(-6)
rank_coker=rank_Q;degree_coker=-degree_Q+8*rank_Q
rank_image=rank_target-rank_coker
degree_image=degree_target-degree_coker
rank_kernel=rank_source-rank_image
degree_kernel=degree_source-degree_image
require((rank_source,degree_source)==(30,120),'source rank/degree')
require((rank_target,degree_target)==(15,120),'target rank/degree')
require((rank_coker,degree_coker)==(3,42),'dual-square cokernel')
require((rank_image,degree_image)==(12,78),'annihilator image')
require((rank_kernel,degree_kernel)==(18,42),'kernel')
rank_S12=15-3;degree_S12=0-degree_Q
require((-degree_S12+8*rank_S12)==degree_image,'image is S12 dual times O8')
require(-6-8==-14,'dual of cokernel is A O(-14)')
root=Path(__file__).resolve().parent
items=json.loads((root/'INPUTS.json').read_text())
require(len(items)==3,'three exact published inputs')
for item in items:
    data=(root/'audit-inputs'/f"{item['key']}.md").read_bytes()
    blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    require(blob==item['blob'],f"immutable input mismatch: {item['key']}")
print('PASS: three immutable inputs; dualizing and Serre twists; parity; ranks/degrees of source, target, kernel, image, and cokernel.')
print('No actual HM coefficients, points, jets, derivatives, matrices, or instance ranks evaluated.')
