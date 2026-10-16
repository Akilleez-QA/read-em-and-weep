"""Explicit artificial complete source -> coefficient -> HPL -> weighted S.

The scalar primitive is obtained from a trivial artificial star-module and an
explicit gerbe primitive. It is not the HM four-block model or its values.
"""
from functools import lru_cache
from fractions import Fraction as Q
import itertools
from raw_engine import RF,SC,JC,Mat,RawSource,I

GRADES=(0,1,1,1,1,2,2,3)

def integer_matrix(r,c,values):return tuple(tuple(Q(values.get((i,j),0))for j in range(c))for i in range(r))

def contractions():
    d=integer_matrix(8,8,{(1,0):1,(5,4):1,(7,6):1});h=JC.transpose(d)
    inc=integer_matrix(8,2,{(2,0):1,(3,1):1});proj=JC.transpose(inc);out={}
    for tag in range(16):
        n=integer_matrix(8,8,{(i,j):Q(((tag+1)**(i+1)+(j+3)*(tag+2)**2)%11,100) for i in range(8)for j in range(8)if GRADES[i]==GRADES[j]-1})
        C=JC.add(JC.identity(8),JC.add(JC.times(d,n),JC.times(n,d)));Ci=JC.inverse(C)
        out[tag]=JC.TinyContraction(d,JC.times(C,inc),JC.times(proj,Ci),JC.times(JC.times(C,h),Ci),GRADES)
    return out


class ArtificialFrames:
    dims=(1,4,2,1)
    mode='synthetic'
    def __init__(self,ex):
        self.ex=ex;self.M=Mat(ex);self.M.model=self;z=ex.scalar(0);o=ex.scalar(1)
        self.frames=tuple(self.M.mul(((o,ex.x(0)*ex.scalar(a)+ex.x(2)*ex.scalar(b)),(z,o)),((o,z),(ex.x(1)*ex.scalar(c)+ex.x(3)*ex.scalar(d),o)),((o,ex.scalar(-1)),(z,o))) for a,b,c,d in [(0,0,0,0),(1,0,0,1),(0,1,1,0),(1,2,2,1),(2,1,1,3),(3,2,2,3)])
    def frame(self,o):return self.frames[o.carrier]
    @lru_cache(maxsize=None)
    def g(self,a,b):return self.M.mul(self.frame(b),self.M.inverse(self.frame(a)))
    def charge(self,o,d):return o.carrier*(d+1)
    def q(self,a,b,d):return self.ex.scalar(self.charge(b,d)-self.charge(a,d))*self.ex.y(d)
    def mu(self,a,b,p):
        u,v=p;M=self.M
        return M.scale(M.add(M.mul(M.D(a,u),M.D(b,v)),M.scale(M.mul(M.D(a,v),M.D(b,u)),-1)),Q(1,2))
    @lru_cache(maxsize=None)
    def s_raw(self,p,a,b):
        M=self.M;ha=self.frame(a);hb=self.frame(b);hai=M.inverse(ha);g=self.g(a,b)
        # First coefficient of Hb star (Ha)^star-inverse.
        U=M.add(self.mu(hb,hai,p),M.scale(M.mul(g,self.mu(ha,hai,p)),-1))
        scalar=M.trace(M.mul(M.inverse(g),U))[0][0]*self.ex.scalar(Q(1,2))
        # delta(f_a cup delta f_b)=delta f_a cup delta f_b.
        sb=self.ex.scalar(Q(15,4)*self.charge(a,p[0]))*self.ex.y(p[0])*self.q(a,b,p[1])
        return scalar+sb
    def leaf(self,name,shape,**data):
        if name=='g_phys':return self.g(*data['owners'])
        if name=='physical_q':return ((self.q(*data['owners'],data['coordinate']),),)
        raise ValueError('artificial source has no HM primitive leaves')


