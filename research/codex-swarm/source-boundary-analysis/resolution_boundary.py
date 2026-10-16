"""Source-free exact lift of a ROW coboundary to a TOTAL coboundary.

Reuses JC's tiny artificial matrix engine; never instantiates its actual
source factory or loads any HM polynomial/jet/coefficient/fiber provider.
"""
from functools import lru_cache
from pathlib import Path
import sys
JC=Path(__file__).resolve().parent.parent/'full-lift-domain'
sys.path.insert(0,str(JC))
import lift as L

class TinyBoundaryPrimitive:
    def __init__(self,delta_lift,row_edge):
        L.need(type(delta_lift)is L.TinyLift,'artificial lift only')
        self.J=delta_lift;self.edge=row_edge
    @lru_cache(maxsize=2048)
    def component(self,s,v):
        L.need(type(s)is int and 0<=s<=3 and type(v)is tuple and len(v)==2+s,'primitive arity')
        local=self.J.local[v[0]]
        if s==0:return local.inclusion(self.edge(v))
        previous=self.delta(s-1,v);target=self.J.component(s-1,v)
        rhs=L.add(target,L.scale(-1,previous))if s in(1,3)else L.add(previous,L.scale(-1,target))
        return local.homotopy(rhs,1-s)
    def delta(self,s,v):
        L.need(len(v)==3+s,'primitive delta arity');out=L.zero(next(iter(self.J.local.values())).n)
        for j in range(len(v)):out=L.add(out,L.scale((-1)**j,self.component(s,v[:j]+v[j+1:])))
        return out
    def total_boundary_component(self,s,v):
        out=self.delta(s,v)
        if s<3:
            d=self.J.local[v[0]].differential(self.component(s+1,v),-s-1)
            out=L.add(out,L.scale((-1)**(2+s),d))
        return out
