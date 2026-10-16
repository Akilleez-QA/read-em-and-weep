"""Executable finite-demand Kcov Pi + A h S Pi coefficient maps.

All coefficients are in the GLOBAL FINITE Laurent frame. Actual-source
admission is absent. Only bounded artificial cochains/oracles may execute.
No Laurent box or full physical common-cover fiber is enumerated.
"""
from collections import defaultdict
from fractions import Fraction as Q
from functools import lru_cache
import itertools
from pathlib import Path
import sys

_SHARED=Path(__file__).resolve().parent.parent/'inserted-coefficients'
if str(_SHARED)not in sys.path:sys.path.insert(0,str(_SHARED))
import interfaces as I
need=I.need
PAIR=(0,1)
TWIST=(-2,-2,0,0)
F34_TWIST=(0,0,-2,-2)

def scalar_pair(pair):
    need(type(pair)in(tuple,list)and len(pair)==2 and all(type(i)is int for i in pair)and tuple(pair)in((0,1),(2,3)),'explicit complementary scalar pair')
    return tuple(pair)

def line_twist(pair):return tuple(-2 if i in pair else 0 for i in range(4))


def rational(c):
    need(type(c)is int or isinstance(c,Q),'exact rational coefficient required')
    return Q(c)

def tag(t):need(type(t)is int and 0<=t<16,'standard tag');return t

def bits(t):tag(t);return tuple((t>>(3-j))&1 for j in range(4))
def pack(b):return sum(x<<(3-i)for i,x in enumerate(b))

def normalize(simplex):
    need(type(simplex)in(tuple,list)and len(simplex)>0,'nonempty simplex')
    simplex=tuple(tag(t)for t in simplex)
    if len(set(simplex))!=len(simplex):return(),0
    p=sorted(range(len(simplex)),key=lambda j:simplex[j]);sign=(-1)**sum(p[i]>p[j]for i in range(len(p))for j in range(i+1,len(p)))
    return tuple(simplex[j]for j in p),sign

def put(chain,simplex,coefficient):
    s,z=normalize(simplex)
    if z:
        chain[s]+=coefficient*z
        if not chain[s]:del chain[s]

def boundary(chain):
    out=defaultdict(int)
    for s,z in chain.items():
        if len(s)==1:continue
        for j in range(len(s)):put(out,s[:j]+s[j+1:],z*(-1)**j)
    return dict(out)

def aw_cells(simplex):
    """A:T->ordered cochains, on a canonical simplex, cut positions fixed."""
    s,orientation=normalize(simplex)
    if not orientation:return[]
    q=len(s)-1
    if q>4:return[]
    records=[]
    for active in itertools.combinations(range(4),q):
        cell=[];p=0;sign=orientation;good=True
        for j in range(4):
            a=bits(s[p])[j]
            if j in active:
                b=bits(s[p+1])[j];p+=1
                if a==b:good=False;break
                sign*=1 if(a,b)==(0,1)else-1;cell.append('C')
            else:cell.append('B'if a else'A')
        if good:records.append((sign,tuple(cell)))
    return records

def stairs(cell):
    need(len(cell)==4 and all(s in('A','B','C')for s in cell),'tensor cell')
    active=[j for j,s in enumerate(cell)if s=='C'];out=[]
    for p in itertools.permutations(active):
        b=[int(s=='B')for s in cell];vertices=[pack(b)]
        for j in p:b[j]=1;vertices.append(pack(b))
        sign=(-1)**sum(p[i]>p[j]for i in range(len(p))for j in range(i+1,len(p)))
        out.append((sign,tuple(vertices)))
    return out

def G_chain(simplex):
    out=defaultdict(int)
    for sign,cell in aw_cells(simplex):
        for staircase_sign,s in stairs(cell):put(out,s,sign*staircase_sign)
    return dict(out)

@lru_cache(maxsize=4096)
def _k_canonical(s):
    if len(s)<=1:return()
    inside=defaultdict(int);put(inside,s,1)
    for t,z in G_chain(s).items():put(inside,t,-z)
    for j in range(len(s)):
        for t,z in _k_canonical(s[:j]+s[j+1:]):put(inside,t,-(-1)**j*z)
    base=s[0]
    for v in s[1:]:base&=v
    out=defaultdict(int)
    for t,z in inside.items():put(out,(base,)+t,z)
    return tuple(sorted(out.items()))

def k_chain(simplex):
    s,z=normalize(simplex)
    return {}if not z else{t:z*a for t,a in _k_canonical(s)}