def fullsign_coefficient(field,e):
    # Projection is after the COMPLETE corrected source, no raw coefficient
    # extraction before cancellation/divisibility. Missing basis is exact zero.
    r=dict(field.terms).get(15,field.ex.rational(0))
    return r.laurent_coefficient(tuple(e))


def source_constant(ex,omit=None,labels=(0,1,2)):
    model=ArtificialFrames(ex);M=model.M
    oo=tuple(I.FullOwner(30,('art-source',i),c,0,0)for i,c in enumerate(labels))
    source=RawSource(M);R=source.residual(oo)
    parts=source.components[oo]
    if omit is not None:R=M.add(*(v for k,v in parts.items()if k!=omit))
    # Transport the whole source to its artificial fixed cohomology frame.
    R=M.mul(M.inverse(model.frame(oo[0])),R,model.frame(oo[0]))
    value=tuple(tuple(fullsign_coefficient(v,(0,0,0,0))for v in row)for row in R)
    component_values={k:tuple(tuple(fullsign_coefficient(v,(0,0,0,0))for v in row)for row in a)for k,a in parts.items()}
    return value,component_values


def run_artificial(omit=None,staircase_limit=None,weight_scale=1):
    """Complete explicit tiny domain, real full5 source and accepted HPL/S.

    Constant-coefficient extraction commutes with this fixture's constant
    contraction matrices. This optimization is specific to this artificial
    input and never asserted for physical field-valued contractions.
    """
    ex=RF.Execution();R,parts=source_constant(ex,omit);source_cache={(0,1,2):R}
    local=contractions();ordered_tags=sorted(range(16),key=lambda t:(t.bit_count(),t))
    ids={t:j for j,t in enumerate(ordered_tags)}
    C={ids[t]:local[t]for t in range(16)}
    # TinyLift's cap is8 vertices; each staircase has just5 explicit vertices.
    rows=[];total=Q(0)
    stairs=SC.staircase_records()
    if staircase_limit is not None:stairs=stairs[:staircase_limit]
    for stair in stairs:
        tags=stair['standard_tags'];owners=tuple(I.FullOwner(30,('outer',t),t.bit_count(),0,t)for t in tags)
        canonical,parity=I.sorted_source(owners);vertices=tuple(ids[o.standard_tag]for o in canonical)
        def residual(vs):
            carriers=[ordered_tags[j].bit_count() for j in vs]
            if len(set(carriers))<3:return JC.zero(2)
            # These physical labels are increasing because the WHOLE tuple
            # was source-sorted before any face recursion.
            if carriers!=sorted(carriers):raise ValueError('artificial source orientation')
            key=tuple(carriers)
            if key not in source_cache:source_cache[key]=source_constant(ex,omit,key)[0]
            return source_cache[key]
        lift=JC.TinyLift({v:C[v]for v in vertices},residual)
        J=lift.component(2,vertices)
        # Explicit artificial3-entry chain map; actual route30 uses the
        # separately pinned REAL selector/dimensions in program.py.
        scalar=J[1][7]+J[0][5]-J[0][6]
        # Complete tiny outer domain has exactly one owner per standard tag.
        # Weight at tag0 is x0^-1 x1^-1 x2^-1 x3^-1, others constant1;
        # target(-1)^4 therefore requests this exact source constant.
        contribution=Q(weight_scale)*stair['orientation']*parity*scalar
        total+=contribution;rows.append({'tags':tags,'outer_parity':parity,'stair_sign':stair['orientation'],'contribution':contribution})
    return {'value':total,'staircases_executed':len(rows),'complete_staircase_sum':len(rows)==24,
            'complete_artificial_domain':True,'coefficient_exponent':(-1,-1,-1,-1),
            'source_components':parts,'source_constant':R,'rows':rows,'field_counts':dict(ex.counts),
            'physical_source_evaluated':False,'actual_fibers_enumerated':False,
            'zero_scope':'This artificial fixture only; not a global obstruction result.'}