def h_requests(cell,e,twist=TWIST):
    """Exact scalar tensor h transpose; all predicates use THIS exponent.

    A derivative caller must shift the requested exponent BEFORE calling h.
    p0 takes the B constant; p_-2 takes C exponent -1.
    """
    e=I.exponent(e);need(len(cell)==4 and all(s in('A','B','C')for s in cell),'tensor cell')
    need(len(twist)==4 and all(type(n)is int for n in twist)and tuple(twist)in(TWIST,F34_TWIST,(0,0,0,0)),'source F34 transport not supplied')
    out=[]
    for j in range(4):
        prefix=list(cell);valid=True
        for i in range(j):
            if twist[i]==0:
                if cell[i]not in('A','B')or e[i]!=0:valid=False;break
                prefix[i]='B'
            elif cell[i]!='C'or e[i]!=-1:valid=False;break
        if not valid:continue
        if cell[j]=='A'and e[j]>=0:sign=-1
        elif cell[j]=='B'and e[j]<0 and e[j]<=twist[j]:sign=1
        else:continue
        sign*=(-1)**sum(s=='C'for s in cell[:j]);prefix[j]='C'
        out.append((sign,tuple(prefix),e))
    return out


def regular_exponent(tags,e,twist=TWIST):
    rows=[bits(t)for t in tags]
    for j in range(4):
        states={b[j]for b in rows}
        if states=={0}and e[j]<0:return False
        if states=={1}and e[j]>twist[j]:return False
    return True


class SyntheticStandardCochain:
    """Complete tiny Laurent data, checked on the STANDARD intersection.

    This checks the entire supplied polynomial, not a common-local claim.
    It does not authenticate an omitted source or arbitrary physical callback.
    """
    mode='synthetic'
    def __init__(self,polynomials,twist=TWIST):
        need(len(twist)==4 and all(type(n)is int for n in twist)and tuple(twist)in(TWIST,F34_TWIST),'scalar pair fixture class')
        self.data={};self.twist=tuple(twist);self.pair=tuple(i for i,n in enumerate(twist)if n==-2);self.calls=[]
        for raw,poly in polynomials.items():
            s,z=normalize(raw);need(len(s)==3 and z==1,'canonical standard triple')
            checked={}
            for e,c in poly.items():
                e=I.exponent(e);c=rational(c)
                need(regular_exponent(s,e,self.twist),'whole coefficient fails standard-target extension')
                if c:checked[e]=c
            self.data[s]=checked
        need(sum(map(len,self.data.values()))<=4096,'synthetic support cap')
    def coefficient(self,s,e):
        s,z=normalize(s);e=I.exponent(e)
        if not z:return Q(0)
        need(len(s)==3,'PiF coefficient degree')
        self.calls.append((s,e));return z*self.data.get(s,{}).get(e,Q(0))
    def support_box(self):
        es=[e for p in self.data.values()for e in p]
        return None if not es else(tuple(min(e[j]for e in es)for j in range(4)),tuple(max(e[j]for e in es)for j in range(4)))
    def require_extension(self,s):
        s,z=normalize(s)
        return not z or len(s)==3


class PiCoefficientProgram:
    """Actual finite factored Pi coefficient sum on SYNTHETIC bounded fibers.

    weight/source factors obey rho/C=Qhat. Source numerator coefficients are
    requested only at eta-sum(quotient exponents), never on a Laurent box.
    Whole-standard extension remains an external, explicitly bound witness;
    physical evidence cannot execute through this API.
    """
    mode='synthetic'
    def __init__(self,cleared_F,quotients,fibers,extension,pair=PAIR):
        for obj in(cleared_F,quotients,fibers):I.require_synthetic(obj.mode)
        self.F=cleared_F;self.Q=quotients;self.fibers=fibers;self.extension=extension;self.pair=scalar_pair(pair);self.trace=[];self.cache={};self.queries=0
    def coefficient(self,standard_triple,e):
        for obj in(self.F,self.Q,self.fibers):I.require_synthetic(obj.mode)
        s,orientation=normalize(standard_triple);e=I.exponent(e)
        if not orientation:return Q(0)
        need(len(s)==3,'PiF degree two')
        if(s,e)in self.cache:return orientation*self.cache[s,e]
        domains=[]
        for j,t in enumerate(s):
            values=tuple(self.fibers.owners(t,('Pi',s,j)))
            need(1<=len(values)<=4,'bounded synthetic fibers only')
            need(all(isinstance(v,I.FullOwner)and v.standard_tag==t and v.occurrence==('Pi',s,j)for v in values),'fiber owner binding')
            need(len({v.common_key for v in values})==len(values),'duplicate fiber label')
            domains.append(values)
        total=Q(0);queries=0
        for owners in itertools.product(*domains):
            witness=self.extension(owners,s);need(isinstance(witness,I.RegularExtensionWitness),'extension witness type');witness.require(owners,s)
            if len({v.physical_key for v in owners})<3:continue # physical-F pullback ONLY
            sorted_owners,sign=I.sorted_source(owners)
            upper=I.exponent(self.F.degree_upper(sorted_owners,pair=self.pair));need(min(upper)>=0,'numerator degree upper')
            factors=[]
            for owner in owners:
                terms=tuple(self.Q.factor_terms(owner,pair=self.pair));need(len(terms)<=16,'quotient term cap')
                terms=tuple((I.exponent(a),rational(c))for a,c in terms if rational(c))
                need(len({a for a,c in terms})==len(terms),'quotient term duplication')
                factors.append(terms)
            for terms in itertools.product(*factors):
                a=tuple(sum(t[0][j]for t in terms)for j in range(4));p=tuple(e[j]-a[j]for j in range(4))
                if min(p)<0 or any(p[j]>upper[j]for j in range(4)):continue
                coefficient=Q(sign)
                for exponent,c in terms:coefficient*=c
                value=rational(self.F.coefficient(sorted_owners,p,pair=self.pair));queries+=1;self.queries+=1
                need(self.queries<=100000,'aggregate synthetic Pi source-query cap')
                need(queries<=20000,'synthetic Pi source-query cap')
                total+=coefficient*value
                self.trace.append({'owners':[v.data()for v in owners],'sorted_owners':[v.data()for v in sorted_owners],
                    'source_sign':sign,'exponent':p,'quotient_exponents':[a for a,c in terms],'target_standard_tags':s,
                    'whole_extension_id':witness.whole_coefficient_id,'source_value_is_synthetic':True})
        self.cache[s,e]=total;return orientation*total
    def require_extension(self,s):
        # Each summand request still invokes its precise whole-extension witness.
        return len(normalize(s)[0])in(0,3)
    def support_box(self):
        """Finite enclosure from numerator DEGREE bounds and quotient supports.

        Enumerates bounded artificial owner assignments, never exponent boxes
        or numerator coefficients. It may overestimate after cancellations.
        """
        for obj in(self.F,self.Q,self.fibers):I.require_synthetic(obj.mode)
        lower=upper=None;assignments=0
        for s in itertools.combinations(range(16),3):
            domains=[]
            for j,t in enumerate(s):
                values=tuple(self.fibers.owners(t,('Pi',s,j)))
                need(1<=len(values)<=4,'bounded synthetic fibers only')
                need(all(isinstance(v,I.FullOwner)and v.standard_tag==t and v.occurrence==('Pi',s,j)for v in values),'fiber owner binding')
                need(len({v.common_key for v in values})==len(values),'duplicate fiber label')
                domains.append(values)
            for owners in itertools.product(*domains):
                assignments+=1;need(assignments<=10000,'synthetic support-assignment cap')
                witness=self.extension(owners,s);need(isinstance(witness,I.RegularExtensionWitness),'extension witness type');witness.require(owners,s)
                if len({v.physical_key for v in owners})<3:continue
                source,_=I.sorted_source(owners)
                degree=I.exponent(self.F.degree_upper(source,pair=self.pair));need(min(degree)>=0,'numerator degree upper')
                factors=[]
                for owner in owners:
                    terms=tuple(self.Q.factor_terms(owner,pair=self.pair));need(len(terms)<=16,'quotient term cap')
                    terms=tuple((I.exponent(a),rational(c))for a,c in terms if rational(c))
                    need(len({a for a,c in terms})==len(terms),'quotient term duplication');factors.append(terms)
                if any(not f for f in factors):continue
                lo=tuple(sum(min(a[j]for a,c in f)for f in factors)for j in range(4))
                hi=tuple(degree[j]+sum(max(a[j]for a,c in f)for f in factors)for j in range(4))
                lower=lo if lower is None else tuple(min(lower[j],lo[j])for j in range(4))
                upper=hi if upper is None else tuple(max(upper[j],hi[j])for j in range(4))
        return None if lower is None else(lower,upper)


class StandardProgram:
    """Execute B=R(Kcov Pi + A h S Pi) F coefficient requests."""
    def __init__(self,pi_coefficients):
        I.require_synthetic(pi_coefficients.mode);self.pi=pi_coefficients;self.pair=scalar_pair(getattr(pi_coefficients,'pair',PAIR));self.twist=line_twist(self.pair);self.calls=[];self.cache={}
    def _read(self,s,e,target,branch,coefficient):
        need(self.pi.require_extension(s),'standard-target extension absent')
        self.calls.append({'standard_simplex':tuple(s),'exponent':e,'target_standard_tags':tuple(target),
            'branch':branch,'coefficient':coefficient,'restriction':'same global finite Laurent frame'})
        need(len(self.calls)<=100000,'synthetic standard-query cap')
        return coefficient*rational(self.pi.coefficient(s,e))
    def branches(self,standard_edge,e):
        I.require_synthetic(self.pi.mode)
        e=I.exponent(e);s,orientation=normalize(standard_edge)
        need(len(standard_edge)==2,'standard edge')
        if not orientation:return{'K':Q(0),'AhS':Q(0)}
        key=(s,e)
        if key not in self.cache:
            K=sum((self._read(t,e,s,'K',z)for t,z in k_chain(s).items()),Q(0))
            A=Q(0)
            for awsign,cell in aw_cells(s):
                for hsign,input_cell,eta in h_requests(cell,e,self.twist):
                    for ssign,t in stairs(input_cell):A+=self._read(t,eta,s,'AhS',awsign*hsign*ssign)
            self.cache[key]={'K':K,'AhS':A}
        return {branch:orientation*v for branch,v in self.cache[key].items()}
    def coefficient(self,owners,e,derivative_direction=None):
        need(len(owners)==2 and all(isinstance(v,I.FullOwner)for v in owners),'full output edge owners')
        need(len({(v.seed,v.occurrence)for v in owners})==2,'output occurrence merged')
        e=I.exponent(e);factor=1
        if derivative_direction is not None:
            d=derivative_direction;need(type(d)is int and 0<=d<4 and d not in self.pair,'only complementary scalar derivatives')
            factor=e[d]+1
            if not factor:return Q(0)
            e=tuple(x+(j==d)for j,x in enumerate(e)) # BEFORE all h predicates
        out=self.branches(tuple(v.standard_tag for v in owners),e)
        return factor*(out['K']+out['AhS'])
    def harmonic_projection(self):
        I.require_synthetic(self.pi.mode)
        cell=tuple('C'if i in self.pair else'B'for i in range(4));e=tuple(-1 if i in self.pair else 0 for i in range(4))
        return sum((z*rational(self.pi.coefficient(s,e))for z,s in stairs(cell)),Q(0))
    def harmonic_image(self,standard_triple,e):
        e=I.exponent(e)
        if e!=tuple(-1 if i in self.pair else 0 for i in range(4)):return Q(0)
        return self.harmonic_projection()*sum(z for z,c in aw_cells(standard_triple)if all(c[i]=='C'if i in self.pair else c[i]in('A','B')for i in range(4)))
    def contract(self):
        return {'program':'R(K_cov Pi + A h S Pi)F','pair':list(self.pair),'homotopy_identity':'delta B+B delta=1-A I P S on the standard complex',
            'harmonic_H2_dimension':1,'source_harmonic_vanishing_witness':False,'actual_first_order_primitive_witness':False,
            'physical_source_evaluated':False,'execution_release':False}


class StandardEdgeOracle:
    """B endpoint for INS whole numerator; does NOT multiply C_a C_b Z."""
    mode='synthetic'
    def __init__(self,program):self.program=program
    def coefficient(self,owners,e,pair=None):
        pair=self.program.pair if pair is None else scalar_pair(pair)
        need(pair==self.program.pair,'scalar source pair changed')
        return self.program.coefficient(owners,e)
    def support_box(self,owners,pair=None):
        pair=self.program.pair if pair is None else scalar_pair(pair)
        need(pair==self.program.pair,'scalar source pair changed')
        need(len(owners)==2 and all(isinstance(o,I.FullOwner)for o in owners),'output edge')
        need(hasattr(self.program.pi,'support_box'),'Pi support enclosure adapter is uninstantiated')
        return self.program.pi.support_box() # K/A/h/S preserve global finite exponents
    def bind(self,owners):return BoundStandardEdge(self,tuple(owners))

class BoundStandardEdge:
    mode='synthetic'
    def __init__(self,oracle,owners):
        need(len(owners)==2 and all(isinstance(o,I.FullOwner)for o in owners),'complete output owners')
        self.oracle=oracle;self.owners=owners
    def coefficient(self,e):return self.oracle.coefficient(self.owners,e)
    def support_box(self):return self.oracle.support_box(self.owners)
